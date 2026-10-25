# Pazaryeri Kuralları Araştırması: Trendyol + Hepsiburada (v0)

Vitrinly'nin üç modülü için kural tabanı: (1) SEO başlık/açıklama yazıcı, (2) uyum denetleyici, (3) görsel prompt üretici (satıcının gerçek ürün fotoğrafını düzenleyerek).

- **Araştırma tarihi:** 25 Ekim 2026
- **Yöntem:** WebSearch (Türkçe sorgular, önce resmi alan adlarıyla sınırlı aramalar). Sayfaların kendisi açılamadı (aşağıya bakın).
- **Makine okunur kural listesi:** `kural-tabani-v0.yaml`

## Etiketler ve erişim durumu

| Etiket | Anlamı |
| --- | --- |
| **VERIFIED** | Sayfa açılıp metin doğrudan okundu (URL + tarih ile). |
| **SNIPPET (resmi)** | Bilgi resmi alan adındaki bir sayfanın arama özetinden geliyor (akademi.trendyol.com, developers.trendyol.com, ticaret.gov.tr, rok.org.tr, titck.gov.tr, hepsiburada.com). Sayfa açılıp okunmadı. |
| **SNIPPET (3. taraf)** | Bilgi blog, entegratör, hukuk bürosu veya araç satıcısı sayfalarının arama özetinden geliyor. Doğrulama gerekir. |
| **UNKNOWN** | Bilgi bulunamadı ya da kaynaklar çelişiyor. |

