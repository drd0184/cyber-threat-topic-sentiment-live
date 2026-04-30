import { ExternalLink } from "lucide-react";
import { formatNumber, formatP2, isNoisyTopic } from "../utils/formatters.js";
import { QualityBadge, SignalBadge } from "./ui.jsx";

export function TopicCard({ topic, onOpen }) {
  const noisy = isNoisyTopic(topic);
  const totalSentiment = Object.values(topic.sentiment_distribution || {}).reduce((sum, value) => sum + Number(value || 0), 0);
  const sentimentPct = (key) => (totalSentiment ? ((topic.sentiment_distribution?.[key] || 0) / totalSentiment) * 100 : 0);
  return (
    <article className="rounded-lg border border-slate-800 bg-slate-950/45 p-4 transition hover:border-cyan-300/35">
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <div className="font-mono text-xs font-bold uppercase tracking-[0.16em] text-cyan-300">Topic ID {topic.topic_id}</div>
          <h3 className="mt-2 text-lg font-semibold leading-6 text-slate-50">{topic.topic_label}</h3>
        </div>
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        <QualityBadge score={topic.topic_confidence || topic.quality_score} />
        {noisy ? <SignalBadge tone="warning">LOW CONFIDENCE</SignalBadge> : null}
      </div>
      {topic.note ? <p className="mt-3 text-sm leading-6 text-slate-400">{topic.note}</p> : null}

      <div className="mt-4 flex flex-wrap gap-2">
        {(topic.top_5_words || []).map((word) => (
          <SignalBadge key={word} tone="muted">{word}</SignalBadge>
        ))}
      </div>

      <div className="mt-4 grid grid-cols-2 gap-2 text-sm">
        <Stat label="Documents" value={formatNumber(topic.docs_assigned ?? topic.total_docs)} />
        <Stat label="Total volume" value={formatNumber(topic.total_volume)} />
        <Stat label="Max |P2|" value={formatP2(topic.max_abs_p2, 2)} tone="text-cyan-100" />
        <Stat label="Max negative P2" value={formatP2(topic.max_negative_p2, 2)} tone="text-red-200" />
        <Stat label="Max positive P2" value={formatP2(topic.max_positive_p2, 2)} tone="text-emerald-200" />
        <Stat label="Average sentiment" value={formatP2(topic.avg_sentiment, 3)} />
      </div>

      <div className="mt-4">
        <div className="mb-2 flex items-center justify-between text-xs text-slate-500">
          <span>Sentiment</span>
          <span>{formatNumber(totalSentiment)} docs</span>
        </div>
        <div className="h-2 overflow-hidden rounded-full bg-slate-800">
          <div className="inline-block h-full bg-red-400" style={{ width: `${sentimentPct("negative")}%` }} />
          <div className="inline-block h-full bg-slate-500" style={{ width: `${sentimentPct("neutral")}%` }} />
          <div className="inline-block h-full bg-emerald-400" style={{ width: `${sentimentPct("positive")}%` }} />
        </div>
      </div>

      <div className="mt-4 grid gap-2">
        {Object.entries(topic.source_type_distribution || {}).slice(0, 3).map(([source, count]) => (
          <div key={source} className="flex items-center justify-between rounded border border-slate-800 bg-slate-900/35 px-2 py-1 text-xs">
            <span className="text-slate-400">{source}</span>
            <span className="font-mono text-slate-200">{formatNumber(count)}</span>
          </div>
        ))}
      </div>

      <button type="button" onClick={() => onOpen(topic.topic_id)} className="mt-4 inline-flex w-full items-center justify-center gap-2 rounded border border-cyan-300/35 bg-cyan-400/10 px-3 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-400/15">
        Apri dettaglio
        <ExternalLink className="h-4 w-4" />
      </button>
    </article>
  );
}

function Stat({ label, value, tone = "text-slate-100" }) {
  return (
    <div className="rounded border border-slate-800 bg-slate-900/40 p-2">
      <span className="block text-xs text-slate-500">{label}</span>
      <strong className={`break-words font-mono text-sm ${tone}`}>{value}</strong>
    </div>
  );
}
