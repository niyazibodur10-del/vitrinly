# F2 ön doğrulama — finans-dogrulayici · 2026-11-04

İLERLEME: tamam (12 senaryo tarandı; öncelik S01, S05, S07, S03, S08 derin, diğerleri hook + çekirdek iddia).
**Özet:** YEŞİL 3 (S06, S08, S11) · SARI 9 (S01, S02, S03, S04, S05, S07, S09, S10, S12) · KIRMIZI 0.
**Ölçüt:** YEŞİL = hook ve çekirdek iddialar doğrulandı, F3'te yalnız küçük iş kalıyor · SARI = hook, başlık veya tezde düzeltme şart (aşağıdaki yeniden yazımla çözülüyor) · KIRMIZI = çekirdek iddia çürük ya da hukuki risk çözülemiyor.
**Öncelikli 5:** S08 YEŞİL (en temiz) · S01 SARI (tez/başlık mantık hatası + Binance ölçüsü) · S05 SARI (hook karşıtlığı bozuk: Japonya faizi de 30 yılın zirvesinde) · S07 SARI (1999 → 2000, 14,4 → 15,4 milyar $) · S03 SARI (124 T$ BofA'nın değil Cerulli'nin; eş ve bağış zaten içinde).
**Kanıt:** FRED NASDAQCOM betikle (zirve 10.03.2000 5.048,62 → dip 09.10.2002 1.114,11 = %77,93) · Fiscal Data debt_to_penny (02.11.2026: 40,502 T$; intragov 7,782 T$) · INSEE IR239 (2Ç 2026 %119,0) · Eurostat 2Ç 2026 İtalya %139,9 · SEC OIG Rapor 509 (Markopolos Mayıs 2000) · trustee/BusinessWire 27.02.2026 (15,366 milyar $).
**Hakeme not:** SARI'ların hepsi tek cümlelik yeniden yazımla düzeliyor. Kazanan S01, S05 veya S07 olursa aşağıdaki "güvenli hook" metne aynen girmeli; F3 rakam tablosu bu dosyadan başlar.
Etiket: **[D]** birincil/2+ kaynakla doğrulandı · **[A]** arama özeti/tek ikincil kaynak · **[X]** doğrulanamadı → metne girmez · **[H]** betik hesabı.

