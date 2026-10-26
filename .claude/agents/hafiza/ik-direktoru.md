# ik-direktoru — hafıza

## Kurallar

## Dersler
- 2026-10-26: github.com sayfaları WebFetch'te özet döndü ama içerik vermedi; raw.githubusercontent.com curl ile erişilebilir (VoltAgent README ve ajan dosyaları okundu). Tercih: raw dosyayı curl ile oku.
- 2026-10-26: Dış koleksiyonlarda (VoltAgent 10 kategori) ses/müzik/video/animasyon ajanı yok; yalnız build-engineer, tooling-engineer, visual-asset-generator, prompt-engineer benzerleri var → medya ajanları projeye özel yazılmalı.
- 2026-10-26: Gereksiz kadro yerine birleştirme: TTS ayrı ajan yerine ses-yonetmeni'ne bağlandı; karakter varlığı ve sahne illüstrasyonu tek ajanda (gorsel-varlik-sanatcisi).
- 2026-10-26: Karar değişikliğinde (senaryo onayı kalktı, Canva, TTS) yalnız adı geçen dosyaları değil tüm ajan/komut/doküman setini grep'le tara ("onaylı senaryo", "görsel API", "bütçe", "Gemini"): senaryo-yazari ve kalite-kapilari gibi listede olmayan yerlerde de eski ifade çıktı.
- 2026-10-26: .gitignore deseni istendiği gibi eklense de gerçek dosya yollarıyla `git check-ignore -v --no-index` ile doğrula: istenen `uretim/**/final/*.mp4` akıştaki gerçek yolları (teslim/, 08-kurgu/) kapsamıyordu → ek desen + önizleme istisnası gerekti.
- 2026-10-26: MCP bağlayıcılarını (Canva) ajan `tools` satırına yazmadan önce alt ajanda erişim doğrulanmalı; doğrulanana kadar "çağrıyı koordinatör yapar, ajan prompt + değerlendirme hazırlar" notu yeterli.
- 2026-10-26 (kadro denetimi): kadro-kontrol.py yapı kontrolü yapar ama skill adının işlevini doğrulamaz. `marketing-skills:youtube-full` 8 ajanda "SEO/retention" diye bağlıydı; SKILL.md'yi okuyunca veri aracı (transkript/RSS) çıktı. Kural: skill bağlamadan önce SKILL.md'nin description satırını oku; adına göre bağlama.
- 2026-10-26: Ajan dosyalarındaki teslim yolları akış dosyasıyla (bugunun-videosu klasör düzeni) ayrışmıştı (10 ajan). Denetimde her ajanın "çıktı" yolunu akış tablosuyla grep'le karşılaştır.
- 2026-10-26: Aynı kararın (sentetik_medya) iki dosyada farklı sahibi vardı → "tek sahip" denetimi yalnız ajan dosyalarında değil komut + ortak-dersler'de de yapılmalı.
- 2026-10-26: CLAUDE.md proje yapılandırmasıdır; alt ajan olarak değiştirmem, yamayı rapora yazar koordinatöre bırakırım (kadro-kontrol bu yüzden KALDI gösterir — beklenen).
- 2026-10-26: Skill/yol referans betiği scratchpad'de yazıldı (tools/ başka ajanın alanı); kalıcı hale getirilmesi uretim-muhendisi'ne talep edildi. Planlanmış çıktı yollarını (henüz yok) "sahibi + oluşturma adımı" ile listelemek kırık referanstan ayırt etmeyi sağlar.
