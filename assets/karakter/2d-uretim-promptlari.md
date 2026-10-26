# 2D karakter üretim prompt'ları (v1)

Kullanım: Gemini uygulaması (Google AI Pro aboneliğin) veya ChatGPT'de **yeni sohbet** aç, `karakter-sayfasi-v1.png`'yi ekle,
prompt'u aynen yapıştır. Her çıktıyı en yüksek çözünürlükte indir ve bana gönder. Ek ücretli servis gerekmez.
Sıra önemli: önce P1; beğenince P2–P4'te P1 çıktısını da referans olarak ekle.

## P1 — 2D karakter sayfası (ana referans)
Redraw this exact character as a 2D cartoon character. Keep everything identical: face shape, dark-brown swept hair,
thick eyebrows, brown eyes, short stubble beard, black button-up shirt with open collar and sleeves rolled to the forearm,
dark charcoal chinos, white sneakers, black watch on the left wrist, slim athletic proportions.
Style: flat 2D cel-shaded illustration, clean bold black outlines, 2-tone shading, no 3D rendering, no gradients, no texture,
modern adult-animation look. Layout: character turnaround on plain light-grey background — front, 3/4, side, back —
full body, same scale, evenly spaced, no text, no labels. Square image, highest resolution.

## P2 — Konuşma pozu (en çok kullanılacak görsel)
Same 2D character from the reference, front view facing the camera, waist-up, neutral friendly expression,
mouth closed, arms relaxed at the sides, plain flat light-grey background, centered, no text.
Same line weight and colors. Highest resolution, 16:9.

## P3 — Ağız şekilleri (dudak senkronu)
Same 2D character, close-up of the head only, front view, identical in every image except the mouth.
A grid of 9 heads on plain light-grey background, one per mouth shape, no text:
1) closed mouth relaxed (M, B, P) 2) slightly open, teeth together (K, S, T) 3) open mouth (E, A short)
4) wide open (AA) 5) rounded open (O) 6) small rounded pucker (U, W) 7) upper teeth on lower lip (F, V)
8) tongue slightly visible behind teeth (L) 9) neutral rest mouth.
Eyes, eyebrows, head angle and hair must not change between the 9 heads.

## P4 — Ayrık parçalar (rig için)
Same 2D character, front view, T-pose-like neutral stance, drawn as SEPARATE body parts laid out apart from each other
on a plain light-grey background with space between every part, no overlap, no text:
head without mouth, hair, torso with shirt, upper left arm, lower left arm, left hand open, left hand pointing,
upper right arm, lower right arm, right hand open, right hand fist, left leg, right leg, left sneaker, right sneaker,
eyes open, eyes closed (blink), eyebrows neutral, eyebrows raised, eyebrows angry.
Same line weight and colors as the reference.

## Kontrol (bana göndermeden önce)
- Yüz v1 sayfasındaki adama benziyor mu? Saat sol bilekte mi? Kıyafet aynı mı?
- Yazı/etiket yok mu? Arka plan düz mü?
Uymayan çıktıyı "keep the character identical to the reference" ekleyerek yeniden ürettir.
