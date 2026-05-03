# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2561 |
| Assigned rows | 2363 |
| Empty BOW rows | 198 |
| Mean dominant_topic_probability | 0.6108 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2363 | 92.27% |
| empty_bow | 198 | 7.73% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 475 | 18.55% |
| 6 | 345 | 13.47% |
| 7 | 342 | 13.35% |
| 2 | 322 | 12.57% |
| -1 | 198 | 7.73% |
| 9 | 192 | 7.50% |
| 1 | 188 | 7.34% |
| 5 | 159 | 6.21% |
| 4 | 153 | 5.97% |
| 8 | 115 | 4.49% |
| 3 | 72 | 2.81% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
