# F0 — Ortam raporu (uretim-muhendisi, 2026-10-27 04:22–04:32 UTC)

**Sonuç: GEÇTİ.** Kurulum hatasız + idempotent, 3 kompozisyon listeleniyor, Pilot 2 karelik test render'ı var, Whisper çalışıyor.
Ortam: 4 vCPU, 15,7 GB RAM, disk 23 GB boş, konteyner yeni açılmış (uptime 1 dk; diskte araçlar/modeller hazırdı, sayfa önbelleği soğuktu).
Etiket: tüm süreler bu konteynerde ölçüldü [Ö]; paralel ajanlar (F1) aynı anda çalışıyordu, yük ort. 1,1–1,6.
Test çıktıları repo dışında: `/tmp/claude-0/-home-user-vitrinly/98cc376a-1af5-5176-856d-bb81c65c71b0/scratchpad/f0/`.

| # | Komut | Çıktı (özet) | Süre | Durum |
|---|---|---|---|---|
| 1 | `tools/kurulum.sh` (1. çalıştırma) | exit 0; `Hazır: RHUBARB=… PY=…/venv TTS_PY=…/kokoro-venv ESRGAN=…` | 19,2 sn | ✅ |
| 2 | `tools/kurulum.sh` (2. çalıştırma, idempotent) | exit 0, aynı çıktı | 1,3 sn | ✅ (kural ≤ 2 sn) |
| 3 | `tools/disk-durum.sh` | Disk boş 23 GB, RAM 15,3 GB kullanılabilir, 4 çekirdek; araçlar 3,5 GB, HF 2,2 GB, node_modules 664 MB | 4,9 sn | ✅ (> 5 GB eşiği) |
| 4 | `cd video && npx remotion compositions` | `Pilot 30 1920x1080 423 (14.10 sec)`, `PilotDikey 30 1080x1920 423`, `AgizTest Still` | 25,5 sn (soğuk) | ✅ |
| 5 | `tools/render-son.sh Pilot <scratch>/pilot-0-1.mp4 --frames=0-1` | **ilk deneme exit 222** (aşağıda) → düzeltme sonrası exit 0: h264 1920x1080 30 fps, 2 kare; AAC 48 kHz stereo; uyarı "ölçülen seviye -inf LUFS → normalizasyon atlandı" | 4,4 sn | ✅ (düzeltildi) |
| 5b | regresyon: `render-son.sh Pilot … --frames=60-119` | 60 kare, 2,0 sn; ebur128 **I −14,0 LUFS**, tepe −2,2 dBFS (normal yol bozulmadı) | 9,1 sn | ✅ |
| 6 | `kokoro-venv/bin/python tools/ses/tts.py metin.txt tts.wav --ses am_fenrir --hiz 0.9` | "Inflation quietly took fifteen percent of your savings. Here is how it happened." → 4,87 sn, 24 kHz mono, 2 cümle | 88,1 sn soğuk / **10,8 sn** sıcak | ✅ |
| 7 | `venv/bin/python tools/ses/yaziya-dok.py tts.wav w.json small.en` | "Inflation quietly took 15% of your savings. Here is how it happened." 13 kelime, kelime zamanlı (ör. Inflation 0,00–0,52 p 0,88) | 44,3 sn soğuk / **3,4 sn** sıcak | ✅ |
| 7b | aynı, `HF_HUB_OFFLINE=1` | aynı metin (ağsız çalışıyor) | 3,4 sn | ✅ |
| 7c | aynı, `medium.en` | aynı metin | 135,7 sn (soğuk, 1,5 GB model) | ✅ |
| 7d | bozuk girdiler: argümansız / olmayan dosya / bozuk WAV / 2 sn sessizlik | exit 1 kullanım / exit 1 "ses dosyası yok" / exit 1 "ffmpeg sesi çözemedi" / exit 0 + UYARI "ortalama güven < 0,3" (Whisper sessizlikte "You" uyduruyor, p 0,11) | — | ✅ |
| 8 | `rhubarb -f json --dialogFile metin.txt tts16.wav` | Rhubarb 1.14.0; 36 ağız işareti, şekiller A B C E F G H X, son işaret 4,83 sn | 10,4 sn | ✅ |
| 9 | `ffmpeg -version`; filtreler; `ebur128` | ffmpeg 6.1.1; loudnorm, ebur128, arnndn, highpass, deesser mevcut (5/5); TTS ham I −21,2 LUFS | 0,08 sn | ✅ |

## Whisper ("başarısız oldu" notu) — teşhis
- Bu konteynerde arıza **yeniden üretilemedi**: model önbelleği tam (small.en 484 MB, medium.en 1,53 GB, `.incomplete` yok), faster-whisper 1.2.1 / ctranslate2 4.8.4, ağlı ve ağsız çalışıyor.
- En olası neden [T]: yeni konteynerde ilk yükleme disk soğukken çok yavaş (small 44 sn, medium 136 sn; sıcakta 3,4 sn) → kısa zaman aşımı olan çağrı ya da oturum kesilmesi "başarısız" gibi göründü; ayrıca betik hata mesajı vermiyordu.
- Düzeltme (`tools/ses/yaziya-dok.py`): model önce yalnız yerel önbellekten yüklenir (`local_files_only=True`, yoksa indirir) → ağ/proxy beklemesi yok; argüman/dosya/ffmpeg hatalarında açık mesaj + exit 1; boş veya düşük güvenli (halüsinasyon) transkriptte uyarı. Çıktı biçimi değişmedi (eski ve yeni JSON birebir aynı, test 7).
- Öneri (çağıran ajanlara): yeni konteynerde ilk Whisper çağrısına ≥ 3 dk zaman aşımı verin.

## Bulunan ikinci arıza — `tools/render-son.sh`
- 2 karelik render'da (0,07 sn ses, ebur128'in 0,4 sn penceresinden kısa) loudnorm ölçümü `input_i=-inf` döndü, ikinci geçiş "measured_I out of range" ile düştü (exit 222).
- Adaylar: (a) ölçülemezse normalizasyonu atla + uyarı, (b) tek geçiş dinamik loudnorm, (c) hata verip dur. **Kazanan (a)**; (b) sessiz/kısa seste sessizce yanlış seviye üretir, (c) önizleme/test render'larını gereksiz kırar. Normal yol değişmedi (test 5b: −14,0 LUFS).

## Değişen dosyalar
- `tools/ses/yaziya-dok.py`, `tools/render-son.sh`, bu rapor, `.claude/agents/hafiza/uretim-muhendisi.md`.
