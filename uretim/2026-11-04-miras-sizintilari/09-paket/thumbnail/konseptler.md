# F4 — Thumbnail konseptleri (erken taslak) · S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It"

İLERLEME: tamam (F4 taslağı). Sıradaki: F8a'da görsel kol GEÇTİ olunca Canva üretimi (koordinatör) → `thumb-uret` v2 kopyası → `thumb-test` → 3 finalist `thumb-rapor.md`.
**Karar (taslak):** 4 konsept aday, 1 elendi. Test & Compare planı **K1 (duygu) · K3 (karşıtlık) · K2 ya da K4 (obje / mizah)**. K2 ile K4 aynı "sızıntı" fikrini taşıyor, ikisinden yalnız biri finale girer. Seçim F8a'da gerçek görselle yapılır.
**Maket kapısı [Ö]** (düz zemin + gri yer tutucu, `konsept-maket.py`, 2 koşu aynı): seçilen metinlerin hepsinde 168x94 satır OCR tam, büyük harf ≥13,5 px, p5 ≥5,0, süre damgası alanı boş, ≤4 kelime. Ayrıntı §3.
**Yeni Canva üretimi:** 4 taban (konsept başına 1) + tutarlılık kapısından kalana en fazla 1 düzeltme. Toplam ≤8. Çağrıyı koordinatör yapar.
Etiketler: [Ö] betik ölçümü · [GÖZ] i.ytimg.com mqdefault incelemesi, 2026-11-04 (8 rakip thumbnail; ızgara repo dışında) · [T] yargı.

