import { BookOpen, ShieldCheck } from "lucide-react";
import { Panel, SectionHeader } from "../components/ui.jsx";

const steps = [
  ["Cyber news RSS", "Fonti pubbliche recenti", "Raccoglie news e alert cyber in data/live/raw."],
  ["Reddit RSS", "Subreddit cyber/security", "Integra discussioni pubbliche recenti senza usare il dataset statico baseline."],
  ["NVD/CISA", "CVE, advisory, KEV", "Aggiunge segnali vulnerabilita e advisory istituzionali."],
  ["Normalizzazione", "Fonti live eterogenee", "Converte tutto in uno schema comune con source, created_at, text_raw, url e cve_ids."],
  ["Preprocessing", "text_raw", "Genera text_clean per topic assignment mantenendo text_raw intatto."],
  ["Topic assignment", "text_clean", "Assegna topic usando modello o mapping approvato per la fase live."],
  ["VADER", "text_raw", "Calcola sentiment sul testo originale."],
  ["Aggregazione 12h", "Topic + sentiment", "Raggruppa volume e sentiment per topic in finestre temporali da 12 ore."],
  ["P2", "volume_factor x sentiment_factor", "Misura momentum semantico e priorita informativa."],
  ["Export dashboard", "data/live/processed", "Produce JSON live separati dagli output statici legacy."],
];

const safeguards = [
  "I vecchi CSV statici e i vecchi JSON dashboard non sono dataset live.",
  "LDA/topic assignment usa testo preprocessato, non label manuali.",
  "VADER usa solo text_raw.",
  "L'aggregazione temporale e su finestre da 12h.",
  "P2 misura semantic momentum, non incidenti verificati.",
  "Modelli e script non vanno rimossi senza conferma.",
];

export function Methodology() {
  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Metodologia" title="Live pipeline plan" description="La dashboard live deve essere alimentata da raccolte recenti, non dagli artifact statici della baseline." icon={BookOpen} />
        <div className="grid gap-4 lg:grid-cols-3">
          {steps.map(([title, input, why], index) => (
            <article key={title} className="rounded-lg border border-slate-800 bg-slate-950/40 p-4">
              <div className="mb-3 flex items-center gap-3">
                <span className="grid h-8 w-8 place-items-center rounded border border-cyan-300/30 bg-cyan-500/10 font-mono text-sm font-bold text-cyan-100">{index + 1}</span>
                <h3 className="font-semibold text-slate-50">{title}</h3>
              </div>
              <dl className="space-y-2 text-sm">
                <div>
                  <dt className="font-mono text-xs uppercase tracking-[0.12em] text-slate-500">Input</dt>
                  <dd className="text-slate-300">{input}</dd>
                </div>
                <div>
                  <dt className="font-mono text-xs uppercase tracking-[0.12em] text-slate-500">Ruolo</dt>
                  <dd className="leading-6 text-slate-400">{why}</dd>
                </div>
              </dl>
            </article>
          ))}
        </div>
      </Panel>

      <Panel className="p-5">
        <SectionHeader eyebrow="Controlli metodologici" title="Interpretazione corretta" description="I segnali sono utili per prioritizzare analisi OSINT, non per dichiarare compromissioni." icon={ShieldCheck} />
        <div className="grid gap-4 lg:grid-cols-2">
          {safeguards.map((item) => (
            <div key={item} className="rounded border border-slate-800 bg-slate-950/40 p-4 text-sm leading-6 text-slate-300">{item}</div>
          ))}
        </div>
        <div className="mt-5 rounded-lg border border-cyan-300/20 bg-cyan-500/10 p-5 font-mono text-sm leading-7 text-cyan-50/90">
          <div>volume_factor = topic_volume / avg_topic_volume</div>
          <div>sentiment_factor = topic_sentiment_sum / avg_abs_topic_sentiment_sum</div>
          <div>P2 = volume_factor * sentiment_factor</div>
        </div>
      </Panel>
    </div>
  );
}
