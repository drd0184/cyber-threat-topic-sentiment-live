import { Clock, ExternalLink } from "lucide-react";
import { formatDate, formatNumber, formatP2, qualityShortLabel } from "../utils/formatters.js";
import { QualityBadge, SeverityBadge, SignalBadge } from "./ui.jsx";

export function AlertCard({ alert, onInspect, compact = false }) {
  const quality = alert.topic_quality || alert.hot_quality;
  return (
    <article className="rounded-lg border border-slate-800 bg-slate-950/45 p-4 transition hover:border-cyan-300/35">
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div className="min-w-0">
          <div className="flex flex-wrap gap-2">
            <SeverityBadge p2Abs={alert.p2_abs} />
            <QualityBadge score={quality?.quality_score} />
          </div>
          <h3 className="mt-3 text-lg font-semibold text-slate-50">{alert.topic_label}</h3>
          <p className="mt-1 flex items-center gap-2 font-mono text-xs text-slate-500">
            <Clock className="h-3.5 w-3.5" />
            {formatDate(alert.time_window)}
          </p>
        </div>
        <div className="shrink-0 text-left md:text-right">
          <div className="font-mono text-2xl font-semibold text-red-100">{formatP2(alert.p2_index, 2)}</div>
          <div className="font-mono text-xs text-slate-500">P2 abs {formatNumber(alert.p2_abs, 2)}</div>
        </div>
      </div>

      <div className="mt-4 grid gap-2 sm:grid-cols-2 xl:grid-cols-4">
        <MiniMetric label="Volume" value={formatNumber(alert.topic_volume)} />
        <MiniMetric label="Sentiment" value={formatP2(alert.topic_sentiment_sum, 2)} />
        <MiniMetric label="Confidenza" value={qualityShortLabel(quality?.quality_score)} />
        <MiniMetric label="Threat %" value={quality?.threat_pct === undefined ? "n/a" : `${formatNumber(quality.threat_pct, 1)}%`} />
      </div>

      {!compact ? (
        <div className="mt-3 flex flex-wrap gap-2">
          {(alert.top_words || []).slice(0, 5).map((word) => (
            <SignalBadge key={word} tone="muted">{word}</SignalBadge>
          ))}
        </div>
      ) : null}

      <div className="mt-4">
        <button type="button" onClick={() => onInspect(alert)} className="inline-flex items-center gap-2 rounded border border-cyan-300/35 bg-cyan-400/10 px-3 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-400/15">
          Apri alert
          <ExternalLink className="h-4 w-4" />
        </button>
      </div>
    </article>
  );
}

function MiniMetric({ label, value }) {
  return (
    <div className="rounded border border-slate-800 bg-slate-900/35 p-2">
      <span className="block text-xs text-slate-500">{label}</span>
      <strong className="break-words font-mono text-sm text-slate-100">{value}</strong>
    </div>
  );
}
