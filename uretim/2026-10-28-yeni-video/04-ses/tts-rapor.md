# F4 ses — TTS + hizalama raporu (ses-yonetmeni, 2026-11-02)
İLERLEME: tamam
SONUÇ: GEÇTİ — anlatım 11:18.2, WER %1.4 (gerçek telaffuz hatası 0), −14.2 LUFS / TP −1.5, hiza p95 5/15 ms, Rhubarb girdileri 27 sahne.
| Kapı | Ölçüm [ölçüm] | Hedef | Sonuç |
|---|---|---|---|
| WER tüm dosya (`hata-orani.py referans-metni.txt kelimeler.json`) | %1.4 (26/1867); sahne toplamı (`olc.py`) %3.05 | ≤ %10 | GEÇTİ |
| Ses yüksekliği (ffmpeg ebur128) | wav −14.2 LUFS, TP −1.5, LRA 2.0 · m4a −14.2 / −1.3 | −14 ±1, TP ≤ −1 | GEÇTİ |
| Süre / biçim | 678.2 sn (11:18), 48 kHz mono 24-bit; 166 kpm (tahmin 11:44 → −26 sn) | ≥ 10 dk | GEÇTİ (pay 78 sn) |
| Hiza (`hiza-dogrula.py`) | baş p95 5 ms, son p95 15 ms (maks 444/922 ms, cümle 93) | p95 ≤ 150 ms | GEÇTİ |
| Shorts ek kayıtları | S1 12.3 sn WER %5.6 (yalnız "U.S."→"US" yazımı), S2 15.3 sn WER %0; ikisi −14.2 LUFS, TP −1.5 | ≤ %10 | GEÇTİ |

Ses: Kokoro-82M `am_fenrir` 0.9, cümle cümle (`tools/ses/tts.py --is 2`, duraklama varsayılanları 0.30/0.40/0.65) → `tools/ses/tts-son.sh`. Tek aday: kanal ses kararı + 1929 F4 yöntemi.
Kanal adı ve "FY" anlatımda geçmiyor (kilitli metin); "trillion" (1), "percent" (8), tüm sayılar tam dosya Whisper'ında hatasız.

## Teslim (04-ses/)
`anlatim.wav` (git dışı) / `anlatim.m4a` sha256 acb373260297 / d76d46f47c7b · `anlatim-ham.zaman.json` (211 cümle) · `sahne-zamanlari.json` (27 sahne, kesme noktaları) · `kelimeler.json` (Whisper small.en, 5fa11c28fe4c) · `kelimeler-hizali.json` 3565ea88c5e8 · `altyazi-remotion.json` · `altyazi-taslak.en.srt` f78cf50d5eae (240 blok, ≤42 kr, ≤5.3 sn, çakışma 0) · `rhubarb/` (Sxx.wav 16 kHz + Sxx.txt + sahneler.json) · `shorts-1-ek.*`, `shorts-2-ek.*` · sahne tablosu `olc-cikti.txt`.

## Telaffuz testi ve düzeltmeler (cümle tek başına Whisper, `tools/ses/cumle-whisper.py`) [ölçüm]
| Cümle | v1 hata | Adaylar (sonuç) | Kazanan |
|---|---|---|---|
| 121 "Thing one: it borrows…" | "barfs" 0.97 (tekrarlı) | `/bˈɑɹOz/` barfs · `+2` barfs · virgül borrows (noktalama değişir) · `/bˈɔɹˌOz/` borrows 0.98 | `/bˈɔɹˌOz/` |
| 172 "on the fridge as A" | "fridges A" | `[fridge](/fɹˈɪʤ/) [as](/ˈæz/)` 0.97/0.95 · `[as](+2)` 0.97/0.96 | fonetik |
| 105 "change an old debt" | "in old" 0.74 | `[an](/ˈæn/)` an 0.67 · `+2` in 0.72 | fonetik (cümle değiştirildi, `ekle-cumle.py`) |
| 198 "A, B, or C: which…" | "Of" 0.15 (artikel /ə/) | `[A](/ˈA/)` A 0.87 · `+2` A 0.33 | fonetik (cümle değiştirildi) |
| 186 "old debt smaller… buy less" | "debts"/"by" | `/dˈɛt/`, `+2`, `/dˈɛtʰ/` hepsi "debts" | düz bırakıldı: t+s birleşmesi ASR artığı, buy/by eşsesli |
Hepsi yalnız telaffuz işareti (`okuma-hazirla.py` TELAFFUZ); görünen kelime aynı, `referans-metni.txt` = kilitli metin. Varyant dosyaları `telaffuz-testi/`.

## Kalan farklar (sınıflandırma) [ölçüm + yorum]
- Eşsesli / normalizasyon: brakes→breaks, brake→break, buy→by, World War Two→"II" (×2), securities, Envelope four→"for" (tek başına "4" 0.71), plane(s).
- Whisper uydurma (p < 0.2): "5.", "hip.", "However," — hizalayıcı attı.
- Whisper atlaması: cümle 93 "So inside the borrowed envelope, there's another interest envelope." tam dosyada yazılmadı; tek başına çözümde 9/9 doğru (0.72–1.00) → ses doğru; hizalı zamanları **ara** (tahmini, 0.35 sn adım, 295.5–298.6 sn).
- Bağlam: debt→debts, cost→costs (tek başına doğru). Yeniden üretilebilir içerik hatası: 0.

## Sonraki ajanlara not
- kurgu-editoru: SRT taslağında 24 blok >21 kr/sn, 3 blok >25 (en yüksek 32.8, #56 "About one thousand six hundred dollars."). Hepsi yazıyla sayı → son SRT'de rakam ("$1,600") yazılınca düşer. Cümle 93 kelime zamanları tahmini: son kapıda render Whisper'ı ile bak.
- animasyon-yonetmeni: Rhubarb ofsetleri `rhubarb/sahneler.json`; sahne süreleri `sahne-zamanlari.json` (metin tahmininden S01–S03 1–2 sn kısa).
- `tools/ses/hizala.py` düzeltildi (uretim-muhendisi'ne bilgi): ilk kelime Whisper'da 0 sn süreli ve >0.4 sn geç gelirse assert düşüyordu (S10 "Americans"); artık <60 ms ilk kelime TTS sınırına oturuyor. `unittest test_ses_hizalama test_hata_orani` 11/11 OK, 2 koşu aynı sha256.

## Yeniden üretim
`anlatim.wav`, `shorts-k-ek.wav`: m4a'dan (`yeniden-uret.adimlar`). Rhubarb wav'ları: `python3 -I tools/ses/rhubarb-hazirla.py --dizin uretim/2026-10-28-yeni-video/04-ses`.
Sıfırdan: `okuma-hazirla.py` → `tts.py okuma-metni.txt anlatim-ham.wav --ses am_fenrir --hiz 0.9 --is 2` → `tts-son.sh anlatim-ham.wav anlatim.wav anlatim.m4a` → `yaziya-dok.py --model small.en` → `hizala.py` → `hiza-dogrula.py` → `rhubarb-hazirla.py` (Kokoro deterministik değil; kilitli sürüm git'teki m4a).