## Senaryo kararları
| ID | Karar | Gerekçe (kısa) | F3'te gereken birincil kaynak |
|---|---|---|---|
| S01 | SARI | Binance 6,3 = şirketin "etkilenen varlık" tahmini; dizüstü = çalışma hipotezi; tez "Bigger heists" veriyle çelişiyor | Binance resmi açıklaması / post-mortem; BB 951 M$ açıklaması (Reuters 2016); NYT 2003 CBI |
| S02 | SARI | Madoff oranı %80 değil ≈%88; Yüksek Mahkeme 5 Ekim [X] | madofftrustee.com; supremecourt.gov order list 05.10.2026 |
| S03 | SARI | 124 T$ = Cerulli (Ara 2024, 2048'e kadar); 54 T$ eş + 18 T$ bağış rakamın içinde → "sızıntı" diye çıkarılırsa çift sayım | Cerulli basın bülteni; BofA 2026 Study of Wealthy Americans |
| S04 | SARI | Hook örnek sokak (sorunsuz), ama gövdedeki rakamların neredeyse hepsi [doğrulanacak]; konut tavsiye algısı | Census AHS/ACS, NAR, Japonya 2023 Konut Araştırması |
| S05 | SARI | Fransa %119,0 [D], İtalya %139,9 [D], OAT >%5 (21 Eki) [D]; ama "bu yıl fırlayan Fransa'nın faizi" yanıltıcı: JGB 10y 24 Eyl 2026 %3,055, 1996'dan beri en yüksek [A] | IMF WEO Eki 2026, MoF Japonya getiri serisi, Banque de France/AFT, BoJ akış verisi |
| S06 | YEŞİL | 40,50 T$ [D]; intragov 7,78 T$ = %19,2 [H] | TIC (Japonya/Çin), H.4.1, MSPD |
| S07 | SARI | SEC'e ilk başvuru Mayıs 2000 (OIG) — hook 1999 diyor; geri kazanım 15,37 milyar $; kayıp 17,5 milyar $ (trustee) | SEC OIG-509; madofftrustee.com; DOJ 2009 itiraf; Markopolos 2009 ifadesi |
| S08 | YEŞİL | Nasdaq rakamları FRED'le birebir [D/H]; Pets.com 9 ay [A, 2. kaynak F3]; 480 milyar $ Çin AI tek kaynak [A] | FRED NASDAQCOM; Pets.com SEC dosyaları; 5 T$ için Fed/WSJ |
| S09 | SARI | Hook'un çekirdeği (NPR 16.10.2012, Celebrity Net Worth) tek kaynak (Ancient Origins) — hook kuralı 2 kaynak | NPR 2012 transkripti; BBC 2019 |
| S10 | SARI | "up to 400 billion" = bugünkü piyasa değerinin %10'u; seyrelmeyi yok sayıyor → yanıltıcı | Apple 10-K hisse sayısı; Wayne sözleşmesi 1976 |
| S11 | YEŞİL | 42 milyar $ (9 Mart), 10 Mart el koyma [A: W-SVB] | Fed Barr raporu 28.04.2023; FDIC |
| S12 | SARI (hafif) | "over fifty" yalnız COMEX gün içi (50,35 $); Londra fiksi 49,45 $ (hafıza kuralı) | LBMA fiks; CFTC 1982 raporu |

## S01 — ayrıntı
| İddia | Durum | Düzeltme |
|---|---|---|
| Binance "six point three billion left" | düzeltilmeli [A, 3 bağımsız haber: BleepingComputer, Euronews, PC Gamer] | 6,3 = Binance'in **etkilenen varlık** tahmini; ~3 milyar $ 30 Eki sabahı donduruldu; bir raporda 5,912 milyar $ (doğrulanmamış). "left" yerine "was hit" |
| "through one laptop" | düzeltilmeli | Binance: ele geçirilmiş bir DevOps mühendisi dizüstü = **çalışma hipotezi**, kapanmış inceleme değil. "early findings point to" |
| Kuzey Kore | doğru (koşullu) | TRM Labs, Chainalysis, Elliptic diyor; hükümet teyidi yok (30 Eki). Aynen "researchers suspect" |
| Bybit ~1,5 milyar $; 4,2 kat | doğru [H: 6,3/1,5 = 4,2; 5,7/1,5 = 3,8] | "about four times" |
| Irak ~1 milyar $ | doğru [A, 3 kaynak] | Saddam imzalı not 920 milyon $ + 90 milyon € ≈ 1 milyar $; "nearly a billion" ✓ |
| "over five hours" | doğrulanamadı (tek kaynak W-CBI; NYT: 04:00'te geldi, "several hours") | "in a few hours" veya düşür |
| Bangladeş denenen | doğru [A, 3 kaynak: BB açıklaması 951 M$] | "nearly a billion" ✓ (951 de yazılabilir); 35 talimat, 5'i işledi, 101 M$ |
| Bangladeş geri dönüş | doğru (aralık) | Sri Lanka 20 M$ tam; Filipinler ~15 M$ (kaynaklarda 14,5–18); Dakka mahkemesi 2025'te 81 M$ el koyma emri verdi, uygulanmadı |
| **Tez/başlık "Bigger heists"** | **düzeltilmeli (mantık)** | Kronolojik sıra para olarak artmıyor: Irak ~1.000 M$ > Mt. Gox ~473 M$ > Bangladeş 101 M$ < Binance 6.300 M$. "Every record heist took less" (alt 2) ve H2 "each one moved more than the one before" **yanlış**. "para ↑" eğrisi çizilemez. Çözüm: "each was the record **of its kind**" ya da ölçüt "ne gerekti" (para değil) |
| Mt. Gox "heist" | hukuk riski | Kayıp yıllara yayılmış hırsızlık + yönetim; Karpelès zimmetten **beraat**, yalnız veri manipülasyonundan mahkûm (2019) [F3 teyit] → ona hırsız denmez; "hackers drained it over years" |

**Güvenli hook adayları (yazar seçer):**
1. "In two thousand three, nearly a billion dollars left Iraq's central bank in trucks. This October, Binance said about six point three billion dollars was hit, and early findings point to one laptop. Let's rank history's biggest heists by what they needed."
2. "…This October, Binance estimated six point three billion dollars was hit, in a breach it traces, for now, to one laptop…"
3. "about six billion" sürümü (rakam soruşturmada değişirse; F7 tek cümle).
Shorts 2: "a billion dollars left" → "nearly a billion"; "six billion left through a laptop" → "Binance says about six billion was hit, possibly through one laptop".

## S05 — ayrıntı
| İddia | Durum | Düzeltme |
|---|---|---|
| Fransa ~%119 | doğru [D: INSEE 2Ç 2026 %119,0; 3.595,5 milyar €] | "at mid-twenty twenty-six" |
| Japonya ">twice" | doğru [A; IMF ~%230 F3] | aynen |
| İtalya %140 | doğru [D: Eurostat 2Ç 2026 %139,9; 2025 yıllık %137,1] | "about one hundred forty" |
| Fransa 10y >%4,9 | doğru [A: 21 Eki >%5 (24 yılın zirvesi, Reuters), 27 Eki 4,72, 30 Eki 4,95] | Tarih şart: "topped five percent in late October" |
| +130 bp Haziran'dan | doğrulanacak (tek kaynak AJ) | Banque de France/MTS günlük seriyle betik |
| Açık %5,4 | çelişki | AJ 2026 %5,4 / IFRAP 2Ç kümülatif %5,14 → hükümet hedefi mi gerçekleşme mi ayır |
| **Hook "this year it's France's borrowing costs that jumped"** | **düzeltilmeli** | JGB 10y Ara 2025 %1,95 → 24 Eyl 2026 %3,055 (+~110 bp, 1996'dan beri zirve) [A, 3 kaynak]. Japonya'nın faizi de fırladı. Paradoks **seviye** üzerinden kurulmalı |

**Güvenli hook adayları:** (1) "Japan owes more than twice the size of its whole economy. France owes about one hundred nineteen percent. Yet France pays more to borrow: around five percent for ten years, against about three for Japan. So which number really tells you which rich country breaks first?" (2) "…Yet lenders charge France more than Japan…" (3) "…Yet it's France that markets are nervous about…" (niteliksel; en zayıf). Ekim JGB değeri F3'te MoF serisinden.

## S07 — ayrıntı
| İddia | Durum | Düzeltme |
|---|---|---|
| "In 1999, an analyst told regulators" | **düzeltilmeli** | SEC OIG-509: Markopolos Boston ofisine **Mayıs 2000**'de gitti; sonra 2001, Kasım 2005 (21 sayfalık not), 2007–08. Wikipedia "May 1999" diyor → birincil OIG seçildi. 1999 = analizi yaptığı yıl |
| "nine more years" | düzeltilmeli [H: Mayıs 2000 → Aralık 2008 = 8,6 yıl] | "eight more years" veya "until two thousand eight" |
| "almost no bumps" | doğru [A: Markopolos — kayıplı ay %4; 2009 ifadesi 87 ayda 3 kayıplı ay, S&P 500'de 28] | aynen; grafikte "3 / 87" kullanılabilir |
| Kâğıtta ~65 milyar $ | doğru (kâğıt bakiye; nominal) | "on paper" şart |
| Gerçek kayıp ~18 milyar $ | düzeltilmeli | Trustee tahmini **17,5 milyar $** ana para → "about seventeen and a half" |
| Geri kazanım ~14,4 milyar $ | eskimiş | **15,366 milyar $** (31.01.2026, trustee/BusinessWire 27.02.2026) [D]; oran 15,37/17,5 = %88 [H] |
| Yüksek Mahkeme 5 Eki 2026 | doğrulanamadı [X] (tek kaynak Law360 başlığı, aramada yok) | Metne girmez ya da supremecourt.gov order list ile teyit; yedek: "the legal fight still isn't over" |
| 150 yıl, 14.04.2021 ölüm, 11.12.2008 tutuklama | doğru [A: W-MAD; DOJ F3] | — |
| Hassasiyet | uyarı | Mark ve Andrew Madoff'un ölümleri anlatılmaz; mağdurlar "thousands of investors" (sayı yok); feeder fonlar ve SEC personeli için suç dili yok ("missed", OIG'nin ifadesi); Madoff'un kendisi suçunu kabul etti (2009) → "fraud" güvenli |
**Güvenli hook:** "…That smooth line was the clue. By two thousand, an analyst had told regulators it was mathematically impossible. So why did it take until two thousand eight?"

## S03 — ayrıntı
| İddia | Durum | Düzeltme |
|---|---|---|
| "124 trillion… Bank of America says" | düzeltilmeli | Rakam **Cerulli Associates**'in (Ara 2024, **2048'e kadar**); BofA aktarıyor. "estimates from Cerulli, cited by Bank of America, through twenty forty-eight" |
| Kırılım | doğru [A, 3 kaynak] | 105 T$ mirasçılara, 18 T$ bağışa; 54 T$ önce hayatta kalan eşe |
| Sızıntı 3 (eş) + 4 (bağış) | **çift sayım riski** | Bunlar 124'ün **içinde**; "124'ten sızıyor" denirse yanlış. Doğrusu: "of the headline, 18 goes to charity and 54 stops at a spouse first" — ayrıca güçlü bir açılış ödülü |
| "biggest handover of money ever" | yorum [T] | "often called the biggest…" |
| %47 / %55 | doğrulanacak (FOR-124) | BofA çalışmasının yayın tarihi çelişkili (Haziran mı 6 Ekim mi) → F3 |

## S08 ve diğerleri — kısa notlar
- **S08:** %78 = nominal **fiyat** endeksi (hafıza kuralı: "price" kelimesi veya ekran notu). 480 milyar $ Çin AI tek ikincil kaynak → doğrulanmazsa metinden çıkar. Bugünkü şirketler Pets.com'a benzetilmez (yazar zaten yazmış) ✓. Gelecek "üç olasılık" ✓.
- **S02:** Hook "over fourteen billion has come back" hâlâ doğru (15,4) ama güncel yaz; oran %88. Irak parasının ~650 milyon $'ı 2003'te saraylarda bulundu [A: CNN/NYT 2003] → "rakam yok" notu yanlış, F3 teyit.
- **S06:** "who's at the front" — intragov 7,78 T$ tek kalem olarak en büyük; ama yabancıların **toplamı** (~9 T$, TIC F3) daha büyük → "single biggest holder" diye kur. "Japan, not China" TIC ile F3.
- **S10:** Güvenli: "Ten percent of today's Apple would be worth hundreds of billions on paper, though early stakes usually get diluted." Wayne ve Hanyecz yaşıyor → saygılı dil ✓.
- **S11:** "The next morning" ✓ (9 Mart çekim, 10 Mart el koyma). 250.000 $ FDIC sınırı F3.
- **S12:** "over fifty" → "about fifty" ya da "briefly over fifty on the futures market". 195 milyon ons tek kaynak (W-SILV) → F3 CFTC.
- **S09:** Hook iddiası doğruysa çok güçlü; NPR 2012 arşiv transkripti bulunmazsa "a number popularised online around twenty twelve".

## Tavsiye dili ve yasal not (tüm senaryolar)
- Taramada "buy/sell/should you/guaranteed" yok ✓. Riskli bölgeler: S04 (konut), S08 (AI hisseleri), S12 (gümüş bugün), S07 kapanış ("too smooth" işareti) → "This isn't advice; it's a pattern worth asking questions about." / "Some investors treat this as a reason to ask more questions" kalıpları.
- Açıklama notu (her video): "This video is for education and entertainment only and is not financial, investment, legal or tax advice. Scenarios about the future are possibilities, not predictions. Leo is a fictional cartoon character. Figures are as of the dates shown; sources are listed below." S01/S02 ek: "Investigations are ongoing; figures may change." S07 ek: "Out of respect for the victims, this video does not dramatise any real person." Sponsorlu/affiliate yok → FTC satırı gerekmez.

## Kaynaklar (bu tur)
- Binance: bleepingcomputer.com/news/security/binance-links-63-billion-crypto-theft-to-compromised-devops-laptop · euronews.com/2026/10/30/how-the-binance-hack-happened-and-who-was-behind-it · pcgamer.com (record $6.3 billion heist)
- Fransa: insee.fr/fr/statistiques/9053525 · tradingeconomics.com/france/government-bond-yield/news/593806 · thedailyguardian.com (5% highest since 2002) · İtalya: eunews.it/en/2026/10/21/eurozone-debt-rises-in-the-second-quarter-of-2026…
- Japonya JGB: businesstoday.com.my/2026/09/24/japans-10-year-bond-yield-hits-30-year-high… · euronews.com/2026/08/17/japans-10-year-bond-yield-hits-a-30-year-high… · english.adnkronos.com/2025/12/05/… (1,95)
- Madoff: sec.gov/files/oig-5090.pdf · en.wikipedia.org/wiki/Harry_Markopolos · businesswire.com/news/home/20260227862149/en
- Cerulli: cerulli.com/press-releases/cerulli-anticipates-124-trillion-in-wealth-will-transfer-through-2048 · thinkadvisor.com/amp/2024/12/09/…
- Irak: irishtimes.com (Saddam withdrew funds) · cnn.com/TRANSCRIPTS/0305/06/lt.03.html · Bangladeş: geo.tv/latest/102210 · unb.com.bd/…/168858
- Veri: fred.stlouisfed.org NASDAQCOM · api.fiscaldata.treasury.gov debt_to_penny (komutlar: `curl -s 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=NASDAQCOM&cosd=2000-03-01&coed=2002-12-31'`; `curl -sg '…/v2/accounting/od/debt_to_penny?sort=-record_date&page[size]=2'`)
