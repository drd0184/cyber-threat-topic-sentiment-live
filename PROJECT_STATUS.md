# Cyber Threat Topic & Sentiment Analysis - Project Status

## Stato corrente - versione live

Questa cartella e la copia live/online del progetto `cyber-threat-topic-sentiment`.
Deriva dalla baseline statica, ma da ora deve essere trattata come ambiente per dati recenti e raccolte periodiche.

I vecchi CSV statici in `data/raw/` e `data/processed/`, i report generati e i vecchi JSON della dashboard non sono dataset live. Restano solo come baseline storica/metodologica finche non viene confermata una rimozione o archiviazione esplicita.

Struttura live da usare per i nuovi dati:

- `data/live/raw/`
- `data/live/processed/`
- `data/live/archive/`
- `config/`

## 1. Obiettivo del progetto

Il progetto implementa una pipeline NLP ispirata al paper su Reddit/Bitcoin, riadattata al dominio cybersecurity, per identificare hot topic cyber combinando:

- topic modeling;
- sentiment analysis;
- aggregazione temporale;
- indice P2 basato su volume e sentiment.

La baseline statica e gia stata usata per validare la pipeline end-to-end. La fase corrente deve sostituire quella sorgente con raccolta live/online da fonti pubbliche recenti.

## 1b. Live Pipeline Plan

La versione live dovra implementare questa sequenza:

1. Raccolta dati da RSS cyber news.
2. Raccolta da Reddit RSS per subreddit cyber/security selezionati.
3. Raccolta da NVD/CISA per vulnerabilita, advisory e known exploited vulnerabilities.
4. Normalizzazione in uno schema comune con campi minimi come `id`, `source`, `source_type`, `created_at`, `title`, `text_raw`, `url`, `tags`, `cve_ids`.
5. Preprocessing del testo per topic assignment, mantenendo `text_raw` intatto per VADER.
6. Topic assignment usando il modello/topic mapping confermato o una futura strategia live approvata.
7. Sentiment analysis con VADER su `text_raw`.
8. Aggregazione su finestre da 12h.
9. Calcolo indice P2.
10. Export dashboard in JSON live, separato dagli output statici legacy.

Aggiornamento raccolta live:

- Fonti Reddit RSS ampliate: `cybersecurity`, `netsec`, `blueteamsec`, `Malware`, `ransomware`, `hacking`, `AskNetsec`, `sysadmin`, `privacy`, `ReverseEngineering`, `osint`, `ComputerSecurity`.
- Fonti news/blog RSS ampliate: The Hacker News, BleepingComputer, KrebsOnSecurity, SANS Internet Storm Center, Cisco Talos Blog, Google Project Zero, Microsoft Security Response Center, Mandiant Blog, Rapid7 Blog, Unit 42.
- GDELT DOC API aggiunta come fonte `news_api` gratuita senza API key per ampliare il corpus social/news recente.
- NVD CVE API 2.0 resta documentata in configurazione, ma e disabilitata per il ramo P2 live e non viene usata per il consolidamento social/news.
- Motivazione: ridurre lo sbilanciamento del dataset live verso CVE/NVD e aumentare segnali recenti provenienti da discussioni pubbliche e fonti editoriali cyber.
- Se una fonte RSS/API fallisce, il collector deve registrare un warning e continuare con le altre fonti.

Correzione metodologica P2 live:

- La pipeline P2 live replica/adatta il paper su fonti social/news, quindi il calcolo P2 deve usare solo fonti social/news: `reddit_rss`, `news_rss`, `news_api` ed eventuali `social_news_api`.
- NVD/CVE e stato disabilitato in `config/live_sources.yml` per il ramo P2 con la nota: `Disabled for P2 replication: CVE/NVD is technical context, not social/news sentiment.`
- I record CVE/NVD gia presenti nel raw live non vengono cancellati: restano in `data/live/raw/live_items_raw.csv` come possibile estensione futura o contesto tecnico separato.
- CVE/NVD non contribuisce piu a sentiment, aggregazione temporale, P2, CYBERCON o dashboard live P2.
- Motivazione: le descrizioni NVD/CVE sono testi tecnico-standardizzati e lessicalmente orientati al rischio; usarli con VADER altera il sentiment e puo generare picchi P2 artificiali.

Step live implementati:

- `scripts/00_collect_live_sources.py`: raccoglie fonti live pubbliche e aggiorna `data/live/raw/live_items_raw.csv`, senza modificare dataset statici.
- `scripts/00_collect_live_sources.py`: ora supporta anche `gdelt_doc_api`, normalizzando articoli GDELT nello schema comune e deduplicando incrementalmente su `id` e `url`.
- `scripts/00b_inspect_live_dataset.py`: ispeziona qualita e distribuzione del raw live, generando report in `reports/live/`.
- `scripts/01_prepare_live_sentiment_dataset.py`: crea `data/live/processed/01_live_sentiment_dataset.csv`, privilegiando social/news e limitando CVE/NVD come contesto tecnico.
- `scripts/01_prepare_live_social_news_dataset.py`: crea `data/live/processed/01_live_social_news_dataset.csv`, usando solo `reddit_rss`, `news_rss`, `news_api` e `social_news_api` come fonti primarie P2 ed escludendo CVE/NVD.
- `scripts/02_live_filter_noise.py`: crea `data/live/processed/02_live_filtered_dataset.csv`, rimuovendo solo record troppo corti o dominati da URL e preservando `text_raw`.
- `scripts/03_live_preprocess_text.py`: crea `data/live/processed/03_live_preprocessed_dataset.csv`, preservando `text_raw` per VADER e aggiungendo `text_clean` per topic modeling/topic assignment.
- `scripts/03b_live_corpus_quality_check.py`: valuta la qualita del corpus social/news preprocessato prima di un eventuale nuovo LDA live, generando report e campioni in `reports/live/`.
- `scripts/04_live_train_lda_baseline.py`: addestra un nuovo modello LDA live da zero sul corpus social/news recente, confrontando 8/10/12/15 topic e salvando il modello in `models/live_lda_model/`.
- `scripts/04b_live_topic_interpretation_helper.py`: genera tabella e report di supporto per interpretare manualmente i topic LDA live.
- `scripts/04c_live_lda_tuning_experiments.py`: esegue esperimenti LDA non distruttivi su unigram/bigram/trigram e griglia di iperparametri, salvando solo report sperimentali in `reports/live/`.
- `scripts/04c_apply_live_topic_labels.py`: applica le label manuali ufficiali e la confidenza ai 10 topic LDA live, senza modificare il modello.
- `scripts/04_live_assign_topics_existing_lda.py`: crea `data/live/processed/04_live_topics_dataset.csv`, assegnando topic ai documenti live con il modello LDA statico gia addestrato, senza riaddestrare o modificare i modelli.
- `scripts/05_live_sentiment_vader.py`: crea `data/live/processed/05_live_sentiment_dataset.csv`, applicando VADER solo a `text_raw` e preservando tutte le colonne gia presenti.
- `scripts/06_live_temporal_aggregation.py`: crea `data/live/processed/06_live_temporal_aggregation_12h.csv`, aggregando topic e sentiment live su finestre temporali da 12 ore.
- `scripts/07_live_compute_p2_index.py`: crea `data/live/processed/07_live_p2_index_12h.csv`, calcolando P2 live da volume e sentiment aggregati.
- `scripts/08_live_inspect_corrected_p2_hotspot.py`: ispeziona il principale hot topic negativo del P2 live corretto social/news-only e salva report/documenti in `reports/live/`.

