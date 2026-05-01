# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2097 |
| Rows removed because text_clean is empty | 189 |
| Final rows | 1908 |
| Mean text_clean length in tokens | 51.45 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1427 | 68.05% |
| reddit_rss | 496 | 23.65% |
| news_rss | 174 | 8.30% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1238 | 64.88% |
| reddit_rss | 496 | 26.00% |
| news_rss | 174 | 9.12% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2097 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1908 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (715), security (610), cve (529), window (521), data (494), system (445), attack (405), exploitation (404), access (385), file (352), user (339), process (325), likely (312), time (310), code (301), use (286), attacker (271), service (271), team (269), device (267), exploit (265), less (262), privilege (257), using (244), tool (241), threat (239), used (227), microsoft (227), elevation (210), server (209)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
