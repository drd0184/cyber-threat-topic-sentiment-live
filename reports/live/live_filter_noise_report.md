# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3358 |
| Rows removed: text_length < 30 | 94 |
| Rows removed: url_ratio > 0.20 | 27 |
| Final rows | 3237 |
| Percent kept | 96.40% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2346 | 69.86% |
| reddit_rss | 811 | 24.15% |
| news_rss | 201 | 5.99% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2252 | 69.57% |
| reddit_rss | 792 | 24.47% |
| news_rss | 193 | 5.96% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3358 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3237 | 100.00% |
