import { useMemo, useState } from "react";
import { Database } from "lucide-react";
import { EmptyState, MetricCard, Panel, SearchInput, SectionHeader } from "../components/ui.jsx";
import { directionLabel, formatDate, formatNumber, formatP2, qualityShortLabel } from "../utils/formatters.js";

const links = [
  ["Live raw", "../../data/live/raw/"],
  ["Live processed", "../../data/live/processed/"],
  ["Live archive", "../../data/live/archive/"],
  ["Config", "../../config/"],
  ["Stato progetto", "../../PROJECT_STATUS.md"],
];

export function DataConsole({ data }) {
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState("all");
  const [direction, setDirection] = useState("all");

  const rows = useMemo(() => {
    const q = query.trim().toLowerCase();
    return data.p2
      .filter((row) => topic === "all" || row.dominant_topic === Number(topic))
      .filter((row) => direction === "all" || row.p2_direction === direction)
      .filter((row) => !q || row.topic_label.toLowerCase().includes(q) || row.top_words.join(" ").toLowerCase().includes(q))
      .slice(0, 120);
  }, [data.p2, topic, direction, query]);

  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Console dati" title="Record P2 e artifact" description="Vista tecnica dei dati live esportati per la dashboard React." icon={Database} />
        <div className="grid gap-4 md:grid-cols-4">
          <MetricCard label="Righe P2 live" value={formatNumber(data.p2.length)} />
          <MetricCard label="Messaggi live" value={formatNumber(data.posts.length)} />
          <MetricCard label="Topic live" value={formatNumber(data.topics.length)} />
          <MetricCard label="Righe validazione" value={formatNumber(data.validation.length)} />
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
        <SectionHeader eyebrow="Artifact" title="Link locali" description="Percorsi live. I CSV e JSON statici della baseline non sono dataset live." icon={Database} />
        <div className="flex flex-wrap gap-2">
          {links.map(([label, href]) => (
            <a key={label} href={href} className="rounded border border-cyan-300/25 bg-cyan-500/10 px-3 py-2 text-sm font-semibold text-cyan-100 hover:bg-cyan-500/15">
              {label}
            </a>
          ))}
        </div>
      </Panel>
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
              <td className="border-b border-slate-900 py-3 pr-4">{qualityShortLabel(row.topic_quality?.quality_score)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
