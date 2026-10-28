# Karakter kartı v2 (anlatıcı, 2D)

Karar (Niyazi, 2026-10-26): v1'deki 3D karakterin aynısı **2D**'ye çevrilir. v1 sayfası tasarım kaynağıdır.
**Ana 2D referans:** `karakter-sayfasi-2d-v1.png` (1536x1024, Niyazi, 2026-10-26) — görünüşler, 9 ifade (konuşma dahil), 9 poz (yürüme, koşma, konuşma, işaret, sunum, oturma, telefon, toplantı, düşünme), 6 sahne örneği. Stil: ince kontur + yumuşak gölgeli 2D illüstrasyon. Eksik: tek tek yüksek çözünürlüklü görseller, ağız şekilleri, ayrık parçalar.

Kaynak: `karakter-sayfasi-v1.png` (Niyazi, 2026-10-26). Adı: **Leo** (Niyazi kararı 2026-10-26; global kitle için kısa, her dilde aynı okunan ad; kurgusal çizgi anlatıcı, danışman değil). Görsel tanım aşağıdaki gibi kalır (tutarlılık için).
Bu kart her görsel/video üretim prompt'una **aynen** eklenir; tutarlılık buna bağlı.

## Tanım (prompt bloğu — İngilizce, modeller için)
2D cartoon character, flat cel-shaded illustration with clean bold black outlines and 2-tone shading (no 3D render, no gradients), Turkish man in his early 30s,
warm light-tan skin, short dark-brown hair with volume swept up and slightly to the side, thick dark eyebrows,
warm brown eyes, short well-groomed dark stubble beard and moustache, friendly confident half-smile.
Outfit (never changes): black button-up shirt with collar open at the neck and sleeves rolled to the forearm,
slim dark charcoal-grey chino trousers, clean white low-top sneakers, black wristwatch on the left wrist.
Slim athletic build, normal proportions (not chibi). Same design as the reference sheet, translated to 2D; consistent line weight.

## Renk paleti (sayfadan)
Siyah (gömlek) · koyu gri (pantolon) · açık ten · kahverengi (saç/göz) · kırık beyaz (ayakkabı).

## Sayfada hazır olanlar
- Görünüşler: ön, 3/4, yan, arka, diğer yan
- Yüz ifadeleri: doğal, mutlu, ciddi, şaşkın, kızgın, üzgün, düşünen, gülüşlü (göz kırpma)
- Pozlar: doğal duruş, yürüme, konuşma (el açık), oturma, işaret etme, sevinç, düşünme/stres

## Eksikler (üretilecek)
- Yüksek çözünürlük: sayfa 1254x1254; tek poz ~100x300 px → 1080p sahne için yetersiz. Her görünüş/poz ayrı, ≥2048 px, düz arka plan.
- Konuşma ağız şekilleri (A–H, X) ve göz kırpma — 2D rig için zorunlu.
- Finans jestleri: grafik gösterme, para sayma, telefona bakma, kafa kaşıma, omuz silkme, el ovuşturma.

## Stil notu
Karakter ve arka planlar aynı 2D dilde: kalın siyah kontur, cel-shading, detaylı mekân, soğuk arka plan + karakterin siyah gömleğini ayıran sıcak/açık ışık (referans-analizi.md).

## Canva karakter kilidi prompt'u (doğrulandı 2026-10-26, paket-v1)
Niyazi kararı: görsel gerçekçi/resimsi olabilir; şart her sahnede aynı karakter. Kaynak: Canva `generate-image`.
**Kazanan yöntem = "taban + düzenleme":** 1) karakter sayfası referansıyla bir taban poz üret, 2) diğer tüm poz/ifadeleri
TABAN görseli 1. referans + karakter sayfası 2. referans vererek "EDIT … ONLY CHANGE …" kalıbıyla üret.
Ölçüm (tools/gorsel/tutarlilik.py, taban a'ya göre): düzenleme ile üretilen 6 görselde kafa HSV histogram korelasyonu
0.84–0.96, ten ΔE ≤4.2, saç ΔE ≤1.3, gömlek ΔE ≤1.6, gövde piksel hizası (kafa dışı >30 fark) %0,2.
Aynı ifadeyi sıfırdan (yalnız kilit prompt + sayfa) üretmek: kafa korelasyonu **0.45**, ten ΔE 6.1 → yüz daralıyor, saç değişiyor → **ELENDİ**.

### 1) Taban prompt (yalnız referans: karakter sayfası, media `MAHZHpeQGdM`; aspectRatio LANDSCAPE_16_9)
```
CHARACTER LOCK (match the reference character sheet exactly): the same man as in the reference sheet — Turkish man in his early 30s, warm light-tan skin, short dark-brown hair with volume swept up and slightly to the side, thick dark eyebrows, warm brown eyes, short well-groomed dark stubble beard and moustache. Outfit never changes: black button-up shirt, collar open at the neck, sleeves rolled to the forearm, black wristwatch on the left wrist. Slim athletic build, normal proportions. STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, warm key light on the character.
SHOT: <kadraj ve poz>
BACKGROUND: <arka plan>, no text, no logos, no watermark. 16:9 landscape.
```
### 2) Düzenleme prompt'u (referanslar: [taban media, MAHZHpeQGdM]; aynı aspectRatio)
```
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: <tek değişiklik>. No text, no logos.
```
Kurallar: değişikliği tek cümlede, ölçülebilir yaz ("mouth clearly open in a tall oval 'aah' shape, NOT smiling");
"talking" tek başına gülümseyen ağız verir (b-alt). Kol/el hareketinde "body stays in the same place" ekle.

### paket-v1 (`assets/karakter/paket-v1/`, 1920x1080 PNG, doğal 1680x944; kaynak: Canva AI, Niyazi hesabı, Canva Kullanım Koşulları)
| Dosya | Canva media | Not |
|---|---|---|
| a-konusma-kapali.png | MAHZHqW0_Uo | taban; kameraya bakan bel üstü, ağız kapalı |
| b-konusma-acik.png | MAHZH81L8Ao | konuşma ağzı "aah" (dudak senkronu için a ile piksel hizalı) |
| b-alt-gulumseyerek-konusma.png | MAHZHuRDpgw | yedek: gülümseyerek konuşma |
| c-isaret.png | MAHZHgRhWHs | ekran soluna işaret (grafik gösterme) |
| d-saskin.png | MAHZHqQmUTY | şaşkın |
| e-dusunen.png | MAHZHnX32MM | düşünen, el çenede |
| f-sevincli.png | MAHZHh7qFXI | sevinçli, iki yumruk havada |
Elenen: d2 sıfırdan şaşkın (MAHZH_jDv78) — kafa kor. 0.45. Kontak: `paket-v1/kontak.jpg`; ölçümler: `paket-v1/tutarlilik.json`.
Tam çözünürlük indirme: `tools/gorsel/canva-indir.md`.
