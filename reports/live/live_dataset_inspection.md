# Live Dataset Inspection

Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.

## Summary

| Metric | Value |
| --- | --- |
| Total rows | 2603 |
| created_at min | 2025-12-16T09:00:00Z |
| created_at max | 2026-04-30T10:52:33Z |
| collected_at min | 2026-04-29T13:22:42Z |
| collected_at max | 2026-04-30T10:55:06Z |
| Unparsable created_at | 0 (0.00%) |
| Unparsable collected_at | 0 (0.00%) |
| Null/empty text_raw | 0 (0.00%) |
| Mean text_raw length | 636.39 |
| Median text_raw length | 302.0 |
| Min text_raw length | 9 |
| Max text_raw length | 66525 |
| text_raw < 30 chars | 44 (1.69%) |
| text_raw < 100 chars | 759 (29.16%) |
| Duplicate id rows | 0 rows / 0 values |
| Duplicate url rows | 0 rows / 0 values |
| Duplicate normalized text_raw rows | 127 rows / 44 values |

## Warnings

- WARNING: Duplicate normalized text_raw rows found: 127.

## Rows By source_type

| source_type | rows | percent_dataset |
| --- | --- | --- |
| cve | 1295 | 49.75% |
| news_api | 783 | 30.08% |
| reddit_rss | 367 | 14.10% |
| news_rss | 158 | 6.07% |

## Rows By source_name

