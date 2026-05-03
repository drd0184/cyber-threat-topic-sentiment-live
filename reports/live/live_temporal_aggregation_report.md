# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2723 |
| Rows used | 2490 |
| Rows discarded | 233 |
| Number of time windows | 170 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-03T12:00:00+00:00 |
| Number of topics present | 10 |
| Encoding used | utf-8 |

## First 10 Aggregated Rows

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-12-16T00:00:00+00:00 | 3 | Memory Exploitation / Buffer & Heap Bugs | high | 2 | -0.1195 | -0.0598 | 0.6143 | 2 | 1.0000 |
| 2025-12-20T12:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 1 | 0.5023 | 0.5023 | 0.5190 | 1 | 1.0000 |
| 2025-12-22T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 1 | 0.9924 | 0.9924 | 0.8098 | 2 | 0.5000 |
| 2025-12-22T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 1 | 0.2824 | 0.2824 | 0.3402 | 2 | 0.5000 |
| 2025-12-27T12:00:00+00:00 | 1 | Command Execution / Payload Delivery | high | 1 | -0.1531 | -0.1531 | 0.4662 | 1 | 1.0000 |
| 2025-12-29T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 1 | -0.9999 | -0.9999 | 0.9997 | 1 | 1.0000 |
| 2026-01-04T12:00:00+00:00 | 5 | Exploit Tooling / Metasploit / RCE | high | 1 | 0.5256 | 0.5256 | 0.9890 | 1 | 1.0000 |
| 2026-01-10T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 1 | -0.2846 | -0.2846 | 0.3866 | 1 | 1.0000 |
| 2026-01-14T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 1 | -0.9887 | -0.9887 | 0.3996 | 4 | 0.2500 |
| 2026-01-14T12:00:00+00:00 | 3 | Memory Exploitation / Buffer & Heap Bugs | high | 2 | 1.9965 | 0.9983 | 0.7734 | 4 | 0.5000 |

## Top 10 Time Window / Topic by Volume

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 56 | -1.4110 | -0.0252 | 0.5764 | 221 | 0.2534 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 51 | 3.4632 | 0.0679 | 0.5583 | 214 | 0.2383 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 42 | 6.1507 | 0.1464 | 0.5931 | 221 | 0.1900 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 42 | 8.4096 | 0.2002 | 0.5796 | 214 | 0.1963 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-05-02T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 1.2534 | 0.0313 | 0.5781 | 195 | 0.2051 |
| 2026-05-02T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 39 | 7.0127 | 0.1798 | 0.6150 | 154 | 0.2532 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | 1.3277 | 0.0349 | 0.6010 | 221 | 0.1719 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7036 | 197 | 0.1929 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -2.1253 | -0.0644 | 0.6186 | 195 | 0.1692 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 31 | -3.2452 | -0.1047 | 0.6584 | 195 | 0.1590 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 27 | -3.2352 | -0.1198 | 0.4911 | 214 | 0.1262 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 18 | -3.1602 | -0.1756 | 0.6378 | 214 | 0.0841 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6640 | 197 | 0.1320 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 494 | 19.84% |
| 6 | Security Risk / Exposure Management | medium | 372 | 14.94% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 360 | 14.46% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 344 | 13.82% |
| 9 | Ransomware / Malware / Email Campaigns | high | 199 | 7.99% |
| 1 | Command Execution / Payload Delivery | high | 195 | 7.83% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 171 | 6.87% |
| 4 | Access Control / Process & API Abuse | medium | 160 | 6.43% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 121 | 4.86% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 74 | 2.97% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
