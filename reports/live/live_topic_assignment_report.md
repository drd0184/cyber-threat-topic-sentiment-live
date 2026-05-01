# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1908 |
| Assigned rows | 1789 |
| Empty BOW rows | 119 |
| Mean dominant_topic_probability | 0.6459 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 1789 | 93.76% |
| empty_bow | 119 | 6.24% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 356 | 18.66% |
| 7 | 252 | 13.21% |
| 6 | 246 | 12.89% |
| 2 | 243 | 12.74% |
| 9 | 148 | 7.76% |
| 1 | 144 | 7.55% |
| 4 | 135 | 7.08% |
| 5 | 125 | 6.55% |
| -1 | 119 | 6.24% |
| 8 | 93 | 4.87% |
| 3 | 47 | 2.46% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
