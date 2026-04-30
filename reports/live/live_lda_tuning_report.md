# Live LDA Tuning Experiments

Experimental tuning report. No official live LDA model or official 04 outputs are overwritten.

## Baseline Comparison

| baseline_config | coherence_cv |
| --- | --- |
| current 10 topics | 0.5082 |
| current 12 topics | 0.5203 |

## Target

Target coherence: 0.55. Target reached: no.

## Top 10 Configurations by Coherence

| experiment_id | token_variant | num_topics | no_below | no_above | alpha | eta | passes | coherence_cv | largest_topic_percent | smallest_topic_percent | empty_bow_count | topic_words_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | unigram | 12 | 3 | 0.5 | symmetric | symmetric | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 18 | unigram | 12 | 3 | 0.5 | symmetric | auto | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 50 | unigram | 12 | 3 | 0.6 | symmetric | auto | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 52 | unigram | 12 | 3 | 0.6 | symmetric | symmetric | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 86 | unigram | 12 | 5 | 0.5 | asymmetric | auto | 20 | 0.5227 | 32.41 | 2.07 | 63 | T0: data, malware, tool, email, security, ddos, attack, code, service, platform | T1: team, security, risk, exposure, remediation, environment, vulnerability, faster, organization, time | T2: pointer, buffer, write, h... |
| 88 | unigram | 12 | 5 | 0.5 | asymmetric | symmetric | 20 | 0.5227 | 32.41 | 2.07 | 63 | T0: data, malware, tool, email, security, ddos, attack, code, service, platform | T1: team, security, risk, exposure, remediation, environment, vulnerability, faster, organization, time | T2: pointer, buffer, write, h... |
| 118 | unigram | 12 | 5 | 0.6 | asymmetric | auto | 20 | 0.5227 | 32.41 | 2.07 | 63 | T0: data, malware, tool, email, security, ddos, attack, code, service, platform | T1: team, security, risk, exposure, remediation, environment, vulnerability, faster, organization, time | T2: pointer, buffer, write, h... |
| 120 | unigram | 12 | 5 | 0.6 | asymmetric | symmetric | 20 | 0.5227 | 32.41 | 2.07 | 63 | T0: data, malware, tool, email, security, ddos, attack, code, service, platform | T1: team, security, risk, exposure, remediation, environment, vulnerability, faster, organization, time | T2: pointer, buffer, write, h... |
| 16 | unigram | 10 | 3 | 0.5 | asymmetric | symmetric | 20 | 0.5220 | 43.82 | 2.80 | 42 | T0: attack, said, data, device, threat, hacker, malware, company, system, security | T1: file, system, command, code, attacker, agent, payload, script, window, figure | T2: phone, crime, fraud, use, reward, year, fede... |
| 14 | unigram | 10 | 3 | 0.5 | asymmetric | auto | 20 | 0.5220 | 43.82 | 2.80 | 42 | T0: attack, said, data, device, threat, hacker, malware, company, system, security | T1: file, system, command, code, attacker, agent, payload, script, window, figure | T2: phone, crime, fraud, use, reward, year, fede... |

## Top 10 Balanced Configurations

| experiment_id | token_variant | num_topics | no_below | no_above | alpha | eta | passes | coherence_cv | largest_topic_percent | smallest_topic_percent | empty_bow_count | topic_words_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52 | unigram | 12 | 3 | 0.6 | symmetric | symmetric | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 50 | unigram | 12 | 3 | 0.6 | symmetric | auto | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 20 | unigram | 12 | 3 | 0.5 | symmetric | symmetric | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 18 | unigram | 12 | 3 | 0.5 | symmetric | auto | 20 | 0.5280 | 16.31 | 3.19 | 42 | T0: attack, device, attacker, said, network, security, access, system, threat, user | T1: file, system, command, code, agent, attacker, payload, figure, script, window | T2: phone, crime, fraud, use, reward, law, fede... |
| 82 | unigram | 12 | 5 | 0.5 | symmetric | auto | 20 | 0.5212 | 14.19 | 2.36 | 63 | T0: data, tool, email, malware, platform, service, security, stryker, workflow, customer | T1: team, security, risk, exposure, remediation, vulnerability, environment, faster, across, organization | T2: pointer, buffe... |
| 114 | unigram | 12 | 5 | 0.6 | symmetric | auto | 20 | 0.5212 | 14.19 | 2.36 | 63 | T0: data, tool, email, malware, platform, service, security, stryker, workflow, customer | T1: team, security, risk, exposure, remediation, vulnerability, environment, faster, across, organization | T2: pointer, buffe... |
| 84 | unigram | 12 | 5 | 0.5 | symmetric | symmetric | 20 | 0.5212 | 14.19 | 2.36 | 63 | T0: data, tool, email, malware, platform, service, security, stryker, workflow, customer | T1: team, security, risk, exposure, remediation, vulnerability, environment, faster, across, organization | T2: pointer, buffe... |
| 116 | unigram | 12 | 5 | 0.6 | symmetric | symmetric | 20 | 0.5212 | 14.19 | 2.36 | 63 | T0: data, tool, email, malware, platform, service, security, stryker, workflow, customer | T1: team, security, risk, exposure, remediation, vulnerability, environment, faster, across, organization | T2: pointer, buffe... |
| 10 | unigram | 10 | 3 | 0.5 | symmetric | auto | 20 | 0.5201 | 17.08 | 2.70 | 42 | T0: attack, attacker, device, said, system, network, user, data, address, access | T1: file, system, command, payload, agent, script, attacker, figure, window, code | T2: phone, crime, use, fraud, reward, law, federal... |
| 12 | unigram | 10 | 3 | 0.5 | symmetric | symmetric | 20 | 0.5201 | 17.08 | 2.70 | 42 | T0: attack, attacker, device, said, system, network, user, data, address, access | T1: file, system, command, payload, agent, script, attacker, figure, window, code | T2: phone, crime, use, fraud, reward, law, federal... |

## Recommendation

Scegliere una configurazione solo se migliora coherence senza produrre topic troppo sbilanciati. Confrontare sempre top words e distribuzioni prima di sostituire il modello live corrente. Migliore candidata bilanciata: experiment_id=52, unigram, 12 topic, coherence=0.5280.

## Methodological Note

La coherence è usata come supporto alla scelta del modello, ma la selezione finale considera anche interpretabilità, stabilità e utilità per P2.
