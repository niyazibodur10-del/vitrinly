# Bölüm 001 Reels'i hangi yoldan paylaşılmalı (@flipbyvote, ilk paylaşım)

Hazırlayan: kanal-analisti · 2026-11-11 · İLERLEME: tamam
**KARAR:** İlk Reels **Instagram mobil uygulamasından (iOS/Android) elle ve planlamadan, "Şimdi paylaş" ile** gönderilsin. Trial **KAPALI**, "Add AI label" **AÇIK**, Facebook'a paylaşım **KAPALI**, kapak 9:16 olarak yüklensin ve profil ızgarası kırpımı (3:4) uygulamada düzeltilsin.
- Neden: (1) Paylaşım yolları arasında erişim farkı olduğunu gösteren resmi bir kaynak yok. Mosseri'nin "fark yok" dediği aktarılıyor ama bu ikinci el [AÖ]. Tek ters anekdot Business Suite masaüstüyle ilgili [AN]. Uygulama bu riski taşımıyor. (2) Bütün ayarları eksiksiz destekleyen tek yol uygulama: AI etiketi, özel kapak, ızgara kırpımı, Trial, müzik ve metin [AÖ]. (3) İlk Reels'te hatayı önlemek erişimden önce geliyor. Yanlış kırpılmış ızgara veya eksik AI etiketi sonradan kısmen düzeltilebilir, ama ilk saatler geri gelmez [T].
- **Trial Reels bu hesapta işe yaramaz:** hesabın şu an 0 takipçisi ve 0 gönderisi var [D-API]. Trial için bildirilen eşik 1.000 takipçi (2025, Mosseri) [AÖ] ya da profesyonel hesapta 200 takipçi (2026 rehberleri) [AÖ]. Trial'ın tek işi takipçiden saklamak. 0 takipçide her Reels zaten yalnız takipçi olmayanlara gider. Trial açılırsa ilk Reels profil ızgarasında da görünmez, bu da profile gelen ziyaretçiyi boş sayfayla karşılar [D-1].
- **Planlı paylaşım:** Mosseri'nin Ağustos 2026 Q&A'sında "There's no difference in terms of your reach" dediği aktarılıyor [AÖ, birincil kaynak bulunamadı]. Erişim cezası kanıtı yok. Yine de ilk Reels'te planlama gerekmiyor, çünkü saat zaten bugün.
- **Sonraki bölümler (günlük):** Graph API ile yayın (`trial_params`, `is_ai_generated`, `cover_url`, `share_to_feed`) gözlem olarak 002'den itibaren denenebilir. 001 ile 002 arasındaki 24 saatlik görüntüleme farkı bu yolu doğrulamaz, çünkü bölümler aynı içerik değil [T]. Karar 3+ bölümlük kıyas sonrası verilecek (§5).

Etiketler: **[D-n]** doğrulandı: birincil kaynak bu oturumda açıldı (§6). **[D-API]** bu oturumda Graph API ile ölçüldü (2026-11-11). **[AÖ]** arama özeti, üçüncü taraf veya ikinci el. **[AN]** anekdot. **[T]** tahmin. **[ÖB]** ön bilgi, bu oturumda doğrulanmadı.

## 1. Yol yol karşılaştırma
| Özellik | IG uygulaması | Business Suite (web/mobil) | IG web | Graph API | 3. taraf planlayıcı |
|---|---|---|---|---|---|
| Erişimde resmi fark | yok [AÖ] | yok; bir yazarın masaüstünde düşük görüntüleme aldığı vaka var [AN] | kanıt yok [T] | yok [AÖ] | yok; Hootsuite testinde n=5 gönderi, anlamlı değil [AÖ] |
| AI etiketi | var ("Label as made with AI") [AÖ] | belirsiz [AÖ] | belirsiz [T] | `is_ai_generated` parametresi var [D-2] | araca göre değişiyor [T] |
| Özel kapak | var [AÖ] | var (kare seçimi veya yükleme) [AÖ] | sınırlı [T] | `cover_url` / `thumb_offset` [D-2] | var [AÖ] |
| Izgara (3:4) kırpımı | var: "Profile grid" sekmesi ve sonradan "Adjust preview" [AÖ] | yok [T] | yok [AÖ] | yok. API ortadaki 9:16'yı ve beslemede 1:1'i kırpar [D-2]; düzeltme sonradan uygulamada | yok [T] |
| Trial Reels | var, uygun hesapta [D-1] | doğrulanamadı [AÖ] | yok [T] | `trial_params` (MANUAL / SS_PERFORMANCE) [D-2] | bazılarında var [AÖ] |
| Konum / hashtag | var / var | var / var [AÖ] | var / var [T] | `location_id` / altyazıda [D-2] | var [AÖ] |
| Facebook'a çapraz paylaşım | var (bağlı Sayfa) [ÖB] | var ("Share to Facebook") [AÖ] | yok [T] | ayrı FB çağrısı gerekir; IG referansında yok [D-2] | var [AÖ] |
| Planlama | var [ÖB] | var [AÖ] | yok [T] | kendi zamanlayıcımızla [T] | var |

