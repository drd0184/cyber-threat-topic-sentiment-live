# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1491 |
| Rows used | 1413 |
| Rows discarded | 78 |
| Number of time windows | 164 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-04-30T12:00:00+00:00 |
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
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 37 | -1.7577 | -0.0475 | 0.7089 | 196 | 0.1888 |
| 2026-04-30T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 29 | -1.1010 | -0.0380 | 0.6861 | 196 | 0.1480 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6640 | 196 | 0.1327 |
| 2026-04-30T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 26 | 3.4465 | 0.1326 | 0.5952 | 196 | 0.1327 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 23 | -2.5968 | -0.1129 | 0.7512 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 22 | -2.6086 | -0.1186 | 0.6923 | 122 | 0.1803 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 19 | -0.9745 | -0.0513 | 0.6793 | 122 | 0.1557 |
| 2026-04-29T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 19 | 0.3710 | 0.0195 | 0.6898 | 92 | 0.2065 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 18 | 0.6451 | 0.0358 | 0.6329 | 69 | 0.2609 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6640 | 196 | 0.1327 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 22 | -2.6086 | -0.1186 | 0.6923 | 122 | 0.1803 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 23 | -2.5968 | -0.1129 | 0.7512 | 122 | 0.1885 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-04-23T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 7 | -2.2713 | -0.3245 | 0.6878 | 31 | 0.2258 |
| 2026-02-11T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 3 | -2.0961 | -0.6987 | 0.9441 | 10 | 0.3000 |
| 2026-04-08T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 7 | -2.0801 | -0.2972 | 0.7761 | 9 | 0.7778 |
| 2026-04-29T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 13 | -2.0573 | -0.1583 | 0.7261 | 92 | 0.1413 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 261 | 18.47% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 203 | 14.37% |
| 6 | Security Risk / Exposure Management | medium | 190 | 13.45% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 185 | 13.09% |
| 9 | Ransomware / Malware / Email Campaigns | high | 124 | 8.78% |
| 4 | Access Control / Process & API Abuse | medium | 113 | 8.00% |
| 1 | Command Execution / Payload Delivery | high | 111 | 7.86% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 108 | 7.64% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 80 | 5.66% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 38 | 2.69% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
