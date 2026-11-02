# Durum — 2026-10-28-yeni-video

- **Tetik:** (kim, ne zaman, UTC)
- **Kanal:** Toonomy (@toonomy), anlatıcı Leo.
- **Slot ve sütun:** Çar 2026-11-04 12:00 ET (17:00 UTC) · B güncel haber · K3 (F9 ONAY ≤ 2026-11-03 17:00 UTC) kaçarsa Paz 2026-11-08 12:00 ET (hakem, `02-senaryo/senaryo-karari.md` §5)
- **Konu:** S08 The Kitchen Table Budget (yedek S06) · kontrol noktaları K1 F3 kilidi ≤11-02 16:00 · K2 F7 ≤11-03 10:00 · K3 F9 ≤11-03 17:00 UTC
- **Stok:** uzun ? / Shorts ?
- **Kod:** video/src/videolar/yeni-video/ · kompozisyon öneki ?
- **Yeniden üretim:** `tools/yeniden-uret.sh 2026-10-28-yeni-video` (tarif: yeniden-uret.adimlar)

| Adım | Sahip | Durum | Teslim | Test kanıtı | Başlangıç–bitiş (UTC) |
|---|---|---|---|---|---|
| F0 açılış | koordinatör | GEÇTİ | durum.md | commit 10-28 10:20 (slot Çar 11-04 B; yedek Paz 11-08) | 10-28 10:20 |
| F0 ortam | uretim-muhendisi | RAPOR YOK | 00-ortam/ortam-raporu.md | 00-ortam/ boş; F3'ten önce `tools/kurulum.sh` kanıtı gerekli (hakem notu) | |
| F1 konu havuzu | trend-avcisi | GEÇTİ | 01-arastirma/konu-havuzu.md | kaynak kapısı GEÇTİ (26 konu, B17/A6/C3) | 10-28 –10:41 |
| F1 rakip özeti | kanal-analisti | GEÇTİ | 01-arastirma/rakip-ozet.md | 30 gün delta [API], ham veri sha256 ba4f87c23718 | 10-28 –10:26 |
| F2 senaryolar | senaryo-yazari | GEÇTİ | 02-senaryo/senaryolar.md | senaryo-kontrol v2 exit 0, 2 koşu aynı (12 senaryo) | 10-28 –10:51 |
| F2 viralite / ön doğrulama / politika | viralite-analisti ‖ finans-dogrulayici ‖ monetizasyon-uyum-uzmani | GEÇTİ | 02-senaryo/ | viralite 2 koşu sha256 dab7ffb8050d · doğrulama Y3/S7/K2 · politika 8Y/4S/0K, 2 koşu aynı | 11-02 –04:27 |
| F2 karar | hakem | GEÇTİ | 02-senaryo/senaryo-karari.md | KAZANAN S08 / YEDEK S06; hakem-karar.py 2 koşu sha256 6d3b6a9622fc; S08–S06 eşit (0.01), hook 9>8 | 11-02 04:30–04:5x |
| F3 metin + doğrulama | senaryo-yazari → finans-dogrulayici ‖ monetizasyon-uyum-uzmani | BEKLİYOR | 03-metin/metin.md | | |
| F4 ses | ses-yonetmeni (+ ses-muhendisi işi) | GEÇTİ | 04-ses/ (anlatim.m4a, kelimeler-hizali.json, altyazi-taslak.en.srt, sahne-zamanlari.json, rhubarb/, shorts-1/2-ek) | 11:18.2; WER %1.4 (gerçek hata 0); −14.2 LUFS TP −1.5; hiza p95 5/15 ms; m4a sha256 d76d46f47c7b; tts-rapor.md | 11-02 05:02–11:3x |
| F4 görsel | gorsel-varlik-sanatcisi | BEKLİYOR | 05-gorsel/ | | |
| F4 müzik + SFX adayları | muzik-ses-tasarimcisi | BEKLİYOR | 06-muzik/ | | |
| F4 paket taslağı | thumbnail-tasarimcisi ‖ youtube-paketleyici | BEKLİYOR | 09-paket/ | | |
| F5 kritik yol testi | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/senkron-rapor.md | | |
| F5 tüm sahneler + 9:16 | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/ | | |
| F6 miks | muzik-ses-tasarimcisi | BEKLİYOR | 06-muzik/stems/ | | |
| F7 kurgu | kurgu-editoru | BEKLİYOR | 08-kurgu/ | | |
| F8 paket | thumbnail ‖ paketleyici ‖ viralite → monetizasyon | BEKLİYOR | 09-paket/ | | |
| F9 hakem | hakem | BEKLİYOR | hakem-raporu.md | | |
| F10 teslim | koordinatör | BEKLİYOR | teslim/ | | |

## Sonraki fazlara notlar
- F3 (senaryo-yazari): S08 zorunlu düzeltmeler D1–D7, P1–P4, H1–H8 → `02-senaryo/senaryo-karari.md` §4. Metinde yayın gününe bağlı zaman sözcüğü yok (kayma güvencesi H7).
