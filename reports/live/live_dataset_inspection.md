# Live Dataset Inspection

Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 4025 |
| created_at min | 2025-12-16T09:00:00Z |
| created_at max | 2026-05-02T02:15:00Z |
| collected_at min | 2026-04-29T13:22:42Z |
| collected_at max | 2026-05-02T02:33:20Z |
| Unparsable created_at | 0 (0.00%) |
| Unparsable collected_at | 0 (0.00%) |
| Null/empty text_raw | 0 (0.00%) |
| Mean text_raw length | 484.92 |
| Median text_raw length | 124.0 |
| Min text_raw length | 8 |
| Max text_raw length | 66525 |
| text_raw < 30 chars | 80 (1.99%) |
| text_raw < 100 chars | 1756 (43.63%) |
| Duplicate id rows | 0 rows / 0 values |
| Duplicate url rows | 0 rows / 0 values |
| Duplicate normalized text_raw rows | 365 rows / 106 values |

## Warnings

- WARNING: Duplicate normalized text_raw rows found: 365.

## Rows By source_type

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1934 | 48.05% |
| cve | 1295 | 32.17% |
| reddit_rss | 604 | 15.01% |
| news_rss | 192 | 4.77% |

## Rows By source_name

| source_name | rows | percent_dataset |
| --- | --- | --- |
| NVD CVE | 1295 | 32.17% |
| cybersecurity | 132 | 3.28% |
| sysadmin | 127 | 3.16% |
| privacy | 75 | 1.86% |
| The Hacker News | 64 | 1.59% |
| blueteamsec | 54 | 1.34% |
| BleepingComputer | 38 | 0.94% |
| netsec | 36 | 0.89% |
| hacking | 35 | 0.87% |
| forbes.com | 35 | 0.87% |
| ReverseEngineering | 33 | 0.82% |
| techradar.com | 31 | 0.77% |
| osint | 30 | 0.75% |
| AskNetsec | 29 | 0.72% |
| Malware | 28 | 0.70% |
| ascii.jp | 28 | 0.70% |
| ComputerSecurity | 25 | 0.62% |
| Rapid7 Blog | 23 | 0.57% |
| cnews.ru | 23 | 0.57% |
| ithome.com.tw | 23 | 0.57% |
| bankinfosecurity.com | 18 | 0.45% |
| Unit 42 | 17 | 0.42% |
| Cisco Talos Blog | 16 | 0.40% |
| manilatimes.net | 16 | 0.40% |
| haberler.com | 16 | 0.40% |
| 163.com | 16 | 0.40% |
| theregister.com | 16 | 0.40% |
| itbrief.co.nz | 15 | 0.37% |
| SANS Internet Storm Center | 14 | 0.35% |
| govinfosecurity.com | 14 | 0.35% |
| esecurityplanet.com | 12 | 0.30% |
| finance.sina.com.cn | 12 | 0.30% |
| fnnews.com | 12 | 0.30% |
| KrebsOnSecurity | 11 | 0.27% |
| finanznachrichten.de | 11 | 0.27% |
| cointelegraph.com | 11 | 0.27% |
| economictimes.indiatimes.com | 11 | 0.27% |
| el-balad.com | 11 | 0.27% |
| csoonline.com | 10 | 0.25% |
| finance.yahoo.com | 10 | 0.25% |
| techcrunch.com | 10 | 0.25% |
| boredpanda.com | 10 | 0.25% |
| fool.com | 10 | 0.25% |
| Google Project Zero | 9 | 0.22% |
| infosecurity-magazine.com | 9 | 0.22% |
| timesofindia.indiatimes.com | 9 | 0.22% |
| baijiahao.baidu.com | 9 | 0.22% |
| jdsupra.com | 8 | 0.20% |
| moneycontrol.com | 8 | 0.20% |
| channellife.co.nz | 8 | 0.20% |
| biz.heraldcorp.com | 7 | 0.17% |
| govtech.com | 6 | 0.15% |
| prnewswire.com | 6 | 0.15% |
| edaily.co.kr | 6 | 0.15% |
| laopcion.com.mx | 6 | 0.15% |
| securitylab.ru | 6 | 0.15% |
| udayavani.com | 6 | 0.15% |
| tvguide.co.uk | 6 | 0.15% |
| birgun.net | 6 | 0.15% |
| yahoo.com | 5 | 0.12% |
| channellife.com.au | 5 | 0.12% |
| zdnet.co.kr | 5 | 0.12% |
| vz.ru | 5 | 0.12% |
| screenrant.com | 5 | 0.12% |
| foxnews.com | 5 | 0.12% |
| punchng.com | 5 | 0.12% |
| hothardware.com | 4 | 0.10% |
| japan.zdnet.com | 4 | 0.10% |
| insurancebusinessmag.com | 4 | 0.10% |
| winnipegfreepress.com | 4 | 0.10% |
| thenews.com.pk | 4 | 0.10% |
| pcmag.com | 4 | 0.10% |
| milliyet.com.tr | 4 | 0.10% |
| thefastmode.com | 4 | 0.10% |
| ddaily.co.kr | 4 | 0.10% |
| cbc.ca | 4 | 0.10% |
| aa.com.tr | 4 | 0.10% |
| kibrispostasi.com | 4 | 0.10% |
| theglobeandmail.com | 4 | 0.10% |
| heise.de | 4 | 0.10% |
| coindesk.com | 4 | 0.10% |
| dostor.org | 4 | 0.10% |
| 9to5mac.com | 4 | 0.10% |
| interfax.ru | 4 | 0.10% |
| itnews.com.au | 4 | 0.10% |
| time.mk | 4 | 0.10% |
| it-online.co.za | 4 | 0.10% |
| tn.com.ar | 4 | 0.10% |
| computing.co.uk | 4 | 0.10% |
| newjerseytelegraph.com | 4 | 0.10% |
| eturbonews.com | 4 | 0.10% |
| natlawreview.com | 4 | 0.10% |
| ghanamma.com | 4 | 0.10% |
| excite.co.jp | 4 | 0.10% |
| maliactu.net | 4 | 0.10% |
| androidauthority.com | 3 | 0.07% |
| mondaq.com | 3 | 0.07% |
| tomshardware.com | 3 | 0.07% |
| cnnturk.com | 3 | 0.07% |
| ura.news | 3 | 0.07% |
| donanimgunlugu.com | 3 | 0.07% |
| ensonhaber.com | 3 | 0.07% |
| womannews.net | 3 | 0.07% |
| miragenews.com | 3 | 0.07% |
| wesh.com | 3 | 0.07% |
| wbaltv.com | 3 | 0.07% |
| scoop.co.nz | 3 | 0.07% |
| straitstimes.com | 3 | 0.07% |
| politis.com.cy | 3 | 0.07% |
| koreaherald.com | 3 | 0.07% |
| nzherald.co.nz | 3 | 0.07% |
| sabah.com.tr | 3 | 0.07% |
| trthaber.com | 3 | 0.07% |
| eurointegration.com.ua | 3 | 0.07% |
| bleedingcool.com | 3 | 0.07% |
| wmur.com | 3 | 0.07% |
| defensenews.com | 3 | 0.07% |
| hindustantimes.com | 3 | 0.07% |
| n.yam.com | 3 | 0.07% |
| odatv.com | 3 | 0.07% |
| finance.eastmoney.com | 3 | 0.07% |
| shorouknews.com | 3 | 0.07% |
| freepressjournal.in | 3 | 0.07% |
| ria.ru | 3 | 0.07% |
| russian.rt.com | 3 | 0.07% |
| europapress.es | 3 | 0.07% |
| newswiretoday.com | 3 | 0.07% |
| portal.sina.com.hk | 3 | 0.07% |
| itbusinessnet.com | 3 | 0.07% |
| biometricupdate.com | 3 | 0.07% |
| itbear.com.cn | 3 | 0.07% |
| am.com.mx | 3 | 0.07% |
| natalie.mu | 3 | 0.07% |
| kmib.co.kr | 3 | 0.07% |
| divyabhaskar.co.in | 3 | 0.07% |
| tribuneindia.com | 3 | 0.07% |
| marketscreener.com | 3 | 0.07% |
| wired.com | 3 | 0.07% |
| itweb.co.za | 3 | 0.07% |
| evrensel.net | 3 | 0.07% |
| nypost.com | 3 | 0.07% |
| thenextweb.com | 3 | 0.07% |
| business.scoop.co.nz | 3 | 0.07% |
| claimsjournal.com | 3 | 0.07% |
| collider.com | 3 | 0.07% |
| itnewsonline.com | 3 | 0.07% |
| alltoc.com | 3 | 0.07% |
| thesun.ng | 3 | 0.07% |
| newsway.co.kr | 3 | 0.07% |
| iefimerida.gr | 3 | 0.07% |
| eurasiareview.com | 3 | 0.07% |
| businessghana.com | 2 | 0.05% |
| digitaljournal.com | 2 | 0.05% |
| securityinfowatch.com | 2 | 0.05% |
| gizmodo.com | 2 | 0.05% |
| insurancejournal.com | 2 | 0.05% |
| inforum.com | 2 | 0.05% |
| computerweekly.com | 2 | 0.05% |
| pymnts.com | 2 | 0.05% |
| bleepingcomputer.com | 2 | 0.05% |
| wsbtv.com | 2 | 0.05% |
| phonandroid.com | 2 | 0.05% |
| propakistani.pk | 2 | 0.05% |
| life.ru | 2 | 0.05% |
| github.com | 2 | 0.05% |
| hollywoodreporter.com | 2 | 0.05% |
| sb.by | 2 | 0.05% |
| t-online.de | 2 | 0.05% |
| freemalaysiatoday.com | 2 | 0.05% |
| iz.ru | 2 | 0.05% |
| lenta.ru | 2 | 0.05% |
| glavcom.ua | 2 | 0.05% |
| bunburymail.com.au | 2 | 0.05% |
| nvi.com.au | 2 | 0.05% |
| bankingnews.gr | 2 | 0.05% |
| dailykos.com | 2 | 0.05% |
| lalsace.fr | 2 | 0.05% |
| elmanana.com | 2 | 0.05% |
| news.cn | 2 | 0.05% |
| wiwo.de | 2 | 0.05% |
| wdrb.com | 2 | 0.05% |
| riasv.ru | 2 | 0.05% |
| aol.co.uk | 2 | 0.05% |
| lbc.co.uk | 2 | 0.05% |
| wwmt.com | 2 | 0.05% |
| jpost.com | 2 | 0.05% |
| udn.com | 2 | 0.05% |
| bd-pratidin.com | 2 | 0.05% |
| hurriyetdailynews.com | 2 | 0.05% |
| wfmz.com | 2 | 0.05% |
| hinews.cn | 2 | 0.05% |
| tech.caijing.com.cn | 2 | 0.05% |
| tech.ifeng.com | 2 | 0.05% |
| androidheadlines.com | 2 | 0.05% |
| vietnamnet.vn | 2 | 0.05% |
| vesti.ru | 2 | 0.05% |
| jawapos.com | 2 | 0.05% |
| fontanka.ru | 2 | 0.05% |
| 1prime.ru | 2 | 0.05% |
| kommersant.ru | 2 | 0.05% |
| politika.rs | 2 | 0.05% |
| vg.no | 2 | 0.05% |
| vedomosti.ru | 2 | 0.05% |
| weser-kurier.de | 2 | 0.05% |
| irishdentist.ie | 2 | 0.05% |
| unian.net | 2 | 0.05% |
| ntdtv.com | 2 | 0.05% |
| comnews.ru | 2 | 0.05% |
| securitybrief.news | 2 | 0.05% |
| itwire.com | 2 | 0.05% |
| jugantor.com | 2 | 0.05% |
| webpronews.com | 2 | 0.05% |
| htxt.co.za | 2 | 0.05% |
| makeuseof.com | 2 | 0.05% |
| infoworld.com | 2 | 0.05% |
| bjnews.com.cn | 2 | 0.05% |
| stcn.com | 2 | 0.05% |
| military.china.com | 2 | 0.05% |
| antaranews.com | 2 | 0.05% |
| nikkei.com | 2 | 0.05% |
| arstechnica.com | 2 | 0.05% |
| senego.com | 2 | 0.05% |
| index.hr | 2 | 0.05% |
| cloud.watch.impress.co.jp | 2 | 0.05% |
| eldia.com.bo | 2 | 0.05% |
| eldestapeweb.com | 2 | 0.05% |
| businessday.co.za | 2 | 0.05% |
| elsiglodetorreon.com.mx | 2 | 0.05% |
| insight.co.kr | 2 | 0.05% |
| newspim.com | 2 | 0.05% |
| inews24.com | 2 | 0.05% |
| etoday.co.kr | 2 | 0.05% |
| segye.com | 2 | 0.05% |
| thehindu.com | 2 | 0.05% |
| hindi.webdunia.com | 2 | 0.05% |
| inewsgr.com | 2 | 0.05% |
| geeky-gadgets.com | 2 | 0.05% |
| kten.com | 2 | 0.05% |
| americanbanker.com | 2 | 0.05% |
| hawaiitelegraph.com | 2 | 0.05% |
| tennesseedaily.com | 2 | 0.05% |
| posta.com.tr | 2 | 0.05% |
| begeek.fr | 2 | 0.05% |
| mersinhaber.com | 2 | 0.05% |
| lrytas.lt | 2 | 0.05% |
| tgrthaber.com | 2 | 0.05% |
| lefigaro.fr | 2 | 0.05% |
| sozcu.com.tr | 2 | 0.05% |
| pcwplus.hu | 2 | 0.05% |
| sanantoniopost.com | 2 | 0.05% |
| aninews.in | 2 | 0.05% |
| capital.ro | 2 | 0.05% |
| aceshowbiz.com | 2 | 0.05% |
| haber1.com | 2 | 0.05% |
| deadline.com | 2 | 0.05% |
| macleayargus.com.au | 2 | 0.05% |
| investegate.co.uk | 2 | 0.05% |
| unternehmen-heute.de | 2 | 0.05% |
| arkansasonline.com | 2 | 0.05% |
| uainfo.org | 2 | 0.05% |
| dailyemerald.com | 2 | 0.05% |
| fox4news.com | 2 | 0.05% |
| livenews.co.nz | 2 | 0.05% |
| medianama.com | 2 | 0.05% |
| allafrica.com | 2 | 0.05% |
| ecodibergamo.it | 2 | 0.05% |
| daily.com.ua | 2 | 0.05% |
| naftemporiki.gr | 2 | 0.05% |
| eldiariodechihuahua.mx | 2 | 0.05% |
| libnanews.com | 2 | 0.05% |
| techweez.com | 2 | 0.05% |
| rediff.com | 2 | 0.05% |
| thisdaylive.com | 2 | 0.05% |
| welivesecurity.com | 2 | 0.05% |
| yorkregion.com | 2 | 0.05% |
| insideottawavalley.com | 2 | 0.05% |
| tmtpost.com | 2 | 0.05% |
| pv-magazine.com | 2 | 0.05% |
| massachusettssun.com | 2 | 0.05% |
| europesun.com | 2 | 0.05% |
| wzzm13.com | 2 | 0.05% |
| sentinel.ht | 2 | 0.05% |
| globalnews.ca | 2 | 0.05% |
| pravda.ru | 2 | 0.05% |
| danas.rs | 2 | 0.05% |
| castanetkamloops.net | 2 | 0.05% |
| abovethelaw.com | 2 | 0.05% |
| mainichi.jp | 2 | 0.05% |
| boerse-express.com | 2 | 0.05% |
| newratings.de | 2 | 0.05% |
| morningstar.com | 2 | 0.05% |
| dailybreeze.com | 2 | 0.05% |
| dailynews.com | 2 | 0.05% |
| sgvtribune.com | 2 | 0.05% |
| lelezard.com | 2 | 0.05% |
| greeleytribune.com | 2 | 0.05% |
| gdnonline.com | 2 | 0.05% |
| y-mainichi.co.jp | 2 | 0.05% |
| heraldk.com | 2 | 0.05% |
| nikkan-gendai.com | 2 | 0.05% |
| kathimerini.com.cy | 2 | 0.05% |
| ecommercenews.co.nz | 2 | 0.05% |
| vetogate.com | 2 | 0.05% |
| newkerala.com | 2 | 0.05% |
| diariosur.es | 2 | 0.05% |
| unn.ua | 2 | 0.05% |
| rpp.pe | 2 | 0.05% |
| ecodisicilia.com | 2 | 0.05% |
| focus.ua | 2 | 0.05% |
| business24.ro | 2 | 0.05% |
| storm.mg | 2 | 0.05% |
| abc.es | 2 | 0.05% |
| busan.com | 2 | 0.05% |
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
| adevarul.ro | 1 | 0.02% |
| bgr.com | 1 | 0.02% |
| express.pk | 1 | 0.02% |
| presse-citron.net | 1 | 0.02% |
| techcabal.com | 1 | 0.02% |
| bangkokbiznews.com | 1 | 0.02% |
| 01net.com | 1 | 0.02% |
| aif.ru | 1 | 0.02% |
| digg.com | 1 | 0.02% |
| etnews.com | 1 | 0.02% |
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
| lexpress.fr | 1 | 0.02% |
| pln-pskov.ru | 1 | 0.02% |
| metroseoul.co.kr | 1 | 0.02% |
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
| dnews.gr | 1 | 0.02% |
| infobae.com | 1 | 0.02% |
| ledauphine.com | 1 | 0.02% |
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
| eluniversal.com.mx | 1 | 0.02% |
| aristeguinoticias.com | 1 | 0.02% |
| funkytaurusmedia.com | 1 | 0.02% |
| dw.com | 1 | 0.02% |
| botasot.info | 1 | 0.02% |
| fnp.de | 1 | 0.02% |
| tagesschau.de | 1 | 0.02% |
| ratopati.com | 1 | 0.02% |
| op-online.de | 1 | 0.02% |
| zeit.de | 1 | 0.02% |
| watson.ch | 1 | 0.02% |
| freiepresse.de | 1 | 0.02% |
| yeniakit.com.tr | 1 | 0.02% |
| turkiyegazetesi.com.tr | 1 | 0.02% |
| stern.de | 1 | 0.02% |
| ntv.com.tr | 1 | 0.02% |
| kannadaprabha.com | 1 | 0.02% |
| n-tv.de | 1 | 0.02% |
| sn.at | 1 | 0.02% |
| bursahakimiyet.com.tr | 1 | 0.02% |
| dunya.com | 1 | 0.02% |
| sdpnoticias.com | 1 | 0.02% |
| vecer.com | 1 | 0.02% |
| rtl.nl | 1 | 0.02% |
| norran.se | 1 | 0.02% |
| computerworld.dk | 1 | 0.02% |
| aktifhaber.com | 1 | 0.02% |
| sana.sy | 1 | 0.02% |
| welt.de | 1 | 0.02% |
| japan.cnet.com | 1 | 0.02% |
| vrt.be | 1 | 0.02% |
| donanimhaber.com | 1 | 0.02% |
| dailynews.co.th | 1 | 0.02% |
| heute.at | 1 | 0.02% |
| bankier.pl | 1 | 0.02% |
| antena3.ro | 1 | 0.02% |
| businesstoday.in | 1 | 0.02% |
| 5.ua | 1 | 0.02% |
| kcci.com | 1 | 0.02% |
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
| haberturk.com | 1 | 0.02% |
| ondacero.es | 1 | 0.02% |
| dailysabah.com | 1 | 0.02% |
| designboom.com | 1 | 0.02% |
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
| techtimes.com | 1 | 0.02% |
| top-channel.tv | 1 | 0.02% |
| jo24.net | 1 | 0.02% |
| panorama.com.al | 1 | 0.02% |
| gamerant.com | 1 | 0.02% |
| balkanweb.com | 1 | 0.02% |
| theblaze.com | 1 | 0.02% |
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
| mashable.com | 1 | 0.02% |
| volksstimme.de | 1 | 0.02% |
| handelsblatt.com | 1 | 0.02% |
| sueddeutsche.de | 1 | 0.02% |
| cepro.com | 1 | 0.02% |
| corp.cnews.ru | 1 | 0.02% |
| vesti-ua.net | 1 | 0.02% |
| slguardian.org | 1 | 0.02% |
| chip.de | 1 | 0.02% |
| tivi.fi | 1 | 0.02% |
| strategypage.com | 1 | 0.02% |
| alaskasnewssource.com | 1 | 0.02% |
| risky.biz | 1 | 0.02% |
| zdnet.com | 1 | 0.02% |
| tekniikkatalous.fi | 1 | 0.02% |
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
| newsweek.com | 1 | 0.02% |
| news.china.com.cn | 1 | 0.02% |
| liputan6.com | 1 | 0.02% |
| webinars.govtech.com | 1 | 0.02% |
| newtalk.tw | 1 | 0.02% |
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
| ibtimes.com.au | 1 | 0.02% |
| diariodemorelos.com | 1 | 0.02% |
| mobileidworld.com | 1 | 0.02% |
| inwestycje.pl | 1 | 0.02% |
| words.filippo.io | 1 | 0.02% |
| elpais.com.uy | 1 | 0.02% |
| quadratin.com.mx | 1 | 0.02% |
| nikkan.co.jp | 1 | 0.02% |
| mariettatimes.com | 1 | 0.02% |
| statecollege.com | 1 | 0.02% |
| jowhar.com | 1 | 0.02% |
| ohmynews.com | 1 | 0.02% |
| ihalla.com | 1 | 0.02% |
| maharashtratimes.com | 1 | 0.02% |
| travelweekly.com.au | 1 | 0.02% |
| hani.co.kr | 1 | 0.02% |
| journalgazette.net | 1 | 0.02% |
| austinchronicle.com | 1 | 0.02% |
| ktvu.com | 1 | 0.02% |
| pitchfork.com | 1 | 0.02% |
| mathrubhumi.com | 1 | 0.02% |
| divyamarathi.bhaskar.com | 1 | 0.02% |
| digi24.ro | 1 | 0.02% |
| rappler.com | 1 | 0.02% |
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
| livehindustan.com | 1 | 0.02% |
| newsbomb.gr | 1 | 0.02% |
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
| ibtimes.co.uk | 1 | 0.02% |
| metronews.ru | 1 | 0.02% |
| dha.com.tr | 1 | 0.02% |
| haksozhaber.net | 1 | 0.02% |
| mngz.ru | 1 | 0.02% |
| cafebiz.vn | 1 | 0.02% |
| lgz.ru | 1 | 0.02% |
| canardpc.com | 1 | 0.02% |
| diyarbakirsoz.com | 1 | 0.02% |
| lakersnation.com | 1 | 0.02% |
| yeniasya.com.tr | 1 | 0.02% |
| stockbiz.vn | 1 | 0.02% |
| lite987.com | 1 | 0.02% |
| 961theeagle.com | 1 | 0.02% |
| wibx950.com | 1 | 0.02% |
| southernhighlandnews.com.au | 1 | 0.02% |
| wgna.com | 1 | 0.02% |
| biz.cnews.ru | 1 | 0.02% |
| mississauga.com | 1 | 0.02% |
| memeburn.com | 1 | 0.02% |
| igamingbusiness.com | 1 | 0.02% |
| helpconsumatori.it | 1 | 0.02% |
| themissouritimes.com | 1 | 0.02% |
| newstribune.com | 1 | 0.02% |
| iraqsun.com | 1 | 0.02% |
| portalsamorzadowy.pl | 1 | 0.02% |
| livemint.com | 1 | 0.02% |
| nearshoreamericas.com | 1 | 0.02% |
| inquirer.com | 1 | 0.02% |
| thefrontierpost.com | 1 | 0.02% |
| upi.com | 1 | 0.02% |
| koreatimes.co.kr | 1 | 0.02% |
| dynamicbusiness.com | 1 | 0.02% |
| zonebourse.com | 1 | 0.02% |
| interaksyon.philstar.com | 1 | 0.02% |
| timeslive.co.za | 1 | 0.02% |
| nbcmontana.com | 1 | 0.02% |
| clydebankpost.co.uk | 1 | 0.02% |
| tagesanzeiger.ch | 1 | 0.02% |
| zazoom.it | 1 | 0.02% |
| bernerzeitung.ch | 1 | 0.02% |
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
| watoday.com.au | 1 | 0.02% |
| nwaonline.com | 1 | 0.02% |
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
| presstv.ir | 1 | 0.02% |
| polygon.com | 1 | 0.02% |
| aljazeera.net | 1 | 0.02% |
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
| index.hu | 1 | 0.02% |
| economx.hu | 1 | 0.02% |
| spartanavenue.com | 1 | 0.02% |
| rnz.co.nz | 1 | 0.02% |
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
| diario.mx | 1 | 0.02% |
| it.euronews.com | 1 | 0.02% |
| downtoearth.org.in | 1 | 0.02% |
| ly.fjsen.com | 1 | 0.02% |
| publico.pt | 1 | 0.02% |
| lagacetadesalamanca.es | 1 | 0.02% |
| marca.com | 1 | 0.02% |
| weekend.perfil.com | 1 | 0.02% |
| jogja.tribunnews.com | 1 | 0.02% |
| inosmi.ru | 1 | 0.02% |
| kontrakty.ua | 1 | 0.02% |
| laut.de | 1 | 0.02% |
| cjme.com | 1 | 0.02% |
| megamodo.com | 1 | 0.02% |
| brasil247.com | 1 | 0.02% |
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
| dailypolitical.com | 1 | 0.02% |
| jagranjosh.com | 1 | 0.02% |
| 24sata.hr | 1 | 0.02% |
| net.hr | 1 | 0.02% |
| wallstreet-online.de | 1 | 0.02% |
| dp.ru | 1 | 0.02% |
| amic.ru | 1 | 0.02% |
| meridiano.net | 1 | 0.02% |
| niagarathisweek.com | 1 | 0.02% |
| simcoe.com | 1 | 0.02% |
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
| chinanationalnews.com | 1 | 0.02% |
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
| dailypioneer.com | 1 | 0.02% |
| newrepublic.com | 1 | 0.02% |
| jamaicaobserver.com | 1 | 0.02% |
| itbrief.news | 1 | 0.02% |
| rstreet.org | 1 | 0.02% |
| insidermonkey.com | 1 | 0.02% |
| wcvb.com | 1 | 0.02% |
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
| objectiv.tv | 1 | 0.02% |
| lesmobiles.com | 1 | 0.02% |
| toffeeweb.com | 1 | 0.02% |
| 10tv.com | 1 | 0.02% |
| dailyinqilab.com | 1 | 0.02% |
| asianews.it | 1 | 0.02% |
| cp24.com | 1 | 0.02% |
| wshu.org | 1 | 0.02% |
| brandonsun.com | 1 | 0.02% |
| kiplinger.com | 1 | 0.02% |
| cambridgetimes.ca | 1 | 0.02% |
| mactech.com | 1 | 0.02% |
| brooklyneagle.com | 1 | 0.02% |
| laleggepertutti.it | 1 | 0.02% |
| rtv.rs | 1 | 0.02% |
| niezalezna.pl | 1 | 0.02% |
| taz.de | 1 | 0.02% |
| dailypakistan.pk | 1 | 0.02% |
| wirtualnemedia.pl | 1 | 0.02% |
| prensalibre.com | 1 | 0.02% |
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
| brisbanetimes.com.au | 1 | 0.02% |
| sandiegouniontribune.com | 1 | 0.02% |
| reporterherald.com | 1 | 0.02% |
| theage.com.au | 1 | 0.02% |
| smh.com.au | 1 | 0.02% |
| mdjonline.com | 1 | 0.02% |
| dglobe.com | 1 | 0.02% |
| echopress.com | 1 | 0.02% |
| placenorthwest.co.uk | 1 | 0.02% |
| troyrecord.com | 1 | 0.02% |
| spokesman.com | 1 | 0.02% |
| whittierdailynews.com | 1 | 0.02% |
| irishtimes.com | 1 | 0.02% |
| wboc.com | 1 | 0.02% |
| theindependent.co.zw | 1 | 0.02% |
| dailymail.com | 1 | 0.02% |
| alquds.co.uk | 1 | 0.02% |
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
| toonippo.co.jp | 1 | 0.02% |
| redlandsdailyfacts.com | 1 | 0.02% |
| timesofsandiego.com | 1 | 0.02% |
| wikitree.co.kr | 1 | 0.02% |
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
| netzwelt.de | 1 | 0.02% |
| t13.cl | 1 | 0.02% |
| kwcdcountry.com | 1 | 0.02% |
| choice.com.au | 1 | 0.02% |
| ostro.org | 1 | 0.02% |
| batonrougepost.com | 1 | 0.02% |
| cincinnatisun.com | 1 | 0.02% |
| ohiostandard.com | 1 | 0.02% |
| oklahomastar.com | 1 | 0.02% |
| russiaherald.com | 1 | 0.02% |
| texasguardian.com | 1 | 0.02% |
| neworleanssun.com | 1 | 0.02% |
| japanherald.com | 1 | 0.02% |
| tucsonpost.com | 1 | 0.02% |
| arabherald.com | 1 | 0.02% |
| greekherald.com | 1 | 0.02% |
| floridastatesman.com | 1 | 0.02% |
| bignewsnetwork.com | 1 | 0.02% |
| hokkoku.co.jp | 1 | 0.02% |
| noviny.sk | 1 | 0.02% |
| cas.sk | 1 | 0.02% |
| econotimes.com | 1 | 0.02% |
| austinglobe.com | 1 | 0.02% |
| londonlovesbusiness.com | 1 | 0.02% |
| blogs.diariovasco.com | 1 | 0.02% |
| sapo.pt | 1 | 0.02% |
| hespress.com | 1 | 0.02% |
| diariodeburgos.es | 1 | 0.02% |
| filmfare.com | 1 | 0.02% |
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
| radiofrance.fr | 1 | 0.02% |
| financialafrik.com | 1 | 0.02% |
| hoy.es | 1 | 0.02% |
| eadt.co.uk | 1 | 0.02% |
| blog.wenxuecity.com | 1 | 0.02% |
| elpais.com | 1 | 0.02% |
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
| theguardian.com | 1 | 0.02% |
| astroawani.com | 1 | 0.02% |
| merkur.de | 1 | 0.02% |
| pleinevie.fr | 1 | 0.02% |
| nile.eg | 1 | 0.02% |
| uzmanpara.milliyet.com.tr | 1 | 0.02% |
| internasional.kompas.com | 1 | 0.02% |
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
| howtogeek.com | 1 | 0.02% |
| ahaber.com.tr | 1 | 0.02% |
| turktime.com | 1 | 0.02% |
| haber7.com | 1 | 0.02% |
| son.tv | 1 | 0.02% |
| haberyazar.com | 1 | 0.02% |
| news.mail.ru | 1 | 0.02% |
| hometownstation.com | 1 | 0.02% |
| dakotawarcollege.com | 1 | 0.02% |
| navhindtimes.in | 1 | 0.02% |
| am1150.ca | 1 | 0.02% |
| theitem.com | 1 | 0.02% |
| denizlihaber.com | 1 | 0.02% |
| wfmd.com | 1 | 0.02% |
| 24tv.ua | 1 | 0.02% |
| diariosigloxxi.com | 1 | 0.02% |
| radikal.com.tr | 1 | 0.02% |
| anlatilaninotesi.com.tr | 1 | 0.02% |
| guelphmercury.com | 1 | 0.02% |
| crestonnews.com | 1 | 0.02% |
| thanhnien.vn | 1 | 0.02% |
| hawaiinewsnow.com | 1 | 0.02% |
| mk.ru | 1 | 0.02% |
| thegardenisland.com | 1 | 0.02% |
| thurrockgazette.co.uk | 1 | 0.02% |
| mix941kmxj.com | 1 | 0.02% |
| newsprom.ru | 1 | 0.02% |
| maldonandburnhamstandard.co.uk | 1 | 0.02% |
| clactonandfrintongazette.co.uk | 1 | 0.02% |
| tumentoday.ru | 1 | 0.02% |
| notimerica.com | 1 | 0.02% |
| t-l.ru | 1 | 0.02% |
| pctechmag.com | 1 | 0.02% |
| nuevodiarioweb.com.ar | 1 | 0.02% |
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
| vicnews.com | 1 | 0.02% |
| vanguardia.com.mx | 1 | 0.02% |
| reporterdiario.com.br | 1 | 0.02% |
| avn.info.ve | 1 | 0.02% |
| ciudadccs.info | 1 | 0.02% |
| thebftonline.com | 1 | 0.02% |
| santamariatimes.com | 1 | 0.02% |
| xx.sdnews.com.cn | 1 | 0.02% |
| elmundo.es | 1 | 0.02% |
| 620ckrm.com | 1 | 0.02% |
| mundiario.com | 1 | 0.02% |
| elcorreo.com | 1 | 0.02% |
| radiopolar.com | 1 | 0.02% |
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
| albiladpress.com | 1 | 0.02% |
| cbs2iowa.com | 1 | 0.02% |
| burgundywave.com | 1 | 0.02% |
| dailybulletin.com | 1 | 0.02% |
| wset.com | 1 | 0.02% |
| timesleader.com | 1 | 0.02% |
| understandingwar.org | 1 | 0.02% |
| radiotamazuj.org | 1 | 0.02% |
| townhall.com | 1 | 0.02% |
| ziare.com | 1 | 0.02% |
| tvline.com | 1 | 0.02% |
| breitbart.com | 1 | 0.02% |
| wcbm.com | 1 | 0.02% |
| sbsun.com | 1 | 0.02% |
| t3n.de | 1 | 0.02% |
| lb.ua | 1 | 0.02% |
| riotimesonline.com | 1 | 0.02% |
| latimes.com | 1 | 0.02% |
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
| koreatimes.com | 1 | 0.02% |

