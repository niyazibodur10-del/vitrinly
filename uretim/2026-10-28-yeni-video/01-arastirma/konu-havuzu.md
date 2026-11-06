# F1 — Konu havuzu (trend-avcisi) · 2026-10-28

İLERLEME: tamam (S1/S2/S3 bitti; kaynak kapısı betikle koşuldu, sonuç dosya sonunda).
**Görev:** Çar 2026-11-04 12:00 ET slotu = **B (güncel haber)**; yedek Paz 2026-11-08 (A/C). İlk video A'ydı (1929), tekrar yok.
**Havuz:** 26 konu = **B 17 · A 6 · C 3**. Her konuda ≥2 bağımsız, açılan (HTTP 200 + anahtar kelime) kaynak; B'de ≥1 kaynak son 30 günden (≥2026-09-28). Kapı: dosya sonu (betik).
**Öneri (karar değil, F2'ye girdi) [tahmin]:** 4 Kasım için **B1 (Çin'de AI balonu patladı — sıra ABD'de mi?)**. Bir haftada bayatlamıyor, küresel (Hindistan dahil) talep ölçüldü, görselleştirmesi kolay. Bu haftanın Big Tech bilançoları (B12) ve CoreWeave borcu (B16) videoya taze veri katar. Yedek B: **B3 (130 milyar $ gümrük vergisi iadesi: para kime gidiyor?)** ve **B14 (konut piyasası)**. Kasım ortası A için: **A1 (1869 Kara Cuma)** doğrulandı, Paz 2026-11-22'ye uygun.
**Etiketler:** [kaynak] linkli kaynakta okundu (başlık/özet metası dahil) · [ölçüm] bu çalışmada API ile ölçüldü (2026-10-28) · [arama özeti] WebSearch özeti, kaynak okunmadı · [tahmin] ajan yorumu.

## 0. Yöntem
| Ölçüm | Araç (`01-arastirma/olcum/`) | Durum 2026-10-28 |
|---|---|---|
| Haber akışı (son 14 gün) | Google News RSS `haber_rss.py` → `s1-haber.json`, `s1b-haber.json` (40 sorgu) | Çalışıyor. **Yeni:** linkler `googlenewsdecoder` ile yayıncı URL'sine çözülüyor |
| Kaynak bulma + açılma testi | `kaynak_bul.py` (RSS → çözüm → curl 200 + anahtar + `datePublished`) → `b-kaynak.json`, `b2-kaynak.json` | Çalışıyor. Reuters/WSJ/Bloomberg/NYT bot korumalı ya da ücretli; bilerek atlandı |
| YouTube talebi | `youtube_arama.py` (yt-dlp `ytsearch15` alaka + `ytsearchdate25` en yeni → API `videos.list`) → `youtube-arama.json` (30 sorgu) | Çalışıyor (`search.list` kullanılmadı, kota korunuyor) |
| Hacker News (30 gün, >50 puan) | Algolia API → `hn-30gun.json` | Çalışıyor |
| Wikipedia pageviews | `wiki_pageviews.py` → `wiki-pageviews.json` | Kısmi: 10 sayfadan 2si ölçüldü (Panic_of_1907, Anthropic), kalanı 429; ham kayıt `olcum/wiki.log` |
| Google Trends / Reddit | — | Ölçülmedi (Trends 429, Reddit .json 403). `pulse:pulse` aynı Reddit ucuna dayandığı için çalıştırılmadı |

**YouTube okunuşu:** "med" = alaka sırasındaki ilk 15 videonun medyan izlenmesi (kalıcı talep). "12 ay en iyi" = 2025-10-28'den sonra yüklenen en çok izlenen video (taze talep / rakip doluluğu). Küçük örneklem; gösterge, kesin ölçü değil.

### 0.1 Üç strateji: kaç kaynaklı ve zamanlı konu verdi
| Strateji | Aday | Kapıyı geçen | Zamanlı (son 30 gün) | Not |
|---|---|---|---|---|
| **S1 Haber akışı** (Google News RSS + çözücü) | 26 | 20 (B1–B17, C1–C3) | 20 | En verimli strateji. RSS çözücü sayesinde açılan, tarihli birincil sayfalar çıktı (geçen tur ikinci el kripto siteleriyle kalmıştık) |
| **S2 Kalıcı tarih olayı / yıldönümü** | 7 | 6 (A1–A6) | 4'ünün güncel bağı var (A1 Kara Cuma 27 Kas, A3 Fed artırımı, A4 rupi, A5 gümrük vergileri) | 1994 tahvil katliamı elendi (§5) |
| **S3 Topluluk (HN; Reddit kapalı)** | 20 terim | 0 yeni konu | — | Talep kanıtı verdi: "Anthropic S-1" **1.697 puan / 1.659 yorum** (2026-10-26), "10-year yield above 5.3%" 125 puan, "deficit nearly $2T" 208 puan |

### 0.2 Önceki dersler
`uretim/*/yayin-sonrasi/` yok: ilk uzun video (1929) bugün 2026-10-28 16:00 UTC'de yayına planlı, performans raporu henüz yok. Hafızadan uygulanan: link testi 200 + anahtar kelime, tarih sayfa metasından, S3'e az zaman ayrıldı, A konularına S1'den güncel bağ eklendi.

### 0.3 Bağlam: 2026 Ekim sonu gündemi [kaynak; linkler konu bloklarında]
Fed Başkanı **Kevin Warsh**; 27–28 Ekim toplantısında faizi sabit tutması, Aralık'ta artırması bekleniyor (karar bugün 18:00 UTC, bu dosyadan sonra). 10 yıllık ABD tahvili yaklaşık 20 yılın ilk kez %5 üstünde. Brent Suudi tesislerine Husi saldırılarıyla 114–116 $ arasında. Altın zirveden yaklaşık %25 aşağıda. Bitcoin 80 bin $ altında. Çin STAR 50 endeksi Temmuz'dan beri yaklaşık %40 düştü. Anthropic S-1 halka arz başvurusunu yaptı. ABD ara seçimleri 3 Kasım'da.

---

## 1. B — Güncel (4 Kasım slotu; bayatlama riski her konuda yazılı)
Satır biçimi: Özet · Neden şimdi · Global bağ · Kaynaklar · İlgi · Hassas · Neden izlenir.

### B1 — China's AI bubble already burst. Is America next?
- **Özet:** Çin'in teknoloji borsası STAR 50, Temmuz'dan bu yana yaklaşık %40 düştü; değer kaybı 480 milyar $ civarında [kaynak K2; 480 milyar $ rakamı haber başlıklarında, F3'te doğrulanmalı].
- **Neden şimdi:** Reuters 26 Ekim, FT 28 Ekim, Futurism 27 Ekim'de haberleştirdi. ABD'de Big Tech bilançoları bu hafta açıklanıyor. **Bayatlama:** düşük; "sırada ABD mi var?" sorusu haftalarca açık kalır [tahmin].
- **Global bağ:** Hindistan izleyicisi şimdiden ilgili (ölçüm aşağıda). ABD/İngiltere/Kanada/Avustralya emeklilik fonları Nvidia ve Big Tech'e bağlı [tahmin].
- **Kaynaklar:**
  - K1: [It Appears That the AI Bubble Has Just Burst in China](https://futurism.com/artificial-intelligence/ai-bubble-burst-china) · Futurism · tarih: 2026-10-27 · anahtar: China
  - K2: [China's A.I. Stocks Have Lost 40 Percent in Four Months](https://www.trendingtopics.eu/china-ai-stocks-crash-star50/) · Trending Topics · tarih: 2026-10-27 · anahtar: STAR
- **İlgi [ölçüm]:** YouTube'da Palki Sharma, "China's AI Bubble Has Burst" 1,20 M izlenme (2026-10-27, bir günde); Reuters videosu 520 K. "What if the AI bubble bursts" sorgusunun medyanı 319 K (C1).
- **Hassas:** hayır. **Neden izlenir:** Herkesin korktuğu "AI balonu patlaması" artık bir ülkede yaşandı; insanlar kendi ülkelerinde neye benzeyeceğini görmek istiyor.

### B2 — Anthropic's IPO filing: $16B revenue, $80B loss — the biggest IPO ever?
- **Özet:** Claude'un yapımcısı Anthropic S-1 başvurusunu yayımladı: 16,3 milyar $ gelir, 80,7 milyar $ net zarar, Nasdaq'ta "ANT" kodu [kaynak K1, K2 başlık/özet].
- **Neden şimdi:** S-1 26 Ekim'de yayımlandı; halka arz tarihi kaynaklarda net değil. **Bayatlama:** orta; işlem başlarsa konu "ilk gün" hikâyesine döner.
- **Global bağ:** Tarihin en büyük halka arzlarından biri olabilir (NPR); AI hisseleri tüm endeks fonlarında var [tahmin].
- **Kaynaklar:**
  - K1: [Anthropic's IPO prospectus shows $16.3 billion in revenue, an $80.7 billion net loss](https://fortune.com/2026/10/26/anthropics-s-1/) · Fortune · tarih: 2026-10-26 · anahtar: Anthropic
  - K2: [Anthropic's S-1 paperwork reveals the stunning finances behind its meteoric rise](https://www.businessinsider.com/anthropic-s-1-filing-public-finances-compute-deals-2026-10) · Business Insider · tarih: 2026-10-26 · anahtar: Anthropic
  - K3: [AI giant Anthropic files for an IPO that could break records](https://www.npr.org/2026/10/26/nx-s1-6014772/anthropic-ai-ipo-could-break-records) · NPR · tarih: 2026-10-26 · anahtar: Anthropic
- **İlgi [ölçüm]:** HN "Anthropic S-1" 1.697 puan. YouTube: Breaking Points 223 K, Prof G 212 K (2026-10-27); alaka medyanı 22 K. Wikipedia "Anthropic" günde ortalama 8.485 görüntüleme (son 30 gün, düz).
- **Hassas:** hayır. **Çıkar çatışması notu:** bu havuzu Anthropic modeli (Claude) hazırladı. Konu seçilirse hakem ve finans-dogrulayici tarafsızlığı ayrıca denetlemeli; tavsiye dili kesinlikle yok.
- **Neden izlenir:** Herkesin kullandığı bir AI şirketinin gerçek gelir ve zarar rakamları ilk kez açıklandı.

### B3 — $130 billion in tariff refunds: where is the money going?
- **Özet:** Yüksek Mahkeme 20 Şubat'ta IEEPA gümrük vergilerini iptal etti. Gümrük şimdiye kadar yaklaşık 130 milyar $ iade işledi; tüketicilerin çoğu bu paradan pay almıyor [kaynak K1].
- **Neden şimdi:** Ekim'de iadeler ve "parayı şirketler tutuyor" tartışması gündemde (Fed anketi; PIIE 26 Ekim). **Bayatlama:** düşük.
- **Global bağ:** Kanada, Hindistan ve İngiltere ihracatçıları gümrük vergisi savaşının tarafı [tahmin].
- **Kaynaklar:**
  - K1: [Importers Are Getting Nearly $130 Billion Back](https://www.moneytalksnews.com/trump-called-the-tariff-ruling-deeply-disappointing-importers-are-getting-nearly-billion-back-im-a-cpa-heres-whether-any-of-it-is-yours/) · Money Talks News · tarih: 2026-10-16 · anahtar: refund
  - K2: [Can the courts end Trump's illegal tariffs?](https://www.piie.com/blogs/realtime-economics/2026/can-courts-end-trumps-illegal-tariffs) · PIIE · tarih: 2026-10-26 · anahtar: tariff
  - K3: [Congressional Hands in the Tariff Cookie Jar](https://www.americanactionforum.org/shipment/congressional-hands-in-the-tariff-cookie-jar/) · American Action Forum · tarih: 2026-10-15 · anahtar: tariff
- **İlgi [ölçüm]:** YouTube alaka medyanı 85 K; CNN'in karar videosu 1,68 M (Şubat). İade/para akışı açısından son 30 günde güçlü bir video bulunamadı.
- **Hassas:** hayır. Siyasi konu; anlatım veriye dayanmalı [tahmin]. **Neden izlenir:** "Fazladan ödediğimiz vergi geri geliyor mu, bana ne düşecek?" sorusu herkesi ilgilendiriyor.

### B4 — The Fed is raising rates again in 2026: why, and what it means for you
- **Özet:** Warsh başkanlığındaki Fed'in 27–28 Ekim'de faizi sabit tutması, ardından Aralık'ta artırması bekleniyor; İngiltere Merkez Bankası da 5 Kasım'da artırıma hazırlanıyor [kaynak K1–K3].
- **Neden şimdi:** Karar bugün açıklanıyor; BoE kararı 5 Kasım. **Bayatlama:** kararın sonucu metne işlenmeli; "neden artırıyorlar" çerçevesi kalıcı.
- **Global bağ:** ABD ve İngiltere faizleri doğrudan, Kanada ve Avustralya mortgage'ları dolaylı etkileniyor.
- **Kaynaklar:**
  - K1: [5 things to watch for in this week's Federal Reserve meeting](https://www.pbs.org/newshour/economy/5-things-to-watch-for-in-this-weeks-federal-reserve-meeting) · PBS NewsHour · tarih: 2026-10-27 · anahtar: Warsh
  - K2: [Fed expected to hold interest rates steady as inflation tops midterm voters' concerns](https://www.nbcnews.com/business/economy/fed-interest-rates-inflation-midterms-trump-rcna605905) · NBC News · tarih: 2026-10-27 · anahtar: Fed
  - K3: [Federal Reserve preview: A pause before a December hike](https://think.ing.com/articles/federal-reserve-preview-a-pause-before-a-december-hike/) · ING Think · tarih: 2026-10-23 · anahtar: December
  - K4: [Interest rates unlikely to reach 4.75% by next summer, say City economists](https://www.theguardian.com/business/2026/oct/25/interest-rates-bank-of-england-rises-summer-2027) · The Guardian · tarih: 2026-10-25 · anahtar: Bank of England
- **İlgi [ölçüm]:** Zayıf. "fed interest rate decision" medyanı 11 K; en iyi video 75 K (CNBC).
- **Hassas:** hayır. **Neden izlenir:** Faizlerin düşmesini beklerken yeniden yükseldiği bir dünyada kredi, mortgage ve birikim hesabı nasıl değişiyor?

### B5 — The 10-year Treasury just crossed 5%: the number that moves your mortgage
- **Özet:** ABD 10 yıllık tahvil faizi yaklaşık 20 yılın ilk kez %5'in üstüne çıktı (1 Ekim'de %5,3) [kaynak K1, HN].
- **Neden şimdi:** Ekim boyunca %5 civarında dalgalanıyor (22 Ekim'de %5'in altına indi). **Bayatlama:** orta; seviye değişebilir, kavram kalıcı.
- **Global bağ:** Küresel tahvil faizleri onlarca yılın zirvesinde (J.P. Morgan, 19 Ekim; arama başlığı).
- **Kaynaklar:**
  - K1: [The 10-Year Treasury Is Above 5% for the First Time in Almost 20 Years](https://www.fool.com/investing/2026/10/18/10-year-treasury-5-20-years-history-says-sp500/) · The Motley Fool · tarih: 2026-10-18 · anahtar: Treasury
  - K2: [The 10-year Treasury yield is above 5%. Should savers lock in now?](https://finance.yahoo.com/personal-finance/investing/article/the-10-year-treasury-yield-is-above-5-should-savers-lock-in-now-193110179.html) · Yahoo Finance · tarih: 2026-10-20 · anahtar: Treasury
- **İlgi [ölçüm]:** Medyan 4,6 K (düşük); CNBC 201 K. HN 125 puan.
- **Hassas:** hayır. **Neden izlenir:** Çoğu insanın hiç bakmadığı tek bir sayı, ev kredisinden borsaya kadar her şeyi belirliyor.

### B6 — $115 oil: what attacks on Saudi refineries do to your gas price
- **Özet:** Husilerin Suudi rafineri ve boru hattına saldırıları Brent'i 114–116 $'a taşıdı; ABD–İran barış görüşmeleri fiyatı aşağı çekiyor [kaynak K1, K2].
- **Neden şimdi:** 27–28 Ekim'de Ras Tanura saldırısı. **Bayatlama:** **yüksek**; barış ya da tırmanma senaryosuna göre hızla değişir.
- **Global bağ:** Petrol ithalatçısı Hindistan, akaryakıt fiyatları (ABD ortalaması 4,26 $/galon, 27 Ekim) [arama başlığı].
- **Kaynaklar:**
  - K1: [Brent prices hit $115 amid concerns over Saudi refinery attack](https://www.dailysabah.com/business/energy/brent-prices-hit-115-amid-concerns-over-saudi-refinery-attack/amp) · Daily Sabah · tarih: 2026-10-28 · anahtar: Brent
  - K2: [Brent Hits $114 as Houthi Attacks Threaten Saudi Energy Infrastructure](https://finance.yahoo.com/energy/articles/brent-hits-114-houthi-attacks-053350014.html) · Yahoo Finance / OilPrice · tarih: 2026-10-23 · anahtar: Brent
  - K3: [Brent Crude Prices Slip Amidst Houthi Attacks](https://www.marinelink.com/news/brent-crude-prices-slip-amidst-houthi-543802) · Marine News · tarih: 2026-10-20 · anahtar: Brent
- **İlgi [ölçüm]:** Medyan 37 K; Al Jazeera 296 K.
- **Hassas: EVET** (saldırılar, ölümler: NYT 22 Ekim "kills 2" [arama başlığı]) → monetizasyon-uyum-uzmani bakmalı. **Neden izlenir:** Uzaktaki bir saldırının pompadaki fiyata nasıl yansıdığını adım adım gösterir.

### B7 — The rupee near 100 per dollar: India's $70 billion fight to defend its currency
- **Özet:** Rupi bu yıl dolara karşı yaklaşık %6 değer kaybetti ve rekor dipler gördü; RBI'ın 140 milyar $'lık döviz girişinin yarısını savunmaya harcadığı tahmin ediliyor [kaynak K1; 70 milyar $ rakamı Reuters başlığından türetildi, arama özeti].
- **Neden şimdi:** CNBC 15 Ekim'de "100'e doğru" tahminini yazdı; Economist 25 Ekim. **Bayatlama:** düşük.
- **Global bağ:** Hindistan (hedef kitle ülkesi) doğrudan; diaspora havaleleri ABD, İngiltere, Kanada ve Avustralya'dan geliyor.
- **Kaynaklar:**
  - K1: [A stronger rupee, shrinking dollar reserve: The balancing act facing RBI](https://timesofindia.indiatimes.com/business/india-business/a-stronger-rupee-shrinking-dollar-reserve-the-balancing-act-facing-rbi/articleshow/135143408.cms) · Times of India · tarih: 2026-10-23 · anahtar: rupee
  - K2: [Rupee closes at 95.15, extends winning streak as RBI curbs dollar demand](https://www.tradingview.com/news/moneycontrol:a7d6679e4094b:0-rupee-closes-at-95-15-extends-winning-streak-as-rbi-curbs-dollar-demand/) · Moneycontrol (TradingView) · tarih: 2026-10-14 · anahtar: rupee
  - K3: [RBI Eases Rupee Jitters; Reserves Under Strain](https://www.briefs.co/news/rbi-steps-cool-rupee-jitters-but-the-heat-isn-t-over/) · Briefs Finance · tarih: 2026-10-15 · anahtar: rupee
- **İlgi [ölçüm]:** "rupee falling" medyanı 78 K; "rupee 100 dollar" en iyisi 35 K (Haziran). Taze rakip yok.
- **Hassas:** hayır. **Neden izlenir:** Hindistan'daki her fiyatı etkileyen "100 rupi = 1 dolar" eşiği psikolojik bir kırılma noktası.

### B8 — Gold crashed 25%, yet everyone is still buying. Who's right?
- **Özet:** Altın İran savaşının başlangıcından bu yana yaklaşık %25 düştü; ETF varlıkları rekorda, Çin merkez bankası Eylül'de 23 ton altın aldı [kaynak K1, K2].
- **Neden şimdi:** 22–27 Ekim'de 4.000 $ civarında test. **Bayatlama:** orta.
- **Global bağ:** Hindistan'da düğün/Diwali altın talebi; Çin'in alımları.
- **Kaynaklar:**
  - K1: [Gold Price Crashed 25%, But Investors are Still Buying](https://finance.yahoo.com/markets/commodities/articles/gold-price-crashed-25-investors-004642833.html) · Yahoo Finance · tarih: 2026-10-27 · anahtar: gold
  - K2: [China buys the gold dip as ETF holdings hit record](https://www.kitco.com/news/article/2026-10-15/china-buys-gold-dip-etf-holdings-hit-record-and-holiday-demand-lifts-q4) · Kitco · tarih: 2026-10-15 · anahtar: gold
- **İlgi [ölçüm]:** Medyan 31 K; Hintçe video 321 K (2026-10-22).
- **Hassas:** hayır. **Neden izlenir:** "Güvenli liman" sandığımız varlığın çeyreğini kaybetmesi, herkesin sorduğu "şimdi alınır mı?" sorusunu doğuruyor (tavsiye vermeden).

### B9 — US bank stocks: the longest losing streak since 2008
- **Özet:** Büyük ABD bankalarının hisseleri 2008'den beri en uzun haftalık düşüş serisini yaşadı; KBW Bank endeksi Ağustos zirvesinden yaklaşık %13 aşağıda [kaynak K2].
- **Neden şimdi:** 15–19 Ekim. **Bayatlama:** orta.
- **Global bağ:** "2008 tekrar mı?" korkusu evrensel [tahmin].
- **Kaynaklar:**
  - K1: [US bank stocks' longest losing streak since 2008 clashes with earnings picture](https://finance.yahoo.com/markets/article/us-bank-stocks-longest-losing-streak-since-2008-clashes-with-earnings-picture-165407807.html) · Yahoo Finance · tarih: 2026-10-19 · anahtar: bank
  - K2: [Big US bank stocks head for longest weekly losing streak since 2008](https://m.economictimes.com/markets/us-stocks/wall-street-guide/big-us-bank-stocks-head-for-longest-weekly-losing-streak-since-2008/articleshow/135002546.cms) · Economic Times · tarih: 2026-10-17 · anahtar: bank
- **İlgi [ölçüm]:** "bank stocks crash" medyanı 117 K, 2 video ≥1 M (genel çöküş içeriği).
- **Hassas:** hayır. Panik dili kullanılmamalı [tahmin]. **Neden izlenir:** "2008'den beri ilk kez" ifadesi tek başına güçlü bir kanca.

### B10 — Bitcoin below $80,000 and Moody's calls a crypto crash the top risk
- **Özet:** Bitcoin bir ayı aşkın sürenin en düşüğüne, 80 bin $ altına indi; Moody's kripto çöküşünü en olası yakın vadeli şoklar arasında saydı [kaynak K1, K2; Moody's bilgisi arama başlığı].
- **Neden şimdi:** 24–26 Ekim. 31 Ekim'de Bitcoin whitepaper'ının 18. yıldönümü. **Bayatlama:** yüksek (fiyat).
- **Global bağ:** Hindistan ve ABD'de geniş perakende kripto kitlesi [tahmin].
- **Kaynaklar:**
  - K1: [Bitcoin price news: BTC falls below $80,000 on renewed Middle East worries](https://www.coindesk.com/markets/2026/10/24/crypto-under-weekend-pressure-bitcoin-slides-below-usd80-000-on-u-s-middle-east-evacuations) · CoinDesk · tarih: 2026-10-24 · anahtar: bitcoin
  - K2: [Bitcoin Falls Below $80,000 as Investors Take Cover Ahead of the Fed](https://www.trendingtopics.eu/bitcoin-below-80000-dollars-fed/) · Trending Topics · tarih: 2026-10-26 · anahtar: bitcoin
- **İlgi [ölçüm]:** Medyan 19 K; More Perfect Union 804 K (Eylül).
- **Hassas:** hayır. Kripto tanıtımı yok; reklam SARI-düşük [tahmin]. **Neden izlenir:** Kripto sahiplerinin "dip mi, çöküş mü?" sorusu.

### B11 — Midterms and your money: what stocks did after every midterm election
- **Özet:** 3 Kasım ara seçimleri öncesinde yatırımcılar tedirgin; S&P 500 son 23 ara seçim döneminin 21'inde kısa vadede yükseldi, ancak bu yıl farklı olabilir [kaynak K1, K2].
- **Neden şimdi:** Seçim 3 Kasım, slot 4 Kasım. **Bayatlama riski: sonuç yayından bir gün önce belli olur.** Metin sonuçtan bağımsız ("tarih ne diyor") yazılmalı ya da sonuç F7'de eklenmeli [tahmin].
- **Global bağ:** Zayıf (ABD odaklı); dolar ve küresel piyasa üzerinden dolaylı.
- **Kaynaklar:**
  - K1: [Investors Are Nervous About the Midterm Elections. Stock Market History Shows You Shouldn't Be](https://money.com/midterm-elections-stock-market-2026/) · MONEY · tarih: 2026-10-26 · anahtar: midterm
  - K2: [Midterm Elections Are Usually Good For The Markets. That May Change This Year.](https://www.investors.com/news/midterm-elections-stock-market-performance-2026/) · Investor's Business Daily · tarih: 2026-10-22 · anahtar: midterm
  - K3: [Gas under Trump 2.0 is now more expensive than it was under Biden](https://www.cnn.com/2026/10/26/economy/gas-oil-trump-iran-election) · CNN · tarih: 2026-10-26 · anahtar: gas
- **İlgi [ölçüm]:** ClearValue Tax "Stocks Have Done THIS After Every Midterm" 981 K (2026-10-19); medyan 7 K.
- **Hassas:** hayır, ancak **siyasi**: taraf tutmayan anlatım şart → monetizasyon-uyum-uzmani bakmalı. **Neden izlenir:** Seçim haftasında herkes "paramı ne bekliyor?" diye soruyor.

### B12 — Big Tech's $700 billion AI bet faces its earnings test
- **Özet:** Microsoft, Alphabet ve Amazon (S&P 500'ün yaklaşık %15'i) bu hafta iki gün içinde bilanço açıklıyor; 2026 toplam yatırım (capex) planı 700 milyar $'ın üstünde [kaynak K1; rakam aralığı kaynaklar arası 725–750 milyar $, arama özeti].
- **Neden şimdi:** 28–30 Ekim bilançoları. **Bayatlama:** 4 Kasım'a kadar sonuçlar belli olur; tek başına değil B1'in veri ayağı olarak güçlü [tahmin].
- **Global bağ:** Endeks fonları üzerinden tüm ülkeler.
- **Kaynaklar:**
  - K1: [Microsoft, Alphabet, Amazon Earnings Meet Fed Rate Decision: 3 Charts To Watch This Week](https://finance.yahoo.com/markets/stocks/articles/microsoft-alphanet-amazon-earnings-meet-113701296.html) · Yahoo Finance · tarih: 2026-10-26 · anahtar: earnings
  - K2: [Big Tech Earnings: $1.7T Backlog, $600B Spend](https://tech-insider.org/big-tech-earnings-ai-boom-test-1-7-trillion-backlog-600-billion-spend-2026/) · Tech Insider · tarih: 2026-10-27 · anahtar: earnings
- **İlgi [ölçüm]:** Zayıf (medyan 711; WSJ 273 K, Haziran). Konu tek başına değil, birleşik çerçevede çalışıyor.
- **Hassas:** hayır. **Neden izlenir:** Bir yılda 700 milyar $'lık harcamanın kâra dönüp dönmediğini gösteren sayılar bu hafta açıklanıyor.

### B13 — Private credit: the $2 trillion corner of finance regulators are watching
- **Özet:** Yarı likit özel kredi fonları kırılgan bölgede; ABD'de emeklilik planlarına özel kredi açılması tartışılıyor; İngiltere Merkez Bankası Barclays'in özel kredi riskini inceliyor [kaynak K1, K2; BoE bilgisi FT başlığı]. 2 trilyon $ büyüklüğü [arama özeti, F3'te doğrulanmalı].
- **Neden şimdi:** 15–26 Ekim (Apollo'nun günlük değerleme hamlesi, Wharton). **Bayatlama:** düşük.
- **Global bağ:** ABD (401k), İngiltere (BoE), Avustralya süper fonları [tahmin].
- **Kaynaklar:**
  - K1: [Debunking 8 Myths About Private Credit and Semiliquid Funds](https://www.morningstar.com/funds/debunking-8-myths-about-private-credit-semiliquid-funds) · Morningstar · tarih: 2026-10-16 · anahtar: private credit
  - K2: [What Is Private Credit and Why Should Americans Care?](https://www.americanprogress.org/article/what-is-private-credit-and-why-should-americans-care/) · Center for American Progress · tarih: 2026-10-19 · anahtar: private credit
- **İlgi [ölçüm]:** "private credit crisis" medyanı **107 K**; Mark Tilbury "It Started: The AI Bank Run" 575 K (2026-10-21).
- **Hassas:** hayır. **Neden izlenir:** Adını çok az kişinin bildiği bir piyasanın bir sonraki kriz olup olmayacağı soruluyor; emeklilik paranız da buraya gidebilir.

### B14 — The housing market's deep freeze: 7% mortgages and the first price cuts
- **Özet:** Ekim'de mortgage faizleri %7'nin üstünde, sözleşmeye geçen alıcılar azaldı, bazı bölgelerde fiyatlar düşmeye başladı [kaynak K1, K2].
- **Neden şimdi:** NAR 20 Ekim, NYT 22 Ekim. **Bayatlama:** düşük.
- **Global bağ:** Kanada, Avustralya ve İngiltere'de de konut erişilebilirliği krizi (Rightmove/Reuters 18 Ekim, arama başlığı).
- **Kaynaklar:**
  - K1: [Fewer Buyers Go Under Contract as Mortgage Rates Remain High](https://www.nar.realtor/news/real-estate-news/economy/fewer-buyers-go-under-contract-as-mortgage-rates-remain-high) · NAR · tarih: 2026-10-20 · anahtar: mortgage
  - K2: [Long Island home prices, sales, supply fall as mortgage rates rise](https://libn.com/2026/10/16/long-island-home-prices-sales-fall-mortgage-rates-rise/) · Long Island Business News · tarih: 2026-10-16 · anahtar: mortgage
  - K3: [Why home prices aren't falling despite a growing surplus of sellers](https://foxbaltimore.com/news/nation-world/why-home-prices-arent-falling-despite-a-growing-surplus-of-sellers) · WBFF (Sinclair) · tarih: 2026-10-16 · anahtar: mortgage
- **İlgi [ölçüm]:** **Havuzun en güçlü talebi:** medyan 153 K, 15 videonun 4'ü ≥1 M; MHFIN 2,98 M (2026-10-10), Graham Stephan 1,99 M. Doygunluk yüksek.
- **Hassas:** hayır. **Neden izlenir:** Ev sahibi olmak isteyen her gencin sorusu: "Fiyatlar nihayet düşecek mi?"

### B15 — America's $2 trillion deficit: who pays when the bill comes due?
- **Özet:** ABD 2026 mali yılını yaklaşık 2 trilyon $ (1,992 trilyon) açıkla kapattı; bu 2021'den beri en büyük açık [kaynak K1, K2].
- **Neden şimdi:** 15–16 Ekim verisi; tahvil faizleri %5. **Bayatlama:** düşük.
- **Global bağ:** Dolar ve Hazine tahvilleri tüm dünyanın rezervi.
- **Kaynaklar:**
  - K1: [Red ink: Federal deficit hits nearly $2 trillion](https://www.npr.org/2026/10/16/nx-s1-6005243/red-ink-federal-deficit-hits-nearly-2-trillion) · NPR · tarih: 2026-10-16 · anahtar: deficit
  - K2: [The US federal budget deficit for 2026 just came in. It's $1.992 trillion.](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) · Yahoo Finance · tarih: 2026-10-16 · anahtar: deficit
  - K3: [The Federal Government Collected $5.4 Trillion. It Still Can't Pay Its Bills.](https://reason.com/2026/10/15/the-federal-government-collected-5-4-trillion-it-still-cant-pay-its-bills/) · Reason · tarih: 2026-10-15 · anahtar: trillion
- **İlgi [ölçüm]:** HN 208 puan. YouTube: How Money Works "National Debt Default…" 3,09 M (Eylül); C2 sorgusunda medyan 323 K.
- **Hassas:** hayır. **Neden izlenir:** Kişi başına düşen borç hesabı, soyut bir trilyonu somut bir sayıya çeviriyor.

### B16 — CoreWeave's 15% bonds: the AI debt nobody talks about
- **Özet:** AI veri merkezi şirketi CoreWeave'in Haziran'da %9 civarı getiriyle satılan tahvilleri Ekim'de %15 getiriye düştü; AI borcuna dair kaygı Wall Street'e yayılıyor [kaynak K1, K3].
- **Neden şimdi:** 15–26 Ekim. **Bayatlama:** orta; B1 ile birleşebilir.
- **Global bağ:** Kredi fonları ve emeklilik portföyleri [tahmin].
- **Kaynaklar:**
  - K1: [CoreWeave Bond Yields Reach 15% as Investors Reassess AI Infrastructure Financing Risks](https://finance.yahoo.com/technology/ai/articles/coreweave-bond-yields-reach-15-101338344.html) · Yahoo Finance · tarih: 2026-10-19 · anahtar: CoreWeave
  - K2: [CoreWeave and Data Center Bonds Slide on Capex and Debt Overhang Concerns](https://www.morningstar.com/bonds/coreweave-data-center-bonds-slide-capex-debt-overhang-concerns) · Morningstar · tarih: 2026-10-16 · anahtar: CoreWeave
  - K3: [AI Debt Fears Are Suddenly Rippling Across Wall Street As Yields Surge](https://www.businessinsider.com/ai-debt-hyperscalers-wall-street-bond-yields-rates-coreweave-2026-10) · Business Insider · tarih: 2026-10-16 · anahtar: CoreWeave
- **İlgi [ölçüm]:** Prof G "CoreWeave Is Imploding" 523 K (2026-10-15); medyan 27 K.
- **Hassas:** hayır. Tek şirket hakkında "batacak" denmez (karalama riski) [tahmin]. **Neden izlenir:** AI patlamasının borçla finanse edilen gizli tarafını gösteriyor.

### B17 — The first $1 trillion holiday season, and why it's not good news
- **Özet:** NRF, 2026 tatil sezonu satışlarının %4,2 artışla ilk kez 1 trilyon $'ı aşacağını öngörüyor; artışın önemli kısmı enflasyondan geliyor [kaynak K1, K3].
- **Neden şimdi:** Tahminler 15–26 Ekim'de açıklandı; Kara Cuma 27 Kasım. **Bayatlama:** düşük (sezon boyunca geçerli). A1 ile seri olabilir [tahmin].
- **Global bağ:** Kara Cuma İngiltere, Kanada, Avustralya ve Hindistan'da da büyük bir alışveriş günü [tahmin].
- **Kaynaklar:**
  - K1: [NRF forecasts 4.2% holiday sales growth, muted seasonal hiring](https://www.retaildive.com/news/nrf-forecasts-2026-holiday-sales-growth-seasonal-hiring/833239/) · Retail Dive · tarih: 2026-10-19 · anahtar: holiday
  - K2: [2026 Holiday Sales Forecast to Rise 4.2% to More Than $1 Trillion](https://www.cpapracticeadvisor.com/2026/10/26/2026-holiday-sales-forecast-to-rise-4-2-to-more-than-1-trillion/192428/) · CPA Practice Advisor · tarih: 2026-10-26 · anahtar: holiday
  - K3: [Inflation expected to push holiday sales above $1 trillion](https://talkbusiness.net/2026/10/inflation-expected-to-push-holiday-sales-above-1-trillion/) · Talk Business & Politics · tarih: 2026-10-16 · anahtar: holiday
- **İlgi:** YouTube ölçülmedi (sezon öncesi). Haber hacmi: Google News "Black Friday holiday shopping forecast" 14 günde 40 haber [ölçüm].
- **Hassas:** hayır. **Neden izlenir:** Rekor bir sayının aslında daha az şey alındığı anlamına gelebileceğini gösteren bir paradoks.

---

## 2. A — Geçmiş (yedek Paz 11-08 / Kasım ortası)

### A1 — Black Friday wasn't about shopping: the 1869 gold panic
- **Özet:** 24 Eylül 1869'da Jay Gould ve Jim Fisk ABD altın piyasasını köşeye sıkıştırmaya çalıştı. Komplo o cuma çöktü ve borsa da sarsıldı [kaynak K1, K2]. Grant'in eniştesi Abel Corbin de "Gold Ring"in parçasıydı [kaynak K3].
- **DOĞRULAMA (stok fikri):** **Doğrulandı**, bir uyarıyla. Alışverişteki "Black Friday" adı 1869'dan türemedi: History.com'a göre adı 1950'lerde Philadelphia polisi Şükran Günü sonrası kalabalık için kullandı [kaynak K1]. Wikipedia 1869'u terimin "kayda geçmiş ilk önemli kullanımı" diye anıyor [kaynak K4]. Bu yüzden başlık "The first Black Friday was a crash" çerçevesiyle doğru, "alışveriş adı 1869'dan geldi" demek yanlış olur. Ayrıca Londra'daki 1866 Overend Gurney paniği de "Black Friday" diye anılıyor [arama bilgisi; Wikipedia 429 verdi, doğrulanmadı] → finans-dogrulayici.
- **Neden şimdi:** Kara Cuma 27 Kasım 2026. Önerilen slot Paz 2026-11-22 [tahmin].
- **Global bağ:** Kara Cuma hedef ülkelerin hepsinde biliniyor.
- **Kaynaklar:**
  - K1: [Why Is It Called Black Friday?](https://www.history.com/articles/black-friday-thanksgiving-origins-history) · History.com · tarih: 2026-10-28 (erişim) · anahtar: Gould
  - K2: [Black Friday, September 24, 1869](https://www.pbs.org/wgbh/americanexperience/features/grant-black-friday/) · PBS American Experience · tarih: 2026-10-28 (erişim) · anahtar: Gould
  - K3: [Black Friday (1869)](https://en.wikipedia.org/wiki/Black_Friday_%281869%29) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: Fisk
  - K4: [Black Friday (shopping)](https://en.wikipedia.org/wiki/Black_Friday_%28shopping%29) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: 1869
- **İlgi [ölçüm]:** "why is it called black friday" medyanı **29 K**, ama son 12 ayın en iyisi yalnız 28 izlenme; "history of black friday" medyanı 11 K. **Talep var, taze rakip yok.** 1869'a özgü sorgu çok niş (medyan 35). Talep Kasım sonunda zirve yapar [tahmin].
- **Hassas:** hayır. **Neden izlenir:** Herkesin bildiğini sandığı bir günün gizli bir finans skandalından adını aldığı yanılgısını düzeltip asıl hikâyeyi anlatıyor.

### A2 — The Panic of 1907: the night J.P. Morgan locked bankers in his library
- **Özet:** Knickerbocker Trust'ın çöküşüyle başlayan banka paniğini J.P. Morgan özel bir kurtarma ile durdurdu; bu kriz Fed'in kurulmasına yol açtı [kaynak K1].
- **Neden şimdi:** Ekim–Kasım 1907 yıldönümü; banka hisselerinde 2008'den beri en uzun düşüş serisi (B9) [tahmin bağ].
- **Kaynaklar:**
  - K1: [The Panic of 1907](https://www.federalreservehistory.org/essays/panic-of-1907) · Federal Reserve History · tarih: 2026-10-28 (erişim) · anahtar: Morgan
  - K2: [Panic of 1907](https://en.wikipedia.org/wiki/Panic_of_1907) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: Morgan
- **İlgi [ölçüm]:** Medyan 163; Investigate Money 59 K (2025-12). Wikipedia günde 250 (zirve 2026-10-22). Talep düşük.
- **Hassas:** hayır. **Neden izlenir:** Bir kişinin bir gecede ABD finans sistemini kurtardığı gerçek bir gerilim hikâyesi.

### A3 — The Volcker Shock: when the Fed pushed rates to 20% to kill inflation
- **Özet:** Volcker Ağustos 1979'da Fed başkanı olduğunda enflasyon yüzde 11'in üstündeydi; agresif faiz artışı 1981–82 resesyonunu getirdi ama enflasyonu kırdı [kaynak K1, K2]. %20 tepe faiz [arama bilgisi, F3'te doğrulanmalı].
- **Neden şimdi:** 2026'da Fed yeniden faiz artırıyor (B4).
- **Kaynaklar:**
  - K1: [The Great Inflation](https://www.federalreservehistory.org/essays/great-inflation) · Federal Reserve History · tarih: 2026-10-28 (erişim) · anahtar: Volcker
  - K2: [Paul Volcker interview](https://www.pbs.org/wgbh/commandingheights/shared/minitext/int_paulvolcker.html) · PBS Commanding Heights · tarih: 2026-10-28 (erişim) · anahtar: Volcker
- **İlgi [ölçüm]:** Medyan 901; en iyisi 2,2 K. Talep düşük, rakip de yok.
- **Hassas:** hayır. **Neden izlenir:** Bugünkü "faizler neden yine artıyor?" sorusunun tarihteki en sert cevabı.

### A4 — The night India pledged its gold: the 1991 crisis
- **Özet:** 1991'de Hindistan'ın döviz rezervi birkaç haftalık ithalata yetecek düzeye indi; ülke temerrütten IMF kredisi ve altın rezervini teminat göstererek kurtuldu, ardından liberalleşme reformları geldi [kaynak K1, K2]. Yaklaşık 47 tonun Londra'ya uçurulması [arama özeti; tonaj/tarih kaynaklar arası çelişkili → F3].
- **Neden şimdi:** Rupi 100'e yaklaşıyor (B7).
- **Global bağ:** Hindistan izleyicisi için güçlü kimlik konusu [tahmin].
- **Kaynaklar:**
  - K1: [1991 Indian economic crisis](https://en.wikipedia.org/wiki/1991_Indian_economic_crisis) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: gold
  - K2: [Has India ever faced bankruptcy? How gold & reforms saved the economy during 1991 crisis](https://businesstoday.in/india/story/has-india-ever-faced-bankruptcy-how-gold-reforms-saved-the-economy-during-1991-crisis-549436-2026-08-16) · Business Today · tarih: 2026-08-16 · anahtar: 1991
- **İlgi [ölçüm]:** Medyan 4,3 K; 2 video ≥1 M (genel Hindistan ekonomisi). Son 12 ayın en iyisi 6,8 K (2026-10-13).
- **Hassas:** hayır. **Neden izlenir:** Bir ülkenin altınını gizlice uçakla yurtdışına göndermek zorunda kaldığı dramatik bir an.

### A5 — Smoot-Hawley 1930: the tariff that made the Depression worse
- **Özet:** 1930 tarihli Smoot-Hawley Yasası ABD gümrük vergilerini yükseltti, misilleme dalgası dünya ticaretini daralttı [kaynak K1, K2].
- **Neden şimdi:** 2026 gümrük vergisi iptali ve iadeleri (B3). 1929 videomuzun devamı olabilir (seri) [tahmin].
- **Kaynaklar:**
  - K1: [Protectionism in the Interwar Period](https://history.state.gov/milestones/1921-1936/protectionism) · U.S. Dept. of State, Office of the Historian · tarih: 2026-10-28 (erişim) · anahtar: Smoot
  - K2: [Smoot–Hawley Tariff Act](https://en.wikipedia.org/wiki/Smoot%E2%80%93Hawley_Tariff_Act) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: 1930
- **İlgi [ölçüm]:** Medyan 10 K; son 12 ayda yalnız 3 video, en iyisi 8,9 K. Rakip boşluğu var.
- **Hassas:** hayır. **Neden izlenir:** Bugünkü gümrük vergisi kavgasının 96 yıl önceki provası.

### A6 — The 1997 Asian Financial Crisis: how Thailand's currency broke a continent
- **Özet:** Temmuz 1997'de Tayland bahtının çöküşüyle başlayan kriz Doğu Asya'ya, 1998'de Latin Amerika ve Doğu Avrupa'ya yayıldı [kaynak K1, K2].
- **Neden şimdi:** Rupi ve yen müdahale tartışmaları (B7) [tahmin bağ].
- **Kaynaklar:**
  - K1: [Asian Financial Crisis](https://www.federalreservehistory.org/essays/asian-financial-crisis) · Federal Reserve History · tarih: 2026-10-28 (erişim) · anahtar: Thailand
  - K2: [1997 Asian financial crisis](https://en.wikipedia.org/wiki/1997_Asian_financial_crisis) · Wikipedia · tarih: 2026-10-28 (erişim) · anahtar: baht
- **İlgi [ölçüm]:** Medyan 51 K, 2 video ≥1 M; Bloomberg Originals 1,58 M (2026-02).
- **Hassas:** düşük (dönemin ayaklanmaları anlatılırsa) [tahmin]. **Neden izlenir:** Bir para biriminin savunulamadığında neler olduğunu gösteriyor; rupi tartışmasıyla doğrudan bağlantılı.

---

## 3. C — Gelecek senaryoları ("senaryo" diye sunulur, tavsiye değil)

### C1 — What if America's AI bubble pops like China's? A month-by-month scenario
- **Özet:** Çin'deki %40'lık düşüş ve CoreWeave borç baskısı bir model olarak kullanılıyor: ABD'de benzer bir düzeltme fonları, işleri ve faizleri nasıl etkiler? [kaynak K1–K3 + tahmin].
- **Neden şimdi:** B1 ve B16 haberleri; NPR Planet Money 20 Ekim "AI balonu patlarsa iş kayıpları hızlanır mı?" [arama başlığı].
- **Kaynaklar:**
  - K1: [It Appears That the AI Bubble Has Just Burst in China](https://futurism.com/artificial-intelligence/ai-bubble-burst-china) · Futurism · tarih: 2026-10-27 · anahtar: bubble
  - K2: [AI Debt Fears Are Suddenly Rippling Across Wall Street As Yields Surge](https://www.businessinsider.com/ai-debt-hyperscalers-wall-street-bond-yields-rates-coreweave-2026-10) · Business Insider · tarih: 2026-10-16 · anahtar: AI
  - K3: [CoreWeave and Data Center Bonds Slide on Capex and Debt Overhang Concerns](https://www.morningstar.com/bonds/coreweave-data-center-bonds-slide-capex-debt-overhang-concerns) · Morningstar · tarih: 2026-10-16 · anahtar: CoreWeave
- **İlgi [ölçüm]:** Medyan **319 K**; Infographics Show "What if the AI Bubble Bursts (Day by Day)" 4,82 M (2026-09-03), New Money 4,38 M. Talep çok yüksek ama format doygun: kopya riski var, viralite cezası olabilir [tahmin].
- **Hassas:** hayır. **Neden izlenir:** En çok korkulan senaryo, artık gerçek bir örneğiyle anlatılabiliyor.

### C2 — What if one rupee became worth one cent? India at 100 per dollar
- **Özet:** Rupi 100 eşiğini geçerse ithalat, akaryakıt, ihracatçılar ve havaleler nasıl etkilenir? [kaynak K1–K2 + tahmin].
- **Kaynaklar:**
  - K1: [A stronger rupee, shrinking dollar reserve: The balancing act facing RBI](https://timesofindia.indiatimes.com/business/india-business/a-stronger-rupee-shrinking-dollar-reserve-the-balancing-act-facing-rbi/articleshow/135143408.cms) · Times of India · tarih: 2026-10-23 · anahtar: rupee
  - K2: [Rupee closes at 95.15, extends winning streak as RBI curbs dollar demand](https://www.tradingview.com/news/moneycontrol:a7d6679e4094b:0-rupee-closes-at-95-15-extends-winning-streak-as-rbi-curbs-dollar-demand/) · Moneycontrol (TradingView) · tarih: 2026-10-14 · anahtar: rupee
- **İlgi [ölçüm]:** "What happens if dollar hits ₹100?" 35 K (Haziran); medyan 16 K, 1 video ≥1 M.
- **Hassas:** hayır. **Neden izlenir:** Hindistan'daki her fiyata dokunan bir eşiğin senaryosu.

### C3 — What if the US couldn't pay its bills? A debt-spiral scenario
- **Özet:** 2 trilyon $ açık ve %5 tahvil faizi bir arada: faiz giderleri büyürse ne olur? [kaynak K1, K2 + tahmin].
- **Kaynaklar:**
  - K1: [Red ink: Federal deficit hits nearly $2 trillion](https://www.npr.org/2026/10/16/nx-s1-6005243/red-ink-federal-deficit-hits-nearly-2-trillion) · NPR · tarih: 2026-10-16 · anahtar: deficit
  - K2: [The 10-Year Treasury Is Above 5% for the First Time in Almost 20 Years](https://www.fool.com/investing/2026/10/18/10-year-treasury-5-20-years-history-says-sp500/) · The Motley Fool · tarih: 2026-10-18 · anahtar: Treasury
- **İlgi [ölçüm]:** Medyan **323 K**, 15 videonun 5'i ≥1 M; How Money Works 3,09 M (2026-09-07).
- **Hassas:** hayır. **Neden izlenir:** Dünyanın en güvenli borçlusu sayılan ülkenin ödeyemezse ne olacağı.

---

## 4. Öncelik özeti (4 Kasım B slotu) [ölçüm + tahmin]
| Sıra | ID | Talep (YT) | Zamanlılık | Bayatlama | Global | Reklam riski [tahmin] |
|---|---|---|---|---|---|---|
| 1 | B1 (+B12/B16 verisi) | 1,2 M / 1 gün, C1 medyanı 319 K | Çok yüksek | Düşük | Yüksek (Hindistan dahil) | YEŞİL |
| 2 | B3 | Medyan 85 K, taze rakip yok | Yüksek | Düşük | Orta | YEŞİL (siyasi dil) |
| 3 | B14 | Medyan 153 K, 4×≥1 M | Yüksek | Düşük | Orta | YEŞİL (doygunluk yüksek) |
| 4 | B13 | Medyan 107 K | Yüksek | Düşük | Orta | YEŞİL |
| 5 | B2 | HN 1.697; YT 223 K | Çok yüksek | Orta | Yüksek | YEŞİL (çıkar çatışması notu) |
| 6 | B15/C3 | C3 medyanı 323 K | Orta | Düşük | Yüksek | YEŞİL |
Seçilmemesi önerilenler (4 Kasım için): B6 (hassas + bayatlama), B11 (sonuç yayından bir gün önce belli olur), B10 ve B5 (fiyat/seviye oynak), B4 (talep zayıf).

## 5. Elenenler (neden)
- **1994 tahvil katliamı (S2):** Wikipedia dışında açılan bağımsız kaynak yok (Fortune 1994 arşivi 404, arama Orange County cinayet haberleri döndürdü). Talep de düşük (medyan 98).
- **Sosyal Güvenlik COLA %3,6:** kitlesi dar (ABD emeklileri); "neden izlenir" cümlesi global kitle için zayıf kaldı.
- **Yen müdahalesi:** açılan kaynaklar ikinci el (investingLive, Moomoo, BigGo), global bağı zayıf.
- **Benzin Trump'ta Biden'dan pahalı:** siyasi; B11'e kaynak olarak katıldı.
- **BoE Kasım artırımı:** B4'e birleştirildi (K4).
- **SPR 1982'den beri en düşük:** tek kaynak (HN, 2026-09-29), 30 günü aşıyor.
- **Pentagon "90 gün şebekesiz" / İngiltere stok çağrısı:** finans değil.
- **Kaynak elemeleri:** Global Times (B1; anahtar kelime makalede değil menüde geçiyordu), ABC tarife sayfası (Şubat 2026 tarihli, güncel değil), Stocktwits capex (Nisan 2026 tarihli), ABC Fed sayfası (Haziran 2026).

## Kontrol listesi (betikle)
Komut: `python3 01-arastirma/kaynak-kontrol.py 01-arastirma/konu-havuzu.md --bugun 2026-10-28` (canlı: curl + anahtar kelime). Çıktı aşağıya eklendi.

```
Kontrol tarihi: 2026-10-28 · konu: 26 · mod: canlı (curl + anahtar kelime)

| ID | Konu | Kaynak | Bağımsız alan | Açılan (200+anahtar) | Açılan bağımsız | Son 30 gün (B) | Sonuç |
|---|---|---|---|---|---|---|---|
| B1 | China's AI bubble already burst. Is America next | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B2 | Anthropic's IPO filing: $16B revenue, $80B loss  | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B3 | $130 billion in tariff refunds: where is the mon | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B4 | The Fed is raising rates again in 2026: why, and | 4 | 4 | 4 | 4 | 4 | GEÇTİ |
| B5 | The 10-year Treasury just crossed 5%: the number | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B6 | $115 oil: what attacks on Saudi refineries do to | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B7 | The rupee near 100 per dollar: India's $70 billi | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B8 | Gold crashed 25%, yet everyone is still buying.  | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B9 | US bank stocks: the longest losing streak since  | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B10 | Bitcoin below $80,000 and Moody's calls a crypto | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B11 | Midterms and your money: what stocks did after e | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B12 | Big Tech's $700 billion AI bet faces its earning | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B13 | Private credit: the $2 trillion corner of financ | 2 | 2 | 2 | 2 | 2 | GEÇTİ |
| B14 | The housing market's deep freeze: 7% mortgages a | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B15 | America's $2 trillion deficit: who pays when the | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B16 | CoreWeave's 15% bonds: the AI debt nobody talks  | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B17 | The first $1 trillion holiday season, and why it | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| A1 | Black Friday wasn't about shopping: the 1869 gol | 4 | 3 | 4 | 3 | — | GEÇTİ |
| A2 | The Panic of 1907: the night J.P. Morgan locked  | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A3 | The Volcker Shock: when the Fed pushed rates to  | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A4 | The night India pledged its gold: the 1991 crisi | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A5 | Smoot-Hawley 1930: the tariff that made the Depr | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A6 | The 1997 Asian Financial Crisis: how Thailand's  | 2 | 2 | 2 | 2 | — | GEÇTİ |
| C1 | What if America's AI bubble pops like China's? A | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C2 | What if one rupee became worth one cent? India a | 2 | 2 | 2 | 2 | — | GEÇTİ |
| C3 | What if the US couldn't pay its bills? A debt-sp | 2 | 2 | 2 | 2 | — | GEÇTİ |

Sütun sayımı: A=6 · B=17 · C=3 · toplam=26
Kapı: GEÇTİ (her konuda >=2 bağımsız açılan kaynak; B'de >=1 kaynak son 30 gün; toplam >=15)
```
Girdi sha256 (ilk 12, son hâl): 1a76e1e5d619 (Kontrol listesi bölümüne kadar; kontrol sonrası yalnız §0 Wikipedia satırı düzeltildi, kaynak satırları değişmedi). Ham veriler: olcum/ (b-kaynak.json, b2-kaynak.json, youtube-arama.json, hn-30gun.json, s1*-haber.json, wiki.log).
