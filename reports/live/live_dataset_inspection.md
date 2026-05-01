# Live Dataset Inspection

Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 3683 |
| created_at min | 2025-12-16T09:00:00Z |
| created_at max | 2026-05-01T13:15:03Z |
| collected_at min | 2026-04-29T13:22:42Z |
| collected_at max | 2026-05-01T13:15:46Z |
| Unparsable created_at | 0 (0.00%) |
| Unparsable collected_at | 0 (0.00%) |
| Null/empty text_raw | 0 (0.00%) |
| Mean text_raw length | 505.55 |
| Median text_raw length | 143.0 |
| Min text_raw length | 8 |
| Max text_raw length | 66525 |
| text_raw < 30 chars | 69 (1.87%) |
| text_raw < 100 chars | 1530 (41.54%) |
| Duplicate id rows | 0 rows / 0 values |
| Duplicate url rows | 0 rows / 0 values |
| Duplicate normalized text_raw rows | 319 rows / 92 values |

## Warnings

- WARNING: Duplicate normalized text_raw rows found: 319.

## Rows By source_type

| source_type | rows | percent_dataset |
| --- | --- | --- |
| news_api | 1685 | 45.75% |
| cve | 1295 | 35.16% |
| reddit_rss | 522 | 14.17% |
| news_rss | 181 | 4.91% |

## Rows By source_name

