# Live VADER Sentiment Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 2882 |
| Output rows | 2882 |
| Mean vader_compound | -0.0216 |
| Min vader_compound | -0.9999 |
| Max vader_compound | 0.9999 |
| Encoding used | utf-8 |

## Sentiment Class Distribution

| sentiment_class | rows | percent_dataset |
| --- | --- | --- |
| neutral | 1135 | 39.38% |
| negative | 975 | 33.83% |
| positive | 772 | 26.79% |

## Sentiment Class by Source Type

| source_type | sentiment_class | rows |
| --- | --- | --- |
| news_api | neutral | 990 |
| news_api | negative | 588 |
| news_api | positive | 319 |
| news_rss | negative | 130 |
| news_rss | positive | 57 |
| news_rss | neutral | 6 |
| reddit_rss | positive | 396 |
| reddit_rss | negative | 257 |
| reddit_rss | neutral | 139 |

## Sentiment Class by Analysis Role

| analysis_role | sentiment_class | rows |
| --- | --- | --- |
| p2_primary_source | neutral | 1135 |
| p2_primary_source | negative | 975 |
| p2_primary_source | positive | 772 |

## Sentiment Class by Topic

| dominant_topic | topic_label | sentiment_class | rows |
| --- | --- | --- | --- |
| -1 | Unassigned / Empty BoW | neutral | 233 |
| -1 | Unassigned / Empty BoW | negative | 13 |
| -1 | Unassigned / Empty BoW | positive | 1 |
| 0 | Network Attacks / Device Access | negative | 244 |
| 0 | Network Attacks / Device Access | neutral | 145 |
| 0 | Network Attacks / Device Access | positive | 138 |
| 1 | Command Execution / Payload Delivery | neutral | 76 |
| 1 | Command Execution / Payload Delivery | positive | 67 |
| 1 | Command Execution / Payload Delivery | negative | 65 |
| 2 | Cybercrime / Fraud / Law Enforcement | negative | 139 |
| 2 | Cybercrime / Fraud / Law Enforcement | neutral | 139 |
| 2 | Cybercrime / Fraud / Law Enforcement | positive | 90 |
| 3 | Memory Exploitation / Buffer & Heap Bugs | negative | 28 |
| 3 | Memory Exploitation / Buffer & Heap Bugs | positive | 26 |
| 3 | Memory Exploitation / Buffer & Heap Bugs | neutral | 23 |
| 4 | Access Control / Process & API Abuse | negative | 83 |
| 4 | Access Control / Process & API Abuse | positive | 51 |
| 4 | Access Control / Process & API Abuse | neutral | 40 |
| 5 | Exploit Tooling / Metasploit / RCE | neutral | 95 |
| 5 | Exploit Tooling / Metasploit / RCE | negative | 54 |
| 5 | Exploit Tooling / Metasploit / RCE | positive | 30 |
| 6 | Security Risk / Exposure Management | positive | 174 |
| 6 | Security Risk / Exposure Management | negative | 120 |
| 6 | Security Risk / Exposure Management | neutral | 88 |
| 7 | Cybersecurity Tools / Generic Discussion | neutral | 139 |
| 7 | Cybersecurity Tools / Generic Discussion | negative | 125 |
| 7 | Cybersecurity Tools / Generic Discussion | positive | 125 |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | negative | 47 |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | neutral | 46 |
| 8 | Microsoft / Privilege Escalation / Patch Exploitation | positive | 30 |
| 9 | Ransomware / Malware / Email Campaigns | neutral | 111 |
| 9 | Ransomware / Malware / Email Campaigns | negative | 57 |
| 9 | Ransomware / Malware / Email Campaigns | positive | 40 |

## Top 10 Most Negative Texts

