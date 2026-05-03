# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2854 |
| Rows removed because text_clean is empty | 293 |
| Final rows | 2561 |
| Mean text_clean length in tokens | 44.18 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1975 | 69.20% |
| reddit_rss | 691 | 24.21% |
| news_rss | 188 | 6.59% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1682 | 65.68% |
| reddit_rss | 691 | 26.98% |
| news_rss | 188 | 7.34% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2854 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2561 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (726), security (680), data (554), window (554), cve (550), system (471), attack (422), access (411), exploitation (407), user (383), file (382), time (370), process (345), use (331), code (321), likely (318), service (304), device (304), team (302), using (286), attacker (277), exploit (272), tool (272), less (269), privilege (264), year (250), threat (246), microsoft (246), used (241), server (238)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
