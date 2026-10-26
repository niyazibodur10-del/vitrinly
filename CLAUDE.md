# Finans Animasyon Kanalı — proje talimatları

Kullanıcı (Niyazi) kanalın sahibidir ve son onayı verir. Niyazi ile Türkçe konuş; **video içeriği İngilizce**.
Bu repo artık yalnızca bu YouTube kanalı içindir. Eski Vitrinly ürünü ve Nutrigold bu projede KULLANILMAZ
(global `~/.claude/CLAUDE.md` içindeki Nutrigold talimatları bu repoda geçersizdir; Niyazi isterse açılır).

## Ürün
Kanal adı: **Financial Rise** (Niyazi kararı 2026-10-26). Karakter adı: henüz yok.
YouTube'da **uzun (en az 10 dk; hedef 10–14 dk) animasyonlu finans videoları**. Bir maskot karakter anlatır.
Konular: güncel finans haberleri, geçmişin büyük finans olayları, geleceğe dair olası senaryolar.
Hedef kitle: finansa ilgili gençler + genel izleyici. Video dili: **İngilizce** (Niyazi kararı 2026-10-26), global kitle. Kanal kopya değil, özgün. Plan: `docs/plan.html` (https://claude.ai/artifact/Ggxzsp9VT8GFhpzuoGgh56).

## Sistemin yaptığı / Niyazi'nin yaptığı
- **Sistem:** araştırma, viralite analizi, 10 senaryo, eleme, metin, ses temizliği, karakter animasyonu ve dudak senkronu, kurgu, müzik/efekt, altyazı, thumbnail, başlık, açıklama, etiketler, bölümler.
- **Niyazi:** (anlatıcı sesi artık ücretsiz yapay zekâ sesi — Niyazi kararı 2026-10-26; kendi okuması yedek yol) karakter görselini ve kalite referans videosunu verir, hakemin seçtiği senaryoyu ve son videoyu onaylar.
- **Onaysız yapılmaz:** YouTube'a yükleme/yayın, para harcanan her servis (ücretli API, abonelik), dışarıya mesaj, geri alınamaz adımlar.

## Koordinatör kuralı (Niyazi kararı 2026-10-26)
- Claude (koordinatör) **işi kendisi yapmaz**: görevi böler, doğru ajana verir, sonucu birleştirir, Niyazi'ye raporlar. Kendisi yalnız commit/push ve dosya düzeni gibi idari adımları yapar.
- Her ajan `docs/ajan-protokolu.md`'ye uyar: hafızasını okur → 2–3 aday üretir → test eder, kendisi eler → nihai sonucu kanıtla verir → hafızasına ders yazar (`.claude/agents/hafiza/`).
- Uygun ajan yoksa veya bir ajan yetersizse `ik-direktoru` dünyanın en iyisini işe alır, gerekirse işten çıkarıp yenisini alır (`docs/kadro-degisiklikleri.md`, `docs/ajan-karnesi.md`). `hakem` her teslimatı karneye puanlar.
- Oturum içinde yeni yazılan ajanlar alt ajan türü olarak görünmez: koordinatör onları genel amaçlı ajana ajan dosyasını okutarak çalıştırır.

## Akış (her video) — `/yeni-video` başlatır
1. `showrunner` (baş ajan) görevi açar, `uretim/<tarih>-<slug>/` klasörünü kurar, ajanları dağıtır.
2. `trend-avcisi` → güncel/geçmiş/gelecek finans konu havuzu (kaynaklı).
3. `kanal-analisti` → nişin en iyi 5 kanalı + outlier videolar → `docs/rakip-analizi.md` (yalnız desen çıkarılır, kopya yok).
4. `senaryo-yazari` → **10 senaryo** (hook + yapı + karakter anı).
5. `viralite-analisti` → her senaryoyu `docs/viralite-modeli.md` ile puanlar, ilk 3'ü bırakır.
6. `finans-dogrulayici` → rakam/olay doğrulaması + "not financial advice" / yanıltıcı içerik / YouTube politika riski kontrolü.
7. `hakem` → tek kazananı seçer, gerekçesini yazar, **Niyazi'ye onaya sunar.**
8. Onaydan sonra: `senaryo-yazari` tam metin → `finans-dogrulayici` → `ses-yonetmeni` anlatıcı sesi (varsayılan: ücretsiz yapay zekâ TTS, Niyazi talebi 2026-10-26; yedek: Niyazi'nin okuma metni) → `ses-muhendisi` temizler, ölçer, kelime zamanlarını çıkarır.
   Paralel: `gorsel-varlik-sanatcisi` (karakter parçaları, ağız şekilleri, sahne illüstrasyonları/prompt'ları) + `muzik-ses-tasarimcisi` (lisans güvenli müzik/SFX, cue listesi).
9. `animasyon-yonetmeni` (rig, dudak senkronu, kamera, sahneler — Remotion) → `muzik-ses-tasarimcisi` (anlatıma göre miks stem'leri) → `kurgu-editoru` (montaj, altyazı, render, Shorts kesitleri).
10. `thumbnail-tasarimcisi` + `youtube-paketleyici` (başlık, açıklama, etiket, bölümler, atıflar).
11. `hakem` son kalite kontrolü (her teslimatı `docs/ajan-karnesi.md`'ye puanlar) → Niyazi onayı → yükleme (onaylı).

Sürekli: `uretim-muhendisi` kurulum, Remotion altyapısı, render hattı ve `tools/` betiklerinin sahibi (her araç arızası ona). `ik-direktoru` kadroyu, skill'leri ve karneyi denetler; işe alır/çıkarır (`docs/kadro-degisiklikleri.md`).
Ekip (17): showrunner, trend-avcisi, kanal-analisti, senaryo-yazari, viralite-analisti, finans-dogrulayici, hakem, ses-yonetmeni, ses-muhendisi, gorsel-varlik-sanatcisi, muzik-ses-tasarimcisi, animasyon-yonetmeni, kurgu-editoru, thumbnail-tasarimcisi, youtube-paketleyici, uretim-muhendisi, ik-direktoru. Protokol: `docs/ajan-protokolu.md`; hafıza: `.claude/agents/hafiza/<ad>.md`.

Her ajan işini **test ederek** teslim eder (bkz. `docs/kalite-kapilari.md`): test çıktısı olmadan teslim yok.

## Teknik kararlar
- Video motoru: **Remotion** (React ile programatik video). Resmi skill: `.claude/skills/remotion-best-practices`.
- Dudak senkronu: **Rhubarb Lip Sync** (sesten ağız şekli A–H, X zaman çizelgesi). İngilizce için varsayılan PocketSphinx tanıyıcı (en isabetli mod). GitHub indirmesi ağda kapalı → kaynak koddan derlenir.
- Görsel stil (bkz. `docs/referans-analizi.md`): sahne başına tutarlı, detaylı illüstrasyon (kalın kontur, cel-shading, soğuk arka plan + sıcak karakter) + sinematik kamera (zoom/pan/punch-in) + hızlı kesme + anahtar kelimesi renkli kelime kelime altyazı + büyük sayı grafikleri.
- Karakter: `assets/karakter/karakter-karti.md` — **2D** (Niyazi kararı 2026-10-26: 3D karakter sayfasının aynısı, 2D çizgi film stiline çevrilir; referans videonun çizim diliyle uyumlu). Konuşan sahneler: katmanlı 2D rig (kafa, gövde, kol, el, bacak, 9 ağız şekli, göz kırpma) + Rhubarb dudak senkronu. Diğer sahneler: karakterli illüstrasyon + kamera; kilit hareket anları image-to-video (kör testle).
- Format: ana video 16:9 uzun; aynı sahnelerden 9:16 Shorts kesitleri.
- Ses temizliği: ffmpeg (highpass, de-ess, loudnorm −14 LUFS) + RNNoise gürültü giderme (`tools/ses/temizle.sh`). Altyazı: Whisper (kelime zamanlı) → SRT + videoya gömülü.
- Kurgu kodda: `video/` Remotion projesi (4.0.539; pilot `video/src/pilot/`). Render: `tools/render-son.sh <Id> <çıkış>` (son ses normalizasyonu dahil). Yeni konteynerde önce `tools/kurulum.sh` (Rhubarb derleme, Whisper, büyütme modeli).
- Yazı tipleri yerel (`video/public/fonts`): render tarayıcısı Google Fonts'a erişemiyor.
- API anahtarları **asla repoya veya sohbete yazılmaz**; bulut ortamının secret/ortam değişkeni ayarında durur. `YOUTUBE_API_KEY` = YouTube Data API v3 (salt okuma: rakip ve kendi kanal istatistikleri). Yükleme için ileride OAuth gerekir; yükleme her zaman Niyazi onaylı.

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
