# F1 — Konu havuzu (trend-avcisi) · 2026-10-27

**Görev:** stok videosu, **sütun A** (tarihin büyük finans çöküşleri). Hedef ilk Pazar slotu 2026-11-01 12:00 ET veya stok. Kanalın **ilk herkese açık videosu** olabilir.
**Havuz:** 23 konu = **A 17** · B 3 · C 3. Her konuda ≥2 bağımsız kaynak, link + içerik testi betikle yapıldı (dosya sonu).

**Etiketler:** **[kaynak]** linkli kaynakta okundu · **[ölçüm]** bu çalışmada API ile ölçüldü (tarih: 2026-10-27) · **[arama özeti]** WebSearch özeti, kaynağın kendisi okunmadı · **[tahmin]** ajan yorumu.
**Kaynak kuralı:** Bağımsız = farklı yayıncı (farklı alan adı). Wikipedia yalnız ikinci/üçüncü kaynak olarak sayıldı. Hiçbir konu yalnız Wikipedia'ya dayanmıyor. Britannica, Investopedia ve SEC bot korumalı (403/402) olduğu için açıldığı kanıtlanamadı, bu yüzden kullanılmadı.

## 0. Yöntem ve ölçüm araçları

| Ölçüm | Araç | Durum (2026-10-27) |
|---|---|---|
| Wikipedia sayfa görüntüleme (en, kullanıcı, günlük, 2026-07-28 → 2026-10-26) | Wikimedia REST API | Çalışıyor. Saniyede birden sık istekte 429 veriyor, bu yüzden bekleyerek ölçüldü. Ölçülemeyen birkaç sayfa "429" diye işaretlendi |
| YouTube arama | `YOUTUBE_API_KEY` `search.list` | **Günlük "Search Queries" kotası doldu** (429 `quotaExceeded`, ilk 7 sorgudan sonra). Arama yt-dlp (`ytsearch15` alaka + `ytsearchdate25` en yeni) ile yapıldı, izlenme ve tarih için API `videos.list` kullanıldı (kota ayrı, çalışıyor) |
| Google Trends | — | 429 (önceki denemeden). Kullanılmadı |
| Reddit | `reddit.com/*.json` | 403. Ölçülemedi |
| Hacker News | Algolia API, son 30 gün, >50 puan | Çalışıyor |
| Haber akışı | WebSearch (son 30 gün) | Çalışıyor. Özetler [arama özeti], linkler ayrıca açıldı |

**YouTube ölçüsünün okunuşu:** "alaka medyanı" = arama sonucundaki ilk 15 videonun medyan izlenmesi. Konunun ömür boyu talebini gösterir. "12 ayın en iyisi" = 2025-10-27'den sonra yüklenmiş en çok izlenen video (alaka 15 + en yeni 25 havuzundan). Taze talebi ve rakip doluluğunu gösterir. Örneklem küçük ve yt-dlp sıralaması YouTube arayüzüne bağlı, bu yüzden göstergedir, kesin ölçü değildir. Bir konuda alaka medyanı yüksek ama 12 ayın en iyisi düşükse **talep var ama son 12 ayda güçlü İngilizce video yok** demektir. Bu fırsat okunur [tahmin].