## 1. Rakip alanı ve ayrışma kuralı [GÖZ]
Bu sorgu kümesinin 8 thumbnail'ı incelendi: wuJfl4Xuj9Q (AJ Osborne), 84mdMwgrks8, OSF3n3Btz7k, i-NkhdYLn3Q, dqKcNE_TZWY (How Money Works), gL8dtgfhhn0, DDxpT1bUfBU, KUx-H5A6b6Y.
- Klişeler: banliyö evi + "FOR SALE" tabelası (4/8), metinde "BOOMERS" kelimesi (5/8), yaşlı insan yüzü veya portresi (4/8), elden ele dolar (How Money Works), yanan para, kırmızı düşüş oku.
- **Bizde yasak:** ev ve satılık tabelası (bu ayrıca H7 kuralı, S04'e saklanıyor), "BOOMERS" kelimesi, yaşlı yüz, elden ele banknot, yanan para, ok.
- **Sahiplenilen öğe:** nakliye kutusu, köşesinden damlayan para, koli bandı (Leo'nun bant gag'i). Sette bu öğelerin hiçbiri yok.
- Maskot ayrışması (rakip-ozet §6): Fred silindir şapkalı ve takım elbiseli, Marcus beyaz yuvarlak kafalı ve sinsi gülüşlü. Leo'da şapka, ceket ve beyaz düz zemin yok. Siyah gömlek doygun ve açık zeminde siluet verir (hafıza 2026-11-02). Her konseptin zemin rengi farklı, Test & Compare'de karışmasınlar diye.

## 2. Konseptler
Ortak Canva ayarı: `generate-image`, aspectRatio **LANDSCAPE_16_9**. Referanslar sırayla **[MAHZHqW0_Uo (taban a), MAHZHpeQGdM (karakter sayfası), MAHZMVzdpqQ (C01, yalnız çizim stili)]**. Çıktı 1680x944 → 1280x720'ye küçültülür (1 px kırpım). Metin ve etiket görsele **yazdırılmaz**, kodla eklenir.
Tüm prompt'ların başına **ORTAK BLOK** aynen eklenir:
```
CHARACTER LOCK (match the first reference image and the reference character sheet exactly): the same man — Turkish man in his early 30s, warm light-tan skin, short dark-brown hair with volume swept up and slightly to the side, thick dark eyebrows, warm brown eyes, short well-groomed dark stubble beard and moustache. Outfit never changes: black button-up shirt, collar open at the neck, sleeves rolled to the forearm, black wristwatch on the left wrist. No hat, no jacket, no tie. Slim athletic build, normal proportions. STYLE LOCK: flat 2D TV-cartoon illustration, bold dark outlines, flat cel-shaded colors with simple 2-tone shadows, simplified shapes, NOT painterly, NOT photorealistic; use only the drawing style of the third reference, not its colors, doors or stage. Warm key light on the character's face. Banknotes are generic green paper bills with no readable text, no portraits, no real currency design.
```

### K1 — Duygu: kutudan para damlıyor (WHO GETS IT?)
- **Fikir:** Leo kucağındaki nakliye kutusuna bakıyor ve kutunun dibinden para damlıyor. Yüzündeki duygu endişeli şaşkınlık. Merak boşluğu şu: miras geliyor ama yolda eriyor, sonunda kime kalacak?
- **Metin:** **WHO GETS IT?** (sarı, lacivert kontur, 2 satır, sol) + küçük kırmızı levhada **$124T** (hakem H8). Alternatif "WHAT'S LEFT?" elendi: kesme işareti 168'de OCR'ı bozuyor (1/2).
- **Başlıkla:** Başlık "heirs might miss it" diyor, metin "o zaman kime?" diye devam ediyor ve tekrar etmiyor. **Alt-1 başlık seçilirse** ("Where Will the Boomers' Money Actually Go?") iki soru üst üste biner. O durumda K1 metni **SMALLER. LATER.** olur ve K3 görseli kalır.
- **Doğruluk:** 124 T$ Cerulli tahmini, 2048'e kadar (D1). Etikette atıf yok, "Bank of America" de yazmaz (H8). Damlayan para D2 çerçevesinde kalıyor: bağış ve uzun yolun maliyetleri anlatılıyor, "kayıp" rakamı verilmiyor.
```
SHOT: medium close-up, the man stands on the RIGHT half of the frame, body turned three-quarters toward the left, hugging a large plain brown cardboard moving box against his chest with both arms. He looks down at the bottom corner of the box, eyes wide, thick eyebrows raised high, mouth in a small worried "o" — anxious surprise, clearly readable. The bottom corner of the box is split open and a few large green banknotes are slipping out and falling. His face is large: head about one third of the frame height, fully visible, not cropped. The box has no writing, no labels.
BACKGROUND: plain deep teal (#0A4E58) studio wall with a soft warm glow behind his head; the LEFT 45% of the frame is completely empty plain teal (space for text added later). No props, no houses, no text, no logos, no watermark. 16:9 landscape.
```
- **Mobil plan:** metin x 60–600, satır 1 y 70 (200 px), satır 2 y 300, levha y 540 (120 px). Büyük harf 168'de 13,5–23,8 px. Yüz 168'de ≥28 px yükseklik (kafa ≥ kare yüksekliğinin %30'u). Para banknotları ≥70 px genişlikte olmalı, 168'de ~9 px (çok sayıda küçük banknot gürültü yapar, en fazla 5–6). Sol %45 yasak bölge: düşen banknot bu alana girerse kod maskeyle siler.

### K2 — Obje: sızdıran kamyon (IT LEAKS)
- **Fikir:** Videonun ana metaforu (The Leaky Moving Truck) tek karede. Kamyon uzaklaşıyor, arkasında yola saçılmış banknot izi kalıyor, Leo bant rulosuyla peşinden koşuyor.
- **Metin:** **IT LEAKS** (lacivert dolgu, beyaz kontur, tek satır, 220 px). Alternatif "LEAKING ALL THE WAY" 4/4 okundu ama 4 kelime ve harfleri daha küçük (16,9 px), bu yüzden elendi.
- **Risk [T]:** Leo'nun yüzü 168'de küçük kalır, duygu zayıflar. Bu konseptte kahraman nesne, yüz değil. Kamyon markasız ve yazısız olmalı.
```
SHOT: wide shot of an empty two-lane road through flat open teal-green countryside, no buildings. A small boxy white moving truck with no brand, no writing and no logo drives away toward the right-middle of the frame; its rear roll-up door is half open and one cardboard box at the edge has a torn corner. A long winding trail of large green banknotes lies on the road behind the truck, sweeping from the truck down to the bottom-left foreground. In the lower-right foreground the man runs after the truck holding a big roll of brown packing tape high in one hand, face alarmed: eyebrows up, mouth open. His head and torso are large in the foreground (head about one quarter of the frame height).
BACKGROUND: pale mint (#96D7C8) clear sky; the TOP-LEFT area (left 45%, top 40% of the frame) is empty plain sky (space for text added later). No houses, no signs, no text, no logos, no watermark. 16:9 landscape.
```
- **Mobil plan:** metin x 60, y 50, tek satır. Büyük harf 168'de 24,9 px. Banknot izi 168'de çizgi olarak okunmalı. Bu yüzden büyük ve az banknot (≥60 px) kullanılır, ize sarı-yeşil ışık verilir. Kamyon ve Leo süre damgası alanına (x ≥1088, y ≥634) taşabilir, metin taşamaz.

### K3 — Karşıtlık: gönderilen kutu ↔ varan kutu (SMALLER. LATER.)
- **Fikir:** Solda büyük, yeni bir nakliye kutusu duruyor, sağda bantla yamanmış, daha küçük bir kutu varıyor. Leo ikisinin arasında envanter listesiyle şüpheli bakıyor. İki satır, iki kelime, iki gerçek (P4 paradoks paketi tipi b).
- **Metin:** **SMALLER.** (lacivert, beyaz kontur) + **LATER.** (kırmızı levhada beyaz). Bu iki kelime hakemin K1 kapanış kartıyla birebir ("çoğu aile için daha küçük ve daha geç") ve D2 ile de uyumlu (eş payı bir gecikme, kayıp değil). Alternatif "SENT BIG, GOT SMALL" elendi: 4 kelime, kırmızı-sarıda p5 3,87, OCR 3/4. Ayrıca Anton'da "≠" glifi yok (ilk maket).
- **Doğruluk koşulu:** Kutuların boy oranı niteliksel ("noticeably smaller", yaklaşık yarı boy). F3 `03-metin/veri/hesap.py` Okafor şelalesinde varış payını büyük çıkarırsa (≥%70), oran ona göre küçültülür. Abartılı boy kıyası yapılmaz (S08 dersi).
```
SHOT: medium-wide shot inside a bright, simple warehouse loading dock. On the LEFT stands one huge, clean, sealed plain brown cardboard moving box, taller than the man. On the RIGHT, arriving on a small hand trolley, is the same kind of box but noticeably smaller (about half the height), battered, its corners patched with several strips of brown packing tape, a single green banknote poking out of a seam. The man stands in the middle holding a clipboard inventory list, looking from the big box to the small box with one eyebrow raised and a skeptical sideways glance, mouth a flat line. His head about one quarter of the frame height, fully visible. Boxes have no writing, no labels.
BACKGROUND: plain warm pale-yellow (#FAE18C) wall; the TOP 35% of the frame is empty plain wall above the boxes (space for text added later). No houses, no signs, no text, no logos, no watermark. 16:9 landscape.
```
- **Mobil plan:** metin y 40 (170 px) ve y 270 (150 px, levha), sol yarı. Büyük harf 168'de ≥16,9 px. Büyük kutunun tepesi metnin altında kalmalı (y ≥ 440), yoksa kutu metne değer ve p5 düşer (iki kez öğrenilmiş ders). Küçük kutu süre damgası alanının dışında, x ≤1050.

### K4 — Mizah / duygu: bant gag'i (IT KEEPS LEAKING)
- **Fikir:** Videonun akılda kalan karakter anı. Leo bir köşeyi bantlıyor, para başka bir köşeden akıyor. Kameraya "yine mi?" diye bakıyor. Rakiplerin hepsi kıyamet tonunda, bunun tonu mizah [T].
- **Metin:** **IT KEEPS LEAKING** (beyaz, lacivert kontur; "LEAKING" lacivert levhada). Alternatif "MORE TAPE?" elendi: izleyici gag'i bilmeden görür, para mesajı yok, OCR 1/2.
- **K2 ile ilişki:** İkisi de sızıntı diyor. Finale yalnız biri girer. K4'te yüz büyük, K2'de metafor bütün olarak görünüyor.
```
SHOT: medium close-up, the man on the RIGHT half of the frame, leaning over a plain brown cardboard box on a table in front of him. One corner of the box is already covered in several crossed strips of brown packing tape; he is stretching a fresh strip of tape from a big roll across it with both hands, while green banknotes spill out of a DIFFERENT corner of the box. He looks straight at the camera with an exasperated, deadpan expression: one eyebrow raised, mouth pressed in a flat sideways grimace. His head about one third of the frame height, fully visible, not cropped. The box has no writing, no labels.
BACKGROUND: plain warm brick-coral (#C4402C) wall with a soft lighter glow behind his head; the LEFT 45% of the frame is empty plain coral (space for text added later). No houses, no text, no logos, no watermark. 16:9 landscape.
```
- **Mobil plan:** metin x 60, y 70 / y 300 (170 px). Büyük harf 168'de 19,2 px. Beyaz-mercan kontrastı ancak koyu tuğla tonda geçti (#EE765C'de p5 2,85 → #C4402C'de 5,1). Zemin daha açık üretilirse koda lacivert levha eklenir. Bant ve banknot sol %45'e girmez.

### Elenen — K5: iki el arasında delikli kutu (senaryodaki ilk fikir)
Yaşlı ve genç iki elin arasında delikli bir kutu. Elendi, çünkü: (1) How Money Works "THE BOOMER WEALTH COLLAPSE" (dqKcNE_TZWY) elden ele para kompozisyonuna çok yakın [GÖZ]; (2) yüz yok, duygu yok; (3) "yaşlı el" kuşak çerçevesini çağırıyor (P2 riski).

## 3. Test kapısı (maket) [Ö]
`THUMB_TMP=<geçici> python3 -I konsept-maket.py` iki koşu → çıktı `diff` aynı. Betik sha256 **270a8cb1474a**, çıktı `maket/olcum.json`, `maket/cikti.txt`. Maket şunları ölçer: metnin zemin rengine karşı p5 kontrastı (yer tutucu çakışması F8a'da gerçek görselde ölçülür), 168x94 satır kırpımı ×4 → tesseract psm 7 (normal + ters), büyük harf yüksekliği ve süre damgası alanı.

| Metin | Kelime | OCR 168 satır | Büyük harf 168 (min) | p5 (min) | Karar |
|---|---|---|---|---|---|
| K1a WHO GETS IT? + $124T | 4 | 4/4 | 13,5 px | 5,01 | **seçildi** |
| K1b WHAT'S LEFT? | 2 | 1/2 | 23,8 | 6,48 | elendi (OCR) |
| K2a IT LEAKS | 2 | 2/2 | 24,9 | 11,51 | **seçildi** |
| K2b LEAKING ALL THE WAY | 4 | 4/4 | 16,9 | 11,51 | elendi (uzun) |
| K3a SMALLER. LATER. | 2 | 2/2 | 16,9 | 5,01 | **seçildi** |
| K3b SENT BIG, GOT SMALL | 4 | 3/4 | 19,2 | 3,87 | elendi (kontrast, OCR) |
| K4a IT KEEPS LEAKING | 3 | 3/3 | 19,2 | 5,10 | **seçildi** |
| K4b MORE TAPE? | 2 | 1/2 | 26,0 | 5,10 | elendi (OCR, bağlamsız) |
İlk koşuda iki düzeltme yapıldı: $124T levhası 90 → 120 px (OCR 0 → 1); K4 zemini #EE765C → #C4402C (p5 2,85 → 5,1). Önizleme: `maket/K*-168.png` (168x94, x4 en yakın komşu).

## 4. F8a üretim ve değerlendirme planı
1. Koordinatör 4 prompt'u (§2) çağırır, media ID'leri bu dosyaya ve `thumb-rapor.md`'ye yazılır. Görsel kol F4'te kutu, kamyon veya bant plakaları üretirse önce onlar kullanılır, prompt üretimi düşer.
2. **Tutarlılık kapısı:** `tools/gorsel/tutarlilik.py` ile taban a'ya göre kafa korelasyonu ≥0,80, ten ΔE ≤5, saç ΔE ≤2. Kalırsa tek düzeltme: üretilen görsel 1. referans, a 2. referans olur ve "EDIT … ONLY CHANGE: the face must match the second reference" yazılır. Yine kalırsa konsept düşer.
3. `uretim/2026-10-28-yeni-video/09-paket/thumbnail/thumb-uret.py` ve `thumb-test.py` (v2) buraya kopyalanır, satır kırpımı psm 7 (bu maketteki `ocr_satir`) eklenir. Kapılar: 1280x720, ≤2 MB, ≤4 kelime, 168x94 bölge OCR tam, p5 ≥4,5, süre damgası alanında metin 0, rakip ızgarasında (repo dışı) renk ve kompozisyon ayrışması.
4. Finalde K1 + K3 + (K2 | K4). Elenenler ve nedenleri `thumb-rapor.md`'de yazılır. Dosya adları paket şemasına uyar: `09-paket/thumbnail/<harf><no>-<ad>.jpg`.
