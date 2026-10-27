# Durum — 2026-10-26-1929-1000-dolar

- **Tetik:** Niyazi "Bugünün videosu gelsin" (2026-10-26 19:50 UTC).
- **Kanal:** Toonomy (@toonomy), anlatıcı Leo. Tempo v2: 2 uzun + 4 Shorts/hafta.
- **Slot ve sütun:** Stok boş → takvim v2 §3/§6 geçiş kuralı: bu video **stok videosu**, sütun **A (tarih çöküşleri)** (raf ömrü uzun).
  Hedef slot: ilk Pazar A slotu **2026-11-01 12:00 ET (TRT 20:00)** — hakem ONAY + Niyazi onayı slottan ≥3 sa önce gelirse; yetişmezse stokta kalır, Pazar 2026-11-08.
- **Stok:** uzun 0 / Shorts 0.
- **Kesinti:** 2026-10-26 ~20:00 UTC F0/F1 ajanları kullanım limitine takıldı (dosya bırakmadılar); 2026-10-27 04:22 UTC yeniden başlatıldı.
- **Not:** F0 ortam kontrolü ve F1 araştırma birbirine bağımlı değil → koordinatör paralel başlattı.

| Adım | Sahip | Durum | Teslim | Test kanıtı | Başlangıç–bitiş (UTC) |
|---|---|---|---|---|---|
| F0 açılış | koordinatör | GEÇTİ | durum.md | slot+sütun+stok yazıldı | 19:50–19:52 |
| F0 ortam | uretim-muhendisi | GEÇTİ | 00-ortam/ortam-raporu.md | kurulum 19,2 sn/1,3 sn idempotent; 3 kompozisyon; 2 karelik Pilot render ✅; Whisper ✅ (ilk yükleme yavaş: small 44 sn, medium 136 sn); render-son.sh kısa ses arızası düzeltildi | 04:22–(ca90b0a) |
| F1 konu havuzu | trend-avcisi | GEÇTİ | 01-arastirma/konu-havuzu.md | kaynak-kontrol.py 23/23 konu GEÇTİ (exit 0); 17 A / 3 B / 3 C | 04:22–(da6c3f9) |
| F1 rakip özeti | kanal-analisti | GEÇTİ | 01-arastirma/rakip-ozet.md | etiket_test 81/81 etiketli; 39 kanal, 1.123 uzun video [API]; not: search uç noktası günlük tavana takıldı (429), docs/rakip-analizi.md'nin erken yenilenmesi önerildi | 04:22–(19f26bd) |
| F2 senaryolar | senaryo-yazari | GEÇTİ | 02-senaryo/senaryolar.md | senaryo-kontrol.py exit 0, 2 koşu aynı; 11 senaryo, 11 açı, 33 başlık ≤60 | (5c30245) |
| F2 viralite / ön doğrulama / politika | viralite-analisti ‖ finans-dogrulayici ‖ monetizasyon-uyum-uzmani | GEÇTİ | 02-senaryo/viralite.md, on-dogrulama.md, politika-on-tarama.md | viralite 2 koşu sha256 aynı, ilk 3 S03/S01/S06; doğrulama 7 YEŞİL 4 SARI 0 KIRMIZI; politika 5 YEŞİL 6 SARI 0 KIRMIZI | (b962b14, 5d91233, 9322f41) |
| F2 karar | hakem | GEÇTİ | 02-senaryo/senaryo-karari.md | kazanan S03 "You Have $1,000 in 1929. Can You Keep It?" (şartlı: F3 zorunlu düzeltmeler D1–D7, P1–P6, H1–H5); yedek S01; hakem-karar.py 2 koşu aynı | (c065502) |
| F3 metin + doğrulama | senaryo-yazari → finans-dogrulayici ‖ monetizasyon-uyum-uzmani | GEÇTİ — **METİN KİLİDİ** (RED-1 düzeltmeleri d874c1b; doğrulama onayı 75dde7d eşlenmeyen 0; politika onayı 7ecfb00 YEŞİL) | 03-metin/metin.md (1.701 kelime ≈11:54; Shorts 56,6 / 58,7 sn) | metin-kontrol.py, dogrulama-kontrol.py, politika-denetim.py 2'şer koşu aynı | 05:10–10:05 |
| F4 ses / görsel / müzik / paket taslak | çoklu | SÜRÜYOR | 04–06, 09 | | |
| F4 müzik + SFX adayları | muzik-ses-tasarimcisi | GEÇTİ | 06-muzik/adaylar.md, lisans-kaydi.md | lisans-kontrol.py dosya 55 · kayıtsız 0 · yasak lisans [] (exit 0, 2 koşu; negatif test exit 1); bölüm başına ön seçim, kesin seçim F6'da WER ile | (d95b3ef) |
| F4 ses son işlem + transkript | ses-muhendisi | GEÇTİ | 04-ses/kelimeler-hizali.json, altyazi-taslak.en.srt, altyazi-remotion.json, rhubarb/ (ses-rapor.md §8) | anlatim.wav −14.2 LUFS/TP −1.5 (ek işlem gereksiz: 4 aday, de-ess adayları sibilansı 7–8 dB kesti, WER farksız); 1701/1701 kelime kilitli metin; atılan yalnız "Yes." 9:07.9 + "up." 10:00.3; akustik hiza p95 7/15 ms (±150 ✓); Rhubarb S01 testi ✓ | 10:15–(bu commit) |
| F5 kritik yol testi | animasyon-yonetmeni | GEÇTİ (tüm sahneler + 9:16 sonraki tur) | 07-animasyon/senkron-rapor.md, kritik-test-onizleme.mp4 (tam render git dışı), kareler/ | K1929Kritik 19,7 sn/591 kare; 3 klon kapı sahnesi (H4) B planı gerekmedi; ekrandaki ağız senkronu −1 kare, tam sahne S01 0 / S04 0 (S02–S13 +1..+2); AgizTest temiz; blackdetect 0; donma yok; −13,9 LUFS; tüm-video ölçümü −4 (ağzın görünmediği S04 62–70 sn bölgesi, rapor) | (bu commit) |
| F5 tüm sahneler + 9:16 | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/* | | |
| F6 miks | muzik-ses-tasarimcisi | GEÇTİ | 06-muzik/cue-listesi.md, cue.json, stems/muzik-stem.wav + sfx-stem.wav (631.63 sn, 48 kHz stereo 24-bit, git dışı), stems/shorts-1/2-muzik-stem.wav (git dışı), stems/miks-onizleme.m4a, atif-satirlari.md | Parça seçimi bölüm başına 2 aday × 25 sn gerçek anlatım dilimi Whisper (olcum-f6-test.json: tüm adaylar anlatım-tek ±1 kelime). Tam önizleme miksi WER %1.62 vs anlatım-tek %1.97 (aynı model/ayar, fark −0.35 puan; ses kolu transkriptine göre +0.69) ≤+1 ✅ (olcum-f6-wer.json); konuşma altı müzik farkı bölüm başına 20.8–23.8 dB, tümü 21.7 dB ✅; önizleme −14.0 LUFS / TP −2.7 dBTP ✅; lisans-kontrol.py exit 0 (55 dosya + 38 cue dosyası kayıtlı, NC/ND/SA yok); 10 müzik dosyası (8 CC0 + 2 kendi üretim) → zorunlu CC BY atfı yok | (F6) |
| F7 kurgu | kurgu-editoru | BEKLİYOR | 08-kurgu/* | | |
| F8 paket | çoklu | BEKLİYOR | 09-paket/* | | |
| F9 hakem | hakem | BEKLİYOR | hakem-raporu.md | | |
| F10 teslim | koordinatör | BEKLİYOR | teslim/ | | |

## Sonraki fazlara notlar (denetçilerden)
- F7 kurgu: Shorts 1'de "NOV 1929" etiketi korunur; Shorts 2'de "12 MONTHS TO SEPT 2026" / "2025 → 2026" kartı cümle başlarken ekranda; Shorts 2 iki parça + atlama kesmesi (S20 ortası çıktı). 9:16 skor kartında "IN A DECADE OF FALLING PRICES" şeridi.
- F8 paket: başlıkta yıl sınırı (1929) korunur; başlık/thumbnail/açıklamada bugüne dönük "paranı nereye koy" hükmü yok; sentetik_medya = true, açıklama satırı "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."; yasal not 03-metin/dogrulama.md §4.
- F5: kritik yol testine 3 Leo klonlu kapı sahnesi zorunlu (H4); B planı tek Leo kapıdan kapıya yürür.
- F6 miks: Ragtime! Jazz (B2) en riskli — müzik konuşmanın 22–24 dB altında + 2–4 kHz oyuk; kendi gerilim yatakları yalnız katman (enerji 150 Hz altında); stüdyo kahkahası CC0 yok → "group giggling" 3 katman; 3 CC BY atfı açıklamaya (lisans-kaydi.md).
- Kaynak: CPU çakışması — TTS/Whisper/render/ESRGAN aynı anda koşmasın (uretim-hatti-testi.md).
