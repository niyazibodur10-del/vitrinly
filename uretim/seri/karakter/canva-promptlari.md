# Flip By Vote · karakter + mekân Canva prompt paketi (v2, 2026-11-10)
İLERLEME: J-A + M-A KABUL (rapor.md) · sıradaki: koordinatör L1-A'yı üretir (aşağıdaki sıra) → gorsel-varlik-sanatcisi değerlendirir.
- **Kota: 12 hakkın 2'si kullanıldı (J-A, M-A); her istek 1 görsel döndürüyor (4 aday değil, koordinatör gözlemi).** Bu yüzden "4 adaydan seç" yok; her istek tek atış, kalanı yeniden deneme hakkından gider.
- **Bölüm 1 sırası (10 hak):** 3 L1-A → 4 L1-B → 5 T-J → 6 T-M → 7 AG-J → 8 AG-M → 9–12 yedek: (a) kalan öğeyi yeniden dene, (b) L1-C (önce KOD: L1-A tezgâh kırpımı + `buyut.py`), (c) GK-J göz kırpma, (d) D-A ikili.
- Bölüm 1 yalnız L1 THE KITCHEN kullanıyor (`../seri-incili.md` §2, `../bolum-001/metin.md` §4). Garaj (L4, bölüm 11+), driveway (L3), araba (L2) promptları hazır, sırası gelince üretilir. Eski K-A/K-B (masa) incil L1 ile değişti, kullanılmaz.
- Referanslar: Jake sayfası `MAHajKKbhbM`, Mike sayfası `MAHajPZXWbU` (imageReferences). Plakalar referanssız (sayfa referansı plakaya karakter sokar).
- Promptlar `araclar/prompt-uret.py` ile üretilir (kilitler tek yerde, birebir). `python3 -I araclar/prompt-uret.py canva-promptlari.md` → 27 prompt, 0 hata; `--negatif` → 4/4 bozulma yakalandı. Stüdyo adı yasak.

## 0. Kurallar (Leo deneyiminden taşınan, ölçülmüş)
- **Kimlik çapası = karakter sayfası; sonraki her poz "taban + EDIT … ONLY CHANGE …"** (Leo: sıfırdan 0,45, düzenleme 0,84–0,96).
- **Plakalar karaktersiz ve sayfasız.** Karakter = ayrı kesik (M4, `uretim/2026-10-28-yeni-video/05-gorsel/araclar/kes-m4.py`) + KOD bindirme. Tezgâh plakası: bel üstü kesik tezgâh arkasına oturur (alt gövde üretilmez).
- **Ekrana yazı/rakam üretilmez**; beyaz tahta boş gelir, "THE BOARD", "$100", ilan kartları, banknot KOD ile.
- Bakış düzenlemede değişmez; ikili kadrajda Jake solda (sağa bakar), Mike sağda (sola bakar) → tek çekim kesmelerinde birbirlerine bakarlar. Aynalama yasak.
- Telefon (Mike) ve kalem (Jake) prop'tur: kilide girmez, KOD katmanı veya düzenleme.

## 1. Bölüm 1 poz gerçeği (metin §4: Jake 10, Mike 10, ikili 3 poz istiyor)
10 hakla 23 poz üretilemez. Öneri (animasyon-yonetmeni ile): her karakter 1 konuşma tabanı (tezgâh arkası, bel üstü) + 2 ağız durumu + sayfadaki 6 ifade portresi (kameraya bakış anları S2/S8 ve tepki yakın planları) + KOD hareketi (punch-in, sarsıntı, eğilme = ölçek/kaydırma). Kollar bağlı, telefon uzatma, kalemle yazma gibi el pozları bölüm 1'de üretilmez: telefon/kalem prop'u kadraj altından KOD ile girer, yazı tahtada KOD ile belirir. Yedek haklar el pozuna değil tutarlılığa harcanır.

