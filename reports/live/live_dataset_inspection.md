# Live Dataset Inspection

Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 5265 |
| created_at min | 2025-12-16T09:00:00Z |
| created_at max | 2026-05-04T13:46:21Z |
| collected_at min | 2026-04-29T13:22:42Z |
| collected_at max | 2026-05-04T13:56:50Z |
| Unparsable created_at | 0 (0.00%) |
| Unparsable collected_at | 0 (0.00%) |
| Null/empty text_raw | 0 (0.00%) |
| Mean text_raw length | 418.84 |
| Median text_raw length | 103.0 |
| Min text_raw length | 6 |
| Max text_raw length | 66525 |
| text_raw < 30 chars | 118 (2.24%) |
| text_raw < 100 chars | 2542 (48.28%) |
| Duplicate id rows | 0 rows / 0 values |
| Duplicate url rows | 0 rows / 0 values |
| Duplicate normalized text_raw rows | 520 rows / 146 values |

## Warnings

- WARNING: Duplicate normalized text_raw rows found: 520.

## Rows By source_type

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 2860 | 54.32% |
| cve | 1295 | 24.60% |
| reddit_rss | 900 | 17.09% |
| news_rss | 210 | 3.99% |

## Rows By source_name

| source_name | rows | percent_dataset |
| --- | --- | --- |
| NVD CVE | 1295 | 24.60% |
| cybersecurity | 243 | 4.62% |
| sysadmin | 182 | 3.46% |
| blueteamsec | 108 | 2.05% |
| privacy | 108 | 2.05% |
| The Hacker News | 70 | 1.33% |
| hacking | 51 | 0.97% |
| BleepingComputer | 48 | 0.91% |
| ReverseEngineering | 44 | 0.84% |
| netsec | 40 | 0.76% |
| forbes.com | 35 | 0.66% |
| AskNetsec | 34 | 0.65% |
| osint | 34 | 0.65% |
| ascii.jp | 34 | 0.65% |
| techradar.com | 31 | 0.59% |
| Malware | 30 | 0.57% |
| ComputerSecurity | 26 | 0.49% |
| cnews.ru | 24 | 0.46% |
| Rapid7 Blog | 23 | 0.44% |
| ithome.com.tw | 23 | 0.44% |
| haberler.com | 21 | 0.40% |
| boredpanda.com | 21 | 0.40% |
| fnnews.com | 20 | 0.38% |
| itbrief.co.nz | 19 | 0.36% |
| theregister.com | 19 | 0.36% |
| rpp.pe | 19 | 0.36% |
| bankinfosecurity.com | 18 | 0.34% |
| Unit 42 | 17 | 0.32% |
| 163.com | 17 | 0.32% |
| SANS Internet Storm Center | 16 | 0.30% |
| Cisco Talos Blog | 16 | 0.30% |
| manilatimes.net | 16 | 0.30% |
| dostor.org | 14 | 0.27% |
| govinfosecurity.com | 14 | 0.27% |
| cointelegraph.com | 13 | 0.25% |
| finance.sina.com.cn | 13 | 0.25% |
| biz.heraldcorp.com | 13 | 0.25% |
| esecurityplanet.com | 12 | 0.23% |
| el-balad.com | 12 | 0.23% |
| fool.com | 12 | 0.23% |
| KrebsOnSecurity | 11 | 0.21% |
| finanznachrichten.de | 11 | 0.21% |
| moneycontrol.com | 11 | 0.21% |
| economictimes.indiatimes.com | 11 | 0.21% |
| baijiahao.baidu.com | 11 | 0.21% |
| excite.co.jp | 11 | 0.21% |
| csoonline.com | 10 | 0.19% |
| jdsupra.com | 10 | 0.19% |
| finance.yahoo.com | 10 | 0.19% |
| techcrunch.com | 10 | 0.19% |
| edaily.co.kr | 10 | 0.19% |
| Google Project Zero | 9 | 0.17% |
| infosecurity-magazine.com | 9 | 0.17% |
| timesofindia.indiatimes.com | 9 | 0.17% |
| zdnet.co.kr | 9 | 0.17% |
| securitylab.ru | 9 | 0.17% |
| zazoom.it | 9 | 0.17% |
| yahoo.com | 8 | 0.15% |
| prnewswire.com | 8 | 0.15% |
| ddaily.co.kr | 8 | 0.15% |
| channellife.co.nz | 8 | 0.15% |
| itwire.com | 8 | 0.15% |
| inewsgr.com | 8 | 0.15% |
| govtech.com | 7 | 0.13% |
| bankingnews.gr | 7 | 0.13% |
| sabah.com.tr | 7 | 0.13% |
| eturbonews.com | 7 | 0.13% |
| collider.com | 7 | 0.13% |
| birgun.net | 7 | 0.13% |
| ensonhaber.com | 6 | 0.11% |
| laopcion.com.mx | 6 | 0.11% |
| n-tv.de | 6 | 0.11% |
| aa.com.tr | 6 | 0.11% |
| vz.ru | 6 | 0.11% |
| screenrant.com | 6 | 0.11% |
| udayavani.com | 6 | 0.11% |
| foxnews.com | 6 | 0.11% |
| tvguide.co.uk | 6 | 0.11% |
| natlawreview.com | 6 | 0.11% |
| punchng.com | 6 | 0.11% |
| hothardware.com | 5 | 0.09% |
| japan.zdnet.com | 5 | 0.09% |
| pcmag.com | 5 | 0.09% |
| milliyet.com.tr | 5 | 0.09% |
| channellife.com.au | 5 | 0.09% |
| theglobeandmail.com | 5 | 0.09% |
| bd-pratidin.com | 5 | 0.09% |
| heise.de | 5 | 0.09% |
| shorouknews.com | 5 | 0.09% |
| coindesk.com | 5 | 0.09% |
| europapress.es | 5 | 0.09% |
| time.mk | 5 | 0.09% |
| ibtimes.com.au | 5 | 0.09% |
| etoday.co.kr | 5 | 0.09% |
| segye.com | 5 | 0.09% |
| divyabhaskar.co.in | 5 | 0.09% |
| marketscreener.com | 5 | 0.09% |
| evrensel.net | 5 | 0.09% |
| yorkregion.com | 5 | 0.09% |
| maliactu.net | 5 | 0.09% |
| vetogate.com | 5 | 0.09% |
| newkerala.com | 5 | 0.09% |
| anlatilaninotesi.com.tr | 5 | 0.09% |
| busan.com | 5 | 0.09% |
| insurancebusinessmag.com | 4 | 0.08% |
| winnipegfreepress.com | 4 | 0.08% |
| cnnturk.com | 4 | 0.08% |
| ura.news | 4 | 0.08% |
| thenews.com.pk | 4 | 0.08% |
| thefastmode.com | 4 | 0.08% |
| cbc.ca | 4 | 0.08% |
| scoop.co.nz | 4 | 0.08% |
| straitstimes.com | 4 | 0.08% |
| yeniakit.com.tr | 4 | 0.08% |
| turkiyegazetesi.com.tr | 4 | 0.08% |
| trthaber.com | 4 | 0.08% |
| kibrispostasi.com | 4 | 0.08% |
| welt.de | 4 | 0.08% |
| wmur.com | 4 | 0.08% |
| 9to5mac.com | 4 | 0.08% |
| freepressjournal.in | 4 | 0.08% |
| interfax.ru | 4 | 0.08% |
| mashable.com | 4 | 0.08% |
| itnews.com.au | 4 | 0.08% |
| it-online.co.za | 4 | 0.08% |
| tn.com.ar | 4 | 0.08% |
| natalie.mu | 4 | 0.08% |
| newspim.com | 4 | 0.08% |
| computing.co.uk | 4 | 0.08% |
| newjerseytelegraph.com | 4 | 0.08% |
| wired.com | 4 | 0.08% |
| itweb.co.za | 4 | 0.08% |
| haksozhaber.net | 4 | 0.08% |
| tgrthaber.com | 4 | 0.08% |
| sozcu.com.tr | 4 | 0.08% |
| nypost.com | 4 | 0.08% |
| aceshowbiz.com | 4 | 0.08% |
| thenextweb.com | 4 | 0.08% |
| aljazeera.net | 4 | 0.08% |
| itnewsonline.com | 4 | 0.08% |
| ghanamma.com | 4 | 0.08% |
| simcoe.com | 4 | 0.08% |
| pravda.ru | 4 | 0.08% |
| cambridgetimes.ca | 4 | 0.08% |
| mainichi.jp | 4 | 0.08% |
| boerse-express.com | 4 | 0.08% |
| alquds.co.uk | 4 | 0.08% |
| gdnonline.com | 4 | 0.08% |
| newsway.co.kr | 4 | 0.08% |
| iefimerida.gr | 4 | 0.08% |
| sapo.pt | 4 | 0.08% |
| abc.es | 4 | 0.08% |
| bursadabugun.com | 4 | 0.08% |
| mirror.co.uk | 4 | 0.08% |
| sudanile.com | 4 | 0.08% |
| vanguardngr.com | 4 | 0.08% |
| vol.at | 4 | 0.08% |
| androidauthority.com | 3 | 0.06% |
| mondaq.com | 3 | 0.06% |
| tomshardware.com | 3 | 0.06% |
| donanimgunlugu.com | 3 | 0.06% |
| etnews.com | 3 | 0.06% |
| sb.by | 3 | 0.06% |
| womannews.net | 3 | 0.06% |
| miragenews.com | 3 | 0.06% |
| wesh.com | 3 | 0.06% |
| wbaltv.com | 3 | 0.06% |
| glavcom.ua | 3 | 0.06% |
| politis.com.cy | 3 | 0.06% |
| koreaherald.com | 3 | 0.06% |
| nzherald.co.nz | 3 | 0.06% |
| eluniversal.com.mx | 3 | 0.06% |
| dw.com | 3 | 0.06% |
| zeit.de | 3 | 0.06% |
| eurointegration.com.ua | 3 | 0.06% |
| bleedingcool.com | 3 | 0.06% |
| defensenews.com | 3 | 0.06% |
| hindustantimes.com | 3 | 0.06% |
| n.yam.com | 3 | 0.06% |
| odatv.com | 3 | 0.06% |
| udn.com | 3 | 0.06% |
| finance.eastmoney.com | 3 | 0.06% |
| techtimes.com | 3 | 0.06% |
| vietnamnet.vn | 3 | 0.06% |
| ria.ru | 3 | 0.06% |
| russian.rt.com | 3 | 0.06% |
| unian.net | 3 | 0.06% |
| newswiretoday.com | 3 | 0.06% |
| portal.sina.com.hk | 3 | 0.06% |
| itbusinessnet.com | 3 | 0.06% |
| biometricupdate.com | 3 | 0.06% |
| makeuseof.com | 3 | 0.06% |
| itbear.com.cn | 3 | 0.06% |
| businessday.co.za | 3 | 0.06% |
| am.com.mx | 3 | 0.06% |
| elsiglodetorreon.com.mx | 3 | 0.06% |
| kmib.co.kr | 3 | 0.06% |
| ohmynews.com | 3 | 0.06% |
| inews24.com | 3 | 0.06% |
| hani.co.kr | 3 | 0.06% |
| tribuneindia.com | 3 | 0.06% |
| aninews.in | 3 | 0.06% |
| timeslive.co.za | 3 | 0.06% |
| capital.ro | 3 | 0.06% |
| business.scoop.co.nz | 3 | 0.06% |
| claimsjournal.com | 3 | 0.06% |
| index.hu | 3 | 0.06% |
| eldiariodechihuahua.mx | 3 | 0.06% |
| rediff.com | 3 | 0.06% |
| dailypolitical.com | 3 | 0.06% |
| insideottawavalley.com | 3 | 0.06% |
| europesun.com | 3 | 0.06% |
| alltoc.com | 3 | 0.06% |
| globalnews.ca | 3 | 0.06% |
| thesun.ng | 3 | 0.06% |
| dailymail.com | 3 | 0.06% |
| toonippo.co.jp | 3 | 0.06% |
| netzwelt.de | 3 | 0.06% |
| theguardian.com | 3 | 0.06% |
| tumentoday.ru | 3 | 0.06% |
| eurasiareview.com | 3 | 0.06% |
| ciudadccs.info | 3 | 0.06% |
| albiladpress.com | 3 | 0.06% |
| prokerala.com | 3 | 0.06% |
| ianslive.in | 3 | 0.06% |
| antimafiaduemila.com | 3 | 0.06% |
| habervitrini.com | 3 | 0.06% |
| talk.ltn.com.tw | 3 | 0.06% |
| focus.de | 3 | 0.06% |
| sankei.com | 3 | 0.06% |
| orangeville.com | 3 | 0.06% |
| modernghana.com | 3 | 0.06% |
| oem.com.mx | 3 | 0.06% |
| northumberlandnews.com | 3 | 0.06% |
| munhwa.com | 3 | 0.06% |
| ziarulprofit.ro | 3 | 0.06% |
| businessghana.com | 2 | 0.04% |
| digitaljournal.com | 2 | 0.04% |
| securityinfowatch.com | 2 | 0.04% |
| gizmodo.com | 2 | 0.04% |
| insurancejournal.com | 2 | 0.04% |
| inforum.com | 2 | 0.04% |
| computerweekly.com | 2 | 0.04% |
| pymnts.com | 2 | 0.04% |
| bleepingcomputer.com | 2 | 0.04% |
| wsbtv.com | 2 | 0.04% |
| phonandroid.com | 2 | 0.04% |
| propakistani.pk | 2 | 0.04% |
| adevarul.ro | 2 | 0.04% |
| bgr.com | 2 | 0.04% |
| life.ru | 2 | 0.04% |
| 01net.com | 2 | 0.04% |
| github.com | 2 | 0.04% |
| hollywoodreporter.com | 2 | 0.04% |
| t-online.de | 2 | 0.04% |
| lexpress.fr | 2 | 0.04% |
| freemalaysiatoday.com | 2 | 0.04% |
| metroseoul.co.kr | 2 | 0.04% |
| iz.ru | 2 | 0.04% |
| lenta.ru | 2 | 0.04% |
| bunburymail.com.au | 2 | 0.04% |
| nvi.com.au | 2 | 0.04% |
| dnews.gr | 2 | 0.04% |
| ledauphine.com | 2 | 0.04% |
| dailykos.com | 2 | 0.04% |
| lalsace.fr | 2 | 0.04% |
| elmanana.com | 2 | 0.04% |
| aristeguinoticias.com | 2 | 0.04% |
| news.cn | 2 | 0.04% |
| tagesschau.de | 2 | 0.04% |
| op-online.de | 2 | 0.04% |
| wiwo.de | 2 | 0.04% |
| bursahakimiyet.com.tr | 2 | 0.04% |
| computerworld.dk | 2 | 0.04% |
| dailynews.co.th | 2 | 0.04% |
| kcci.com | 2 | 0.04% |
| wdrb.com | 2 | 0.04% |
| riasv.ru | 2 | 0.04% |
| aol.co.uk | 2 | 0.04% |
| lbc.co.uk | 2 | 0.04% |
| wwmt.com | 2 | 0.04% |
| jpost.com | 2 | 0.04% |
| haberturk.com | 2 | 0.04% |
| hurriyetdailynews.com | 2 | 0.04% |
| wfmz.com | 2 | 0.04% |
| designboom.com | 2 | 0.04% |
| hinews.cn | 2 | 0.04% |
| tech.caijing.com.cn | 2 | 0.04% |
| tech.ifeng.com | 2 | 0.04% |
| androidheadlines.com | 2 | 0.04% |
| gamerant.com | 2 | 0.04% |
| theblaze.com | 2 | 0.04% |
| vesti.ru | 2 | 0.04% |
| jawapos.com | 2 | 0.04% |
| fontanka.ru | 2 | 0.04% |
| 1prime.ru | 2 | 0.04% |
| kommersant.ru | 2 | 0.04% |
| politika.rs | 2 | 0.04% |
| vg.no | 2 | 0.04% |
| vedomosti.ru | 2 | 0.04% |
| weser-kurier.de | 2 | 0.04% |
| irishdentist.ie | 2 | 0.04% |
| ntdtv.com | 2 | 0.04% |
| chip.de | 2 | 0.04% |
| comnews.ru | 2 | 0.04% |
| securitybrief.news | 2 | 0.04% |
| tekniikkatalous.fi | 2 | 0.04% |
| jugantor.com | 2 | 0.04% |
| webpronews.com | 2 | 0.04% |
| htxt.co.za | 2 | 0.04% |
| newsweek.com | 2 | 0.04% |
| infoworld.com | 2 | 0.04% |
| bjnews.com.cn | 2 | 0.04% |
| stcn.com | 2 | 0.04% |
| military.china.com | 2 | 0.04% |
| antaranews.com | 2 | 0.04% |
| nikkei.com | 2 | 0.04% |
| newtalk.tw | 2 | 0.04% |
| arstechnica.com | 2 | 0.04% |
| senego.com | 2 | 0.04% |
| index.hr | 2 | 0.04% |
| cloud.watch.impress.co.jp | 2 | 0.04% |
| eldia.com.bo | 2 | 0.04% |
| eldestapeweb.com | 2 | 0.04% |
| mariettatimes.com | 2 | 0.04% |
| insight.co.kr | 2 | 0.04% |
| thehindu.com | 2 | 0.04% |
| divyamarathi.bhaskar.com | 2 | 0.04% |
| hindi.webdunia.com | 2 | 0.04% |
| digi24.ro | 2 | 0.04% |
| rappler.com | 2 | 0.04% |
| livehindustan.com | 2 | 0.04% |
| newsbomb.gr | 2 | 0.04% |
| geeky-gadgets.com | 2 | 0.04% |
| kten.com | 2 | 0.04% |
| americanbanker.com | 2 | 0.04% |
| hawaiitelegraph.com | 2 | 0.04% |
| tennesseedaily.com | 2 | 0.04% |
| ibtimes.co.uk | 2 | 0.04% |
| posta.com.tr | 2 | 0.04% |
| dha.com.tr | 2 | 0.04% |
| begeek.fr | 2 | 0.04% |
| mersinhaber.com | 2 | 0.04% |
| lrytas.lt | 2 | 0.04% |
| lefigaro.fr | 2 | 0.04% |
| yeniasya.com.tr | 2 | 0.04% |
| pcwplus.hu | 2 | 0.04% |
| mississauga.com | 2 | 0.04% |
| newstribune.com | 2 | 0.04% |
| livemint.com | 2 | 0.04% |
| sanantoniopost.com | 2 | 0.04% |
| zonebourse.com | 2 | 0.04% |
| bernerzeitung.ch | 2 | 0.04% |
| haber1.com | 2 | 0.04% |
| deadline.com | 2 | 0.04% |
| macleayargus.com.au | 2 | 0.04% |
| investegate.co.uk | 2 | 0.04% |
| unternehmen-heute.de | 2 | 0.04% |
| watoday.com.au | 2 | 0.04% |
| arkansasonline.com | 2 | 0.04% |
| nwaonline.com | 2 | 0.04% |
| uainfo.org | 2 | 0.04% |
| dailyemerald.com | 2 | 0.04% |
| presstv.ir | 2 | 0.04% |
| fox4news.com | 2 | 0.04% |
| livenews.co.nz | 2 | 0.04% |
| rnz.co.nz | 2 | 0.04% |
| medianama.com | 2 | 0.04% |
| allafrica.com | 2 | 0.04% |
| ecodibergamo.it | 2 | 0.04% |
| daily.com.ua | 2 | 0.04% |
| naftemporiki.gr | 2 | 0.04% |
| diario.mx | 2 | 0.04% |
| it.euronews.com | 2 | 0.04% |
| marca.com | 2 | 0.04% |
| inosmi.ru | 2 | 0.04% |
| brasil247.com | 2 | 0.04% |
| libnanews.com | 2 | 0.04% |
| techweez.com | 2 | 0.04% |
| thisdaylive.com | 2 | 0.04% |
| wallstreet-online.de | 2 | 0.04% |
| amic.ru | 2 | 0.04% |
| welivesecurity.com | 2 | 0.04% |
| niagarathisweek.com | 2 | 0.04% |
| tmtpost.com | 2 | 0.04% |
| pv-magazine.com | 2 | 0.04% |
| massachusettssun.com | 2 | 0.04% |
| chinanationalnews.com | 2 | 0.04% |
| dailypioneer.com | 2 | 0.04% |
| jamaicaobserver.com | 2 | 0.04% |
| wzzm13.com | 2 | 0.04% |
| sentinel.ht | 2 | 0.04% |
| wcvb.com | 2 | 0.04% |
| objectiv.tv | 2 | 0.04% |
| danas.rs | 2 | 0.04% |
| dailyinqilab.com | 2 | 0.04% |
| castanetkamloops.net | 2 | 0.04% |
| abovethelaw.com | 2 | 0.04% |
| laleggepertutti.it | 2 | 0.04% |
| newratings.de | 2 | 0.04% |
| prensalibre.com | 2 | 0.04% |
| morningstar.com | 2 | 0.04% |
| dailybreeze.com | 2 | 0.04% |
| brisbanetimes.com.au | 2 | 0.04% |
| smh.com.au | 2 | 0.04% |
| mdjonline.com | 2 | 0.04% |
| dailynews.com | 2 | 0.04% |
| sgvtribune.com | 2 | 0.04% |
| lelezard.com | 2 | 0.04% |
| irishtimes.com | 2 | 0.04% |
| greeleytribune.com | 2 | 0.04% |
| y-mainichi.co.jp | 2 | 0.04% |
| heraldk.com | 2 | 0.04% |
| nikkan-gendai.com | 2 | 0.04% |
| wikitree.co.kr | 2 | 0.04% |
| kathimerini.com.cy | 2 | 0.04% |
| ecommercenews.co.nz | 2 | 0.04% |
| batonrougepost.com | 2 | 0.04% |
| russiaherald.com | 2 | 0.04% |
| japanherald.com | 2 | 0.04% |
| bignewsnetwork.com | 2 | 0.04% |
| austinglobe.com | 2 | 0.04% |
| diariosur.es | 2 | 0.04% |
| filmfare.com | 2 | 0.04% |
| unn.ua | 2 | 0.04% |
| radiofrance.fr | 2 | 0.04% |
| ecodisicilia.com | 2 | 0.04% |
| elpais.com | 2 | 0.04% |
| focus.ua | 2 | 0.04% |
| internasional.kompas.com | 2 | 0.04% |
| business24.ro | 2 | 0.04% |
| howtogeek.com | 2 | 0.04% |
| ahaber.com.tr | 2 | 0.04% |
| turktime.com | 2 | 0.04% |
| haber7.com | 2 | 0.04% |
| haberyazar.com | 2 | 0.04% |
| news.mail.ru | 2 | 0.04% |
| denizlihaber.com | 2 | 0.04% |
| mk.ru | 2 | 0.04% |
| t-l.ru | 2 | 0.04% |
| pctechmag.com | 2 | 0.04% |
| nuevodiarioweb.com.ar | 2 | 0.04% |
| vicnews.com | 2 | 0.04% |
| storm.mg | 2 | 0.04% |
| radiopolar.com | 2 | 0.04% |
| townhall.com | 2 | 0.04% |
| ziare.com | 2 | 0.04% |
| breitbart.com | 2 | 0.04% |
| latimes.com | 2 | 0.04% |
| koreatimes.com | 2 | 0.04% |
| messengernewspapers.co.uk | 2 | 0.04% |
| dogruhaber.com.tr | 2 | 0.04% |
| tribune.net.ph | 2 | 0.04% |
| digit.in | 2 | 0.04% |
| thereporterethiopia.com | 2 | 0.04% |
| fr.allafrica.com | 2 | 0.04% |
| dnes.bg | 2 | 0.04% |
| correiodopovo.com.br | 2 | 0.04% |
| correiobraziliense.com.br | 2 | 0.04% |
| kitabat.com | 2 | 0.04% |
| mopo.de | 2 | 0.04% |
| alahalygate.com | 2 | 0.04% |
| indianexpress.com | 2 | 0.04% |
| parisguardian.com | 2 | 0.04% |
| lesnumeriques.com | 2 | 0.04% |
| bramptonguardian.com | 2 | 0.04% |
| nordbayern.de | 2 | 0.04% |
| blic.rs | 2 | 0.04% |
| tanea.gr | 2 | 0.04% |
| tvanouvelles.ca | 2 | 0.04% |
| ynet.co.il | 2 | 0.04% |
| lindependant.fr | 2 | 0.04% |
| t24.com.tr | 2 | 0.04% |
| muskokaregion.com | 2 | 0.04% |
| northbaynipissing.com | 2 | 0.04% |
| insideclimatenews.org | 2 | 0.04% |
| cna.com.tw | 2 | 0.04% |
| malijet.com | 2 | 0.04% |
| ilpost.it | 2 | 0.04% |
| thedailystar.net | 2 | 0.04% |
| infranken.de | 2 | 0.04% |
| itc.ua | 2 | 0.04% |
| rnanews.com | 2 | 0.04% |
| hngn.com | 2 | 0.04% |
| durhamregion.com | 2 | 0.04% |
| insidehalton.com | 2 | 0.04% |
| shikoku-np.co.jp | 2 | 0.04% |
| ilgiornale.it | 2 | 0.04% |
| contentmanager.de | 2 | 0.04% |
| dainiktribuneonline.com | 2 | 0.04% |
| em.com.br | 2 | 0.04% |
| quotidianodelsud.it | 2 | 0.04% |
| eldiariodelapampa.com.ar | 2 | 0.04% |
| meteoweb.eu | 2 | 0.04% |
| news-medical.net | 2 | 0.04% |
| diariodemallorca.es | 2 | 0.04% |
| yerelgundem.com | 2 | 0.04% |
| bangkokpost.com | 1 | 0.02% |
| governing.com | 1 | 0.02% |
| abc7news.com | 1 | 0.02% |
| cnn.com | 1 | 0.02% |
| edition.cnn.com | 1 | 0.02% |
| us.cnn.com | 1 | 0.02% |
| fox9.com | 1 | 0.02% |
| hachettebookgroup.com | 1 | 0.02% |
| bangordailynews.com | 1 | 0.02% |
| bt.no | 1 | 0.02% |
| cnet.com | 1 | 0.02% |
| ryt9.com | 1 | 0.02% |
| antivirus-sniper.macupdate.com | 1 | 0.02% |
| express.pk | 1 | 0.02% |
| presse-citron.net | 1 | 0.02% |
| techcabal.com | 1 | 0.02% |
| bangkokbiznews.com | 1 | 0.02% |
| aif.ru | 1 | 0.02% |
| digg.com | 1 | 0.02% |
| generation-nt.com | 1 | 0.02% |
| playground.ru | 1 | 0.02% |
| digitaltrends.com | 1 | 0.02% |
| alanbatnews.net | 1 | 0.02% |
| itnewsafrica.com | 1 | 0.02% |
| trustedreviews.com | 1 | 0.02% |
| news.tuoitre.vn | 1 | 0.02% |
| georgeherald.com | 1 | 0.02% |
| pjmedia.com | 1 | 0.02% |
| regions.ru | 1 | 0.02% |
| businesstimes.com.sg | 1 | 0.02% |
| pln-pskov.ru | 1 | 0.02% |
| fedpress.ru | 1 | 0.02% |
| wxii12.com | 1 | 0.02% |
| y95country.com | 1 | 0.02% |
| local12.com | 1 | 0.02% |
| kingfm.com | 1 | 0.02% |
| buffalobulletin.com | 1 | 0.02% |
| profitline.hu | 1 | 0.02% |
| de.nachrichten.yahoo.com | 1 | 0.02% |
| directionsmag.com | 1 | 0.02% |
| circleid.com | 1 | 0.02% |
| koco.com | 1 | 0.02% |
| wvtm13.com | 1 | 0.02% |
| wlwt.com | 1 | 0.02% |
| hirek.prim.hu | 1 | 0.02% |
| ottawacitizen.com | 1 | 0.02% |
| news.ltn.com.tw | 1 | 0.02% |
| infobae.com | 1 | 0.02% |
| dna.fr | 1 | 0.02% |
| laprovincia.es | 1 | 0.02% |
| northweststar.com.au | 1 | 0.02% |
| armenews.com | 1 | 0.02% |
| elcomercio.es | 1 | 0.02% |
| mandurahmail.com.au | 1 | 0.02% |
| salzburg24.at | 1 | 0.02% |
| republicain-lorrain.fr | 1 | 0.02% |
| lejsl.com | 1 | 0.02% |
| lavozdegalicia.es | 1 | 0.02% |
| diariopalentino.es | 1 | 0.02% |
| eldia.es | 1 | 0.02% |
| bbc.com | 1 | 0.02% |
| groundup.org.za | 1 | 0.02% |
| zetatijuana.com | 1 | 0.02% |
| funkytaurusmedia.com | 1 | 0.02% |
| botasot.info | 1 | 0.02% |
| fnp.de | 1 | 0.02% |
| ratopati.com | 1 | 0.02% |
| watson.ch | 1 | 0.02% |
| freiepresse.de | 1 | 0.02% |
| stern.de | 1 | 0.02% |
| ntv.com.tr | 1 | 0.02% |
| kannadaprabha.com | 1 | 0.02% |
| sn.at | 1 | 0.02% |
| dunya.com | 1 | 0.02% |
| sdpnoticias.com | 1 | 0.02% |
| vecer.com | 1 | 0.02% |
| rtl.nl | 1 | 0.02% |
| norran.se | 1 | 0.02% |
| aktifhaber.com | 1 | 0.02% |
| sana.sy | 1 | 0.02% |
| japan.cnet.com | 1 | 0.02% |
| vrt.be | 1 | 0.02% |
| donanimhaber.com | 1 | 0.02% |
| heute.at | 1 | 0.02% |
| bankier.pl | 1 | 0.02% |
| antena3.ro | 1 | 0.02% |
| businesstoday.in | 1 | 0.02% |
| 5.ua | 1 | 0.02% |
| twincities.com | 1 | 0.02% |
| king5.com | 1 | 0.02% |
| wtsp.com | 1 | 0.02% |
| wwltv.com | 1 | 0.02% |
| wusa9.com | 1 | 0.02% |
| fox43.com | 1 | 0.02% |
| daytondailynews.com | 1 | 0.02% |
| kmbc.com | 1 | 0.02% |
| fox17online.com | 1 | 0.02% |
| journal-news.com | 1 | 0.02% |
| siliconrepublic.com | 1 | 0.02% |
| 5newsonline.com | 1 | 0.02% |
| beckershospitalreview.com | 1 | 0.02% |
| legalinsurrection.com | 1 | 0.02% |
| wcbi.com | 1 | 0.02% |
| war.obozrevatel.com | 1 | 0.02% |
| dailymail.co.uk | 1 | 0.02% |
| wlox.com | 1 | 0.02% |
| wthr.com | 1 | 0.02% |
| yn.xinhuanet.com | 1 | 0.02% |
| news.ycwb.com | 1 | 0.02% |
| kob.com | 1 | 0.02% |
| china.com.cn | 1 | 0.02% |
| digi.china.com | 1 | 0.02% |
| dunyanews.tv | 1 | 0.02% |
| diena.lt | 1 | 0.02% |
| deperu.com | 1 | 0.02% |
| photo.china.com.cn | 1 | 0.02% |
| ondacero.es | 1 | 0.02% |
| dailysabah.com | 1 | 0.02% |
| press24.mk | 1 | 0.02% |
| nj.com | 1 | 0.02% |
| haber3.com | 1 | 0.02% |
| eluniverso.com | 1 | 0.02% |
| idnes.cz | 1 | 0.02% |
| mobile.zol.com.cn | 1 | 0.02% |
| ai.zol.com.cn | 1 | 0.02% |
| posttoday.com | 1 | 0.02% |
| news.cnfol.com | 1 | 0.02% |
| ettoday.net | 1 | 0.02% |
| 3c.ltn.com.tw | 1 | 0.02% |
| bj.xinhuanet.com | 1 | 0.02% |
| nbd.com.cn | 1 | 0.02% |
| tass.ru | 1 | 0.02% |
| ruhrnachrichten.de | 1 | 0.02% |
| top-channel.tv | 1 | 0.02% |
| jo24.net | 1 | 0.02% |
| panorama.com.al | 1 | 0.02% |
| balkanweb.com | 1 | 0.02% |
| lafranceagricole.fr | 1 | 0.02% |
| elwatannews.com | 1 | 0.02% |
| tecmundo.com.br | 1 | 0.02% |
| computerwoche.de | 1 | 0.02% |
| bandaancha.eu | 1 | 0.02% |
| jabar.tribunnews.com | 1 | 0.02% |
| dotekomanie.cz | 1 | 0.02% |
| bug.hr | 1 | 0.02% |
| jpnn.com | 1 | 0.02% |
| gorod48.ru | 1 | 0.02% |
| mskagency.ru | 1 | 0.02% |
| makassar.tribunnews.com | 1 | 0.02% |
| volksstimme.de | 1 | 0.02% |
| handelsblatt.com | 1 | 0.02% |
| sueddeutsche.de | 1 | 0.02% |
| cepro.com | 1 | 0.02% |
| corp.cnews.ru | 1 | 0.02% |
| vesti-ua.net | 1 | 0.02% |
| slguardian.org | 1 | 0.02% |
| tivi.fi | 1 | 0.02% |
| strategypage.com | 1 | 0.02% |
| alaskasnewssource.com | 1 | 0.02% |
| risky.biz | 1 | 0.02% |
| zdnet.com | 1 | 0.02% |
| fakti.bg | 1 | 0.02% |
| stcatharinesstandard.ca | 1 | 0.02% |
| therecord.com | 1 | 0.02% |
| thepeterboroughexaminer.com | 1 | 0.02% |
| hydrocarbonprocessing.com | 1 | 0.02% |
| winfuture.de | 1 | 0.02% |
| financial-news.co.uk | 1 | 0.02% |
| berliner-zeitung.de | 1 | 0.02% |
| ukrinform.ua | 1 | 0.02% |
| localnews8.com | 1 | 0.02% |
| kesq.com | 1 | 0.02% |
| openpr.com | 1 | 0.02% |
| datacenterknowledge.com | 1 | 0.02% |
| mirrorspectator.com | 1 | 0.02% |
| kotaku.com | 1 | 0.02% |
| explosion.com | 1 | 0.02% |
| wowo.com | 1 | 0.02% |
| news.china.com.cn | 1 | 0.02% |
| liputan6.com | 1 | 0.02% |
| webinars.govtech.com | 1 | 0.02% |
| cfi.net.cn | 1 | 0.02% |
| futures.cnfol.com | 1 | 0.02% |
| setn.com | 1 | 0.02% |
| mp.cnfol.com | 1 | 0.02% |
| finance.ifeng.com | 1 | 0.02% |
| stock.hexun.com | 1 | 0.02% |
| ec.ltn.com.tw | 1 | 0.02% |
| northcountrynow.com | 1 | 0.02% |
| business2community.com | 1 | 0.02% |
| infotechlead.com | 1 | 0.02% |
| clarin.com | 1 | 0.02% |
| wwwhatsnew.com | 1 | 0.02% |
| computerworld.pl | 1 | 0.02% |
| icij.org | 1 | 0.02% |
| tecnoandroid.it | 1 | 0.02% |
| arede.info | 1 | 0.02% |
| extra.ec | 1 | 0.02% |
| diariodemorelos.com | 1 | 0.02% |
| mobileidworld.com | 1 | 0.02% |
| inwestycje.pl | 1 | 0.02% |
| words.filippo.io | 1 | 0.02% |
| elpais.com.uy | 1 | 0.02% |
| quadratin.com.mx | 1 | 0.02% |
| nikkan.co.jp | 1 | 0.02% |
| statecollege.com | 1 | 0.02% |
| jowhar.com | 1 | 0.02% |
| ihalla.com | 1 | 0.02% |
| maharashtratimes.com | 1 | 0.02% |
| travelweekly.com.au | 1 | 0.02% |
| journalgazette.net | 1 | 0.02% |
| austinchronicle.com | 1 | 0.02% |
| ktvu.com | 1 | 0.02% |
| pitchfork.com | 1 | 0.02% |
| mathrubhumi.com | 1 | 0.02% |
| india.com | 1 | 0.02% |
| firstpost.com | 1 | 0.02% |
| thetoc.gr | 1 | 0.02% |
| loksatta.com | 1 | 0.02% |
| newsx.com | 1 | 0.02% |
| dantri.com.vn | 1 | 0.02% |
| bollywoodlife.com | 1 | 0.02% |
| world.kbs.co.kr | 1 | 0.02% |
| punjabitribuneonline.com | 1 | 0.02% |
| navbharattimes.indiatimes.com | 1 | 0.02% |
| bhaskar.com | 1 | 0.02% |
| gulte.com | 1 | 0.02% |
| idiva.com | 1 | 0.02% |
| pr.com | 1 | 0.02% |
| srilankasource.com | 1 | 0.02% |
| news8000.com | 1 | 0.02% |
| channelbuzz.ca | 1 | 0.02% |
| totaltele.com | 1 | 0.02% |
| dominicanrepublicpost.com | 1 | 0.02% |
| aljazeera.com | 1 | 0.02% |
| rte.ie | 1 | 0.02% |
| dcvelocity.com | 1 | 0.02% |
| californiatelegraph.com | 1 | 0.02% |
| republikein.com.na | 1 | 0.02% |
| bozemandailychronicle.com | 1 | 0.02% |
| bmmagazine.co.uk | 1 | 0.02% |
| vm.ru | 1 | 0.02% |
| metronews.ru | 1 | 0.02% |
| mngz.ru | 1 | 0.02% |
| cafebiz.vn | 1 | 0.02% |
| lgz.ru | 1 | 0.02% |
| canardpc.com | 1 | 0.02% |
| diyarbakirsoz.com | 1 | 0.02% |
| lakersnation.com | 1 | 0.02% |
| stockbiz.vn | 1 | 0.02% |
| lite987.com | 1 | 0.02% |
| 961theeagle.com | 1 | 0.02% |
| wibx950.com | 1 | 0.02% |
| southernhighlandnews.com.au | 1 | 0.02% |
| wgna.com | 1 | 0.02% |
| biz.cnews.ru | 1 | 0.02% |
| memeburn.com | 1 | 0.02% |
| igamingbusiness.com | 1 | 0.02% |
| helpconsumatori.it | 1 | 0.02% |
| themissouritimes.com | 1 | 0.02% |
| iraqsun.com | 1 | 0.02% |
| portalsamorzadowy.pl | 1 | 0.02% |
| nearshoreamericas.com | 1 | 0.02% |
| inquirer.com | 1 | 0.02% |
| thefrontierpost.com | 1 | 0.02% |
| upi.com | 1 | 0.02% |
| koreatimes.co.kr | 1 | 0.02% |
| dynamicbusiness.com | 1 | 0.02% |
| interaksyon.philstar.com | 1 | 0.02% |
| nbcmontana.com | 1 | 0.02% |
| clydebankpost.co.uk | 1 | 0.02% |
| tagesanzeiger.ch | 1 | 0.02% |
| mittelstandcafe.de | 1 | 0.02% |
| drimble.nl | 1 | 0.02% |
| nieuws.nl | 1 | 0.02% |
| vecernji.ba | 1 | 0.02% |
| juneesoutherncross.com.au | 1 | 0.02% |
| braidwoodtimes.com.au | 1 | 0.02% |
| armidaleexpress.com.au | 1 | 0.02% |
| crookwellgazette.com.au | 1 | 0.02% |
| theleader.com.au | 1 | 0.02% |
| thecourier.com.au | 1 | 0.02% |
| batemansbaypost.com.au | 1 | 0.02% |
| cootamundraherald.com.au | 1 | 0.02% |
| camdencourier.com.au | 1 | 0.02% |
| yasstribune.com.au | 1 | 0.02% |
| northerndailyleader.com.au | 1 | 0.02% |
| dailyadvertiser.com.au | 1 | 0.02% |
| mudgeeguardian.com.au | 1 | 0.02% |
| portnews.com.au | 1 | 0.02% |
| asahi.com | 1 | 0.02% |
| manningrivertimes.com.au | 1 | 0.02% |
| bluemountainsgazette.com.au | 1 | 0.02% |
| newcastleherald.com.au | 1 | 0.02% |
| inverelltimes.com.au | 1 | 0.02% |
| lithgowmercury.com.au | 1 | 0.02% |
| illawarramercury.com.au | 1 | 0.02% |
| tagesspiegel.de | 1 | 0.02% |
| thesunchronicle.com | 1 | 0.02% |
| indiatvnews.com | 1 | 0.02% |
| techstory.in | 1 | 0.02% |
| english.pravda.ru | 1 | 0.02% |
| daily-tribune.com | 1 | 0.02% |
| saltwire.com | 1 | 0.02% |
| afr.com | 1 | 0.02% |
| internetua.com | 1 | 0.02% |
| whmi.com | 1 | 0.02% |
| utilitydive.com | 1 | 0.02% |
| michigandaily.com | 1 | 0.02% |
| wdsu.com | 1 | 0.02% |
| blackseanews.net | 1 | 0.02% |
| podrobnosti.ua | 1 | 0.02% |
| island.lk | 1 | 0.02% |
| businessinsurance.com | 1 | 0.02% |
| polygon.com | 1 | 0.02% |
| aktivni.metropolitan.si | 1 | 0.02% |
| borsonline.hu | 1 | 0.02% |
| sc.stock.cnfol.com | 1 | 0.02% |
| mundoenlinea.cl | 1 | 0.02% |
| informationweek.com | 1 | 0.02% |
| investorplace.com | 1 | 0.02% |
| bgonair.bg | 1 | 0.02% |
| thehindubusinessline.com | 1 | 0.02% |
| blikk.hu | 1 | 0.02% |
| femina.hu | 1 | 0.02% |
| economx.hu | 1 | 0.02% |
| spartanavenue.com | 1 | 0.02% |
| theverge.com | 1 | 0.02% |
| chinesepress.com | 1 | 0.02% |
| kztv10.com | 1 | 0.02% |
| kristv.com | 1 | 0.02% |
| primerafuente.com.ar | 1 | 0.02% |
| nationalmortgagenews.com | 1 | 0.02% |
| larepubliquedespyrenees.fr | 1 | 0.02% |
| torquenews.com | 1 | 0.02% |
| scroll.in | 1 | 0.02% |
| money.it | 1 | 0.02% |
| toronto.citynews.ca | 1 | 0.02% |
| nrc.nl | 1 | 0.02% |
| elconfidencial.com | 1 | 0.02% |
| downtoearth.org.in | 1 | 0.02% |
| ly.fjsen.com | 1 | 0.02% |
| publico.pt | 1 | 0.02% |
| lagacetadesalamanca.es | 1 | 0.02% |
| weekend.perfil.com | 1 | 0.02% |
| jogja.tribunnews.com | 1 | 0.02% |
| kontrakty.ua | 1 | 0.02% |
| laut.de | 1 | 0.02% |
| cjme.com | 1 | 0.02% |
| megamodo.com | 1 | 0.02% |
| closermag.fr | 1 | 0.02% |
| elperiodicodearagon.com | 1 | 0.02% |
| comingsoon.it | 1 | 0.02% |
| fatimanews.com.br | 1 | 0.02% |
| kaos911.com | 1 | 0.02% |
| administradores.com.br | 1 | 0.02% |
| al-monitor.com | 1 | 0.02% |
| linux.org.ru | 1 | 0.02% |
| thenational.scot | 1 | 0.02% |
| marketintelligencecenter.com | 1 | 0.02% |
| dailyexcelsior.com | 1 | 0.02% |
| lina.sh | 1 | 0.02% |
| themoscowtimes.com | 1 | 0.02% |
| ko.com.ua | 1 | 0.02% |
| yorkpress.co.uk | 1 | 0.02% |
| ticweb.es | 1 | 0.02% |
| jagranjosh.com | 1 | 0.02% |
| 24sata.hr | 1 | 0.02% |
| net.hr | 1 | 0.02% |
| dp.ru | 1 | 0.02% |
| meridiano.net | 1 | 0.02% |
| gadgetsmagazine.com.ph | 1 | 0.02% |
| spacedaily.com | 1 | 0.02% |
| insight.scmagazineuk.com | 1 | 0.02% |
| 21stcenturywire.com | 1 | 0.02% |
| ghanaiantimes.com.gh | 1 | 0.02% |
| donews.com | 1 | 0.02% |
| tech.china.com | 1 | 0.02% |
| pakistantelegraph.com | 1 | 0.02% |
| birminghamstar.com | 1 | 0.02% |
| laosnews.net | 1 | 0.02% |
| newyorkstatesman.com | 1 | 0.02% |
| coloradostar.com | 1 | 0.02% |
| nashvilleherald.com | 1 | 0.02% |
| stlouisstar.com | 1 | 0.02% |
| saltlakecitysun.com | 1 | 0.02% |
| myanmarnews.net | 1 | 0.02% |
| utv.ie | 1 | 0.02% |
| eejournal.com | 1 | 0.02% |
| elektroniknet.de | 1 | 0.02% |
| thejournal.com | 1 | 0.02% |
| newrepublic.com | 1 | 0.02% |
| itbrief.news | 1 | 0.02% |
| rstreet.org | 1 | 0.02% |
| insidermonkey.com | 1 | 0.02% |
| wxow.com | 1 | 0.02% |
| mensxp.com | 1 | 0.02% |
| bianet.org | 1 | 0.02% |
| slugmag.com | 1 | 0.02% |
| wape.com | 1 | 0.02% |
| kiro7.com | 1 | 0.02% |
| 99jamzmiami.com | 1 | 0.02% |
| actionnewsjax.com | 1 | 0.02% |
| star945.com | 1 | 0.02% |
| y100fm.com | 1 | 0.02% |
| wftv.com | 1 | 0.02% |
| kono1011.com | 1 | 0.02% |
| 1055thedove.com | 1 | 0.02% |
| wsoctv.com | 1 | 0.02% |
| hits1053sanantonio.com | 1 | 0.02% |
| latele.ch | 1 | 0.02% |
| eaglesanantonio.com | 1 | 0.02% |
| wokv.com | 1 | 0.02% |
| powerorlando.com | 1 | 0.02% |
| 1015vibe.com | 1 | 0.02% |
| wpxi.com | 1 | 0.02% |
| b985.com | 1 | 0.02% |
| theboneonline.com | 1 | 0.02% |
| eagledayton.com | 1 | 0.02% |
| wgauradio.com | 1 | 0.02% |
| french.china.org.cn | 1 | 0.02% |
| mymagic949.com | 1 | 0.02% |
| kissrocks.com | 1 | 0.02% |
| magic1021.com | 1 | 0.02% |
| hits973.com | 1 | 0.02% |
| k991fm.com | 1 | 0.02% |
| journaldunet.com | 1 | 0.02% |
| lesmobiles.com | 1 | 0.02% |
| toffeeweb.com | 1 | 0.02% |
| 10tv.com | 1 | 0.02% |
| asianews.it | 1 | 0.02% |
| cp24.com | 1 | 0.02% |
| wshu.org | 1 | 0.02% |
| brandonsun.com | 1 | 0.02% |
| kiplinger.com | 1 | 0.02% |
| mactech.com | 1 | 0.02% |
| brooklyneagle.com | 1 | 0.02% |
| rtv.rs | 1 | 0.02% |
| niezalezna.pl | 1 | 0.02% |
| taz.de | 1 | 0.02% |
| dailypakistan.pk | 1 | 0.02% |
| wirtualnemedia.pl | 1 | 0.02% |
| twz.com | 1 | 0.02% |
| autoexpress.co.uk | 1 | 0.02% |
| studiob.rs | 1 | 0.02% |
| nin.rs | 1 | 0.02% |
| finans.mynet.com | 1 | 0.02% |
| sud.ua | 1 | 0.02% |
| newsnet5.com | 1 | 0.02% |
| labs.watchtowr.com | 1 | 0.02% |
| independent.co.uk | 1 | 0.02% |
| aliran.com | 1 | 0.02% |
| sharemanthan.in | 1 | 0.02% |
| sandiegouniontribune.com | 1 | 0.02% |
| reporterherald.com | 1 | 0.02% |
| theage.com.au | 1 | 0.02% |
| dglobe.com | 1 | 0.02% |
| echopress.com | 1 | 0.02% |
| placenorthwest.co.uk | 1 | 0.02% |
| troyrecord.com | 1 | 0.02% |
| spokesman.com | 1 | 0.02% |
| whittierdailynews.com | 1 | 0.02% |
| wboc.com | 1 | 0.02% |
| theindependent.co.zw | 1 | 0.02% |
| jamestown.org | 1 | 0.02% |
| wahpetondailynews.com | 1 | 0.02% |
| thehardtackle.com | 1 | 0.02% |
| sentinelandenterprise.com | 1 | 0.02% |
| dailytrust.com | 1 | 0.02% |
| bostonherald.com | 1 | 0.02% |
| dailyjournalonline.com | 1 | 0.02% |
| tvxs.gr | 1 | 0.02% |
| liberta.it | 1 | 0.02% |
| pressdemocrat.com | 1 | 0.02% |
| blogs.itmedia.co.jp | 1 | 0.02% |
| mochimag.com | 1 | 0.02% |
| ocregister.com | 1 | 0.02% |
| presstelegram.com | 1 | 0.02% |
| redlandsdailyfacts.com | 1 | 0.02% |
| timesofsandiego.com | 1 | 0.02% |
| the-miyanichi.co.jp | 1 | 0.02% |
| newsit.gr | 1 | 0.02% |
| postandcourier.com | 1 | 0.02% |
| gipedo.politis.com.cy | 1 | 0.02% |
| carolinajournal.com | 1 | 0.02% |
| wbkr.com | 1 | 0.02% |
| topics.or.jp | 1 | 0.02% |
| aspentimes.com | 1 | 0.02% |
| dailyuw.com | 1 | 0.02% |
| paymentweek.com | 1 | 0.02% |
| bfmtv.com | 1 | 0.02% |
| bigpara.hurriyet.com.tr | 1 | 0.02% |
| idrw.org | 1 | 0.02% |
| techtudo.com.br | 1 | 0.02% |
| dol.com.br | 1 | 0.02% |
| gamestar.de | 1 | 0.02% |
| t13.cl | 1 | 0.02% |
| kwcdcountry.com | 1 | 0.02% |
| choice.com.au | 1 | 0.02% |
| ostro.org | 1 | 0.02% |
| cincinnatisun.com | 1 | 0.02% |
| ohiostandard.com | 1 | 0.02% |
| oklahomastar.com | 1 | 0.02% |
| texasguardian.com | 1 | 0.02% |
| neworleanssun.com | 1 | 0.02% |
| tucsonpost.com | 1 | 0.02% |
| arabherald.com | 1 | 0.02% |
| greekherald.com | 1 | 0.02% |
| floridastatesman.com | 1 | 0.02% |
| hokkoku.co.jp | 1 | 0.02% |
| noviny.sk | 1 | 0.02% |
| cas.sk | 1 | 0.02% |
| econotimes.com | 1 | 0.02% |
| londonlovesbusiness.com | 1 | 0.02% |
| blogs.diariovasco.com | 1 | 0.02% |
| hespress.com | 1 | 0.02% |
| diariodeburgos.es | 1 | 0.02% |
| wosu.org | 1 | 0.02% |
| rtvutrecht.nl | 1 | 0.02% |
| chinapress.com.my | 1 | 0.02% |
| makaangola.org | 1 | 0.02% |
| eleco.com.ar | 1 | 0.02% |
| golosarmenii.am | 1 | 0.02% |
| countercurrents.org | 1 | 0.02% |
| israelherald.com | 1 | 0.02% |
| estadao.com.br | 1 | 0.02% |
| businessworld.in | 1 | 0.02% |
| financialafrik.com | 1 | 0.02% |
| hoy.es | 1 | 0.02% |
| eadt.co.uk | 1 | 0.02% |
| blog.wenxuecity.com | 1 | 0.02% |
| news.cts.com.tw | 1 | 0.02% |
| francetoday.com | 1 | 0.02% |
| nagpurtoday.in | 1 | 0.02% |
| scmp.com | 1 | 0.02% |
| corriereadriatico.it | 1 | 0.02% |
| dagensps.se | 1 | 0.02% |
| ici.fr | 1 | 0.02% |
| elmalaeb.com | 1 | 0.02% |
| pcchip.hr | 1 | 0.02% |
| kocaeligazetesi.com.tr | 1 | 0.02% |
| astroawani.com | 1 | 0.02% |
| merkur.de | 1 | 0.02% |
| pleinevie.fr | 1 | 0.02% |
| nile.eg | 1 | 0.02% |
| uzmanpara.milliyet.com.tr | 1 | 0.02% |
| q947fm.iheart.com | 1 | 0.02% |
| c101.iheart.com | 1 | 0.02% |
| siol.net | 1 | 0.02% |
| jeuneafrique.com | 1 | 0.02% |
| f1vilag.hu | 1 | 0.02% |
| larazon.es | 1 | 0.02% |
| damernasvarld.expressen.se | 1 | 0.02% |
| realitatea.net | 1 | 0.02% |
| rocketerie.iheart.com | 1 | 0.02% |
| 995thefox.iheart.com | 1 | 0.02% |
| 985thefox.iheart.com | 1 | 0.02% |
| wnnj.iheart.com | 1 | 0.02% |
| mebpersonel.com | 1 | 0.02% |
| german.china.org.cn | 1 | 0.02% |
| rock1067.iheart.com | 1 | 0.02% |
| piter.tv | 1 | 0.02% |
| jogjapolitan.harianjogja.com | 1 | 0.02% |
| leiphone.com | 1 | 0.02% |
| healthcareitnews.com | 1 | 0.02% |
| hackaday.com | 1 | 0.02% |
| blueprint.ng | 1 | 0.02% |
| son.tv | 1 | 0.02% |
| hometownstation.com | 1 | 0.02% |
| dakotawarcollege.com | 1 | 0.02% |
| navhindtimes.in | 1 | 0.02% |
| am1150.ca | 1 | 0.02% |
| theitem.com | 1 | 0.02% |
| wfmd.com | 1 | 0.02% |
| 24tv.ua | 1 | 0.02% |
| diariosigloxxi.com | 1 | 0.02% |
| radikal.com.tr | 1 | 0.02% |
| guelphmercury.com | 1 | 0.02% |
| crestonnews.com | 1 | 0.02% |
| thanhnien.vn | 1 | 0.02% |
| hawaiinewsnow.com | 1 | 0.02% |
| thegardenisland.com | 1 | 0.02% |
| thurrockgazette.co.uk | 1 | 0.02% |
| mix941kmxj.com | 1 | 0.02% |
| newsprom.ru | 1 | 0.02% |
| maldonandburnhamstandard.co.uk | 1 | 0.02% |
| clactonandfrintongazette.co.uk | 1 | 0.02% |
| notimerica.com | 1 | 0.02% |
| 13abc.com | 1 | 0.02% |
| newsminer.com | 1 | 0.02% |
| contractormag.com | 1 | 0.02% |
| thirdsector.co.uk | 1 | 0.02% |
| irishsun.com | 1 | 0.02% |
| indiagazette.com | 1 | 0.02% |
| londonmercury.com | 1 | 0.02% |
| washingtonexaminer.com | 1 | 0.02% |
| seekingalpha.com | 1 | 0.02% |
| thespec.com | 1 | 0.02% |
| siliconangle.com | 1 | 0.02% |
| kjzz.org | 1 | 0.02% |
| pontianak.tribunnews.com | 1 | 0.02% |
| scdaily.com | 1 | 0.02% |
| abclinuxu.cz | 1 | 0.02% |
| larepublica.pe | 1 | 0.02% |
| batam.tribunnews.com | 1 | 0.02% |
| jc.uol.com.br | 1 | 0.02% |
| diarioelargentino.com | 1 | 0.02% |
| citylimits.org | 1 | 0.02% |
| racismoambiental.net.br | 1 | 0.02% |
| gx94radio.com | 1 | 0.02% |
| vanguardia.com.mx | 1 | 0.02% |
| reporterdiario.com.br | 1 | 0.02% |
| avn.info.ve | 1 | 0.02% |
| thebftonline.com | 1 | 0.02% |
| santamariatimes.com | 1 | 0.02% |
| xx.sdnews.com.cn | 1 | 0.02% |
| elmundo.es | 1 | 0.02% |
| 620ckrm.com | 1 | 0.02% |
| mundiario.com | 1 | 0.02% |
| elcorreo.com | 1 | 0.02% |
| alo.rs | 1 | 0.02% |
| nbcwashington.com | 1 | 0.02% |
| thebusinessjournal.com | 1 | 0.02% |
| montereyherald.com | 1 | 0.02% |
| elpuntavui.cat | 1 | 0.02% |
| cope.es | 1 | 0.02% |
| thailand-business-news.com | 1 | 0.02% |
| taiwandaily.net | 1 | 0.02% |
| ktvl.com | 1 | 0.02% |
| katu.com | 1 | 0.02% |
| wgxa.tv | 1 | 0.02% |
| mynews4.com | 1 | 0.02% |
| vietnam.vnanet.vn | 1 | 0.02% |
| lematin.ma | 1 | 0.02% |
| abc6onyourside.com | 1 | 0.02% |
| midmichigannow.com | 1 | 0.02% |
| wgme.com | 1 | 0.02% |
| bamada.net | 1 | 0.02% |
| thecable.ng | 1 | 0.02% |
| chattanoogan.com | 1 | 0.02% |
| 9news.com.au | 1 | 0.02% |
| cbs6albany.com | 1 | 0.02% |
| eng.kavkaz-uzel.eu | 1 | 0.02% |
| thestar.com.my | 1 | 0.02% |
| sonara.net | 1 | 0.02% |
| cnycentral.com | 1 | 0.02% |
| news3lv.com | 1 | 0.02% |
| cbs2iowa.com | 1 | 0.02% |
| burgundywave.com | 1 | 0.02% |
| dailybulletin.com | 1 | 0.02% |
| wset.com | 1 | 0.02% |
| timesleader.com | 1 | 0.02% |
| understandingwar.org | 1 | 0.02% |
| radiotamazuj.org | 1 | 0.02% |
| tvline.com | 1 | 0.02% |
| wcbm.com | 1 | 0.02% |
| sbsun.com | 1 | 0.02% |
| t3n.de | 1 | 0.02% |
| lb.ua | 1 | 0.02% |
| riotimesonline.com | 1 | 0.02% |
| eenadu.net | 1 | 0.02% |
| stile.it | 1 | 0.02% |
| jiji.com | 1 | 0.02% |
| woman.excite.co.jp | 1 | 0.02% |
| pastemagazine.com | 1 | 0.02% |
| stripes.com | 1 | 0.02% |
| insidephilanthropy.com | 1 | 0.02% |
| hanasone.mainichi.jp | 1 | 0.02% |
| radioseoul1650.com | 1 | 0.02% |
| mpacorn.com | 1 | 0.02% |
| thecamarilloacorn.com | 1 | 0.02% |
| fansided.com | 1 | 0.02% |
| nigerianobservernews.com | 1 | 0.02% |
| monocle.com | 1 | 0.02% |
| thedailyworld.com | 1 | 0.02% |
| dailypost.ng | 1 | 0.02% |
| ninersnation.com | 1 | 0.02% |
| hbook.com | 1 | 0.02% |
| fool.ca | 1 | 0.02% |
| kazokuchannel.doorblog.jp | 1 | 0.02% |
| ruthfullyyours.com | 1 | 0.02% |
| ligaportal.at | 1 | 0.02% |
| newsitaliane.it | 1 | 0.02% |
| j-cast.com | 1 | 0.02% |
| 373news.com | 1 | 0.02% |
| townandcountrymag.com | 1 | 0.02% |
| ivpressonline.com | 1 | 0.02% |
| lancashiretelegraph.co.uk | 1 | 0.02% |
| burytimes.co.uk | 1 | 0.02% |
| wapt.com | 1 | 0.02% |
| vv.com.ua | 1 | 0.02% |
| qzwb.com | 1 | 0.02% |
| timeshighereducation.com | 1 | 0.02% |
| journaldugeek.com | 1 | 0.02% |
| anf-news.com | 1 | 0.02% |
| bloomberght.com | 1 | 0.02% |
| f5haber.com | 1 | 0.02% |
| haberankara.com | 1 | 0.02% |
| habermeydan.com | 1 | 0.02% |
| haber61.net | 1 | 0.02% |
| ferra.ru | 1 | 0.02% |
| yenialanya.com | 1 | 0.02% |
| haberaktuel.com | 1 | 0.02% |
| iphoneaddict.fr | 1 | 0.02% |
| ozgurkocaeli.com.tr | 1 | 0.02% |
| kamuajans.com | 1 | 0.02% |
| haber.mynet.com | 1 | 0.02% |
| vice.com | 1 | 0.02% |
| myhostnews.com | 1 | 0.02% |
| wfaa.com | 1 | 0.02% |
| news.cyol.com | 1 | 0.02% |
| cqnews.net | 1 | 0.02% |
| banglanews24.today | 1 | 0.02% |
| ifj.org | 1 | 0.02% |
| en.dailypakistan.com.pk | 1 | 0.02% |
| stiintasitehnica.com | 1 | 0.02% |
| tazabek.kg | 1 | 0.02% |
| pratahkal.com | 1 | 0.02% |
| heraldscotland.com | 1 | 0.02% |
| hartvannederland.nl | 1 | 0.02% |
| wsbradio.com | 1 | 0.02% |
| tageblatt.lu | 1 | 0.02% |
| romaniatv.net | 1 | 0.02% |
| jurnalul.ro | 1 | 0.02% |
| lewrockwell.com | 1 | 0.02% |
| anbariloche.com.ar | 1 | 0.02% |
| eldiariomontanes.es | 1 | 0.02% |
| greenme.it | 1 | 0.02% |
| elvocero.com | 1 | 0.02% |
| e.dennikn.sk | 1 | 0.02% |
| zdg.md | 1 | 0.02% |
| akhbarelyom.com | 1 | 0.02% |
| elcorreodeburgos.com | 1 | 0.02% |
| diumenge.ara.cat | 1 | 0.02% |
| canal26.com | 1 | 0.02% |
| ara.cat | 1 | 0.02% |
| philenews.com | 1 | 0.02% |
| ugandaonline.net | 1 | 0.02% |
| talouselama.fi | 1 | 0.02% |
| antena3.com | 1 | 0.02% |
| walesonline.co.uk | 1 | 0.02% |
| bolognatoday.it | 1 | 0.02% |
| tercerainformacion.es | 1 | 0.02% |
| pronto.com.ar | 1 | 0.02% |
| adgully.com | 1 | 0.02% |
| catanzaroinforma.it | 1 | 0.02% |
| theeagleonline.com.ng | 1 | 0.02% |
| newsday.co.zw | 1 | 0.02% |
| egyptindependent.com | 1 | 0.02% |
| dialogos.com.cy | 1 | 0.02% |
| forbes.ru | 1 | 0.02% |
| spiegel.de | 1 | 0.02% |
| athina984.gr | 1 | 0.02% |
| geekzone.co.nz | 1 | 0.02% |
| laprovence.com | 1 | 0.02% |
| ilsimplicissimus2.com | 1 | 0.02% |
| kath.net | 1 | 0.02% |
| jhm.fr | 1 | 0.02% |
| merdeka.com | 1 | 0.02% |
| okaz.com.sa | 1 | 0.02% |
| az-online.de | 1 | 0.02% |
| hindi.moneycontrol.com | 1 | 0.02% |
| kyivpost.com | 1 | 0.02% |
| quotidianodipuglia.it | 1 | 0.02% |
| bresciaoggi.it | 1 | 0.02% |
| tuttomercatoweb.com | 1 | 0.02% |
| rodiaki.gr | 1 | 0.02% |
| pcwelt.de | 1 | 0.02% |
| cyprus-mail.com | 1 | 0.02% |
| eleftherostypos.gr | 1 | 0.02% |
| sbctv.gr | 1 | 0.02% |
| livelaw.in | 1 | 0.02% |
| games.24tv.ua | 1 | 0.02% |
| bloodhorse.com | 1 | 0.02% |
| pressian.com | 1 | 0.02% |
| book.asahi.com | 1 | 0.02% |
| pocket-lint.com | 1 | 0.02% |
| shtfplan.com | 1 | 0.02% |
| kenyastar.com | 1 | 0.02% |
| kibrisgazetesi.com | 1 | 0.02% |
| hongkongherald.com | 1 | 0.02% |
| business-review.eu | 1 | 0.02% |
| timeturk.com | 1 | 0.02% |
| gundemkibris.com | 1 | 0.02% |
| zavtra.ru | 1 | 0.02% |
| times-standard.com | 1 | 0.02% |
| abc.net.au | 1 | 0.02% |
| krone.at | 1 | 0.02% |
| wyomingnews.com | 1 | 0.02% |
| timesfreepress.com | 1 | 0.02% |
| piacesprofit.hu | 1 | 0.02% |
| newhamburgindependent.ca | 1 | 0.02% |
| wz-net.de | 1 | 0.02% |
| pakobserver.net | 1 | 0.02% |
| cesky.radio.cz | 1 | 0.02% |
| campbell.edu | 1 | 0.02% |
| morgenpost.de | 1 | 0.02% |
| newsmonkey.be | 1 | 0.02% |
| cherokeescout.com | 1 | 0.02% |
| prabhasakshi.com | 1 | 0.02% |
| elpatagonico.com | 1 | 0.02% |
| pronedra.ru | 1 | 0.02% |
| vernonmorningstar.com | 1 | 0.02% |
| ultimahora.es | 1 | 0.02% |
| kboo.fm | 1 | 0.02% |
| publimetro.com.mx | 1 | 0.02% |
| brazilsun.com | 1 | 0.02% |
| elperiodico.cat | 1 | 0.02% |
| theshillongtimes.com | 1 | 0.02% |
| observador.pt | 1 | 0.02% |
| ilgiorno.it | 1 | 0.02% |
| tribuna.com.mx | 1 | 0.02% |
| acento.com.do | 1 | 0.02% |
| elperiodico.com.do | 1 | 0.02% |
| novinite.com | 1 | 0.02% |
| perspectivasur.com | 1 | 0.02% |
| naturalnews.com | 1 | 0.02% |
| kcentv.com | 1 | 0.02% |
| letemps.ch | 1 | 0.02% |
| diariovasco.com | 1 | 0.02% |
| adn.com | 1 | 0.02% |
| chinatechnews.com | 1 | 0.02% |
| yankton.net | 1 | 0.02% |
| minuto30.com | 1 | 0.02% |
| 9tv.co.il | 1 | 0.02% |
| agenciagov.ebc.com.br | 1 | 0.02% |
| publico.es | 1 | 0.02% |
| warrackherald.com.au | 1 | 0.02% |
| agi.it | 1 | 0.02% |
| polityka.pl | 1 | 0.02% |
| ennaharonline.com | 1 | 0.02% |
| almontasaf.net | 1 | 0.02% |
| aawsat.com | 1 | 0.02% |
| albayan.ae | 1 | 0.02% |
| healthimpactnews.com | 1 | 0.02% |
| maravipost.com | 1 | 0.02% |
| oe24.at | 1 | 0.02% |
| emaratalyoum.com | 1 | 0.02% |
| watfordobserver.co.uk | 1 | 0.02% |
| sherwoodparknews.com | 1 | 0.02% |
| derbund.ch | 1 | 0.02% |
| pelop.gr | 1 | 0.02% |
| dailyheraldtribune.com | 1 | 0.02% |
| gazetaexpress.com | 1 | 0.02% |
| kincardinenews.com | 1 | 0.02% |
| devondispatch.ca | 1 | 0.02% |
| wiartonecho.com | 1 | 0.02% |
| morungexpress.com | 1 | 0.02% |
| huffingtonpost.co.uk | 1 | 0.02% |
| progressive-charlestown.com | 1 | 0.02% |
| wlos.com | 1 | 0.02% |
| cbnews.fr | 1 | 0.02% |
| sangbadpratidin.in | 1 | 0.02% |
| expert.ru | 1 | 0.02% |
| chilecomparte.cl | 1 | 0.02% |
| iafrica.com | 1 | 0.02% |
| mekomi.walla.co.il | 1 | 0.02% |
| arynews.tv | 1 | 0.02% |
| parrysound.com | 1 | 0.02% |
| newuniversity.org | 1 | 0.02% |
| pplware.sapo.pt | 1 | 0.02% |
| manoramanews.com | 1 | 0.02% |
| pc.co.il | 1 | 0.02% |
| gunes.com | 1 | 0.02% |
| zvw.de | 1 | 0.02% |
| wral.com | 1 | 0.02% |
| en.globes.co.il | 1 | 0.02% |
| portfolio.hu | 1 | 0.02% |
| abcnyheter.no | 1 | 0.02% |
| bollywoodhungama.com | 1 | 0.02% |
| chaozhoudaily.com | 1 | 0.02% |
| eeo.com.cn | 1 | 0.02% |
| challenges.fr | 1 | 0.02% |
| blitzquotidiano.it | 1 | 0.02% |
| rtp.pt | 1 | 0.02% |
| mdzol.com | 1 | 0.02% |
| businessonline.it | 1 | 0.02% |
| english.elpais.com | 1 | 0.02% |
| tribunademinas.com.br | 1 | 0.02% |
| dailyrecord.co.uk | 1 | 0.02% |
| washingtonmonthly.com | 1 | 0.02% |
| cosmopolitan.com | 1 | 0.02% |
| capitalethiopia.com | 1 | 0.02% |
| politicamentecorretto.com | 1 | 0.02% |
| nakedcapitalism.com | 1 | 0.02% |
| geo.tv | 1 | 0.02% |
| news.ifeng.com | 1 | 0.02% |
| yourtango.com | 1 | 0.02% |
| blog.detail.dev | 1 | 0.02% |
| praca.egospodarka.pl | 1 | 0.02% |
| taxydromos.gr | 1 | 0.02% |
| dailymaverick.co.za | 1 | 0.02% |
| jutarnji.hr | 1 | 0.02% |
| unsertirol24.com | 1 | 0.02% |
| morningstaronline.co.uk | 1 | 0.02% |
| alfajertv.com | 1 | 0.02% |
| finance.walla.co.il | 1 | 0.02% |
| beveiligingnieuws.nl | 1 | 0.02% |
| aiwaegypt.com | 1 | 0.02% |
| suedtirolnews.it | 1 | 0.02% |
| ladepeche.fr | 1 | 0.02% |
| voria.gr | 1 | 0.02% |
| kikar.co.il | 1 | 0.02% |
| lapresse.tn | 1 | 0.02% |
| military.com | 1 | 0.02% |
| ilfattonisseno.it | 1 | 0.02% |
| newscentralasia.net | 1 | 0.02% |
| root.cz | 1 | 0.02% |
| tickerreport.com | 1 | 0.02% |
| wpdh.com | 1 | 0.02% |
| sanook.com | 1 | 0.02% |
| yerkir.am | 1 | 0.02% |
| haberts.com | 1 | 0.02% |
| mobeigi.com | 1 | 0.02% |
| vz.lt | 1 | 0.02% |
| technologyreview.com | 1 | 0.02% |
| mynet.com | 1 | 0.02% |
| forum.ixbt.com | 1 | 0.02% |
| ogunhaber.com | 1 | 0.02% |
| m.metroseoul.co.kr | 1 | 0.02% |
| 26sep.net | 1 | 0.02% |
| banklesstimes.com | 1 | 0.02% |
| pharmiweb.com | 1 | 0.02% |
| tonyskansascity.com | 1 | 0.02% |
| deccanchronicle.com | 1 | 0.02% |
| echo-news.co.uk | 1 | 0.02% |
| newsghana.com.gh | 1 | 0.02% |
| middleeasteye.net | 1 | 0.02% |
| wlz-online.de | 1 | 0.02% |
| cawalisse.com | 1 | 0.02% |
| bnnbloomberg.ca | 1 | 0.02% |
| patrasevents.gr | 1 | 0.02% |
| neviditelnypes.lidovky.cz | 1 | 0.02% |
| namibian.com.na | 1 | 0.02% |
| klack.de | 1 | 0.02% |
| sott.net | 1 | 0.02% |
| oz-online.de | 1 | 0.02% |
| pressafrik.com | 1 | 0.02% |
| ilmessaggero.it | 1 | 0.02% |
| yle.fi | 1 | 0.02% |
| cursdeguvernare.ro | 1 | 0.02% |
| libertatea.ro | 1 | 0.02% |
| dn.se | 1 | 0.02% |
| local21news.com | 1 | 0.02% |
| metro.co.uk | 1 | 0.02% |
| kreisbote.de | 1 | 0.02% |
| manchestereveningnews.co.uk | 1 | 0.02% |
| echoroukonline.com | 1 | 0.02% |
| organiser.org | 1 | 0.02% |
| calciomercato.com | 1 | 0.02% |
| karfitsa.gr | 1 | 0.02% |
| wgal.com | 1 | 0.02% |
| wmtw.com | 1 | 0.02% |
| iwate-np.co.jp | 1 | 0.02% |
| megatv.com | 1 | 0.02% |
| saratogian.com | 1 | 0.02% |
| comicbook.com | 1 | 0.02% |
| pentictonherald.ca | 1 | 0.02% |
| oneidadispatch.com | 1 | 0.02% |
| patheos.com | 1 | 0.02% |
| pineandlakes.com | 1 | 0.02% |
| minyu-net.com | 1 | 0.02% |
| agara.co.jp | 1 | 0.02% |
| citizenlab.ca | 1 | 0.02% |
| freiburg.de | 1 | 0.02% |
| elperiodico.com | 1 | 0.02% |
| webwire.com | 1 | 0.02% |
| smallwarsjournal.com | 1 | 0.02% |
| burgasinfo.com | 1 | 0.02% |
| news.finance.ua | 1 | 0.02% |
| tempo.co | 1 | 0.02% |
| atlantico.fr | 1 | 0.02% |
| novinite.bg | 1 | 0.02% |
| thesalemnewsonline.com | 1 | 0.02% |
| theadvocate.com.au | 1 | 0.02% |
| punto-informatico.it | 1 | 0.02% |
| m.kauno.diena.lt | 1 | 0.02% |
| 15min.lt | 1 | 0.02% |
| klaipeda.diena.lt | 1 | 0.02% |
| it-business.de | 1 | 0.02% |
| nwzonline.de | 1 | 0.02% |
| reseller.co.nz | 1 | 0.02% |
| biobiochile.cl | 1 | 0.02% |
| globalissues.org | 1 | 0.02% |
| ziarulnational.md | 1 | 0.02% |
| euronews.com | 1 | 0.02% |
| politico.eu | 1 | 0.02% |
| diaridegirona.cat | 1 | 0.02% |
| wrmf.com | 1 | 0.02% |
| theconversation.com | 1 | 0.02% |
| dutchitchannel.nl | 1 | 0.02% |
| sciencesetavenir.fr | 1 | 0.02% |
| talcualdigital.com | 1 | 0.02% |
| newsbeast.gr | 1 | 0.02% |
| informacion.es | 1 | 0.02% |
| hkcna.hk | 1 | 0.02% |
| puntonoticias.com | 1 | 0.02% |
| clevescene.com | 1 | 0.02% |
| sbnation.com | 1 | 0.02% |
| cuartopoder.mx | 1 | 0.02% |
| globalsecurity.org | 1 | 0.02% |
| stranieriinitalia.it | 1 | 0.02% |
| correiodobrasil.com.br | 1 | 0.02% |
| weltwoche.ch | 1 | 0.02% |
| recorderonline.com | 1 | 0.02% |
| laois-nationalist.ie | 1 | 0.02% |
| breakingnews.ie | 1 | 0.02% |
| tdg.ch | 1 | 0.02% |
| 20min.ch | 1 | 0.02% |
| navabharat.com | 1 | 0.02% |
| dongascience.com | 1 | 0.02% |
| gazzetta.gr | 1 | 0.02% |
| vir.com.vn | 1 | 0.02% |
| telefonino.net | 1 | 0.02% |
| warontherocks.com | 1 | 0.02% |
| epikaira.gr | 1 | 0.02% |
| borsaitaliana.it | 1 | 0.02% |
| ultimahora.com | 1 | 0.02% |
| tradersmagazine.com | 1 | 0.02% |
| artvoice.com | 1 | 0.02% |
| ricentral.com | 1 | 0.02% |
| herald-dispatch.com | 1 | 0.02% |
| cachevalleydaily.com | 1 | 0.02% |
| the-dispatch.com | 1 | 0.02% |
| nhonews.com | 1 | 0.02% |
| news-expressky.com | 1 | 0.02% |
| coronadonewsca.com | 1 | 0.02% |
| macg.co | 1 | 0.02% |
| lecourrier.vn | 1 | 0.02% |
| lamarseillaise.fr | 1 | 0.02% |
| hellenicnews.com | 1 | 0.02% |
| reformer.com | 1 | 0.02% |
| nvdaily.com | 1 | 0.02% |
| newsday.com | 1 | 0.02% |
| k-tipos.gr | 1 | 0.02% |
| eyemagazine.com | 1 | 0.02% |
| quinewspisa.it | 1 | 0.02% |
| news.kbs.co.kr | 1 | 0.02% |
| nspna.com | 1 | 0.02% |
| skai.gr | 1 | 0.02% |
| allaboutthejersey.com | 1 | 0.02% |
| ign.com | 1 | 0.02% |
| j-town.net | 1 | 0.02% |