### 0.1 Üç arama stratejisi: hangisi kaç kaynaklı ve zamanlı konu verdi
| Strateji | Ne yapıldı | Aday | Kaynak testini geçen | Zamanlı (son 30 gün haber bağı) | Değerlendirme |
|---|---|---|---|---|---|
| **S1 Haber akışı** | WebSearch: piyasa, petrol, Fed, altın, kripto, özel kredi, CoreWeave (Ekim 2026) | 9 | 6 (B1–B3, C1–C3) | 6 | Zamanlamayı bu strateji verdi. Ayrıca 5 A konusuna güncel bağ getirdi (A1, A2, A3, A4, A12). Yan kaynakların çoğu ikinci el (kripto haber siteleri) olduğu için eleme oranı yüksek |
| **S2 Kalıcı tarih olayı + yıldönümü** | 36 + 12 Wikipedia sayfası pageviews, 28 YouTube sorgusu | 28 | 17 (A1–A17) | 5 yıldönümü (A1 29 Eki, A3 15–16 Kas, A7 Ekim–Aralık 2001'in 25. yılı, A8 11 Kas, A14 19 Eki) | En çok kaynaklı konuyu bu verdi. Kurumsal kaynak açık (Federal Reserve History, US State Dept. Historian, PBS, Econlib) |
| **S3 Topluluk gündemi (Reddit/HN)** | HN Algolia, 20 terim; Reddit 403 | 1 | 0 yeni konu (B1'e destek kaynağı oldu: "OpenAI annualised revenues $20B less than previously signalled", 434 puan, 2026-10-08) | 1 | En zayıf strateji. HN'de finans tarihi gündemi yok, Reddit kapalı. `pulse:pulse` aynı Reddit uç noktasına dayandığı için çalıştırılmadı |

**Sonuç:** A için S2 ile S1'in güncel bağı birlikte kullanıldı. S3 bu nişte konu üretmiyor (hafızaya yazıldı).

### 0.2 Önceki dersler
`uretim/*/yayin-sonrasi/` yok, çünkü kanalda henüz yayın yok. Uygulanacak performans dersi bulunmuyor. Rakip deseni (`docs/rakip-analizi.md` §5): en büyük outlier'ları kalıcı konu + kişi/ülke çapası üretiyor. Bu, A sütunu ve somut özneli başlıklar lehine bir kanıt.

### 0.3 Bağlam: Ekim 2026'da piyasa ne konuşuyor [kaynak, linkler B konularında]
- **Petrol:** Brent 2026-10-16'da 109,86 $ ile Mayıs'tan beri en yüksek seviyede. İran savaşı 2026-02-28'de başladı, Nisan'daki zirve 126,41 $.
- **Fed:** Eylül 2026'da 25 bp artırım yaptı (3,75–4,00 %). ABD Eylül TÜFE'si yıllık %3,7. FOMC 27–28 Ekim'de toplanıyor.
- **"AI balonu" korkusu:** CoreWeave 14–16 Ekim'de sert düştü, 5 yıllık CDS rekor ~1.194 bp. Nasdaq haftalık −%4'ün üzerinde.
- **Altın:** 29 Ocak 2026 rekorundan (5.318 $) ~%22 aşağıda (5 Ekim: 4.157 $).
→ A sütununda bu gündemle "eşleşen" tarih olayları: 1929 (çöküş korkusu), 1973 (petrol şoku), 1923 (enflasyon), dot-com ve Railway Mania (teknoloji balonu), Hunt kardeşler (emtia zirvesinden çöküş).

---

## 1. Öncelik tablosu: ilk herkese açık video için A sıralaması [ölçüm + tahmin]

Sıralama ölçütü: kanıtlı talep (Wikipedia + YouTube) × zamanlama (Pazar 2026-11-01'e yakın yıldönümü veya güncel bağ) × geniş kitle × reklam riski × görselleştirme. Puan değil, F2 için öneri. Kararı viralite-analisti ve hakem verir.

| Sıra | ID | Konu | Wiki ort./gün (son 30 g) [ölçüm] | Wiki trend (son 30 g / önceki 60 g) | YT alaka medyanı (≥1 M video, 15'te) [ölçüm] | YT 12 ayın en iyisi [ölçüm] | Zamanlama | Reklam riski [tahmin] |
|---|---|---|---|---|---|---|---|---|
| 1 | A1 | 1929 çöküşü ve Büyük Buhran | 1.374 (Great Depression: 3.126) | +11 % | 901 K (6/15) | İngilizce: 2 K. Endonezce bir video 1,66 M (API, 2026-07-26) | 29 Eki Kara Salı yıldönümü + "crash" korkusu | SARI-düşük (intihar miti kullanılmayacak) |
| 2 | A2 | 1973 petrol şoku | 730 | −5 % | 8 K. Sorguya en yakın 2 video 1,57 M ve 437 K | 1,57 M (Asian Boss, 2026-04-03) · 1,47 M (Wendover, "Iran war oil") | Brent 110 $, İran savaşı | SARI (süren savaş: anlatıda savaş değil ekonomi odağı) |
| 3 | A3 | Weimar hiperenflasyonu 1923 | 361 | +17 % | 48 K (1/15) | 48 K | 15–16 Kas 1923 Rentenmark (103. yıl). TÜFE %3,7. **Pilot kancası hazır** | YEŞİL-SARI (Nazi sembolü görseli yok) |
| 4 | A4 | Dot-com balonu (AI merceği) | 1.632 · CoreWeave 1.710 (önceki 60 g: 569, **3,0×**) | −3 % / CoreWeave +201 % | 290 K (1/15) | 611 K (Infographics "AI Bubble vs Dot Com", 2026-07-18) · AI-bubble sorgusunda 1,09 M (2026-10-22) | En sıcak gündem | YEŞİL (rakip benzerliği riski: viralite cezası) |
| 5 | A6 | Madoff Ponzi | 516 | −5 % | **749 K (7/15)** | 280 K (2026-01-21) | 11 Ara tutuklama yıldönümü | YEŞİL |
| 6 | A7 | Enron | 1.760 | **+47 %** (zirve 2026-10-26: 3.267) | 297 K (3/15) | 58 K | Çöküşün 25. yılı (Ekim–Aralık 2001) | YEŞİL |
| 7 | A8 | FTX | 461 (Bankruptcy of FTX) | +52 % (zirve 2026-10-09) | **1,83 M (9/15)** | 13 K | 11 Kas 2022'nin 4. yılı. SBF af talebi (Haziran 2026) | SARI-düşük (kripto: tanıtım yok) |
| 8 | A9 | Lale çılgınlığı | 715 | −2 % | (sorgu gürültülü) üst: 297 K, 265 K | 297 K (Extra History, 2026-05-09) | Kalıcı | YEŞİL |

Diğer A'lar (A5, A10–A17) aşağıda. Ham ölçüm verisi ve betikler: `01-arastirma/olcum/` (youtube-arama.json, wiki-pageviews-*.json, hn-30gun.json; anahtar dosyalarda yok, ortam değişkeninden okunur).

**Trend-avcisinin önerisi (F2'ye girdi, karar değil) [tahmin]:** İlk herkese açık video için **A1 (1929)** öne çıkıyor. Nişin en geniş ve kanıtlı talebi bunda. İngilizce tarafta son 12 ayda güçlü bir video yok. 29 Ekim yıldönümüyle güncel "crash" korkusu üst üste geliyor. Kanalın "The Collapse" serisini tanımlamaya da en uygun konu. **A2** en zamanlı olanı, ama savaş bağlamı reklam riskini artırıyor. **A3** pilot kancası hazır olduğu için üretim riski en düşük olanı. Talebi orta, Kasım yıldönümü Pazar slotuna denk geliyor.

---

## 2. A — Geçmiş: tarihin büyük finans çöküşleri (17)

### A1 — The 1929 Crash: Black Tuesday and the Great Depression
- **Özet:** Ekim 1929'da borçla şişen ABD borsası çöktü. Dow 28 Ekim'de ~%13, ertesi gün ("Black Tuesday") yine sert düştü. Ardından gelen bankacılık krizi Büyük Buhran'a dönüştü [kaynak K1, K2].
- **Neden şimdi:** 29 Ekim Kara Salı'nın 97. yıldönümü (yayından 3 gün önce). Ekim 2026'da "Black Monday" korkusu ve AI kaynaklı satış haberleri var (B1) [kaynak B1-K1].
- **Global bağ:** ABD kaynaklı, ama Buhran İngiltere, Kanada, Avustralya ve Hindistan'ı da vurdu. "Borsa yine çöker mi?" sorusu evrensel [tahmin].
- **Kaynaklar:**
  - K1: [Stock Market Crash of 1929](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: October 1929
  - K2: [Stock market crashes on Black Tuesday](https://www.history.com/this-day-in-history/october-29/stock-market-crashes) · HISTORY · tarih: yok (erişim 2026-10-27) · anahtar: Black Tuesday
  - K3: [The Stock Market Crash of 1929](https://internationalbanker.com/history-of-financial-crises/the-stock-market-crash-of-1929/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: 1929
- **İlgi kanıtı [ölçüm]:** Wikipedia "Wall Street crash of 1929" günde ort. 1.374 (son 30 g), "Great Depression" 3.126. Nişin en yüksek tarih sayfası. YouTube alaka medyanı 901 K, 15'te 6 video ≥1 M (CrashCourse 7,87 M, 2013; The Plain Bagel 3,94 M, 2018). 12 ayın en iyi İngilizce videosu ~2 K. Dev videolar eski, yeni kaliteli anlatım yok.
- **Hassas:** **hassas-düşük.** "Pencereden atlayan bankacılar" miti ve intihar anlatısı monetizasyon §5'e göre kullanılmaz. İşsizlik ve yoksulluk saygılı anlatılır.
- **Reklam dostu risk [tahmin]:** SARI-düşük. Başlık ve thumbnail'da "crash" kelimesi serbest, şok görseli yok.
- **Görselleştirme (≥3 kendi grafiği):** (1) Dow 1928–1932 (381 → 41, ~%89 düşüş, F3'te doğrulanacak) (2) marjin borcu balonu (3) ABD işsizliği 1929–33 (4) banka iflası sayacı.
- **Neden izlenir:** "Bugünkü balon korkusu 1929'a benziyor mu?" sorusunu, tarihin en ünlü çöküşünü adım adım yaşatarak cevaplar.

### A2 — The 1973 Oil Shock: when oil quadrupled and the world broke
- **Özet:** Ekim 1973'te Arap üretici ülkelerin (OAPEC) ambargosuyla petrol fiyatı aylar içinde ~4 katına çıktı. Kuyruklar, stagflasyon ve 1970'lerin Büyük Enflasyonu bunu izledi. Sonunda Volcker faizleri çok yükseltti [kaynak K1–K3].
- **Neden şimdi:** 2026'da İran savaşı sürüyor (2026-02-28'den beri), Brent 2026-10-16'da 109,86 $ [kaynak B2-K1, K2]. Ambargo Ekim 1973'te başlamıştı, yani tam 53. yıl.
- **Global bağ:** Benzin fiyatı her ülkenin cebine dokunuyor. ABD, İngiltere ve Hindistan'da akaryakıt enflasyonu gündemde [tahmin].
- **Kaynaklar:**
  - K1: [Oil Shock of 1973–74](https://www.federalreservehistory.org/essays/oil-shock-of-1973-74) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: embargo
  - K2: [Oil Embargo, 1973–1974](https://history.state.gov/milestones/1969-1976/oil-embargo) · US Dept. of State, Office of the Historian · tarih: yok (erişim 2026-10-27) · anahtar: embargo
  - K3: [1970s Energy Crisis](https://www.history.com/articles/energy-crisis) · HISTORY · tarih: yok (erişim 2026-10-27) · anahtar: 1973
  - K4: [Volcker's Announcement of Anti-Inflation Measures](https://www.federalreservehistory.org/essays/anti-inflation-measures) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: Volcker
- **İlgi kanıtı [ölçüm]:** Wikipedia "1973 oil crisis" günde 730. "Stagflation" 256, "Paul Volcker" 354 (Fed'in Eylül artırımında zirve: 1.702, 2026-09-17). YouTube'da taze talep güçlü: "Why The Oil Crisis is Way Worse Than You Think" 1,57 M (2026-04-03), Wendover "How the Iran War Spiked Oil Prices" 1,47 M (2026-04-17), Bloomberg Originals 730 K (2026-07-17). Saf "1973 oil crisis explained" sorgusunun alaka medyanı düşük (8 K): talep tarih anlatısından çok güncel petrol bağından geliyor.
- **Hassas:** **hassas** (süren bir savaşa atıf var). Savaş görseli, ölüm ya da yıkım yok. Odak ekonomik mekanizma. monetizasyon-uyum-uzmani bakmalı.
- **Reklam dostu risk [tahmin]:** SARI. Konu 1973 olarak çerçevelenirse risk düşer. 2026 savaşı yalnız bağlam cümlesi olur.
- **Görselleştirme:** (1) petrol fiyatı 1972–1974 basamağı (~3 $ → ~12 $, F3'te doğrulanacak) (2) ABD TÜFE 1965–1982 ve Volcker faizi (3) 1973 ile 2026 Brent eğrisi yan yana (4) benzin kuyruğu metaforu.
- **Neden izlenir:** "Benzin neden bu kadar pahalı ve 1973'teki gibi her şeyi pahalandırır mı?" sorusu bugün herkesin cebinde.

### A3 — Weimar Germany 1923: when a loaf of bread cost billions
- **Özet:** Ruhr işgali sonrası açığı para basarak kapatan Almanya'da fiyatlar 1923'te saat saat arttı. Kasım 1923'te Rentenmark ile durduruldu [kaynak K1, K2, K3].
- **Neden şimdi:** Hiperenflasyonun zirvesi ve Rentenmark Kasım 1923'te (103. yıl, Pazar slotu 1 Kasım). ABD TÜFE'si %3,7'ye çıktı, Fed yeniden faiz artırıyor [kaynak B2-K3, K4]. Pilot klipte (`uretim/ses-testi/pilot/`) 1923 kancası hazır.
- **Global bağ:** "Birikimim bir fincan kahveye dönerse?" Enflasyonu yaşayan her ülkeye kişisel bağ (İngiltere, Hindistan, Kanada) [tahmin].
- **Kaynaklar:**
  - K1: [Hyperinflation (Concise Encyclopedia of Economics)](https://www.econlib.org/library/Enc/Hyperinflation.html) · Econlib (Liberty Fund) · tarih: yok (erişim 2026-10-27) · anahtar: German
  - K2: [The German Hyperinflation, 1923](https://www.pbs.org/wgbh/commandingheights/shared/minitextlo/ess_germanhyperinflation.html) · PBS Commanding Heights · tarih: yok (erişim 2026-10-27) · anahtar: 1923
  - K3: [Hyperinflation in the Weimar Republic](https://en.wikipedia.org/wiki/Hyperinflation_in_the_Weimar_Republic) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1923
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 361 (önceki 60 güne göre +%17, zirve 2026-10-15). YouTube alaka medyanı 48 K. En büyük 1,87 M (Money & Macro, Nazi ekonomisi açısı), 507 K. 12 ayın en iyisi 48 K. Talep orta, rakip doluluğu düşük.
- **Hassas:** **hassas-düşük.** Hitler'in yükselişine tek cümleyle değinilebilir. Gamalı haç ya da Nazi görseli yok.
- **Reklam dostu risk [tahmin]:** YEŞİL-SARI.
- **Görselleştirme:** (1) 1 $ = X mark log grafiği (1919–1923) (2) ekmek fiyatı merdiveni (3) banknot değerinin "üzerine yazılan sıfırlar" sayacı (4) Rentenmark sonrası düzleşen eğri. Pilotta "birikim → kahve" grafiği zaten var.
- **Neden izlenir:** Paranın gözünüzün önünde eridiği en uç örnek. "Bu bizim paramıza olabilir mi?" merakını doğrudan tetikler.

### A4 — The Dot-Com Bubble (through today's AI lens)
- **Özet:** Nasdaq 1995'te ~750'den 10 Mart 2000'de 5.048'e çıktı, Ekim 2002'ye kadar ~%78 düştü. Pets.com gibi kârsız şirketler battı [kaynak K1, K2].
- **Neden şimdi:** Ekim 2026'da CoreWeave'in hissesi ve tahvilleri çöktü, "AI balonu" tartışması zirvede [kaynak K3, K4].
- **Global bağ:** Teknoloji hisseleri dünya endekslerinin ve emeklilik fonlarının büyük kısmı [tahmin].
- **Kaynaklar:**
  - K1: [The Dotcom Bubble Burst (2000)](https://internationalbanker.com/history-of-financial-crises/the-dotcom-bubble-burst-2000/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: Nasdaq
  - K2: [Dot-com bubble](https://en.wikipedia.org/wiki/Dot-com_bubble) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 2000
  - K3: [Everyone's wondering if, and when, the AI bubble will pop. Here's what went down 25 years ago](https://fortune.com/2025/09/28/ai-dot-com-bubble-parallels-history-explained-companies-revenue-infrastructure) · Fortune · tarih: 2025-09-28 · anahtar: fiber
  - K4: [Black Monday fears intensify as prediction markets shrug off 2026 crash](https://finbold.com/black-monday-fears-intensify-as-prediction-markets-shrug-off-2026-crash/) · Finbold · tarih: 2026-10-18 · anahtar: CoreWeave
- **İlgi kanıtı [ölçüm]:** Wikipedia "Dot-com bubble" günde 1.632. "CoreWeave" 1.710 (önceki 60 günde 569, **3,0×**, zirve 7.545, 2026-10-15). YouTube: "AI Bubble vs Dot Com Crash" (Infographics) 611 K, 2026-07-18. Infographics'in "What if the AI Bubble Bursts" videosu 4,81 M (2026-09-03, API). Son hafta: JayzTwoCents 1,09 M, The Tech Report 522 K, All-In "CoreWeave Crash" 920 K (2026-10-17).
- **Hassas:** hayır.
- **Reklam dostu risk [tahmin]:** YEŞİL. **Özgünlük riski:** "AI vs dot-com" açısı Infographics'te iki kez işlendi. Aynı kalıp viralite modelinde `benzer_aci` −1,5 cezası alır. Özgün açı önerisi: tek bir hissenin hikâyesi (ör. 2000'in "en değerli şirketinin" uzun toparlanması, F3'te doğrulanacak) ya da A5 Railway Mania.
- **Görselleştirme:** (1) Nasdaq 1995–2015 (zirve → 15 yıl toparlanma) (2) fiyat/kazanç oranı 1999 ile 2026 (3) "lit fiber" oranı (4) halka arz sayısı.
- **Neden izlenir:** "AI balonu patlarsa ne olur?" sorusuna, gerçekten patlamış bir balonun gün gün hikâyesiyle cevap verir.

### A5 — Railway Mania 1845–47: Britain's AI-bubble ancestor
- **Özet:** 1840'larda İngiltere'de demiryolu hisseleri çılgınca yükseldi, borsada kotasyonlu demiryolu sayısı patladı. 1847 panikle çöktü, ama inşa edilen raylar ülkeyi dönüştürdü [kaynak K1–K4].
- **Neden şimdi:** AI veri merkezi harcaması "yeni demiryolu" diye tartışılıyor. CoreWeave borç korkusu (B1) [kaynak K1, K2].
- **Global bağ:** İngiltere izleyicisi için yerli hikâye. "Yararlı teknoloji yine de balon olabilir" dersi evrensel [tahmin].
- **Kaynaklar:**
  - K1: [The Railway Bubble vs. the AI Bubble](https://awealthofcommonsense.com/2025/11/the-railway-bubble-vs-the-ai-bubble/) · A Wealth of Common Sense (Ben Carlson) · tarih: 2025-11-25 · anahtar: railway
  - K2: [A Revolutionary Technology or a Bubble?](https://www.td.com/ca/en/asset-management/insights/blog/a-revolutionary-technology-or-a-bubble) · TD Asset Management · tarih: yok (erişim 2026-10-27) · anahtar: railway
  - K3: [Is the AI bubble about to burst?](https://unherd.com/2025/08/is-the-ai-bubble-about-to-burst/) · UnHerd (John Rapley) · tarih: 2025-08 (gün yok) · anahtar: railway
  - K4: [Railway Mania](https://en.wikipedia.org/wiki/Railway_Mania) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1847
- **İlgi kanıtı [ölçüm]:** YouTube "Railway Mania bubble 1840s" alaka medyanı **57**, 12 ayın en iyisi 208. Wikipedia: ölçülemedi (429, 3 tekrar sonrası). **Kanıtlı talep zayıf.** Rakip yok denecek kadar az: özgün açı, ama talep testi yok.
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) demiryolu hisse endeksi 1843–1850 (2) onaylanan hat uzunluğu (Parlamento) (3) temettü %7 → %2,4 [arama özeti, doğrulanacak] (4) 1846 ile 2026 "altyapı harcaması / GSYH" karşılaştırması.
- **Neden izlenir:** "AI balonu" tartışmasına herkesin bildiği dot-com yerine kimsenin anlatmadığı, daha çarpıcı bir ata gösterir. Risk: arama talebi kanıtsız.

### A6 — Bernie Madoff: the $65 billion Ponzi scheme
- **Özet:** Nasdaq'ın eski başkanı Madoff, onlarca yıl "istikrarlı getiri" vaadiyle tarihin en büyük Ponzi şemasını yürüttü. Aralık 2008'de çöktü [kaynak K1–K3].
- **Neden şimdi:** 11 Aralık 2008 tutuklama yıldönümü (stok için Aralık'a yakın uygun). Kalıcı "dolandırıcılık" merakı [tahmin].
- **Global bağ:** Mağdurlar ABD, İngiltere ve Avrupa'daydı. "Too good to be true" dersi evrensel.
- **Kaynaklar:**
  - K1: [The Madoff Affair](https://www.pbs.org/wgbh/frontline/documentary/madoff/) · PBS FRONTLINE · tarih: yok (erişim 2026-10-27) · anahtar: Madoff
  - K2: [Bernie Madoff's Ponzi Scheme (2008)](https://internationalbanker.com/history-of-financial-crises/bernie-madoffs-ponzi-scheme-2008/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: Madoff
  - K3: [Madoff investment scandal](https://en.wikipedia.org/wiki/Madoff_investment_scandal) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: Ponzi
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 516. YouTube alaka medyanı **749 K, 15'te 7 video ≥1 M** (FRONTLINE 11,6 M, 60 Minutes 5,1 M). 12 ayın en iyisi 280 K ("Would Bernie Madoff's Fraud Even Be That Bad By Today's Standards?", 2026-01-21).
- **Hassas:** **hassas-düşük** (mağdurlar var, oğlunun intiharı anlatılmaz).
- **Reklam dostu risk [tahmin]:** YEŞİL (eğitsel, eleştirel; monetizasyon §5 "Ponzi anlatılabilir").
- **Görselleştirme:** (1) Madoff'un "düz" getiri eğrisi ile S&P 500 (2) para giriş/çıkış akış şeması (3) mağdur dağılımı haritası (4) Markopolos uyarı zaman çizelgesi.
- **Neden izlenir:** "Hiç kaybetmeyen yatırım" vaadinin nasıl 65 milyar dolarlık bir yalana dönüştüğünü ve uyarıların neden duyulmadığını anlatır.

### A7 — Enron: America's most admired company that was a lie
- **Özet:** Enron muhasebe hileleriyle borcunu gizledi. 2001'de çöktü, 2 Aralık 2001'de iflas etti. Arthur Andersen de onunla battı, Sarbanes-Oxley yasası doğdu [kaynak K1–K3].
- **Neden şimdi:** Çöküşün 25. yılı (Ekim–Aralık 2001). Wikipedia ilgisi son 30 günde +%47, 2026-10-26'da zirve. Zirvenin nedeni bulunamadı [tahmin: yıldönümü yazıları].
- **Global bağ:** Kurumsal yönetişim, emeklilik fonları. Hindistan'da Dabhol santrali bağlantısı [tahmin, doğrulanmadı].
- **Kaynaklar:**
  - K1: [On this day: Enron files for bankruptcy](https://www.cityam.com/on-this-day-enron-files-for-bankruptcy/) · City A.M. · tarih: yok (erişim 2026-10-27) · anahtar: Enron
  - K2: [Dec. 2, 2001: Enron files for bankruptcy](https://abajournal.com/magazine/article/dec_2_2001_enron_files_for_bankruptcy) · ABA Journal · tarih: yok (erişim 2026-10-27) · anahtar: Enron
  - K3: [The Enron Scandal (2001)](https://internationalbanker.com/history-of-financial-crises/the-enron-scandal-2001/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: Enron
  - K4: [Enron scandal](https://en.wikipedia.org/wiki/Enron_scandal) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 2001
- **İlgi kanıtı [ölçüm]:** Wikipedia günde **1.760** (önceki 60 gün 1.195, **+%47**). YouTube alaka medyanı 297 K, 15'te 3 video ≥1 M (ColdFusion 8,75 M). 12 ayın en iyisi 58 K.
- **Hassas:** hassas-düşük (çalışanların emeklilik kaybı).
- **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) hisse 90 $ → 0,26 $ eğrisi (2) "özel amaçlı şirket" borç saklama şeması (3) Fortune "most innovative" yılları ve gerçek nakit akışı (4) iflas boyutu karşılaştırması.
- **Neden izlenir:** Dünyanın en hayran olunan şirketinin bir muhasebe illüzyonu olduğu ortaya çıkıyor. 25. yılında "bugün bir Enron var mı?" sorusu.

### A8 — FTX: the $32 billion crypto empire that vanished in a week
- **Özet:** Kasım 2022'de FTX'te müşteri parasının Alameda'ya aktarıldığı ortaya çıktı. Para çekme dalgası bir haftada şirketi batırdı. SBF 25 yıl hapis aldı [kaynak K1–K3].
- **Neden şimdi:** 11 Kasım 2022 iflasının 4. yılı. SBF Haziran 2026'da af başvurusu yaptı [arama özeti: Fortune etiket sayfası]. Wikipedia ilgisi +%52 (zirve 2026-10-09).
- **Global bağ:** Kripto kullanıcıları (Hindistan, ABD, İngiltere), Bahamalar.
- **Kaynaklar:**
  - K1: [A timeline of the historic collapse of FTX](https://abc11.com/post/a-timeline-of-the-historic-collapse-of-ftx/12468749/) · ABC News (ABC11) · tarih: 2022-11-18 · anahtar: FTX
  - K2: [Sam Bankman-Fried apologizes for FTX's collapse](https://www.fortune.com/2022/11/22/sam-bankman-fried-apologizes-ftx-collapse-alameda-research-bankruptcy) · Fortune · tarih: 2022-11-22 · anahtar: FTX
  - K3: [Bankruptcy of FTX](https://en.wikipedia.org/wiki/Bankruptcy_of_FTX) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: November 2022
- **İlgi kanıtı [ölçüm]:** Wikipedia "Bankruptcy of FTX" günde 461 (+%52), "FTX" 779 (+%34, zirve 2026-10-08). YouTube alaka medyanı **1,83 M, 15'te 9 video ≥1 M** (James Jani 11,0 M, ColdFusion 8,8 M). 12 ayın en iyisi 13 K. **Çok doymuş:** büyük kanallar konuyu kapatmış.
- **Hassas:** hayır. **Reklam [tahmin]:** SARI-düşük. Kripto tanıtımı, referans linki ya da "coin al" yok (monetizasyon §5).
- **Görselleştirme:** (1) FTT token fiyatı Kasım 2022 (2) müşteri parası akış şeması FTX → Alameda (3) 7 günlük para çekme sayacı (4) 32 milyar → 0 değer eğrisi.
- **Neden izlenir:** Bir dahinin imparatorluğunun 7 günde çöküşü ve "paran borsada güvende mi?" sorusu.

### A9 — Tulip Mania 1637: the first bubble (and the myth)
- **Özet:** 1630'larda Hollanda'da nadir lale soğanlarının vadeli kontratları uçtu, Şubat 1637'de çöktü. Modern tarihçiler çöküşün ekonomik etkisinin abartıldığını söylüyor [kaynak K1–K3].
- **Neden şimdi:** Kalıcı konu. "Pokémon kartı yatırımı" gibi yeni çılgınlıklarla karşılaştırılıyor (YouTube 553 K, 2026-07-25, API) [ölçüm].
- **Global bağ:** "Balon" kavramının çıkış noktası, her ülkede okul müfredatında [tahmin].
- **Kaynaklar:**
  - K1: [The Real Story Behind the 17th-Century 'Tulip Mania' Financial Crash](https://www.history.com/articles/tulip-mania-financial-crash-holland) · HISTORY · tarih: yok (erişim 2026-10-27) · anahtar: 1637
  - K2: [Bubbles (Concise Encyclopedia of Economics)](https://www.econlib.org/library/Enc/Bubbles.html) · Econlib · tarih: yok (erişim 2026-10-27) · anahtar: Tulip
  - K3: [Tulip mania](https://en.wikipedia.org/wiki/Tulip_mania) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1637
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 715. YouTube: Extra History 297 K (2026-05-09), Jabzy 265 K. Alaka medyanı sorgu gürültüsünden dolayı güvenilmez. API sorgusunda medyan 109 K.
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) "Viceroy" soğanı fiyatı ile ev ve maaş karşılaştırması (2) Şubat 1637 fiyat endeksi (3) mit ile gerçek tablosu.
- **Neden izlenir:** "Bir çiçek soğanı ev fiyatına mı satıldı?" sorusu ve herkesin bildiği hikâyenin yarısının mit olduğu sürprizi.

### A10 — The South Sea Bubble 1720 (and John Law's Mississippi twin)
- **Özet:** 1720'de İngiltere'de South Sea Company, Fransa'da John Law'un Mississippi şirketi devlet borcunu hisseye çevirip balon yaptı ve aynı yıl çöktü. Isaac Newton'ın para kaybettiği anlatılır [kaynak K1, K2; Newton detayı F3'te doğrulanacak].
- **Neden şimdi:** Kalıcı. "Devlet borcu + hype" bugünkü borç tartışmasıyla eşleşiyor [tahmin].
- **Global bağ:** İngiltere'nin ilk başbakanı Walpole bu krizden çıktı (İngiltere izleyicisi).
- **Kaynaklar:**
  - K1: [South Sea Bubble, 1720](https://www.library.hbs.edu/hc/ssb/) · Harvard Business School Baker Library · tarih: yok (erişim 2026-10-27) · anahtar: 1720
  - K2: [South Sea Company](https://en.wikipedia.org/wiki/South_Sea_Company) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1720
  - K3: [John Law's Company (Mississippi Company)](https://en.wikipedia.org/wiki/Mississippi_Company) · Wikipedia (K2 ile aynı yayıncı, bağımsız sayılmadı) · tarih: yok (erişim 2026-10-27) · anahtar: Law
- **İlgi kanıtı [ölçüm]:** Wikipedia "South Sea Company" günde 424 (+%15). "John Law" 168. YouTube alaka medyanı 36 K, 15'te 4 video ≥1 M (Extra History 3,47 M ve 2,37 M). 12 ayın en iyisi 926: talep var, yeni video yok.
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) South Sea hisse fiyatı 1720 (~128 → ~1.000 → ~150 £, doğrulanacak) (2) Londra ve Paris balonları üst üste (3) Newton'un alım-satım zaman çizelgesi.
- **Neden izlenir:** "Tarihin en zeki insanı bile balona kandıysa biz neyiz?" kancası.

### A11 — Zimbabwe: the 100-trillion-dollar banknote
- **Özet:** Zimbabwe'de 2008'de aylık enflasyon astronomik seviyeye ulaştı. 100 trilyon dolarlık banknot bir otobüs biletine yetmedi, 2009'da yerel para terk edildi [kaynak K1, K2].
- **Neden şimdi:** Kalıcı. A3 ile seri olabilir ("hiperenflasyon" listesi) [tahmin].
- **Global bağ:** Banknot koleksiyoncuları. Afrika diasporası (İngiltere).
- **Kaynaklar:**
  - K1: [Visitors snap up 100-trillion Zimbabwe bank notes](https://mg.co.za/article/2011-01-03-visitors-snap-up-100trillion-zimbabwe-bank-notes/) · Mail & Guardian · tarih: 2011-01-03 · anahtar: trillion
  - K2: [Hyperinflation in Zimbabwe](https://en.wikipedia.org/wiki/Hyperinflation_in_Zimbabwe) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: trillion
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 264. YouTube alaka medyanı 77 K, 15'te 4 video ≥1 M (Half-Asleep Chris 9,8 M, PolyMatter 7,6 M). 12 ayın en iyisi 1,3 K.
- **Hassas:** **hassas** (yoksulluk, açlık, siyasi baskı; insani acı merkezde). Monetizasyon bakmalı.
- **Reklam [tahmin]:** SARI.
- **Görselleştirme:** (1) banknot nominal değer merdiveni (2) fiyatların ikiye katlanma süresi (3) GSYH çöküşü.
- **Neden izlenir:** Trilyonluk banknotla ekmek alamamak, paranın ne olduğunu en net sorgulatan görüntü.

### A12 — The Hunt Brothers: cornering the world's silver (Silver Thursday 1980)
- **Özet:** Teksaslı milyarder Hunt kardeşler 1970'lerde dünya gümüşünün büyük kısmını topladı. Gümüş Ocak 1980'de 48,70 $ ile zirve yaptı. Borsa kuralları değişince 27 Mart 1980'de ("Silver Thursday") çöktüler [kaynak K1, K2].
- **Neden şimdi:** Altın 2026'nın Ocak rekorundan ~%22 düştü (B3). Emtia "zirveden çöküş" gündemi [kaynak B3-K1].
- **Global bağ:** Hindistan altın ve gümüş talebi. Emtia yatırımı merakı [tahmin].
- **Kaynaklar:**
  - K1: [A tale of two silver markets—and two disasters](https://www.abajournal.com/magazine/article/panic-1893-hunt-brothers-1980) · ABA Journal · tarih: yok (erişim 2026-10-27) · anahtar: silver
  - K2: [Silver Thursday](https://en.wikipedia.org/wiki/Silver_Thursday) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1980
  - K3: [Editorial: Hunts' silver play the stuff of legend](https://www.northernminer.com/news/editorial-hunts-silver-play-the-stuff-of-legend/1003323583/) · The Northern Miner (ücretli duvar; başlık açılıyor) · tarih: yok (erişim 2026-10-27) · anahtar: Hunt
- **İlgi kanıtı [ölçüm]:** Wikipedia "Silver Thursday" günde 126. YouTube: "They Bought Nearly All the World's Silver. It Ended in Disaster" 312 K (2026-07-18), alaka medyanı 3 K. Konu YouTube'da yeni yeni patlıyor.
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) gümüş 1979–1980 (6 $ → 48,70 $ → 10,80 $) (2) Hunt'ların ons stoku (3) marjin çağrısı zinciri (4) 1980 gümüş ile 2026 altın eğrisi yan yana.
- **Neden izlenir:** İki kardeşin bir metali "satın alıp" dünyayı ele geçirmeye çalışması ve bir günde kaybetmesi, gerilim filmi gibi bir hikâye.

### A13 — Japan's Bubble 1989: when Tokyo was worth more than America
- **Özet:** 1980'lerin sonunda Japon hisse ve arsa fiyatları şişti. Nikkei Aralık 1989'da zirve yaptı, sonra "kayıp on yıllar" geldi [kaynak K1, K2].
- **Neden şimdi:** Japonya 10 yıllık tahvil faizi 2026 Eylül'de ~%3 ile 1996'dan beri en yüksek. Yen zayıf [kaynak K3].
- **Global bağ:** Japonya dünyanın en büyük alacaklılarından. Faiz şoku küresel piyasaları etkiler [tahmin].
- **Kaynaklar:**
  - K1: [Japan's Lost Decade (1992)](https://internationalbanker.com/history-of-financial-crises/japans-lost-decade-1992/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: Nikkei
  - K2: [Japanese asset price bubble](https://en.wikipedia.org/wiki/Japanese_asset_price_bubble) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: Nikkei
  - K3: [Japan 10Y Bond Yield traded above 3 percent](https://tradingeconomics.com/japan/government-bond-yield/news/579798) · Trading Economics · tarih: 2026-09-01 · anahtar: Japan
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 386. YouTube alaka medyanı 104 K (ColdFusion 2,82 M). 12 ayın en iyisi 414 K ("The Economic Crisis We Learned Nothing From", 2025-12-17).
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) Nikkei 1985–2024 (34 yıl sonra rekor, doğrulanacak) (2) "İmparatorluk Sarayı arazisi = Kaliforniya" iddiası (doğrulanacak) (3) Tokyo arsa fiyat endeksi.
- **Neden izlenir:** Dünyanın en zengin ülkesi olacağı düşünülen Japonya'nın 30 yıl kaybetmesi. "Bir ülke balondan nasıl hiç çıkamaz?" sorusu.

### A14 — Black Monday 1987: the day the market fell 22.6%
- **Özet:** 19 Ekim 1987'de Dow tek günde %22,6 düştü. Tarihin en büyük günlük düşüşü. Portföy sigortası ve programlı satış zinciri suçlandı [kaynak K1, K2].
- **Neden şimdi:** 39. yıldönümü yeni geçti (19 Ekim). 2026 Ekim'inde "Black Monday" korkusu haberlerde [kaynak B1-K1].
- **Global bağ:** Çöküş Hong Kong, Londra, Sidney ve Yeni Zelanda'yı aynı gün vurdu (Avustralya ve İngiltere izleyicisi).
- **Kaynaklar:**
  - K1: [Stock Market Crash of 1987](https://www.federalreservehistory.org/essays/stock-market-crash-of-1987) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: October 19
  - K2: [Black Monday (1987)](https://internationalbanker.com/history-of-financial-crises/black-monday-1987/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: 1987
  - K3: [Black Monday (1987)](https://en.wikipedia.org/wiki/Black_Monday_%281987%29) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1987
- **İlgi kanıtı [ölçüm]:** Wikipedia ölçülemedi (429). YouTube alaka medyanı 68 K, 15'te 2 video ≥1 M. 12 ayın en iyisi 47 K ("Black Monday: The Biggest Crash EVER!", 2026-10-22, 5 günde).
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) Dow 19 Ekim saatlik (2) ülke ülke düşüş haritası (3) 1987 ile 1929 ile 2020 günlük düşüş sıralaması.
- **Neden izlenir:** "Borsa bir günde %22 düşebilir mi?" Düştü, ve şaşırtıcı biçimde ekonomi çökmedi.

### A15 — LTCM 1998: the Nobel-winning hedge fund that almost broke Wall Street
- **Özet:** İki Nobel ödüllü ekonomistin yer aldığı LTCM aşırı kaldıraçla 1998 Rusya krizinde çöktü. Fed'in koordinasyonuyla 14 banka 3,6 milyar $ kurtarma yaptı [kaynak K1, K2].
- **Neden şimdi:** Kalıcı. 2026'daki özel kredi ve kaldıraç endişesi bağ kurabilir [tahmin].
- **Global bağ:** Küresel tahvil piyasaları, Rusya temerrüdü.
- **Kaynaklar:**
  - K1: [Near Failure of Long-Term Capital Management](https://www.federalreservehistory.org/essays/ltcm-near-failure) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: 1998
  - K2: [Long-Term Capital Management](https://en.wikipedia.org/wiki/Long-Term_Capital_Management) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 1998
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 257 (−%33). YouTube 12 ayın en iyisi **1,04 M** ("The Most Dangerous Hedge Fund in History", Hamish Hodder, 2025-11-15). Alaka medyanı 6,5 K.
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) LTCM özsermaye 1994–1998 (2) kaldıraç oranı (~25:1, doğrulanacak) (3) kurtarmaya katılan bankalar şeması.
- **Neden izlenir:** Dünyanın en zeki ekipleri matematikle "riski yok etti" ve piyasa onları birkaç haftada sildi.

### A16 — Black Wednesday 1992: the man who broke the Bank of England
- **Özet:** 16 Eylül 1992'de İngiltere sterlini ERM'den çıkarmak zorunda kaldı. George Soros'un fonunun bu bahisten ~1 milyar $ kazandığı bildirildi [kaynak K1, K2].
- **Neden şimdi:** Kalıcı. İngiltere izleyicisi için yerli hikâye.
- **Global bağ:** İngiltere. Döviz sabitlemesi dersi (Hindistan ve gelişen piyasalar).
- **Kaynaklar:**
  - K1: [Black Wednesday 20 years on: how the day unfolded](https://www.theguardian.com/business/2012/sep/13/black-wednesday-20-years-pound-erm) · The Guardian · tarih: 2012-09-13 · anahtar: 1992
  - K2: [Black Wednesday](https://en.wikipedia.org/wiki/Black_Wednesday) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 16 September 1992
- **İlgi kanıtı [ölçüm]:** Wikipedia günde 482. YouTube: Business Casual 2,91 M, Patrick Boyle 1,33 M (alaka sorgusu gürültülü, medyan 1,9 K). 12 ayın en iyisi 2,3 K: talep kanıtlı, yeni İngilizce video yok.
- **Hassas:** **dikkat:** Soros siyasi olarak kutuplaştırıcı bir figür. Komplo çerçevesi yok, yalnız işlem mekaniği anlatılır. Monetizasyon bakmalı.
- **Reklam [tahmin]:** YEŞİL-SARI.
- **Görselleştirme:** (1) sterlin/DM kuru ve ERM bandı (2) gün içi faiz artışları %10 → %12 → %15 (3) Soros pozisyon büyüklüğü.
- **Neden izlenir:** Tek bir yatırımcının bir merkez bankasına karşı bahse girip kazanması.

### A17 — Lehman Brothers 2008: the weekend that broke the world
- **Özet:** Konut kredisi balonu çöktü. Lehman 15 Eylül 2008'de iflas etti, küresel finans krizi ve Büyük Durgunluk başladı [kaynak K1, K2].
- **Neden şimdi:** Kalıcı. Özel kredi tartışmaları "yeni 2008 mi?" diye çerçeveleniyor [arama özeti].
- **Global bağ:** Tüm kitle ülkeleri etkilendi (İngiltere'de Northern Rock).
- **Kaynaklar:**
  - K1: [The Great Recession](https://www.federalreservehistory.org/essays/great-recession-of-200709) · Federal Reserve History · tarih: yok (erişim 2026-10-27) · anahtar: Great Recession
  - K2: [The Subprime Mortgage Crisis (2007-08)](https://internationalbanker.com/history-of-financial-crises/the-subprime-mortgage-crisis-2007-08/) · International Banker · tarih: yok (erişim 2026-10-27) · anahtar: Lehman
  - K3: [Bankruptcy of Lehman Brothers](https://en.wikipedia.org/wiki/Bankruptcy_of_Lehman_Brothers) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: 2008
- **İlgi kanıtı [ölçüm]:** Wikipedia "2008 financial crisis" günde 2.184, "Lehman Brothers" 1.537. YouTube alaka medyanı 213 K, 15'te 4 video ≥1 M. 12 ayın en iyisi 245 K. Diary of a CEO "crash expert" 8,76 M (2026-04-06, API). **Çok doymuş.**
- **Hassas:** hassas-düşük (ev kaybı, işsizlik).
- **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** (1) Case-Shiller ev fiyat endeksi (2) Lehman kaldıraç 30:1 (doğrulanacak) (3) 15 Eylül haftası gün gün zaman çizelgesi.
- **Neden izlenir:** Tek bir hafta sonunda verilen "kurtarmayalım" kararının dünyayı nasıl değiştirdiği.

---

## 3. B — Güncel (sonraki Çarşamba slotları için; stoklanmaz)

### B1 — The AI credit scare: CoreWeave's crash and "is this 2000 again?"
- **Özet:** AI bulut şirketi CoreWeave'in hissesi 14–16 Ekim 2026'da sert düştü. 5 yıllık CDS ~1.194 bp ile rekor kırdı. Veri merkezi borcu ve AI gelirleri sorgulanıyor [kaynak K1, K2; rakamlar arama özetinde kaynaklar arası çelişkili].
- **Neden şimdi:** Son 2 hafta. FOMC 27–28 Ekim.
- **Global bağ:** Nvidia, Oracle ve teknoloji fonları, yani dünya emeklilik portföyleri [tahmin].
- **Kaynaklar:**
  - K1: [Black Monday fears intensify as prediction markets shrug off 2026 crash](https://finbold.com/black-monday-fears-intensify-as-prediction-markets-shrug-off-2026-crash/) · Finbold · tarih: 2026-10-18 · anahtar: CoreWeave
  - K2: [CoreWeave Credit Default Swaps Signal Over 60% Default Risk](https://www.kucoin.com/news/flash/coreweave-credit-default-swaps-signal-over-60-default-risk) · KuCoin News (Benzinga/Bloomberg verisini aktarıyor) · tarih: 2026-10-16 · anahtar: CoreWeave
  - K3: [OpenAI annualised revenues $20B less than previously signalled](https://news.ycombinator.com/item?id=50008187) · Hacker News (434 puan, 301 yorum) · tarih: 2026-10-08 · anahtar: OpenAI
- **İlgi kanıtı [ölçüm]:** Wikipedia "CoreWeave" 3,0× (zirve 7.545, 2026-10-15). YouTube son 10 gün: All-In 920 K, JayzTwoCents 1,09 M, Mark Tilbury "It Started: The AI Bank Run" 560 K (2026-10-21).
- **Hassas:** hayır. **Reklam:** YEŞİL. Tek şirkete "batacak" demek yanıltıcı/karalayıcı riski taşır: finans-dogrulayici bakmalı [tahmin].
- **Görselleştirme:** CDS eğrisi, borç/gelir oranı, 2000 ile 2026 capex/GSYH.
- **Neden izlenir:** "AI balonu patlıyor mu?" sorusu şu an YouTube'un en sıcak finans sorusu.
- **Kaynak kalitesi notu:** Birincil kaynaklar (Reuters, Bloomberg) bot korumalı ya da ücretli. Elimizdekiler ikinci el. B seçilirse F3'te birincil kaynak şart.

### B2 — $110 oil + a Fed that's hiking again: is stagflation back?
- **Özet:** Brent 2026-10-16'da 109,86 $. ABD Eylül TÜFE'si %3,7 (çekirdek %2,6). Fed Eylül'de 3,75–4,00 %'e artırdı, 28 Ekim kararı bekleniyor [kaynak K1–K4].
- **Neden şimdi:** FOMC 27–28 Ekim 2026.
- **Global bağ:** Akaryakıt ve ipotek faizi (ABD, İngiltere, Kanada, Avustralya), Hindistan petrol ithalatı.
- **Kaynaklar:**
  - K1: [Brent touches US$110 for the first time since May on Middle East tensions](https://en.mercopress.com/2026/10/17/brent-touches-us-110-for-the-first-time-since-may-on-middle-east-tensions) · MercoPress · tarih: 2026-10-17 · anahtar: Brent
  - K2: [Oil gains as Middle East conflict and tanker attacks lift Brent to US$105.48](https://www.nationthailand.com/news/world/40072133) · The Nation (Thailand) · tarih: 2026-10-12 · anahtar: Brent
  - K3: [US CPI September 2026 headline inflation report](https://blog.orbitremit.com/us-cpi-september-2026-headline-inflation-report/) · OrbitRemit · tarih: 2026-10-19 · anahtar: 3.7
  - K4: [Taking Stock – September 16, 2026 – Fed rate decision](https://www.empower.com/investment-insights/trends/taking-stock-september-16-2026-fed-rate-decision) · Empower · tarih: 2026-09-16 · anahtar: 3.75
- **İlgi kanıtı [ölçüm]:** Wikipedia "Paul Volcker" Fed kararı günü 1.702 (2026-09-17). YouTube "Iran war oil price" sorgusu: Wendover 1,47 M, Bloomberg 730 K.
- **Hassas:** **hassas** (savaş). **Reklam:** SARI [tahmin].
- **Görselleştirme:** Brent 2026 eğrisi, TÜFE bileşenleri, Fed faiz basamağı.
- **Neden izlenir:** "Benzin, kira, kredi neden yine pahalanıyor?" sorusunun tek videoda cevabı.

### B3 — Gold's 22% fall from its record: what just happened?
- **Özet:** Altın 29 Ocak 2026'da 5.318 $ rekor kapanış yaptı, 5 Ekim'de 4.157 $'a indi. Nedenler: yükselen faiz ve getiriler, güçlü dolar (K2, Ekim). İlk sert kırılma Şubat'ta Warsh'ın Fed başkanlığına aday gösterilmesiyle geldi (K3, 2026-02-02) [kaynak K1–K3].
- **Neden şimdi:** Ekim boyunca düşüş sürüyor. FOMC.
- **Global bağ:** **Hindistan** (dünyanın en büyük altın tüketicilerinden). YouTube'daki en büyük "gold crash" videoları Hint kanallarında [ölçüm: 759 K Telugu, 337 K Hintçe].
- **Kaynaklar:**
  - K1: [Gold Price in October 2026](https://pricegold.net/2026/october/) · PriceGold.net (günlük fiyat tablosu, son satır 2026-10-27) · tarih: 2026-10-27 · anahtar: 4,157
  - K2: [Gold Edges Lower as Dollar Strength Checks This Year's Historic Rally](https://political.org/2026/10/04/gold-edges-lower-as-dollar-strength-checks-this-years-historic-rally/) · Political.org · tarih: 2026-10-04 · anahtar: gold
  - K3: [Gold and Silver Prices Have Dropped Significantly](https://www.vol.at/gold-and-silver-prices-have-dropped-significantly/9963512) · VOL.AT · tarih: 2026-02-02 (Şubat düşüşü: Warsh adaylığı) · anahtar: Warsh
- **İlgi kanıtı [ölçüm]:** Wikipedia "Gold as an investment" günde 132 (düşük). YouTube "gold price crash 2026" alaka medyanı 49 K, Hint kanalları önde.
- **Hassas:** hayır. **Reklam:** YEŞİL. "Altın al/sat" yok, tavsiye dili riski var [tahmin].
- **Görselleştirme:** altın 2024–2026, reel faiz ile altın, 1980 zirvesi ile 2026 zirvesi (A12'ye köprü).
- **Neden izlenir:** "Güvenli liman" bir yılda nasıl %20 kaybettirdi?
- **Kaynak kalitesi notu:** Üç kaynak da ikincil ya da küçük yayıncı. B seçilirse birincil fiyat kaynağı (LBMA, World Bank) gerekir.

---

## 4. C — Gelecek senaryoları ("senaryo" diye sunulur, tavsiye değil)

### C1 — What if oil hits $150? A day-by-day scenario
- **Özet:** Goldman'ın yayımlanmış yukarı yönlü senaryoları (Körfez üretimi uzun süre düşük kalırsa 2027'de Brent >120 $ veya ~125 $) üzerinden kurgusal bir "150 $" stres senaryosu [kaynak K1, K2; 150 $ bizim varsayımımız, tahmin].
- **Neden şimdi:** Brent 110 $ (B2).
- **Global bağ:** Benzin, uçak bileti, gıda. Her ülke.
- **Kaynaklar:**
  - K1: [Brent Crude may hit $125 in 2027 if oil supply…](https://www.uniindia.com/business-economy/business-brent-crude-oil-supply-sachs/210889) · UNI India · tarih: 2026-10-12 · anahtar: 125
  - K2: [Could oil stay near US$100? Goldman Sachs just changed its forecast](https://www.fool.com.au/2026/09/08/could-oil-stay-near-us100-goldman-sachs-just-changed-its-forecast/) · The Motley Fool Australia · tarih: 2026-09-08 · anahtar: Goldman
  - K3: [ICYMI: Goldman flags $120 oil risk, lifts Brent and WTI forecasts](https://investinglive.com/commodities/icymi-goldman-flags-120-oil-risk-lifts-brent-and-wti-forecasts/) · investingLive · tarih: yok (erişim 2026-10-27) · anahtar: 120
- **İlgi kanıtı [ölçüm]:** "Iran war oil price" sorgusunda 1,47 M ve 730 K (2026). "Why The Oil Crisis is Way Worse Than You Think" 1,57 M.
- **Hassas:** **hassas** (savaş senaryosu). Kurgu gerçekçi sahte haber gibi görünmemeli (monetizasyon §3 "gerçekçi sahte olay").
- **Reklam [tahmin]:** SARI.
- **Görselleştirme:** fiyat → TÜFE aktarım zinciri, ülke başına benzin fiyatı haritası, 1973 / 2008 / 2026 karşılaştırması.
- **Neden izlenir:** "En kötü senaryoda hayatım nasıl değişir?" sorusu.

### C2 — What if the AI data-center boom stops? (the dark-fiber replay)
- **Özet:** 2000'lerin fiber yatırımının büyük kısmı yıllarca "karanlık" kaldı, Global Crossing 2002'de battı. AI veri merkezi borcu aynı yola girerse ne olur? [kaynak K1–K3; senaryo kısmı tahmin].
- **Neden şimdi:** B1 (CoreWeave).
- **Global bağ:** Teknoloji fonları, enerji talebi (veri merkezleri), istihdam.
- **Kaynaklar:**
  - K1: [Everyone's wondering if, and when, the AI bubble will pop](https://fortune.com/2025/09/28/ai-dot-com-bubble-parallels-history-explained-companies-revenue-infrastructure) · Fortune · tarih: 2025-09-28 · anahtar: fiber
  - K2: [Global Crossing](https://en.wikipedia.org/wiki/Global_Crossing) · Wikipedia · tarih: yok (erişim 2026-10-27) · anahtar: bankruptcy
  - K3: [CoreWeave Credit Default Swaps Signal Over 60% Default Risk](https://www.kucoin.com/news/flash/coreweave-credit-default-swaps-signal-over-60-default-risk) · KuCoin News · tarih: 2026-10-16 · anahtar: CoreWeave
- **İlgi kanıtı [ölçüm]:** Infographics "What if the AI Bubble Bursts (Day by Day)" **4,81 M** (2026-09-03). Talep kanıtlı, ama **aynı başlık kalıbı = `benzer_aci` cezası riski**. Özgün açı şart (ör. "fiber" ya da "elektrik şebekesi" merceği).
- **Hassas:** hayır. **Reklam:** YEŞİL [tahmin].
- **Görselleştirme:** fiber kullanım oranı 2001–2005, AI capex 2023–2026, "boş veri merkezi" kurgusal zaman çizelgesi.
- **Neden izlenir:** Herkesin konuştuğu AI patlamasının "durursa" ne olacağını tarihten bir prova ile gösterir.

### C3 — What if the dollar lost its crown? A reserve-currency scenario
- **Özet:** Dolar bugün dünya döviz rezervlerinin ~%58'i [kaynak K2]. Rezerv statüsü aşınırsa faiz, ithalat ve ABD borcu ne olur? Kurgusal senaryo [K1, K2; senaryo tahmin].
- **Neden şimdi:** ABD borcu ve "dollar reset" videoları yüksek izleniyor [ölçüm].
- **Global bağ:** Dolarla ithalat yapan her ülke (Hindistan, Türkiye), ABD tasarruf sahipleri.
- **Kaynaklar:**
  - K1: [The International Role of the U.S. Dollar – 2025 Edition](https://www.federalreserve.gov/econres/notes/feds-notes/the-international-role-of-the-u-s-dollar-2025-edition-20250718.html) · Federal Reserve Board (FEDS Notes) · tarih: 2025-07-18 · anahtar: dollar
  - K2: [Dollar Dominance Monitor](https://www.atlanticcouncil.org/programs/geoeconomics-center/dollar-dominance-monitor/) · Atlantic Council · tarih: yok (canlı sayfa, erişim 2026-10-27) · anahtar: dollar
  - K3: [Understanding the National Debt](https://fiscaldata.treasury.gov/americas-finance-guide/national-debt/) · U.S. Treasury Fiscal Data · tarih: yok (canlı sayfa, erişim 2026-10-27) · anahtar: debt
- **İlgi kanıtı [ölçüm]:** "US national debt crisis" alaka medyanı **745 K, 15'te 7 video ≥1 M**. 12 ayda: "How Did America Pay Off The National Debt Last Time?" 1,17 M, Infographics "What If The World Dumps US Debt?" 1,12 M, ProfSteveKeen "Dollar Reset" 945 K.
- **Hassas:** hayır. **Reklam:** YEŞİL. "Dollar collapse" korku/clickbait çerçevesi yanıltıcı başlık riski taşır [tahmin].
- **Görselleştirme:** rezerv payı 1999–2026, ABD borç/GSYH, faiz gideri ile savunma bütçesi.
- **Neden izlenir:** "Dünyanın parası dolar olmaktan çıkarsa cüzdanıma ne olur?" merakı. Talep kanıtı çok güçlü.

---

## 5. Elenenler (neden)
| Aday | Strateji | Neden elendi |
|---|---|---|
| Nixon şoku 1971 | S2 | YouTube alaka medyanı 105, 12 ayın en iyisi 7 K. Soyut konu, karakter gerilimi zayıf. A2 ve C3'e alt bölüm olarak girebilir |
| Volcker şoku 1979–82 | S2 | Ayrı konu yerine A2'nin 3. perdesi (Wikipedia 354/gün, YouTube 12 ay en iyi 2 K) |
| İzlanda bankacılık çöküşü 2008 | S2 | Talep zayıf: Wikipedia 129/gün, 12 ay en iyi 513 |
| Venezuela hiperenflasyonu | S2 | Süren insani kriz (hassas). 12 ay en iyi 66 izlenme. A11 aynı dersi daha güvenli veriyor |
| GameStop 2021 | S2 | Doymuş, ilgi düşüyor (Wikipedia −%12), 12 ay en iyi 1,3 K |
| Silicon Valley Bank 2023 | S2 | Sönüyor: Wikipedia 191/gün |
| 1997 Asya krizi | S2 | Bloomberg 1,57 M (Tayland) iyi, ama hedef kitle ülkelerine bağ zayıf. Sonraki tura |
| Panic of 1907 | S2 | Orta talep (Wikipedia 250/gün, 12 ay en iyi 59 K). Havuz sınırı. Yedek |
| Barings / Nick Leeson 1995 | S2 | Talep güçlü (ColdFusion 4,26 M, LADbible 524 K, 2026-01), ama bu turda **ikinci bağımsız açılan kaynak bulunamadı**. Sonraki turda ilk aday |
| John Law ayrı konu | S2 | A10'a birleştirildi (aynı yıl, ikiz balon) |
| Telekom/fiber balonu ayrı konu | S2 | A4 ve C2'ye birleştirildi. YouTube talebi ölçülemedi (sorgu medyanı 24) |
| Nifty Fifty | S2 | Talep yok (sorgu medyanı 70) |
| Bitcoin −%36 (Ekim 2026) | S1 | Kaynaklar yalnız kripto borsası blogları (KuCoin, Bitsgap). Güvenilir ikinci kaynak yok. Tanıtım riski |
| Özel kredi (private credit) krizi | S1 | Son 30 günde tarihli bağımsız 2 kaynak doğrulanamadı (stock3 Almanca, tarih belirsiz; Yahoo 2026-04). YouTube talebi güçlü (Plain Bagel 307 K, Mark Tilbury 560 K): kaynak bulunursa B adayı |
| SBF affı (Ekim 2026) | S1 | Ekim 2026 haberi yok. Son haber Haziran 2026. A8'e bağlam olarak girdi |

---

## Kontrol listesi (betikle)

Komut: `python3 uretim/2026-10-26-secim/01-arastirma/kaynak-kontrol.py uretim/2026-10-26-secim/01-arastirma/konu-havuzu.md --bugun 2026-10-27`
Kural: konu başına ≥2 farklı alan adı. Link testi = HTTP 200 + sayfa metninde anahtar kelime (soft-404 ve bot sayfası elenir; örnek: `federalreservehistory.org/essays/lehman-brothers` 200 döndürüp "Content Not Found" gösterdiği için çıkarıldı). B konularında ≥1 kaynak son 30 günden (2026-09-27 ve sonrası).

**Betik çıktısı (canlı, 2026-10-27, çıkış kodu 0):**

Kontrol tarihi: 2026-10-27 · konu: 23 · mod: canlı (curl + anahtar kelime)

| ID | Konu | Kaynak | Bağımsız alan | Açılan (200+anahtar) | Açılan bağımsız | Son 30 gün (B) | Sonuç |
|---|---|---|---|---|---|---|---|
| A1 | The 1929 Crash: Black Tuesday and the Great Depr | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A2 | The 1973 Oil Shock: when oil quadrupled and the  | 4 | 3 | 4 | 3 | — | GEÇTİ |
| A3 | Weimar Germany 1923: when a loaf of bread cost b | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A4 | The Dot-Com Bubble (through today's AI lens) | 4 | 4 | 4 | 4 | — | GEÇTİ |
| A5 | Railway Mania 1845–47: Britain's AI-bubble ances | 4 | 4 | 4 | 4 | — | GEÇTİ |
| A6 | Bernie Madoff: the $65 billion Ponzi scheme | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A7 | Enron: America's most admired company that was a | 4 | 4 | 4 | 4 | — | GEÇTİ |
| A8 | FTX: the $32 billion crypto empire that vanished | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A9 | Tulip Mania 1637: the first bubble (and the myth | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A10 | The South Sea Bubble 1720 (and John Law's Missis | 3 | 2 | 3 | 2 | — | GEÇTİ |
| A11 | Zimbabwe: the 100-trillion-dollar banknote | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A12 | The Hunt Brothers: cornering the world's silver  | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A13 | Japan's Bubble 1989: when Tokyo was worth more t | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A14 | Black Monday 1987: the day the market fell 22.6% | 3 | 3 | 3 | 3 | — | GEÇTİ |
| A15 | LTCM 1998: the Nobel-winning hedge fund that alm | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A16 | Black Wednesday 1992: the man who broke the Bank | 2 | 2 | 2 | 2 | — | GEÇTİ |
| A17 | Lehman Brothers 2008: the weekend that broke the | 3 | 3 | 3 | 3 | — | GEÇTİ |
| B1 | The AI credit scare: CoreWeave's crash and "is t | 3 | 3 | 3 | 3 | 3 | GEÇTİ |
| B2 | $110 oil + a Fed that's hiking again: is stagfla | 4 | 4 | 4 | 4 | 3 | GEÇTİ |
| B3 | Gold's 22% fall from its record: what just happe | 3 | 3 | 3 | 3 | 2 | GEÇTİ |
| C1 | What if oil hits $150? A day-by-day scenario | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C2 | What if the AI data-center boom stops? (the dark | 3 | 3 | 3 | 3 | — | GEÇTİ |
| C3 | What if the dollar lost its crown? A reserve-cur | 3 | 3 | 3 | 3 | — | GEÇTİ |

Sütun sayımı: A=17 · B=3 · C=3 · toplam=23
Kapı: GEÇTİ (her konuda >=2 bağımsız açılan kaynak; B'de >=1 kaynak son 30 gün; toplam >=15)

**Elle ek kontrol (betiğin ölçmediği):**
- [x] Uydurma kaynak yok: her link curl ile açıldı ve sayfada konu anahtar kelimesi bulundu (tablo).
- [x] B konularının tarihleri sayfa metadata'sından (`datePublished` / `article:published_time`) okundu: B1 2026-10-08/16/18 · B2 2026-09-16, 2026-10-12/17/19 · B3 2026-10-04/27 (+ 2026-02-02 bağlam).
- [x] Düzeltilen hatalar: Yahoo "Erik Gordon" yazısı 2025-08-15 tarihli çıktı (arama özeti güncel sanıyordu) → kullanılmadı. IBTimes CoreWeave yazısı 2025-12-16 (eski düşüş) → kullanılmadı. VOL.AT altın yazısı 2026-02-02 → yalnız Şubat bağlamı olarak etiketlendi. Fed History "lehman-brothers" sayfası 200 ama "Content Not Found" → çıkarıldı.
- [ ] Zayıf nokta: A11, A15 ve A16'da Wikipedia dışı tek kaynak var (2 bağımsız kapısı geçiyor, ama F3'te birincil kaynak eklenmeli). A10'da K3 (Wikipedia) K2 ile aynı yayıncı, bağımsız sayılmadı.
- [ ] B1 ve B3'te kaynaklar ikinci el (kripto haber sitesi, küçük yayıncı). B seçilirse F3'te Reuters/Bloomberg/LBMA gibi birincil kaynak şart.
- [x] Tüm sayılar [ölçüm] (API, 2026-10-27), [kaynak] ya da [arama özeti] / [tahmin] etiketli. "Doğrulanacak" yazan tarihsel rakamlar F3'te finans-dogrulayici'ye.

