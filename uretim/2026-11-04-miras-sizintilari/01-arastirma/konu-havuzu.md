# F1 — Konu havuzu (trend-avcisi) · 2026-11-04

İLERLEME: tamam (S1 outlier taraması, S2 haber akışı, S3 kalıcı olay listesi bitti; kapı betikle koşuldu, sonuç dosya sonunda).
**Görev:** Paz 2026-11-08 12:00 ET slotu, sütun **A (tarih) veya C (gelecek)**. Niyazi hedefi: milyon izlenme potansiyeli; izlenme ve abone ihtiyacı acil.
**Havuz:** 25 konu = **C 10 · A 13 · B 2** (B yalnız bağlam ve kanca için, bu slota önerilmez). Her konuda ≥2 bağımsız, açılan kaynak (HTTP 200 + anahtar kelime), outlier kanıtı, arama ilgisi ve risk satırı var.
**İlk 5 (öneri, karar F2'de) [ölçüm + tahmin]:** 1) **A1** Biggest heists in money history (Binance'in 6,3 milyar $'ı listenin başına geçti) · 2) **C1** What happens when the boomers are gone (124 trilyon $) · 3) **C2** Which country goes bankrupt first · 4) **A2** Madoff · 5) **C4** AI balonu patlarsa ne olur. Gerekçeler §4'te.
**Etiketler:** [ölçüm] bu çalışmada API ile ölçüldü (2026-11-04) · [kaynak] linkli sayfada okundu (başlık/meta dahil) · [arama özeti] okunmadı · [tahmin] ajan yorumu.

## 0. Yöntem
| Ölçüm | Araç (`01-arastirma/olcum/`) | Durum 2026-11-04 |
|---|---|---|
| Outlier taraması (son 12 ay, izlenme/abone) | `outlier_tarama.py`: yt-dlp arama, filtre "bu yıl + izlenme sırası" (`sp=CAMSAggF`), sorgu başına 30 video → `videos.list` + `channels.list` → `outlier-ham.json` (sha256 `06ae9ef76af5`). Analiz `outlier_analiz.py` → `outlier.tsv` (≥10x), `outlier-3x.tsv` | Çalışıyor. 68 sorgu, 1.739 video; son 12 ayın uzun (≥8 dk) videosu 1.419; **≥10x olan 156** |
| Arama talebi | `youtube_arama.py` (alaka ilk 15 medyanı + en yeni 25) → `aday-talep.json` (33 sorgu, sha256 `8b1f2c0f7da0`) | Çalışıyor. `search.list` kullanılmadı |
| Haber akışı (7–30 gün) | `haber_rss.py` → `haber-7g.json`; `kaynak_bul.py` (RSS → yayıncı URL → 200 + anahtar + meta tarih) → `kaynak.json`, `kaynak2.json` | Çalışıyor |
| Google Trends / Reddit / Wikipedia pageviews | — | Ölçülmedi: Trends 429 ve Reddit 403 (2026-10-27/28 ölçümü), pageviews token tasarrufu için atlandı. İlgi kanıtı YouTube + haber hacmi |

**Okuma:** "oran" = izlenme / kanal abone sayısı (bugünkü abone; video sonrası büyüme oranı düşürür, yani alt sınır). "med" = alaka sırasındaki ilk 15 videonun medyan izlenmesi. Niyazi ölçütü 10–100x; 100x üstü de yazıldı (küçük kanal + algoritma itişi = konu kendi başına taşıyor).

### 0.1 Üç strateji: kaç kaynaklı ve zamanlı konu verdi
| Strateji | Aday | Kapıyı geçen | Zamanlı (30 gün içinde haber kancası) | Not |
|---|---|---|---|---|
| **S1 Outlier taraması** (40 geniş + 28 aday sorgu) | 15 | 12 (C1–C5, C7, A3, A5, A7, A10, A11, B1) | 9 | **En verimli.** Konu desenini doğrudan veriyor (§1) |
| **S2 Haber akışı** (Google News RSS + çözücü) | 8 | 6 (A1, C6, C8, C9, C10, B2) | 6 | En zamanlı; Binance (A1) buradan çıktı, S1 doğruladı |
| **S3 Kalıcı olay listesi + önceki havuz** | 12 | 7 (A2, A4, A6, A8, A9, A12, A13) | 4 | Newton, John Law, lale çılgınlığı, Leeson elendi (§5) |

### 0.2 Önceki dersler
`uretim/*/yayin-sonrasi/` yok (1929 ve S08 videolarının 48 sa/7 g raporu henüz yazılmadı), uygulanacak "sonraki video için" maddesi yok. Hafızadan uygulananlar: link testi 200 + anahtar kelime, tarih sayfa metasından, "alaka medyanı yüksek + 12 ayın en iyisi düşük = talep var, taze rakip yok" okuması (A2 Madoff), izleyicinin yazdığı soruyu ölçme, search.list yerine yt-dlp.
**Önceki havuzdan yeniden puanlananlar:** eski C1 (AI balonu) → C4; eski C3 (ABD borcunu ödeyemezse) → C3; eski A1 (1869 Kara Cuma) → A13 (Paz 11-22'ye uygun, bu slota değil). **S06 (10 yıllık %5 → mortgage, 7,50):** B sütunu, bu A/C slotuna uymuyor. Talep medyanı 4,6 K, milyon potansiyeli düşük [tahmin]. Çarşamba B yedeği olarak kalsın.

## 1. Outlier desenleri (son 12 ay, nişte ≥10x) [ölçüm; yalnız desen, kopya yok]
| Desen | Kanıt (video · izlenme / abone = oran · tarih) | Bizde karşılığı |
|---|---|---|
| **D1 Şok olaydan 1–5 gün sonra "nasıl oldu" hikâyesi** | Gloam "How Binance Lost $6,300,000,000 in One Night" 1,89 M / 6,1 K = **310x** (2026-10-30) | A1 |
| **D2 "Ne olur / sırada ne var" senaryosu (korkulan olay)** | Not Unprecedented "The AI Bubble Will Burst. Here's What Happens Next" 735 K / 2,3 K = **316x** · Finance Bureau "What Happens If Trump Loses The Midterms?" 4,26 M = 32x · Empire of Money "What Happens If the Dollar Collapses? Day-by-Day" 70x | C4, C5, C7 |
| **D3 Borç bilmecesi: "kim kime borçlu / kim önce batar"** | OBF "Which Rich Country Goes Bankrupt First?" **8,64 M** / 741 K = 11,7x (2026-10-13) · Finance Stack 154x · PENNY "Who Does America Owe $40 Trillion? (ELI5)" 169x · Hidden Capital "If Every Nation Is in Debt… Who Are They Paying?" 113x · USAFacts 16,7 M | C2, C3 |
| **D4 Kuşak çatışması (boomer ↔ Gen Z, ev, emeklilik)** | AJ Osborne "What Happens When All the Baby Boomers Are Gone?" 121x · Philosophase 42x (928 K) · "Retired Americans Living in RVs" 100x · "Who Will Buy Boomers' Houses…" 32x | C1 |
| **D5 Ünlü tarihi efsaneyi çürütme** | Greenback Stories "The 1929 Crash Didn't Cause The Great Depression" 366x · Documentary Empire "Where Did Mansa Musa Get So Much Gold?" 66x · hoser "Mansa Musa was far from the richest guy" 863 K | A3 |
| **D6 Tuhaf kişi + absürt servet** | MonteLago "Everyone Called Him an Idiot. He Got Richer Every Time. (Timothy Dexter)" 991 K / 3,9 K = **252x** · "Nizam of Hyderabad, the Richest Man on Earth" 99x | A5, A11 |
| **D7 Dolandırıcılık / gizli para makinesi (2D animasyon)** | DOKio "Scam 1992 … 2D Animation" 104x · Truth Finance (Mallya 53x, Nirav Modi 22x) · The Dictator Lab "How Did Hitler Fund a Huge Military When Germany Was Broke?" 2,0 M = 38x | A2, A7, A10 |

**Desen dersi [tahmin]:** milyonluk outlier'ların hepsi finansa ilgisi olmayanın da soracağı tek bir soru taşıyor (kim önce batar, boomer'lar gidince ne olur, bir gecede 6 milyar nasıl çalındı). Başlıkta tek büyük rakam veya sıralama sorusu var. 2D animasyon + anlatıcı formatı Hindistan'da çok güçlü (D7).

---

## 2. C — Gelecek senaryoları ("senaryo" diye sunulur, tavsiye değil)
Satır biçimi: Özet · Neden şimdi · Global bağ · Kaynaklar · Outlier · İlgi · Risk/Hassas · Neden izlenir.

### C1 — What happens when the boomers are gone? The $124 trillion handover
- **Özet:** Bank of America'ya göre 124 trilyon $ servet el değiştiriyor. Evler, hisseler ve emeklilik fonları satışa çıkınca konut fiyatları, borsa ve miras alan kuşak için olası yollar senaryo olarak anlatılır [kaynak K1; senaryo kısmı tahmin].
- **Neden şimdi:** BofA araştırması 6 Ekim, Dunham'ın "serap" uyarısı 5 Ekim, WBUR programı 7 Ekim. Konu kalıcı, haber kancası taze.
- **Global bağ:** Boomer servet ve konut yığılması ABD, İngiltere, Kanada ve Avustralya'da aynı tartışma; Hindistan'da aile mirası açısından okunur [tahmin].
- **Kaynaklar:**
  - K1: [Wealthy boomers doubt their heirs will keep giving as $124 trillion changes hands](https://fortune.com/2026/10/06/wealthy-baby-boomers-losing-faith-in-heirs-philanthropic-giving-gen-z-millennials-bank-of-america-research/) · Fortune · tarih: 2026-10-06 · anahtar: boomer
  - K2: [Great Wealth Transfer might give way to a 'mirage,' Dunham research warns](https://www.investmentnews.com/retirement-planning/great-wealth-transfer-might-give-way-to-a-mirage-dunham-research-warns/268471) · InvestmentNews · tarih: 2026-10-05 · anahtar: boomer
  - K3: [Senior Class: Old money](https://www.wbur.org/onpoint/2026/10/07/senior-class-wealth-money-baby-boomers) · WBUR On Point · tarih: 2026-10-07 · anahtar: boomer
- **Outlier [ölçüm]:** AJ Osborne 595 K / 4,9 K = **121x** (2026-07-22) · Philosophase "Why Everybody Blames the Boomers Now" 928 K = 42x · Damon Cassidy "Baby Boomers: The Most SELFISH Generation" 1,96 M (5,8x) · Austin Williams "What Happens When All The Boomers Are GONE?" 815 K (2026-09-11).
- **İlgi [ölçüm]:** "what happens when baby boomers die economy" medyanı **424 K**, 15'in 3'ü ≥1 M (How Money Works 2,47 M, 2024). Haber: RSS 28 sonuç / 30 gün.
- **Risk/Hassas:** hayır (ölüm soyut, demografik). Kuşak suçlama dili kutuplaştırabilir; nötr kalınmalı. Rakip doluluğu orta. **Neden izlenir:** Her izleyici ya mirasçı ya da ev alıcısı; bu el değişimi onun geleceğini doğrudan değiştiriyor.

### C2 — Which country goes bankrupt first? A stress test of the world's debt
- **Özet:** Borç/GSYH, faiz yükü ve tahvil faizlerine göre zengin ülkeler arasında "ilk kim zorlanır" senaryosu; Fransa'nın borç maliyetleri örnek olarak kullanılır [kaynak K1, K2 + tahmin].
- **Neden şimdi:** Al Jazeera 20 Ekim (Fransa), Yahoo UK 21 Ekim "21 ülke çöküşe ne kadar yakın". 10 yıllık ABD tahvili %5 üstünde (önceki havuz B5).
- **Global bağ:** ABD, İngiltere, Kanada, Avustralya ve Hindistan'ın hepsi sıralamada yer alır; izleyici kendi ülkesini arar [tahmin].
- **Kaynaklar:**
  - K1: [France's growing debt woes: How bond markets set countries' borrowing costs](https://www.aljazeera.com/economy/2026/10/20/frances-growing-debt-woes-how-bond-markets-set-countries-borrowing-costs) · Al Jazeera · tarih: 2026-10-20 · anahtar: debt
  - K2: [How close are 21 countries to economic collapse?](https://uk.finance.yahoo.com/news/close-21-countries-economic-collapse-150000929.html) · Yahoo Finance UK · tarih: 2026-10-21 · anahtar: debt
  - K3: [Sovereign default](https://en.wikipedia.org/wiki/Sovereign_default) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: default
- **Outlier [ölçüm]:** OBF "Which Rich Country Goes Bankrupt First?" **8,64 M** / 741 K = 11,7x (2026-10-13) · Finance Stack 176 K / 1,1 K = **154x** (2026-11-01) · Broke Economy "(America Is #3)" 17x · Money Matrix "The G7 Country…" 17x.
- **İlgi [ölçüm]:** Tam sorgu medyanı 1,6 K (sorgu yeni, alaka listesi küçük kanallarla dolu), ama 3 haftada 4 yeni video ≥10x: talep taze ve sıcak.
- **Risk/Hassas:** düşük (Sri Lanka gibi gerçek kriz mağdurları anılırsa "hassas"). **Kopya riski yüksek:** OBF'nin sıralama formatı şimdiden kopyalanıyor; açımız farklı olmalı (ör. Leo bir "iflas yarışması"nı hakem gibi yönetir, ölçüt şeffaf). **Neden izlenir:** Herkes kendi ülkesinin listede kaçıncı olduğunu merak ediyor.

### C3 — Who does America owe $40 trillion, and what if they all asked for it back?
- **Özet:** 40 trilyon $'lık borcun sahipleri (Fed, yabancılar, emeklilik fonları, sıradan tasarruf sahipleri) ve "herkes aynı anda geri isterse" senaryosu [kaynak K1–K3 + tahmin].
- **Neden şimdi:** Borç 40 trilyon $'ı geçti; IMF uyarısı 16 Ekim, faiz yükü haberi 21 Ekim.
- **Global bağ:** Japonya, Çin, İngiltere ve Kanada en büyük alacaklılar arasında; doların küresel rolü [tahmin].
- **Kaynaklar:**
  - K1: [With U.S. debt above $40 trillion, the IMF chief warns that economic growth alone won't solve the problem](https://fortune.com/2026/10/16/imf-chief-kristalina-georgieva-warns-us-national-debt-economic-growth-not-enough-scott-bessent-treasury-deficit/) · Fortune · tarih: 2026-10-16 · anahtar: debt
  - K2: [Sizing Up the $40 Trillion National Debt](https://www.independent.org/article/2026/10/20/size-national-debt/) · Independent Institute · tarih: 2026-10-20 · anahtar: debt
  - K3: [Interest payments on America's $40 trillion debt eats up a huge piece of the budget](https://nypost.com/2026/10/21/business/interest-payments-on-americas-40-trillion-debt-eats-up-a-huge-piece-of-the-budget/) · New York Post · tarih: 2026-10-21 · anahtar: debt
- **Outlier [ölçüm]:** PENNY "Who Does America Owe $40 Trillion? (ELI5)" 860 K / 5,1 K = **169x** (2026-10-24) · Hidden Capital 113x · USAFacts "How Big Is the US National Debt?" 16,7 M = 13,7x · Infographics "What If The World Dumps US Debt?" 1,13 M (0,1x, dev kanal).
- **İlgi [ölçüm]:** Tam sorgu medyanı 42 K; "what happens if america defaults" medyanı 102 K, 3 video ≥1 M (How Money Works 3,09 M, 2026-09-07).
- **Risk/Hassas:** hayır. S08 (ABD bütçesi = bir hane) ile örtüşme riski: aynı veriyi tekrar kullanmamalı [tahmin]. **Neden izlenir:** "Borç" denince kimse kime borçlu olunduğunu bilmiyor; cevap şaşırtıcı.

### C4 — The AI bubble pops: what happens next, month by month
- **Özet:** Çin'in AI hisselerinde 480 milyar $'lık düşüşü ve ABD teknoloji satışları model alınarak "patlarsa ilk 12 ay" senaryosu [kaynak K1–K3 + tahmin].
- **Neden şimdi:** Futurism 30 Ekim "Stock Market Bloodbath", Nvidia bilançosu 17 Kasım [arama özeti, haber-7g.json].
- **Global bağ:** Endeks fonu ve emeklilik hesabı olan herkes; İngiltere için Oxford Economics resesyon uyarısı [arama özeti].
- **Kaynaklar:**
  - K1: [Stock Market Bloodbath Spikes Fears of AI Bubble Bursting](https://futurism.com/future-society/stock-market-bloodbath-ai-bubble-earnings) · Futurism · tarih: 2026-10-30 · anahtar: bubble
  - K2: [China's AI Bubble Bursts: Tech Stock Crash Wipes $480 Billion](https://www.globalbankingandfinance.com/analysis-in-china-ai-bubble-already-burst/) · Global Banking & Finance Review · tarih: 2026-10-26 · anahtar: bubble
  - K3: [How to invest if you think the AI bubble is about to burst](https://africa.businessinsider.com/markets/how-to-invest-if-you-think-the-ai-bubble-is-about-to-burst/qnln2t5) · Business Insider Africa · tarih: 2026-11-02 · anahtar: bubble
- **Outlier [ölçüm]:** Not Unprecedented 735 K / 2,3 K = **316x** (2026-10-09) · Silicon Money "Why Tech CEOs Are Quietly Cancelling Their AI Plans" 85x · Economy Media "How AI Became More Expensive Than The Workers It Replaced" 3,3 M = 24x · Infographics "The AI bubble is about to pop…" 4,24 M (2026-10-27).
- **İlgi [ölçüm]:** "what if the ai bubble pops" medyanı **591 K**, 4 video ≥1 M. En yüksek talep, ama en yüksek doygunluk.
- **Risk/Hassas:** hayır. **Doygunluk çok yüksek:** Infographics'in "day by day" formatı iki kez yapıldı, kopya cezası riski var [tahmin]. **Neden izlenir:** Herkesin korktuğu çöküşün somut bir takvimi.

### C5 — Blue sweep: what happens to your money in 2027?
- **Özet:** Ara seçimin ilk sonuçları Demokratların Kongre'yi alabileceğini gösteriyor (sonuç kesinleşmedi). Bölünmüş hükümetin vergi, harcama, borç tavanı ve AI düzenlemesi için olası yolları [kaynak K1; senaryo tahmin].
- **Neden şimdi:** Seçim 3 Kasım; Reuters/Yahoo 4 Kasım "early results point to blue sweep". **Bayatlama:** orta; 8 Kasım'a kadar sonuç netleşir, haftalarca konuşulur.
- **Global bağ:** Zayıf–orta: dolar ve borsa üzerinden; seçimin kendisi ABD'ye özgü.
- **Kaynaklar:**
  - K1: [Analysts react to US midterm election results](https://finance.yahoo.com/markets/stocks/articles/analysts-react-us-midterm-election-025738421.html) · Yahoo Finance (Reuters) · tarih: 2026-11-04 · anahtar: Democrat
  - K2: [What the midterm elections could mean for markets, debt](https://www.foxbusiness.com/politics/what-midterm-elections-could-mean-markets-debt) · Fox Business · tarih: 2026-11-03 · anahtar: Democrat
  - K3: [US midterm elections promise political uncertainty but economic stability](https://home.cib.natixis.com/articles/us-midterm-elections-promise-political-uncertainty-but-economic-stability) · Natixis CIB · tarih: 2026-11-03 · anahtar: Democrat
- **Outlier [ölçüm]:** Finance Bureau "What Happens If Trump Loses The Midterms?" **4,26 M** / 134 K = 32x (2026-10-16) · Political Pengu 155x · TLDR News Global 1,90 M.
- **İlgi [ölçüm]:** Tam sorgu medyanı 22 K; talep seçimden önce zirve yaptı, sonrası ölçülmedi.
- **Risk/Hassas:** siyasi içerik; reklam uygunluğu için tarafsız dil şart → monetizasyon-uyum-uzmani. Global kitle bağı zayıf. **Neden izlenir:** Sonuç belli oldu, şimdi herkes cebine ne olacağını soruyor.

### C6 — What if everyone pulled their money out at once? (And AI agents could make it happen in seconds)
- **Özet:** Kesirli rezerv bankacılığı neden "herkes aynı anda isterse" dayanamaz; bankalar müşterilerin AI ajanlarının ucuz mevduatı tek tıkla kaydırmasından korkuyor [kaynak K1, K2 + tahmin].
- **Neden şimdi:** American Banker 28 Ekim, Yahoo 29 Ekim.
- **Global bağ:** Banka hesabı olan herkes; 2023 SVB koşusu hatırlanıyor [tahmin].
- **Kaynaklar:**
  - K1: [Understanding the banking industry's reaction to AI agents](https://www.americanbanker.com/opinion/understanding-the-banking-industrys-reaction-to-ai-agents) · American Banker · tarih: 2026-10-28 · anahtar: bank
  - K2: [Banks fear customers' AI agents could drain the cheap deposits they need to make loans](https://finance.yahoo.com/technology/ai/articles/banks-fear-customers-ai-agents-090700564.html) · Yahoo Finance · tarih: 2026-10-29 · anahtar: bank
  - K3: [Bank run](https://en.wikipedia.org/wiki/Bank_run) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: run
- **Outlier [ölçüm]:** son 12 ayda ≥10x yok (Tiny Economy "What If Everyone Withdrew Their Money on the Same Day?" 2,2 K, 2026-11-02). **Taze rakip yok.**
- **İlgi [ölçüm]:** "what if everyone withdrew money from banks" medyanı **190 K**, 6 video ≥1 M (liste gürültülü: Kurzgesagt UBI 10,9 M dahil).
- **Risk/Hassas:** hayır; panik dili kullanılmamalı. **Neden izlenir:** "Param bankada duruyor mu?" sorusunun cevabı çoğu kişiyi şaşırtıyor, AI açısı ise yeni.

### C7 — What happens if the dollar collapses? A day-by-day scenario
- **Özet:** Dolar rezerv para statüsünü kaybederse ithalat, faiz, gelişen piyasalar ve havaleler nasıl etkilenir; Çin yuanın "Pepsi" rolünü kabul ediyor [kaynak K1 + tahmin].
- **Neden şimdi:** Fortune 31 Ekim; dolar endeksi seçim sonrası bir ayın en düşüğünde [arama özeti, WSJ başlığı 11-04].
- **Global bağ:** Güçlü: Hindistan (rupi), Kanada, Avustralya; doların küresel rolü herkese dokunur.
- **Kaynaklar:**
  - K1: [China sees yuan vs. dollar like Pepsi vs. Coke](https://fortune.com/2026/10/31/china-us-currency-wars-yuan-vs-dollar-pepsi-coke-pretodollar-dedollarization/) · Fortune · tarih: 2026-10-31 · anahtar: dollar
  - K2: [Reserve currency](https://en.wikipedia.org/wiki/Reserve_currency) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: dollar
- **Outlier [ölçüm]:** Empire of Money "WHAT HAPPENS IF THE DOLLAR COLLAPSES? | A DAY-BY-DAY SCENARIO" 79 K / 1,1 K = **70x** (2025-12-22) · Lock Stock Finance "Petrodollar" 2,93 M = 13x · Prof Steve Keen 977 K.
- **İlgi [ölçüm]:** medyan **170 K**; ≥1 M yok.
- **Risk/Hassas:** hayır; komplo/"reset" dilinden uzak durulmalı. **Neden izlenir:** Dünyanın parası çökerse cebimdeki paraya ne olur sorusu.

### C8 — If AI takes the jobs, who buys anything?
- **Özet:** Goldman'a göre AI her 11 çalışandan birinin yerini alabilir; işsiz tüketici, vergi tabanı ve "AI vergisi" tartışması senaryo olarak [kaynak K1–K3 + tahmin].
- **Neden şimdi:** Goldman tahmini 22 Ekim, Kongre'de işsizlik sigortası tasarıları 23 Ekim.
- **Kaynaklar:**
  - K1: [AI could displace one in 11 workers, Goldman says](https://fortune.com/2026/10/22/goldman-sachs-forecast-how-many-jobs-lost-to-ai-9-percent/) · Fortune · tarih: 2026-10-22 · anahtar: AI
  - K2: [As AI layoff fears mount, lawmakers weigh a bigger safety net for workers](https://www.cbsnews.com/news/ai-layoffs-congress-bills-unemployment-benefits-tax/) · CBS News · tarih: 2026-10-23 · anahtar: AI
  - K3: [Goldman Sachs sees AI-fueled layoffs displacing nearly 10% of workers](https://www.businessinsider.com/ai-layoffs-job-market-prediction-goldman-sachs-2026-10) · Business Insider · tarih: 2026-10-23 · anahtar: AI
- **Outlier [ölçüm]:** ≥10x yok; Meerkat Explains "If AI Takes The Jobs, Who Buys Anything?" 4x (2026-10-30); BBC Global 1,98 M (2x).
- **İlgi [ölçüm]:** tam sorgu medyanı 713 (gürültülü); listede Diary of a CEO 24,5 M "only 5 jobs remain" (2025). Talep büyük ama finans kanallarına değil, sohbet formatlarına gidiyor [tahmin].
- **Risk/Hassas:** hayır. **Neden izlenir:** Herkes işini kaybetme korkusunu yaşıyor; ekonomi sorusu ("kim alışveriş yapacak?") az soruluyor.

### C9 — Social Security's 2032 cliff: what a 26% cut would look like
- **Özet:** CBO'ya göre fon tükenirse 2032'de yardımlar yaklaşık %26 düşebilir; ortalama emekli için anlamı ve olası çözümler [kaynak K3 başlık; rakam F3'te CBO'dan doğrulanmalı].
- **Neden şimdi:** ara seçimin ana konularından (CBS 29 Ekim).
- **Global bağ:** zayıf (ABD); İngiltere/Kanada/Avustralya emeklilik sistemleriyle karşılaştırma yapılabilir [tahmin].
- **Kaynaklar:**
  - K1: [Social Security surfaces as key issue in midterm races as insolvency looms](https://www.cbsnews.com/news/social-security-trust-fund-midterm-elections/) · CBS News · tarih: 2026-10-29 · anahtar: Social Security
  - K2: [The future of Social Security is on the line in the midterms](https://www.ms.now/opinion/social-security-midterm-elections-senate-retirement) · MS NOW · tarih: 2026-10-30 · anahtar: Social Security
  - K3: [Warren Buffett once called cutting Social Security a 'mistake.' Now the CBO says the hit may be 26% by 2032](https://finance.yahoo.com/economy/policy/articles/warren-buffett-once-called-cutting-173000014.html) · Yahoo Finance · tarih: 2026-11-02 · anahtar: Social Security
- **Outlier [ölçüm]:** ≥10x yok; en iyisi Kevin Explains 180 K (2x). Büyük emeklilik kanalları dolu.
- **İlgi [ölçüm]:** medyan 5,4 K; "pension crisis explained" 51 K (Economics Explained "Did Pensions Destroy France?" 748 K).
- **Risk/Hassas:** hayır. **Neden izlenir:** Milyonlarca ailenin aylık geliri bir tarihe bağlı.

### C10 — What if China dumped all its US Treasuries overnight?
- **Özet:** Çin'in kâğıt üzerindeki ABD tahvil stoku azalıyor, ama saklama verisi Belçika ve Kanada üzerinden tuttuğunu gösteriyor. "Bir gecede satarsa" senaryosu [kaynak K1, K2 + tahmin].
- **Neden şimdi:** Fortune 18 Ekim, Yahoo 19 Ekim.
- **Kaynaklar:**
  - K1: [China looks like it's dumping Treasury debt but may actually be stashing it in Canada and Belgium](https://fortune.com/2026/10/18/china-dedollarization-us-treasury-debt-holdings-stealth-canada-belgium-custodians/) · Fortune · tarih: 2026-10-18 · anahtar: Treasur
  - K2: [China's Treasury Pile Is Shrinking on Paper. The Custody Data Tell a Different Story](https://finance.yahoo.com/markets/currencies/articles/chinas-treasury-pile-shrinking-paper-121500428.html) · Yahoo Finance · tarih: 2026-10-19 · anahtar: Treasur
- **Outlier [ölçüm]:** Wealth Chronicles 10x (11 K, küçük). Behind Asia 1,37 M (2025-01, 12 ay dışı).
- **İlgi [ölçüm]:** medyan 1,3 K. Düşük. C3'e alt bölüm olarak girebilir.
- **Risk/Hassas:** hayır. **Neden izlenir:** "Çin elindeki silahı kullanırsa" gerilimi.

---

## 3. A — Geçmiş
### A1 — The biggest heists in money history, and Binance just topped them all
- **Özet:** Binance'ten 29–30 Ekim'de çalınan 5,7–6,3 milyar $ (kaynaklar arası fark var → F3), tarihin en büyük kripto hırsızlığı olabilir. Mt. Gox'tan Bangladeş Merkez Bankası'na büyük para soygunlarının sıralaması ve "nasıl yaptılar" hikâyesi [kaynak K1–K3; diğer soygun rakamları F3].
- **Neden şimdi:** olay 6 gün önce; RSS 55 haber / 10 gün. Kalıcı "en büyük soygunlar" talebiyle birleşiyor.
- **Global bağ:** güçlü: soygun merakı finans dışı izleyiciyi de çeker; kripto kullanıcıları Hindistan ve ABD'de büyük [tahmin].
- **Kaynaklar:**
  - K1: [Binance probes possible $5.7 billion crypto hack, possibly the biggest in history](https://finance.yahoo.com/markets/crypto/articles/binance-probes-possible-5-7-234755783.html) · Yahoo Finance · tarih: 2026-10-30 · anahtar: Binance
  - K2: [Binance probes potential $5.8 billion crypto-theft hack](https://www.bleepingcomputer.com/news/security/binance-probes-potential-58-billion-crypto-theft-hack/) · BleepingComputer · tarih: 2026-10-29 · anahtar: Binance
  - K3: [Bitcoin Price Slides Below $79,000 as Binance Loses $5.8 Billion in Massive Hack](https://bitcoinmagazine.com/news/bitcoin-price-slides-binance) · Bitcoin Magazine · tarih: 2026-10-29 · anahtar: Binance
  - K4: [Mt. Gox](https://en.wikipedia.org/wiki/Mt._Gox) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Gox
- **Outlier [ölçüm]:** Gloam "How Binance Lost $6,300,000,000 in One Night" 1,89 M / 6,1 K = **310x** (2026-10-30, 5 günde) · voidzilla "the largest hack. ever." 2,53 M · CNN 1,54 M · fern "The Bank Heist of the Century" **6,12 M** (2026-03-22).
- **İlgi [ölçüm]:** "biggest bank heist in history" medyanı **2,05 M**, 15'in **10'u ≥1 M** (havuzun en yüksek medyanı). "biggest crypto hack history" medyanı 112 K.
- **Risk/Hassas:** düşük (şiddet yok; "nasıl yapılır" talimatı verilmez, reklam açısından suç anlatımı yalnız bilgi düzeyinde) → monetizasyon-uyum-uzmani bakar. Binance tek başına anlatılırsa Gloam ile örtüşür; açımız **sıralama + tarih**. **Neden izlenir:** Bir gecede 6 milyar doların nasıl kaybolduğunu ve tarihteki büyük soygunlarla yarışını herkes bilmek ister.

### A2 — Bernie Madoff: the $65 billion lie everyone believed
- **Özet:** Madoff'un Ponzi düzeni 2008'de çöktü; yatırımcıların kâğıt üzerindeki kaybı yaklaşık 65 milyar $ [kaynak K1]. Mahkeme süreçleri hâlâ sürüyor [kaynak K2].
- **Neden şimdi:** ABD Yüksek Mahkemesi 5 Ekim'de feeder fon iade (clawback) temyizini reddetti; el konulan bir tablo 9 Ekim'de bulundu. Aralık 2008 çöküşünün 18. yıldönümü [tahmin bağ].
- **Global bağ:** Mağdurlar ABD, Avrupa ve Asya'da; Ponzi kavramı evrensel.
- **Kaynaklar:**
  - K1: [Bernie Madoff](https://en.wikipedia.org/wiki/Bernie_Madoff) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Madoff
  - K2: [High Court Won't Hear Madoff Feeder Funds' Clawback Appeal](https://www.law360.com/articles/2533543/high-court-won-t-hear-madoff-feeder-funds-clawback-appeal) · Law360 · tarih: 2026-10-05 · anahtar: Madoff
  - K3: [Wichita woman finds original painting linked to Bernie Madoff's seized assets](https://www.kake.com/home/wichita-woman-finds-original-painting-linked-to-bernie-madoff-s-seized-assets/article_ca8a6a5a-250a-4a92-ade0-c37c98d72318.html) · KAKE · tarih: 2026-10-09 · anahtar: Madoff
- **Outlier [ölçüm]:** Built on Lies "The Man Who Stole $65 Billion and Made Everyone Thank Him" 91 K / 2,4 K = **38x** (2026-07-03). Başka taze büyük video yok.
- **İlgi [ölçüm]:** medyan **1,18 M**, 15'in **8'i ≥1 M** (FRONTLINE 11,9 M, 2021). **Talep var, taze rakip yok** (hafıza kuralı).
- **Risk/Hassas:** **hassas** (dolandırıcılık mağdurları; oğlu Mark Madoff'un intiharı anlatılırsa) → monetizasyon-uyum-uzmani. Netflix (2023) yüzünden "bildik hikâye" riski var; yeni açı gerekli. **Neden izlenir:** Dünyanın en zeki yatırımcılarının 17 yıl kandırılması.

### A3 — Mansa Musa wasn't the richest man ever. Here's who was
- **Özet:** Mali hükümdarına yakıştırılan "400 milyar $" rakamı 2012'deki bir web sitesi listesine dayanıyor. 1324 hac yolculuğunun Kahire'de altın fiyatını düşürdüğü anlatılıyor [kaynak K1, K2]. Video efsaneyi ve tarihteki gerçek servet karşılaştırmasını anlatır.
- **Neden şimdi:** Ancient Origins doğrulama yazısı 23 Ekim.
- **Global bağ:** güçlü: Hindistan, Afrika ve İngiliz izleyicide yüksek; "richest person ever" evrensel arama.
- **Kaynaklar:**
  - K1: [$400 Billion Mansa Musa Fortune Traces to a 2012 Website List](https://www.ancient-origins.net/news-history-archaeology/mansa-musa-400-billion-richest-man-fact-check-00103294) · Ancient Origins · tarih: 2026-10-23 · anahtar: Mansa
  - K2: [Mansa Musa](https://en.wikipedia.org/wiki/Mansa_Musa) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Mansa
  - K3: [Mansa Musa: Is this the richest man who ever lived?](https://www.bbc.com/news/world-africa-47379458) · BBC · tarih: 2026-11-04 (erişim) · anahtar: Mansa
- **Outlier [ölçüm]:** Documentary Empire "Where Did Mansa Musa Get So Much Gold?" 943 K / 14 K = **66x** · Story Plug Studio (Hintçe) 43x · hoser "Mansa Musa was far from the richest guy" 863 K.
- **İlgi [ölçüm]:** medyan **170 K**, 5 video ≥1 M (jack pockets "Who's The Richest Person In History?" 9,69 M, 2025-09).
- **Risk/Hassas:** hayır (köle ticareti bağlamı anılırsa dikkat). **Neden izlenir:** Herkesin bildiği "tarihin en zengini" bilgisi yanlış çıkıyor.

### A4 — The most expensive mistakes in money history ($800 for 10% of Apple)
- **Özet:** Ronald Wayne 1976'da Apple'daki %10 payını 800 $'a sattı; bugünkü değeri 400 milyar $'a kadar. 10.000 bitcoin'e alınan iki pizza gibi örneklerle bir sıralama [kaynak K1–K3; değerler F3].
- **Neden şimdi:** kalıcı konu; Apple ve Bitcoin haberleriyle her dönem yeniden tetikleniyor. Zayıf kanca.
- **Kaynaklar:**
  - K1: [Apple cofounder Ronald Wayne—whose stake would be worth up to $400 billion](https://fortune.com/2026/04/27/apple-cofounder-ronald-wayne-missed-billionaire-opportunity-no-regrets-gen-z-advice-steve-jobs-steve-wozniak/) · Fortune · tarih: 2026-04-27 · anahtar: Wayne
  - K2: [Ronald Wayne](https://en.wikipedia.org/wiki/Ronald_Wayne) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Wayne
  - K3: [Laszlo Hanyecz](https://en.wikipedia.org/wiki/Laszlo_Hanyecz) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: pizza
- **Outlier [ölçüm]:** BE AMAZED "Most Expensive Mistakes in History - Part 2" 1,16 M (2026-04-19). Nişte ≥10x örnek bulunmadı.
- **İlgi [ölçüm]:** medyan **625 K**, 6 video ≥1 M.
- **Risk/Hassas:** hayır. Liste formatı genel eğlence kanallarında dolu. **Neden izlenir:** "Ben olsam satmazdım" pişmanlık merakı herkese hitap ediyor.

### A5 — The idiot who got rich: Timothy Dexter's accidental fortune
- **Özet:** 18. yüzyıl Newburyport tüccarı Dexter "aptalca" ticaretlerden (Newcastle'a kömür) zengin oldu ve noktalama işaretsiz bir kitap yayımladı [kaynak K1, K2].
- **Neden şimdi:** kanca yok (kalıcı).
- **Kaynaklar:**
  - K1: [Timothy Dexter](https://en.wikipedia.org/wiki/Timothy_Dexter) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Dexter
  - K2: [A Pickle for the Knowing Ones (Project Gutenberg arama)](https://www.gutenberg.org/ebooks/search/?query=pickle+for+the+knowing+ones) · Project Gutenberg · tarih: 2026-11-04 (erişim) · anahtar: Pickle
- **Outlier [ölçüm]:** MonteLago 991 K / 3,9 K = **252x** (2026-07-14).
- **İlgi [ölçüm]:** medyan 70 K; Sam O'Nella 17,0 M (2020).
- **Risk/Hassas:** hayır. İkinci kaynak zayıf (birincil kitap listesi); F3'te tarih kaynağı lazım. **Neden izlenir:** Her kararı yanlış olan adamın her seferinde kazanması.

### A6 — The dot-com crash: the AI bubble's dress rehearsal
- **Özet:** 1995–2000 internet balonu ve Nasdaq'ın 2000–2002 çöküşü; Dalio'nun balon göstergesi AI'yı 1929 ve 2000 ile aynı seviyede görüyor [kaynak K1, K2].
- **Neden şimdi:** AI satışları (C4); Dalio yorumu 17 Ekim.
- **Kaynaklar:**
  - K1: [Dot-com bubble](https://en.wikipedia.org/wiki/Dot-com_bubble) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: dot-com
  - K2: [Ray Dalio says his bubble indicator puts AI level with 1929 and 2000](https://ppc.land/ray-dalio-says-his-bubble-indicator-puts-ai-level-with-1929-and-2000/) · PPC Land · tarih: 2026-10-17 · anahtar: dot-com
  - K3: [Is There an AI Bubble and What Does That Even Mean?](https://losspreventionmedia.com/is-there-an-ai-bubble-what-does-that-even-mean/) · Loss Prevention Magazine · tarih: 2026-10-27 · anahtar: dot-com
- **Outlier [ölçüm]:** ≥10x yok; Damon Cassidy 2,21 M (7x), Infographics "AI Bubble vs Dot Com Crash" 628 K.
- **İlgi [ölçüm]:** medyan **386 K**, 2 video ≥1 M.
- **Risk/Hassas:** hayır. C4 ile birleşebilir. **Neden izlenir:** "Bunu daha önce yaşadık mı?" sorusunun cevabı.

### A7 — How Hitler paid for a war with money that didn't exist (MEFO bills)
- **Özet:** Nazi Almanyası silahlanmayı bütçe dışı MEFO senetleriyle finanse etti [kaynak K1]; Weimar sonrası ekonomik bağlam [kaynak K2].
- **Kaynaklar:**
  - K1: [Mefo bills](https://en.wikipedia.org/wiki/Mefo_bills) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Mefo
  - K2: [Germany After WWI: Economic, Social, and Political Aftermath](https://encyclopedia.ushmm.org/content/en/article/world-war-i-aftermath) · Holocaust Encyclopedia (USHMM) · tarih: 2026-09-22 · anahtar: Weimar
- **Outlier [ölçüm]:** The Dictator Lab 1,99 M / 52,7 K = **38x** (2025-11-20) · How Business Worked "bUt hItLer fIxEd ThE eCoNomY!" 1,44 M.
- **İlgi [ölçüm]:** medyan 2,0 K (tam sorgu); Money & Macro "How the Nazis created an economic miracle" 1,88 M.
- **Risk/Hassas:** **hassas** (Nazi rejimi, savaş, Holokost bağlamı) → reklam uygunluğu riski yüksek; maskotlu animasyonda ton zor [tahmin]. **Neden izlenir:** Batık bir ülkenin dünyanın en büyük ordusunu nasıl finanse ettiği gizemi.

### A8 — The brothers who tried to buy all the world's silver
- **Özet:** Hunt kardeşler 1979–80'de gümüşü köşeye sıkıştırmaya çalıştı; 27 Mart 1980 "Silver Thursday" çöküşü [kaynak K1].
- **Neden şimdi:** gümüş 2026'nın en düşüğünde, altın zirveden ~%30 aşağıda (B1).
- **Kaynaklar:**
  - K1: [Silver Thursday](https://en.wikipedia.org/wiki/Silver_Thursday) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Hunt
  - K2: [Silver Price Hits 2026 Low. Will It Crash Further?](https://finance.yahoo.com/markets/commodities/articles/silver-price-hits-2026-low-103125664.html) · Yahoo Finance · tarih: 2026-10-25 · anahtar: silver
- **Outlier [ölçüm]:** Investigate Money "They Bought Nearly All the World's Silver" 313 K = **12x** · Why X "Silver Is Running Out… So Why Is It Crashing?" 766 K = 17x.
- **İlgi [ölçüm]:** medyan 20 K.
- **Risk/Hassas:** hayır. **Neden izlenir:** İki milyarderin bir metali tekeline alıp her şeyi kaybetmesi.

### A9 — Weimar hyperinflation: when a loaf of bread cost 200 billion marks
- **Özet:** 1921–23 Almanya'sında fiyatlar her birkaç günde ikiye katlandı [kaynak K1, K2; rakam F3].
- **Neden şimdi:** yeni Weimar kitabı (Globe and Mail 23 Ekim); enflasyon kalıcı tema.
- **Kaynaklar:**
  - K1: [Hyperinflation in the Weimar Republic](https://en.wikipedia.org/wiki/Hyperinflation_in_the_Weimar_Republic) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Weimar
  - K2: [Germany After WWI: Economic, Social, and Political Aftermath](https://encyclopedia.ushmm.org/content/en/article/world-war-i-aftermath) · USHMM · tarih: 2026-09-22 · anahtar: Weimar
  - K3: [New book about doomed Weimar Germany reveals fascinating contradictions](https://www.theglobeandmail.com/culture/books/article-sebestyens-history-of-doomed-weimar-germany-reveals-fascinating/) · The Globe and Mail · tarih: 2026-10-23 · anahtar: Weimar
- **Outlier [ölçüm]:** ≥10x yok (12 ayda en iyisi Markets of the Past 77 K).
- **İlgi [ölçüm]:** medyan 49 K, 2 video ≥1 M (eski).
- **Risk/Hassas:** düşük–orta (Nazilerin yükselişi anlatılırsa) [tahmin]. **Neden izlenir:** Paranın değerini kaybetmesinin en görsel örneği (el arabasıyla para).

### A10 — Scam 1992: how Harshad Mehta moved India's stock market
- **Özet:** 1992'de Harshad Mehta banka makbuzlarıyla borsaya fon akıttı; skandal Hindistan'da düzenlemeyi değiştirdi [kaynak K1].
- **Neden şimdi:** "Scam" dizisinin yeni sezonu (Scam 2010) yayında [arama özeti, Economic Times 11-02]; Hindistan dizi gündemi (K2).
- **Global bağ:** Hindistan çok güçlü, diğer ülkeler zayıf.
- **Kaynaklar:**
  - K1: [Harshad Mehta](https://en.wikipedia.org/wiki/Harshad_Mehta) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Mehta
  - K2: [From Scam 1992 The Harshad Mehta Story to Rocket Boys: 5 gripping OTT web series](https://www.hindustantimes.com/entertainment/web-series/from-scam-1992-the-harshad-mehta-story-to-rocket-boys-5-gripping-ott-web-series-on-sonyliv-based-on-india-most-fascinating-and-true-events-101790846832860.html) · Hindustan Times · tarih: 2026-10-02 · anahtar: Harshad
- **Outlier [ölçüm]:** DOKio "Scam 1992 Explain | 2D Animation" 907 K / 8,7 K = **104x** · AB FinDoc 19x.
- **İlgi [ölçüm]:** medyan **5,44 M**, 9 video ≥1 M (çoğu dizi/film içeriği; finans anlatımı değil).
- **Risk/Hassas:** hayır. Kitle tek ülke. **Neden izlenir:** Hindistan'ın "Wolf of Wall Street"i.

### A11 — The richest man on Earth used a diamond as a paperweight: the Nizam of Hyderabad
- **Özet:** Son Nizam Mir Osman Ali Khan 20. yüzyılın en zenginleri arasında sayıldı; Jacob elmasını kâğıt ağırlığı olarak kullandığı anlatılır [kaynak K1; anekdot F3]. Mülk davaları sürüyor [kaynak K2].
- **Kaynaklar:**
  - K1: [Mir Osman Ali Khan](https://en.wikipedia.org/wiki/Mir_Osman_Ali_Khan) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: Nizam
  - K2: [Telangana HC won't interfere in division of properties linked to Hyderabad's last Nizam](https://theprint.in/feature/telangana-hc-wont-interfere-in-division-of-properties-linked-to-hyderabads-last-nizam/3051940/) · ThePrint · tarih: 2026-09-24 · anahtar: Nizam
- **Outlier [ölçüm]:** The British Empire Files 704 K / 7,1 K = **99x** (2026-09-08).
- **İlgi [ölçüm]:** medyan 7,8 K.
- **Risk/Hassas:** düşük (1948 Hyderabad ilhakı şiddeti anlatılırsa hassas). **Neden izlenir:** Hayal edilemeyecek bir servetin nasıl eridiği.

### A12 — Japan 1989: the bubble that took 34 years to recover
- **Özet:** Nikkei 1989 zirvesini ancak 2024'te geçebildi; arsa ve hisse balonu ve "kayıp on yıllar" [kaynak K1, K2].
- **Kaynaklar:**
  - K1: [Japanese asset price bubble](https://en.wikipedia.org/wiki/Japanese_asset_price_bubble) · Wikipedia · tarih: 2026-11-04 (erişim) · anahtar: bubble
  - K2: [Why Japan's Nikkei Took 34 Years To Reclaim Its 1989 Peak](https://hdfcsky.com/sky-learn/market-wtf-by-sky/why-japans-nikkei-took-34-years-to-reclaim-its-1989-peak) · HDFC Sky · tarih: 2026-10-13 · anahtar: Nikkei
- **Outlier [ölçüm]:** ≥10x yok (How Business Worked 416 K, 1,4x).
- **İlgi [ölçüm]:** medyan 31 K. Düşük.
- **Risk/Hassas:** hayır. **Neden izlenir:** "Borsa hep çıkar" inancını yıkan gerçek örnek.

### A13 — Black Friday wasn't about shopping: the 1869 gold panic
- **Özet:** 24 Eylül 1869'da Gould ve Fisk'in altın piyasasını köşeye sıkıştırma girişimi çöktü; alışverişteki "Black Friday" adı ise 1950'lerin Philadelphia'sından geliyor [kaynak K1, K2; önceki havuz A1'de doğrulandı].
- **Neden şimdi:** Kara Cuma 27 Kasım; Paz 11-22 slotuna uygun, bu slot için erken.
- **Kaynaklar:**
  - K1: [Why Is It Called Black Friday?](https://www.history.com/articles/black-friday-thanksgiving-origins-history) · History.com · tarih: 2026-11-04 (erişim) · anahtar: Gould
  - K2: [Black Friday, September 24, 1869](https://www.pbs.org/wgbh/americanexperience/features/grant-black-friday/) · PBS American Experience · tarih: 2026-11-04 (erişim) · anahtar: Gould
  - K3: [Black Friday's Origins Are Far More Interesting Than I Initially Thought](https://www.huffingtonpost.co.uk/entry/black-friday-2026-meaning_uk_6ac5fdbbe4b05f9f91f2a934) · HuffPost UK · tarih: 2026-10-07 · anahtar: Black Friday
- **Outlier [ölçüm]:** nişte yok; 12 ayda en iyisi 68 izlenme. Taze rakip yok.
- **İlgi [ölçüm]:** "why is it called black friday" medyanı 30 K.
- **Risk/Hassas:** hayır. **Neden izlenir:** Herkesin bildiği günün adının sandığı yerden gelmediği.

---

## 4. B — Güncel (bağlam ve kanca; bu A/C slotuna önerilmez)
### B1 — Gold crashed 30% from its record. What just happened?
- **Özet:** Altın rekordan yaklaşık %27–30 düştü ve bir yılın en düşüğüne indi [kaynak K1, K2].
- **Kaynaklar:**
  - K1: [What gold's nearly 30% crash from all-time highs tells us about markets and the economy](https://www.businessinsider.com/gold-price-crash-why-metal-is-down-inlation-interest-rates-2026-11) · Business Insider · tarih: 2026-11-03 · anahtar: gold
  - K2: [Why Is Gold Going Down? Gold Falls 27% From Its Record](https://cryptoticker.io/en/is-gold-a-safe-haven-gold-price-crisis/) · CryptoTicker · tarih: 2026-10-31 · anahtar: gold
- **Outlier [ölçüm]:** TSCS "WTF Just Happened to Gold?" 848 K / 12,4 K = **68x** (2026-10-28).
- **İlgi [ölçüm]:** "why is gold crashing" medyanı 56 K. **Risk/Hassas:** hayır; fiyat oynak, bayatlar. **Neden izlenir:** "Güvenli liman" sanılan şeyin çöküşü.

### B2 — Anthropic's IPO: the questions before day one
- **Özet:** Anthropic Nasdaq'ta işlem görmeye hazırlanıyor; güvenlik ve değerleme tartışması [kaynak K1–K3].
- **Kaynaklar:**
  - K1: [Anthropic set to make stock market debut as questions swirl about safety of AI](https://www.cnn.com/2026/10/26/tech/anthropic-files-ipo) · CNN · tarih: 2026-10-26 · anahtar: Anthropic
  - K2: [Anthropic's IPO expected to reshape San Francisco's housing market](https://abc7news.com/post/anthropics-ipo-expected-reshape-san-franciscos-housing-market-most-us-cant-afford-houses/19982939/) · ABC7 · tarih: 2026-10-27 · anahtar: Anthropic
  - K3: [The SEC Should Block Anthropic's IPO to Protect the Public](https://techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public) · Tech Policy Press · tarih: 2026-11-02 · anahtar: Anthropic
- **Outlier [ölçüm]:** önceki havuzda ölçüldü (Breaking Points 223 K); bu turda ≥10x yok. **İlgi:** RSS 100 sonuç / 10 gün. **Risk/Hassas:** **çıkar çatışması** (bu havuzu Claude hazırladı); seçilirse hakem ve finans-dogrulayici tarafsızlığı ayrıca denetlemeli. **Neden izlenir:** Herkesin kullandığı bir AI şirketi borsaya açılıyor.

---

## 5. Öncelik ve ilk 5'in gerekçesi (Paz 11-08, A/C) [ölçüm + tahmin]
| Sıra | ID | Medyan (YT) | En güçlü outlier | ≥1 M / 15 | Kanca (≤30 g) | Geniş kitle | Doygunluk | Reklam riski [tahmin] |
|---|---|---|---|---|---|---|---|---|
| 1 | A1 Soygunlar + Binance | **2,05 M** | 310x (1,89 M, 5 gün) · fern 6,12 M | **10** | 10-29/30 | Çok yüksek | Orta | SARI (suç anlatımı) |
| 2 | C1 Boomer'lar giderse | 424 K | 121x · 42x (928 K) | 3 | 10-05/07 | Çok yüksek (4 ülke) | Orta | YEŞİL |
| 3 | C2 Önce kim batar | 1,6 K (yeni sorgu) | **8,64 M** (11,7x) · 154x | 1 | 10-20/21 | Yüksek | **Yüksek (kopya dalgası)** | YEŞİL |
| 4 | A2 Madoff | **1,18 M** | 38x (taze rakip yok) | **8** | 10-05/09 (zayıf) | Yüksek | Düşük (taze) / yüksek (eski) | SARI (hassas) |
| 5 | C4 AI balonu patlarsa | 591 K | 316x · 4,24 M | 4 | 10-30 | Yüksek | **Çok yüksek** | YEŞİL |
| 6 | A3 Mansa Musa efsanesi | 170 K | 66x · 863 K | 5 | 10-23 | Yüksek (Hindistan/Afrika) | Orta | YEŞİL |
| 7 | C5 Seçim sonrası para | 22 K | 4,26 M (32x) | 1 | 11-04 | Düşük (ABD) | Orta | SARI (siyasi) |
| 8 | C3 40 trilyon $ kime | 42 K | 169x · 113x | 0 | 10-16/21 | Yüksek | Orta | YEŞİL |
- **1. A1:** Havuzun en yüksek kalıcı talebi (soygun sorgusunda 15 videonun 10'u milyon üstü) taze bir şokla birleşiyor. 6 bin aboneli bir kanal 5 günde 1,89 M izlendi. Konuyu algoritma kendisi itiyor. Finansa ilgisi olmayan da tıklar. Açımız sıralama + tarih olmalı, Binance tek başına anlatılmamalı (Gloam ile örtüşür).
- **2. C1:** Kuşak sorusu dört hedef ülkenin hepsinde kişisel: izleyici ya mirasçı ya ev alıcısı. 4,9 bin aboneli kanal 595 K (121x) aldı, konu 424 K medyanla kalıcı. Leo'nun "zaman makinesi" senaryo formatına uygun [tahmin].
- **3. C2:** Nişin son 12 ayının en büyük mutlak outlier'ı (8,64 M) ve 3 gün önce 154x yapan bir kopyası var: talep sıcak. Risk: kopya dalgası başladı; ölçütü şeffaf, özgün bir "stres testi" çerçevesi şart, yoksa elenmeli.
- **4. A2:** "Talep var, taze rakip yok" kuralının en net örneği: medyan 1,18 M, son 12 ayda büyük bir anlatım yok. Hassas işareti ve "bildik hikâye" riski yüzünden 4. sırada.
- **5. C4:** En büyük ham talep (591 K medyan, 316x küçük kanal), ama Infographics aynı formatı 8 gün önce 4,24 M ile yaptı. Ancak farklı bir mekanizma açısıyla (ör. A6 dot-com karşılaştırması veya C6 banka) girilmeli.

## 6. Elenenler (neden)
- **Isaac Newton / South Sea Bubble:** tam sorgu medyanı 36, açılan bağımsız güncel kaynak 1 (Fair Observer). Kancası (AI balonu) A6/C4'te daha güçlü.
- **John Law / Mississippi balonu:** medyan 546; talep yok.
- **Lale çılgınlığı:** RSS kaynakları konu dışı çıktı (BigGo/Bitcoin, Vibes/AI); 12 ayda en iyisi Extra History 306 K; özgün açı yok.
- **Nick Leeson / Barings:** medyan 30 K; ikinci bağımsız güncel kaynak bulunmadı (önceki havuz notu çözülmedi). LADbible röportajı 525 K var, sonraki tura.
- **"What caused the Great Depression" (366x, medyan 1,28 M):** kanalın ilk videosu 1929'du; tekrar riski. Seri devamı olarak ayrıca düşünülebilir [tahmin].
- **"Most expensive thing ever" (20,6 M), Japonya doğum oranı (6,66 M), Costco ekonomisi (3,1 M):** finans bağı zayıf veya genel bilgi kanalı formatı.
- **Petrodolar (2,93 M, 13x):** C7'ye alt bölüm olarak katıldı.
- **Kaynak elemeleri:** Bulwark (C7; konu sağlık), Nikkei Asia savunma vergisi (A12; konu dışı), AOL (C9; Yahoo ile aynı Fortune metni, bağımsız değil), Kitco (C7; konu altın/banka), Smithsonian/Atlas Obscura/Britannica (403), History.com Madoff (404), BBC Nizam (404).

## Kontrol listesi (betikle)

Komut: `python3 01-arastirma/kaynak-kontrol.py 01-arastirma/konu-havuzu.md --bugun 2026-11-04` → çıkış 0 (`olcum/kapi-cikti.txt`)

| ID | Konu | Kaynak | Bağımsız alan | Açılan (200+anahtar) | Açılan bağımsız | Son 30 gün (B) | Sonuç |
|---|---|---|---|---|---|---|---|
| C1 | What happens when the boomers are gone? The $124 | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C2 | Which country goes bankrupt first? A stress test | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C3 | Who does America owe $40 trillion, and what if t | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C4 | The AI bubble pops: what happens next, month by  | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C5 | Blue sweep: what happens to your money in 2027? | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C6 | What if everyone pulled their money out at once? | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C7 | What happens if the dollar collapses? A day-by-d | 2 | 2 | 2 | 2 | — | GEÇTİ |
| C8 | If AI takes the jobs, who buys anything? | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C9 | Social Security's 2032 cliff: what a 26% cut wou | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C10 | What if China dumped all its US Treasuries overn | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A1 | The biggest heists in money history, and Binance | 4 | 4 | 4 | 4 | — | GEÇTİ |
| A2 | Bernie Madoff: the $65 billion lie everyone beli | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A3 | Mansa Musa wasn't the richest man ever. Here's w | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A4 | The most expensive mistakes in money history ($8 | 3 | 2 | 3 | 2 | — | GEÇTİ |
| A5 | The idiot who got rich: Timothy Dexter's acciden | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A6 | The dot-com crash: the AI bubble's dress rehears | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A7 | How Hitler paid for a war with money that didn't | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A8 | The brothers who tried to buy all the world's si | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A9 | Weimar hyperinflation: when a loaf of bread cost | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A10 | Scam 1992: how Harshad Mehta moved India's stock | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A11 | The richest man on Earth used a diamond as a pap | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A12 | Japan 1989: the bubble that took 34 years to rec | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A13 | Black Friday wasn't about shopping: the 1869 gol | 3 | 3 | 3 | 3 | — | GEÇTİ |
| B1 | Gold crashed 30% from its record. What just happ | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B2 | Anthropic's IPO: the questions before day one | 3 | 3 | 3 | 3 | 3 | GEÇTİ |

Sütun sayımı: A=13 · B=2 · C=10 · toplam=25
Kapı: GEÇTİ (her konuda >=2 bağımsız açılan kaynak; B'de >=1 kaynak son 30 gün; toplam >=15)

Komut: `python3 01-arastirma/olcum/alan_kontrol.py 01-arastirma/konu-havuzu.md` → Alan kapısı: GEÇTİ (25 konu) (her konuda Outlier / İlgi / Hassas / Neden izlenir satırı; tablo `olcum/alan-cikti.txt`)

C sütunu ek kontrol (elle, kaynak tarihlerinden): 10 C konusunun 10'unda ≥1 kaynak son 30 gün içinde (en eski güncel kaynak C10 2026-10-18). Outlier verisi: `olcum/outlier-ham.json` sha256 06ae9ef76af5, talep `olcum/aday-talep.json` sha256 8b1f2c0f7da0.
