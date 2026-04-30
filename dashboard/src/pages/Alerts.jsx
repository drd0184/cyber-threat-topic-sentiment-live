import { useEffect, useMemo, useState } from "react";
import { AlertTriangle, SlidersHorizontal, X } from "lucide-react";
import { AlertCard } from "../components/AlertCard.jsx";
import { TopicLineChart } from "../components/charts.jsx";
import { PostsTable } from "../components/TopicDetailPanel.jsx";
import { EmptyState, Panel, SearchInput, SectionHeader } from "../components/ui.jsx";
import { formatDate, formatNumber, formatP2, getSeverity } from "../utils/formatters.js";

export function Alerts({ data, selectedAlert, openAlert, setSelectedAlertKey }) {
  const [direction, setDirection] = useState("all");
  const [topic, setTopic] = useState("all");
  const [quality, setQuality] = useState("all");
  const [severity, setSeverity] = useState("all");
  const [sort, setSort] = useState("p2_abs_desc");
  const [query, setQuery] = useState("");
  const [detailOpen, setDetailOpen] = useState(Boolean(selectedAlert));

  useEffect(() => {
    if (selectedAlert) {
      setDetailOpen(true);
      setTopic(String(selectedAlert.dominant_topic));
    }
  }, [selectedAlert]);

  const alerts = useMemo(() => {
    const q = query.trim().toLowerCase();
    const rows = data.p2
      .filter((row) => direction === "all" || row.p2_direction === direction)
      .filter((row) => topic === "all" || row.dominant_topic === Number(topic))
      .filter((row) => quality === "all" || row.topic_quality?.quality_score === quality)
      .filter((row) => severity === "all" || getSeverity(row.p2_abs) === severity)
      .filter((row) => !q || row.topic_label.toLowerCase().includes(q) || (row.top_words || []).join(" ").toLowerCase().includes(q));
    const sorters = {
      p2_abs_desc: (a, b) => b.p2_abs - a.p2_abs,
      p2_index_asc: (a, b) => a.p2_index - b.p2_index,
      time_desc: (a, b) => b.time_window.localeCompare(a.time_window),
      volume_desc: (a, b) => b.topic_volume - a.topic_volume,
    };
    return rows.sort(sorters[sort]);
  }, [data.p2, direction, topic, quality, severity, sort, query]);

  const alertPosts = selectedAlert
    ? [...(data.postsByAlert.get(`${selectedAlert.time_window}-${selectedAlert.dominant_topic}`) || [])].sort((a, b) => Math.abs(b.vader_compound) - Math.abs(a.vader_compound))
    : [];
  const topicRows = selectedAlert ? data.p2ByTopic.get(selectedAlert.dominant_topic) || [] : [];

  const inspect = (alert) => {
    setSelectedAlertKey(`${alert.time_window}-${alert.dominant_topic}`);
    setDetailOpen(true);
    openAlert(alert);
  };

  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Allarmi" title="Alert di momentum semantico" description="Filtra per Topic, gravità, confidenza e finestra temporale." icon={AlertTriangle} />
        <FilterBar
          direction={direction}
          setDirection={setDirection}
          topic={topic}
          setTopic={setTopic}
          quality={quality}
          setQuality={setQuality}
          severity={severity}
          setSeverity={setSeverity}
          sort={sort}
          setSort={setSort}
          query={query}
          setQuery={setQuery}
          topics={data.topics}
        />
        <div className="mt-5 grid gap-4 xl:grid-cols-[1fr_420px]">
          <div className="space-y-3">
            {alerts.length ? alerts.map((alert) => <AlertCard key={`${alert.time_window}-${alert.dominant_topic}`} alert={alert} onInspect={inspect} />) : <EmptyState />}
          </div>
          {detailOpen && selectedAlert ? (
            <aside className="sticky top-24 h-fit rounded-lg border border-cyan-300/25 bg-slate-950/85 p-4 shadow-2xl shadow-black/30">
              <div className="mb-3 flex items-start justify-between gap-3">
                <div>
                  <div className="font-mono text-xs uppercase tracking-[0.16em] text-cyan-300">Dettaglio Alert</div>
                  <h3 className="mt-2 text-lg font-semibold text-slate-50">{selectedAlert.topic_label}</h3>
                  <p className="font-mono text-xs text-slate-500">{formatDate(selectedAlert.time_window)}</p>
                </div>
                <button onClick={() => setDetailOpen(false)} className="rounded border border-slate-700 p-2 text-slate-400 hover:text-slate-100"><X className="h-4 w-4" /></button>
              </div>
              <div className="grid grid-cols-2 gap-2">
                <DetailMetric label="P2" value={formatP2(selectedAlert.p2_index, 2)} />
                <DetailMetric label="Volume" value={formatNumber(selectedAlert.topic_volume)} />
                <DetailMetric label="Sentiment" value={formatP2(selectedAlert.topic_sentiment_sum, 2)} />
                <DetailMetric label="Confidenza" value={selectedAlert.topic_quality?.quality_score?.toUpperCase() || "n/a"} />
                <DetailMetric label="Threat %" value={selectedAlert.hot_quality ? `${formatNumber(selectedAlert.hot_quality.threat_pct, 1)}%` : selectedAlert.topic_quality ? `${formatNumber(selectedAlert.topic_quality.threat_pct, 1)}%` : "n/a"} />
              </div>
              <p className="mt-3 rounded border border-amber-300/20 bg-amber-500/10 p-3 text-sm leading-6 text-amber-50/80">
                Il segnale è da interpretare come priorità informativa, non come conferma di attacco.
              </p>
              <div className="mt-4 h-52 rounded border border-slate-800 bg-slate-950/40 p-3">
                <TopicLineChart rows={topicRows} dataKey="p2_index" color="#EF4444" />
              </div>
              <h4 className="mt-4 text-sm font-semibold text-slate-300">Post associati</h4>
              <PostsTable posts={alertPosts.slice(0, 30)} />
            </aside>
          ) : null}
        </div>
      </Panel>
    </div>
  );
}

