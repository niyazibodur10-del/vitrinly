# kanal-analisti — hafıza

## Kurallar
- Erişim durumu (2026-10-26): youtube.com curl → proxy CONNECT 403; youtube.com/socialblade WebFetch → DNS ENOTFOUND; socialblade, playboard, piped/invidious aynaları → 403; googleapis.com (YouTube Data API v3) erişilebilir ama anahtarsız 403 "unregistered callers".
- Bu yüzden sayılar WebSearch özetinden gelir → [AÖ] etiketli; ölçülemeyen (son 20 video, medyan, tempo) "YAPILAMADI" diye yazılır, tahmin [T] etiketli.
- `YOUTUBE_API_KEY` ortam değişkeni varsa önce onu dene (kota 10.000 birim/gün yeterli); anahtar repoya/sohbete yazılmaz.
- Erişim güncellemesi (2026-10-27): `YOUTUBE_API_KEY` VAR ve çalışıyor. `channels`/`playlistItems`/`videos` sorunsuz; **`search` ayrı bir günlük sorgu tavanına takılıyor (15 sorguda 429 "Search Queries per day"; proje trend-avcisi ile paylaşılıyor olabilir)** → aramayı en sona bırakma, en başta az ve hedefli yap; kanal listesi + `playlistItems` (1 birim) tercih. i.ytimg.com thumbnail açık. youtube.com artık 200; yt-dlp `--write-auto-subs --sub-langs en-orig` ~8 videoda altyazı veriyor, sonra 429/bot kontrolü → 4 sn aralıkla, ≤10 video.

## Dersler
- 2026-10-26 (rakip analizi v1): kanıt zayıf (n≈6 outlier, medyan ölçülemedi). Öneriler viralite modeline doğrudan yazılmadı; karar hakem/Niyazi'ye bırakıldı — doğru yaklaşım.
- 2026-10-26: TR'de animasyon/maskot anlatımlı finans kanalı bulunamadı (arama motoru kapsamıyla sınırlı) — kanal artık İngilizce/global, TR boşluğu yalnız not.
- 2026-10-26: API anahtarı gelince ilk iş: 5 kanal × son 30 video, yerel medyan outlier tablosu ve tarihli yeniden ölçüm.
- 2026-10-26 (monetizasyon araştırması): support.google.com/youtube ve blog.youtube WebFetch ile AÇILIYOR → politika iddiaları birincil kaynakla [B-Kn] yazılabilir; youtube.com (Creator Insider) ve canva.com/policies açılmıyor → [AÖ]. Küçük model 125 karakter alıntı sınırı koyuyor: tam metin için bölüm bölüm, "kısa ardışık parçalarla" sor.
- 2026-10-26: Haber sitelerinin "eşik ikiye katlandı" iddiasını blog.youtube (2026-08-10) + support 12843009'dan doğruladım; support 72851 hâlâ eski eşiği gösteriyor. Ders: tek yardım sayfasına güvenme, "Changes to YPP" sayfasını ve resmi blogu da aç.
- 2026-10-26: Etiket testi betiği (scratchpad/etiket_test.py; yeniden yaz): bölüm bazında rakam/politika içeren tablo satırı ve maddelerde [B-K|AÖ-A|T|ÖB] ya da repo yolu arar; tablo başlık satırlarını atlar; K/A kodlarının tanımlı ve kullanılmış olduğunu çapraz kontrol eder. İlk koşuda 27 etiketsiz satır çıktı (başlık altında "miras" etiket yetmez) → her satıra açık etiket.
- 2026-10-26: Kendi kanalımızın durumu (uretim/kanal-kimligi/mevcut-durum.md) politika riskini değiştirdi (eski 4 "Shocking" video, "get rich" anahtar kelimeleri). Ders: politika araştırmasında önce kanalın mevcut halini oku.
- 2026-10-27 (F1 rakip özeti, ilk API'li ölçüm): v1'in "aktif" saydığı 5 kanaldan 3'ü (Business Casual, OverSimplified, Swedish Investor) + MagnatesMedia 12 ayda uzun video yayınlamamış. Ders: kanal seçmeden önce son yükleme tarihini API'yle ölç; WebSearch özetine güvenme.
- 2026-10-27: Kalıp başlık kanalı açar ama tekrarı skoru düşürür ("real reason/true origin" n=119, medyan 0,55). Kalıp istatistiğini her zaman kanal içi medyana göre ve "medyan ≥1.000 kanal" filtresiyle yeniden koş; havuz farkı çoğu zaman kanal etkisi (süre örneği: havuzda 10–15 dk zayıf, kanal içinde fark yok).
- 2026-10-27: Konu doygunluğu = başlık taraması (anahtar kelime → n, medyan skor, ≥2x sayısı). Tulip/FTX/Enron/South Sea küçük AI kanallarıyla dolu ve izlenmesiz; 1929/2008 kalabalık ama kazananlı. Yeni kanal örneklerinde hayatta kalan yanlılığını her zaman yaz.
- 2026-10-27: Etiket testi betiği artık repoda: `uretim/2026-10-26-secim/01-arastirma/etiket_test.py` (etiket regex'i `[ETİKET` + `],: ` kabul eder; test bölümünü atlar). Ham veriyi JSON olarak teslim klasörüne koy, `grep -c AIza` ile anahtar sızıntısı kontrolü yap.
