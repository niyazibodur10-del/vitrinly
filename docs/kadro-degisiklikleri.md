# Kadro değişiklikleri

| Tarih | Değişiklik | Ajan | Neden |
|---|---|---|---|
| 2026-10-26 | işe alındı | ik-direktoru | Niyazi talebi: sistem kendi kadrosunu denetlesin, işe alsın, çıkarsın |
| 2026-10-26 | işe alındı | muzik-ses-tasarimcisi | Müzik/SFX seçimi, lisans kaydı ve miks sahipsizdi (ses-muhendisi ve kurgu-editoru arasında bölünmüştü). Telif riski en yüksek alan; tek sahip ve lisans kaydı şart. Dış koleksiyonlarda (VoltAgent) karşılığı yok → projeye özel yazıldı. |
| 2026-10-26 | işe alındı | uretim-muhendisi | Remotion projesi, `tools/kurulum.sh`, render hattı ve `tools/` betikleri sahipsizdi (animasyon-yonetmeni yapıyordu). Konteyner her oturumda silindiği için tek komutla kurulum kritik. Örnek: VoltAgent build-engineer / tooling-engineer, medya hattına uyarlandı. |
| 2026-10-26 | işe alındı | gorsel-varlik-sanatcisi | Karakter varlık hazırlığı (büyütme, kesme, rig parçaları, ağız şekilleri) ve sahne illüstrasyon prompt'ları sahipsizdi. İki aday rol (karakter varlık hazırlayıcı + sahne illüstrasyon/prompt uzmanı) TEK ajanda birleştirildi: aynı stil kaynağı, aynı araçlar, tutarlılık tek elden. Örnek: VoltAgent visual-asset-generator + prompt-engineer. |
| 2026-10-26 | yeniden yazıldı + kapsam genişletildi | ses-yonetmeni | Niyazi ücretsiz AI anlatıcı sesi istiyor. Ayrı "TTS uzmanı" almak yerine anlatıcı sesinin tek sahibi ses-yonetmeni yapıldı (Yol A: TTS seçimi/üretimi/testi, Yol B: Niyazi okuması). Çakışma önlendi. |
| 2026-10-26 | daraltıldı | ses-muhendisi | Müzik/efekt miksi muzik-ses-tasarimcisi'ne geçti; yalnız anlatım sesi. Zincir tanımı gerçek betiğe (RNNoise, `tools/ses/temizle.sh`) göre düzeltildi. |
| 2026-10-26 | daraltıldı | animasyon-yonetmeni | Görsel üretim/kesme gorsel-varlik-sanatcisi'ne, kurulum/araç uretim-muhendisi'ne geçti; rig, senkron, kamera, sahne kodu kaldı. Shorts dikey kompozisyonu eklendi. |
| 2026-10-26 | daraltıldı + genişletildi | kurgu-editoru | Müzik seçimi/ducking muzik-ses-tasarimcisi'ne geçti (stem'ler hazır gelir); 9:16 Shorts kesitleri eklendi. |
| 2026-10-26 | genişletildi | hakem | Her teslimatı `docs/ajan-karnesi.md`'ye puanlama görevi; lisans kaydı kontrolü; Edit aracı eklendi. |
| 2026-10-26 | genişletildi | kanal-analisti | Yayın sonrası kendi kanal istatistikleri (viralite kalibrasyon verisi) eklendi; Edit aracı. |
| 2026-10-26 | yeniden yazıldı (hepsi) | 14 ajan | Protokol satırı, "dünyanın en iyisi" kimliği, alana özgü "2–3 aday → test → eleme" adımı, test kapısı ve "Kullandığın skill'ler" bölümü eklendi; Skill aracı skill kullanan herkese verildi. 17 hafıza dosyası oluşturuldu, öğrenilmiş dersler tohumlandı. |
| 2026-10-26 | değerlendirildi, alınmadı | tts-uzmani (ayrı) | ses-yonetmeni ile çakışırdı → birleştirildi. |
| 2026-10-26 | değerlendirildi, alınmadı | sahne-illustratoru (ayrı) | gorsel-varlik-sanatcisi ile aynı stil/araç → birleştirildi. |
| 2026-10-26 | güncellendi | CLAUDE.md Akış + /video-uret komutu | yeni ajanlar akışa bağlandı |