| source_name | rows | percent_dataset |
| --- | --- | --- |
| NVD CVE | 1295 | 35.16% |
| cybersecurity | 107 | 2.91% |
| sysadmin | 102 | 2.77% |
| The Hacker News | 61 | 1.66% |
| privacy | 60 | 1.63% |
| blueteamsec | 50 | 1.36% |
| netsec | 33 | 0.90% |
| BleepingComputer | 33 | 0.90% |
| hacking | 33 | 0.90% |
| forbes.com | 33 | 0.90% |
| techradar.com | 31 | 0.84% |
| ReverseEngineering | 30 | 0.81% |
| AskNetsec | 29 | 0.79% |
| osint | 27 | 0.73% |
| Malware | 26 | 0.71% |
| ComputerSecurity | 25 | 0.68% |
| ascii.jp | 24 | 0.65% |
| cnews.ru | 23 | 0.62% |
| ithome.com.tw | 23 | 0.62% |
| Rapid7 Blog | 22 | 0.60% |
| Cisco Talos Blog | 16 | 0.43% |
| Unit 42 | 16 | 0.43% |
| manilatimes.net | 16 | 0.43% |
| 163.com | 16 | 0.43% |
| itbrief.co.nz | 15 | 0.41% |
| theregister.com | 15 | 0.41% |
| bankinfosecurity.com | 14 | 0.38% |
| govinfosecurity.com | 14 | 0.38% |
| SANS Internet Storm Center | 13 | 0.35% |
| esecurityplanet.com | 12 | 0.33% |
| finance.sina.com.cn | 12 | 0.33% |
| KrebsOnSecurity | 11 | 0.30% |
| finanznachrichten.de | 11 | 0.30% |
| cointelegraph.com | 11 | 0.30% |
| el-balad.com | 11 | 0.30% |
| economictimes.indiatimes.com | 10 | 0.27% |
| techcrunch.com | 10 | 0.27% |
| haberler.com | 10 | 0.27% |
| Google Project Zero | 9 | 0.24% |
| csoonline.com | 9 | 0.24% |
| infosecurity-magazine.com | 9 | 0.24% |
| timesofindia.indiatimes.com | 9 | 0.24% |
| baijiahao.baidu.com | 9 | 0.24% |
| fool.com | 9 | 0.24% |
| finance.yahoo.com | 8 | 0.22% |
| moneycontrol.com | 8 | 0.22% |
| channellife.co.nz | 8 | 0.22% |
| boredpanda.com | 8 | 0.22% |
| jdsupra.com | 7 | 0.19% |
| govtech.com | 6 | 0.16% |
| edaily.co.kr | 6 | 0.16% |
| laopcion.com.mx | 6 | 0.16% |
| securitylab.ru | 6 | 0.16% |
| udayavani.com | 6 | 0.16% |
| biz.heraldcorp.com | 6 | 0.16% |
| tvguide.co.uk | 6 | 0.16% |
| yahoo.com | 5 | 0.14% |
| prnewswire.com | 5 | 0.14% |
| channellife.com.au | 5 | 0.14% |
| fnnews.com | 5 | 0.14% |
| hothardware.com | 4 | 0.11% |
| japan.zdnet.com | 4 | 0.11% |
| insurancebusinessmag.com | 4 | 0.11% |
| winnipegfreepress.com | 4 | 0.11% |
| thenews.com.pk | 4 | 0.11% |
| pcmag.com | 4 | 0.11% |
| thefastmode.com | 4 | 0.11% |
| ddaily.co.kr | 4 | 0.11% |
| zdnet.co.kr | 4 | 0.11% |
| aa.com.tr | 4 | 0.11% |
| kibrispostasi.com | 4 | 0.11% |
| vz.ru | 4 | 0.11% |
| screenrant.com | 4 | 0.11% |
| heise.de | 4 | 0.11% |
| coindesk.com | 4 | 0.11% |
| dostor.org | 4 | 0.11% |
| 9to5mac.com | 4 | 0.11% |
| interfax.ru | 4 | 0.11% |
| itnews.com.au | 4 | 0.11% |
| time.mk | 4 | 0.11% |
| it-online.co.za | 4 | 0.11% |
| tn.com.ar | 4 | 0.11% |
| foxnews.com | 4 | 0.11% |
| computing.co.uk | 4 | 0.11% |
| newjerseytelegraph.com | 4 | 0.11% |
| eturbonews.com | 4 | 0.11% |
| excite.co.jp | 4 | 0.11% |
| androidauthority.com | 3 | 0.08% |
| mondaq.com | 3 | 0.08% |
| tomshardware.com | 3 | 0.08% |
| cnnturk.com | 3 | 0.08% |
| ura.news | 3 | 0.08% |
| donanimgunlugu.com | 3 | 0.08% |
| ensonhaber.com | 3 | 0.08% |
| milliyet.com.tr | 3 | 0.08% |
| womannews.net | 3 | 0.08% |
| miragenews.com | 3 | 0.08% |
| cbc.ca | 3 | 0.08% |
| wesh.com | 3 | 0.08% |
| scoop.co.nz | 3 | 0.08% |
| straitstimes.com | 3 | 0.08% |
| politis.com.cy | 3 | 0.08% |
| koreaherald.com | 3 | 0.08% |
| sabah.com.tr | 3 | 0.08% |
| eurointegration.com.ua | 3 | 0.08% |
| bleedingcool.com | 3 | 0.08% |
| wmur.com | 3 | 0.08% |
| defensenews.com | 3 | 0.08% |
| hindustantimes.com | 3 | 0.08% |
| theglobeandmail.com | 3 | 0.08% |
| n.yam.com | 3 | 0.08% |
| odatv.com | 3 | 0.08% |
| finance.eastmoney.com | 3 | 0.08% |
| shorouknews.com | 3 | 0.08% |
| freepressjournal.in | 3 | 0.08% |
| russian.rt.com | 3 | 0.08% |
| newswiretoday.com | 3 | 0.08% |
| portal.sina.com.hk | 3 | 0.08% |
| itbusinessnet.com | 3 | 0.08% |
| biometricupdate.com | 3 | 0.08% |
| natalie.mu | 3 | 0.08% |
| divyabhaskar.co.in | 3 | 0.08% |
| tribuneindia.com | 3 | 0.08% |
| marketscreener.com | 3 | 0.08% |
| wired.com | 3 | 0.08% |
| itweb.co.za | 3 | 0.08% |
| thenextweb.com | 3 | 0.08% |
| business.scoop.co.nz | 3 | 0.08% |
| claimsjournal.com | 3 | 0.08% |
| itnewsonline.com | 3 | 0.08% |
| alltoc.com | 3 | 0.08% |
| iefimerida.gr | 3 | 0.08% |
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
| wbaltv.com | 2 | 0.05% |
| glavcom.ua | 2 | 0.05% |
| bunburymail.com.au | 2 | 0.05% |
| nvi.com.au | 2 | 0.05% |
| bankingnews.gr | 2 | 0.05% |
| dailykos.com | 2 | 0.05% |
| lalsace.fr | 2 | 0.05% |
| elmanana.com | 2 | 0.05% |
| nzherald.co.nz | 2 | 0.05% |
| news.cn | 2 | 0.05% |
| wiwo.de | 2 | 0.05% |
| trthaber.com | 2 | 0.05% |
| wdrb.com | 2 | 0.05% |
| aol.co.uk | 2 | 0.05% |
| lbc.co.uk | 2 | 0.05% |
| jpost.com | 2 | 0.05% |
| bd-pratidin.com | 2 | 0.05% |
| hurriyetdailynews.com | 2 | 0.05% |
| wfmz.com | 2 | 0.05% |
| hinews.cn | 2 | 0.05% |
| tech.caijing.com.cn | 2 | 0.05% |
| tech.ifeng.com | 2 | 0.05% |
| androidheadlines.com | 2 | 0.05% |
| vietnamnet.vn | 2 | 0.05% |
| vesti.ru | 2 | 0.05% |
| europapress.es | 2 | 0.05% |
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
| itbear.com.cn | 2 | 0.05% |
| index.hr | 2 | 0.05% |
| cloud.watch.impress.co.jp | 2 | 0.05% |
| eldia.com.bo | 2 | 0.05% |
| eldestapeweb.com | 2 | 0.05% |
| businessday.co.za | 2 | 0.05% |
| am.com.mx | 2 | 0.05% |
| insight.co.kr | 2 | 0.05% |
| newspim.com | 2 | 0.05% |
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
| evrensel.net | 2 | 0.05% |
| lrytas.lt | 2 | 0.05% |
| lefigaro.fr | 2 | 0.05% |
| sanantoniopost.com | 2 | 0.05% |
| aninews.in | 2 | 0.05% |
| nypost.com | 2 | 0.05% |
| capital.ro | 2 | 0.05% |
| aceshowbiz.com | 2 | 0.05% |
| deadline.com | 2 | 0.05% |
| macleayargus.com.au | 2 | 0.05% |
| investegate.co.uk | 2 | 0.05% |
| unternehmen-heute.de | 2 | 0.05% |
| arkansasonline.com | 2 | 0.05% |
| natlawreview.com | 2 | 0.05% |
| uainfo.org | 2 | 0.05% |
| fox4news.com | 2 | 0.05% |
| livenews.co.nz | 2 | 0.05% |
| medianama.com | 2 | 0.05% |
| allafrica.com | 2 | 0.05% |
| ecodibergamo.it | 2 | 0.05% |
| daily.com.ua | 2 | 0.05% |
| naftemporiki.gr | 2 | 0.05% |
| eldiariodechihuahua.mx | 2 | 0.05% |
| libnanews.com | 2 | 0.05% |
| ghanamma.com | 2 | 0.05% |
| techweez.com | 2 | 0.05% |
| rediff.com | 2 | 0.05% |
| thisdaylive.com | 2 | 0.05% |
| welivesecurity.com | 2 | 0.05% |
| insideottawavalley.com | 2 | 0.05% |
| tmtpost.com | 2 | 0.05% |
| massachusettssun.com | 2 | 0.05% |
| europesun.com | 2 | 0.05% |
| wzzm13.com | 2 | 0.05% |
| sentinel.ht | 2 | 0.05% |
| punchng.com | 2 | 0.05% |
| globalnews.ca | 2 | 0.05% |
| pravda.ru | 2 | 0.05% |
| danas.rs | 2 | 0.05% |
| mainichi.jp | 2 | 0.05% |
| boerse-express.com | 2 | 0.05% |
| newratings.de | 2 | 0.05% |
| morningstar.com | 2 | 0.05% |
| thesun.ng | 2 | 0.05% |
| dailybreeze.com | 2 | 0.05% |
| dailynews.com | 2 | 0.05% |
| sgvtribune.com | 2 | 0.05% |
| greeleytribune.com | 2 | 0.05% |
| maliactu.net | 2 | 0.05% |
| gdnonline.com | 2 | 0.05% |
| y-mainichi.co.jp | 2 | 0.05% |
| heraldk.com | 2 | 0.05% |
| kathimerini.com.cy | 2 | 0.05% |
| ecommercenews.co.nz | 2 | 0.05% |
| newkerala.com | 2 | 0.05% |
| diariosur.es | 2 | 0.05% |
| unn.ua | 2 | 0.05% |
| rpp.pe | 2 | 0.05% |
| ecodisicilia.com | 2 | 0.05% |
| bangkokpost.com | 1 | 0.03% |
| governing.com | 1 | 0.03% |
| abc7news.com | 1 | 0.03% |
| cnn.com | 1 | 0.03% |
| edition.cnn.com | 1 | 0.03% |
| us.cnn.com | 1 | 0.03% |
| fox9.com | 1 | 0.03% |
| hachettebookgroup.com | 1 | 0.03% |
| bangordailynews.com | 1 | 0.03% |
| bt.no | 1 | 0.03% |
| cnet.com | 1 | 0.03% |
| ryt9.com | 1 | 0.03% |
| antivirus-sniper.macupdate.com | 1 | 0.03% |
| adevarul.ro | 1 | 0.03% |
| bgr.com | 1 | 0.03% |
| express.pk | 1 | 0.03% |
| presse-citron.net | 1 | 0.03% |
| techcabal.com | 1 | 0.03% |
| bangkokbiznews.com | 1 | 0.03% |
| 01net.com | 1 | 0.03% |
| aif.ru | 1 | 0.03% |
| digg.com | 1 | 0.03% |
| etnews.com | 1 | 0.03% |
| generation-nt.com | 1 | 0.03% |
| playground.ru | 1 | 0.03% |
| digitaltrends.com | 1 | 0.03% |
| alanbatnews.net | 1 | 0.03% |
| itnewsafrica.com | 1 | 0.03% |
| trustedreviews.com | 1 | 0.03% |
| news.tuoitre.vn | 1 | 0.03% |
| georgeherald.com | 1 | 0.03% |
| pjmedia.com | 1 | 0.03% |
| regions.ru | 1 | 0.03% |
| businesstimes.com.sg | 1 | 0.03% |
| lexpress.fr | 1 | 0.03% |
| pln-pskov.ru | 1 | 0.03% |
| metroseoul.co.kr | 1 | 0.03% |
| fedpress.ru | 1 | 0.03% |
| wxii12.com | 1 | 0.03% |
| y95country.com | 1 | 0.03% |
| local12.com | 1 | 0.03% |
| kingfm.com | 1 | 0.03% |
| buffalobulletin.com | 1 | 0.03% |
| profitline.hu | 1 | 0.03% |
| de.nachrichten.yahoo.com | 1 | 0.03% |
| directionsmag.com | 1 | 0.03% |
| circleid.com | 1 | 0.03% |
| koco.com | 1 | 0.03% |
| lenta.ru | 1 | 0.03% |
| wvtm13.com | 1 | 0.03% |
| wlwt.com | 1 | 0.03% |
| hirek.prim.hu | 1 | 0.03% |
| ottawacitizen.com | 1 | 0.03% |
| news.ltn.com.tw | 1 | 0.03% |
| dnews.gr | 1 | 0.03% |
| infobae.com | 1 | 0.03% |
| ledauphine.com | 1 | 0.03% |
| dna.fr | 1 | 0.03% |
| laprovincia.es | 1 | 0.03% |
| northweststar.com.au | 1 | 0.03% |
| armenews.com | 1 | 0.03% |
| elcomercio.es | 1 | 0.03% |
| mandurahmail.com.au | 1 | 0.03% |
| salzburg24.at | 1 | 0.03% |
| republicain-lorrain.fr | 1 | 0.03% |
| lejsl.com | 1 | 0.03% |
| lavozdegalicia.es | 1 | 0.03% |
| diariopalentino.es | 1 | 0.03% |
| eldia.es | 1 | 0.03% |
| bbc.com | 1 | 0.03% |
| groundup.org.za | 1 | 0.03% |
| zetatijuana.com | 1 | 0.03% |
| eluniversal.com.mx | 1 | 0.03% |
| aristeguinoticias.com | 1 | 0.03% |
| funkytaurusmedia.com | 1 | 0.03% |
| dw.com | 1 | 0.03% |
| botasot.info | 1 | 0.03% |
| fnp.de | 1 | 0.03% |
| tagesschau.de | 1 | 0.03% |
| ratopati.com | 1 | 0.03% |
| op-online.de | 1 | 0.03% |
| zeit.de | 1 | 0.03% |
| watson.ch | 1 | 0.03% |
| freiepresse.de | 1 | 0.03% |
| yeniakit.com.tr | 1 | 0.03% |
| turkiyegazetesi.com.tr | 1 | 0.03% |
| stern.de | 1 | 0.03% |
| ntv.com.tr | 1 | 0.03% |
| kannadaprabha.com | 1 | 0.03% |
| n-tv.de | 1 | 0.03% |
| sn.at | 1 | 0.03% |
| bursahakimiyet.com.tr | 1 | 0.03% |
| dunya.com | 1 | 0.03% |
| sdpnoticias.com | 1 | 0.03% |
| vecer.com | 1 | 0.03% |
| rtl.nl | 1 | 0.03% |
| norran.se | 1 | 0.03% |
| computerworld.dk | 1 | 0.03% |
| aktifhaber.com | 1 | 0.03% |
| sana.sy | 1 | 0.03% |
| welt.de | 1 | 0.03% |
| japan.cnet.com | 1 | 0.03% |
| vrt.be | 1 | 0.03% |
| donanimhaber.com | 1 | 0.03% |
| dailynews.co.th | 1 | 0.03% |
| heute.at | 1 | 0.03% |
| bankier.pl | 1 | 0.03% |
| antena3.ro | 1 | 0.03% |
| businesstoday.in | 1 | 0.03% |
| 5.ua | 1 | 0.03% |
| kcci.com | 1 | 0.03% |
| twincities.com | 1 | 0.03% |
| king5.com | 1 | 0.03% |
| wtsp.com | 1 | 0.03% |
| wwltv.com | 1 | 0.03% |
| wusa9.com | 1 | 0.03% |
| fox43.com | 1 | 0.03% |
| daytondailynews.com | 1 | 0.03% |
| kmbc.com | 1 | 0.03% |
| fox17online.com | 1 | 0.03% |
| journal-news.com | 1 | 0.03% |
| siliconrepublic.com | 1 | 0.03% |
| 5newsonline.com | 1 | 0.03% |
| beckershospitalreview.com | 1 | 0.03% |
| legalinsurrection.com | 1 | 0.03% |
| riasv.ru | 1 | 0.03% |
| wcbi.com | 1 | 0.03% |
| war.obozrevatel.com | 1 | 0.03% |
| dailymail.co.uk | 1 | 0.03% |
| wlox.com | 1 | 0.03% |
| wthr.com | 1 | 0.03% |
| wwmt.com | 1 | 0.03% |
| yn.xinhuanet.com | 1 | 0.03% |
| news.ycwb.com | 1 | 0.03% |
| kob.com | 1 | 0.03% |
| china.com.cn | 1 | 0.03% |
| digi.china.com | 1 | 0.03% |
| udn.com | 1 | 0.03% |
| dunyanews.tv | 1 | 0.03% |
| diena.lt | 1 | 0.03% |
| deperu.com | 1 | 0.03% |
| photo.china.com.cn | 1 | 0.03% |
| haberturk.com | 1 | 0.03% |
| ondacero.es | 1 | 0.03% |
| dailysabah.com | 1 | 0.03% |
| designboom.com | 1 | 0.03% |
| press24.mk | 1 | 0.03% |
| nj.com | 1 | 0.03% |
| haber3.com | 1 | 0.03% |
| eluniverso.com | 1 | 0.03% |
| idnes.cz | 1 | 0.03% |
| mobile.zol.com.cn | 1 | 0.03% |
| ai.zol.com.cn | 1 | 0.03% |
| posttoday.com | 1 | 0.03% |
| news.cnfol.com | 1 | 0.03% |
| ettoday.net | 1 | 0.03% |
| 3c.ltn.com.tw | 1 | 0.03% |
| bj.xinhuanet.com | 1 | 0.03% |
| nbd.com.cn | 1 | 0.03% |
| tass.ru | 1 | 0.03% |
| ruhrnachrichten.de | 1 | 0.03% |
| techtimes.com | 1 | 0.03% |
| top-channel.tv | 1 | 0.03% |
| jo24.net | 1 | 0.03% |
| panorama.com.al | 1 | 0.03% |
| gamerant.com | 1 | 0.03% |
| balkanweb.com | 1 | 0.03% |
| theblaze.com | 1 | 0.03% |
| lafranceagricole.fr | 1 | 0.03% |
| elwatannews.com | 1 | 0.03% |
| tecmundo.com.br | 1 | 0.03% |
| computerwoche.de | 1 | 0.03% |
| ria.ru | 1 | 0.03% |
| bandaancha.eu | 1 | 0.03% |
| jabar.tribunnews.com | 1 | 0.03% |
| dotekomanie.cz | 1 | 0.03% |
| bug.hr | 1 | 0.03% |
| jpnn.com | 1 | 0.03% |
| gorod48.ru | 1 | 0.03% |
| mskagency.ru | 1 | 0.03% |
| makassar.tribunnews.com | 1 | 0.03% |
| mashable.com | 1 | 0.03% |
| volksstimme.de | 1 | 0.03% |
| handelsblatt.com | 1 | 0.03% |
| sueddeutsche.de | 1 | 0.03% |
| cepro.com | 1 | 0.03% |
| corp.cnews.ru | 1 | 0.03% |
| vesti-ua.net | 1 | 0.03% |
| slguardian.org | 1 | 0.03% |
| chip.de | 1 | 0.03% |
| tivi.fi | 1 | 0.03% |
| strategypage.com | 1 | 0.03% |
| alaskasnewssource.com | 1 | 0.03% |
| risky.biz | 1 | 0.03% |
| zdnet.com | 1 | 0.03% |
| tekniikkatalous.fi | 1 | 0.03% |
| fakti.bg | 1 | 0.03% |
| stcatharinesstandard.ca | 1 | 0.03% |
| therecord.com | 1 | 0.03% |
| thepeterboroughexaminer.com | 1 | 0.03% |
| hydrocarbonprocessing.com | 1 | 0.03% |
| winfuture.de | 1 | 0.03% |
| financial-news.co.uk | 1 | 0.03% |
| berliner-zeitung.de | 1 | 0.03% |
| ukrinform.ua | 1 | 0.03% |
| localnews8.com | 1 | 0.03% |
| kesq.com | 1 | 0.03% |
| openpr.com | 1 | 0.03% |
| datacenterknowledge.com | 1 | 0.03% |
| mirrorspectator.com | 1 | 0.03% |
| kotaku.com | 1 | 0.03% |
| explosion.com | 1 | 0.03% |
| wowo.com | 1 | 0.03% |
| newsweek.com | 1 | 0.03% |
| news.china.com.cn | 1 | 0.03% |
| liputan6.com | 1 | 0.03% |
| webinars.govtech.com | 1 | 0.03% |
| nikkei.com | 1 | 0.03% |
| newtalk.tw | 1 | 0.03% |
| cfi.net.cn | 1 | 0.03% |
| arstechnica.com | 1 | 0.03% |
| futures.cnfol.com | 1 | 0.03% |
| setn.com | 1 | 0.03% |
| senego.com | 1 | 0.03% |
| mp.cnfol.com | 1 | 0.03% |
| finance.ifeng.com | 1 | 0.03% |
| stock.hexun.com | 1 | 0.03% |
| ec.ltn.com.tw | 1 | 0.03% |
| northcountrynow.com | 1 | 0.03% |
| business2community.com | 1 | 0.03% |
| infotechlead.com | 1 | 0.03% |
| clarin.com | 1 | 0.03% |
| wwwhatsnew.com | 1 | 0.03% |
| computerworld.pl | 1 | 0.03% |
| icij.org | 1 | 0.03% |
| tecnoandroid.it | 1 | 0.03% |
| arede.info | 1 | 0.03% |
| extra.ec | 1 | 0.03% |
| ibtimes.com.au | 1 | 0.03% |
| elsiglodetorreon.com.mx | 1 | 0.03% |
| diariodemorelos.com | 1 | 0.03% |
| mobileidworld.com | 1 | 0.03% |
| inwestycje.pl | 1 | 0.03% |
| words.filippo.io | 1 | 0.03% |
| elpais.com.uy | 1 | 0.03% |
| quadratin.com.mx | 1 | 0.03% |
| kmib.co.kr | 1 | 0.03% |
| nikkan.co.jp | 1 | 0.03% |
| mariettatimes.com | 1 | 0.03% |
| statecollege.com | 1 | 0.03% |
| jowhar.com | 1 | 0.03% |
| ohmynews.com | 1 | 0.03% |
| ihalla.com | 1 | 0.03% |
| maharashtratimes.com | 1 | 0.03% |
| inews24.com | 1 | 0.03% |
| travelweekly.com.au | 1 | 0.03% |
| hani.co.kr | 1 | 0.03% |
| journalgazette.net | 1 | 0.03% |
| austinchronicle.com | 1 | 0.03% |
| ktvu.com | 1 | 0.03% |
| pitchfork.com | 1 | 0.03% |
| mathrubhumi.com | 1 | 0.03% |
| divyamarathi.bhaskar.com | 1 | 0.03% |
| digi24.ro | 1 | 0.03% |
| rappler.com | 1 | 0.03% |
| india.com | 1 | 0.03% |
| firstpost.com | 1 | 0.03% |
| thetoc.gr | 1 | 0.03% |
| loksatta.com | 1 | 0.03% |
| newsx.com | 1 | 0.03% |
| dantri.com.vn | 1 | 0.03% |
| bollywoodlife.com | 1 | 0.03% |
| world.kbs.co.kr | 1 | 0.03% |
| punjabitribuneonline.com | 1 | 0.03% |
| navbharattimes.indiatimes.com | 1 | 0.03% |
| bhaskar.com | 1 | 0.03% |
| gulte.com | 1 | 0.03% |
| idiva.com | 1 | 0.03% |
| livehindustan.com | 1 | 0.03% |
| newsbomb.gr | 1 | 0.03% |
| pr.com | 1 | 0.03% |
| srilankasource.com | 1 | 0.03% |
| news8000.com | 1 | 0.03% |
| channelbuzz.ca | 1 | 0.03% |
| totaltele.com | 1 | 0.03% |
| dominicanrepublicpost.com | 1 | 0.03% |
| aljazeera.com | 1 | 0.03% |
| rte.ie | 1 | 0.03% |
| dcvelocity.com | 1 | 0.03% |
| californiatelegraph.com | 1 | 0.03% |
| republikein.com.na | 1 | 0.03% |
| bozemandailychronicle.com | 1 | 0.03% |
| bmmagazine.co.uk | 1 | 0.03% |
| vm.ru | 1 | 0.03% |
| ibtimes.co.uk | 1 | 0.03% |
| metronews.ru | 1 | 0.03% |
| dha.com.tr | 1 | 0.03% |
| haksozhaber.net | 1 | 0.03% |
| mngz.ru | 1 | 0.03% |
| cafebiz.vn | 1 | 0.03% |
| lgz.ru | 1 | 0.03% |
| canardpc.com | 1 | 0.03% |
| mersinhaber.com | 1 | 0.03% |
| tgrthaber.com | 1 | 0.03% |
| diyarbakirsoz.com | 1 | 0.03% |
| lakersnation.com | 1 | 0.03% |
| yeniasya.com.tr | 1 | 0.03% |
| sozcu.com.tr | 1 | 0.03% |
| stockbiz.vn | 1 | 0.03% |
| lite987.com | 1 | 0.03% |
| 961theeagle.com | 1 | 0.03% |
| wibx950.com | 1 | 0.03% |
| southernhighlandnews.com.au | 1 | 0.03% |
| wgna.com | 1 | 0.03% |
| biz.cnews.ru | 1 | 0.03% |
| pcwplus.hu | 1 | 0.03% |
| mississauga.com | 1 | 0.03% |
| memeburn.com | 1 | 0.03% |
| igamingbusiness.com | 1 | 0.03% |
| helpconsumatori.it | 1 | 0.03% |
| themissouritimes.com | 1 | 0.03% |
| newstribune.com | 1 | 0.03% |
| iraqsun.com | 1 | 0.03% |
| portalsamorzadowy.pl | 1 | 0.03% |
| livemint.com | 1 | 0.03% |
| nearshoreamericas.com | 1 | 0.03% |
| inquirer.com | 1 | 0.03% |
| thefrontierpost.com | 1 | 0.03% |
| upi.com | 1 | 0.03% |
| koreatimes.co.kr | 1 | 0.03% |
| dynamicbusiness.com | 1 | 0.03% |
| zonebourse.com | 1 | 0.03% |
| interaksyon.philstar.com | 1 | 0.03% |
| timeslive.co.za | 1 | 0.03% |
| nbcmontana.com | 1 | 0.03% |
| clydebankpost.co.uk | 1 | 0.03% |
| tagesanzeiger.ch | 1 | 0.03% |
| zazoom.it | 1 | 0.03% |
| bernerzeitung.ch | 1 | 0.03% |
| mittelstandcafe.de | 1 | 0.03% |
| drimble.nl | 1 | 0.03% |
| nieuws.nl | 1 | 0.03% |
| vecernji.ba | 1 | 0.03% |
| haber1.com | 1 | 0.03% |
| juneesoutherncross.com.au | 1 | 0.03% |
| braidwoodtimes.com.au | 1 | 0.03% |
| armidaleexpress.com.au | 1 | 0.03% |
| crookwellgazette.com.au | 1 | 0.03% |
| theleader.com.au | 1 | 0.03% |
| thecourier.com.au | 1 | 0.03% |
| batemansbaypost.com.au | 1 | 0.03% |
| cootamundraherald.com.au | 1 | 0.03% |
| camdencourier.com.au | 1 | 0.03% |
| yasstribune.com.au | 1 | 0.03% |
| northerndailyleader.com.au | 1 | 0.03% |
| dailyadvertiser.com.au | 1 | 0.03% |
| mudgeeguardian.com.au | 1 | 0.03% |
| portnews.com.au | 1 | 0.03% |
| asahi.com | 1 | 0.03% |
| manningrivertimes.com.au | 1 | 0.03% |
| bluemountainsgazette.com.au | 1 | 0.03% |
| newcastleherald.com.au | 1 | 0.03% |
| inverelltimes.com.au | 1 | 0.03% |
| lithgowmercury.com.au | 1 | 0.03% |
| illawarramercury.com.au | 1 | 0.03% |
| tagesspiegel.de | 1 | 0.03% |
| thesunchronicle.com | 1 | 0.03% |
| indiatvnews.com | 1 | 0.03% |
| watoday.com.au | 1 | 0.03% |
| nwaonline.com | 1 | 0.03% |
| techstory.in | 1 | 0.03% |
| english.pravda.ru | 1 | 0.03% |
| daily-tribune.com | 1 | 0.03% |
| saltwire.com | 1 | 0.03% |
| afr.com | 1 | 0.03% |
| internetua.com | 1 | 0.03% |
| whmi.com | 1 | 0.03% |
| utilitydive.com | 1 | 0.03% |
| michigandaily.com | 1 | 0.03% |
| wdsu.com | 1 | 0.03% |
| blackseanews.net | 1 | 0.03% |
| podrobnosti.ua | 1 | 0.03% |
| dailyemerald.com | 1 | 0.03% |
| island.lk | 1 | 0.03% |
| businessinsurance.com | 1 | 0.03% |
| presstv.ir | 1 | 0.03% |
| polygon.com | 1 | 0.03% |
| aljazeera.net | 1 | 0.03% |
| aktivni.metropolitan.si | 1 | 0.03% |
| borsonline.hu | 1 | 0.03% |
| sc.stock.cnfol.com | 1 | 0.03% |
| mundoenlinea.cl | 1 | 0.03% |
| informationweek.com | 1 | 0.03% |
| collider.com | 1 | 0.03% |
| investorplace.com | 1 | 0.03% |
| bgonair.bg | 1 | 0.03% |
| thehindubusinessline.com | 1 | 0.03% |
| blikk.hu | 1 | 0.03% |
| femina.hu | 1 | 0.03% |
| index.hu | 1 | 0.03% |
| economx.hu | 1 | 0.03% |
| spartanavenue.com | 1 | 0.03% |
| rnz.co.nz | 1 | 0.03% |
| theverge.com | 1 | 0.03% |
| chinesepress.com | 1 | 0.03% |
| kztv10.com | 1 | 0.03% |
| kristv.com | 1 | 0.03% |
| primerafuente.com.ar | 1 | 0.03% |
| nationalmortgagenews.com | 1 | 0.03% |
| larepubliquedespyrenees.fr | 1 | 0.03% |
| torquenews.com | 1 | 0.03% |
| scroll.in | 1 | 0.03% |
| money.it | 1 | 0.03% |
| toronto.citynews.ca | 1 | 0.03% |
| nrc.nl | 1 | 0.03% |
| elconfidencial.com | 1 | 0.03% |
| diario.mx | 1 | 0.03% |
| it.euronews.com | 1 | 0.03% |
| downtoearth.org.in | 1 | 0.03% |
| ly.fjsen.com | 1 | 0.03% |
| publico.pt | 1 | 0.03% |
| lagacetadesalamanca.es | 1 | 0.03% |
| marca.com | 1 | 0.03% |
| weekend.perfil.com | 1 | 0.03% |
| jogja.tribunnews.com | 1 | 0.03% |
| inosmi.ru | 1 | 0.03% |
| kontrakty.ua | 1 | 0.03% |
| laut.de | 1 | 0.03% |
| cjme.com | 1 | 0.03% |
| megamodo.com | 1 | 0.03% |
| brasil247.com | 1 | 0.03% |
| closermag.fr | 1 | 0.03% |
| elperiodicodearagon.com | 1 | 0.03% |
| comingsoon.it | 1 | 0.03% |
| fatimanews.com.br | 1 | 0.03% |
| kaos911.com | 1 | 0.03% |
| administradores.com.br | 1 | 0.03% |
| al-monitor.com | 1 | 0.03% |
| linux.org.ru | 1 | 0.03% |
| thenational.scot | 1 | 0.03% |
| marketintelligencecenter.com | 1 | 0.03% |
| dailyexcelsior.com | 1 | 0.03% |
| lina.sh | 1 | 0.03% |
| themoscowtimes.com | 1 | 0.03% |
| ko.com.ua | 1 | 0.03% |
| yorkpress.co.uk | 1 | 0.03% |
| ticweb.es | 1 | 0.03% |
| dailypolitical.com | 1 | 0.03% |
| jagranjosh.com | 1 | 0.03% |
| 24sata.hr | 1 | 0.03% |
| net.hr | 1 | 0.03% |
| wallstreet-online.de | 1 | 0.03% |
| dp.ru | 1 | 0.03% |
| amic.ru | 1 | 0.03% |
| meridiano.net | 1 | 0.03% |
| niagarathisweek.com | 1 | 0.03% |
| yorkregion.com | 1 | 0.03% |
| simcoe.com | 1 | 0.03% |
| gadgetsmagazine.com.ph | 1 | 0.03% |
| spacedaily.com | 1 | 0.03% |
| insight.scmagazineuk.com | 1 | 0.03% |
| 21stcenturywire.com | 1 | 0.03% |
| ghanaiantimes.com.gh | 1 | 0.03% |
| donews.com | 1 | 0.03% |
| pv-magazine.com | 1 | 0.03% |
| tech.china.com | 1 | 0.03% |
| pakistantelegraph.com | 1 | 0.03% |
| birminghamstar.com | 1 | 0.03% |
| laosnews.net | 1 | 0.03% |
| chinanationalnews.com | 1 | 0.03% |
| newyorkstatesman.com | 1 | 0.03% |
| coloradostar.com | 1 | 0.03% |
| nashvilleherald.com | 1 | 0.03% |
| stlouisstar.com | 1 | 0.03% |
| saltlakecitysun.com | 1 | 0.03% |
| myanmarnews.net | 1 | 0.03% |
| utv.ie | 1 | 0.03% |
| eejournal.com | 1 | 0.03% |
| elektroniknet.de | 1 | 0.03% |
| thejournal.com | 1 | 0.03% |
| dailypioneer.com | 1 | 0.03% |
| newrepublic.com | 1 | 0.03% |
| jamaicaobserver.com | 1 | 0.03% |
| itbrief.news | 1 | 0.03% |
| rstreet.org | 1 | 0.03% |
| insidermonkey.com | 1 | 0.03% |
| wcvb.com | 1 | 0.03% |
| wxow.com | 1 | 0.03% |
| mensxp.com | 1 | 0.03% |
| bianet.org | 1 | 0.03% |
| slugmag.com | 1 | 0.03% |
| wape.com | 1 | 0.03% |
| kiro7.com | 1 | 0.03% |
| 99jamzmiami.com | 1 | 0.03% |
| actionnewsjax.com | 1 | 0.03% |
| star945.com | 1 | 0.03% |
| y100fm.com | 1 | 0.03% |
| wftv.com | 1 | 0.03% |
| kono1011.com | 1 | 0.03% |
| 1055thedove.com | 1 | 0.03% |
| wsoctv.com | 1 | 0.03% |
| hits1053sanantonio.com | 1 | 0.03% |
| latele.ch | 1 | 0.03% |
| eaglesanantonio.com | 1 | 0.03% |
| wokv.com | 1 | 0.03% |
| powerorlando.com | 1 | 0.03% |
| 1015vibe.com | 1 | 0.03% |
| wpxi.com | 1 | 0.03% |
| b985.com | 1 | 0.03% |
| theboneonline.com | 1 | 0.03% |
| eagledayton.com | 1 | 0.03% |
| wgauradio.com | 1 | 0.03% |
| french.china.org.cn | 1 | 0.03% |
| mymagic949.com | 1 | 0.03% |
| kissrocks.com | 1 | 0.03% |
| magic1021.com | 1 | 0.03% |
| hits973.com | 1 | 0.03% |
| k991fm.com | 1 | 0.03% |
| journaldunet.com | 1 | 0.03% |
| objectiv.tv | 1 | 0.03% |
| lesmobiles.com | 1 | 0.03% |
| toffeeweb.com | 1 | 0.03% |
| 10tv.com | 1 | 0.03% |
| dailyinqilab.com | 1 | 0.03% |
| asianews.it | 1 | 0.03% |
| castanetkamloops.net | 1 | 0.03% |
| cp24.com | 1 | 0.03% |
| wshu.org | 1 | 0.03% |
| brandonsun.com | 1 | 0.03% |
| kiplinger.com | 1 | 0.03% |
| cambridgetimes.ca | 1 | 0.03% |
| abovethelaw.com | 1 | 0.03% |
| mactech.com | 1 | 0.03% |
| brooklyneagle.com | 1 | 0.03% |
| laleggepertutti.it | 1 | 0.03% |
| rtv.rs | 1 | 0.03% |
| niezalezna.pl | 1 | 0.03% |
| taz.de | 1 | 0.03% |
| dailypakistan.pk | 1 | 0.03% |
| wirtualnemedia.pl | 1 | 0.03% |
| prensalibre.com | 1 | 0.03% |
| twz.com | 1 | 0.03% |
| autoexpress.co.uk | 1 | 0.03% |
| studiob.rs | 1 | 0.03% |
| nin.rs | 1 | 0.03% |
| finans.mynet.com | 1 | 0.03% |
| sud.ua | 1 | 0.03% |
| newsnet5.com | 1 | 0.03% |
| labs.watchtowr.com | 1 | 0.03% |
| independent.co.uk | 1 | 0.03% |
| aliran.com | 1 | 0.03% |
| sharemanthan.in | 1 | 0.03% |
| brisbanetimes.com.au | 1 | 0.03% |
| sandiegouniontribune.com | 1 | 0.03% |
| reporterherald.com | 1 | 0.03% |
| theage.com.au | 1 | 0.03% |
| smh.com.au | 1 | 0.03% |
| mdjonline.com | 1 | 0.03% |
| dglobe.com | 1 | 0.03% |
| echopress.com | 1 | 0.03% |
| placenorthwest.co.uk | 1 | 0.03% |
| troyrecord.com | 1 | 0.03% |
| lelezard.com | 1 | 0.03% |
| spokesman.com | 1 | 0.03% |
| whittierdailynews.com | 1 | 0.03% |
| irishtimes.com | 1 | 0.03% |
| wboc.com | 1 | 0.03% |
| theindependent.co.zw | 1 | 0.03% |
| dailymail.com | 1 | 0.03% |
| alquds.co.uk | 1 | 0.03% |
| jamestown.org | 1 | 0.03% |
| wahpetondailynews.com | 1 | 0.03% |
| thehardtackle.com | 1 | 0.03% |
| sentinelandenterprise.com | 1 | 0.03% |
| dailytrust.com | 1 | 0.03% |
| bostonherald.com | 1 | 0.03% |
| dailyjournalonline.com | 1 | 0.03% |
| tvxs.gr | 1 | 0.03% |
| liberta.it | 1 | 0.03% |
| pressdemocrat.com | 1 | 0.03% |
| blogs.itmedia.co.jp | 1 | 0.03% |
| mochimag.com | 1 | 0.03% |
| ocregister.com | 1 | 0.03% |
| presstelegram.com | 1 | 0.03% |
| nikkan-gendai.com | 1 | 0.03% |
| toonippo.co.jp | 1 | 0.03% |
| newsway.co.kr | 1 | 0.03% |
| redlandsdailyfacts.com | 1 | 0.03% |
| timesofsandiego.com | 1 | 0.03% |
| wikitree.co.kr | 1 | 0.03% |
| the-miyanichi.co.jp | 1 | 0.03% |
| newsit.gr | 1 | 0.03% |
| postandcourier.com | 1 | 0.03% |
| gipedo.politis.com.cy | 1 | 0.03% |
| carolinajournal.com | 1 | 0.03% |
| wbkr.com | 1 | 0.03% |
| topics.or.jp | 1 | 0.03% |
| aspentimes.com | 1 | 0.03% |
| dailyuw.com | 1 | 0.03% |
| paymentweek.com | 1 | 0.03% |
| bfmtv.com | 1 | 0.03% |
| bigpara.hurriyet.com.tr | 1 | 0.03% |
| idrw.org | 1 | 0.03% |
| techtudo.com.br | 1 | 0.03% |
| dol.com.br | 1 | 0.03% |
| gamestar.de | 1 | 0.03% |
| netzwelt.de | 1 | 0.03% |
| t13.cl | 1 | 0.03% |
| vetogate.com | 1 | 0.03% |
| kwcdcountry.com | 1 | 0.03% |
| choice.com.au | 1 | 0.03% |
| ostro.org | 1 | 0.03% |
| batonrougepost.com | 1 | 0.03% |
| cincinnatisun.com | 1 | 0.03% |
| ohiostandard.com | 1 | 0.03% |
| oklahomastar.com | 1 | 0.03% |
| russiaherald.com | 1 | 0.03% |
| texasguardian.com | 1 | 0.03% |
| neworleanssun.com | 1 | 0.03% |
| japanherald.com | 1 | 0.03% |
| tucsonpost.com | 1 | 0.03% |
| arabherald.com | 1 | 0.03% |
| greekherald.com | 1 | 0.03% |
| floridastatesman.com | 1 | 0.03% |
| bignewsnetwork.com | 1 | 0.03% |
| hokkoku.co.jp | 1 | 0.03% |
| noviny.sk | 1 | 0.03% |
| cas.sk | 1 | 0.03% |
| econotimes.com | 1 | 0.03% |
| austinglobe.com | 1 | 0.03% |
| londonlovesbusiness.com | 1 | 0.03% |
| blogs.diariovasco.com | 1 | 0.03% |
| sapo.pt | 1 | 0.03% |
| hespress.com | 1 | 0.03% |
| diariodeburgos.es | 1 | 0.03% |
| filmfare.com | 1 | 0.03% |
| wosu.org | 1 | 0.03% |
| rtvutrecht.nl | 1 | 0.03% |
| chinapress.com.my | 1 | 0.03% |
| makaangola.org | 1 | 0.03% |
| eleco.com.ar | 1 | 0.03% |
| golosarmenii.am | 1 | 0.03% |
| countercurrents.org | 1 | 0.03% |
| israelherald.com | 1 | 0.03% |
| estadao.com.br | 1 | 0.03% |
| businessworld.in | 1 | 0.03% |
| radiofrance.fr | 1 | 0.03% |
| financialafrik.com | 1 | 0.03% |
| hoy.es | 1 | 0.03% |
| eadt.co.uk | 1 | 0.03% |
| blog.wenxuecity.com | 1 | 0.03% |
| elpais.com | 1 | 0.03% |
| news.cts.com.tw | 1 | 0.03% |
| francetoday.com | 1 | 0.03% |
| nagpurtoday.in | 1 | 0.03% |
| scmp.com | 1 | 0.03% |
| corriereadriatico.it | 1 | 0.03% |
| focus.ua | 1 | 0.03% |
| dagensps.se | 1 | 0.03% |
| ici.fr | 1 | 0.03% |
| elmalaeb.com | 1 | 0.03% |
| pcchip.hr | 1 | 0.03% |
| kocaeligazetesi.com.tr | 1 | 0.03% |
| theguardian.com | 1 | 0.03% |
| astroawani.com | 1 | 0.03% |
| merkur.de | 1 | 0.03% |
| pleinevie.fr | 1 | 0.03% |
| nile.eg | 1 | 0.03% |
| uzmanpara.milliyet.com.tr | 1 | 0.03% |
| internasional.kompas.com | 1 | 0.03% |
| q947fm.iheart.com | 1 | 0.03% |
| c101.iheart.com | 1 | 0.03% |
| siol.net | 1 | 0.03% |
| jeuneafrique.com | 1 | 0.03% |
| f1vilag.hu | 1 | 0.03% |
| larazon.es | 1 | 0.03% |
| business24.ro | 1 | 0.03% |
| damernasvarld.expressen.se | 1 | 0.03% |
| realitatea.net | 1 | 0.03% |
| rocketerie.iheart.com | 1 | 0.03% |
| 995thefox.iheart.com | 1 | 0.03% |
| 985thefox.iheart.com | 1 | 0.03% |
| wnnj.iheart.com | 1 | 0.03% |
| mebpersonel.com | 1 | 0.03% |
| german.china.org.cn | 1 | 0.03% |
| rock1067.iheart.com | 1 | 0.03% |
| piter.tv | 1 | 0.03% |
| jogjapolitan.harianjogja.com | 1 | 0.03% |
| leiphone.com | 1 | 0.03% |

