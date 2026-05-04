# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3616 |
| Rows removed: text_length < 30 | 105 |
| Rows removed: url_ratio > 0.20 | 29 |
| Final rows | 3482 |
| Percent kept | 96.29% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2519 | 69.66% |
| reddit_rss | 887 | 24.53% |
| news_rss | 210 | 5.81% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2414 | 69.33% |
| reddit_rss | 866 | 24.87% |
| news_rss | 202 | 5.80% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3616 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3482 | 100.00% |
