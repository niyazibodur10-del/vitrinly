# F4 görsel kol — Canva prompt paketi · 1929-1000-dolar

**Ajan:** gorsel-varlik-sanatcisi · **Tarih:** 2026-10-27 · **Üreten:** koordinatör (`mcp__Canva__generate-image`; bu ajanın aracı yok) · **Sahne eşlemesi:** `sahne-listesi.md`
**Kaynak kilit:** `assets/karakter/karakter-karti.md` → "Canva karakter kilidi prompt'u" (taban + düzenleme). Bu dosya `araclar/prompt-uret.py` ile kartın kod bloklarından **birebir** üretildi; denetim `araclar/prompt-kontrol.py` (§6).
**Maliyet:** Niyazi'nin Canva aboneliğindeki aylık AI hakkı; ek ücret yok. **Sayı:** çekirdek 19 (C01–C19) + seçmeli 3 (C20–C22); tekrar payı ≤5 → tavan 27.

## 1. Koordinatör için çalışma sırası

1. Her üretim: `generate-image` → prompt = aşağıdaki ```prompt bloğu **aynen**, referanslar = "Referanslar" satırındaki media id'ler (sırası önemli: 1. taban/çapa, 2. karakter sayfası), aspectRatio = belirtilen değer.
2. `<Cxx media id>` yer tutucusu = o Cxx'in **kabul edilmiş** media id'si (önce o üretilmeli ve geçmeli).
3. Tam çözünürlük: `tools/gorsel/canva-indir.md` (tuval `DAHZHv3mU9w`, sayfa başlığı = Cxx) → `05-gorsel/canva-ham/Cxx.png` (1920x1080; C22 için 1080x1920 sayfa). Birden çok aday varsa `Cxx-a.png`, `Cxx-b.png`.
4. §5 üretim kaydına media id + tarih + deneme no yaz (ya da bana ilet; değerlendirmede ben doldururum).
5. Dalga sırası (bir dalgada ≤5 paralel iş; hafıza: 5 paralel sorunsuz, iş başı ~20–40 sn):

| Dalga | İşler | Bağımlılık | Amaç |
|---|---|---|---|
| 1 | **C01, C02**, C06, C07, C08 | yok (hepsi hazır id'lerle) | F5 kritik yol: stüdyo + tam boy taban + rig başlangıcı |
| 2 | **C03** (← C01), **C04** (← C02), C09, C10, C11 | C01, C02 kabul | konuşan Leo plakası + yürüme; rig tamam |
| 3 | **C05** (← C04), C12, C13, C14, C15 | C04 kabul | Box Leo + jestler |
| 4 | C16, C17, C18, C19 (+ seçmeli C20, C21, C22 ← C01) | yok | dönem plakaları |

**F5 kritik yol testi için en az gereken:** C01, C02, C03, C04, C05 (konuşan Leo = paket-v1 a/b kesikleri, hazır: `hazirlik/a-konusma-kapali/M4-renk-arindirma.png`). Rig ağızları (C06–C11) testte yoksa animasyon-yonetmeni a/b + vektör ağızla geçici çalışır.

## 2. Tasarım kararları (aday → eleme)

| Konu | Adaylar | Seçilen | Gerekçe |
|---|---|---|---|
| Leo tutarlılığı | (A) taban + EDIT ONLY CHANGE · (B) her poz sıfırdan kilit prompt | A | Kart ölçümü: A kafa kor. 0.84–0.96; B 0.45 (yüz daralıyor) |
| Tam boy poz | (A) C02 tam boy taban (çapa = paket-v1 a + sayfa) → C04 → C05 zinciri · (B) paket-v1 a'dan doğrudan "zoom out" düzenlemesi · (C) her tam boy pozu sayfadan sıfırdan | A | B'de "same framing" kuralı bozulur, model kadrajı tutamaz; C sıfırdan = tutarsız. A'da tek kadraj değişimi C02'de olur, sonrası aynı ölçekte düzenleme |
| Plaka referansı | (A) referans yok, STYLE LOCK metni · (B) karakter sayfası referansı + "no people" · (C) sonraki stüdyo plakalarında C01 referansı | A (ilk plaka ve dönem plakaları) + C (C03, C22) | B: sayfa referansı Leo'yu sahneye sokma eğilimi (canva-testi test1/2'de sayfa referansıyla hep Leo çizildi); C aynı stüdyoyu korur. C01 stili Leo kesiğiyle uyumsuz çıkarsa (kontur yok, fotogerçekçi) **tek tekrar B ile** |
| Plakada yazı | (A) modele levha/şerit yazısı yazdır · (B) boş levha + KOD yazı | B | AI harfleri bozuk; rakamlar kaynaklı ve doğrulanmış olmalı → yalnız KOD |
| Rig ağızları | (A) Canva düzenleme (yama) · (B) yalnız vektör ağız (pilot) | A (+ B yedek) | A çizim diliyle aynı; fark maskesiyle yama hizalı (paket-v1 a↔b %0,2) |

## 3. Ortak kilitler (her prompt'ta birebir)
- Leo **taban** prompt'ları (C02): kartın `CHARACTER LOCK … STYLE LOCK … warm key light on the character.` paragrafı birebir.
- Leo **düzenleme** prompt'ları (C04–C14, C20, C21): kartın `EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, …` kalıbı; poz/görünüm değişenlerde (C04, C05) "same framing / same body position" yerine **ölçek kilidi** (aynı boy, tam boy) — kimlik çekirdeği ve "The second reference is the character model sheet; the face must match it." birebir.
- **Karaktersiz plakalar** (C01, C03, C15–C19, C22): Leo çizilmez (katman olarak eklenir) → karakter kilidi yerine `STYLE LOCK` cümlesi birebir + `EMPTY SCENE … no man in a black shirt` (Leo benzeri ikinci adam çıkmasın) + yazı yasağı + %80 taşma kuralı.
## 4. Prompt'lar
### C01 · Stüdyo geniş plan — 3 dev kapı · P0
- **Tür:** CV-A karaktersiz plaka
- **Referanslar:** yok (ilk plaka; sayfa referansı Leo'yu sahneye sokma riski taşır → bkz. §2 aday B)
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S01, S04, S11, S14 (bulanık), S17, S19, S22 (punch-in), S23, S24 + Sh1 kapı kırpımları
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; üç kapı tam görünür ve renk tonu ayrışır (HSV H: mavi 190–240°, yeşil 90–160°, kahve 15–40°; kapı başına medyan); kapı üstü levha alanları boş

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: a TV game-show studio stage seen from the audience, wide shot. Three giant identical closed doors stand side by side in the middle of the stage, evenly spaced, full height visible: left door painted saturated royal blue, center door emerald green, right door warm chocolate brown, each with simple raised panels, a round brass knob and an EMPTY blank rectangular plate above the frame (plates left blank on purpose). Polished dark stage floor with soft reflections, a few round stage lights on the floor, dark audience silhouettes only as a thin soft shape at the very bottom edge. Open empty floor space on the left third and right third of the stage (a host will be composited there later).
LIGHT AND PALETTE: deep navy and indigo studio darkness with warm golden spotlights falling on each door; cool background, warm light pools; high contrast, cinematic.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C02 · Leo tam boy taban (ön, ayakta) · P0
- **Tür:** CV-L taban (yüz çapası = paket-v1 tabanı)
- **Referanslar:** [MAHZHqW0_Uo (paket-v1 a), MAHZHpeQGdM (karakter sayfası)]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** C04/C05'in tabanı; S04 klonları; B planı (tek Leo yürür)
- **Kabul:** Kafa kırpımı taban kafa yüksekliğine ölçeklenip HSV hist kor. **≥0.80** (ölçek farklı olduğu için tutarlilik.py kadraj eşikleri uygulanmaz), ten/saç/gömlek ΔE eşikleri aynı; kontrol listesi 9/9 (7 + koyu gri chino + beyaz ayakkabı); ayaklar kadrajda; düz zemin (M4 kesilebilir)

```prompt
CHARACTER LOCK (match the reference character sheet exactly): the same man as in the reference sheet — Turkish man in his early 30s, warm light-tan skin, short dark-brown hair with volume swept up and slightly to the side, thick dark eyebrows, warm brown eyes, short well-groomed dark stubble beard and moustache. Outfit never changes: black button-up shirt, collar open at the neck, sleeves rolled to the forearm, black wristwatch on the left wrist. Slim athletic build, normal proportions. STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, warm key light on the character.
SHOT: full body, head to toe, front view facing the camera, standing relaxed, arms down at his sides, neutral friendly closed-mouth half-smile; he also wears slim dark charcoal-grey chino trousers and clean white low-top sneakers; the whole figure fills about 85% of the frame height, centered, feet fully visible with a little floor margin. His face, hair and beard are exactly those of the first reference image.
BACKGROUND: plain flat slate-blue background (#3E5A7E), evenly lit, no shadows on the wall, no text, no logos, no watermark. 16:9 landscape.
```

### C03 · Stüdyo orta plan — kürsü + boş dev ekran · P0
- **Tür:** CV-A karaktersiz plaka
- **Referanslar:** [<C01 media id>] (aynı stüdyo tasarımı)
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S02, S03, S08, S13, S15, S16, S20 (KOD soğuk mavi renk notu), S21 + Sh2 zemini (C22 yoksa)
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; C01 ile aynı stüdyo (renk paleti, zemin, ışık dili) — kontaktta yan yana; ekran yüzeyi düz ve boş (KOD grafik yerleşecek); kürsü ön yüzü boş

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: the same TV game-show studio as the reference image, medium shot closer to the stage. Foreground left third: a sleek host podium (lectern) with a plain empty dark front panel, its top edge at about 60% of the frame height, empty behind it (a host will be composited standing behind it). Background right two-thirds: a huge blank dark video wall screen with a thin glowing edge, completely empty, flat and evenly dark (graphics will be added later). The edge of the three colored doors (blue, green, brown) is softly visible far behind, out of focus.
LIGHT AND PALETTE: same palette as the reference: deep navy and indigo studio darkness, warm golden key light on the podium area, cool blue glow from the screen edge.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C04 · Leo tam boy yürüme (3/4, sağa doğru) · P0
- **Tür:** CV-L düzenleme (poz değişimi)
- **Referanslar:** [<C02 media id>, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S04 Stock/Bank klonları (2 kopya), S18 küçük ölçek, B planı
- **Kabul:** Kafa kırpımı taban kafa yüksekliğine ölçeklenip HSV hist kor. **≥0.80** (ölçek farklı olduğu için tutarlilik.py kadraj eşikleri uygulanmaz), ten/saç/gömlek ΔE eşikleri aynı; kontrol listesi 9/9 (7 + koyu gri chino + beyaz ayakkabı); ayaklar kadrajda; düz zemin (M4 kesilebilir); yürüme adımı okunur (bir ayak önde, karşı kol önde)

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same slim dark charcoal-grey chino trousers, same clean white low-top sneakers, same character size and camera distance (full body, head to toe visible, feet not cropped), same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: he is now walking to the right of the frame in a three-quarter view, mid-stride, left foot forward and right arm swinging forward, relaxed confident walk, head turned slightly toward the camera with the same closed-mouth half-smile; body stays centered in the frame. No text, no logos.
```

### C05 · Leo tam boy kutuyla yürüme (Box Leo) · P0
- **Tür:** CV-L düzenleme (poz değişimi)
- **Referanslar:** [<C04 media id>, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S04 Box Leo, S18 (bakkala yürür)
- **Kabul:** Kafa kırpımı taban kafa yüksekliğine ölçeklenip HSV hist kor. **≥0.80** (ölçek farklı olduğu için tutarlilik.py kadraj eşikleri uygulanmaz), ten/saç/gömlek ΔE eşikleri aynı; kontrol listesi 9/9 (7 + koyu gri chino + beyaz ayakkabı); ayaklar kadrajda; düz zemin (M4 kesilebilir); kutu düz kahverengi karton, yazısız, iki kolla göğüste

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same slim dark charcoal-grey chino trousers, same clean white low-top sneakers, same character size and camera distance (full body, head to toe visible, feet not cropped), same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: he hugs a plain brown cardboard shoebox with its lid on against his chest with both arms while walking (same three-quarter view, same mid-stride legs, same walking direction); the box is plain with no print and no text; the black wristwatch on his left wrist stays visible. No text, no logos.
```

### C06 · Rig: göz kırpma (gözler kapalı) · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** tüm konuşan sahneler (2–6 sn'de bir kırpma); S04 'Remember that laugh' göz kırpma tek göz için KOD maskesi
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: both eyes fully closed in a relaxed blink: upper eyelids down, closed eyes drawn as a soft curved lash line, eyebrows, mouth and everything else unchanged. No text, no logos.
```

### C07 · Rig: ağız B (dişler birleşik, hafif açık) · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** Rhubarb B (K, S, T, EE)
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: the mouth is slightly open with the upper and lower teeth together and visible, lips relaxed, as when saying 'ee' or 'ss'; NOT smiling, mouth corners neutral, jaw not dropped. No text, no logos.
```

### C08 · Rig: ağız C (orta açık, rahat) · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** Rhubarb C (EH, AE) ve H (L)
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: the mouth is open at medium height, relaxed, jaw slightly lowered, upper teeth partly visible, as when saying 'eh'; NOT smiling, mouth corners neutral; less open than a tall 'aah'. No text, no logos.
```

### C09 · Rig: ağız E (yuvarlak 'oh') · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** Rhubarb E (AO, ER)
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: the mouth is open in a medium rounded oval shape, lips slightly pushed forward, as when saying 'oh'; NOT smiling, mouth corners neutral. No text, no logos.
```

### C10 · Rig: ağız F (büzük 'oo') · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** Rhubarb F (UW, OW, W)
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: the lips are pushed forward into a small tight round pucker with a small opening, as when saying 'oo' or 'w'; NOT smiling. No text, no logos.
```

### C11 · Rig: ağız G (üst diş alt dudakta 'f') · P1
- **Tür:** RIG düzenleme (kanal varlığı, bir kez)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** Rhubarb G (F, V)
- **Kabul:** Piksel hizası: değişen bölge dışında (|fark|>30) piksel ≤%1 (paket-v1 ölçümü %0,2); kafa hist kor. ≥0.84; istenen şekil doğru ve **gülümseme yok** (ağız köşeleri nötr); değişen bölge kutusu yalnız ağız/çene (göz kırpmada yalnız gözler) — `araclar/fark-maskesi` ile ölçülür
- **Not:** A ve X = paket-v1 a (kapalı), D = b (tall 'aah'). Kabul edilenler `assets/karakter/parcalar/agiz/` ve `goz/` altına fark maskesiyle yama olarak girer.

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: the upper front teeth rest lightly on the lower lip, as when saying 'f' or 'v'; NOT smiling, mouth corners neutral. No text, no logos.
```

### C12 · Leo iki elle sunum (avuçlar açık) · P2
- **Tür:** CV-L düzenleme (kol değişimi)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S01 'Let's play', S16 skor tablosu, S21 iki panel
- **Kabul:** `tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4, ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); M4 kesme artığı ≤0.01, saçak ≤150 px

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: both forearms are raised and extended outward to the sides at waist-to-chest height with palms open and facing up, a welcoming presenting gesture like a game-show host; head, torso and body stay in the same place, mouth closed with the same half-smile; the black wristwatch stays on the left wrist. No text, no logos.
```

### C13 · Leo kollar kavuşturmuş, kendinden emin (Bank Leo) · P2
- **Tür:** CV-L düzenleme (kol değişimi)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S07 sağ panel, S08 arka plan
- **Kabul:** `tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4, ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); M4 kesme artığı ≤0.01, saçak ≤150 px (saat kavuşturulmuş kolda görünür kalmalı)

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: his arms are crossed over his chest, a confident relaxed closed-mouth smile; head, torso and body stay in the same place; the black wristwatch on the left wrist stays visible on top. No text, no logos.
```

### C14 · Leo kutuyu göğüs hizasında tutar (Box Leo, bel üstü) · P2
- **Tür:** CV-L düzenleme (kol değişimi)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S11 (KOD: kulağa doğru döndürüp sallama), S12, S14
- **Kabul:** `tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4, ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); M4 kesme artığı ≤0.01, saçak ≤150 px; kutu yazısız düz kahverengi karton

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: he holds a plain brown cardboard shoebox with its lid on in both hands at chest height, slightly curious closed-mouth smile; head, torso and body stay in the same place; the box has no print and no text; the black wristwatch on the left wrist stays visible. No text, no logos.
```

### C15 · Sepya 1929 New York sokağı · P3
- **Tür:** CV-A karaktersiz plaka · İll.
- **Referanslar:** yok
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S01 açılış karesi (0:00–0:02, yavaş zoom), S18 Box Leo yürür (C05 küçük ölçek)
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; gerçek bina/marka tanınmıyor; dönem öğeleri okunur (1920'ler araç, şapkalı yayalar uzakta)

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: a 1929 New York City street in autumn, eye-level wide shot down the sidewalk: brick and stone buildings with fire escapes, generic shop fronts with blank awnings, a 1920s automobile parked at the curb, gas street lamps, a few tiny distant pedestrians in period coats and fedora hats with undetailed faces far in the background; the near sidewalk on the right third is empty (a character may walk there later). Generic architecture, no recognizable real building.
LIGHT AND PALETTE: cool desaturated sepia with blue-grey shadows (a cold 1929 mood), soft overcast daylight; muted so a warm-lit cartoon host composited on top stands out.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C16 · Sepya 1929 borsa binası dışı + kâğıt şerit yağmuru · P3
- **Tür:** CV-A karaktersiz plaka · İll.
- **Referanslar:** yok
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S05 (mavi kapının içinden görünür), S06/S07 bulanık-karartılmış zemin
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; şeritlerde yazı/rakam yok; bina jenerik (gerçek borsa cephesi kopyası değil)

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: the exterior of a grand generic neoclassical financial exchange building in 1929 with tall columns and wide stone steps, low camera angle; long curling strips of blank paper ticker tape and confetti fall through the air and lie on the steps; the strips are completely blank. The steps in the left third are empty (a character will be composited there later).
LIGHT AND PALETTE: cool desaturated sepia with blue-grey shadows (a cold 1929 mood), soft overcast daylight; muted so a warm-lit cartoon host composited on top stands out. A faint warm glow from inside the columns.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C17 · Sepya 1930 banka içi — mermer zemin, dev kasa kapısı · P3
- **Tür:** CV-A karaktersiz plaka · İll.
- **Referanslar:** yok
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S07 sağ panel, S10 kasa önü (grafikte bulanık), S18 kilitli kapı (KOD zincir)
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; kasa kapısı kadrajın sağ yarısında tam görünür (KOD zincir için)

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: the interior of a 1930 American bank hall: polished checkered marble floor, marble columns, brass teller cages along the left wall, and on the right half a huge round steel vault door, closed, with a big wheel handle and bolts, fully visible. The center-left floor is empty (a character will be composited there later). No signs on the walls.
LIGHT AND PALETTE: cool desaturated sepia with blue-grey shadows, soft light from tall windows, a cold quiet mood.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C18 · Sepya 1930 banka önü kuyruk · P3
- **Tür:** CV-A plaka (arka planda stilize kalabalık) · İll.
- **Referanslar:** yok
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S09 (Bank Leo ön planda, bel üstü; KOD kuyruk oku yan bankaya)
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de (bu plakada yalnız ARKA PLANDA stilize kuyruk var); yüzler yakın plan değil, ağlayan/çaresiz yüz yok (politika G2); tabelada yazı yok
- **Not:** Bu plakada kişi var (arka plan kalabalığı); NOPPL kuralı 'ön planda' kişi yasağıdır.

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: a 1930 city street outside a generic stone bank building with tall closed doors and a blank stone plaque above them (no lettering). A long orderly line of people in period coats and hats waits along the sidewalk toward the doors, seen from behind and in profile at mid-distance, small and stylized with simple undetailed faces, calm and patient postures. The foreground right third is empty (a character will be composited there later). A second similar bank is visible further down the street on the left.
LIGHT AND PALETTE: cool desaturated sepia with blue-grey shadows (a cold 1929 mood), soft overcast daylight; muted so a warm-lit cartoon host composited on top stands out.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C19 · Sepya 1930'lar dükkân vitrini (etiketsiz) · P3
- **Tür:** CV-A karaktersiz plaka · İll.
- **Referanslar:** yok
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S12 (KOD fiyat etiketleri vitrine yerleşir) + Sh2
- **Kabul:** 1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 incelemede harf/rakam/logo/tabela yazısı yok; stil: kalın kontur + cel-shading, M4 kesik Leo ile yan yana kontaktta kontur kalınlığı ve gölge dili uyumlu; önemli öğe merkez %80'de; ürünler temsili (marka/etiket yok), etiket yerleri boş; dikey merkez şeridinde vitrin okunur (Sh2 kırpımı)

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: the front window of a 1930s general store, straight-on medium shot: shelves behind the glass with generic unbranded goods (plain jars, bread loaves, plain cans with no labels, folded shirts, a pair of shoes), each item with a small EMPTY blank tag hanging in front of it (tags left blank on purpose). Wooden window frame, a blank awning above.
LIGHT AND PALETTE: cool desaturated sepia with blue-grey shadows outside, slightly warmer light inside the shop window.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 16:9 landscape.
```

