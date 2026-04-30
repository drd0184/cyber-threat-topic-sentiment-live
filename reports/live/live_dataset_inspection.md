# Live Dataset Inspection

Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 3132 |
| created_at min | 2025-12-16T09:00:00Z |
| created_at max | 2026-04-30T13:31:57Z |
| collected_at min | 2026-04-29T13:22:42Z |
| collected_at max | 2026-04-30T13:36:00Z |
| Unparsable created_at | 0 (0.00%) |
| Unparsable collected_at | 0 (0.00%) |
| Null/empty text_raw | 0 (0.00%) |
| Mean text_raw length | 546.99 |
| Median text_raw length | 203.0 |
| Min text_raw length | 8 |
| Max text_raw length | 66525 |
| text_raw < 30 chars | 60 (1.92%) |
| text_raw < 100 chars | 1188 (37.93%) |
| Duplicate id rows | 0 rows / 0 values |
| Duplicate url rows | 0 rows / 0 values |
| Duplicate normalized text_raw rows | 219 rows / 69 values |

## Warnings

- WARNING: Duplicate normalized text_raw rows found: 219.

## Rows By source_type

| source_type | rows | percent_dataset |
| --- | --- | --- |
| cve | 1295 | 41.35% |
| news_api | 1280 | 40.87% |
| reddit_rss | 395 | 12.61% |
| news_rss | 162 | 5.17% |

## Rows By source_name

