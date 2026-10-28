# Ortak dersler (tüm ajanlar)

Okuma kuralı: dosyanın tamamını okuma. `grep -n '^## ' docs/ogrenme/ortak-dersler.md` ile başlıkları gör, yalnız alanınla ilgili bölümleri aç. Yeni ders doğru başlığın altına, en fazla 3 satır yazılır. Bölüm 25 maddeyi geçerse ik-direktoru budar.
(2026-10-28: ik-direktoru konu başlıklarına göre yeniden düzenledi. İçerik korundu, tekrarlar birleştirildi.)

## Hazır betikler (yeniden yazma, kopyala + parametrele)
Kalıcı araçlar `tools/` altında (sahibi uretim-muhendisi): `render-son.sh`, `render-parca.sh` (düzeltme turunda parça render), `senkron-testi.py`, `altyazi-uret.py`, `altyazi-hiza.py`, `viralite.py`, `disk-durum.sh`, `kadro-kontrol.py`; `tools/ses/`: `tts.py`, `tts-son.sh`, `temizle.sh`, `hizala.py`, `hiza-dogrula.py`, `rhubarb-hazirla.py`, `cumle-whisper.py`, `yaziya-dok.py`, `hata-orani.py`, `ses-olc.py`, `miks.py`; `tools/yayin/` (yükleme, kanal).
Video klasöründe kalan kapı betikleri (1929 videosu, `uretim/2026-10-26-1929-1000-dolar/`). Sonraki videoda kopyalanır; `tools/`'a taşınması uretim-muhendisi'nden istendi (2026-10-28):
| Faz / sahip | Betik |
|---|---|
| F1 trend-avcisi | `01-arastirma/kaynak-kontrol.py`, `olcum/youtube_arama.py`, `olcum/wiki_pageviews.py`, (2026-10-28 klasöründe) `olcum/haber_rss.py`, `olcum/kaynak_bul.py` · kanal-analisti `01-arastirma/etiket_test.py` |
| F2 senaryo-yazari / viralite / politika / hakem | `02-senaryo/senaryo-kontrol.py`, `viralite-duyarlilik.py`, `viralite-outlier.py`, `politika-tarama.py`, `hakem-karar.py` |
| F3 senaryo-yazari / finans / politika | `03-metin/metin-kontrol.py` (kpm parametresini **160** yap), `dogrulama-kontrol.py`, `dogrulama-hesap.py`, `veri/hesap.py`, `politika-denetim.py` |
| F4 ses-muhendisi | `04-ses/son-islem.sh`, `olc.py`, `son-olc.py`, `okuma-hazirla.py` |
| F4 gorsel-varlik-sanatcisi | `05-gorsel/araclar/prompt-uret.py`, `prompt-kontrol.py`, `stil-olcum.py`, `rig-yama.py` |
| F4/F6 muzik-ses-tasarimcisi | `06-muzik/lisans-kontrol.py`, `aday-olc.py`, `cue-uret.py`, `f6.py`, `ozgun-uret.py` |
| F5 animasyon-yonetmeni | **genel (2026-10-28):** `tools/animasyon/rhubarb-toplu.py` (← rhubarb-tum.py, paralel), `sahne-veri.py` (← hazirla-tam.py veri kısmı, birebir), `csv-ts.py` (← grafik-veri.py), `sessizlik_kapisi.py`; videoya özel kalan: varlık hazırlığı (`hazirla*.py` görsel kısmı), `agiz-gorunur.py`, `efekt-cue.py` |
| F7 kurgu-editoru | `08-kurgu/kurgu_ses.py`, `ses_kayma.py`, `srt_kontrol.py`, `kadans.py` |

