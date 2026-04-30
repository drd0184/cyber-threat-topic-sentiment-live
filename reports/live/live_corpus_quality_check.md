# Live Corpus Quality Check

Diagnostic report for `data/live/processed/03_live_preprocessed_dataset.csv`. This report does not modify the dataset and does not run LDA, VADER, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 1078 |
| created_at min | 2025-12-16T09:00:00+00:00 |
| created_at max | 2026-04-30T10:52:33+00:00 |
| Mean text_raw length | 867.89 |
| Median text_raw length | 101.00 |
| Mean text_clean tokens | 76.24 |
| Median text_clean tokens | 10.00 |
| Encoding used | utf-8 |

## Warnings

No warning thresholds triggered.

## Source Type Distribution

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 578 | 53.62% |
| reddit_rss | 348 | 32.28% |
| news_rss | 152 | 14.10% |

## Source Name Distribution Top 30

| source_name | rows | percent_dataset |
| --- | --- | --- |
| The Hacker News | 54 | 5.01% |
| sysadmin | 48 | 4.45% |
| cybersecurity | 45 | 4.17% |
| privacy | 39 | 3.62% |
| blueteamsec | 36 | 3.34% |
| netsec | 28 | 2.60% |
| ReverseEngineering | 27 | 2.50% |
| AskNetsec | 27 | 2.50% |
| hacking | 26 | 2.41% |
| osint | 25 | 2.32% |
| ComputerSecurity | 24 | 2.23% |
| Malware | 23 | 2.13% |
| techradar.com | 22 | 2.04% |
| Rapid7 Blog | 22 | 2.04% |
| BleepingComputer | 21 | 1.95% |
| forbes.com | 16 | 1.48% |
| Unit 42 | 15 | 1.39% |
| Cisco Talos Blog | 15 | 1.39% |
| cnews.ru | 14 | 1.30% |
| ascii.jp | 14 | 1.30% |
| ithome.com.tw | 12 | 1.11% |
| KrebsOnSecurity | 10 | 0.93% |
| Google Project Zero | 9 | 0.83% |
| cointelegraph.com | 9 | 0.83% |
| esecurityplanet.com | 8 | 0.74% |
| infosecurity-magazine.com | 7 | 0.65% |
| techcrunch.com | 7 | 0.65% |
| csoonline.com | 6 | 0.56% |
| bankinfosecurity.com | 6 | 0.56% |
| timesofindia.indiatimes.com | 6 | 0.56% |

## Keyword Coverage

| keyword | documents | percent_dataset |
| --- | --- | --- |
| cve | 59 | 5.47% |
| vulnerability | 91 | 8.44% |
| ransomware | 51 | 4.73% |
| malware | 90 | 8.35% |
| phishing | 30 | 2.78% |
| breach | 34 | 3.15% |
| exploit | 76 | 7.05% |
| ddos | 47 | 4.36% |
| botnet | 7 | 0.65% |
| zeroday | 0 | 0.00% |
| zero-day | 13 | 1.21% |
| data leak | 2 | 0.19% |

## Top 50 Global Tokens

| token | count |
| --- | --- |
| vulnerability | 694 |
| cve | 516 |
| security | 508 |
| window | 487 |
| data | 416 |
| system | 394 |
| exploitation | 389 |
| access | 340 |
| attack | 338 |
| process | 316 |
| file | 305 |
| likely | 303 |
| user | 279 |
| code | 277 |
| time | 262 |
| attacker | 254 |
| exploit | 254 |
| privilege | 251 |
| less | 250 |
| device | 245 |
| use | 237 |
| service | 235 |
| team | 230 |
| using | 214 |
| threat | 213 |
| used | 207 |
| elevation | 204 |
| payload | 203 |
| microsoft | 202 |
| pointer | 196 |
| tool | 193 |
| write | 180 |
| buffer | 180 |
| command | 167 |
| call | 166 |
| year | 160 |
| environment | 160 |
| function | 159 |
| server | 155 |
| target | 151 |
| execution | 151 |
| malware | 144 |
| chain | 141 |
| risk | 140 |
| remote | 139 |
| heap | 134 |
| bug | 134 |
| information | 133 |
| dynamic | 133 |
| across | 131 |

## Top 30 Tokens by Source Type

