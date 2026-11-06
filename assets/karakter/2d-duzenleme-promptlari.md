# 2D karakter — düzenleme (edit) prompt'ları v2

> Not (2026-10-26, Niyazi kararı): varsayılan üretim yolu **Canva bağlayıcısı** (`generate-image`, referans = karakter sayfası; ek ücret yok; çağrıları koordinatör yapar, prompt ve değerlendirme gorsel-varlik-sanatcisi). Aşağıdaki prompt'lar Canva için de girdi olarak kullanılır; sohbet uygulamasıyla elle üretim yalnız yedek yoldur. Ücretli görsel API kullanılmıyor.

Neden: sohbet modelleri istenen her şeyi tek bir sayfaya sıkıştırıyor (1264x843, ağızlar karakterin yüzüne/sakalına uymuyor,
ayaklar çıplak). Rig için **aynı görselin sadece bir yeri değişmiş kopyaları** gerekiyor. Bunu en tutarlı yapan yöntem:
tek ana görsel üret, sonra **aynı sohbette** onu düzenlet. Değişen bölgeyi ben otomatik keserim (fark maskesi).

Kurallar: Gemini uygulaması (Nano Banana) veya ChatGPT. Her adımda **bir önceki çıktıyı** düzenlet. Her çıktıyı ayrı indir,
dosya adını aşağıdaki gibi koy. Yeni sohbet sadece E0'da.

## E0 — Ana görsel (yeni sohbet, `karakter-sayfasi-2d-v1.png` ekle) → `E0-ana.png`
Extract only the "KONUŞMA" (talking) figure from this sheet and redraw it as a single standalone image:
same 2D character, waist-up, front view facing the camera, both hands relaxed and visible, mouth closed, neutral friendly expression,
plain flat light-grey background (#E6E6E6), character centered, 16:9, highest possible resolution.
Single image only. No text, no labels, no other panels.

## E1–E9 — Ağızlar (aynı sohbet, her seferinde E0'ı düzenlet) → `E1-agiz-A.png` ... `E9-agiz-X.png`
Şablon: "Edit the previous image. Change ONLY the mouth to: <ŞEKİL>. Keep everything else exactly identical:
same pose, same framing, same size, same position, same background, same beard, same eyes. Single image, no text."
- E1 A: lips closed and pressed together (M, B, P)
- E2 B: mouth slightly open, teeth together and visible (K, S, T, Z)
- E3 C: mouth open, relaxed (E, I)
- E4 D: mouth wide open (A)
- E5 E: rounded open mouth (O, Ö)
- E6 F: small rounded pucker (U, Ü, V)
- E7 G: upper teeth touching lower lip (F)
- E8 H: mouth open with tongue tip behind upper teeth (L)
- E9 X: relaxed closed mouth at rest

## E10–E14 — Göz ve jestler (aynı sohbet, E0'ı düzenlet)
- E10 `E10-goz-kapali.png`: "Change ONLY the eyes to closed (blink). Keep everything else exactly identical."
- E11 `E11-isaret.png`: "Change ONLY the right arm: pointing to the right side of the frame. Keep everything else identical."
- E12 `E12-acik-eller.png`: "Change ONLY the arms: both palms open, explaining gesture. Keep everything else identical."
- E13 `E13-sasirma.png`: "Change ONLY the facial expression to surprised (raised eyebrows, wide eyes), mouth closed. Keep everything else identical."
- E14 `E14-dusunme.png`: "Change ONLY the right hand: on the chin, thinking. Keep everything else identical."

## Kontrol
İki görseli üst üste koyduğunda yalnız istenen bölge değişmiş olmalı. Karakter kaymış/büyümüşse aynı prompt'u
"the framing moved, keep it pixel-identical" ekleyerek tekrarlat.
