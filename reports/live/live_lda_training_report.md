# Live LDA Training Report

## Summary

| Metric | Value |
| --- | --- |
| Input rows | 1078 |
| Rows used | 1078 |
| Vocabulary size | 3464 |
| Configurations tested | 8, 10, 12, 15 |
| Selected num_topics | 10 |
| Selected coherence c_v | 0.5082 |
| Encoding used | utf-8 |

## Coherence by Configuration

| num_topics | coherence_cv |
| --- | --- |
| 8 | 0.4321 |
| 10 | 0.5082 |
| 12 | 0.5203 |
| 15 | 0.4837 |

## Selection Rationale

La configurazione con coherence piu alta e 12 topic, ma la differenza rispetto a 10 topic e 0.0121, inferiore alla soglia 0.02; selezionati 10 topic per interpretabilita.

## Final Topics

| topic_id | top_words |
| --- | --- |
| 0 | attack, attacker, device, system, said, network, user, data, address, access, security, hacker |
| 1 | file, system, command, attacker, payload, window, code, figure, script, agent, execution, using |
| 2 | phone, crime, fraud, use, reward, law, year, federal, police, group, help, online |
| 3 | pointer, buffer, write, heap, payload, data, dynamic, exploit, object, process, call, skip |
| 4 | access, process, attack, adversary, window, security, api, handle, system, target, used, check |
| 5 | module, code, exploit, request, update, add, metasploit, cve, digicat, rce, user, pull |
| 6 | security, team, data, risk, vulnerability, exposure, environment, remediation, model, time, organization, attack |
| 7 | job, version, tool, year, exploit, cpanel, cybersecurity, list, security, user, actually, data |
| 8 | vulnerability, cve, exploitation, window, likely, less, privilege, elevation, microsoft, service, remote, code |
| 9 | file, window, ransomware, platform, email, encryption, talos, figure, system, malware, ddos, example |

## Document Distribution by Topic

| dominant_topic | docs_assigned | percent_docs |
| --- | --- | --- |
| -1 | 42 | 3.90% |
| 0 | 175 | 16.23% |
| 1 | 87 | 8.07% |
| 2 | 137 | 12.71% |
| 3 | 28 | 2.60% |
| 4 | 87 | 8.07% |
| 5 | 99 | 9.18% |
| 6 | 99 | 9.18% |
| 7 | 153 | 14.19% |
| 8 | 69 | 6.40% |
| 9 | 102 | 9.46% |

## Source Type Distribution by Topic (Ex Post)

| dominant_topic | source_type | rows |
| --- | --- | --- |
| 0 | news_api | 104 |
| 0 | reddit_rss | 42 |
| 0 | news_rss | 29 |
| 1 | reddit_rss | 47 |
| 1 | news_api | 26 |
| 1 | news_rss | 14 |
| 2 | news_api | 96 |
| 2 | reddit_rss | 35 |
| 2 | news_rss | 6 |
| 3 | reddit_rss | 15 |
| 3 | news_rss | 7 |
| 3 | news_api | 6 |
| 4 | news_api | 43 |
| 4 | reddit_rss | 27 |
| 4 | news_rss | 17 |
| 5 | news_api | 48 |
| 5 | reddit_rss | 38 |
| 5 | news_rss | 13 |
| 6 | news_api | 44 |
| 6 | reddit_rss | 32 |
| 6 | news_rss | 23 |
| 7 | reddit_rss | 72 |
| 7 | news_api | 65 |
| 7 | news_rss | 16 |
| 8 | news_api | 37 |
| 8 | news_rss | 19 |
| 8 | reddit_rss | 13 |
| 9 | news_api | 70 |
| 9 | reddit_rss | 24 |
| 9 | news_rss | 8 |

## Methodological Note

Questo modello LDA live è addestrato esclusivamente su fonti social/news recenti. Il vecchio LDA statico non viene usato per assegnare topic nella pipeline live principale.
