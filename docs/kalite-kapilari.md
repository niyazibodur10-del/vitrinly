# Kalite kapıları (her ajan testle teslim eder)

| Aşama | Test | Geçme ölçütü |
|---|---|---|
| Konu havuzu | kaynak sayımı | her konu ≥2 bağımsız kaynak, linkler açılıyor |
| Rakip analizi | sayı-kaynak eşleşmesi | her sayının kaynağı ve ölçüm tarihi var |
| Senaryolar | çeşitlilik kontrolü | 10 senaryo, en az 5 farklı açı türü |
| Viralite | betikle hesap, 2 kez çalıştırma | aynı sonuç, tablo + gerekçe |
| Metin | süre ve kanca sayımı | hedef süre ±%10 (≥10 dk; ~150 kelime/dk → ≥1.500 kelime), ilk 15 sn'de net vaat, her ≤90 sn'de yeniden kanca |
| Doğrulama | metindeki tüm rakamlar tabloda | doğrulanamayan rakam kalmadı |
| Ses | ebur128 (son stereo dosyada) + gürültü tabanı | −14 LUFS ±1, true peak ≤ −1 dBTP, belirgin uğultu/eko yok |
| Anlatıcı sesi (TTS) | aday tablosu + Whisper WER + kör dinleme | ticari kullanıma uygun lisans, WER ≤ %10, kanal adı doğru |
| Müzik/SFX | lisans kaydı + miksli dilim WER + seviye ölçümü | her dosya lisans kaydında, anlaşılırlık bozulmadı, NC/ND yok |
| Görsel varlık | kontakt sayfası + çözünürlük listesi | karakter kartına uygun ve sahneler arası tutarlı (stil gerçekçi/resimsi olabilir), karakter ≥2048 px, sahne ≥1920x1080, kesme artığı yok, üretim kaydı (Canva prompt + media ID) |
| Araç/kurulum | temiz ortamda kurulum + örnek render | hatasız kurulum, kompozisyonlar listeleniyor, örnek render kapılardan geçiyor |
| Dudak senkronu | `tools/senkron-testi.py` + `AgizTest` karesi | ağız-ses sapması ≤2 kare |
| Kurgu | ffprobe + kare örnekleri | 1080p+, doğru fps, siyah kare/boşluk yok |
| Altyazı | yazım + hiza | yazım hatası yok, ±150 ms |
| Thumbnail | mobil küçültme + kontrast | 168x94'te okunuyor, metin ≤4 kelime |
| Paket | karakter + bölüm eşleşmesi | başlık ≤60 karakter, bölümler gerçek zamanlara denk |
| Hakem | tüm tablo | hepsi geçti → bitmiş video Niyazi onayına (senaryo kararı Niyazi'ye sorulmaz) |
