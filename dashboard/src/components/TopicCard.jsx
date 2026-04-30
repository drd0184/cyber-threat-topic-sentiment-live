import { ExternalLink } from "lucide-react";
import { formatNumber, formatP2, isNoisyTopic } from "../utils/formatters.js";
import { QualityBadge, SignalBadge } from "./ui.jsx";

export function TopicCard({ topic, onOpen }) {
  const noisy = isNoisyTopic(topic);
  return (
    <article className="rounded-lg border border-slate-800 bg-slate-950/45 p-4 transition hover:border-cyan-300/35">
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <div className="font-mono text-xs font-bold uppercase tracking-[0.16em] text-cyan-300">Topic ID {topic.topic_id}</div>
          <h3 className="mt-2 text-lg font-semibold leading-6 text-slate-50">{topic.topic_label}</h3>
        </div>
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        <QualityBadge score={topic.quality_score} />
        {noisy ? <SignalBadge tone="warning">NOISY SIGNAL</SignalBadge> : null}
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        {(topic.top_5_words || []).map((word) => (
          <SignalBadge key={word} tone="muted">{word}</SignalBadge>
        ))}
      </div>

      <div className="mt-4 grid grid-cols-2 gap-2 text-sm">
        <Stat label="Documents" value={formatNumber(topic.total_docs)} />
        <Stat label="Total volume" value={formatNumber(topic.total_volume)} />
        <Stat label="Max negative P2" value={formatP2(topic.max_negative_p2, 2)} tone="text-red-200" />
        <Stat label="Average sentiment" value={formatP2(topic.avg_sentiment, 3)} />
        <Stat label="Threat %" value={`${formatNumber(topic.threat_pct, 1)}%`} tone="text-amber-100" />
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
