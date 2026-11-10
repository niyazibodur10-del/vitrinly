# Flip By Vote · karakter + mekân Canva prompt paketi (v1, 2026-11-10)
İLERLEME: prompt paketi tamam · sıradaki: koordinatör dalga 1'i Canva'da üretir → gorsel-varlik-sanatcisi kontakt sayfası + eleme (`uretim/seri/karakter/rapor.md`).
- **Kota planı: 11 istek + 1 yedek = 12** (her istek ~4 aday). Sıra: Dalga 1 = J-A, M-A, G-A, P-A, A-A, K-A (6, birbirinden bağımsız) → Dalga 2 = D-A, T-J, T-M (3) → Dalga 3 = AG-J, AG-M (2) → 12. hak: ilk kalan öğenin B varyantı (öncelik: sayfa > taban > plaka > göz kırpma GK-J).
- **İlk Canva'ya gidecek iki prompt: J-A ve M-A** (aşağıda aynen). Referans yok, aspectRatio `LANDSCAPE_16_9`.
- Promptlar elle değil `araclar/prompt-uret.py` ile üretildi: kilit blokları (JAKE/MIKE/STYLE) tek yerde, her promptta birebir. Kontrol: `python3 -I araclar/prompt-uret.py canva-promptlari.md` → 0 hata; `--negatif` → 4 bozulma yakalandı.
- Stil: özgün stilize 3D animasyon filmi görünümü; promptlarda stüdyo/film adı YOK (betik yasaklar). Gerçek kişi/ünlü benzerliği yasak cümlesi her karakter promptunda.