## Source Distribution

| source_type | source_name | rows | percent_dataset | percent_source_type |
| --- | --- | --- | --- | --- |
| cve | NVD CVE | 1295 | 32.17% | 100.00% |
| reddit_rss | cybersecurity | 132 | 3.28% | 21.85% |
| reddit_rss | sysadmin | 127 | 3.16% | 21.03% |
| reddit_rss | privacy | 75 | 1.86% | 12.42% |
| news_rss | The Hacker News | 64 | 1.59% | 33.33% |
| reddit_rss | blueteamsec | 54 | 1.34% | 8.94% |
| news_rss | BleepingComputer | 38 | 0.94% | 19.79% |
| reddit_rss | netsec | 36 | 0.89% | 5.96% |
| news_api | forbes.com | 35 | 0.87% | 1.81% |
| reddit_rss | hacking | 35 | 0.87% | 5.79% |
| reddit_rss | ReverseEngineering | 33 | 0.82% | 5.46% |
| news_api | techradar.com | 31 | 0.77% | 1.60% |
| reddit_rss | osint | 30 | 0.75% | 4.97% |
| reddit_rss | AskNetsec | 29 | 0.72% | 4.80% |
| news_api | ascii.jp | 28 | 0.70% | 1.45% |
| reddit_rss | Malware | 28 | 0.70% | 4.64% |
| reddit_rss | ComputerSecurity | 25 | 0.62% | 4.14% |
| news_api | cnews.ru | 23 | 0.57% | 1.19% |
| news_api | ithome.com.tw | 23 | 0.57% | 1.19% |
| news_rss | Rapid7 Blog | 23 | 0.57% | 11.98% |
| news_api | bankinfosecurity.com | 18 | 0.45% | 0.93% |
| news_rss | Unit 42 | 17 | 0.42% | 8.85% |
| news_api | 163.com | 16 | 0.40% | 0.83% |
| news_api | haberler.com | 16 | 0.40% | 0.83% |
| news_api | manilatimes.net | 16 | 0.40% | 0.83% |
| news_api | theregister.com | 16 | 0.40% | 0.83% |
| news_rss | Cisco Talos Blog | 16 | 0.40% | 8.33% |
| news_api | itbrief.co.nz | 15 | 0.37% | 0.78% |
| news_api | govinfosecurity.com | 14 | 0.35% | 0.72% |
| news_rss | SANS Internet Storm Center | 14 | 0.35% | 7.29% |
| news_api | esecurityplanet.com | 12 | 0.30% | 0.62% |
| news_api | finance.sina.com.cn | 12 | 0.30% | 0.62% |
| news_api | fnnews.com | 12 | 0.30% | 0.62% |
| news_api | cointelegraph.com | 11 | 0.27% | 0.57% |
| news_api | economictimes.indiatimes.com | 11 | 0.27% | 0.57% |
| news_api | el-balad.com | 11 | 0.27% | 0.57% |
| news_api | finanznachrichten.de | 11 | 0.27% | 0.57% |
| news_rss | KrebsOnSecurity | 11 | 0.27% | 5.73% |
| news_api | boredpanda.com | 10 | 0.25% | 0.52% |
| news_api | csoonline.com | 10 | 0.25% | 0.52% |
| news_api | finance.yahoo.com | 10 | 0.25% | 0.52% |
| news_api | fool.com | 10 | 0.25% | 0.52% |
| news_api | techcrunch.com | 10 | 0.25% | 0.52% |
| news_api | baijiahao.baidu.com | 9 | 0.22% | 0.47% |
| news_api | infosecurity-magazine.com | 9 | 0.22% | 0.47% |
| news_api | timesofindia.indiatimes.com | 9 | 0.22% | 0.47% |
| news_rss | Google Project Zero | 9 | 0.22% | 4.69% |
| news_api | channellife.co.nz | 8 | 0.20% | 0.41% |
| news_api | jdsupra.com | 8 | 0.20% | 0.41% |
| news_api | moneycontrol.com | 8 | 0.20% | 0.41% |
| news_api | biz.heraldcorp.com | 7 | 0.17% | 0.36% |
| news_api | birgun.net | 6 | 0.15% | 0.31% |
| news_api | edaily.co.kr | 6 | 0.15% | 0.31% |
| news_api | govtech.com | 6 | 0.15% | 0.31% |
| news_api | laopcion.com.mx | 6 | 0.15% | 0.31% |
| news_api | prnewswire.com | 6 | 0.15% | 0.31% |
| news_api | securitylab.ru | 6 | 0.15% | 0.31% |
| news_api | tvguide.co.uk | 6 | 0.15% | 0.31% |
| news_api | udayavani.com | 6 | 0.15% | 0.31% |
| news_api | channellife.com.au | 5 | 0.12% | 0.26% |
| news_api | foxnews.com | 5 | 0.12% | 0.26% |
| news_api | punchng.com | 5 | 0.12% | 0.26% |
| news_api | screenrant.com | 5 | 0.12% | 0.26% |
| news_api | vz.ru | 5 | 0.12% | 0.26% |
| news_api | yahoo.com | 5 | 0.12% | 0.26% |
| news_api | zdnet.co.kr | 5 | 0.12% | 0.26% |
| news_api | 9to5mac.com | 4 | 0.10% | 0.21% |
| news_api | aa.com.tr | 4 | 0.10% | 0.21% |
| news_api | cbc.ca | 4 | 0.10% | 0.21% |
| news_api | coindesk.com | 4 | 0.10% | 0.21% |
| news_api | computing.co.uk | 4 | 0.10% | 0.21% |
| news_api | ddaily.co.kr | 4 | 0.10% | 0.21% |
| news_api | dostor.org | 4 | 0.10% | 0.21% |
| news_api | eturbonews.com | 4 | 0.10% | 0.21% |
| news_api | excite.co.jp | 4 | 0.10% | 0.21% |
| news_api | ghanamma.com | 4 | 0.10% | 0.21% |
| news_api | heise.de | 4 | 0.10% | 0.21% |
| news_api | hothardware.com | 4 | 0.10% | 0.21% |
| news_api | insurancebusinessmag.com | 4 | 0.10% | 0.21% |
| news_api | interfax.ru | 4 | 0.10% | 0.21% |
| news_api | it-online.co.za | 4 | 0.10% | 0.21% |
| news_api | itnews.com.au | 4 | 0.10% | 0.21% |
| news_api | japan.zdnet.com | 4 | 0.10% | 0.21% |
| news_api | kibrispostasi.com | 4 | 0.10% | 0.21% |
| news_api | maliactu.net | 4 | 0.10% | 0.21% |
| news_api | milliyet.com.tr | 4 | 0.10% | 0.21% |
| news_api | natlawreview.com | 4 | 0.10% | 0.21% |
| news_api | newjerseytelegraph.com | 4 | 0.10% | 0.21% |
| news_api | pcmag.com | 4 | 0.10% | 0.21% |
| news_api | thefastmode.com | 4 | 0.10% | 0.21% |
| news_api | theglobeandmail.com | 4 | 0.10% | 0.21% |
| news_api | thenews.com.pk | 4 | 0.10% | 0.21% |
| news_api | time.mk | 4 | 0.10% | 0.21% |
| news_api | tn.com.ar | 4 | 0.10% | 0.21% |
| news_api | winnipegfreepress.com | 4 | 0.10% | 0.21% |
| news_api | alltoc.com | 3 | 0.07% | 0.16% |
| news_api | am.com.mx | 3 | 0.07% | 0.16% |
| news_api | androidauthority.com | 3 | 0.07% | 0.16% |
| news_api | biometricupdate.com | 3 | 0.07% | 0.16% |
| news_api | bleedingcool.com | 3 | 0.07% | 0.16% |
| news_api | business.scoop.co.nz | 3 | 0.07% | 0.16% |
| news_api | claimsjournal.com | 3 | 0.07% | 0.16% |
| news_api | cnnturk.com | 3 | 0.07% | 0.16% |
| news_api | collider.com | 3 | 0.07% | 0.16% |
| news_api | defensenews.com | 3 | 0.07% | 0.16% |
| news_api | divyabhaskar.co.in | 3 | 0.07% | 0.16% |
| news_api | donanimgunlugu.com | 3 | 0.07% | 0.16% |
| news_api | ensonhaber.com | 3 | 0.07% | 0.16% |
| news_api | eurasiareview.com | 3 | 0.07% | 0.16% |
| news_api | eurointegration.com.ua | 3 | 0.07% | 0.16% |
| news_api | europapress.es | 3 | 0.07% | 0.16% |
| news_api | evrensel.net | 3 | 0.07% | 0.16% |
| news_api | finance.eastmoney.com | 3 | 0.07% | 0.16% |
| news_api | freepressjournal.in | 3 | 0.07% | 0.16% |
| news_api | hindustantimes.com | 3 | 0.07% | 0.16% |
| news_api | iefimerida.gr | 3 | 0.07% | 0.16% |
| news_api | itbear.com.cn | 3 | 0.07% | 0.16% |
| news_api | itbusinessnet.com | 3 | 0.07% | 0.16% |
| news_api | itnewsonline.com | 3 | 0.07% | 0.16% |
| news_api | itweb.co.za | 3 | 0.07% | 0.16% |
| news_api | kmib.co.kr | 3 | 0.07% | 0.16% |
| news_api | koreaherald.com | 3 | 0.07% | 0.16% |
| news_api | marketscreener.com | 3 | 0.07% | 0.16% |
| news_api | miragenews.com | 3 | 0.07% | 0.16% |
| news_api | mondaq.com | 3 | 0.07% | 0.16% |
| news_api | n.yam.com | 3 | 0.07% | 0.16% |
| news_api | natalie.mu | 3 | 0.07% | 0.16% |
| news_api | newsway.co.kr | 3 | 0.07% | 0.16% |
| news_api | newswiretoday.com | 3 | 0.07% | 0.16% |
| news_api | nypost.com | 3 | 0.07% | 0.16% |
| news_api | nzherald.co.nz | 3 | 0.07% | 0.16% |
| news_api | odatv.com | 3 | 0.07% | 0.16% |
| news_api | politis.com.cy | 3 | 0.07% | 0.16% |
| news_api | portal.sina.com.hk | 3 | 0.07% | 0.16% |
| news_api | ria.ru | 3 | 0.07% | 0.16% |
| news_api | russian.rt.com | 3 | 0.07% | 0.16% |
| news_api | sabah.com.tr | 3 | 0.07% | 0.16% |
| news_api | scoop.co.nz | 3 | 0.07% | 0.16% |
| news_api | shorouknews.com | 3 | 0.07% | 0.16% |
| news_api | straitstimes.com | 3 | 0.07% | 0.16% |
| news_api | thenextweb.com | 3 | 0.07% | 0.16% |
| news_api | thesun.ng | 3 | 0.07% | 0.16% |
| news_api | tomshardware.com | 3 | 0.07% | 0.16% |
| news_api | tribuneindia.com | 3 | 0.07% | 0.16% |
| news_api | trthaber.com | 3 | 0.07% | 0.16% |
| news_api | ura.news | 3 | 0.07% | 0.16% |
| news_api | wbaltv.com | 3 | 0.07% | 0.16% |
| news_api | wesh.com | 3 | 0.07% | 0.16% |
| news_api | wired.com | 3 | 0.07% | 0.16% |
| news_api | wmur.com | 3 | 0.07% | 0.16% |
| news_api | womannews.net | 3 | 0.07% | 0.16% |
| news_api | 1prime.ru | 2 | 0.05% | 0.10% |
| news_api | abc.es | 2 | 0.05% | 0.10% |
| news_api | abovethelaw.com | 2 | 0.05% | 0.10% |
| news_api | aceshowbiz.com | 2 | 0.05% | 0.10% |
| news_api | allafrica.com | 2 | 0.05% | 0.10% |
| news_api | americanbanker.com | 2 | 0.05% | 0.10% |
| news_api | androidheadlines.com | 2 | 0.05% | 0.10% |
| news_api | aninews.in | 2 | 0.05% | 0.10% |
| news_api | antaranews.com | 2 | 0.05% | 0.10% |
| news_api | aol.co.uk | 2 | 0.05% | 0.10% |
| news_api | arkansasonline.com | 2 | 0.05% | 0.10% |
| news_api | arstechnica.com | 2 | 0.05% | 0.10% |
| news_api | bankingnews.gr | 2 | 0.05% | 0.10% |
| news_api | bd-pratidin.com | 2 | 0.05% | 0.10% |
| news_api | begeek.fr | 2 | 0.05% | 0.10% |
| news_api | bjnews.com.cn | 2 | 0.05% | 0.10% |
| news_api | bleepingcomputer.com | 2 | 0.05% | 0.10% |
| news_api | boerse-express.com | 2 | 0.05% | 0.10% |
| news_api | bunburymail.com.au | 2 | 0.05% | 0.10% |
| news_api | busan.com | 2 | 0.05% | 0.10% |
| news_api | business24.ro | 2 | 0.05% | 0.10% |
| news_api | businessday.co.za | 2 | 0.05% | 0.10% |
| news_api | businessghana.com | 2 | 0.05% | 0.10% |
| news_api | capital.ro | 2 | 0.05% | 0.10% |
| news_api | castanetkamloops.net | 2 | 0.05% | 0.10% |
| news_api | cloud.watch.impress.co.jp | 2 | 0.05% | 0.10% |
| news_api | comnews.ru | 2 | 0.05% | 0.10% |
| news_api | computerweekly.com | 2 | 0.05% | 0.10% |
| news_api | daily.com.ua | 2 | 0.05% | 0.10% |
| news_api | dailybreeze.com | 2 | 0.05% | 0.10% |
| news_api | dailyemerald.com | 2 | 0.05% | 0.10% |
| news_api | dailykos.com | 2 | 0.05% | 0.10% |
| news_api | dailynews.com | 2 | 0.05% | 0.10% |
| news_api | danas.rs | 2 | 0.05% | 0.10% |
| news_api | deadline.com | 2 | 0.05% | 0.10% |
| news_api | diariosur.es | 2 | 0.05% | 0.10% |
| news_api | digitaljournal.com | 2 | 0.05% | 0.10% |
| news_api | ecodibergamo.it | 2 | 0.05% | 0.10% |
| news_api | ecodisicilia.com | 2 | 0.05% | 0.10% |
| news_api | ecommercenews.co.nz | 2 | 0.05% | 0.10% |
| news_api | eldestapeweb.com | 2 | 0.05% | 0.10% |
| news_api | eldia.com.bo | 2 | 0.05% | 0.10% |
| news_api | eldiariodechihuahua.mx | 2 | 0.05% | 0.10% |
| news_api | elmanana.com | 2 | 0.05% | 0.10% |
| news_api | elsiglodetorreon.com.mx | 2 | 0.05% | 0.10% |
| news_api | etoday.co.kr | 2 | 0.05% | 0.10% |
| news_api | europesun.com | 2 | 0.05% | 0.10% |
| news_api | focus.ua | 2 | 0.05% | 0.10% |
| news_api | fontanka.ru | 2 | 0.05% | 0.10% |
| news_api | fox4news.com | 2 | 0.05% | 0.10% |
| news_api | freemalaysiatoday.com | 2 | 0.05% | 0.10% |
| news_api | gdnonline.com | 2 | 0.05% | 0.10% |
| news_api | geeky-gadgets.com | 2 | 0.05% | 0.10% |
| news_api | github.com | 2 | 0.05% | 0.10% |
| news_api | gizmodo.com | 2 | 0.05% | 0.10% |
| news_api | glavcom.ua | 2 | 0.05% | 0.10% |
| news_api | globalnews.ca | 2 | 0.05% | 0.10% |
| news_api | greeleytribune.com | 2 | 0.05% | 0.10% |
| news_api | haber1.com | 2 | 0.05% | 0.10% |
| news_api | hawaiitelegraph.com | 2 | 0.05% | 0.10% |
| news_api | heraldk.com | 2 | 0.05% | 0.10% |
| news_api | hindi.webdunia.com | 2 | 0.05% | 0.10% |
| news_api | hinews.cn | 2 | 0.05% | 0.10% |
| news_api | hollywoodreporter.com | 2 | 0.05% | 0.10% |
| news_api | htxt.co.za | 2 | 0.05% | 0.10% |
| news_api | hurriyetdailynews.com | 2 | 0.05% | 0.10% |
| news_api | index.hr | 2 | 0.05% | 0.10% |
| news_api | inews24.com | 2 | 0.05% | 0.10% |
| news_api | inewsgr.com | 2 | 0.05% | 0.10% |
| news_api | inforum.com | 2 | 0.05% | 0.10% |
| news_api | infoworld.com | 2 | 0.05% | 0.10% |
| news_api | insideottawavalley.com | 2 | 0.05% | 0.10% |
| news_api | insight.co.kr | 2 | 0.05% | 0.10% |
| news_api | insurancejournal.com | 2 | 0.05% | 0.10% |
| news_api | investegate.co.uk | 2 | 0.05% | 0.10% |
| news_api | irishdentist.ie | 2 | 0.05% | 0.10% |
| news_api | itwire.com | 2 | 0.05% | 0.10% |
| news_api | iz.ru | 2 | 0.05% | 0.10% |
| news_api | jawapos.com | 2 | 0.05% | 0.10% |
| news_api | jpost.com | 2 | 0.05% | 0.10% |
| news_api | jugantor.com | 2 | 0.05% | 0.10% |
| news_api | kathimerini.com.cy | 2 | 0.05% | 0.10% |
| news_api | kommersant.ru | 2 | 0.05% | 0.10% |
| news_api | kten.com | 2 | 0.05% | 0.10% |
| news_api | lalsace.fr | 2 | 0.05% | 0.10% |
| news_api | lbc.co.uk | 2 | 0.05% | 0.10% |
| news_api | lefigaro.fr | 2 | 0.05% | 0.10% |
| news_api | lelezard.com | 2 | 0.05% | 0.10% |
| news_api | lenta.ru | 2 | 0.05% | 0.10% |
| news_api | libnanews.com | 2 | 0.05% | 0.10% |
| news_api | life.ru | 2 | 0.05% | 0.10% |
| news_api | livenews.co.nz | 2 | 0.05% | 0.10% |
| news_api | lrytas.lt | 2 | 0.05% | 0.10% |
| news_api | macleayargus.com.au | 2 | 0.05% | 0.10% |
| news_api | mainichi.jp | 2 | 0.05% | 0.10% |
| news_api | makeuseof.com | 2 | 0.05% | 0.10% |
| news_api | massachusettssun.com | 2 | 0.05% | 0.10% |
| news_api | medianama.com | 2 | 0.05% | 0.10% |
| news_api | mersinhaber.com | 2 | 0.05% | 0.10% |
| news_api | military.china.com | 2 | 0.05% | 0.10% |
| news_api | morningstar.com | 2 | 0.05% | 0.10% |
| news_api | naftemporiki.gr | 2 | 0.05% | 0.10% |
| news_api | newkerala.com | 2 | 0.05% | 0.10% |
| news_api | newratings.de | 2 | 0.05% | 0.10% |
| news_api | news.cn | 2 | 0.05% | 0.10% |
| news_api | newspim.com | 2 | 0.05% | 0.10% |
| news_api | nikkan-gendai.com | 2 | 0.05% | 0.10% |
| news_api | nikkei.com | 2 | 0.05% | 0.10% |
| news_api | ntdtv.com | 2 | 0.05% | 0.10% |
| news_api | nvi.com.au | 2 | 0.05% | 0.10% |
| news_api | pcwplus.hu | 2 | 0.05% | 0.10% |
| news_api | phonandroid.com | 2 | 0.05% | 0.10% |
| news_api | politika.rs | 2 | 0.05% | 0.10% |
| news_api | posta.com.tr | 2 | 0.05% | 0.10% |
| news_api | pravda.ru | 2 | 0.05% | 0.10% |
| news_api | propakistani.pk | 2 | 0.05% | 0.10% |
| news_api | pv-magazine.com | 2 | 0.05% | 0.10% |
| news_api | pymnts.com | 2 | 0.05% | 0.10% |
| news_api | rediff.com | 2 | 0.05% | 0.10% |
| news_api | riasv.ru | 2 | 0.05% | 0.10% |
| news_api | rpp.pe | 2 | 0.05% | 0.10% |
| news_api | sanantoniopost.com | 2 | 0.05% | 0.10% |
| news_api | sb.by | 2 | 0.05% | 0.10% |
| news_api | securitybrief.news | 2 | 0.05% | 0.10% |
| news_api | securityinfowatch.com | 2 | 0.05% | 0.10% |
| news_api | segye.com | 2 | 0.05% | 0.10% |
| news_api | senego.com | 2 | 0.05% | 0.10% |
| news_api | sentinel.ht | 2 | 0.05% | 0.10% |
| news_api | sgvtribune.com | 2 | 0.05% | 0.10% |
| news_api | sozcu.com.tr | 2 | 0.05% | 0.10% |
| news_api | stcn.com | 2 | 0.05% | 0.10% |
| news_api | storm.mg | 2 | 0.05% | 0.10% |
| news_api | t-online.de | 2 | 0.05% | 0.10% |
| news_api | tech.caijing.com.cn | 2 | 0.05% | 0.10% |
| news_api | tech.ifeng.com | 2 | 0.05% | 0.10% |
| news_api | techweez.com | 2 | 0.05% | 0.10% |
| news_api | tennesseedaily.com | 2 | 0.05% | 0.10% |
| news_api | tgrthaber.com | 2 | 0.05% | 0.10% |
| news_api | thehindu.com | 2 | 0.05% | 0.10% |
| news_api | thisdaylive.com | 2 | 0.05% | 0.10% |
| news_api | tmtpost.com | 2 | 0.05% | 0.10% |
| news_api | uainfo.org | 2 | 0.05% | 0.10% |
| news_api | udn.com | 2 | 0.05% | 0.10% |
| news_api | unian.net | 2 | 0.05% | 0.10% |
| news_api | unn.ua | 2 | 0.05% | 0.10% |
| news_api | unternehmen-heute.de | 2 | 0.05% | 0.10% |
| news_api | vedomosti.ru | 2 | 0.05% | 0.10% |
| news_api | vesti.ru | 2 | 0.05% | 0.10% |
| news_api | vetogate.com | 2 | 0.05% | 0.10% |
| news_api | vg.no | 2 | 0.05% | 0.10% |
| news_api | vietnamnet.vn | 2 | 0.05% | 0.10% |
| news_api | wdrb.com | 2 | 0.05% | 0.10% |
| news_api | webpronews.com | 2 | 0.05% | 0.10% |
| news_api | welivesecurity.com | 2 | 0.05% | 0.10% |
| news_api | weser-kurier.de | 2 | 0.05% | 0.10% |
| news_api | wfmz.com | 2 | 0.05% | 0.10% |
| news_api | wiwo.de | 2 | 0.05% | 0.10% |
| news_api | wsbtv.com | 2 | 0.05% | 0.10% |
| news_api | wwmt.com | 2 | 0.05% | 0.10% |
| news_api | wzzm13.com | 2 | 0.05% | 0.10% |
| news_api | y-mainichi.co.jp | 2 | 0.05% | 0.10% |
| news_api | yorkregion.com | 2 | 0.05% | 0.10% |
| news_api | 01net.com | 1 | 0.02% | 0.05% |
| news_api | 1015vibe.com | 1 | 0.02% | 0.05% |
| news_api | 1055thedove.com | 1 | 0.02% | 0.05% |
| news_api | 10tv.com | 1 | 0.02% | 0.05% |
| news_api | 13abc.com | 1 | 0.02% | 0.05% |
| news_api | 21stcenturywire.com | 1 | 0.02% | 0.05% |
| news_api | 24sata.hr | 1 | 0.02% | 0.05% |
| news_api | 24tv.ua | 1 | 0.02% | 0.05% |
| news_api | 373news.com | 1 | 0.02% | 0.05% |
| news_api | 3c.ltn.com.tw | 1 | 0.02% | 0.05% |
| news_api | 5.ua | 1 | 0.02% | 0.05% |
| news_api | 5newsonline.com | 1 | 0.02% | 0.05% |
| news_api | 620ckrm.com | 1 | 0.02% | 0.05% |
| news_api | 961theeagle.com | 1 | 0.02% | 0.05% |
| news_api | 985thefox.iheart.com | 1 | 0.02% | 0.05% |
| news_api | 995thefox.iheart.com | 1 | 0.02% | 0.05% |
| news_api | 99jamzmiami.com | 1 | 0.02% | 0.05% |
| news_api | 9news.com.au | 1 | 0.02% | 0.05% |
| news_api | abc6onyourside.com | 1 | 0.02% | 0.05% |
| news_api | abc7news.com | 1 | 0.02% | 0.05% |
| news_api | abclinuxu.cz | 1 | 0.02% | 0.05% |
| news_api | actionnewsjax.com | 1 | 0.02% | 0.05% |
| news_api | adevarul.ro | 1 | 0.02% | 0.05% |
| news_api | administradores.com.br | 1 | 0.02% | 0.05% |
| news_api | afr.com | 1 | 0.02% | 0.05% |
| news_api | ahaber.com.tr | 1 | 0.02% | 0.05% |
| news_api | ai.zol.com.cn | 1 | 0.02% | 0.05% |
| news_api | aif.ru | 1 | 0.02% | 0.05% |
| news_api | aktifhaber.com | 1 | 0.02% | 0.05% |
| news_api | aktivni.metropolitan.si | 1 | 0.02% | 0.05% |
| news_api | al-monitor.com | 1 | 0.02% | 0.05% |
| news_api | alanbatnews.net | 1 | 0.02% | 0.05% |
| news_api | alaskasnewssource.com | 1 | 0.02% | 0.05% |
| news_api | albiladpress.com | 1 | 0.02% | 0.05% |
| news_api | aliran.com | 1 | 0.02% | 0.05% |
| news_api | aljazeera.com | 1 | 0.02% | 0.05% |
| news_api | aljazeera.net | 1 | 0.02% | 0.05% |
| news_api | alo.rs | 1 | 0.02% | 0.05% |
| news_api | alquds.co.uk | 1 | 0.02% | 0.05% |
| news_api | am1150.ca | 1 | 0.02% | 0.05% |
| news_api | amic.ru | 1 | 0.02% | 0.05% |
| news_api | anlatilaninotesi.com.tr | 1 | 0.02% | 0.05% |
| news_api | antena3.ro | 1 | 0.02% | 0.05% |
| news_api | antivirus-sniper.macupdate.com | 1 | 0.02% | 0.05% |
| news_api | arabherald.com | 1 | 0.02% | 0.05% |
| news_api | arede.info | 1 | 0.02% | 0.05% |
| news_api | aristeguinoticias.com | 1 | 0.02% | 0.05% |
| news_api | armenews.com | 1 | 0.02% | 0.05% |
| news_api | armidaleexpress.com.au | 1 | 0.02% | 0.05% |
| news_api | asahi.com | 1 | 0.02% | 0.05% |
| news_api | asianews.it | 1 | 0.02% | 0.05% |
| news_api | aspentimes.com | 1 | 0.02% | 0.05% |
| news_api | astroawani.com | 1 | 0.02% | 0.05% |
| news_api | austinchronicle.com | 1 | 0.02% | 0.05% |
| news_api | austinglobe.com | 1 | 0.02% | 0.05% |
| news_api | autoexpress.co.uk | 1 | 0.02% | 0.05% |
| news_api | avn.info.ve | 1 | 0.02% | 0.05% |
| news_api | b985.com | 1 | 0.02% | 0.05% |
| news_api | balkanweb.com | 1 | 0.02% | 0.05% |
| news_api | bamada.net | 1 | 0.02% | 0.05% |
| news_api | bandaancha.eu | 1 | 0.02% | 0.05% |
| news_api | bangkokbiznews.com | 1 | 0.02% | 0.05% |
| news_api | bangkokpost.com | 1 | 0.02% | 0.05% |
| news_api | bangordailynews.com | 1 | 0.02% | 0.05% |
| news_api | bankier.pl | 1 | 0.02% | 0.05% |
| news_api | batam.tribunnews.com | 1 | 0.02% | 0.05% |
| news_api | batemansbaypost.com.au | 1 | 0.02% | 0.05% |
| news_api | batonrougepost.com | 1 | 0.02% | 0.05% |
| news_api | bbc.com | 1 | 0.02% | 0.05% |
| news_api | beckershospitalreview.com | 1 | 0.02% | 0.05% |
| news_api | berliner-zeitung.de | 1 | 0.02% | 0.05% |
| news_api | bernerzeitung.ch | 1 | 0.02% | 0.05% |
| news_api | bfmtv.com | 1 | 0.02% | 0.05% |
| news_api | bgonair.bg | 1 | 0.02% | 0.05% |
| news_api | bgr.com | 1 | 0.02% | 0.05% |
| news_api | bhaskar.com | 1 | 0.02% | 0.05% |
| news_api | bianet.org | 1 | 0.02% | 0.05% |
| news_api | bignewsnetwork.com | 1 | 0.02% | 0.05% |
| news_api | bigpara.hurriyet.com.tr | 1 | 0.02% | 0.05% |
| news_api | birminghamstar.com | 1 | 0.02% | 0.05% |
| news_api | biz.cnews.ru | 1 | 0.02% | 0.05% |
| news_api | bj.xinhuanet.com | 1 | 0.02% | 0.05% |
| news_api | blackseanews.net | 1 | 0.02% | 0.05% |
| news_api | blikk.hu | 1 | 0.02% | 0.05% |
| news_api | blog.wenxuecity.com | 1 | 0.02% | 0.05% |
| news_api | blogs.diariovasco.com | 1 | 0.02% | 0.05% |
| news_api | blogs.itmedia.co.jp | 1 | 0.02% | 0.05% |
| news_api | bluemountainsgazette.com.au | 1 | 0.02% | 0.05% |
| news_api | blueprint.ng | 1 | 0.02% | 0.05% |
| news_api | bmmagazine.co.uk | 1 | 0.02% | 0.05% |
| news_api | bollywoodlife.com | 1 | 0.02% | 0.05% |
| news_api | borsonline.hu | 1 | 0.02% | 0.05% |
| news_api | bostonherald.com | 1 | 0.02% | 0.05% |
| news_api | botasot.info | 1 | 0.02% | 0.05% |
| news_api | bozemandailychronicle.com | 1 | 0.02% | 0.05% |
| news_api | braidwoodtimes.com.au | 1 | 0.02% | 0.05% |
| news_api | brandonsun.com | 1 | 0.02% | 0.05% |
| news_api | brasil247.com | 1 | 0.02% | 0.05% |
| news_api | breitbart.com | 1 | 0.02% | 0.05% |
| news_api | brisbanetimes.com.au | 1 | 0.02% | 0.05% |
| news_api | brooklyneagle.com | 1 | 0.02% | 0.05% |
| news_api | bt.no | 1 | 0.02% | 0.05% |
| news_api | buffalobulletin.com | 1 | 0.02% | 0.05% |
| news_api | bug.hr | 1 | 0.02% | 0.05% |
| news_api | burgundywave.com | 1 | 0.02% | 0.05% |
| news_api | bursahakimiyet.com.tr | 1 | 0.02% | 0.05% |
| news_api | business2community.com | 1 | 0.02% | 0.05% |
| news_api | businessinsurance.com | 1 | 0.02% | 0.05% |
| news_api | businesstimes.com.sg | 1 | 0.02% | 0.05% |
| news_api | businesstoday.in | 1 | 0.02% | 0.05% |
| news_api | businessworld.in | 1 | 0.02% | 0.05% |
| news_api | c101.iheart.com | 1 | 0.02% | 0.05% |
| news_api | cafebiz.vn | 1 | 0.02% | 0.05% |
| news_api | californiatelegraph.com | 1 | 0.02% | 0.05% |
| news_api | cambridgetimes.ca | 1 | 0.02% | 0.05% |
| news_api | camdencourier.com.au | 1 | 0.02% | 0.05% |
| news_api | canardpc.com | 1 | 0.02% | 0.05% |
| news_api | carolinajournal.com | 1 | 0.02% | 0.05% |
| news_api | cas.sk | 1 | 0.02% | 0.05% |
| news_api | cbs2iowa.com | 1 | 0.02% | 0.05% |
| news_api | cbs6albany.com | 1 | 0.02% | 0.05% |
| news_api | cepro.com | 1 | 0.02% | 0.05% |
| news_api | cfi.net.cn | 1 | 0.02% | 0.05% |
| news_api | channelbuzz.ca | 1 | 0.02% | 0.05% |
| news_api | chattanoogan.com | 1 | 0.02% | 0.05% |
| news_api | china.com.cn | 1 | 0.02% | 0.05% |
| news_api | chinanationalnews.com | 1 | 0.02% | 0.05% |
| news_api | chinapress.com.my | 1 | 0.02% | 0.05% |
| news_api | chinesepress.com | 1 | 0.02% | 0.05% |
| news_api | chip.de | 1 | 0.02% | 0.05% |
| news_api | choice.com.au | 1 | 0.02% | 0.05% |
| news_api | cincinnatisun.com | 1 | 0.02% | 0.05% |
| news_api | circleid.com | 1 | 0.02% | 0.05% |
| news_api | citylimits.org | 1 | 0.02% | 0.05% |
| news_api | ciudadccs.info | 1 | 0.02% | 0.05% |
| news_api | cjme.com | 1 | 0.02% | 0.05% |
| news_api | clactonandfrintongazette.co.uk | 1 | 0.02% | 0.05% |
| news_api | clarin.com | 1 | 0.02% | 0.05% |
| news_api | closermag.fr | 1 | 0.02% | 0.05% |
| news_api | clydebankpost.co.uk | 1 | 0.02% | 0.05% |
| news_api | cnet.com | 1 | 0.02% | 0.05% |
| news_api | cnn.com | 1 | 0.02% | 0.05% |
| news_api | cnycentral.com | 1 | 0.02% | 0.05% |
| news_api | coloradostar.com | 1 | 0.02% | 0.05% |
| news_api | comingsoon.it | 1 | 0.02% | 0.05% |
| news_api | computerwoche.de | 1 | 0.02% | 0.05% |
| news_api | computerworld.dk | 1 | 0.02% | 0.05% |
| news_api | computerworld.pl | 1 | 0.02% | 0.05% |
| news_api | contractormag.com | 1 | 0.02% | 0.05% |
| news_api | cootamundraherald.com.au | 1 | 0.02% | 0.05% |
| news_api | cope.es | 1 | 0.02% | 0.05% |
| news_api | corp.cnews.ru | 1 | 0.02% | 0.05% |
| news_api | corriereadriatico.it | 1 | 0.02% | 0.05% |
| news_api | countercurrents.org | 1 | 0.02% | 0.05% |
| news_api | cp24.com | 1 | 0.02% | 0.05% |
| news_api | crestonnews.com | 1 | 0.02% | 0.05% |
| news_api | crookwellgazette.com.au | 1 | 0.02% | 0.05% |
| news_api | dagensps.se | 1 | 0.02% | 0.05% |
| news_api | daily-tribune.com | 1 | 0.02% | 0.05% |
| news_api | dailyadvertiser.com.au | 1 | 0.02% | 0.05% |
| news_api | dailybulletin.com | 1 | 0.02% | 0.05% |
| news_api | dailyexcelsior.com | 1 | 0.02% | 0.05% |
| news_api | dailyinqilab.com | 1 | 0.02% | 0.05% |
| news_api | dailyjournalonline.com | 1 | 0.02% | 0.05% |
| news_api | dailymail.co.uk | 1 | 0.02% | 0.05% |
| news_api | dailymail.com | 1 | 0.02% | 0.05% |
| news_api | dailynews.co.th | 1 | 0.02% | 0.05% |
| news_api | dailypakistan.pk | 1 | 0.02% | 0.05% |
| news_api | dailypioneer.com | 1 | 0.02% | 0.05% |
| news_api | dailypolitical.com | 1 | 0.02% | 0.05% |
| news_api | dailypost.ng | 1 | 0.02% | 0.05% |
| news_api | dailysabah.com | 1 | 0.02% | 0.05% |
| news_api | dailytrust.com | 1 | 0.02% | 0.05% |
| news_api | dailyuw.com | 1 | 0.02% | 0.05% |
| news_api | dakotawarcollege.com | 1 | 0.02% | 0.05% |
| news_api | damernasvarld.expressen.se | 1 | 0.02% | 0.05% |
| news_api | dantri.com.vn | 1 | 0.02% | 0.05% |
| news_api | datacenterknowledge.com | 1 | 0.02% | 0.05% |
| news_api | daytondailynews.com | 1 | 0.02% | 0.05% |
| news_api | dcvelocity.com | 1 | 0.02% | 0.05% |
| news_api | de.nachrichten.yahoo.com | 1 | 0.02% | 0.05% |
| news_api | denizlihaber.com | 1 | 0.02% | 0.05% |
| news_api | deperu.com | 1 | 0.02% | 0.05% |
| news_api | designboom.com | 1 | 0.02% | 0.05% |
| news_api | dglobe.com | 1 | 0.02% | 0.05% |
| news_api | dha.com.tr | 1 | 0.02% | 0.05% |
| news_api | diario.mx | 1 | 0.02% | 0.05% |
| news_api | diariodeburgos.es | 1 | 0.02% | 0.05% |
| news_api | diariodemorelos.com | 1 | 0.02% | 0.05% |
| news_api | diarioelargentino.com | 1 | 0.02% | 0.05% |
| news_api | diariopalentino.es | 1 | 0.02% | 0.05% |
| news_api | diariosigloxxi.com | 1 | 0.02% | 0.05% |
| news_api | diena.lt | 1 | 0.02% | 0.05% |
| news_api | digg.com | 1 | 0.02% | 0.05% |
| news_api | digi.china.com | 1 | 0.02% | 0.05% |
| news_api | digi24.ro | 1 | 0.02% | 0.05% |
| news_api | digitaltrends.com | 1 | 0.02% | 0.05% |
| news_api | directionsmag.com | 1 | 0.02% | 0.05% |
| news_api | divyamarathi.bhaskar.com | 1 | 0.02% | 0.05% |
| news_api | diyarbakirsoz.com | 1 | 0.02% | 0.05% |
| news_api | dna.fr | 1 | 0.02% | 0.05% |
| news_api | dnews.gr | 1 | 0.02% | 0.05% |
| news_api | dol.com.br | 1 | 0.02% | 0.05% |
| news_api | dominicanrepublicpost.com | 1 | 0.02% | 0.05% |
| news_api | donanimhaber.com | 1 | 0.02% | 0.05% |
| news_api | donews.com | 1 | 0.02% | 0.05% |
| news_api | dotekomanie.cz | 1 | 0.02% | 0.05% |
| news_api | downtoearth.org.in | 1 | 0.02% | 0.05% |
| news_api | dp.ru | 1 | 0.02% | 0.05% |
| news_api | drimble.nl | 1 | 0.02% | 0.05% |
| news_api | dunya.com | 1 | 0.02% | 0.05% |
| news_api | dunyanews.tv | 1 | 0.02% | 0.05% |
| news_api | dw.com | 1 | 0.02% | 0.05% |
| news_api | dynamicbusiness.com | 1 | 0.02% | 0.05% |
| news_api | eadt.co.uk | 1 | 0.02% | 0.05% |
| news_api | eagledayton.com | 1 | 0.02% | 0.05% |
| news_api | eaglesanantonio.com | 1 | 0.02% | 0.05% |
| news_api | ec.ltn.com.tw | 1 | 0.02% | 0.05% |
| news_api | echopress.com | 1 | 0.02% | 0.05% |
| news_api | economx.hu | 1 | 0.02% | 0.05% |
| news_api | econotimes.com | 1 | 0.02% | 0.05% |
| news_api | edition.cnn.com | 1 | 0.02% | 0.05% |
| news_api | eejournal.com | 1 | 0.02% | 0.05% |
| news_api | eenadu.net | 1 | 0.02% | 0.05% |
| news_api | elcomercio.es | 1 | 0.02% | 0.05% |
| news_api | elconfidencial.com | 1 | 0.02% | 0.05% |
| news_api | elcorreo.com | 1 | 0.02% | 0.05% |
| news_api | eldia.es | 1 | 0.02% | 0.05% |
| news_api | eleco.com.ar | 1 | 0.02% | 0.05% |
| news_api | elektroniknet.de | 1 | 0.02% | 0.05% |
| news_api | elmalaeb.com | 1 | 0.02% | 0.05% |
| news_api | elmundo.es | 1 | 0.02% | 0.05% |
| news_api | elpais.com | 1 | 0.02% | 0.05% |
| news_api | elpais.com.uy | 1 | 0.02% | 0.05% |
| news_api | elperiodicodearagon.com | 1 | 0.02% | 0.05% |
| news_api | elpuntavui.cat | 1 | 0.02% | 0.05% |
| news_api | eluniversal.com.mx | 1 | 0.02% | 0.05% |
| news_api | eluniverso.com | 1 | 0.02% | 0.05% |
| news_api | elwatannews.com | 1 | 0.02% | 0.05% |
| news_api | eng.kavkaz-uzel.eu | 1 | 0.02% | 0.05% |
| news_api | english.pravda.ru | 1 | 0.02% | 0.05% |
| news_api | estadao.com.br | 1 | 0.02% | 0.05% |
| news_api | etnews.com | 1 | 0.02% | 0.05% |
| news_api | ettoday.net | 1 | 0.02% | 0.05% |
| news_api | explosion.com | 1 | 0.02% | 0.05% |
| news_api | express.pk | 1 | 0.02% | 0.05% |
| news_api | extra.ec | 1 | 0.02% | 0.05% |
| news_api | f1vilag.hu | 1 | 0.02% | 0.05% |
| news_api | fakti.bg | 1 | 0.02% | 0.05% |
| news_api | fansided.com | 1 | 0.02% | 0.05% |
| news_api | fatimanews.com.br | 1 | 0.02% | 0.05% |
| news_api | fedpress.ru | 1 | 0.02% | 0.05% |
| news_api | femina.hu | 1 | 0.02% | 0.05% |
| news_api | filmfare.com | 1 | 0.02% | 0.05% |
| news_api | finance.ifeng.com | 1 | 0.02% | 0.05% |
| news_api | financial-news.co.uk | 1 | 0.02% | 0.05% |
| news_api | financialafrik.com | 1 | 0.02% | 0.05% |
| news_api | finans.mynet.com | 1 | 0.02% | 0.05% |
| news_api | firstpost.com | 1 | 0.02% | 0.05% |
| news_api | floridastatesman.com | 1 | 0.02% | 0.05% |
| news_api | fnp.de | 1 | 0.02% | 0.05% |
| news_api | fool.ca | 1 | 0.02% | 0.05% |
| news_api | fox17online.com | 1 | 0.02% | 0.05% |
| news_api | fox43.com | 1 | 0.02% | 0.05% |
| news_api | fox9.com | 1 | 0.02% | 0.05% |
| news_api | francetoday.com | 1 | 0.02% | 0.05% |
| news_api | freiepresse.de | 1 | 0.02% | 0.05% |
| news_api | french.china.org.cn | 1 | 0.02% | 0.05% |
| news_api | funkytaurusmedia.com | 1 | 0.02% | 0.05% |
| news_api | futures.cnfol.com | 1 | 0.02% | 0.05% |
| news_api | gadgetsmagazine.com.ph | 1 | 0.02% | 0.05% |
| news_api | gamerant.com | 1 | 0.02% | 0.05% |
| news_api | gamestar.de | 1 | 0.02% | 0.05% |
| news_api | generation-nt.com | 1 | 0.02% | 0.05% |
| news_api | georgeherald.com | 1 | 0.02% | 0.05% |
| news_api | german.china.org.cn | 1 | 0.02% | 0.05% |
| news_api | ghanaiantimes.com.gh | 1 | 0.02% | 0.05% |
| news_api | gipedo.politis.com.cy | 1 | 0.02% | 0.05% |
| news_api | golosarmenii.am | 1 | 0.02% | 0.05% |
| news_api | gorod48.ru | 1 | 0.02% | 0.05% |
| news_api | governing.com | 1 | 0.02% | 0.05% |
| news_api | greekherald.com | 1 | 0.02% | 0.05% |
| news_api | groundup.org.za | 1 | 0.02% | 0.05% |
| news_api | guelphmercury.com | 1 | 0.02% | 0.05% |
| news_api | gulte.com | 1 | 0.02% | 0.05% |
| news_api | gx94radio.com | 1 | 0.02% | 0.05% |
| news_api | haber3.com | 1 | 0.02% | 0.05% |
| news_api | haber7.com | 1 | 0.02% | 0.05% |
| news_api | haberturk.com | 1 | 0.02% | 0.05% |
| news_api | haberyazar.com | 1 | 0.02% | 0.05% |
| news_api | hachettebookgroup.com | 1 | 0.02% | 0.05% |
| news_api | hackaday.com | 1 | 0.02% | 0.05% |
| news_api | haksozhaber.net | 1 | 0.02% | 0.05% |
| news_api | hanasone.mainichi.jp | 1 | 0.02% | 0.05% |
| news_api | handelsblatt.com | 1 | 0.02% | 0.05% |
| news_api | hani.co.kr | 1 | 0.02% | 0.05% |
| news_api | hawaiinewsnow.com | 1 | 0.02% | 0.05% |
| news_api | hbook.com | 1 | 0.02% | 0.05% |
| news_api | healthcareitnews.com | 1 | 0.02% | 0.05% |
| news_api | helpconsumatori.it | 1 | 0.02% | 0.05% |
| news_api | hespress.com | 1 | 0.02% | 0.05% |
| news_api | heute.at | 1 | 0.02% | 0.05% |
| news_api | hirek.prim.hu | 1 | 0.02% | 0.05% |
| news_api | hits1053sanantonio.com | 1 | 0.02% | 0.05% |
| news_api | hits973.com | 1 | 0.02% | 0.05% |
| news_api | hokkoku.co.jp | 1 | 0.02% | 0.05% |
| news_api | hometownstation.com | 1 | 0.02% | 0.05% |
| news_api | howtogeek.com | 1 | 0.02% | 0.05% |
| news_api | hoy.es | 1 | 0.02% | 0.05% |
| news_api | hydrocarbonprocessing.com | 1 | 0.02% | 0.05% |
| news_api | ibtimes.co.uk | 1 | 0.02% | 0.05% |
| news_api | ibtimes.com.au | 1 | 0.02% | 0.05% |
| news_api | ici.fr | 1 | 0.02% | 0.05% |
| news_api | icij.org | 1 | 0.02% | 0.05% |
| news_api | idiva.com | 1 | 0.02% | 0.05% |
| news_api | idnes.cz | 1 | 0.02% | 0.05% |
| news_api | idrw.org | 1 | 0.02% | 0.05% |
| news_api | igamingbusiness.com | 1 | 0.02% | 0.05% |
| news_api | ihalla.com | 1 | 0.02% | 0.05% |
| news_api | illawarramercury.com.au | 1 | 0.02% | 0.05% |
| news_api | independent.co.uk | 1 | 0.02% | 0.05% |
| news_api | index.hu | 1 | 0.02% | 0.05% |
| news_api | india.com | 1 | 0.02% | 0.05% |
| news_api | indiagazette.com | 1 | 0.02% | 0.05% |
| news_api | indiatvnews.com | 1 | 0.02% | 0.05% |
| news_api | infobae.com | 1 | 0.02% | 0.05% |
| news_api | informationweek.com | 1 | 0.02% | 0.05% |
| news_api | infotechlead.com | 1 | 0.02% | 0.05% |
| news_api | inosmi.ru | 1 | 0.02% | 0.05% |
| news_api | inquirer.com | 1 | 0.02% | 0.05% |
| news_api | insidephilanthropy.com | 1 | 0.02% | 0.05% |
| news_api | insidermonkey.com | 1 | 0.02% | 0.05% |
| news_api | insight.scmagazineuk.com | 1 | 0.02% | 0.05% |
| news_api | interaksyon.philstar.com | 1 | 0.02% | 0.05% |
| news_api | internasional.kompas.com | 1 | 0.02% | 0.05% |
| news_api | internetua.com | 1 | 0.02% | 0.05% |
| news_api | inverelltimes.com.au | 1 | 0.02% | 0.05% |
| news_api | investorplace.com | 1 | 0.02% | 0.05% |
| news_api | inwestycje.pl | 1 | 0.02% | 0.05% |
| news_api | iraqsun.com | 1 | 0.02% | 0.05% |
| news_api | irishsun.com | 1 | 0.02% | 0.05% |
| news_api | irishtimes.com | 1 | 0.02% | 0.05% |
| news_api | island.lk | 1 | 0.02% | 0.05% |
| news_api | israelherald.com | 1 | 0.02% | 0.05% |
| news_api | it.euronews.com | 1 | 0.02% | 0.05% |
| news_api | itbrief.news | 1 | 0.02% | 0.05% |
| news_api | itnewsafrica.com | 1 | 0.02% | 0.05% |
| news_api | j-cast.com | 1 | 0.02% | 0.05% |
| news_api | jabar.tribunnews.com | 1 | 0.02% | 0.05% |
| news_api | jagranjosh.com | 1 | 0.02% | 0.05% |
| news_api | jamaicaobserver.com | 1 | 0.02% | 0.05% |
| news_api | jamestown.org | 1 | 0.02% | 0.05% |
| news_api | japan.cnet.com | 1 | 0.02% | 0.05% |
| news_api | japanherald.com | 1 | 0.02% | 0.05% |
| news_api | jc.uol.com.br | 1 | 0.02% | 0.05% |
| news_api | jeuneafrique.com | 1 | 0.02% | 0.05% |
| news_api | jiji.com | 1 | 0.02% | 0.05% |
| news_api | jo24.net | 1 | 0.02% | 0.05% |
| news_api | jogja.tribunnews.com | 1 | 0.02% | 0.05% |
| news_api | jogjapolitan.harianjogja.com | 1 | 0.02% | 0.05% |
| news_api | journal-news.com | 1 | 0.02% | 0.05% |
| news_api | journaldunet.com | 1 | 0.02% | 0.05% |
| news_api | journalgazette.net | 1 | 0.02% | 0.05% |
| news_api | jowhar.com | 1 | 0.02% | 0.05% |
| news_api | jpnn.com | 1 | 0.02% | 0.05% |
| news_api | juneesoutherncross.com.au | 1 | 0.02% | 0.05% |
| news_api | k991fm.com | 1 | 0.02% | 0.05% |
| news_api | kannadaprabha.com | 1 | 0.02% | 0.05% |
| news_api | kaos911.com | 1 | 0.02% | 0.05% |
| news_api | katu.com | 1 | 0.02% | 0.05% |
| news_api | kazokuchannel.doorblog.jp | 1 | 0.02% | 0.05% |
| news_api | kcci.com | 1 | 0.02% | 0.05% |
| news_api | kesq.com | 1 | 0.02% | 0.05% |
| news_api | king5.com | 1 | 0.02% | 0.05% |
| news_api | kingfm.com | 1 | 0.02% | 0.05% |
| news_api | kiplinger.com | 1 | 0.02% | 0.05% |
| news_api | kiro7.com | 1 | 0.02% | 0.05% |
| news_api | kissrocks.com | 1 | 0.02% | 0.05% |
| news_api | kjzz.org | 1 | 0.02% | 0.05% |
| news_api | kmbc.com | 1 | 0.02% | 0.05% |
| news_api | ko.com.ua | 1 | 0.02% | 0.05% |
| news_api | kob.com | 1 | 0.02% | 0.05% |
| news_api | kocaeligazetesi.com.tr | 1 | 0.02% | 0.05% |
| news_api | koco.com | 1 | 0.02% | 0.05% |
| news_api | kono1011.com | 1 | 0.02% | 0.05% |
| news_api | kontrakty.ua | 1 | 0.02% | 0.05% |
| news_api | koreatimes.co.kr | 1 | 0.02% | 0.05% |
| news_api | koreatimes.com | 1 | 0.02% | 0.05% |
| news_api | kotaku.com | 1 | 0.02% | 0.05% |
| news_api | kristv.com | 1 | 0.02% | 0.05% |
| news_api | ktvl.com | 1 | 0.02% | 0.05% |
| news_api | ktvu.com | 1 | 0.02% | 0.05% |
| news_api | kwcdcountry.com | 1 | 0.02% | 0.05% |
| news_api | kztv10.com | 1 | 0.02% | 0.05% |
| news_api | labs.watchtowr.com | 1 | 0.02% | 0.05% |
| news_api | lafranceagricole.fr | 1 | 0.02% | 0.05% |
| news_api | lagacetadesalamanca.es | 1 | 0.02% | 0.05% |
| news_api | lakersnation.com | 1 | 0.02% | 0.05% |
| news_api | laleggepertutti.it | 1 | 0.02% | 0.05% |
| news_api | laosnews.net | 1 | 0.02% | 0.05% |
| news_api | laprovincia.es | 1 | 0.02% | 0.05% |
| news_api | larazon.es | 1 | 0.02% | 0.05% |
| news_api | larepublica.pe | 1 | 0.02% | 0.05% |
| news_api | larepubliquedespyrenees.fr | 1 | 0.02% | 0.05% |
| news_api | latele.ch | 1 | 0.02% | 0.05% |
| news_api | latimes.com | 1 | 0.02% | 0.05% |
| news_api | laut.de | 1 | 0.02% | 0.05% |
| news_api | lavozdegalicia.es | 1 | 0.02% | 0.05% |
| news_api | lb.ua | 1 | 0.02% | 0.05% |
| news_api | ledauphine.com | 1 | 0.02% | 0.05% |
| news_api | legalinsurrection.com | 1 | 0.02% | 0.05% |
| news_api | leiphone.com | 1 | 0.02% | 0.05% |
| news_api | lejsl.com | 1 | 0.02% | 0.05% |
| news_api | lematin.ma | 1 | 0.02% | 0.05% |
| news_api | lesmobiles.com | 1 | 0.02% | 0.05% |
| news_api | lexpress.fr | 1 | 0.02% | 0.05% |
| news_api | lgz.ru | 1 | 0.02% | 0.05% |
| news_api | liberta.it | 1 | 0.02% | 0.05% |
| news_api | ligaportal.at | 1 | 0.02% | 0.05% |
| news_api | lina.sh | 1 | 0.02% | 0.05% |
| news_api | linux.org.ru | 1 | 0.02% | 0.05% |
| news_api | liputan6.com | 1 | 0.02% | 0.05% |
| news_api | lite987.com | 1 | 0.02% | 0.05% |
| news_api | lithgowmercury.com.au | 1 | 0.02% | 0.05% |
| news_api | livehindustan.com | 1 | 0.02% | 0.05% |
| news_api | livemint.com | 1 | 0.02% | 0.05% |
| news_api | local12.com | 1 | 0.02% | 0.05% |
| news_api | localnews8.com | 1 | 0.02% | 0.05% |
| news_api | loksatta.com | 1 | 0.02% | 0.05% |
| news_api | londonlovesbusiness.com | 1 | 0.02% | 0.05% |
| news_api | londonmercury.com | 1 | 0.02% | 0.05% |
| news_api | ly.fjsen.com | 1 | 0.02% | 0.05% |
| news_api | mactech.com | 1 | 0.02% | 0.05% |
| news_api | magic1021.com | 1 | 0.02% | 0.05% |
| news_api | maharashtratimes.com | 1 | 0.02% | 0.05% |
| news_api | makaangola.org | 1 | 0.02% | 0.05% |
| news_api | makassar.tribunnews.com | 1 | 0.02% | 0.05% |
| news_api | maldonandburnhamstandard.co.uk | 1 | 0.02% | 0.05% |
| news_api | mandurahmail.com.au | 1 | 0.02% | 0.05% |
| news_api | manningrivertimes.com.au | 1 | 0.02% | 0.05% |
| news_api | marca.com | 1 | 0.02% | 0.05% |
| news_api | mariettatimes.com | 1 | 0.02% | 0.05% |
| news_api | marketintelligencecenter.com | 1 | 0.02% | 0.05% |
| news_api | mashable.com | 1 | 0.02% | 0.05% |
| news_api | mathrubhumi.com | 1 | 0.02% | 0.05% |
| news_api | mdjonline.com | 1 | 0.02% | 0.05% |
| news_api | mebpersonel.com | 1 | 0.02% | 0.05% |
| news_api | megamodo.com | 1 | 0.02% | 0.05% |
| news_api | memeburn.com | 1 | 0.02% | 0.05% |
| news_api | mensxp.com | 1 | 0.02% | 0.05% |
| news_api | meridiano.net | 1 | 0.02% | 0.05% |
| news_api | merkur.de | 1 | 0.02% | 0.05% |
| news_api | metronews.ru | 1 | 0.02% | 0.05% |
| news_api | metroseoul.co.kr | 1 | 0.02% | 0.05% |
| news_api | michigandaily.com | 1 | 0.02% | 0.05% |
| news_api | midmichigannow.com | 1 | 0.02% | 0.05% |
| news_api | mirrorspectator.com | 1 | 0.02% | 0.05% |
| news_api | mississauga.com | 1 | 0.02% | 0.05% |
| news_api | mittelstandcafe.de | 1 | 0.02% | 0.05% |
| news_api | mix941kmxj.com | 1 | 0.02% | 0.05% |
| news_api | mk.ru | 1 | 0.02% | 0.05% |
| news_api | mngz.ru | 1 | 0.02% | 0.05% |
| news_api | mobile.zol.com.cn | 1 | 0.02% | 0.05% |
| news_api | mobileidworld.com | 1 | 0.02% | 0.05% |
| news_api | mochimag.com | 1 | 0.02% | 0.05% |
| news_api | money.it | 1 | 0.02% | 0.05% |
| news_api | monocle.com | 1 | 0.02% | 0.05% |
| news_api | montereyherald.com | 1 | 0.02% | 0.05% |
| news_api | mp.cnfol.com | 1 | 0.02% | 0.05% |
| news_api | mpacorn.com | 1 | 0.02% | 0.05% |
| news_api | mskagency.ru | 1 | 0.02% | 0.05% |
| news_api | mudgeeguardian.com.au | 1 | 0.02% | 0.05% |
| news_api | mundiario.com | 1 | 0.02% | 0.05% |
| news_api | mundoenlinea.cl | 1 | 0.02% | 0.05% |
| news_api | myanmarnews.net | 1 | 0.02% | 0.05% |
| news_api | mymagic949.com | 1 | 0.02% | 0.05% |
| news_api | mynews4.com | 1 | 0.02% | 0.05% |
| news_api | n-tv.de | 1 | 0.02% | 0.05% |
| news_api | nagpurtoday.in | 1 | 0.02% | 0.05% |
| news_api | nashvilleherald.com | 1 | 0.02% | 0.05% |
| news_api | nationalmortgagenews.com | 1 | 0.02% | 0.05% |
| news_api | navbharattimes.indiatimes.com | 1 | 0.02% | 0.05% |
| news_api | navhindtimes.in | 1 | 0.02% | 0.05% |
| news_api | nbcmontana.com | 1 | 0.02% | 0.05% |
| news_api | nbcwashington.com | 1 | 0.02% | 0.05% |
| news_api | nbd.com.cn | 1 | 0.02% | 0.05% |
| news_api | nearshoreamericas.com | 1 | 0.02% | 0.05% |
| news_api | net.hr | 1 | 0.02% | 0.05% |
| news_api | netzwelt.de | 1 | 0.02% | 0.05% |
| news_api | newcastleherald.com.au | 1 | 0.02% | 0.05% |
| news_api | neworleanssun.com | 1 | 0.02% | 0.05% |
| news_api | newrepublic.com | 1 | 0.02% | 0.05% |
| news_api | news.china.com.cn | 1 | 0.02% | 0.05% |
| news_api | news.cnfol.com | 1 | 0.02% | 0.05% |
| news_api | news.cts.com.tw | 1 | 0.02% | 0.05% |
| news_api | news.ltn.com.tw | 1 | 0.02% | 0.05% |
| news_api | news.mail.ru | 1 | 0.02% | 0.05% |
| news_api | news.tuoitre.vn | 1 | 0.02% | 0.05% |
| news_api | news.ycwb.com | 1 | 0.02% | 0.05% |
| news_api | news3lv.com | 1 | 0.02% | 0.05% |
| news_api | news8000.com | 1 | 0.02% | 0.05% |
| news_api | newsbomb.gr | 1 | 0.02% | 0.05% |
| news_api | newsit.gr | 1 | 0.02% | 0.05% |
| news_api | newsitaliane.it | 1 | 0.02% | 0.05% |
| news_api | newsminer.com | 1 | 0.02% | 0.05% |
| news_api | newsnet5.com | 1 | 0.02% | 0.05% |
| news_api | newsprom.ru | 1 | 0.02% | 0.05% |
| news_api | newstribune.com | 1 | 0.02% | 0.05% |
| news_api | newsweek.com | 1 | 0.02% | 0.05% |
| news_api | newsx.com | 1 | 0.02% | 0.05% |
| news_api | newtalk.tw | 1 | 0.02% | 0.05% |
| news_api | newyorkstatesman.com | 1 | 0.02% | 0.05% |
| news_api | niagarathisweek.com | 1 | 0.02% | 0.05% |
| news_api | nieuws.nl | 1 | 0.02% | 0.05% |
| news_api | niezalezna.pl | 1 | 0.02% | 0.05% |
| news_api | nigerianobservernews.com | 1 | 0.02% | 0.05% |
| news_api | nikkan.co.jp | 1 | 0.02% | 0.05% |
| news_api | nile.eg | 1 | 0.02% | 0.05% |
| news_api | nin.rs | 1 | 0.02% | 0.05% |
| news_api | ninersnation.com | 1 | 0.02% | 0.05% |
| news_api | nj.com | 1 | 0.02% | 0.05% |
| news_api | norran.se | 1 | 0.02% | 0.05% |
| news_api | northcountrynow.com | 1 | 0.02% | 0.05% |
| news_api | northerndailyleader.com.au | 1 | 0.02% | 0.05% |
| news_api | northweststar.com.au | 1 | 0.02% | 0.05% |
| news_api | notimerica.com | 1 | 0.02% | 0.05% |
| news_api | noviny.sk | 1 | 0.02% | 0.05% |
| news_api | nrc.nl | 1 | 0.02% | 0.05% |
| news_api | ntv.com.tr | 1 | 0.02% | 0.05% |
| news_api | nuevodiarioweb.com.ar | 1 | 0.02% | 0.05% |
| news_api | nwaonline.com | 1 | 0.02% | 0.05% |
| news_api | objectiv.tv | 1 | 0.02% | 0.05% |
| news_api | ocregister.com | 1 | 0.02% | 0.05% |
| news_api | ohiostandard.com | 1 | 0.02% | 0.05% |
| news_api | ohmynews.com | 1 | 0.02% | 0.05% |
| news_api | oklahomastar.com | 1 | 0.02% | 0.05% |
| news_api | ondacero.es | 1 | 0.02% | 0.05% |
| news_api | op-online.de | 1 | 0.02% | 0.05% |
| news_api | openpr.com | 1 | 0.02% | 0.05% |
| news_api | ostro.org | 1 | 0.02% | 0.05% |
| news_api | ottawacitizen.com | 1 | 0.02% | 0.05% |
| news_api | pakistantelegraph.com | 1 | 0.02% | 0.05% |
| news_api | panorama.com.al | 1 | 0.02% | 0.05% |
| news_api | pastemagazine.com | 1 | 0.02% | 0.05% |
| news_api | paymentweek.com | 1 | 0.02% | 0.05% |
| news_api | pcchip.hr | 1 | 0.02% | 0.05% |
| news_api | pctechmag.com | 1 | 0.02% | 0.05% |
| news_api | photo.china.com.cn | 1 | 0.02% | 0.05% |
| news_api | pitchfork.com | 1 | 0.02% | 0.05% |
| news_api | piter.tv | 1 | 0.02% | 0.05% |
| news_api | pjmedia.com | 1 | 0.02% | 0.05% |
| news_api | placenorthwest.co.uk | 1 | 0.02% | 0.05% |
| news_api | playground.ru | 1 | 0.02% | 0.05% |
| news_api | pleinevie.fr | 1 | 0.02% | 0.05% |
| news_api | pln-pskov.ru | 1 | 0.02% | 0.05% |
| news_api | podrobnosti.ua | 1 | 0.02% | 0.05% |
| news_api | polygon.com | 1 | 0.02% | 0.05% |
| news_api | pontianak.tribunnews.com | 1 | 0.02% | 0.05% |
| news_api | portalsamorzadowy.pl | 1 | 0.02% | 0.05% |
| news_api | portnews.com.au | 1 | 0.02% | 0.05% |
| news_api | postandcourier.com | 1 | 0.02% | 0.05% |
| news_api | posttoday.com | 1 | 0.02% | 0.05% |
| news_api | powerorlando.com | 1 | 0.02% | 0.05% |
| news_api | pr.com | 1 | 0.02% | 0.05% |
| news_api | prensalibre.com | 1 | 0.02% | 0.05% |
| news_api | press24.mk | 1 | 0.02% | 0.05% |
| news_api | pressdemocrat.com | 1 | 0.02% | 0.05% |
| news_api | presse-citron.net | 1 | 0.02% | 0.05% |
| news_api | presstelegram.com | 1 | 0.02% | 0.05% |
| news_api | presstv.ir | 1 | 0.02% | 0.05% |
| news_api | primerafuente.com.ar | 1 | 0.02% | 0.05% |
| news_api | profitline.hu | 1 | 0.02% | 0.05% |
| news_api | publico.pt | 1 | 0.02% | 0.05% |
| news_api | punjabitribuneonline.com | 1 | 0.02% | 0.05% |
| news_api | q947fm.iheart.com | 1 | 0.02% | 0.05% |
| news_api | quadratin.com.mx | 1 | 0.02% | 0.05% |
| news_api | racismoambiental.net.br | 1 | 0.02% | 0.05% |
| news_api | radikal.com.tr | 1 | 0.02% | 0.05% |
| news_api | radiofrance.fr | 1 | 0.02% | 0.05% |
| news_api | radiopolar.com | 1 | 0.02% | 0.05% |
| news_api | radioseoul1650.com | 1 | 0.02% | 0.05% |
| news_api | radiotamazuj.org | 1 | 0.02% | 0.05% |
| news_api | rappler.com | 1 | 0.02% | 0.05% |
| news_api | ratopati.com | 1 | 0.02% | 0.05% |
| news_api | realitatea.net | 1 | 0.02% | 0.05% |
| news_api | redlandsdailyfacts.com | 1 | 0.02% | 0.05% |
| news_api | regions.ru | 1 | 0.02% | 0.05% |
| news_api | reporterdiario.com.br | 1 | 0.02% | 0.05% |
| news_api | reporterherald.com | 1 | 0.02% | 0.05% |
| news_api | republicain-lorrain.fr | 1 | 0.02% | 0.05% |
| news_api | republikein.com.na | 1 | 0.02% | 0.05% |
| news_api | riotimesonline.com | 1 | 0.02% | 0.05% |
| news_api | risky.biz | 1 | 0.02% | 0.05% |
| news_api | rnz.co.nz | 1 | 0.02% | 0.05% |
| news_api | rock1067.iheart.com | 1 | 0.02% | 0.05% |
| news_api | rocketerie.iheart.com | 1 | 0.02% | 0.05% |
| news_api | rstreet.org | 1 | 0.02% | 0.05% |
| news_api | rte.ie | 1 | 0.02% | 0.05% |
| news_api | rtl.nl | 1 | 0.02% | 0.05% |
| news_api | rtv.rs | 1 | 0.02% | 0.05% |
| news_api | rtvutrecht.nl | 1 | 0.02% | 0.05% |
| news_api | ruhrnachrichten.de | 1 | 0.02% | 0.05% |
| news_api | russiaherald.com | 1 | 0.02% | 0.05% |
| news_api | ruthfullyyours.com | 1 | 0.02% | 0.05% |
| news_api | ryt9.com | 1 | 0.02% | 0.05% |
| news_api | saltlakecitysun.com | 1 | 0.02% | 0.05% |
| news_api | saltwire.com | 1 | 0.02% | 0.05% |
| news_api | salzburg24.at | 1 | 0.02% | 0.05% |
| news_api | sana.sy | 1 | 0.02% | 0.05% |
| news_api | sandiegouniontribune.com | 1 | 0.02% | 0.05% |
| news_api | santamariatimes.com | 1 | 0.02% | 0.05% |
| news_api | sapo.pt | 1 | 0.02% | 0.05% |
| news_api | sbsun.com | 1 | 0.02% | 0.05% |
| news_api | sc.stock.cnfol.com | 1 | 0.02% | 0.05% |
| news_api | scdaily.com | 1 | 0.02% | 0.05% |
| news_api | scmp.com | 1 | 0.02% | 0.05% |
| news_api | scroll.in | 1 | 0.02% | 0.05% |
| news_api | sdpnoticias.com | 1 | 0.02% | 0.05% |
| news_api | seekingalpha.com | 1 | 0.02% | 0.05% |
| news_api | sentinelandenterprise.com | 1 | 0.02% | 0.05% |
| news_api | setn.com | 1 | 0.02% | 0.05% |
| news_api | sharemanthan.in | 1 | 0.02% | 0.05% |
| news_api | siliconangle.com | 1 | 0.02% | 0.05% |
| news_api | siliconrepublic.com | 1 | 0.02% | 0.05% |
| news_api | simcoe.com | 1 | 0.02% | 0.05% |
| news_api | siol.net | 1 | 0.02% | 0.05% |
| news_api | slguardian.org | 1 | 0.02% | 0.05% |
| news_api | slugmag.com | 1 | 0.02% | 0.05% |
| news_api | smh.com.au | 1 | 0.02% | 0.05% |
| news_api | sn.at | 1 | 0.02% | 0.05% |
| news_api | son.tv | 1 | 0.02% | 0.05% |
| news_api | sonara.net | 1 | 0.02% | 0.05% |
| news_api | southernhighlandnews.com.au | 1 | 0.02% | 0.05% |
| news_api | spacedaily.com | 1 | 0.02% | 0.05% |
| news_api | spartanavenue.com | 1 | 0.02% | 0.05% |
| news_api | spokesman.com | 1 | 0.02% | 0.05% |
| news_api | srilankasource.com | 1 | 0.02% | 0.05% |
| news_api | star945.com | 1 | 0.02% | 0.05% |
| news_api | statecollege.com | 1 | 0.02% | 0.05% |
| news_api | stcatharinesstandard.ca | 1 | 0.02% | 0.05% |
| news_api | stern.de | 1 | 0.02% | 0.05% |
| news_api | stile.it | 1 | 0.02% | 0.05% |
| news_api | stlouisstar.com | 1 | 0.02% | 0.05% |
| news_api | stock.hexun.com | 1 | 0.02% | 0.05% |
| news_api | stockbiz.vn | 1 | 0.02% | 0.05% |
| news_api | strategypage.com | 1 | 0.02% | 0.05% |
| news_api | stripes.com | 1 | 0.02% | 0.05% |
| news_api | studiob.rs | 1 | 0.02% | 0.05% |
| news_api | sud.ua | 1 | 0.02% | 0.05% |
| news_api | sueddeutsche.de | 1 | 0.02% | 0.05% |
| news_api | t-l.ru | 1 | 0.02% | 0.05% |
| news_api | t13.cl | 1 | 0.02% | 0.05% |
| news_api | t3n.de | 1 | 0.02% | 0.05% |
| news_api | tagesanzeiger.ch | 1 | 0.02% | 0.05% |
| news_api | tagesschau.de | 1 | 0.02% | 0.05% |
| news_api | tagesspiegel.de | 1 | 0.02% | 0.05% |
| news_api | taiwandaily.net | 1 | 0.02% | 0.05% |
| news_api | tass.ru | 1 | 0.02% | 0.05% |
| news_api | taz.de | 1 | 0.02% | 0.05% |
| news_api | tech.china.com | 1 | 0.02% | 0.05% |
| news_api | techcabal.com | 1 | 0.02% | 0.05% |
| news_api | techstory.in | 1 | 0.02% | 0.05% |
| news_api | techtimes.com | 1 | 0.02% | 0.05% |
| news_api | techtudo.com.br | 1 | 0.02% | 0.05% |
| news_api | tecmundo.com.br | 1 | 0.02% | 0.05% |
| news_api | tecnoandroid.it | 1 | 0.02% | 0.05% |
| news_api | tekniikkatalous.fi | 1 | 0.02% | 0.05% |
| news_api | texasguardian.com | 1 | 0.02% | 0.05% |
| news_api | thailand-business-news.com | 1 | 0.02% | 0.05% |
| news_api | thanhnien.vn | 1 | 0.02% | 0.05% |
| news_api | the-miyanichi.co.jp | 1 | 0.02% | 0.05% |
| news_api | theage.com.au | 1 | 0.02% | 0.05% |
| news_api | thebftonline.com | 1 | 0.02% | 0.05% |
| news_api | theblaze.com | 1 | 0.02% | 0.05% |
| news_api | theboneonline.com | 1 | 0.02% | 0.05% |
| news_api | thebusinessjournal.com | 1 | 0.02% | 0.05% |
| news_api | thecable.ng | 1 | 0.02% | 0.05% |
| news_api | thecamarilloacorn.com | 1 | 0.02% | 0.05% |
| news_api | thecourier.com.au | 1 | 0.02% | 0.05% |
| news_api | thedailyworld.com | 1 | 0.02% | 0.05% |
| news_api | thefrontierpost.com | 1 | 0.02% | 0.05% |
| news_api | thegardenisland.com | 1 | 0.02% | 0.05% |
| news_api | theguardian.com | 1 | 0.02% | 0.05% |
| news_api | thehardtackle.com | 1 | 0.02% | 0.05% |
| news_api | thehindubusinessline.com | 1 | 0.02% | 0.05% |
| news_api | theindependent.co.zw | 1 | 0.02% | 0.05% |
| news_api | theitem.com | 1 | 0.02% | 0.05% |
| news_api | thejournal.com | 1 | 0.02% | 0.05% |
| news_api | theleader.com.au | 1 | 0.02% | 0.05% |
| news_api | themissouritimes.com | 1 | 0.02% | 0.05% |
| news_api | themoscowtimes.com | 1 | 0.02% | 0.05% |
| news_api | thenational.scot | 1 | 0.02% | 0.05% |
| news_api | thepeterboroughexaminer.com | 1 | 0.02% | 0.05% |
| news_api | therecord.com | 1 | 0.02% | 0.05% |
| news_api | thespec.com | 1 | 0.02% | 0.05% |
| news_api | thestar.com.my | 1 | 0.02% | 0.05% |
| news_api | thesunchronicle.com | 1 | 0.02% | 0.05% |
| news_api | thetoc.gr | 1 | 0.02% | 0.05% |
| news_api | theverge.com | 1 | 0.02% | 0.05% |
| news_api | thirdsector.co.uk | 1 | 0.02% | 0.05% |
| news_api | thurrockgazette.co.uk | 1 | 0.02% | 0.05% |
| news_api | ticweb.es | 1 | 0.02% | 0.05% |
| news_api | timesleader.com | 1 | 0.02% | 0.05% |
| news_api | timeslive.co.za | 1 | 0.02% | 0.05% |
| news_api | timesofsandiego.com | 1 | 0.02% | 0.05% |
| news_api | tivi.fi | 1 | 0.02% | 0.05% |
| news_api | toffeeweb.com | 1 | 0.02% | 0.05% |
| news_api | toonippo.co.jp | 1 | 0.02% | 0.05% |
| news_api | top-channel.tv | 1 | 0.02% | 0.05% |
| news_api | topics.or.jp | 1 | 0.02% | 0.05% |
| news_api | toronto.citynews.ca | 1 | 0.02% | 0.05% |
| news_api | torquenews.com | 1 | 0.02% | 0.05% |
| news_api | totaltele.com | 1 | 0.02% | 0.05% |
| news_api | townhall.com | 1 | 0.02% | 0.05% |
| news_api | travelweekly.com.au | 1 | 0.02% | 0.05% |
| news_api | troyrecord.com | 1 | 0.02% | 0.05% |
| news_api | trustedreviews.com | 1 | 0.02% | 0.05% |
| news_api | tucsonpost.com | 1 | 0.02% | 0.05% |
| news_api | tumentoday.ru | 1 | 0.02% | 0.05% |
| news_api | turkiyegazetesi.com.tr | 1 | 0.02% | 0.05% |
| news_api | turktime.com | 1 | 0.02% | 0.05% |
| news_api | tvline.com | 1 | 0.02% | 0.05% |
| news_api | tvxs.gr | 1 | 0.02% | 0.05% |
| news_api | twincities.com | 1 | 0.02% | 0.05% |
| news_api | twz.com | 1 | 0.02% | 0.05% |
| news_api | ukrinform.ua | 1 | 0.02% | 0.05% |
| news_api | understandingwar.org | 1 | 0.02% | 0.05% |
| news_api | upi.com | 1 | 0.02% | 0.05% |
| news_api | us.cnn.com | 1 | 0.02% | 0.05% |
| news_api | utilitydive.com | 1 | 0.02% | 0.05% |
| news_api | utv.ie | 1 | 0.02% | 0.05% |
| news_api | uzmanpara.milliyet.com.tr | 1 | 0.02% | 0.05% |
| news_api | vanguardia.com.mx | 1 | 0.02% | 0.05% |
| news_api | vecer.com | 1 | 0.02% | 0.05% |
| news_api | vecernji.ba | 1 | 0.02% | 0.05% |
| news_api | vesti-ua.net | 1 | 0.02% | 0.05% |
| news_api | vicnews.com | 1 | 0.02% | 0.05% |
| news_api | vietnam.vnanet.vn | 1 | 0.02% | 0.05% |
| news_api | vm.ru | 1 | 0.02% | 0.05% |
| news_api | volksstimme.de | 1 | 0.02% | 0.05% |
| news_api | vrt.be | 1 | 0.02% | 0.05% |
| news_api | wahpetondailynews.com | 1 | 0.02% | 0.05% |
| news_api | wallstreet-online.de | 1 | 0.02% | 0.05% |
| news_api | wape.com | 1 | 0.02% | 0.05% |
| news_api | war.obozrevatel.com | 1 | 0.02% | 0.05% |
| news_api | washingtonexaminer.com | 1 | 0.02% | 0.05% |
| news_api | watoday.com.au | 1 | 0.02% | 0.05% |
| news_api | watson.ch | 1 | 0.02% | 0.05% |
| news_api | wbkr.com | 1 | 0.02% | 0.05% |
| news_api | wboc.com | 1 | 0.02% | 0.05% |
| news_api | wcbi.com | 1 | 0.02% | 0.05% |
| news_api | wcbm.com | 1 | 0.02% | 0.05% |
| news_api | wcvb.com | 1 | 0.02% | 0.05% |
| news_api | wdsu.com | 1 | 0.02% | 0.05% |
| news_api | webinars.govtech.com | 1 | 0.02% | 0.05% |
| news_api | weekend.perfil.com | 1 | 0.02% | 0.05% |
| news_api | welt.de | 1 | 0.02% | 0.05% |
| news_api | wfmd.com | 1 | 0.02% | 0.05% |
| news_api | wftv.com | 1 | 0.02% | 0.05% |
| news_api | wgauradio.com | 1 | 0.02% | 0.05% |
| news_api | wgme.com | 1 | 0.02% | 0.05% |
| news_api | wgna.com | 1 | 0.02% | 0.05% |
| news_api | wgxa.tv | 1 | 0.02% | 0.05% |
| news_api | whittierdailynews.com | 1 | 0.02% | 0.05% |
| news_api | whmi.com | 1 | 0.02% | 0.05% |
| news_api | wibx950.com | 1 | 0.02% | 0.05% |
| news_api | wikitree.co.kr | 1 | 0.02% | 0.05% |
| news_api | winfuture.de | 1 | 0.02% | 0.05% |
| news_api | wirtualnemedia.pl | 1 | 0.02% | 0.05% |
| news_api | wlox.com | 1 | 0.02% | 0.05% |
| news_api | wlwt.com | 1 | 0.02% | 0.05% |
| news_api | wnnj.iheart.com | 1 | 0.02% | 0.05% |
| news_api | wokv.com | 1 | 0.02% | 0.05% |
| news_api | woman.excite.co.jp | 1 | 0.02% | 0.05% |
| news_api | words.filippo.io | 1 | 0.02% | 0.05% |
| news_api | world.kbs.co.kr | 1 | 0.02% | 0.05% |
| news_api | wosu.org | 1 | 0.02% | 0.05% |
| news_api | wowo.com | 1 | 0.02% | 0.05% |
| news_api | wpxi.com | 1 | 0.02% | 0.05% |
| news_api | wset.com | 1 | 0.02% | 0.05% |
| news_api | wshu.org | 1 | 0.02% | 0.05% |
| news_api | wsoctv.com | 1 | 0.02% | 0.05% |
| news_api | wthr.com | 1 | 0.02% | 0.05% |
| news_api | wtsp.com | 1 | 0.02% | 0.05% |
| news_api | wusa9.com | 1 | 0.02% | 0.05% |
| news_api | wvtm13.com | 1 | 0.02% | 0.05% |
| news_api | wwltv.com | 1 | 0.02% | 0.05% |
| news_api | wwwhatsnew.com | 1 | 0.02% | 0.05% |
| news_api | wxii12.com | 1 | 0.02% | 0.05% |
| news_api | wxow.com | 1 | 0.02% | 0.05% |
| news_api | xx.sdnews.com.cn | 1 | 0.02% | 0.05% |
| news_api | y100fm.com | 1 | 0.02% | 0.05% |
| news_api | y95country.com | 1 | 0.02% | 0.05% |
| news_api | yasstribune.com.au | 1 | 0.02% | 0.05% |
| news_api | yeniakit.com.tr | 1 | 0.02% | 0.05% |
| news_api | yeniasya.com.tr | 1 | 0.02% | 0.05% |
| news_api | yn.xinhuanet.com | 1 | 0.02% | 0.05% |
| news_api | yorkpress.co.uk | 1 | 0.02% | 0.05% |
| news_api | zazoom.it | 1 | 0.02% | 0.05% |
| news_api | zdnet.com | 1 | 0.02% | 0.05% |
| news_api | zeit.de | 1 | 0.02% | 0.05% |
| news_api | zetatijuana.com | 1 | 0.02% | 0.05% |
| news_api | ziare.com | 1 | 0.02% | 0.05% |
| news_api | zonebourse.com | 1 | 0.02% | 0.05% |

