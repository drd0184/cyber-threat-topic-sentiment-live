import liveSummary from "../data/live_summary.json";
import liveP2 from "../data/live_p2.json";
import liveTopics from "../data/live_topics.json";
import livePosts from "../data/live_posts.json";
import liveAlerts from "../data/live_alerts.json";
import liveMetadata from "../data/live_metadata.json";
import { cleanQualityNote, isNoisyTopic } from "./formatters.js";

export const TOPIC_LABELS = {
  0: "Network Attacks / Device Access",
  1: "Command Execution / Payload Delivery",
  2: "Cybercrime / Fraud / Law Enforcement",
  3: "Memory Exploitation / Buffer & Heap Bugs",
  4: "Access Control / Process & API Abuse",
  5: "Exploit Tooling / Metasploit / RCE",
  6: "Security Risk / Exposure Management",
  7: "Cybersecurity Tools / Generic Discussion",
  8: "Microsoft / Privilege Escalation / Patch Exploitation",
  9: "Ransomware / Malware / Email Campaigns",
};

const EMPTY_SUMMARY = {
  total_documents: 0,
  total_posts: 0,
  total_topics: 0,
  total_time_windows: 0,
  average_vader_compound: 0,
  average_sentiment: 0,
  cybercon_level: 5,
  cybercon_label: "NOMINAL",
  cybercon_warning: null,
  hottest_negative_alert: null,
  hottest_positive_alert: null,
  hottest_negative: null,
  hottest_positive: null,
  source_type_distribution: {},
  topic_confidence_distribution: {},
  severity_distribution: {},
};

function topicIdOf(row) {
  return Number(row?.dominant_topic ?? row?.topic_id);
}

function withOfficialTopic(row, topicMap = new Map()) {
  if (!row) return row;
  const topicId = topicIdOf(row);
  const topic = topicMap.get(topicId);
  const topicConfidence = row.topic_confidence || row.quality_score || topic?.topic_confidence || topic?.quality_score || "none";
  const topicQuality = {
    quality_score: topicConfidence,
    quality_note: cleanQualityNote(topicConfidence, row.note || topic?.note),
  };
  const topWords = row.top_words || topic?.top_words || [];
  const enriched = {
    ...row,
    dominant_topic: Number.isFinite(topicId) ? topicId : row.dominant_topic,
    topic_id: row.topic_id ?? (Number.isFinite(topicId) ? topicId : undefined),
    topic_label: TOPIC_LABELS[topicId] || row.topic_label || `Topic ${topicId}`,
    topic_confidence: topicConfidence,
    quality_score: topicConfidence,
    topic_quality: topicQuality,
    top_words: topWords,
    top_5_words: row.top_5_words || topWords.slice(0, 5),
    warning:
      row.warning ||
      (topicConfidence === "low" ? "Low-confidence topic. Interpretare il segnale con cautela." : null),
    is_low_confidence: topicConfidence === "low",
  };

  return {
    ...enriched,
    is_noisy: isNoisyTopic(enriched),
  };
}

function buildDashboardData() {
  const summary = { ...EMPTY_SUMMARY, ...liveSummary };
  const rawTopics = liveTopics || [];
  const topicMap = new Map(rawTopics.map((topic) => [Number(topic.topic_id), topic]));

  const topics = rawTopics.map((topic) => withOfficialTopic(topic, topicMap));
  const p2 = (liveP2 || []).map((row) => withOfficialTopic(row, topicMap));
  const alerts = (liveAlerts || []).map((row) => {
    const enriched = withOfficialTopic(
      {
        ...row,
        p2_direction: row.direction || row.p2_direction,
        negative_count: row.sentiment_counts?.negative ?? row.negative_count,
        neutral_count: row.sentiment_counts?.neutral ?? row.neutral_count,
        positive_count: row.sentiment_counts?.positive ?? row.positive_count,
        reddit_count: row.source_counts?.reddit_rss ?? row.reddit_count,
        news_count: (row.source_counts?.news_rss ?? 0) + (row.source_counts?.news_api ?? 0),
        news_api_count: row.source_counts?.news_api ?? row.news_api_count,
      },
      topicMap
    );
    return enriched;
  });
  const posts = (livePosts || []).map((row) => withOfficialTopic(row, topicMap));

  const alertByKey = new Map(alerts.map((alert) => [`${alert.time_window}-${alert.dominant_topic}`, alert]));
  const p2WithAlert = p2.map((row) => ({
    ...row,
    alert: alertByKey.get(`${row.time_window}-${row.dominant_topic}`) || null,
  }));

  const p2ByTopic = new Map();
  for (const row of p2WithAlert) {
    if (!p2ByTopic.has(row.dominant_topic)) p2ByTopic.set(row.dominant_topic, []);
    p2ByTopic.get(row.dominant_topic).push(row);
  }

  const postsByTopic = new Map();
  const postsByAlert = new Map();
  for (const post of posts) {
    if (!postsByTopic.has(post.dominant_topic)) postsByTopic.set(post.dominant_topic, []);
    postsByTopic.get(post.dominant_topic).push(post);
    const key = `${post.time_window}-${post.dominant_topic}`;
    if (!postsByAlert.has(key)) postsByAlert.set(key, []);
    postsByAlert.get(key).push(post);
  }

  const topTopicIds = [...p2WithAlert]
    .sort((a, b) => b.p2_abs - a.p2_abs)
    .filter((row, index, rows) => rows.findIndex((item) => item.dominant_topic === row.dominant_topic) === index)
    .slice(0, 5)
    .map((row) => row.dominant_topic);

  const enrichedSummary = {
    ...summary,
    hottest_negative: withOfficialTopic(summary.hottest_negative_alert || summary.hottest_negative, topicMap),
    hottest_positive: withOfficialTopic(summary.hottest_positive_alert || summary.hottest_positive, topicMap),
  };

  return {
    summary: enrichedSummary,
    metadata: liveMetadata || {},
    p2: p2WithAlert,
    alerts,
    posts,
    topics,
    topicQuality: topics,
    hotTopicsQuality: [],
    validation: [],
    p2ByTopic,
    postsByTopic,
    postsByAlert,
    topTopicIds,
    hasLiveData: p2WithAlert.length > 0 || posts.length > 0,
    dataMode: "live",
    dataSource: "dashboard/src/data/live_*.json",
  };
}

export const dashboardData = buildDashboardData();
