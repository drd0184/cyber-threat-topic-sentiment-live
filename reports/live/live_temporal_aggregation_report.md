# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2882 |
| Rows used | 2635 |
| Rows discarded | 247 |
| Number of time windows | 171 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-04T00:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 59 | -2.1400 | -0.0363 | 0.5738 | 221 | 0.2670 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 51 | 3.4632 | 0.0679 | 0.5657 | 214 | 0.2383 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 42 | -10.6871 | -0.2545 | 0.6599 | 195 | 0.2154 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 7.2040 | 0.1801 | 0.5925 | 221 | 0.1810 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 39 | 7.8433 | 0.2011 | 0.5920 | 214 | 0.1822 |
| 2026-05-02T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 38 | 6.1685 | 0.1623 | 0.6149 | 154 | 0.2468 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7036 | 196 | 0.1939 |
| 2026-05-02T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 36 | 0.6675 | 0.0185 | 0.5880 | 194 | 0.1856 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 36 | 1.8639 | 0.0518 | 0.6128 | 221 | 0.1629 |
| 2026-05-02T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 33 | -0.1751 | -0.0053 | 0.6255 | 194 | 0.1701 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 42 | -10.6871 | -0.2545 | 0.6599 | 195 | 0.2154 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 18 | -3.1602 | -0.1756 | 0.6256 | 214 | 0.0841 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 31 | -2.9857 | -0.0963 | 0.4946 | 214 | 0.1449 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 25 | -2.9172 | -0.1167 | 0.6647 | 196 | 0.1276 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 30 | -2.6552 | -0.0885 | 0.6706 | 194 | 0.1546 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 22 | -2.6086 | -0.1186 | 0.6923 | 122 | 0.1803 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 23 | -2.5968 | -0.1129 | 0.7512 | 122 | 0.1885 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 527 | 20.00% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 389 | 14.76% |
| 6 | Security Risk / Exposure Management | medium | 382 | 14.50% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 368 | 13.97% |
| 1 | Command Execution / Payload Delivery | high | 208 | 7.89% |
| 9 | Ransomware / Malware / Email Campaigns | high | 208 | 7.89% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 179 | 6.79% |
| 4 | Access Control / Process & API Abuse | medium | 174 | 6.60% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 123 | 4.67% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 77 | 2.92% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