> **Bu turda hiçbir madde VERIFIED değil.** Ortamın çıkış proxy'si, aşağıdaki sitelerin hepsini engelledi (CONNECT 403 / DNS çözülemedi). Bu yüzden WebFetch/curl ile hiçbir sayfa açılamadı: developers.trendyol.com, akademi.trendyol.com, partner.trendyol.com, trendyol.com, developers.hepsiburada.com, merchant.hepsiburada.com, hepsiburada.com, mevzuat.gov.tr, resmigazete.gov.tr, ticaret.gov.tr, birfatura.com (test). GitHub kod araması da oturum politikası nedeniyle kapalıydı.
> Aşağıdaki "SNIPPET (resmi)" maddeleri güvenilirliği en yüksek olanlar. Ürüne almadan önce bir insanın tarayıcıda açıp metni teyit etmesi gerekiyor (ayrıntılar bölüm H'de).

---

## A. Arama ve sıralama faktörleri

### Trendyol
- **SNIPPET (resmi): Trendyol Arama Motoru sayfası** ([detay/49](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/49)). Kriterler "dikkate alınabilecek" diye veriliyor; ağırlıklar açıklanmıyor.
  - **Sorgu sinyalleri:** müşterinin yazdığı anahtar kelime, cinsiyet içeren arama terimi olup olmadığı, kategori filtresi kullanım adedi, kategori bazlı tıklanma verisi, arama terimi ile ürün bilgileri arasındaki alaka.
  - **Ürün performansı:** görüntülenme, tıklanma ve satın alma sayıları ile ürünler arası tamamlayıcılık oranı.
  - **Reklam verisi:** TBM, bütçe, reklam tıklanma ve satın alma sayıları.
  - **Satıcı ve operasyon verisi:** iade adedi.
  - **Ürün bilgisinin eksiksizliği:** isim, açıklama, görsel, beden, fiyat, marka, özellikler, stok. Doğru girilen özellikler filtrelemede ürünü öne çıkarıyor.
  - **Ürün adında spesifik özellik:** görünürlüğü artırıyor. Sayfadaki örnek: "Siyah Kruvaze Yaka Dantel Elbise" aramasında yalnızca yüz küsur sonuç çıkıyor.
  - **Mağaza adının aramada çıkması:** jenerik kelime içermemeli, "ltd." veya "a.ş." gibi ekler taşımamalı ve 40 karakterden kısa olmalı. Ziyaret oranı ve mağaza adının aranma sıklığı da etkili.
  - **Koleksiyonlar:** satıcı ya da influencer koleksiyonlarının içeriği sıralamayı etkileyebiliyor.
- **SNIPPET (resmi):** Ürün reklamları ürünü üst sıralara taşıyor; Trendyol, BuyBox kazanan ürünleri otomatik seçiyor ([ads.trendyol.com](https://ads.trendyol.com/)). Bu Trendyol'un kendi pazarlama metni.
- **SNIPPET (3. taraf):** Ajanslar ek olarak satış hızı, puan ve yorum, fiyat rekabeti ve kargo hızını sayıyor. Bunların hiçbiri resmi olarak ağırlıklandırılmamış.

### Hepsiburada
- **SNIPPET (resmi):** "Sıralama algoritması hakkında" sayfası ([staticpage/64572361330497](https://www.hepsiburada.com/staticpage/64572361330497)).
  - "Önerilen" sıralama algoritma destekli ve en çok satanları üste çıkarıyor.
  - Yeni eklenen veya sponsorlu ürünler öncelikli gösterilebiliyor.
  - Diğer sıralama seçenekleri: çok satan, değerlendirme sayısı, fiyat, yeni, yüksek puan.
- **SNIPPET (3. taraf)** (Joy Akademi, Dopinger, Roketfy):
  - teknik özellik alanlarının eksiksizliği,
  - başlıkta anahtar kelime,
  - gönderim süresi, iptal ve iade oranı, mağaza puanı,
  - tıklama, satış ve iade verisinden öğrenen ML,
  - yeni ürünlerin ilk satışlarla test edilmesi.
- **UNKNOWN:** Hepsiburada'nın metin alanlarını (başlık, açıklama) arama alaka sinyali olarak nasıl kullandığı resmi olarak bulunamadı.

**Ürüne etkisi:** SEO yazıcı, resmi olarak doğrulanabilen iki kaldıraca odaklanmalı: (a) başlıkta aranan spesifik özellikler (renk, malzeme, model, gramaj), (b) kategori özellik alanlarının eksiksiz ve doğru doldurulması. Performans sinyalleri (CTR, satış) yazının kontrolünde değil. Bu yüzden "sıralama garantisi" vaadi verilmemeli. Panelde bir "özellik doluluk skoru" göstermek, resmi olarak dayanağı olan bir metrik.

---

## B. Başlık (ürün adı) kuralları

### Trendyol

| Kural | Durum | Kaynak |
| --- | --- | --- |
| API'de `title` zorunlu, **en fazla 100 karakter** | SNIPPET (resmi) | [Ürün Aktarma v2](https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-aktarma-v2createproducts), [Product Create v2](https://developers.trendyol.com/v2.0/docs/product-create-v2) |
| Ürün adı ve açıklamaya **yalnızca görseldeki ürünün kendi markası** yazılır; farklı markalar yazılmaz | SNIPPET (resmi) | [Kalite Standartları detay/204](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/204) |
| Görsel veya açıklamadakinden farklı ya da birden fazla markayla ürün açmak "Hatalı Marka Girişi" sayılır: ürün kapatılır ve ihlal puanı verilir | SNIPPET (resmi) | [detay/205](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/205), [detay/242](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/242) |
| Başka bir e-ticaret sitesinin adı veya adresi ürün sayfasında yer alamaz | SNIPPET (resmi) | detay/204 |
| Ürün adı, aramalarda kolay bulunacak şekilde yazılmalı | SNIPPET (resmi) | [Tekil Ürün Oluştur detay/147](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/147) |
| Model kodu en az 8 karakter; renk ve beden varyantlarında aynı model kodu kullanılır; tire kullanılabilir | SNIPPET (resmi) | detay/147 |
| Marka tanımlamada alt kategori veya ürün ismi içeren markalar, barkod numarası olan markalar ve özel karakter içeren markalar kabul edilmez | SNIPPET (resmi) | [Marka Tanımlama detay/145](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/145) |
| Başlıkta BÜYÜK HARF, emoji veya özel karakter yasağı | **UNKNOWN** | detay/242'nin tam metni görülemedi |
| Anahtar kelime doldurma (keyword stuffing) için açık yasak | **UNKNOWN** | Resmi metinde bulunamadı |

### Hepsiburada

| Kural | Durum | Kaynak |
| --- | --- | --- |
| Başlık en fazla 255 karakter | SNIPPET (3. taraf), çelişkili | [birfatura](https://birfatura.com/hepsiburada-urun-yukleme-yollari/) (başka bir kaynak 50–150 öneriyor) |
| Aşırı büyük harf, emoji ve sembol kullanılmaz; marka başa yazılır | SNIPPET (3. taraf) | birfatura |
| Akademi'de "Ürün Adı" eğitimi ve SSS'de "Ürün başlığı/adı nasıl olmalıdır?" sorusu var; içerik görülemedi | UNKNOWN | [akademi SSS](https://akademi.hepsiburada.com/portal/faq), [toplu ürün eğitimi](https://akademi.hepsiburada.com/portal/course/toplu-urun-eklerken-dikkat-edilmesi-gerekenler-172801) |
| API alan adı `productName` | SNIPPET (3. taraf) | Packagist PHP istemcileri, [peliel docs](https://docs.marketplace.peliel.com/hepsiburada/ueruen-goenderme) |

**Ürüne etkisi:** Başlık yazıcının sert sınırları şunlar olmalı:
- Trendyol için ≤100 karakter (block).
- Hepsiburada için resmi sınır doğrulanana kadar ihtiyatlı bir hedef (ör. ≤150 karakter önerisi, 255 karakter hard warn).
- Başlıkta yalnızca satıcının kendi markası geçmeli. Rakip marka ve "X uyumlu" gibi ifadeler denetimden geçmeli. "Uyumlu" kullanımının serbest olup olmadığı UNKNOWN.
- Başka site adı ya da URL geçmemeli.
- Emoji, tüm-büyük-harf ve tekrar eden kelimeler, resmi dayanak bulunana kadar **warn** seviyesinde tutulmalı.

---

## C. Açıklama / içerik kuralları

### Trendyol
- **SNIPPET (resmi):** API'de `description` zorunlu, **HTML string, en fazla 30.000 karakter** ([Ürün Aktarma v2](https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-aktarma-v2createproducts)). Hangi HTML etiketlerinin kabul edildiği **UNKNOWN**.
- **SNIPPET (resmi):** Açıklamada ürün özellikleri ve kullanım detayı yer almalı.
  - **Gıdada:** Türk Gıda Kodeksi Etiketleme Yönetmeliği'ndeki bilgiler zorunlu. Bunlar: gıdanın adı, bileşenler, net miktar, son tüketim tarihi, işletmecinin unvanı ve adresi, işletme kayıt numarası.
  - **Elektronikte:** garanti koşulları ve kurulum bilgisi.
  - Kaynak: [detay/242](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/242), [detay/204](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/204).
- **SNIPPET (resmi):** Ret sebepleri arasında "Açıklama ve görsel uyumsuz" ile "Renk ve görsel uyumsuz" var ([Ürün Ret Sebepleri detay/349](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/349)).
- **SNIPPET (resmi):** Barem, fiyat veya desi hakkında yanıltıcı bilgi vermek ihlal puanı gerektiriyor. İndirimler müşteriyi yanıltmamalı (detay/205).
- **SNIPPET (resmi):** Satışı yasak ya da yüksek sağlık riskli bir ürünü kategori değiştirerek veya isim, görsel, açıklamayı yanlış yazarak listelemek ihlal puanı gerektiriyor ([Satışı Uygun Olmayan Ürünler detay/241](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/241)).
- **SNIPPET (resmi):** Müşteri sorularını dış mecralara yönlendirmek, ilgisiz cevap vermek ve yanıltıcı cevap vermek ihlal puanı gerektiriyor ([Müşteri Soruları Kuralları detay/243](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/243), detay/205). API'de cevap 10–2000 karakter olmalı ve yasaklı kelime filtresinden geçiyor (bkz. G).
- **UNKNOWN:** Açıklamada telefon, e-posta ve URL yasağının açık maddesi. "E-posta / Telefon numaraları / İnternet Üyelik Hesapları" başlığı görüldü ama bağlamı net değil. Dış mecraya yönlendirme yasağıyla birlikte düşünüldüğünde yüksek olasılıkla yasak; yine de teyit gerekiyor.

### Hepsiburada
- **UNKNOWN:** Akademi'de "Ürün Eklerken Dikkat Edilmesi Gerekenler / Ürün Açıklaması" eğitimi var, ancak içeriği görülemedi ([link](https://akademi.hepsiburada.com/portal/course/urun-eklerken-dikkat-edilmesi-gerekenler-urun-aciklamasi-162691)).
- **SNIPPET (3. taraf):** Zorunlu alanlar kategoriye göre değişiyor; eksik alan onaydan dönüşe yol açıyor. API alanları: `productDescription`, `brand`, `barcode`, `merchantSku`, `image1..image5`.
- **SNIPPET (resmi):** Fikri mülkiyet şikayetinde ilan kaldırılabiliyor. Haklı itirazda ilan 24 saat içinde geri açılıyor ([FSMH süreci](https://www.hepsiburada.com/staticpage/672485678087016)).

**Ürüne etkisi:**
- Açıklama yazıcı HTML üretmeli, ancak kategori bazlı **zorunlu bilgi blokları** eklemeli. Takviye ve gıda için TGK etiket bilgileri, elektronik için garanti ve kurulum bilgisi gerekiyor.
- Çıkan metin, ürünün yapılandırılmış özellikleriyle (renk, beden, gramaj) **tutarlılık kontrolünden** geçmeli. Trendyol'da "açıklama ve görsel uyumsuz" bir ret sebebi.
- İletişim bilgisi, URL ve başka site adı içeren metin block edilmeli.

---

## D. Görsel kuralları

### Trendyol

| Kural | Durum | Kaynak |
| --- | --- | --- |
| API: görsel URL'leri SSL'li **https** olmalı; barkod başına **en fazla 8 görsel**; **1200x1800 px, 96 dpi** (2:3) | SNIPPET (resmi) | [Ürün Aktarma v2](https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-aktarma-v2createproducts) |
| Akademi: görsel **en az 600x800**, web için 72 dpi, **en fazla 10 MB**; standart bir ölçü belirlenmeli | SNIPPET (resmi) | [detay/242](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/242) |
| Görselde **logo, yazı veya kalite sorunu** ret sebebi | SNIPPET (resmi) | [detay/349](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/349) |
| Görsel ürünle aynı boyut, renk ve marka özelliklerini taşımalı; taşımayan ürün satışa açılmaz | SNIPPET (resmi) | detay/204 |
| Farklı marka veya e-ticaret sitesi logosu ya da adı taşıyan görsel kabul edilmez | SNIPPET (resmi) | detay/204 |
| Görseller telifsiz ya da satıcıya ait olmalı | SNIPPET (resmi) | detay/242 |
| Görselde **sağlık beyanı bulunmamalı** | SNIPPET (resmi) | detay/242 |
| Çocukların vücudunu teşhir eden görseller reddedilir (cansız manken kullanılabilir); çocuk ve gençleri olumsuz etkileyebilecek içerik yasak | SNIPPET (resmi) | detay/242, detay/241 |
| Arka plan rengi (beyaz zorunluluğu) | **UNKNOWN** (3. taraf: "beyaz/nötr tercih edilir") | birfatura, photoroom |
| Kolaj veya çoklu ürün yasağı | SNIPPET (3. taraf): "ana görselde tek ürün, karışık görseller reddedilir" | [idifo](https://idifo.com/blog/trendyol-gorsel-kurallari/), [webaction](https://webaction.com.tr/yapay-zeka-kullanarak-urun-fotograflari-duzenlenebilir-mi/) |
| Yapay zekâ ile üretilmiş görsel | **UNKNOWN** (resmi kural bulunamadı). 3. taraf: "ürünü birebir yansıtıyorsa kullanılabilir". Şikayetvar'da AI görsellerin yanılttığına dair tüketici şikayetleri var | [digitalkafalar](https://www.digitalkafalar.com/trendyolda-yapay-zeka-urun-fotografi-kullanilir/), [sikayetvar](https://www.sikayetvar.com/trendyol/trendyolda-yapay-zeka-ile-hazirlanan-urun-gorselleri-tuketiciyi-yaniltiyor) |

> Not: API'deki 1200x1800 ile Akademi'deki "min 600x800" birbiriyle çelişmiyor. Her ikisi de 2:3 oranında. Güvenli hedef **1200x1800, 2:3**.

### Hepsiburada

| Kural | Durum | Kaynak |
| --- | --- | --- |
| Akademi'de "Ürün Görsel Ölçüleri" eğitimi var; değerler görülemedi | UNKNOWN | [link](https://akademi.hepsiburada.com/portal/course/urun-gorsel-olculeri-167928) |
| En az 500x500 px; önerilen ≥1200x1200 (kare); bazı kaynaklar en az 800 veya 1000 px diyor | SNIPPET (3. taraf), çelişkili | [emstudio](https://www.emstudio.tr/hepsiburada-e-ticaret-fotograf-olculeri-2025-rehberi/), [meayt](https://www.meayt.com/blog/hepsiburada-urun-gorseli-boyutlari-ve-kurallari/), [netkasam](https://www.netkasam.com/blogs/hepsiburadaya-urun-yukleme-nasil-yapilir) |
| Ana görselde saf beyaz zemin (255,255,255), gölge yok; ürün karenin %85'inden fazlasını kaplamalı | SNIPPET (3. taraf) | emstudio, meayt |
| Logo, yazı, filigran, ikon ve sosyal medya adresi yasak | SNIPPET (3. taraf), birden çok kaynakta tutarlı | meayt, diyaframpro |
| Yalnızca JPG ve PNG; görsel URL'leri erişilebilir olmalı (sistem 5 kez deniyor) | SNIPPET (resmi-kardeş: developers.hepsiexpress.com) | [hepsiexpress ürün bilgisi gönderme](https://developers.hepsiexpress.com/?docs=dokuman/entegrasyon/urun-bilgisi-gonderme) |
| Dosya boyutu sınırı 5–10 MB | SNIPPET (3. taraf), çelişkili | — |
| Ürün videosu şartları için ayrı bir Akademi sayfası var | UNKNOWN (içerik görülemedi) | [video şartları](https://akademi.hepsiburada.com/portal/course/urun-ekleme-asamasinda-video-sartlari-nelerdir-191652) |

**Ürüne etkisi (görsel prompt üretici için kritik):**
1. **Platform profilleri ayrı olmalı.** Trendyol için 2:3 (1200x1800), Hepsiburada için kare (≥1200x1200). Çıktı her ikisine ayrı ayrı export edilmeli.
2. **Prompt'a sabit negatif kısıtlar eklenmeli:** metin, logo, filigran, rozet ("%50 indirim", "en çok satan"), başka marka, site adı ve sağlık beyanı/ikon eklenmeyecek.
3. **Sadakat kısıtı:** Ürünün rengi, şekli, etiketi, ölçek ve oranı değiştirilmemeli. Trendyol'da görsel-ürün uyumsuzluğu ret sebebi ve buybox ihlali. 2026 yönetmeliği de yanıltıcı uygulamaları sıkılaştırdı. Bu yüzden düzenleme yalnızca arka plan, ışık ve sahne üzerinde olmalı; ürün pikselleri korunmalı (maskeli inpainting).
4. **Ana görsel tek ürün ve sade zemin olmalı.** Lifestyle ya da sahne görselleri ikincil görsel olarak önerilmeli.
5. **Çocuk ürünlerinde** insan model üretimi kapalı olmalı (manken veya düz serim).
6. AI kullanımına dair resmi pazaryeri kuralı yok. Ancak gerçek kişinin AI kopyasıyla ürün kullanıyormuş gibi gösterilmesi artık yönetmelikle yasak (bkz. F). Bu yüzden **"insan yüzü üretimi" varsayılan olarak kapalı** olmalı.

---

## E. İhlal ve ceza sistemi

### Trendyol: SNIPPET (resmi)
Kaynaklar: [detay/205](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/205) ve [detay/209](https://akademi.trendyol.com/satici-bilgi-merkezi/detay/209).

- **Puan eşikleri:**

  | Toplam puan | Yaptırım |
  | --- | --- |
  | 12 | 2 gün askı |
  | 24 | 5 gün askı |
  | 36 | 7 gün askı |
  | 48 | Süresiz askı; 15 gün sonra sözleşme feshi |

- **Puanların ömrü:** Hesap kapanmadıysa her puan 6 ay sonra siliniyor.
- **İtiraz:** Puan yansıdıktan sonraki 7 gün içinde yapılabiliyor. İtiraz geçerli bulunursa puan siliniyor ve askı uygulanmıyor. Puanlar Satıcı Paneli'ndeki "İhlaller" ekranından izleniyor.
- **İçerik ile ilgili puanlı ihlaller:**
  - "İçerik Kalitesine Aykırılık": hatalı marka girişi,
  - ürünü yanlış kategoride listeleme,
  - barem, fiyat veya desi hakkında yanıltıcı bilgi,
  - yanıltıcı indirim,
  - satışı yasak ürünü kategori değiştirerek veya yanlış içerikle listeleme,
  - sorularda dış mecraya yönlendirme ya da yanıltıcı cevap,
  - sahte değerlendirme oluşturma.
- **Buybox ihlali:** Görsel, isim veya açıklamadan farklı ürün gönderilirse ürün derhal kapatılıyor.
- **Ret süreci:** Reddedilen ürünler Satıcı Paneli > Ürün > Ürün Listesi > "Revize Gerekenler" altında görünüyor. Kontrol yaklaşık 3 iş günü sürüyor (detay/147).
- **UNKNOWN:** İhlal başına kaç puan verildiği. Tablonun var olduğu görülüyor ama rakamlar özetlerde yok.
- **SNIPPET (3. taraf):** "Para cezası 10.000 TL'ye kadar" iddiası tek bir blogda geçiyor ([birfatura](https://birfatura.com/trendyol-cezasi-ne-kadar/)). Doğrulanmadı.

### Hepsiburada
- **UNKNOWN:** Resmi bir puan veya ceza tablosu bulunamadı.
- **SNIPPET (3. taraf)** ([birfatura](https://birfatura.com/hepsiburada-cezalari-nelerdir/), [yengec](https://yengec.co/blog/hepsiburada-magaza-cezalari/)):
  - kargo gecikmesi, eksik ürün, iptal ve yanlış ürün için sipariş bedeli üzerinden yüzdesel ceza;
  - mağaza puanı düşüşü, görünürlük kaybı, komisyon artışı;
  - "6 ay içinde 4 kez listeye giren hesap süresiz kapatılır" iddiası (tek kaynak).
- **SNIPPET (resmi):** Satıcı puanı kriterleri arasında eksik, hatalı veya hasarlı ürün göndermemek var ([Satıcı puanları](https://www.hepsiburada.com/satici-puanlari-nasil-hesaplaniyor)).

**Ürüne etkisi:**
- Uyum denetleyicinin sonuç ekranı, Trendyol için "bu madde ihlal puanı riski taşır" etiketini kural bazında gösterebilir: hatalı marka, yanlış kategori, yanıltıcı fiyat/indirim, yanıltıcı soru cevabı.
- Puan rakamı UNKNOWN olduğu için **puan miktarı gösterilmemeli**; yalnızca risk seviyesi gösterilmeli.
- Soru-cevap modülü planlanırsa, cevaplar dış mecraya yönlendirme ve iletişim bilgisi açısından **block** filtresinden geçmeli.

---

## F. Türk reklam hukuku (ilan metinlerine uygulanabilir kısım)

### F1. Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği: 2026 değişikliği
- **SNIPPET (resmi):** Değişiklik **1 Temmuz 2026 tarihli ve 33297 sayılı Resmî Gazete**'de yayımlandı ve **1 Ağustos 2026**'da yürürlüğe girdi. Kaynaklar: [ticaret.gov.tr duyurusu](https://ticaret.gov.tr/haberler/ticaret-bakanligi-tarafindan-ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeliginde-yapilan-degisikliklerle-tuketicilerin-aldatici-reklam-ve-ticari-uygulamalara-karsi-korunmasi-guclendiriliyor), [ROK özeti](https://www.rok.org.tr/haberler/ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeligi-degisikligi/), [ROK PDF](https://www.rok.org.tr/wp-content/uploads/2026/07/Reklam-Yonetmeligi_Temmuz-26-1.pdf).
- **İndirim öncesi fiyat** (SNIPPET, resmi): referans fiyat, indirimin başlangıcından önceki **10 gün** içinde uygulanan **en düşük fiyat**. Önceki kural 30 gündü.
  - Çabuk bozulan mallar ve hizmetlerde, indirimden bir önceki fiyat esas alınıyor.
  - Ürün birden fazla kanalda satılıyorsa, yalnızca indirimin uygulandığı kanaldaki fiyat esas alınıyor (3. taraf).
  - Koşullu satış teklifleri de indirimli satış reklamı kurallarına dahil edildi.
  - Kaynak: [ticaret.gov.tr: indirimli satış düzenlemesi](https://ticaret.gov.tr/haberler/ticaret-bakanligindan-indirimli-satis-reklamlarinda-seffafligi-artiracak-yeni-duzenleme).
- **Yapay zekâ** (SNIPPET, resmi/ROK):
  - Gerçek kişilerin AI ile oluşturulmuş dijital kopyalarıyla, o kişi ürünü kullanıyor, deneyimliyor veya tavsiye ediyormuş izlenimi veren reklamlar yasak.
  - Satın almayı etkileyebilecek AI ya da gerçeğinden ayırt edilemeyen dijital karakterler açıkça etiketlenmeli.
- **Çevresel beyan** (SNIPPET, resmi): "çevresel beyan" kavramı tanımlara eklendi. "Çevre dostu", "yeşil" gibi genel ifadeler açıklama yapılmadan kullanılamaz.
- **Tüketici yorumları** (SNIPPET, resmi/3. taraf):
  - Yalnızca ürünü satın alanlar değerlendirme yapabilir.
  - Olumlu ve olumsuz yorumlar ayrım yapılmadan, objektif sıralamayla ve **en az 1 yıl** gösterilmeli.
  - Sahte yorum ya da onay ifadesi için anlaşma yapmak yasak.
- **Diğer değişiklikler** (SNIPPET):
  - Influencer reklamları "reklam" veya "tanıtım" etiketiyle açıkça ayırt edilebilir olmalı.
  - Akademik unvanın gerçeğe aykırı kullanımı yasak.
  - Çocuklara profillemeyle hedefli reklam yasak.
  - **Takviye edici gıdada karşılaştırmalı reklam yasağı kaldırıldı**, ancak sağlık beyanı kapsamındaki konular karşılaştırılamaz.
- **Ceza** (SNIPPET, 3. taraf): Aldatıcı indirim reklamına "39,9 milyon TL'ye kadar" ceza iddiası tek bir hukuk bülteninde geçiyor ([Kurşun & Partners](https://kursunpartners.com/tr/hukuk-bulteni/gelisme/indirimli-satis-reklamlarinda-son-10-gun-en-dusuk-fiyat-kurali/)). Teyit edilmedi.

### F2. Genel ilkeler (mevcut yönetmelik)
- **SNIPPET (3. taraf / mevzuat özeti):** Reklamdaki iddiaların doğruluğunu reklam veren ispatlamak zorunda. Dayanak: Yönetmelik m.9 ve 6502 sayılı Kanun (TKHK) m.61/6.
- **Karşılaştırmalı reklam (m.8):** Aldatıcı olmamalı ve rakibin markası, logosu, ticaret unvanı gibi ayırt edici unsurlarına yer verilmemeli. Dolaylı karşılaştırma mümkün, ancak somut ve ölçülebilir veriye dayanmalı.
- **Üstünlük ifadeleri:** "En iyi", "yegâne", "1 numara" gibi ifadeler doktrinde dolaylı karşılaştırma sayılıyor ve ispat gerektiriyor. "1 numara" için özel bir düzenleme bulunamadı: **UNKNOWN**.
- **Madde numaraları:** 2026 değişikliğiyle numaralar kaymış olabilir. Konsolide metin mevzuat.gov.tr'de açılamadı: **UNKNOWN**.

### F3. Takviye edici gıda
- **SNIPPET (resmi metin özeti):** "Gıda ve Takviye Edici Gıdalarda Sağlık Beyanı Kullanımı Hakkında Yönetmelik" 2023 tarihli ([mevzuat PDF](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.40155.pdf)).
  - Sağlık beyanı yalnızca bu yönetmeliğe uygun olarak kullanılabilir.
  - Beyan belirsiz, yanlış veya yanıltıcı olamaz.
  - Başka ürünler hakkında şüphe uyandıramaz ve aşırı tüketimi teşvik edemez.
  - Hastalığı önleme, tedavi etme veya iyileştirme iddiası ürünü ilaç tanımına sokar ve yasaktır.
  - Kılavuz eklerindeki beyanlar başvurusuz kullanılabiliyor; diğer beyanlar TİTCK değerlendirmesinden geçiyor.
- **SNIPPET (resmi):** Takviye edici gıda onayı sağlık beyanlarını kapsamıyor (Onay İşlemleri Uygulama Talimatı, 14/3/2025; [TİSD kopyası](https://www.tisd.org.tr/Upload/mevzuat/611.pdf)).
- **SNIPPET (eski yönetmelik metni):** Etikette zorunlu ifadeler var: "İlaç değildir", "hastalıkların önlenmesi veya tedavi edilmesi amacıyla kullanılmaz", "normal beslenmenin yerine geçemez". Ayrıca "Takviye Edici Gıda Onay Numarası" ve işletme kayıt numarası yer almalı. Güncel metin teyit edilmeli.
- **SNIPPET (resmi):** Trendyol, görsellerde sağlık beyanını yasaklıyor (detay/242).

### F4. Kozmetik
- **SNIPPET (resmi):** Kozmetik Ürünler Yönetmeliği (RG 08.05.2023, 32184 sayılı). TİTCK'nin "Kozmetik Ürün İddialarına İlişkin Kılavuz"u 08.10.2024 tarihli olurla güncellendi ([TİTCK kılavuzlar](https://www.titck.gov.tr/duyuru/kozmetik-urunlere-iliskin-kilavuzlar-27122018173130)). Kılavuza göre:
  - iddialar gerçek ve kanıtlanabilir olmalı;
  - bileşen özelliğine atıf yapılıyorsa ürün o özelliği taşımalı;
  - "hiçbir istenmeyen etki yapmaz" türü iddialar uygun değil;
  - ürünü beşeri tıbbi ürünle karıştıracak ifadeler uygun değil;
  - "**Bakanlık/Kurum onaylıdır**" iddiası ve görseli kullanılamaz.
- **UNKNOWN:** "… içermez" (free-from) iddialarına ilişkin ayrıntılı kriterler. Kılavuzun tam metni açılamadı.

**Ürüne etkisi:**
- Uyum denetleyicinin ilk sürümü **dört kural ailesiyle** çıkabilir:
  1. Hastalık ve tedavi iddiası (takviye ve kozmetik: block).
  2. Doğrulanamayan üstünlük ifadesi ("en iyi", "1 numara", "garantili", "%100": warn, ispat isteyen).
  3. Genel yeşil iddia ("çevre dostu", "doğa dostu", "sürdürülebilir", "yeşil": açıklama yoksa warn).
  4. Fiyat ve indirim (üstü çizili fiyat son 10 günün en düşüğünden yüksekse block). Bunun için fiyat geçmişi verisi gerekir. API'den fiyat geçmişi alınamıyorsa satıcıdan beyan istenmeli.
- Görsel modülü gerçek kişi görünümlü AI insan üretmemeli. Üretirse "yapay zekâ ile oluşturulmuştur" etiketi ve tavsiye izlenimi vermeme kuralı gerekir. Varsayılan: kapalı.
- "Bakanlık onaylı" ve "TİTCK onaylı" ifadeleri kozmetikte block. Takviyede "onay numarası" geçebilir, ancak "sağlık beyanı onaylı" anlamı taşımamalı.

---

## G. Satıcı API'leri

| Yetenek | Trendyol | Hepsiburada |
| --- | --- | --- |
| Ürün oluşturma | **Var**, SNIPPET (resmi). `POST https://apigw.trendyol.com/integration/product/sellers/{sellerId}/v2/products`; istek başına en fazla 1.000 item. V1 servisleri 15 Eyl/15 Eki 2026'da kapatıldı (tarihler sayfalar arasında çelişkili) ve V1'e istek atınca 426 dönüyor. [Ürün V2 servisleri](https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-v2-api-endpoint), [Product Create v2](https://developers.trendyol.com/v2.0/docs/product-create-v2) | **Var**, SNIPPET (resmi). "Katalog Ürün Entegrasyonu": Kategori Bilgilerini Alma, Kategori Özelliklerini Alma, Özellik Değerini Alma, Ürün Bilgisi Gönderme, Hızlı Ürün Yükleme. [developers.hepsiburada.com](https://developers.hepsiburada.com/?docs=dokuman/talep-entegrasyonu) |
| Ürün güncelleme | **Var**, SNIPPET (resmi). Onaylı ve onaysız ürün için ayrı v2 servisleri. [Approved Product v2](https://developers.trendyol.com/v2.0/docs/product-update-approved-product-v2), [Onaysız ürün v2](https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-g%C3%BCncelleme-onays%C4%B1z-%C3%BCr%C3%BCn-v2). Changelog'da "content bazlı yapıya geçiş" notu var | Muhtemelen var; ayrıntısı UNKNOWN |
| Görsel yükleme | Dosya yükleme yok; **https URL** ile gönderiliyor (en fazla 8 görsel, 1200x1800). SNIPPET (resmi) | URL ile (`image1..image5`, JPG/PNG, URL erişilebilir olmalı). SNIPPET (3. taraf + hepsiexpress). Görsel sayısı üst sınırı UNKNOWN |
| Kategori ve özellik listesi | **Var** (getCategoryTree, kategori özellikleri). SNIPPET (resmi) | **Var**. SNIPPET (resmi) |
| Müşteri soruları: çekme ve cevaplama | **Var**, SNIPPET (resmi). Filtreleme servisi (tarih verilmezse son 1 hafta); `POST .../sellers/{sellerId}/questions/{id}/answers`; cevap 10–2000 karakter, yasaklı kelime kontrolü var, yalnızca `WAITING_FOR_ANSWER` durumundaki sorular cevaplanabiliyor. Rate limit: çekme 1000/dk, cevap 500/dk. v3.0 soru servisleri yayınlandı. [Cevaplama](https://developers.trendyol.com/docs/m%C3%BC%C5%9Fteri-sorular%C4%B1n%C4%B1-cevaplama), [Çekme](https://developers.trendyol.com/docs/m%C3%BC%C5%9Fteri-sorular%C4%B1n%C4%B1-%C3%A7ekme) | **Var**, SNIPPET (resmi menü). Soru Listesi, Soru Detayı, Soru Cevaplama, Sorun Bildirme, Statü Bazlı Soru Sayısı, Soruların Filtrelenmesi. Test ortamı URL'lerinde "-sit" var; canlıda kaldırılıyor. Endpoint ayrıntıları UNKNOWN |
| Ürün yorumları (reviews) | **UNKNOWN**. Resmi dokümanda yorum servisi bulunamadı. Portaldaki "Review endpoint" bağlantısı büyük olasılıkla doküman arayüzünün buton metni, bir yorum API'si değil. 3. taraf "yorum çekme modülleri" var ([faprika](https://www.faprika.com/blog/trendyol-yorum-cekme-modulu)) ama hangi servisi kullandıkları belirsiz | **UNKNOWN**. Bulunamadı |
| Kimlik doğrulama | Basic auth (supplierId, API KEY, API SECRET; panelde "Entegrasyon Bilgileri"). **User-Agent başlığı zorunlu**, entegratör adıyla. SNIPPET (resmi) | Panelde Bilgilerim > Entegrasyon > "Servis Anahtarı" (entegratör bazlı secret key). SNIPPET (resmi). Erişim onayı için Satıcı Destek talebi gerekebilir (3. taraf) |
| AI ajanları için indeks | `developers.trendyol.com/llms.txt` var (SNIPPET) | — |

**Ürüne etkisi:**
- Trendyol'da "yaz → onayla → yayınla" akışı API ile kurulabilir: ürün güncelleme v2 ve görsel için https URL. Vitrinly görselleri kendi CDN'inde **https** ile barındırmalı.
- Hepsiburada'da ürün gönderme var, ancak güncelleme ve görsel limitleri doğrulanmalı.
- Soru-cevap modülü her iki platformda teknik olarak mümkün.
- Yorum analizi için resmi API olmadığı varsayılmalı. Yorum özelliği V1 kapsamına alınmamalı.
- Entegratör olarak kayıt gerekebilir. Trendyol'da User-Agent'ta entegratör adı, Hepsiburada'da "Entegratörlerim" listesi var. Bu, **iş geliştirme açısından ilk açık konu**.

---

## H. Açık sorular ve doğrulama listesi (öncelik sırasıyla)

1. **Trendyol Akademi detay/242:** başlıkta büyük harf, emoji ve özel karakter kuralları; arka plan kuralı; kolaj kuralı.
2. **Trendyol ihlal puanı tablosu:** ihlal başına kaç puan verildiği (detay/205).
3. **Hepsiburada Akademi:** "Ürün Adı", "Ürün Açıklaması" ve "Ürün Görsel Ölçüleri" eğitimleri ile SSS. Login gerekebilir; Vitrinly'nin bir satıcı hesabıyla açılmalı.
4. **developers.hepsiburada.com:** `productName` uzunluk sınırı, görsel sayısı, güncelleme servisi, soru-cevap endpoint şeması, yorum servisinin olup olmadığı.
5. **developers.trendyol.com:** description alanında izin verilen HTML etiketleri; bir yorum servisi olup olmadığı (llms.txt üzerinden).
6. **Resmî Gazete 33297 (1.7.2026):** değişiklik metninin tamamı ve madde numaraları; konsolide yönetmelik metni.
7. **TİTCK Kozmetik İddia Kılavuzu (2024):** "içermez" iddiaları ve yasaklı ifade örnekleri.
8. **Sağlık beyanı yönetmeliği ekleri:** izinli beyan listesi (takviye için "izinli ifade" beyaz listesi kurmak üzere).

## Kaynak listesi

Bütün kaynaklar 25.10.2026 tarihinde arama sonucu ya da özeti olarak görüldü; hiçbir sayfa doğrudan açılamadı.

**Trendyol (resmi):**
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/49 (Arama Motoru)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/145 (Marka Tanımlama)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/147 (Tekil Ürün Oluştur)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/204 (Kalite Standartları)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/205 (İyi Ticaret Sistemine Uyum)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/209 (Satış Kısıtlamaları)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/241 (Satışı Uygun Olmayan Ürünler)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/242 (Ürün Listeleme Kuralları)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/243 (Müşteri Soruları Kuralları)
- https://akademi.trendyol.com/satici-bilgi-merkezi/detay/349 (Ürün Ret Sebepleri)
- https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-aktarma-v2createproducts
- https://developers.trendyol.com/v2.0/docs/product-create-v2
- https://developers.trendyol.com/docs/%C3%BCr%C3%BCn-v2-api-endpoint
- https://developers.trendyol.com/v2.0/docs/product-update-approved-product-v2
- https://developers.trendyol.com/docs/m%C3%BC%C5%9Fteri-sorular%C4%B1n%C4%B1-cevaplama
- https://developers.trendyol.com/docs/m%C3%BC%C5%9Fteri-sorular%C4%B1n%C4%B1-%C3%A7ekme
- https://developers.trendyol.com/docs/1-servis-limitleri
- https://developers.trendyol.com/changelog/changelog
- https://ads.trendyol.com/

**Hepsiburada (resmi):**
- https://www.hepsiburada.com/staticpage/64572361330497 (Sıralama algoritması)
- https://www.hepsiburada.com/satici-puanlari-nasil-hesaplaniyor
- https://www.hepsiburada.com/staticpage/672485678087016 (FSMH süreci)
- https://developers.hepsiburada.com/?docs=dokuman/talep-entegrasyonu
- https://developers.hepsiburada.com/hepsiburada/docs/entegrat%C3%B6re-servis-anahtar%C4%B1-eklemeg%C3%B6r%C3%BCnt%C3%BCleme
- https://developers.hepsiexpress.com/?docs=dokuman/entegrasyon/urun-bilgisi-gonderme
- https://akademi.hepsiburada.com/portal/course/urun-gorsel-olculeri-167928
- https://akademi.hepsiburada.com/portal/course/urun-eklerken-dikkat-edilmesi-gerekenler-urun-aciklamasi-162691
- https://akademi.hepsiburada.com/portal/faq

**Mevzuat ve kamu kurumları:**
- https://ticaret.gov.tr/haberler/ticaret-bakanligi-tarafindan-ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeliginde-yapilan-degisikliklerle-tuketicilerin-aldatici-reklam-ve-ticari-uygulamalara-karsi-korunmasi-guclendiriliyor
- https://ticaret.gov.tr/haberler/ticaret-bakanligindan-indirimli-satis-reklamlarinda-seffafligi-artiracak-yeni-duzenleme
- https://ticaret.gov.tr/haberler/aldaticici-reklam-ve-haksiz-ticari-uygulamalarla-mucadelede-yeni-donem-basliyor
- https://www.rok.org.tr/haberler/ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeligi-degisikligi/
- https://www.rok.org.tr/wp-content/uploads/2026/07/Reklam-Yonetmeligi_Temmuz-26-1.pdf
- https://tuketici.ticaret.gov.tr/data/5e819a8e13b876a1b04c7a4a/T%C4%B0CAR%C4%B0%20REKLAM%20VE%20HAKSIZ%20T%C4%B0CAR%C4%B0%20UYGULAMALAR%20Y%C3%96NETMEL%C4%B0%C4%9E%C4%B0.pdf
- https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.40155.pdf (Sağlık Beyanı Yönetmeliği)
- https://www.titck.gov.tr/duyuru/kozmetik-urunlere-iliskin-kilavuzlar-27122018173130
- https://www.tisd.org.tr/Upload/mevzuat/611.pdf (TEG Onay Talimatı 2025)

**Üçüncü taraf (yalnızca destekleyici):**
- birfatura.com, yengec.co, emstudio.tr, meayt.com, netkasam.com, idifo.com, webaction.com.tr, digitalkafalar.com, photoroom.com, kursunpartners.com, joyakademi.com, dopinger.com, faprika.com, packagist.org (Hepsiburada PHP istemcileri), sikayetvar.com