## Source Distribution

| source_type | source_name | rows | percent_dataset | percent_source_type |
| --- | --- | --- | --- | --- |
| cve | NVD CVE | 1295 | 35.16% | 100.00% |
| reddit_rss | cybersecurity | 107 | 2.91% | 20.50% |
| reddit_rss | sysadmin | 102 | 2.77% | 19.54% |
| news_rss | The Hacker News | 61 | 1.66% | 33.70% |
| reddit_rss | privacy | 60 | 1.63% | 11.49% |
| reddit_rss | blueteamsec | 50 | 1.36% | 9.58% |
| news_api | forbes.com | 33 | 0.90% | 1.96% |
| news_rss | BleepingComputer | 33 | 0.90% | 18.23% |
| reddit_rss | hacking | 33 | 0.90% | 6.32% |
| reddit_rss | netsec | 33 | 0.90% | 6.32% |
| news_api | techradar.com | 31 | 0.84% | 1.84% |
| reddit_rss | ReverseEngineering | 30 | 0.81% | 5.75% |
| reddit_rss | AskNetsec | 29 | 0.79% | 5.56% |
| reddit_rss | osint | 27 | 0.73% | 5.17% |
| reddit_rss | Malware | 26 | 0.71% | 4.98% |
| reddit_rss | ComputerSecurity | 25 | 0.68% | 4.79% |
| news_api | ascii.jp | 24 | 0.65% | 1.42% |
| news_api | cnews.ru | 23 | 0.62% | 1.36% |
| news_api | ithome.com.tw | 23 | 0.62% | 1.36% |
| news_rss | Rapid7 Blog | 22 | 0.60% | 12.15% |
| news_api | 163.com | 16 | 0.43% | 0.95% |
| news_api | manilatimes.net | 16 | 0.43% | 0.95% |
| news_rss | Cisco Talos Blog | 16 | 0.43% | 8.84% |
| news_rss | Unit 42 | 16 | 0.43% | 8.84% |
| news_api | itbrief.co.nz | 15 | 0.41% | 0.89% |
| news_api | theregister.com | 15 | 0.41% | 0.89% |
| news_api | bankinfosecurity.com | 14 | 0.38% | 0.83% |
| news_api | govinfosecurity.com | 14 | 0.38% | 0.83% |
| news_rss | SANS Internet Storm Center | 13 | 0.35% | 7.18% |
| news_api | esecurityplanet.com | 12 | 0.33% | 0.71% |
| news_api | finance.sina.com.cn | 12 | 0.33% | 0.71% |
| news_api | cointelegraph.com | 11 | 0.30% | 0.65% |
| news_api | el-balad.com | 11 | 0.30% | 0.65% |
| news_api | finanznachrichten.de | 11 | 0.30% | 0.65% |
| news_rss | KrebsOnSecurity | 11 | 0.30% | 6.08% |
| news_api | economictimes.indiatimes.com | 10 | 0.27% | 0.59% |
| news_api | haberler.com | 10 | 0.27% | 0.59% |
| news_api | techcrunch.com | 10 | 0.27% | 0.59% |
| news_api | baijiahao.baidu.com | 9 | 0.24% | 0.53% |
| news_api | csoonline.com | 9 | 0.24% | 0.53% |
| news_api | fool.com | 9 | 0.24% | 0.53% |
| news_api | infosecurity-magazine.com | 9 | 0.24% | 0.53% |
| news_api | timesofindia.indiatimes.com | 9 | 0.24% | 0.53% |
| news_rss | Google Project Zero | 9 | 0.24% | 4.97% |
| news_api | boredpanda.com | 8 | 0.22% | 0.47% |
| news_api | channellife.co.nz | 8 | 0.22% | 0.47% |
| news_api | finance.yahoo.com | 8 | 0.22% | 0.47% |
| news_api | moneycontrol.com | 8 | 0.22% | 0.47% |
| news_api | jdsupra.com | 7 | 0.19% | 0.42% |
| news_api | biz.heraldcorp.com | 6 | 0.16% | 0.36% |
| news_api | edaily.co.kr | 6 | 0.16% | 0.36% |
| news_api | govtech.com | 6 | 0.16% | 0.36% |
| news_api | laopcion.com.mx | 6 | 0.16% | 0.36% |
| news_api | securitylab.ru | 6 | 0.16% | 0.36% |
| news_api | tvguide.co.uk | 6 | 0.16% | 0.36% |
| news_api | udayavani.com | 6 | 0.16% | 0.36% |
| news_api | channellife.com.au | 5 | 0.14% | 0.30% |
| news_api | fnnews.com | 5 | 0.14% | 0.30% |
| news_api | prnewswire.com | 5 | 0.14% | 0.30% |
| news_api | yahoo.com | 5 | 0.14% | 0.30% |
| news_api | 9to5mac.com | 4 | 0.11% | 0.24% |
| news_api | aa.com.tr | 4 | 0.11% | 0.24% |
| news_api | coindesk.com | 4 | 0.11% | 0.24% |
| news_api | computing.co.uk | 4 | 0.11% | 0.24% |
| news_api | ddaily.co.kr | 4 | 0.11% | 0.24% |
| news_api | dostor.org | 4 | 0.11% | 0.24% |
| news_api | eturbonews.com | 4 | 0.11% | 0.24% |
| news_api | excite.co.jp | 4 | 0.11% | 0.24% |
| news_api | foxnews.com | 4 | 0.11% | 0.24% |
| news_api | heise.de | 4 | 0.11% | 0.24% |
| news_api | hothardware.com | 4 | 0.11% | 0.24% |
| news_api | insurancebusinessmag.com | 4 | 0.11% | 0.24% |
| news_api | interfax.ru | 4 | 0.11% | 0.24% |
| news_api | it-online.co.za | 4 | 0.11% | 0.24% |
| news_api | itnews.com.au | 4 | 0.11% | 0.24% |
| news_api | japan.zdnet.com | 4 | 0.11% | 0.24% |
| news_api | kibrispostasi.com | 4 | 0.11% | 0.24% |
| news_api | newjerseytelegraph.com | 4 | 0.11% | 0.24% |
| news_api | pcmag.com | 4 | 0.11% | 0.24% |
| news_api | screenrant.com | 4 | 0.11% | 0.24% |
| news_api | thefastmode.com | 4 | 0.11% | 0.24% |
| news_api | thenews.com.pk | 4 | 0.11% | 0.24% |
| news_api | time.mk | 4 | 0.11% | 0.24% |
| news_api | tn.com.ar | 4 | 0.11% | 0.24% |
| news_api | vz.ru | 4 | 0.11% | 0.24% |
| news_api | winnipegfreepress.com | 4 | 0.11% | 0.24% |
| news_api | zdnet.co.kr | 4 | 0.11% | 0.24% |
| news_api | alltoc.com | 3 | 0.08% | 0.18% |
| news_api | androidauthority.com | 3 | 0.08% | 0.18% |
| news_api | biometricupdate.com | 3 | 0.08% | 0.18% |
| news_api | bleedingcool.com | 3 | 0.08% | 0.18% |
| news_api | business.scoop.co.nz | 3 | 0.08% | 0.18% |
| news_api | cbc.ca | 3 | 0.08% | 0.18% |
| news_api | claimsjournal.com | 3 | 0.08% | 0.18% |
| news_api | cnnturk.com | 3 | 0.08% | 0.18% |
| news_api | defensenews.com | 3 | 0.08% | 0.18% |
| news_api | divyabhaskar.co.in | 3 | 0.08% | 0.18% |
| news_api | donanimgunlugu.com | 3 | 0.08% | 0.18% |
| news_api | ensonhaber.com | 3 | 0.08% | 0.18% |
| news_api | eurointegration.com.ua | 3 | 0.08% | 0.18% |
| news_api | finance.eastmoney.com | 3 | 0.08% | 0.18% |
| news_api | freepressjournal.in | 3 | 0.08% | 0.18% |
| news_api | hindustantimes.com | 3 | 0.08% | 0.18% |
| news_api | iefimerida.gr | 3 | 0.08% | 0.18% |
| news_api | itbusinessnet.com | 3 | 0.08% | 0.18% |
| news_api | itnewsonline.com | 3 | 0.08% | 0.18% |
| news_api | itweb.co.za | 3 | 0.08% | 0.18% |
| news_api | koreaherald.com | 3 | 0.08% | 0.18% |
| news_api | marketscreener.com | 3 | 0.08% | 0.18% |
| news_api | milliyet.com.tr | 3 | 0.08% | 0.18% |
| news_api | miragenews.com | 3 | 0.08% | 0.18% |
| news_api | mondaq.com | 3 | 0.08% | 0.18% |
| news_api | n.yam.com | 3 | 0.08% | 0.18% |
| news_api | natalie.mu | 3 | 0.08% | 0.18% |
| news_api | newswiretoday.com | 3 | 0.08% | 0.18% |
| news_api | odatv.com | 3 | 0.08% | 0.18% |
| news_api | politis.com.cy | 3 | 0.08% | 0.18% |
| news_api | portal.sina.com.hk | 3 | 0.08% | 0.18% |
| news_api | russian.rt.com | 3 | 0.08% | 0.18% |
| news_api | sabah.com.tr | 3 | 0.08% | 0.18% |
| news_api | scoop.co.nz | 3 | 0.08% | 0.18% |
| news_api | shorouknews.com | 3 | 0.08% | 0.18% |
| news_api | straitstimes.com | 3 | 0.08% | 0.18% |
| news_api | theglobeandmail.com | 3 | 0.08% | 0.18% |
| news_api | thenextweb.com | 3 | 0.08% | 0.18% |
| news_api | tomshardware.com | 3 | 0.08% | 0.18% |
| news_api | tribuneindia.com | 3 | 0.08% | 0.18% |
| news_api | ura.news | 3 | 0.08% | 0.18% |
| news_api | wesh.com | 3 | 0.08% | 0.18% |
| news_api | wired.com | 3 | 0.08% | 0.18% |
| news_api | wmur.com | 3 | 0.08% | 0.18% |
| news_api | womannews.net | 3 | 0.08% | 0.18% |
| news_api | 1prime.ru | 2 | 0.05% | 0.12% |
| news_api | aceshowbiz.com | 2 | 0.05% | 0.12% |
| news_api | allafrica.com | 2 | 0.05% | 0.12% |
| news_api | am.com.mx | 2 | 0.05% | 0.12% |
| news_api | americanbanker.com | 2 | 0.05% | 0.12% |
| news_api | androidheadlines.com | 2 | 0.05% | 0.12% |
| news_api | aninews.in | 2 | 0.05% | 0.12% |
| news_api | antaranews.com | 2 | 0.05% | 0.12% |
| news_api | aol.co.uk | 2 | 0.05% | 0.12% |
| news_api | arkansasonline.com | 2 | 0.05% | 0.12% |
| news_api | bankingnews.gr | 2 | 0.05% | 0.12% |
| news_api | bd-pratidin.com | 2 | 0.05% | 0.12% |
| news_api | begeek.fr | 2 | 0.05% | 0.12% |
| news_api | bjnews.com.cn | 2 | 0.05% | 0.12% |
| news_api | bleepingcomputer.com | 2 | 0.05% | 0.12% |
| news_api | boerse-express.com | 2 | 0.05% | 0.12% |
| news_api | bunburymail.com.au | 2 | 0.05% | 0.12% |
| news_api | businessday.co.za | 2 | 0.05% | 0.12% |
| news_api | businessghana.com | 2 | 0.05% | 0.12% |
| news_api | capital.ro | 2 | 0.05% | 0.12% |
| news_api | cloud.watch.impress.co.jp | 2 | 0.05% | 0.12% |
| news_api | comnews.ru | 2 | 0.05% | 0.12% |
| news_api | computerweekly.com | 2 | 0.05% | 0.12% |
| news_api | daily.com.ua | 2 | 0.05% | 0.12% |
| news_api | dailybreeze.com | 2 | 0.05% | 0.12% |
| news_api | dailykos.com | 2 | 0.05% | 0.12% |
| news_api | dailynews.com | 2 | 0.05% | 0.12% |
| news_api | danas.rs | 2 | 0.05% | 0.12% |
| news_api | deadline.com | 2 | 0.05% | 0.12% |
| news_api | diariosur.es | 2 | 0.05% | 0.12% |
| news_api | digitaljournal.com | 2 | 0.05% | 0.12% |
| news_api | ecodibergamo.it | 2 | 0.05% | 0.12% |
| news_api | ecodisicilia.com | 2 | 0.05% | 0.12% |
| news_api | ecommercenews.co.nz | 2 | 0.05% | 0.12% |
| news_api | eldestapeweb.com | 2 | 0.05% | 0.12% |
| news_api | eldia.com.bo | 2 | 0.05% | 0.12% |
| news_api | eldiariodechihuahua.mx | 2 | 0.05% | 0.12% |
| news_api | elmanana.com | 2 | 0.05% | 0.12% |
| news_api | etoday.co.kr | 2 | 0.05% | 0.12% |
| news_api | europapress.es | 2 | 0.05% | 0.12% |
| news_api | europesun.com | 2 | 0.05% | 0.12% |
| news_api | evrensel.net | 2 | 0.05% | 0.12% |
| news_api | fontanka.ru | 2 | 0.05% | 0.12% |
| news_api | fox4news.com | 2 | 0.05% | 0.12% |
| news_api | freemalaysiatoday.com | 2 | 0.05% | 0.12% |
| news_api | gdnonline.com | 2 | 0.05% | 0.12% |
| news_api | geeky-gadgets.com | 2 | 0.05% | 0.12% |
| news_api | ghanamma.com | 2 | 0.05% | 0.12% |
| news_api | github.com | 2 | 0.05% | 0.12% |
| news_api | gizmodo.com | 2 | 0.05% | 0.12% |
| news_api | glavcom.ua | 2 | 0.05% | 0.12% |
| news_api | globalnews.ca | 2 | 0.05% | 0.12% |
| news_api | greeleytribune.com | 2 | 0.05% | 0.12% |
| news_api | hawaiitelegraph.com | 2 | 0.05% | 0.12% |
| news_api | heraldk.com | 2 | 0.05% | 0.12% |
| news_api | hindi.webdunia.com | 2 | 0.05% | 0.12% |
| news_api | hinews.cn | 2 | 0.05% | 0.12% |
| news_api | hollywoodreporter.com | 2 | 0.05% | 0.12% |
| news_api | htxt.co.za | 2 | 0.05% | 0.12% |
| news_api | hurriyetdailynews.com | 2 | 0.05% | 0.12% |
| news_api | index.hr | 2 | 0.05% | 0.12% |
| news_api | inewsgr.com | 2 | 0.05% | 0.12% |
| news_api | inforum.com | 2 | 0.05% | 0.12% |
| news_api | infoworld.com | 2 | 0.05% | 0.12% |
| news_api | insideottawavalley.com | 2 | 0.05% | 0.12% |
| news_api | insight.co.kr | 2 | 0.05% | 0.12% |
| news_api | insurancejournal.com | 2 | 0.05% | 0.12% |
| news_api | investegate.co.uk | 2 | 0.05% | 0.12% |
| news_api | irishdentist.ie | 2 | 0.05% | 0.12% |
| news_api | itbear.com.cn | 2 | 0.05% | 0.12% |
| news_api | itwire.com | 2 | 0.05% | 0.12% |
| news_api | iz.ru | 2 | 0.05% | 0.12% |
| news_api | jawapos.com | 2 | 0.05% | 0.12% |
| news_api | jpost.com | 2 | 0.05% | 0.12% |
| news_api | jugantor.com | 2 | 0.05% | 0.12% |
| news_api | kathimerini.com.cy | 2 | 0.05% | 0.12% |
| news_api | kommersant.ru | 2 | 0.05% | 0.12% |
| news_api | kten.com | 2 | 0.05% | 0.12% |
| news_api | lalsace.fr | 2 | 0.05% | 0.12% |
| news_api | lbc.co.uk | 2 | 0.05% | 0.12% |
| news_api | lefigaro.fr | 2 | 0.05% | 0.12% |
| news_api | libnanews.com | 2 | 0.05% | 0.12% |
| news_api | life.ru | 2 | 0.05% | 0.12% |
| news_api | livenews.co.nz | 2 | 0.05% | 0.12% |
| news_api | lrytas.lt | 2 | 0.05% | 0.12% |
| news_api | macleayargus.com.au | 2 | 0.05% | 0.12% |
| news_api | mainichi.jp | 2 | 0.05% | 0.12% |
| news_api | makeuseof.com | 2 | 0.05% | 0.12% |
| news_api | maliactu.net | 2 | 0.05% | 0.12% |
| news_api | massachusettssun.com | 2 | 0.05% | 0.12% |
| news_api | medianama.com | 2 | 0.05% | 0.12% |
| news_api | military.china.com | 2 | 0.05% | 0.12% |
| news_api | morningstar.com | 2 | 0.05% | 0.12% |
| news_api | naftemporiki.gr | 2 | 0.05% | 0.12% |
| news_api | natlawreview.com | 2 | 0.05% | 0.12% |
| news_api | newkerala.com | 2 | 0.05% | 0.12% |
| news_api | newratings.de | 2 | 0.05% | 0.12% |
| news_api | news.cn | 2 | 0.05% | 0.12% |
| news_api | newspim.com | 2 | 0.05% | 0.12% |
| news_api | ntdtv.com | 2 | 0.05% | 0.12% |
| news_api | nvi.com.au | 2 | 0.05% | 0.12% |
| news_api | nypost.com | 2 | 0.05% | 0.12% |
| news_api | nzherald.co.nz | 2 | 0.05% | 0.12% |
| news_api | phonandroid.com | 2 | 0.05% | 0.12% |
| news_api | politika.rs | 2 | 0.05% | 0.12% |
| news_api | posta.com.tr | 2 | 0.05% | 0.12% |
| news_api | pravda.ru | 2 | 0.05% | 0.12% |
| news_api | propakistani.pk | 2 | 0.05% | 0.12% |
| news_api | punchng.com | 2 | 0.05% | 0.12% |
| news_api | pymnts.com | 2 | 0.05% | 0.12% |
| news_api | rediff.com | 2 | 0.05% | 0.12% |
| news_api | rpp.pe | 2 | 0.05% | 0.12% |
| news_api | sanantoniopost.com | 2 | 0.05% | 0.12% |
| news_api | sb.by | 2 | 0.05% | 0.12% |
| news_api | securitybrief.news | 2 | 0.05% | 0.12% |
| news_api | securityinfowatch.com | 2 | 0.05% | 0.12% |
| news_api | segye.com | 2 | 0.05% | 0.12% |
| news_api | sentinel.ht | 2 | 0.05% | 0.12% |
| news_api | sgvtribune.com | 2 | 0.05% | 0.12% |
| news_api | stcn.com | 2 | 0.05% | 0.12% |
| news_api | t-online.de | 2 | 0.05% | 0.12% |
| news_api | tech.caijing.com.cn | 2 | 0.05% | 0.12% |
| news_api | tech.ifeng.com | 2 | 0.05% | 0.12% |
| news_api | techweez.com | 2 | 0.05% | 0.12% |
| news_api | tennesseedaily.com | 2 | 0.05% | 0.12% |
| news_api | thehindu.com | 2 | 0.05% | 0.12% |
| news_api | thesun.ng | 2 | 0.05% | 0.12% |
| news_api | thisdaylive.com | 2 | 0.05% | 0.12% |
| news_api | tmtpost.com | 2 | 0.05% | 0.12% |
| news_api | trthaber.com | 2 | 0.05% | 0.12% |
| news_api | uainfo.org | 2 | 0.05% | 0.12% |
| news_api | unian.net | 2 | 0.05% | 0.12% |
| news_api | unn.ua | 2 | 0.05% | 0.12% |
| news_api | unternehmen-heute.de | 2 | 0.05% | 0.12% |
| news_api | vedomosti.ru | 2 | 0.05% | 0.12% |
| news_api | vesti.ru | 2 | 0.05% | 0.12% |
| news_api | vg.no | 2 | 0.05% | 0.12% |
| news_api | vietnamnet.vn | 2 | 0.05% | 0.12% |
| news_api | wbaltv.com | 2 | 0.05% | 0.12% |
| news_api | wdrb.com | 2 | 0.05% | 0.12% |
| news_api | webpronews.com | 2 | 0.05% | 0.12% |
| news_api | welivesecurity.com | 2 | 0.05% | 0.12% |
| news_api | weser-kurier.de | 2 | 0.05% | 0.12% |
| news_api | wfmz.com | 2 | 0.05% | 0.12% |
| news_api | wiwo.de | 2 | 0.05% | 0.12% |
| news_api | wsbtv.com | 2 | 0.05% | 0.12% |
| news_api | wzzm13.com | 2 | 0.05% | 0.12% |
| news_api | y-mainichi.co.jp | 2 | 0.05% | 0.12% |
| news_api | 01net.com | 1 | 0.03% | 0.06% |
| news_api | 1015vibe.com | 1 | 0.03% | 0.06% |
| news_api | 1055thedove.com | 1 | 0.03% | 0.06% |
| news_api | 10tv.com | 1 | 0.03% | 0.06% |
| news_api | 21stcenturywire.com | 1 | 0.03% | 0.06% |
| news_api | 24sata.hr | 1 | 0.03% | 0.06% |
| news_api | 3c.ltn.com.tw | 1 | 0.03% | 0.06% |
| news_api | 5.ua | 1 | 0.03% | 0.06% |
| news_api | 5newsonline.com | 1 | 0.03% | 0.06% |
| news_api | 961theeagle.com | 1 | 0.03% | 0.06% |
| news_api | 985thefox.iheart.com | 1 | 0.03% | 0.06% |
| news_api | 995thefox.iheart.com | 1 | 0.03% | 0.06% |
| news_api | 99jamzmiami.com | 1 | 0.03% | 0.06% |
| news_api | abc7news.com | 1 | 0.03% | 0.06% |
| news_api | abovethelaw.com | 1 | 0.03% | 0.06% |
| news_api | actionnewsjax.com | 1 | 0.03% | 0.06% |
| news_api | adevarul.ro | 1 | 0.03% | 0.06% |
| news_api | administradores.com.br | 1 | 0.03% | 0.06% |
| news_api | afr.com | 1 | 0.03% | 0.06% |
| news_api | ai.zol.com.cn | 1 | 0.03% | 0.06% |
| news_api | aif.ru | 1 | 0.03% | 0.06% |
| news_api | aktifhaber.com | 1 | 0.03% | 0.06% |
| news_api | aktivni.metropolitan.si | 1 | 0.03% | 0.06% |
| news_api | al-monitor.com | 1 | 0.03% | 0.06% |
| news_api | alanbatnews.net | 1 | 0.03% | 0.06% |
| news_api | alaskasnewssource.com | 1 | 0.03% | 0.06% |
| news_api | aliran.com | 1 | 0.03% | 0.06% |
| news_api | aljazeera.com | 1 | 0.03% | 0.06% |
| news_api | aljazeera.net | 1 | 0.03% | 0.06% |
| news_api | alquds.co.uk | 1 | 0.03% | 0.06% |
| news_api | amic.ru | 1 | 0.03% | 0.06% |
| news_api | antena3.ro | 1 | 0.03% | 0.06% |
| news_api | antivirus-sniper.macupdate.com | 1 | 0.03% | 0.06% |
| news_api | arabherald.com | 1 | 0.03% | 0.06% |
| news_api | arede.info | 1 | 0.03% | 0.06% |
| news_api | aristeguinoticias.com | 1 | 0.03% | 0.06% |
| news_api | armenews.com | 1 | 0.03% | 0.06% |
| news_api | armidaleexpress.com.au | 1 | 0.03% | 0.06% |
| news_api | arstechnica.com | 1 | 0.03% | 0.06% |
| news_api | asahi.com | 1 | 0.03% | 0.06% |
| news_api | asianews.it | 1 | 0.03% | 0.06% |
| news_api | aspentimes.com | 1 | 0.03% | 0.06% |
| news_api | astroawani.com | 1 | 0.03% | 0.06% |
| news_api | austinchronicle.com | 1 | 0.03% | 0.06% |
| news_api | austinglobe.com | 1 | 0.03% | 0.06% |
| news_api | autoexpress.co.uk | 1 | 0.03% | 0.06% |
| news_api | b985.com | 1 | 0.03% | 0.06% |
| news_api | balkanweb.com | 1 | 0.03% | 0.06% |
| news_api | bandaancha.eu | 1 | 0.03% | 0.06% |
| news_api | bangkokbiznews.com | 1 | 0.03% | 0.06% |
| news_api | bangkokpost.com | 1 | 0.03% | 0.06% |
| news_api | bangordailynews.com | 1 | 0.03% | 0.06% |
| news_api | bankier.pl | 1 | 0.03% | 0.06% |
| news_api | batemansbaypost.com.au | 1 | 0.03% | 0.06% |
| news_api | batonrougepost.com | 1 | 0.03% | 0.06% |
| news_api | bbc.com | 1 | 0.03% | 0.06% |
| news_api | beckershospitalreview.com | 1 | 0.03% | 0.06% |
| news_api | berliner-zeitung.de | 1 | 0.03% | 0.06% |
| news_api | bernerzeitung.ch | 1 | 0.03% | 0.06% |
| news_api | bfmtv.com | 1 | 0.03% | 0.06% |
| news_api | bgonair.bg | 1 | 0.03% | 0.06% |
| news_api | bgr.com | 1 | 0.03% | 0.06% |
| news_api | bhaskar.com | 1 | 0.03% | 0.06% |
| news_api | bianet.org | 1 | 0.03% | 0.06% |
| news_api | bignewsnetwork.com | 1 | 0.03% | 0.06% |
| news_api | bigpara.hurriyet.com.tr | 1 | 0.03% | 0.06% |
| news_api | birminghamstar.com | 1 | 0.03% | 0.06% |
| news_api | biz.cnews.ru | 1 | 0.03% | 0.06% |
| news_api | bj.xinhuanet.com | 1 | 0.03% | 0.06% |
| news_api | blackseanews.net | 1 | 0.03% | 0.06% |
| news_api | blikk.hu | 1 | 0.03% | 0.06% |
| news_api | blog.wenxuecity.com | 1 | 0.03% | 0.06% |
| news_api | blogs.diariovasco.com | 1 | 0.03% | 0.06% |
| news_api | blogs.itmedia.co.jp | 1 | 0.03% | 0.06% |
| news_api | bluemountainsgazette.com.au | 1 | 0.03% | 0.06% |
| news_api | bmmagazine.co.uk | 1 | 0.03% | 0.06% |
| news_api | bollywoodlife.com | 1 | 0.03% | 0.06% |
| news_api | borsonline.hu | 1 | 0.03% | 0.06% |
| news_api | bostonherald.com | 1 | 0.03% | 0.06% |
| news_api | botasot.info | 1 | 0.03% | 0.06% |
| news_api | bozemandailychronicle.com | 1 | 0.03% | 0.06% |
| news_api | braidwoodtimes.com.au | 1 | 0.03% | 0.06% |
| news_api | brandonsun.com | 1 | 0.03% | 0.06% |
| news_api | brasil247.com | 1 | 0.03% | 0.06% |
| news_api | brisbanetimes.com.au | 1 | 0.03% | 0.06% |
| news_api | brooklyneagle.com | 1 | 0.03% | 0.06% |
| news_api | bt.no | 1 | 0.03% | 0.06% |
| news_api | buffalobulletin.com | 1 | 0.03% | 0.06% |
| news_api | bug.hr | 1 | 0.03% | 0.06% |
| news_api | bursahakimiyet.com.tr | 1 | 0.03% | 0.06% |
| news_api | business24.ro | 1 | 0.03% | 0.06% |
| news_api | business2community.com | 1 | 0.03% | 0.06% |
| news_api | businessinsurance.com | 1 | 0.03% | 0.06% |
| news_api | businesstimes.com.sg | 1 | 0.03% | 0.06% |
| news_api | businesstoday.in | 1 | 0.03% | 0.06% |
| news_api | businessworld.in | 1 | 0.03% | 0.06% |
| news_api | c101.iheart.com | 1 | 0.03% | 0.06% |
| news_api | cafebiz.vn | 1 | 0.03% | 0.06% |
| news_api | californiatelegraph.com | 1 | 0.03% | 0.06% |
| news_api | cambridgetimes.ca | 1 | 0.03% | 0.06% |
| news_api | camdencourier.com.au | 1 | 0.03% | 0.06% |
| news_api | canardpc.com | 1 | 0.03% | 0.06% |
| news_api | carolinajournal.com | 1 | 0.03% | 0.06% |
| news_api | cas.sk | 1 | 0.03% | 0.06% |
| news_api | castanetkamloops.net | 1 | 0.03% | 0.06% |
| news_api | cepro.com | 1 | 0.03% | 0.06% |
| news_api | cfi.net.cn | 1 | 0.03% | 0.06% |
| news_api | channelbuzz.ca | 1 | 0.03% | 0.06% |
| news_api | china.com.cn | 1 | 0.03% | 0.06% |
| news_api | chinanationalnews.com | 1 | 0.03% | 0.06% |
| news_api | chinapress.com.my | 1 | 0.03% | 0.06% |
| news_api | chinesepress.com | 1 | 0.03% | 0.06% |
| news_api | chip.de | 1 | 0.03% | 0.06% |
| news_api | choice.com.au | 1 | 0.03% | 0.06% |
| news_api | cincinnatisun.com | 1 | 0.03% | 0.06% |
| news_api | circleid.com | 1 | 0.03% | 0.06% |
| news_api | cjme.com | 1 | 0.03% | 0.06% |
| news_api | clarin.com | 1 | 0.03% | 0.06% |
| news_api | closermag.fr | 1 | 0.03% | 0.06% |
| news_api | clydebankpost.co.uk | 1 | 0.03% | 0.06% |
| news_api | cnet.com | 1 | 0.03% | 0.06% |
| news_api | cnn.com | 1 | 0.03% | 0.06% |
| news_api | collider.com | 1 | 0.03% | 0.06% |
| news_api | coloradostar.com | 1 | 0.03% | 0.06% |
| news_api | comingsoon.it | 1 | 0.03% | 0.06% |
| news_api | computerwoche.de | 1 | 0.03% | 0.06% |
| news_api | computerworld.dk | 1 | 0.03% | 0.06% |
| news_api | computerworld.pl | 1 | 0.03% | 0.06% |
| news_api | cootamundraherald.com.au | 1 | 0.03% | 0.06% |
| news_api | corp.cnews.ru | 1 | 0.03% | 0.06% |
| news_api | corriereadriatico.it | 1 | 0.03% | 0.06% |
| news_api | countercurrents.org | 1 | 0.03% | 0.06% |
| news_api | cp24.com | 1 | 0.03% | 0.06% |
| news_api | crookwellgazette.com.au | 1 | 0.03% | 0.06% |
| news_api | dagensps.se | 1 | 0.03% | 0.06% |
| news_api | daily-tribune.com | 1 | 0.03% | 0.06% |
| news_api | dailyadvertiser.com.au | 1 | 0.03% | 0.06% |
| news_api | dailyemerald.com | 1 | 0.03% | 0.06% |
| news_api | dailyexcelsior.com | 1 | 0.03% | 0.06% |
| news_api | dailyinqilab.com | 1 | 0.03% | 0.06% |
| news_api | dailyjournalonline.com | 1 | 0.03% | 0.06% |
| news_api | dailymail.co.uk | 1 | 0.03% | 0.06% |
| news_api | dailymail.com | 1 | 0.03% | 0.06% |
| news_api | dailynews.co.th | 1 | 0.03% | 0.06% |
| news_api | dailypakistan.pk | 1 | 0.03% | 0.06% |
| news_api | dailypioneer.com | 1 | 0.03% | 0.06% |
| news_api | dailypolitical.com | 1 | 0.03% | 0.06% |
| news_api | dailysabah.com | 1 | 0.03% | 0.06% |
| news_api | dailytrust.com | 1 | 0.03% | 0.06% |
| news_api | dailyuw.com | 1 | 0.03% | 0.06% |
| news_api | damernasvarld.expressen.se | 1 | 0.03% | 0.06% |
| news_api | dantri.com.vn | 1 | 0.03% | 0.06% |
| news_api | datacenterknowledge.com | 1 | 0.03% | 0.06% |
| news_api | daytondailynews.com | 1 | 0.03% | 0.06% |
| news_api | dcvelocity.com | 1 | 0.03% | 0.06% |
| news_api | de.nachrichten.yahoo.com | 1 | 0.03% | 0.06% |
| news_api | deperu.com | 1 | 0.03% | 0.06% |
| news_api | designboom.com | 1 | 0.03% | 0.06% |
| news_api | dglobe.com | 1 | 0.03% | 0.06% |
| news_api | dha.com.tr | 1 | 0.03% | 0.06% |
| news_api | diario.mx | 1 | 0.03% | 0.06% |
| news_api | diariodeburgos.es | 1 | 0.03% | 0.06% |
| news_api | diariodemorelos.com | 1 | 0.03% | 0.06% |
| news_api | diariopalentino.es | 1 | 0.03% | 0.06% |
| news_api | diena.lt | 1 | 0.03% | 0.06% |
| news_api | digg.com | 1 | 0.03% | 0.06% |
| news_api | digi.china.com | 1 | 0.03% | 0.06% |
| news_api | digi24.ro | 1 | 0.03% | 0.06% |
| news_api | digitaltrends.com | 1 | 0.03% | 0.06% |
| news_api | directionsmag.com | 1 | 0.03% | 0.06% |
| news_api | divyamarathi.bhaskar.com | 1 | 0.03% | 0.06% |
| news_api | diyarbakirsoz.com | 1 | 0.03% | 0.06% |
| news_api | dna.fr | 1 | 0.03% | 0.06% |
| news_api | dnews.gr | 1 | 0.03% | 0.06% |
| news_api | dol.com.br | 1 | 0.03% | 0.06% |
| news_api | dominicanrepublicpost.com | 1 | 0.03% | 0.06% |
| news_api | donanimhaber.com | 1 | 0.03% | 0.06% |
| news_api | donews.com | 1 | 0.03% | 0.06% |
| news_api | dotekomanie.cz | 1 | 0.03% | 0.06% |
| news_api | downtoearth.org.in | 1 | 0.03% | 0.06% |
| news_api | dp.ru | 1 | 0.03% | 0.06% |
| news_api | drimble.nl | 1 | 0.03% | 0.06% |
| news_api | dunya.com | 1 | 0.03% | 0.06% |
| news_api | dunyanews.tv | 1 | 0.03% | 0.06% |
| news_api | dw.com | 1 | 0.03% | 0.06% |
| news_api | dynamicbusiness.com | 1 | 0.03% | 0.06% |
| news_api | eadt.co.uk | 1 | 0.03% | 0.06% |
| news_api | eagledayton.com | 1 | 0.03% | 0.06% |
| news_api | eaglesanantonio.com | 1 | 0.03% | 0.06% |
| news_api | ec.ltn.com.tw | 1 | 0.03% | 0.06% |
| news_api | echopress.com | 1 | 0.03% | 0.06% |
| news_api | economx.hu | 1 | 0.03% | 0.06% |
| news_api | econotimes.com | 1 | 0.03% | 0.06% |
| news_api | edition.cnn.com | 1 | 0.03% | 0.06% |
| news_api | eejournal.com | 1 | 0.03% | 0.06% |
| news_api | elcomercio.es | 1 | 0.03% | 0.06% |
| news_api | elconfidencial.com | 1 | 0.03% | 0.06% |
| news_api | eldia.es | 1 | 0.03% | 0.06% |
| news_api | eleco.com.ar | 1 | 0.03% | 0.06% |
| news_api | elektroniknet.de | 1 | 0.03% | 0.06% |
| news_api | elmalaeb.com | 1 | 0.03% | 0.06% |
| news_api | elpais.com | 1 | 0.03% | 0.06% |
| news_api | elpais.com.uy | 1 | 0.03% | 0.06% |
| news_api | elperiodicodearagon.com | 1 | 0.03% | 0.06% |
| news_api | elsiglodetorreon.com.mx | 1 | 0.03% | 0.06% |
| news_api | eluniversal.com.mx | 1 | 0.03% | 0.06% |
| news_api | eluniverso.com | 1 | 0.03% | 0.06% |
| news_api | elwatannews.com | 1 | 0.03% | 0.06% |
| news_api | english.pravda.ru | 1 | 0.03% | 0.06% |
| news_api | estadao.com.br | 1 | 0.03% | 0.06% |
| news_api | etnews.com | 1 | 0.03% | 0.06% |
| news_api | ettoday.net | 1 | 0.03% | 0.06% |
| news_api | explosion.com | 1 | 0.03% | 0.06% |
| news_api | express.pk | 1 | 0.03% | 0.06% |
| news_api | extra.ec | 1 | 0.03% | 0.06% |
| news_api | f1vilag.hu | 1 | 0.03% | 0.06% |
| news_api | fakti.bg | 1 | 0.03% | 0.06% |
| news_api | fatimanews.com.br | 1 | 0.03% | 0.06% |
| news_api | fedpress.ru | 1 | 0.03% | 0.06% |
| news_api | femina.hu | 1 | 0.03% | 0.06% |
| news_api | filmfare.com | 1 | 0.03% | 0.06% |
| news_api | finance.ifeng.com | 1 | 0.03% | 0.06% |
| news_api | financial-news.co.uk | 1 | 0.03% | 0.06% |
| news_api | financialafrik.com | 1 | 0.03% | 0.06% |
| news_api | finans.mynet.com | 1 | 0.03% | 0.06% |
| news_api | firstpost.com | 1 | 0.03% | 0.06% |
| news_api | floridastatesman.com | 1 | 0.03% | 0.06% |
| news_api | fnp.de | 1 | 0.03% | 0.06% |
| news_api | focus.ua | 1 | 0.03% | 0.06% |
| news_api | fox17online.com | 1 | 0.03% | 0.06% |
| news_api | fox43.com | 1 | 0.03% | 0.06% |
| news_api | fox9.com | 1 | 0.03% | 0.06% |
| news_api | francetoday.com | 1 | 0.03% | 0.06% |
| news_api | freiepresse.de | 1 | 0.03% | 0.06% |
| news_api | french.china.org.cn | 1 | 0.03% | 0.06% |
| news_api | funkytaurusmedia.com | 1 | 0.03% | 0.06% |
| news_api | futures.cnfol.com | 1 | 0.03% | 0.06% |
| news_api | gadgetsmagazine.com.ph | 1 | 0.03% | 0.06% |
| news_api | gamerant.com | 1 | 0.03% | 0.06% |
| news_api | gamestar.de | 1 | 0.03% | 0.06% |
| news_api | generation-nt.com | 1 | 0.03% | 0.06% |
| news_api | georgeherald.com | 1 | 0.03% | 0.06% |
| news_api | german.china.org.cn | 1 | 0.03% | 0.06% |
| news_api | ghanaiantimes.com.gh | 1 | 0.03% | 0.06% |
| news_api | gipedo.politis.com.cy | 1 | 0.03% | 0.06% |
| news_api | golosarmenii.am | 1 | 0.03% | 0.06% |
| news_api | gorod48.ru | 1 | 0.03% | 0.06% |
| news_api | governing.com | 1 | 0.03% | 0.06% |
| news_api | greekherald.com | 1 | 0.03% | 0.06% |
| news_api | groundup.org.za | 1 | 0.03% | 0.06% |
| news_api | gulte.com | 1 | 0.03% | 0.06% |
| news_api | haber1.com | 1 | 0.03% | 0.06% |
| news_api | haber3.com | 1 | 0.03% | 0.06% |
| news_api | haberturk.com | 1 | 0.03% | 0.06% |
| news_api | hachettebookgroup.com | 1 | 0.03% | 0.06% |
| news_api | haksozhaber.net | 1 | 0.03% | 0.06% |
| news_api | handelsblatt.com | 1 | 0.03% | 0.06% |
| news_api | hani.co.kr | 1 | 0.03% | 0.06% |
| news_api | helpconsumatori.it | 1 | 0.03% | 0.06% |
| news_api | hespress.com | 1 | 0.03% | 0.06% |
| news_api | heute.at | 1 | 0.03% | 0.06% |
| news_api | hirek.prim.hu | 1 | 0.03% | 0.06% |
| news_api | hits1053sanantonio.com | 1 | 0.03% | 0.06% |
| news_api | hits973.com | 1 | 0.03% | 0.06% |
| news_api | hokkoku.co.jp | 1 | 0.03% | 0.06% |
| news_api | hoy.es | 1 | 0.03% | 0.06% |
| news_api | hydrocarbonprocessing.com | 1 | 0.03% | 0.06% |
| news_api | ibtimes.co.uk | 1 | 0.03% | 0.06% |
| news_api | ibtimes.com.au | 1 | 0.03% | 0.06% |
| news_api | ici.fr | 1 | 0.03% | 0.06% |
| news_api | icij.org | 1 | 0.03% | 0.06% |
| news_api | idiva.com | 1 | 0.03% | 0.06% |
| news_api | idnes.cz | 1 | 0.03% | 0.06% |
| news_api | idrw.org | 1 | 0.03% | 0.06% |
| news_api | igamingbusiness.com | 1 | 0.03% | 0.06% |
| news_api | ihalla.com | 1 | 0.03% | 0.06% |
| news_api | illawarramercury.com.au | 1 | 0.03% | 0.06% |
| news_api | independent.co.uk | 1 | 0.03% | 0.06% |
| news_api | index.hu | 1 | 0.03% | 0.06% |
| news_api | india.com | 1 | 0.03% | 0.06% |
| news_api | indiatvnews.com | 1 | 0.03% | 0.06% |
| news_api | inews24.com | 1 | 0.03% | 0.06% |
| news_api | infobae.com | 1 | 0.03% | 0.06% |
| news_api | informationweek.com | 1 | 0.03% | 0.06% |
| news_api | infotechlead.com | 1 | 0.03% | 0.06% |
| news_api | inosmi.ru | 1 | 0.03% | 0.06% |
| news_api | inquirer.com | 1 | 0.03% | 0.06% |
| news_api | insidermonkey.com | 1 | 0.03% | 0.06% |
| news_api | insight.scmagazineuk.com | 1 | 0.03% | 0.06% |
| news_api | interaksyon.philstar.com | 1 | 0.03% | 0.06% |
| news_api | internasional.kompas.com | 1 | 0.03% | 0.06% |
| news_api | internetua.com | 1 | 0.03% | 0.06% |
| news_api | inverelltimes.com.au | 1 | 0.03% | 0.06% |
| news_api | investorplace.com | 1 | 0.03% | 0.06% |
| news_api | inwestycje.pl | 1 | 0.03% | 0.06% |
| news_api | iraqsun.com | 1 | 0.03% | 0.06% |
| news_api | irishtimes.com | 1 | 0.03% | 0.06% |
| news_api | island.lk | 1 | 0.03% | 0.06% |
| news_api | israelherald.com | 1 | 0.03% | 0.06% |
| news_api | it.euronews.com | 1 | 0.03% | 0.06% |
| news_api | itbrief.news | 1 | 0.03% | 0.06% |
| news_api | itnewsafrica.com | 1 | 0.03% | 0.06% |
| news_api | jabar.tribunnews.com | 1 | 0.03% | 0.06% |
| news_api | jagranjosh.com | 1 | 0.03% | 0.06% |
| news_api | jamaicaobserver.com | 1 | 0.03% | 0.06% |
| news_api | jamestown.org | 1 | 0.03% | 0.06% |
| news_api | japan.cnet.com | 1 | 0.03% | 0.06% |
| news_api | japanherald.com | 1 | 0.03% | 0.06% |
| news_api | jeuneafrique.com | 1 | 0.03% | 0.06% |
| news_api | jo24.net | 1 | 0.03% | 0.06% |
| news_api | jogja.tribunnews.com | 1 | 0.03% | 0.06% |
| news_api | jogjapolitan.harianjogja.com | 1 | 0.03% | 0.06% |
| news_api | journal-news.com | 1 | 0.03% | 0.06% |
| news_api | journaldunet.com | 1 | 0.03% | 0.06% |
| news_api | journalgazette.net | 1 | 0.03% | 0.06% |
| news_api | jowhar.com | 1 | 0.03% | 0.06% |
| news_api | jpnn.com | 1 | 0.03% | 0.06% |
| news_api | juneesoutherncross.com.au | 1 | 0.03% | 0.06% |
| news_api | k991fm.com | 1 | 0.03% | 0.06% |
| news_api | kannadaprabha.com | 1 | 0.03% | 0.06% |
| news_api | kaos911.com | 1 | 0.03% | 0.06% |
| news_api | kcci.com | 1 | 0.03% | 0.06% |
| news_api | kesq.com | 1 | 0.03% | 0.06% |
| news_api | king5.com | 1 | 0.03% | 0.06% |
| news_api | kingfm.com | 1 | 0.03% | 0.06% |
| news_api | kiplinger.com | 1 | 0.03% | 0.06% |
| news_api | kiro7.com | 1 | 0.03% | 0.06% |
| news_api | kissrocks.com | 1 | 0.03% | 0.06% |
| news_api | kmbc.com | 1 | 0.03% | 0.06% |
| news_api | kmib.co.kr | 1 | 0.03% | 0.06% |
| news_api | ko.com.ua | 1 | 0.03% | 0.06% |
| news_api | kob.com | 1 | 0.03% | 0.06% |
| news_api | kocaeligazetesi.com.tr | 1 | 0.03% | 0.06% |
| news_api | koco.com | 1 | 0.03% | 0.06% |
| news_api | kono1011.com | 1 | 0.03% | 0.06% |
| news_api | kontrakty.ua | 1 | 0.03% | 0.06% |
| news_api | koreatimes.co.kr | 1 | 0.03% | 0.06% |
| news_api | kotaku.com | 1 | 0.03% | 0.06% |
| news_api | kristv.com | 1 | 0.03% | 0.06% |
| news_api | ktvu.com | 1 | 0.03% | 0.06% |
| news_api | kwcdcountry.com | 1 | 0.03% | 0.06% |
| news_api | kztv10.com | 1 | 0.03% | 0.06% |
| news_api | labs.watchtowr.com | 1 | 0.03% | 0.06% |
| news_api | lafranceagricole.fr | 1 | 0.03% | 0.06% |
| news_api | lagacetadesalamanca.es | 1 | 0.03% | 0.06% |
| news_api | lakersnation.com | 1 | 0.03% | 0.06% |
| news_api | laleggepertutti.it | 1 | 0.03% | 0.06% |
| news_api | laosnews.net | 1 | 0.03% | 0.06% |
| news_api | laprovincia.es | 1 | 0.03% | 0.06% |
| news_api | larazon.es | 1 | 0.03% | 0.06% |
| news_api | larepubliquedespyrenees.fr | 1 | 0.03% | 0.06% |
| news_api | latele.ch | 1 | 0.03% | 0.06% |
| news_api | laut.de | 1 | 0.03% | 0.06% |
| news_api | lavozdegalicia.es | 1 | 0.03% | 0.06% |
| news_api | ledauphine.com | 1 | 0.03% | 0.06% |
| news_api | legalinsurrection.com | 1 | 0.03% | 0.06% |
| news_api | leiphone.com | 1 | 0.03% | 0.06% |
| news_api | lejsl.com | 1 | 0.03% | 0.06% |
| news_api | lelezard.com | 1 | 0.03% | 0.06% |
| news_api | lenta.ru | 1 | 0.03% | 0.06% |
| news_api | lesmobiles.com | 1 | 0.03% | 0.06% |
| news_api | lexpress.fr | 1 | 0.03% | 0.06% |
| news_api | lgz.ru | 1 | 0.03% | 0.06% |
| news_api | liberta.it | 1 | 0.03% | 0.06% |
| news_api | lina.sh | 1 | 0.03% | 0.06% |
| news_api | linux.org.ru | 1 | 0.03% | 0.06% |
| news_api | liputan6.com | 1 | 0.03% | 0.06% |
| news_api | lite987.com | 1 | 0.03% | 0.06% |
| news_api | lithgowmercury.com.au | 1 | 0.03% | 0.06% |
| news_api | livehindustan.com | 1 | 0.03% | 0.06% |
| news_api | livemint.com | 1 | 0.03% | 0.06% |
| news_api | local12.com | 1 | 0.03% | 0.06% |
| news_api | localnews8.com | 1 | 0.03% | 0.06% |
| news_api | loksatta.com | 1 | 0.03% | 0.06% |
| news_api | londonlovesbusiness.com | 1 | 0.03% | 0.06% |
| news_api | ly.fjsen.com | 1 | 0.03% | 0.06% |
| news_api | mactech.com | 1 | 0.03% | 0.06% |
| news_api | magic1021.com | 1 | 0.03% | 0.06% |
| news_api | maharashtratimes.com | 1 | 0.03% | 0.06% |
| news_api | makaangola.org | 1 | 0.03% | 0.06% |
| news_api | makassar.tribunnews.com | 1 | 0.03% | 0.06% |
| news_api | mandurahmail.com.au | 1 | 0.03% | 0.06% |
| news_api | manningrivertimes.com.au | 1 | 0.03% | 0.06% |
| news_api | marca.com | 1 | 0.03% | 0.06% |
| news_api | mariettatimes.com | 1 | 0.03% | 0.06% |
| news_api | marketintelligencecenter.com | 1 | 0.03% | 0.06% |
| news_api | mashable.com | 1 | 0.03% | 0.06% |
| news_api | mathrubhumi.com | 1 | 0.03% | 0.06% |
| news_api | mdjonline.com | 1 | 0.03% | 0.06% |
| news_api | mebpersonel.com | 1 | 0.03% | 0.06% |
| news_api | megamodo.com | 1 | 0.03% | 0.06% |
| news_api | memeburn.com | 1 | 0.03% | 0.06% |
| news_api | mensxp.com | 1 | 0.03% | 0.06% |
| news_api | meridiano.net | 1 | 0.03% | 0.06% |
| news_api | merkur.de | 1 | 0.03% | 0.06% |
| news_api | mersinhaber.com | 1 | 0.03% | 0.06% |
| news_api | metronews.ru | 1 | 0.03% | 0.06% |
| news_api | metroseoul.co.kr | 1 | 0.03% | 0.06% |
| news_api | michigandaily.com | 1 | 0.03% | 0.06% |
| news_api | mirrorspectator.com | 1 | 0.03% | 0.06% |
| news_api | mississauga.com | 1 | 0.03% | 0.06% |
| news_api | mittelstandcafe.de | 1 | 0.03% | 0.06% |
| news_api | mngz.ru | 1 | 0.03% | 0.06% |
| news_api | mobile.zol.com.cn | 1 | 0.03% | 0.06% |
| news_api | mobileidworld.com | 1 | 0.03% | 0.06% |
| news_api | mochimag.com | 1 | 0.03% | 0.06% |
| news_api | money.it | 1 | 0.03% | 0.06% |
| news_api | mp.cnfol.com | 1 | 0.03% | 0.06% |
| news_api | mskagency.ru | 1 | 0.03% | 0.06% |
| news_api | mudgeeguardian.com.au | 1 | 0.03% | 0.06% |
| news_api | mundoenlinea.cl | 1 | 0.03% | 0.06% |
| news_api | myanmarnews.net | 1 | 0.03% | 0.06% |
| news_api | mymagic949.com | 1 | 0.03% | 0.06% |
| news_api | n-tv.de | 1 | 0.03% | 0.06% |
| news_api | nagpurtoday.in | 1 | 0.03% | 0.06% |
| news_api | nashvilleherald.com | 1 | 0.03% | 0.06% |
| news_api | nationalmortgagenews.com | 1 | 0.03% | 0.06% |
| news_api | navbharattimes.indiatimes.com | 1 | 0.03% | 0.06% |
| news_api | nbcmontana.com | 1 | 0.03% | 0.06% |
| news_api | nbd.com.cn | 1 | 0.03% | 0.06% |
| news_api | nearshoreamericas.com | 1 | 0.03% | 0.06% |
| news_api | net.hr | 1 | 0.03% | 0.06% |
| news_api | netzwelt.de | 1 | 0.03% | 0.06% |
| news_api | newcastleherald.com.au | 1 | 0.03% | 0.06% |
| news_api | neworleanssun.com | 1 | 0.03% | 0.06% |
| news_api | newrepublic.com | 1 | 0.03% | 0.06% |
| news_api | news.china.com.cn | 1 | 0.03% | 0.06% |
| news_api | news.cnfol.com | 1 | 0.03% | 0.06% |
| news_api | news.cts.com.tw | 1 | 0.03% | 0.06% |
| news_api | news.ltn.com.tw | 1 | 0.03% | 0.06% |
| news_api | news.tuoitre.vn | 1 | 0.03% | 0.06% |
| news_api | news.ycwb.com | 1 | 0.03% | 0.06% |
| news_api | news8000.com | 1 | 0.03% | 0.06% |
| news_api | newsbomb.gr | 1 | 0.03% | 0.06% |
| news_api | newsit.gr | 1 | 0.03% | 0.06% |
| news_api | newsnet5.com | 1 | 0.03% | 0.06% |
| news_api | newstribune.com | 1 | 0.03% | 0.06% |
| news_api | newsway.co.kr | 1 | 0.03% | 0.06% |
| news_api | newsweek.com | 1 | 0.03% | 0.06% |
| news_api | newsx.com | 1 | 0.03% | 0.06% |
| news_api | newtalk.tw | 1 | 0.03% | 0.06% |
| news_api | newyorkstatesman.com | 1 | 0.03% | 0.06% |
| news_api | niagarathisweek.com | 1 | 0.03% | 0.06% |
| news_api | nieuws.nl | 1 | 0.03% | 0.06% |
| news_api | niezalezna.pl | 1 | 0.03% | 0.06% |
| news_api | nikkan-gendai.com | 1 | 0.03% | 0.06% |
| news_api | nikkan.co.jp | 1 | 0.03% | 0.06% |
| news_api | nikkei.com | 1 | 0.03% | 0.06% |
| news_api | nile.eg | 1 | 0.03% | 0.06% |
| news_api | nin.rs | 1 | 0.03% | 0.06% |
| news_api | nj.com | 1 | 0.03% | 0.06% |
| news_api | norran.se | 1 | 0.03% | 0.06% |
| news_api | northcountrynow.com | 1 | 0.03% | 0.06% |
| news_api | northerndailyleader.com.au | 1 | 0.03% | 0.06% |
| news_api | northweststar.com.au | 1 | 0.03% | 0.06% |
| news_api | noviny.sk | 1 | 0.03% | 0.06% |
| news_api | nrc.nl | 1 | 0.03% | 0.06% |
| news_api | ntv.com.tr | 1 | 0.03% | 0.06% |
| news_api | nwaonline.com | 1 | 0.03% | 0.06% |
| news_api | objectiv.tv | 1 | 0.03% | 0.06% |
| news_api | ocregister.com | 1 | 0.03% | 0.06% |
| news_api | ohiostandard.com | 1 | 0.03% | 0.06% |
| news_api | ohmynews.com | 1 | 0.03% | 0.06% |
| news_api | oklahomastar.com | 1 | 0.03% | 0.06% |
| news_api | ondacero.es | 1 | 0.03% | 0.06% |
| news_api | op-online.de | 1 | 0.03% | 0.06% |
| news_api | openpr.com | 1 | 0.03% | 0.06% |
| news_api | ostro.org | 1 | 0.03% | 0.06% |
| news_api | ottawacitizen.com | 1 | 0.03% | 0.06% |
| news_api | pakistantelegraph.com | 1 | 0.03% | 0.06% |
| news_api | panorama.com.al | 1 | 0.03% | 0.06% |
| news_api | paymentweek.com | 1 | 0.03% | 0.06% |
| news_api | pcchip.hr | 1 | 0.03% | 0.06% |
| news_api | pcwplus.hu | 1 | 0.03% | 0.06% |
| news_api | photo.china.com.cn | 1 | 0.03% | 0.06% |
| news_api | pitchfork.com | 1 | 0.03% | 0.06% |
| news_api | piter.tv | 1 | 0.03% | 0.06% |
| news_api | pjmedia.com | 1 | 0.03% | 0.06% |
| news_api | placenorthwest.co.uk | 1 | 0.03% | 0.06% |
| news_api | playground.ru | 1 | 0.03% | 0.06% |
| news_api | pleinevie.fr | 1 | 0.03% | 0.06% |
| news_api | pln-pskov.ru | 1 | 0.03% | 0.06% |
| news_api | podrobnosti.ua | 1 | 0.03% | 0.06% |
| news_api | polygon.com | 1 | 0.03% | 0.06% |
| news_api | portalsamorzadowy.pl | 1 | 0.03% | 0.06% |
| news_api | portnews.com.au | 1 | 0.03% | 0.06% |
| news_api | postandcourier.com | 1 | 0.03% | 0.06% |
| news_api | posttoday.com | 1 | 0.03% | 0.06% |
| news_api | powerorlando.com | 1 | 0.03% | 0.06% |
| news_api | pr.com | 1 | 0.03% | 0.06% |
| news_api | prensalibre.com | 1 | 0.03% | 0.06% |
| news_api | press24.mk | 1 | 0.03% | 0.06% |
| news_api | pressdemocrat.com | 1 | 0.03% | 0.06% |
| news_api | presse-citron.net | 1 | 0.03% | 0.06% |
| news_api | presstelegram.com | 1 | 0.03% | 0.06% |
| news_api | presstv.ir | 1 | 0.03% | 0.06% |
| news_api | primerafuente.com.ar | 1 | 0.03% | 0.06% |
| news_api | profitline.hu | 1 | 0.03% | 0.06% |
| news_api | publico.pt | 1 | 0.03% | 0.06% |
| news_api | punjabitribuneonline.com | 1 | 0.03% | 0.06% |
| news_api | pv-magazine.com | 1 | 0.03% | 0.06% |
| news_api | q947fm.iheart.com | 1 | 0.03% | 0.06% |
| news_api | quadratin.com.mx | 1 | 0.03% | 0.06% |
| news_api | radiofrance.fr | 1 | 0.03% | 0.06% |
| news_api | rappler.com | 1 | 0.03% | 0.06% |
| news_api | ratopati.com | 1 | 0.03% | 0.06% |
| news_api | realitatea.net | 1 | 0.03% | 0.06% |
| news_api | redlandsdailyfacts.com | 1 | 0.03% | 0.06% |
| news_api | regions.ru | 1 | 0.03% | 0.06% |
| news_api | reporterherald.com | 1 | 0.03% | 0.06% |
| news_api | republicain-lorrain.fr | 1 | 0.03% | 0.06% |
| news_api | republikein.com.na | 1 | 0.03% | 0.06% |
| news_api | ria.ru | 1 | 0.03% | 0.06% |
| news_api | riasv.ru | 1 | 0.03% | 0.06% |
| news_api | risky.biz | 1 | 0.03% | 0.06% |
| news_api | rnz.co.nz | 1 | 0.03% | 0.06% |
| news_api | rock1067.iheart.com | 1 | 0.03% | 0.06% |
| news_api | rocketerie.iheart.com | 1 | 0.03% | 0.06% |
| news_api | rstreet.org | 1 | 0.03% | 0.06% |
| news_api | rte.ie | 1 | 0.03% | 0.06% |
| news_api | rtl.nl | 1 | 0.03% | 0.06% |
| news_api | rtv.rs | 1 | 0.03% | 0.06% |
| news_api | rtvutrecht.nl | 1 | 0.03% | 0.06% |
| news_api | ruhrnachrichten.de | 1 | 0.03% | 0.06% |
| news_api | russiaherald.com | 1 | 0.03% | 0.06% |
| news_api | ryt9.com | 1 | 0.03% | 0.06% |
| news_api | saltlakecitysun.com | 1 | 0.03% | 0.06% |
| news_api | saltwire.com | 1 | 0.03% | 0.06% |
| news_api | salzburg24.at | 1 | 0.03% | 0.06% |
| news_api | sana.sy | 1 | 0.03% | 0.06% |
| news_api | sandiegouniontribune.com | 1 | 0.03% | 0.06% |
| news_api | sapo.pt | 1 | 0.03% | 0.06% |
| news_api | sc.stock.cnfol.com | 1 | 0.03% | 0.06% |
| news_api | scmp.com | 1 | 0.03% | 0.06% |
| news_api | scroll.in | 1 | 0.03% | 0.06% |
| news_api | sdpnoticias.com | 1 | 0.03% | 0.06% |
| news_api | senego.com | 1 | 0.03% | 0.06% |
| news_api | sentinelandenterprise.com | 1 | 0.03% | 0.06% |
| news_api | setn.com | 1 | 0.03% | 0.06% |
| news_api | sharemanthan.in | 1 | 0.03% | 0.06% |
| news_api | siliconrepublic.com | 1 | 0.03% | 0.06% |
| news_api | simcoe.com | 1 | 0.03% | 0.06% |
| news_api | siol.net | 1 | 0.03% | 0.06% |
| news_api | slguardian.org | 1 | 0.03% | 0.06% |
| news_api | slugmag.com | 1 | 0.03% | 0.06% |
| news_api | smh.com.au | 1 | 0.03% | 0.06% |
| news_api | sn.at | 1 | 0.03% | 0.06% |
| news_api | southernhighlandnews.com.au | 1 | 0.03% | 0.06% |
| news_api | sozcu.com.tr | 1 | 0.03% | 0.06% |
| news_api | spacedaily.com | 1 | 0.03% | 0.06% |
| news_api | spartanavenue.com | 1 | 0.03% | 0.06% |
| news_api | spokesman.com | 1 | 0.03% | 0.06% |
| news_api | srilankasource.com | 1 | 0.03% | 0.06% |
| news_api | star945.com | 1 | 0.03% | 0.06% |
| news_api | statecollege.com | 1 | 0.03% | 0.06% |
| news_api | stcatharinesstandard.ca | 1 | 0.03% | 0.06% |
| news_api | stern.de | 1 | 0.03% | 0.06% |
| news_api | stlouisstar.com | 1 | 0.03% | 0.06% |
| news_api | stock.hexun.com | 1 | 0.03% | 0.06% |
| news_api | stockbiz.vn | 1 | 0.03% | 0.06% |
| news_api | strategypage.com | 1 | 0.03% | 0.06% |
| news_api | studiob.rs | 1 | 0.03% | 0.06% |
| news_api | sud.ua | 1 | 0.03% | 0.06% |
| news_api | sueddeutsche.de | 1 | 0.03% | 0.06% |
| news_api | t13.cl | 1 | 0.03% | 0.06% |
| news_api | tagesanzeiger.ch | 1 | 0.03% | 0.06% |
| news_api | tagesschau.de | 1 | 0.03% | 0.06% |
| news_api | tagesspiegel.de | 1 | 0.03% | 0.06% |
| news_api | tass.ru | 1 | 0.03% | 0.06% |
| news_api | taz.de | 1 | 0.03% | 0.06% |
| news_api | tech.china.com | 1 | 0.03% | 0.06% |
| news_api | techcabal.com | 1 | 0.03% | 0.06% |
| news_api | techstory.in | 1 | 0.03% | 0.06% |
| news_api | techtimes.com | 1 | 0.03% | 0.06% |
| news_api | techtudo.com.br | 1 | 0.03% | 0.06% |
| news_api | tecmundo.com.br | 1 | 0.03% | 0.06% |
| news_api | tecnoandroid.it | 1 | 0.03% | 0.06% |
| news_api | tekniikkatalous.fi | 1 | 0.03% | 0.06% |
| news_api | texasguardian.com | 1 | 0.03% | 0.06% |
| news_api | tgrthaber.com | 1 | 0.03% | 0.06% |
| news_api | the-miyanichi.co.jp | 1 | 0.03% | 0.06% |
| news_api | theage.com.au | 1 | 0.03% | 0.06% |
| news_api | theblaze.com | 1 | 0.03% | 0.06% |
| news_api | theboneonline.com | 1 | 0.03% | 0.06% |
| news_api | thecourier.com.au | 1 | 0.03% | 0.06% |
| news_api | thefrontierpost.com | 1 | 0.03% | 0.06% |
| news_api | theguardian.com | 1 | 0.03% | 0.06% |
| news_api | thehardtackle.com | 1 | 0.03% | 0.06% |
| news_api | thehindubusinessline.com | 1 | 0.03% | 0.06% |
| news_api | theindependent.co.zw | 1 | 0.03% | 0.06% |
| news_api | thejournal.com | 1 | 0.03% | 0.06% |
| news_api | theleader.com.au | 1 | 0.03% | 0.06% |
| news_api | themissouritimes.com | 1 | 0.03% | 0.06% |
| news_api | themoscowtimes.com | 1 | 0.03% | 0.06% |
| news_api | thenational.scot | 1 | 0.03% | 0.06% |
| news_api | thepeterboroughexaminer.com | 1 | 0.03% | 0.06% |
| news_api | therecord.com | 1 | 0.03% | 0.06% |
| news_api | thesunchronicle.com | 1 | 0.03% | 0.06% |
| news_api | thetoc.gr | 1 | 0.03% | 0.06% |
| news_api | theverge.com | 1 | 0.03% | 0.06% |
| news_api | ticweb.es | 1 | 0.03% | 0.06% |
| news_api | timeslive.co.za | 1 | 0.03% | 0.06% |
| news_api | timesofsandiego.com | 1 | 0.03% | 0.06% |
| news_api | tivi.fi | 1 | 0.03% | 0.06% |
| news_api | toffeeweb.com | 1 | 0.03% | 0.06% |
| news_api | toonippo.co.jp | 1 | 0.03% | 0.06% |
| news_api | top-channel.tv | 1 | 0.03% | 0.06% |
| news_api | topics.or.jp | 1 | 0.03% | 0.06% |
| news_api | toronto.citynews.ca | 1 | 0.03% | 0.06% |
| news_api | torquenews.com | 1 | 0.03% | 0.06% |
| news_api | totaltele.com | 1 | 0.03% | 0.06% |
| news_api | travelweekly.com.au | 1 | 0.03% | 0.06% |
| news_api | troyrecord.com | 1 | 0.03% | 0.06% |
| news_api | trustedreviews.com | 1 | 0.03% | 0.06% |
| news_api | tucsonpost.com | 1 | 0.03% | 0.06% |
| news_api | turkiyegazetesi.com.tr | 1 | 0.03% | 0.06% |
| news_api | tvxs.gr | 1 | 0.03% | 0.06% |
| news_api | twincities.com | 1 | 0.03% | 0.06% |
| news_api | twz.com | 1 | 0.03% | 0.06% |
| news_api | udn.com | 1 | 0.03% | 0.06% |
| news_api | ukrinform.ua | 1 | 0.03% | 0.06% |
| news_api | upi.com | 1 | 0.03% | 0.06% |
| news_api | us.cnn.com | 1 | 0.03% | 0.06% |
| news_api | utilitydive.com | 1 | 0.03% | 0.06% |
| news_api | utv.ie | 1 | 0.03% | 0.06% |
| news_api | uzmanpara.milliyet.com.tr | 1 | 0.03% | 0.06% |
| news_api | vecer.com | 1 | 0.03% | 0.06% |
| news_api | vecernji.ba | 1 | 0.03% | 0.06% |
| news_api | vesti-ua.net | 1 | 0.03% | 0.06% |
| news_api | vetogate.com | 1 | 0.03% | 0.06% |
| news_api | vm.ru | 1 | 0.03% | 0.06% |
| news_api | volksstimme.de | 1 | 0.03% | 0.06% |
| news_api | vrt.be | 1 | 0.03% | 0.06% |
| news_api | wahpetondailynews.com | 1 | 0.03% | 0.06% |
| news_api | wallstreet-online.de | 1 | 0.03% | 0.06% |
| news_api | wape.com | 1 | 0.03% | 0.06% |
| news_api | war.obozrevatel.com | 1 | 0.03% | 0.06% |
| news_api | watoday.com.au | 1 | 0.03% | 0.06% |
| news_api | watson.ch | 1 | 0.03% | 0.06% |
| news_api | wbkr.com | 1 | 0.03% | 0.06% |
| news_api | wboc.com | 1 | 0.03% | 0.06% |
| news_api | wcbi.com | 1 | 0.03% | 0.06% |
| news_api | wcvb.com | 1 | 0.03% | 0.06% |
| news_api | wdsu.com | 1 | 0.03% | 0.06% |
| news_api | webinars.govtech.com | 1 | 0.03% | 0.06% |
| news_api | weekend.perfil.com | 1 | 0.03% | 0.06% |
| news_api | welt.de | 1 | 0.03% | 0.06% |
| news_api | wftv.com | 1 | 0.03% | 0.06% |
| news_api | wgauradio.com | 1 | 0.03% | 0.06% |
| news_api | wgna.com | 1 | 0.03% | 0.06% |
| news_api | whittierdailynews.com | 1 | 0.03% | 0.06% |
| news_api | whmi.com | 1 | 0.03% | 0.06% |
| news_api | wibx950.com | 1 | 0.03% | 0.06% |
| news_api | wikitree.co.kr | 1 | 0.03% | 0.06% |
| news_api | winfuture.de | 1 | 0.03% | 0.06% |
| news_api | wirtualnemedia.pl | 1 | 0.03% | 0.06% |
| news_api | wlox.com | 1 | 0.03% | 0.06% |
| news_api | wlwt.com | 1 | 0.03% | 0.06% |
| news_api | wnnj.iheart.com | 1 | 0.03% | 0.06% |
| news_api | wokv.com | 1 | 0.03% | 0.06% |
| news_api | words.filippo.io | 1 | 0.03% | 0.06% |
| news_api | world.kbs.co.kr | 1 | 0.03% | 0.06% |
| news_api | wosu.org | 1 | 0.03% | 0.06% |
| news_api | wowo.com | 1 | 0.03% | 0.06% |
| news_api | wpxi.com | 1 | 0.03% | 0.06% |
| news_api | wshu.org | 1 | 0.03% | 0.06% |
| news_api | wsoctv.com | 1 | 0.03% | 0.06% |
| news_api | wthr.com | 1 | 0.03% | 0.06% |
| news_api | wtsp.com | 1 | 0.03% | 0.06% |
| news_api | wusa9.com | 1 | 0.03% | 0.06% |
| news_api | wvtm13.com | 1 | 0.03% | 0.06% |
| news_api | wwltv.com | 1 | 0.03% | 0.06% |
| news_api | wwmt.com | 1 | 0.03% | 0.06% |
| news_api | wwwhatsnew.com | 1 | 0.03% | 0.06% |
| news_api | wxii12.com | 1 | 0.03% | 0.06% |
| news_api | wxow.com | 1 | 0.03% | 0.06% |
| news_api | y100fm.com | 1 | 0.03% | 0.06% |
| news_api | y95country.com | 1 | 0.03% | 0.06% |
| news_api | yasstribune.com.au | 1 | 0.03% | 0.06% |
| news_api | yeniakit.com.tr | 1 | 0.03% | 0.06% |
| news_api | yeniasya.com.tr | 1 | 0.03% | 0.06% |
| news_api | yn.xinhuanet.com | 1 | 0.03% | 0.06% |
| news_api | yorkpress.co.uk | 1 | 0.03% | 0.06% |
| news_api | yorkregion.com | 1 | 0.03% | 0.06% |
| news_api | zazoom.it | 1 | 0.03% | 0.06% |
| news_api | zdnet.com | 1 | 0.03% | 0.06% |
| news_api | zeit.de | 1 | 0.03% | 0.06% |
| news_api | zetatijuana.com | 1 | 0.03% | 0.06% |
| news_api | zonebourse.com | 1 | 0.03% | 0.06% |

