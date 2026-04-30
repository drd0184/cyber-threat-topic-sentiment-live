# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1078 |
| Rows used | 1036 |
| Rows discarded | 42 |
| Number of time windows | 162 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-04-30T00:00:00+00:00 |
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
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 30 | -2.9738 | -0.0991 | 0.7368 | 130 | 0.2308 |
| 2026-04-30T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 21 | 1.6078 | 0.0766 | 0.6771 | 130 | 0.1615 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 17 | -1.8931 | -0.1114 | 0.8099 | 80 | 0.2125 |
| 2026-04-29T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 17 | 5.4273 | 0.3193 | 0.7180 | 58 | 0.2931 |
| 2026-04-30T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 14 | 2.3245 | 0.1660 | 0.5590 | 130 | 0.1077 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 14 | -1.8659 | -0.1333 | 0.6739 | 62 | 0.2258 |
| 2026-04-30T00:00:00+00:00 | 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 11 | 0.7989 | 0.0726 | 0.6438 | 130 | 0.0846 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 11 | -1.4203 | -0.1291 | 0.7437 | 130 | 0.0846 |
| 2026-04-30T00:00:00+00:00 | 1 | Command Execution / Payload Delivery | high | 11 | -0.0923 | -0.0084 | 0.6177 | 130 | 0.0846 |
| 2026-04-29T12:00:00+00:00 | 1 | Command Execution / Payload Delivery | high | 11 | -2.0048 | -0.1823 | 0.5702 | 80 | 0.1375 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 5 | -4.1810 | -0.8362 | 0.7383 | 18 | 0.2778 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 30 | -2.9738 | -0.0991 | 0.7368 | 130 | 0.2308 |
| 2026-04-29T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 6 | -2.2354 | -0.3726 | 0.8030 | 58 | 0.1034 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 6 | -2.1178 | -0.3530 | 0.7931 | 14 | 0.4286 |
| 2026-02-11T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 3 | -2.0961 | -0.6987 | 0.9441 | 10 | 0.3000 |
| 2026-04-29T12:00:00+00:00 | 1 | Command Execution / Payload Delivery | high | 11 | -2.0048 | -0.1823 | 0.5702 | 80 | 0.1375 |
| 2026-04-03T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 5 | -1.9933 | -0.3987 | 0.6739 | 8 | 0.6250 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 17 | -1.8931 | -0.1114 | 0.8099 | 80 | 0.2125 |
| 2026-04-21T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 3 | -1.8885 | -0.6295 | 0.5576 | 18 | 0.1667 |
| 2026-04-23T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -1.8694 | -0.3116 | 0.7019 | 26 | 0.2308 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 176 | 16.99% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 151 | 14.58% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 136 | 13.13% |
| 9 | Ransomware / Malware / Email Campaigns | high | 103 | 9.94% |
| 6 | Security Risk / Exposure Management | medium | 100 | 9.65% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 99 | 9.56% |
| 4 | Access Control / Process & API Abuse | medium | 88 | 8.49% |
| 1 | Command Execution / Payload Delivery | high | 86 | 8.30% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 69 | 6.66% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 28 | 2.70% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
