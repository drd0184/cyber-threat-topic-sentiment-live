# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 3348 |
| Assigned rows | 3036 |
| Empty BOW rows | 312 |
| Mean dominant_topic_probability | 0.5869 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 3036 | 90.68% |
| empty_bow | 312 | 9.32% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 620 | 18.52% |
| 7 | 449 | 13.41% |
| 6 | 445 | 13.29% |
| 2 | 432 | 12.90% |
| -1 | 312 | 9.32% |
| 1 | 237 | 7.08% |
| 9 | 223 | 6.66% |
| 5 | 210 | 6.27% |
| 4 | 196 | 5.85% |
| 8 | 140 | 4.18% |
| 3 | 84 | 2.51% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
