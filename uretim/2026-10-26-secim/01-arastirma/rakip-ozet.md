# F1 rakip özeti: animasyonlu / anlatımlı finans tarihi (sütun A, kanalın ilk herkese açık videosu)

Hazırlayan: kanal-analisti · **Ölçüm tarihi: 2026-10-27** (aksi yazılmadıkça her sayı bu tarihte ölçüldü) [API].
Ham veri: `uretim/2026-10-26-secim/01-arastirma/rakip-veri-2026-10-27.json` (51 kanal, 89 outlier satırı).

## 0. Durum, kaynak ve etiketler

- **`docs/rakip-analizi.md` güncellenmedi:** tarihi 2026-10-26, yani 1 günlük (kural: 14 günden eskiyse güncellenir). Bu dosya video için odaklı özet. **Not:** v1'in hiç API verisi yoktu ve artık geçersiz iki varsayım taşıyor: Türkçe dil ve "aktif" sayılan kanallar. API'ye göre Business Casual, OverSimplified, The Swedish Investor ve MagnatesMedia **son 12 ayda hiç uzun video yayınlamadı** [API]. Erken yenileme önerilir; karar koordinatörde (§7).
- **Kendi veri: yok.** Kanalda herkese açık video yok (eski 4 video gizli). 7/28 gün raporu çıkarılamaz [API: kendi kanal, 2026-10-27].
- **Veri yolları (2–3 yol denendi, hepsi 2026-10-27) [API][ALT][GÖZ]:**

| Yol | Sonuç (2026-10-27) | Ne için kullanıldı |
|---|---|---|
| YouTube Data API v3 (`YOUTUBE_API_KEY`) | **Çalışıyor.** `channels`, `playlistItems` ve `videos` sorunsuz. `search` 15 sorgudan sonra **429 "Search Queries per day"** verdi (ayrı bir günlük arama tavanı var; aynı proje trend-avcisi ile paylaşılıyor olabilir [T]) | Abone, izlenme, süre, son 20 video, medyan, outlier |
| i.ytimg.com thumbnail | HTTP 200, erişiliyor [GÖZ] | 20 outlier thumbnail'i görsel inceleme |
| yt-dlp otomatik altyazı (youtube.com) | **Kısmen.** 8/10 video "en-orig" altyazısı indi [ALT]. Sonra 429 ve "Sign in to confirm you're not a bot" | İlk 30 sn hook metni |
| WebSearch / üçüncü taraf siteler | Bu iş için gerekmedi | — |

- **Etiketler:** **[API]** Data API ölçümü (2026-10-27) · **[H]** API sayılarından hesap · **[ALT]** yt-dlp otomatik altyazı (2026-10-27) · **[GÖZ]** thumbnail görsel incelemesi (hqdefault, 2026-10-27) · **[T]** tahmin · **[ÖB]** ön bilgi, ölçülmedi.
- **Outlier tanımı [H]:** video izlenmesi ÷ kanalın son 20 uzun videosunun (≥4 dk, 2026-10-20 öncesi) medyanı. İzlenme ölçüm anındaki toplamdır, yani eski videolar avantajlı. Son 7 günde yayınlananlar medyana katılmadı.
- **Örneklem [API]:** 15 niş araması (son 12 ay, uzun video, izlenmeye göre) → 175 kanal + 12 kanal tanıdığından elle eklendi. Her kanaldan son 50 yükleme alındı: toplam 6.436 video, harcanan ≈1.900 kota birimi. Desen istatistikleri, Hintçe ve konu dışı kanallar çıkarılarak 39 İngilizce finans/ekonomi-tarih kanalının **son 12 ayda yayınlanan 1.123 uzun videosu** üzerinden.

## 1. Son 12 ayın niş outlier'ları (İngilizce, finans/ekonomi-tarih; ≥3x ve ≥20 bin izlenme) [API][H]

