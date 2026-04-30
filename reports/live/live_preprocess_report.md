# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1632 |
| Rows removed because text_clean is empty | 141 |
| Final rows | 1491 |
| Mean text_clean length in tokens | 58.27 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1102 | 67.52% |
| reddit_rss | 374 | 22.92% |
| news_rss | 156 | 9.56% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 961 | 64.45% |
| reddit_rss | 374 | 25.08% |
| news_rss | 156 | 10.46% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1632 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1491 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (703), security (543), cve (520), window (496), data (451), system (402), exploitation (397), attack (361), access (353), process (317), file (312), likely (304), user (293), code (288), time (276), exploit (259), attacker (257), less (253), privilege (252), use (248), device (248), service (243), team (235), threat (225), using (223), used (211), microsoft (210), tool (205), elevation (204), payload (203)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