### C20 · Leo sol bilek saatine bakar (Bank Leo kuyrukta) · P4 seçmeli
- **Tür:** CV-L düzenleme (kol değişimi)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S09 (yoksa B: e düşünen)
- **Kabul:** `tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4, ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); M4 kesme artığı ≤0.01, saçak ≤150 px; saat SOL bilekte ve okunur

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: he raises his left forearm in front of his chest and looks down at the black wristwatch on his left wrist with a slightly impatient closed-mouth expression; torso stays in the same place. No text, no logos.
```

### C21 · Leo el sallar (kapanış) · P4 seçmeli
- **Tür:** CV-L düzenleme (kol değişimi)
- **Referanslar:** [MAHZHqW0_Uo, MAHZHpeQGdM]
- **aspectRatio:** LANDSCAPE_16_9
- **Kullanım:** S24 (yoksa B: b-alt)
- **Kabul:** `tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4, ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); M4 kesme artığı ≤0.01, saçak ≤150 px

```prompt
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: his right hand is raised beside his head, palm open toward the camera in a friendly goodbye wave, warm closed-mouth smile; head, torso and body stay in the same place; the black wristwatch stays on the left wrist. No text, no logos.
```

### C22 · Dikey stüdyo zemini (Shorts) · P4 seçmeli
- **Tür:** CV-A karaktersiz plaka (9:16)
- **Referanslar:** [<C01 media id>]
- **aspectRatio:** PORTRAIT_9_16 (bağlayıcıdaki dikey değer)
- **Kullanım:** Sh1/Sh2 zemin (yoksa B: C03 merkez kırpım bulanık)
- **Kabul:** 1080x1920'ye uygun dikey oran; ön planda insan yok; yazı yok; alt %35 ve üst %15 sade (Shorts arayüzü + Leo katmanı)

```prompt
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, detailed environment painting in the same art style as a 2D animated series background, consistent line weight.
SCENE: the same TV game-show studio as the reference image in a tall vertical frame: the three giant doors (blue, green, brown) seen in steep perspective from a low angle, stacked visually from near to far up the frame, warm spotlights, dark empty stage floor in the lower third.
LIGHT AND PALETTE: same palette as the reference: deep navy and indigo darkness, warm golden spotlights.
EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt.
Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom).
No text, no letters, no numbers, no signage, no logos, no watermark. 9:16 portrait.
```

## 5. Üretim kaydı (lisans/kaynak; değerlendirmede doldurulur)
Kaynak: Canva AI (`generate-image`), Niyazi'nin hesabı, Canva Kullanım Koşulları (ticari kullanım serbest). Her satır: prompt = §4'teki blok.

| Id | Deneme | Canva media ID | Üretim tarihi (UTC) | Ham dosya | Karar |
|---|---|---|---|---|---|
| C01 | 1 | MAHZMVzdpqQ | 2026-10-27 09:50 | canva-ham/C01.png | KABUL (rapor.md) |
| C02 | 1 | MAHZMdkmnN0 | 2026-10-27 09:50 | canva-ham/C02.png | KABUL (rapor.md) |
| C03 | 1 | MAHZMp2sz2k | 2026-10-27 | canva-ham/C03.png | KABUL (rapor.md) |
| C04 | 1 | MAHZMqkRJiU | 2026-10-27 | canva-ham/C04.png | KABUL (rapor.md) |
| C05 | 1 | MAHZMgBwQoo | 2026-10-27 | canva-ham/C05.png | KABUL (rapor.md) |
| C06 | 1 | MAHZMRc8cCA | 2026-10-27 09:50 | canva-ham/C06.png | KABUL (rapor.md) |
| C07 | 1 | MAHZMeBO7dI | 2026-10-27 09:50 | canva-ham/C07.png | KABUL (rapor.md) |
| C08 | 1 | MAHZMVNWYYg | 2026-10-27 09:50 | canva-ham/C08.png | KABUL (rapor.md) |
| C09 | 1 | MAHZMaSYoyg | 2026-10-27 10:00 | canva-ham/C09.png | KABUL (rapor.md) |
| C10 | 1 | MAHZMW-dAug | 2026-10-27 10:00 | canva-ham/C10.png | KABUL (rapor.md) |
| C11 | 1 | MAHZMeA_toQ | 2026-10-27 10:00 | canva-ham/C11.png | RED (rapor.md) |
| C11 | 2 (C11b) | MAHZMoaZcZQ | 2026-10-27 | canva-ham/C11b.png | RED (rapor.md) |
| C12 | 1 | MAHZMoyEe7E | 2026-10-27 | canva-ham/C12.png | KABUL (rapor.md) |
| C13 | 1 | MAHZMrenVrY | 2026-10-27 | canva-ham/C13.png | KABUL (rapor.md) |
| C14 | 1 | MAHZMtnkERI | 2026-10-27 | canva-ham/C14.png | KABUL (rapor.md) |
| C15 | 1 | MAHZMq8FB-s | 2026-10-27 | canva-ham/C15.png | KABUL (rapor.md) |
| C16 | 1 | MAHZMV2vMzc | 2026-10-27 10:00 | canva-ham/C16.png | KABUL (rapor.md) |
| C17 | 1 | MAHZMQUEnkg | 2026-10-27 10:00 | canva-ham/C17.png | KABUL (rapor.md) |
| C18 | 1 | MAHZMcBq1IA | 2026-10-27 10:00 | canva-ham/C18.png | KABUL (rapor.md) |
| C19 | 1 | MAHZMW-dF0U | 2026-10-27 10:00 | canva-ham/C19.png | KABUL (rapor.md) |
| C20 | 1 | MAHZMjxzZXc | 2026-10-27 | canva-ham/C20.png | KABUL (rapor.md) |
| C21 | 1 | MAHZMh_COeU | 2026-10-27 | canva-ham/C21.png | KABUL (rapor.md) |
| C22 | 1 | MAHZMuFI2-4 | 2026-10-27 | canva-ham/C22.png | KABUL (rapor.md) |

**Video başına Canva kullanımı (F10 raporu için):** üretilen = 23 (2026-10-27, dalga 1–3; kabul 21, red 2 = C11, C11b) / çekirdek plan 19 / tavan 27.

## 6. Denetim
`python3 -I araclar/prompt-kontrol.py canva-promptlari.md` → her Cxx: kimlik/kilit bloğu birebir, sayfa referansı (Leo'lu), yazı yasağı, aspectRatio, kabul ölçütü, id sırası. Çıktı: `araclar/prompt-kontrol-cikti.txt`.
