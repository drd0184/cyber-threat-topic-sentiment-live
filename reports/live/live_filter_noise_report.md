# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 3158 |
| Rows removed: text_length < 30 | 86 |
| Rows removed: url_ratio > 0.20 | 25 |
| Final rows | 3047 |
| Percent kept | 96.49% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2208 | 69.92% |
| reddit_rss | 754 | 23.88% |
| news_rss | 196 | 6.21% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2122 | 69.64% |
| reddit_rss | 736 | 24.15% |
| news_rss | 189 | 6.20% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3158 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 3047 | 100.00% |
