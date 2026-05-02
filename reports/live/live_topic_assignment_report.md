# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2379 |
| Assigned rows | 2207 |
| Empty BOW rows | 172 |
| Mean dominant_topic_probability | 0.6201 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2207 | 92.77% |
| empty_bow | 172 | 7.23% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 445 | 18.71% |
| 6 | 324 | 13.62% |
| 7 | 308 | 12.95% |
| 2 | 301 | 12.65% |
| 9 | 178 | 7.48% |
| 1 | 177 | 7.44% |
| -1 | 172 | 7.23% |
| 5 | 151 | 6.35% |
| 4 | 149 | 6.26% |
| 8 | 112 | 4.71% |
| 3 | 62 | 2.61% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
