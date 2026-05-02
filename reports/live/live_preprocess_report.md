# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2648 |
| Rows removed because text_clean is empty | 269 |
| Final rows | 2379 |
| Mean text_clean length in tokens | 45.74 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1835 | 69.30% |
| reddit_rss | 627 | 23.68% |
| news_rss | 186 | 7.02% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1566 | 65.83% |
| reddit_rss | 627 | 26.36% |
| news_rss | 186 | 7.82% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2648 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2379 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (723), security (661), cve (547), window (545), data (537), system (465), attack (417), exploitation (407), access (405), user (369), file (368), time (352), process (336), code (319), use (318), likely (318), service (300), team (295), device (289), attacker (276), using (273), exploit (271), less (269), tool (263), privilege (263), threat (246), microsoft (243), year (237), used (237), server (236)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
