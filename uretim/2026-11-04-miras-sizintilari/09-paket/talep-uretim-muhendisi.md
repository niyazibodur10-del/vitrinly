# Talep → uretim-muhendisi: Shorts "Related video" köprüsü yayın paketine (youtube-paketleyici, 2026-11-04)

**Neden:** kanal-ozet ders 2 — 341 Shorts izlenmesi uzun videoya +5 getirdi; Studio'da Related video kurulup kurulmadığı bile doğrulanamadı. Köprü yüklemenin parçası olmalı, hafızaya bırakılmamalı.
**Bulgu [D]:** Data API v3 `videos` kaynağında Related video / bağlı video alanı yok (developers.google.com/youtube/v3/docs/videos, 2026-11-04; yazılabilir: snippet, status, localizations, recordingDetails, paidProductPlacementDetails). API ile kurulamaz → Studio adımı kalır.
**Şu an:** Shorts paketleri `ilgili_video: {"baslik", "video_id": null, "uygulama"}` taşıyor; `yukle.py --dry-run` → `[UYARI] şema: bilinmeyen alan 'ilgili_video'` (hata değil).
**İstenen (öneri; uygulama senin kararın):**
1. `yayin_paket.SEMA`'ya `ilgili_video.baslik` (str), `ilgili_video.video_id` (str|None) — API'ye gitmeyen alan; `tur=="shorts"` iken yoksa UYARI.
2. `yukle.py`: Shorts yüklemesinden sonra `yayin-sonucu.txt`'deki uzun video ID'si ile "Studio → Shorts → Ayrıntılar → Related video → <başlık> (<ID>)" satırını sonuç çıktısına ve `--manuel-paket` YAYIN.md'sine bassın; uzun video herkese açık değilse "Short'u yayından önce bağla" uyarısı.
3. (İsteğe bağlı) yayın sonrası kontrol: Short sayfasında bağlantı görünüyor mu, koordinatör listesine madde.
**Test önerisi:** `test_yayin.py`'ye 2 durum (alan var → uyarı yok; shorts'ta alan yok → uyarı).
