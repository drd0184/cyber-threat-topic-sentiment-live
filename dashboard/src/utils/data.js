import { cleanQualityNote, isNoisyTopic } from "./formatters.js";

export const TOPIC_LABELS = {
  0: "Generic Vulnerability Signals",
  1: "Data Leak / Botnet / Cloud",
  2: "DDoS / Attack Protection",
  3: "CVE / Remote Exploit / Buffer Overflow",
  4: "Ransomware / Malware / Attacks",
  5: "SQL Injection / DoS / Microsoft",
  6: "Ransomware / Business Risk / WannaCry",
  7: "Zero-day / Browser Exploit Signals",
  8: "CVE / Patch / RSA BSAFE",
  9: "Cybersecurity / IoT / Botnet",
};

const EMPTY_SUMMARY = {
  total_posts: 0,
  total_topics: 0,
  total_time_windows: 0,
  average_sentiment: 0,
  cybercon_level: 5,
  high_quality_topics_count: 0,
  medium_quality_topics_count: 0,
  low_quality_topics_count: 0,
  most_reliable_topics: [],
  noisy_topics: [],
  hottest_negative: null,
  hottest_positive: null,
};

function topicIdOf(row) {
  return Number(row?.dominant_topic ?? row?.topic_id);
}

function withOfficialTopic(row) {
  if (!row) return row;
  const topicId = topicIdOf(row);
  const qualityScore = row.quality_score ?? row.topic_quality?.quality_score;
  const topicQuality = row.topic_quality
    ? {
        ...row.topic_quality,
        quality_note: cleanQualityNote(row.topic_quality.quality_score, row.topic_quality.quality_note),
      }
    : row.topic_quality;

  const enriched = {
    ...row,
    topic_label_raw: row.topic_label,
    topic_label: TOPIC_LABELS[topicId] || row.topic_label || `Topic ${topicId}`,
    topic_quality: topicQuality,
    quality_note: cleanQualityNote(qualityScore, row.quality_note),
  };

  return {
    ...enriched,
    is_noisy: isNoisyTopic(enriched),
  };
}

function buildDashboardData(raw = {}) {
  const p2 = raw.p2 || [];
  const posts = raw.posts || [];
  const summary = { ...EMPTY_SUMMARY, ...(raw.summary || {}) };
  const topics = raw.topics || [];
  const topicQuality = raw.topicQuality || raw.topic_quality || [];
  const hotTopicsQuality = raw.hotTopicsQuality || raw.hot_topics_quality || [];
  const validation = raw.validation || [];

  const hotQualityMap = new Map(
    hotTopicsQuality.map((row) => {
      const enriched = withOfficialTopic(row);
      return [`${row.time_window}-${row.dominant_topic}`, enriched];
    })
  );

  const enrichedP2 = p2.map((row) => {
    const enriched = withOfficialTopic(row);
    return {
      ...enriched,
      hot_quality: hotQualityMap.get(`${row.time_window}-${row.dominant_topic}`) || null,
    };
  });

  const enrichedPosts = posts.map(withOfficialTopic);
  const enrichedTopics = topics.map(withOfficialTopic);
  const enrichedTopicQuality = topicQuality.map(withOfficialTopic);
  const enrichedValidation = validation.map(withOfficialTopic);
  const enrichedSummary = {
    ...summary,
    hottest_negative: withOfficialTopic(summary.hottest_negative),
    hottest_positive: withOfficialTopic(summary.hottest_positive),
  };

  const p2ByTopic = new Map();
  for (const row of enrichedP2) {
    if (!p2ByTopic.has(row.dominant_topic)) p2ByTopic.set(row.dominant_topic, []);
    p2ByTopic.get(row.dominant_topic).push(row);
  }

  const postsByTopic = new Map();
  const postsByAlert = new Map();
  for (const post of enrichedPosts) {
    if (!postsByTopic.has(post.dominant_topic)) postsByTopic.set(post.dominant_topic, []);
    postsByTopic.get(post.dominant_topic).push(post);
    const key = `${post.time_window}-${post.dominant_topic}`;
    if (!postsByAlert.has(key)) postsByAlert.set(key, []);
    postsByAlert.get(key).push(post);
  }

  const topTopicIds = [...enrichedP2]
    .sort((a, b) => b.p2_abs - a.p2_abs)
    .filter((row, index, rows) => rows.findIndex((item) => item.dominant_topic === row.dominant_topic) === index)
    .slice(0, 5)
    .map((row) => row.dominant_topic);

  return {
    summary: enrichedSummary,
    p2: enrichedP2,
    posts: enrichedPosts,
    topics: enrichedTopics,
    topicQuality: enrichedTopicQuality,
    hotTopicsQuality: hotTopicsQuality.map(withOfficialTopic),
    validation: enrichedValidation,
    p2ByTopic,
    postsByTopic,
    postsByAlert,
    topTopicIds,
    hasLiveData: enrichedP2.length > 0 || enrichedPosts.length > 0,
    dataMode: "live-pending",
    dataSource: "data/live/processed exports",
  };
}

export const dashboardData = buildDashboardData();
