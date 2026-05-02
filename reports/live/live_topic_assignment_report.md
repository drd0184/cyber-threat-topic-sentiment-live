# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2169 |
| Assigned rows | 2030 |
| Empty BOW rows | 139 |
| Mean dominant_topic_probability | 0.6309 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2030 | 93.59% |
| empty_bow | 139 | 6.41% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 410 | 18.90% |
| 6 | 299 | 13.79% |
| 7 | 284 | 13.09% |
| 2 | 275 | 12.68% |
| 1 | 163 | 7.51% |
| 9 | 163 | 7.51% |
| 4 | 140 | 6.45% |
| 5 | 139 | 6.41% |
| -1 | 139 | 6.41% |
| 8 | 104 | 4.79% |
| 3 | 53 | 2.44% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