## Source Distribution

| source_type | source_name | rows | percent_dataset | percent_source_type |
| --- | --- | --- | --- | --- |
| cve | NVD CVE | 1295 | 24.60% | 100.00% |
| reddit_rss | cybersecurity | 243 | 4.62% | 27.00% |
| reddit_rss | sysadmin | 182 | 3.46% | 20.22% |
| reddit_rss | blueteamsec | 108 | 2.05% | 12.00% |
| reddit_rss | privacy | 108 | 2.05% | 12.00% |
| news_rss | The Hacker News | 70 | 1.33% | 33.33% |
| reddit_rss | hacking | 51 | 0.97% | 5.67% |
| news_rss | BleepingComputer | 48 | 0.91% | 22.86% |
| reddit_rss | ReverseEngineering | 44 | 0.84% | 4.89% |
| reddit_rss | netsec | 40 | 0.76% | 4.44% |
| news_api | forbes.com | 35 | 0.66% | 1.22% |
| news_api | ascii.jp | 34 | 0.65% | 1.19% |
| reddit_rss | AskNetsec | 34 | 0.65% | 3.78% |
| reddit_rss | osint | 34 | 0.65% | 3.78% |
| news_api | techradar.com | 31 | 0.59% | 1.08% |
| reddit_rss | Malware | 30 | 0.57% | 3.33% |
| reddit_rss | ComputerSecurity | 26 | 0.49% | 2.89% |
| news_api | cnews.ru | 24 | 0.46% | 0.84% |
| news_api | ithome.com.tw | 23 | 0.44% | 0.80% |
| news_rss | Rapid7 Blog | 23 | 0.44% | 10.95% |
| news_api | boredpanda.com | 21 | 0.40% | 0.73% |
| news_api | haberler.com | 21 | 0.40% | 0.73% |
| news_api | fnnews.com | 20 | 0.38% | 0.70% |
| news_api | itbrief.co.nz | 19 | 0.36% | 0.66% |
| news_api | rpp.pe | 19 | 0.36% | 0.66% |
| news_api | theregister.com | 19 | 0.36% | 0.66% |
| news_api | bankinfosecurity.com | 18 | 0.34% | 0.63% |
| news_api | 163.com | 17 | 0.32% | 0.59% |
| news_rss | Unit 42 | 17 | 0.32% | 8.10% |
| news_api | manilatimes.net | 16 | 0.30% | 0.56% |
| news_rss | Cisco Talos Blog | 16 | 0.30% | 7.62% |
| news_rss | SANS Internet Storm Center | 16 | 0.30% | 7.62% |
| news_api | dostor.org | 14 | 0.27% | 0.49% |
| news_api | govinfosecurity.com | 14 | 0.27% | 0.49% |
| news_api | biz.heraldcorp.com | 13 | 0.25% | 0.45% |
| news_api | cointelegraph.com | 13 | 0.25% | 0.45% |
| news_api | finance.sina.com.cn | 13 | 0.25% | 0.45% |
| news_api | el-balad.com | 12 | 0.23% | 0.42% |
| news_api | esecurityplanet.com | 12 | 0.23% | 0.42% |
| news_api | fool.com | 12 | 0.23% | 0.42% |
| news_api | baijiahao.baidu.com | 11 | 0.21% | 0.38% |
| news_api | economictimes.indiatimes.com | 11 | 0.21% | 0.38% |
| news_api | excite.co.jp | 11 | 0.21% | 0.38% |
| news_api | finanznachrichten.de | 11 | 0.21% | 0.38% |
| news_api | moneycontrol.com | 11 | 0.21% | 0.38% |
| news_rss | KrebsOnSecurity | 11 | 0.21% | 5.24% |
| news_api | csoonline.com | 10 | 0.19% | 0.35% |
| news_api | edaily.co.kr | 10 | 0.19% | 0.35% |
| news_api | finance.yahoo.com | 10 | 0.19% | 0.35% |
| news_api | jdsupra.com | 10 | 0.19% | 0.35% |
| news_api | techcrunch.com | 10 | 0.19% | 0.35% |
| news_api | infosecurity-magazine.com | 9 | 0.17% | 0.31% |
| news_api | securitylab.ru | 9 | 0.17% | 0.31% |
| news_api | timesofindia.indiatimes.com | 9 | 0.17% | 0.31% |
| news_api | zazoom.it | 9 | 0.17% | 0.31% |
| news_api | zdnet.co.kr | 9 | 0.17% | 0.31% |
| news_rss | Google Project Zero | 9 | 0.17% | 4.29% |
| news_api | channellife.co.nz | 8 | 0.15% | 0.28% |
| news_api | ddaily.co.kr | 8 | 0.15% | 0.28% |
| news_api | inewsgr.com | 8 | 0.15% | 0.28% |
| news_api | itwire.com | 8 | 0.15% | 0.28% |
| news_api | prnewswire.com | 8 | 0.15% | 0.28% |
| news_api | yahoo.com | 8 | 0.15% | 0.28% |
| news_api | bankingnews.gr | 7 | 0.13% | 0.24% |
| news_api | birgun.net | 7 | 0.13% | 0.24% |
| news_api | collider.com | 7 | 0.13% | 0.24% |
| news_api | eturbonews.com | 7 | 0.13% | 0.24% |
| news_api | govtech.com | 7 | 0.13% | 0.24% |
| news_api | sabah.com.tr | 7 | 0.13% | 0.24% |
| news_api | aa.com.tr | 6 | 0.11% | 0.21% |
| news_api | ensonhaber.com | 6 | 0.11% | 0.21% |
| news_api | foxnews.com | 6 | 0.11% | 0.21% |
| news_api | laopcion.com.mx | 6 | 0.11% | 0.21% |
| news_api | n-tv.de | 6 | 0.11% | 0.21% |
| news_api | natlawreview.com | 6 | 0.11% | 0.21% |
| news_api | punchng.com | 6 | 0.11% | 0.21% |
| news_api | screenrant.com | 6 | 0.11% | 0.21% |
| news_api | tvguide.co.uk | 6 | 0.11% | 0.21% |
| news_api | udayavani.com | 6 | 0.11% | 0.21% |
| news_api | vz.ru | 6 | 0.11% | 0.21% |
| news_api | anlatilaninotesi.com.tr | 5 | 0.09% | 0.17% |
| news_api | bd-pratidin.com | 5 | 0.09% | 0.17% |
| news_api | busan.com | 5 | 0.09% | 0.17% |
| news_api | channellife.com.au | 5 | 0.09% | 0.17% |
| news_api | coindesk.com | 5 | 0.09% | 0.17% |
| news_api | divyabhaskar.co.in | 5 | 0.09% | 0.17% |
| news_api | etoday.co.kr | 5 | 0.09% | 0.17% |
| news_api | europapress.es | 5 | 0.09% | 0.17% |
| news_api | evrensel.net | 5 | 0.09% | 0.17% |
| news_api | heise.de | 5 | 0.09% | 0.17% |
| news_api | hothardware.com | 5 | 0.09% | 0.17% |
| news_api | ibtimes.com.au | 5 | 0.09% | 0.17% |
| news_api | japan.zdnet.com | 5 | 0.09% | 0.17% |
| news_api | maliactu.net | 5 | 0.09% | 0.17% |
| news_api | marketscreener.com | 5 | 0.09% | 0.17% |
| news_api | milliyet.com.tr | 5 | 0.09% | 0.17% |
| news_api | newkerala.com | 5 | 0.09% | 0.17% |
| news_api | pcmag.com | 5 | 0.09% | 0.17% |
| news_api | segye.com | 5 | 0.09% | 0.17% |
| news_api | shorouknews.com | 5 | 0.09% | 0.17% |
| news_api | theglobeandmail.com | 5 | 0.09% | 0.17% |
| news_api | time.mk | 5 | 0.09% | 0.17% |
| news_api | vetogate.com | 5 | 0.09% | 0.17% |
| news_api | yorkregion.com | 5 | 0.09% | 0.17% |
| news_api | 9to5mac.com | 4 | 0.08% | 0.14% |
| news_api | abc.es | 4 | 0.08% | 0.14% |
| news_api | aceshowbiz.com | 4 | 0.08% | 0.14% |
| news_api | aljazeera.net | 4 | 0.08% | 0.14% |
| news_api | alquds.co.uk | 4 | 0.08% | 0.14% |
| news_api | boerse-express.com | 4 | 0.08% | 0.14% |
| news_api | bursadabugun.com | 4 | 0.08% | 0.14% |
| news_api | cambridgetimes.ca | 4 | 0.08% | 0.14% |
| news_api | cbc.ca | 4 | 0.08% | 0.14% |
| news_api | cnnturk.com | 4 | 0.08% | 0.14% |
| news_api | computing.co.uk | 4 | 0.08% | 0.14% |
| news_api | freepressjournal.in | 4 | 0.08% | 0.14% |
| news_api | gdnonline.com | 4 | 0.08% | 0.14% |
| news_api | ghanamma.com | 4 | 0.08% | 0.14% |
| news_api | haksozhaber.net | 4 | 0.08% | 0.14% |
| news_api | iefimerida.gr | 4 | 0.08% | 0.14% |
| news_api | insurancebusinessmag.com | 4 | 0.08% | 0.14% |
| news_api | interfax.ru | 4 | 0.08% | 0.14% |
| news_api | it-online.co.za | 4 | 0.08% | 0.14% |
| news_api | itnews.com.au | 4 | 0.08% | 0.14% |
| news_api | itnewsonline.com | 4 | 0.08% | 0.14% |
| news_api | itweb.co.za | 4 | 0.08% | 0.14% |
| news_api | kibrispostasi.com | 4 | 0.08% | 0.14% |
| news_api | mainichi.jp | 4 | 0.08% | 0.14% |
| news_api | mashable.com | 4 | 0.08% | 0.14% |
| news_api | mirror.co.uk | 4 | 0.08% | 0.14% |
| news_api | natalie.mu | 4 | 0.08% | 0.14% |
| news_api | newjerseytelegraph.com | 4 | 0.08% | 0.14% |
| news_api | newspim.com | 4 | 0.08% | 0.14% |
| news_api | newsway.co.kr | 4 | 0.08% | 0.14% |
| news_api | nypost.com | 4 | 0.08% | 0.14% |
| news_api | pravda.ru | 4 | 0.08% | 0.14% |
| news_api | sapo.pt | 4 | 0.08% | 0.14% |
| news_api | scoop.co.nz | 4 | 0.08% | 0.14% |
| news_api | simcoe.com | 4 | 0.08% | 0.14% |
| news_api | sozcu.com.tr | 4 | 0.08% | 0.14% |
| news_api | straitstimes.com | 4 | 0.08% | 0.14% |
| news_api | sudanile.com | 4 | 0.08% | 0.14% |
| news_api | tgrthaber.com | 4 | 0.08% | 0.14% |
| news_api | thefastmode.com | 4 | 0.08% | 0.14% |
| news_api | thenews.com.pk | 4 | 0.08% | 0.14% |
| news_api | thenextweb.com | 4 | 0.08% | 0.14% |
| news_api | tn.com.ar | 4 | 0.08% | 0.14% |
| news_api | trthaber.com | 4 | 0.08% | 0.14% |
| news_api | turkiyegazetesi.com.tr | 4 | 0.08% | 0.14% |
| news_api | ura.news | 4 | 0.08% | 0.14% |
| news_api | vanguardngr.com | 4 | 0.08% | 0.14% |
| news_api | vol.at | 4 | 0.08% | 0.14% |
| news_api | welt.de | 4 | 0.08% | 0.14% |
| news_api | winnipegfreepress.com | 4 | 0.08% | 0.14% |
| news_api | wired.com | 4 | 0.08% | 0.14% |
| news_api | wmur.com | 4 | 0.08% | 0.14% |
| news_api | yeniakit.com.tr | 4 | 0.08% | 0.14% |
| news_api | albiladpress.com | 3 | 0.06% | 0.10% |
| news_api | alltoc.com | 3 | 0.06% | 0.10% |
| news_api | am.com.mx | 3 | 0.06% | 0.10% |
| news_api | androidauthority.com | 3 | 0.06% | 0.10% |
| news_api | aninews.in | 3 | 0.06% | 0.10% |
| news_api | antimafiaduemila.com | 3 | 0.06% | 0.10% |
| news_api | biometricupdate.com | 3 | 0.06% | 0.10% |
| news_api | bleedingcool.com | 3 | 0.06% | 0.10% |
| news_api | business.scoop.co.nz | 3 | 0.06% | 0.10% |
| news_api | businessday.co.za | 3 | 0.06% | 0.10% |
| news_api | capital.ro | 3 | 0.06% | 0.10% |
| news_api | ciudadccs.info | 3 | 0.06% | 0.10% |
| news_api | claimsjournal.com | 3 | 0.06% | 0.10% |
| news_api | dailymail.com | 3 | 0.06% | 0.10% |
| news_api | dailypolitical.com | 3 | 0.06% | 0.10% |
| news_api | defensenews.com | 3 | 0.06% | 0.10% |
| news_api | donanimgunlugu.com | 3 | 0.06% | 0.10% |
| news_api | dw.com | 3 | 0.06% | 0.10% |
| news_api | eldiariodechihuahua.mx | 3 | 0.06% | 0.10% |
| news_api | elsiglodetorreon.com.mx | 3 | 0.06% | 0.10% |
| news_api | eluniversal.com.mx | 3 | 0.06% | 0.10% |
| news_api | etnews.com | 3 | 0.06% | 0.10% |
| news_api | eurasiareview.com | 3 | 0.06% | 0.10% |
| news_api | eurointegration.com.ua | 3 | 0.06% | 0.10% |
| news_api | europesun.com | 3 | 0.06% | 0.10% |
| news_api | finance.eastmoney.com | 3 | 0.06% | 0.10% |
| news_api | focus.de | 3 | 0.06% | 0.10% |
| news_api | glavcom.ua | 3 | 0.06% | 0.10% |
| news_api | globalnews.ca | 3 | 0.06% | 0.10% |
| news_api | habervitrini.com | 3 | 0.06% | 0.10% |
| news_api | hani.co.kr | 3 | 0.06% | 0.10% |
| news_api | hindustantimes.com | 3 | 0.06% | 0.10% |
| news_api | ianslive.in | 3 | 0.06% | 0.10% |
| news_api | index.hu | 3 | 0.06% | 0.10% |
| news_api | inews24.com | 3 | 0.06% | 0.10% |
| news_api | insideottawavalley.com | 3 | 0.06% | 0.10% |
| news_api | itbear.com.cn | 3 | 0.06% | 0.10% |
| news_api | itbusinessnet.com | 3 | 0.06% | 0.10% |
| news_api | kmib.co.kr | 3 | 0.06% | 0.10% |
| news_api | koreaherald.com | 3 | 0.06% | 0.10% |
| news_api | makeuseof.com | 3 | 0.06% | 0.10% |
| news_api | miragenews.com | 3 | 0.06% | 0.10% |
| news_api | modernghana.com | 3 | 0.06% | 0.10% |
| news_api | mondaq.com | 3 | 0.06% | 0.10% |
| news_api | munhwa.com | 3 | 0.06% | 0.10% |
| news_api | n.yam.com | 3 | 0.06% | 0.10% |
| news_api | netzwelt.de | 3 | 0.06% | 0.10% |
| news_api | newswiretoday.com | 3 | 0.06% | 0.10% |
| news_api | northumberlandnews.com | 3 | 0.06% | 0.10% |
| news_api | nzherald.co.nz | 3 | 0.06% | 0.10% |
| news_api | odatv.com | 3 | 0.06% | 0.10% |
| news_api | oem.com.mx | 3 | 0.06% | 0.10% |
| news_api | ohmynews.com | 3 | 0.06% | 0.10% |
| news_api | orangeville.com | 3 | 0.06% | 0.10% |
| news_api | politis.com.cy | 3 | 0.06% | 0.10% |
| news_api | portal.sina.com.hk | 3 | 0.06% | 0.10% |
| news_api | prokerala.com | 3 | 0.06% | 0.10% |
| news_api | rediff.com | 3 | 0.06% | 0.10% |
| news_api | ria.ru | 3 | 0.06% | 0.10% |
| news_api | russian.rt.com | 3 | 0.06% | 0.10% |
| news_api | sankei.com | 3 | 0.06% | 0.10% |
| news_api | sb.by | 3 | 0.06% | 0.10% |
| news_api | talk.ltn.com.tw | 3 | 0.06% | 0.10% |
| news_api | techtimes.com | 3 | 0.06% | 0.10% |
| news_api | theguardian.com | 3 | 0.06% | 0.10% |
| news_api | thesun.ng | 3 | 0.06% | 0.10% |
| news_api | timeslive.co.za | 3 | 0.06% | 0.10% |
| news_api | tomshardware.com | 3 | 0.06% | 0.10% |
| news_api | toonippo.co.jp | 3 | 0.06% | 0.10% |
| news_api | tribuneindia.com | 3 | 0.06% | 0.10% |
| news_api | tumentoday.ru | 3 | 0.06% | 0.10% |
| news_api | udn.com | 3 | 0.06% | 0.10% |
| news_api | unian.net | 3 | 0.06% | 0.10% |
| news_api | vietnamnet.vn | 3 | 0.06% | 0.10% |
| news_api | wbaltv.com | 3 | 0.06% | 0.10% |
| news_api | wesh.com | 3 | 0.06% | 0.10% |
| news_api | womannews.net | 3 | 0.06% | 0.10% |
| news_api | zeit.de | 3 | 0.06% | 0.10% |
| news_api | ziarulprofit.ro | 3 | 0.06% | 0.10% |
| news_api | 01net.com | 2 | 0.04% | 0.07% |
| news_api | 1prime.ru | 2 | 0.04% | 0.07% |
| news_api | abovethelaw.com | 2 | 0.04% | 0.07% |
| news_api | adevarul.ro | 2 | 0.04% | 0.07% |
| news_api | ahaber.com.tr | 2 | 0.04% | 0.07% |
| news_api | alahalygate.com | 2 | 0.04% | 0.07% |
| news_api | allafrica.com | 2 | 0.04% | 0.07% |
| news_api | americanbanker.com | 2 | 0.04% | 0.07% |
| news_api | amic.ru | 2 | 0.04% | 0.07% |
| news_api | androidheadlines.com | 2 | 0.04% | 0.07% |
| news_api | antaranews.com | 2 | 0.04% | 0.07% |
| news_api | aol.co.uk | 2 | 0.04% | 0.07% |
| news_api | aristeguinoticias.com | 2 | 0.04% | 0.07% |
| news_api | arkansasonline.com | 2 | 0.04% | 0.07% |
| news_api | arstechnica.com | 2 | 0.04% | 0.07% |
| news_api | austinglobe.com | 2 | 0.04% | 0.07% |
| news_api | batonrougepost.com | 2 | 0.04% | 0.07% |
| news_api | begeek.fr | 2 | 0.04% | 0.07% |
| news_api | bernerzeitung.ch | 2 | 0.04% | 0.07% |
| news_api | bgr.com | 2 | 0.04% | 0.07% |
| news_api | bignewsnetwork.com | 2 | 0.04% | 0.07% |
| news_api | bjnews.com.cn | 2 | 0.04% | 0.07% |
| news_api | bleepingcomputer.com | 2 | 0.04% | 0.07% |
| news_api | blic.rs | 2 | 0.04% | 0.07% |
| news_api | bramptonguardian.com | 2 | 0.04% | 0.07% |
| news_api | brasil247.com | 2 | 0.04% | 0.07% |
| news_api | breitbart.com | 2 | 0.04% | 0.07% |
| news_api | brisbanetimes.com.au | 2 | 0.04% | 0.07% |
| news_api | bunburymail.com.au | 2 | 0.04% | 0.07% |
| news_api | bursahakimiyet.com.tr | 2 | 0.04% | 0.07% |
| news_api | business24.ro | 2 | 0.04% | 0.07% |
| news_api | businessghana.com | 2 | 0.04% | 0.07% |
| news_api | castanetkamloops.net | 2 | 0.04% | 0.07% |
| news_api | chinanationalnews.com | 2 | 0.04% | 0.07% |
| news_api | chip.de | 2 | 0.04% | 0.07% |
| news_api | cloud.watch.impress.co.jp | 2 | 0.04% | 0.07% |
| news_api | cna.com.tw | 2 | 0.04% | 0.07% |
| news_api | comnews.ru | 2 | 0.04% | 0.07% |
| news_api | computerweekly.com | 2 | 0.04% | 0.07% |
| news_api | computerworld.dk | 2 | 0.04% | 0.07% |
| news_api | contentmanager.de | 2 | 0.04% | 0.07% |
| news_api | correiobraziliense.com.br | 2 | 0.04% | 0.07% |
| news_api | correiodopovo.com.br | 2 | 0.04% | 0.07% |
| news_api | daily.com.ua | 2 | 0.04% | 0.07% |
| news_api | dailybreeze.com | 2 | 0.04% | 0.07% |
| news_api | dailyemerald.com | 2 | 0.04% | 0.07% |
| news_api | dailyinqilab.com | 2 | 0.04% | 0.07% |
| news_api | dailykos.com | 2 | 0.04% | 0.07% |
| news_api | dailynews.co.th | 2 | 0.04% | 0.07% |
| news_api | dailynews.com | 2 | 0.04% | 0.07% |
| news_api | dailypioneer.com | 2 | 0.04% | 0.07% |
| news_api | dainiktribuneonline.com | 2 | 0.04% | 0.07% |
| news_api | danas.rs | 2 | 0.04% | 0.07% |
| news_api | deadline.com | 2 | 0.04% | 0.07% |
| news_api | denizlihaber.com | 2 | 0.04% | 0.07% |
| news_api | designboom.com | 2 | 0.04% | 0.07% |
| news_api | dha.com.tr | 2 | 0.04% | 0.07% |
| news_api | diario.mx | 2 | 0.04% | 0.07% |
| news_api | diariodemallorca.es | 2 | 0.04% | 0.07% |
| news_api | diariosur.es | 2 | 0.04% | 0.07% |
| news_api | digi24.ro | 2 | 0.04% | 0.07% |
| news_api | digit.in | 2 | 0.04% | 0.07% |
| news_api | digitaljournal.com | 2 | 0.04% | 0.07% |
| news_api | divyamarathi.bhaskar.com | 2 | 0.04% | 0.07% |
| news_api | dnes.bg | 2 | 0.04% | 0.07% |
| news_api | dnews.gr | 2 | 0.04% | 0.07% |
| news_api | dogruhaber.com.tr | 2 | 0.04% | 0.07% |
| news_api | durhamregion.com | 2 | 0.04% | 0.07% |
| news_api | ecodibergamo.it | 2 | 0.04% | 0.07% |
| news_api | ecodisicilia.com | 2 | 0.04% | 0.07% |
| news_api | ecommercenews.co.nz | 2 | 0.04% | 0.07% |
| news_api | eldestapeweb.com | 2 | 0.04% | 0.07% |
| news_api | eldia.com.bo | 2 | 0.04% | 0.07% |
| news_api | eldiariodelapampa.com.ar | 2 | 0.04% | 0.07% |
| news_api | elmanana.com | 2 | 0.04% | 0.07% |
| news_api | elpais.com | 2 | 0.04% | 0.07% |
| news_api | em.com.br | 2 | 0.04% | 0.07% |
| news_api | filmfare.com | 2 | 0.04% | 0.07% |
| news_api | focus.ua | 2 | 0.04% | 0.07% |
| news_api | fontanka.ru | 2 | 0.04% | 0.07% |
| news_api | fox4news.com | 2 | 0.04% | 0.07% |
| news_api | fr.allafrica.com | 2 | 0.04% | 0.07% |
| news_api | freemalaysiatoday.com | 2 | 0.04% | 0.07% |
| news_api | gamerant.com | 2 | 0.04% | 0.07% |
| news_api | geeky-gadgets.com | 2 | 0.04% | 0.07% |
| news_api | github.com | 2 | 0.04% | 0.07% |
| news_api | gizmodo.com | 2 | 0.04% | 0.07% |
| news_api | greeleytribune.com | 2 | 0.04% | 0.07% |
| news_api | haber1.com | 2 | 0.04% | 0.07% |
| news_api | haber7.com | 2 | 0.04% | 0.07% |
| news_api | haberturk.com | 2 | 0.04% | 0.07% |
| news_api | haberyazar.com | 2 | 0.04% | 0.07% |
| news_api | hawaiitelegraph.com | 2 | 0.04% | 0.07% |
| news_api | heraldk.com | 2 | 0.04% | 0.07% |
| news_api | hindi.webdunia.com | 2 | 0.04% | 0.07% |
| news_api | hinews.cn | 2 | 0.04% | 0.07% |
| news_api | hngn.com | 2 | 0.04% | 0.07% |
| news_api | hollywoodreporter.com | 2 | 0.04% | 0.07% |
| news_api | howtogeek.com | 2 | 0.04% | 0.07% |
| news_api | htxt.co.za | 2 | 0.04% | 0.07% |
| news_api | hurriyetdailynews.com | 2 | 0.04% | 0.07% |
| news_api | ibtimes.co.uk | 2 | 0.04% | 0.07% |
| news_api | ilgiornale.it | 2 | 0.04% | 0.07% |
| news_api | ilpost.it | 2 | 0.04% | 0.07% |
| news_api | index.hr | 2 | 0.04% | 0.07% |
| news_api | indianexpress.com | 2 | 0.04% | 0.07% |
| news_api | inforum.com | 2 | 0.04% | 0.07% |
| news_api | infoworld.com | 2 | 0.04% | 0.07% |
| news_api | infranken.de | 2 | 0.04% | 0.07% |
| news_api | inosmi.ru | 2 | 0.04% | 0.07% |
| news_api | insideclimatenews.org | 2 | 0.04% | 0.07% |
| news_api | insidehalton.com | 2 | 0.04% | 0.07% |
| news_api | insight.co.kr | 2 | 0.04% | 0.07% |
| news_api | insurancejournal.com | 2 | 0.04% | 0.07% |
| news_api | internasional.kompas.com | 2 | 0.04% | 0.07% |
| news_api | investegate.co.uk | 2 | 0.04% | 0.07% |
| news_api | irishdentist.ie | 2 | 0.04% | 0.07% |
| news_api | irishtimes.com | 2 | 0.04% | 0.07% |
| news_api | it.euronews.com | 2 | 0.04% | 0.07% |
| news_api | itc.ua | 2 | 0.04% | 0.07% |
| news_api | iz.ru | 2 | 0.04% | 0.07% |
| news_api | jamaicaobserver.com | 2 | 0.04% | 0.07% |
| news_api | japanherald.com | 2 | 0.04% | 0.07% |
| news_api | jawapos.com | 2 | 0.04% | 0.07% |
| news_api | jpost.com | 2 | 0.04% | 0.07% |
| news_api | jugantor.com | 2 | 0.04% | 0.07% |
| news_api | kathimerini.com.cy | 2 | 0.04% | 0.07% |
| news_api | kcci.com | 2 | 0.04% | 0.07% |
| news_api | kitabat.com | 2 | 0.04% | 0.07% |
| news_api | kommersant.ru | 2 | 0.04% | 0.07% |
| news_api | koreatimes.com | 2 | 0.04% | 0.07% |
| news_api | kten.com | 2 | 0.04% | 0.07% |
| news_api | laleggepertutti.it | 2 | 0.04% | 0.07% |
| news_api | lalsace.fr | 2 | 0.04% | 0.07% |
| news_api | latimes.com | 2 | 0.04% | 0.07% |
| news_api | lbc.co.uk | 2 | 0.04% | 0.07% |
| news_api | ledauphine.com | 2 | 0.04% | 0.07% |
| news_api | lefigaro.fr | 2 | 0.04% | 0.07% |
| news_api | lelezard.com | 2 | 0.04% | 0.07% |
| news_api | lenta.ru | 2 | 0.04% | 0.07% |
| news_api | lesnumeriques.com | 2 | 0.04% | 0.07% |
| news_api | lexpress.fr | 2 | 0.04% | 0.07% |
| news_api | libnanews.com | 2 | 0.04% | 0.07% |
| news_api | life.ru | 2 | 0.04% | 0.07% |
| news_api | lindependant.fr | 2 | 0.04% | 0.07% |
| news_api | livehindustan.com | 2 | 0.04% | 0.07% |
| news_api | livemint.com | 2 | 0.04% | 0.07% |
| news_api | livenews.co.nz | 2 | 0.04% | 0.07% |
| news_api | lrytas.lt | 2 | 0.04% | 0.07% |
| news_api | macleayargus.com.au | 2 | 0.04% | 0.07% |
| news_api | malijet.com | 2 | 0.04% | 0.07% |
| news_api | marca.com | 2 | 0.04% | 0.07% |
| news_api | mariettatimes.com | 2 | 0.04% | 0.07% |
| news_api | massachusettssun.com | 2 | 0.04% | 0.07% |
| news_api | mdjonline.com | 2 | 0.04% | 0.07% |
| news_api | medianama.com | 2 | 0.04% | 0.07% |
| news_api | mersinhaber.com | 2 | 0.04% | 0.07% |
| news_api | messengernewspapers.co.uk | 2 | 0.04% | 0.07% |
| news_api | meteoweb.eu | 2 | 0.04% | 0.07% |
| news_api | metroseoul.co.kr | 2 | 0.04% | 0.07% |
| news_api | military.china.com | 2 | 0.04% | 0.07% |
| news_api | mississauga.com | 2 | 0.04% | 0.07% |
| news_api | mk.ru | 2 | 0.04% | 0.07% |
| news_api | mopo.de | 2 | 0.04% | 0.07% |
| news_api | morningstar.com | 2 | 0.04% | 0.07% |
| news_api | muskokaregion.com | 2 | 0.04% | 0.07% |
| news_api | naftemporiki.gr | 2 | 0.04% | 0.07% |
| news_api | newratings.de | 2 | 0.04% | 0.07% |
| news_api | news-medical.net | 2 | 0.04% | 0.07% |
| news_api | news.cn | 2 | 0.04% | 0.07% |
| news_api | news.mail.ru | 2 | 0.04% | 0.07% |
| news_api | newsbomb.gr | 2 | 0.04% | 0.07% |
| news_api | newstribune.com | 2 | 0.04% | 0.07% |
| news_api | newsweek.com | 2 | 0.04% | 0.07% |
| news_api | newtalk.tw | 2 | 0.04% | 0.07% |
| news_api | niagarathisweek.com | 2 | 0.04% | 0.07% |
| news_api | nikkan-gendai.com | 2 | 0.04% | 0.07% |
| news_api | nikkei.com | 2 | 0.04% | 0.07% |
| news_api | nordbayern.de | 2 | 0.04% | 0.07% |
| news_api | northbaynipissing.com | 2 | 0.04% | 0.07% |
| news_api | ntdtv.com | 2 | 0.04% | 0.07% |
| news_api | nuevodiarioweb.com.ar | 2 | 0.04% | 0.07% |
| news_api | nvi.com.au | 2 | 0.04% | 0.07% |
| news_api | nwaonline.com | 2 | 0.04% | 0.07% |
| news_api | objectiv.tv | 2 | 0.04% | 0.07% |
| news_api | op-online.de | 2 | 0.04% | 0.07% |
| news_api | parisguardian.com | 2 | 0.04% | 0.07% |
| news_api | pctechmag.com | 2 | 0.04% | 0.07% |
| news_api | pcwplus.hu | 2 | 0.04% | 0.07% |
| news_api | phonandroid.com | 2 | 0.04% | 0.07% |
| news_api | politika.rs | 2 | 0.04% | 0.07% |
| news_api | posta.com.tr | 2 | 0.04% | 0.07% |
| news_api | prensalibre.com | 2 | 0.04% | 0.07% |
| news_api | presstv.ir | 2 | 0.04% | 0.07% |
| news_api | propakistani.pk | 2 | 0.04% | 0.07% |
| news_api | pv-magazine.com | 2 | 0.04% | 0.07% |
| news_api | pymnts.com | 2 | 0.04% | 0.07% |
| news_api | quotidianodelsud.it | 2 | 0.04% | 0.07% |
| news_api | radiofrance.fr | 2 | 0.04% | 0.07% |
| news_api | radiopolar.com | 2 | 0.04% | 0.07% |
| news_api | rappler.com | 2 | 0.04% | 0.07% |
| news_api | riasv.ru | 2 | 0.04% | 0.07% |
| news_api | rnanews.com | 2 | 0.04% | 0.07% |
| news_api | rnz.co.nz | 2 | 0.04% | 0.07% |
| news_api | russiaherald.com | 2 | 0.04% | 0.07% |
| news_api | sanantoniopost.com | 2 | 0.04% | 0.07% |
| news_api | securitybrief.news | 2 | 0.04% | 0.07% |
| news_api | securityinfowatch.com | 2 | 0.04% | 0.07% |
| news_api | senego.com | 2 | 0.04% | 0.07% |
| news_api | sentinel.ht | 2 | 0.04% | 0.07% |
| news_api | sgvtribune.com | 2 | 0.04% | 0.07% |
| news_api | shikoku-np.co.jp | 2 | 0.04% | 0.07% |
| news_api | smh.com.au | 2 | 0.04% | 0.07% |
| news_api | stcn.com | 2 | 0.04% | 0.07% |
| news_api | storm.mg | 2 | 0.04% | 0.07% |
| news_api | t-l.ru | 2 | 0.04% | 0.07% |
| news_api | t-online.de | 2 | 0.04% | 0.07% |
| news_api | t24.com.tr | 2 | 0.04% | 0.07% |
| news_api | tagesschau.de | 2 | 0.04% | 0.07% |
| news_api | tanea.gr | 2 | 0.04% | 0.07% |
| news_api | tech.caijing.com.cn | 2 | 0.04% | 0.07% |
| news_api | tech.ifeng.com | 2 | 0.04% | 0.07% |
| news_api | techweez.com | 2 | 0.04% | 0.07% |
| news_api | tekniikkatalous.fi | 2 | 0.04% | 0.07% |
| news_api | tennesseedaily.com | 2 | 0.04% | 0.07% |
| news_api | theblaze.com | 2 | 0.04% | 0.07% |
| news_api | thedailystar.net | 2 | 0.04% | 0.07% |
| news_api | thehindu.com | 2 | 0.04% | 0.07% |
| news_api | thereporterethiopia.com | 2 | 0.04% | 0.07% |
| news_api | thisdaylive.com | 2 | 0.04% | 0.07% |
| news_api | tmtpost.com | 2 | 0.04% | 0.07% |
| news_api | townhall.com | 2 | 0.04% | 0.07% |
| news_api | tribune.net.ph | 2 | 0.04% | 0.07% |
| news_api | turktime.com | 2 | 0.04% | 0.07% |
| news_api | tvanouvelles.ca | 2 | 0.04% | 0.07% |
| news_api | uainfo.org | 2 | 0.04% | 0.07% |
| news_api | unn.ua | 2 | 0.04% | 0.07% |
| news_api | unternehmen-heute.de | 2 | 0.04% | 0.07% |
| news_api | vedomosti.ru | 2 | 0.04% | 0.07% |
| news_api | vesti.ru | 2 | 0.04% | 0.07% |
| news_api | vg.no | 2 | 0.04% | 0.07% |
| news_api | vicnews.com | 2 | 0.04% | 0.07% |
| news_api | wallstreet-online.de | 2 | 0.04% | 0.07% |
| news_api | watoday.com.au | 2 | 0.04% | 0.07% |
| news_api | wcvb.com | 2 | 0.04% | 0.07% |
| news_api | wdrb.com | 2 | 0.04% | 0.07% |
| news_api | webpronews.com | 2 | 0.04% | 0.07% |
| news_api | welivesecurity.com | 2 | 0.04% | 0.07% |
| news_api | weser-kurier.de | 2 | 0.04% | 0.07% |
| news_api | wfmz.com | 2 | 0.04% | 0.07% |
| news_api | wikitree.co.kr | 2 | 0.04% | 0.07% |
| news_api | wiwo.de | 2 | 0.04% | 0.07% |
| news_api | wsbtv.com | 2 | 0.04% | 0.07% |
| news_api | wwmt.com | 2 | 0.04% | 0.07% |
| news_api | wzzm13.com | 2 | 0.04% | 0.07% |
| news_api | y-mainichi.co.jp | 2 | 0.04% | 0.07% |
| news_api | yeniasya.com.tr | 2 | 0.04% | 0.07% |
| news_api | yerelgundem.com | 2 | 0.04% | 0.07% |
| news_api | ynet.co.il | 2 | 0.04% | 0.07% |
| news_api | ziare.com | 2 | 0.04% | 0.07% |
| news_api | zonebourse.com | 2 | 0.04% | 0.07% |
| news_api | 1015vibe.com | 1 | 0.02% | 0.03% |
| news_api | 1055thedove.com | 1 | 0.02% | 0.03% |
| news_api | 10tv.com | 1 | 0.02% | 0.03% |
| news_api | 13abc.com | 1 | 0.02% | 0.03% |
| news_api | 15min.lt | 1 | 0.02% | 0.03% |
| news_api | 20min.ch | 1 | 0.02% | 0.03% |
| news_api | 21stcenturywire.com | 1 | 0.02% | 0.03% |
| news_api | 24sata.hr | 1 | 0.02% | 0.03% |
| news_api | 24tv.ua | 1 | 0.02% | 0.03% |
| news_api | 26sep.net | 1 | 0.02% | 0.03% |
| news_api | 373news.com | 1 | 0.02% | 0.03% |
| news_api | 3c.ltn.com.tw | 1 | 0.02% | 0.03% |
| news_api | 5.ua | 1 | 0.02% | 0.03% |
| news_api | 5newsonline.com | 1 | 0.02% | 0.03% |
| news_api | 620ckrm.com | 1 | 0.02% | 0.03% |
| news_api | 961theeagle.com | 1 | 0.02% | 0.03% |
| news_api | 985thefox.iheart.com | 1 | 0.02% | 0.03% |
| news_api | 995thefox.iheart.com | 1 | 0.02% | 0.03% |
| news_api | 99jamzmiami.com | 1 | 0.02% | 0.03% |
| news_api | 9news.com.au | 1 | 0.02% | 0.03% |
| news_api | 9tv.co.il | 1 | 0.02% | 0.03% |
| news_api | aawsat.com | 1 | 0.02% | 0.03% |
| news_api | abc.net.au | 1 | 0.02% | 0.03% |
| news_api | abc6onyourside.com | 1 | 0.02% | 0.03% |
| news_api | abc7news.com | 1 | 0.02% | 0.03% |
| news_api | abclinuxu.cz | 1 | 0.02% | 0.03% |
| news_api | abcnyheter.no | 1 | 0.02% | 0.03% |
| news_api | acento.com.do | 1 | 0.02% | 0.03% |
| news_api | actionnewsjax.com | 1 | 0.02% | 0.03% |
| news_api | adgully.com | 1 | 0.02% | 0.03% |
| news_api | administradores.com.br | 1 | 0.02% | 0.03% |
| news_api | adn.com | 1 | 0.02% | 0.03% |
| news_api | afr.com | 1 | 0.02% | 0.03% |
| news_api | agara.co.jp | 1 | 0.02% | 0.03% |
| news_api | agenciagov.ebc.com.br | 1 | 0.02% | 0.03% |
| news_api | agi.it | 1 | 0.02% | 0.03% |
| news_api | ai.zol.com.cn | 1 | 0.02% | 0.03% |
| news_api | aif.ru | 1 | 0.02% | 0.03% |
| news_api | aiwaegypt.com | 1 | 0.02% | 0.03% |
| news_api | akhbarelyom.com | 1 | 0.02% | 0.03% |
| news_api | aktifhaber.com | 1 | 0.02% | 0.03% |
| news_api | aktivni.metropolitan.si | 1 | 0.02% | 0.03% |
| news_api | al-monitor.com | 1 | 0.02% | 0.03% |
| news_api | alanbatnews.net | 1 | 0.02% | 0.03% |
| news_api | alaskasnewssource.com | 1 | 0.02% | 0.03% |
| news_api | albayan.ae | 1 | 0.02% | 0.03% |
| news_api | alfajertv.com | 1 | 0.02% | 0.03% |
| news_api | aliran.com | 1 | 0.02% | 0.03% |
| news_api | aljazeera.com | 1 | 0.02% | 0.03% |
| news_api | allaboutthejersey.com | 1 | 0.02% | 0.03% |
| news_api | almontasaf.net | 1 | 0.02% | 0.03% |
| news_api | alo.rs | 1 | 0.02% | 0.03% |
| news_api | am1150.ca | 1 | 0.02% | 0.03% |
| news_api | anbariloche.com.ar | 1 | 0.02% | 0.03% |
| news_api | anf-news.com | 1 | 0.02% | 0.03% |
| news_api | antena3.com | 1 | 0.02% | 0.03% |
| news_api | antena3.ro | 1 | 0.02% | 0.03% |
| news_api | antivirus-sniper.macupdate.com | 1 | 0.02% | 0.03% |
| news_api | ara.cat | 1 | 0.02% | 0.03% |
| news_api | arabherald.com | 1 | 0.02% | 0.03% |
| news_api | arede.info | 1 | 0.02% | 0.03% |
| news_api | armenews.com | 1 | 0.02% | 0.03% |
| news_api | armidaleexpress.com.au | 1 | 0.02% | 0.03% |
| news_api | artvoice.com | 1 | 0.02% | 0.03% |
| news_api | arynews.tv | 1 | 0.02% | 0.03% |
| news_api | asahi.com | 1 | 0.02% | 0.03% |
| news_api | asianews.it | 1 | 0.02% | 0.03% |
| news_api | aspentimes.com | 1 | 0.02% | 0.03% |
| news_api | astroawani.com | 1 | 0.02% | 0.03% |
| news_api | athina984.gr | 1 | 0.02% | 0.03% |
| news_api | atlantico.fr | 1 | 0.02% | 0.03% |
| news_api | austinchronicle.com | 1 | 0.02% | 0.03% |
| news_api | autoexpress.co.uk | 1 | 0.02% | 0.03% |
| news_api | avn.info.ve | 1 | 0.02% | 0.03% |
| news_api | az-online.de | 1 | 0.02% | 0.03% |
| news_api | b985.com | 1 | 0.02% | 0.03% |
| news_api | balkanweb.com | 1 | 0.02% | 0.03% |
| news_api | bamada.net | 1 | 0.02% | 0.03% |
| news_api | bandaancha.eu | 1 | 0.02% | 0.03% |
| news_api | bangkokbiznews.com | 1 | 0.02% | 0.03% |
| news_api | bangkokpost.com | 1 | 0.02% | 0.03% |
| news_api | banglanews24.today | 1 | 0.02% | 0.03% |
| news_api | bangordailynews.com | 1 | 0.02% | 0.03% |
| news_api | bankier.pl | 1 | 0.02% | 0.03% |
| news_api | banklesstimes.com | 1 | 0.02% | 0.03% |
| news_api | batam.tribunnews.com | 1 | 0.02% | 0.03% |
| news_api | batemansbaypost.com.au | 1 | 0.02% | 0.03% |
| news_api | bbc.com | 1 | 0.02% | 0.03% |
| news_api | beckershospitalreview.com | 1 | 0.02% | 0.03% |
| news_api | berliner-zeitung.de | 1 | 0.02% | 0.03% |
| news_api | beveiligingnieuws.nl | 1 | 0.02% | 0.03% |
| news_api | bfmtv.com | 1 | 0.02% | 0.03% |
| news_api | bgonair.bg | 1 | 0.02% | 0.03% |
| news_api | bhaskar.com | 1 | 0.02% | 0.03% |
| news_api | bianet.org | 1 | 0.02% | 0.03% |
| news_api | bigpara.hurriyet.com.tr | 1 | 0.02% | 0.03% |
| news_api | biobiochile.cl | 1 | 0.02% | 0.03% |
| news_api | birminghamstar.com | 1 | 0.02% | 0.03% |
| news_api | biz.cnews.ru | 1 | 0.02% | 0.03% |
| news_api | bj.xinhuanet.com | 1 | 0.02% | 0.03% |
| news_api | blackseanews.net | 1 | 0.02% | 0.03% |
| news_api | blikk.hu | 1 | 0.02% | 0.03% |
| news_api | blitzquotidiano.it | 1 | 0.02% | 0.03% |
| news_api | blog.detail.dev | 1 | 0.02% | 0.03% |
| news_api | blog.wenxuecity.com | 1 | 0.02% | 0.03% |
| news_api | blogs.diariovasco.com | 1 | 0.02% | 0.03% |
| news_api | blogs.itmedia.co.jp | 1 | 0.02% | 0.03% |
| news_api | bloodhorse.com | 1 | 0.02% | 0.03% |
| news_api | bloomberght.com | 1 | 0.02% | 0.03% |
| news_api | bluemountainsgazette.com.au | 1 | 0.02% | 0.03% |
| news_api | blueprint.ng | 1 | 0.02% | 0.03% |
| news_api | bmmagazine.co.uk | 1 | 0.02% | 0.03% |
| news_api | bnnbloomberg.ca | 1 | 0.02% | 0.03% |
| news_api | bollywoodhungama.com | 1 | 0.02% | 0.03% |
| news_api | bollywoodlife.com | 1 | 0.02% | 0.03% |
| news_api | bolognatoday.it | 1 | 0.02% | 0.03% |
| news_api | book.asahi.com | 1 | 0.02% | 0.03% |
| news_api | borsaitaliana.it | 1 | 0.02% | 0.03% |
| news_api | borsonline.hu | 1 | 0.02% | 0.03% |
| news_api | bostonherald.com | 1 | 0.02% | 0.03% |
| news_api | botasot.info | 1 | 0.02% | 0.03% |
| news_api | bozemandailychronicle.com | 1 | 0.02% | 0.03% |
| news_api | braidwoodtimes.com.au | 1 | 0.02% | 0.03% |
| news_api | brandonsun.com | 1 | 0.02% | 0.03% |
| news_api | brazilsun.com | 1 | 0.02% | 0.03% |
| news_api | breakingnews.ie | 1 | 0.02% | 0.03% |
| news_api | bresciaoggi.it | 1 | 0.02% | 0.03% |
| news_api | brooklyneagle.com | 1 | 0.02% | 0.03% |
| news_api | bt.no | 1 | 0.02% | 0.03% |
| news_api | buffalobulletin.com | 1 | 0.02% | 0.03% |
| news_api | bug.hr | 1 | 0.02% | 0.03% |
| news_api | burgasinfo.com | 1 | 0.02% | 0.03% |
| news_api | burgundywave.com | 1 | 0.02% | 0.03% |
| news_api | burytimes.co.uk | 1 | 0.02% | 0.03% |
| news_api | business-review.eu | 1 | 0.02% | 0.03% |
| news_api | business2community.com | 1 | 0.02% | 0.03% |
| news_api | businessinsurance.com | 1 | 0.02% | 0.03% |
| news_api | businessonline.it | 1 | 0.02% | 0.03% |
| news_api | businesstimes.com.sg | 1 | 0.02% | 0.03% |
| news_api | businesstoday.in | 1 | 0.02% | 0.03% |
| news_api | businessworld.in | 1 | 0.02% | 0.03% |
| news_api | c101.iheart.com | 1 | 0.02% | 0.03% |
| news_api | cachevalleydaily.com | 1 | 0.02% | 0.03% |
| news_api | cafebiz.vn | 1 | 0.02% | 0.03% |
| news_api | calciomercato.com | 1 | 0.02% | 0.03% |
| news_api | californiatelegraph.com | 1 | 0.02% | 0.03% |
| news_api | camdencourier.com.au | 1 | 0.02% | 0.03% |
| news_api | campbell.edu | 1 | 0.02% | 0.03% |
| news_api | canal26.com | 1 | 0.02% | 0.03% |
| news_api | canardpc.com | 1 | 0.02% | 0.03% |
| news_api | capitalethiopia.com | 1 | 0.02% | 0.03% |
| news_api | carolinajournal.com | 1 | 0.02% | 0.03% |
| news_api | cas.sk | 1 | 0.02% | 0.03% |
| news_api | catanzaroinforma.it | 1 | 0.02% | 0.03% |
| news_api | cawalisse.com | 1 | 0.02% | 0.03% |
| news_api | cbnews.fr | 1 | 0.02% | 0.03% |
| news_api | cbs2iowa.com | 1 | 0.02% | 0.03% |
| news_api | cbs6albany.com | 1 | 0.02% | 0.03% |
| news_api | cepro.com | 1 | 0.02% | 0.03% |
| news_api | cesky.radio.cz | 1 | 0.02% | 0.03% |
| news_api | cfi.net.cn | 1 | 0.02% | 0.03% |
| news_api | challenges.fr | 1 | 0.02% | 0.03% |
| news_api | channelbuzz.ca | 1 | 0.02% | 0.03% |
| news_api | chaozhoudaily.com | 1 | 0.02% | 0.03% |
| news_api | chattanoogan.com | 1 | 0.02% | 0.03% |
| news_api | cherokeescout.com | 1 | 0.02% | 0.03% |
| news_api | chilecomparte.cl | 1 | 0.02% | 0.03% |
| news_api | china.com.cn | 1 | 0.02% | 0.03% |
| news_api | chinapress.com.my | 1 | 0.02% | 0.03% |
| news_api | chinatechnews.com | 1 | 0.02% | 0.03% |
| news_api | chinesepress.com | 1 | 0.02% | 0.03% |
| news_api | choice.com.au | 1 | 0.02% | 0.03% |
| news_api | cincinnatisun.com | 1 | 0.02% | 0.03% |
| news_api | circleid.com | 1 | 0.02% | 0.03% |
| news_api | citizenlab.ca | 1 | 0.02% | 0.03% |
| news_api | citylimits.org | 1 | 0.02% | 0.03% |
| news_api | cjme.com | 1 | 0.02% | 0.03% |
| news_api | clactonandfrintongazette.co.uk | 1 | 0.02% | 0.03% |
| news_api | clarin.com | 1 | 0.02% | 0.03% |
| news_api | clevescene.com | 1 | 0.02% | 0.03% |
| news_api | closermag.fr | 1 | 0.02% | 0.03% |
| news_api | clydebankpost.co.uk | 1 | 0.02% | 0.03% |
| news_api | cnet.com | 1 | 0.02% | 0.03% |
| news_api | cnn.com | 1 | 0.02% | 0.03% |
| news_api | cnycentral.com | 1 | 0.02% | 0.03% |
| news_api | coloradostar.com | 1 | 0.02% | 0.03% |
| news_api | comicbook.com | 1 | 0.02% | 0.03% |
| news_api | comingsoon.it | 1 | 0.02% | 0.03% |
| news_api | computerwoche.de | 1 | 0.02% | 0.03% |
| news_api | computerworld.pl | 1 | 0.02% | 0.03% |
| news_api | contractormag.com | 1 | 0.02% | 0.03% |
| news_api | cootamundraherald.com.au | 1 | 0.02% | 0.03% |
| news_api | cope.es | 1 | 0.02% | 0.03% |
| news_api | coronadonewsca.com | 1 | 0.02% | 0.03% |
| news_api | corp.cnews.ru | 1 | 0.02% | 0.03% |
| news_api | correiodobrasil.com.br | 1 | 0.02% | 0.03% |
| news_api | corriereadriatico.it | 1 | 0.02% | 0.03% |
| news_api | cosmopolitan.com | 1 | 0.02% | 0.03% |
| news_api | countercurrents.org | 1 | 0.02% | 0.03% |
| news_api | cp24.com | 1 | 0.02% | 0.03% |
| news_api | cqnews.net | 1 | 0.02% | 0.03% |
| news_api | crestonnews.com | 1 | 0.02% | 0.03% |
| news_api | crookwellgazette.com.au | 1 | 0.02% | 0.03% |
| news_api | cuartopoder.mx | 1 | 0.02% | 0.03% |
| news_api | cursdeguvernare.ro | 1 | 0.02% | 0.03% |
| news_api | cyprus-mail.com | 1 | 0.02% | 0.03% |
| news_api | dagensps.se | 1 | 0.02% | 0.03% |
| news_api | daily-tribune.com | 1 | 0.02% | 0.03% |
| news_api | dailyadvertiser.com.au | 1 | 0.02% | 0.03% |
| news_api | dailybulletin.com | 1 | 0.02% | 0.03% |
| news_api | dailyexcelsior.com | 1 | 0.02% | 0.03% |
| news_api | dailyheraldtribune.com | 1 | 0.02% | 0.03% |
| news_api | dailyjournalonline.com | 1 | 0.02% | 0.03% |
| news_api | dailymail.co.uk | 1 | 0.02% | 0.03% |
| news_api | dailymaverick.co.za | 1 | 0.02% | 0.03% |
| news_api | dailypakistan.pk | 1 | 0.02% | 0.03% |
| news_api | dailypost.ng | 1 | 0.02% | 0.03% |
| news_api | dailyrecord.co.uk | 1 | 0.02% | 0.03% |
| news_api | dailysabah.com | 1 | 0.02% | 0.03% |
| news_api | dailytrust.com | 1 | 0.02% | 0.03% |
| news_api | dailyuw.com | 1 | 0.02% | 0.03% |
| news_api | dakotawarcollege.com | 1 | 0.02% | 0.03% |
| news_api | damernasvarld.expressen.se | 1 | 0.02% | 0.03% |
| news_api | dantri.com.vn | 1 | 0.02% | 0.03% |
| news_api | datacenterknowledge.com | 1 | 0.02% | 0.03% |
| news_api | daytondailynews.com | 1 | 0.02% | 0.03% |
| news_api | dcvelocity.com | 1 | 0.02% | 0.03% |
| news_api | de.nachrichten.yahoo.com | 1 | 0.02% | 0.03% |
| news_api | deccanchronicle.com | 1 | 0.02% | 0.03% |
| news_api | deperu.com | 1 | 0.02% | 0.03% |
| news_api | derbund.ch | 1 | 0.02% | 0.03% |
| news_api | devondispatch.ca | 1 | 0.02% | 0.03% |
| news_api | dglobe.com | 1 | 0.02% | 0.03% |
| news_api | dialogos.com.cy | 1 | 0.02% | 0.03% |
| news_api | diaridegirona.cat | 1 | 0.02% | 0.03% |
| news_api | diariodeburgos.es | 1 | 0.02% | 0.03% |
| news_api | diariodemorelos.com | 1 | 0.02% | 0.03% |
| news_api | diarioelargentino.com | 1 | 0.02% | 0.03% |
| news_api | diariopalentino.es | 1 | 0.02% | 0.03% |
| news_api | diariosigloxxi.com | 1 | 0.02% | 0.03% |
| news_api | diariovasco.com | 1 | 0.02% | 0.03% |
| news_api | diena.lt | 1 | 0.02% | 0.03% |
| news_api | digg.com | 1 | 0.02% | 0.03% |
| news_api | digi.china.com | 1 | 0.02% | 0.03% |
| news_api | digitaltrends.com | 1 | 0.02% | 0.03% |
| news_api | directionsmag.com | 1 | 0.02% | 0.03% |
| news_api | diumenge.ara.cat | 1 | 0.02% | 0.03% |
| news_api | diyarbakirsoz.com | 1 | 0.02% | 0.03% |
| news_api | dn.se | 1 | 0.02% | 0.03% |
| news_api | dna.fr | 1 | 0.02% | 0.03% |
| news_api | dol.com.br | 1 | 0.02% | 0.03% |
| news_api | dominicanrepublicpost.com | 1 | 0.02% | 0.03% |
| news_api | donanimhaber.com | 1 | 0.02% | 0.03% |
| news_api | donews.com | 1 | 0.02% | 0.03% |
| news_api | dongascience.com | 1 | 0.02% | 0.03% |
| news_api | dotekomanie.cz | 1 | 0.02% | 0.03% |
| news_api | downtoearth.org.in | 1 | 0.02% | 0.03% |
| news_api | dp.ru | 1 | 0.02% | 0.03% |
| news_api | drimble.nl | 1 | 0.02% | 0.03% |
| news_api | dunya.com | 1 | 0.02% | 0.03% |
| news_api | dunyanews.tv | 1 | 0.02% | 0.03% |
| news_api | dutchitchannel.nl | 1 | 0.02% | 0.03% |
| news_api | dynamicbusiness.com | 1 | 0.02% | 0.03% |
| news_api | e.dennikn.sk | 1 | 0.02% | 0.03% |
| news_api | eadt.co.uk | 1 | 0.02% | 0.03% |
| news_api | eagledayton.com | 1 | 0.02% | 0.03% |
| news_api | eaglesanantonio.com | 1 | 0.02% | 0.03% |
| news_api | ec.ltn.com.tw | 1 | 0.02% | 0.03% |
| news_api | echo-news.co.uk | 1 | 0.02% | 0.03% |
| news_api | echopress.com | 1 | 0.02% | 0.03% |
| news_api | echoroukonline.com | 1 | 0.02% | 0.03% |
| news_api | economx.hu | 1 | 0.02% | 0.03% |
| news_api | econotimes.com | 1 | 0.02% | 0.03% |
| news_api | edition.cnn.com | 1 | 0.02% | 0.03% |
| news_api | eejournal.com | 1 | 0.02% | 0.03% |
| news_api | eenadu.net | 1 | 0.02% | 0.03% |
| news_api | eeo.com.cn | 1 | 0.02% | 0.03% |
| news_api | egyptindependent.com | 1 | 0.02% | 0.03% |
| news_api | elcomercio.es | 1 | 0.02% | 0.03% |
| news_api | elconfidencial.com | 1 | 0.02% | 0.03% |
| news_api | elcorreo.com | 1 | 0.02% | 0.03% |
| news_api | elcorreodeburgos.com | 1 | 0.02% | 0.03% |
| news_api | eldia.es | 1 | 0.02% | 0.03% |
| news_api | eldiariomontanes.es | 1 | 0.02% | 0.03% |
| news_api | eleco.com.ar | 1 | 0.02% | 0.03% |
| news_api | eleftherostypos.gr | 1 | 0.02% | 0.03% |
| news_api | elektroniknet.de | 1 | 0.02% | 0.03% |
| news_api | elmalaeb.com | 1 | 0.02% | 0.03% |
| news_api | elmundo.es | 1 | 0.02% | 0.03% |
| news_api | elpais.com.uy | 1 | 0.02% | 0.03% |
| news_api | elpatagonico.com | 1 | 0.02% | 0.03% |
| news_api | elperiodico.cat | 1 | 0.02% | 0.03% |
| news_api | elperiodico.com | 1 | 0.02% | 0.03% |
| news_api | elperiodico.com.do | 1 | 0.02% | 0.03% |
| news_api | elperiodicodearagon.com | 1 | 0.02% | 0.03% |
| news_api | elpuntavui.cat | 1 | 0.02% | 0.03% |
| news_api | eluniverso.com | 1 | 0.02% | 0.03% |
| news_api | elvocero.com | 1 | 0.02% | 0.03% |
| news_api | elwatannews.com | 1 | 0.02% | 0.03% |
| news_api | emaratalyoum.com | 1 | 0.02% | 0.03% |
| news_api | en.dailypakistan.com.pk | 1 | 0.02% | 0.03% |
| news_api | en.globes.co.il | 1 | 0.02% | 0.03% |
| news_api | eng.kavkaz-uzel.eu | 1 | 0.02% | 0.03% |
| news_api | english.elpais.com | 1 | 0.02% | 0.03% |
| news_api | english.pravda.ru | 1 | 0.02% | 0.03% |
| news_api | ennaharonline.com | 1 | 0.02% | 0.03% |
| news_api | epikaira.gr | 1 | 0.02% | 0.03% |
| news_api | estadao.com.br | 1 | 0.02% | 0.03% |
| news_api | ettoday.net | 1 | 0.02% | 0.03% |
| news_api | euronews.com | 1 | 0.02% | 0.03% |
| news_api | expert.ru | 1 | 0.02% | 0.03% |
| news_api | explosion.com | 1 | 0.02% | 0.03% |
| news_api | express.pk | 1 | 0.02% | 0.03% |
| news_api | extra.ec | 1 | 0.02% | 0.03% |
| news_api | eyemagazine.com | 1 | 0.02% | 0.03% |
| news_api | f1vilag.hu | 1 | 0.02% | 0.03% |
| news_api | f5haber.com | 1 | 0.02% | 0.03% |
| news_api | fakti.bg | 1 | 0.02% | 0.03% |
| news_api | fansided.com | 1 | 0.02% | 0.03% |
| news_api | fatimanews.com.br | 1 | 0.02% | 0.03% |
| news_api | fedpress.ru | 1 | 0.02% | 0.03% |
| news_api | femina.hu | 1 | 0.02% | 0.03% |
| news_api | ferra.ru | 1 | 0.02% | 0.03% |
| news_api | finance.ifeng.com | 1 | 0.02% | 0.03% |
| news_api | finance.walla.co.il | 1 | 0.02% | 0.03% |
| news_api | financial-news.co.uk | 1 | 0.02% | 0.03% |
| news_api | financialafrik.com | 1 | 0.02% | 0.03% |
| news_api | finans.mynet.com | 1 | 0.02% | 0.03% |
| news_api | firstpost.com | 1 | 0.02% | 0.03% |
| news_api | floridastatesman.com | 1 | 0.02% | 0.03% |
| news_api | fnp.de | 1 | 0.02% | 0.03% |
| news_api | fool.ca | 1 | 0.02% | 0.03% |
| news_api | forbes.ru | 1 | 0.02% | 0.03% |
| news_api | forum.ixbt.com | 1 | 0.02% | 0.03% |
| news_api | fox17online.com | 1 | 0.02% | 0.03% |
| news_api | fox43.com | 1 | 0.02% | 0.03% |
| news_api | fox9.com | 1 | 0.02% | 0.03% |
| news_api | francetoday.com | 1 | 0.02% | 0.03% |
| news_api | freiburg.de | 1 | 0.02% | 0.03% |
| news_api | freiepresse.de | 1 | 0.02% | 0.03% |
| news_api | french.china.org.cn | 1 | 0.02% | 0.03% |
| news_api | funkytaurusmedia.com | 1 | 0.02% | 0.03% |
| news_api | futures.cnfol.com | 1 | 0.02% | 0.03% |
| news_api | gadgetsmagazine.com.ph | 1 | 0.02% | 0.03% |
| news_api | games.24tv.ua | 1 | 0.02% | 0.03% |
| news_api | gamestar.de | 1 | 0.02% | 0.03% |
| news_api | gazetaexpress.com | 1 | 0.02% | 0.03% |
| news_api | gazzetta.gr | 1 | 0.02% | 0.03% |
| news_api | geekzone.co.nz | 1 | 0.02% | 0.03% |
| news_api | generation-nt.com | 1 | 0.02% | 0.03% |
| news_api | geo.tv | 1 | 0.02% | 0.03% |
| news_api | georgeherald.com | 1 | 0.02% | 0.03% |
| news_api | german.china.org.cn | 1 | 0.02% | 0.03% |
| news_api | ghanaiantimes.com.gh | 1 | 0.02% | 0.03% |
| news_api | gipedo.politis.com.cy | 1 | 0.02% | 0.03% |
| news_api | globalissues.org | 1 | 0.02% | 0.03% |
| news_api | globalsecurity.org | 1 | 0.02% | 0.03% |
| news_api | golosarmenii.am | 1 | 0.02% | 0.03% |
| news_api | gorod48.ru | 1 | 0.02% | 0.03% |
| news_api | governing.com | 1 | 0.02% | 0.03% |
| news_api | greekherald.com | 1 | 0.02% | 0.03% |
| news_api | greenme.it | 1 | 0.02% | 0.03% |
| news_api | groundup.org.za | 1 | 0.02% | 0.03% |
| news_api | guelphmercury.com | 1 | 0.02% | 0.03% |
| news_api | gulte.com | 1 | 0.02% | 0.03% |
| news_api | gundemkibris.com | 1 | 0.02% | 0.03% |
| news_api | gunes.com | 1 | 0.02% | 0.03% |
| news_api | gx94radio.com | 1 | 0.02% | 0.03% |
| news_api | haber.mynet.com | 1 | 0.02% | 0.03% |
| news_api | haber3.com | 1 | 0.02% | 0.03% |
| news_api | haber61.net | 1 | 0.02% | 0.03% |
| news_api | haberaktuel.com | 1 | 0.02% | 0.03% |
| news_api | haberankara.com | 1 | 0.02% | 0.03% |
| news_api | habermeydan.com | 1 | 0.02% | 0.03% |
| news_api | haberts.com | 1 | 0.02% | 0.03% |
| news_api | hachettebookgroup.com | 1 | 0.02% | 0.03% |
| news_api | hackaday.com | 1 | 0.02% | 0.03% |
| news_api | hanasone.mainichi.jp | 1 | 0.02% | 0.03% |
| news_api | handelsblatt.com | 1 | 0.02% | 0.03% |
| news_api | hartvannederland.nl | 1 | 0.02% | 0.03% |
| news_api | hawaiinewsnow.com | 1 | 0.02% | 0.03% |
| news_api | hbook.com | 1 | 0.02% | 0.03% |
| news_api | healthcareitnews.com | 1 | 0.02% | 0.03% |
| news_api | healthimpactnews.com | 1 | 0.02% | 0.03% |
| news_api | hellenicnews.com | 1 | 0.02% | 0.03% |
| news_api | helpconsumatori.it | 1 | 0.02% | 0.03% |
| news_api | herald-dispatch.com | 1 | 0.02% | 0.03% |
| news_api | heraldscotland.com | 1 | 0.02% | 0.03% |
| news_api | hespress.com | 1 | 0.02% | 0.03% |
| news_api | heute.at | 1 | 0.02% | 0.03% |
| news_api | hindi.moneycontrol.com | 1 | 0.02% | 0.03% |
| news_api | hirek.prim.hu | 1 | 0.02% | 0.03% |
| news_api | hits1053sanantonio.com | 1 | 0.02% | 0.03% |
| news_api | hits973.com | 1 | 0.02% | 0.03% |
| news_api | hkcna.hk | 1 | 0.02% | 0.03% |
| news_api | hokkoku.co.jp | 1 | 0.02% | 0.03% |
| news_api | hometownstation.com | 1 | 0.02% | 0.03% |
| news_api | hongkongherald.com | 1 | 0.02% | 0.03% |
| news_api | hoy.es | 1 | 0.02% | 0.03% |
| news_api | huffingtonpost.co.uk | 1 | 0.02% | 0.03% |
| news_api | hydrocarbonprocessing.com | 1 | 0.02% | 0.03% |
| news_api | iafrica.com | 1 | 0.02% | 0.03% |
| news_api | ici.fr | 1 | 0.02% | 0.03% |
| news_api | icij.org | 1 | 0.02% | 0.03% |
| news_api | idiva.com | 1 | 0.02% | 0.03% |
| news_api | idnes.cz | 1 | 0.02% | 0.03% |
| news_api | idrw.org | 1 | 0.02% | 0.03% |
| news_api | ifj.org | 1 | 0.02% | 0.03% |
| news_api | igamingbusiness.com | 1 | 0.02% | 0.03% |
| news_api | ign.com | 1 | 0.02% | 0.03% |
| news_api | ihalla.com | 1 | 0.02% | 0.03% |
| news_api | ilfattonisseno.it | 1 | 0.02% | 0.03% |
| news_api | ilgiorno.it | 1 | 0.02% | 0.03% |
| news_api | illawarramercury.com.au | 1 | 0.02% | 0.03% |
| news_api | ilmessaggero.it | 1 | 0.02% | 0.03% |
| news_api | ilsimplicissimus2.com | 1 | 0.02% | 0.03% |
| news_api | independent.co.uk | 1 | 0.02% | 0.03% |
| news_api | india.com | 1 | 0.02% | 0.03% |
| news_api | indiagazette.com | 1 | 0.02% | 0.03% |
| news_api | indiatvnews.com | 1 | 0.02% | 0.03% |
| news_api | infobae.com | 1 | 0.02% | 0.03% |
| news_api | informacion.es | 1 | 0.02% | 0.03% |
| news_api | informationweek.com | 1 | 0.02% | 0.03% |
| news_api | infotechlead.com | 1 | 0.02% | 0.03% |
| news_api | inquirer.com | 1 | 0.02% | 0.03% |
| news_api | insidephilanthropy.com | 1 | 0.02% | 0.03% |
| news_api | insidermonkey.com | 1 | 0.02% | 0.03% |
| news_api | insight.scmagazineuk.com | 1 | 0.02% | 0.03% |
| news_api | interaksyon.philstar.com | 1 | 0.02% | 0.03% |
| news_api | internetua.com | 1 | 0.02% | 0.03% |
| news_api | inverelltimes.com.au | 1 | 0.02% | 0.03% |
| news_api | investorplace.com | 1 | 0.02% | 0.03% |
| news_api | inwestycje.pl | 1 | 0.02% | 0.03% |
| news_api | iphoneaddict.fr | 1 | 0.02% | 0.03% |
| news_api | iraqsun.com | 1 | 0.02% | 0.03% |
| news_api | irishsun.com | 1 | 0.02% | 0.03% |
| news_api | island.lk | 1 | 0.02% | 0.03% |
| news_api | israelherald.com | 1 | 0.02% | 0.03% |
| news_api | it-business.de | 1 | 0.02% | 0.03% |
| news_api | itbrief.news | 1 | 0.02% | 0.03% |
| news_api | itnewsafrica.com | 1 | 0.02% | 0.03% |
| news_api | ivpressonline.com | 1 | 0.02% | 0.03% |
| news_api | iwate-np.co.jp | 1 | 0.02% | 0.03% |
| news_api | j-cast.com | 1 | 0.02% | 0.03% |
| news_api | j-town.net | 1 | 0.02% | 0.03% |
| news_api | jabar.tribunnews.com | 1 | 0.02% | 0.03% |
| news_api | jagranjosh.com | 1 | 0.02% | 0.03% |
| news_api | jamestown.org | 1 | 0.02% | 0.03% |
| news_api | japan.cnet.com | 1 | 0.02% | 0.03% |
| news_api | jc.uol.com.br | 1 | 0.02% | 0.03% |
| news_api | jeuneafrique.com | 1 | 0.02% | 0.03% |
| news_api | jhm.fr | 1 | 0.02% | 0.03% |
| news_api | jiji.com | 1 | 0.02% | 0.03% |
| news_api | jo24.net | 1 | 0.02% | 0.03% |
| news_api | jogja.tribunnews.com | 1 | 0.02% | 0.03% |
| news_api | jogjapolitan.harianjogja.com | 1 | 0.02% | 0.03% |
| news_api | journal-news.com | 1 | 0.02% | 0.03% |
| news_api | journaldugeek.com | 1 | 0.02% | 0.03% |
| news_api | journaldunet.com | 1 | 0.02% | 0.03% |
| news_api | journalgazette.net | 1 | 0.02% | 0.03% |
| news_api | jowhar.com | 1 | 0.02% | 0.03% |
| news_api | jpnn.com | 1 | 0.02% | 0.03% |
| news_api | juneesoutherncross.com.au | 1 | 0.02% | 0.03% |
| news_api | jurnalul.ro | 1 | 0.02% | 0.03% |
| news_api | jutarnji.hr | 1 | 0.02% | 0.03% |
| news_api | k-tipos.gr | 1 | 0.02% | 0.03% |
| news_api | k991fm.com | 1 | 0.02% | 0.03% |
| news_api | kamuajans.com | 1 | 0.02% | 0.03% |
| news_api | kannadaprabha.com | 1 | 0.02% | 0.03% |
| news_api | kaos911.com | 1 | 0.02% | 0.03% |
| news_api | karfitsa.gr | 1 | 0.02% | 0.03% |
| news_api | kath.net | 1 | 0.02% | 0.03% |
| news_api | katu.com | 1 | 0.02% | 0.03% |
| news_api | kazokuchannel.doorblog.jp | 1 | 0.02% | 0.03% |
| news_api | kboo.fm | 1 | 0.02% | 0.03% |
| news_api | kcentv.com | 1 | 0.02% | 0.03% |
| news_api | kenyastar.com | 1 | 0.02% | 0.03% |
| news_api | kesq.com | 1 | 0.02% | 0.03% |
| news_api | kibrisgazetesi.com | 1 | 0.02% | 0.03% |
| news_api | kikar.co.il | 1 | 0.02% | 0.03% |
| news_api | kincardinenews.com | 1 | 0.02% | 0.03% |
| news_api | king5.com | 1 | 0.02% | 0.03% |
| news_api | kingfm.com | 1 | 0.02% | 0.03% |
| news_api | kiplinger.com | 1 | 0.02% | 0.03% |
| news_api | kiro7.com | 1 | 0.02% | 0.03% |
| news_api | kissrocks.com | 1 | 0.02% | 0.03% |
| news_api | kjzz.org | 1 | 0.02% | 0.03% |
| news_api | klack.de | 1 | 0.02% | 0.03% |
| news_api | klaipeda.diena.lt | 1 | 0.02% | 0.03% |
| news_api | kmbc.com | 1 | 0.02% | 0.03% |
| news_api | ko.com.ua | 1 | 0.02% | 0.03% |
| news_api | kob.com | 1 | 0.02% | 0.03% |
| news_api | kocaeligazetesi.com.tr | 1 | 0.02% | 0.03% |
| news_api | koco.com | 1 | 0.02% | 0.03% |
| news_api | kono1011.com | 1 | 0.02% | 0.03% |
| news_api | kontrakty.ua | 1 | 0.02% | 0.03% |
| news_api | koreatimes.co.kr | 1 | 0.02% | 0.03% |
| news_api | kotaku.com | 1 | 0.02% | 0.03% |
| news_api | kreisbote.de | 1 | 0.02% | 0.03% |
| news_api | kristv.com | 1 | 0.02% | 0.03% |
| news_api | krone.at | 1 | 0.02% | 0.03% |
| news_api | ktvl.com | 1 | 0.02% | 0.03% |
| news_api | ktvu.com | 1 | 0.02% | 0.03% |
| news_api | kwcdcountry.com | 1 | 0.02% | 0.03% |
| news_api | kyivpost.com | 1 | 0.02% | 0.03% |
| news_api | kztv10.com | 1 | 0.02% | 0.03% |
| news_api | labs.watchtowr.com | 1 | 0.02% | 0.03% |
| news_api | ladepeche.fr | 1 | 0.02% | 0.03% |
| news_api | lafranceagricole.fr | 1 | 0.02% | 0.03% |
| news_api | lagacetadesalamanca.es | 1 | 0.02% | 0.03% |
| news_api | lakersnation.com | 1 | 0.02% | 0.03% |
| news_api | lamarseillaise.fr | 1 | 0.02% | 0.03% |
| news_api | lancashiretelegraph.co.uk | 1 | 0.02% | 0.03% |
| news_api | laois-nationalist.ie | 1 | 0.02% | 0.03% |
| news_api | laosnews.net | 1 | 0.02% | 0.03% |
| news_api | lapresse.tn | 1 | 0.02% | 0.03% |
| news_api | laprovence.com | 1 | 0.02% | 0.03% |
| news_api | laprovincia.es | 1 | 0.02% | 0.03% |
| news_api | larazon.es | 1 | 0.02% | 0.03% |
| news_api | larepublica.pe | 1 | 0.02% | 0.03% |
| news_api | larepubliquedespyrenees.fr | 1 | 0.02% | 0.03% |
| news_api | latele.ch | 1 | 0.02% | 0.03% |
| news_api | laut.de | 1 | 0.02% | 0.03% |
| news_api | lavozdegalicia.es | 1 | 0.02% | 0.03% |
| news_api | lb.ua | 1 | 0.02% | 0.03% |
| news_api | lecourrier.vn | 1 | 0.02% | 0.03% |
| news_api | legalinsurrection.com | 1 | 0.02% | 0.03% |
| news_api | leiphone.com | 1 | 0.02% | 0.03% |
| news_api | lejsl.com | 1 | 0.02% | 0.03% |
| news_api | lematin.ma | 1 | 0.02% | 0.03% |
| news_api | lesmobiles.com | 1 | 0.02% | 0.03% |
| news_api | letemps.ch | 1 | 0.02% | 0.03% |
| news_api | lewrockwell.com | 1 | 0.02% | 0.03% |
| news_api | lgz.ru | 1 | 0.02% | 0.03% |
| news_api | liberta.it | 1 | 0.02% | 0.03% |
| news_api | libertatea.ro | 1 | 0.02% | 0.03% |
| news_api | ligaportal.at | 1 | 0.02% | 0.03% |
| news_api | lina.sh | 1 | 0.02% | 0.03% |
| news_api | linux.org.ru | 1 | 0.02% | 0.03% |
| news_api | liputan6.com | 1 | 0.02% | 0.03% |
| news_api | lite987.com | 1 | 0.02% | 0.03% |
| news_api | lithgowmercury.com.au | 1 | 0.02% | 0.03% |
| news_api | livelaw.in | 1 | 0.02% | 0.03% |
| news_api | local12.com | 1 | 0.02% | 0.03% |
| news_api | local21news.com | 1 | 0.02% | 0.03% |
| news_api | localnews8.com | 1 | 0.02% | 0.03% |
| news_api | loksatta.com | 1 | 0.02% | 0.03% |
| news_api | londonlovesbusiness.com | 1 | 0.02% | 0.03% |
| news_api | londonmercury.com | 1 | 0.02% | 0.03% |
| news_api | ly.fjsen.com | 1 | 0.02% | 0.03% |
| news_api | m.kauno.diena.lt | 1 | 0.02% | 0.03% |
| news_api | m.metroseoul.co.kr | 1 | 0.02% | 0.03% |
| news_api | macg.co | 1 | 0.02% | 0.03% |
| news_api | mactech.com | 1 | 0.02% | 0.03% |
| news_api | magic1021.com | 1 | 0.02% | 0.03% |
| news_api | maharashtratimes.com | 1 | 0.02% | 0.03% |
| news_api | makaangola.org | 1 | 0.02% | 0.03% |
| news_api | makassar.tribunnews.com | 1 | 0.02% | 0.03% |
| news_api | maldonandburnhamstandard.co.uk | 1 | 0.02% | 0.03% |
| news_api | manchestereveningnews.co.uk | 1 | 0.02% | 0.03% |
| news_api | mandurahmail.com.au | 1 | 0.02% | 0.03% |
| news_api | manningrivertimes.com.au | 1 | 0.02% | 0.03% |
| news_api | manoramanews.com | 1 | 0.02% | 0.03% |
| news_api | maravipost.com | 1 | 0.02% | 0.03% |
| news_api | marketintelligencecenter.com | 1 | 0.02% | 0.03% |
| news_api | mathrubhumi.com | 1 | 0.02% | 0.03% |
| news_api | mdzol.com | 1 | 0.02% | 0.03% |
| news_api | mebpersonel.com | 1 | 0.02% | 0.03% |
| news_api | megamodo.com | 1 | 0.02% | 0.03% |
| news_api | megatv.com | 1 | 0.02% | 0.03% |
| news_api | mekomi.walla.co.il | 1 | 0.02% | 0.03% |
| news_api | memeburn.com | 1 | 0.02% | 0.03% |
| news_api | mensxp.com | 1 | 0.02% | 0.03% |
| news_api | merdeka.com | 1 | 0.02% | 0.03% |
| news_api | meridiano.net | 1 | 0.02% | 0.03% |
| news_api | merkur.de | 1 | 0.02% | 0.03% |
| news_api | metro.co.uk | 1 | 0.02% | 0.03% |
| news_api | metronews.ru | 1 | 0.02% | 0.03% |
| news_api | michigandaily.com | 1 | 0.02% | 0.03% |
| news_api | middleeasteye.net | 1 | 0.02% | 0.03% |
| news_api | midmichigannow.com | 1 | 0.02% | 0.03% |
| news_api | military.com | 1 | 0.02% | 0.03% |
| news_api | minuto30.com | 1 | 0.02% | 0.03% |
| news_api | minyu-net.com | 1 | 0.02% | 0.03% |
| news_api | mirrorspectator.com | 1 | 0.02% | 0.03% |
| news_api | mittelstandcafe.de | 1 | 0.02% | 0.03% |
| news_api | mix941kmxj.com | 1 | 0.02% | 0.03% |
| news_api | mngz.ru | 1 | 0.02% | 0.03% |
| news_api | mobeigi.com | 1 | 0.02% | 0.03% |
| news_api | mobile.zol.com.cn | 1 | 0.02% | 0.03% |
| news_api | mobileidworld.com | 1 | 0.02% | 0.03% |
| news_api | mochimag.com | 1 | 0.02% | 0.03% |
| news_api | money.it | 1 | 0.02% | 0.03% |
| news_api | monocle.com | 1 | 0.02% | 0.03% |
| news_api | montereyherald.com | 1 | 0.02% | 0.03% |
| news_api | morgenpost.de | 1 | 0.02% | 0.03% |
| news_api | morningstaronline.co.uk | 1 | 0.02% | 0.03% |
| news_api | morungexpress.com | 1 | 0.02% | 0.03% |
| news_api | mp.cnfol.com | 1 | 0.02% | 0.03% |
| news_api | mpacorn.com | 1 | 0.02% | 0.03% |
| news_api | mskagency.ru | 1 | 0.02% | 0.03% |
| news_api | mudgeeguardian.com.au | 1 | 0.02% | 0.03% |
| news_api | mundiario.com | 1 | 0.02% | 0.03% |
| news_api | mundoenlinea.cl | 1 | 0.02% | 0.03% |
| news_api | myanmarnews.net | 1 | 0.02% | 0.03% |
| news_api | myhostnews.com | 1 | 0.02% | 0.03% |
| news_api | mymagic949.com | 1 | 0.02% | 0.03% |
| news_api | mynet.com | 1 | 0.02% | 0.03% |
| news_api | mynews4.com | 1 | 0.02% | 0.03% |
| news_api | nagpurtoday.in | 1 | 0.02% | 0.03% |
| news_api | nakedcapitalism.com | 1 | 0.02% | 0.03% |
| news_api | namibian.com.na | 1 | 0.02% | 0.03% |
| news_api | nashvilleherald.com | 1 | 0.02% | 0.03% |
| news_api | nationalmortgagenews.com | 1 | 0.02% | 0.03% |
| news_api | naturalnews.com | 1 | 0.02% | 0.03% |
| news_api | navabharat.com | 1 | 0.02% | 0.03% |
| news_api | navbharattimes.indiatimes.com | 1 | 0.02% | 0.03% |
| news_api | navhindtimes.in | 1 | 0.02% | 0.03% |
| news_api | nbcmontana.com | 1 | 0.02% | 0.03% |
| news_api | nbcwashington.com | 1 | 0.02% | 0.03% |
| news_api | nbd.com.cn | 1 | 0.02% | 0.03% |
| news_api | nearshoreamericas.com | 1 | 0.02% | 0.03% |
| news_api | net.hr | 1 | 0.02% | 0.03% |
| news_api | neviditelnypes.lidovky.cz | 1 | 0.02% | 0.03% |
| news_api | newcastleherald.com.au | 1 | 0.02% | 0.03% |
| news_api | newhamburgindependent.ca | 1 | 0.02% | 0.03% |
| news_api | neworleanssun.com | 1 | 0.02% | 0.03% |
| news_api | newrepublic.com | 1 | 0.02% | 0.03% |
| news_api | news-expressky.com | 1 | 0.02% | 0.03% |
| news_api | news.china.com.cn | 1 | 0.02% | 0.03% |
| news_api | news.cnfol.com | 1 | 0.02% | 0.03% |
| news_api | news.cts.com.tw | 1 | 0.02% | 0.03% |
| news_api | news.cyol.com | 1 | 0.02% | 0.03% |
| news_api | news.finance.ua | 1 | 0.02% | 0.03% |
| news_api | news.ifeng.com | 1 | 0.02% | 0.03% |
| news_api | news.kbs.co.kr | 1 | 0.02% | 0.03% |
| news_api | news.ltn.com.tw | 1 | 0.02% | 0.03% |
| news_api | news.tuoitre.vn | 1 | 0.02% | 0.03% |
| news_api | news.ycwb.com | 1 | 0.02% | 0.03% |
| news_api | news3lv.com | 1 | 0.02% | 0.03% |
| news_api | news8000.com | 1 | 0.02% | 0.03% |
| news_api | newsbeast.gr | 1 | 0.02% | 0.03% |
| news_api | newscentralasia.net | 1 | 0.02% | 0.03% |
| news_api | newsday.co.zw | 1 | 0.02% | 0.03% |
| news_api | newsday.com | 1 | 0.02% | 0.03% |
| news_api | newsghana.com.gh | 1 | 0.02% | 0.03% |
| news_api | newsit.gr | 1 | 0.02% | 0.03% |
| news_api | newsitaliane.it | 1 | 0.02% | 0.03% |
| news_api | newsminer.com | 1 | 0.02% | 0.03% |
| news_api | newsmonkey.be | 1 | 0.02% | 0.03% |
| news_api | newsnet5.com | 1 | 0.02% | 0.03% |
| news_api | newsprom.ru | 1 | 0.02% | 0.03% |
| news_api | newsx.com | 1 | 0.02% | 0.03% |
| news_api | newuniversity.org | 1 | 0.02% | 0.03% |
| news_api | newyorkstatesman.com | 1 | 0.02% | 0.03% |
| news_api | nhonews.com | 1 | 0.02% | 0.03% |
| news_api | nieuws.nl | 1 | 0.02% | 0.03% |
| news_api | niezalezna.pl | 1 | 0.02% | 0.03% |
| news_api | nigerianobservernews.com | 1 | 0.02% | 0.03% |
| news_api | nikkan.co.jp | 1 | 0.02% | 0.03% |
| news_api | nile.eg | 1 | 0.02% | 0.03% |
| news_api | nin.rs | 1 | 0.02% | 0.03% |
| news_api | ninersnation.com | 1 | 0.02% | 0.03% |
| news_api | nj.com | 1 | 0.02% | 0.03% |
| news_api | norran.se | 1 | 0.02% | 0.03% |
| news_api | northcountrynow.com | 1 | 0.02% | 0.03% |
| news_api | northerndailyleader.com.au | 1 | 0.02% | 0.03% |
| news_api | northweststar.com.au | 1 | 0.02% | 0.03% |
| news_api | notimerica.com | 1 | 0.02% | 0.03% |
| news_api | novinite.bg | 1 | 0.02% | 0.03% |
| news_api | novinite.com | 1 | 0.02% | 0.03% |
| news_api | noviny.sk | 1 | 0.02% | 0.03% |
| news_api | nrc.nl | 1 | 0.02% | 0.03% |
| news_api | nspna.com | 1 | 0.02% | 0.03% |
| news_api | ntv.com.tr | 1 | 0.02% | 0.03% |
| news_api | nvdaily.com | 1 | 0.02% | 0.03% |
| news_api | nwzonline.de | 1 | 0.02% | 0.03% |
| news_api | observador.pt | 1 | 0.02% | 0.03% |
| news_api | ocregister.com | 1 | 0.02% | 0.03% |
| news_api | oe24.at | 1 | 0.02% | 0.03% |
| news_api | ogunhaber.com | 1 | 0.02% | 0.03% |
| news_api | ohiostandard.com | 1 | 0.02% | 0.03% |
| news_api | okaz.com.sa | 1 | 0.02% | 0.03% |
| news_api | oklahomastar.com | 1 | 0.02% | 0.03% |
| news_api | ondacero.es | 1 | 0.02% | 0.03% |
| news_api | oneidadispatch.com | 1 | 0.02% | 0.03% |
| news_api | openpr.com | 1 | 0.02% | 0.03% |
| news_api | organiser.org | 1 | 0.02% | 0.03% |
| news_api | ostro.org | 1 | 0.02% | 0.03% |
| news_api | ottawacitizen.com | 1 | 0.02% | 0.03% |
| news_api | oz-online.de | 1 | 0.02% | 0.03% |
| news_api | ozgurkocaeli.com.tr | 1 | 0.02% | 0.03% |
| news_api | pakistantelegraph.com | 1 | 0.02% | 0.03% |
| news_api | pakobserver.net | 1 | 0.02% | 0.03% |
| news_api | panorama.com.al | 1 | 0.02% | 0.03% |
| news_api | parrysound.com | 1 | 0.02% | 0.03% |
| news_api | pastemagazine.com | 1 | 0.02% | 0.03% |
| news_api | patheos.com | 1 | 0.02% | 0.03% |
| news_api | patrasevents.gr | 1 | 0.02% | 0.03% |
| news_api | paymentweek.com | 1 | 0.02% | 0.03% |
| news_api | pc.co.il | 1 | 0.02% | 0.03% |
| news_api | pcchip.hr | 1 | 0.02% | 0.03% |
| news_api | pcwelt.de | 1 | 0.02% | 0.03% |
| news_api | pelop.gr | 1 | 0.02% | 0.03% |
| news_api | pentictonherald.ca | 1 | 0.02% | 0.03% |
| news_api | perspectivasur.com | 1 | 0.02% | 0.03% |
| news_api | pharmiweb.com | 1 | 0.02% | 0.03% |
| news_api | philenews.com | 1 | 0.02% | 0.03% |
| news_api | photo.china.com.cn | 1 | 0.02% | 0.03% |
| news_api | piacesprofit.hu | 1 | 0.02% | 0.03% |
| news_api | pineandlakes.com | 1 | 0.02% | 0.03% |
| news_api | pitchfork.com | 1 | 0.02% | 0.03% |
| news_api | piter.tv | 1 | 0.02% | 0.03% |
| news_api | pjmedia.com | 1 | 0.02% | 0.03% |
| news_api | placenorthwest.co.uk | 1 | 0.02% | 0.03% |
| news_api | playground.ru | 1 | 0.02% | 0.03% |
| news_api | pleinevie.fr | 1 | 0.02% | 0.03% |
| news_api | pln-pskov.ru | 1 | 0.02% | 0.03% |
| news_api | pocket-lint.com | 1 | 0.02% | 0.03% |
| news_api | podrobnosti.ua | 1 | 0.02% | 0.03% |
| news_api | politicamentecorretto.com | 1 | 0.02% | 0.03% |
| news_api | politico.eu | 1 | 0.02% | 0.03% |
| news_api | polityka.pl | 1 | 0.02% | 0.03% |
| news_api | polygon.com | 1 | 0.02% | 0.03% |
| news_api | pontianak.tribunnews.com | 1 | 0.02% | 0.03% |
| news_api | portalsamorzadowy.pl | 1 | 0.02% | 0.03% |
| news_api | portfolio.hu | 1 | 0.02% | 0.03% |
| news_api | portnews.com.au | 1 | 0.02% | 0.03% |
| news_api | postandcourier.com | 1 | 0.02% | 0.03% |
| news_api | posttoday.com | 1 | 0.02% | 0.03% |
| news_api | powerorlando.com | 1 | 0.02% | 0.03% |
| news_api | pplware.sapo.pt | 1 | 0.02% | 0.03% |
| news_api | pr.com | 1 | 0.02% | 0.03% |
| news_api | prabhasakshi.com | 1 | 0.02% | 0.03% |
| news_api | praca.egospodarka.pl | 1 | 0.02% | 0.03% |
| news_api | pratahkal.com | 1 | 0.02% | 0.03% |
| news_api | press24.mk | 1 | 0.02% | 0.03% |
| news_api | pressafrik.com | 1 | 0.02% | 0.03% |
| news_api | pressdemocrat.com | 1 | 0.02% | 0.03% |
| news_api | presse-citron.net | 1 | 0.02% | 0.03% |
| news_api | pressian.com | 1 | 0.02% | 0.03% |
| news_api | presstelegram.com | 1 | 0.02% | 0.03% |
| news_api | primerafuente.com.ar | 1 | 0.02% | 0.03% |
| news_api | profitline.hu | 1 | 0.02% | 0.03% |
| news_api | progressive-charlestown.com | 1 | 0.02% | 0.03% |
| news_api | pronedra.ru | 1 | 0.02% | 0.03% |
| news_api | pronto.com.ar | 1 | 0.02% | 0.03% |
| news_api | publico.es | 1 | 0.02% | 0.03% |
| news_api | publico.pt | 1 | 0.02% | 0.03% |
| news_api | publimetro.com.mx | 1 | 0.02% | 0.03% |
| news_api | punjabitribuneonline.com | 1 | 0.02% | 0.03% |
| news_api | punto-informatico.it | 1 | 0.02% | 0.03% |
| news_api | puntonoticias.com | 1 | 0.02% | 0.03% |
| news_api | q947fm.iheart.com | 1 | 0.02% | 0.03% |
| news_api | quadratin.com.mx | 1 | 0.02% | 0.03% |
| news_api | quinewspisa.it | 1 | 0.02% | 0.03% |
| news_api | quotidianodipuglia.it | 1 | 0.02% | 0.03% |
| news_api | qzwb.com | 1 | 0.02% | 0.03% |
| news_api | racismoambiental.net.br | 1 | 0.02% | 0.03% |
| news_api | radikal.com.tr | 1 | 0.02% | 0.03% |
| news_api | radioseoul1650.com | 1 | 0.02% | 0.03% |
| news_api | radiotamazuj.org | 1 | 0.02% | 0.03% |
| news_api | ratopati.com | 1 | 0.02% | 0.03% |
| news_api | realitatea.net | 1 | 0.02% | 0.03% |
| news_api | recorderonline.com | 1 | 0.02% | 0.03% |
| news_api | redlandsdailyfacts.com | 1 | 0.02% | 0.03% |
| news_api | reformer.com | 1 | 0.02% | 0.03% |
| news_api | regions.ru | 1 | 0.02% | 0.03% |
| news_api | reporterdiario.com.br | 1 | 0.02% | 0.03% |
| news_api | reporterherald.com | 1 | 0.02% | 0.03% |
| news_api | republicain-lorrain.fr | 1 | 0.02% | 0.03% |
| news_api | republikein.com.na | 1 | 0.02% | 0.03% |
| news_api | reseller.co.nz | 1 | 0.02% | 0.03% |
| news_api | ricentral.com | 1 | 0.02% | 0.03% |
| news_api | riotimesonline.com | 1 | 0.02% | 0.03% |
| news_api | risky.biz | 1 | 0.02% | 0.03% |
| news_api | rock1067.iheart.com | 1 | 0.02% | 0.03% |
| news_api | rocketerie.iheart.com | 1 | 0.02% | 0.03% |
| news_api | rodiaki.gr | 1 | 0.02% | 0.03% |
| news_api | romaniatv.net | 1 | 0.02% | 0.03% |
| news_api | root.cz | 1 | 0.02% | 0.03% |
| news_api | rstreet.org | 1 | 0.02% | 0.03% |
| news_api | rte.ie | 1 | 0.02% | 0.03% |
| news_api | rtl.nl | 1 | 0.02% | 0.03% |
| news_api | rtp.pt | 1 | 0.02% | 0.03% |
| news_api | rtv.rs | 1 | 0.02% | 0.03% |
| news_api | rtvutrecht.nl | 1 | 0.02% | 0.03% |
| news_api | ruhrnachrichten.de | 1 | 0.02% | 0.03% |
| news_api | ruthfullyyours.com | 1 | 0.02% | 0.03% |
| news_api | ryt9.com | 1 | 0.02% | 0.03% |
| news_api | saltlakecitysun.com | 1 | 0.02% | 0.03% |
| news_api | saltwire.com | 1 | 0.02% | 0.03% |
| news_api | salzburg24.at | 1 | 0.02% | 0.03% |
| news_api | sana.sy | 1 | 0.02% | 0.03% |
| news_api | sandiegouniontribune.com | 1 | 0.02% | 0.03% |
| news_api | sangbadpratidin.in | 1 | 0.02% | 0.03% |
| news_api | sanook.com | 1 | 0.02% | 0.03% |
| news_api | santamariatimes.com | 1 | 0.02% | 0.03% |
| news_api | saratogian.com | 1 | 0.02% | 0.03% |
| news_api | sbctv.gr | 1 | 0.02% | 0.03% |
| news_api | sbnation.com | 1 | 0.02% | 0.03% |
| news_api | sbsun.com | 1 | 0.02% | 0.03% |
| news_api | sc.stock.cnfol.com | 1 | 0.02% | 0.03% |
| news_api | scdaily.com | 1 | 0.02% | 0.03% |
| news_api | sciencesetavenir.fr | 1 | 0.02% | 0.03% |
| news_api | scmp.com | 1 | 0.02% | 0.03% |
| news_api | scroll.in | 1 | 0.02% | 0.03% |
| news_api | sdpnoticias.com | 1 | 0.02% | 0.03% |
| news_api | seekingalpha.com | 1 | 0.02% | 0.03% |
| news_api | sentinelandenterprise.com | 1 | 0.02% | 0.03% |
| news_api | setn.com | 1 | 0.02% | 0.03% |
| news_api | sharemanthan.in | 1 | 0.02% | 0.03% |
| news_api | sherwoodparknews.com | 1 | 0.02% | 0.03% |
| news_api | shtfplan.com | 1 | 0.02% | 0.03% |
| news_api | siliconangle.com | 1 | 0.02% | 0.03% |
| news_api | siliconrepublic.com | 1 | 0.02% | 0.03% |
| news_api | siol.net | 1 | 0.02% | 0.03% |
| news_api | skai.gr | 1 | 0.02% | 0.03% |
| news_api | slguardian.org | 1 | 0.02% | 0.03% |
| news_api | slugmag.com | 1 | 0.02% | 0.03% |
| news_api | smallwarsjournal.com | 1 | 0.02% | 0.03% |
| news_api | sn.at | 1 | 0.02% | 0.03% |
| news_api | son.tv | 1 | 0.02% | 0.03% |
| news_api | sonara.net | 1 | 0.02% | 0.03% |
| news_api | sott.net | 1 | 0.02% | 0.03% |
| news_api | southernhighlandnews.com.au | 1 | 0.02% | 0.03% |
| news_api | spacedaily.com | 1 | 0.02% | 0.03% |
| news_api | spartanavenue.com | 1 | 0.02% | 0.03% |
| news_api | spiegel.de | 1 | 0.02% | 0.03% |
| news_api | spokesman.com | 1 | 0.02% | 0.03% |
| news_api | srilankasource.com | 1 | 0.02% | 0.03% |
| news_api | star945.com | 1 | 0.02% | 0.03% |
| news_api | statecollege.com | 1 | 0.02% | 0.03% |
| news_api | stcatharinesstandard.ca | 1 | 0.02% | 0.03% |
| news_api | stern.de | 1 | 0.02% | 0.03% |
| news_api | stiintasitehnica.com | 1 | 0.02% | 0.03% |
| news_api | stile.it | 1 | 0.02% | 0.03% |
| news_api | stlouisstar.com | 1 | 0.02% | 0.03% |
| news_api | stock.hexun.com | 1 | 0.02% | 0.03% |
| news_api | stockbiz.vn | 1 | 0.02% | 0.03% |
| news_api | stranieriinitalia.it | 1 | 0.02% | 0.03% |
| news_api | strategypage.com | 1 | 0.02% | 0.03% |
| news_api | stripes.com | 1 | 0.02% | 0.03% |
| news_api | studiob.rs | 1 | 0.02% | 0.03% |
| news_api | sud.ua | 1 | 0.02% | 0.03% |
| news_api | sueddeutsche.de | 1 | 0.02% | 0.03% |
| news_api | suedtirolnews.it | 1 | 0.02% | 0.03% |
| news_api | t13.cl | 1 | 0.02% | 0.03% |
| news_api | t3n.de | 1 | 0.02% | 0.03% |
| news_api | tageblatt.lu | 1 | 0.02% | 0.03% |
| news_api | tagesanzeiger.ch | 1 | 0.02% | 0.03% |
| news_api | tagesspiegel.de | 1 | 0.02% | 0.03% |
| news_api | taiwandaily.net | 1 | 0.02% | 0.03% |
| news_api | talcualdigital.com | 1 | 0.02% | 0.03% |
| news_api | talouselama.fi | 1 | 0.02% | 0.03% |
| news_api | tass.ru | 1 | 0.02% | 0.03% |
| news_api | taxydromos.gr | 1 | 0.02% | 0.03% |
| news_api | taz.de | 1 | 0.02% | 0.03% |
| news_api | tazabek.kg | 1 | 0.02% | 0.03% |
| news_api | tdg.ch | 1 | 0.02% | 0.03% |
| news_api | tech.china.com | 1 | 0.02% | 0.03% |
| news_api | techcabal.com | 1 | 0.02% | 0.03% |
| news_api | technologyreview.com | 1 | 0.02% | 0.03% |
| news_api | techstory.in | 1 | 0.02% | 0.03% |
| news_api | techtudo.com.br | 1 | 0.02% | 0.03% |
| news_api | tecmundo.com.br | 1 | 0.02% | 0.03% |
| news_api | tecnoandroid.it | 1 | 0.02% | 0.03% |
| news_api | telefonino.net | 1 | 0.02% | 0.03% |
| news_api | tempo.co | 1 | 0.02% | 0.03% |
| news_api | tercerainformacion.es | 1 | 0.02% | 0.03% |
| news_api | texasguardian.com | 1 | 0.02% | 0.03% |
| news_api | thailand-business-news.com | 1 | 0.02% | 0.03% |
| news_api | thanhnien.vn | 1 | 0.02% | 0.03% |
| news_api | the-dispatch.com | 1 | 0.02% | 0.03% |
| news_api | the-miyanichi.co.jp | 1 | 0.02% | 0.03% |
| news_api | theadvocate.com.au | 1 | 0.02% | 0.03% |
| news_api | theage.com.au | 1 | 0.02% | 0.03% |
| news_api | thebftonline.com | 1 | 0.02% | 0.03% |
| news_api | theboneonline.com | 1 | 0.02% | 0.03% |
| news_api | thebusinessjournal.com | 1 | 0.02% | 0.03% |
| news_api | thecable.ng | 1 | 0.02% | 0.03% |
| news_api | thecamarilloacorn.com | 1 | 0.02% | 0.03% |
| news_api | theconversation.com | 1 | 0.02% | 0.03% |
| news_api | thecourier.com.au | 1 | 0.02% | 0.03% |
| news_api | thedailyworld.com | 1 | 0.02% | 0.03% |
| news_api | theeagleonline.com.ng | 1 | 0.02% | 0.03% |
| news_api | thefrontierpost.com | 1 | 0.02% | 0.03% |
| news_api | thegardenisland.com | 1 | 0.02% | 0.03% |
| news_api | thehardtackle.com | 1 | 0.02% | 0.03% |
| news_api | thehindubusinessline.com | 1 | 0.02% | 0.03% |
| news_api | theindependent.co.zw | 1 | 0.02% | 0.03% |
| news_api | theitem.com | 1 | 0.02% | 0.03% |
| news_api | thejournal.com | 1 | 0.02% | 0.03% |
| news_api | theleader.com.au | 1 | 0.02% | 0.03% |
| news_api | themissouritimes.com | 1 | 0.02% | 0.03% |
| news_api | themoscowtimes.com | 1 | 0.02% | 0.03% |
| news_api | thenational.scot | 1 | 0.02% | 0.03% |
| news_api | thepeterboroughexaminer.com | 1 | 0.02% | 0.03% |
| news_api | therecord.com | 1 | 0.02% | 0.03% |
| news_api | thesalemnewsonline.com | 1 | 0.02% | 0.03% |
| news_api | theshillongtimes.com | 1 | 0.02% | 0.03% |
| news_api | thespec.com | 1 | 0.02% | 0.03% |
| news_api | thestar.com.my | 1 | 0.02% | 0.03% |
| news_api | thesunchronicle.com | 1 | 0.02% | 0.03% |
| news_api | thetoc.gr | 1 | 0.02% | 0.03% |
| news_api | theverge.com | 1 | 0.02% | 0.03% |
| news_api | thirdsector.co.uk | 1 | 0.02% | 0.03% |
| news_api | thurrockgazette.co.uk | 1 | 0.02% | 0.03% |
| news_api | tickerreport.com | 1 | 0.02% | 0.03% |
| news_api | ticweb.es | 1 | 0.02% | 0.03% |
| news_api | times-standard.com | 1 | 0.02% | 0.03% |
| news_api | timesfreepress.com | 1 | 0.02% | 0.03% |
| news_api | timeshighereducation.com | 1 | 0.02% | 0.03% |
| news_api | timesleader.com | 1 | 0.02% | 0.03% |
| news_api | timesofsandiego.com | 1 | 0.02% | 0.03% |
| news_api | timeturk.com | 1 | 0.02% | 0.03% |
| news_api | tivi.fi | 1 | 0.02% | 0.03% |
| news_api | toffeeweb.com | 1 | 0.02% | 0.03% |
| news_api | tonyskansascity.com | 1 | 0.02% | 0.03% |
| news_api | top-channel.tv | 1 | 0.02% | 0.03% |
| news_api | topics.or.jp | 1 | 0.02% | 0.03% |
| news_api | toronto.citynews.ca | 1 | 0.02% | 0.03% |
| news_api | torquenews.com | 1 | 0.02% | 0.03% |
| news_api | totaltele.com | 1 | 0.02% | 0.03% |
| news_api | townandcountrymag.com | 1 | 0.02% | 0.03% |
| news_api | tradersmagazine.com | 1 | 0.02% | 0.03% |
| news_api | travelweekly.com.au | 1 | 0.02% | 0.03% |
| news_api | tribuna.com.mx | 1 | 0.02% | 0.03% |
| news_api | tribunademinas.com.br | 1 | 0.02% | 0.03% |
| news_api | troyrecord.com | 1 | 0.02% | 0.03% |
| news_api | trustedreviews.com | 1 | 0.02% | 0.03% |
| news_api | tucsonpost.com | 1 | 0.02% | 0.03% |
| news_api | tuttomercatoweb.com | 1 | 0.02% | 0.03% |
| news_api | tvline.com | 1 | 0.02% | 0.03% |
| news_api | tvxs.gr | 1 | 0.02% | 0.03% |
| news_api | twincities.com | 1 | 0.02% | 0.03% |
| news_api | twz.com | 1 | 0.02% | 0.03% |
| news_api | ugandaonline.net | 1 | 0.02% | 0.03% |
| news_api | ukrinform.ua | 1 | 0.02% | 0.03% |
| news_api | ultimahora.com | 1 | 0.02% | 0.03% |
| news_api | ultimahora.es | 1 | 0.02% | 0.03% |
| news_api | understandingwar.org | 1 | 0.02% | 0.03% |
| news_api | unsertirol24.com | 1 | 0.02% | 0.03% |
| news_api | upi.com | 1 | 0.02% | 0.03% |
| news_api | us.cnn.com | 1 | 0.02% | 0.03% |
| news_api | utilitydive.com | 1 | 0.02% | 0.03% |
| news_api | utv.ie | 1 | 0.02% | 0.03% |
| news_api | uzmanpara.milliyet.com.tr | 1 | 0.02% | 0.03% |
| news_api | vanguardia.com.mx | 1 | 0.02% | 0.03% |
| news_api | vecer.com | 1 | 0.02% | 0.03% |
| news_api | vecernji.ba | 1 | 0.02% | 0.03% |
| news_api | vernonmorningstar.com | 1 | 0.02% | 0.03% |
| news_api | vesti-ua.net | 1 | 0.02% | 0.03% |
| news_api | vice.com | 1 | 0.02% | 0.03% |
| news_api | vietnam.vnanet.vn | 1 | 0.02% | 0.03% |
| news_api | vir.com.vn | 1 | 0.02% | 0.03% |
| news_api | vm.ru | 1 | 0.02% | 0.03% |
| news_api | volksstimme.de | 1 | 0.02% | 0.03% |
| news_api | voria.gr | 1 | 0.02% | 0.03% |
| news_api | vrt.be | 1 | 0.02% | 0.03% |
| news_api | vv.com.ua | 1 | 0.02% | 0.03% |
| news_api | vz.lt | 1 | 0.02% | 0.03% |
| news_api | wahpetondailynews.com | 1 | 0.02% | 0.03% |
| news_api | walesonline.co.uk | 1 | 0.02% | 0.03% |
| news_api | wape.com | 1 | 0.02% | 0.03% |
| news_api | wapt.com | 1 | 0.02% | 0.03% |
| news_api | war.obozrevatel.com | 1 | 0.02% | 0.03% |
| news_api | warontherocks.com | 1 | 0.02% | 0.03% |
| news_api | warrackherald.com.au | 1 | 0.02% | 0.03% |
| news_api | washingtonexaminer.com | 1 | 0.02% | 0.03% |
| news_api | washingtonmonthly.com | 1 | 0.02% | 0.03% |
| news_api | watfordobserver.co.uk | 1 | 0.02% | 0.03% |
| news_api | watson.ch | 1 | 0.02% | 0.03% |
| news_api | wbkr.com | 1 | 0.02% | 0.03% |
| news_api | wboc.com | 1 | 0.02% | 0.03% |
| news_api | wcbi.com | 1 | 0.02% | 0.03% |
| news_api | wcbm.com | 1 | 0.02% | 0.03% |
| news_api | wdsu.com | 1 | 0.02% | 0.03% |
| news_api | webinars.govtech.com | 1 | 0.02% | 0.03% |
| news_api | webwire.com | 1 | 0.02% | 0.03% |
| news_api | weekend.perfil.com | 1 | 0.02% | 0.03% |
| news_api | weltwoche.ch | 1 | 0.02% | 0.03% |
| news_api | wfaa.com | 1 | 0.02% | 0.03% |
| news_api | wfmd.com | 1 | 0.02% | 0.03% |
| news_api | wftv.com | 1 | 0.02% | 0.03% |
| news_api | wgal.com | 1 | 0.02% | 0.03% |
| news_api | wgauradio.com | 1 | 0.02% | 0.03% |
| news_api | wgme.com | 1 | 0.02% | 0.03% |
| news_api | wgna.com | 1 | 0.02% | 0.03% |
| news_api | wgxa.tv | 1 | 0.02% | 0.03% |
| news_api | whittierdailynews.com | 1 | 0.02% | 0.03% |
| news_api | whmi.com | 1 | 0.02% | 0.03% |
| news_api | wiartonecho.com | 1 | 0.02% | 0.03% |
| news_api | wibx950.com | 1 | 0.02% | 0.03% |
| news_api | winfuture.de | 1 | 0.02% | 0.03% |
| news_api | wirtualnemedia.pl | 1 | 0.02% | 0.03% |
| news_api | wlos.com | 1 | 0.02% | 0.03% |
| news_api | wlox.com | 1 | 0.02% | 0.03% |
| news_api | wlwt.com | 1 | 0.02% | 0.03% |
| news_api | wlz-online.de | 1 | 0.02% | 0.03% |
| news_api | wmtw.com | 1 | 0.02% | 0.03% |
| news_api | wnnj.iheart.com | 1 | 0.02% | 0.03% |
| news_api | wokv.com | 1 | 0.02% | 0.03% |
| news_api | woman.excite.co.jp | 1 | 0.02% | 0.03% |
| news_api | words.filippo.io | 1 | 0.02% | 0.03% |
| news_api | world.kbs.co.kr | 1 | 0.02% | 0.03% |
| news_api | wosu.org | 1 | 0.02% | 0.03% |
| news_api | wowo.com | 1 | 0.02% | 0.03% |
| news_api | wpdh.com | 1 | 0.02% | 0.03% |
| news_api | wpxi.com | 1 | 0.02% | 0.03% |
| news_api | wral.com | 1 | 0.02% | 0.03% |
| news_api | wrmf.com | 1 | 0.02% | 0.03% |
| news_api | wsbradio.com | 1 | 0.02% | 0.03% |
| news_api | wset.com | 1 | 0.02% | 0.03% |
| news_api | wshu.org | 1 | 0.02% | 0.03% |
| news_api | wsoctv.com | 1 | 0.02% | 0.03% |
| news_api | wthr.com | 1 | 0.02% | 0.03% |
| news_api | wtsp.com | 1 | 0.02% | 0.03% |
| news_api | wusa9.com | 1 | 0.02% | 0.03% |
| news_api | wvtm13.com | 1 | 0.02% | 0.03% |
| news_api | wwltv.com | 1 | 0.02% | 0.03% |
| news_api | wwwhatsnew.com | 1 | 0.02% | 0.03% |
| news_api | wxii12.com | 1 | 0.02% | 0.03% |
| news_api | wxow.com | 1 | 0.02% | 0.03% |
| news_api | wyomingnews.com | 1 | 0.02% | 0.03% |
| news_api | wz-net.de | 1 | 0.02% | 0.03% |
| news_api | xx.sdnews.com.cn | 1 | 0.02% | 0.03% |
| news_api | y100fm.com | 1 | 0.02% | 0.03% |
| news_api | y95country.com | 1 | 0.02% | 0.03% |
| news_api | yankton.net | 1 | 0.02% | 0.03% |
| news_api | yasstribune.com.au | 1 | 0.02% | 0.03% |
| news_api | yenialanya.com | 1 | 0.02% | 0.03% |
| news_api | yerkir.am | 1 | 0.02% | 0.03% |
| news_api | yle.fi | 1 | 0.02% | 0.03% |
| news_api | yn.xinhuanet.com | 1 | 0.02% | 0.03% |
| news_api | yorkpress.co.uk | 1 | 0.02% | 0.03% |
| news_api | yourtango.com | 1 | 0.02% | 0.03% |
| news_api | zavtra.ru | 1 | 0.02% | 0.03% |
| news_api | zdg.md | 1 | 0.02% | 0.03% |
| news_api | zdnet.com | 1 | 0.02% | 0.03% |
| news_api | zetatijuana.com | 1 | 0.02% | 0.03% |
| news_api | ziarulnational.md | 1 | 0.02% | 0.03% |
| news_api | zvw.de | 1 | 0.02% | 0.03% |

