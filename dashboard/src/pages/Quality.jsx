import { BarChart3, ShieldCheck } from "lucide-react";
import { MetricCard, Panel, QualityBadge, SectionHeader } from "../components/ui.jsx";
import { formatNumber, formatP2 } from "../utils/formatters.js";

const explanation = [
  "Tutti i topic sono inclusi nel P2 e nella dashboard.",
  "topic_confidence non esclude un topic: rende esplicita l'affidabilita interpretativa.",
  "I topic low-confidence vengono mostrati con warning, non nascosti.",
  "P2 e raw semantic momentum: non valida incidenti reali.",
];

export function Quality({ data }) {
  const { summary, topics } = data;
  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Qualita e affidabilita" title="Confidenza dei Topic" description="La dashboard non nasconde topic deboli: li include e segnala i limiti interpretativi." icon={ShieldCheck} />
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
        <SectionHeader eyebrow="Topic table" title="Affidabilita operativa" description="Tutti i topic ufficiali LDA live a 10 topic sono presenti." icon={BarChart3} />
        <div className="thin-scrollbar overflow-x-auto">
          <table className="w-full min-w-[980px] border-collapse text-left text-sm">
            <thead className="font-mono text-xs uppercase tracking-[0.12em] text-slate-500">
              <tr>
                <th className="border-b border-slate-800 py-3 pr-4">Topic</th>
                <th className="border-b border-slate-800 py-3 pr-4">Confidenza</th>
                <th className="border-b border-slate-800 py-3 pr-4">Docs</th>
                <th className="border-b border-slate-800 py-3 pr-4">Max abs P2</th>
                <th className="border-b border-slate-800 py-3 pr-4">Nota</th>
              </tr>
            </thead>
            <tbody>
              {topics.map((topic) => (
                <tr key={topic.topic_id} className="text-slate-300">
                  <td className="border-b border-slate-900 py-3 pr-4">T{topic.topic_id} {topic.topic_label}</td>
                  <td className="border-b border-slate-900 py-3 pr-4"><QualityBadge score={topic.topic_confidence} /></td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatNumber(topic.docs_assigned ?? topic.total_docs)}</td>
                  <td className="border-b border-slate-900 py-3 pr-4">{formatP2(topic.max_abs_p2, 2)}</td>
                  <td className="border-b border-slate-900 py-3 pr-4 text-slate-400">{topic.note}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Interpretazione" title="Limite P2" description="Il P2 ordina priorita informative, non conferme operative." icon={ShieldCheck} />
        <p className="rounded-lg border border-amber-300/20 bg-amber-500/10 p-4 text-sm leading-6 text-amber-50/85">
          Low-confidence non significa esclusione. Significa che il cluster semantico e ampio o meno stabile: gli alert restano nel monitor, ma richiedono piu cautela nella lettura.
        </p>
      </Panel>
    </div>
  );
}
