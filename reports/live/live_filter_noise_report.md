# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1707 |
| Rows removed: text_length < 30 | 56 |
| Rows removed: url_ratio > 0.20 | 19 |
| Final rows | 1632 |
| Percent kept | 95.61% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1158 | 67.84% |
| reddit_rss | 387 | 22.67% |
| news_rss | 162 | 9.49% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1102 | 67.52% |
| reddit_rss | 374 | 22.92% |
| news_rss | 156 | 9.56% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1707 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1632 | 100.00% |