| source_type | rank | token | count |
| --- | --- | --- | --- |
| news_api | 1 | attack | 45 |
| news_api | 2 | malware | 40 |
| news_api | 3 | ddos | 40 |
| news_api | 4 | ransomware | 35 |
| news_api | 5 | cyberattack | 30 |
| news_api | 6 | threat | 30 |
| news_api | 7 | data | 30 |
| news_api | 8 | security | 27 |
| news_api | 9 | exploit | 27 |
| news_api | 10 | cyber | 23 |
| news_api | 11 | zero | 19 |
| news_api | 12 | hacker | 19 |
| news_api | 13 | google | 18 |
| news_api | 14 | breach | 18 |
| news_api | 15 | risk | 15 |
| news_api | 16 | news | 14 |
| news_api | 17 | fbi | 14 |
| news_api | 18 | claude | 14 |
| news_api | 19 | ascii | 14 |
| news_api | 20 | window | 13 |
| news_api | 21 | group | 13 |
| news_api | 22 | scam | 13 |
| news_api | 23 | android | 13 |
| news_api | 24 | report | 12 |
| news_api | 25 | udayavani | 12 |
| news_api | 26 | hit | 12 |
| news_api | 27 | user | 11 |
| news_api | 28 | iphone | 11 |
| news_api | 29 | supply | 11 |
| news_api | 30 | chain | 11 |
| news_rss | 1 | vulnerability | 667 |
| news_rss | 2 | cve | 482 |
| news_rss | 3 | window | 402 |
| news_rss | 4 | security | 389 |
| news_rss | 5 | exploitation | 385 |
| news_rss | 6 | data | 319 |
| news_rss | 7 | likely | 299 |
| news_rss | 8 | process | 297 |
| news_rss | 9 | access | 292 |
| news_rss | 10 | system | 282 |
| news_rss | 11 | file | 254 |
| news_rss | 12 | attack | 252 |
| news_rss | 13 | privilege | 243 |
| news_rss | 14 | less | 237 |
| news_rss | 15 | user | 225 |
| news_rss | 16 | attacker | 223 |
| news_rss | 17 | code | 207 |
| news_rss | 18 | elevation | 204 |
| news_rss | 19 | exploit | 198 |
| news_rss | 20 | pointer | 196 |
| news_rss | 21 | device | 196 |
| news_rss | 22 | team | 194 |
| news_rss | 23 | service | 193 |
| news_rss | 24 | payload | 184 |
| news_rss | 25 | buffer | 180 |
| news_rss | 26 | time | 177 |
| news_rss | 27 | microsoft | 170 |
| news_rss | 28 | write | 167 |
| news_rss | 29 | used | 164 |
| news_rss | 30 | function | 154 |
| reddit_rss | 1 | system | 103 |
| reddit_rss | 2 | use | 99 |
| reddit_rss | 3 | security | 92 |
| reddit_rss | 4 | time | 80 |
| reddit_rss | 5 | tool | 80 |
| reddit_rss | 6 | window | 72 |
| reddit_rss | 7 | year | 71 |
| reddit_rss | 8 | data | 67 |
| reddit_rss | 9 | code | 63 |
| reddit_rss | 10 | phone | 63 |
| reddit_rss | 11 | using | 59 |
| reddit_rss | 12 | crime | 53 |
| reddit_rss | 13 | site | 50 |
| reddit_rss | 14 | actually | 50 |
| reddit_rss | 15 | even | 48 |
| reddit_rss | 16 | file | 46 |
| reddit_rss | 17 | run | 45 |
| reddit_rss | 18 | access | 45 |
| reddit_rss | 19 | reward | 44 |
| reddit_rss | 20 | password | 44 |
| reddit_rss | 21 | user | 43 |
| reddit_rss | 22 | fraud | 43 |
| reddit_rss | 23 | feel | 41 |
| reddit_rss | 24 | attack | 41 |
| reddit_rss | 25 | check | 41 |
| reddit_rss | 26 | without | 40 |
| reddit_rss | 27 | real | 40 |
| reddit_rss | 28 | report | 40 |
| reddit_rss | 29 | help | 40 |
| reddit_rss | 30 | used | 40 |

## Methodological Note

Questo controllo valuta il corpus social/news preprocessato prima di un eventuale nuovo LDA live. Non usa CVE/NVD come fonte primaria e non calcola sentiment o P2.
