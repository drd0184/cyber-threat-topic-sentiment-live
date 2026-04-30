import { Search } from "lucide-react";
import { directionLabel, getDirectionColor, getQualityColor, getSeverity, qualityLabel, severityColor, severityLabel } from "../utils/formatters.js";

export function Panel({ children, className = "" }) {
  return <section className={`intel-panel ${className}`}>{children}</section>;
}

export function SectionHeader({ eyebrow, title, description, icon: Icon, action }) {
  return (
    <div className="mb-5 flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
      <div>
        <div className="mb-2 flex items-center gap-2 font-mono text-xs font-bold uppercase tracking-[0.18em] text-cyan-300">
          {Icon ? <Icon className="h-4 w-4" /> : null}
          {eyebrow}
        </div>
        <h2 className="text-2xl font-semibold tracking-[0.01em] text-slate-50">{title}</h2>
        {description ? <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">{description}</p> : null}
      </div>
      {action}
    </div>
  );
}

export function MetricCard({ label, value, icon: Icon, tone = "neutral" }) {
  const toneClass = tone === "negative" ? "text-red-200" : tone === "positive" ? "text-emerald-200" : "text-cyan-100";
  return (
    <div className="min-h-[112px] rounded-lg border border-slate-800 bg-slate-950/45 p-4 shadow-sm">
      <div className="flex items-center justify-between gap-3">
        <span className="font-mono text-xs font-bold uppercase tracking-[0.14em] text-slate-500">{label}</span>
        {Icon ? <Icon className="h-4 w-4 text-cyan-300" /> : null}
      </div>
      <strong className={`mt-3 block font-mono text-2xl font-semibold ${toneClass}`}>{value}</strong>
    </div>
  );
}

export function QualityBadge({ score }) {
  return <span className={`confidence-badge ${getQualityColor(score)}`}>{qualityLabel(score)}</span>;
}

export function SignalBadge({ children, tone = "neutral" }) {
  const classes = {
    negative: "border-red-400/40 bg-red-500/10 text-red-100",
    positive: "border-emerald-400/40 bg-emerald-500/10 text-emerald-100",
    warning: "border-amber-400/40 bg-amber-500/10 text-amber-100",
    neutral: "border-cyan-400/30 bg-cyan-500/10 text-cyan-100",
    muted: "border-slate-600/50 bg-slate-600/10 text-slate-300",
  }[tone];
  return <span className={`rounded border px-2 py-1 font-mono text-[10px] font-bold uppercase tracking-[0.08em] ${classes}`}>{children}</span>;
}

export function SeverityBadge({ p2Abs }) {
  const severity = getSeverity(p2Abs);
  return <span className={`rounded border px-2 py-1 font-mono text-[10px] font-bold uppercase ${severityColor(severity)}`}>{severityLabel(severity)}</span>;
}

export function DirectionBadge({ direction }) {
  return <span className={`rounded border px-2 py-1 font-mono text-[10px] font-bold uppercase ${getDirectionColor(direction)}`}>{directionLabel(direction)}</span>;
}

export function SearchInput({ value, onChange, placeholder = "Cerca" }) {
  return (
    <label className="relative block">
      <Search className="pointer-events-none absolute left-3 top-2.5 h-4 w-4 text-slate-500" />
      <input
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder={placeholder}
        className="w-full rounded-lg border border-slate-700 bg-slate-950/75 py-2 pl-9 pr-3 text-sm text-slate-100 outline-none transition placeholder:text-slate-600 focus:border-cyan-300/60"
      />
    </label>
  );
}

export function EmptyState({ title = "Nessun segnale", body = "Modifica i filtri per visualizzare più risultati." }) {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-950/40 p-8 text-center">
      <div className="text-sm font-semibold text-slate-200">{title}</div>
      <p className="mt-2 text-sm text-slate-500">{body}</p>
    </div>
  );
}