| source_name | rows | percent_dataset |
| --- | --- | --- |
| NVD CVE | 1295 | 49.75% |
| The Hacker News | 54 | 2.07% |
| cybersecurity | 50 | 1.92% |
| sysadmin | 50 | 1.92% |
| privacy | 40 | 1.54% |
| blueteamsec | 38 | 1.46% |
| netsec | 29 | 1.11% |
| hacking | 28 | 1.08% |
| AskNetsec | 27 | 1.04% |
| ReverseEngineering | 27 | 1.04% |
| osint | 27 | 1.04% |
| Malware | 26 | 1.00% |
| ComputerSecurity | 25 | 0.96% |
| Rapid7 Blog | 22 | 0.85% |
| techradar.com | 22 | 0.85% |
| BleepingComputer | 21 | 0.81% |
| cnews.ru | 19 | 0.73% |
| forbes.com | 17 | 0.65% |
| ithome.com.tw | 17 | 0.65% |
| Cisco Talos Blog | 15 | 0.58% |
| Unit 42 | 15 | 0.58% |
| ascii.jp | 14 | 0.54% |
| SANS Internet Storm Center | 12 | 0.46% |
| finance.sina.com.cn | 11 | 0.42% |
| 163.com | 11 | 0.42% |
| KrebsOnSecurity | 10 | 0.38% |
| Google Project Zero | 9 | 0.35% |
| cointelegraph.com | 9 | 0.35% |
| esecurityplanet.com | 8 | 0.31% |
| infosecurity-magazine.com | 7 | 0.27% |
| techcrunch.com | 7 | 0.27% |
| csoonline.com | 6 | 0.23% |
| bankinfosecurity.com | 6 | 0.23% |
| moneycontrol.com | 6 | 0.23% |
| timesofindia.indiatimes.com | 6 | 0.23% |
| laopcion.com.mx | 6 | 0.23% |
| baijiahao.baidu.com | 6 | 0.23% |
| udayavani.com | 6 | 0.23% |
| tvguide.co.uk | 6 | 0.23% |
| finanznachrichten.de | 5 | 0.19% |
| yahoo.com | 5 | 0.19% |
| itbrief.co.nz | 5 | 0.19% |
| biz.heraldcorp.com | 5 | 0.19% |
| hothardware.com | 4 | 0.15% |
| manilatimes.net | 4 | 0.15% |
| govtech.com | 4 | 0.15% |
| economictimes.indiatimes.com | 4 | 0.15% |
| haberler.com | 4 | 0.15% |
| zdnet.co.kr | 4 | 0.15% |
| vz.ru | 4 | 0.15% |
| coindesk.com | 4 | 0.15% |
| 9to5mac.com | 4 | 0.15% |
| theregister.com | 4 | 0.15% |
| jdsupra.com | 3 | 0.12% |
| finance.yahoo.com | 3 | 0.12% |
| androidauthority.com | 3 | 0.12% |
| ura.news | 3 | 0.12% |
| thenews.com.pk | 3 | 0.12% |
| ensonhaber.com | 3 | 0.12% |
| womannews.net | 3 | 0.12% |
| thefastmode.com | 3 | 0.12% |
| edaily.co.kr | 3 | 0.12% |
| politis.com.cy | 3 | 0.12% |
| aa.com.tr | 3 | 0.12% |
| kibrispostasi.com | 3 | 0.12% |
| bleedingcool.com | 3 | 0.12% |
| screenrant.com | 3 | 0.12% |
| finance.eastmoney.com | 3 | 0.12% |
| heise.de | 3 | 0.12% |
| dostor.org | 3 | 0.12% |
| newswiretoday.com | 3 | 0.12% |
| boredpanda.com | 3 | 0.12% |
| divyabhaskar.co.in | 3 | 0.12% |
| japan.zdnet.com | 2 | 0.08% |
| digitaljournal.com | 2 | 0.08% |
| gizmodo.com | 2 | 0.08% |
| insurancejournal.com | 2 | 0.08% |
| insurancebusinessmag.com | 2 | 0.08% |
| computerweekly.com | 2 | 0.08% |
| winnipegfreepress.com | 2 | 0.08% |
| mondaq.com | 2 | 0.08% |
| bleepingcomputer.com | 2 | 0.08% |
| phonandroid.com | 2 | 0.08% |
| propakistani.pk | 2 | 0.08% |
| pcmag.com | 2 | 0.08% |
| milliyet.com.tr | 2 | 0.08% |
| github.com | 2 | 0.08% |
| sb.by | 2 | 0.08% |
| freemalaysiatoday.com | 2 | 0.08% |
| ddaily.co.kr | 2 | 0.08% |
| channellife.com.au | 2 | 0.08% |
| wesh.com | 2 | 0.08% |
| iz.ru | 2 | 0.08% |
| glavcom.ua | 2 | 0.08% |
| bunburymail.com.au | 2 | 0.08% |
| nvi.com.au | 2 | 0.08% |
| straitstimes.com | 2 | 0.08% |
| lalsace.fr | 2 | 0.08% |
| elmanana.com | 2 | 0.08% |
| news.cn | 2 | 0.08% |
| wiwo.de | 2 | 0.08% |
| wdrb.com | 2 | 0.08% |
| n.yam.com | 2 | 0.08% |
| bd-pratidin.com | 2 | 0.08% |
| hurriyetdailynews.com | 2 | 0.08% |
| wfmz.com | 2 | 0.08% |
| hinews.cn | 2 | 0.08% |
| tech.caijing.com.cn | 2 | 0.08% |
| tech.ifeng.com | 2 | 0.08% |
| androidheadlines.com | 2 | 0.08% |
| shorouknews.com | 2 | 0.08% |
| vietnamnet.vn | 2 | 0.08% |
| freepressjournal.in | 2 | 0.08% |
| interfax.ru | 2 | 0.08% |
| vesti.ru | 2 | 0.08% |
| jawapos.com | 2 | 0.08% |
| fontanka.ru | 2 | 0.08% |
| 1prime.ru | 2 | 0.08% |
| securitylab.ru | 2 | 0.08% |
| ntdtv.com | 2 | 0.08% |
| webpronews.com | 2 | 0.08% |
| itnews.com.au | 2 | 0.08% |
| el-balad.com | 2 | 0.08% |
| itbusinessnet.com | 2 | 0.08% |
| govinfosecurity.com | 2 | 0.08% |
| bjnews.com.cn | 2 | 0.08% |
| military.china.com | 2 | 0.08% |
| itbear.com.cn | 2 | 0.08% |
| time.mk | 2 | 0.08% |
| index.hr | 2 | 0.08% |
| eldia.com.bo | 2 | 0.08% |
| eldestapeweb.com | 2 | 0.08% |
| am.com.mx | 2 | 0.08% |
| natalie.mu | 2 | 0.08% |
| insight.co.kr | 2 | 0.08% |
| fnnews.com | 2 | 0.08% |
| newspim.com | 2 | 0.08% |
| thehindu.com | 2 | 0.08% |
| hindi.webdunia.com | 2 | 0.08% |
| bangkokpost.com | 1 | 0.04% |
| businessghana.com | 1 | 0.04% |
| securityinfowatch.com | 1 | 0.04% |
| governing.com | 1 | 0.04% |
| abc7news.com | 1 | 0.04% |
| inforum.com | 1 | 0.04% |
| cnn.com | 1 | 0.04% |
| edition.cnn.com | 1 | 0.04% |
| us.cnn.com | 1 | 0.04% |
| fox9.com | 1 | 0.04% |
| hachettebookgroup.com | 1 | 0.04% |
| bangordailynews.com | 1 | 0.04% |
| pymnts.com | 1 | 0.04% |
| tomshardware.com | 1 | 0.04% |
| wsbtv.com | 1 | 0.04% |
| bt.no | 1 | 0.04% |
| cnnturk.com | 1 | 0.04% |
| cnet.com | 1 | 0.04% |
| ryt9.com | 1 | 0.04% |
| antivirus-sniper.macupdate.com | 1 | 0.04% |
| adevarul.ro | 1 | 0.04% |
| bgr.com | 1 | 0.04% |
| express.pk | 1 | 0.04% |
| life.ru | 1 | 0.04% |
| donanimgunlugu.com | 1 | 0.04% |
| presse-citron.net | 1 | 0.04% |
| techcabal.com | 1 | 0.04% |
| bangkokbiznews.com | 1 | 0.04% |
| 01net.com | 1 | 0.04% |
| aif.ru | 1 | 0.04% |
| digg.com | 1 | 0.04% |
| etnews.com | 1 | 0.04% |
| generation-nt.com | 1 | 0.04% |
| playground.ru | 1 | 0.04% |
| prnewswire.com | 1 | 0.04% |
| digitaltrends.com | 1 | 0.04% |
| alanbatnews.net | 1 | 0.04% |
| itnewsafrica.com | 1 | 0.04% |
| trustedreviews.com | 1 | 0.04% |
| news.tuoitre.vn | 1 | 0.04% |
| hollywoodreporter.com | 1 | 0.04% |
| t-online.de | 1 | 0.04% |
| georgeherald.com | 1 | 0.04% |
| pjmedia.com | 1 | 0.04% |
| miragenews.com | 1 | 0.04% |
| regions.ru | 1 | 0.04% |
| businesstimes.com.sg | 1 | 0.04% |
| lexpress.fr | 1 | 0.04% |
| pln-pskov.ru | 1 | 0.04% |
| metroseoul.co.kr | 1 | 0.04% |
| fedpress.ru | 1 | 0.04% |
| wxii12.com | 1 | 0.04% |
| channellife.co.nz | 1 | 0.04% |
| y95country.com | 1 | 0.04% |
| local12.com | 1 | 0.04% |
| kingfm.com | 1 | 0.04% |
| buffalobulletin.com | 1 | 0.04% |
| profitline.hu | 1 | 0.04% |
| de.nachrichten.yahoo.com | 1 | 0.04% |
| directionsmag.com | 1 | 0.04% |
| circleid.com | 1 | 0.04% |
| cbc.ca | 1 | 0.04% |
| koco.com | 1 | 0.04% |
| lenta.ru | 1 | 0.04% |
| wbaltv.com | 1 | 0.04% |
| wvtm13.com | 1 | 0.04% |
| wlwt.com | 1 | 0.04% |
| hirek.prim.hu | 1 | 0.04% |
| ottawacitizen.com | 1 | 0.04% |
| news.ltn.com.tw | 1 | 0.04% |
| dnews.gr | 1 | 0.04% |
| infobae.com | 1 | 0.04% |
| ledauphine.com | 1 | 0.04% |
| scoop.co.nz | 1 | 0.04% |
| bankingnews.gr | 1 | 0.04% |
| dna.fr | 1 | 0.04% |
| laprovincia.es | 1 | 0.04% |
| northweststar.com.au | 1 | 0.04% |
| dailykos.com | 1 | 0.04% |
| armenews.com | 1 | 0.04% |
| elcomercio.es | 1 | 0.04% |
| mandurahmail.com.au | 1 | 0.04% |
| salzburg24.at | 1 | 0.04% |
| republicain-lorrain.fr | 1 | 0.04% |
| lejsl.com | 1 | 0.04% |
| lavozdegalicia.es | 1 | 0.04% |
| diariopalentino.es | 1 | 0.04% |
| eldia.es | 1 | 0.04% |
| bbc.com | 1 | 0.04% |
| groundup.org.za | 1 | 0.04% |
| koreaherald.com | 1 | 0.04% |
| zetatijuana.com | 1 | 0.04% |
| nzherald.co.nz | 1 | 0.04% |
| eluniversal.com.mx | 1 | 0.04% |
| aristeguinoticias.com | 1 | 0.04% |
| funkytaurusmedia.com | 1 | 0.04% |
| dw.com | 1 | 0.04% |
| botasot.info | 1 | 0.04% |
| fnp.de | 1 | 0.04% |
| tagesschau.de | 1 | 0.04% |
| ratopati.com | 1 | 0.04% |
| op-online.de | 1 | 0.04% |
| zeit.de | 1 | 0.04% |
| watson.ch | 1 | 0.04% |
| freiepresse.de | 1 | 0.04% |
| yeniakit.com.tr | 1 | 0.04% |
| turkiyegazetesi.com.tr | 1 | 0.04% |
| stern.de | 1 | 0.04% |
| sabah.com.tr | 1 | 0.04% |
| ntv.com.tr | 1 | 0.04% |
| trthaber.com | 1 | 0.04% |
| kannadaprabha.com | 1 | 0.04% |
| n-tv.de | 1 | 0.04% |
| sn.at | 1 | 0.04% |
| bursahakimiyet.com.tr | 1 | 0.04% |
| dunya.com | 1 | 0.04% |
| sdpnoticias.com | 1 | 0.04% |
| vecer.com | 1 | 0.04% |
| rtl.nl | 1 | 0.04% |
| eurointegration.com.ua | 1 | 0.04% |
| norran.se | 1 | 0.04% |
| computerworld.dk | 1 | 0.04% |
| aktifhaber.com | 1 | 0.04% |
| sana.sy | 1 | 0.04% |
| welt.de | 1 | 0.04% |
| japan.cnet.com | 1 | 0.04% |
| vrt.be | 1 | 0.04% |
| donanimhaber.com | 1 | 0.04% |
| dailynews.co.th | 1 | 0.04% |
| heute.at | 1 | 0.04% |
| bankier.pl | 1 | 0.04% |
| antena3.ro | 1 | 0.04% |
| businesstoday.in | 1 | 0.04% |
| 5.ua | 1 | 0.04% |
| kcci.com | 1 | 0.04% |
| twincities.com | 1 | 0.04% |
| wmur.com | 1 | 0.04% |
| king5.com | 1 | 0.04% |
| wtsp.com | 1 | 0.04% |
| wwltv.com | 1 | 0.04% |
| defensenews.com | 1 | 0.04% |
| wusa9.com | 1 | 0.04% |
| fox43.com | 1 | 0.04% |
| daytondailynews.com | 1 | 0.04% |
| kmbc.com | 1 | 0.04% |
| fox17online.com | 1 | 0.04% |
| journal-news.com | 1 | 0.04% |
| siliconrepublic.com | 1 | 0.04% |
| 5newsonline.com | 1 | 0.04% |
| beckershospitalreview.com | 1 | 0.04% |
| hindustantimes.com | 1 | 0.04% |
| legalinsurrection.com | 1 | 0.04% |
| riasv.ru | 1 | 0.04% |
| wcbi.com | 1 | 0.04% |
| war.obozrevatel.com | 1 | 0.04% |
| dailymail.co.uk | 1 | 0.04% |
| aol.co.uk | 1 | 0.04% |
| lbc.co.uk | 1 | 0.04% |
| wlox.com | 1 | 0.04% |
| wthr.com | 1 | 0.04% |
| wwmt.com | 1 | 0.04% |
| theglobeandmail.com | 1 | 0.04% |
| jpost.com | 1 | 0.04% |
| odatv.com | 1 | 0.04% |
| yn.xinhuanet.com | 1 | 0.04% |
| news.ycwb.com | 1 | 0.04% |
| kob.com | 1 | 0.04% |
| china.com.cn | 1 | 0.04% |
| digi.china.com | 1 | 0.04% |
| udn.com | 1 | 0.04% |
| dunyanews.tv | 1 | 0.04% |
| diena.lt | 1 | 0.04% |
| deperu.com | 1 | 0.04% |
| photo.china.com.cn | 1 | 0.04% |
| haberturk.com | 1 | 0.04% |
| ondacero.es | 1 | 0.04% |
| dailysabah.com | 1 | 0.04% |
| designboom.com | 1 | 0.04% |
| press24.mk | 1 | 0.04% |
| nj.com | 1 | 0.04% |
| haber3.com | 1 | 0.04% |
| eluniverso.com | 1 | 0.04% |
| idnes.cz | 1 | 0.04% |
| mobile.zol.com.cn | 1 | 0.04% |
| ai.zol.com.cn | 1 | 0.04% |
| posttoday.com | 1 | 0.04% |
| news.cnfol.com | 1 | 0.04% |
| ettoday.net | 1 | 0.04% |
| 3c.ltn.com.tw | 1 | 0.04% |
| bj.xinhuanet.com | 1 | 0.04% |
| nbd.com.cn | 1 | 0.04% |
| tass.ru | 1 | 0.04% |
| ruhrnachrichten.de | 1 | 0.04% |
| techtimes.com | 1 | 0.04% |
| top-channel.tv | 1 | 0.04% |
| jo24.net | 1 | 0.04% |
| panorama.com.al | 1 | 0.04% |
| gamerant.com | 1 | 0.04% |
| balkanweb.com | 1 | 0.04% |
| theblaze.com | 1 | 0.04% |
| lafranceagricole.fr | 1 | 0.04% |
| elwatannews.com | 1 | 0.04% |
| tecmundo.com.br | 1 | 0.04% |
| computerwoche.de | 1 | 0.04% |
| ria.ru | 1 | 0.04% |
| russian.rt.com | 1 | 0.04% |
| bandaancha.eu | 1 | 0.04% |
| europapress.es | 1 | 0.04% |
| jabar.tribunnews.com | 1 | 0.04% |
| dotekomanie.cz | 1 | 0.04% |
| bug.hr | 1 | 0.04% |
| kommersant.ru | 1 | 0.04% |
| jpnn.com | 1 | 0.04% |
| gorod48.ru | 1 | 0.04% |
| mskagency.ru | 1 | 0.04% |
| politika.rs | 1 | 0.04% |
| vg.no | 1 | 0.04% |
| makassar.tribunnews.com | 1 | 0.04% |
| vedomosti.ru | 1 | 0.04% |
| mashable.com | 1 | 0.04% |
| volksstimme.de | 1 | 0.04% |
| handelsblatt.com | 1 | 0.04% |
| weser-kurier.de | 1 | 0.04% |
| sueddeutsche.de | 1 | 0.04% |
| cepro.com | 1 | 0.04% |
| irishdentist.ie | 1 | 0.04% |
| corp.cnews.ru | 1 | 0.04% |
| vesti-ua.net | 1 | 0.04% |
| unian.net | 1 | 0.04% |
| slguardian.org | 1 | 0.04% |
| chip.de | 1 | 0.04% |
| comnews.ru | 1 | 0.04% |
| tivi.fi | 1 | 0.04% |
| strategypage.com | 1 | 0.04% |
| securitybrief.news | 1 | 0.04% |
| alaskasnewssource.com | 1 | 0.04% |
| risky.biz | 1 | 0.04% |
| itwire.com | 1 | 0.04% |
| zdnet.com | 1 | 0.04% |
| tekniikkatalous.fi | 1 | 0.04% |
| fakti.bg | 1 | 0.04% |
| stcatharinesstandard.ca | 1 | 0.04% |
| therecord.com | 1 | 0.04% |
| thepeterboroughexaminer.com | 1 | 0.04% |
| hydrocarbonprocessing.com | 1 | 0.04% |
| jugantor.com | 1 | 0.04% |
| winfuture.de | 1 | 0.04% |
| financial-news.co.uk | 1 | 0.04% |
| berliner-zeitung.de | 1 | 0.04% |
| ukrinform.ua | 1 | 0.04% |
| localnews8.com | 1 | 0.04% |
| kesq.com | 1 | 0.04% |
| openpr.com | 1 | 0.04% |
| portal.sina.com.hk | 1 | 0.04% |
| datacenterknowledge.com | 1 | 0.04% |
| mirrorspectator.com | 1 | 0.04% |
| htxt.co.za | 1 | 0.04% |
| kotaku.com | 1 | 0.04% |
| explosion.com | 1 | 0.04% |
| wowo.com | 1 | 0.04% |
| biometricupdate.com | 1 | 0.04% |
| newsweek.com | 1 | 0.04% |
| makeuseof.com | 1 | 0.04% |
| infoworld.com | 1 | 0.04% |
| news.china.com.cn | 1 | 0.04% |
| liputan6.com | 1 | 0.04% |
| stcn.com | 1 | 0.04% |
| webinars.govtech.com | 1 | 0.04% |
| antaranews.com | 1 | 0.04% |
| nikkei.com | 1 | 0.04% |
| newtalk.tw | 1 | 0.04% |
| cfi.net.cn | 1 | 0.04% |
| arstechnica.com | 1 | 0.04% |
| futures.cnfol.com | 1 | 0.04% |
| setn.com | 1 | 0.04% |
| senego.com | 1 | 0.04% |
| mp.cnfol.com | 1 | 0.04% |
| cloud.watch.impress.co.jp | 1 | 0.04% |
| finance.ifeng.com | 1 | 0.04% |
| stock.hexun.com | 1 | 0.04% |
| ec.ltn.com.tw | 1 | 0.04% |
| northcountrynow.com | 1 | 0.04% |
| business2community.com | 1 | 0.04% |
| infotechlead.com | 1 | 0.04% |
| clarin.com | 1 | 0.04% |
| it-online.co.za | 1 | 0.04% |
| wwwhatsnew.com | 1 | 0.04% |
| computerworld.pl | 1 | 0.04% |
| icij.org | 1 | 0.04% |
| tecnoandroid.it | 1 | 0.04% |
| arede.info | 1 | 0.04% |
| businessday.co.za | 1 | 0.04% |
| extra.ec | 1 | 0.04% |
| ibtimes.com.au | 1 | 0.04% |
| elsiglodetorreon.com.mx | 1 | 0.04% |
| tn.com.ar | 1 | 0.04% |
| foxnews.com | 1 | 0.04% |
| diariodemorelos.com | 1 | 0.04% |
| mobileidworld.com | 1 | 0.04% |
| inwestycje.pl | 1 | 0.04% |
| words.filippo.io | 1 | 0.04% |
| elpais.com.uy | 1 | 0.04% |
| quadratin.com.mx | 1 | 0.04% |
| kmib.co.kr | 1 | 0.04% |
| nikkan.co.jp | 1 | 0.04% |
| mariettatimes.com | 1 | 0.04% |
| statecollege.com | 1 | 0.04% |
| jowhar.com | 1 | 0.04% |
| ohmynews.com | 1 | 0.04% |
| ihalla.com | 1 | 0.04% |
| maharashtratimes.com | 1 | 0.04% |
| inews24.com | 1 | 0.04% |
| travelweekly.com.au | 1 | 0.04% |
| etoday.co.kr | 1 | 0.04% |
| segye.com | 1 | 0.04% |
| hani.co.kr | 1 | 0.04% |
| journalgazette.net | 1 | 0.04% |
| austinchronicle.com | 1 | 0.04% |
| ktvu.com | 1 | 0.04% |
| pitchfork.com | 1 | 0.04% |
| mathrubhumi.com | 1 | 0.04% |
| divyamarathi.bhaskar.com | 1 | 0.04% |
| digi24.ro | 1 | 0.04% |
| rappler.com | 1 | 0.04% |
| india.com | 1 | 0.04% |
| firstpost.com | 1 | 0.04% |
| tribuneindia.com | 1 | 0.04% |
| thetoc.gr | 1 | 0.04% |
| loksatta.com | 1 | 0.04% |
| newsx.com | 1 | 0.04% |
| dantri.com.vn | 1 | 0.04% |
| inewsgr.com | 1 | 0.04% |
| bollywoodlife.com | 1 | 0.04% |
| world.kbs.co.kr | 1 | 0.04% |
| punjabitribuneonline.com | 1 | 0.04% |
| navbharattimes.indiatimes.com | 1 | 0.04% |
| bhaskar.com | 1 | 0.04% |
| gulte.com | 1 | 0.04% |
| idiva.com | 1 | 0.04% |
| livehindustan.com | 1 | 0.04% |
| newsbomb.gr | 1 | 0.04% |