Nota di coerenza: il ramo live P2 corretto parte da `01_live_social_news_dataset.csv`. Gli step live `01`, `02` e `03` non eseguono LDA, topic assignment, VADER, P2 o dashboard export. Preparano soltanto il dataset live per le analisi successive. Lo step live `04_live_train_lda_baseline.py` addestra il modello LDA live ufficiale su `text_clean`; `04c_apply_live_topic_labels.py` applica solo label manuali e confidenza. Lo step live `05` esegue solo VADER su `text_raw`. Lo step live `06` esegue solo aggregazione temporale. Lo step live `07` calcola solo P2 live; non ricalcola LDA/VADER e non esporta la dashboard.

Aggiornamento consolidamento social/news con GDELT:

- `config/live_sources.yml` include `gdelt_doc_api` abilitato con `source_type: news_api`, `max_records_per_keyword: 50` e keyword cyber threat.
- Reddit resta raccolto solo via RSS; non e stata integrata Reddit API.
- La raccolta GDELT usa GDELT DOC API in modalita `ArtList`/JSON con sort `DateDesc`, timeout/retry e pausa tra keyword per ridurre rate limit.
- Lo step `01_prepare_live_social_news_dataset.py` include ora `reddit_rss`, `news_rss`, `news_api` e `social_news_api`, escludendo ogni altra fonte.
- Non sono stati eseguiti addestramento LDA live, VADER, P2 o modifiche dashboard in questo consolidamento.

## 2. Dataset legacy statico

Questa sezione documenta la baseline storica. Non descrive il dataset live corrente.

Dataset CSV statico di contenuti cyber/social in `data/raw/tweets_final.csv`, con colonne simili a:

`_id`, `date`, `id`, `relevant`, `text`, `tweet`, `type`, `watson`, `annotation`, `urls`.

Uso delle colonne:

- `text` viene usato come testo grezzo;
- `date` viene usato come timestamp;
- `type`, `annotation` e `relevant` NON sono usati come feature;
- `type`, `annotation` e `relevant` sono conservati solo come metadata per controllo qualitativo ex post.

## 3. Struttura cartelle

- `data/raw/`
- `data/processed/`
- `data/live/raw/`
- `data/live/processed/`
- `data/live/archive/`
- `config/`
- `models/lda_model/`
- `scripts/`
- `reports/`
- `reports/figures/`
- `reports/tables/`
- `notebooks/`

## 4. Pipeline completata

Tutti gli script sotto sono stati creati e verificati nella sessione corrente.

| Script | Input | Output | Scopo | Colonne principali prodotte |
|---|---|---|---|---|
| `scripts/01_normalize_dataset.py` | `data/raw/tweets_final.csv` | `data/processed/01_static_dataset_normalized.csv` | Normalizza il CSV raw in uno schema stabile. | `id`, `source`, `created_at`, `text_raw`, `original_type`, `annotation`, `relevant`, `urls` |
| `scripts/02_filter_noise.py` | `data/processed/01_static_dataset_normalized.csv` | `data/processed/02_filtered_dataset.csv` | Rimuove testi troppo corti e post dominati da URL. | `text_length`, `url_chars`, `url_ratio` |
| `scripts/03_preprocess_text.py` | `data/processed/02_filtered_dataset.csv` | `data/processed/03_preprocessed_dataset.csv` | Crea testo pulito per LDA con stopwords, domain stopwords e lemmatizzazione. | `text_clean` |
| `scripts/03b_filter_cyber_relevance.py` | `data/processed/03_preprocessed_dataset.csv` | `data/processed/03b_cyber_relevant_dataset.csv` | Filtra record cyber rilevanti usando solo keyword lessicali su `text_clean`, senza label manuali. | `cyber_keyword_matches` |
| `scripts/04_topic_modeling_lda.py` | `data/processed/03b_cyber_relevant_dataset.csv` | `data/processed/04_lda_topics_dataset.csv`, `data/processed/04_lda_topic_words.csv`, `models/lda_model/` | Addestra LDA finale ufficiale con `num_topics=10`. | `dominant_topic`, `dominant_topic_probability`, tabella `topic_id`/`top_words` |
| `scripts/04b_compare_lda_configs.py` | `data/processed/03b_cyber_relevant_dataset.csv` | `data/processed/04b_lda_config_comparison.csv` | Confronta configurazioni LDA con 8, 10, 12 e 15 topic. | `num_topics`, `topic_id`, `top_words`, `docs_assigned`, `percent_docs`, metadata ex post dominanti |
| `scripts/05_sentiment_vader.py` | `data/processed/04_lda_topics_dataset.csv` | `data/processed/05_sentiment_dataset.csv` | Applica VADER a `text_raw`, non a `text_clean`. | `vader_neg`, `vader_neu`, `vader_pos`, `vader_compound`, `sentiment_class` |
| `scripts/06_temporal_aggregation.py` | `data/processed/05_sentiment_dataset.csv` | `data/processed/06_temporal_aggregation_12h.csv` | Aggrega volume e sentiment per topic su finestre da 12 ore. | `time_window`, `topic_volume`, `topic_sentiment_sum`, `topic_sentiment_mean`, `avg_topic_probability`, `total_window_volume`, `topic_volume_share` |
| `scripts/07_compute_p2_index.py` | `data/processed/06_temporal_aggregation_12h.csv` | `data/processed/07_p2_index_12h.csv` | Calcola indice P2 da volume aggregato e sentiment aggregato. | `avg_topic_volume`, `avg_abs_topic_sentiment_sum`, `volume_factor`, `sentiment_factor`, `p2_index`, `p2_abs`, `p2_direction` |
| `scripts/08_visualize_p2_results.py` | `data/processed/07_p2_index_12h.csv`, `data/processed/04_lda_topic_words.csv` | `reports/figures/p2_timeseries_by_topic.png`, `reports/figures/top_negative_hot_topics.png`, `reports/figures/topic_volume_timeseries.png`, `reports/tables/top_p2_hot_topics.csv` | Genera visualizzazioni statiche PNG e tabella degli hot topics P2. | Grafici P2/volume e tabella ordinata per `p2_abs` |
| `scripts/09_generate_dashboard.py` | `data/processed/07_p2_index_12h.csv`, `data/processed/04_lda_topic_words.csv`, opzionale `data/processed/05_sentiment_dataset.csv` | `reports/dashboard.html` | Genera dashboard HTML statica interattiva. | Dashboard con overview, topic, P2, hot topics, volume, sentiment e tabella P2 |
| `scripts/10_quality_assessment.py` | `data/processed/04_lda_topics_dataset.csv`, `data/processed/04_lda_topic_words.csv`, `data/processed/07_p2_index_12h.csv`, `data/processed/05_sentiment_dataset.csv` | `reports/tables/topic_quality_assessment.csv`, `reports/tables/p2_hot_topics_quality.csv`, `reports/tables/p2_vs_volume_vs_sentiment.csv` | Valuta qualitativamente topic LDA e hot topic P2 usando label originali solo ex post. | Quality score topic, distribuzioni annotation/type per hot topic, confronto P2-volume-sentiment |
| `scripts/11_export_dashboard_data.py` | `data/processed/07_p2_index_12h.csv`, `data/processed/05_sentiment_dataset.csv`, `data/processed/04_lda_topic_words.csv` | `dashboard/src/data/p2.json`, `dashboard/src/data/posts.json`, `dashboard/src/data/topics.json`, `dashboard/src/data/summary.json` | Esporta dati puliti per una dashboard React interattiva. | JSON con `topic_label`, topic words, post con finestra 12h, summary e hot topic principali |

