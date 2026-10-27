# trend-avcisi — hafıza

## Kurallar
- Link "açılıyor" = HTTP 200 **ve** sayfa metninde konu anahtar kelimesi. Yalnız durum kodu yetmez: 200 dönüp "Content Not Found" / "Just a moment..." / "request verification" gösteren sayfalar var. Kontrol `uretim/2026-10-26-secim/01-arastirma/kaynak-kontrol.py` ile yapılır (yeniden kullan).
- Haber kaynağının tarihini arama özetinden değil, sayfanın `datePublished` / `article:published_time` metadata'sından al. Arama özeti eski yazıları "bu ay" diye sunabiliyor.
- Markdown linkte parantezli URL (ör. `Black_Monday_(1987)`) `%28`/`%29` ile kodlanır, yoksa ayrıştırıcı linki keser.

## Dersler
### 2026-10-27 — F1 konu havuzu (A sütunu, ilk herkese açık video)
- **Erişim haritası (2026-10-27):** Wikimedia pageviews API çalışıyor ama UA şart ve ~1 istek/4–8 sn hızında bile 429 veriyor. Liste kısa tutulmalı, tekrar beklemeli yapılmalı. YouTube Data API `search.list` günlük "Search Queries" kotası diğer ajanlarla paylaşılıyor ve 7 sorguda doldu. Çözüm: `pip install yt-dlp` + `ytsearch15:`/`ytsearchdate25:` ile ID topla, `videos.list` ile istatistik al (ayrı kota, çalışıyor). Google Trends 429, Reddit .json 403. Britannica, Investopedia ve SEC bot korumalı (403/402): kaynak olarak kanıtlanamıyor.
- **Açık ve güvenilir kaynaklar:** federalreservehistory.org/essays/*, history.state.gov/milestones, econlib.org/library/Enc, pbs.org (Frontline, Commanding Heights), history.com (bazı yollar 404), internationalbanker.com/history-of-financial-crises (liste sayfasından gerçek slug alınmalı, tahmin edilen slug 404), Guardian, ABA Journal, City A.M.
- **Strateji karşılaştırması:** S2 (kalıcı olay listesi + pageviews + YouTube) 17 kaynaklı A konusu verdi. S1 (haber akışı) zamanlamayı ve 6 B/C konusu verdi. S3 (HN; Reddit kapalı) bu nişte 0 yeni konu verdi. Bir dahaki sefere S3'e zaman ayırma, S1'i A konularına "güncel bağ" bulmak için kullan.
- **Okuma kuralı:** "alaka medyanı yüksek + son 12 ayın en iyisi düşük" = talep var, taze rakip yok. 2026-10'da 1929, South Sea ve Black Wednesday bu durumdaydı. Talep sinyali için Wikipedia'nın son 30 gün / önceki 60 gün oranı yararlı (Enron +%47, CoreWeave 3×).
- Sonraki tur için hazır aday: Barings/Nick Leeson (talep güçlü, ikinci bağımsız açılan kaynak bulunmalı), özel kredi (B; son 30 günden tarihli 2 kaynak gerek).
