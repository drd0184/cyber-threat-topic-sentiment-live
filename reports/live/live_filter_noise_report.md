# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 2960 |
| Rows removed: text_length < 30 | 82 |
| Rows removed: url_ratio > 0.20 | 24 |
| Final rows | 2854 |
| Percent kept | 96.42% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2057 | 69.49% |
| reddit_rss | 708 | 23.92% |
| news_rss | 195 | 6.59% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1975 | 69.20% |
| reddit_rss | 691 | 24.21% |
| news_rss | 188 | 6.59% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2960 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 2854 | 100.00% |
