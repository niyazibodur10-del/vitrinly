# Ortak dersler (tüm ajanlar)

- 2026-10-26: Ağ politikası GitHub sürüm indirmelerini, pixabay/incompetech/freesound/youtube/instagram/socialblade erişimini engelliyor; git clone, Hugging Face, PyPI, npm, download.pytorch.org, archive.org, opengameart, kenney.nl açık.
- 2026-10-26: Render tarayıcısı Google Fonts sertifikasına güvenmiyor → yazı tipleri yerel (`video/public/fonts`).
- 2026-10-26: Mono anlatım stereoya kopyalanınca LUFS ~+3 ölçülür → normalizasyon son stereo dosyada (`tools/render-son.sh`).
- 2026-10-26: Whisper aynı sese ±2 kelime oynar; tek sayıya değil tekrar eden hatalara bak.
- 2026-10-26: Hugging Face `trust_remote_code` gerektiren modeller güvenlik nedeniyle çalıştırılamıyor; yerel ağırlık + bilinen kütüphane kullan.
- 2026-10-26: raw.githubusercontent.com curl ile erişilebilir (github.com sayfaları WebFetch'te içerik vermeyebilir); freemusicarchive.org erişilebilir.
- 2026-10-26: Lisans kuralı (tüm medya): ticari kullanıma izin vermeyen (NC/ND, "kişisel kullanım") müzik, efekt, ses modeli ve görsel kullanılmaz; her dış varlığın kaynağı + lisansı üretim klasöründe kayıtlı olmalı.
- 2026-10-26: YouTube yayını: `tools/yayin/yukle.py` (paket şeması başlık yorumunda). Cihaz akışıyla altyazı yüklenemez (kapsam yok) → altyazı Studio'dan; tam animasyon "değiştirilmiş/yapay içerik" beyanı gerektirmeyebilir (YouTube yardım 14328491: gerçekçi olmayan animasyon muaf) — `durum.sentetik_medya` video başına hakem/finans-dogrulayici kararı. Oauth/googleapis/accounts.google.com konteynerden erişilebilir.
- 2026-10-26: Render hızı ölçümü (4 vCPU, Remotion 4.0.539, `tools/render-son.sh`): ~5,4 kare/sn ≈ gerçek sürenin 5,5 katı; 12 dk video ≈ 66 dk, ≈450 MB → final videolar git'e girmez (GitHub 100 MB sınırı).