## Top 30 Inspection Words By source_type

### cve

vulnerability (967), file (413), kernel (369), may (348), issue (339), fix (328), exploit (321), attackers (319), function (299), linux (288), used (287), following (285), resolved (270), attacker (268), attack (266), user (259), allows (257), access (253), manipulation (248), code (234), path (229), arbitrary (221), remote (207), argument (205), component (201), prior (196), version (194), data (192), system (189), affected (186)

### news_api

cyber (112), data (104), security (98), new (86), scam (76), says (74), breach (68), news (54), ransomware (49), malware (48), ddos (48), attack (47), report (46), cyberattack (46), financial (42), risk (42), stay (40), china (39), ontario (39), web (38), openai (36), aile (36), iran (35), exploit (35), trump (35), cybersecurity (34), safe (34), day (34), amid (34), may (34)

### news_rss

vulnerability (509), security (415), exploitation (381), windows (373), data (327), likely (302), access (288), less (240), process (226), code (209), privilege (207), new (206), elevation (198), file (191), microsoft (182), exploit (180), system (176), vulnerabilities (172), one (170), used (167), also (164), pointer (159), teams (157), using (155), attack (155), user (152), buffer (150), execution (145), would (143), attacks (138)

### reddit_rss

link (928), comments (918), submitted (900), like (299), security (235), would (229), use (224), one (211), data (194), work (168), people (167), windows (163), know (162), time (161), using (156), something (154), anyone (154), still (153), get (151), new (151), also (147), actually (143), need (142), don (141), access (134), https (131), want (131), even (124), help (117), user (116)
