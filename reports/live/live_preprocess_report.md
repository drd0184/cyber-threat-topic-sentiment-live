# Live Preprocess Report

Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1186 |
| Rows removed because text_clean is empty | 108 |
| Final rows | 1078 |
| Mean text_clean length in tokens | 76.24 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 686 | 57.84% |
| reddit_rss | 348 | 29.34% |
| news_rss | 152 | 12.82% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 578 | 53.62% |
| reddit_rss | 348 | 32.28% |
| news_rss | 152 | 14.10% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1186 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1078 | 100.00% |

## Top 30 Tokens After Preprocessing

vulnerability (694), cve (516), security (508), window (487), data (416), system (394), exploitation (389), access (340), attack (338), process (316), file (305), likely (303), user (279), code (277), time (262), attacker (254), exploit (254), privilege (251), less (250), device (245), use (237), service (235), team (230), using (214), threat (213), used (207), elevation (204), payload (203), microsoft (202), pointer (196)

## Methodological Note

text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.
