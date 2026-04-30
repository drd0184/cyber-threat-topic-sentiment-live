import { useEffect, useMemo, useState } from "react";
import { Activity, AlertTriangle, BarChart3, Clock, Database, MessageSquare, RadioTower, Tags } from "lucide-react";
import { AlertCard } from "../components/AlertCard.jsx";
import { P2TrendChart } from "../components/charts.jsx";
import { CyberconScale } from "../components/CyberconScale.jsx";
import { MetricCard, Panel, QualityBadge, SectionHeader, SignalBadge } from "../components/ui.jsx";
import { cleanQualityNote, formatDate, formatNumber, formatP2, qualityShortLabel } from "../utils/formatters.js";

const CYBERCON_TEXT =
  "CYBERCON sintetizza l'intensita del segnale P2 piu forte osservato nella pipeline live. Non rappresenta un incidente verificato.";

export function Overview({ data, openAlert, openTopic }) {
  const { summary, metadata, alerts, topics } = data;
  const cyberconDriver = alerts[0] || summary.hottest_negative;
  const topAlerts = summary.top_alerts?.length ? summary.top_alerts : alerts.slice(0, 8);
  const topTopics = useMemo(
    () => (summary.top_topics?.length ? summary.top_topics : [...topics].sort((a, b) => b.max_abs_p2 - a.max_abs_p2).slice(0, 6)),
    [summary.top_topics, topics]
  );
  const p2Trend = summary.p2_trend || [];
  const criticalHighAlerts = alerts.filter((alert) => ["critical", "high"].includes(alert.severity)).length;
  const primarySource = topEntry(summary.source_type_distribution);
  const isStale = useMemo(() => {
    const latest = new Date(metadata.latest_document_created_at || summary.latest_document_created_at);
    const generated = new Date(metadata.generated_at_utc || summary.generated_at_utc);
    if (Number.isNaN(latest.getTime()) || Number.isNaN(generated.getTime())) return false;
    return generated.getTime() - latest.getTime() > 24 * 60 * 60 * 1000;
  }, [metadata, summary]);

  if (!data.hasLiveData) {
    return (
      <div className="space-y-5">
        <HeaderBlock />
        <Panel className="p-5">
          <SectionHeader eyebrow="Pipeline live" title="Dati attesi" description="La dashboard legge solo artifact live separati dagli output statici legacy." icon={Activity} />
          <div className="grid gap-4 md:grid-cols-3">
            <MetricCard label="Record P2 live" value="0" icon={BarChart3} />
            <MetricCard label="Documenti live" value="0" icon={MessageSquare} />
            <MetricCard label="Topic live" value="0" icon={Tags} />
          </div>
        </Panel>
      </div>
    );
  }

  return (
    <div className="space-y-5">
      <HeaderBlock />
      <UpdateStatusBar metadata={metadata} summary={summary} isStale={isStale} />

      <section className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_minmax(420px,0.82fr)]">
        <PrimaryAlert alert={summary.hottest_negative || topAlerts[0]} onInspect={openAlert} />
        <CyberconCard summary={summary} driver={cyberconDriver} />
      </section>

      <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <MetricCard label="Documenti analizzati" value={formatNumber(summary.total_documents || summary.total_posts)} icon={MessageSquare} />
        <MetricCard label="Topic monitorati" value={formatNumber(summary.total_topics)} icon={Tags} />
        <MetricCard label="Finestre temporali" value={formatNumber(summary.total_time_windows)} icon={Activity} />
        <MetricCard label="Sentiment medio" value={formatP2(summary.average_vader_compound ?? summary.average_sentiment, 4)} icon={BarChart3} tone={(summary.average_vader_compound ?? summary.average_sentiment) < 0 ? "negative" : "positive"} />
        <MetricCard label="Alert critical/high" value={formatNumber(criticalHighAlerts)} icon={AlertTriangle} tone={criticalHighAlerts > 0 ? "negative" : "neutral"} />
        <MetricCard label="Fonte principale" value={primarySource ? `${primarySource.key} (${formatNumber(primarySource.value)})` : "n/a"} icon={Database} />
        <MetricCard label="Ultima raccolta" value={formatDate(metadata.latest_collected_at || summary.latest_collected_at, true)} icon={Clock} />
        <MetricCard label="Max |P2|" value={formatNumber(summary.max_abs_p2, 2)} icon={RadioTower} tone={summary.max_abs_p2 >= 15 ? "negative" : "neutral"} />
      </section>

      <Panel className="p-5">
        <SectionHeader eyebrow="Trend" title="Trend P2 nel tempo" description="Massimo |P2| per finestra temporale. Sintesi compatta, senza micro-linee per ogni finestra/topic." icon={BarChart3} />
        <div className="h-[340px]">
          <P2TrendChart trend={p2Trend} />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Alert" title="Alert principali" description="Top alert ordinati per P2 assoluto. Gli alert low-confidence restano inclusi e marcati." icon={AlertTriangle} />
        <div className="grid gap-4 lg:grid-cols-2">
          {topAlerts.map((alert) => (
            <AlertCard key={`${alert.time_window}-${alert.dominant_topic}-${alert.alert_id || ""}`} alert={alert} onInspect={openAlert} compact />
          ))}
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Topic" title="Topic piu rilevanti" description="Top 6 topic per max |P2|. Il resto e disponibile nel Topic Explorer." icon={Tags} />
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {topTopics.map((topicLike) => {
            const topic = topics.find((item) => item.topic_id === topicLike.topic_id) || topicLike;
            return <HomeTopicCard key={topic.topic_id} topic={topic} onOpen={openTopic} />;
          })}
        </div>
      </Panel>

      <section className="grid gap-5 lg:grid-cols-2">
        <SummaryPanel title="Source summary" values={summary.source_type_distribution} />
        <SummaryPanel title="Sentiment summary" values={summary.sentiment_distribution} />
      </section>
    </div>
  );
}