## 5. Risultati numerici principali

- Dataset normalizzato: 21368 righe.
- Dopo filtro rumore: 14155 righe.
- Dopo preprocessing testo: 14097 righe.
- Dopo filtro cyber relevance: 10252 righe.

LDA finale:

- documenti usati: 10252;
- vocabolario: 2877;
- `num_topics`: 10.

VADER:

- righe finali: 10252;
- media `vader_compound`: -0.0494;
- min `vader_compound`: -0.9515;
- max `vader_compound`: 0.9714;
- negative: 5040;
- positive: 3339;
- neutral: 1873.

Aggregazione temporale:

- righe input: 10252;
- righe aggregate: 167;
- finestre temporali: 18;
- range: 2018-08-30 12:00:00+00:00 -> 2018-09-12 00:00:00+00:00;
- topic presenti: 10.

P2:

- righe input: 167;
- topic: 10;
- finestre temporali: 18;
- righe output: 167;
- hot topic negativo piu forte: 2018-09-06 12:00:00+00:00, topic 4, `p2_index = -31.6853`;
- hot topic positivo piu forte: 2018-09-07 12:00:00+00:00, topic 0, `p2_index = 6.3828`.

## 6. Decisioni metodologiche

- `text_raw` viene conservato intatto per VADER.
- `text_clean` viene usato per LDA.
- Il filtro cyber relevance usa keyword su `text_clean`, non label manuali.
- `original_type`, `annotation` e `relevant` non entrano mai nei modelli o nei calcoli.
- LDA usa solo `text_clean`.
- VADER usa solo `text_raw`.
- P2 usa solo volume aggregato e sentiment aggregato.
- `num_topics=10` e stato scelto dopo confronto con 8, 10, 12 e 15 topic per miglior compromesso tra interpretabilita e granularita.

## 7. Topic LDA finali

I topic finali provengono da `data/processed/04_lda_topic_words.csv`.

Mappa interpretativa manuale ufficiale:

```python
TOPIC_LABELS = {
    0: "Generic Vulnerability Signals",
    1: "Data Leak / Botnet / Cloud",
    2: "DDoS / Attack Protection",
    3: "CVE / Remote Exploit / Buffer Overflow",
    4: "Ransomware / Malware / Attacks",
    5: "SQL Injection / DoS / Microsoft",
    6: "Ransomware / Business Risk / WannaCry",
    7: "Zero-day / Browser Exploit Signals",
    8: "CVE / Patch / RSA BSAFE",
    9: "Cybersecurity / IoT / Botnet",
}
```

Queste label sono interpretazioni manuali basate sulle `top_words` LDA, non label usate dal modello.

| topic_id | Label manuale ufficiale | top_words |
|---:|---|---|
| 0 | Generic Vulnerability Signals | vulnerability, security, website, team, courage, thank, story, management, notify, obb |
| 1 | Data Leak / Botnet / Cloud | north, data, email, technology, botnet, keep, vulnerability, well, leak, cloud |
| 2 | DDoS / Attack Protection | ddos, attack, protection, site, first, scripting, functionality, cross, server, video |
| 3 | CVE / Remote Exploit / Buffer Overflow | cve, discovered, campaign, remote, buffer, overflow, exploit, business, vuln, based |
| 4 | Ransomware / Malware / Attacks | ransomware, cybersecurity, attack, hacker, via, hack, target, malware, contain, threat |
| 5 | SQL Injection / DoS / Microsoft | vulnerability, service, denial, injection, sql, security, cve, exists, microsoft, exploitable |
| 6 | Ransomware / Business Risk / WannaCry | ransomware, cyber, attack, vulnerability, risk, business, cybersecurity, wannacry, korean, key |
| 7 | Zero-day / Browser Exploit Signals | vulnerability, window, time, exploit, daytoday, really, economy, zero, browser, emotional |
| 8 | CVE / Patch / RSA BSAFE | vulnerability, cve, version, prior, rsa, file, bsafe, patch, contains, bug |
| 9 | Cybersecurity / IoT / Botnet | cybersecurity, infosec, security, vulnerability, iot, botnet, infographic, patch, latest, corruption |

## 8. Dashboard HTML

Stato attuale:

- `scripts/09_generate_dashboard.py` genera `reports/dashboard.html`;
- la dashboard e stata riscritta con stile piu pulito tipo OSINT/intelligence monitor, ispirato concettualmente a `pizzint.watch`;
- la dashboard deve essere locale, statica, navigabile e apribile nel browser;
- la dashboard non deve ricalcolare la pipeline, ma leggere gli output gia generati.

Input principali dashboard:

- `data/processed/07_p2_index_12h.csv`;
- `data/processed/04_lda_topic_words.csv`;
- `data/processed/05_sentiment_dataset.csv`, se utile.

