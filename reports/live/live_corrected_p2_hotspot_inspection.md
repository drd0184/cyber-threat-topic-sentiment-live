# Corrected Live P2 Hotspot Inspection

## Hotspot Description

Strongest negative P2 hotspot in the corrected social/news-only live pipeline.

| Field | Value |
| --- | --- |
| time_window | 2026-04-28T12:00:00+00:00 |
| dominant_topic | 4 |
| topic_label | Ransomware / Malware / Attacks |
| p2_index | -24.1336 |
| topic_volume | 9 |
| topic_sentiment_sum | -3.8837 |
| severity | high |

## Document Summary

| Metric | Value |
| --- | --- |
| Hotspot documents | 9 |
| Mean vader_compound | -0.4315 |
| Min vader_compound | -0.9532 |
| Max vader_compound | 0.5719 |
| Mean dominant_topic_probability | 0.2838 |
| P2 CSV encoding | utf-8 |
| Sentiment CSV encoding | utf-8 |

## Source Type Distribution

| source_type | rows | percent_hotspot |
| --- | --- | --- |
| reddit_rss | 6 | 66.67% |
| news_rss | 3 | 33.33% |

## Source Name Distribution

| source_name | rows | percent_hotspot |
| --- | --- | --- |
| privacy | 3 | 33.33% |
| BleepingComputer | 2 | 22.22% |
| blueteamsec | 2 | 22.22% |
| The Hacker News | 1 | 11.11% |
| ReverseEngineering | 1 | 11.11% |

## Sentiment Class Distribution

| sentiment_class | rows | percent_hotspot |
| --- | --- | --- |
| negative | 7 | 77.78% |
| positive | 2 | 22.22% |

## Top 10 Most Negative Documents

| id | created_at | source_type | source_name | vader_compound | sentiment_class | title |
| --- | --- | --- | --- | --- | --- | --- |
| https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html | 2026-04-28T14:01:00+00:00 | news_rss | The Hacker News | -0.9532 | negative | VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows, Linux, ESXi |
| https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/ | 2026-04-28T21:25:57+00:00 | news_rss | BleepingComputer | -0.8957 | negative | Broken VECT 2.0 ransomware acts as a data wiper for large files |
| https://www.bleepingcomputer.com/news/security/us-reportedly-charges-scattered-spider-hacker-arrested-in-finland/ | 2026-04-28T15:39:52+00:00 | news_rss | BleepingComputer | -0.8591 | negative | US reportedly charges Scattered Spider hacker arrested in Finland |
| t3_1sy2twb | 2026-04-28T14:20:43+00:00 | reddit_rss | privacy | -0.6705 | negative | Police Surveillance Abuse Exposed as Officers Face Allegations of Using Licence Plate Data to Stalk Exes, Strangers |
| t3_1sycwhm | 2026-04-28T20:16:00+00:00 | reddit_rss | privacy | -0.6670 | negative | How to start over without being linked |
| t3_1sy6s21 | 2026-04-28T16:42:03+00:00 | reddit_rss | blueteamsec | -0.4995 | negative | MAD Bugs: QEMU and UTM Escape |
| t3_1sy6cin | 2026-04-28T16:26:32+00:00 | reddit_rss | blueteamsec | -0.4767 | negative | BlueNoroff Uses ClickFix, Fileless PowerShell, and AI-Generated Fake Zoom Meetings to Target Web3 Sector |
| t3_1syfqie | 2026-04-28T22:02:00+00:00 | reddit_rss | privacy | 0.5661 | positive | Do services like Incogni or Aura actually do what they say? Do they provide proof that your info is actually removed from the databases t... |
| t3_1sy7ruo | 2026-04-28T17:16:32+00:00 | reddit_rss | ReverseEngineering | 0.5719 | positive | Building a perfect clone of 1993 game SimTower (via RE) |

## Methodological Note

Questo hotspot è calcolato solo su fonti social/news. CVE/NVD non contribuisce al P2.
