import { useMemo, useState } from "react";
import { FileSearch } from "lucide-react";
import { cleanQualityNote, directionLabel, formatDate, formatNumber, formatP2, isNoisyTopic } from "../utils/formatters.js";
import { EmptyState, MetricCard, Panel, QualityBadge, SearchInput, SectionHeader, SeverityBadge, SignalBadge } from "./ui.jsx";
import { SentimentDistributionChart, TopicAreaChart, TopicBarChart, TopicLineChart } from "./charts.jsx";

export function TopicDetailPanel({ topic, p2Rows = [], posts = [], alerts = [], onInspectAlert }) {
  const [sentiment, setSentiment] = useState("all");
  const [query, setQuery] = useState("");

  const filteredPosts = useMemo(() => {
    const q = query.trim().toLowerCase();
    return posts
      .filter((post) => sentiment === "all" || post.sentiment_class === sentiment)
      .filter((post) => !q || post.text_raw.toLowerCase().includes(q))
      .slice(0, 150);
  }, [posts, sentiment, query]);

  if (!topic) {
    return (
      <Panel className="p-5">
        <EmptyState title="Seleziona un topic per visualizzare il dettaglio." body="Usa Apri dettaglio su una card Topic per caricare timeline, post e alert collegati." />
      </Panel>
    );
  }

  const noisy = isNoisyTopic(topic);
  const qualityNote = cleanQualityNote(topic.quality_score, topic.quality_note);

  return (
    <Panel className="p-5">
      <SectionHeader
        eyebrow="Dettaglio Topic"
        title={`Topic ${topic.topic_id} — ${topic.topic_label}`}
        description={qualityNote}
        icon={FileSearch}
        action={
          <div className="flex flex-wrap gap-2">
            <QualityBadge score={topic.quality_score} />
            {noisy ? <SignalBadge tone="warning">NOISY SIGNAL</SignalBadge> : null}
          </div>
        }
      />

      <div className="mb-5 flex flex-wrap gap-2">
        {(topic.top_words || []).map((word) => (
          <SignalBadge key={word} tone="muted">{word}</SignalBadge>
        ))}
      </div>

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-6">
        <MetricCard label="Documents" value={formatNumber(topic.total_docs)} />
        <MetricCard label="Total volume" value={formatNumber(topic.total_volume)} />
        <MetricCard label="Max negative P2" value={formatP2(topic.max_negative_p2, 2)} tone="negative" />
        <MetricCard label="Average sentiment" value={formatP2(topic.avg_sentiment, 3)} />
        <MetricCard label="Threat %" value={`${formatNumber(topic.threat_pct, 1)}%`} tone="negative" />
        <MetricCard label="Irrelevant %" value={`${formatNumber(topic.irrelevant_pct, 1)}%`} />
      </div>

      <div className="mt-6 grid gap-4 xl:grid-cols-[minmax(0,0.95fr)_minmax(0,1.05fr)]">
        <div className="h-80 rounded-lg border border-slate-800 bg-slate-950/35 p-4">
          <div className="mb-3">
            <h3 className="text-sm font-semibold text-slate-300">Distribuzione sentiment</h3>
            <p className="mt-1 text-xs leading-5 text-slate-500">Ripartizione dei messaggi assegnati a questo Topic.</p>
          </div>
          <div className="h-[250px]">
            <SentimentDistributionChart posts={posts} />
          </div>
        </div>
        <div className="rounded-lg border border-slate-800 bg-slate-950/35 p-4">
          <h3 className="mb-3 text-sm font-semibold text-slate-300">Alert relativi a questo Topic</h3>
          <div className="space-y-3">
            {alerts.slice(0, 8).map((alert) => (
              <TopicAlertCard key={`${alert.time_window}-${alert.dominant_topic}`} alert={alert} onInspectAlert={onInspectAlert} />
            ))}
          </div>
          {alerts.length > 8 ? <p className="mt-3 text-xs text-slate-500">Mostrati i primi 8 alert per intensità.</p> : null}
        </div>
      </div>

      <div className="mt-6 grid gap-4 xl:grid-cols-3">
        <ChartBox title="P2 timeline topic"><TopicLineChart rows={p2Rows} dataKey="p2_index" color="#22D3EE" /></ChartBox>
        <ChartBox title="Volume timeline topic"><TopicBarChart rows={p2Rows} dataKey="topic_volume" color="#3B82F6" /></ChartBox>
        <ChartBox title="Sentiment timeline topic"><TopicAreaChart rows={p2Rows} dataKey="topic_sentiment_sum" color="#22C55E" /></ChartBox>
      </div>

      <div className="mt-6">
        <div className="rounded-lg border border-slate-800 bg-slate-950/35 p-4">
          <div className="mb-3 flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
            <h3 className="text-sm font-semibold text-slate-300">Post associati al Topic</h3>
            <div className="flex gap-2">
              <SearchInput value={query} onChange={setQuery} placeholder="Cerca nei post" />
              <select value={sentiment} onChange={(event) => setSentiment(event.target.value)} className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100">
                <option value="all">Tutti</option>
                <option value="negative">Negativi</option>
                <option value="positive">Positivi</option>
                <option value="neutral">Neutri</option>
              </select>
            </div>
          </div>
          <PostsTable posts={filteredPosts} />
        </div>
      </div>
    </Panel>
  );
}

