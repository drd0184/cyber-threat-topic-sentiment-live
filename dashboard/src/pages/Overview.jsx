import { Activity, AlertTriangle, BarChart3, MessageSquare, ShieldCheck, Tags } from "lucide-react";
import { AlertCard } from "../components/AlertCard.jsx";
import { MiniTimeline, P2OverviewChart } from "../components/charts.jsx";
import { CyberconScale } from "../components/CyberconScale.jsx";
import { MetricCard, Panel, QualityBadge, SectionHeader, SignalBadge } from "../components/ui.jsx";
import { CYBERCON_SCALE, cleanQualityNote, formatDate, formatNumber, formatP2, qualityShortLabel } from "../utils/formatters.js";

const CYBERCON_TEXT =
  "CYBERCON è un livello sintetico di attenzione che riassume quanto un topic cyber stia mostrando un segnale di priorità nel flusso informativo analizzato. Non rappresenta la conferma di un incidente reale, ma indica il livello di attenzione che il sistema assegna a un tema sulla base dell’intensità del segnale rilevato.";

export function Overview({ data, openAlert, openTopic }) {
  const { summary, p2, topics, topTopicIds } = data;
  const hotFeed = [...p2].sort((a, b) => b.p2_abs - a.p2_abs).slice(0, 5);
  const hottest = summary.hottest_negative;

  if (!data.hasLiveData) {
    return (
      <div className="space-y-6">
        <Panel className="p-5 md:p-6">
          <div className="mb-5">
            <h1 className="text-3xl font-semibold uppercase tracking-[0.05em] text-white md:text-5xl">
              INDICE CYBER DI HOT TOPIC
            </h1>
            <p className="mt-3 text-lg text-cyan-100/85">Versione live in preparazione</p>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
              Nessun export live e stato ancora prodotto in `data/live/processed`. I JSON statici della baseline non vengono caricati come fonte dati della dashboard live.
            </p>
          </div>
        </Panel>
        <Panel className="p-5">
          <SectionHeader eyebrow="Pipeline live" title="Dati attesi" description="La dashboard resta pronta per ricevere export live separati dagli artifact statici legacy." icon={Activity} />
          <div className="grid gap-4 md:grid-cols-3">
            <MetricCard label="Record P2 live" value="0" icon={BarChart3} />
            <MetricCard label="Messaggi live" value="0" icon={MessageSquare} />
            <MetricCard label="Topic live" value="0" icon={Tags} />
          </div>
        </Panel>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <Panel className="p-5 md:p-6">
        <div className="mb-5">
          <h1 className="text-3xl font-semibold uppercase tracking-[0.05em] text-white md:text-5xl">
            INDICE CYBER DI HOT TOPIC
          </h1>
          <p className="mt-3 text-lg text-cyan-100/85">Semantic Intelligence Monitor</p>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
            Il sistema misura momentum semantico delle minacce cyber. Non conferma incidenti reali.
          </p>
        </div>

        <div className="grid gap-5 xl:grid-cols-[minmax(0,0.92fr)_minmax(520px,1.08fr)]">
          <PrimaryAlert alert={hottest} onInspect={() => openAlert(hottest)} />
          <div className="space-y-4">
            <CyberconScale level={summary.cybercon_level} />
            <CyberconExplainer />
          </div>
        </div>
      </Panel>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <MetricCard label="Messaggi analizzati" value={formatNumber(summary.total_posts)} icon={MessageSquare} />
        <MetricCard label="Topic monitorati" value={formatNumber(summary.total_topics)} icon={Tags} />
        <MetricCard label="Finestre temporali" value={formatNumber(summary.total_time_windows)} icon={Activity} />
        <MetricCard label="Sentiment medio" value={formatP2(summary.average_sentiment, 4)} icon={BarChart3} tone={summary.average_sentiment < 0 ? "negative" : "positive"} />
      </div>

      <div className="grid gap-6 xl:grid-cols-[1.25fr_0.95fr]">
        <Panel className="p-5">
          <SectionHeader eyebrow="Timeline" title="Finestra temporale 12h" description="Ogni barra apre l'alert con P2 assoluto più forte nella finestra." icon={Activity} />
          <MiniTimeline p2={p2} onSelectAlert={openAlert} />
        </Panel>
        <Panel className="p-5">
          <SectionHeader eyebrow="Allarmi" title="Alert ad alta priorità" description="Segnali ordinati per momentum semantico assoluto." icon={AlertTriangle} />
          <div className="space-y-3">
            {hotFeed.map((alert) => (
              <AlertCard key={`${alert.time_window}-${alert.dominant_topic}`} alert={alert} onInspect={openAlert} compact />
            ))}
          </div>
        </Panel>
      </div>

      <Panel className="p-5">
        <SectionHeader eyebrow="Indice P2" title="Momentum dei Topic principali" description="Vista sui Topic con P2 assoluto più intenso." icon={BarChart3} />
        <div className="h-[360px]">
          <P2OverviewChart p2={p2} topTopicIds={topTopicIds} topics={topics} />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Qualità e affidabilità" title="Confidenza dei Topic" description="Le label originali non sono state usate dal modello; servono solo per controllo ex post." icon={ShieldCheck} />
        <div className="grid gap-4 md:grid-cols-3">
          <MetricCard label="HIGH CONFIDENCE" value={formatNumber(summary.high_quality_topics_count)} tone="positive" />
          <MetricCard label="MEDIUM CONFIDENCE" value={formatNumber(summary.medium_quality_topics_count)} />
          <MetricCard label="LOW CONFIDENCE" value={formatNumber(summary.low_quality_topics_count)} tone="negative" />
        </div>
        <div className="mt-4 grid gap-4 lg:grid-cols-2">
          <TopicList title="Topic più affidabili" ids={summary.most_reliable_topics} topics={topics} onClick={openTopic} tone="positive" />
          <TopicList title="Topic da leggere con cautela" ids={summary.noisy_topics} topics={topics} onClick={openTopic} tone="negative" />
        </div>
      </Panel>
    </div>
  );
}

function PrimaryAlert({ alert, onInspect }) {
  if (!alert) return null;
  const quality = alert.topic_quality;
  return (
    <div className="rounded-lg border border-red-400/25 bg-red-500/10 p-5">
      <div className="mb-4 flex flex-wrap gap-2">
        <SignalBadge tone="negative">Alert principale</SignalBadge>
        <QualityBadge score={quality?.quality_score} />
        <SignalBadge tone="muted">Confidenza {qualityShortLabel(quality?.quality_score)}</SignalBadge>
      </div>
      <h2 className="text-2xl font-semibold text-slate-50">Topic: {alert.topic_label}</h2>
      <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-400">
        {cleanQualityNote(quality?.quality_score, quality?.quality_note)} Il segnale è da interpretare come priorità informativa, non come conferma di attacco.
      </p>
      <div className="mt-5 grid gap-2 sm:grid-cols-2 xl:grid-cols-3">
        <Kpi label="Finestra temporale" value={formatDate(alert.time_window)} />
        <Kpi label="P2" value={formatP2(alert.p2_index, 2)} tone="text-red-100" />
        <Kpi label="Volume" value={formatNumber(alert.topic_volume)} />
        <Kpi label="Sentiment" value={formatP2(alert.topic_sentiment_sum, 2)} />
        <Kpi label="Confidenza" value={qualityShortLabel(quality?.quality_score)} />
        <Kpi label="Threat %" value={`${formatNumber(quality?.threat_pct, 1)}%`} />
      </div>
      <button type="button" onClick={onInspect} className="mt-5 rounded border border-red-200/30 bg-red-400/10 px-4 py-2 text-sm font-semibold text-red-100 hover:bg-red-400/15">
        Analizza alert
      </button>
    </div>
  );
}

function CyberconExplainer() {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-950/45 p-4">
      <h3 className="text-sm font-semibold text-slate-50">Che cos'è CYBERCON?</h3>
      <p className="mt-2 text-sm leading-6 text-slate-400">{CYBERCON_TEXT}</p>
      <div className="mt-4 space-y-2">
        {CYBERCON_SCALE.map((item) => (
          <div key={item.level} className="border-t border-slate-800 pt-2 text-xs text-slate-500">
            <span className="font-mono text-slate-200">CYBERCON {item.level}</span>
            <span> — {item.homeDescription}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function Kpi({ label, value, tone = "text-slate-100" }) {
  return (
    <div className="rounded border border-slate-800 bg-slate-950/40 p-3">
      <span className="block text-xs uppercase tracking-[0.12em] text-slate-500">{label}</span>
      <strong className={`mt-1 block break-words font-mono text-sm ${tone}`}>{value}</strong>
    </div>
  );
}

function TopicList({ title, ids, topics, onClick, tone }) {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-950/35 p-4">
      <h3 className="text-sm font-semibold text-slate-300">{title}</h3>
      <div className="mt-3 flex flex-wrap gap-2">
        {ids.map((id) => {
          const topic = topics.find((item) => item.topic_id === id);
          return (
            <button key={id} type="button" onClick={() => onClick(id)} className={`rounded border px-2 py-1 text-sm ${tone === "positive" ? "border-emerald-300/30 bg-emerald-500/10 text-emerald-100" : "border-amber-300/30 bg-amber-500/10 text-amber-100"}`}>
              T{id} {topic?.topic_label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