| source_name | rows | percent_dataset |
| --- | --- | --- |
| NVD CVE | 1295 | 41.35% |
| cybersecurity | 64 | 2.04% |
| sysadmin | 57 | 1.82% |
| The Hacker News | 56 | 1.79% |
| privacy | 43 | 1.37% |
| blueteamsec | 39 | 1.25% |
| netsec | 31 | 0.99% |
| hacking | 29 | 0.93% |
| AskNetsec | 27 | 0.86% |
| ReverseEngineering | 27 | 0.86% |
| osint | 27 | 0.86% |
| techradar.com | 27 | 0.86% |
| forbes.com | 27 | 0.86% |
| Malware | 26 | 0.83% |
| ComputerSecurity | 25 | 0.80% |
| BleepingComputer | 23 | 0.73% |
| cnews.ru | 23 | 0.73% |
| ithome.com.tw | 23 | 0.73% |
| Rapid7 Blog | 22 | 0.70% |
| ascii.jp | 19 | 0.61% |
| 163.com | 16 | 0.51% |
| Cisco Talos Blog | 15 | 0.48% |
| Unit 42 | 15 | 0.48% |
| manilatimes.net | 14 | 0.45% |
| SANS Internet Storm Center | 12 | 0.38% |
| esecurityplanet.com | 12 | 0.38% |
| bankinfosecurity.com | 12 | 0.38% |
| itbrief.co.nz | 12 | 0.38% |
| finance.sina.com.cn | 12 | 0.38% |
| cointelegraph.com | 11 | 0.35% |
| theregister.com | 11 | 0.35% |
| KrebsOnSecurity | 10 | 0.32% |
| el-balad.com | 10 | 0.32% |
| Google Project Zero | 9 | 0.29% |
| csoonline.com | 9 | 0.29% |
| infosecurity-magazine.com | 9 | 0.29% |
| govinfosecurity.com | 9 | 0.29% |
| finanznachrichten.de | 8 | 0.26% |
| timesofindia.indiatimes.com | 8 | 0.26% |
| economictimes.indiatimes.com | 8 | 0.26% |
| techcrunch.com | 8 | 0.26% |
| baijiahao.baidu.com | 8 | 0.26% |
| finance.yahoo.com | 7 | 0.22% |
| moneycontrol.com | 7 | 0.22% |
| channellife.co.nz | 7 | 0.22% |
| haberler.com | 6 | 0.19% |
| laopcion.com.mx | 6 | 0.19% |
| udayavani.com | 6 | 0.19% |
| tvguide.co.uk | 6 | 0.19% |
| fool.com | 6 | 0.19% |
| govtech.com | 5 | 0.16% |
| jdsupra.com | 5 | 0.16% |
| yahoo.com | 5 | 0.16% |
| channellife.com.au | 5 | 0.16% |
| biz.heraldcorp.com | 5 | 0.16% |
| boredpanda.com | 5 | 0.16% |
| hothardware.com | 4 | 0.13% |
| japan.zdnet.com | 4 | 0.13% |
| insurancebusinessmag.com | 4 | 0.13% |
| winnipegfreepress.com | 4 | 0.13% |
| thenews.com.pk | 4 | 0.13% |
| thefastmode.com | 4 | 0.13% |
| zdnet.co.kr | 4 | 0.13% |
| aa.com.tr | 4 | 0.13% |
| vz.ru | 4 | 0.13% |
| screenrant.com | 4 | 0.13% |
| coindesk.com | 4 | 0.13% |
| 9to5mac.com | 4 | 0.13% |
| interfax.ru | 4 | 0.13% |
| itnews.com.au | 4 | 0.13% |
| it-online.co.za | 4 | 0.13% |
| androidauthority.com | 3 | 0.10% |
| mondaq.com | 3 | 0.10% |
| ura.news | 3 | 0.10% |
| ensonhaber.com | 3 | 0.10% |
| milliyet.com.tr | 3 | 0.10% |
| prnewswire.com | 3 | 0.10% |
| womannews.net | 3 | 0.10% |
| miragenews.com | 3 | 0.10% |
| ddaily.co.kr | 3 | 0.10% |
| edaily.co.kr | 3 | 0.10% |
| cbc.ca | 3 | 0.10% |
| politis.com.cy | 3 | 0.10% |
| koreaherald.com | 3 | 0.10% |
| kibrispostasi.com | 3 | 0.10% |
| bleedingcool.com | 3 | 0.10% |
| hindustantimes.com | 3 | 0.10% |
| finance.eastmoney.com | 3 | 0.10% |
| heise.de | 3 | 0.10% |
| dostor.org | 3 | 0.10% |
| freepressjournal.in | 3 | 0.10% |
| securitylab.ru | 3 | 0.10% |
| newswiretoday.com | 3 | 0.10% |
| portal.sina.com.hk | 3 | 0.10% |
| itbusinessnet.com | 3 | 0.10% |
| biometricupdate.com | 3 | 0.10% |
| time.mk | 3 | 0.10% |
| foxnews.com | 3 | 0.10% |
| fnnews.com | 3 | 0.10% |
| divyabhaskar.co.in | 3 | 0.10% |
| computing.co.uk | 3 | 0.10% |
| newjerseytelegraph.com | 3 | 0.10% |
| itweb.co.za | 3 | 0.10% |
| alltoc.com | 3 | 0.10% |
| businessghana.com | 2 | 0.06% |
| digitaljournal.com | 2 | 0.06% |
| securityinfowatch.com | 2 | 0.06% |
| gizmodo.com | 2 | 0.06% |
| insurancejournal.com | 2 | 0.06% |
| computerweekly.com | 2 | 0.06% |
| pymnts.com | 2 | 0.06% |
| bleepingcomputer.com | 2 | 0.06% |
| tomshardware.com | 2 | 0.06% |
| cnnturk.com | 2 | 0.06% |
| phonandroid.com | 2 | 0.06% |
| propakistani.pk | 2 | 0.06% |
| life.ru | 2 | 0.06% |
| donanimgunlugu.com | 2 | 0.06% |
| pcmag.com | 2 | 0.06% |
| github.com | 2 | 0.06% |
| sb.by | 2 | 0.06% |
| t-online.de | 2 | 0.06% |
| freemalaysiatoday.com | 2 | 0.06% |
| wesh.com | 2 | 0.06% |
| iz.ru | 2 | 0.06% |
| glavcom.ua | 2 | 0.06% |
| bunburymail.com.au | 2 | 0.06% |
| nvi.com.au | 2 | 0.06% |
| scoop.co.nz | 2 | 0.06% |
| straitstimes.com | 2 | 0.06% |
| dailykos.com | 2 | 0.06% |
| lalsace.fr | 2 | 0.06% |
| elmanana.com | 2 | 0.06% |
| nzherald.co.nz | 2 | 0.06% |
| news.cn | 2 | 0.06% |
| wiwo.de | 2 | 0.06% |
| sabah.com.tr | 2 | 0.06% |
| eurointegration.com.ua | 2 | 0.06% |
| wdrb.com | 2 | 0.06% |
| aol.co.uk | 2 | 0.06% |
| lbc.co.uk | 2 | 0.06% |
| theglobeandmail.com | 2 | 0.06% |
| n.yam.com | 2 | 0.06% |
| odatv.com | 2 | 0.06% |
| bd-pratidin.com | 2 | 0.06% |
| hurriyetdailynews.com | 2 | 0.06% |
| wfmz.com | 2 | 0.06% |
| hinews.cn | 2 | 0.06% |
| tech.caijing.com.cn | 2 | 0.06% |
| tech.ifeng.com | 2 | 0.06% |
| androidheadlines.com | 2 | 0.06% |
| shorouknews.com | 2 | 0.06% |
| vietnamnet.vn | 2 | 0.06% |
| russian.rt.com | 2 | 0.06% |
| vesti.ru | 2 | 0.06% |
| europapress.es | 2 | 0.06% |
| jawapos.com | 2 | 0.06% |
| fontanka.ru | 2 | 0.06% |
| 1prime.ru | 2 | 0.06% |
| vg.no | 2 | 0.06% |
| weser-kurier.de | 2 | 0.06% |
| ntdtv.com | 2 | 0.06% |
| securitybrief.news | 2 | 0.06% |
| itwire.com | 2 | 0.06% |
| jugantor.com | 2 | 0.06% |
| webpronews.com | 2 | 0.06% |
| htxt.co.za | 2 | 0.06% |
| infoworld.com | 2 | 0.06% |
| bjnews.com.cn | 2 | 0.06% |
| stcn.com | 2 | 0.06% |
| military.china.com | 2 | 0.06% |
| antaranews.com | 2 | 0.06% |
| itbear.com.cn | 2 | 0.06% |
| index.hr | 2 | 0.06% |
| eldia.com.bo | 2 | 0.06% |
| eldestapeweb.com | 2 | 0.06% |
| am.com.mx | 2 | 0.06% |
| tn.com.ar | 2 | 0.06% |
| natalie.mu | 2 | 0.06% |
| insight.co.kr | 2 | 0.06% |
| newspim.com | 2 | 0.06% |
| thehindu.com | 2 | 0.06% |
| hindi.webdunia.com | 2 | 0.06% |
| tribuneindia.com | 2 | 0.06% |
| geeky-gadgets.com | 2 | 0.06% |
| americanbanker.com | 2 | 0.06% |
| marketscreener.com | 2 | 0.06% |
| hawaiitelegraph.com | 2 | 0.06% |
| posta.com.tr | 2 | 0.06% |
| wired.com | 2 | 0.06% |
| eturbonews.com | 2 | 0.06% |
| lrytas.lt | 2 | 0.06% |
| sanantoniopost.com | 2 | 0.06% |
| nypost.com | 2 | 0.06% |
| deadline.com | 2 | 0.06% |
| macleayargus.com.au | 2 | 0.06% |
| investegate.co.uk | 2 | 0.06% |
| arkansasonline.com | 2 | 0.06% |
| natlawreview.com | 2 | 0.06% |
| claimsjournal.com | 2 | 0.06% |
| fox4news.com | 2 | 0.06% |
| itnewsonline.com | 2 | 0.06% |
| livenews.co.nz | 2 | 0.06% |
| medianama.com | 2 | 0.06% |
| allafrica.com | 2 | 0.06% |
| ecodibergamo.it | 2 | 0.06% |
| libnanews.com | 2 | 0.06% |
| techweez.com | 2 | 0.06% |
| thisdaylive.com | 2 | 0.06% |
| welivesecurity.com | 2 | 0.06% |
| tmtpost.com | 2 | 0.06% |
| sentinel.ht | 2 | 0.06% |
| bangkokpost.com | 1 | 0.03% |
| governing.com | 1 | 0.03% |
| abc7news.com | 1 | 0.03% |
| inforum.com | 1 | 0.03% |
| cnn.com | 1 | 0.03% |
| edition.cnn.com | 1 | 0.03% |
| us.cnn.com | 1 | 0.03% |
| fox9.com | 1 | 0.03% |
| hachettebookgroup.com | 1 | 0.03% |
| bangordailynews.com | 1 | 0.03% |
| wsbtv.com | 1 | 0.03% |
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
| hollywoodreporter.com | 1 | 0.03% |
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
| wbaltv.com | 1 | 0.03% |
| wvtm13.com | 1 | 0.03% |
| wlwt.com | 1 | 0.03% |
| hirek.prim.hu | 1 | 0.03% |
| ottawacitizen.com | 1 | 0.03% |
| news.ltn.com.tw | 1 | 0.03% |
| dnews.gr | 1 | 0.03% |
| infobae.com | 1 | 0.03% |
| ledauphine.com | 1 | 0.03% |
| bankingnews.gr | 1 | 0.03% |
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
| trthaber.com | 1 | 0.03% |
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
| wmur.com | 1 | 0.03% |
| king5.com | 1 | 0.03% |
| wtsp.com | 1 | 0.03% |
| wwltv.com | 1 | 0.03% |
| defensenews.com | 1 | 0.03% |
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
| jpost.com | 1 | 0.03% |
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
| kommersant.ru | 1 | 0.03% |
| jpnn.com | 1 | 0.03% |
| gorod48.ru | 1 | 0.03% |
| mskagency.ru | 1 | 0.03% |
| politika.rs | 1 | 0.03% |
| makassar.tribunnews.com | 1 | 0.03% |
| vedomosti.ru | 1 | 0.03% |
| mashable.com | 1 | 0.03% |
| volksstimme.de | 1 | 0.03% |
| handelsblatt.com | 1 | 0.03% |
| sueddeutsche.de | 1 | 0.03% |
| cepro.com | 1 | 0.03% |
| irishdentist.ie | 1 | 0.03% |
| corp.cnews.ru | 1 | 0.03% |
| vesti-ua.net | 1 | 0.03% |
| unian.net | 1 | 0.03% |
| slguardian.org | 1 | 0.03% |
| chip.de | 1 | 0.03% |
| comnews.ru | 1 | 0.03% |
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
| makeuseof.com | 1 | 0.03% |
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
| cloud.watch.impress.co.jp | 1 | 0.03% |
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
| businessday.co.za | 1 | 0.03% |
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
| etoday.co.kr | 1 | 0.03% |
| segye.com | 1 | 0.03% |
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
| inewsgr.com | 1 | 0.03% |
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
| kten.com | 1 | 0.03% |
| news8000.com | 1 | 0.03% |
| channelbuzz.ca | 1 | 0.03% |
| totaltele.com | 1 | 0.03% |
| dominicanrepublicpost.com | 1 | 0.03% |
| aljazeera.com | 1 | 0.03% |
| rte.ie | 1 | 0.03% |
| dcvelocity.com | 1 | 0.03% |
| tennesseedaily.com | 1 | 0.03% |
| californiatelegraph.com | 1 | 0.03% |
| republikein.com.na | 1 | 0.03% |
| bozemandailychronicle.com | 1 | 0.03% |
| bmmagazine.co.uk | 1 | 0.03% |
| vm.ru | 1 | 0.03% |
| ibtimes.co.uk | 1 | 0.03% |
| metronews.ru | 1 | 0.03% |
| dha.com.tr | 1 | 0.03% |
| begeek.fr | 1 | 0.03% |
| haksozhaber.net | 1 | 0.03% |
| evrensel.net | 1 | 0.03% |
| mngz.ru | 1 | 0.03% |
| cafebiz.vn | 1 | 0.03% |
| lgz.ru | 1 | 0.03% |
| canardpc.com | 1 | 0.03% |
| mersinhaber.com | 1 | 0.03% |
| tgrthaber.com | 1 | 0.03% |
| diyarbakirsoz.com | 1 | 0.03% |
| lefigaro.fr | 1 | 0.03% |
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
| aninews.in | 1 | 0.03% |
| upi.com | 1 | 0.03% |
| koreatimes.co.kr | 1 | 0.03% |
| dynamicbusiness.com | 1 | 0.03% |
| zonebourse.com | 1 | 0.03% |
| interaksyon.philstar.com | 1 | 0.03% |
| timeslive.co.za | 1 | 0.03% |
| nbcmontana.com | 1 | 0.03% |
| clydebankpost.co.uk | 1 | 0.03% |
| capital.ro | 1 | 0.03% |
| tagesanzeiger.ch | 1 | 0.03% |
| zazoom.it | 1 | 0.03% |
| bernerzeitung.ch | 1 | 0.03% |
| aceshowbiz.com | 1 | 0.03% |
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
| unternehmen-heute.de | 1 | 0.03% |
| asahi.com | 1 | 0.03% |
| manningrivertimes.com.au | 1 | 0.03% |
| bluemountainsgazette.com.au | 1 | 0.03% |
| newcastleherald.com.au | 1 | 0.03% |
| inverelltimes.com.au | 1 | 0.03% |
| lithgowmercury.com.au | 1 | 0.03% |
| illawarramercury.com.au | 1 | 0.03% |
| tagesspiegel.de | 1 | 0.03% |
| thenextweb.com | 1 | 0.03% |
| thesunchronicle.com | 1 | 0.03% |
| indiatvnews.com | 1 | 0.03% |
| watoday.com.au | 1 | 0.03% |
| nwaonline.com | 1 | 0.03% |
| techstory.in | 1 | 0.03% |
| english.pravda.ru | 1 | 0.03% |
| daily-tribune.com | 1 | 0.03% |
| saltwire.com | 1 | 0.03% |
| afr.com | 1 | 0.03% |
| business.scoop.co.nz | 1 | 0.03% |
| internetua.com | 1 | 0.03% |
| whmi.com | 1 | 0.03% |
| utilitydive.com | 1 | 0.03% |
| michigandaily.com | 1 | 0.03% |
| wdsu.com | 1 | 0.03% |
| blackseanews.net | 1 | 0.03% |
| uainfo.org | 1 | 0.03% |
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
| daily.com.ua | 1 | 0.03% |
| nrc.nl | 1 | 0.03% |
| naftemporiki.gr | 1 | 0.03% |
| elconfidencial.com | 1 | 0.03% |
| diario.mx | 1 | 0.03% |
| eldiariodechihuahua.mx | 1 | 0.03% |
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
| ghanamma.com | 1 | 0.03% |
| marketintelligencecenter.com | 1 | 0.03% |
| dailyexcelsior.com | 1 | 0.03% |
| lina.sh | 1 | 0.03% |
| themoscowtimes.com | 1 | 0.03% |
| rediff.com | 1 | 0.03% |
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
| insideottawavalley.com | 1 | 0.03% |
| simcoe.com | 1 | 0.03% |
| gadgetsmagazine.com.ph | 1 | 0.03% |
| spacedaily.com | 1 | 0.03% |
| insight.scmagazineuk.com | 1 | 0.03% |
| 21stcenturywire.com | 1 | 0.03% |
| ghanaiantimes.com.gh | 1 | 0.03% |
| donews.com | 1 | 0.03% |
| pv-magazine.com | 1 | 0.03% |
| tech.china.com | 1 | 0.03% |
| massachusettssun.com | 1 | 0.03% |
| pakistantelegraph.com | 1 | 0.03% |
| birminghamstar.com | 1 | 0.03% |
| laosnews.net | 1 | 0.03% |
| chinanationalnews.com | 1 | 0.03% |
| newyorkstatesman.com | 1 | 0.03% |
| coloradostar.com | 1 | 0.03% |
| nashvilleherald.com | 1 | 0.03% |
| stlouisstar.com | 1 | 0.03% |
| saltlakecitysun.com | 1 | 0.03% |
| europesun.com | 1 | 0.03% |
| myanmarnews.net | 1 | 0.03% |
| utv.ie | 1 | 0.03% |
| eejournal.com | 1 | 0.03% |
| elektroniknet.de | 1 | 0.03% |
| thejournal.com | 1 | 0.03% |
| dailypioneer.com | 1 | 0.03% |
| newrepublic.com | 1 | 0.03% |
| excite.co.jp | 1 | 0.03% |
| jamaicaobserver.com | 1 | 0.03% |
| itbrief.news | 1 | 0.03% |
| wzzm13.com | 1 | 0.03% |
| punchng.com | 1 | 0.03% |

