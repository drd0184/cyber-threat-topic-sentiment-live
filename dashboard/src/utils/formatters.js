export const CYBERCON_SCALE = [
  { level: 1, state: "CRITICAL", description: "Critical semantic momentum", threshold: "p2_abs >= 30", homeDescription: "Critical: segnale molto forte, attenzione immediata." },
  { level: 2, state: "HIGH", description: "High semantic momentum", threshold: "p2_abs >= 15", homeDescription: "High: segnale rilevante, analisi prioritaria." },
  { level: 3, state: "ELEVATED", description: "Elevated signal", threshold: "p2_abs >= 8", homeDescription: "Elevated: segnale significativo, da monitorare." },
  { level: 4, state: "WATCH", description: "Monitoring", threshold: "p2_abs >= 3", homeDescription: "Monitoring: segnale contenuto ma attivo." },
  { level: 5, state: "NOMINAL", description: "Nominal", threshold: "p2_abs < 3", homeDescription: "Nominal: segnale debole o stabile." },
];

export const QUALITY_NOTES = {
  high: "Topic coerente e ben interpretabile.",
  medium: "Topic interpretabile, con segnali parzialmente misti.",
  low: "Topic ampio o rumoroso. Incluso nel P2, ma da interpretare con cautela.",
};

export function formatNumber(value, digits = 0) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "n/a";
  return Number(value).toLocaleString("it-IT", {
    maximumFractionDigits: digits,
    minimumFractionDigits: digits,
  });
}

export function formatP2(value, digits = 2) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "n/a";
  return `${Number(value) > 0 ? "+" : ""}${formatNumber(value, digits)}`;
}

export function formatDate(value, compact = false) {
  if (!value) return "n/a";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("it-IT", {
    year: compact ? undefined : "numeric",
    month: compact ? "short" : "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }).format(date);
}

export function getCyberconLevel(p2Abs) {
  if (p2Abs >= 30) return 1;
  if (p2Abs >= 15) return 2;
  if (p2Abs >= 8) return 3;
  if (p2Abs >= 3) return 4;
  return 5;
}

export function getCyberconState(level) {
  return CYBERCON_SCALE.find((item) => item.level === Number(level))?.state || "NOMINAL";
}

export function getSeverity(p2Abs) {
  if (p2Abs >= 30) return "critical";
  if (p2Abs >= 15) return "high";
  if (p2Abs >= 8) return "elevated";
  if (p2Abs >= 3) return "watch";
  return "low";
}

export function severityLabel(severity) {
  return {
    critical: "CRITICAL",
    high: "HIGH",
    elevated: "ELEVATED",
    watch: "WATCH",
    low: "LOW",
    nominal: "NOMINAL",
  }[severity] || "LOW";
}

export function directionLabel(direction) {
  return {
    negative: "negativo",
    positive: "positivo",
    neutral: "neutro",
  }[direction] || "neutro";
}

export function getDirectionColor(direction) {
  if (direction === "negative") return "text-red-200 border-red-400/40 bg-red-500/10";
  if (direction === "positive") return "text-emerald-200 border-emerald-400/40 bg-emerald-500/10";
  return "text-cyan-100 border-cyan-400/30 bg-cyan-500/10";
}

export function getQualityColor(score) {
  if (score === "high") return "text-emerald-100 border-emerald-400/40 bg-emerald-500/10";
  if (score === "medium") return "text-amber-100 border-amber-400/40 bg-amber-500/10";
  if (score === "low") return "text-red-100 border-red-400/40 bg-red-500/10";
  return "text-slate-200 border-slate-500/50 bg-slate-500/10";
}

export function qualityLabel(score) {
  if (score === "high") return "HIGH CONFIDENCE";
  if (score === "medium") return "MEDIUM CONFIDENCE";
  if (score === "low") return "LOW CONFIDENCE";
  return "CONFIDENCE N/A";
}

export function qualityShortLabel(score) {
  if (score === "high") return "HIGH";
  if (score === "medium") return "MEDIUM";
  if (score === "low") return "LOW";
  return "N/A";
}

export function cleanQualityNote(score, note) {
  return note || QUALITY_NOTES[score] || "Confidenza del Topic non disponibile.";
}

export function isNoisyTopic(topic) {
  const topicId = Number(topic?.topic_id ?? topic?.dominant_topic);
  return topicId === 7 || topic?.quality_score === "low" || topic?.topic_confidence === "low" || topic?.topic_quality?.quality_score === "low";
}

export function severityColor(severity) {
  if (severity === "critical") return "text-red-100 border-red-400/50 bg-red-500/15";
  if (severity === "high") return "text-orange-100 border-orange-400/40 bg-orange-500/10";
  if (severity === "elevated") return "text-amber-100 border-amber-400/40 bg-amber-500/10";
  if (severity === "watch") return "text-cyan-100 border-cyan-400/30 bg-cyan-500/10";
  if (severity === "low") return "text-slate-200 border-slate-500/40 bg-slate-500/10";
  return "text-slate-200 border-slate-500/40 bg-slate-500/10";
}

export function topicKey(topicId) {
  return `T${topicId}`;
}