## 9. Export dati per dashboard React

Stato attuale:

- `scripts/11_export_dashboard_data.py` esporta JSON puliti per una dashboard React interattiva;
- legge solo output gia generati dalla pipeline;
- non usa `original_type`, `annotation` o `relevant` per i calcoli;
- aggiunge `topic_label` tramite la mappa manuale dei topic;
- calcola `time_window` dei post con floor a 12 ore;
- limita `text_raw` esportato a 500 caratteri;
- limita `posts.json` a 5000 post ad alta rilevanza, privilegiando sentiment forte e topic probability alta;
- esporta gli `id` dei post come stringhe per evitare perdita di precisione in JavaScript;
- esporta `top_words` in `topics.json` come lista di parole;
- aggiunge metadata topic `category`, `icon` e `accent` per la UI.

Output generati:

- `dashboard/src/data/p2.json`: 167 record P2 con label topic, top words e topic quality;
- `dashboard/src/data/posts.json`: 5000 post con sentiment, topic, finestra 12h e testo troncato;
- `dashboard/src/data/topics.json`: 10 topic arricchiti con top words, quality, metriche P2, sentiment e metadata UI;
- `dashboard/src/data/summary.json`: statistiche globali, hot topic negativo e positivo, sentiment medio;
- `dashboard/src/data/topic_quality.json`: 10 record di quality assessment topic;
- `dashboard/src/data/hot_topics_quality.json`: 10 record di validazione ex post degli hot topic P2 negativi;
- `dashboard/src/data/validation.json`: 30 record di confronto tra ranking per volume, sentiment e P2.
- `dashboard/src/data/p2_hot_topics_quality.json` e `dashboard/src/data/p2_validation.json`: copie legacy aggiornate con gli stessi dati puliti.

Risultati export:

- total posts esportati: 5000;
- total topics: 10;
- total time windows: 18;
- hottest negative: topic 4, `Ransomware / Malware / Attacks`, `p2_index = -31.6853`;
- hottest positive: topic 0, `Generic Vulnerability Signals`, `p2_index = 6.3828`.

## 10. Quality assessment ex post

Stato attuale:

- `scripts/10_quality_assessment.py` valuta qualitativamente topic LDA e hot topic P2;
- usa `original_type`, `annotation` e `relevant` solo come controllo ex post, non per ricalcolare modelli o P2;
- produce tabelle di supporto alla relazione finale.

Output generati:

- `reports/tables/topic_quality_assessment.csv`;
- `reports/tables/p2_hot_topics_quality.csv`;
- `reports/tables/p2_vs_volume_vs_sentiment.csv`.

Risultati principali:

- topic quality counts: high = 4, medium = 5, low = 1;
- topic piu affidabili: T3 `CVE / Remote Exploit / Buffer Overflow`, T8 `CVE / Patch / RSA BSAFE`, T2 `DDoS / Attack Protection`, T5 `SQL Injection / DoS / Microsoft`, T4 `Ransomware / Malware / Attacks`;
- topic da leggere con cautela: T6 `Ransomware / Business Risk / WannaCry`, T7 `Zero-day / Browser Exploit Signals`, T0 `Generic Vulnerability Signals`;
- principale hot topic P2 negativo: T4 `Ransomware / Malware / Attacks`;
- threat_pct sul principale hot topic negativo: 17.1%. Il segnale P2 va interpretato come priorita informativa, non come conferma di attacco.

## 11. Dashboard React interattiva

Stato attuale:

- e stata rifattorizzata una web app React locale nella cartella `dashboard/`;
- tecnologie configurate: Vite, React, Tailwind CSS, Recharts, lucide-react;
- la dashboard legge direttamente i JSON locali in `dashboard/src/data/`;
- non richiede backend;
- avvio previsto da `dashboard/` con `npm install` e `npm run dev`.

File principali:

- `dashboard/package.json`;
- `dashboard/index.html`;
- `dashboard/vite.config.js`;
- `dashboard/tailwind.config.js`;
- `dashboard/postcss.config.js`;
- `dashboard/src/main.jsx`;
- `dashboard/src/App.jsx`;
- `dashboard/src/styles.css`.

Architettura frontend:

- `dashboard/src/components/AppShell.jsx`;
- `dashboard/src/components/ui.jsx`;
- `dashboard/src/components/charts.jsx`;
- `dashboard/src/components/AlertCard.jsx`;
- `dashboard/src/components/TopicCard.jsx`;
- `dashboard/src/components/TopicDetailPanel.jsx`;
- `dashboard/src/pages/Overview.jsx`;
- `dashboard/src/pages/Alerts.jsx`;
- `dashboard/src/pages/TopicExplorer.jsx`;
- `dashboard/src/pages/Quality.jsx`;
- `dashboard/src/pages/Methodology.jsx`;
- `dashboard/src/pages/DataConsole.jsx`;
- `dashboard/src/utils/data.js`;
- `dashboard/src/utils/formatters.js`.

Funzionalita implementate:

- UI revisionata con impostazione cyber threat intelligence / OSINT monitoring, dark, pulita e meno decorativa;
- topic label ufficiali in inglese applicate a script, JSON e dashboard React;
- rimossa la status bar inutile e rimossi badge/testi di finta console dalla home;
- sidebar semplificata con `Panoramica`, `Allarmi`, `Esplora Topic`, `Qualita e affidabilita`, `Metodologia`, `Console dati`;
- main status section con titolo `INDICE CYBER DI HOT TOPIC`, sottotitolo `Semantic Intelligence Monitor` e nota sul limite interpretativo;
- sostituito il vecchio gauge CYBERCON con `dashboard/src/components/CyberconScale.jsx`, scala orizzontale 1-5 senza archi, tachimetri o elementi circolari;
- aggiunto box `Che cos'e CYBERCON?` con spiegazione non matematica in home e legenda sintetica CYBERCON 1-5;
- fix dei badge confidence tramite classe `confidence-badge`: `MEDIUM CONFIDENCE` resta su una sola riga in Allarmi, Esplora Topic, Dettaglio Topic e Qualita;
- alert principale con Topic, finestra temporale, P2, volume, sentiment, confidenza e bottone `Analizza alert`;
- `Analizza alert` apre la pagina `Allarmi` con dettaglio dell'alert selezionato e filtro sul Topic;
- alert cards rese leggibili con severity, topic label, timestamp, P2, volume, sentiment, confidence e bottone `Apri alert`;
- topic cards rifatte con Topic ID, label ufficiale, badge HIGH/MEDIUM/LOW CONFIDENCE, badge `NOISY SIGNAL`, top 5 words e metriche Documents, Total volume, Max negative P2, Average sentiment, Threat %;
- `Apri dettaglio` imposta correttamente `selectedTopicId`;
- il dettaglio Topic non mostra piu T0 di default: se nessun Topic e selezionato mostra `Seleziona un topic per visualizzare il dettaglio.`;
- dettaglio Topic funzionante per tutti i Topic con P2 timeline, Volume timeline, Sentiment timeline, donut chart sentiment, post associati e alert relativi;
- ripristinata la donut chart/ciambella `Distribuzione sentiment` per Topic con conteggi, percentuali, totale post e tooltip;
- alert relativi al Topic ridisegnati come card compatte: timestamp, severity/direction, P2, Volume, Sentiment, P2 abs, frase breve e bottone `Apri alert`;
- pagina `Qualita e affidabilita` riscritta per spiegare uso ex post delle label originali, confidence e limite del P2;
- pagina `Metodologia` riscritta in italiano chiaro: LDA su `text_clean`, VADER su `text_raw`, aggregazione 12h, `P2 = volume_factor x sentiment_factor`;
- Console dati mantenuta come vista tecnica dei record P2 e degli artifact locali;
- footer unico: `Demo locale per finalita didattiche. P2 misura momentum semantico, non incidenti verificati.`