| Video | Kanal (açılış, abone) | Yayın | Süre | İzlenme | Kanal medyanı | Skor |
|---|---|---|---|---|---|---|
| How America Replaced Britain as the World's Economic Superpower | Histonom (2025-12, 2,7 B) | 2026-01-06 | 13,2 dk | 185.295 | 154 | 1.199x |
| The Family That Owns Most of London (Grosvenor Family) | Financial Dynasty (2026-01, 3,4 B) | 2026-04-02 | 18,8 dk | 348.957 | 432 | 807x |
| Who Actually Pays For The World Cup? (Follow The Money) | Money and Marker (2026-03, 1,7 B) | 2026-06-25 | 17,7 dk | 129.697 | 469 | 276x |
| The Balkan Economic Trap No One Ever Escapes | The Money Files (2025-11, 4,8 B) | 2026-01-16 | 21,5 dk | 106.805 | 1.200 | 89x |
| The Great Depression of 1929: When the Dream Collapsed | SLICE History (301 B) | 2025-11-02 | 51,4 dk | 540.465 | 15.775 | 34x |
| What Happens If Trump Loses The Midterms? | Finance Bureau (2025-10, 129 B) | 2026-10-16 | 19,1 dk | 3.252.388 | 97.095 | 34x |
| The Real Reason Hitler Never Invaded Switzerland | Markets of the Past (2026-04, 99,9 B) | 2026-10-18 | 30,9 dk | 1.318.152 | 96.274 | 14x |
| The Economics of Money Laundering | Marcus Explains (2026-07, 30 B) | 2026-08-11 | 25,1 dk | 507.814 | 37.816 | 13x |
| The Real Reason Japan Attacked Pearl Harbor | Markets of the Past | 2026-09-04 | 31,9 dk | 873.206 | 96.274 | 9,1x |
| The 2008 Financial Crisis Explained Like You're 5 | Fred - Money Historian (5,1 B) | 2026-03-04 | 36,1 dk | 245.402 | 50.559 | 4,9x |
| The 'Buy Now Pay Later' Trap Is Getting Worse | Grant Rudow (156 B) | 2026-03-21 | 15,6 dk | 2.719.794 | 562.255 | 4,8x |
| The True Origin of The Great Depression: What Historians Get Wrong | Markets of the Past | 2026-07-09 | 25,3 dk | 422.497 | 96.274 | 4,4x |
| Why A National Debt Default Now Looks Genuinely Possible… (sort of) | How Money Works (1,76 M) | 2026-09-07 | 18,6 dk | 3.083.675 | 768.019 | 4,0x |
| We (Still) Don't Know How Epstein Got So Rich… | How Money Works | 2026-01-14 | 23,0 dk | 3.052.775 | 768.019 | 4,0x |
| The Real Origins of the Great Depression: What Historians Get Wrong | Uncover Things (2026-03, 5 B) | 2026-08-15 | 29 dk | 198.705 | 3 videoluk kanal, medyan anlamsız | — |

