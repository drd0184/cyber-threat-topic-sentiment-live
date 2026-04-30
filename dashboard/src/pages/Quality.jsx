import { BarChart3, ShieldCheck } from "lucide-react";
import { MetricCard, Panel, QualityBadge, SectionHeader } from "../components/ui.jsx";
import { cleanQualityNote, formatNumber, formatP2 } from "../utils/formatters.js";

const explanation = [
  "Le label originali non sono state usate come feature.",
  "Sono usate solo per controllo ex post.",
  "HIGH / MEDIUM / LOW CONFIDENCE indica quanto è interpretabile il Topic.",
  "P2 non è una prova di incidente.",
];

export function Quality({ data }) {
  const { summary, topics, validation } = data;
  const primary = summary.hottest_negative;
  if (!primary) {
    return (
      <div className="space-y-6">
        <Panel className="p-5">
          <SectionHeader eyebrow="Qualita e affidabilita" title="Nessun P2 live disponibile" description="Gli artifact statici legacy non vengono trattati come dati live." icon={ShieldCheck} />
          <div className="grid gap-4 md:grid-cols-4">
            {explanation.map((item) => (
              <div key={item} className="rounded-lg border border-slate-800 bg-slate-950/40 p-4 text-sm leading-6 text-slate-300">
                {item}
              </div>
            ))}
          </div>
        </Panel>
      </div>
    );
  }
  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Qualità e affidabilità" title="Confidenza dei Topic" description="La pagina separa interpretabilità semantica, controllo ex post e priorità P2." icon={ShieldCheck} />
        <div className="grid gap-4 md:grid-cols-4">
          {explanation.map((item) => (
            <div key={item} className="rounded-lg border border-slate-800 bg-slate-950/40 p-4 text-sm leading-6 text-slate-300">
              {item}
            </div>
          ))}
        </div>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          <MetricCard label="HIGH CONFIDENCE" value={formatNumber(summary.high_quality_topics_count)} tone="positive" />
          <MetricCard label="MEDIUM CONFIDENCE" value={formatNumber(summary.medium_quality_topics_count)} />
          <MetricCard label="LOW CONFIDENCE" value={formatNumber(summary.low_quality_topics_count)} tone="negative" />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Topic quality" title="Validazione ex post" description="Threat % e Irrelevant % descrivono il controllo successivo sui metadata, non feature usate dal modello." icon={BarChart3} />
        <div className="thin-scrollbar overflow-x-auto">
          <table className="w-full min-w-[980px] border-collapse text-left text-sm">
            <thead className="font-mono text-xs uppercase tracking-[0.12em] text-slate-500">
              <tr>
                <th className="border-b border-slate-800 py-3 pr-4">Topic</th>
                <th className="border-b border-slate-800 py-3 pr-4">Confidenza</th>
                <th className="border-b border-slate-800 py-3 pr-4">Threat %</th>
                <th className="border-b border-slate-800 py-3 pr-4">Irrelevant %</th>
                <th className="border-b border-slate-800 py-3 pr-4">Nota qualità</th>
              </tr>
            </thead>
            <tbody>
              {topics.map((topic) => (
                <tr key={topic.topic_id} className="text-slate-300">
                  <td className="border-b border-slate-900 py-3 pr-4">T{topic.topic_id} {topic.topic_label}</td>
                  <td className="border-b border-slate-900 py-3 pr-4"><QualityBadge score={topic.quality_score} /></td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatNumber(topic.threat_pct, 1)}%</td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatNumber(topic.irrelevant_pct, 1)}%</td>
                  <td className="border-b border-slate-900 py-3 pr-4 text-slate-400">{cleanQualityNote(topic.quality_score, topic.quality_note)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Alert principale" title="Limite interpretativo P2" description="Il P2 ordina priorità informative, non conferme operative." icon={ShieldCheck} />
        <p className="rounded-lg border border-amber-300/20 bg-amber-500/10 p-4 text-sm leading-6 text-amber-50/85">
          Hot Topic negativo principale: T{primary.dominant_topic} {primary.topic_label}. Validazione ex post: le label originali non sono state usate dal modello. Il segnale è da interpretare come priorità informativa, non come conferma di attacco.
        </p>
        <div className="mt-5 grid gap-3 md:grid-cols-3">
          <MetricCard label="P2 principale" value={formatP2(primary.p2_index, 2)} tone="negative" />
          <MetricCard label="Volume" value={formatNumber(primary.topic_volume)} />
          <MetricCard label="CYBERCON" value={summary.cybercon_level} tone="negative" />
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Controllo ranking" title="P2 vs Volume vs Sentiment" description="Confronto per mostrare che P2 combina volume e sentiment aggregato." icon={BarChart3} />
        <div className="thin-scrollbar overflow-x-auto">
          <table className="w-full min-w-[920px] border-collapse text-left text-sm">
            <thead className="font-mono text-xs uppercase tracking-[0.12em] text-slate-500">
              <tr>
                <th className="border-b border-slate-800 py-3 pr-4">Ranking</th>
                <th className="border-b border-slate-800 py-3 pr-4">Topic</th>
                <th className="border-b border-slate-800 py-3 pr-4">Volume</th>
                <th className="border-b border-slate-800 py-3 pr-4">Sentiment</th>
                <th className="border-b border-slate-800 py-3 pr-4">P2</th>
              </tr>
            </thead>
            <tbody>
              {validation.slice(0, 18).map((row) => (
                <tr key={`${row.ranking_type}-${row.rank}`} className="text-slate-300">
                  <td className="border-b border-slate-900 py-3 pr-4 font-mono text-xs">{row.ranking_type} #{row.rank}</td>
                  <td className="border-b border-slate-900 py-3 pr-4">T{row.dominant_topic} {row.topic_label}</td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatNumber(row.topic_volume)}</td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatP2(row.topic_sentiment_sum, 2)}</td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatP2(row.p2_index, 2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>
    </div>
  );
}