function FilterBar(props) {
  return (
    <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-6">
      <SearchInput value={props.query} onChange={props.setQuery} placeholder="Cerca topic / top words" />
      <Select value={props.direction} onChange={props.setDirection}>
        <option value="all">Tutte le direzioni</option>
        <option value="negative">Negativo</option>
        <option value="positive">Positivo</option>
      </Select>
      <Select value={props.topic} onChange={props.setTopic}>
        <option value="all">Tutti i topic</option>
        {props.topics.map((topic) => <option key={topic.topic_id} value={topic.topic_id}>T{topic.topic_id} {topic.topic_label}</option>)}
      </Select>
      <Select value={props.quality} onChange={props.setQuality}>
        <option value="all">Tutte le confidenze</option>
        <option value="high">Alta</option>
        <option value="medium">Media</option>
        <option value="low">Bassa</option>
      </Select>
      <Select value={props.severity} onChange={props.setSeverity}>
        <option value="all">Tutte le severità</option>
        <option value="critical">CRITICAL</option>
        <option value="high">HIGH</option>
        <option value="elevated">ELEVATED</option>
        <option value="watch">WATCH</option>
        <option value="nominal">NOMINAL</option>
      </Select>
      <Select value={props.sort} onChange={props.setSort}>
        <option value="p2_abs_desc">P2 assoluto decrescente</option>
        <option value="p2_index_asc">P2 crescente</option>
        <option value="time_desc">Tempo recente</option>
        <option value="volume_desc">Volume decrescente</option>
      </Select>
    </div>
  );
}

function Select({ value, onChange, children }) {
  return (
    <label className="relative">
      <SlidersHorizontal className="pointer-events-none absolute left-3 top-2.5 h-4 w-4 text-slate-500" />
      <select value={value} onChange={(event) => onChange(event.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950/75 py-2 pl-9 pr-3 text-sm text-slate-100 outline-none focus:border-cyan-300/60">
        {children}
      </select>
    </label>
  );
}

function DetailMetric({ label, value }) {
  return (
    <div className="rounded border border-slate-800 bg-slate-900/40 p-2">
      <span className="block text-xs text-slate-500">{label}</span>
      <strong className="font-mono text-slate-100">{value}</strong>
    </div>
  );
}
