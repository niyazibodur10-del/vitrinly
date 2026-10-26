# Pilot klip v1 — rapor (2026-10-26)

Dosya: `pilot-v1.mp4` · 1920x1080 · 30 fps · H.264 · 18.8 sn · ses `birlesik-v2` 2.6–21.4 sn.
Kaynak kod: `video/src/pilot/` (Remotion 4.0.539). Render: `tools/render-son.sh Pilot <çıkış>`.

## Ne var
1. Sabah odası + konuşan karakter (dudak senkronu, göz kırpma, nefes/baş hareketi, yavaş yaklaşma)
2. "Savings → a cup of coffee" grafiği (birikim destesi erir, fincan "cup" kelimesinde gelir), köşede konuşan karakter
3. "Sounds impossible?" yüze ani yakınlaşma + sarsıntı
4. 1923 eski kâğıt kartı + "GERMANY" mührü ("Germany" kelimesinde)
5. "That's exactly what happened" — kararan ışık, yaklaşma
Altyazı: kelime kelime, anahtar kelime sarı (referans videodaki stil).

## Testler
| Kapı | Sonuç |
|---|---|
| Çözünürlük/fps/süre (ffprobe) | 1920x1080, 30 fps, 18.8 sn ✅ |
| Ses (ebur128, son dosya) | −13.8 LUFS, tepe −3.9 dBFS ✅ |
| Siyah kare (blackdetect) | 0 ✅ |
| Dudak senkronu (`tools/senkron-testi.py`) | en iyi gecikme 1 kare (33 ms) ✅ (kapı ≤2 kare) |
| Ağız şekilleri görsel kontrol (`AgizTest` kompozisyonu) | 9 şekil yüz üzerinde ✅ |

## Bilinen sınırlar (gerçek videodan önce çözülecek)
- Karakter görseli düşük çözünürlüklü sayfadan ×4 büyütüldü; yakın planda yumuşak. Yüksek çözünürlüklü tek görsel (E0) gelince keskinleşir.
- Ağızlar vektör çizim: çizim stiliyle %100 aynı değil. E1–E9 ağız görselleri gelince karakterin kendi ağızları kullanılacak.
- Kollar/eller hareket etmiyor (tek görsel). Jest pozları (E11–E14) gelince eklenecek.
- Sahne arka planları kodla çizildi (sade). Gerçek videoda sahne illüstrasyonları görsel model ile üretilecek (bütçe onayı gerekli).
- İlk ses ölçümü stereo/mono farkı nedeniyle −10.6 LUFS çıktı → son normalizasyon artık render betiğinde.
