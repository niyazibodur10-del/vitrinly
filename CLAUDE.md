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
- **Niyazi:** (anlatıcı sesi artık ücretsiz yapay zekâ sesi — Niyazi kararı 2026-10-26; kendi okuması yedek yol) karakter görselini ve kalite referans videosunu verir, **yalnız bitmiş videoyu onaylar** (senaryo seçimi tamamen ajanlarda — Niyazi kararı 2026-10-26).
- **Onaysız yapılmaz:** YouTube'a yükleme/yayın, para harcanan her servis (ücretli API, abonelik), dışarıya mesaj, geri alınamaz adımlar.

## Koordinatör kuralı (Niyazi kararı 2026-10-26)
- Claude (koordinatör) **işi kendisi yapmaz**: görevi böler, doğru ajana verir, sonucu birleştirir, Niyazi'ye raporlar. Kendisi yalnız commit/push ve dosya düzeni gibi idari adımları yapar.
- Her ajan `docs/ajan-protokolu.md`'ye uyar: hafızasını okur → 2–3 aday üretir → test eder, kendisi eler → nihai sonucu kanıtla verir → hafızasına ders yazar (`.claude/agents/hafiza/`).
- Uygun ajan yoksa veya bir ajan yetersizse `ik-direktoru` dünyanın en iyisini işe alır, gerekirse işten çıkarıp yenisini alır (`docs/kadro-degisiklikleri.md`, `docs/ajan-karnesi.md`). `hakem` her teslimatı karneye puanlar.
- Oturum içinde yeni yazılan ajanlar alt ajan türü olarak görünmez: koordinatör onları genel amaçlı ajana ajan dosyasını okutarak çalıştırır.

