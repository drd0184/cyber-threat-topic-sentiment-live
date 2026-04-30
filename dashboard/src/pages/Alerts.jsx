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
  const [sourceType, setSourceType] = useState("all");
  const [timeRange, setTimeRange] = useState("all");
  const [sort, setSort] = useState("p2_abs_desc");
  const [query, setQuery] = useState("");
  const [page, setPage] = useState(1);
  const [detailOpen, setDetailOpen] = useState(Boolean(selectedAlert));
  const pageSize = 20;

  useEffect(() => {
    if (selectedAlert) {
      setDetailOpen(true);
      setTopic(String(selectedAlert.dominant_topic));
    }
  }, [selectedAlert]);

  const alerts = useMemo(() => {
    const q = query.trim().toLowerCase();
    const validTimes = data.alerts.map((row) => new Date(row.time_window).getTime()).filter((value) => !Number.isNaN(value));
    const maxTime = Math.max(...validTimes);
    const cutoff = timeRange === "72h" ? maxTime - 72 * 60 * 60 * 1000 : timeRange === "24h" ? maxTime - 24 * 60 * 60 * 1000 : null;
    const rows = data.alerts
      .filter((row) => direction === "all" || (row.p2_direction || row.direction) === direction)
      .filter((row) => topic === "all" || row.dominant_topic === Number(topic))
      .filter((row) => quality === "all" || row.topic_confidence === quality)
      .filter((row) => severity === "all" || row.severity === severity || getSeverity(row.p2_abs) === severity)
      .filter((row) => sourceType === "all" || (row.source_counts?.[sourceType] ?? row.source_distribution?.[sourceType] ?? 0) > 0)
      .filter((row) => !cutoff || new Date(row.time_window).getTime() >= cutoff)
      .filter((row) => !q || row.topic_label.toLowerCase().includes(q) || (row.top_words || []).join(" ").toLowerCase().includes(q));
    const sorters = {
      p2_abs_desc: (a, b) => b.p2_abs - a.p2_abs,
      p2_index_asc: (a, b) => a.p2_index - b.p2_index,
      time_desc: (a, b) => b.time_window.localeCompare(a.time_window),
      severity_desc: (a, b) => severityRank(b.severity) - severityRank(a.severity) || b.p2_abs - a.p2_abs,
      volume_desc: (a, b) => b.topic_volume - a.topic_volume,
    };
    return rows.sort(sorters[sort]);
  }, [data.alerts, direction, topic, quality, severity, sourceType, timeRange, sort, query]);

  useEffect(() => {
    setPage(1);
  }, [direction, topic, quality, severity, sourceType, timeRange, sort, query]);

  const pageCount = Math.max(1, Math.ceil(alerts.length / pageSize));
  const safePage = Math.min(page, pageCount);
  const visibleAlerts = alerts.slice((safePage - 1) * pageSize, safePage * pageSize);

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
        <SectionHeader eyebrow="Alert" title="Alert di momentum semantico" description="Filtra per severity, direzione, topic, confidenza, fonte e intervallo. I topic low-confidence restano inclusi." icon={AlertTriangle} />
        <FilterBar
          direction={direction}
          setDirection={setDirection}
          topic={topic}
          setTopic={setTopic}
          quality={quality}
          setQuality={setQuality}
          severity={severity}
          setSeverity={setSeverity}
          sourceType={sourceType}
          setSourceType={setSourceType}
          timeRange={timeRange}
          setTimeRange={setTimeRange}
          sort={sort}
          setSort={setSort}
          query={query}
          setQuery={setQuery}
          topics={data.topics}
        />
        <div className="mt-5 grid gap-4 xl:grid-cols-[1fr_420px]">
          <div>
            <div className="mb-3 flex flex-col gap-2 rounded border border-slate-800 bg-slate-950/40 p-3 text-sm text-slate-400 md:flex-row md:items-center md:justify-between">
              <span>{formatNumber(alerts.length)} alert trovati. Mostrati {formatNumber(visibleAlerts.length)} per pagina.</span>
              <Pagination page={safePage} pageCount={pageCount} setPage={setPage} />
            </div>
            <div className="space-y-3">
              {visibleAlerts.length ? visibleAlerts.map((alert) => <AlertCard key={`${alert.time_window}-${alert.dominant_topic}`} alert={alert} onInspect={inspect} />) : <EmptyState />}
            </div>
            <div className="mt-3">
              <Pagination page={safePage} pageCount={pageCount} setPage={setPage} />
            </div>
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
                <DetailMetric label="Confidenza" value={selectedAlert.topic_confidence?.toUpperCase() || "n/a"} />
                <DetailMetric label="Severity" value={selectedAlert.severity?.toUpperCase() || getSeverity(selectedAlert.p2_abs).toUpperCase()} />
                <DetailMetric label="Fonti" value={`R ${selectedAlert.source_counts?.reddit_rss ?? selectedAlert.reddit_count ?? 0} / N ${selectedAlert.source_counts?.news_rss ?? 0} / G ${selectedAlert.source_counts?.news_api ?? selectedAlert.news_api_count ?? 0}`} />
              </div>
              {selectedAlert.topic_confidence === "low" ? (
                <p className="mt-3 rounded border border-amber-300/30 bg-amber-500/10 p-3 text-sm leading-6 text-amber-100">
                  Topic low-confidence: il segnale e incluso, ma va interpretato con cautela.
                </p>
              ) : null}
              <p className="mt-3 rounded border border-amber-300/20 bg-amber-500/10 p-3 text-sm leading-6 text-amber-50/80">
                Il segnale e da interpretare come priorita informativa, non come conferma di attacco.
              </p>
              <div className="mt-4 h-52 rounded border border-slate-800 bg-slate-950/40 p-3">
                <TopicLineChart rows={topicRows} dataKey="p2_index" color="#EF4444" />
              </div>
              <h4 className="mt-4 text-sm font-semibold text-slate-300">Documenti associati</h4>
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
    <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-8">
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
        <option value="all">Tutte le severity</option>
        <option value="critical">CRITICAL</option>
        <option value="high">HIGH</option>
        <option value="elevated">ELEVATED</option>
        <option value="watch">WATCH</option>
        <option value="low">LOW</option>
      </Select>
      <Select value={props.sourceType} onChange={props.setSourceType}>
        <option value="all">Tutte le fonti</option>
        <option value="reddit_rss">Reddit RSS</option>
        <option value="news_rss">News RSS</option>
        <option value="news_api">GDELT DOC API</option>
      </Select>
      <Select value={props.timeRange} onChange={props.setTimeRange}>
        <option value="all">Tutto il periodo</option>
        <option value="72h">Ultime 72h</option>
        <option value="24h">Ultime 24h</option>
      </Select>
      <Select value={props.sort} onChange={props.setSort}>
        <option value="p2_abs_desc">P2 assoluto</option>
        <option value="p2_index_asc">P2 crescente</option>
        <option value="time_desc">Tempo recente</option>
        <option value="severity_desc">Severity</option>
        <option value="volume_desc">Volume</option>
      </Select>
    </div>
  );
}

function Pagination({ page, pageCount, setPage }) {
  return (
    <div className="flex items-center gap-2">
      <button
        type="button"
        onClick={() => setPage(Math.max(1, page - 1))}
        disabled={page <= 1}
        className="rounded border border-slate-700 px-3 py-1 text-xs font-semibold text-slate-200 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Prec
      </button>
      <span className="font-mono text-xs text-slate-400">Pagina {page} / {pageCount}</span>
      <button
        type="button"
        onClick={() => setPage(Math.min(pageCount, page + 1))}
        disabled={page >= pageCount}
        className="rounded border border-slate-700 px-3 py-1 text-xs font-semibold text-slate-200 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Succ
      </button>
    </div>
  );
}

function severityRank(value) {
  return { low: 1, watch: 2, elevated: 3, high: 4, critical: 5 }[value] || 0;
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
