# Durum — 2026-10-26 (slug F2'de belli olacak)

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
| F1 konu havuzu | trend-avcisi | SÜRÜYOR | 01-arastirma/konu-havuzu.md | | 19:52– |
| F1 rakip özeti | kanal-analisti | SÜRÜYOR | 01-arastirma/rakip-ozet.md | | 19:52– |
| F2 senaryolar | senaryo-yazari | BEKLİYOR | 02-senaryo/senaryolar.md | | |
| F2 viralite / ön doğrulama / politika | viralite-analisti ‖ finans-dogrulayici ‖ monetizasyon-uyum-uzmani | BEKLİYOR | 02-senaryo/* | | |
| F2 karar | hakem | BEKLİYOR | 02-senaryo/senaryo-karari.md | | |
| F3 metin + doğrulama | senaryo-yazari → finans-dogrulayici ‖ monetizasyon-uyum-uzmani | BEKLİYOR | 03-metin/* | | |
| F4 ses / görsel / müzik / paket taslak | çoklu | BEKLİYOR | 04–06, 09 | | |
| F5 animasyon | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/* | | |
| F6 miks | muzik-ses-tasarimcisi | BEKLİYOR | 06-muzik/stems | | |
| F7 kurgu | kurgu-editoru | BEKLİYOR | 08-kurgu/* | | |
| F8 paket | çoklu | BEKLİYOR | 09-paket/* | | |
| F9 hakem | hakem | BEKLİYOR | hakem-raporu.md | | |
| F10 teslim | koordinatör | BEKLİYOR | teslim/ | | |
