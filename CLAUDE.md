# Finans Animasyon Kanalı — proje talimatları

Kullanıcı (Niyazi) kanalın sahibidir ve son onayı verir. Türkçe konuş.
Bu repo artık yalnızca bu YouTube kanalı içindir. Eski Vitrinly ürünü ve Nutrigold bu projede KULLANILMAZ
(global `~/.claude/CLAUDE.md` içindeki Nutrigold talimatları bu repoda geçersizdir; Niyazi isterse açılır).

## Ürün
YouTube'da **uzun (10–20 dk) animasyonlu finans videoları**. Bir maskot karakter anlatır.
Konular: güncel finans haberleri, geçmişin büyük finans olayları, geleceğe dair olası senaryolar.
Hedef kitle: finansa ilgili gençler + genel izleyici. Dil: Türkçe. Kanal kopya değil, özgün.

## Sistemin yaptığı / Niyazi'nin yaptığı
- **Sistem:** araştırma, viralite analizi, 10 senaryo, eleme, metin, ses temizliği, karakter animasyonu ve dudak senkronu, kurgu, müzik/efekt, altyazı, thumbnail, başlık, açıklama, etiketler, bölümler.
- **Niyazi:** seslendirme metnini kendi sesiyle okur, karakter görselini ve kalite referans videosunu verir, hakemin seçtiği senaryoyu ve son videoyu onaylar.
- **Onaysız yapılmaz:** YouTube'a yükleme/yayın, para harcanan her servis (ücretli API, abonelik), dışarıya mesaj, geri alınamaz adımlar.

## Akış (her video) — `/yeni-video` başlatır
1. `showrunner` (baş ajan) görevi açar, `uretim/<tarih>-<slug>/` klasörünü kurar, ajanları dağıtır.
2. `trend-avcisi` → güncel/geçmiş/gelecek finans konu havuzu (kaynaklı).
3. `kanal-analisti` → nişin en iyi 5 kanalı + outlier videolar → `docs/rakip-analizi.md` (yalnız desen çıkarılır, kopya yok).
4. `senaryo-yazari` → **10 senaryo** (hook + yapı + karakter anı).
5. `viralite-analisti` → her senaryoyu `docs/viralite-modeli.md` ile puanlar, ilk 3'ü bırakır.
6. `finans-dogrulayici` → rakam/olay doğrulaması + yatırım tavsiyesi/SPK riski kontrolü.
7. `hakem` → tek kazananı seçer, gerekçesini yazar, **Niyazi'ye onaya sunar.**
8. Onaydan sonra: `senaryo-yazari` tam metin + `ses-yonetmeni` okuma metni → Niyazi okur → `ses-muhendisi` temizler.
9. `animasyon-yonetmeni` (karakter + sahneler, Remotion) → `kurgu-editoru` (montaj, müzik, altyazı, render).
10. `thumbnail-tasarimcisi` + `youtube-paketleyici` (başlık, açıklama, etiket, bölümler).
11. `hakem` son kalite kontrolü → Niyazi onayı → yükleme (onaylı).

Her ajan işini **test ederek** teslim eder (bkz. `docs/kalite-kapilari.md`): test çıktısı olmadan teslim yok.

## Teknik kararlar
- Video motoru: **Remotion** (React ile programatik video). Resmi skill: `.claude/skills/remotion-best-practices`.
- Dudak senkronu: **Rhubarb Lip Sync** (sesten ağız şekli A–H, X zaman çizelgesi). Türkçe için `--recognizer phonetic`.
- Karakter: Niyazi'nin görseli katmanlara ayrılır (kafa, gövde, kollar, eller, bacaklar, 9 ağız şekli, göz kırpma) ve Remotion'da kemik/pivot ile hareket ettirilir. Kalite referansı gelince AI image-to-video (ör. Hedra Omnia, Kling Avatar) ile kör test yapılır; seçim teste göre.
- Ses temizliği: ffmpeg (highpass, de-ess, loudnorm −14 LUFS) + DeepFilterNet gürültü giderme. Altyazı: Whisper (kelime zamanlı) → SRT + videoya gömülü.
- Kurgu kodda: `video/` Remotion projesi (henüz kurulmadı).

## Kurallar
- Rakam uydurma. Doğrulanmış (kaynaklı), arama özeti, tahmin ayrı etiketlenir.
- Videolar yatırım tavsiyesi vermez; geleceğe dair her şey "senaryo" diye sunulur, açıklamaya yasal not eklenir.
- Telifli müzik/görüntü yok: yalnız lisanslı veya kendi üretimimiz.
- Rakip kanallar kopyalanmaz: format, hook tipi, tempo gibi desenler çıkarılır; içerik, karakter, görsel dil özgündür.
- Her iş commit + push edilir (konteyner silinir).

## Dosya düzeni
- `.claude/agents/` ajanlar · `.claude/commands/` komutlar · `.claude/skills/` skill'ler
- `docs/` kalıcı bilgi (viralite modeli, kalite kapıları, rakip analizi, kanal kimliği)
- `assets/karakter/`, `assets/referans/`, `assets/ses-ham/` Niyazi'nin dosyaları · `uretim/` video başına çalışma klasörü
