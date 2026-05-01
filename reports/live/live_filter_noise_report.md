# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1976 |
| Rows removed: text_length < 30 | 59 |
| Rows removed: url_ratio > 0.20 | 22 |
| Final rows | 1895 |
| Percent kept | 95.90% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1343 | 67.97% |
| reddit_rss | 459 | 23.23% |
| news_rss | 174 | 8.81% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1284 | 67.76% |
| reddit_rss | 444 | 23.43% |
| news_rss | 167 | 8.81% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1976 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1895 | 100.00% |
