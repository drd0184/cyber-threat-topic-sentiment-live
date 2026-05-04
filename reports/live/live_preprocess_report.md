# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3237 |
| Rows removed because text_clean is empty | 355 |
| Final rows | 2882 |
| Mean text_clean length in tokens | 41.82 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2252 | 69.57% |
| reddit_rss | 792 | 24.47% |
| news_rss | 193 | 5.96% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1897 | 65.82% |
| reddit_rss | 792 | 27.48% |
| news_rss | 193 | 6.70% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3237 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2882 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (733), security (707), window (613), data (580), cve (553), system (484), access (437), attack (433), exploitation (410), user (400), time (399), file (399), process (358), use (350), code (331), device (321), likely (320), using (310), service (310), team (310), tool (297), attacker (281), exploit (273), less (269), privilege (265), server (265), year (262), threat (256), microsoft (255), used (253)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