Nota metodologica dashboard:

- `original_type`, `annotation` e `relevant` non vengono usati per ricalcolare P2 o modelli;
- sono mostrati solo come validazione ex post della qualita interpretativa.

Nota ambiente:

- `scripts/11_export_dashboard_data.py` e stato eseguito correttamente;
- `scripts/10_quality_assessment.py` e stato rieseguito dopo la pulizia delle note qualita;
- la build Vite e stata verificata con successo dopo la revisione UX/UI;
- la build Vite e stata verificata con successo dopo il fix CYBERCON scale / confidence badge / donut sentiment / topic alerts;
- Vite segnala un bundle grande perche la dashboard importa JSON statici, incluso `posts.json`;
- il dev server Vite e stato avviato su `http://127.0.0.1:5173/`;
- in PowerShell puo servire `npm.cmd run build`/`npm.cmd run dev` se `npm.ps1` e bloccato dalla execution policy.

Comandi operativi:

```powershell
python scripts/11_export_dashboard_data.py
cd dashboard
npm install
npm run dev
```

## 12. Problema rilevato nella dashboard

La legenda dei topic mostrava piu topic con lo stesso nome, ad esempio `vulnerability`, perche la dashboard usava probabilmente la prima parola delle `top_words`. Questo e metodologicamente insufficiente: bisogna usare topic label manuali piu descrittive basate sulle `top_words`.

Nota operativa: `scripts/09_generate_dashboard.py` e `scripts/11_export_dashboard_data.py` usano entrambi la mappa manuale `TOPIC_LABELS`.

## 13. Prossimi step

Live pipeline corrente:

