# Live Sentiment Dataset Report

Dataset derived from `data/live/raw/live_items_raw.csv` for later sentiment analysis. No NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export is performed here.

## Summary

| Metric | Value |
| --- | --- |
| Raw initial rows | 1716 |
| Rows after invalid removal | 1716 |
| Rows with unparsable created_at removed | 0 |
| Rows with null/empty text_raw removed | 0 |
| Normalized text duplicates removed | 25 |
| Social/news items kept | 416 |
| CVE items kept | 200 |
| CVE items excluded from analysis dataset only | 1075 |
| Final rows | 616 |
| Final CVE percent | 32.47% |
| Final created_at range | 2025-12-16T09:00:00Z -> 2026-04-29T13:41:41Z |
| MAX_CVE_ITEMS | 200 |
| MAX_CVE_SHARE | 0.33 |

## Source Type Distribution Before

| source_type | rows | percent_dataset |
| --- | --- | --- |
| cve | 1295 | 75.47% |
| reddit_rss | 277 | 16.14% |
| news_rss | 144 | 8.39% |

## Source Type Distribution After Dedup Before CVE Cap

| source_type | rows | percent_dataset |
| --- | --- | --- |
| cve | 1275 | 75.40% |
| reddit_rss | 272 | 16.09% |
| news_rss | 144 | 8.52% |

## Source Type Distribution After

| source_type | rows | percent_dataset |
| --- | --- | --- |
| reddit_rss | 272 | 44.16% |
| cve | 200 | 32.47% |
| news_rss | 144 | 23.38% |

## Methodological Note

Il raw dataset conserva tutti i record raccolti. Il sentiment dataset privilegia social/news perché il progetto è centrato sul sentiment e sul semantic momentum. I CVE/NVD sono mantenuti come contesto tecnico, ma limitati per evitare che testi standardizzati dominino l’analisi.
