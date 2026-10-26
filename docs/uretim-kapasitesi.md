# Üretim kapasitesi ve darboğaz analizi (v1.1, 2026-10-26 — Canva, TTS ve depolama kararlarıyla hizalandı)

Soru: Haftada 3 uzun video (≥10 dk, İngilizce) + 6 Shorts, `/bugunun-videosu` akışıyla yapılabilir mi?
Etiketler: **[Ö]** bu ortamda ölçüldü, **[H]** ölçüm veya bilinen değerden hesap, **[AÖ]** arama özeti, **[T]** tahmin.
Henüz hiçbir tam video üretilmedi. Süreler pilot klip (18,8 sn) ve ajanların iş tanımlarından çıkarılmış tahminlerdir. İlk 3 videoda her adımın gerçek başlangıç ve bitiş saati `durum.md`'ye yazılır, bu dosya o verilerle v2'ye güncellenir.

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

Niyazi'nin süresi [H]: video başına izleme (~12 dk) + karar (~5–10 dk), yani haftada ~1–1,5 saat. Senaryo onayı kalktığı için Niyazi akışın ortasında beklenmez. Tek insan beklemesi sondaki onaydır ve stok bu beklemeyi tamponlar.

## 3. Darboğazlar (işin nerede beklediği)
1. **Animasyon sahne kodlaması (F5)**, aktif iş süresi olarak en uzun adım. Her video 150–200 çekimi Remotion'da kodlamak demek. Çözüm: uretim-muhendisi ile animasyon-yonetmeni `video/src/ortak/` altında 10–15 parametrik sahne şablonu kurar: konuşan karakter, sayı sayacı, çizgi/bar grafik, harita, zaman çizelgesi, belge/mühür, karşılaştırma, alıntı kartı, kamera hareketli illüstrasyon. Hedef: F5 ≤ 2 saat [T]. Şablonlar YouTube'un "şablon içerik" riskini artırmamalı. Bu yüzden yapı ve açılış her videoda farklı kalır, şablonlar yalnız teknik yapı taşı olur.
2. **Render (F7)**, CPU'ya bağlı. 66 dk [H], her RED sonrası tekrar ediyor. Çözüm: bölüm bölüm render + birleştirme (yalnız değişen bölüm yeniden render edilir) ve `--concurrency` ayarı. Bunlar uretim-muhendisi'ne verilir.
3. **Görsel üretim (F4)**, dış bağımlılık. Görseller Canva bağlayıcısıyla üretilir (Niyazi'nin aboneliği, ek ücret yok; Gemini API kullanılmıyor). Açık riskler: (a) aylık Canva AI hakkının video başına 120–200 görsele ve haftada 3 videoya yetip yetmediği ölçülmedi; (b) bağlayıcı yalnız 199x112 önizleme döndürüyor, tam çözünürlüklü dosyayı otomatik çekme yolu yok (uretim-muhendisi'nin işi); (c) Canva çağrıları alt ajanlarda erişilebilir olmayabilir, koordinatör yapar. Bunlar çözülmezse yalnız B planı (grafik ağırlıklı) yapılabilir. Test: `uretim/canva-testi/rapor.md`.
4. **Niyazi onayı (F10→F11)**, insan beklemesi. Stok kuralı (`docs/yayin-takvimi.md`) ve planlı yayın (private + publishAt) bu beklemeyi yayın saatinden ayırır.
5. **Oturum ve bağlam sınırı**, bilinmiyor. 9–18 saatlik akış tek oturuma sığmayabilir. Çözüm: `durum.md` kontrol noktası ve her fazdan sonra commit. Akış ilk geçmemiş adımdan devam eder.

## 4. Üretim planı adayları (2–3 aday → kıyas)
| | P1 · Tam rig + illüstrasyon + az image-to-video | **P2 · İllüstrasyon + kamera ağırlıklı (önerilen varsayılan)** | P3 · Grafik ağırlıklı (0 ₺) |
|---|---|---|---|
| Konuşan karakter | Sürenin ~%25'i | Açılış, dönüş anı, kapanış (~%10–15) | Köşe karakteri + kısa konuşmalar |
| Görsel | 150–200 illüstrasyon + 3–6 image-to-video | 120–180 illüstrasyon, kamera hareketi | Kodla çizilen grafik/harita/sayaç, az illüstrasyon |
| F5 süresi [T] | 4–6 saat | 2–3 saat | 2–3 saat |
| Ek para | $0 görsel (Canva aboneliği) + image-to-video (fiyat bilinmiyor, onay gerekir) | $0 (Canva aboneliği) | $0 |
| Risk | Haftada 3 için en yavaş plan; image-to-video kör testi yapılmadı | Karakter bağı daha zayıf | Referans stilin (detaylı illüstrasyon) altında kalır; hakem RED riski |
| Kalite kapısı sayısı | 17 (dudak senkronu + image-to-video kör testi dahil) | 16 | 15 |
| Haftada 3'e uygunluk | Haftada 1 (vitrin videosu, Pazar A) | **Haftada 2–3** | Yalnız yedek / gecikme planı |

Seçim: **P2 varsayılan, P1 haftada en fazla 1 vitrin videosu, P3 yalnız B planı.** P1, haftada 3 için kritik yolu ~2–3 saat uzattığı için elendi [T]. P3 ise kanalın görsel kimliğinin (`docs/referans-analizi.md`) altında kaldığı için varsayılan olamaz.
**Kritik yol testi (henüz YAPILMADI):** Canva ile 10+ görsellik karakter tutarlılığı testi geçince ve tam çözünürlüklü indirme yolu çözülünce P2 ile 60 sn'lik uçtan uca dilim üretilir. F5 ve F7 süreleri ölçülür, kapılar uygulanır. Bu test geçmeden haftada 3 taahhüt edilmez.

