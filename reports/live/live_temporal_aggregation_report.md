# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 3348 |
| Rows used | 3036 |
| Rows discarded | 312 |
| Number of time windows | 173 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-05T00:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 55 | -0.5519 | -0.0100 | 0.5755 | 221 | 0.2489 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 49 | 2.9088 | 0.0594 | 0.5682 | 213 | 0.2300 |
| 2026-05-04T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 46 | -1.4753 | -0.0321 | 0.5757 | 209 | 0.2201 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 44 | 6.6930 | 0.1521 | 0.5871 | 221 | 0.1991 |
| 2026-05-04T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 42 | -0.9874 | -0.0235 | 0.5824 | 138 | 0.3043 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 40 | -10.8186 | -0.2705 | 0.6574 | 195 | 0.2051 |
| 2026-05-02T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 38 | 6.1685 | 0.1623 | 0.6160 | 153 | 0.2484 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 38 | 7.8433 | 0.2064 | 0.5773 | 213 | 0.1784 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7036 | 196 | 0.1939 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 37 | 1.3277 | 0.0359 | 0.6076 | 221 | 0.1674 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 40 | -10.8186 | -0.2705 | 0.6574 | 195 | 0.2051 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-05T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 14 | -3.7203 | -0.2657 | 0.6058 | 78 | 0.1795 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 31 | -3.3973 | -0.1096 | 0.6577 | 193 | 0.1606 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 19 | -3.1602 | -0.1663 | 0.6392 | 213 | 0.0892 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 31 | -2.9857 | -0.0963 | 0.4946 | 213 | 0.1455 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 25 | -2.9172 | -0.1167 | 0.6646 | 196 | 0.1276 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6805 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 620 | 20.42% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 449 | 14.79% |
| 6 | Security Risk / Exposure Management | medium | 445 | 14.66% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 432 | 14.23% |
| 1 | Command Execution / Payload Delivery | high | 237 | 7.81% |
| 9 | Ransomware / Malware / Email Campaigns | high | 223 | 7.35% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 210 | 6.92% |
| 4 | Access Control / Process & API Abuse | medium | 196 | 6.46% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 140 | 4.61% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 84 | 2.77% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