- consolidamento fonti social/news con GDELT completato con `scripts/00_collect_live_sources.py`;
- raw live totale dopo integrazione GDELT: 2603 righe;
- nuove righe aggiunte nel run riuscito: 887;
- distribuzione raw aggiornata: cve=1295, news_api=783, reddit_rss=367, news_rss=158;
- item GDELT raccolti per keyword nel run riuscito: ransomware=50, malware=50, phishing=50, data breach=50, cyber attack=50, cyberattack=50, zero-day=0, zero day=50, vulnerability=50, exploit=50, DDoS=50, botnet=50, infostealer=50, supply chain attack=50, credential theft=50, APT=50, threat actor=50;
- keyword GDELT fallita nel run riuscito: `zero-day`;
- fonti fallite nel run riuscito: `reddit_ransomware_new` HTTP 403, `microsoft_security_response_center` feed non valido, `mandiant_blog` feed non valido;
- un secondo rilancio ravvicinato del collector ha incontrato rate limit GDELT 429 ed e terminato per timeout prima di scrivere output; il raw valido resta quello del run riuscito con `collected_at` massimo 2026-04-30 10:55:06+00:00;
- config GDELT aggiornata a `sort: DateDesc` e pausa tra keyword aumentata per ridurre richieste duplicate/rate limit nei prossimi run;
- dataset P2 social/news creato con `scripts/01_prepare_live_social_news_dataset.py`;
- input: `data/live/raw/live_items_raw.csv`;
- output: `data/live/processed/01_live_social_news_dataset.csv`;
- report: `reports/live/live_social_news_dataset_report.md`;
- righe raw iniziali: 2603;
- righe social/news mantenute: 1245;
- CVE esclusi dal ramo P2: 1295;
- duplicati testuali normalizzati rimossi: 63;
- distribuzione social/news: news_api=727, reddit_rss=360, news_rss=158;
- range temporale social/news: 2025-12-16 09:00:00+00:00 -> 2026-04-30 10:52:33+00:00;
- filtro rumore live rieseguito su social/news con `scripts/02_live_filter_noise.py`;
- righe filtrate social/news: 1186;
- distribuzione filtrata: news_api=686, reddit_rss=348, news_rss=152;
- preprocessing live rieseguito su social/news con `scripts/03_live_preprocess_text.py`;
- righe preprocessate: 1078;
- distribuzione preprocessata: news_api=578, reddit_rss=348, news_rss=152;
- lunghezza media `text_clean`: 77.78 token;
- top 30 token preprocessati: vulnerability (694), cve (516), security (508), window (487), data (416), system (394), link (390), exploitation (389), comment (372), submitted (347), access (340), attack (338), process (316), file (305), likely (303), user (279), code (277), time (262), attacker (254), exploit (254), privilege (251), less (250), device (245), use (237), service (235), team (230), using (214), threat (213), used (207), elevation (204);
- quality check corpus live completato con `scripts/03b_live_corpus_quality_check.py`;
- report quality: `reports/live/live_corpus_quality_check.md`;
- campioni quality: `reports/live/live_corpus_samples.csv`;
- campioni esportati: 60, con 20 record per `reddit_rss`, 20 per `news_rss`, 20 per `news_api`;
- warning quality: nessuna soglia attivata;
- metriche quality: `news_api`=53.62%, `reddit_rss`=32.28%, `news_rss`=14.10%; source_name maggiore `The Hacker News`=5.01%; media/mediana `text_raw`=867.89/101.00 caratteri; media/mediana `text_clean`=77.78/10.00 token;
- keyword coverage quality: cve=5.47%, vulnerability=8.44%, ransomware=4.73%, malware=8.35%, phishing=2.78%, breach=3.15%, exploit=7.05%, ddos=4.36%, botnet=0.65%, zeroday=0.00%, zero-day=1.21%, data leak=0.19%;
- LDA baseline live addestrato con `scripts/04_live_train_lda_baseline.py`;
- input LDA live: `data/live/processed/03_live_preprocessed_dataset.csv`;
- output topic dataset live: `data/live/processed/04_live_lda_topics_dataset.csv`;
- output topic words live: `data/live/processed/04_live_lda_topic_words.csv`;
- confronto configurazioni: `reports/live/live_lda_config_comparison.csv`;
- report training: `reports/live/live_lda_training_report.md`;
- modello live salvato in `models/live_lda_model/`;
- modello statico legacy in `models/lda_model/` non modificato;
- righe input/usate LDA live: 1078 / 1078;
- vocabolario LDA live: 3475;
- configurazioni testate: 8, 10, 12, 15 topic;
- coherence c_v: 8=0.4646, 10=0.4747, 12=0.4507, 15=0.4896;
- configurazione selezionata: 10 topic, perche 15 topic ha coherence maggiore ma differenza da 10 topic = 0.0149, sotto soglia 0.02;
- documenti assegnati LDA live: assigned=1040, empty_bow=38;
- distribuzione topic LDA live: T0=140, T1=105, T2=225, T3=51, T4=30, T5=68, T6=188, T7=87, T8=72, T9=74, empty_bow=-1=38;
- topic interpretation helper completato con `scripts/04b_live_topic_interpretation_helper.py`;
- tabella interpretativa: `reports/live/live_topic_interpretation_table.csv`;
- report interpretativo: `reports/live/live_topic_interpretation_report.md`;
- topic riassunti: 10, escludendo `dominant_topic = -1`;
- campi interpretativi prodotti: top words, documenti assegnati, percentuale documenti, probabilita media topic, distribuzione source_type, top 10 source_name, top 10 titoli rappresentativi, top 10 token e suggested_label preliminare;
- stopword Reddit/RSS aggiunte a `scripts/03_live_preprocess_text.py`: comment, comments, link, links, submitted, submit, post, posted, thread, subreddit, reddit, article, source, anyone, something, looking, trying;
- preprocessing rieseguito dopo stopword: righe preprocessate=1078, media `text_clean`=76.24 token;
- top 30 token aggiornati dopo stopword: vulnerability (694), cve (516), security (508), window (487), data (416), system (394), exploitation (389), access (340), attack (338), process (316), file (305), likely (303), user (279), code (277), time (262), attacker (254), exploit (254), privilege (251), less (250), device (245), use (237), service (235), team (230), using (214), threat (213), used (207), elevation (204), payload (203), microsoft (202), pointer (196);
- quality check, LDA live e topic interpretation helper rieseguiti dopo stopword;
- LDA live post-stopword: vocabolario=3464, coherence c_v 8=0.4321, 10=0.5082, 12=0.5203, 15=0.4837;
- configurazione selezionata post-stopword: 10 topic, perche 12 topic ha coherence maggiore ma differenza da 10 topic = 0.0121, sotto soglia 0.02;
- distribuzione topic LDA live post-stopword: T0=175, T1=87, T2=137, T3=28, T4=87, T5=99, T6=99, T7=153, T8=69, T9=102, empty_bow=-1=42;
- topic words finali post-stopword: T0 `attack, attacker, device, system, said, network, user, data, address, access, security, hacker`; T1 `file, system, command, attacker, payload, window, code, figure, script, agent, execution, using`; T2 `phone, crime, fraud, use, reward, law, year, federal, police, group, help, online`; T3 `pointer, buffer, write, heap, payload, data, dynamic, exploit, object, process, call, skip`; T4 `access, process, attack, adversary, window, security, api, handle, system, target, used, check`; T5 `module, code, exploit, request, update, add, metasploit, cve, digicat, rce, user, pull`; T6 `security, team, data, risk, vulnerability, exposure, environment, remediation, model, time, organization, attack`; T7 `job, version, tool, year, exploit, cpanel, cybersecurity, list, security, user, actually, data`; T8 `vulnerability, cve, exploitation, window, likely, less, privilege, elevation, microsoft, service, remote, code`; T9 `file, window, ransomware, platform, email, encryption, talos, figure, system, malware, ddos, example`;
- tuning sperimentale LDA completato con `scripts/04c_live_lda_tuning_experiments.py`;
- output tuning: `reports/live/live_lda_tuning_results.csv` e `reports/live/live_lda_tuning_report.md`;
- esperimenti tuning eseguiti: 384;
- varianti token testate: unigram, unigram+bigrams, unigram+bigrams+trigrams;
- griglia tuning: no_below=[3,5], no_above=[0.5,0.6], num_topics=[8,10,12,15], alpha=[symmetric,asymmetric], eta=[auto,symmetric], passes=[10,20], iterations=200;
- migliore coherence assoluta tuning: 0.5280, experiment_id=20, unigram, 12 topic, no_below=3, no_above=0.5, alpha=symmetric, eta=symmetric, passes=20;
- migliore configurazione bilanciata tuning: 0.5280, experiment_id=52, unigram, 12 topic, no_below=3, no_above=0.6, alpha=symmetric, eta=symmetric, passes=20, largest_topic_percent=16.31%, smallest_topic_percent=3.19%;
- target coherence 0.55 non raggiunto;
- raccomandazione tuning: non sostituire automaticamente il modello ufficiale solo per coherence; valutare interpretabilita, stabilita e utilita per P2 prima di promuovere una configurazione;
- decisione ufficiale post-tuning: mantenere il modello LDA live a 10 topic, con coherence 0.5082;
- motivazione decisione ufficiale: la configurazione a 12 topic migliora la coherence solo marginalmente, mentre aumenta frammentazione e riduce interpretabilita operativa per P2;
- target coherence 0.55 non raggiunto; migliore coherence assoluta 0.5280 su 384 configurazioni sperimentali;
- topic label ufficiali applicate con `scripts/04c_apply_live_topic_labels.py`;
- input/output label: `data/live/processed/04_live_lda_topics_dataset.csv`;
- report label: `reports/live/live_topic_labels_report.md`;
- distribuzione `topic_confidence`: medium=498, high=385, low=153, none=42;
- sentiment VADER live completato con `scripts/05_live_sentiment_vader.py`;
- input: `data/live/processed/04_live_lda_topics_dataset.csv`;
- output: `data/live/processed/05_live_sentiment_dataset.csv`;
- report: `reports/live/live_sentiment_vader_report.md`;
- righe output sentiment: 1078;
- media `vader_compound`: -0.0492;
- min/max `vader_compound`: -0.9999 / 0.9999;
- distribuzione sentiment live: negative=418, neutral=371, positive=289;
- aggregazione temporale live completata con `scripts/06_live_temporal_aggregation.py`;
- input: `data/live/processed/05_live_sentiment_dataset.csv`;
- output: `data/live/processed/06_live_temporal_aggregation_12h.csv`;
- report: `reports/live/live_temporal_aggregation_report.md`;
- righe usate: 1036;
- righe scartate: 42;
- righe aggregate: 485;
- finestre temporali: 162;
- range temporale: 2025-12-16 00:00:00+00:00 -> 2026-04-30 00:00:00+00:00;
- topic presenti: 10;
- `cve_count` aggregato nel P2 corretto: 0;
- P2 live social/news completato con `scripts/07_live_compute_p2_index.py`;
- input: `data/live/processed/06_live_temporal_aggregation_12h.csv`;
- output: `data/live/processed/07_live_p2_index_12h.csv`;
- report: `reports/live/live_p2_index_report.md`;
- righe output P2: 485;
- topic P2 presenti: 10;
- finestre temporali P2: 162;
- hot topic negativo piu forte: 2026-04-30 00:00:00+00:00, topic 7 `Cybersecurity Tools / Generic Discussion`, confidence `low`, `p2_index = -42.8092`, severity `critical`, cybercon_level 1;
- hot topic positivo piu forte: 2026-04-29 00:00:00+00:00, topic 7 `Cybersecurity Tools / Generic Discussion`, confidence `low`, `p2_index = 44.2728`, severity `critical`, cybercon_level 1;
- distribuzione severity: low=436, watch=26, elevated=13, high=7, critical=3;
- distribuzione direzione P2: negative=224, positive=139, neutral=122.

