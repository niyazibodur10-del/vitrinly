# Yayın takvimi — Financial Rise (v1, 2026-10-26)

Hedef: haftada **3 uzun video** (≥10 dk) + **6 Shorts** (her uzun videodan 2). Üretim `/bugunun-videosu` ile yapılır.
Etiketler: **[AÖ]** arama özeti (üçüncü taraf blog/araştırma), **[T]** tahmin, **[H]** hesap. Burada ölçülmüş kendi verimiz yok. İlk 4 haftadan sonra YouTube Studio verisiyle yeniden ayarlanır.

## 1. Haftalık takvim (öneri, [T])
| Gün | Uzun video | Shorts | Sütun |
|---|---|---|---|
| Pazartesi | — | 09:00 ET: Pazar videosunun Shorts-1 | — |
| **Salı** | **12:00 ET** | 09:00 ET: Pazar videosunun Shorts-2 | **B · Bugün** (Money News, Explained) |
| Çarşamba | — | 09:00 ET: Salı videosunun Shorts-1 | — |
| Perşembe | — | 09:00 ET: Salı videosunun Shorts-2 | — |
| **Cuma** | **12:00 ET** | — | **C · Gelecek** (What If…) |
| Cumartesi | — | 09:00 ET: Cuma videosunun Shorts-1 | — |
| **Pazar** | **12:00 ET** | 09:00 ET: Cuma videosunun Shorts-2 | **A · Geçmiş** (The Collapse) |

Toplam: 3 uzun + 6 Shorts. Her Shorts, kendi uzun videosu yayınlandıktan 1–2 gün sonra çıkar ve "ilgili video" bağlantısıyla o videoya yönlendirir.

### Saatlerin diğer bölgelerdeki karşılığı
Saat ET (New York) yerel saatine sabitlenir. Yaz saati geçişlerinde UTC karşılığı değişir.
| Slot | ET | Londra | Hindistan (IST) | Türkiye (TRT) |
|---|---|---|---|---|
| Uzun, kış (EST, UTC−5) | 12:00 | 17:00 | 22:30 | 20:00 |
| Uzun, yaz (EDT, UTC−4) | 12:00 | 17:00 | 21:30 | 19:00 |
| Shorts, kış | 09:00 | 14:00 | 19:30 | 17:00 |
| Shorts, yaz | 09:00 | 14:00 | 18:30 | 16:00 |
Not: ABD ile İngiltere yaz saatine farklı tarihlerde geçer. Mart ve Ekim–Kasım'daki 1–3 haftalık aralıkta Londra karşılığı 1 saat kayar.

