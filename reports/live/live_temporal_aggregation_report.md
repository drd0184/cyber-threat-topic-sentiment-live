# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2379 |
| Rows used | 2207 |
| Rows discarded | 172 |
| Number of time windows | 168 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-02T12:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 57 | -1.4110 | -0.0248 | 0.5721 | 221 | 0.2579 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 51 | 2.9693 | 0.0582 | 0.5662 | 214 | 0.2383 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 41 | 6.1507 | 0.1500 | 0.5920 | 221 | 0.1855 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 39 | 8.6772 | 0.2225 | 0.5891 | 214 | 0.1822 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7036 | 197 | 0.1929 |
| 2026-05-02T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 38 | 0.6675 | 0.0176 | 0.5890 | 198 | 0.1919 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 37 | 1.3277 | 0.0359 | 0.6080 | 221 | 0.1674 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 33 | -2.1253 | -0.0644 | 0.6186 | 195 | 0.1692 |
| 2026-05-02T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 33 | 0.6172 | 0.0187 | 0.6384 | 198 | 0.1667 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -10.0444 | -0.2450 | 0.6620 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 32 | -3.7373 | -0.1168 | 0.6540 | 198 | 0.1616 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 18 | -3.1602 | -0.1756 | 0.6256 | 214 | 0.0841 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 29 | -3.0089 | -0.1038 | 0.5064 | 214 | 0.1355 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-05-01T00:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 13 | -2.5181 | -0.1937 | 0.6427 | 195 | 0.0667 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 445 | 20.16% |
| 6 | Security Risk / Exposure Management | medium | 324 | 14.68% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 308 | 13.96% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 301 | 13.64% |
| 9 | Ransomware / Malware / Email Campaigns | high | 178 | 8.07% |
| 1 | Command Execution / Payload Delivery | high | 177 | 8.02% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 151 | 6.84% |
| 4 | Access Control / Process & API Abuse | medium | 149 | 6.75% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 112 | 5.07% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 62 | 2.81% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