## 2. Adım adım (Niyazi, telefonda, ≈10 dk)
1. Bitmiş 001 videosunu (83 sn, 9:16, 1080×1920) ve kapak dosyasını (`kapak-1080x1920.jpg`) telefona aktar: `uretim/seri/bolum-001/teslim/`. Kaliteyi korumak için kablo ya da AirDrop kullan, mesajlaşma uygulamasıyla gönderme [T].
2. Gönderiden ÖNCE uygulamada şu yolu aç: Profil → ☰ → Account Status → "Recommendations". Hesap öneriye uygun görünmeli [ÖB]. Uygun değilse paylaşma, koordinatöre bildir.
3. + → Reel → videoyu seç. Uygulama içinde müzik veya filtre ekleme: ses kendi miksimiz, ayrıca lisans riski doğar.
4. Kapak: "Edit cover" → "Add from camera roll" → kapak `kapak-1080x1920.jpg`. Ardından **"Profile grid"** sekmesinde 3:4 kırpımda yüzlerin ve "$100" yazısının içeride kaldığını kontrol et.
5. Altyazı: paket taslağındaki İngilizce metin ve o bölümün seçeneklerini adıyla soran soru (`politika-format.md` §1-B). Hashtag sayısı 3–5, konuyla ilgili olsun [ÖB: Mosseri, hashtag'in erişime katkısı az]. Konum ekleme: kurgu dizi, ABD kitlesi, konumun katkısına dair kanıt yok [T].
6. Advanced settings → **"Add AI label" AÇIK** (politika raporu §3 önerisi; zorunlu değil).
7. **Trial toggle'ı görünürse KAPALI bırak.**
8. **"Share to Facebook" KAPALI.** Gerekçe §4'te.
9. **20:00 TSİ'de (17:00Z, 12:00 ET)** "Share" ile hemen paylaş. Bu saat CLAUDE.md'de sabit (Niyazi 2026-11-11, üç platform aynı anda); planlama gerekmez. Ardından aynı bölüm için hikâyeye anket çıkartması ekle. Anket oyları da sayılıyor (az yorum kuralı).
10. Paylaştıktan sonraki ilk 60 dakika: koordinatör yorum yanıtlarını Graph API ile verir (kalıcı izin var). Ben 24 saatlik ölçümü `GET /{media-id}/insights` ile alırım: views, reach, comments, saves, shares. 48 saatlik rapor `uretim/seri/bolum-001/yayin-sonrasi/performans-48s.md` dosyasına yazılır.

## 3. Reddedilen seçenekler
- **Graph API (001 için):** AI etiketi, kapak ve Trial destekleniyor [D-2], ama 3:4 ızgara kırpımı ayarlanamıyor. Kapak ortadan kırpılır [D-2], düzeltme sonradan uygulamada yapılmalı. Ayrıca API'den hiç Reels gönderilmedi; ilk yayını denenmemiş bir hatta yapmak hata riski taşır [T]. Paylaşım kotası 0/100 [D-API], yani engel kota değil. **002'den itibaren aday** (§5).
- **Meta Business Suite:** AI etiketi ve Trial desteği doğrulanamadı [AÖ]. Izgara kırpımı yok. Masaüstünden gönderilen Reels'in düşük dağıtım aldığına dair bir anekdot var [AN: Jon Loomer]. Avantajı (FB çapraz paylaşım ve planlama) bugün gerekmiyor.
- **Instagram web:** kapak, kırpım ve AI etiketi kontrolü belirsiz ya da yok [T/AÖ]. İlk gönderide eksik ayar riski var.
- **3. taraf planlayıcılar (Later, Buffer, Metricool…):** erişim avantajı yok [AÖ]. Ek hesap bağlantısı gerekiyor, birçoğu ücretli (onay kuralı). Graph API'nin üstüne bir katman daha ekliyorlar. Bizim kendi API hattımız zaten var.
- **Trial Reels:** hesap uygun değil (0 takipçi) [D-API + AÖ eşikleri]. Uygun olsa bile 0 takipçide getirisi yok, üstelik profil ızgarasından gizler [D-1].
- **Planlı paylaşım:** cezası yok [AÖ]. Bugün gerekmiyor, uygulamada canlı paylaşım daha az adım.

## 4. Facebook çapraz paylaşım neden KAPALI
- Oy döngüsü tek yerde toplanmalı. FB'deki yorumlar kazanan seçimine girmezse izleyici kandırılmış olur. Girerse ikinci bir API ve izin yolu gerekir [T].
- FB yorumlarına yanıt vermek CLAUDE.md'deki kalıcı izin kapsamında değil (izin IG/YT için verilmiş) [T: yorum, Niyazi teyidi gerekir].
- Bağlı FB Sayfası olup olmadığı bu oturumda ölçülmedi [T]. FB, döngü kurulunca ayrı bir test olarak açılır.

## 5. Yol testi (002 sonrası)
- 002, 003 ve 004'ü Graph API ile yayınla (`is_ai_generated=true`, `cover_url`, `share_to_feed=true`). Ardından ızgara kırpımını uygulamada "Adjust preview" ile düzelt.
- Bölümler aynı içerik olmadığı için bu kıyas nedensel değil. Uygulama ile API arasında 24 saatlik views/reach'te sistematik ve büyük bir fark çıkarsa (ör. API ile yayınlanan 3 bölümün 3'ü de uygulamayla yayınlanan medyanın %50'sinin altında kalırsa [T: eşik önerisi]) uygulamaya dönülür.
- Trial: hesap 200 (ya da 1.000) takipçiyi geçince toggle'ın görünüp görünmediği kontrol edilir. Trial, ana bölüm için değil, alternatif kancalı ikinci kesit için kullanılır [T].

## 6. Kaynaklar
- [D-1] Instagram for Creators, "Trial reels" (2024-12-10): https://creators.instagram.com/blog/instagram-trial-reels. Trial Reels Feed'de, Reels sekmesinde, profildeki Reels sekmesinde ve ana ızgarada görünmez; otomatik paylaşım ilk 72 saatteki görüntülemeye göre.
- [D-2] Meta for Developers, IG User Media referansı: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media. Belgelenen parametreler: `trial_params`, `cover_url`, `thumb_offset`, `share_to_feed`, `location_id`, `is_ai_generated`. Kapak 9:16 ortadan, beslemede 1:1 kırpılır; FB çapraz paylaşımından söz edilmiyor.
- [D-API] `GET /17841419169966345?fields=followers_count,media_count` → 0 / 0; `content_publishing_limit` → kullanım 0 / 100 / 24 sa (2026-11-11).
- [AÖ] Mosseri, Ağustos 2026 Q&A, Kontentino aktarımı: https://www.kontentino.com/q-and-a/does-scheduling-instagram-posts-affect-reach/. Birincil video bulunamadı.
- [AÖ] Trial eşikleri: Social Media Today (1.000, 2025) https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/ · Planoly (200 / 1.000, 2026) https://www.planoly.com/blog/how-to-post-a-trial-reel-on-instagram
- [AÖ] Hootsuite deneyi (2025-04-30, n=5+5, satıcı): https://blog.hootsuite.com/experiment-third-party-scheduling-instagram/
- [AÖ] Izgara 3:4: https://planoly.com/blog/guide-to-instagrams-new-vertical-grid · AI etiketi: https://help.instagram.com/761121959519495 (sayfa WebFetch ile açılmadı) · Business Suite "Share to Facebook": https://www.graphed.com/blog/how-to-create-a-reel-on-meta-business-suite
- [AN] Jon Loomer, Business Suite Reels hatası: https://www.jonloomer.com/qvt/instagram-reels-bug-and-meta-business-suite/

## Erişim engelleri
- help.instagram.com WebFetch ile boş döndü. Uygulamadaki AI etiketi ve Trial eşiği Meta'nın kendi yardım metniyle doğrulanamadı.
- Mosseri'nin planlama açıklamasının birincil kaynağı (video veya story) bulunamadı.
- Graph API `account_type` alanı v21'de yok. Hesap türü (Creator/Business) yalnız uygulamadan doğrulanabilir.