## 2. Tutarlılık testi ve eleme ölçütü (gelen her görsel)
**Hedef renkler = kabul edilen sayfaların ölçülen medyanı** (`araclar/sayfa-olcum.py`; kanonik kaynak artık sayfa, ilk taslak hex'leri değil):
| Öğe | Jake (J-A) | Mike (M-A) |
|---|---|---|
| Üst | lacivert hoodie #293347, gri bağcık, baskı yok | kırmızı #901B18 + siyah büyük kareli flanel, açık, kol dirsek altı kıvrık; beyaz tişört #E9E5E2 |
| Alt | bej chino #BCAB91, beyaz spor ayakkabı #E3DEDB | koyu indigo jean #2A3445, kahverengi bot #4C2E1F |
| Saç | koyu kahve #452E20, kısa, üst sağa | dağınık kestane-kumral #6B3F23, alna düşen |
| Yüz | kahverengi göz, kısa hafif sakal+bıyık, oval | mavi göz, sakalsız, yanak kızarıklığı, hafif kare |

**Kesin eleme (biri bile → ELE):** yanlış renk/kıyafet (ör. hoodie siyah/gri, flanel başka desen, kapüşon başta, kol kıvrık değil); yazı/logo/harf/rakam (1:1 + 2× kırpım); şapka/gözlük/saat/takı; Jake sakalsız veya dolgun sakallı; Mike'ta sakal; sayfada figürler arası kıyafet/saç farkı (ön-yan-arka ve 6 ifade aynı kişi değil); ekstra kişi; el/parmak bozukluğu ön planda; 2D/çizgi kontur veya fotogerçekçi stil; tanınır ünlü/var olan çizgi film karakteri benzerliği.
**Puanlama (geçenler arasında seçim):** kontrol listesi Jake 8 / Mike 8 madde (saç şekli, saç rengi, kaş, göz rengi, sakal durumu, üst giysi, alt giysi + ayakkabı, yüz oranı) tam puan şart; sonra (a) sayfa içi tutarlılık: 6 ifade kafası ↔ ön görünüm kafa HSV kor. (ortalama en yüksek kazanır), (b) ifadelerin okunurluğu (6/6 ayırt edilebilir), (c) arka görünümde kapüşon/flanel deseni doğru.
**Türev pozlar (taban, ağız, ikili) eşikleri:** sayfaya/tabana göre kafa hist kor. ≥0,84, ten ΔE ≤8, saç ΔE ≤10, giysi ΔE ≤8; ağız düzenlemesinde kafa merkez kayması ≤4 px ve ölçek farkı ≤%2 (yama oturmalı), ağız dışındaki yüz farkı (fark maskesi) yalnız ağız bölgesinde.
**İkili (D-A):** iki yüz kendi sayfasına kor. ≥0,80 (iki kişi tek üretimde, eşik bir basamak düşük), Mike Jake'ten hafif uzun, figürler değmiyor (ayrı kesilebilir).
**Plakalar:** gerçek boyut 9:16; kişi yok; yazı/logo/plaka yok (1:1 + 2× kırpım); orta %60 şerit y %35–85 boş (bel üstü kesik bindirme testi: T-J/T-M kesiği konulur, ölçek ve ışık uyumu göz incelemesi); alt %25 sakin; 4 plaka birbirine stil olarak uyumlu (aynı render dili, kontur yok; ilk seçilen G-A ile yan yana kontakt sayfada). `stil-olcum.py` 2D için ayarlı → 3D için ilk kabul edilen plaka değerleri taban alınır, diğerleri ±%25 içinde.
**Kontakt sayfası:** her öğe için referans sayfa + gelen görsel yan yana, elenenler gerekçeyle `uretim/seri/karakter/rapor.md`'ye; her dosyaya prompt ID + Canva media ID + üretim tarihi.

## 3. Konuşan sahne yaklaşımı (3D görünümlü stilde en düşük maliyet)
| Yol | Hak maliyeti (karakter başına) | Risk |
|---|---|---|
| **1. Aynı poz, ağız kapalı / yarı açık / açık + yama** | taban 1 + ağız 1 (istek 1 görsel döndürüyor → 2 durum: kapalı + açık; yarı açık = 2 karelik alfa karışımı) | Düzenleme ağız dışında yüzü de değiştirebilir (Leo'da bakış değişince 0,70); 3D gölgelendirmede yama sınırı ton basamağı yapabilir → Leo `rig-yama.py` (fark maskesi +11 px, Gauss 4,5) + gerekirse ten Lab eşleme. Yalnız bir kafa açısında konuşur; her yeni açı = 2 hak. |
| 2. Kafa + göz katmanı + ağız yaması (rig) | taban 1 + ağız 1 + göz 1 + kesme işi | 3D ışıkta boyun ekleminde dikiş ve gölge kopukluğu görünür; kafa döndürme 2D'deki gibi inandırıcı değil (perspektif sabit). Leo rig'i 2D düz renkte çalıştı, 3D'de en riskli yol. Kazanç az: kafa sallama KOD ile tüm kesiğe (hafif dönme/ölçek) zaten verilebilir. |
| 3. Yalnız kamera + altyazı + ifade değişimi | 0 ek (sayfadaki 6 ifade + sahne kesikleri) | Yakın planda konuşan ama ağzı kıpırdamayan yüz "ölü" görünür; Reels'te izleyici fark eder. Geniş plan, sırtı dönük, dinleyen tepki çekimi ve dış ses için sorunsuz. |

**Öneri: 1 + 3 karma.** Konuşan yakın plan yalnız T-J / T-M tabanıyla (2 durumlu ağız: kapalı + açık; ara kare alfa karışımı). Rhubarb eşlemesi: X, A → kapalı; B, C, E, F, G, H → yarı açık (yoksa açık); D → açık. Geçişte 2 karelik alfa karışımı. Her şeye "nefes" (ölçek %0,5 salınım) + konuşma vurgusunda kafa-kesik mikro dönme KOD ile. Diğer tüm çekimler yol 3: ikili/mekân geniş planlar, dinleyenin tepki ifadesi (sayfadan değil, gerekirse ifade düzenlemesi taban üzerinden). Bölüm başına ek hak = 0 (taban ve ağızlar tüm sezon tekrar kullanılır; değişen plaka ve kamera). Göz kırpma: 12. hak kalırsa GK-J; yoksa sonraki ay. Image-to-video (canlı ağız) ücretli olabilir → yalnız Niyazi onayıyla, burada planlanmadı.
Not: tek açı = dikey diyalogda karşılıklı kesme (Jake sola, Mike sağa bakar → yan yana kesmede birbirlerine bakarlar).

## 4. Promptlar (betik çıktısı; elle düzenleme yapma, `araclar/prompt-uret.py`'yi değiştir)
<!-- PROMPTLAR:BAŞ -->
### J-A · Jake sayfası · sıra 1 (dalga 1)
- aspectRatio: `LANDSCAPE_16_9` · referans: yok · not: tek görselde dönüş + 6 ifade (iç tutarlılık aynı üretimde) · 2126 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
CHARACTER MODEL SHEET of Jake Miller only, one character, nobody else. LAYOUT: left 40% of the image is a full-body turnaround in a relaxed neutral standing pose, arms down at the sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. Right 60% is a neat 3 x 2 grid of six head-and-shoulders portraits, all the same size and same front-facing angle, showing: neutral, warm smile, surprised, worried, excited, thoughtful (hand on chin only in thoughtful). Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. 16:9 landscape.
```

### M-A · Mike sayfası · sıra 1 (dalga 1)
- aspectRatio: `LANDSCAPE_16_9` · referans: yok · not: J-A ile paralel · 2206 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
CHARACTER MODEL SHEET of Mike Carter only, one character, nobody else. LAYOUT: left 40% of the image is a full-body turnaround in a relaxed neutral standing pose, arms down at the sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. Right 60% is a neat 3 x 2 grid of six head-and-shoulders portraits, all the same size and same front-facing angle, showing: neutral, warm smile, surprised, worried, excited, thoughtful (hand on chin only in thoughtful). Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. 16:9 landscape.
```

### J-B · Jake sayfası · sıra yedek-1 (J-A elenirse)
- aspectRatio: `LANDSCAPE_16_9` · referans: yok · not: bölünmüş yol: önce yalnız dönüş (yüz daha büyük), ifadeler sonra J-B2 düzenlemesiyle · 1958 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
CHARACTER MODEL SHEET of Jake Miller only, one character, nobody else. LAYOUT: full-body turnaround only, three figures side by side, large and evenly spaced, relaxed neutral standing pose, arms down at the sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. No expression portraits. Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. 16:9 landscape.
```

### J-B2 · Jake sayfası · sıra yedek-1 devamı
- aspectRatio: `LANDSCAPE_16_9` · referans: [J-B kazanan] · not: yalnız J-B seçilirse · 581 karakter
```
EDIT the reference image into an expression sheet of the same man: keep the same face, hair, stubble, navy hoodie, render style, background and lighting. Replace the three full-body figures with a neat 3 x 2 grid of six head-and-shoulders portraits, all the same size and front-facing angle, showing: neutral, warm smile, surprised, worried, excited, thoughtful (hand on chin only in thoughtful). Only the facial expression changes. No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. 16:9 landscape.
```

### M-B · Mike sayfası · sıra yedek-1 (M-A elenirse)
- aspectRatio: `LANDSCAPE_16_9` · referans: yok · not: J-B ile aynı mantık; ifadeler M-B2 = J-B2 metni, 'navy hoodie' yerine 'open buffalo-check flannel over white T-shirt' · 2038 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
CHARACTER MODEL SHEET of Mike Carter only, one character, nobody else. LAYOUT: full-body turnaround only, three figures side by side, large and evenly spaced, relaxed neutral standing pose, arms down at the sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. No expression portraits. Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. 16:9 landscape.
```

### J-C · Jake sayfası · sıra 3 (yalnız A ve B ikisi de kalırsa)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: dikey sayfa; figürler küçük → yüz ölçümü zayıf · 1969 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
CHARACTER MODEL SHEET of Jake Miller only, one character, nobody else. LAYOUT: top half is a full-body turnaround (front view, exact side profile facing right, back view, same height, one baseline); bottom half is a 3 x 2 grid of six head-and-shoulders portraits, same size and angle: neutral, warm smile, surprised, worried, excited, thoughtful. Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### M-C · Mike sayfası · sıra 3 (yalnız A ve B ikisi de kalırsa)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · 2049 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
CHARACTER MODEL SHEET of Mike Carter only, one character, nobody else. LAYOUT: top half is a full-body turnaround (front view, exact side profile facing right, back view, same height, one baseline); bottom half is a 3 x 2 grid of six head-and-shoulders portraits, same size and angle: neutral, warm smile, surprised, worried, excited, thoughtful. Same face, same hair, same outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### D-A · İkili · sıra 1 (dalga 2)
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajKKbhbM, MAHajPZXWbU] · not: boy/oran referansı + kesilebilir (zeminde ayrı iki figür) · 2763 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The first reference is Jake's model sheet, the second is Mike's model sheet; both faces, hair and outfits must match their sheets exactly.
SHOT: full-body two-shot of the two friends standing side by side facing the camera with a small gap between them (not touching, not overlapping): Jake on the left, hands in his hoodie pocket, small calm smile; Mike on the right, slightly taller, hands on his hips, big confident grin. Both full figures visible from shoes to hair with margin around them, feet on one baseline at 88% of the frame height.
BACKGROUND: plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### D-B · İkili · sıra 2
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajKKbhbM, MAHajPZXWbU] · not: diyalog iki-çekimi tabanı; D-A geçerse yalnız yedek hakla · 2596 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The first reference is Jake's model sheet, the second is Mike's; faces, hair and outfits must match exactly.
SHOT: waist-up two-shot, the friends standing shoulder to shoulder with a small gap, turned slightly toward each other, Mike on the right mid-laugh pointing a thumb at Jake, Jake on the left raising one eyebrow; heads at the same height band (top of heads at 20% of the frame), bodies continue past the bottom edge.
BACKGROUND: plain flat medium slate-blue background, evenly lit, no shadows on the background.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### D-C · İkili · sıra 3 (mekânlar kilitlendikten sonra, isteğe bağlı)
- aspectRatio: `PORTRAIT_9_16` · referans: [<G kazanan>, MAHajKKbhbM, MAHajPZXWbU] · not: 3 referans bağlayıcıda denenmedi (risk); afiş/tanıtım görseli · 2390 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The first reference is the garage set; keep the set, camera and light. The second and third references are Jake's and Mike's model sheets; faces, hair and outfits must match exactly.
SHOT: the two friends standing in the open center of the garage, Jake on the left, Mike on the right, full figures, facing camera.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-A · Garaj (incil L4, bölüm 11+) · sıra bölüm 11 öncesi
- aspectRatio: `PORTRAIT_9_16` · referans: yok · 1809 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the friends' home base: a lived-in suburban two-car garage seen from inside, looking toward a half-open roll-up garage door at the back that shows a sunny driveway and a strip of blue sky. Concrete floor with a few faint old oil stains. Left wall: long wooden workbench with a pegboard of hand tools, a clamp work lamp. Right wall: grey metal shelving with plain unmarked cardboard boxes and secondhand finds (an old bicycle, a vintage radio, a desk lamp, a box fan). Back left corner: a worn mustard-yellow armchair. A blank whiteboard leaning on the shelves. Center floor kept clear.
LIGHT: cool daylight spilling in from the garage door, warm light from the clamp lamp and a string of warm bulbs across the ceiling beams.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-B · Garaj (incil L4, bölüm 11+) · sıra bölüm 11 öncesi (B)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: plan/oy sahneleri için (beyaz tahtaya KOD yazı) · 1533 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the same kind of lived-in suburban garage, reverse angle: looking at the inner back wall with a long wooden workbench, a pegboard of hand tools, a large blank whiteboard mounted above the bench, plain unmarked cardboard boxes stacked at the sides, an old bicycle hanging on wall hooks, a worn mustard-yellow armchair at the right. Center floor kept clear.
LIGHT: cool fluorescent tube light from above, warm pool from a clamp lamp on the workbench.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-C · Garaj (incil L4, bölüm 11+) · sıra sonraki ay (gece sürümü)
- aspectRatio: `PORTRAIT_9_16` · referans: [G kazanan] · not: kriz/gece bölümleri; 12'lik pakete dahil değil · 421 karakter
```
EDIT the reference image. Keep the same garage, same camera, same objects and same 3D render style. ONLY CHANGE: it is night; the garage door shows a dark blue night sky, the warm ceiling bulbs and the clamp lamp are the main light, deeper cool shadows. No people. No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### P-A · Garage sale sokağı (incil L3) · sıra L3 gerekince (B)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · 1676 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a sunny American suburban residential street on a Saturday morning, seen from the sidewalk at eye level, the street and sidewalk receding into the distance. Modest one-story houses with trees; on several front lawns and driveways stand garage-sale folding tables full of secondhand items (table lamps, a toaster, vinyl records in plain sleeves, toys, old electronics, a clothes rack, a bicycle leaning on a table). Price stickers are blank colored dots. The sidewalk in the center is clear.
LIGHT: bright warm morning sun from the side, cool blue shade under the trees and on the far houses.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### P-B · Garage sale sokağı (incil L3) · sıra L3 gerekince ilk
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: pazarlık sahneleri (alıcı-satıcı) · 1525 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a single suburban driveway garage sale up close: an open garage behind, two long folding tables in an L shape covered with secondhand items (lamps, a toaster, an old game console with no logos, records in plain sleeves, a box of tools, a clothes rack), a blank cardboard sign on an easel, blank colored-dot price stickers. The driveway space in front of the tables is clear.
LIGHT: warm morning sun, cool blue shadow inside the open garage.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### A-A · Arkadaşların arabası (incil L2) · sıra bölüm gerektirince
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: iki koltuk iki-çekim; bel üstü kesikler koltuk önüne, alt gövdeyi ön konsol/direksiyon örter · 1631 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: inside the friends' old, well-loved compact car (a generic early-2000s hatchback, no brand badges), camera mounted on the dashboard looking back at the two empty front seats side by side, steering wheel at the lower left foreground edge, worn grey fabric seats with headrests, a coffee cup in the holder, a phone mount without a phone, a small crack in the dashboard plastic. Through the rear and side windows: a passing suburban street, slightly blurred.
LIGHT: warm late-afternoon sun through the side windows, cool shade inside the cabin roof.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### A-B · Arkadaşların arabası (incil L2) · sıra bölüm gerektirince (B)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: tek çekim (Mike sürerken) · 1476 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: inside the same kind of old compact hatchback (no brand badges), camera on the passenger side dashboard looking at the empty driver seat alone, steering wheel in the lower foreground, driver side window showing a passing suburban street slightly blurred, worn grey fabric seat, a coffee cup in the holder.
LIGHT: warm late-afternoon sun through the side window, cool shade on the roof liner.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### K-A · ESKİ mutfak masası (incil L1 ile değişti) · sıra kullanma
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: masa üstü kadraj %62–75'te (Leo dersi): bel üstü kesik masa arkasına oturur, 0 ek üretim · 1787 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a small rented apartment kitchen-dining nook in the evening, camera at seated eye level directly across a simple square wooden table: the tabletop runs across the bottom 30% of the frame and continues past the bottom edge; on it only a closed laptop at one side, two mugs and a notepad with blank pages. Behind the table the central area is open, no chairs visible there (seated characters will be composited later, their lower bodies hidden by the table). Background: compact kitchen counters with a few dishes, an open shelf with plain jars, a small window showing a dusky blue city sky with soft distant lights.
LIGHT: warm pendant lamp hanging above the table, cool blue dusk light from the window.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### K-B · ESKİ mutfak masası (incil L1 ile değişti) · sıra kullanma
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: kuruluş çekimi · 1490 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the same kind of small apartment kitchen-dining nook in the evening, establishing three-quarter high angle: a simple square wooden table with two mismatched empty chairs, a closed laptop, two mugs, a notepad with blank pages, compact kitchen counters, an open shelf with plain jars, a small window with a dusky blue city sky.
LIGHT: warm pendant lamp above the table, cool blue dusk light from the window.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### L1-A · L1 Mutfak · A geniş tezgâh ikili · sıra 1 (bölüm 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: S1, S3–S8; masa/tezgâh dersi: bel üstü taban kesiği tezgâh arkasına oturur · 1853 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a small, lived-in American apartment kitchen, the friends' home base, on a bright morning: muted blue-grey cabinets, a light wood countertop, a small window with soft morning sky and a fire escape outside, a tall white fridge with a large blank white dry-erase board on its door. Camera across the breakfast counter at standing chest height, straight-on. The countertop runs across the bottom of the frame and is clear except a ceramic mug and a small fruit bowl at the far left edge. Behind it: open kitchen floor space, the stove and cabinets, the window on the left, the fridge with the blank whiteboard at the right edge.
LIGHT: warm morning sun from the window, soft cool fill in the shadows.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; the front edge of the countertop sits at 68-72% of the frame height and the counter continues past the bottom edge; the central 60% of the width between 22% and 70% of the frame height is open kitchen space (two waist-up characters will be composited standing behind the counter, their lower bodies hidden by it); busy detail only at the sides and top; extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. The whiteboard is completely blank. Vertical 9:16 portrait.
```

