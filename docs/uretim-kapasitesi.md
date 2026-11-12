# Üretim kapasitesi ve darboğaz analizi (v1.3, 2026-10-28 — ortam optimizasyonu ölçümleri §0; v1.2 2026-10-26 tempo 2 + 4)

Soru: Haftada **2 uzun video** (10–14 dk, İngilizce) + **4 Shorts**, `/bugunun-videosu` akışıyla yapılabilir mi? (Niyazi kararı 2026-10-26; takvim `docs/yayin-takvimi.md` v2: Çarşamba + Pazar.)
**v1 notu:** Bu dosyanın v1–v1.1 sürümü haftada 3 uzun + 6 Shorts'u soruyordu. Sonucu: "şartlar sağlanırsa sınırda mümkün; iyi durumda ~27, kötü durumda ~54 saat/hafta otomatik üretim; her hafta en az bir gecikme beklenir" [H/T]. Bu sonuç ve kalite/politika riski tempo kararının gerekçesine girdi. Ayrıntılar git geçmişinde.
Etiketler: **[Ö]** bu ortamda ölçüldü, **[H]** ölçüm veya bilinen değerden hesap, **[AÖ]** arama özeti, **[T]** tahmin.
Henüz hiçbir tam video üretilmedi. Süreler pilot klip (18,8 sn) ve ajanların iş tanımlarından çıkarılmış tahminlerdir. İlk 3 videoda her adımın gerçek başlangıç ve bitiş saati `durum.md`'ye yazılır, bu dosya o verilerle v2'ye güncellenir.

## 0. Ortam optimizasyonu v1.3 (2026-10-28, uretim-muhendisi) [Ö]
İlk video (1929) ~1,5 gün sürdü (oturum limitleri dahil). Makine tarafındaki darboğazlar ölçüldü ve araçlar değişti. Ortam: 4 vCPU, 15 GB, boşta ölçüm (paralel render yokken).

| Adım | Önce | Sonra | Araç / not |
|---|---|---|---|
| Kurulum, temiz konteyner + boş önbellek | **407 sn** (sıralı pip) | **111 sn** (uv + 5 paralel iş; kritik yol Rhubarb derlemesi) | `tools/kurulum.sh` v2, sabit sürümler `tools/gereksinim/*.txt`; tekrar 2,3 → 1,5–1,9 sn |
| Kurulumu oturumda beklemek | her oturum elle | SessionStart kancası | `.claude/hooks/oturum-baslat.sh` (bulut konteyner durumu kancadan sonra önbelleğe alınır; model ısıtma arka planda) |
| Render, 600 kare (1929 en ağır bölüm); tam final 18.949 kare ≈ 31 dk (değişmedi, CPU sınırı) | 1×c4 152,0 sn | 2 parça×c2 **141,5 sn (−%7)**; Pilot 3 parça 60 → 47 sn (−%22) | `render-parca.sh --is 2` (varsayılan; tek parça kalınca c4) |
| Düzeltme turu: hangi parça değişti? | elle `--yeniden`/`--sifirla` (unutulursa eski görüntü yayına) | **otomatik iz**: her 6. kare 1/4 ölçek, toleranslı karşılaştırma | `render-parca.sh` + `tools/render-iz.py`; Pilot'ta tek rakam değişikliği → yalnız 1/3 parça; değişiklik yoksa 0 parça. İz maliyeti ~10 sn/600 kare |
| Önizleme (taslak) render | yok | 960x540 crf30 veryfast: 600 kare **42,3 sn (3,6x hızlı)** | `render-son.sh … --onizleme`, `render-parca.sh … --onizleme` (ayrı önbellek) |
| Kare kaybı (-shortest) | 1929 F7'de 4 kare | çıktı kare sayısı = kompozisyon, değilse HATA | `render-parca.sh` kapısı |
| Whisper, 3 dosya (76 sn ses) | 3 ayrı çağrı 43,7 sn | toplu tek model **26,7 sn (−%39)**, çıktı bayt bayt aynı | `yaziya-dok.py --model small.en a.wav a.json b.wav b.json …` (soğuk diskte her ayrı çağrı +40–130 sn) |
| Whisper, tek 60 sn dosya | 29,1 sn (4 iş parçacığı) | **22,3 sn** (2 iş parçacığı) | varsayılan `--is 2`; `cumle-whisper.py` da 2 iş parçacığı |
| TTS 16 cümle (55,6 sn ses) | 43,4 sn | **38,2 sn (−%12)** | `tts.py --is 2` (varsayılan). Kokoro deterministik değil |
| Rhubarb 6 sahne (150 sn ses) | 1×4 iş parçacığı 67,1 sn | **44,0 sn (−%34)** | `tools/animasyon/rhubarb-toplu.py --is 2` (12 dk ≈ 4,7 → 3,1 dk [H]) |
| Video başına iskelet | 1929'a özel betikler | genel araçlar | `tools/yeni-video.sh` (klasör + durum.md + tarif + kit kopyası + test kompozisyonu), `tools/animasyon/sahne-veri.py` (1929 veri-tam.ts ile birebir aynı çıktı), `csv-ts.py`, `rhubarb-toplu.py` |
| Konteyner gidince final mp4 | 6 betik + el bilgisi | tek komut | `tools/yeniden-uret.sh <klasör>` + `uretim/<klasör>/yeniden-uret.adimlar` (1929 tarifi hazır; ölçüm aşağıda) |

