# Vitrinly proje hafızası

Oturumlar arası kalıcı hafıza. Konteyner her oturumda sıfırdan açılır ve eski konuşma kayıtları taşınmaz; kalıcı olan yalnızca bu repodur. Ürün kararları `CLAUDE.md`'de, bu dosyada durum, öğrenilenler ve açık işler var. Yeni bir karar veya önemli bir bilgi geldiğinde bu dosyayı güncelle ve commit'le.

## Durum (2026-10-26)
- Faz 0 sürüyor. Yapılanlar:
  - `docs/research/pazaryeri-kurallari.md`: Trendyol + Hepsiburada sıralama, başlık, açıklama, görsel, ceza kuralları, reklam hukuku, satıcı API'leri. Sonunda açık sorular ve doğrulama listesi var.
  - `docs/research/kural-tabani-v0.yaml`: 47 kurallık başlangıç kural tabanı. Hiçbir kural VERIFIED değil (resmi sayfalar ortamdan açılamadı); hepsi SNIPPET/UNKNOWN.
  - `demo/vitrinly-demo.html`: Faz 0 demosu (kural motoru, AI uyum/SEO, görsel planı, soru-cevap).
- Sırada: landing + bekleme listesi, satıcı görüşmeleri, kural tabanındaki kuralları resmi kaynaktan doğrulama.

## Ekip
- Yazılım ve tasarım ajanları repoda: `.claude/agents/` (her oturumda otomatik yüklenir). Önceki oturumda `~/.claude/agents` altındaydılar ve konteynerle birlikte kayboldular; bu yüzden repoya taşındı (2026-10-26).
- `~/.claude/agents` altındaki Nutrigold ajanları arşivdir, Niyazi istemedikçe kullanılmaz.

## Ortam notları
- Bulut ortamında `YOUTUBE_*` değişkenleri tanımlı (API anahtarı + OAuth). **Vitrinly ile ilgisi yok**, Niyazi'nin ayrı bir işine ait. Vitrinly işlerinde kullanma.
- n8n bağlı, ama kayıtlı kimlik bilgisi yok (2026-10-26).
- Niyazi'nin abonelikleri ve görsel sağlayıcı kararları: `CLAUDE.md` → Decisions.