## Source Distribution

| source_type | source_name | rows | percent_dataset | percent_source_type |
| --- | --- | --- | --- | --- |
| cve | NVD CVE | 1295 | 41.35% | 100.00% |
| reddit_rss | cybersecurity | 64 | 2.04% | 16.20% |
| reddit_rss | sysadmin | 57 | 1.82% | 14.43% |
| news_rss | The Hacker News | 56 | 1.79% | 34.57% |
| reddit_rss | privacy | 43 | 1.37% | 10.89% |
| reddit_rss | blueteamsec | 39 | 1.25% | 9.87% |
| reddit_rss | netsec | 31 | 0.99% | 7.85% |
| reddit_rss | hacking | 29 | 0.93% | 7.34% |
| news_api | forbes.com | 27 | 0.86% | 2.11% |
| news_api | techradar.com | 27 | 0.86% | 2.11% |
| reddit_rss | AskNetsec | 27 | 0.86% | 6.84% |
| reddit_rss | ReverseEngineering | 27 | 0.86% | 6.84% |
| reddit_rss | osint | 27 | 0.86% | 6.84% |
| reddit_rss | Malware | 26 | 0.83% | 6.58% |
| reddit_rss | ComputerSecurity | 25 | 0.80% | 6.33% |
| news_api | cnews.ru | 23 | 0.73% | 1.80% |
| news_api | ithome.com.tw | 23 | 0.73% | 1.80% |
| news_rss | BleepingComputer | 23 | 0.73% | 14.20% |
| news_rss | Rapid7 Blog | 22 | 0.70% | 13.58% |
| news_api | ascii.jp | 19 | 0.61% | 1.48% |
| news_api | 163.com | 16 | 0.51% | 1.25% |
| news_rss | Cisco Talos Blog | 15 | 0.48% | 9.26% |
| news_rss | Unit 42 | 15 | 0.48% | 9.26% |
| news_api | manilatimes.net | 14 | 0.45% | 1.09% |
| news_api | bankinfosecurity.com | 12 | 0.38% | 0.94% |
| news_api | esecurityplanet.com | 12 | 0.38% | 0.94% |
| news_api | finance.sina.com.cn | 12 | 0.38% | 0.94% |
| news_api | itbrief.co.nz | 12 | 0.38% | 0.94% |
| news_rss | SANS Internet Storm Center | 12 | 0.38% | 7.41% |
| news_api | cointelegraph.com | 11 | 0.35% | 0.86% |
| news_api | theregister.com | 11 | 0.35% | 0.86% |
| news_api | el-balad.com | 10 | 0.32% | 0.78% |
| news_rss | KrebsOnSecurity | 10 | 0.32% | 6.17% |
| news_api | csoonline.com | 9 | 0.29% | 0.70% |
| news_api | govinfosecurity.com | 9 | 0.29% | 0.70% |
| news_api | infosecurity-magazine.com | 9 | 0.29% | 0.70% |
| news_rss | Google Project Zero | 9 | 0.29% | 5.56% |
| news_api | baijiahao.baidu.com | 8 | 0.26% | 0.62% |
| news_api | economictimes.indiatimes.com | 8 | 0.26% | 0.62% |
| news_api | finanznachrichten.de | 8 | 0.26% | 0.62% |
| news_api | techcrunch.com | 8 | 0.26% | 0.62% |
| news_api | timesofindia.indiatimes.com | 8 | 0.26% | 0.62% |
| news_api | channellife.co.nz | 7 | 0.22% | 0.55% |
| news_api | finance.yahoo.com | 7 | 0.22% | 0.55% |
| news_api | moneycontrol.com | 7 | 0.22% | 0.55% |
| news_api | fool.com | 6 | 0.19% | 0.47% |
| news_api | haberler.com | 6 | 0.19% | 0.47% |
| news_api | laopcion.com.mx | 6 | 0.19% | 0.47% |
| news_api | tvguide.co.uk | 6 | 0.19% | 0.47% |
| news_api | udayavani.com | 6 | 0.19% | 0.47% |
| news_api | biz.heraldcorp.com | 5 | 0.16% | 0.39% |
| news_api | boredpanda.com | 5 | 0.16% | 0.39% |
| news_api | channellife.com.au | 5 | 0.16% | 0.39% |
| news_api | govtech.com | 5 | 0.16% | 0.39% |
| news_api | jdsupra.com | 5 | 0.16% | 0.39% |
| news_api | yahoo.com | 5 | 0.16% | 0.39% |
| news_api | 9to5mac.com | 4 | 0.13% | 0.31% |
| news_api | aa.com.tr | 4 | 0.13% | 0.31% |
| news_api | coindesk.com | 4 | 0.13% | 0.31% |
| news_api | hothardware.com | 4 | 0.13% | 0.31% |
| news_api | insurancebusinessmag.com | 4 | 0.13% | 0.31% |
| news_api | interfax.ru | 4 | 0.13% | 0.31% |
| news_api | it-online.co.za | 4 | 0.13% | 0.31% |
| news_api | itnews.com.au | 4 | 0.13% | 0.31% |
| news_api | japan.zdnet.com | 4 | 0.13% | 0.31% |
| news_api | screenrant.com | 4 | 0.13% | 0.31% |
| news_api | thefastmode.com | 4 | 0.13% | 0.31% |
| news_api | thenews.com.pk | 4 | 0.13% | 0.31% |
| news_api | vz.ru | 4 | 0.13% | 0.31% |
| news_api | winnipegfreepress.com | 4 | 0.13% | 0.31% |
| news_api | zdnet.co.kr | 4 | 0.13% | 0.31% |
| news_api | alltoc.com | 3 | 0.10% | 0.23% |
| news_api | androidauthority.com | 3 | 0.10% | 0.23% |
| news_api | biometricupdate.com | 3 | 0.10% | 0.23% |
| news_api | bleedingcool.com | 3 | 0.10% | 0.23% |
| news_api | cbc.ca | 3 | 0.10% | 0.23% |
| news_api | computing.co.uk | 3 | 0.10% | 0.23% |
| news_api | ddaily.co.kr | 3 | 0.10% | 0.23% |
| news_api | divyabhaskar.co.in | 3 | 0.10% | 0.23% |
| news_api | dostor.org | 3 | 0.10% | 0.23% |
| news_api | edaily.co.kr | 3 | 0.10% | 0.23% |
| news_api | ensonhaber.com | 3 | 0.10% | 0.23% |
| news_api | finance.eastmoney.com | 3 | 0.10% | 0.23% |
| news_api | fnnews.com | 3 | 0.10% | 0.23% |
| news_api | foxnews.com | 3 | 0.10% | 0.23% |
| news_api | freepressjournal.in | 3 | 0.10% | 0.23% |
| news_api | heise.de | 3 | 0.10% | 0.23% |
| news_api | hindustantimes.com | 3 | 0.10% | 0.23% |
| news_api | itbusinessnet.com | 3 | 0.10% | 0.23% |
| news_api | itweb.co.za | 3 | 0.10% | 0.23% |
| news_api | kibrispostasi.com | 3 | 0.10% | 0.23% |
| news_api | koreaherald.com | 3 | 0.10% | 0.23% |
| news_api | milliyet.com.tr | 3 | 0.10% | 0.23% |
| news_api | miragenews.com | 3 | 0.10% | 0.23% |
| news_api | mondaq.com | 3 | 0.10% | 0.23% |
| news_api | newjerseytelegraph.com | 3 | 0.10% | 0.23% |
| news_api | newswiretoday.com | 3 | 0.10% | 0.23% |
| news_api | politis.com.cy | 3 | 0.10% | 0.23% |
| news_api | portal.sina.com.hk | 3 | 0.10% | 0.23% |
| news_api | prnewswire.com | 3 | 0.10% | 0.23% |
| news_api | securitylab.ru | 3 | 0.10% | 0.23% |
| news_api | time.mk | 3 | 0.10% | 0.23% |
| news_api | ura.news | 3 | 0.10% | 0.23% |
| news_api | womannews.net | 3 | 0.10% | 0.23% |
| news_api | 1prime.ru | 2 | 0.06% | 0.16% |
| news_api | allafrica.com | 2 | 0.06% | 0.16% |
| news_api | am.com.mx | 2 | 0.06% | 0.16% |
| news_api | americanbanker.com | 2 | 0.06% | 0.16% |
| news_api | androidheadlines.com | 2 | 0.06% | 0.16% |
| news_api | antaranews.com | 2 | 0.06% | 0.16% |
| news_api | aol.co.uk | 2 | 0.06% | 0.16% |
| news_api | arkansasonline.com | 2 | 0.06% | 0.16% |
| news_api | bd-pratidin.com | 2 | 0.06% | 0.16% |
| news_api | bjnews.com.cn | 2 | 0.06% | 0.16% |
| news_api | bleepingcomputer.com | 2 | 0.06% | 0.16% |
| news_api | bunburymail.com.au | 2 | 0.06% | 0.16% |
| news_api | businessghana.com | 2 | 0.06% | 0.16% |
| news_api | claimsjournal.com | 2 | 0.06% | 0.16% |
| news_api | cnnturk.com | 2 | 0.06% | 0.16% |
| news_api | computerweekly.com | 2 | 0.06% | 0.16% |
| news_api | dailykos.com | 2 | 0.06% | 0.16% |
| news_api | deadline.com | 2 | 0.06% | 0.16% |
| news_api | digitaljournal.com | 2 | 0.06% | 0.16% |
| news_api | donanimgunlugu.com | 2 | 0.06% | 0.16% |
| news_api | ecodibergamo.it | 2 | 0.06% | 0.16% |
| news_api | eldestapeweb.com | 2 | 0.06% | 0.16% |
| news_api | eldia.com.bo | 2 | 0.06% | 0.16% |
| news_api | elmanana.com | 2 | 0.06% | 0.16% |
| news_api | eturbonews.com | 2 | 0.06% | 0.16% |
| news_api | eurointegration.com.ua | 2 | 0.06% | 0.16% |
| news_api | europapress.es | 2 | 0.06% | 0.16% |
| news_api | fontanka.ru | 2 | 0.06% | 0.16% |
| news_api | fox4news.com | 2 | 0.06% | 0.16% |
| news_api | freemalaysiatoday.com | 2 | 0.06% | 0.16% |
| news_api | geeky-gadgets.com | 2 | 0.06% | 0.16% |
| news_api | github.com | 2 | 0.06% | 0.16% |
| news_api | gizmodo.com | 2 | 0.06% | 0.16% |
| news_api | glavcom.ua | 2 | 0.06% | 0.16% |
| news_api | hawaiitelegraph.com | 2 | 0.06% | 0.16% |
| news_api | hindi.webdunia.com | 2 | 0.06% | 0.16% |
| news_api | hinews.cn | 2 | 0.06% | 0.16% |
| news_api | htxt.co.za | 2 | 0.06% | 0.16% |
| news_api | hurriyetdailynews.com | 2 | 0.06% | 0.16% |
| news_api | index.hr | 2 | 0.06% | 0.16% |
| news_api | infoworld.com | 2 | 0.06% | 0.16% |
| news_api | insight.co.kr | 2 | 0.06% | 0.16% |
| news_api | insurancejournal.com | 2 | 0.06% | 0.16% |
| news_api | investegate.co.uk | 2 | 0.06% | 0.16% |
| news_api | itbear.com.cn | 2 | 0.06% | 0.16% |
| news_api | itnewsonline.com | 2 | 0.06% | 0.16% |
| news_api | itwire.com | 2 | 0.06% | 0.16% |
| news_api | iz.ru | 2 | 0.06% | 0.16% |
| news_api | jawapos.com | 2 | 0.06% | 0.16% |
| news_api | jugantor.com | 2 | 0.06% | 0.16% |
| news_api | lalsace.fr | 2 | 0.06% | 0.16% |
| news_api | lbc.co.uk | 2 | 0.06% | 0.16% |
| news_api | libnanews.com | 2 | 0.06% | 0.16% |
| news_api | life.ru | 2 | 0.06% | 0.16% |
| news_api | livenews.co.nz | 2 | 0.06% | 0.16% |
| news_api | lrytas.lt | 2 | 0.06% | 0.16% |
| news_api | macleayargus.com.au | 2 | 0.06% | 0.16% |
| news_api | marketscreener.com | 2 | 0.06% | 0.16% |
| news_api | medianama.com | 2 | 0.06% | 0.16% |
| news_api | military.china.com | 2 | 0.06% | 0.16% |
| news_api | n.yam.com | 2 | 0.06% | 0.16% |
| news_api | natalie.mu | 2 | 0.06% | 0.16% |
| news_api | natlawreview.com | 2 | 0.06% | 0.16% |
| news_api | news.cn | 2 | 0.06% | 0.16% |
| news_api | newspim.com | 2 | 0.06% | 0.16% |
| news_api | ntdtv.com | 2 | 0.06% | 0.16% |
| news_api | nvi.com.au | 2 | 0.06% | 0.16% |
| news_api | nypost.com | 2 | 0.06% | 0.16% |
| news_api | nzherald.co.nz | 2 | 0.06% | 0.16% |
| news_api | odatv.com | 2 | 0.06% | 0.16% |
| news_api | pcmag.com | 2 | 0.06% | 0.16% |
| news_api | phonandroid.com | 2 | 0.06% | 0.16% |
| news_api | posta.com.tr | 2 | 0.06% | 0.16% |
| news_api | propakistani.pk | 2 | 0.06% | 0.16% |
| news_api | pymnts.com | 2 | 0.06% | 0.16% |
| news_api | russian.rt.com | 2 | 0.06% | 0.16% |
| news_api | sabah.com.tr | 2 | 0.06% | 0.16% |
| news_api | sanantoniopost.com | 2 | 0.06% | 0.16% |
| news_api | sb.by | 2 | 0.06% | 0.16% |
| news_api | scoop.co.nz | 2 | 0.06% | 0.16% |
| news_api | securitybrief.news | 2 | 0.06% | 0.16% |
| news_api | securityinfowatch.com | 2 | 0.06% | 0.16% |
| news_api | sentinel.ht | 2 | 0.06% | 0.16% |
| news_api | shorouknews.com | 2 | 0.06% | 0.16% |
| news_api | stcn.com | 2 | 0.06% | 0.16% |
| news_api | straitstimes.com | 2 | 0.06% | 0.16% |
| news_api | t-online.de | 2 | 0.06% | 0.16% |
| news_api | tech.caijing.com.cn | 2 | 0.06% | 0.16% |
| news_api | tech.ifeng.com | 2 | 0.06% | 0.16% |
| news_api | techweez.com | 2 | 0.06% | 0.16% |
| news_api | theglobeandmail.com | 2 | 0.06% | 0.16% |
| news_api | thehindu.com | 2 | 0.06% | 0.16% |
| news_api | thisdaylive.com | 2 | 0.06% | 0.16% |
| news_api | tmtpost.com | 2 | 0.06% | 0.16% |
| news_api | tn.com.ar | 2 | 0.06% | 0.16% |
| news_api | tomshardware.com | 2 | 0.06% | 0.16% |
| news_api | tribuneindia.com | 2 | 0.06% | 0.16% |
| news_api | vesti.ru | 2 | 0.06% | 0.16% |
| news_api | vg.no | 2 | 0.06% | 0.16% |
| news_api | vietnamnet.vn | 2 | 0.06% | 0.16% |
| news_api | wdrb.com | 2 | 0.06% | 0.16% |
| news_api | webpronews.com | 2 | 0.06% | 0.16% |
| news_api | welivesecurity.com | 2 | 0.06% | 0.16% |
| news_api | weser-kurier.de | 2 | 0.06% | 0.16% |
| news_api | wesh.com | 2 | 0.06% | 0.16% |
| news_api | wfmz.com | 2 | 0.06% | 0.16% |
| news_api | wired.com | 2 | 0.06% | 0.16% |
| news_api | wiwo.de | 2 | 0.06% | 0.16% |
| news_api | 01net.com | 1 | 0.03% | 0.08% |
| news_api | 21stcenturywire.com | 1 | 0.03% | 0.08% |
| news_api | 24sata.hr | 1 | 0.03% | 0.08% |
| news_api | 3c.ltn.com.tw | 1 | 0.03% | 0.08% |
| news_api | 5.ua | 1 | 0.03% | 0.08% |
| news_api | 5newsonline.com | 1 | 0.03% | 0.08% |
| news_api | 961theeagle.com | 1 | 0.03% | 0.08% |
| news_api | abc7news.com | 1 | 0.03% | 0.08% |
| news_api | aceshowbiz.com | 1 | 0.03% | 0.08% |
| news_api | adevarul.ro | 1 | 0.03% | 0.08% |
| news_api | administradores.com.br | 1 | 0.03% | 0.08% |
| news_api | afr.com | 1 | 0.03% | 0.08% |
| news_api | ai.zol.com.cn | 1 | 0.03% | 0.08% |
| news_api | aif.ru | 1 | 0.03% | 0.08% |
| news_api | aktifhaber.com | 1 | 0.03% | 0.08% |
| news_api | aktivni.metropolitan.si | 1 | 0.03% | 0.08% |
| news_api | al-monitor.com | 1 | 0.03% | 0.08% |
| news_api | alanbatnews.net | 1 | 0.03% | 0.08% |
| news_api | alaskasnewssource.com | 1 | 0.03% | 0.08% |
| news_api | aljazeera.com | 1 | 0.03% | 0.08% |
| news_api | aljazeera.net | 1 | 0.03% | 0.08% |
| news_api | amic.ru | 1 | 0.03% | 0.08% |
| news_api | aninews.in | 1 | 0.03% | 0.08% |
| news_api | antena3.ro | 1 | 0.03% | 0.08% |
| news_api | antivirus-sniper.macupdate.com | 1 | 0.03% | 0.08% |
| news_api | arede.info | 1 | 0.03% | 0.08% |
| news_api | aristeguinoticias.com | 1 | 0.03% | 0.08% |
| news_api | armenews.com | 1 | 0.03% | 0.08% |
| news_api | armidaleexpress.com.au | 1 | 0.03% | 0.08% |
| news_api | arstechnica.com | 1 | 0.03% | 0.08% |
| news_api | asahi.com | 1 | 0.03% | 0.08% |
| news_api | austinchronicle.com | 1 | 0.03% | 0.08% |
| news_api | balkanweb.com | 1 | 0.03% | 0.08% |
| news_api | bandaancha.eu | 1 | 0.03% | 0.08% |
| news_api | bangkokbiznews.com | 1 | 0.03% | 0.08% |
| news_api | bangkokpost.com | 1 | 0.03% | 0.08% |
| news_api | bangordailynews.com | 1 | 0.03% | 0.08% |
| news_api | bankier.pl | 1 | 0.03% | 0.08% |
| news_api | bankingnews.gr | 1 | 0.03% | 0.08% |
| news_api | batemansbaypost.com.au | 1 | 0.03% | 0.08% |
| news_api | bbc.com | 1 | 0.03% | 0.08% |
| news_api | beckershospitalreview.com | 1 | 0.03% | 0.08% |
| news_api | begeek.fr | 1 | 0.03% | 0.08% |
| news_api | berliner-zeitung.de | 1 | 0.03% | 0.08% |
| news_api | bernerzeitung.ch | 1 | 0.03% | 0.08% |
| news_api | bgonair.bg | 1 | 0.03% | 0.08% |
| news_api | bgr.com | 1 | 0.03% | 0.08% |
| news_api | bhaskar.com | 1 | 0.03% | 0.08% |
| news_api | birminghamstar.com | 1 | 0.03% | 0.08% |
| news_api | biz.cnews.ru | 1 | 0.03% | 0.08% |
| news_api | bj.xinhuanet.com | 1 | 0.03% | 0.08% |
| news_api | blackseanews.net | 1 | 0.03% | 0.08% |
| news_api | blikk.hu | 1 | 0.03% | 0.08% |
| news_api | bluemountainsgazette.com.au | 1 | 0.03% | 0.08% |
| news_api | bmmagazine.co.uk | 1 | 0.03% | 0.08% |
| news_api | bollywoodlife.com | 1 | 0.03% | 0.08% |
| news_api | borsonline.hu | 1 | 0.03% | 0.08% |
| news_api | botasot.info | 1 | 0.03% | 0.08% |
| news_api | bozemandailychronicle.com | 1 | 0.03% | 0.08% |
| news_api | braidwoodtimes.com.au | 1 | 0.03% | 0.08% |
| news_api | brasil247.com | 1 | 0.03% | 0.08% |
| news_api | bt.no | 1 | 0.03% | 0.08% |
| news_api | buffalobulletin.com | 1 | 0.03% | 0.08% |
| news_api | bug.hr | 1 | 0.03% | 0.08% |
| news_api | bursahakimiyet.com.tr | 1 | 0.03% | 0.08% |
| news_api | business.scoop.co.nz | 1 | 0.03% | 0.08% |
| news_api | business2community.com | 1 | 0.03% | 0.08% |
| news_api | businessday.co.za | 1 | 0.03% | 0.08% |
| news_api | businessinsurance.com | 1 | 0.03% | 0.08% |
| news_api | businesstimes.com.sg | 1 | 0.03% | 0.08% |
| news_api | businesstoday.in | 1 | 0.03% | 0.08% |
| news_api | cafebiz.vn | 1 | 0.03% | 0.08% |
| news_api | californiatelegraph.com | 1 | 0.03% | 0.08% |
| news_api | camdencourier.com.au | 1 | 0.03% | 0.08% |
| news_api | canardpc.com | 1 | 0.03% | 0.08% |
| news_api | capital.ro | 1 | 0.03% | 0.08% |
| news_api | cepro.com | 1 | 0.03% | 0.08% |
| news_api | cfi.net.cn | 1 | 0.03% | 0.08% |
| news_api | channelbuzz.ca | 1 | 0.03% | 0.08% |
| news_api | china.com.cn | 1 | 0.03% | 0.08% |
| news_api | chinanationalnews.com | 1 | 0.03% | 0.08% |
| news_api | chinesepress.com | 1 | 0.03% | 0.08% |
| news_api | chip.de | 1 | 0.03% | 0.08% |
| news_api | circleid.com | 1 | 0.03% | 0.08% |
| news_api | cjme.com | 1 | 0.03% | 0.08% |
| news_api | clarin.com | 1 | 0.03% | 0.08% |
| news_api | closermag.fr | 1 | 0.03% | 0.08% |
| news_api | cloud.watch.impress.co.jp | 1 | 0.03% | 0.08% |
| news_api | clydebankpost.co.uk | 1 | 0.03% | 0.08% |
| news_api | cnet.com | 1 | 0.03% | 0.08% |
| news_api | cnn.com | 1 | 0.03% | 0.08% |
| news_api | collider.com | 1 | 0.03% | 0.08% |
| news_api | coloradostar.com | 1 | 0.03% | 0.08% |
| news_api | comingsoon.it | 1 | 0.03% | 0.08% |
| news_api | comnews.ru | 1 | 0.03% | 0.08% |
| news_api | computerwoche.de | 1 | 0.03% | 0.08% |
| news_api | computerworld.dk | 1 | 0.03% | 0.08% |
| news_api | computerworld.pl | 1 | 0.03% | 0.08% |
| news_api | cootamundraherald.com.au | 1 | 0.03% | 0.08% |
| news_api | corp.cnews.ru | 1 | 0.03% | 0.08% |
| news_api | crookwellgazette.com.au | 1 | 0.03% | 0.08% |
| news_api | daily-tribune.com | 1 | 0.03% | 0.08% |
| news_api | daily.com.ua | 1 | 0.03% | 0.08% |
| news_api | dailyadvertiser.com.au | 1 | 0.03% | 0.08% |
| news_api | dailyemerald.com | 1 | 0.03% | 0.08% |
| news_api | dailyexcelsior.com | 1 | 0.03% | 0.08% |
| news_api | dailymail.co.uk | 1 | 0.03% | 0.08% |
| news_api | dailynews.co.th | 1 | 0.03% | 0.08% |
| news_api | dailypioneer.com | 1 | 0.03% | 0.08% |
| news_api | dailypolitical.com | 1 | 0.03% | 0.08% |
| news_api | dailysabah.com | 1 | 0.03% | 0.08% |
| news_api | dantri.com.vn | 1 | 0.03% | 0.08% |
| news_api | datacenterknowledge.com | 1 | 0.03% | 0.08% |
| news_api | daytondailynews.com | 1 | 0.03% | 0.08% |
| news_api | dcvelocity.com | 1 | 0.03% | 0.08% |
| news_api | de.nachrichten.yahoo.com | 1 | 0.03% | 0.08% |
| news_api | defensenews.com | 1 | 0.03% | 0.08% |
| news_api | deperu.com | 1 | 0.03% | 0.08% |
| news_api | designboom.com | 1 | 0.03% | 0.08% |
| news_api | dha.com.tr | 1 | 0.03% | 0.08% |
| news_api | diario.mx | 1 | 0.03% | 0.08% |
| news_api | diariodemorelos.com | 1 | 0.03% | 0.08% |
| news_api | diariopalentino.es | 1 | 0.03% | 0.08% |
| news_api | diena.lt | 1 | 0.03% | 0.08% |
| news_api | digg.com | 1 | 0.03% | 0.08% |
| news_api | digi.china.com | 1 | 0.03% | 0.08% |
| news_api | digi24.ro | 1 | 0.03% | 0.08% |
| news_api | digitaltrends.com | 1 | 0.03% | 0.08% |
| news_api | directionsmag.com | 1 | 0.03% | 0.08% |
| news_api | divyamarathi.bhaskar.com | 1 | 0.03% | 0.08% |
| news_api | diyarbakirsoz.com | 1 | 0.03% | 0.08% |
| news_api | dna.fr | 1 | 0.03% | 0.08% |
| news_api | dnews.gr | 1 | 0.03% | 0.08% |
| news_api | dominicanrepublicpost.com | 1 | 0.03% | 0.08% |
| news_api | donanimhaber.com | 1 | 0.03% | 0.08% |
| news_api | donews.com | 1 | 0.03% | 0.08% |
| news_api | dotekomanie.cz | 1 | 0.03% | 0.08% |
| news_api | downtoearth.org.in | 1 | 0.03% | 0.08% |
| news_api | dp.ru | 1 | 0.03% | 0.08% |
| news_api | drimble.nl | 1 | 0.03% | 0.08% |
| news_api | dunya.com | 1 | 0.03% | 0.08% |
| news_api | dunyanews.tv | 1 | 0.03% | 0.08% |
| news_api | dw.com | 1 | 0.03% | 0.08% |
| news_api | dynamicbusiness.com | 1 | 0.03% | 0.08% |
| news_api | ec.ltn.com.tw | 1 | 0.03% | 0.08% |
| news_api | economx.hu | 1 | 0.03% | 0.08% |
| news_api | edition.cnn.com | 1 | 0.03% | 0.08% |
| news_api | eejournal.com | 1 | 0.03% | 0.08% |
| news_api | elcomercio.es | 1 | 0.03% | 0.08% |
| news_api | elconfidencial.com | 1 | 0.03% | 0.08% |
| news_api | eldia.es | 1 | 0.03% | 0.08% |
| news_api | eldiariodechihuahua.mx | 1 | 0.03% | 0.08% |
| news_api | elektroniknet.de | 1 | 0.03% | 0.08% |
| news_api | elpais.com.uy | 1 | 0.03% | 0.08% |
| news_api | elperiodicodearagon.com | 1 | 0.03% | 0.08% |
| news_api | elsiglodetorreon.com.mx | 1 | 0.03% | 0.08% |
| news_api | eluniversal.com.mx | 1 | 0.03% | 0.08% |
| news_api | eluniverso.com | 1 | 0.03% | 0.08% |
| news_api | elwatannews.com | 1 | 0.03% | 0.08% |
| news_api | english.pravda.ru | 1 | 0.03% | 0.08% |
| news_api | etnews.com | 1 | 0.03% | 0.08% |
| news_api | etoday.co.kr | 1 | 0.03% | 0.08% |
| news_api | ettoday.net | 1 | 0.03% | 0.08% |
| news_api | europesun.com | 1 | 0.03% | 0.08% |
| news_api | evrensel.net | 1 | 0.03% | 0.08% |
| news_api | excite.co.jp | 1 | 0.03% | 0.08% |
| news_api | explosion.com | 1 | 0.03% | 0.08% |
| news_api | express.pk | 1 | 0.03% | 0.08% |
| news_api | extra.ec | 1 | 0.03% | 0.08% |
| news_api | fakti.bg | 1 | 0.03% | 0.08% |
| news_api | fatimanews.com.br | 1 | 0.03% | 0.08% |
| news_api | fedpress.ru | 1 | 0.03% | 0.08% |
| news_api | femina.hu | 1 | 0.03% | 0.08% |
| news_api | finance.ifeng.com | 1 | 0.03% | 0.08% |
| news_api | financial-news.co.uk | 1 | 0.03% | 0.08% |
| news_api | firstpost.com | 1 | 0.03% | 0.08% |
| news_api | fnp.de | 1 | 0.03% | 0.08% |
| news_api | fox17online.com | 1 | 0.03% | 0.08% |
| news_api | fox43.com | 1 | 0.03% | 0.08% |
| news_api | fox9.com | 1 | 0.03% | 0.08% |
| news_api | freiepresse.de | 1 | 0.03% | 0.08% |
| news_api | funkytaurusmedia.com | 1 | 0.03% | 0.08% |
| news_api | futures.cnfol.com | 1 | 0.03% | 0.08% |
| news_api | gadgetsmagazine.com.ph | 1 | 0.03% | 0.08% |
| news_api | gamerant.com | 1 | 0.03% | 0.08% |
| news_api | generation-nt.com | 1 | 0.03% | 0.08% |
| news_api | georgeherald.com | 1 | 0.03% | 0.08% |
| news_api | ghanaiantimes.com.gh | 1 | 0.03% | 0.08% |
| news_api | ghanamma.com | 1 | 0.03% | 0.08% |
| news_api | gorod48.ru | 1 | 0.03% | 0.08% |
| news_api | governing.com | 1 | 0.03% | 0.08% |
| news_api | groundup.org.za | 1 | 0.03% | 0.08% |
| news_api | gulte.com | 1 | 0.03% | 0.08% |
| news_api | haber1.com | 1 | 0.03% | 0.08% |
| news_api | haber3.com | 1 | 0.03% | 0.08% |
| news_api | haberturk.com | 1 | 0.03% | 0.08% |
| news_api | hachettebookgroup.com | 1 | 0.03% | 0.08% |
| news_api | haksozhaber.net | 1 | 0.03% | 0.08% |
| news_api | handelsblatt.com | 1 | 0.03% | 0.08% |
| news_api | hani.co.kr | 1 | 0.03% | 0.08% |
| news_api | helpconsumatori.it | 1 | 0.03% | 0.08% |
| news_api | heute.at | 1 | 0.03% | 0.08% |
| news_api | hirek.prim.hu | 1 | 0.03% | 0.08% |
| news_api | hollywoodreporter.com | 1 | 0.03% | 0.08% |
| news_api | hydrocarbonprocessing.com | 1 | 0.03% | 0.08% |
| news_api | ibtimes.co.uk | 1 | 0.03% | 0.08% |
| news_api | ibtimes.com.au | 1 | 0.03% | 0.08% |
| news_api | icij.org | 1 | 0.03% | 0.08% |
| news_api | idiva.com | 1 | 0.03% | 0.08% |
| news_api | idnes.cz | 1 | 0.03% | 0.08% |
| news_api | igamingbusiness.com | 1 | 0.03% | 0.08% |
| news_api | ihalla.com | 1 | 0.03% | 0.08% |
| news_api | illawarramercury.com.au | 1 | 0.03% | 0.08% |
| news_api | index.hu | 1 | 0.03% | 0.08% |
| news_api | india.com | 1 | 0.03% | 0.08% |
| news_api | indiatvnews.com | 1 | 0.03% | 0.08% |
| news_api | inews24.com | 1 | 0.03% | 0.08% |
| news_api | inewsgr.com | 1 | 0.03% | 0.08% |
| news_api | infobae.com | 1 | 0.03% | 0.08% |
| news_api | informationweek.com | 1 | 0.03% | 0.08% |
| news_api | inforum.com | 1 | 0.03% | 0.08% |
| news_api | infotechlead.com | 1 | 0.03% | 0.08% |
| news_api | inosmi.ru | 1 | 0.03% | 0.08% |
| news_api | inquirer.com | 1 | 0.03% | 0.08% |
| news_api | insideottawavalley.com | 1 | 0.03% | 0.08% |
| news_api | insight.scmagazineuk.com | 1 | 0.03% | 0.08% |
| news_api | interaksyon.philstar.com | 1 | 0.03% | 0.08% |
| news_api | internetua.com | 1 | 0.03% | 0.08% |
| news_api | inverelltimes.com.au | 1 | 0.03% | 0.08% |
| news_api | investorplace.com | 1 | 0.03% | 0.08% |
| news_api | inwestycje.pl | 1 | 0.03% | 0.08% |
| news_api | iraqsun.com | 1 | 0.03% | 0.08% |
| news_api | irishdentist.ie | 1 | 0.03% | 0.08% |
| news_api | island.lk | 1 | 0.03% | 0.08% |
| news_api | it.euronews.com | 1 | 0.03% | 0.08% |
| news_api | itbrief.news | 1 | 0.03% | 0.08% |
| news_api | itnewsafrica.com | 1 | 0.03% | 0.08% |
| news_api | jabar.tribunnews.com | 1 | 0.03% | 0.08% |
| news_api | jagranjosh.com | 1 | 0.03% | 0.08% |
| news_api | jamaicaobserver.com | 1 | 0.03% | 0.08% |
| news_api | japan.cnet.com | 1 | 0.03% | 0.08% |
| news_api | jo24.net | 1 | 0.03% | 0.08% |
| news_api | jogja.tribunnews.com | 1 | 0.03% | 0.08% |
| news_api | journal-news.com | 1 | 0.03% | 0.08% |
| news_api | journalgazette.net | 1 | 0.03% | 0.08% |
| news_api | jowhar.com | 1 | 0.03% | 0.08% |
| news_api | jpnn.com | 1 | 0.03% | 0.08% |
| news_api | jpost.com | 1 | 0.03% | 0.08% |
| news_api | juneesoutherncross.com.au | 1 | 0.03% | 0.08% |
| news_api | kannadaprabha.com | 1 | 0.03% | 0.08% |
| news_api | kaos911.com | 1 | 0.03% | 0.08% |
| news_api | kcci.com | 1 | 0.03% | 0.08% |
| news_api | kesq.com | 1 | 0.03% | 0.08% |
| news_api | king5.com | 1 | 0.03% | 0.08% |
| news_api | kingfm.com | 1 | 0.03% | 0.08% |
| news_api | kmbc.com | 1 | 0.03% | 0.08% |
| news_api | kmib.co.kr | 1 | 0.03% | 0.08% |
| news_api | ko.com.ua | 1 | 0.03% | 0.08% |
| news_api | kob.com | 1 | 0.03% | 0.08% |
| news_api | koco.com | 1 | 0.03% | 0.08% |
| news_api | kommersant.ru | 1 | 0.03% | 0.08% |
| news_api | kontrakty.ua | 1 | 0.03% | 0.08% |
| news_api | koreatimes.co.kr | 1 | 0.03% | 0.08% |
| news_api | kotaku.com | 1 | 0.03% | 0.08% |
| news_api | kristv.com | 1 | 0.03% | 0.08% |
| news_api | kten.com | 1 | 0.03% | 0.08% |
| news_api | ktvu.com | 1 | 0.03% | 0.08% |
| news_api | kztv10.com | 1 | 0.03% | 0.08% |
| news_api | lafranceagricole.fr | 1 | 0.03% | 0.08% |
| news_api | lagacetadesalamanca.es | 1 | 0.03% | 0.08% |
| news_api | lakersnation.com | 1 | 0.03% | 0.08% |
| news_api | laosnews.net | 1 | 0.03% | 0.08% |
| news_api | laprovincia.es | 1 | 0.03% | 0.08% |
| news_api | larepubliquedespyrenees.fr | 1 | 0.03% | 0.08% |
| news_api | laut.de | 1 | 0.03% | 0.08% |
| news_api | lavozdegalicia.es | 1 | 0.03% | 0.08% |
| news_api | ledauphine.com | 1 | 0.03% | 0.08% |
| news_api | lefigaro.fr | 1 | 0.03% | 0.08% |
| news_api | legalinsurrection.com | 1 | 0.03% | 0.08% |
| news_api | lejsl.com | 1 | 0.03% | 0.08% |
| news_api | lenta.ru | 1 | 0.03% | 0.08% |
| news_api | lexpress.fr | 1 | 0.03% | 0.08% |
| news_api | lgz.ru | 1 | 0.03% | 0.08% |
| news_api | lina.sh | 1 | 0.03% | 0.08% |
| news_api | linux.org.ru | 1 | 0.03% | 0.08% |
| news_api | liputan6.com | 1 | 0.03% | 0.08% |
| news_api | lite987.com | 1 | 0.03% | 0.08% |
| news_api | lithgowmercury.com.au | 1 | 0.03% | 0.08% |
| news_api | livehindustan.com | 1 | 0.03% | 0.08% |
| news_api | livemint.com | 1 | 0.03% | 0.08% |
| news_api | local12.com | 1 | 0.03% | 0.08% |
| news_api | localnews8.com | 1 | 0.03% | 0.08% |
| news_api | loksatta.com | 1 | 0.03% | 0.08% |
| news_api | ly.fjsen.com | 1 | 0.03% | 0.08% |
| news_api | maharashtratimes.com | 1 | 0.03% | 0.08% |
| news_api | makassar.tribunnews.com | 1 | 0.03% | 0.08% |
| news_api | makeuseof.com | 1 | 0.03% | 0.08% |
| news_api | mandurahmail.com.au | 1 | 0.03% | 0.08% |
| news_api | manningrivertimes.com.au | 1 | 0.03% | 0.08% |
| news_api | marca.com | 1 | 0.03% | 0.08% |
| news_api | mariettatimes.com | 1 | 0.03% | 0.08% |
| news_api | marketintelligencecenter.com | 1 | 0.03% | 0.08% |
| news_api | mashable.com | 1 | 0.03% | 0.08% |
| news_api | massachusettssun.com | 1 | 0.03% | 0.08% |
| news_api | mathrubhumi.com | 1 | 0.03% | 0.08% |
| news_api | megamodo.com | 1 | 0.03% | 0.08% |
| news_api | memeburn.com | 1 | 0.03% | 0.08% |
| news_api | meridiano.net | 1 | 0.03% | 0.08% |
| news_api | mersinhaber.com | 1 | 0.03% | 0.08% |
| news_api | metronews.ru | 1 | 0.03% | 0.08% |
| news_api | metroseoul.co.kr | 1 | 0.03% | 0.08% |
| news_api | michigandaily.com | 1 | 0.03% | 0.08% |
| news_api | mirrorspectator.com | 1 | 0.03% | 0.08% |
| news_api | mississauga.com | 1 | 0.03% | 0.08% |
| news_api | mittelstandcafe.de | 1 | 0.03% | 0.08% |
| news_api | mngz.ru | 1 | 0.03% | 0.08% |
| news_api | mobile.zol.com.cn | 1 | 0.03% | 0.08% |
| news_api | mobileidworld.com | 1 | 0.03% | 0.08% |
| news_api | money.it | 1 | 0.03% | 0.08% |
| news_api | mp.cnfol.com | 1 | 0.03% | 0.08% |
| news_api | mskagency.ru | 1 | 0.03% | 0.08% |
| news_api | mudgeeguardian.com.au | 1 | 0.03% | 0.08% |
| news_api | mundoenlinea.cl | 1 | 0.03% | 0.08% |
| news_api | myanmarnews.net | 1 | 0.03% | 0.08% |
| news_api | n-tv.de | 1 | 0.03% | 0.08% |
| news_api | naftemporiki.gr | 1 | 0.03% | 0.08% |
| news_api | nashvilleherald.com | 1 | 0.03% | 0.08% |
| news_api | nationalmortgagenews.com | 1 | 0.03% | 0.08% |
| news_api | navbharattimes.indiatimes.com | 1 | 0.03% | 0.08% |
| news_api | nbcmontana.com | 1 | 0.03% | 0.08% |
| news_api | nbd.com.cn | 1 | 0.03% | 0.08% |
| news_api | nearshoreamericas.com | 1 | 0.03% | 0.08% |
| news_api | net.hr | 1 | 0.03% | 0.08% |
| news_api | newcastleherald.com.au | 1 | 0.03% | 0.08% |
| news_api | newrepublic.com | 1 | 0.03% | 0.08% |
| news_api | news.china.com.cn | 1 | 0.03% | 0.08% |
| news_api | news.cnfol.com | 1 | 0.03% | 0.08% |
| news_api | news.ltn.com.tw | 1 | 0.03% | 0.08% |
| news_api | news.tuoitre.vn | 1 | 0.03% | 0.08% |
| news_api | news.ycwb.com | 1 | 0.03% | 0.08% |
| news_api | news8000.com | 1 | 0.03% | 0.08% |
| news_api | newsbomb.gr | 1 | 0.03% | 0.08% |
| news_api | newstribune.com | 1 | 0.03% | 0.08% |
| news_api | newsweek.com | 1 | 0.03% | 0.08% |
| news_api | newsx.com | 1 | 0.03% | 0.08% |
| news_api | newtalk.tw | 1 | 0.03% | 0.08% |
| news_api | newyorkstatesman.com | 1 | 0.03% | 0.08% |
| news_api | niagarathisweek.com | 1 | 0.03% | 0.08% |
| news_api | nieuws.nl | 1 | 0.03% | 0.08% |
| news_api | nikkan.co.jp | 1 | 0.03% | 0.08% |
| news_api | nikkei.com | 1 | 0.03% | 0.08% |
| news_api | nj.com | 1 | 0.03% | 0.08% |
| news_api | norran.se | 1 | 0.03% | 0.08% |
| news_api | northcountrynow.com | 1 | 0.03% | 0.08% |
| news_api | northerndailyleader.com.au | 1 | 0.03% | 0.08% |
| news_api | northweststar.com.au | 1 | 0.03% | 0.08% |
| news_api | nrc.nl | 1 | 0.03% | 0.08% |
| news_api | ntv.com.tr | 1 | 0.03% | 0.08% |
| news_api | nwaonline.com | 1 | 0.03% | 0.08% |
| news_api | ohmynews.com | 1 | 0.03% | 0.08% |
| news_api | ondacero.es | 1 | 0.03% | 0.08% |
| news_api | op-online.de | 1 | 0.03% | 0.08% |
| news_api | openpr.com | 1 | 0.03% | 0.08% |
| news_api | ottawacitizen.com | 1 | 0.03% | 0.08% |
| news_api | pakistantelegraph.com | 1 | 0.03% | 0.08% |
| news_api | panorama.com.al | 1 | 0.03% | 0.08% |
| news_api | pcwplus.hu | 1 | 0.03% | 0.08% |
| news_api | photo.china.com.cn | 1 | 0.03% | 0.08% |
| news_api | pitchfork.com | 1 | 0.03% | 0.08% |
| news_api | pjmedia.com | 1 | 0.03% | 0.08% |
| news_api | playground.ru | 1 | 0.03% | 0.08% |
| news_api | pln-pskov.ru | 1 | 0.03% | 0.08% |
| news_api | podrobnosti.ua | 1 | 0.03% | 0.08% |
| news_api | politika.rs | 1 | 0.03% | 0.08% |
| news_api | polygon.com | 1 | 0.03% | 0.08% |
| news_api | portalsamorzadowy.pl | 1 | 0.03% | 0.08% |
| news_api | portnews.com.au | 1 | 0.03% | 0.08% |
| news_api | posttoday.com | 1 | 0.03% | 0.08% |
| news_api | pr.com | 1 | 0.03% | 0.08% |
| news_api | press24.mk | 1 | 0.03% | 0.08% |
| news_api | presse-citron.net | 1 | 0.03% | 0.08% |
| news_api | presstv.ir | 1 | 0.03% | 0.08% |
| news_api | primerafuente.com.ar | 1 | 0.03% | 0.08% |
| news_api | profitline.hu | 1 | 0.03% | 0.08% |
| news_api | publico.pt | 1 | 0.03% | 0.08% |
| news_api | punchng.com | 1 | 0.03% | 0.08% |
| news_api | punjabitribuneonline.com | 1 | 0.03% | 0.08% |
| news_api | pv-magazine.com | 1 | 0.03% | 0.08% |
| news_api | quadratin.com.mx | 1 | 0.03% | 0.08% |
| news_api | rappler.com | 1 | 0.03% | 0.08% |
| news_api | ratopati.com | 1 | 0.03% | 0.08% |
| news_api | rediff.com | 1 | 0.03% | 0.08% |
| news_api | regions.ru | 1 | 0.03% | 0.08% |
| news_api | republicain-lorrain.fr | 1 | 0.03% | 0.08% |
| news_api | republikein.com.na | 1 | 0.03% | 0.08% |
| news_api | ria.ru | 1 | 0.03% | 0.08% |
| news_api | riasv.ru | 1 | 0.03% | 0.08% |
| news_api | risky.biz | 1 | 0.03% | 0.08% |
| news_api | rnz.co.nz | 1 | 0.03% | 0.08% |
| news_api | rte.ie | 1 | 0.03% | 0.08% |
| news_api | rtl.nl | 1 | 0.03% | 0.08% |
| news_api | ruhrnachrichten.de | 1 | 0.03% | 0.08% |
| news_api | ryt9.com | 1 | 0.03% | 0.08% |
| news_api | saltlakecitysun.com | 1 | 0.03% | 0.08% |
| news_api | saltwire.com | 1 | 0.03% | 0.08% |
| news_api | salzburg24.at | 1 | 0.03% | 0.08% |
| news_api | sana.sy | 1 | 0.03% | 0.08% |
| news_api | sc.stock.cnfol.com | 1 | 0.03% | 0.08% |
| news_api | scroll.in | 1 | 0.03% | 0.08% |
| news_api | sdpnoticias.com | 1 | 0.03% | 0.08% |
| news_api | segye.com | 1 | 0.03% | 0.08% |
| news_api | senego.com | 1 | 0.03% | 0.08% |
| news_api | setn.com | 1 | 0.03% | 0.08% |
| news_api | siliconrepublic.com | 1 | 0.03% | 0.08% |
| news_api | simcoe.com | 1 | 0.03% | 0.08% |
| news_api | slguardian.org | 1 | 0.03% | 0.08% |
| news_api | sn.at | 1 | 0.03% | 0.08% |
| news_api | southernhighlandnews.com.au | 1 | 0.03% | 0.08% |
| news_api | sozcu.com.tr | 1 | 0.03% | 0.08% |
| news_api | spacedaily.com | 1 | 0.03% | 0.08% |
| news_api | spartanavenue.com | 1 | 0.03% | 0.08% |
| news_api | srilankasource.com | 1 | 0.03% | 0.08% |
| news_api | statecollege.com | 1 | 0.03% | 0.08% |
| news_api | stcatharinesstandard.ca | 1 | 0.03% | 0.08% |
| news_api | stern.de | 1 | 0.03% | 0.08% |
| news_api | stlouisstar.com | 1 | 0.03% | 0.08% |
| news_api | stock.hexun.com | 1 | 0.03% | 0.08% |
| news_api | stockbiz.vn | 1 | 0.03% | 0.08% |
| news_api | strategypage.com | 1 | 0.03% | 0.08% |
| news_api | sueddeutsche.de | 1 | 0.03% | 0.08% |
| news_api | tagesanzeiger.ch | 1 | 0.03% | 0.08% |
| news_api | tagesschau.de | 1 | 0.03% | 0.08% |
| news_api | tagesspiegel.de | 1 | 0.03% | 0.08% |
| news_api | tass.ru | 1 | 0.03% | 0.08% |
| news_api | tech.china.com | 1 | 0.03% | 0.08% |
| news_api | techcabal.com | 1 | 0.03% | 0.08% |
| news_api | techstory.in | 1 | 0.03% | 0.08% |
| news_api | techtimes.com | 1 | 0.03% | 0.08% |
| news_api | tecmundo.com.br | 1 | 0.03% | 0.08% |
| news_api | tecnoandroid.it | 1 | 0.03% | 0.08% |
| news_api | tekniikkatalous.fi | 1 | 0.03% | 0.08% |
| news_api | tennesseedaily.com | 1 | 0.03% | 0.08% |
| news_api | tgrthaber.com | 1 | 0.03% | 0.08% |
| news_api | theblaze.com | 1 | 0.03% | 0.08% |
| news_api | thecourier.com.au | 1 | 0.03% | 0.08% |
| news_api | thefrontierpost.com | 1 | 0.03% | 0.08% |
| news_api | thehindubusinessline.com | 1 | 0.03% | 0.08% |
| news_api | thejournal.com | 1 | 0.03% | 0.08% |
| news_api | theleader.com.au | 1 | 0.03% | 0.08% |
| news_api | themissouritimes.com | 1 | 0.03% | 0.08% |
| news_api | themoscowtimes.com | 1 | 0.03% | 0.08% |
| news_api | thenational.scot | 1 | 0.03% | 0.08% |
| news_api | thenextweb.com | 1 | 0.03% | 0.08% |
| news_api | thepeterboroughexaminer.com | 1 | 0.03% | 0.08% |
| news_api | therecord.com | 1 | 0.03% | 0.08% |
| news_api | thesunchronicle.com | 1 | 0.03% | 0.08% |
| news_api | thetoc.gr | 1 | 0.03% | 0.08% |
| news_api | theverge.com | 1 | 0.03% | 0.08% |
| news_api | ticweb.es | 1 | 0.03% | 0.08% |
| news_api | timeslive.co.za | 1 | 0.03% | 0.08% |
| news_api | tivi.fi | 1 | 0.03% | 0.08% |
| news_api | top-channel.tv | 1 | 0.03% | 0.08% |
| news_api | toronto.citynews.ca | 1 | 0.03% | 0.08% |
| news_api | torquenews.com | 1 | 0.03% | 0.08% |
| news_api | totaltele.com | 1 | 0.03% | 0.08% |
| news_api | travelweekly.com.au | 1 | 0.03% | 0.08% |
| news_api | trthaber.com | 1 | 0.03% | 0.08% |
| news_api | trustedreviews.com | 1 | 0.03% | 0.08% |
| news_api | turkiyegazetesi.com.tr | 1 | 0.03% | 0.08% |
| news_api | twincities.com | 1 | 0.03% | 0.08% |
| news_api | uainfo.org | 1 | 0.03% | 0.08% |
| news_api | udn.com | 1 | 0.03% | 0.08% |
| news_api | ukrinform.ua | 1 | 0.03% | 0.08% |
| news_api | unian.net | 1 | 0.03% | 0.08% |
| news_api | unternehmen-heute.de | 1 | 0.03% | 0.08% |
| news_api | upi.com | 1 | 0.03% | 0.08% |
| news_api | us.cnn.com | 1 | 0.03% | 0.08% |
| news_api | utilitydive.com | 1 | 0.03% | 0.08% |
| news_api | utv.ie | 1 | 0.03% | 0.08% |
| news_api | vecer.com | 1 | 0.03% | 0.08% |
| news_api | vecernji.ba | 1 | 0.03% | 0.08% |
| news_api | vedomosti.ru | 1 | 0.03% | 0.08% |
| news_api | vesti-ua.net | 1 | 0.03% | 0.08% |
| news_api | vm.ru | 1 | 0.03% | 0.08% |
| news_api | volksstimme.de | 1 | 0.03% | 0.08% |
| news_api | vrt.be | 1 | 0.03% | 0.08% |
| news_api | wallstreet-online.de | 1 | 0.03% | 0.08% |
| news_api | war.obozrevatel.com | 1 | 0.03% | 0.08% |
| news_api | watoday.com.au | 1 | 0.03% | 0.08% |
| news_api | watson.ch | 1 | 0.03% | 0.08% |
| news_api | wbaltv.com | 1 | 0.03% | 0.08% |
| news_api | wcbi.com | 1 | 0.03% | 0.08% |
| news_api | wdsu.com | 1 | 0.03% | 0.08% |
| news_api | webinars.govtech.com | 1 | 0.03% | 0.08% |
| news_api | weekend.perfil.com | 1 | 0.03% | 0.08% |
| news_api | welt.de | 1 | 0.03% | 0.08% |
| news_api | wgna.com | 1 | 0.03% | 0.08% |
| news_api | whmi.com | 1 | 0.03% | 0.08% |
| news_api | wibx950.com | 1 | 0.03% | 0.08% |
| news_api | winfuture.de | 1 | 0.03% | 0.08% |
| news_api | wlox.com | 1 | 0.03% | 0.08% |
| news_api | wlwt.com | 1 | 0.03% | 0.08% |
| news_api | wmur.com | 1 | 0.03% | 0.08% |
| news_api | words.filippo.io | 1 | 0.03% | 0.08% |
| news_api | world.kbs.co.kr | 1 | 0.03% | 0.08% |
| news_api | wowo.com | 1 | 0.03% | 0.08% |
| news_api | wsbtv.com | 1 | 0.03% | 0.08% |
| news_api | wthr.com | 1 | 0.03% | 0.08% |
| news_api | wtsp.com | 1 | 0.03% | 0.08% |
| news_api | wusa9.com | 1 | 0.03% | 0.08% |
| news_api | wvtm13.com | 1 | 0.03% | 0.08% |
| news_api | wwltv.com | 1 | 0.03% | 0.08% |
| news_api | wwmt.com | 1 | 0.03% | 0.08% |
| news_api | wwwhatsnew.com | 1 | 0.03% | 0.08% |
| news_api | wxii12.com | 1 | 0.03% | 0.08% |
| news_api | wzzm13.com | 1 | 0.03% | 0.08% |
| news_api | y95country.com | 1 | 0.03% | 0.08% |
| news_api | yasstribune.com.au | 1 | 0.03% | 0.08% |
| news_api | yeniakit.com.tr | 1 | 0.03% | 0.08% |
| news_api | yeniasya.com.tr | 1 | 0.03% | 0.08% |
| news_api | yn.xinhuanet.com | 1 | 0.03% | 0.08% |
| news_api | yorkpress.co.uk | 1 | 0.03% | 0.08% |
| news_api | yorkregion.com | 1 | 0.03% | 0.08% |
| news_api | zazoom.it | 1 | 0.03% | 0.08% |
| news_api | zdnet.com | 1 | 0.03% | 0.08% |
| news_api | zeit.de | 1 | 0.03% | 0.08% |
| news_api | zetatijuana.com | 1 | 0.03% | 0.08% |
| news_api | zonebourse.com | 1 | 0.03% | 0.08% |