**Bu VM'de 2 iş parçacığı doyuyor:** Whisper, Rhubarb, TTS ve render'da "nproc kadar eşzamanlılık" yerine 2×(nproc/2) daha hızlı çıktı. Yeni araçta varsayılanı ölçmeden nproc yapma.
**Yeniden üretim testi** (temiz çalışma ağacı, boş parça önbelleği): `tools/yeniden-uret.sh 2026-10-26-1929-1000-dolar --kontrol` 15 adım hatasız (ilk denemede iki hata buldu ve düzeltildi: ffmpeg tarifin stdin'ini yutuyordu; final cue'sunun 3 CC0 müzik kaynağı git dışıydı → repoya alındı). Süre ≈ **41 dk**: ses zinciri (m4a → wav, f6 stem'leri 178 sn, kurgu miksi 16 sn, Shorts yatakları 1 sn) ~3,3 dk + final render ~33 dk (iz 122 sn + 11 parça ≈ 10 kare/sn + mux 74 sn) + 2 Shorts 130 + 154 sn. Sonuç yayınlanan dosyalarla: kare sayıları aynı (18.949 / 1.487 / 1.681), Shorts görüntüsü **bit-aynı** (PSNR inf), final PSNR ort. 68,8 dB (min 45,9; Chromium blur gürültüsü), ses −14,0 LUFS / TP −2,3 (yayınlanan −2,2). sha256 farklı (ses git'teki AAC'den).
**Kalan darboğaz:** tam render (1929: 18.949 kare ≈ 26–29 dk) CPU'ya bağlı; GPU yok. Düzeltme turları artık yalnız değişen parça (~3 dk/parça). Ajan tarafında en uzun faz hâlâ F5 sahne kodlaması → kit kopyası (`yeni-video.sh`) ilk adım; ortak bileşenlerin `video/src/ortak/`'a taşınması animasyon-yonetmeni ile birlikte yapılacak.

## 1. Ölçülen tek veri: render hızı [Ö]
- Ortam: 4 vCPU, 15 GB RAM, Remotion 4.0.539, `tools/render-son.sh` (h264 crf18 + 2 geçişli loudnorm).
- `Pilot` (18,8 sn, 564 kare, 1080p30): toplam **110,7 sn**. Sabit yük (bundle + tarayıcı, 2 kare) 6,6 sn, kalan ~104 sn. Yani ~5,4 kare/sn, **gerçek sürenin ~5,5 katı**.
- 12 dk video (21.600 kare) için **~66 dk** [H]. 2 Shorts (2×60 sn) için ~11 dk [H]. Gerçek videonun büyük bitmap'leri ve kamera hareketleri render'ı yavaşlatabilir [T]. **Güncelleme 2026-10-26 (hat testi, `docs/uretim-hatti-testi.md`):** Pilot v2 (423 kare) `--concurrency=4` ile ~8–10 kare/sn [Ö] → 12 dk ≈ 36–45 dk [H]; düzeltme turunda `tools/render-parca.sh` yalnız değişen parçayı render eder (~4–6 dk). TTS, Whisper ve Rhubarb artık kurulu ve ölçüldü (aynı belge).
- Dosya boyutu: pilot 11,7 MB / 18,8 sn, yani ~0,62 MB/sn. 12 dk ≈ **~450 MB** [H]. Bu, GitHub'ın dosya başına 100 MB sınırını aşar (bkz. bölüm 6).

## 2. Bir uzun video: adım süreleri (duvar saati, [T] aksi belirtilmedikçe)
Varsayımlar: 12 dk video, ~150–200 sahne görseli, 1 RED turu. Kritik yol **kalın** yazılmıştır.

| Faz | Adım (sahip) | İyi durum | Kötü durum | Not |
|---|---|---|---|---|
| F0 | **Ortam kurulumu** (uretim-muhendisi) | 15 dk | 40 dk | Konteyner her oturumda sıfırlanıyor: Rhubarb derleme, npm, Kokoro/Whisper modelleri |
| F1 | **Konu havuzu** ‖ rakip özeti | 20 dk | 40 dk | Paralel |
| F2 | **10 senaryo → viralite ‖ ön doğrulama → hakem** | 50 dk | 100 dk | |
| F3 | **Tam metin → doğrulama** (+1 RED) | 60 dk | 150 dk | Rakam doğrulama ağ hızına bağlı |
| F4 | Ses: TTS + son işlem + Whisper | 30 dk | 75 dk | Kokoro ve Whisper bu konteynerde kurulu değil, hızları ölçülmedi |
| F4 | **Görsel: prompt + Canva üretimi + kesme + kontakt** | 60 dk | 120 dk | Canva bağlayıcısı (ek ücret yok); çağrıları koordinatör yapar. Hız, aylık AI hakkı ve tam çözünürlük indirme ölçülmedi |
| F4 | Müzik adayları ‖ paket taslağı | 30 dk | 60 dk | Kritik yolda değil |
| F5 | **Animasyon: Rhubarb + 10–20 sn test + tüm sahneler** | 150 dk | 270 dk | **1 numaralı darboğaz.** Yeniden kullanılabilir sahne kütüphanesi yok (yalnız pilot) |
| F6 | Müzik miksi | 30 dk | 60 dk | F5 ile paralel |
| F7 | **Kurgu + render 16:9 (~66 dk [H]) + 2 Shorts (~11 dk [H])** | 120 dk | 210 dk | RED sonrası yeniden render +66 dk |
| F8 | **Thumbnail ‖ paket ‖ son viralite** | 30 dk | 60 dk | |
| F9 | **Hakem son kontrol** (kendi ölçümü) | 30 dk | 60 dk | |
| F10 | **Teslim paketi + YAYIN.md** | 15 dk | 15 dk | |
| | **Kritik yol toplamı** [H, tahminlerden] | **~9 saat** | **~18 saat** | |

Niyazi'nin süresi [H]: video başına izleme (~12 dk) + karar (~5–10 dk), yani haftada 2 videoda ~35–45 dk. Senaryo onayı kalktığı için Niyazi akışın ortasında beklenmez. Tek insan beklemesi sondaki onaydır ve stok bu beklemeyi tamponlar.

## 3. Darboğazlar (işin nerede beklediği)
1. **Animasyon sahne kodlaması (F5)**, aktif iş süresi olarak en uzun adım. Her video 150–200 çekimi Remotion'da kodlamak demek. Çözüm: uretim-muhendisi ile animasyon-yonetmeni `video/src/ortak/` altında 10–15 parametrik sahne şablonu kurar: konuşan karakter, sayı sayacı, çizgi/bar grafik, harita, zaman çizelgesi, belge/mühür, karşılaştırma, alıntı kartı, kamera hareketli illüstrasyon. Hedef: F5 ≤ 2 saat [T]. Şablonlar YouTube'un "şablon içerik" riskini artırmamalı. Bu yüzden yapı ve açılış her videoda farklı kalır, şablonlar yalnız teknik yapı taşı olur.
2. **Render (F7)**, CPU'ya bağlı. 66 dk [H], her RED sonrası tekrar ediyor. Çözüm: bölüm bölüm render + birleştirme (yalnız değişen bölüm yeniden render edilir) ve `--concurrency` ayarı. Bunlar uretim-muhendisi'ne verilir.
3. **Görsel üretim (F4)**, dış bağımlılık. Görseller Canva bağlayıcısıyla üretilir (Niyazi'nin aboneliği, ek ücret yok; Gemini API kullanılmıyor). Açık riskler: (a) aylık Canva AI hakkının video başına 120–200 görsele, yani haftada 2 videoda ayda ~1.040–1.730 görsele [H: 2 × 120–200 × 4,33] yetip yetmediği ölçülmedi (v1'de 3/hafta için ~1.560–2.600 idi); (b) bağlayıcı yalnız 199x112 önizleme döndürüyor, tam çözünürlüklü dosyayı otomatik çekme yolu yok (uretim-muhendisi'nin işi); (c) Canva çağrıları alt ajanlarda erişilebilir olmayabilir, koordinatör yapar. Bunlar çözülmezse yalnız B planı (grafik ağırlıklı) yapılabilir. Test: `uretim/canva-testi/rapor.md`.
4. **Niyazi onayı (F10→F11)**, insan beklemesi. Stok kuralı (`docs/yayin-takvimi.md`) ve planlı yayın (private + publishAt) bu beklemeyi yayın saatinden ayırır.
5. **Oturum ve bağlam sınırı**, bilinmiyor. 9–18 saatlik akış tek oturuma sığmayabilir. Çözüm: `durum.md` kontrol noktası ve her fazdan sonra commit. Akış ilk geçmemiş adımdan devam eder.

## 4. Üretim planı adayları (2–3 aday → kıyas)
| | P1 · Tam rig + illüstrasyon + az image-to-video | **P2 · İllüstrasyon + kamera ağırlıklı (önerilen varsayılan)** | P3 · Grafik ağırlıklı (0 ₺) |
|---|---|---|---|
| Konuşan karakter | Sürenin ~%25'i | Açılış, dönüş anı, kapanış (~%10–15) | Köşe karakteri + kısa konuşmalar |
| Görsel | 150–200 illüstrasyon + 3–6 image-to-video | 120–180 illüstrasyon, kamera hareketi | Kodla çizilen grafik/harita/sayaç, az illüstrasyon |
| F5 süresi [T] | 4–6 saat | 2–3 saat | 2–3 saat |
| Ek para | $0 görsel (Canva aboneliği) + image-to-video (fiyat bilinmiyor, onay gerekir) | $0 (Canva aboneliği) | $0 |
| Risk | En yavaş plan; image-to-video kör testi yapılmadı | Karakter bağı daha zayıf | Referans stilin (detaylı illüstrasyon) altında kalır; hakem RED riski |
| Kalite kapısı sayısı | 17 (dudak senkronu + image-to-video kör testi dahil) | 16 | 15 |
| Haftada 2'ye uygunluk | En fazla 2 haftada 1 (vitrin videosu, Pazar A/C) | **Haftada 2** | Yalnız yedek / gecikme planı |

Seçim: **P2 varsayılan, P1 en fazla 2 haftada 1 vitrin videosu (Pazar), P3 yalnız B planı.** P1 varsayılan olarak elendi, çünkü kritik yolu ~2–3 saat uzatıyor ve Pazartesi tetikli B videosunun payını yiyor [T]. 2 + 4 temposunda Pazar videosu Perşembe tetiklendiği için P1'e yer açılabilir. P3 ise kanalın görsel kimliğinin (`docs/referans-analizi.md`) altında kaldığı için varsayılan olamaz.
**Kritik yol testi (henüz YAPILMADI):** Canva ile 10+ görsellik karakter tutarlılığı testi geçince ve tam çözünürlüklü indirme yolu çözülünce P2 ile 60 sn'lik uçtan uca dilim üretilir. F5 ve F7 süreleri ölçülür, kapılar uygulanır. Bu test geçmeden haftada 2 taahhüt edilmez; takvim yalnız hafta 0'dan (stok üretimi) başlar.

## 5. Sonuç: haftada 2 uzun + 4 Shorts mümkün mü?
- **Şart bağımlılıklar kapanırsa evet, tamponlu [H/T].** İyi durumda 2 × ~9 saat ≈ **18 saat/hafta**, kötü durumda 2 × ~18 saat ≈ **36 saat/hafta** otomatik üretim. Kötü durum bile tek bir videoyu ~2,5 günlük pencereye (Pazartesi tetik → Çarşamba slot; Perşembe tetik → Pazar slot) sığdırır. 3/hafta'da kötü durum ~54 saat/hafta idi ve iki üretim üst üste biniyordu; 2/hafta'da üretimler çakışmaz.
- **Boşta kalan kapasite işe dönüşür [T]:** haftada ~1–2 günlük boşluk (Cuma–Cumartesi) stok A/C üretimine, sahne şablon kütüphanesine (darboğaz 1) ve RED turlarına gider. Kalite kapısı sıkılaşınca tempo değil tampon erir.
- Shorts ek yükü küçüktür: video başına ~30–45 dk [T]. Kesitler aynı sahnelerden çıkar, render ~11 dk [H] sürer. 4 Shorts ana kısıt değildir.
- **Bugün hâlâ mümkün değil.** Aşağıdaki şart bağımlılıklar eksik (bölüm 6). Canva'dan tam çözünürlüklü görsel alınamadıkça ve karakter görselleri olmadan yalnız P3 yapılabilir.
- **Geçiş:** hafta 0 = 1 stok video + 2 stok Shorts; hafta 1 = 1 uzun + 2 Shorts; hafta 2'den itibaren 2 + 4 (`docs/yayin-takvimi.md` §6). İlk 3 videoda her adımın ölçülen süresi bu dosyaya işlenir (v2). Kritik yol >18 saat ölçülürse ya da 4 haftada 2 slot kaçarsa tempo geçici olarak 1 + 2'ye iner.
- **Haftada 3'e dönüş ön koşulları** (yalnız Niyazi kararıyla): sahne kütüphanesi tamam, kritik yol ≤ 9 saat ölçülmüş, son 8 videonun politika raporu YEŞİL.
- Politika riski [AÖ, plan v1]: YouTube'un 2026-07 "inauthentic content" netleştirmesi seri/şablon üretimi ve finansta tavsiye veren yapay zekâ personalarını hedef alıyor. 2/hafta, 3/hafta'ya göre seri üretim görünümünü azaltır ama riski kaldırmaz [T]. Önlemler değişmedi: her videoda özgün araştırma ve kaynak listesi, değişen yapı ve açılış, tavsiye dili yok, karakter uzman gibi sunulmaz, TTS kullanımı açıklamada belirtilir. finans-dogrulayici ve monetizasyon-uyum-uzmani bu kontrolleri her videoda yapar.

## 6. Dış bağımlılıklar (şart olanlar)
| # | Bağımlılık | Kimden | Durum (2026-10-26) | Yoksa |
|---|---|---|---|---|
| 1 | **Görsel üretim: Canva bağlayıcısı** (`generate-image`, referans = karakter sayfası; Niyazi'nin Canva aboneliği, ek ücret yok — Niyazi kararı 2026-10-26; Gemini API kullanılmıyor) | Niyazi (bağlı hesap) + koordinatör (çağrılar) + gorsel-varlik-sanatcisi (prompt, değerlendirme) + uretim-muhendisi (tam çözünürlük indirme) | 2 görsellik test geçti, karakter tanınır (`uretim/canva-testi/rapor.md`). Açık: tam çözünürlüklü indirme yolu yok (yalnız 199x112 önizleme); aylık AI hakkının haftada 2 videoya (~1.040–1.730 görsel/ay [H]) yetip yetmediği ölçülmedi; 10+ görselde tutarlılık ölçülmedi | Yalnız P3 |
| 2 | **Karakter görselleri E0–E14** (`assets/karakter/2d-duzenleme-promptlari.md`) | Canva bağlayıcısı (koordinatör çağırır, prompt'lar gorsel-varlik-sanatcisi) veya Niyazi elle | Yok; elde yalnız düşük çözünürlüklü sayfalar var | Konuşan planlar yumuşak, kollar sabit; yakın plan kullanılamaz |
| 3 | **TTS anlatıcı sesi onayı** (Kokoro-82M, Apache-2.0) | ses-yonetmeni testi → Niyazi bir kez dinleyip onaylar | Aday tablosu, WER ve kör dinleme testi tamamlanmadı; Kokoro bu konteynerde kurulu değil | Her videoda Niyazi okur (+40–60 dk/video, akış otomatik olmaz) |
| 4 | **YouTube yükleme: OAuth (cihaz akışı) + gerekirse API denetimi** | Niyazi (`docs/yayin-kurulumu.md` adımları, ~10 dk, bir kez) + uretim-muhendisi (`tools/yayin/yukle.py`) | Araç yazıldı; OAuth ortam değişkenleri henüz yok. Denetim kilidi **belirsiz**: 2020 duyurusu, denetlenmemiş projelerin yüklemelerini private'a kilitliyor; `videos.insert` sayfasının güncel hâli kilit olmadığını yazıyor (uretim-muhendisi'nin 2026-10-26 okuması). Önce tek test yüklemesi yapılır (Niyazi onayıyla). Kota: varsayılan günde 100 `videos.insert` [AÖ/uretim-muhendisi]; haftada 6 yükleme (2 uzun + 4 Shorts) rahat sığar. Cihaz akışı altyazı yükleyemez; SRT Studio'dan elle eklenir | `--manuel-paket` ile Studio'dan elle yükleme (video başına ~5–10 dk Niyazi) |
| 5 | **Depolama** (12 dk video ≈ 450 MB [H], haftada ~0,9 GB uzun video + Shorts) | Niyazi kararı | **Öneri (Niyazi onayı bekliyor):** final video ve Shorts teslimde Niyazi'ye dosya olarak gönderilir; onaydan sonra YouTube'a yüklenen video arşiv sayılır; `uretim/` altında git'e yalnız küçük önizleme (`*onizleme*.mp4`) + metadata girer. `.gitignore`'a `uretim/**/final/*.mp4`, `uretim/**/teslim/*.mp4`, `uretim/**/08-kurgu/*.mp4` eklendi (önizleme hariç). Ayrıntı: `.claude/commands/bugunun-videosu.md` bölüm 3 | Teslim dosyası oturum sonunda kaybolur. Diğer seçenekler: Git LFS (kota ve fiyatı doğrulanmadı), Google Drive |
| 6 | Image-to-video (yalnız P1) | Niyazi bütçe onayı | Model ve fiyat seçilmedi, kör test yapılmadı | P1 yerine P2 |
| 7 | `YOUTUBE_API_KEY` (salt okuma) | — | Ortamda **var** | — |

## Onaylı bütçe
| Kalem | Tavan | Onay tarihi |
|---|---|---|
| Görsel üretim: Canva bağlayıcısı | Ek ücret yok (Niyazi'nin mevcut aboneliği, aylık AI hakkı içinde) | 2026-10-26 (Niyazi kararı) |
| Ücretli görsel API (Gemini vb.) | Kullanılmıyor (onay yok) | — |
| Image-to-video | — (onay yok) | — |
Tavan boşken `/bugunun-videosu` ek para harcayan hiçbir adımı çalıştırmaz. Canva aboneliği içindeki üretim ek harcama sayılmaz; kullanılan üretim sayısı `durum.md`'ye yazılır.

Kaynaklar: [YouTube Data API — Videos: insert](https://developers.google.com/youtube/v3/docs/videos/insert) · [Ayrshare: unverified app / audit](https://www.ayrshare.com/solutions/google-api-error-403-unverified-app-how-to-fix-the-audit-pipeline/) · [Ayrshare: 10k quota](https://www.ayrshare.com/solutions/how-to-bypass-the-youtube-10k-unit-limit-fixing-the-403-quota-exceeded-error.md) · [Rapid Developers: upload automation](https://www.rapidevelopers.com/md/api-automations/how-to-automate-youtube-video-uploads-using-the-api) · Canva görsel testi: `uretim/canva-testi/rapor.md` · politika: `docs/plan.html` kaynakları.
