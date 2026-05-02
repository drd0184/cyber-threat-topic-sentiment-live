# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2749 |
| Rows removed: text_length < 30 | 78 |
| Rows removed: url_ratio > 0.20 | 23 |
| Final rows | 2648 |
| Percent kept | 96.33% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1913 | 69.59% |
| reddit_rss | 643 | 23.39% |
| news_rss | 193 | 7.02% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1835 | 69.30% |
| reddit_rss | 627 | 23.68% |
| news_rss | 186 | 7.02% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2749 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2648 | 100.00% |