## 0. Kurallar (Leo deneyiminden taşınan, ölçülmüş)
- **Kimlik çapası = karakter sayfası; sonraki her poz "taban + EDIT … ONLY CHANGE …"** ile üretilir. Leo'da sıfırdan kilit prompt kafa korelasyonu 0,45 verdi (yasak), düzenleme 0,84–0,96.
- **Plakalar karaktersiz ve sayfasız** üretilir (sayfa referansı plakaya karakter sokuyor — Leo dersi). Karakter = ayrı kesik (M4 kesme, `uretim/2026-10-28-yeni-video/05-gorsel/araclar/kes-m4.py`) + KOD bindirme.
- **Ekrana yazı/rakam üretilmez**; tabela, fiyat etiketi, beyaz tahta boş gelir, yazı Remotion'da KOD ile eklenir (izleyici adı kartı dahil).
- Bakış düzenlemede değişmez ("same eye direction"); aynalama yasak (Jake'in saç ayrımı sağa, aynalanınca kimlik kayar).
- Taban pozlarda düz slate-blue zemin (M4 Lab anahtarıyla temiz kesim); sayfa ve ikilide açık gri zemin.

## 1. Kota ve dalga planı (en fazla 12 istek)
| # | ID | Ne | Referans | Bağımlılık |
|---|---|---|---|---|
| 1 | J-A | Jake sayfası (dönüş + 6 ifade) | yok | — |
| 2 | M-A | Mike sayfası | yok | — |
| 3–6 | G-A, P-A, A-A, K-A | 4 mekân plakası 9:16 | yok | — (dalga 1'de paralel) |
| 7 | D-A | İkili tam boy, 9:16 | Jake + Mike sayfası | 1, 2 |
| 8–9 | T-J, T-M | Konuşma tabanı (bel üstü, 9:16, ağız kapalı) | ilgili sayfa | 1, 2 |
| 10–11 | AG-J, AG-M | Ağız açık düzenlemesi | [taban, sayfa] | 8, 9 |
| 12 | yedek | Kalan ilk öğenin B varyantı; hiçbiri kalmadıysa GK-J (göz kırpma) | — | — |

Karar kuralları: sayfa (J-A/M-A) 4 adaydan biri ölçütü geçmezse 12. hak J-B/M-B'ye (bölünmüş yol; B2 ifade düzenlemesi bir hak daha ister → o durumda D-A ertelenir, T-J/T-M dönüş görünümünden üretilir). İkisi de kalırsa ESKALASYON (C varyantı sonraki ay hakkıyla). Plaka B/C varyantları ve G-C (gece) bu 12'nin dışında, sonraki bölümlerin hakkıyla.
Çıktı boyutu: dikey doğal boyut büyük olasılıkla 944x1680 [tahmin: yatay 1680x944'ün aynası, ilk üretimde `get-assets` ile doğrulanır]. Tam boy için 1080x1920 dikey export tuvali gerekir (`tools/gorsel/canva-indir.md` yöntemi; `resize-design` ile mevcut tuvalden, AI hakkı harcamaz) → uretim-muhendisi/koordinatör. Karakter ≥2048 px için export sonrası `tools/karakter/buyut.py`.

## 2. Tutarlılık testi ve eleme ölçütü (gelen her aday)
Hedef renkler (Lab ΔE ölçümü, `tools/gorsel/tutarlilik.py`; sayfa seçildikten sonra hedef = seçilen sayfanın ön görünümü):
| Öğe | Jake hedef | Mike hedef |
|---|---|---|
| Üst | lacivert hoodie ≈ #1F2B47, gri bağcık, baskı/logo yok | kırmızı ≈ #B3272D + siyah büyük kareli flanel, açık; beyaz tişört ≈ #F2F2F0 |
| Alt | bej chino ≈ #CDB48E, beyaz düz spor ayakkabı | koyu indigo jean ≈ #23314D, kahverengi bot |
| Saç | kısa koyu kahve ≈ #3B2A20, üst sağa taranmış | dağınık kumral ≈ #A07A4E, alna düşen |
| Yüz | kahverengi göz, hafif kısa sakal+bıyık, oval yüz | mavi göz, sakalsız, hafif kare yüz, yanak kızarıklığı |

**Kesin eleme (biri bile → ELE):** yanlış renk/kıyafet (ör. hoodie siyah/gri, flanel başka desen, kapüşon başta, kol kıvrık değil); yazı/logo/harf/rakam (1:1 + 2× kırpım); şapka/gözlük/saat/takı; Jake sakalsız veya dolgun sakallı; Mike'ta sakal; sayfada figürler arası kıyafet/saç farkı (ön-yan-arka ve 6 ifade aynı kişi değil); ekstra kişi; el/parmak bozukluğu ön planda; 2D/çizgi kontur veya fotogerçekçi stil; tanınır ünlü/var olan çizgi film karakteri benzerliği.
**Puanlama (geçenler arasında seçim):** kontrol listesi Jake 8 / Mike 8 madde (saç şekli, saç rengi, kaş, göz rengi, sakal durumu, üst giysi, alt giysi + ayakkabı, yüz oranı) tam puan şart; sonra (a) sayfa içi tutarlılık: 6 ifade kafası ↔ ön görünüm kafa HSV kor. (ortalama en yüksek kazanır), (b) ifadelerin okunurluğu (6/6 ayırt edilebilir), (c) arka görünümde kapüşon/flanel deseni doğru.
**Türev pozlar (taban, ağız, ikili) eşikleri:** sayfaya/tabana göre kafa hist kor. ≥0,84, ten ΔE ≤8, saç ΔE ≤10, giysi ΔE ≤8; ağız düzenlemesinde kafa merkez kayması ≤4 px ve ölçek farkı ≤%2 (yama oturmalı), ağız dışındaki yüz farkı (fark maskesi) yalnız ağız bölgesinde.
**İkili (D-A):** iki yüz kendi sayfasına kor. ≥0,80 (iki kişi tek üretimde, eşik bir basamak düşük), Mike Jake'ten hafif uzun, figürler değmiyor (ayrı kesilebilir).
**Plakalar:** gerçek boyut 9:16; kişi yok; yazı/logo/plaka yok (1:1 + 2× kırpım); orta %60 şerit y %35–85 boş (bel üstü kesik bindirme testi: T-J/T-M kesiği konulur, ölçek ve ışık uyumu göz incelemesi); alt %25 sakin; 4 plaka birbirine stil olarak uyumlu (aynı render dili, kontur yok; ilk seçilen G-A ile yan yana kontakt sayfada). `stil-olcum.py` 2D için ayarlı → 3D için ilk kabul edilen plaka değerleri taban alınır, diğerleri ±%25 içinde.
**Kontakt sayfası:** her öğe için referans/sayfa + 4 aday yan yana, elenenler gerekçeyle `uretim/seri/karakter/rapor.md`'ye; her dosyaya prompt ID + Canva media ID + üretim tarihi.

## 3. Konuşan sahne yaklaşımı (3D görünümlü stilde en düşük maliyet)
| Yol | Hak maliyeti (karakter başına) | Risk |
|---|---|---|
| **1. Aynı poz, ağız kapalı / yarı açık / açık + yama** | taban 1 + ağız 1 (4 adaydan yarı açık ve açık seçilir; çıkmazsa +1) | Düzenleme ağız dışında yüzü de değiştirebilir (Leo'da bakış değişince 0,70); 3D gölgelendirmede yama sınırı ton basamağı yapabilir → Leo `rig-yama.py` (fark maskesi +11 px, Gauss 4,5) + gerekirse ten Lab eşleme. Yalnız bir kafa açısında konuşur; her yeni açı = 2 hak. |
| 2. Kafa + göz katmanı + ağız yaması (rig) | taban 1 + ağız 1 + göz 1 + kesme işi | 3D ışıkta boyun ekleminde dikiş ve gölge kopukluğu görünür; kafa döndürme 2D'deki gibi inandırıcı değil (perspektif sabit). Leo rig'i 2D düz renkte çalıştı, 3D'de en riskli yol. Kazanç az: kafa sallama KOD ile tüm kesiğe (hafif dönme/ölçek) zaten verilebilir. |
| 3. Yalnız kamera + altyazı + ifade değişimi | 0 ek (sayfadaki 6 ifade + sahne kesikleri) | Yakın planda konuşan ama ağzı kıpırdamayan yüz "ölü" görünür; Reels'te izleyici fark eder. Geniş plan, sırtı dönük, dinleyen tepki çekimi ve dış ses için sorunsuz. |

**Öneri: 1 + 3 karma.** Konuşan yakın plan yalnız T-J / T-M tabanıyla (2 durumlu ağız: kapalı + açık; yarı açık 4 adaydan çıkarsa 3 durum). Rhubarb eşlemesi: X, A → kapalı; B, C, E, F, G, H → yarı açık (yoksa açık); D → açık. Geçişte 2 karelik alfa karışımı. Her şeye "nefes" (ölçek %0,5 salınım) + konuşma vurgusunda kafa-kesik mikro dönme KOD ile. Diğer tüm çekimler yol 3: ikili/mekân geniş planlar, dinleyenin tepki ifadesi (sayfadan değil, gerekirse ifade düzenlemesi taban üzerinden). Bölüm başına ek hak = 0 (taban ve ağızlar tüm sezon tekrar kullanılır; değişen plaka ve kamera). Göz kırpma: 12. hak kalırsa GK-J; yoksa sonraki ay. Image-to-video (canlı ağız) ücretli olabilir → yalnız Niyazi onayıyla, burada planlanmadı.
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
- aspectRatio: `PORTRAIT_9_16` · referans: [Jake sayfası kazanan, Mike sayfası kazanan] · not: boy/oran referansı + kesilebilir (zeminde ayrı iki figür) · 2763 karakter
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
- aspectRatio: `PORTRAIT_9_16` · referans: [Jake sayfası, Mike sayfası] · not: diyalog iki-çekimi tabanı; D-A geçerse yalnız yedek hakla · 2596 karakter
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
- aspectRatio: `PORTRAIT_9_16` · referans: [G kazanan plaka, Jake sayfası, Mike sayfası] · not: 3 referans bağlayıcıda denenmedi (risk); afiş/tanıtım görseli · 2390 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The first reference is the garage set; keep the set, camera and light. The second and third references are Jake's and Mike's model sheets; faces, hair and outfits must match exactly.
SHOT: the two friends standing in the open center of the garage, Jake on the left, Mike on the right, full figures, facing camera.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-A · Garaj (merkez üs) · sıra 1 (dalga 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · 1809 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the friends' home base: a lived-in suburban two-car garage seen from inside, looking toward a half-open roll-up garage door at the back that shows a sunny driveway and a strip of blue sky. Concrete floor with a few faint old oil stains. Left wall: long wooden workbench with a pegboard of hand tools, a clamp work lamp. Right wall: grey metal shelving with plain unmarked cardboard boxes and secondhand finds (an old bicycle, a vintage radio, a desk lamp, a box fan). Back left corner: a worn mustard-yellow armchair. A blank whiteboard leaning on the shelves. Center floor kept clear.
LIGHT: cool daylight spilling in from the garage door, warm light from the clamp lamp and a string of warm bulbs across the ceiling beams.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-B · Garaj (merkez üs) · sıra 2
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: plan/oy sahneleri için (beyaz tahtaya KOD yazı) · 1533 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the same kind of lived-in suburban garage, reverse angle: looking at the inner back wall with a long wooden workbench, a pegboard of hand tools, a large blank whiteboard mounted above the bench, plain unmarked cardboard boxes stacked at the sides, an old bicycle hanging on wall hooks, a worn mustard-yellow armchair at the right. Center floor kept clear.
LIGHT: cool fluorescent tube light from above, warm pool from a clamp lamp on the workbench.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### G-C · Garaj (merkez üs) · sıra sonraki ay (gece sürümü)
- aspectRatio: `PORTRAIT_9_16` · referans: [G kazanan] · not: kriz/gece bölümleri; 12'lik pakete dahil değil · 421 karakter
```
EDIT the reference image. Keep the same garage, same camera, same objects and same 3D render style. ONLY CHANGE: it is night; the garage door shows a dark blue night sky, the warm ceiling bulbs and the clamp lamp are the main light, deeper cool shadows. No people. No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### P-A · Garage sale sokağı · sıra 1 (dalga 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · 1676 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a sunny American suburban residential street on a Saturday morning, seen from the sidewalk at eye level, the street and sidewalk receding into the distance. Modest one-story houses with trees; on several front lawns and driveways stand garage-sale folding tables full of secondhand items (table lamps, a toaster, vinyl records in plain sleeves, toys, old electronics, a clothes rack, a bicycle leaning on a table). Price stickers are blank colored dots. The sidewalk in the center is clear.
LIGHT: bright warm morning sun from the side, cool blue shade under the trees and on the far houses.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### P-B · Garage sale sokağı · sıra 2
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: pazarlık sahneleri (alıcı-satıcı) · 1525 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a single suburban driveway garage sale up close: an open garage behind, two long folding tables in an L shape covered with secondhand items (lamps, a toaster, an old game console with no logos, records in plain sleeves, a box of tools, a clothes rack), a blank cardboard sign on an easel, blank colored-dot price stickers. The driveway space in front of the tables is clear.
LIGHT: warm morning sun, cool blue shadow inside the open garage.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### A-A · Mike'ın arabası · sıra 1 (dalga 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: iki koltuk iki-çekim; bel üstü kesikler koltuk önüne, alt gövdeyi ön konsol/direksiyon örter · 1625 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: inside Mike's old, well-loved compact car (a generic early-2000s hatchback, no brand badges), camera mounted on the dashboard looking back at the two empty front seats side by side, steering wheel at the lower left foreground edge, worn grey fabric seats with headrests, a coffee cup in the holder, a phone mount without a phone, a small crack in the dashboard plastic. Through the rear and side windows: a passing suburban street, slightly blurred.
LIGHT: warm late-afternoon sun through the side windows, cool shade inside the cabin roof.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### A-B · Mike'ın arabası · sıra 2
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: tek çekim (Mike sürerken) · 1476 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: inside the same kind of old compact hatchback (no brand badges), camera on the passenger side dashboard looking at the empty driver seat alone, steering wheel in the lower foreground, driver side window showing a passing suburban street slightly blurred, worn grey fabric seat, a coffee cup in the holder.
LIGHT: warm late-afternoon sun through the side window, cool shade on the roof liner.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### K-A · Daire mutfak masası · sıra 1 (dalga 1)
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: masa üstü kadraj %62–75'te (Leo dersi): bel üstü kesik masa arkasına oturur, 0 ek üretim · 1787 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: a small rented apartment kitchen-dining nook in the evening, camera at seated eye level directly across a simple square wooden table: the tabletop runs across the bottom 30% of the frame and continues past the bottom edge; on it only a closed laptop at one side, two mugs and a notepad with blank pages. Behind the table the central area is open, no chairs visible there (seated characters will be composited later, their lower bodies hidden by the table). Background: compact kitchen counters with a few dishes, an open shelf with plain jars, a small window showing a dusky blue city sky with soft distant lights.
LIGHT: warm pendant lamp hanging above the table, cool blue dusk light from the window.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### K-B · Daire mutfak masası · sıra 2
- aspectRatio: `PORTRAIT_9_16` · referans: yok · not: kuruluş çekimi · 1490 karakter
```
STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light (warm-colored characters will be composited in front).
SCENE: the same kind of small apartment kitchen-dining nook in the evening, establishing three-quarter high angle: a simple square wooden table with two mismatched empty chairs, a closed laptop, two mugs, a notepad with blank pages, compact kitchen counters, an open shelf with plain jars, a small window with a dusky blue city sky.
LIGHT: warm pendant lamp above the table, cool blue dusk light from the window.
EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces.
VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### T-J · Konuşma tabanı Jake · sıra 1 (dalga 2)
- aspectRatio: `PORTRAIT_9_16` · referans: [Jake sayfası kazanan] · not: Mike'a bakar (kadraj solu) · 1892 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.
The reference image is the model sheet of Jake Miller; the face, hair and outfit must match it exactly.
SHOT: waist-up portrait of Jake Miller alone, body and head turned about 20 degrees toward frame-left, eyes looking toward frame-left at someone just off-screen at eye level, relaxed neutral expression, mouth gently closed, arms relaxed and out of frame below; top of the head at 18% of the frame height, body continues past the bottom edge, centered.
BACKGROUND: plain flat medium slate-blue background, evenly lit, no shadows on the background.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### T-M · Konuşma tabanı Mike · sıra 1 (dalga 2)
- aspectRatio: `PORTRAIT_9_16` · referans: [Mike sayfası kazanan] · not: Jake'e bakar (kadraj sağı) · 1974 karakter
```
STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. Original character design, not resembling any existing cartoon character, celebrity or real person.
MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.
The reference image is the model sheet of Mike Carter; the face, hair and outfit must match it exactly.
SHOT: waist-up portrait of Mike Carter alone, body and head turned about 20 degrees toward frame-right, eyes looking toward frame-right at someone just off-screen at eye level, relaxed neutral expression, mouth gently closed, arms relaxed and out of frame below; top of the head at 18% of the frame height, body continues past the bottom edge, centered.
BACKGROUND: plain flat medium slate-blue background, evenly lit, no shadows on the background.
No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, no color swatches. Vertical 9:16 portrait.
```

### AG-J · Ağız açık Jake · sıra 1 (dalga 3)
- aspectRatio: `PORTRAIT_9_16` · referans: [T-J kazanan, Jake sayfası] · not: 4 adaydan yarı-açık + açık iki durum seçilir · 704 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Jake), same face, same hair, same navy hoodie with grey drawstrings, same stubble, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: mouth open mid-word in a relaxed talking shape: jaw dropped slightly, lips in a soft open oval, a little of the upper teeth visible, NOT smiling, NOT shouting; the rest of the face (eyes, eyebrows, cheeks) unchanged. No text, no logos. Vertical 9:16 portrait.
```

### AG-M · Ağız açık Mike · sıra 1 (dalga 3)
- aspectRatio: `PORTRAIT_9_16` · referans: [T-M kazanan, Mike sayfası] · 755 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Mike), same face, same hair, same open red-and-black buffalo-check flannel over the white T-shirt, rolled sleeves, clean-shaven face, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: mouth open mid-word in a relaxed talking shape: jaw dropped slightly, lips in a soft open oval, a little of the upper teeth visible, NOT smiling, NOT shouting; the rest of the face (eyes, eyebrows, cheeks) unchanged. No text, no logos. Vertical 9:16 portrait.
```

### GK-J · Göz kırpma Jake · sıra yedek-2
- aspectRatio: `PORTRAIT_9_16` · referans: [T-J kazanan, Jake sayfası] · not: yedek hak kalırsa · 568 karakter
```
EDIT the first reference image. Keep EVERYTHING identical: same man (Jake), same face, same hair, same navy hoodie with grey drawstrings, same stubble, same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference is the character model sheet; the face must match it. ONLY CHANGE: both eyelids fully closed in a natural blink, eyebrows relaxed, mouth unchanged. No text, no logos. Vertical 9:16 portrait.
```
<!-- PROMPTLAR:SON -->