## Stato attuale pipeline live - riallineamento downstream

Decisione ufficiale:

- Il modello LDA live ufficiale resta a 10 topic.
- La coherence ufficiale del modello live a 10 topic e 0.5082.
- Il tuning sperimentale ha testato 384 configurazioni; il target 0.55 non e stato raggiunto.
- La migliore coherence assoluta ottenuta nel tuning e 0.5280, ma con configurazione a 12 topic.
- La configurazione a 12 topic non viene promossa perche il miglioramento e marginale e aumenta la frammentazione.
- La scelta ufficiale privilegia interpretabilita, stabilita e utilita per il calcolo P2.
- Non sono stati modificati `models/live_lda_model/`.
- Non e stata modificata la dashboard.

File downstream riallineati:

- `scripts/04c_apply_live_topic_labels.py`
- `scripts/05_live_sentiment_vader.py`
- `scripts/06_live_temporal_aggregation.py`
- `scripts/07_live_compute_p2_index.py`

Nota importante:

- `scripts/05_live_sentiment_vader.py` e stato corretto per usare il dataset LDA live ufficiale `04_live_lda_topics_dataset.csv`.
- Il vecchio dataset `04_live_topics_dataset.csv` non e piu l'input della pipeline VADER live principale.
- Gli script downstream consumano ora il dataset topic live corretto e preservano `topic_label` e `topic_confidence`.

### Risultati ultimo run live

Distribuzione sentiment:

- negative = 418
- neutral = 371
- positive = 289

Metriche principali:

- Media `vader_compound` = -0.0492
- Righe aggregate = 485
- Finestre temporali = 162

Hot topic negativo:

- time_window = 2026-04-30 00:00:00+00:00
- topic = 7
- label = Cybersecurity Tools / Generic Discussion
- P2 = -42.8092
- severity = critical

Hot topic positivo:

- time_window = 2026-04-29 00:00:00+00:00
- topic = 7
- label = Cybersecurity Tools / Generic Discussion
- P2 = 44.2728
- severity = critical

Distribuzione severity:

- low = 436
- watch = 26
- elevated = 13
- high = 7
- critical = 3

Top 10 P2 assoluti:

| time_window | topic | label | P2 | severity |
|---|---:|---|---:|---|
| 2026-04-29 00:00 | 7 | Cybersecurity Tools / Generic Discussion | 44.2728 | critical |
| 2026-04-30 00:00 | 7 | Cybersecurity Tools / Generic Discussion | -42.8092 | critical |
| 2026-04-30 00:00 | 2 | Cybercrime / Fraud / Law Enforcement | 37.5804 | critical |
| 2026-04-30 00:00 | 6 | Security Risk / Exposure Management | 23.7477 | high |
| 2026-04-29 12:00 | 1 | Command Execution / Payload Delivery | -18.7251 | high |
| 2026-04-29 00:00 | 0 | Network Attacks / Device Access | 17.3896 | high |
| 2026-04-28 12:00 | 0 | Network Attacks / Device Access | -16.8262 | high |
| 2026-04-29 12:00 | 9 | Ransomware / Malware / Email Campaigns | -16.2756 | high |
| 2026-04-29 12:00 | 7 | Cybersecurity Tools / Generic Discussion | -15.4428 | high |
| 2026-04-28 12:00 | 7 | Cybersecurity Tools / Generic Discussion | 15.3902 | high |

Interpretazione metodologica:

- Il modello LDA live a 10 topic resta la baseline ufficiale.
- Gli script downstream ora consumano il dataset LDA live corretto.
- Il topic 7 compare sia nel picco positivo sia nel picco negativo: non va interpretato come topic intrinsecamente positivo o negativo, perche il segno del P2 dipende dalla finestra temporale aggregata.
- La maggior parte delle finestre resta in severity `low`, mentre solo 3 finestre risultano `critical`.
- Lo stato attuale puo essere considerato una baseline live stabile.

## Scheduled Live Pipeline

Automazione implementata:

- `scripts/04_live_assign_topics_existing_live_lda.py`: assegna topic al dataset live preprocessato usando il modello LDA live ufficiale in `models/live_lda_model/`, senza riaddestrare il modello.
- `scripts/run_live_pipeline.py`: orchestratore operativo della pipeline live.
- `run_live_pipeline.bat`: launcher Windows dalla root del progetto.
- `docs/live_scheduling_windows.md`: istruzioni per configurare Windows Task Scheduler.

Sequenza operativa schedulata:

1. `scripts/00_collect_live_sources.py`
2. `scripts/00b_inspect_live_dataset.py`
3. `scripts/01_prepare_live_social_news_dataset.py`
4. `scripts/02_live_filter_noise.py`
5. `scripts/03_live_preprocess_text.py`
6. `scripts/04_live_assign_topics_existing_live_lda.py`
7. `scripts/04c_apply_live_topic_labels.py`
8. `scripts/05_live_sentiment_vader.py`
9. `scripts/06_live_temporal_aggregation.py`
10. `scripts/07_live_compute_p2_index.py`

