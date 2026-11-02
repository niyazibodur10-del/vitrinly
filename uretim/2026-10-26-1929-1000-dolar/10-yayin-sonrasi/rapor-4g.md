# F12 yayın sonrası, ara rapor (4,5 gün): BVJwZ1C9R1U "You Have $1,000 in 1929. Can You Keep It?"

İLERLEME: tamam (sıradaki iş 7 g raporu `performans-7g.md`, 2026-11-04 16:00 UTC sonrası; 28 g raporu 2026-11-25 sonrası)
Hazırlayan: kanal-analisti · **Ölçüm: 2026-11-02 04:22 UTC** [API] · ham veri `olcum/olcum-2026-11-02.json` (betik `olcum/olc.py`)

**ÖZET (ilk 10 satır)**
- 4,5 günde **203 görüntüleme, 1 beğeni, 0 organik yorum, kanal 3 abone** [API]. Bu, ~1.165'lik başa baş hedefinin **%17'si** [H: 203 ÷ 1.165].
- Hız ~45 görüntüleme/gün [H: 203 ÷ 4,5]. Doğrusal gitse bile 28. günde ≤~1.260 olur (üst sınır). İlk günlerden sonra düşüş olağan olduğu için gerçekçi aralık **~400–800** [T].
- Genç niş rakiplerin ilk uzun videosu (bugünkü ömür boyu izlenme, n=14): **medyan 2.853**. 14 kanalın 3'ü 203'ün altında, 9'u 1.165'in üstünde [API][H]. Kıyas bize karşı yanlı (bkz. §3).
- **CTR, gösterim, AVD, tutma eğrisi, trafik kaynağı, Test & Compare: ÖLÇÜLEMEDİ.** `yt-analytics.readonly` kapsamı yok, Studio CSV de gelmedi.
- YPP: 3/1.000 abone. Herkese açık uzun video izlenme saati ölçülemedi; tahmini ~10–17 saat / 8.000 [T: 203 × 3–5 dk].
- Karar: tek videoyla format kararı verilmez. Sinyal zayıf ama kırmızı değil. Asıl eksik veri; 7 g raporundan önce Studio CSV şart.

## 1. Veri yolları (2026-11-02)
| Yol | Sonuç | Ne verdi |
|---|---|---|
| YouTube Data API v3 (`YOUTUBE_API_KEY`) | Çalışıyor | izlenme, beğeni, yorum, abone, rakip ilk videoları (≈40 kota birimi) [API] |
| YouTube Analytics API | Erişim yok: token yalnız `youtube` kapsamlı | — |
| Niyazi'nin Studio CSV'si / ekran görüntüsü | Gelmedi | — |
| WebSearch / üçüncü taraf siteler | Gerekmedi (kendi kanalımız için 3. taraf veri anlamsız) | — |

## 2. Kendi video (ölçüm 2026-11-02 04:22 UTC)
| Metrik | Değer | Etiket |
|---|---|---|
| Görüntüleme | 203 | [API] |
| Beğeni / görüntüleme | 1 / 203 = %0,5 | [API][H] (genel referans %2–4 [ÖB], düşük) |
| Yorum | 1 = kendi sabit yorumumuz (09:44 UTC); organik yorum 0, yanıt 0 | [API] |
| Kanal abone | 3 | [API] |
| Kanal toplam izlenme | 203: gizli eski 4 video sayılmıyor, tamamı bu videodan | [API] |
| Herkese açık video sayısı | 1 (Shorts 1/2 henüz açık değil: planlı 2 ve 3 Kasım) | [API] |
| Süre | 10:32 (≥10 dk kuralı tuttu) | [API] |
| `publishedAt` | 2026-10-28 09:37:48Z. Planlanan yayın 16:00 UTC'ydi. API bu alanda yükleme anını gösteriyor olabilir; gerçek yayın anı **ölçülemedi**. Yaş hesabı 16:00'dan yapıldı | [API][T] |
| Gösterim, CTR, AVD, izlenme %, ilk 30 sn tutma, düşüş noktaları, trafik kaynakları, abone kazanımı (video bazında), Test & Compare | **ölçülemedi** | — |

## 3. Rakip ilk-video kıyası [API: playlistItems + videos, 2026-11-02]
Örneklem: `rakip-veri-2026-10-27.json` içinde 2025-05 sonrası açılmış ve ≥1.000 abonesi olan 16 kanal. Elenenler: Finance Bureau (yükleme listesinin sonuna ulaşılamadı), HinExp (Hintçe). Kalan n=14.

