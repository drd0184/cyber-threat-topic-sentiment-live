# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2169 |
| Rows used | 2030 |
| Rows discarded | 139 |
| Number of time windows | 167 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-02T00:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 56 | -2.2233 | -0.0397 | 0.5645 | 221 | 0.2534 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 52 | 3.2895 | 0.0633 | 0.5493 | 207 | 0.2512 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 8.9035 | 0.2226 | 0.5847 | 207 | 0.1932 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 39 | 7.2040 | 0.1847 | 0.5930 | 221 | 0.1765 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 39 | 1.3277 | 0.0340 | 0.6032 | 221 | 0.1765 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7096 | 197 | 0.1929 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -2.1253 | -0.0644 | 0.6186 | 195 | 0.1692 |
| 2026-05-01T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 31 | 2.4985 | 0.0806 | 0.5580 | 207 | 0.1498 |
| 2026-05-01T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 30 | 1.0160 | 0.0339 | 0.5993 | 195 | 0.1538 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 28 | -3.2120 | -0.1147 | 0.4911 | 207 | 0.1353 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 26 | -3.0703 | -0.1181 | 0.6640 | 197 | 0.1320 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 14 | -2.8420 | -0.2030 | 0.6117 | 207 | 0.0676 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-05-01T00:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 13 | -2.5181 | -0.1937 | 0.6198 | 195 | 0.0667 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 410 | 20.20% |
| 6 | Security Risk / Exposure Management | medium | 299 | 14.73% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 284 | 13.99% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 275 | 13.55% |
| 1 | Command Execution / Payload Delivery | high | 163 | 8.03% |
| 9 | Ransomware / Malware / Email Campaigns | high | 163 | 8.03% |
| 4 | Access Control / Process & API Abuse | medium | 140 | 6.90% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 139 | 6.85% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 104 | 5.12% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 53 | 2.61% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