Policy operativa:

- Il run operativo puo essere schedulato ogni 12 ore, ad esempio alle 00:00 e alle 12:00.
- Il run operativo non chiama `scripts/04_live_train_lda_baseline.py`.
- Il modello LDA live ufficiale in `models/live_lda_model/` viene usato solo per assegnare topic.
- Il retraining LDA resta manuale o periodico separato.
- La pipeline schedulata non modifica la dashboard.
- La pipeline schedulata non cancella il raw dataset.

Logging:

- I log vengono salvati in `logs/live_pipeline/`.
- Ogni run genera `logs/live_pipeline/live_pipeline_YYYYMMDD_HHMMSS.log`.
- L'ultimo run e copiato in `logs/live_pipeline/latest_run.log`.

Istruzioni Windows Task Scheduler:

- Aprire Utilita di pianificazione.
- Creare una nuova attivita.
- Aggiungere due trigger giornalieri: 00:00 e 12:00.
- Azione:
  - Programma: percorso completo a `run_live_pipeline.bat`;
  - Start in: root del progetto.
- Dopo il run, verificare `logs/live_pipeline/latest_run.log`.

Stato dei modelli e dashboard:

- `models/live_lda_model/` non e stato modificato dall'automazione.
- La dashboard non e stata modificata.

## Cloud Scheduling with GitHub Actions

Automazione cloud implementata:

- Workflow: `.github/workflows/live_pipeline.yml`
- Nome workflow: `Live Cyber Threat Pipeline`
- Trigger automatico: `0 0,12 * * *`
- Trigger manuale: `workflow_dispatch`
- Runner: `ubuntu-latest`
- Python: 3.11
- Dipendenze: `requirements.txt`
- Entry point: `python scripts/run_live_pipeline.py`

Policy cloud:

- La pipeline gira automaticamente alle 00:00 e alle 12:00 UTC.
- Non richiede il PC locale acceso.
- Usa solo fonti pubbliche social/news configurate: Reddit RSS, news/blog RSS e GDELT DOC API.
- Non usa sorgenti tecnico-descrittive come input P2.
- Non usa CVE/NVD nella pipeline live social/news.
- Non riaddestra LDA.
- Non chiama `scripts/04_live_train_lda_baseline.py`.
- Usa `models/live_lda_model/` solo per assegnare topic.
- Aggiorna dataset live, report live ed eventuali dashboard data esportati da script live dedicati.
- Non modifica la dashboard UI.

Commit automatico output:

- Il workflow configura il bot `github-actions[bot]`.
- Se gli output cambiano, esegue commit e push con messaggio `chore: update live pipeline outputs [skip ci]`.
- Se non ci sono modifiche, stampa `No changes to commit`.
- Il workflow non viene attivato da `push`, ma solo da schedule e avvio manuale, evitando loop inutili.

Documentazione:

- Setup GitHub Actions: `docs/github_actions_setup.md`
- Scheduling Windows locale: `docs/live_scheduling_windows.md`

Snapshot ispezione hotspot precedente:

- ispezione hotspot P2 corretta completata con `scripts/08_live_inspect_corrected_p2_hotspot.py`;
- input P2: `data/live/processed/07_live_p2_index_12h.csv`;
- input sentiment: `data/live/processed/05_live_sentiment_dataset.csv`;
- report: `reports/live/live_corrected_p2_hotspot_inspection.md`;
- documenti hotspot: `reports/live/live_corrected_p2_hotspot_documents.csv`;
- hotspot ispezionato: 2026-04-28 12:00:00+00:00, topic 4 `Ransomware / Malware / Attacks`, `p2_index = -24.1336`, severity `high`;
- documenti hotspot: 9;
- distribuzione fonti hotspot: reddit_rss=6, news_rss=3;
- distribuzione sentiment hotspot: negative=7, positive=2;
- media/min/max `vader_compound` hotspot: -0.4315 / -0.9532 / 0.5719;
- media `dominant_topic_probability` hotspot: 0.2838.

Prossimi step live:

1. Esportare JSON live separati dagli output statici legacy.
2. Collegare o affiancare gli output live alla dashboard senza sovrascrivere i JSON statici legacy.

Prossimi step dashboard/statici:

1. Avviare la dashboard da `dashboard/` con `npm run dev`.
2. Eventuale prossimo miglioramento: code splitting o lazy loading dei JSON per ridurre il warning sul bundle grande.
3. Iniziare relazione finale e presentazione.

## Static Baseline Snapshot

Questa sezione conserva lo snapshot della baseline statica da cui deriva questa copia live. Non descrive lo stato operativo corrente della cartella.

Stato baseline:

- pipeline completata end-to-end da dataset raw a dashboard React;
- dataset iniziale: `data/raw/tweets_final.csv`;
- righe dataset normalizzato: 21368;
- righe finali cyber rilevanti dopo filtro e preprocessing: 10252;
- LDA finale con `num_topics=10`;
- VADER applicato su `text_raw`;
- topic modeling LDA applicato su `text_clean`;
- aggregazione temporale su finestre da 12h;
- calcolo indice P2 da volume aggregato e sentiment aggregato;
- quality assessment ex post prodotto in `reports/tables/`;
- dashboard React interattiva in `dashboard/`;
- CYBERCON scale orizzontale 1-5;
- Topic explorer con topic label ufficiali in inglese;
- alert drill-down nella pagina `Allarmi`;
- donut sentiment per Topic nel dettaglio Topic;
- nota metodologica: `original_type`, `annotation` e `relevant` sono usati solo per validazione ex post, mai come feature dei modelli o del calcolo P2.

La baseline statica resta un riferimento storico e riproducibile, ma non deve essere usata come sorgente dati live.

## Live / Online Version

Questa cartella e gia la copia `cyber-threat-topic-sentiment-live`. Le modifiche live devono restare separate dalla baseline statica originale.

Proposta operativa:

- mantenere la baseline statica originale come riferimento separato;
- aggiungere collector da fonti gratuite, preferibilmente RSS, CISA e NVD;
- usare il modello LDA gia addestrato in `models/lda_model/` per assegnare Topic ai nuovi documenti social/news;
- applicare VADER sui nuovi `text_raw` social/news;
- aggregare i nuovi documenti social/news in finestre temporali incrementali;
- aggiornare i JSON live della dashboard da `data/live/processed`, escludendo CVE/NVD dal calcolo P2 e CYBERCON;
- mantenere separati dati live e output statici legacy, cosi la baseline resta confrontabile e ripristinabile.