## Source Distribution

| source_type | source_name | rows | percent_dataset | percent_source_type |
| --- | --- | --- | --- | --- |
| cve | NVD CVE | 1295 | 49.75% | 100.00% |
| news_rss | The Hacker News | 54 | 2.07% | 34.18% |
| reddit_rss | cybersecurity | 50 | 1.92% | 13.62% |
| reddit_rss | sysadmin | 50 | 1.92% | 13.62% |
| reddit_rss | privacy | 40 | 1.54% | 10.90% |
| reddit_rss | blueteamsec | 38 | 1.46% | 10.35% |
| reddit_rss | netsec | 29 | 1.11% | 7.90% |
| reddit_rss | hacking | 28 | 1.08% | 7.63% |
| reddit_rss | AskNetsec | 27 | 1.04% | 7.36% |
| reddit_rss | ReverseEngineering | 27 | 1.04% | 7.36% |
| reddit_rss | osint | 27 | 1.04% | 7.36% |
| reddit_rss | Malware | 26 | 1.00% | 7.08% |
| reddit_rss | ComputerSecurity | 25 | 0.96% | 6.81% |
| news_api | techradar.com | 22 | 0.85% | 2.81% |
| news_rss | Rapid7 Blog | 22 | 0.85% | 13.92% |
| news_rss | BleepingComputer | 21 | 0.81% | 13.29% |
| news_api | cnews.ru | 19 | 0.73% | 2.43% |
| news_api | forbes.com | 17 | 0.65% | 2.17% |
| news_api | ithome.com.tw | 17 | 0.65% | 2.17% |
| news_rss | Cisco Talos Blog | 15 | 0.58% | 9.49% |
| news_rss | Unit 42 | 15 | 0.58% | 9.49% |
| news_api | ascii.jp | 14 | 0.54% | 1.79% |
| news_rss | SANS Internet Storm Center | 12 | 0.46% | 7.59% |
| news_api | 163.com | 11 | 0.42% | 1.40% |
| news_api | finance.sina.com.cn | 11 | 0.42% | 1.40% |
| news_rss | KrebsOnSecurity | 10 | 0.38% | 6.33% |
| news_api | cointelegraph.com | 9 | 0.35% | 1.15% |
| news_rss | Google Project Zero | 9 | 0.35% | 5.70% |
| news_api | esecurityplanet.com | 8 | 0.31% | 1.02% |
| news_api | infosecurity-magazine.com | 7 | 0.27% | 0.89% |
| news_api | techcrunch.com | 7 | 0.27% | 0.89% |
| news_api | baijiahao.baidu.com | 6 | 0.23% | 0.77% |
| news_api | bankinfosecurity.com | 6 | 0.23% | 0.77% |
| news_api | csoonline.com | 6 | 0.23% | 0.77% |
| news_api | laopcion.com.mx | 6 | 0.23% | 0.77% |
| news_api | moneycontrol.com | 6 | 0.23% | 0.77% |
| news_api | timesofindia.indiatimes.com | 6 | 0.23% | 0.77% |
| news_api | tvguide.co.uk | 6 | 0.23% | 0.77% |
| news_api | udayavani.com | 6 | 0.23% | 0.77% |
| news_api | biz.heraldcorp.com | 5 | 0.19% | 0.64% |
| news_api | finanznachrichten.de | 5 | 0.19% | 0.64% |
| news_api | itbrief.co.nz | 5 | 0.19% | 0.64% |
| news_api | yahoo.com | 5 | 0.19% | 0.64% |
| news_api | 9to5mac.com | 4 | 0.15% | 0.51% |
| news_api | coindesk.com | 4 | 0.15% | 0.51% |
| news_api | economictimes.indiatimes.com | 4 | 0.15% | 0.51% |
| news_api | govtech.com | 4 | 0.15% | 0.51% |
| news_api | haberler.com | 4 | 0.15% | 0.51% |
| news_api | hothardware.com | 4 | 0.15% | 0.51% |
| news_api | manilatimes.net | 4 | 0.15% | 0.51% |
| news_api | theregister.com | 4 | 0.15% | 0.51% |
| news_api | vz.ru | 4 | 0.15% | 0.51% |
| news_api | zdnet.co.kr | 4 | 0.15% | 0.51% |
| news_api | aa.com.tr | 3 | 0.12% | 0.38% |
| news_api | androidauthority.com | 3 | 0.12% | 0.38% |
| news_api | bleedingcool.com | 3 | 0.12% | 0.38% |
| news_api | boredpanda.com | 3 | 0.12% | 0.38% |
| news_api | divyabhaskar.co.in | 3 | 0.12% | 0.38% |
| news_api | dostor.org | 3 | 0.12% | 0.38% |
| news_api | edaily.co.kr | 3 | 0.12% | 0.38% |
| news_api | ensonhaber.com | 3 | 0.12% | 0.38% |
| news_api | finance.eastmoney.com | 3 | 0.12% | 0.38% |
| news_api | finance.yahoo.com | 3 | 0.12% | 0.38% |
| news_api | heise.de | 3 | 0.12% | 0.38% |
| news_api | jdsupra.com | 3 | 0.12% | 0.38% |
| news_api | kibrispostasi.com | 3 | 0.12% | 0.38% |
| news_api | newswiretoday.com | 3 | 0.12% | 0.38% |
| news_api | politis.com.cy | 3 | 0.12% | 0.38% |
| news_api | screenrant.com | 3 | 0.12% | 0.38% |
| news_api | thefastmode.com | 3 | 0.12% | 0.38% |
| news_api | thenews.com.pk | 3 | 0.12% | 0.38% |
| news_api | ura.news | 3 | 0.12% | 0.38% |
| news_api | womannews.net | 3 | 0.12% | 0.38% |
| news_api | 1prime.ru | 2 | 0.08% | 0.26% |
| news_api | am.com.mx | 2 | 0.08% | 0.26% |
| news_api | androidheadlines.com | 2 | 0.08% | 0.26% |
| news_api | bd-pratidin.com | 2 | 0.08% | 0.26% |
| news_api | bjnews.com.cn | 2 | 0.08% | 0.26% |
| news_api | bleepingcomputer.com | 2 | 0.08% | 0.26% |
| news_api | bunburymail.com.au | 2 | 0.08% | 0.26% |
| news_api | channellife.com.au | 2 | 0.08% | 0.26% |
| news_api | computerweekly.com | 2 | 0.08% | 0.26% |
| news_api | ddaily.co.kr | 2 | 0.08% | 0.26% |
| news_api | digitaljournal.com | 2 | 0.08% | 0.26% |
| news_api | el-balad.com | 2 | 0.08% | 0.26% |
| news_api | eldestapeweb.com | 2 | 0.08% | 0.26% |
| news_api | eldia.com.bo | 2 | 0.08% | 0.26% |
| news_api | elmanana.com | 2 | 0.08% | 0.26% |
| news_api | fnnews.com | 2 | 0.08% | 0.26% |
| news_api | fontanka.ru | 2 | 0.08% | 0.26% |
| news_api | freemalaysiatoday.com | 2 | 0.08% | 0.26% |
| news_api | freepressjournal.in | 2 | 0.08% | 0.26% |
| news_api | github.com | 2 | 0.08% | 0.26% |
| news_api | gizmodo.com | 2 | 0.08% | 0.26% |
| news_api | glavcom.ua | 2 | 0.08% | 0.26% |
| news_api | govinfosecurity.com | 2 | 0.08% | 0.26% |
| news_api | hindi.webdunia.com | 2 | 0.08% | 0.26% |
| news_api | hinews.cn | 2 | 0.08% | 0.26% |
| news_api | hurriyetdailynews.com | 2 | 0.08% | 0.26% |
| news_api | index.hr | 2 | 0.08% | 0.26% |
| news_api | insight.co.kr | 2 | 0.08% | 0.26% |
| news_api | insurancebusinessmag.com | 2 | 0.08% | 0.26% |
| news_api | insurancejournal.com | 2 | 0.08% | 0.26% |
| news_api | interfax.ru | 2 | 0.08% | 0.26% |
| news_api | itbear.com.cn | 2 | 0.08% | 0.26% |
| news_api | itbusinessnet.com | 2 | 0.08% | 0.26% |
| news_api | itnews.com.au | 2 | 0.08% | 0.26% |
| news_api | iz.ru | 2 | 0.08% | 0.26% |
| news_api | japan.zdnet.com | 2 | 0.08% | 0.26% |
| news_api | jawapos.com | 2 | 0.08% | 0.26% |
| news_api | lalsace.fr | 2 | 0.08% | 0.26% |
| news_api | military.china.com | 2 | 0.08% | 0.26% |
| news_api | milliyet.com.tr | 2 | 0.08% | 0.26% |
| news_api | mondaq.com | 2 | 0.08% | 0.26% |
| news_api | n.yam.com | 2 | 0.08% | 0.26% |
| news_api | natalie.mu | 2 | 0.08% | 0.26% |
| news_api | news.cn | 2 | 0.08% | 0.26% |
| news_api | newspim.com | 2 | 0.08% | 0.26% |
| news_api | ntdtv.com | 2 | 0.08% | 0.26% |
| news_api | nvi.com.au | 2 | 0.08% | 0.26% |
| news_api | pcmag.com | 2 | 0.08% | 0.26% |
| news_api | phonandroid.com | 2 | 0.08% | 0.26% |
| news_api | propakistani.pk | 2 | 0.08% | 0.26% |
| news_api | sb.by | 2 | 0.08% | 0.26% |
| news_api | securitylab.ru | 2 | 0.08% | 0.26% |
| news_api | shorouknews.com | 2 | 0.08% | 0.26% |
| news_api | straitstimes.com | 2 | 0.08% | 0.26% |
| news_api | tech.caijing.com.cn | 2 | 0.08% | 0.26% |
| news_api | tech.ifeng.com | 2 | 0.08% | 0.26% |
| news_api | thehindu.com | 2 | 0.08% | 0.26% |
| news_api | time.mk | 2 | 0.08% | 0.26% |
| news_api | vesti.ru | 2 | 0.08% | 0.26% |
| news_api | vietnamnet.vn | 2 | 0.08% | 0.26% |
| news_api | wdrb.com | 2 | 0.08% | 0.26% |
| news_api | webpronews.com | 2 | 0.08% | 0.26% |
| news_api | wesh.com | 2 | 0.08% | 0.26% |
| news_api | wfmz.com | 2 | 0.08% | 0.26% |
| news_api | winnipegfreepress.com | 2 | 0.08% | 0.26% |
| news_api | wiwo.de | 2 | 0.08% | 0.26% |
| news_api | 01net.com | 1 | 0.04% | 0.13% |
| news_api | 3c.ltn.com.tw | 1 | 0.04% | 0.13% |
| news_api | 5.ua | 1 | 0.04% | 0.13% |
| news_api | 5newsonline.com | 1 | 0.04% | 0.13% |
| news_api | abc7news.com | 1 | 0.04% | 0.13% |
| news_api | adevarul.ro | 1 | 0.04% | 0.13% |
| news_api | ai.zol.com.cn | 1 | 0.04% | 0.13% |
| news_api | aif.ru | 1 | 0.04% | 0.13% |
| news_api | aktifhaber.com | 1 | 0.04% | 0.13% |
| news_api | alanbatnews.net | 1 | 0.04% | 0.13% |
| news_api | alaskasnewssource.com | 1 | 0.04% | 0.13% |
| news_api | antaranews.com | 1 | 0.04% | 0.13% |
| news_api | antena3.ro | 1 | 0.04% | 0.13% |
| news_api | antivirus-sniper.macupdate.com | 1 | 0.04% | 0.13% |
| news_api | aol.co.uk | 1 | 0.04% | 0.13% |
| news_api | arede.info | 1 | 0.04% | 0.13% |
| news_api | aristeguinoticias.com | 1 | 0.04% | 0.13% |
| news_api | armenews.com | 1 | 0.04% | 0.13% |
| news_api | arstechnica.com | 1 | 0.04% | 0.13% |
| news_api | austinchronicle.com | 1 | 0.04% | 0.13% |
| news_api | balkanweb.com | 1 | 0.04% | 0.13% |
| news_api | bandaancha.eu | 1 | 0.04% | 0.13% |
| news_api | bangkokbiznews.com | 1 | 0.04% | 0.13% |
| news_api | bangkokpost.com | 1 | 0.04% | 0.13% |
| news_api | bangordailynews.com | 1 | 0.04% | 0.13% |
| news_api | bankier.pl | 1 | 0.04% | 0.13% |
| news_api | bankingnews.gr | 1 | 0.04% | 0.13% |
| news_api | bbc.com | 1 | 0.04% | 0.13% |
| news_api | beckershospitalreview.com | 1 | 0.04% | 0.13% |
| news_api | berliner-zeitung.de | 1 | 0.04% | 0.13% |
| news_api | bgr.com | 1 | 0.04% | 0.13% |
| news_api | bhaskar.com | 1 | 0.04% | 0.13% |
| news_api | biometricupdate.com | 1 | 0.04% | 0.13% |
| news_api | bj.xinhuanet.com | 1 | 0.04% | 0.13% |
| news_api | bollywoodlife.com | 1 | 0.04% | 0.13% |
| news_api | botasot.info | 1 | 0.04% | 0.13% |
| news_api | bt.no | 1 | 0.04% | 0.13% |
| news_api | buffalobulletin.com | 1 | 0.04% | 0.13% |
| news_api | bug.hr | 1 | 0.04% | 0.13% |
| news_api | bursahakimiyet.com.tr | 1 | 0.04% | 0.13% |
| news_api | business2community.com | 1 | 0.04% | 0.13% |
| news_api | businessday.co.za | 1 | 0.04% | 0.13% |
| news_api | businessghana.com | 1 | 0.04% | 0.13% |
| news_api | businesstimes.com.sg | 1 | 0.04% | 0.13% |
| news_api | businesstoday.in | 1 | 0.04% | 0.13% |
| news_api | cbc.ca | 1 | 0.04% | 0.13% |
| news_api | cepro.com | 1 | 0.04% | 0.13% |
| news_api | cfi.net.cn | 1 | 0.04% | 0.13% |
| news_api | channellife.co.nz | 1 | 0.04% | 0.13% |
| news_api | china.com.cn | 1 | 0.04% | 0.13% |
| news_api | chip.de | 1 | 0.04% | 0.13% |
| news_api | circleid.com | 1 | 0.04% | 0.13% |
| news_api | clarin.com | 1 | 0.04% | 0.13% |
| news_api | cloud.watch.impress.co.jp | 1 | 0.04% | 0.13% |
| news_api | cnet.com | 1 | 0.04% | 0.13% |
| news_api | cnn.com | 1 | 0.04% | 0.13% |
| news_api | cnnturk.com | 1 | 0.04% | 0.13% |
| news_api | comnews.ru | 1 | 0.04% | 0.13% |
| news_api | computerwoche.de | 1 | 0.04% | 0.13% |
| news_api | computerworld.dk | 1 | 0.04% | 0.13% |
| news_api | computerworld.pl | 1 | 0.04% | 0.13% |
| news_api | corp.cnews.ru | 1 | 0.04% | 0.13% |
| news_api | dailykos.com | 1 | 0.04% | 0.13% |
| news_api | dailymail.co.uk | 1 | 0.04% | 0.13% |
| news_api | dailynews.co.th | 1 | 0.04% | 0.13% |
| news_api | dailysabah.com | 1 | 0.04% | 0.13% |
| news_api | dantri.com.vn | 1 | 0.04% | 0.13% |
| news_api | datacenterknowledge.com | 1 | 0.04% | 0.13% |
| news_api | daytondailynews.com | 1 | 0.04% | 0.13% |
| news_api | de.nachrichten.yahoo.com | 1 | 0.04% | 0.13% |
| news_api | defensenews.com | 1 | 0.04% | 0.13% |
| news_api | deperu.com | 1 | 0.04% | 0.13% |
| news_api | designboom.com | 1 | 0.04% | 0.13% |
| news_api | diariodemorelos.com | 1 | 0.04% | 0.13% |
| news_api | diariopalentino.es | 1 | 0.04% | 0.13% |
| news_api | diena.lt | 1 | 0.04% | 0.13% |
| news_api | digg.com | 1 | 0.04% | 0.13% |
| news_api | digi.china.com | 1 | 0.04% | 0.13% |
| news_api | digi24.ro | 1 | 0.04% | 0.13% |
| news_api | digitaltrends.com | 1 | 0.04% | 0.13% |
| news_api | directionsmag.com | 1 | 0.04% | 0.13% |
| news_api | divyamarathi.bhaskar.com | 1 | 0.04% | 0.13% |
| news_api | dna.fr | 1 | 0.04% | 0.13% |
| news_api | dnews.gr | 1 | 0.04% | 0.13% |
| news_api | donanimgunlugu.com | 1 | 0.04% | 0.13% |
| news_api | donanimhaber.com | 1 | 0.04% | 0.13% |
| news_api | dotekomanie.cz | 1 | 0.04% | 0.13% |
| news_api | dunya.com | 1 | 0.04% | 0.13% |
| news_api | dunyanews.tv | 1 | 0.04% | 0.13% |
| news_api | dw.com | 1 | 0.04% | 0.13% |
| news_api | ec.ltn.com.tw | 1 | 0.04% | 0.13% |
| news_api | edition.cnn.com | 1 | 0.04% | 0.13% |
| news_api | elcomercio.es | 1 | 0.04% | 0.13% |
| news_api | eldia.es | 1 | 0.04% | 0.13% |
| news_api | elpais.com.uy | 1 | 0.04% | 0.13% |
| news_api | elsiglodetorreon.com.mx | 1 | 0.04% | 0.13% |
| news_api | eluniversal.com.mx | 1 | 0.04% | 0.13% |
| news_api | eluniverso.com | 1 | 0.04% | 0.13% |
| news_api | elwatannews.com | 1 | 0.04% | 0.13% |
| news_api | etnews.com | 1 | 0.04% | 0.13% |
| news_api | etoday.co.kr | 1 | 0.04% | 0.13% |
| news_api | ettoday.net | 1 | 0.04% | 0.13% |
| news_api | eurointegration.com.ua | 1 | 0.04% | 0.13% |
| news_api | europapress.es | 1 | 0.04% | 0.13% |
| news_api | explosion.com | 1 | 0.04% | 0.13% |
| news_api | express.pk | 1 | 0.04% | 0.13% |
| news_api | extra.ec | 1 | 0.04% | 0.13% |
| news_api | fakti.bg | 1 | 0.04% | 0.13% |
| news_api | fedpress.ru | 1 | 0.04% | 0.13% |
| news_api | finance.ifeng.com | 1 | 0.04% | 0.13% |
| news_api | financial-news.co.uk | 1 | 0.04% | 0.13% |
| news_api | firstpost.com | 1 | 0.04% | 0.13% |
| news_api | fnp.de | 1 | 0.04% | 0.13% |
| news_api | fox17online.com | 1 | 0.04% | 0.13% |
| news_api | fox43.com | 1 | 0.04% | 0.13% |
| news_api | fox9.com | 1 | 0.04% | 0.13% |
| news_api | foxnews.com | 1 | 0.04% | 0.13% |
| news_api | freiepresse.de | 1 | 0.04% | 0.13% |
| news_api | funkytaurusmedia.com | 1 | 0.04% | 0.13% |
| news_api | futures.cnfol.com | 1 | 0.04% | 0.13% |
| news_api | gamerant.com | 1 | 0.04% | 0.13% |
| news_api | generation-nt.com | 1 | 0.04% | 0.13% |
| news_api | georgeherald.com | 1 | 0.04% | 0.13% |
| news_api | gorod48.ru | 1 | 0.04% | 0.13% |
| news_api | governing.com | 1 | 0.04% | 0.13% |
| news_api | groundup.org.za | 1 | 0.04% | 0.13% |
| news_api | gulte.com | 1 | 0.04% | 0.13% |
| news_api | haber3.com | 1 | 0.04% | 0.13% |
| news_api | haberturk.com | 1 | 0.04% | 0.13% |
| news_api | hachettebookgroup.com | 1 | 0.04% | 0.13% |
| news_api | handelsblatt.com | 1 | 0.04% | 0.13% |
| news_api | hani.co.kr | 1 | 0.04% | 0.13% |
| news_api | heute.at | 1 | 0.04% | 0.13% |
| news_api | hindustantimes.com | 1 | 0.04% | 0.13% |
| news_api | hirek.prim.hu | 1 | 0.04% | 0.13% |
| news_api | hollywoodreporter.com | 1 | 0.04% | 0.13% |
| news_api | htxt.co.za | 1 | 0.04% | 0.13% |
| news_api | hydrocarbonprocessing.com | 1 | 0.04% | 0.13% |
| news_api | ibtimes.com.au | 1 | 0.04% | 0.13% |
| news_api | icij.org | 1 | 0.04% | 0.13% |
| news_api | idiva.com | 1 | 0.04% | 0.13% |
| news_api | idnes.cz | 1 | 0.04% | 0.13% |
| news_api | ihalla.com | 1 | 0.04% | 0.13% |
| news_api | india.com | 1 | 0.04% | 0.13% |
| news_api | inews24.com | 1 | 0.04% | 0.13% |
| news_api | inewsgr.com | 1 | 0.04% | 0.13% |
| news_api | infobae.com | 1 | 0.04% | 0.13% |
| news_api | inforum.com | 1 | 0.04% | 0.13% |
| news_api | infotechlead.com | 1 | 0.04% | 0.13% |
| news_api | infoworld.com | 1 | 0.04% | 0.13% |
| news_api | inwestycje.pl | 1 | 0.04% | 0.13% |
| news_api | irishdentist.ie | 1 | 0.04% | 0.13% |
| news_api | it-online.co.za | 1 | 0.04% | 0.13% |
| news_api | itnewsafrica.com | 1 | 0.04% | 0.13% |
| news_api | itwire.com | 1 | 0.04% | 0.13% |
| news_api | jabar.tribunnews.com | 1 | 0.04% | 0.13% |
| news_api | japan.cnet.com | 1 | 0.04% | 0.13% |
| news_api | jo24.net | 1 | 0.04% | 0.13% |
| news_api | journal-news.com | 1 | 0.04% | 0.13% |
| news_api | journalgazette.net | 1 | 0.04% | 0.13% |
| news_api | jowhar.com | 1 | 0.04% | 0.13% |
| news_api | jpnn.com | 1 | 0.04% | 0.13% |
| news_api | jpost.com | 1 | 0.04% | 0.13% |
| news_api | jugantor.com | 1 | 0.04% | 0.13% |
| news_api | kannadaprabha.com | 1 | 0.04% | 0.13% |
| news_api | kcci.com | 1 | 0.04% | 0.13% |
| news_api | kesq.com | 1 | 0.04% | 0.13% |
| news_api | king5.com | 1 | 0.04% | 0.13% |
| news_api | kingfm.com | 1 | 0.04% | 0.13% |
| news_api | kmbc.com | 1 | 0.04% | 0.13% |
| news_api | kmib.co.kr | 1 | 0.04% | 0.13% |
| news_api | kob.com | 1 | 0.04% | 0.13% |
| news_api | koco.com | 1 | 0.04% | 0.13% |
| news_api | kommersant.ru | 1 | 0.04% | 0.13% |
| news_api | koreaherald.com | 1 | 0.04% | 0.13% |
| news_api | kotaku.com | 1 | 0.04% | 0.13% |
| news_api | ktvu.com | 1 | 0.04% | 0.13% |
| news_api | lafranceagricole.fr | 1 | 0.04% | 0.13% |
| news_api | laprovincia.es | 1 | 0.04% | 0.13% |
| news_api | lavozdegalicia.es | 1 | 0.04% | 0.13% |
| news_api | lbc.co.uk | 1 | 0.04% | 0.13% |
| news_api | ledauphine.com | 1 | 0.04% | 0.13% |
| news_api | legalinsurrection.com | 1 | 0.04% | 0.13% |
| news_api | lejsl.com | 1 | 0.04% | 0.13% |
| news_api | lenta.ru | 1 | 0.04% | 0.13% |
| news_api | lexpress.fr | 1 | 0.04% | 0.13% |
| news_api | life.ru | 1 | 0.04% | 0.13% |
| news_api | liputan6.com | 1 | 0.04% | 0.13% |
| news_api | livehindustan.com | 1 | 0.04% | 0.13% |
| news_api | local12.com | 1 | 0.04% | 0.13% |
| news_api | localnews8.com | 1 | 0.04% | 0.13% |
| news_api | loksatta.com | 1 | 0.04% | 0.13% |
| news_api | maharashtratimes.com | 1 | 0.04% | 0.13% |
| news_api | makassar.tribunnews.com | 1 | 0.04% | 0.13% |
| news_api | makeuseof.com | 1 | 0.04% | 0.13% |
| news_api | mandurahmail.com.au | 1 | 0.04% | 0.13% |
| news_api | mariettatimes.com | 1 | 0.04% | 0.13% |
| news_api | mashable.com | 1 | 0.04% | 0.13% |
| news_api | mathrubhumi.com | 1 | 0.04% | 0.13% |
| news_api | metroseoul.co.kr | 1 | 0.04% | 0.13% |
| news_api | miragenews.com | 1 | 0.04% | 0.13% |
| news_api | mirrorspectator.com | 1 | 0.04% | 0.13% |
| news_api | mobile.zol.com.cn | 1 | 0.04% | 0.13% |
| news_api | mobileidworld.com | 1 | 0.04% | 0.13% |
| news_api | mp.cnfol.com | 1 | 0.04% | 0.13% |
| news_api | mskagency.ru | 1 | 0.04% | 0.13% |
| news_api | n-tv.de | 1 | 0.04% | 0.13% |
| news_api | navbharattimes.indiatimes.com | 1 | 0.04% | 0.13% |
| news_api | nbd.com.cn | 1 | 0.04% | 0.13% |
| news_api | news.china.com.cn | 1 | 0.04% | 0.13% |
| news_api | news.cnfol.com | 1 | 0.04% | 0.13% |
| news_api | news.ltn.com.tw | 1 | 0.04% | 0.13% |
| news_api | news.tuoitre.vn | 1 | 0.04% | 0.13% |
| news_api | news.ycwb.com | 1 | 0.04% | 0.13% |
| news_api | newsbomb.gr | 1 | 0.04% | 0.13% |
| news_api | newsweek.com | 1 | 0.04% | 0.13% |
| news_api | newsx.com | 1 | 0.04% | 0.13% |
| news_api | newtalk.tw | 1 | 0.04% | 0.13% |
| news_api | nikkan.co.jp | 1 | 0.04% | 0.13% |
| news_api | nikkei.com | 1 | 0.04% | 0.13% |
| news_api | nj.com | 1 | 0.04% | 0.13% |
| news_api | norran.se | 1 | 0.04% | 0.13% |
| news_api | northcountrynow.com | 1 | 0.04% | 0.13% |
| news_api | northweststar.com.au | 1 | 0.04% | 0.13% |
| news_api | ntv.com.tr | 1 | 0.04% | 0.13% |
| news_api | nzherald.co.nz | 1 | 0.04% | 0.13% |
| news_api | odatv.com | 1 | 0.04% | 0.13% |
| news_api | ohmynews.com | 1 | 0.04% | 0.13% |
| news_api | ondacero.es | 1 | 0.04% | 0.13% |
| news_api | op-online.de | 1 | 0.04% | 0.13% |
| news_api | openpr.com | 1 | 0.04% | 0.13% |
| news_api | ottawacitizen.com | 1 | 0.04% | 0.13% |
| news_api | panorama.com.al | 1 | 0.04% | 0.13% |
| news_api | photo.china.com.cn | 1 | 0.04% | 0.13% |
| news_api | pitchfork.com | 1 | 0.04% | 0.13% |
| news_api | pjmedia.com | 1 | 0.04% | 0.13% |
| news_api | playground.ru | 1 | 0.04% | 0.13% |
| news_api | pln-pskov.ru | 1 | 0.04% | 0.13% |
| news_api | politika.rs | 1 | 0.04% | 0.13% |
| news_api | portal.sina.com.hk | 1 | 0.04% | 0.13% |
| news_api | posttoday.com | 1 | 0.04% | 0.13% |
| news_api | press24.mk | 1 | 0.04% | 0.13% |
| news_api | presse-citron.net | 1 | 0.04% | 0.13% |
| news_api | prnewswire.com | 1 | 0.04% | 0.13% |
| news_api | profitline.hu | 1 | 0.04% | 0.13% |
| news_api | punjabitribuneonline.com | 1 | 0.04% | 0.13% |
| news_api | pymnts.com | 1 | 0.04% | 0.13% |
| news_api | quadratin.com.mx | 1 | 0.04% | 0.13% |
| news_api | rappler.com | 1 | 0.04% | 0.13% |
| news_api | ratopati.com | 1 | 0.04% | 0.13% |
| news_api | regions.ru | 1 | 0.04% | 0.13% |
| news_api | republicain-lorrain.fr | 1 | 0.04% | 0.13% |
| news_api | ria.ru | 1 | 0.04% | 0.13% |
| news_api | riasv.ru | 1 | 0.04% | 0.13% |
| news_api | risky.biz | 1 | 0.04% | 0.13% |
| news_api | rtl.nl | 1 | 0.04% | 0.13% |
| news_api | ruhrnachrichten.de | 1 | 0.04% | 0.13% |
| news_api | russian.rt.com | 1 | 0.04% | 0.13% |
| news_api | ryt9.com | 1 | 0.04% | 0.13% |
| news_api | sabah.com.tr | 1 | 0.04% | 0.13% |
| news_api | salzburg24.at | 1 | 0.04% | 0.13% |
| news_api | sana.sy | 1 | 0.04% | 0.13% |
| news_api | scoop.co.nz | 1 | 0.04% | 0.13% |
| news_api | sdpnoticias.com | 1 | 0.04% | 0.13% |
| news_api | securitybrief.news | 1 | 0.04% | 0.13% |
| news_api | securityinfowatch.com | 1 | 0.04% | 0.13% |
| news_api | segye.com | 1 | 0.04% | 0.13% |
| news_api | senego.com | 1 | 0.04% | 0.13% |
| news_api | setn.com | 1 | 0.04% | 0.13% |
| news_api | siliconrepublic.com | 1 | 0.04% | 0.13% |
| news_api | slguardian.org | 1 | 0.04% | 0.13% |
| news_api | sn.at | 1 | 0.04% | 0.13% |
| news_api | statecollege.com | 1 | 0.04% | 0.13% |
| news_api | stcatharinesstandard.ca | 1 | 0.04% | 0.13% |
| news_api | stcn.com | 1 | 0.04% | 0.13% |
| news_api | stern.de | 1 | 0.04% | 0.13% |
| news_api | stock.hexun.com | 1 | 0.04% | 0.13% |
| news_api | strategypage.com | 1 | 0.04% | 0.13% |
| news_api | sueddeutsche.de | 1 | 0.04% | 0.13% |
| news_api | t-online.de | 1 | 0.04% | 0.13% |
| news_api | tagesschau.de | 1 | 0.04% | 0.13% |
| news_api | tass.ru | 1 | 0.04% | 0.13% |
| news_api | techcabal.com | 1 | 0.04% | 0.13% |
| news_api | techtimes.com | 1 | 0.04% | 0.13% |
| news_api | tecmundo.com.br | 1 | 0.04% | 0.13% |
| news_api | tecnoandroid.it | 1 | 0.04% | 0.13% |
| news_api | tekniikkatalous.fi | 1 | 0.04% | 0.13% |
| news_api | theblaze.com | 1 | 0.04% | 0.13% |
| news_api | theglobeandmail.com | 1 | 0.04% | 0.13% |
| news_api | thepeterboroughexaminer.com | 1 | 0.04% | 0.13% |
| news_api | therecord.com | 1 | 0.04% | 0.13% |
| news_api | thetoc.gr | 1 | 0.04% | 0.13% |
| news_api | tivi.fi | 1 | 0.04% | 0.13% |
| news_api | tn.com.ar | 1 | 0.04% | 0.13% |
| news_api | tomshardware.com | 1 | 0.04% | 0.13% |
| news_api | top-channel.tv | 1 | 0.04% | 0.13% |
| news_api | travelweekly.com.au | 1 | 0.04% | 0.13% |
| news_api | tribuneindia.com | 1 | 0.04% | 0.13% |
| news_api | trthaber.com | 1 | 0.04% | 0.13% |
| news_api | trustedreviews.com | 1 | 0.04% | 0.13% |
| news_api | turkiyegazetesi.com.tr | 1 | 0.04% | 0.13% |
| news_api | twincities.com | 1 | 0.04% | 0.13% |
| news_api | udn.com | 1 | 0.04% | 0.13% |
| news_api | ukrinform.ua | 1 | 0.04% | 0.13% |
| news_api | unian.net | 1 | 0.04% | 0.13% |
| news_api | us.cnn.com | 1 | 0.04% | 0.13% |
| news_api | vecer.com | 1 | 0.04% | 0.13% |
| news_api | vedomosti.ru | 1 | 0.04% | 0.13% |
| news_api | vesti-ua.net | 1 | 0.04% | 0.13% |
| news_api | vg.no | 1 | 0.04% | 0.13% |
| news_api | volksstimme.de | 1 | 0.04% | 0.13% |
| news_api | vrt.be | 1 | 0.04% | 0.13% |
| news_api | war.obozrevatel.com | 1 | 0.04% | 0.13% |
| news_api | watson.ch | 1 | 0.04% | 0.13% |
| news_api | wbaltv.com | 1 | 0.04% | 0.13% |
| news_api | wcbi.com | 1 | 0.04% | 0.13% |
| news_api | webinars.govtech.com | 1 | 0.04% | 0.13% |
| news_api | welt.de | 1 | 0.04% | 0.13% |
| news_api | weser-kurier.de | 1 | 0.04% | 0.13% |
| news_api | winfuture.de | 1 | 0.04% | 0.13% |
| news_api | wlox.com | 1 | 0.04% | 0.13% |
| news_api | wlwt.com | 1 | 0.04% | 0.13% |
| news_api | wmur.com | 1 | 0.04% | 0.13% |
| news_api | words.filippo.io | 1 | 0.04% | 0.13% |
| news_api | world.kbs.co.kr | 1 | 0.04% | 0.13% |
| news_api | wowo.com | 1 | 0.04% | 0.13% |
| news_api | wsbtv.com | 1 | 0.04% | 0.13% |
| news_api | wthr.com | 1 | 0.04% | 0.13% |
| news_api | wtsp.com | 1 | 0.04% | 0.13% |
| news_api | wusa9.com | 1 | 0.04% | 0.13% |
| news_api | wvtm13.com | 1 | 0.04% | 0.13% |
| news_api | wwltv.com | 1 | 0.04% | 0.13% |
| news_api | wwmt.com | 1 | 0.04% | 0.13% |
| news_api | wwwhatsnew.com | 1 | 0.04% | 0.13% |
| news_api | wxii12.com | 1 | 0.04% | 0.13% |
| news_api | y95country.com | 1 | 0.04% | 0.13% |
| news_api | yeniakit.com.tr | 1 | 0.04% | 0.13% |
| news_api | yn.xinhuanet.com | 1 | 0.04% | 0.13% |
| news_api | zdnet.com | 1 | 0.04% | 0.13% |
| news_api | zeit.de | 1 | 0.04% | 0.13% |
| news_api | zetatijuana.com | 1 | 0.04% | 0.13% |

