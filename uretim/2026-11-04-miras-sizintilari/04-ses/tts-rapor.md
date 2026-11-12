# F4 ses — TTS + ses mühendisliği raporu (ses-yonetmeni, 2026-11-04)
İLERLEME: tamam
SONUÇ: GEÇTİ — anlatım 13:01.4, WER %1.0 (yeniden üretilebilir telaffuz hatası 0), −14.2 LUFS / TP −1.5, hiza p95 6/15 ms, Rhubarb 31 sahne.
| Kapı | Ölçüm [ölçüm] | Hedef | Sonuç |
|---|---|---|---|
| WER tüm dosya (`hata-orani.py referans-metni.txt kelimeler.json`) | %1.0 (22/2225); sahne toplamı (`olc.py`) %1.80 | ≤ %10 | GEÇTİ |
| Ses yüksekliği (ffmpeg ebur128 peak=true) | wav −14.2 LUFS, TP −1.5, LRA 2.1 · m4a −14.2 / −1.1 | −14 ±1, TP ≤ −1 | GEÇTİ |
| Süre / biçim | 781.4 sn (13:01), 48 kHz mono 24-bit; 169 kpm (metin tahmini 13:46 → −44.6 sn) | ≥ 10 dk | GEÇTİ (pay 3:01) |
| Hiza (`hiza-dogrula.py`) | baş p95 6 ms (maks 8), son p95 15 ms (maks 29); 260 cümle | p95 ≤ 150 ms | GEÇTİ |
| Shorts ek kayıtları | S1 36.6 sn WER %1.0 (yalnız "Cerulli"→"Cerule" yazımı) · S2 20.0 sn WER %0 · ikisi −14.2 LUFS, TP −1.5/−1.4 (m4a −1.3/−1.4) | ≤ %10 | GEÇTİ |

Metin: `03-metin/metin.md` v1.1 sha256 22ba68b7750c (31 sahne, 260 cümle, 2.203 kelime). Ses: Kokoro-82M `am_fenrir` 0.9, `tools/ses/tts.py --is 2` (0.30/0.40/0.65) → `tools/ses/tts-son.sh`. Tek aday: kanal ses kararı + 2026-11-02 F4 zinciri ilk seferde geçti.

## Teslim (04-ses/) — sha256 ilk 12
`anlatim.wav` (git dışı) 485cf2e03ce0 · `anlatim.m4a` bfc14fe1c80a · `anlatim-ham.zaman.json` (260 cümle) · `sahne-zamanlari.json` 056b15d8c953 (31 sahne, kesme noktaları) · `kelimeler.json` 9ae1d0f760f1 (Whisper small.en) · `kelimeler-hizali.json` 594d9ceac983 (whisper 2176 / bolme 20 / ara 7) · `altyazi-remotion.json` · `altyazi-taslak.en.srt` 94f6fdadadf7 (296 blok, ≤42 kr, ≤5.5 sn, çakışma 0, >21 kr/sn 20 blok, >25 0) · `rhubarb/` (S01–S31 16 kHz wav + txt + sahneler.json) · `shorts-1-ek.*` f47267a88f9b (m4a) · `shorts-2-ek.*` 3151dc6f49a1 · sahne tablosu `olc-cikti.txt`.