Büyük kanalların taban çizgisi [API]: Economics Explained medyan 638.286 (son 12 ayda ≥3x videosu yok, en iyisi 2026'dan önceki NZ videosu, 3,66 M) · How Money Works 768.019 · Moon 611.630 · The Infographics Show 420.083.

## 2. En önemli 5 desen (her biri ≥2 örnekli; tek örnekliler "zayıf kanıt")

### D1. Tarih olayı + "bildiğin yanlış" açısı tutuyor, ama yalnız ünlü olayda [API][H]
- Örnekler: Markets of the Past, Great Depression 422 B ve 1929 Crash 222 B · Uncover Things, Great Depression 199 B (3. videosu) ve Reformation "It Started in a Bank" 317 B (1. videosu) · Markets of the Past, Pearl Harbor 873 B.
- **Uyarı (doygunluk):** Aynı kalıp kanalın rutini olunca skor düşüyor. "Real reason / true origin / get wrong / never taught" geçen başlıklar: n=119, 12 kanal, **medyan skor 0,55**; geri kalan başlıklarda 1,02 [H]. Kalıp kanalı **açtı**, ama tekrarı tek tek videoları taşımıyor.
- Aynı thumbnail ve başlık kalıbıyla küçük konu düşük kalıyor: "True Origin of Income Tax" 12.809 · "Panic of 1907" 17.897 · "Central Banking" 47.026 → "Great Depression" 422.497 ve "Civil War" 567.162 [API]. **Çıkarım:** olay adı herkesin bildiği olmalı (1929, 2008, Weimar). Kurumsal veya niş konu ilk video için zayıf.

### D2. Klasik çöküş konularında arz taşmış, ama talep 1929'da yoğun [API][H]
- Başlık anahtar kelimesine göre veri setindeki uzun videolar (her dönem):

| Olay | n (12 ayda) | Medyan skor | ≥2x | En iyi örnek |
|---|---|---|---|---|
| 1929 / Great Depression | 39 (35) | 1,10 | 15 | SLICE 540 B · Markets of the Past 422 B |
| 2008 krizi | 31 (29) | 1,10 | 11 | Fred - Money Historian 245 B |
| Rockefeller / Morgan / Rothschild / Medici | 34 (30) | 1,85 | 16 | (12 ay İngilizce) Markets of the Past, Rothschild 33,6 B |
| Tulip mania | 17 (17) | 1,00 | 4 | İngilizce en iyisi 3.444 |
| Hiperenflasyon (Weimar / Zimbabwe) | 6 (5) | 0,65 | 0 | Markets of the Past, Weimar 38,9 B |
| FTX / SBF | 7 (5) | 0,60 | 0 | 12 ayda en iyisi 164 |
| Madoff / Ponzi | 18 (14) | 0,85 | 3 | — |
| Enron | 4 (4) | 1,75 | 2 | hepsi <1 B |
| Japonya balonu | 3 | 1,00 | 0 | <500 |
| South Sea / John Law | 3 | 1,10 | 0 | <50 |

- **Okuma:** Tulip, FTX, Enron, Theranos, South Sea ve John Law küçük yapay zekâ üretimi "2D Animation" kanallarıyla dolu ve bunlar onlarca, yüzlerce izlenmede kalıyor. **Arz doygun, talep kanıtı yok** [H]. 1929 ve 2008 ise hem kalabalık hem 100 bin+ kazanan çıkarıyor. **Fark açıda:** kazananlar "bilinen hikâye yanlış" ya da "bugünle bağ" kuruyor ("1929 Pattern Is Back", The Money Files 22.351, 18,6x).
- Talep sinyali (12 ay, bugünle bağ): AI balonu ve dot-com karşılaştırması (Infographics 610.622, 1,5x · New Money "Big Short investor… AI Bubble" 4,34 M, 28x) [API]. Tarih + güncel köprü, A sütununda bile ek talep getiriyor.

### D3. Yeni kanallar ilk 6 videoda bir kırılma yakalıyor; sürmesi kalıbın ünlü konularla tekrarına bağlı [API]
| Kanal (açılış) | İlk 5 video izlenmesi | Kırılma | Sonra | Abone (2026-10-27) |
|---|---|---|---|---|
| Markets of the Past (2026-04-10) | 4.816 · 3.535 · 23.092 · 3.096 · 2.561 | 3. video ilk "True Origin" (23 B), **6. video** WWI 302 B | Kalıp + ünlü olaylar ×100 video | 99.900 |
| Marcus Explains (2026-07-06) | 2.887 · 14.211 · 9.692 · 6.135 · 3.071 | **6. video** "The Economics of Money Laundering" 508 B | "Economics of X / How X makes money" kalıbı | 30.000 |
| Uncover Things (2026-03-30) | 317.334 (1.) · 4.147 · 198.705 | **1. video** | 3 videoda durdu | 4.990 |
| Financial Dynasty (2026-01-03) | 1.494 · **348.957** · 1.337 · 918 · 2.165 | 2. video (Grosvenor) | "The Family That…" tekrarı tutmadı (Arnault 1.337, Rothschild 2.165) | 3.420 |
| Histonom (2025-12-24) | 1.044 · 2.880 · 262 · 13.606 · 224 | **6. video** 185 B | Sonraki videolar yüzlerde | 2.700 |
| Dimeline (2026-07-25) | 1.053 · 660 · 3.589 · 3.479 · 602 | yok | "Entire History of X" | 98 |

- **Çıkarım [H]:** 6 yeni kanalın 5'inde ilk 6 video içinde ≥100 B'lik bir video çıktı. Ama bu kanallar arama sonuçlarından seçildi (**hayatta kalan yanlılığı**, kırılmayan kanalları göremiyoruz [T]). Kırılmanın aboneye dönüşmesi, kazanan **başlık mekanizmasının büyük konularla** tekrarına bağlı: Markets 99,9 B, Marcus 30 B; tek vuruşlu kanallar 2,7–5 B.
- **Abone dönüşümü [H]:** 1.000 izlenme başına abone: Markets 8,4 · Marcus 7,1 · Financial Dynasty 9,3 · Histonom 11,0 · Economics Explained 7,5 · How Money Works 5,8 (toplam izlenme ÷ abone, [API]). Kabaca **1.000 abone ≈ 90–170 bin izlenme** [H]. YPP için abone eşiği, tek bir 100 B+ vuruşla erişilebilir.

### D4. Thumbnail: iki aile, ikisi de "tek özne + tek kanıt nesnesi" [GÖZ]
- **Aile 1 — belgesel portre** (Markets of the Past ×5, Uncover Things ×2; 199–873 B): solda siyah-beyaz gerçekçi tarihî yüz (Hoover, Wilson, Yamamoto, Luther), sağda yıpranmış harita veya gazete ve **kırmızı oklar / düşen grafik**, altta beyaz kutulu 2 katmanlı metin. **Metin uzun: 6–11 kelime** (ör. "THE TRUE ORIGIN OF THE GREAT DEPRESSION: WHAT HISTORIANS GET WRONG"). v1'deki "≤4 kelime" [ÖB] kuralıyla çelişiyor. Kısa varyant da var: "1929 WASN'T THE REAL CAUSE" (4 kelime, 199 B).
- **Aile 2 — çizgi karakter + sayı** (Financial Dynasty 349 B: tek çizgi karakter + konak + "WHO OWNS LONDON?" 3 kelime · Marcus Explains 508 B: doodle karakter + nakit valizi + 5 etiketli rakam · Money and Marker 130 B: 6 rakam kutucuğu ($7.5B, 12 of 14…)). Renk: koyu lacivert/mavi zemin + sıcak vurgu.
- Ortak: renk sayısı az (siyah-beyaz + **kırmızı** vurgu, ya da mavi + sarı/kırmızı); 1 yüz; yüz ifadesi ciddi veya şaşkın. **Maskot olan outlier yok** → Leo'nun tekrar eden yüzü bu nişte boşluk (fırsat ve risk: kanıtı yok [T]).
- Zayıf karşı örnek: aynı Aile 1 şablonu, küçük konuda 12.809 (Income Tax). Thumbnail şablonu tek başına yetmiyor.

### D5. Hook: ilk 30 sn'de "yaygın inanç → ters köşe" ya da "somut sahne"; tempo hızlı konuşma [ALT]
- **Mit düzeltme (n=3):** "Most people think they know how the Great Depression started… That story is dangerously incomplete… The crash was a symptom" (jwmdk6-X6LM, 422 B) · "Most people think they know why Japan attacked Pearl Harbor…" (B-KUG2U1k60, 873 B) · "Here is something that makes almost no sense…" (36J1tL9ulGA, 1,3 M).
- **Somut sahne, ikinci tekil hitap (n=3):** "Walk down any street in Mayfair… there's a very good chance all of it belongs to one family" (YAyJWVRqMKE, 349 B) · 1846 Skibbereen kulübesi (YWOqTHIlOos, 231 B) · 72.000 kişilik statta 100 seyirci (aq1fOuoF9bA, 130 B).
- **Rakamla açılış (n=1, zayıf kanıt):** "A money launderer charges about 8% on every dirty dollar… catches less than 1%" (5lpKA72DQmo, 508 B).
- **Konuşma hızı [H]:** ilk ~30 sn'de 88–113 kelime (7 video) ≈ **175–225 kelime/dk**. Tek yavaş örnek SLICE (54 kelime, müzikli atmosfer, 540 B). Bizim TTS hızı (`am_fenrir` 0,9) ölçülüp bu bantla karşılaştırılmalı → ses-yonetmeni [T].
- **Ölçülemedi:** sahne değişim temposu (video indirilmedi, skill kapsamı dışı), tutma eğrisi (rakip için erişilemez).

## 3. Süre [API][H]
- 12 ay, 39 kanal, 1.123 video. Uzunluğa göre medyan skor: 4–10 dk 0,73 · **10–15 dk 1,11** · 15–20 dk 1,00 · 20–30 dk 1,00 · 30+ dk 0,92. Outlier'ların medyan süresi 23,2 dk, tümü 21,8 dk.
- Medyanı ≥1.000 olan 21 kanala bakınca 10–15 dk'da ≥3x oranı %1, 20–30 dk'da %14. Ama **kanal içi karşılaştırmada** <15 dk ile ≥15 dk arasında tutarlı bir fark yok: 8 kanaldan 4'ünde kısa video daha iyi, 4'ünde daha kötü (ColdFusion 1,16 / 0,90 · How Money Works 1,22 / 1,04 · Who Gets Paid 0,08 / 0,92 · Wall Street Millennial 0,53 / 0,71). Havuzdaki fark kanal etkisi [H].
- **Sonuç:** 10–14 dk hedefi için ceza kanıtı yok. Nişin kazananları ise 17–32 dk. Watch-hour (YPP) için ileride 15–18 dk denenebilir [T] (karar monetizasyon-uyum-uzmani ve senaryo-yazari'nın).

## 4. Başlık kalıpları (12 ay, 1.123 video) [H]

| Kalıp | n / kanal | Medyan skor | ≥3x oranı | Diğerleri: medyan / ≥3x |
|---|---|---|---|---|
| "Economics of X / How X (actually) makes money / Inside the X" | 44 / 7 | **1,91** | **%36** | 0,98 / %16 |
| "Rise and fall / collapse / died / bankrupt" | 60 / 22 | 1,36 | %23 | 0,97 / %16 |
| "Explained" | 52 / 19 | 1,09 | %29 | 0,98 / %16 |
| "What if / What happens if" | 11 / 6 | 1,09 | %18 | — |
| "Family / empire / dynasty / fortune" | 93 / 18 | 1,13 | %15 | — |
| "Real reason / true origin / get wrong" | 119 / 12 | 0,55 | %15 | 1,02 / %17 |
| "Entire history / in N minutes" | 33 / 8 | 0,89 | %18 | — |
| Soru işareti | 134 / 25 | 0,91 | %11 | 1,00 / %17 |

Medyanı ≥1.000 olan kanallarla tekrarlanınca sıralama korunuyor: "Economics of" 1,91 / %38 · "Collapse" 1,59 / %24 · "Real reason" 0,49 · "Family" 0,57 · soru işareti 0,88 [H]. Uyarı: "Economics of" kalıbının çoğu tek kanaldan (Marcus Explains), bu yüzden kanal etkisi karışık.

## 5. Bu video için öneri (senaryo-yazari / viralite-analisti / thumbnail-tasarimcisi / youtube-paketleyici)
1. **Konu [H, D1–D2]:** herkesin bildiği büyük çöküş (1929, 2008, Weimar hiperenflasyonu). Tulip, FTX, Enron ve South Sea ilk video için **doygun arz** (D2).
2. **Açı [H, D1/§4]:** "bilinen hikâyenin yanlış kısmı" veya **mekanizma** ("who actually paid / how the money moved"). Ama başlıkta rakiplerin birebir kalıbı kullanılmaz (§6).
3. **İlk 30 sn [ALT, D5]:** somut sahne veya yaygın inanç → ters köşe. İkisi de Leo'nun ikinci tekil hitabıyla uyumlu.
4. **Thumbnail [GÖZ, D4]:** tek özne (Leo) + tek kanıt nesnesi (düşen grafik / gazete / banka kapısı) + **tek vurgu rengi** (kırmızı). Metin kısa tutulur (yine 168×94 testi). Uzun metinli Aile 1, A/B (Test & Compare) varyantı olarak denenebilir.
5. **Seri düşüncesi:** kırılma çoğu kanalda ilk 6 videoda geldi. Kazanan mekanizmayı (açı + başlık tipi) büyük konularla tekrar edebilmek için ilk 6 video **farklı açı tiplerinde** denensin (D3) [T].

## 6. Kopyalamama: desen → bizim karşılığımız
| Rakip deseni | Yapma | Bizim özgün karşılığımız |
|---|---|---|
| "The True Origin of X: What Historians Get Wrong" (Markets of the Past) | Aynı başlık iskeleti, siyah-beyaz portre + beyaz kutu şablonu | Leo'nun "dosyayı yeniden açması": soru başlıkta değil hook'ta. Başlık mekanizmayı söyler (ör. "The Loan That Turned 1929 Into a Depression" [T, örnek]) |
| "The Economics of X" (Marcus Explains) | Aynı kalıp ve doodle karakter | "Follow the dollar": Leo bir doları olay boyunca takip eder (tarih sütununa uygulanmış mekanizma anlatısı) |
| "The Family That Owns…" | Aynı aile serisi | Kişi yerine **nesne/kurum** çapası (banka kapısı, borsa bandı) |
| Siyah-beyaz yüz + kırmızı ok | Aynı kompozisyon | Leo (renkli, sıcak) + soğuk tarihî zemin: kanal stil kararıyla tutarlı, maskot nişte boşluk |
| "Most people think…" açılışı | Aynı cümle | Leo'nun kendi yanılgısıyla açılış ("I used to believe…") ya da somut sahne |

## 7. Riskler ve açık noktalar
- **Hayatta kalan yanlılığı:** yeni kanal örnekleri arama sonuçlarından. Kırılmayan yüzlerce kanal görünmüyor [T]. D3 "mümkün" diyor, "olası" demiyor.
- **Yapay zekâ kanalları seli [API başlık taraması; politika etkisi T]:** doygun konulardaki küçük kanalların çoğu "2D Animation / AI Animation" etiketli. YouTube'un "inauthentic / seri üretim" politikası açısından bu kalabalığa benzememek gerekiyor (monetizasyon-uyum-uzmani'na girdi; politika ölçümü bu raporda yok).
- **Ölçülemeyenler [ALT kapsamı 8 video]:** sahne temposu, rakip tutma ve CTR, ilk 30 sn tutma. Hook tipi 8 transkriptle sınırlı.
- **API arama tavanı [API 429, 2026-10-27]:** `search` günlük sorgu limiti 15 sorguda doldu. Event aramaları yapılamadı; D2 bunun yerine veri setindeki 6.436 videonun başlık taramasıyla yapıldı. Sonraki ölçümlerde `search` yerine `playlistItems` + kanal listesi kullanılmalı (1 birim).
- **v1 rakip analizi [API]:** 5 "seçilmiş" kanaldan 3'ü (Business Casual, OverSimplified, Swedish Investor) son 12 ayda uzun video yayınlamamış. Yeni aday kanallar: Markets of the Past, Marcus Explains, How Money Works, Moon, Economics Explained. Erken yenileme (API'li v2) önerilir; karar koordinatörde.

## 8. Test (kapı: her sayının kaynağı ve ölçüm tarihi var)
Betik: `uretim/2026-10-26-secim/01-arastirma/etiket_test.py` (üst bilgide ölçüm tarihi 2026-10-27 olmalı; rakam içeren her satırda ya da bağlı olduğu başlıkta [API|H|ALT|GÖZ|T|ÖB] etiketi aranır; tablo başlık satırları atlanır).

```
$ python3 uretim/2026-10-26-secim/01-arastirma/etiket_test.py uretim/2026-10-26-secim/01-arastirma/rakip-ozet.md
1. koşu: rakamlı satır 81, etiketsiz 13 → etiketler eklendi
son koşu: rakamlı satır 81, etiketsiz 0   → GEÇTİ
```
- [x] Erişim engelleri bölümü güncel (§0, 2026-10-27: API search 429, yt-dlp bot kontrolü).
- [x] Her desen ≥2 örnekli. Tek örnekli olan (rakamla açılış hook'u) "zayıf kanıt" etiketli.
- [x] Ham veri JSON'da; API anahtarı dosyalarda yok (`grep -c AIza` → 0).
- [ ] Sahne temposu ve rakip tutma: ölçülemedi (§7).
