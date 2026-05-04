# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3482 |
| Rows removed because text_clean is empty | 386 |
| Final rows | 3096 |
| Mean text_clean length in tokens | 40.5 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2414 | 69.33% |
| reddit_rss | 866 | 24.87% |
| news_rss | 202 | 5.80% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2028 | 65.50% |
| reddit_rss | 866 | 27.97% |
| news_rss | 202 | 6.52% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3482 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3096 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (739), security (726), window (631), data (613), cve (557), system (491), access (447), attack (440), user (426), time (412), exploitation (410), file (410), use (365), process (363), code (337), device (326), using (323), likely (321), team (315), service (314), tool (308), server (290), attacker (281), year (277), exploit (277), microsoft (274), less (271), privilege (266), threat (261), used (260)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