function HeaderBlock() {
  return (
    <Panel className="p-5 md:p-6">
      <h1 className="text-3xl font-semibold uppercase text-white md:text-5xl">CYBER THREAT HOT TOPIC INDEX</h1>
      <p className="mt-3 text-lg text-cyan-100/85">Semantic Intelligence Monitor</p>
      <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
        P2 misura il momentum semantico dei topic cyber su fonti social/news. Non conferma incidenti reali.
      </p>
    </Panel>
  );
}

function UpdateStatusBar({ metadata, summary, isStale }) {
  const [now, setNow] = useState(new Date());

  useEffect(() => {
    const timer = window.setInterval(() => setNow(new Date()), 1000);
    return () => window.clearInterval(timer);
  }, []);

  return (
    <Panel className="p-4">
      <div className="mb-3 flex items-center gap-2 font-mono text-xs font-bold uppercase tracking-[0.16em] text-cyan-300">
        <Clock className="h-4 w-4" />
        Stato aggiornamento
      </div>
      <div className="grid gap-2 sm:grid-cols-2 xl:grid-cols-6">
        <StatusItem label="Local time" value={formatDate(now.toISOString())} />
        <StatusItem label="UTC time" value={formatUtc(now.toISOString())} />
        <StatusItem label="Last pipeline export" value={formatUtc(metadata.generated_at_utc || summary.generated_at_utc)} />
        <StatusItem label="Latest collected item" value={formatDate(metadata.latest_collected_at || summary.latest_collected_at)} />
        <StatusItem label="Latest document timestamp" value={formatDate(metadata.latest_document_created_at || summary.latest_document_created_at)} />
        <StatusItem label="Schedule" value="00:00 / 12:00 UTC" />
      </div>
      {isStale ? (
        <p className="mt-3 rounded border border-amber-300/30 bg-amber-500/10 p-3 text-sm text-amber-100">
          Dataset non aggiornato nelle ultime 24h.
        </p>
      ) : null}
    </Panel>
  );
}

function StatusItem({ label, value }) {
  return (
    <div className="min-h-[70px] rounded border border-slate-800 bg-slate-950/40 p-3">
      <span className="block text-[10px] uppercase tracking-[0.12em] text-slate-500">{label}</span>
      <strong className="mt-1 block break-words font-mono text-xs text-slate-100">{value || "n/a"}</strong>
    </div>
  );
}

function PrimaryAlert({ alert, onInspect }) {
  if (!alert) return null;
  const isLow = alert.topic_confidence === "low";
  return (
    <Panel className="p-5">
      <div className="mb-4 flex flex-wrap gap-2">
        <SignalBadge tone="negative">Alert principale</SignalBadge>
        <QualityBadge score={alert.topic_confidence} />
        <SignalBadge tone="muted">{alert.severity?.toUpperCase()}</SignalBadge>
      </div>
      <h2 className="text-2xl font-semibold text-slate-50">T{alert.dominant_topic} {alert.topic_label}</h2>
      <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-400">
        {cleanQualityNote(alert.topic_confidence, alert.note)} Segnale informativo, non conferma di incidente.
      </p>
      {isLow ? <LowConfidenceWarning /> : null}
      <div className="mt-5 grid gap-2 sm:grid-cols-2 xl:grid-cols-4">
        <Kpi label="P2" value={formatP2(alert.p2_index, 2)} tone="text-red-100" />
        <Kpi label="Time window" value={formatDate(alert.time_window)} />
        <Kpi label="Volume" value={formatNumber(alert.topic_volume)} />
        <Kpi label="Sentiment sum" value={formatP2(alert.topic_sentiment_sum, 2)} />
        <Kpi label="Sources" value={`R ${alert.source_counts?.reddit_rss ?? 0} / N ${alert.source_counts?.news_rss ?? 0} / G ${alert.source_counts?.news_api ?? 0}`} />
        <Kpi label="Sentiment counts" value={`- ${alert.sentiment_counts?.negative ?? 0} / = ${alert.sentiment_counts?.neutral ?? 0} / + ${alert.sentiment_counts?.positive ?? 0}`} />
        <Kpi label="Confidence" value={qualityShortLabel(alert.topic_confidence)} />
        <Kpi label="Severity" value={alert.severity?.toUpperCase()} />
      </div>
      <button type="button" onClick={() => onInspect(alert)} className="mt-5 rounded border border-cyan-300/35 bg-cyan-400/10 px-4 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-400/15">
        Analizza alert
      </button>
    </Panel>
  );
}

