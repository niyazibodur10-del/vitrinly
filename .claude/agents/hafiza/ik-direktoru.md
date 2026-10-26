# ik-direktoru — hafıza

## Kurallar

## Dersler
- 2026-10-26: github.com sayfaları WebFetch'te özet döndü ama içerik vermedi; raw.githubusercontent.com curl ile erişilebilir (VoltAgent README ve ajan dosyaları okundu). Tercih: raw dosyayı curl ile oku.
- 2026-10-26: Dış koleksiyonlarda (VoltAgent 10 kategori) ses/müzik/video/animasyon ajanı yok; yalnız build-engineer, tooling-engineer, visual-asset-generator, prompt-engineer benzerleri var → medya ajanları projeye özel yazılmalı.
- 2026-10-26: Gereksiz kadro yerine birleştirme: TTS ayrı ajan yerine ses-yonetmeni'ne bağlandı; karakter varlığı ve sahne illüstrasyonu tek ajanda (gorsel-varlik-sanatcisi).
- 2026-10-26: Karar değişikliğinde (senaryo onayı kalktı, Canva, TTS) yalnız adı geçen dosyaları değil tüm ajan/komut/doküman setini grep'le tara ("onaylı senaryo", "görsel API", "bütçe", "Gemini"): senaryo-yazari ve kalite-kapilari gibi listede olmayan yerlerde de eski ifade çıktı.
- 2026-10-26: .gitignore deseni istendiği gibi eklense de gerçek dosya yollarıyla `git check-ignore -v --no-index` ile doğrula: istenen `uretim/**/final/*.mp4` akıştaki gerçek yolları (teslim/, 08-kurgu/) kapsamıyordu → ek desen + önizleme istisnası gerekti.
- 2026-10-26: MCP bağlayıcılarını (Canva) ajan `tools` satırına yazmadan önce alt ajanda erişim doğrulanmalı; doğrulanana kadar "çağrıyı koordinatör yapar, ajan prompt + değerlendirme hazırlar" notu yeterli.