### L1-B · L1 Mutfak · B buzdolabı tahtası · sıra 2 (bölüm 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: S2, S4 tahta; yazılar KOD (THE BOARD, $100, $1,000,000) · 1604 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a small, lived-in American apartment kitchen, the friends' home base, on a bright morning: muted blue-grey cabinets, a light wood countertop, a small window with soft morning sky and a fire escape outside, a tall white fridge with a large blank white dry-erase board on its door. Closer angle on the fridge: the fridge door fills the right half of the frame; the large blank white whiteboard is mounted on it with its top at 18% and bottom at 58% of the frame height, a marker on a small tray, a few plain round magnets. The left half is an open area of kitchen wall and counter edge where one waist-up character will be composited.
LIGHT: warm morning sun from the window, soft cool fill in the shadows.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level, straight-on to the fridge door (whiteboard not skewed, flat rectangle); bottom 25% of the frame is calm low-detail lower fridge and floor; extend the scenery past every edge.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. The whiteboard is completely blank. Vertical 9:16 portrait.
```

### L1-C · L1 Mutfak · C tezgâh insert · sıra 3 (önce KOD: L1-A tezgâh kırpımı + büyütme; yetmezse)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: S1 SLAM insert, S7 banknot yakın; banknot KOD · 1508 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: extreme close-up of the light wood countertop of small, lived-in American apartment kitchen, the friends' home base, on a bright morning: muted blue-grey cabinets, a light wood countertop, a small window with soft morning sky and a fire escape outside, a tall white fridge with a large blank white dry-erase board on its door. Low camera just above the counter surface, shallow depth of field: the counter surface fills the lower 60% of the frame with an empty clear spot in the center (a hand and a bill will be composited there later), a ceramic cereal bowl with a spoon at the right edge, the kitchen and window softly blurred behind.
LIGHT: warm morning sun from the window, soft cool fill in the shadows.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: keep the empty counter spot between 45% and 70% of the frame height, centered; extend past every edge.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. The whiteboard is completely blank. Vertical 9:16 portrait.
```

