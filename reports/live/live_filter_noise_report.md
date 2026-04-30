# Live Noise Filter Report

Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Initial rows | 1245 |
| Rows removed: text_length < 30 | 41 |
| Rows removed: url_ratio > 0.20 | 18 |
| Final rows | 1186 |
| Percent kept | 95.26% |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 727 | 58.39% |
| reddit_rss | 360 | 28.92% |
| news_rss | 158 | 12.69% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 686 | 57.84% |
| reddit_rss | 348 | 29.34% |
| news_rss | 152 | 12.82% |

## Analysis Role Distribution Before

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1245 | 100.00% |

## Analysis Role Distribution After

| analysis_role | rows | percent_dataset |
| --- | --- | --- |
| p2_primary_source | 1186 | 100.00% |
