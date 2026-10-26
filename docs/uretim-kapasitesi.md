# Üretim kapasitesi ve darboğaz analizi (v1, 2026-10-26)

Soru: Haftada 3 uzun video (≥10 dk, İngilizce) + 6 Shorts, `/bugunun-videosu` akışıyla yapılabilir mi?
Etiketler: **[Ö]** bu ortamda ölçüldü, **[H]** ölçüm veya bilinen değerden hesap, **[AÖ]** arama özeti, **[T]** tahmin.
Henüz hiçbir tam video üretilmedi. Süreler pilot klip (18,8 sn) ve ajanların iş tanımlarından çıkarılmış tahminlerdir. İlk 3 videoda her adımın gerçek başlangıç ve bitiş saati `durum.md`'ye yazılır, bu dosya o verilerle v2'ye güncellenir.

## 1. Ölçülen tek veri: render hızı [Ö]
- Ortam: 4 vCPU, 15 GB RAM, Remotion 4.0.539, `tools/render-son.sh` (h264 crf18 + 2 geçişli loudnorm).
- `Pilot` (18,8 sn, 564 kare, 1080p30): toplam **110,7 sn**. Sabit yük (bundle + tarayıcı, 2 kare) 6,6 sn, kalan ~104 sn. Yani ~5,4 kare/sn, **gerçek sürenin ~5,5 katı**.
- 12 dk video (21.600 kare) için **~66 dk** [H]. 2 Shorts (2×60 sn) için ~11 dk [H]. Gerçek videonun büyük bitmap'leri ve kamera hareketleri render'ı yavaşlatabilir [T]. Remotion `--concurrency` ayarı denenmedi (uretim-muhendisi'nin işi).
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
| F4 | **Görsel: prompt + üretim + kesme + kontakt** | 60 dk | 120 dk | Görsel API ve bütçe onayı şart |
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
3. **Görsel üretim (F4)**, dış bağımlılık ve bütçe. API yoksa video başına 150–200 görsel üretilemez. O durumda yalnız B planı (grafik ağırlıklı) yapılabilir.
4. **Niyazi onayı (F10→F11)**, insan beklemesi. Stok kuralı (`docs/yayin-takvimi.md`) ve planlı yayın (private + publishAt) bu beklemeyi yayın saatinden ayırır.
5. **Oturum ve bağlam sınırı**, bilinmiyor. 9–18 saatlik akış tek oturuma sığmayabilir. Çözüm: `durum.md` kontrol noktası ve her fazdan sonra commit. Akış ilk geçmemiş adımdan devam eder.

## 4. Üretim planı adayları (2–3 aday → kıyas)
| | P1 · Tam rig + illüstrasyon + az image-to-video | **P2 · İllüstrasyon + kamera ağırlıklı (önerilen varsayılan)** | P3 · Grafik ağırlıklı (0 ₺) |
|---|---|---|---|
| Konuşan karakter | Sürenin ~%25'i | Açılış, dönüş anı, kapanış (~%10–15) | Köşe karakteri + kısa konuşmalar |
| Görsel | 150–200 illüstrasyon + 3–6 image-to-video | 120–180 illüstrasyon, kamera hareketi | Kodla çizilen grafik/harita/sayaç, az illüstrasyon |
| F5 süresi [T] | 4–6 saat | 2–3 saat | 2–3 saat |
| Para [H, plan v1 fiyatı, doğrulanmadı] | ~$8–20 + image-to-video (fiyat bilinmiyor) | ~$6–18 | $0 |
| Risk | Haftada 3 için en yavaş plan; image-to-video kör testi yapılmadı | Karakter bağı daha zayıf | Referans stilin (detaylı illüstrasyon) altında kalır; hakem RED riski |
| Kalite kapısı sayısı | 17 (dudak senkronu + image-to-video kör testi dahil) | 16 | 15 |
| Haftada 3'e uygunluk | Haftada 1 (vitrin videosu, Pazar A) | **Haftada 2–3** | Yalnız yedek / gecikme planı |

Seçim: **P2 varsayılan, P1 haftada en fazla 1 vitrin videosu, P3 yalnız B planı.** P1, haftada 3 için kritik yolu ~2–3 saat uzattığı için elendi [T]. P3 ise kanalın görsel kimliğinin (`docs/referans-analizi.md`) altında kaldığı için varsayılan olamaz.
**Kritik yol testi (henüz YAPILMADI):** E0–E14 ve görsel API onayı gelince P2 ile 60 sn'lik uçtan uca dilim üretilir. F5 ve F7 süreleri ölçülür, kapılar uygulanır. Bu test geçmeden haftada 3 taahhüt edilmez.

## 5. Sonuç: haftada 3 uzun + 6 Shorts mümkün mü?
- **Şartlar sağlanırsa sınırda mümkün [H/T].** İyi durumda 3 × ~9 saat ≈ 27 saat/hafta otomatik üretim yeterli. Kötü durumda 3 × ~18 saat ≈ 54 saat/hafta. Bu da oturumların neredeyse kesintisiz çalışmasını ve her hafta en az bir videonun gecikmesini (stok devreye girer) gerektirir.
- Shorts ek yükü küçüktür: video başına ~30–45 dk [T]. Kesitler aynı sahnelerden çıkar, render ~11 dk [H] sürer. Bu yüzden 6 Shorts ana kısıt değildir.
- **Bugün mümkün değil.** Aşağıdaki şart bağımlılıklar eksik. Görsel API ve karakter görselleri olmadan yalnız P3 yapılabilir.
- **Öneri (geçiş):** 1. hafta 1 uzun + 2 Shorts + 1 stok video, 2. hafta 2 + 4, 3. hafta 3 + 6. Her adımın ölçülen süresi bu dosyaya işlenir. 3. haftada kritik yol >12 saat ise tempo haftada 2'de tutulur ve sahne kütüphanesi tamamlanınca yeniden denenir.
- Politika riski [AÖ, plan v1]: YouTube'un 2026-07 "inauthentic content" netleştirmesi seri/şablon üretimi ve finansta tavsiye veren yapay zekâ personalarını hedef alıyor. **Haftada 3 + TTS anlatıcı bu riski artırır.** Önlemler: her videoda özgün araştırma ve kaynak listesi, değişen yapı ve açılış, tavsiye dili yok, karakter uzman gibi sunulmaz, TTS kullanımı açıklamada belirtilir (paketleyici kararı). finans-dogrulayici bu kontrolleri her videoda yapar.

## 6. Dış bağımlılıklar (şart olanlar)
| # | Bağımlılık | Kimden | Durum (2026-10-26) | Yoksa |
|---|---|---|---|---|
| 1 | **Görsel üretim API'si + bütçe onayı** (Gemini görsel modeli; anahtar ortam değişkeninde) | Niyazi | Anahtar ortamda yok (`GEMINI_API_KEY`/`GOOGLE_API_KEY` tanımsız). Bütçe onayı yok. Plan v1 tahmini video başına ~$8–20 [AÖ fiyat, doğrulanmadı] → haftada 3 ≈ ayda ~13 video ≈ **~$105–260/ay** [H] | Yalnız P3 |
| 2 | **Karakter görselleri E0–E14** (`assets/karakter/2d-duzenleme-promptlari.md`) | Niyazi (Gemini uygulamasında) | Yok; elde yalnız düşük çözünürlüklü sayfalar var | Konuşan planlar yumuşak, kollar sabit; yakın plan kullanılamaz |
| 3 | **TTS anlatıcı sesi onayı** (Kokoro-82M, Apache-2.0) | ses-yonetmeni testi → Niyazi bir kez dinleyip onaylar | Aday tablosu, WER ve kör dinleme testi tamamlanmadı; Kokoro bu konteynerde kurulu değil | Her videoda Niyazi okur (+40–60 dk/video, akış otomatik olmaz) |
| 4 | **YouTube yükleme: OAuth (cihaz akışı) + gerekirse API denetimi** | Niyazi (`docs/yayin-kurulumu.md` adımları, ~10 dk, bir kez) + uretim-muhendisi (`tools/yayin/yukle.py`) | Araç yazıldı; OAuth ortam değişkenleri henüz yok. Denetim kilidi **belirsiz**: 2020 duyurusu, denetlenmemiş projelerin yüklemelerini private'a kilitliyor; `videos.insert` sayfasının güncel hâli kilit olmadığını yazıyor (uretim-muhendisi'nin 2026-10-26 okuması). Önce tek test yüklemesi yapılır (Niyazi onayıyla). Kota: varsayılan günde 100 `videos.insert` [AÖ/uretim-muhendisi]; haftada 9 yükleme rahat sığar. Cihaz akışı altyazı yükleyemez; SRT Studio'dan elle eklenir | `--manuel-paket` ile Studio'dan elle yükleme (video başına ~5–10 dk Niyazi) |
| 5 | **Depolama** (12 dk video ≈ 450 MB [H], haftada ~1,5 GB) | Niyazi kararı | Yok. Git'e 100 MB'ı aşan dosya girmez; konteyner silinir | Teslim dosyası oturum sonunda kaybolur. Seçenekler: Git LFS (kota ve fiyatı doğrulanmadı), Google Drive, ya da teslimde "private YouTube yüklemesi" (Niyazi'nin ön onayı gerekir) |
| 6 | Image-to-video (yalnız P1) | Niyazi bütçe onayı | Model ve fiyat seçilmedi, kör test yapılmadı | P1 yerine P2 |
| 7 | `YOUTUBE_API_KEY` (salt okuma) | — | Ortamda **var** | — |

## Onaylı bütçe
| Kalem | Tavan | Onay tarihi |
|---|---|---|
| Görsel API | — (onay yok) | — |
| Image-to-video | — (onay yok) | — |
Tavan boşken `/bugunun-videosu` para harcayan hiçbir adımı çalıştırmaz.

Kaynaklar: [YouTube Data API — Videos: insert](https://developers.google.com/youtube/v3/docs/videos/insert) · [Ayrshare: unverified app / audit](https://www.ayrshare.com/solutions/google-api-error-403-unverified-app-how-to-fix-the-audit-pipeline/) · [Ayrshare: 10k quota](https://www.ayrshare.com/solutions/how-to-bypass-the-youtube-10k-unit-limit-fixing-the-403-quota-exceeded-error.md) · [Rapid Developers: upload automation](https://www.rapidevelopers.com/md/api-automations/how-to-automate-youtube-video-uploads-using-the-api) · görsel fiyatları ve politika: `docs/plan.html` kaynakları.