## Top 30 Inspection Words By source_type

### cve

vulnerability (967), file (413), kernel (369), may (348), issue (339), fix (328), exploit (321), attackers (319), function (299), linux (288), used (287), following (285), resolved (270), attacker (268), attack (266), user (259), allows (257), access (253), manipulation (248), code (234), path (229), arbitrary (221), remote (207), argument (205), component (201), prior (196), version (194), data (192), system (189), affected (186)

### news_api

data (85), security (83), cyber (76), says (70), new (68), scam (62), breach (62), ransomware (48), ddos (48), malware (47), cyberattack (45), attack (44), financial (42), report (38), risk (36), web (34), exploit (34), safe (33), dark (32), amid (32), day (31), rebel (31), openai (31), attacks (30), stay (30), news (30), iran (30), google (29), threat (29), fuel (29)

### news_rss

vulnerability (504), security (409), exploitation (380), windows (371), data (323), likely (302), access (284), less (240), process (226), privilege (206), code (205), new (202), elevation (198), file (190), exploit (179), microsoft (178), system (176), vulnerabilities (170), one (169), used (166), also (163), pointer (159), teams (157), using (153), attack (153), user (152), buffer (150), execution (145), would (143), time (135)

### reddit_rss

link (628), comments (617), submitted (602), like (228), security (171), use (171), would (166), one (145), data (132), work (120), something (117), people (115), anyone (114), new (112), time (108), know (107), using (106), still (105), also (104), don (101), https (100), get (96), actually (95), windows (95), access (94), need (93), system (91), way (91), want (86), com (85)
