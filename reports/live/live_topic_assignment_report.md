# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1078 |
| Assigned rows | 1036 |
| Empty BOW rows | 42 |
| Mean dominant_topic_probability | 0.7051 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | C:\Users\PC Gaming\Desktop\cyber-threat-topic-sentiment-live\models\live_lda_model\lda_model.gensim |
| Dictionary | C:\Users\PC Gaming\Desktop\cyber-threat-topic-sentiment-live\models\live_lda_model\dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 1036 | 96.10% |
| empty_bow | 42 | 3.90% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 176 | 16.33% |
| 7 | 151 | 14.01% |
| 2 | 136 | 12.62% |
| 9 | 103 | 9.55% |
| 6 | 100 | 9.28% |
| 5 | 99 | 9.18% |
| 4 | 88 | 8.16% |
| 1 | 86 | 7.98% |
| 8 | 69 | 6.40% |
| -1 | 42 | 3.90% |
| 3 | 28 | 2.60% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