function TopicAlertCard({ alert, onInspectAlert }) {
  const direction = alert.p2_direction || "neutral";
  const tone = direction === "negative" ? "negative" : direction === "positive" ? "positive" : "muted";
  const accent = direction === "negative" ? "border-red-400/35 bg-red-500/10" : direction === "positive" ? "border-emerald-400/35 bg-emerald-500/10" : "border-slate-700 bg-slate-900/35";
  return (
    <article className={`rounded-lg border p-3 ${accent}`}>
      <div className="flex items-start justify-between gap-3">
        <span className="font-mono text-xs text-slate-400">{formatDate(alert.time_window)}</span>
        <div className="flex flex-wrap justify-end gap-2">
          <SeverityBadge p2Abs={alert.p2_abs} />
          <SignalBadge tone={tone}>{directionLabel(direction).toUpperCase()}</SignalBadge>
        </div>
      </div>
      <div className="mt-3 grid gap-2 sm:grid-cols-4">
        <AlertMetric label="P2" value={formatP2(alert.p2_index, 2)} tone={direction === "negative" ? "text-red-100" : direction === "positive" ? "text-emerald-100" : "text-slate-100"} large />
        <AlertMetric label="Volume" value={formatNumber(alert.topic_volume)} />
        <AlertMetric label="Sentiment" value={formatP2(alert.topic_sentiment_sum, 2)} />
        <AlertMetric label="P2 abs" value={formatNumber(alert.p2_abs, 2)} />
      </div>
      <div className="mt-3 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <p className="text-sm leading-5 text-slate-400">
          Segnale {directionLabel(direction)} rilevato per questo Topic nella finestra temporale.
        </p>
        {onInspectAlert ? (
          <button type="button" onClick={() => onInspectAlert(alert)} className="shrink-0 rounded border border-cyan-300/35 bg-cyan-400/10 px-3 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-400/15">
            Apri alert
          </button>
        ) : null}
      </div>
    </article>
  );
}

function AlertMetric({ label, value, tone = "text-slate-100", large = false }) {
  return (
    <div>
      <span className="block text-[10px] uppercase tracking-[0.12em] text-slate-500">{label}</span>
      <strong className={`mt-1 block font-mono ${large ? "text-xl" : "text-sm"} ${tone}`}>{value}</strong>
    </div>
  );
}

function ChartBox({ title, children }) {
  return (
    <div className="h-72 rounded-lg border border-slate-800 bg-slate-950/35 p-4">
      <h3 className="mb-3 text-sm font-semibold text-slate-400">{title}</h3>
      {children}
    </div>
  );
}

export function PostsTable({ posts }) {
  if (!posts.length) return <EmptyState title="Nessun post trovato" body="Prova con un filtro sentiment o una ricerca diversa." />;
  return (
    <div className="thin-scrollbar max-h-[520px] overflow-y-auto">
      <table className="w-full border-collapse text-left text-sm">
        <thead className="sticky top-0 bg-slate-950 text-xs uppercase tracking-[0.12em] text-slate-500">
          <tr>
            <th className="border-b border-slate-800 py-2 pr-3">Tempo</th>
            <th className="border-b border-slate-800 py-2 pr-3">Sentiment</th>
            <th className="border-b border-slate-800 py-2 pr-3">Testo</th>
          </tr>
        </thead>
        <tbody>
          {posts.map((post) => (
            <tr key={post.id} className="align-top text-slate-300">
              <td className="border-b border-slate-900 py-3 pr-3 font-mono text-xs text-slate-500">{formatDate(post.created_at)}</td>
              <td className="border-b border-slate-900 py-3 pr-3">
                <span className="font-mono text-xs text-slate-200">{post.sentiment_class}</span>
                <div className="font-mono text-xs text-slate-500">{formatP2(post.vader_compound, 3)}</div>
              </td>
              <td className="border-b border-slate-900 py-3 pr-3 leading-6">{post.text_raw}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