function CyberconCard({ summary, driver }) {
  return (
    <Panel className="p-5">
      <CyberconScale level={summary.cybercon_level} compact />
      <p className="mt-4 text-sm leading-6 text-slate-400">{CYBERCON_TEXT}</p>
      {driver ? (
        <div className="mt-4 rounded border border-slate-800 bg-slate-950/40 p-3">
          <span className="block font-mono text-xs uppercase tracking-[0.12em] text-slate-500">Driver livello</span>
          <strong className="mt-1 block text-slate-100">T{driver.dominant_topic} {driver.topic_label}</strong>
          <div className="mt-2 flex flex-wrap gap-2">
            <SignalBadge tone="muted">P2 {formatP2(driver.p2_index, 2)}</SignalBadge>
            <QualityBadge score={driver.topic_confidence} />
          </div>
        </div>
      ) : null}
      {summary.cybercon_warning || driver?.topic_confidence === "low" ? <LowConfidenceWarning /> : null}
    </Panel>
  );
}

function LowConfidenceWarning() {
  return (
    <p className="mt-3 rounded border border-amber-300/30 bg-amber-500/10 p-3 text-sm leading-6 text-amber-100">
      Topic low-confidence: interpretare con cautela.
    </p>
  );
}

function HomeTopicCard({ topic, onOpen }) {
  const totalSentiment = Object.values(topic.sentiment_distribution || {}).reduce((sum, value) => sum + Number(value || 0), 0);
  const pct = (key) => (totalSentiment ? ((topic.sentiment_distribution?.[key] || 0) / totalSentiment) * 100 : 0);
  return (
    <article className="rounded-lg border border-slate-800 bg-slate-950/45 p-4">
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="font-mono text-xs font-bold uppercase tracking-[0.14em] text-cyan-300">Topic {topic.topic_id}</div>
          <h3 className="mt-2 text-lg font-semibold leading-6 text-slate-50">{topic.topic_label}</h3>
        </div>
        <QualityBadge score={topic.topic_confidence} />
      </div>
      {topic.topic_confidence === "low" ? <p className="mt-3 text-sm text-amber-100">Interpretare con cautela.</p> : null}
      <div className="mt-3 flex flex-wrap gap-2">
        {(topic.top_words || []).slice(0, 5).map((word) => <SignalBadge key={word} tone="muted">{word}</SignalBadge>)}
      </div>
      <div className="mt-4 grid grid-cols-2 gap-2">
        <Kpi label="Docs" value={formatNumber(topic.docs_assigned ?? topic.total_docs)} />
        <Kpi label="Max |P2|" value={formatNumber(topic.max_abs_p2, 2)} />
        <Kpi label="Max negative" value={formatP2(topic.max_negative_p2, 2)} />
        <Kpi label="Max positive" value={formatP2(topic.max_positive_p2, 2)} />
      </div>
      <div className="mt-4 h-2 overflow-hidden rounded-full bg-slate-800">
        <div className="inline-block h-full bg-red-400" style={{ width: `${pct("negative")}%` }} />
        <div className="inline-block h-full bg-slate-500" style={{ width: `${pct("neutral")}%` }} />
        <div className="inline-block h-full bg-emerald-400" style={{ width: `${pct("positive")}%` }} />
      </div>
      <button type="button" onClick={() => onOpen(topic.topic_id)} className="mt-4 w-full rounded border border-cyan-300/35 bg-cyan-400/10 px-3 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-400/15">
        Apri topic
      </button>
    </article>
  );
}

function SummaryPanel({ title, values = {} }) {
  return (
    <Panel className="p-5">
      <SectionHeader eyebrow="Summary" title={title} icon={Database} />
      <div className="space-y-2">
        {Object.entries(values).map(([key, value]) => (
          <div key={key} className="flex items-center justify-between rounded border border-slate-800 bg-slate-950/40 px-3 py-2 text-sm">
            <span className="text-slate-300">{key}</span>
            <span className="font-mono text-slate-100">{formatNumber(value)}</span>
          </div>
        ))}
      </div>
    </Panel>
  );
}

function Kpi({ label, value, tone = "text-slate-100" }) {
  return (
    <div className="min-h-[66px] rounded border border-slate-800 bg-slate-950/40 p-3">
      <span className="block text-[10px] uppercase tracking-[0.12em] text-slate-500">{label}</span>
      <strong className={`mt-1 block break-words font-mono text-sm ${tone}`}>{value || "n/a"}</strong>
    </div>
  );
}

function formatUtc(value) {
  if (!value) return "n/a";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return `${new Intl.DateTimeFormat("it-IT", {
    timeZone: "UTC",
    year: "numeric",
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }).format(date)} UTC`;
}

function topEntry(values = {}) {
  return Object.entries(values)
    .map(([key, value]) => ({ key, value: Number(value || 0) }))
    .sort((a, b) => b.value - a.value)[0];
}