## Akış ve hız (koordinatör + herkes)
- 2026-10-28 (uretim-muhendisi, hız araçları): yeni video `tools/yeni-video.sh <tarih-slug> --kisa <Önek>` ile açılır (klasör + durum.md + yeniden üretim tarifi + kit kopyası). Taslak render `--onizleme` (3,6x hızlı, yayın için değil). Uzun video `render-parca.sh` ile: değişen parçayı KENDİ bulur (`--yeniden` gerekmez), `--kaynak <BaşkaId>` ile başka kompozisyonun parçaları tohumlanır. Whisper'ı dosya başına değil toplu çağır (`yaziya-dok.py --model small.en a.wav a.json b.wav b.json`, −%39). Her video `uretim/<klasör>/yeniden-uret.adimlar`'ı doldurur (git dışı her büyük dosya için "dosya | komut"); git dışı kaynak (müzik, wav) tarifte yeniden üretilemiyorsa git'e girer — 1929'da 3 müzik kaynağı eksik çıktı.
- 2026-10-28: 1929 videosu commit zamanlarına göre ~5 sa aktif çalıştı ama 25,5 sa sürdü. Aradaki üç ~4 saatlik boşluk oturum limitiydi. Darboğaz CPU değil token: kısa okuma, tek ölçüm, kısa rapor ve ara commit kuralları (`docs/ajan-protokolu.md` §1–5) bu yüzden zorunlu.
- 2026-10-28: F8'i erken başlatmak işe yaradı (paket ve thumbnail F5 sürerken bitti, F7'den sonra yalnız 7 dk fark kontrolü kaldı). Akışta artık F8a (erken) ve F8b (fark) var.
- 2026-10-27: Kanca/sahne zamanları önce metin tahmininden gelir; kesin zamanlar ses kolundan (`04-ses/kelimeler-hizali.json`) sonra alınır. Görsel olay zamanları `06-muzik/animasyon-efekt-cue.json`'da tutulur.

