# Kanal kimliği: banner ve profil fotoğrafı raporu

Hazırlayan: thumbnail-tasarimcisi, 2026-10-26. YouTube'da hiçbir şey değiştirilmedi ve para harcanmadı.
Etiketler: **[D]** doğrulanmış (kaynaklı veya bizim ölçümümüz), **[AÖ]** arama özeti / yaygın rehber, **[T]** tahmin veya yargı.

## Teslim
| Dosya | Boyut | Durum |
|---|---|---|
| `banner-2560x1440.jpg` | 2560x1440 JPEG, 423 126 bayt (≤6 MB) | kazanan A-s2 |
| `profil-800.png` | 800x800 PNG, 428 118 bayt | kazanan P4 |
| `onizleme/` | adaylar, bölge ve kırpma önizlemeleri, profil karşılaştırmaları, `olcumler.json` | |
| `tools/gorsel/kanal-gorselleri.py` | yeniden çalıştırılabilir; ad, slogan, ritim, karakter ve arka plan parametre | |
| `canva-promptlari.md` | isteğe bağlı Canva iyileştirmeleri (K1–K3) | |

Kaynak görseller: Canva paket-v1, `f-sevincli.png` (media `MAHZHh7qFXI`, banner) ve `a-konusma-kapali.png` (media `MAHZHqW0_Uo`, profil). Profil kırpması Real-ESRGAN x4 ile büyütüldü. Metinler kodla yazıldı (Anton, Fredoka 700; `video/public/fonts`).

## Kısıtlar
- **[D]** YouTube Yardım "Manage your channel branding" (support.google.com/youtube/answer/10456525, 2026-10-26 okundu): yükleme için en az 2048x1152 ve 16:9; "at the minimum dimension, the safe area for text and logos: 1235 x 338 px"; TV için önerilen 2560x1440; ≤6 MB; gölge, kenarlık veya çerçeve gibi dosya süslemesi eklenmemeli. Profil: JPG/GIF/BMP/PNG, ≤15 MB, "renders at 98 X 98 px".
- **[D, hesap]** Güvenli alan 2560 tuvale ölçeklenince 1235x338 × 1,25 = 1544x423. Yaygın kullanılan 1546x423 değeri ile örtüşüyor. Betik 1546x423 kullanıyor: x 507–2053, y 508–931.
- **[AÖ]** Diğer kırpmalar yardım sayfasında yok; yaygın tasarım rehberlerinden alındı: masaüstü 2560x423 (tam genişlik, orta bant), tablet 1855x423, TV tam tuval. 800x800 profil önerisi de yardım sayfasında yok (sayfa yalnız 98 px gösterimi veriyor).

## Banner: adaylar ve testler
Her aday 2 sloganla denendi: s1 "Money stories, animated." / s2 "Past crashes. Today's news. What's next.". Ritim: "NEW VIDEOS TUE · FRI · SUN". Bu ritim `docs/yayin-takvimi.md` v1'den alındı ve oradaki takvim [T] etiketli. Takvim değişirse `--ritim` ile yeniden üretilir.

| Aday | Kompozisyon | Güvenli alan taşması | Kafa bantta | Metin kontrastı, en kötü %5 (WCAG) [D] | Mobilde ad / slogan / ritim yüksekliği (390 CSS px) [D] | Karar |
|---|---|---|---|---|---|---|
| **A-s2** | karakter solda (sevinçli), şehir ve yükselen grafik, metin sağda | yok | evet (632,530–956,779) | ad 13.55 · RISE 11.05 · slogan 12.43 · ritim 11.95 | 34.8 / 12.1 / 11.6 px | **KAZANAN** |
| A-s1 | aynı, kısa slogan | yok | evet | 13.55 · 11.05 · 12.23 · 11.95 | 34.8 / 15.9 / 11.6 | yedek |
| B-s1/s2 | karakter sağda, metne işaret ediyor | yok | evet | 17.08 · 10.24 · 15.25–16.0 · 11.95 | 31.8 / 11.1–15.9 / 11.6 | **ELENDİ** |
| C-s1/s2 | minimal logo-tipi, karakter yok | yok | – | 17.08 · 11.05 · 11.9–16.85 · 11.95 | 36.8 / 15.9 / 11.6 | **ELENDİ** |

Ölçüm yöntemleri:
- Kontrast: metin dolgu rengi ile metin kutusunun 12 px çevresindeki zemin pikselleri karşılaştırıldı (metin pikselleri hariç). Pikseller arasındaki en kötü %5'lik dilim raporlandı.
- Taşma: her metin kutusu, ritim hapı ve kafa kutusu güvenli alanla karşılaştırıldı.
- Dosya boyutları 0,32–0,42 MB arası.

Eleme gerekçeleri:
- **B:** işaret eden elin ucu y=1006'da, yani mobil ve masaüstü bandının (y ≤931) dışında **[D]**. Bu cihazlarda jest görünmüyor; geriye bağlamsız bir yarım kol kalıyor. Eli banda almak için karakteri küçültmek gerekiyor, ama o zaman bel kesiti havada kalıyor.
- **C:** ölçümleri temiz, ancak maskot yok. Kanalın ayırt edici yanı ekranda anlatıcı maskot (`docs/rakip-analizi.md` §6). Thumbnail'larla görsel bağ kurmuyor **[T]**.
- **s1 → s2:** s2 üç sütunu (Geçmiş / Bugün / Gelecek) tek satırda anlatıyor; s1 yalnız formatı söylüyor. s2 mobilde 12.1 CSS px, belirlediğim ≥11 px eşiğinin üstünde **[T, eşik yargı]**. s1 daha büyük (15.9 px); okunurluk önceliklendirilirse `--slogan-alt` yerine s1 seçilebilir.

