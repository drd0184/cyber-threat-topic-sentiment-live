# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1723 |
| Assigned rows | 1630 |
| Empty BOW rows | 93 |
| Mean dominant_topic_probability | 0.6607 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 1630 | 94.60% |
| empty_bow | 93 | 5.40% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 324 | 18.80% |
| 7 | 225 | 13.06% |
| 2 | 225 | 13.06% |
| 6 | 225 | 13.06% |
| 9 | 139 | 8.07% |
| 1 | 124 | 7.20% |
| 4 | 123 | 7.14% |
| 5 | 114 | 6.62% |
| -1 | 93 | 5.40% |
| 8 | 86 | 4.99% |
| 3 | 45 | 2.61% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