## Ağ ve erişim
- Engelli: GitHub sürüm indirmeleri, pixabay, incompetech, freesound, instagram, socialblade, youtube watch sayfası (302). Açık: git clone, Hugging Face, PyPI, npm, download.pytorch.org, archive.org, opengameart, kenney.nl, freemusicarchive.org, raw.githubusercontent.com (curl; github.com sayfaları WebFetch'te içerik vermeyebilir), youtube.com kanal RSS (`/feeds/videos.xml?channel_id=`), `i.ytimg.com`, `youtubeanalytics.googleapis.com` (OAuth, `yt-analytics.readonly`), oauth/googleapis/accounts.google.com. İşe başlamadan ihtiyacın olan adresi yeniden ölç.
- Render tarayıcısı Google Fonts sertifikasına güvenmiyor → yazı tipleri yerel (`video/public/fonts`).
- Hugging Face `trust_remote_code` gerektiren modeller çalıştırılmaz; yerel ağırlık + bilinen kütüphane.

## Araçlar, ortam, render
- Konteyner 4 vCPU. Render, Whisper, TTS, Real-ESRGAN aynı anda koşmaz (paralelde TTS ~2,2x, Whisper ~1,8x yavaşlar). Süre ölçerken `uptime` ile yükü not et.
- Render hızı ~5,4 kare/sn ≈ gerçek sürenin 5,5 katı (12 dk ≈ 66 dk, ≈450 MB). Final mp4'ler git'e girmez (100 MB sınırı).
- Kokoro (espeak-ng) uzun kurulum yolunda kırılır (~160 karakter) → araçlar `~/.finansal-arac` altında.
- `render-parca.sh`: son muxta `-t <görüntü süresi>` kullanılır (eski `-shortest` son 4 kareyi kesiyordu, düzeltildi). Kurgu katmanı vurgusuz karelerde sahne kompozisyonuyla piksel-aynı → parça önbelleği hardlink'le yeniden kullanılır, yalnız değişen parça render edilir (final 4 dk).
- Whisper ilk model yüklemesi yavaş (small 44 sn, medium 136 sn); aynı sese ±2 kelime oynar → tek sayıya değil tekrar eden hatalara bak. Aynı model/ayarla Whisper deterministik (hakem JSON'u kurgu-editoru'nunkiyle bayt bayt aynı çıktı) → aynı sha256'lı dosyada tam yeniden koşu gereksiz.

## Ses ve altyazı
- Anlatıcı her zaman karar verilen ses: Kokoro `am_fenrir` 0.9 (~153 Hz). Render öncesi `video/public/*-ses.wav` kaynağı kontrol edilir (pilot v1 yanlış sesle render edilmişti).
- **Konuşma hızı: am_fenrir 0.9 uzun metinde 161,6 kelime/dk** (1929: 1.701 kelime = 10:31,6; metin 143 varsaymıştı, −82 sn). Süre tahmini **160 kpm**; ≥10 dk için ≥1.750 kelime (≈10:56, 25+ sn pay). Pay gerekirse hız değil duraklama (`--cumle/--paragraf`) artırılır. İlk 30 sn 168 kpm, rakip bandı 175–225.
- Mono anlatım stereoya kopyalanınca LUFS ~+3 ölçülür → normalizasyon son stereo dosyada (`tools/render-son.sh`).
- Altyazı/dudak senkronu zamanı `04-ses/kelimeler-hizali.json`'dan (akustik p95 ≤15 ms). Ham `kelimeler.json` cümle başlarında 250–500 ms erken. `altyazi-hiza.py` ham Whisper'a karşı sahte KALDI verir → son kapı render sesinden yeni Whisper ile.
- `hata-orani.py` sayı, sıra sayısı, ay+gün, on yıl ve para biçimini eşler (1929 WER %2,5 → %0,9). ANLATIM'da sayılar yazıyla, rakam GÖRSEL'de.
- 161,6 kpm'de 16 SRT bloğu >21 kr/sn çıktı (en yüksek 24,1). Sınır 25; daha hızlı ses seçilirse SRT blokları bölünür.

## Animasyon, kurgu, SFX
- SFX vuruşları kelime zamanına değil **görsel olay zamanına** bağlanır: kaynak `06-muzik/animasyon-efekt-cue.json` (animasyon-yonetmeni, kare doğruluk). 1929'da 20+ vuruş 0,4–3 sn kayıktı, kurguda yeniden zamanlandı. Kapı: her vuruş görsel olaya ±2 kare.
- **Abone ol animasyonu (Niyazi 2026-10-28, her video):** profil resmi (`uretim/kanal-kimligi/profil-800.png`) + Subscribe düğmesi + imleç tıklaması + klik sesi. Uzun videoda 3–4 kez (ilk ~60–90 sn'den sonra, ortalarda, kapanışta; doruk/açıklama anına binmez), her Shorts'ta en fazla 1 kez, sonda. Zincir: senaryo-yazari anları işaretler (`ABONE-n`) → animasyon-yonetmeni kare zamanını `animasyon-efekt-cue.json`'a `tur: "abone"` diye yazar ve o alanı boş bırakır → muzik-ses-tasarimcisi klik sesini (lisans kaydında) SFX stem'ine koyar → kurgu-editoru ortak bileşeni final katmana yerleştirir ve sayar → hakem sayımı ve sesi doğrular. Ortak bileşen `video/src/ortak/` (uretim-muhendisi). 1929'daki satır içi `Abone` (k1929/b3.tsx) profil resmi, imleç ve ses içermiyordu.
- Dudak senkronu kapısı ağzın göründüğü aralıklarda (`07-animasyon/agiz-gorunur.json`) + tam sahnede: `tools/senkron-testi.py --araliklar … [--bant formant] [--ofset <kesit başı>]`. Rig yamasında alfa taban kesik silüetiyle sınırlanır (zemin pikseli hale yapıyor).
- Kompozisyonlar sahne başına (`K<slug>-Sxx`) + tam (`K<slug>Tam`) verilir. Shorts kesit başı altyazı öbeği başına oturur. Sahne parçası uzatılırsa sonraki cümlenin sesi sızar → köprü kuyruğu sessiz render.
- 1929 açık riskleri (F12'de bak): S18'de ~1,5 sn boş an; Shorts 1 S10'da grafik ~4 sn geç geldi → dikey kesitte grafik ≤1 sn'de girer. Shorts'ta tek zaman penceresi kullanılır (12/48 ay karışıklığı).

## Metin ve doğrulama
- "Toparlanma X yıl sürdü" iddiaları nominal **fiyat** endeksine dayanır → "price only, before dividends" notu (metin, grafik, paket).
- Kaldıraç matematiği Shorts kancalarında da betikle doğrulanır (30:1'de tam silinme ~%3,2).
- Her rakamın kaynağı `03-metin/metin.md` §8 tablosunda, türetilenler `03-metin/veri/hesap.py`'de. FDIC banka kaybı: Brief History of Deposit Insurance Bölüm 3 Tablo 5 (PDF → pdftotext). FRED CSV doğrudan curl.
- AI personası riski en çok Leo'nun **bugüne dönük kuralında** ve ekrandaki not/levhada çıkar ("I believe now…", "DO NOT TOUCH", "most people picked wrong"). Emir yerine betimleyici tarih cümlesi.

## Politika, lisans, yayın (YPP)
- YPP: 1 Şubat 2027'den yeni başvuranlar için 1.000 abone + 8.000 saat/12 ay veya 20 M Shorts/90 gün (support.google.com/youtube/answer/12843009). Shorts akışı saatleri uzun video saatine sayılmaz → uzun video ana yol, Shorts huni.
- "Inauthentic content" (eski "repetitious"): şablon/seri üretim ve "aynı durumda aynı sonuç" videoları para kazanamaz; kendi karakterini AI ile görselleştirmek izinli (answer/1311392). Sahne görselleri videolar arası aynen tekrarlanmaz.
- "AI Personas Related to Sensitive Topics": kendini uzman gibi sunup finans tavsiyesi veren AI personası para kazanamaz → Leo maskot kalır, tavsiye vermez; açıklamada "Narration voice is AI-generated" (answer/1311392).
- Başlık/thumbnail ayrıca puanlanır (answer/6162278 "all portions"): doğrulanmamış pay, gerçek kişiye suç çağrışımı, "who got rich" çerçevesi metin temizken bile risk.
- `durum.sentetik_medya` video başına monetizasyon-uyum-uzmani kararı (youtube-paketleyici yazar, hakem kontrol eder). Gerçekçi olmayan animasyon beyandan muaf olabilir (answer/14328491); AI ses satırı her durumda kalır.
- Lisans: NC/ND/"kişisel kullanım" medya yok. Müzik/efekt yalnız `assets/muzik`, `assets/efekt`, `06-muzik/kaynak` (CC0 veya kendi üretim); kayıt `assets/LISANSLAR.md` + `06-muzik/lisans-kaydi.md`, kanıt `assets/lisans-kanit/`. `.gitignore` *.wav dışlar → varlıklar FLAC/OGG/MP3/M4A. Kapı: `06-muzik/lisans-kontrol.py` exit 0. CC BY atıf metni açıklamaya aynen.
- Yükleme `tools/yayin/yukle.py`. Cihaz akışı altyazı yükleyemez → Studio. Test & Compare'de belirsiz sonuçta ilk yüklenen varyant kalır → ilk sıraya en iyi ön tahmin. Planlı/gizli videoda test kurulamaz, API yok (Studio masaüstü). Başlık testi thumbnail testinden sonra.

## Araştırma ve veri
- YouTube Data API `search` ayrı günlük tavanlı (15 sorguda 429), proje paylaşımlı → `playlistItems`/`videos` (1 birim) tercih. Kota dolunca `python3 -m yt_dlp --flat-playlist --print "%(id)s" "ytsearch15:<sorgu>"` + `videos.list`. yt-dlp otomatik altyazı ~8 videoda sonra bot kontrolü.
- `marketing-skills:youtube-full` bir veri aracıdır (transkript/RSS/arama); SEO veya retention kuralı vermez.
- Wikimedia pageviews: UA başlığı şart, istekler arası ≥4–8 sn. Link kanıtı = HTTP 200 + sayfada anahtar kelime (soft-404 var).
- 2026-10-28 (trend-avcisi): güncel haber kaynağı için Google News RSS + `googlenewsdecoder` (PyPI) açık ve hızlı; Reuters/WSJ/Bloomberg/NYT curl'de kapalı. Hazır betik: `uretim/2026-10-28-yeni-video/01-arastirma/olcum/kaynak_bul.py`. finans-dogrulayici F3'te aynı yolla birincil kaynak bulabilir.

## Görsel ve thumbnail
- Pillow: `Fredoka-700.woff2` değişken yazı tipi → `font.set_variation_by_axes([700])`; woff2 doğrudan açılır; Fredoka'da "ş" yok (Türkçe etikette DejaVuSans-Bold). RGBA'ya yarı saydam çizim ayrı katmana + `alpha_composite`. Kontur `cv2.dilate` + elips çekirdek.
- Banner güvenli alanı 2048x1152'de 1235x338 (answer/10456525); profil 98x98 görünür. Kanal görselleri `tools/gorsel/kanal-gorselleri.py --ad`.