## Top 30 Inspection Words By source_type

### cve

vulnerability (967), file (413), kernel (369), may (348), issue (339), fix (328), exploit (321), attackers (319), function (299), linux (288), used (287), following (285), resolved (270), attacker (268), attack (266), user (259), allows (257), access (253), manipulation (248), code (234), path (229), arbitrary (221), remote (207), argument (205), component (201), prior (196), version (194), data (192), system (189), affected (186)

### news_api

security (80), data (80), cyber (72), new (65), breach (59), says (56), scam (55), ddos (48), ransomware (47), malware (46), cyberattack (44), attack (44), financial (39), report (37), web (33), safe (32), dark (31), rebel (31), amid (31), risk (30), google (29), attacks (29), stay (29), news (29), threat (28), hackers (28), fuel (28), openai (28), ways (27), anatomy (26)

### news_rss

vulnerability (504), security (408), exploitation (380), windows (368), data (315), likely (302), access (284), less (240), process (226), privilege (204), code (203), elevation (198), new (195), file (189), system (176), exploit (176), microsoft (175), vulnerabilities (169), one (168), used (165), also (163), pointer (159), teams (157), attack (153), user (151), using (150), buffer (150), execution (143), would (143), time (135)

### reddit_rss

link (546), comments (533), submitted (520), like (191), use (148), security (144), would (138), one (120), data (110), new (100), anyone (96), know (91), work (91), people (91), https (90), still (89), also (89), time (88), something (86), system (85), don (85), using (85), windows (84), access (82), actually (79), need (78), get (77), com (75), way (73), code (72)