## 5. Sonuç: haftada 3 uzun + 6 Shorts mümkün mü?
- **Şartlar sağlanırsa sınırda mümkün [H/T].** İyi durumda 3 × ~9 saat ≈ 27 saat/hafta otomatik üretim yeterli. Kötü durumda 3 × ~18 saat ≈ 54 saat/hafta. Bu da oturumların neredeyse kesintisiz çalışmasını ve her hafta en az bir videonun gecikmesini (stok devreye girer) gerektirir.
- Shorts ek yükü küçüktür: video başına ~30–45 dk [T]. Kesitler aynı sahnelerden çıkar, render ~11 dk [H] sürer. Bu yüzden 6 Shorts ana kısıt değildir.
- **Bugün mümkün değil.** Aşağıdaki şart bağımlılıklar eksik. Canva'dan tam çözünürlüklü görsel alınamadıkça ve karakter görselleri olmadan yalnız P3 yapılabilir.
- **Öneri (geçiş):** 1. hafta 1 uzun + 2 Shorts + 1 stok video, 2. hafta 2 + 4, 3. hafta 3 + 6. Her adımın ölçülen süresi bu dosyaya işlenir. 3. haftada kritik yol >12 saat ise tempo haftada 2'de tutulur ve sahne kütüphanesi tamamlanınca yeniden denenir.
- Politika riski [AÖ, plan v1]: YouTube'un 2026-07 "inauthentic content" netleştirmesi seri/şablon üretimi ve finansta tavsiye veren yapay zekâ personalarını hedef alıyor. **Haftada 3 + TTS anlatıcı bu riski artırır.** Önlemler: her videoda özgün araştırma ve kaynak listesi, değişen yapı ve açılış, tavsiye dili yok, karakter uzman gibi sunulmaz, TTS kullanımı açıklamada belirtilir (youtube-paketleyici kararı). finans-dogrulayici bu kontrolleri her videoda yapar.

## 6. Dış bağımlılıklar (şart olanlar)
| # | Bağımlılık | Kimden | Durum (2026-10-26) | Yoksa |
|---|---|---|---|---|
| 1 | **Görsel üretim: Canva bağlayıcısı** (`generate-image`, referans = karakter sayfası; Niyazi'nin Canva aboneliği, ek ücret yok — Niyazi kararı 2026-10-26; Gemini API kullanılmıyor) | Niyazi (bağlı hesap) + koordinatör (çağrılar) + gorsel-varlik-sanatcisi (prompt, değerlendirme) + uretim-muhendisi (tam çözünürlük indirme) | 2 görsellik test geçti, karakter tanınır (`uretim/canva-testi/rapor.md`). Açık: tam çözünürlüklü indirme yolu yok (yalnız 199x112 önizleme); aylık AI hakkının haftada 3 videoya yetip yetmediği ölçülmedi; 10+ görselde tutarlılık ölçülmedi | Yalnız P3 |
| 2 | **Karakter görselleri E0–E14** (`assets/karakter/2d-duzenleme-promptlari.md`) | Canva bağlayıcısı (koordinatör çağırır, prompt'lar gorsel-varlik-sanatcisi) veya Niyazi elle | Yok; elde yalnız düşük çözünürlüklü sayfalar var | Konuşan planlar yumuşak, kollar sabit; yakın plan kullanılamaz |
| 3 | **TTS anlatıcı sesi onayı** (Kokoro-82M, Apache-2.0) | ses-yonetmeni testi → Niyazi bir kez dinleyip onaylar | Aday tablosu, WER ve kör dinleme testi tamamlanmadı; Kokoro bu konteynerde kurulu değil | Her videoda Niyazi okur (+40–60 dk/video, akış otomatik olmaz) |
| 4 | **YouTube yükleme: OAuth (cihaz akışı) + gerekirse API denetimi** | Niyazi (`docs/yayin-kurulumu.md` adımları, ~10 dk, bir kez) + uretim-muhendisi (`tools/yayin/yukle.py`) | Araç yazıldı; OAuth ortam değişkenleri henüz yok. Denetim kilidi **belirsiz**: 2020 duyurusu, denetlenmemiş projelerin yüklemelerini private'a kilitliyor; `videos.insert` sayfasının güncel hâli kilit olmadığını yazıyor (uretim-muhendisi'nin 2026-10-26 okuması). Önce tek test yüklemesi yapılır (Niyazi onayıyla). Kota: varsayılan günde 100 `videos.insert` [AÖ/uretim-muhendisi]; haftada 9 yükleme rahat sığar. Cihaz akışı altyazı yükleyemez; SRT Studio'dan elle eklenir | `--manuel-paket` ile Studio'dan elle yükleme (video başına ~5–10 dk Niyazi) |
| 5 | **Depolama** (12 dk video ≈ 450 MB [H], haftada ~1,5 GB) | Niyazi kararı | **Öneri (Niyazi onayı bekliyor):** final video ve Shorts teslimde Niyazi'ye dosya olarak gönderilir; onaydan sonra YouTube'a yüklenen video arşiv sayılır; `uretim/` altında git'e yalnız küçük önizleme (`*onizleme*.mp4`) + metadata girer. `.gitignore`'a `uretim/**/final/*.mp4`, `uretim/**/teslim/*.mp4`, `uretim/**/08-kurgu/*.mp4` eklendi (önizleme hariç). Ayrıntı: `.claude/commands/bugunun-videosu.md` bölüm 3 | Teslim dosyası oturum sonunda kaybolur. Diğer seçenekler: Git LFS (kota ve fiyatı doğrulanmadı), Google Drive |
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
