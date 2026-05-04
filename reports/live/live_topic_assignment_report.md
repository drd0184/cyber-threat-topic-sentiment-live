# Live LDA Topic Assignment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 3096 |
| Assigned rows | 2819 |
| Empty BOW rows | 277 |
| Mean dominant_topic_probability | 0.5918 |
| Min dominant_topic_probability | 0.0000 |
| Max dominant_topic_probability | 0.9999 |
| Encoding used | utf-8 |
| Model | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/lda_model.gensim |
| Dictionary | /home/runner/work/cyber-threat-topic-sentiment-live/cyber-threat-topic-sentiment-live/models/live_lda_model/dictionary.gensim |

## Topic Assignment Status

| topic_assignment_status | rows | percent_dataset |
| --- | --- | --- |
| assigned | 2819 | 91.05% |
| empty_bow | 277 | 8.95% |

## Dominant Topic Distribution

| dominant_topic | rows | percent_dataset |
| --- | --- | --- |
| 0 | 567 | 18.31% |
| 7 | 410 | 13.24% |
| 2 | 405 | 13.08% |
| 6 | 405 | 13.08% |
| -1 | 277 | 8.95% |
| 1 | 223 | 7.20% |
| 9 | 212 | 6.85% |
| 5 | 201 | 6.49% |
| 4 | 179 | 5.78% |
| 8 | 135 | 4.36% |
| 3 | 82 | 2.65% |

## Methodological Note

Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. I documenti social/news recenti vengono proiettati sullo spazio topic salvato in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato.
