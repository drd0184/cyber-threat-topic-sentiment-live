# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2181 |
| Rows removed: text_length < 30 | 62 |
| Rows removed: url_ratio > 0.20 | 22 |
| Final rows | 2097 |
| Percent kept | 96.15% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1489 | 68.27% |
| reddit_rss | 511 | 23.43% |
| news_rss | 181 | 8.30% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1427 | 68.05% |
| reddit_rss | 496 | 23.65% |
| news_rss | 174 | 8.30% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2181 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2097 | 100.00% |
