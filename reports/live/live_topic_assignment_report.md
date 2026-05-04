# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2882 |
| Assigned rows | 2635 |
| Empty BOW rows | 247 |
| Mean dominant_topic_probability | 0.5989 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2635 | 91.43% |
| empty_bow | 247 | 8.57% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 527 | 18.29% |
| 7 | 389 | 13.50% |
| 6 | 382 | 13.25% |
| 2 | 368 | 12.77% |
| -1 | 247 | 8.57% |
| 1 | 208 | 7.22% |
| 9 | 208 | 7.22% |
| 5 | 179 | 6.21% |
| 4 | 174 | 6.04% |
| 8 | 123 | 4.27% |
| 3 | 77 | 2.67% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
