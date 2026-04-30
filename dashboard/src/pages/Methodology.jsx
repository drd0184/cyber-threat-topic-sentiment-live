import { BookOpen, ShieldCheck } from "lucide-react";
import { Panel, SectionHeader } from "../components/ui.jsx";

const steps = [
  ["Reddit RSS", "Subreddit cyber/security", "Integra discussioni pubbliche recenti."],
  ["News/blog RSS", "Fonti editoriali cyber", "Raccoglie articoli e analisi da blog/news specializzati."],
  ["GDELT DOC API", "News API pubblica", "Amplia il corpus social/news recente senza API key."],
  ["Normalizzazione", "Fonti live eterogenee", "Converte tutto in uno schema comune con source, created_at, text_raw e url."],
  ["Preprocessing", "text_raw -> text_clean", "Genera text_clean per LDA mantenendo text_raw intatto per VADER."],
  ["LDA live a 10 topic", "text_clean", "Assegna topic con il modello ufficiale stabile in models/live_lda_model/."],
  ["VADER", "text_raw", "Calcola sentiment sul testo originale."],
  ["Aggregazione 12h", "Topic + sentiment", "Raggruppa volume e sentiment per topic in finestre temporali da 12 ore."],
  ["P2", "volume_factor x sentiment_factor", "Misura momentum semantico e priorita informativa."],
  ["Export dashboard", "live_*.json", "Produce JSON live separati dagli output statici legacy."],
];

const safeguards = [
  "La dashboard principale usa solo Reddit RSS, news/blog RSS e GDELT DOC API.",
  "Fonti tecnico-descrittive come NVD/CVE/CISA/vendor advisories sono escluse dal P2 principale.",
  "I vecchi dati statici non sono usati dalla dashboard live.",
  "Tutti i topic sono inclusi nel P2, anche quelli low-confidence.",
  "VADER usa solo text_raw; LDA usa text_clean.",
  "GitHub Actions esegue la pipeline alle 00:00 e 12:00 UTC.",
];

export function Methodology() {
  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Metodologia" title="Pipeline live ufficiale" description="La dashboard e alimentata dagli output gia prodotti dalla pipeline live schedulata." icon={BookOpen} />
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
        <SectionHeader eyebrow="Controlli metodologici" title="Interpretazione corretta" description="I segnali servono per prioritizzare analisi OSINT, non per dichiarare compromissioni." icon={ShieldCheck} />
        <div className="grid gap-4 lg:grid-cols-2">
          {safeguards.map((item) => (
            <div key={item} className="rounded border border-slate-800 bg-slate-950/40 p-4 text-sm leading-6 text-slate-300">{item}</div>
          ))}
        </div>
        <div className="mt-5 rounded-lg border border-cyan-300/20 bg-cyan-500/10 p-5 text-sm leading-7 text-cyan-50/90">
          <p className="mb-3 font-semibold text-cyan-100">
            La pipeline schedulata non riaddestra LDA. Il modello topic viene mantenuto stabile per rendere confrontabile il P2 nel tempo. Il retraining e una procedura separata e manuale.
          </p>
          <div className="font-mono">volume_factor = topic_volume / avg_topic_volume</div>
          <div className="font-mono">sentiment_factor = topic_sentiment_sum / avg_abs_topic_sentiment_sum</div>
          <div className="font-mono">P2 = volume_factor * sentiment_factor</div>
        </div>
      </Panel>
    </div>
  );
}
