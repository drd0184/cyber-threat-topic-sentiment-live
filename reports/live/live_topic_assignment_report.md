# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2723 |
| Assigned rows | 2490 |
| Empty BOW rows | 233 |
| Mean dominant_topic_probability | 0.6031 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2490 | 91.44% |
| empty_bow | 233 | 8.56% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 494 | 18.14% |
| 6 | 372 | 13.66% |
| 7 | 360 | 13.22% |
| 2 | 344 | 12.63% |
| -1 | 233 | 8.56% |
| 9 | 199 | 7.31% |
| 1 | 195 | 7.16% |
| 5 | 171 | 6.28% |
| 4 | 160 | 5.88% |
| 8 | 121 | 4.44% |
| 3 | 74 | 2.72% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