## Top 30 Inspection Words By source_type

### cve

vulnerability (967), file (413), kernel (369), may (348), issue (339), fix (328), exploit (321), attackers (319), function (299), linux (288), used (287), following (285), resolved (270), attacker (268), attack (266), user (259), allows (257), access (253), manipulation (248), code (234), path (229), arbitrary (221), remote (207), argument (205), component (201), prior (196), version (194), data (192), system (189), affected (186)

### news_api

data (71), security (68), new (58), breach (53), cyber (49), malware (46), ransomware (44), ddos (44), cyberattack (43), attack (43), says (35), rebel (31), scam (28), amid (28), google (27), threat (27), hackers (26), report (25), attacks (24), party (24), zero (23), third (23), day (22), cybersecurity (21), news (21), hit (20), exploit (20), supply (19), chain (19), claude (19)

### news_rss

vulnerability (501), security (391), exploitation (379), windows (361), data (311), likely (299), access (280), less (237), process (226), privilege (203), code (201), elevation (198), file (187), new (185), system (175), exploit (173), microsoft (170), vulnerabilities (167), one (164), also (161), used (161), pointer (159), teams (155), buffer (150), user (149), using (147), attack (143), execution (142), would (135), function (132)

### reddit_rss

link (409), comments (401), submitted (393), like (144), use (109), security (102), would (89), one (82), data (79), https (77), anyone (73), system (69), time (69), still (68), new (68), windows (68), using (66), code (66), know (61), work (60), also (60), com (59), actually (58), people (58), something (58), access (57), don (56), years (54), need (53), even (51)