## Telaffuz testi (cümle tek başına Whisper, `tools/ses/cumle-whisper.py`; dosyalar `telaffuz-testi/test1–4`) [ölçüm]
| Kelime / cümle | Varsayılan | Adaylar (sonuç) | Kazanan |
|---|---|---|---|
| Cerulli (×6 + Shorts 1) | /sˈɛɹʌli/ "SER-uh-lee" → "Sarily" 0.40 (vurgu yanlış) | /səɹˈuli/ "Cerule" · /ʧəɹˈuli/ "Cherouli" · /sɛɹˈuli/, /səɹˈuːli/ "Cerule" · /səɹˈulˌi/ "Cerule" 0.60 | `/səɹˈulˌi/` suh-ROO-lee |
| Okafors (×5) | /ˈɑkəfˌɔɹs/ → "Aka Force" | /Okˈɑfɔɹz/ 1/3 ("O 'Coffers", "Okafwars") · /Okˈɑfˌɔɹz/ 3/3 "Okafors" | `/Okˈɑfˌɔɹz/` oh-KAH-fors |
| Cümle 67 "Stop two is care." | tam + tek başına "Stop to his care" | `[two](/tˈu/) [is](/ˈɪz/)` "Stop 2 is care" 0.74 · `[is](+2)` aynı 0.72 | IPA (`ekle-cumle.py` ile eklendi) |
| CareScout, Medicare, Medicaid, Gen X, millennials, U.K., two-fifths, Fed | doğru (0.78–1.00) | — | düz bırakıldı |
"Cerulli" Whisper sözlüğünde yok: `initial_prompt="Cerulli Associates…"` ile 9/9 aday "Cerulli" yazıldı (varsayılan dahil) → ASR ayırt etmiyor; karar vurgu kuralıyla (İtalyanca ve Amerikanlaşmış iki okunuşta da vurgu "ROO"da). Firmanın kendi okunuşu doğrulanamadı [arama özeti: yalnız soyadı için İtalyanca "chai-ROOL-lee"]. Hepsi yalnız telaffuz işareti (`okuma-hazirla.py` TELAFFUZ, regex); `referans-metni.txt` = kilitli metin.

## Kalan farklar (sınıflandırma) [ölçüm + yorum]
- ASR yazımı / eşsesli / normalizasyon: Cerulli→Cerule (×6), heirs→airs/Ayres (×2), U.S./U.K.→US/UK, ",000"→"zero" token (×4), "%" sonrası percent silinmesi (×4), grey→gray, "To: the kids"→"two of".
- Whisper uydurma (hizalayıcı attı): "care." 3:20.7 p 0.006 (cümle 67 sonrası tekrar), "Last," 6:57.5 p 0.026 (cümle 137 tek başına doğru).
- Eş-sesletim (tek başına da tekrarlıyor, 3'er varyant denendi, düzelmedi): 191 "picked taxes"→"pick" (/t/+/t/ birleşmesi), 211 "I open the doors"→"opened" (/n/+/ð/). İnsan okumasında da aynı birleşme olur; içerik hatası değil, düz bırakıldı.
- Yeniden üretilebilir içerik hatası: 0.

## Sonraki ajanlara not
- animasyon-yonetmeni / kurgu-editoru: ses metin tahmininden 44.6 sn kısa (169 kpm); sahne süreleri `sahne-zamanlari.json`'dan (S13 −4.1, S14 −5.6, S19 −4.8, S24 −4.4, S27 −4.7 sn en çok kısalanlar). ABONE noktaları sahne başlarına bağlı: S06 1:46.3, S18 ve S31 başları dosyada.
- kurgu-editoru: SRT taslağı kilitli metin yazımıyla (sayılar yazıyla); rakamlı son SRT'de kr/sn düşer. "ara" (tahmini) zamanlı 7 kelime hepsi "dollars/pounds" (Whisper "$" içine katıyor), akustik kapı etkilenmedi.

## Yeniden üretim
`anlatim.wav`, `shorts-k-ek.wav`: m4a'dan (`ffmpeg -i anlatim.m4a -ar 48000 -ac 1 -c:a pcm_s24le anlatim.wav`; kilitli sürüm git'teki m4a). Rhubarb wav'ları: `python3 -I tools/ses/rhubarb-hazirla.py --dizin uretim/2026-11-04-miras-sizintilari/04-ses`.
Sıfırdan (Kokoro deterministik değil): `okuma-hazirla.py` → `kokoro-venv/bin/python tools/ses/tts.py okuma-metni.txt anlatim-ham.wav --ses am_fenrir --hiz 0.9 --is 2` (5:20 dk) → `tts-son.sh anlatim-ham.wav anlatim.wav anlatim.m4a` → `yaziya-dok.py --model small.en --is 2 anlatim.wav kelimeler.json shorts-1-ek.wav shorts-1-ek.json shorts-2-ek.wav shorts-2-ek.json` (2:40 dk) → `olc.py` → `tools/ses/hizala.py --dizin .` → `hiza-dogrula.py --dizin .` → `rhubarb-hazirla.py --dizin .`. Metin değişirse yalnız etkilenen cümle: `tts.py` ile o cümle → `ekle-cumle.py anlatim-ham.wav anlatim-ham.zaman.json <i> <kaynak.wav> <kaynak.zaman.json> <j>` → tts-son'dan itibaren.
