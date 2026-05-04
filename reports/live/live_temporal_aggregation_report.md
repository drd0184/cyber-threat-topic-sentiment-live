# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 3096 |
| Rows used | 2819 |
| Rows discarded | 277 |
| Number of time windows | 172 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-04T12:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 57 | -2.1461 | -0.0377 | 0.5767 | 221 | 0.2579 |
| 2026-05-01T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 52 | 3.3093 | 0.0636 | 0.5645 | 214 | 0.2430 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 41 | 7.4281 | 0.1812 | 0.5850 | 221 | 0.1855 |
| 2026-05-04T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -0.9874 | -0.0241 | 0.5889 | 138 | 0.2971 |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -11.2590 | -0.2746 | 0.6547 | 195 | 0.2103 |
| 2026-05-02T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 0.8454 | 0.0211 | 0.5781 | 193 | 0.2073 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7037 | 196 | 0.1939 |
| 2026-05-02T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 37 | 6.1685 | 0.1667 | 0.6086 | 153 | 0.2418 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 37 | 1.3277 | 0.0359 | 0.6071 | 221 | 0.1674 |
| 2026-05-01T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 37 | 8.3372 | 0.2253 | 0.5801 | 214 | 0.1729 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-01T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 41 | -11.2590 | -0.2746 | 0.6547 | 195 | 0.2103 |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-02T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 32 | -3.7373 | -0.1168 | 0.6512 | 193 | 0.1658 |
| 2026-05-01T12:00:00+00:00 | 9 | Ransomware / Malware / Email Campaigns | high | 19 | -3.1602 | -0.1663 | 0.6392 | 214 | 0.0888 |
| 2026-05-01T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 32 | -2.9857 | -0.0933 | 0.4920 | 214 | 0.1495 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 25 | -2.9172 | -0.1167 | 0.6647 | 196 | 0.1276 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6806 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 567 | 20.11% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 410 | 14.54% |
| 6 | Security Risk / Exposure Management | medium | 405 | 14.37% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 405 | 14.37% |
| 1 | Command Execution / Payload Delivery | high | 223 | 7.91% |
| 9 | Ransomware / Malware / Email Campaigns | high | 212 | 7.52% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 201 | 7.13% |
| 4 | Access Control / Process & API Abuse | medium | 179 | 6.35% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 135 | 4.79% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 82 | 2.91% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
