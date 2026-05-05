# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3913 |
| Rows removed: text_length < 30 | 116 |
| Rows removed: url_ratio > 0.20 | 32 |
| Final rows | 3765 |
| Percent kept | 96.22% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2745 | 70.15% |
| reddit_rss | 948 | 24.23% |
| news_rss | 220 | 5.62% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2629 | 69.83% |
| reddit_rss | 925 | 24.57% |
| news_rss | 211 | 5.60% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3913 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3765 | 100.00% |
