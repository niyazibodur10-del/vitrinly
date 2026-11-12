# Kanal görselleri için Canva prompt'ları (banner + profil)

Hazırlayan: thumbnail-tasarimcisi, 2026-10-26. Canva çağrılarını koordinatör yapar (bağlayıcı alt ajanda yok).
Yöntem: `assets/karakter/karakter-karti.md` içindeki **taban + düzenleme** kalıbı (sıfırdan üretim elendi: kafa korelasyonu 0.45).
Referanslar: taban `MAHZHqW0_Uo` (paket-v1 a), karakter sayfası `MAHZHpeQGdM`. aspectRatio: `LANDSCAPE_16_9` (bu dosyada doğrulanmış tek değer budur; kare seçenek varsa profil için o kullanılabilir, yoksa 16:9 üretilip kodla kırpılır).
**Görsellere metin yazdırılmaz.** Kanal adı, slogan ve ritim `tools/gorsel/kanal-gorselleri.py` ile kodla yazılır.
Çıktılar `uretim/kanal-kimligi/kaynak/` klasörüne konur. Tam çözünürlük için `tools/gorsel/canva-indir.md` izlenir (1680x944 → 1920x1080 export).

Not: Mevcut çalışan sürüm Canva üretimi gerektirmiyor. Paket-v1'deki `f-sevincli.png` (banner) ve `a-konusma-kapali.png` (profil) yeterli oldu. Aşağıdakiler isteğe bağlı iyileştirmeler. Her biri 1 yapay zekâ hakkı harcar (abonelik dahilinde, ek ücret yok).

## K1: Banner karakteri, kollar kavuşturulmuş ve kendinden emin (isteğe bağlı alternatif poz)
Referanslar `[MAHZHqW0_Uo, MAHZHpeQGdM]`, LANDSCAPE_16_9.
```
EDIT the first reference image. Keep EVERYTHING identical: same man, same face, same hair, same beard, same black shirt with rolled sleeves, same black wristwatch on left wrist, same framing and camera distance, same body position, same plain slate-blue background, same lighting and same 2D cartoon cel-shaded style with bold outlines. The second reference is the character model sheet; the face must match it. ONLY CHANGE: arms are crossed confidently over the chest at the same height as now, warm closed-mouth confident smile; body stays in the same place. No text, no logos.
```
Neden: kavuşturulmuş kollar göğüs hizasında kalır. Böylece mobil güvenli bantta (y 508–931) yarım kesilen el görünmez. Mevcut sürüm bu sorunu karakteri büyütüp yumrukları bandın altına indirerek çözüyor.
Kullanım: `--banner-karakter uretim/kanal-kimligi/kaynak/k1-kollar-kavusuk.png`

## K2: Banner arka planı, karaktersiz şehir ve yükselen grafik (isteğe bağlı; kod arka planının yerine)
Referans `[MAHZHpeQGdM]` (yalnız stil için), LANDSCAPE_16_9.
```
STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, same drawing style as the reference sheet. NO people, NO characters.
SHOT: wide cinematic city skyline at dusk seen from a rooftop, deep navy-blue sky (#0B1630 to #13284D), cool blue buildings with a few warm yellow lit windows, a large glowing green stock-market line chart rising from the lower left to the upper right across the whole sky, ending with an arrow; the left 40% of the frame is calmer and darker (space for a character), the middle band is uncluttered (space for a title).
BACKGROUND: no text, no numbers, no logos, no watermark. 16:9 landscape.
```
Kullanım: `--arkaplan uretim/kanal-kimligi/kaynak/k2-sehir.png`. Betik görseli 2560x1440'a kaplar ve metin kontrastı için %35 lacivert ile karartır. Kontrast ölçümü `olcumler.json`'da yeniden yapılır. Hedef: en kötü %5 ≥ 4.5:1.
Büyütme: 1920x1080 export → Real-ESRGAN x4 → 2560x1440'a küçültülür (`tools/karakter/buyut.py`). Tek başına LANCZOS ile x1,33 büyütme kabul edilebilir ama daha yumuşak sonuç verir.

## K3: Profil, yakın plan kafa ve omuz (isteğe bağlı; daha keskin profil için)
Referanslar `[MAHZHqW0_Uo, MAHZHpeQGdM]`, LANDSCAPE_16_9. Taban kalıbı kullanılır, çünkü kadraj değişiyor ve "same framing" kuralı burada uygulanamaz.
```
CHARACTER LOCK (match the reference character sheet exactly): the same man as in the first reference image and the reference sheet — Turkish man in his early 30s, warm light-tan skin, short dark-brown hair with volume swept up and slightly to the side, thick dark eyebrows, warm brown eyes, short well-groomed dark stubble beard and moustache. Outfit never changes: black button-up shirt, collar open at the neck. STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows, warm key light on the character.
SHOT: tight head-and-shoulders close-up, face centered horizontally, looking straight into the camera, friendly confident closed-mouth half-smile, head fills the upper two thirds of the frame, top of the hair fully visible with a little space above.
BACKGROUND: plain flat slate-blue background (#3D597A), no text, no logos, no watermark. 16:9 landscape.
```
Kabul testi (zorunlu): `tools/gorsel/tutarlilik.py` ile taban `a`'ya karşı kafa korelasyonu ≥ 0.84 ve ten ΔE ≤ 4.2 olmalı. Ölçüt karakter kartından alındı. Altında kalırsa elenir ve paket-v1 kırpması kullanılmaya devam eder.
Kullanım: `--profil-karakter uretim/kanal-kimligi/kaynak/k3-yakin-plan.png` (kafa tepesi ve ortalama otomatik bulunur).

## Yeniden üretim komutu
```
~/.finansal-arac/venv/bin/python tools/gorsel/kanal-gorselleri.py \
  --ad "FINANCIAL RISE" --banner-karakter <png> --profil-karakter <png> [--arkaplan <png>] \
  --kazanan-banner A-s2 --kazanan-profil P4
```
