# Kalite kapıları (her ajan testle teslim eder)

Ana hedef: kanalın para kazanması (YPP kabulü + sürdürülebilir gelir). Politika ve retention kapıları bu yüzden diğerleri kadar bağlayıcıdır; YouTube politika kaynakları `docs/monetizasyon.md` ve `.claude/agents/monetizasyon-uyum-uzmani.md`'de.

| Aşama | Test | Geçme ölçütü |
|---|---|---|
| Konu havuzu | kaynak sayımı | her konu ≥2 bağımsız kaynak, linkler açılıyor |
| Rakip analizi | sayı-kaynak eşleşmesi | her sayının kaynağı ve ölçüm tarihi var |
| Senaryolar | çeşitlilik kontrolü | 10 senaryo, en az 5 farklı açı türü |
| Viralite | betikle hesap, 2 kez çalıştırma | aynı sonuç, tablo + gerekçe |
| Politika ön taraması (F2) | 10 senaryo tablosu | her senaryoda YEŞİL/SARI/KIRMIZI + politika kaynağı (URL + tarih); KIRMIZI elenir |
| Metin | süre ve kanca sayımı | hedef süre ±%10 (≥10 dk; ~150 kelime/dk → ≥1.500 kelime), ilk 15 sn'de net vaat, her ≤90 sn'de yeniden kanca |
| Retention (metin) | ilk 30 sn planı + retention haritası | 0–15 sn somut kanca + net vaat, kanal tanıtımı/logo yok, ilk 60 sn'de abone çağrısı yok, her ≤90 sn'de yeniden kanca haritada işaretli |
| Doğrulama | metindeki tüm rakamlar tabloda | doğrulanamayan rakam kalmadı |
| YPP politika (metin, F3) | `03-metin/politika-denetimi.md` | anlamlı anlatı/yorum/eğitim değeri var (haber okuma/liste değil), maskot insan uzman gibi sunulmuyor ve kişiye özel tavsiye yok, başlık/ilk 30 sn reklam dostu, önceki metinlerle kalıp tekrarı yok (n-gram ölçümü yazılı); KIRMIZI bulgu yok |
| Ses | ebur128 (son stereo dosyada) + gürültü tabanı | −14 LUFS ±1, true peak ≤ −1 dBTP, belirgin uğultu/eko yok |
| Anlatıcı sesi (TTS) | aday tablosu + Whisper WER + kör dinleme | ticari kullanıma uygun lisans, WER ≤ %10, kanal adı doğru |
| Müzik/SFX | lisans kaydı + miksli dilim WER + seviye ölçümü | her dosya lisans kaydında, anlaşılırlık bozulmadı, NC/ND yok |
| Görsel varlık | kontakt sayfası + çözünürlük listesi | karakter kartına uygun ve sahneler arası tutarlı (stil gerçekçi/resimsi olabilir), karakter ≥2048 px, sahne ≥1920x1080, kesme artığı yok, üretim kaydı (Canva prompt + media ID) |
| Araç/kurulum | temiz ortamda kurulum + örnek render | hatasız kurulum, kompozisyonlar listeleniyor, örnek render kapılardan geçiyor |
| Dudak senkronu | `tools/senkron-testi.py --araliklar <ekranda ağız aralıkları>` (+ tam sahne; `--ofset` sahne kesiti, `--bant formant` ek bilgi) + `AgizTest` karesi | ağız-ses sapması ≤2 kare (ağzın göründüğü aralıklarda; dış ses bölümü kapıya girmez) |
| Kurgu | ffprobe + kare örnekleri | 1080p+, doğru fps, siyah kare/boşluk yok |
| Retention (kurgu) | ilk 30 sn kesim listesi | ilk görsel değişim ≤3 sn, ilk 30 sn'de kanal intro'su/logo animasyonu yok, retention haritasındaki her yeniden kancada görsel/ses vurgusu, sonra her 5–10 sn'de görsel değişim |
| Altyazı | yazım + hiza | yazım hatası yok, ±150 ms |
| Thumbnail | mobil küçültme + kontrast | 168x94'te okunuyor, metin ≤4 kelime, içerikle tutarlı (videoda olmayan vaat/olay yok), gerçek kişi/marka logosu yok |
| Paket | karakter + bölüm eşleşmesi | başlık ≤60 karakter, bölümler gerçek zamanlara denk, açıklamada "Not financial advice" + "Narration voice is AI-generated" + lisans atıfları |
| **YPP politika (video, F8)** | `09-paket/politika-raporu.md` + hakem yeniden kontrolü | inauthentic/mass-produced değil (gerekçeli), reused/dış görüntü yok, AI personası yok, AI beyanı kararı pakette (`durum.sentetik_medya`) ve açıklama satırı var, reklam uygunluğu öz beyan yanıtları hazır, lisans kaydı tam + Content ID itiraz kanıtı, özgünlük ve insan katkısı kanıtı (özgün karakter, kaynaklı araştırma, editoryal kararlar) — **`docs/monetizasyon.md` §3 Ö1–Ö12 özgün katkı listesinin 12/12'si işaretli (Ö2 ≥3 kendi veri grafiği, Ö5 karakter rolü değişkenliği, Ö6 sahne tekrarı ≤ %20, Ö7 metin tekrarı ≤ %10 betikle ölçülmüş); YPP başvurusu öncesi son 10 videoda istisna yok**, önceki videolardan aynen yeniden kullanılan sahne oranı ölçülmüş ve ≤ %20 (iç kural; giriş/çıkış hariç) |
| Kanal düzeyi özgünlük (her 5 videoda) | son videoların başlık/açılış/yapı/sonuç benzerlik tablosu | "aynı durum, aynı sonuç" deseni yok; sütunlar arası çeşitlilik; `docs/ypp-hazirlik.md` güncel |
| Yayın sonrası analiz (48 sa / 7 g / 28 g) | `yayin-sonrasi/performans-*.md` | her sayının kaynağı (Analytics API / Studio dışa aktarımı / Data API) ve tarihi var, tutma düşüşleri sahneye eşlenmiş, "sonraki video için 3 ders" yazılmış, YPP ilerlemesi satırı var |
| Kanal sayfası (`/kanal-acilisi`) | görsel ölçüleri + mobil/TV önizlemesi + metin kontrolü | banner 2560x1440 (≥2048x1152), metin/logo 1235x338 güvenli alanda, ≤6 MB; profil resmi 98x98'de okunuyor; filigran ≥150x150, <1 MB; kanal açıklamasının ilk 150 karakteri ne izleneceğini söylüyor; `docs/kanal-kimligi.md` var |
| Hakem | tüm tablo (YPP politika ve retention dahil, kendi ölçümüyle) | hepsi geçti → bitmiş video Niyazi onayına (senaryo kararı Niyazi'ye sorulmaz) |
