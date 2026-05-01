# Live Temporal Aggregation Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1723 |
| Rows used | 1630 |
| Rows discarded | 93 |
| Number of time windows | 165 |
| Min time_window | 2025-12-16T00:00:00+00:00 |
| Max time_window | 2026-05-01T00:00:00+00:00 |
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
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 55 | -2.5724 | -0.0468 | 0.5785 | 219 | 0.2511 |
| 2026-04-30T12:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 40 | 6.9662 | 0.1742 | 0.5871 | 219 | 0.1826 |
| 2026-04-30T00:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | -1.7577 | -0.0463 | 0.7040 | 197 | 0.1929 |
| 2026-04-30T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 38 | 1.3277 | 0.0349 | 0.6010 | 219 | 0.1735 |
| 2026-04-30T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 29 | -1.1010 | -0.0380 | 0.6852 | 197 | 0.1472 |
| 2026-04-30T12:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 28 | 2.3497 | 0.0839 | 0.6467 | 219 | 0.1279 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 27 | -2.3273 | -0.0862 | 0.6564 | 197 | 0.1371 |
| 2026-04-30T00:00:00+00:00 | 6 | Security Risk / Exposure Management | medium | 25 | 2.7035 | 0.1081 | 0.6031 | 197 | 0.1269 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |

## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum

| time_window | dominant_topic | topic_label | topic_confidence | topic_volume | topic_sentiment_sum | topic_sentiment_mean | avg_topic_probability | total_window_volume | topic_volume_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-21T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 6 | -4.5210 | -0.7535 | 0.7259 | 20 | 0.3000 |
| 2026-05-01T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 19 | -3.0117 | -0.1585 | 0.6709 | 66 | 0.2879 |
| 2026-04-28T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 21 | -2.9166 | -0.1389 | 0.7056 | 89 | 0.2360 |
| 2026-04-29T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 23 | -2.6086 | -0.1134 | 0.6803 | 122 | 0.1885 |
| 2026-04-29T12:00:00+00:00 | 7 | Cybersecurity Tools / Generic Discussion | low | 22 | -2.5968 | -0.1180 | 0.7667 | 122 | 0.1803 |
| 2026-04-22T00:00:00+00:00 | 4 | Access Control / Process & API Abuse | medium | 9 | -2.5945 | -0.2883 | 0.8049 | 17 | 0.5294 |
| 2026-04-30T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 55 | -2.5724 | -0.0468 | 0.5785 | 219 | 0.2511 |
| 2026-04-30T00:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 27 | -2.3273 | -0.0862 | 0.6564 | 197 | 0.1371 |
| 2026-04-23T12:00:00+00:00 | 0 | Network Attacks / Device Access | medium | 7 | -2.2713 | -0.3245 | 0.6878 | 31 | 0.2258 |
| 2026-02-11T00:00:00+00:00 | 2 | Cybercrime / Fraud / Law Enforcement | medium | 3 | -2.0961 | -0.6987 | 0.9441 | 10 | 0.3000 |

## Total Distribution by Topic Label

| dominant_topic | topic_label | topic_confidence | topic_volume | percent_used_rows |
| --- | --- | --- | --- | --- |
| 0 | Network Attacks / Device Access | medium | 324 | 19.88% |
| 2 | Cybercrime / Fraud / Law Enforcement | medium | 225 | 13.80% |
| 7 | Cybersecurity Tools / Generic Discussion | low | 225 | 13.80% |
| 6 | Security Risk / Exposure Management | medium | 225 | 13.80% |
| 9 | Ransomware / Malware / Email Campaigns | high | 139 | 8.53% |
| 1 | Command Execution / Payload Delivery | high | 124 | 7.61% |
| 4 | Access Control / Process & API Abuse | medium | 123 | 7.55% |
| 5 | Exploit Tooling / Metasploit / RCE | high | 114 | 6.99% |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | high | 86 | 5.28% |
| 3 | Memory Exploitation / Buffer & Heap Bugs | high | 45 | 2.76% |

## Methodological Note

L’aggregazione temporale trasforma i singoli documenti live in segnali topic-level su finestre da 12 ore, combinando volume e sentiment.
