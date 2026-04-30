# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1491 |
| Assigned rows | 1413 |
| Empty BOW rows | 78 |
| Mean dominant_topic_probability | 0.6771 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 1413 | 94.77% |
| empty_bow | 78 | 5.23% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 261 | 17.51% |
| 7 | 203 | 13.62% |
| 6 | 190 | 12.74% |
| 2 | 185 | 12.41% |
| 9 | 124 | 8.32% |
| 4 | 113 | 7.58% |
| 1 | 111 | 7.44% |
| 5 | 108 | 7.24% |
| 8 | 80 | 5.37% |
| -1 | 78 | 5.23% |
| 3 | 38 | 2.55% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
