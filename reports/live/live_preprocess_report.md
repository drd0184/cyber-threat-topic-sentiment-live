# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3047 |
| Rows removed because text_clean is empty | 324 |
| Final rows | 2723 |
| Mean text_clean length in tokens | 42.67 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2122 | 69.64% |
| reddit_rss | 736 | 24.15% |
| news_rss | 189 | 6.20% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1798 | 66.03% |
| reddit_rss | 736 | 27.03% |
| news_rss | 189 | 6.94% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3047 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2723 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (730), security (691), window (564), data (563), cve (552), system (477), attack (424), access (424), exploitation (409), file (390), user (386), time (386), process (346), use (340), code (327), likely (319), device (315), team (309), service (304), using (293), tool (287), attacker (279), exploit (272), less (269), privilege (265), year (253), threat (251), microsoft (248), used (245), server (242)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