| Kanal (açılış) | İlk uzun video | Süre | İzlenme (bugün) |
|---|---|---|---|
| Wealth Chronicles (2026-06) | 2026-06-21 | 14 dk | 30 [API] |
| History Unburied (2026-09) | 2026-09-29 | 4 dk | 59 [API] |
| The Money Files (2025-11) | 2025-11-26 | 30 dk | 134 [API] |
| Money and Marker (2026-03) | 2026-06-09 | 9 dk | 538 [API] |
| Histonom (2025-12) | 2026-01-01 | 8 dk | 1.044 [API] |
| Financial Dynasty (2026-01) | 2026-03-29 | 18 dk | 1.496 [API] |
| Dial-Up Days (2025-08) | 2025-09-04 | 12 dk | 2.694 [API] |
| Marcus Explains (2026-07) | 2026-07-13 | 29 dk | 3.012 [API] |
| Markets of the Past (2026-04) | 2026-04-18 | 28 dk | 5.054 [API] |
| Truth Vault (2025-10) | 2026-05-27 | 20 dk | 5.182 [API] |
| Drowsy Historian (2025-05) | 2025-05-16 | 127 dk | 19.726 [API] |
| Who Gets Paid (2025-07) | 2026-07-27 | 19 dk | 35.709 [API] |
| Global Decline Explained (2025-09) | 2026-03-23 | 14 dk | 275.225 [API] |
| Uncover Things (2026-03) | 2026-08-12 | 26 dk | 323.790 [API] |

- Medyan: ilk video 2.853, ilk 3 video 2.946 [H].
- **Yanlılık 1:** onların sayısı aylarca birikmiş ömür boyu izlenme, bizimki 4,5 günlük.
- **Yanlılık 2 (hayatta kalan):** örneklem sonradan büyüyen kanallardan seçildi. Silinmiş videolar ve büyümemiş kanallar listede yok.
- Bu yüzden 203 "geride" anlamına gelmez. Aynı yaşta kıyas ölçülemedi (Data API geçmiş izlenme vermiyor).
- Desen [H, zayıf kanıt]: büyük ilk videolar 14–29 dk süreli. Kısa (4–9 dk) ilk videolar alt yarıda. Bizim 10:32 alt sınırda. Bu korelasyon, nedensellik değil.

## 4. Yorumlar
- Organik yorum yok. Yanıt taslağı gerekmiyor. `09-paket/yorum-yanitlari.md` hazır bekliyor.
- **youtube-paketleyici'ye not:** sabit yorum iki soru soruyor ("hangi kapı + neden tek cümle" ve "sıradaki kriz"). 203 görüntülemede 0 yanıt [API]. Sonraki videoda tek, tek kelimeyle yanıtlanabilir soru kullanılmalı (A/B/C) [T, n=1].

## 5. YPP ilerlemesi (monetizasyon-uyum-uzmani → `docs/ypp-hazirlik.md`)
| Ölçüt | Hedef | Şimdi | Etiket |
|---|---|---|---|
| Abone | 1.000 | 3 | [API] |
| Herkese açık uzun video saati (12 ay; Shorts akışı saatleri sayılmaz) | 8.000 | ölçülemedi; ~10–17 saat | [T: 203 × 3–5 dk ÷ 60] |
| Video başı başa baş görüntüleme | ~1.165 (4 dk AVD) | 203 (4,5 g) | [API] / docs/monetizasyon.md |

## 6. Sonraki video için 3 ders (n=1, analitik yok → hepsi zayıf kanıt)
1. **youtube-paketleyici:** sabit yorum ve kapanış CTA'sında tek, tek dokunuşla yanıtlanan soru kullan ("A, B or C?"). İki soru ve "neden" istemek 0 yanıt getirdi [API: 0/203].
2. **thumbnail-tasarimcisi (+ Niyazi, YAYIN.md):** Test & Compare'i yayın anında 3 varyantla başlat ve sonucu 7. günde ekran görüntüsüyle kaydet. CTR olmadan thumbnail kararlarımız tamamen kalibrasyonsuz; bu videonun T&C durumu bilinmiyor.
3. **senaryo-yazari / kurgu-editoru:** beğeni oranı %0,5 [API][H]. Doruk sonrası ilk açıklama anında ekranda kısa bir "like if you'd have picked the shoebox" etkileşim anı dene (abone ol animasyonuyla çakışmasın). Etkisini 2. videoda beğeni/görüntüleme ile ölç.
- Tekrar kuralı: hiçbiri henüz 2 videoda tekrarlanmadı, `ortak-dersler.md`'ye taşınmadı.

## 7. Erişim engelleri ve kalibrasyon
- **viralite-analisti'ne kalibrasyon girdisi:** bu videonun son viralite puanı ile 4,5 g = 203 görüntüleme, beğeni %0,5. CTR/AVD olmadan model kalibrasyonu yalnız görüntüleme ekseninde yapılabilir. 7 g sayısını bekle.
- **Koordinatöre (uretim-muhendisi + Niyazi):** 7 g raporu 2026-11-04 16:00 UTC'den sonra yazılacak. O rapordan önce iki yoldan biri lazım: (a) `yt-analytics.readonly` kapsamıyla tek seferlik yeniden yetki, (b) Niyazi'nin Studio → Analytics → "Advanced mode" → dışa aktarımı (CSV), içinde Reach (gösterim, CTR), Engagement (AVD, tutma) ve trafik kaynakları.

## Test
Etiket testi (satır içi python, §2–§5 sayılı tablo satırları): ilk koşu 14 etiketsiz (rakip tablosu) → [API] eklendi → 0. `grep -c AIza olcum/olcum-2026-11-02.json` → 0.