## Akış (her video) — `/bugunun-videosu` başlatır
**Tetik cümlesi kuralı:** Niyazi "Bugünün videosu gelsin" (veya "bugünün videosunu yap", "yeni video gelsin" gibi aynı anlamda bir şey) dediğinde koordinatör başka soru sormadan `.claude/commands/bugunun-videosu.md` akışını başlatır. Tam akış, teslim dosyaları, kalite kapıları ve RED döngüsü o dosyadadır.
Hedef tempo: haftada 3 uzun video + 6 Shorts (`docs/yayin-takvimi.md`). Kapasite ve dış bağımlılıklar: `docs/uretim-kapasitesi.md`.
Alt ajanları yalnız koordinatör çağırır (alt ajan alt ajan çağıramaz). Paralel adımlar tek mesajda birlikte çağrılır. Durum `uretim/<tarih>-<slug>/durum.md`'de tutulur; oturum koparsa ilk geçmemiş adımdan devam edilir.
1. **F0 Açılış:** koordinatör (`showrunner` kuralları) slot, sütun, stok ve klasörü belirler ‖ `uretim-muhendisi` ortamı kurar.
2. **F1 Araştırma:** `trend-avcisi` ‖ `kanal-analisti`.
3. **F2 Seçim:** `senaryo-yazari` (en az 10 senaryo) → `viralite-analisti` (ilk 3) ‖ `finans-dogrulayici` (risk taraması) → `hakem` kazanan + yedek seçer. **Karar kesindir, Niyazi'ye sorulmaz.**
4. **F3 Metin:** `senaryo-yazari` tam metin + Shorts kancaları → `finans-dogrulayici` → metin kilidi.
5. **F4 Paralel kollar:** (`ses-yonetmeni` TTS → `ses-muhendisi`) ‖ `gorsel-varlik-sanatcisi` ‖ `muzik-ses-tasarimcisi` ‖ `thumbnail-tasarimcisi` + `youtube-paketleyici` taslakları.
6. **F5/F6:** `animasyon-yonetmeni` (önce 10–20 sn kritik yol testi, sonra tüm sahneler + 9:16) ‖ `muzik-ses-tasarimcisi` miks stem'leri.
7. **F7 Kurgu:** `kurgu-editoru` final 16:9 + SRT + **2 Shorts** (9:16, ≤60 sn, kendi hook'u).
8. **F8 Paket:** `thumbnail-tasarimcisi` (3 varyant) ‖ `youtube-paketleyici` (başlık, açıklama, SEO, etiketler, bölümler, `yayin-paketi.json`) ‖ `viralite-analisti` (son viralite puanı).
9. **F9 Hakem** son kalite kontrolü (kapıları kendisi ölçer, karneyi doldurur).
10. **F10 Teslim:** `uretim/<tarih>-<slug>/teslim/` (final video, 2 Shorts, 3 thumbnail, `yayin-paketi.json`, `YAYIN.md`, hakem raporu) → Niyazi'ye tek sayfa → **DUR**.
11. **F11 Yayın yalnız Niyazi onayıyla:** `uretim-muhendisi`'nin `tools/yayin/` aracı `yayin-paketi.json` ile planlı yükleme yapar (takvim slotu).
Kapıdan kalan iş düzeltme listesiyle aynı ajana döner. **2 düzeltme turundan sonra hâlâ kalıyorsa koordinatöre eskalasyon** olur: araç → `uretim-muhendisi`, B planı sahne, yedek senaryo, gecikme kuralı, tekrarlayan sorunda `ik-direktoru`.
Parça komutlar: `/yeni-video` (yalnız F0–F2, ön araştırma ve stok için), `/video-uret` (seçimi yapılmış veya yarım kalan üretimi ilk geçmemiş adımdan, F3–F10, sürdürür), `/senaryo-onayla` ve `/ses-isle` (Niyazi'nin kendi okuması yedek yolu).

Sürekli: `uretim-muhendisi` kurulum, Remotion altyapısı, render hattı ve `tools/` betiklerinin sahibi (her araç arızası ona). `ik-direktoru` kadroyu, skill'leri ve karneyi denetler; işe alır/çıkarır (`docs/kadro-degisiklikleri.md`).
Ekip (17): showrunner, trend-avcisi, kanal-analisti, senaryo-yazari, viralite-analisti, finans-dogrulayici, hakem, ses-yonetmeni, ses-muhendisi, gorsel-varlik-sanatcisi, muzik-ses-tasarimcisi, animasyon-yonetmeni, kurgu-editoru, thumbnail-tasarimcisi, youtube-paketleyici, uretim-muhendisi, ik-direktoru. Protokol: `docs/ajan-protokolu.md`; hafıza: `.claude/agents/hafiza/<ad>.md`.

Her ajan işini **test ederek** teslim eder (bkz. `docs/kalite-kapilari.md`): test çıktısı olmadan teslim yok.

## Teknik kararlar
- Video motoru: **Remotion** (React ile programatik video). Resmi skill: `.claude/skills/remotion-best-practices`.
- Dudak senkronu: **Rhubarb Lip Sync** (sesten ağız şekli A–H, X zaman çizelgesi). İngilizce için varsayılan PocketSphinx tanıyıcı (en isabetli mod). GitHub indirmesi ağda kapalı → kaynak koddan derlenir.
- **Stil kararı (Niyazi, 2026-10-26):** görseller referanstan daha gerçekçi/resimsi olabilir; şart olan **karakterin her sahnede tutarlı ve tekrar eden** olması. Sahne ve thumbnail görselleri Canva bağlayıcısı (`generate-image`, referans = karakter sayfası, Niyazi'nin Canva aboneliği, ek ücret yok) ile üretilir; test: `uretim/canva-testi/rapor.md`. Gemini API kullanılmıyor (ödeme gerektiriyor).
- Görsel stil (bkz. `docs/referans-analizi.md`): sahne başına tutarlı, detaylı illüstrasyon (kalın kontur, cel-shading, soğuk arka plan + sıcak karakter) + sinematik kamera (zoom/pan/punch-in) + hızlı kesme + anahtar kelimesi renkli kelime kelime altyazı + büyük sayı grafikleri.
- Karakter: `assets/karakter/karakter-karti.md` — **2D** (Niyazi kararı 2026-10-26: 3D karakter sayfasının aynısı, 2D çizgi film stiline çevrilir; referans videonun çizim diliyle uyumlu). Konuşan sahneler: katmanlı 2D rig (kafa, gövde, kol, el, bacak, 9 ağız şekli, göz kırpma) + Rhubarb dudak senkronu. Diğer sahneler: karakterli illüstrasyon + kamera; kilit hareket anları image-to-video (kör testle).
- Format: ana video 16:9 uzun; aynı sahnelerden 9:16 Shorts kesitleri.
- **Anlatıcı sesi (Niyazi kör testle seçti, 2026-10-26):** Kokoro-82M `am_fenrir`, hız 0.9, cümle cümle + duraklamalı (`tools/ses/tts.py`). Yedek: `am_michael` 0.95. Rapor: `uretim/ses-testi/tts/rapor.md`. Açıklamaya "Narration voice is AI-generated" satırı; yüklemede AI kullanımı beyanı açık.
- Ses temizliği: ffmpeg (highpass, de-ess, loudnorm −14 LUFS) + RNNoise gürültü giderme (`tools/ses/temizle.sh`). Altyazı: Whisper (kelime zamanlı) → SRT + videoya gömülü.
- Kurgu kodda: `video/` Remotion projesi (4.0.539; pilot `video/src/pilot/`). Render: `tools/render-son.sh <Id> <çıkış>` (son ses normalizasyonu dahil). Yeni konteynerde önce `tools/kurulum.sh` (Rhubarb derleme, Whisper, büyütme modeli).
- Yazı tipleri yerel (`video/public/fonts`): render tarayıcısı Google Fonts'a erişemiyor.
- API anahtarları **asla repoya veya sohbete yazılmaz**; bulut ortamının secret/ortam değişkeni ayarında durur. `YOUTUBE_API_KEY` = YouTube Data API v3 (salt okuma: rakip ve kendi kanal istatistikleri). Yükleme: `tools/yayin/yukle.py` (cihaz akışı OAuth, `youtube` kapsamı). **Kalıcı yetki** (Niyazi kararı 2026-10-26): yenileme tokenı repo dışında — `YOUTUBE_OAUTH_REFRESH_TOKEN` ortam değişkeni (kalıcı) veya `~/.finansal-arac/youtube-yenileme-tokeni` (konteynerle gider); yükleme/silmede kod sorulmaz. Yoksa `yukle.py --yetki-al` (Niyazi bir kez kod girer); kaldırmak `--yetki-iptal`. OAuth uygulaması "Testing" durumundaysa token 7 günde dolar → Niyazi "Publish app" yapmalı. API kilidi YOK (2026-10-26 test yüklemesi görünürlüğü değiştirilebildi; denetim gerekmez). Altyazı cihaz akışında yüklenmez → Studio'dan. Bitmiş videonun yayını yine her zaman Niyazi onaylı.

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