Tasarım sırasında düzeltilen sorunlar:
1. RGBA görsele doğrudan yarı saydam çizgi çizmek karışım yapmıyor; ızgara düz beyaz çıktı. Ayrı katmana alınarak düzeltildi.
2. Yükselen grafik metnin arkasından geçiyordu (slogan en kötü %5: 1.94). Grafik metnin altına indirildi (12.43).
3. Yumruklar bandın alt kenarında yarım görünüyordu. Karakter büyütülerek (boy 1140 px, tuvalin altından taşar) yumruklar bant dışına indirildi; böylece kafa da büyüdü.
4. Kare MaxFilter konturu basamaklıydı. Dairesel çekirdeğe geçildi.

Kırpma önizlemeleri: `onizleme/banner-*-bolgeler.jpg` (bölge çizgili tam görünüm) ve `onizleme/banner-*-kirpmalar.jpg`. İkincisi TV, masaüstü (1284 px), tablet, mobil (390 CSS px gerçek boy) ve mobil ×3 görünümlerini içerir.

## Profil: adaylar ve testler
Ölçüm, 800 px görselde daire içinde yapıldı **[D]**. 98 px ve 36 px önizlemeleri açık ve koyu temada: `onizleme/profil-karsilastirma.png`, `onizleme/profil-tema-acik-koyu.png`.

| Aday | Tanım | Ten–zemin WCAG / ΔE76 | Saç ve gömlek–zemin WCAG | Daire kenarı, açık / koyu tema WCAG | 36 px gözlem [T] | Karar |
|---|---|---|---|---|---|---|
| **P4** | yeşil zemin, beyaz yükselen çizgi, yakın plan yüz | 1.11 / 91.9 | **9.63** | 1.94 / 9.89 | yüz ve saç silueti net; akışta en dikkat çeken daire | **KAZANAN** |
| P1 | lacivert zemin, sıcak ışık, altın halka | **6.68** / 85.2 | 1.21 (krem kontur kurtarıyor) | 1.55 / 12.4 | yüz net, daire koyu temada halka sayesinde seçiliyor | yedek |
| P2 | "FR" monogramı ve ok | (ölçüt uygun değil; altın R ten sayıldı) | – | 17.08 / 1.12 | ok harflerin üstünden geçiyor, 36 px'te harfler karışıyor; koyu temada daire kayboluyor | ELENDİ |
| P3 | P1 ve ok rozeti | 6.68 / 85.2 | 1.24 | 1.55 / 12.4 | rozet 36 px'te yaklaşık 10 px; okunmuyor, bildirim noktasına benziyor | ELENDİ |

Kazanan gerekçesi: küçük boyutta şekil tanıma büyük ölçüde parlaklık kenarlarına dayanır **[AÖ, görme bilimi genel kabulü]**. P4'te koyu saç ve gömlek siluetinin zemine karşıtlığı 9.63:1. Ten ile zemin arasında parlaklık farkı az (1.11), ama renk tonu farkı çok büyük (ΔE 91.9). Ayrıca yeşil daire hem açık hem koyu temada kenarını koruyor. P1 marka laciverti ile daha uyumlu ve güçlü bir yedek. İlk kırpmada yüz dairenin yaklaşık üçte biriydi ve 36 px'te seçilmedi. Kırpma 0.62'den 0.47 karakter boyuna sıkılaştırıldı; yüz şimdi dairenin yaklaşık %45'i (ten piksel oranı 0.445).

## Kanal adı parametresi (koordinatör notu üzerine)
- `--ad` parametresi eklendi; ad metni kodda sabit değil. Çok kelimeli adlarda son kelime altın, tek kelimelik adlarda tamamı altın. Monogram (P2) baş harflerden üretiliyor.
- Betik ad için tek satırı ve kelime sınırındaki tüm iki satırlık bölmeleri dener, her birini banda sığdırır, en büyük yazıyı seçer (eşitlikte tek satır). Önce ad küçültülür, slogan korunur.
- Test edilen adlar **[D]** (`onizleme/ad-uzunluk-testi-mobil.jpg`): "MONEYX" (6 karakter), "COIN STORY" (10), "FINANCIAL RISE" (14), "THE MONEY TIMELINE X" (20). Hepsinde taşma yok. Mobilde ad yüksekliği sırasıyla 38.6 / 38.6 / 34.8 / 23.0 CSS px; slogan her durumda 12.1 px.
- Yeni ad gelince: `--ad "<YENİ AD>" --kazanan-banner A-s2 --kazanan-profil P4`. Profil (P4) ad içermediği için değişmez.

## Riskler ve açık konular
- Ritim satırı (TUE · FRI · SUN) takvim v1'e bağlı [T]. Takvim değişirse banner yeniden üretilmeli.
- Kaynak karakter görseli 1680x944'ten büyütülmüş. Banner'da ölçek yaklaşık 1.06 olduğundan sorun yok. Profilde Real-ESRGAN kullanıldı; daha keskin profil için Canva K3 isteğe bağlı.
- Kırpma bölgeleri (masaüstü, tablet) [AÖ]. YouTube Studio'nun yükleme önizlemesi kesin sonucu gösterir. Yükleme öncesi orada göz kontrolü önerilir (Niyazi onayıyla).
- Profil fotoğrafı API ile değiştirilemiyor (`mevcut-durum.md`); Studio'dan Niyazi yükler. Banner `channelBanners.insert` ile yüklenebilir, ama yalnız onayla.