### T-J · Konuşma tabanı Jake · sıra 1 (dalga 2)
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajKKbhbM] · not: ÜRETİLDİ: kadraj soluna baktı → Jake ikilide SAĞDA, aynalanmaz · 1894 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
The reference image is the model sheet of Jake Miller; the face, hair and outfit must match it exactly.
SHOT: waist-up portrait of Jake Miller alone, body and head turned about 20 degrees toward frame-right, eyes looking toward frame-right at someone just off-screen at eye level, relaxed neutral expression, mouth gently closed, arms relaxed and out of frame below; top of the head at 18% of the frame height, body continues past the bottom edge, centered.
BACKGROUND: plain flat medium slate-blue background, evenly lit, no shadows on the background.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### T-M · Konuşma tabanı Mike · sıra 1 (dalga 2)
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajPZXWbU] · not: ÜRETİLDİ: kadraj soluna baktı → Mike AYNALANIR, ikilide SOLDA · 1972 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The reference image is the model sheet of Mike Carter; the face, hair and outfit must match it exactly.
SHOT: waist-up portrait of Mike Carter alone, body and head turned about 20 degrees toward frame-left, eyes looking toward frame-left at someone just off-screen at eye level, relaxed neutral expression, mouth gently closed, arms relaxed and out of frame below; top of the head at 18% of the frame height, body continues past the bottom edge, centered.
BACKGROUND: plain flat medium slate-blue background, evenly lit, no shadows on the background.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### AG-J · Ağız açık Jake · sıra 1 (dalga 3)
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajBqI-Qs, MAHajKKbhbM] · not: tek görsel: açık durum; yarı = agiz-yama.py optik akış ara karesi · 704 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Jake), same face, same hair, same navy hoodie with grey drawstrings, same stubble, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: mouth open mid-word in a relaxed talking shape: jaw dropped slightly, lips in a soft open oval, a little of the upper teeth visible, NOT smiling, NOT shouting; the rest of the face (eyes, eyebrows, cheeks) unchanged. No text, no logos. Vertical 9:16 portrait.
```

### AG-M · Ağız açık Mike · sıra 1 (dalga 3)
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajIzpXBs, MAHajPZXWbU] · 755 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Mike), same face, same hair, same open red-and-black buffalo-check flannel over the white T-shirt, rolled sleeves, clean-shaven face, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: mouth open mid-word in a relaxed talking shape: jaw dropped slightly, lips in a soft open oval, a little of the upper teeth visible, NOT smiling, NOT shouting; the rest of the face (eyes, eyebrows, cheeks) unchanged. No text, no logos. Vertical 9:16 portrait.
```

### GK-J · Göz kırpma Jake · sıra yedek-2
- aspectRatio: `PORTRAIT_9_16` · referans: [MAHajBqI-Qs, MAHajKKbhbM] · not: yedek hak kalırsa · 568 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Jake), same face, same hair, same navy hoodie with grey drawstrings, same stubble, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: both eyelids fully closed in a natural blink, eyebrows relaxed, mouth unchanged. No text, no logos. Vertical 9:16 portrait.
```
<!-- PROMPTLAR:SON -->
