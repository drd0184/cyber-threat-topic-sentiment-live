# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3765 |
| Rows removed because text_clean is empty | 417 |
| Final rows | 3348 |
| Mean text_clean length in tokens | 38.95 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2629 | 69.83% |
| reddit_rss | 925 | 24.57% |
| news_rss | 211 | 5.60% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2212 | 66.07% |
| reddit_rss | 925 | 27.63% |
| news_rss | 211 | 6.30% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3765 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3348 | 100.00% |

## Top 30 Tokens After Preprocessing

security (765), vulnerability (741), data (650), window (638), cve (558), system (498), access (454), attack (445), user (438), time (431), file (416), exploitation (410), use (374), process (367), code (353), using (339), device (327), likely (322), team (321), service (320), tool (317), server (303), year (288), attacker (285), exploit (279), microsoft (279), used (272), less (272), privilege (266), threat (263)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
