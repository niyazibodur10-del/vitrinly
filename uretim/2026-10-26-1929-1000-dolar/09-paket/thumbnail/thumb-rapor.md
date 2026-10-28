# F8 — Thumbnail raporu · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Hazırlayan:** thumbnail-tasarimcisi · 2026-10-27 · **Durum:** 3 finalist hazır (Test & Compare)
**Üretim:** `thumb-uret.py` (tüm adaylar + ölçüm) → `thumb-test.py <rakip_klasörü> A2 B1 D1` (OCR, mobil sayfa, rakip yan yana, benzerlik). İki koşu aynı sha256 (A2 585152d2…, B1 0dac58ad…, D1 72fab445…).
**Yeni Canva üretimi: 0.** Yalnız mevcut kabul edilmiş varlıklar; metin, "?", damga, zincir/kilit, karartma kodla. AI-assisted illüstrasyon (açıklama satırı paket-taslak'ta zaten var).
Etiketler: **[Ö]** betik ölçümü · **[T]** yargı.

## Finalistler (Test & Compare: tek değişken thumbnail, başlık sabit T1)

| # | Dosya | Açı | Metin | Kaynak (Canva media ID) |
|---|---|---|---|---|
| 1 | `A2-kapilar.jpg` | obje / oyun | ONE IS A **DISASTER** | C01 stüdyo `MAHZMVzdpqQ` + Leo `c-isaret` `MAHZHgRhWHs` (ekran soluna işaret = kapılar) |
| 2 | `B1-kutu.jpg` | duygu (yakın yüz) | THE **SURPRISE** DOOR + kutuda "1929" damgası | C01 bulanık (kahve kapı yakın) + Leo `C14` kutu `MAHZMtnkERI` gövdesi + `d-saskin` `MAHZHqQmUTY` kafası (aynı kadraj, kafa satırları ±3 px; yaka çizgisinde yumuşak geçiş) |
| 3 | `D1-kilitler.jpg` | bahis / sonuç (S17) | EVERY DOOR **LOCKED** | C01 yeşil+kahve kapıya punch-in `MAHZMVzdpqQ` + kod zincir/asma kilit + Leo `d-saskin` `MAHZHqQmUTY` |

Başlıkla okunuş: "Can you keep it?" + A "biri felaket → hangisi?" · B "sürpriz kapı kutu mu, neden?" · D "her kapı kilitli → kutu bile mi?". Hiçbiri başlığı tekrar etmiyor, cevabı (kutu kazandı) vermiyor.
Doğruluk: A = videonun kendi cümlesi (S01 "one is a disaster"); B = S11 "DOOR 3" / hook "one is a surprise", 1929 yıl çapası; D = 8:42 bölüm adı "March 1933: Every Door Locked", S17'de üç kapıya zincir + kilit iniyor. Bugüne dönük hüküm, gerçek kişi, logo, gerçek banka adı, kan/felaket görüntüsü yok. Leo kaybeden değil (H2): şaşkın/işaret eden sunucu.

## Test kapısı [Ö]

| Ölçüt | A2 | B1 | D1 | Eşik |
|---|---|---|---|---|
| Boyut / dosya | 1280x720, 131 KB | 1280x720, 110 KB | 1280x720, 144 KB | ≤2 MB ✅ |
| Kelime | 4 | 3 + "1929" = 4 | 3 | ≤4 ✅ |
| 168x94'te büyük harf yüksekliği (en küçük) | 14,2 px | 16,3 px | 14,0 px (LOCKED 22,6) | ≥9 ✅ |
| OCR 168x94 (tesseract, x4 büyütme) | 4/4 | 1/1 (tam boyutta da 1/3 → araç sınırı, göz kontrolü okunur) | 3/3 | tam boyutta okunanın %100'ü ✅ |
| Kontrast dolgu ↔ kontur (WCAG) | 18,8 / sarı 13,0 | 18,8 / 13,0 | 18,8 / 13,0 | ≥4,5 ✅ |
| Kontrast dolgu ↔ kontursuz zemin, en kötü %5 | 4,71 (DISASTER) | 12,2 | 5,42 (LOCKED) | ≥4,5 ✅ |
| Sağ alt süre damgası alanında metin | 0 px | 0 px | 0 px | 0 ✅ |
| Yüz yüksekliği (≥216 px) | ≈259 px | ≈292 px | ≈314 px | ✅ |

- "1929" damgası (B): kutu üstünde ikincil çapa; medyan kontrast 3,78, mobil 9,4 px (sınırda; ana metin değil).
- Mobil kontrol sayfası: `test/mobil-168x94-finalist.png` (168x94 + gri ton + 1,2 px bulanık "kısık göz"); adaylar `test/mobil-168x94-adaylar.png`. Ölçüm dökümü `test/olcum-adaylar.json`, OCR `test/ocr-168x94-*.json`.
- **Rakip yan yana:** 10 rakip outlier (i.ytimg.com mqdefault, 2026-10-27; repo DIŞI, scratchpad) arasında masaüstü ızgara + mobil liste, başlıkla. Göz kontrolü: rakiplerin hiçbirinde karakter + kapı/oyun dili yok; Marcus Explains parlak çok-nesneli çizgi, Markets of the Past siyah-beyaz portre + uzun metin. Bizimkiler ayrışıyor [T]. Sayısal (`test/rakip-benzerlik.json`): en yakın rakibe renk farkı 93–108, dHash 19–27; rakiplerin kendi aralarındaki medyan 112,5 → renk ölçüsü ayrışmayı tek başına kanıtlamıyor (üçümüz de koyu lacivert). Risk: koyu tema akışında koyu thumbnail daha az öne çıkar → F12'de CTR'a bakılmalı.
- Finalistler arası ayrışma (Test & Compare için): renk farkı 76–107, dHash 29–36 (en yakın çift A2–D1, aynı stüdyo).

## Elenenler

| Aday | Neden |
|---|---|
| A1 "PICK A DOOR" | Görsel zaten "kapı seç" diyor, bilgi eklemiyor; A2 bahsi ekliyor (OCR ikisi de tam). |
| B2 "EVERYONE LAUGHED" | Şaşkın yüzle çelişen duygu; 168'de OCR tam boyutta okunanı kaybetti (0/1). |
| **C konsepti (C1 "STOCKS −89%", C2 "THE −89% DOOR")** — finalistten çıkarıldı | Çapa verisiyle (FRH-29: 63 → 381,17 → ~190,6 → 41,22) çizilen Dow çizgisi küçükte "dağ/üçgen" okunuyor, çöküş hissi zayıf; 1. kapının cevabını veriyor; "düşen borsa grafiği" nişin genel kalıbı. C2 168'de OCR 0. Yerine D üretildi. |
| D2 "MARCH 1933" | Genel izleyiciye merak yaratmıyor; 168'de "1933" OCR'da kayboldu. |
| D3 "EVERY BANK CLOSED" | Doğru (6 Mart 1933, FDIC-BH3) ama oyun dilinden çıkıp gerçek dünya alarmı gibi okunuyor; bugünkü haber sanılma / sansasyon riski. D1 videonun kendi bölüm adını kullanıyor. |

İlk turda yapılan düzeltmeler: A'da Leo eli zemini gösteriyordu → parmak ucu kapılara ölçülerek yerleştirildi; Anton'un dar boşluğu 168'de kelimeleri birleştiriyordu (OCR "ONES A") → boşluk 0,32 em, A2 OCR 2/4 → 4/4; D'de zincir/kilit metnin arkasından geçiyordu (p5 1,29 / 1,1) → metnin altına alındı (5,42); A üst bandına lacivert gradyan (DISASTER p5 4,43 → 4,71).

## Riskler / devir
- monetizasyon-uyum-uzmani (F8): D1 "EVERY DOOR LOCKED" bölüm adı ve S17 sahnesiyle aynı, kontrol edilsin. B1'de kafa değişimi = aynı karakterin kendi pozlarının birleşimi (yeni AI üretimi yok).
- F7 render kareleri gelince isteğe bağlı: aynı kompozisyonlar render karesiyle değiştirilebilir; şart değil (varlıklar videodakilerin aynısı).
- Önerilen Test & Compare sırası: A2, B1, D1 (başarı ölçütü: Studio izlenme süresi payı).
