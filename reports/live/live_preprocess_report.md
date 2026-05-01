# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1895 |
| Rows removed because text_clean is empty | 172 |
| Final rows | 1723 |
| Mean text_clean length in tokens | 54.41 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1284 | 67.76% |
| reddit_rss | 444 | 23.43% |
| news_rss | 167 | 8.81% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1112 | 64.54% |
| reddit_rss | 444 | 25.77% |
| news_rss | 167 | 9.69% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1895 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1723 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (710), security (586), cve (524), window (513), data (480), system (429), exploitation (402), attack (392), access (378), file (333), process (323), user (322), likely (311), code (300), time (296), use (271), attacker (268), exploit (261), team (261), device (260), service (259), less (258), privilege (255), using (238), threat (234), tool (225), used (224), microsoft (219), elevation (210), payload (204)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
