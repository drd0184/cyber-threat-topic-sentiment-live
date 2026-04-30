import { useMemo, useState } from "react";
import { Database } from "lucide-react";
import { EmptyState, MetricCard, Panel, SearchInput, SectionHeader } from "../components/ui.jsx";
import { directionLabel, formatDate, formatNumber, formatP2, qualityShortLabel } from "../utils/formatters.js";

export function DataConsole({ data }) {
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState("all");
  const [direction, setDirection] = useState("all");
  const { metadata, summary } = data;

  const rows = useMemo(() => {
    const q = query.trim().toLowerCase();
    return data.p2
      .filter((row) => topic === "all" || row.dominant_topic === Number(topic))
      .filter((row) => direction === "all" || row.p2_direction === direction)
      .filter((row) => !q || row.topic_label.toLowerCase().includes(q) || row.top_words.join(" ").toLowerCase().includes(q))
      .slice(0, 160);
  }, [data.p2, topic, direction, query]);

  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Console dati" title="Artifact live" description="Vista tecnica dei JSON live esportati per la dashboard React." icon={Database} />
        <div className="grid gap-4 md:grid-cols-4">
          <MetricCard label="Righe P2 live" value={formatNumber(data.p2.length)} />
          <MetricCard label="Documenti live" value={formatNumber(data.posts.length)} />
          <MetricCard label="Topic live" value={formatNumber(data.topics.length)} />
          <MetricCard label="Alert live" value={formatNumber(data.alerts.length)} />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Metadata" title="Stato export" description="Timestamp, scope e file input della dashboard live." icon={Database} />
        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          <Info label="generated_at_utc" value={formatDate(metadata.generated_at_utc)} />
          <Info label="latest_collected_at" value={formatDate(metadata.latest_collected_at)} />
          <Info label="latest_document_created_at" value={formatDate(metadata.latest_document_created_at)} />
          <Info label="total docs" value={formatNumber(metadata.total_documents)} />
          <Info label="data_scope" value={metadata.data_scope} />
          <Info label="schedule" value={metadata.pipeline_schedule} />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Distribuzioni" title="Controlli rapidi" description="Distribuzioni aggregate esportate nei JSON live." icon={Database} />
        <div className="grid gap-4 lg:grid-cols-4">
          <Distribution title="Source type" values={summary.source_type_distribution} />
          <Distribution title="Topic distribution" values={summary.topic_distribution} />
          <Distribution title="Topic confidence" values={summary.topic_confidence_distribution} />
          <Distribution title="Severity" values={summary.severity_distribution} />
        </div>
      </Panel>

      <Panel className="p-5">
        <div className="mb-5 grid gap-3 md:grid-cols-[1fr_220px_180px]">
          <SearchInput value={query} onChange={setQuery} placeholder="Cerca segnali live" />
          <select value={topic} onChange={(event) => setTopic(event.target.value)} className="rounded-lg border border-slate-700 bg-slate-950/75 px-3 py-2 text-sm text-slate-100">
            <option value="all">Tutti i topic</option>
            {data.topics.map((topicItem) => <option key={topicItem.topic_id} value={topicItem.topic_id}>T{topicItem.topic_id} {topicItem.topic_label}</option>)}
          </select>
          <select value={direction} onChange={(event) => setDirection(event.target.value)} className="rounded-lg border border-slate-700 bg-slate-950/75 px-3 py-2 text-sm text-slate-100">
            <option value="all">Tutte le direzioni</option>
            <option value="negative">Negativo</option>
            <option value="positive">Positivo</option>
          </select>
        </div>
        {rows.length ? <SignalsTable rows={rows} /> : <EmptyState />}
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Input" title="File usati" description="La dashboard live non legge vecchi dati statici." icon={Database} />
        <div className="grid gap-2">
          {Object.entries(metadata.input_files || {}).map(([key, value]) => (
            <div key={key} className="rounded border border-slate-800 bg-slate-950/40 p-3 font-mono text-xs text-slate-300">
              <span className="text-cyan-300">{key}</span>: {value}
            </div>
          ))}
        </div>
      </Panel>
    </div>
  );
}

function Info({ label, value }) {
  return (
    <div className="rounded border border-slate-800 bg-slate-950/40 p-3">
      <span className="block text-xs uppercase tracking-[0.12em] text-slate-500">{label}</span>
      <strong className="mt-1 block break-words font-mono text-sm text-slate-100">{value || "n/a"}</strong>
    </div>
  );
}

function Distribution({ title, values = {} }) {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-950/40 p-4">
      <h3 className="text-sm font-semibold text-slate-300">{title}</h3>
      <div className="mt-3 space-y-2">
        {Object.entries(values).map(([key, value]) => (
          <div key={key} className="flex items-center justify-between gap-3 rounded border border-slate-800 bg-slate-900/35 px-3 py-2 text-sm">
            <span className="text-slate-400">{key}</span>
            <span className="font-mono text-slate-100">{formatNumber(value)}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function SignalsTable({ rows }) {
  return (
    <div className="thin-scrollbar max-h-[640px] overflow-auto">
      <table className="w-full min-w-[980px] border-collapse text-left text-sm">
        <thead className="sticky top-0 bg-slate-950 font-mono text-xs uppercase tracking-[0.12em] text-slate-500">
          <tr>
            <th className="border-b border-slate-800 py-3 pr-4">Finestra</th>
            <th className="border-b border-slate-800 py-3 pr-4">Topic</th>
            <th className="border-b border-slate-800 py-3 pr-4">Direzione</th>
            <th className="border-b border-slate-800 py-3 pr-4">Volume</th>
            <th className="border-b border-slate-800 py-3 pr-4">Sentiment</th>
            <th className="border-b border-slate-800 py-3 pr-4">P2</th>
            <th className="border-b border-slate-800 py-3 pr-4">Confidenza</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={`${row.time_window}-${row.dominant_topic}`} className="text-slate-300">
              <td className="border-b border-slate-900 py-3 pr-4 font-mono text-xs">{formatDate(row.time_window)}</td>
              <td className="border-b border-slate-900 py-3 pr-4">T{row.dominant_topic} {row.topic_label}</td>
              <td className="border-b border-slate-900 py-3 pr-4">{directionLabel(row.p2_direction)}</td>
              <td className="border-b border-slate-900 py-3 pr-4">{formatNumber(row.topic_volume)}</td>
              <td className="border-b border-slate-900 py-3 pr-4">{formatP2(row.topic_sentiment_sum, 2)}</td>
              <td className="border-b border-slate-900 py-3 pr-4">{formatP2(row.p2_index, 2)}</td>
              <td className="border-b border-slate-900 py-3 pr-4">{qualityShortLabel(row.topic_confidence)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
