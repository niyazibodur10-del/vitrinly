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

---

# Pilot klip v2 — doğru anlatıcı + müzik/efekt miksi (2026-10-26, ses-muhendisi → animasyon-yonetmeni)

**Neden v2:** v1 yanlış ses paketiyle yapılmıştı (`video/public/pilot-ses.wav` = Niyazi'nin kendi okuması `birlesik-v2`). Kesin karar anlatıcı **Kokoro-82M `am_fenrir`, hız 0.9**, cümle cümle + duraklamalı (`tools/ses/tts.py`) + `tools/ses/tts-son.sh` + CC0 müzik/efekt miksi (`tools/ses/miks.py`). Niyazi sesi pilottan çıkarıldı (yerel kopya: `uretim/ses-testi/ses/pilot-ses-v1-niyazi.wav`, git dışı).
Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[tahmin]** yorum.

Dosya: `pilot-v2.mp4` · 1920x1080 · 30 fps · H.264 · **14.1 sn** (v1 18.8 sn: TTS anlatım Niyazi'nin okumasından hızlı; 1.0 sn müzik girişi + 11.1 sn anlatım + 2.0 sn çıkış). Altyazı `pilot-v2.en.srt`. Thumbnail aynı.
Metin (pilotta kullanılan kısım, `okuma-metni.md` P01 + P02'nin ilk 3 cümlesi): `v2/pilot-metin.txt`.

## Ses zinciri
1. `tools/ses/tts.py v2/pilot-metin.txt ham.wav --ses am_fenrir --hiz 0.9` (Python 3.12 venv `~/.finansal-arac/kokoro-venv`, kokoro 0.9.4, torch 2.14 CPU) → `tools/ses/tts-son.sh` → `v2/anlatim-v2.wav` (git dışı) / `v2/anlatim-v2.m4a`, cümle zamanları `v2/anlatim-v2.zaman.json` (`"ses": "am_fenrir", "hiz": 0.9`).
2. `tools/ses/miks.py v2/anlatim-v2.wav assets/muzik/merak-unsolved-investigation-isaiah658.ogg ... --muzik-db -6 --duck-db 6 --giris 1.0 --cikis-sn 2.0` + 5 efekt (anlatıma göre sn @ dB): whoosh-uzun −0.8@−6 (giriş), pop-pluck 4.1@−6 ("cup"), whoosh-kisa 5.5@−6 (yüze yakınlaşma kesmesi), yazi-daktilo 7.3@−10 ("1923"), muhur-impact-punch 8.68@−5 ("Germany" mührü) → `v2/pilot-ses-v2.m4a` → WAV'a açılıp `video/public/pilot-ses.wav`. Hizalama ölçümü: anlatım (+1.0 sn) ile pilot-ses.wav arası çapraz korelasyon gecikmesi **0 ms** [ölçüm].
3. Kelime zamanları: Whisper medium.en (`v2/anlatim-v2-kelimeler.json`, ofset +1.0 sn). Ağız: Rhubarb 1.14.0 PocketSphinx + `--dialogFile`, **temiz anlatım** (+1.0 sn boşluk) üzerinde → `agiz-zamanlari.json`. `video/src/pilot/data.ts` ve SRT `v2/veri-uret.py` ile üretildi.

## Adaylar ve eleme [ölçüm]
| Aday | Ölçüm | Karar |
|---|---|---|
| A: varsayılan duraklama (cümle 0.30 / soru 0.40 / paragraf 0.65) | 11.08 sn, 143 kpm, WER %0, güven 0.980, f0 153 Hz | **seçildi**: Niyazi'nin kör testte seçtiği ayarın aynısı |
| B: soru 0.60 / paragraf 0.80 | 11.43 sn, 139 kpm, WER %0, güven 0.979 | elendi: ölçümde fark yok, karar verilen ayardan sapma |
| Müzik: Unsolved Investigation (merak) | miks −13.8 LUFS / TP −1.8, konuşma altı fark medyan **22.6 dB** (p10–p90 16.0–27.2), miks WER %0 | **seçildi**: 18–24 dB bandında, gizem tonu 1923 kancasına uygun |
| Müzik: 80s Mysterywave (gerilim) | −13.9 / −2.0, fark 25.3 dB (18.9–27.9), WER %0 | elendi: müzik bandın altında kalıyor (fazla kısık) |
| Rhubarb girdi: temiz anlatım | senkron korelasyonu 0.52, gecikme 1 kare | **seçildi** |
| Rhubarb girdi: müzikli miks | korelasyon 0.40, gecikme 1 kare | elendi: müzik tanıyıcıyı bozuyor |

## Remotion uyarlaması (`video/src/pilot/Pilot.tsx`)
`PILOT_SURE` 18.8 → **14.1**. Sahne sınırları (sn): sabah 0–2.8 · birikim 2.8–6.5 · şaşırma 6.5–8.0 · 1923 8.0–10.3 · final 10.3–14.1 (her kesme konuşma boşluğuna veya cümle sınırına denk). Kelime tetikleri `KELIME` sabitinde: fincan "cup" **5.10 sn**, mühür "Germany" **9.68 sn** (Whisper kelime başlangıcı, ses zamanı).

## Testler (son dosya `pilot-v2.mp4`) [ölçüm]
| Kapı | Sonuç |
|---|---|
| ffprobe | 1920x1080, 30/1 fps, h264 + AAC 48 kHz stereo, 14.10 sn ✅ |
| Ses (ebur128, son dosya) | **−13.8 LUFS**, true peak **−1.8 dBTP**, LRA 3.9 ✅ (−14 ±1, ≤ −1) |
| Siyah kare (blackdetect d=0.1, pix_th 0.10) | 0 ✅ |
| Dudak senkronu (`tools/senkron-testi.py` video + agiz-zamanlari.json) | en iyi gecikme **1 kare (33 ms)**, korelasyon 0.52 ✅ (≤2 kare) |
| Metin doğruluğu (Whisper medium.en, videonun sesi) | **WER %0** (26/26), ort. güven 0.976, düşük güvenli kelime 0 ✅ |
| Anlatıcı = am_fenrir | (1) TTS çıktısı `"ses": "am_fenrir", "hiz": 0.9` kaydıyla üretildi; (2) video sesi ile am_fenrir anlatım stem'i korelasyonu **0.985**, gecikme 0 ms; (3) anlatım perdesi **153 Hz** (TTS raporundaki fenrir 153 Hz; Niyazi'nin okuması 106 Hz) ✅ |
| Müzik konuşmanın altında | miks stem ölçümü medyan **22.6 dB** (p10 16.0); son videoda (video − anlatım artığı, efektler dahil) medyan **21.0 dB**, p10 12.7 (p10'u mühür/pop efektleri düşürüyor) ✅ |
| Altyazı | 6 blok, metin senaryo yazımıyla aynı, zamanlar Whisper'dan (aynı ses) ✅ |
| Kare kontrolü | `v2/kare-konusma-7.2sn.jpg` ("impossible", ağız D açık), `v2/kare-sessiz-13.0sn.jpg` (müzik çıkışı, ağız X kapalı), `v2/kare-muhur-9.9sn.jpg` (GERMANY mührü) ✅ |
| Yayın paketi | `yayin-paketi.json` ve `yayin-paketi-test.json` → pilot-v2.mp4 / pilot-v2.en.srt; `yukle.py --dry-run`: 0 hata (uyarı: 14 sn < 600 sn, test klibi için beklenen) ✅ |

## Bilinen sınırlar
- v1'deki görsel sınırlar aynen geçerli (büyütülmüş karakter, vektör ağızlar, hareketsiz kollar, kodla çizilmiş arka planlar).
- Final sahnede (10.3–14.1) son 2 sn yalnız müzik + kapalı ağız; gerçek videoda bir sonraki sahneye bağlanır [tahmin].
- Yayın paketinin açıklamasında CLAUDE.md'nin istediği "Narration voice is AI-generated" satırı yok (youtube-paketleyici alanı; bu işte yalnız dosya yolları değişti).
