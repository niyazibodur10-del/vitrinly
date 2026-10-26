# kanal-analisti — hafıza

## Kurallar
- Erişim durumu (2026-10-26): youtube.com curl → proxy CONNECT 403; youtube.com/socialblade WebFetch → DNS ENOTFOUND; socialblade, playboard, piped/invidious aynaları → 403; googleapis.com (YouTube Data API v3) erişilebilir ama anahtarsız 403 "unregistered callers".
- Bu yüzden sayılar WebSearch özetinden gelir → [AÖ] etiketli; ölçülemeyen (son 20 video, medyan, tempo) "YAPILAMADI" diye yazılır, tahmin [T] etiketli.
- `YOUTUBE_API_KEY` ortam değişkeni varsa önce onu dene (kota 10.000 birim/gün yeterli); anahtar repoya/sohbete yazılmaz.

## Dersler
- 2026-10-26 (rakip analizi v1): kanıt zayıf (n≈6 outlier, medyan ölçülemedi). Öneriler viralite modeline doğrudan yazılmadı; karar hakem/Niyazi'ye bırakıldı — doğru yaklaşım.
- 2026-10-26: TR'de animasyon/maskot anlatımlı finans kanalı bulunamadı (arama motoru kapsamıyla sınırlı) — kanal artık İngilizce/global, TR boşluğu yalnız not.
- 2026-10-26: API anahtarı gelince ilk iş: 5 kanal × son 30 video, yerel medyan outlier tablosu ve tarihli yeniden ölçüm.
