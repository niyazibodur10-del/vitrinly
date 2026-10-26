# Canva görsel üretim testi (2026-10-26)

Yöntem: Canva bağlayıcısı `generate-image`, referans = `assets/karakter/karakter-sayfasi-2d-v1.png` (Canva media MAHZHpeQGdM).
Maliyet: Canva Pro/Business aylık yapay zekâ hakkından 2 üretim; ek ücret yok (Canva Yardım: aylık "AI allowance", sabit sayı belirtilmiyor; üretilen görseller Canva Kullanım Koşullarına uyarak ticari kullanılabilir).

| Test | Canva media | Önizleme | Gözlem |
|---|---|---|---|
| 1: 1923 Almanya, el arabasıyla para | MAHZHqSww90 | test1-1923-onizleme.png | Karakter tanınır (saç, sakal, siyah gömlek, gri pantolon, beyaz ayakkabı). Sahne zengin. Stil fazla gerçekçi/resimsi; kalın kontur yok. |
| 2: mutfak, fincan + değersiz banknot, "flat 2D, thick outlines" vurgulu | MAHZHthG9ZM | test2-mutfak-onizleme.png | Karakter tanınır, ifade doğru (şok). Stil daha düz illüstrasyon; prompt ile stil kontrol edilebiliyor. |

Açık konular:
- Bağlayıcı yalnız 199x112 önizleme döndürüyor; tam çözünürlüklü dosyayı otomatik çekmenin yolu henüz yok (seçenekler: Canva tasarımına yerleştirip export-design, veya Niyazi'nin Canva'dan indirmesi). → uretim-muhendisi'ne iş.
- Aylık hak sayısı hesapta görünüyor (AI usage tracker); haftada 3 video × ~150 sahne için yeterli olup olmadığı ölçülmeli.
- Tutarlılık 2 görselde iyi; 10+ görselde ölçülmeli (gorsel-varlik-sanatcisi stil testi).

## Güncelleme (2026-10-26, gorsel-varlik-sanatcisi)
- Tam çözünürlük çözüldü: Canva çalışma tuvali `DAHZHv3mU9w` (1920x1080) + `insert_fill` + `export-design png` → `test2-mutfak-tam.png` 1920x1080. Adımlar: `tools/gorsel/canva-indir.md`. Canva üretimlerinin doğal boyutu 1680x944.
- Tutarlılık 7 görselde ölçüldü (paket-v1): taban+düzenleme yöntemi tutarlı, sıfırdan üretim değil. Bkz. `assets/karakter/karakter-karti.md` → "Canva karakter kilidi prompt'u".

## Bağlantı kontrolü (2026-10-26, koordinatör, kanal öncesi denetim)
- `search-designs` ✅ (export tuvali `DAHZHv3mU9w` 1920x1080 erişilebilir) · `list-brand-kits` ✅ (1 marka kiti `kAFwxg7XRn8`).
- `generate-image` düzenleme yöntemi (referans: taban `MAHZHqW0_Uo` + sayfa `MAHZHpeQGdM`, LANDSCAPE_16_9): "şehir silüeti önünde altın para tutuyor" → `MAHZInD7qDk`, ~25 sn, SUCCESS. Görsel kontrol: yüz, saç, sakal, siyah gömlek, kol saati, çizim stili korunmuş ✅. Ek ücret yok (abonelik AI hakkı).
