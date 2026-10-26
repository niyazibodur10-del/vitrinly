# kanal-analisti — hafıza

## Kurallar
- Erişim durumu (2026-10-26): youtube.com curl → proxy CONNECT 403; youtube.com/socialblade WebFetch → DNS ENOTFOUND; socialblade, playboard, piped/invidious aynaları → 403; googleapis.com (YouTube Data API v3) erişilebilir ama anahtarsız 403 "unregistered callers".
- Bu yüzden sayılar WebSearch özetinden gelir → [AÖ] etiketli; ölçülemeyen (son 20 video, medyan, tempo) "YAPILAMADI" diye yazılır, tahmin [T] etiketli.
- `YOUTUBE_API_KEY` ortam değişkeni varsa önce onu dene (kota 10.000 birim/gün yeterli); anahtar repoya/sohbete yazılmaz.

## Dersler
- 2026-10-26 (rakip analizi v1): kanıt zayıf (n≈6 outlier, medyan ölçülemedi). Öneriler viralite modeline doğrudan yazılmadı; karar hakem/Niyazi'ye bırakıldı — doğru yaklaşım.
- 2026-10-26: TR'de animasyon/maskot anlatımlı finans kanalı bulunamadı (arama motoru kapsamıyla sınırlı) — kanal artık İngilizce/global, TR boşluğu yalnız not.
- 2026-10-26: API anahtarı gelince ilk iş: 5 kanal × son 30 video, yerel medyan outlier tablosu ve tarihli yeniden ölçüm.
- 2026-10-26 (monetizasyon araştırması): support.google.com/youtube ve blog.youtube WebFetch ile AÇILIYOR → politika iddiaları birincil kaynakla [B-Kn] yazılabilir; youtube.com (Creator Insider) ve canva.com/policies açılmıyor → [AÖ]. Küçük model 125 karakter alıntı sınırı koyuyor: tam metin için bölüm bölüm, "kısa ardışık parçalarla" sor.
- 2026-10-26: Haber sitelerinin "eşik ikiye katlandı" iddiasını blog.youtube (2026-08-10) + support 12843009'dan doğruladım; support 72851 hâlâ eski eşiği gösteriyor. Ders: tek yardım sayfasına güvenme, "Changes to YPP" sayfasını ve resmi blogu da aç.
- 2026-10-26: Etiket testi betiği (scratchpad/etiket_test.py; yeniden yaz): bölüm bazında rakam/politika içeren tablo satırı ve maddelerde [B-K|AÖ-A|T|ÖB] ya da repo yolu arar; tablo başlık satırlarını atlar; K/A kodlarının tanımlı ve kullanılmış olduğunu çapraz kontrol eder. İlk koşuda 27 etiketsiz satır çıktı (başlık altında "miras" etiket yetmez) → her satıra açık etiket.
- 2026-10-26: Kendi kanalımızın durumu (uretim/kanal-kimligi/mevcut-durum.md) politika riskini değiştirdi (eski 4 "Shocking" video, "get rich" anahtar kelimeleri). Ders: politika araştırmasında önce kanalın mevcut halini oku.
