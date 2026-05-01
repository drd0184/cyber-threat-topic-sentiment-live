# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1908 |
| Rows used | 1789 |
| Rows discarded | 119 |
| Number of time windows | 166 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-01T12:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 57 | -2.3920 | -0.0420 | 0.5697 | 220 | 0.2591 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -9.7044 | -0.2367 | 0.6722 | 195 | 0.2103 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 7.2040 | 0.1801 | 0.5925 | 220 | 0.1818 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7097 | 197 | 0.1929 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | 1.3277 | 0.0349 | 0.6052 | 220 | 0.1727 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -2.3276 | -0.0705 | 0.6207 | 195 | 0.1692 |
| 2026-04-30T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 29 | -1.1010 | -0.0380 | 0.6861 | 197 | 0.1472 |
| 2026-05-01T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 29 | 1.0160 | 0.0350 | 0.5967 | 195 | 0.1487 |
| 2026-04-30T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 27 | 2.2725 | 0.0842 | 0.6250 | 220 | 0.1227 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6630 | 197 | 0.1320 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -9.7044 | -0.2367 | 0.6722 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6630 | 197 | 0.1320 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 57 | -2.3920 | -0.0420 | 0.5697 | 220 | 0.2591 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -2.3276 | -0.0705 | 0.6207 | 195 | 0.1692 |
| 2026-04-23T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 7 | -2.2713 | -0.3245 | 0.6878 | 31 | 0.2258 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 356 | 19.90% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 252 | 14.09% |
| 6 | Security Risk / Exposure Management | medium | 246 | 13.75% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 243 | 13.58% |
| 9 | Ransomware / Malware / Email Campaigns | high | 148 | 8.27% |
| 1 | Command Execution / Payload Delivery | high | 144 | 8.05% |
| 4 | Access Control / Process & API Abuse | medium | 135 | 7.55% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 125 | 6.99% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 93 | 5.20% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 47 | 2.63% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