| id | created_at | source_type | topic_label | vader_compound | title |
| --- | --- | --- | --- | --- | --- |
| blt6be9cec698ae1713 | 2026-04-14T21:48:16Z | news_rss | Microsoft / Privilege Escalation / Patch Exploitation | -0.9999 | Patch Tuesday - April 2026 |
| t3_1pyfmdx | 2025-12-29T07:08:37Z | reddit_rss | Cybercrime / Fraud / Law Enforcement | -0.9999 | Information about how/where to report Internet crimes |
| https://projectzero.google/2025/12/thinking-outside-the-box | 2025-12-16T09:00:00Z | news_rss | Memory Exploitation / Buffer & Heap Bugs | -0.9989 | Thinking Outside The Box [dusted off draft from 2017] |
| https://krebsonsecurity.com/?p=73470 | 2026-04-21T14:53:59Z | news_rss | Network Attacks / Device Access | -0.9982 | ‘Scattered Spider’ Member ‘Tylerb’ Pleads Guilty |
| https://krebsonsecurity.com/?p=73488 | 2026-04-30T14:04:26Z | news_rss | Network Attacks / Device Access | -0.9979 | Anti-DDoS Firm Heaped Attacks on Brazilian ISPs |
| 69e62568645a220001422bae | 2026-04-21T10:00:29Z | news_rss | Command Execution / Payload Delivery | -0.9978 | Bad Apples: Weaponizing native macOS primitives for movement and execution |
| https://krebsonsecurity.com/?p=73368 | 2026-03-23T15:43:04Z | news_rss | Access Control / Process & API Abuse | -0.9970 | ‘CanisterWorm’ Springs Wiper Attack Targeting Iran |
| 69ef666bd2ad2b00012dca72 | 2026-04-28T13:23:20Z | news_rss | Network Attacks / Device Access | -0.9955 | Five defender priorities from the Talos Year in Review |
| blt5b539d98d5e0f97e | 2026-04-08T13:39:52Z | news_rss | Network Attacks / Device Access | -0.9952 | FortiGate CVE-2025-59718 Exploitation: Incident Response Findings |
| 69ef6227d2ad2b00012dca41 | 2026-04-29T10:00:42Z | news_rss | Command Execution / Payload Delivery | -0.9902 | AI-powered honeypots: Turning the tables on malicious AI agents |

## Top 10 Most Positive Texts

| id | created_at | source_type | topic_label | vader_compound | title |
| --- | --- | --- | --- | --- | --- |
| https://projectzero.google/2026/26/windows-administrator-protection | 2026-01-26T08:00:00Z | news_rss | Memory Exploitation / Buffer & Heap Bugs | 0.9999 | Bypassing Windows Administrator Protection |
| https://projectzero.google/2026/01/0-click-android-part1 | 2026-01-14T17:59:00Z | news_rss | Memory Exploitation / Buffer & Heap Bugs | 0.9999 | A 0-click exploit chain for the Pixel 9 Part 1: Decoding Dolby |
| blt76d15aecf237782c | 2026-04-15T12:37:00Z | news_rss | Security Risk / Exposure Management | 0.9998 | A Clearer Path from Prioritized Exposures to Remediation Progress |
| blt067c529962c6a487 | 2026-04-28T08:00:00Z | news_rss | Security Risk / Exposure Management | 0.9997 | MDR Selection is a Partnership Decision |
| https://projectzero.google/2026/02/windows-administrator-protection | 2026-02-26T08:00:00Z | news_rss | Access Control / Process & API Abuse | 0.9996 | A Deep Dive into the GetProcessHandleFromHwnd API |
| bltc6b62f52a9995f21 | 2026-04-20T16:20:32Z | news_rss | Security Risk / Exposure Management | 0.9996 | Project Glasswing and the Next Challenge for Defenders: Turning Faster Discovery into Faster Action |
| bltf188bfe7ed9149dc | 2026-04-23T13:25:47Z | news_rss | Security Risk / Exposure Management | 0.9994 | AI is Changing Vulnerability Discovery and your Software Supply Chain Strategy has to Change with it |
| blt71ca5e4ec0fd2ade | 2026-04-29T23:00:00Z | news_rss | Security Risk / Exposure Management | 0.9991 | Five Things we Took Away from Gartner SRM Sydney 2026 |
| https://projectzero.google/2026/03/mutational-grammar-fuzzing | 2026-03-05T08:00:00Z | news_rss | Memory Exploitation / Buffer & Heap Bugs | 0.9990 | On the Effectiveness of Mutational Grammar Fuzzing |
| blt4666ae2fff340632 | 2026-04-21T13:58:29Z | news_rss | Security Risk / Exposure Management | 0.9988 | From Bulk Export to AI-ready Security Workflows: Introducing Rapid7’s Open-Source MCP Server and Agent Skill |

## Methodological Note

VADER viene applicato a text_raw perche il testo grezzo conserva punteggiatura, maiuscole, negazioni e segnali espressivi utili alla sentiment analysis. text_clean resta riservato al topic assignment.