## Top 30 Inspection Words By source_type

### cve

vulnerability (967), file (413), kernel (369), may (348), issue (339), fix (328), exploit (321), attackers (319), function (299), linux (288), used (287), following (285), resolved (270), attacker (268), attack (266), user (259), allows (257), access (253), manipulation (248), code (234), path (229), arbitrary (221), remote (207), argument (205), component (201), prior (196), version (194), data (192), system (189), affected (186)

### news_api

ddos (43), malware (40), ransomware (37), cyberattack (36), new (31), data (31), security (29), cyber (27), attack (27), threat (23), google (20), exploit (20), zero (20), attacks (19), day (19), siber (17), breach (16), hit (15), latest (15), bahn (15), fbi (14), ascii (14), fake (14), scam (14), hackers (14), claude (14), news (14), windows (13), android (13), risk (13)

### news_rss

vulnerability (500), security (389), exploitation (379), windows (360), data (311), likely (299), access (279), less (237), process (226), privilege (203), code (201), elevation (198), file (187), new (184), system (175), exploit (173), microsoft (170), vulnerabilities (167), one (164), also (161), used (161), pointer (159), teams (155), buffer (150), user (149), using (147), attack (143), execution (141), would (135), function (132)

### reddit_rss

link (377), comments (373), submitted (365), like (134), use (99), security (91), would (83), https (74), one (74), data (71), system (68), new (65), windows (64), code (63), anyone (62), still (61), time (61), using (59), com (57), know (57), work (56), something (56), don (54), also (54), actually (52), years (52), people (51), access (50), need (49), even (48)
