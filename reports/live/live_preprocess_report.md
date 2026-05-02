# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2396 |
| Rows removed because text_clean is empty | 227 |
| Final rows | 2169 |
| Mean text_clean length in tokens | 48.62 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1633 | 68.16% |
| reddit_rss | 578 | 24.12% |
| news_rss | 185 | 7.72% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1406 | 64.82% |
| reddit_rss | 578 | 26.65% |
| news_rss | 185 | 8.53% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2396 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2169 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (721), security (642), window (537), cve (534), data (529), system (455), attack (412), exploitation (404), access (398), user (364), file (364), time (342), process (335), likely (318), code (311), use (311), service (291), device (289), team (284), attacker (273), exploit (271), using (268), less (268), privilege (262), tool (253), threat (245), used (236), microsoft (236), year (230), server (228)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
