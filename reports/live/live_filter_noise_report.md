# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2491 |
| Rows removed: text_length < 30 | 73 |
| Rows removed: url_ratio > 0.20 | 22 |
| Final rows | 2396 |
| Percent kept | 96.19% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1706 | 68.49% |
| reddit_rss | 593 | 23.81% |
| news_rss | 192 | 7.71% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1633 | 68.16% |
| reddit_rss | 578 | 24.12% |
| news_rss | 185 | 7.72% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2491 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2396 | 100.00% |