### Gerekçe
- **Saat [AÖ]:** Üçüncü taraf çalışmalar uzun video için en güçlü pencereyi öğleden sonra ile akşamüstü arasında veriyor. Kaynakların aralıkları birbirini tutmuyor: 14:00–16:00, 15:00–18:00 ve 20:00–23:00 diyenler var ([Blogging Wizard](https://bloggingwizard.com/best-time-to-publish-youtube-videos/), [iQFluence](https://iqfluence.io/public/blog/best-time-to-post-on-youtube), [WsCube](https://www.wscubetech.com/blog/best-time-to-post-on-youtube/)). 12:00 ET'de yayın ABD'deki öğleden sonra–akşam zirvesinden 3–6 saat önce dizine girer. Bu saat İngiltere'de akşamüstüne (17:00), Hindistan'da gecenin geç saatine (21:30–22:30) denk gelir. Üç kitleyi aynı anda kapsayan tek makul pencere bu [T].
- **Gün [AÖ]:** Çalışmalar burada da çelişiyor. Buffer'ın analizi uzun video için Pazar'ı en güçlü, Perşembe'yi en zayıf gün buluyor. SocialPilot Çarşamba–Cuma diyor. Bir blog ABD için Salı–Çarşamba, İngiltere için Perşembe öneriyor ama birincil kaynak göstermiyor. Salı, Cuma ve Pazar bu iddiaların her birinden birer güne denk geliyor. Aynı zamanda aralar eşit kalıyor (2–3 gün) ve zayıf denen Perşembe'den kaçınılıyor [T].
- **Sütun–gün eşleşmesi [T]:** B (haber) Salı'ya konur, çünkü hafta sonu ve Pazartesi'nin haberleri 7–10 günlük tazelik penceresinde kalır. C (What If) Cuma'ya konur, çünkü hafta sonu merak içeriği izlenir. A (Geçmiş) Pazar'a konur: en uzun raf ömrüne sahip sütun en çok izlenme iddia edilen güne gelir.
- **Shorts 09:00 ET [T]:** Hindistan'da akşam (18:30–19:30), İngiltere'de öğleden sonra, ABD'de sabaha denk gelir. Shorts akışı dağıtımı saate uzun videodan daha az bağlıdır [AÖ, genel kabul]. Bu yüzden saat, uzun videonun ulaşamadığı Hindistan akşamına göre seçildi.
- **Doğrulama yolu:** 4 hafta sonra (12 uzun video) YouTube Studio → Kitle → "İzleyicilerinizin YouTube'da olduğu zamanlar" ile karşılaştırılır. Tek değişken değiştirilir (önce saat, sonra gün). Değişiklik bu dosyada sürüm artırarak kaydedilir.

## 2. Sütun rotasyonu
- Her hafta her sütundan bir video yayınlanır: Salı B, Cuma C, Pazar A.
- **Aynı sütun art arda iki kez yayınlanmaz.**
- **Büyük haber istisnası:** Kanalın konusuna doğrudan dokunan büyük bir olay olursa (merkez bankası şoku, büyük iflas, piyasa çöküşü) Cuma'daki C slotu ikinci bir B videosuna verilebilir. Bu ayda en fazla 1 kez yapılır ve `durum.md`'ye yazılır. Yerinden olan C videosu stoğa girer.
- Konu seçiminde trend-avcisi sütunu `$ARGUMENTS` ya da bu tablodan alır. Konunun kendisini yine 10 senaryo → viralite → hakem süreci belirler.
- 5. videodan sonra (plan v1 kuralı) sütun oranı kendi verimizle ayarlanır: CTR, ortalama izlenme yüzdesi, abone kazanımı. Hedef rakam uydurulmaz.

## 3. Stok kuralı
- **Her an en az 1 uzun video stokta durur.** Stok videosu kalite kapılarından geçmiş, hakem ONAY'ı almış ve Niyazi'nin onayladığı ama yayınlanmamış videodur.
- Stok video dosyası git'te durmaz (~450 MB). Depolama önerisi (Niyazi onayı bekliyor, `.claude/commands/bugunun-videosu.md` bölüm 3): dosya teslimde Niyazi'ye gönderilir, yüklendikten sonra YouTube'daki kopya arşiv sayılır.
- Stok videosu **raf ömrü uzun** bir sütundan seçilir (A veya C). B (haber) stoklanmaz, çünkü 7–10 günde bayatlar.
- Stok ayrıca **en az 2 Shorts** içerir (herhangi bir uzun videodan, zamana bağlı olmayan kesitler).
- Niyazi stok videosunu onaylarken onayın biçimi açıkça sorulur: "**herhangi bir slotta yayınlanabilir**". Bu onay yoksa stok video da kendi slotu için ayrıca onay bekler.
- **Başlangıç:** Takvim başlamadan önce 1 stok video (A veya C) üretilir. Önerilen geçiş, kapasite ölçülene kadar şöyledir: 1. hafta 1 uzun + 2 Shorts + 1 stok video, 2. hafta 2 uzun + 4 Shorts, 3. hafta 3 uzun + 6 Shorts (bkz. `docs/uretim-kapasitesi.md`).
- Stok tablosu (koordinatör günceller):

| Video | Sütun | Hakem | Niyazi onayı | Planlanan slot | Durum |
|---|---|---|---|---|---|
| — | — | — | — | — | (henüz yok) |

## 4. Üretim tetik günleri (öneri, [T])
Niyazi'nin "Bugünün videosu gelsin" demesi için önerilen günler (Türkiye saati) şunlardır. Her uzun video için uçtan uca tahmini süre ~8–12 saattir (bkz. `docs/uretim-kapasitesi.md`).

| Tetik | Üretilen video | Yayın | Pay |
|---|---|---|---|
| Pazar sabahı | Salı B (haber) | Salı 12:00 ET | ~1,5 gün; haber tazeliği için en geç tetik |
| Çarşamba sabahı | Cuma C | Cuma 12:00 ET | ~2 gün |
| Cuma sabahı | Pazar A | Pazar 12:00 ET | ~2 gün |
Her video Niyazi onayından sonra hemen planlanmış yayına (private + publishAt) bağlanır. Böylece Niyazi'nin yayın saatinde uyanık olması gerekmez.

## 5. Gecikme olursa
| Durum | Ne yapılır |
|---|---|
| Slottan 24 saat önce video hâlâ F9 hakem ONAY'ında değil | Koordinatör alarm verir. Stoktaki video slota atanır (Niyazi'nin "herhangi bir slot" onayı varsa). Niyazi'ye tek satır bilgi verilir. Geciken video bir sonraki uygun slota kayar ve sütun rotasyonu yeniden dizilir. |
| Geciken video B (haber) ise | Haberin üzerinden ≤10 gün geçtiyse sonraki slota alınır. Daha fazla geçtiyse senaryo-yazari videoyu kalıcı bir açıya (A) çevirir ve finans-dogrulayici yeniden doğrular. Çevrilemiyorsa video iptal edilir ve neden `durum.md`'ye yazılır. |
| Stok yok ve video gecikti | Slot **boş kalır**. Kapıdan geçmemiş video yayınlanmaz, aceleyle de üretilmez. O gün stoktaki bir Shorts yayınlanabilir. |
| Niyazi'nin onayı gecikti | Yayın yapılmaz. Onay gelince sıradaki slota planlanır. Onaysız otomatik yayın yoktur. |
| Shorts gecikti | O günün Shorts'u atlanır ya da stoktaki Shorts yayınlanır. Bir uzun videonun 2 Shorts'u kaçırılırsa ertesi hafta telafi edilmez; Shorts zamana bağlıdır. |
| Aynı haftada 2 slot kaçtı | Darboğaz analizi yapılır (`business-operations-skills:process-mapper`). Tempo geçici olarak haftada 2 uzun videoya iner. Niyazi'ye neden ve geri dönüş planıyla rapor verilir. |
| Yükleme aracı veya API engeli (denetim, kota) | Video private yüklenir ya da elle yükleme adımları `YAYIN.md`'de Niyazi'ye verilir (bkz. `docs/uretim-kapasitesi.md`). |

Kaynaklar (yalnız saat/gün için, [AÖ]): [Blogging Wizard](https://bloggingwizard.com/best-time-to-publish-youtube-videos/) · [iQFluence](https://iqfluence.io/public/blog/best-time-to-post-on-youtube) · [WsCube Tech](https://www.wscubetech.com/blog/best-time-to-post-on-youtube/) · [SocialKit](https://socialk.it/en/best-time-to-post/youtube). Buffer (1,8 milyon video) ve SocialPilot (301 bin video) çalışmalarına bu bloglar üzerinden ulaşıldı; birincil kaynakları okunmadı.
