# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2561 |
| Rows used | 2363 |
| Rows discarded | 198 |
| Number of time windows | 169 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-03T00:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 54 | -1.4882 | -0.0276 | 0.5682 | 221 | 0.2443 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 52 | 2.9693 | 0.0571 | 0.5683 | 214 | 0.2430 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.6871 | -0.2607 | 0.6633 | 195 | 0.2103 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 41 | 6.4689 | 0.1578 | 0.5963 | 221 | 0.1855 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 8.9035 | 0.2226 | 0.5814 | 214 | 0.1869 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 39 | 1.3277 | 0.0340 | 0.6032 | 221 | 0.1765 |
| 2026-05-02T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 39 | 1.1813 | 0.0303 | 0.5889 | 195 | 0.2000 |
| 2026-05-02T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 38 | 5.4777 | 0.1442 | 0.6007 | 152 | 0.2500 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7036 | 197 | 0.1929 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -3.4873 | -0.1057 | 0.6552 | 195 | 0.1692 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.6871 | -0.2607 | 0.6633 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -3.4873 | -0.1057 | 0.6552 | 195 | 0.1692 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 27 | -3.2352 | -0.1198 | 0.4940 | 214 | 0.1262 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 19 | -3.1602 | -0.1663 | 0.6392 | 214 | 0.0888 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 22 | -2.6086 | -0.1186 | 0.6923 | 122 | 0.1803 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 23 | -2.5968 | -0.1129 | 0.7512 | 122 | 0.1885 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-05-01T00:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 13 | -2.5181 | -0.1937 | 0.6426 | 195 | 0.0667 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 475 | 20.10% |
| 6 | Security Risk / Exposure Management | medium | 345 | 14.60% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 342 | 14.47% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 322 | 13.63% |
| 9 | Ransomware / Malware / Email Campaigns | high | 192 | 8.13% |
| 1 | Command Execution / Payload Delivery | high | 188 | 7.96% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 159 | 6.73% |
| 4 | Access Control / Process & API Abuse | medium | 153 | 6.47% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 115 | 4.87% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 72 | 3.05% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
