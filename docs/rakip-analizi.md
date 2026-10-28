# Rakip analizi v1: animasyonlu / karakter anlatımlı finans-ekonomi nişi

Hazırlayan: kanal-analisti · Erişim/ölçüm tarihi: **2026-10-26** (aksi yazılmadıkça her kaynak bu tarihte okundu).
Amaç: nişin en iyi 5 kanalını ve outlier videolarını bulmak, **yalnızca desen** çıkarmak. Kopya yok (bkz. bölüm 6).

## 0. Önce okunmalı: veri erişimi ve etiketler

**Bu raporda doğrudan YouTube ölçümü yok.** Erişim denemeleri (2026-10-26):

| Host | Yöntem | Sonuç |
|---|---|---|
| www.youtube.com | curl (proxy) | **CONNECT 403** (ajan proxy'si reddetti) |
| www.youtube.com, socialblade.com | WebFetch | `getaddrinfo ENOTFOUND` (DNS engeli) |
| vidiq.com, outlierkit.com, socialcounts.org, en.wikipedia.org | WebFetch | `ENOTFOUND` |
| socialblade.com, playboard.co, piped/invidious aynaları | curl | CONNECT 403 |
| www.googleapis.com (YouTube Data API v3) | curl | Erişiliyor, ama **403 "unregistered callers"**: API anahtarı yok |
| Diğer istatistik sitelerinin curl ile denenmesi | — | Otomatik izin sınıflandırıcısı reddetti; bunun yerine WebSearch kullanıldı |

Sonuçlar:
- **"Son 20 videonun izlenmeleri" ve "kanal medyanı" hiçbir kanal için ölçülemedi.** Bu yüzden tablolarda kanal medyanı yok. Outlier skorları, kaynakta bulunan **ortalama** (veya kaynağın kendi yerel medyanı) üzerinden hesaplandı ve öyle etiketlendi.
- Tüm sayılar WebSearch'ün döndürdüğü üçüncü taraf özetlerinden (vidIQ, OutlierKit, Socialcounts, SponsorRadar vb.) geliyor. Bu sitelerin kendi veri tarihleri farklı; her satırda "veri tarihi" ayrıca yazıldı.
- Başlık, thumbnail, hook ve tempo desenleri videolar açılamadığı için **ölçülmedi**. Bunlar ajanın 2026-06 öncesi genel bilgisine dayanıyor ve **"ön bilgi"** diye etiketlendi. Kurguya girmeden önce ölçümle doğrulanmaları gerekiyor (bkz. bölüm 8).

**Etiketler:**
- **[AÖ]** arama özeti: üçüncü taraf sitenin WebSearch özetinde görünen sayı, sayfanın kendisi açılamadı.
- **[H]** hesap: [AÖ] sayılardan bizim yaptığımız aritmetik.
- **[T]** tahmin.
- **[ÖB]** ön bilgi: ajanın genel bilgisi, bu oturumda ölçülmedi.

Kaynak kodları (S1…) bölüm 9'da URL'leriyle birlikte listelendi.

**Gerekli aksiyon (Niyazi):** Google Cloud'da ücretsiz bir YouTube Data API v3 anahtarı açılırsa (kota 10.000 birim/gün; bu iş için yeterli) son 20 video, medyan ve outlier tabloları otomatik ve tarihli olarak doldurulabilir. Anahtar açmak para harcatmaz ama hesap işlemi olduğu için onaya bırakıldı.

---

## 1. Aday listesi (17 aday: 9 global, 8 TR)

Seçim ölçütleri (görevdeki sırayla): (a) son 12 ayda ortalama izlenme / abone oranı, (b) outlier sıklığı, (c) format benzerliği (animasyon + karakter/anlatıcı + finans/ekonomi + uzun video). (a) ve (b) için 12 aylık pencere ölçülemedi; mevcut en iyi vekil, kaynaktaki "ortalama izlenme / abone" oranı. Aktiflik ayrıca not edildi.

### Global

| # | Kanal | Format (kısa) | Abone [AÖ] (veri tarihi, kaynak) | Ort. izlenme/video [AÖ] | Ort./abone [H] | Aktif mi? |
|---|---|---|---|---|---|---|
| G1 | **The Infographics Show** | 2D vektör karakter animasyonu, "what if" ve hikâye; para/ekonomi konuları da var | 15,5 M (tarihsiz, S3); 16 M (tarihsiz, S1); 14,5 M (S2) | 1,1 M (S3) | 0,071 | Evet, ~9 video/hafta (S3) |
| G2 | **Economics Explained** | Ülke/makro ekonomi; animasyonlu harita + anlatıcı sesi | 2.872.808 (2026-07-18, S8); 2,87 M (S9) | ~534 K (S10'daki 38 video / 20,3 M izlenmeden [H], pencere belirsiz) | 0,19 | Evet, 0,75/hafta (S9, veri 2025-07-03) |
| G3 | **Business Casual** | Animasyonlu, anlatıcılı iş-tarihi belgeseli (Rockefeller, J.P. Morgan) | 1,1 M (S13); 1,2 M (2026-10-13, S14); 1.150.000 (S15) | 1,1 M (S13; 102,9 M / 91 video) | ~1,0 | **Hayır**: ~3 yıldır yükleme yok (S13); 91 video (S14, 2026-10-13) |
| G4 | **The Swedish Investor** | Animasyonlu yatırım kitabı özetleri | ~1,0 M (2026-07, S17); 1.020.000 (S18); 967 K (2025-05-20, S19) | Bulunamadı | — | Düşük: 0,25/hafta (S19, 2025-05-20) |
| G5 | **OverSimplified** | Karakterli, komik 2D tarih anlatımı, uzun bölümler, seri yapısı | ~9,58 M (2026-07 sonu, S21); 9,6 M (S22) | 42,6 M (S22); 1,405 Mr / 33 video = 42,6 M [H] (S21) | 4,4 | **Hayır**: son yükleme ~1 yıldan eski (S23, 2026-07-20); son kesin tarih 2024-01-19 (S24) |
| G6 | Two Cents (PBS) | Sunucu + animasyon, kişisel finans | 802 K (2025-04, S25); ~828 K (2026-09, S26) | Bulunamadı | — | **Hayır**: son bölüm 2025-04-16 (S27, tek kaynak) |
| G7 | Al Mokhbir Al Eqtisadi (Arapça) | Harita ağırlıklı ekonomi belgesel-denemesi, yüz yok | 2,45 M (2024-11, S28); 2,8 M (tarihsiz, S29) | Kaynaklar karışık, hesaplanmadı | — | Evet, 0,75/hafta (S28); ort. süre 16,81 dk (S28) |
| G8 | CGP Grey | Çöp adam, eğitim; ara sıra ekonomi | 7,04 M (tarihsiz, S30) | Bulunamadı | — | Seyrek [ÖB] |
| G9 | VisualEconomik EN | Motion graphics ekonomi | 207 K (S31) | 22 K (S31) | 0,106 | Evet, 2026-07-02'de yükleme var (S31) |

Elenen veya verisi olmayan global adaylar: How Money Works (stok görüntü + grafik; karakter yok. OutlierKit'teki 2,9 M / 837,1 K satırı Economics Explained ile karışmış görünüyor, **çelişkili, kullanılmadı**, S12), Chris Invest (beyaz tahta; sayı bulunamadı), Crash Course Economics (sunuculu, seri bitmiş [ÖB]), Principles by Ray Dalio (tek büyük animasyon [ÖB]), WhiteBoard Finance (sayı yok), "Practical Wisdom" (arama doğrulamadı).

### Türkiye

| # | Kanal | Format | Abone [AÖ] | Not |
|---|---|---|---|---|
| T1 | DFT Tarih | Hareketli harita + animasyonlu tarih anlatımı | 991 K, 266 video (2025-06-05, S32); 1,07 M (tarihsiz, S33) | Format olarak TR'deki en yakın örnek, ama finans değil, maskot yok |
| T2 | Ya Sonra? (@YaaSonra) | Senaryolu animasyon ("Zombi İstilası Part 5"), ikinci tekil anlatım; bizim stil referansımız | Bulunamadı (S34) | Kalite referansı 01 bu hesaptan (bkz. `referans-analizi.md`) |
| T3 | Özcan Show | Türk yapımı animasyon dizisi, ~8 dk bölümler (S35) | Bulunamadı | Komedi; finans değil |
| T4 | Barış Özcan | Sunuculu, hareketli grafik ağırlıklı anlatım | 6,7 M (2025-07, S36) | Animasyonlu karakter yok; konu sanat, tasarım ve teknoloji |
| T5 | EKONOMİBİZ | Günlük piyasa yorumu (dolar, altın, BIST) | 128 K (S37) | Animasyon yok |
| T6 | Nasıl Bir Ekonomi TV | Canlı yayın / sunuculu | Bulunamadı | Animasyon yok |
| T7 | Mesele Ekonomi | Sunuculu, sade dille ekonomi (2018'den beri) | Bulunamadı | Animasyon yok |
| T8 | Flu TV, "Olmaz Öyle Saçma Ekonomi" | Mizah + ekonomi analizi | Bulunamadı | Animasyon belirsiz |

**TR sonucu [AÖ + değerlendirme]:** Aramalarda **animasyonlu veya maskot anlatımlı bir Türkçe finans-ekonomi kanalı bulunamadı.** TR ekonomi kanalları sunuculu veya canlı yayın formatında; TR animasyon kanalları ise tarih, komedi veya senaryo üzerine. Bu bir **boşluk**: format kanıtı globalde, dil ve konu boşluğu TR'de. Uyarı: Bu sonuç arama motorunun kapsamıyla sınırlı. YouTube'da doğrudan "ekonomi animasyon" araması yapılamadı.

---

## 2. Seçim: en iyi 5 kanal ve gerekçe

Puanlama: format benzerliği 0–5, oran ve outlier kanıtı 0–5, aktiflik 0–5. Ağırlıklar 0,5 / 0,3 / 0,2. Puanlar ajanın değerlendirmesi, yani **[T]**.

| Kanal | Format | Oran / outlier | Aktiflik | Toplam [H] | Karar |
|---|---|---|---|---|---|
| The Infographics Show | 4 | 3 | 5 | 3,9 | **Seçildi** |
| OverSimplified | 5 | 5 | 1 | 4,2 | **Seçildi**: format referansı (finans değil) |
| Business Casual | 4 | 4 | 1 | 3,4 | **Seçildi**: "geçmişin büyük finans olayları" ayağı |
| Economics Explained | 3 | 4 | 4 | 3,5 | **Seçildi**: finans çekirdeği |
| The Swedish Investor | 4 | 3 | 2 | 3,3 | **Seçildi**: yatırım psikolojisi, kalıcı outlier |
| Al Mokhbir Al Eqtisadi | 3 | 2 | 4 | 2,9 | Yedek: İngilizce dışı dil analoğu |
| Two Cents | 3 | 1 | 0 | 1,8 | Elendi: kapandı |
| VisualEconomik EN | 2 | 2 | 4 | 2,4 | Elendi: düşük oran, karakter yok |
| DFT Tarih (TR) | 3 | 1 (veri yok) | 4 | 2,6 | Elendi ama TR biçim notu olarak tutuldu |

Gerekçe özeti:
- **The Infographics Show:** Karakterli 2D animasyonun en büyük ve en aktif örneği. "What if" ve senaryo konuları, bizim "geleceğe dair olası senaryolar" ayağıyla birebir örtüşüyor.
- **OverSimplified:** Finans değil, ama formatı bize en çok benzeyen kanal: tek anlatıcı, tutarlı karakterler, ~20 dk ve seri yapısı. Ort./abone oranı 4,4 [H] ile nişin üstünde. Pasif olduğu için desen çıkarmak için kullanılıyor, güncel trend için değil.
- **Business Casual:** Animasyonlu iş-tarihi belgeseli. Ort./abone ~1,0 [H] (pasif kanalda bile yüksek). "Kişi + imparatorluk + para" şablonu bizim tarih ayağımız.
- **Economics Explained:** Finans ve makro çekirdeği, aktif. Kaynakta outlier skoru hesaplanmış tek video bu kanalda (8,0x, S11).
- **The Swedish Investor:** Animasyonlu yatırım anlatımı. Kalıcı (evergreen) outlier örneği: Psychology of Money özeti 5,4 M.
- TR'den 5'e giren yok, çünkü animasyonlu finans kanalı bulunamadı (bölüm 1).

---

## 3. Kanal kartları

> Her kartta "son videolar ve medyan" satırı **ölçülemedi** (bölüm 0). Outlier skoru = video izlenmesi / kanal ortalaması **[H]**. Gerçek tanım medyan ister; medyan ortalamadan genelde düşük olduğundan gerçek skorlar muhtemelen **daha yüksek** [T].

### 3.1 The Infographics Show
- **Abone:** 15,5 M (S3, tarihsiz) · 16 M ve 6,9 Mr izlenme (S1, tarihsiz) · 14,5 M (S2). Kaynaklar çelişiyor, aralık 14,5–16 M [AÖ].
- **Toplam:** 6,8 Mr izlenme, ~6,2 K yükleme, ortalama 1,1 M/video (S3) [AÖ].
- **Yükleme sıklığı:** ~9 video/hafta (S3) [AÖ].
- **Süre aralığı:** ortalama 16 dk (TheTVDB dizi kaydı, S5); 2020'den bir bölüm 12 dk (S5) [AÖ]. Tahmini aralık 10–20 dk [T].
- **Son 20 video / medyan:** ölçülemedi.
- **Bilinen videolar ve outlier skoru:**

| Video | İzlenme [AÖ] | Kaynak | Outlier (ort. 1,1 M'ye göre) [H] |
|---|---|---|---|
| "What happens when you die?" | 21 M+ | S4 (blog, tarihsiz) | ~19x |
| "Why You Don't Want To Make More Than $75,000" (2019) | ~403 K | S6 | ~0,37x (para konusu, düşük) |
| "What If The US Dollar Became Worthless?" (2020) | bulunamadı | S6 | — |

- **Konu yönelimi:** son dönem "AI paniği, teknoloji şirket savaşları, yaklaşan ekonomik çöküş" (S3, yapay zekâyla üretilmiş analiz) [AÖ].
- **Üretim:** 2D vektör, sistematik, dış kaynaklı animasyon (S3). Başlık fikirleri bir araçla üretiliyor (S7, satıcı vaka çalışması) [AÖ].
- **Başlık kalıpları [ÖB]:** "What If…", "What Happens When…", "Why You Don't Want…", "X vs Y", "How X Actually…". İkinci tekil hitap ve felaket çerçevesi sık.
- **Thumbnail kalıpları [ÖB]:** 1–2 çizgi karakter, abartılı yüz ifadesi, tek merkez obje (para, bomba, harita), 0–3 kelime metin, doygun sıcak renk ile koyu arka plan karşıtlığı.
- **İlk 30 sn hook [ÖB]:** soğuk açılış: varsayım cümlesi ("Imagine…", "What if…") + hemen sponsor/konu geçişi; senaryo tek cümlede kurulur.
- **Tempo [ÖB]:** sürekli hareketli karakter sahneleri; kesme aralığı ölçülmedi. Tahmini 3–6 sn [T].
- **Karakterin rolü [ÖB]:** sabit maskot yok. Tek kullanımlık "temsilci" karakterler (sıradan adam, asker, CEO) senaryoyu canlandırır; anlatıcı ekranda görünmez.

### 3.2 Economics Explained
- **Abone:** 2.872.808, 439 video, günde ~344 abone (2026-07-18, S8) · 2,87 M ve 367,36 M izlenme (S9) · 2,86 M (2026-06, S10) [AÖ].
- **Yükleme sıklığı:** 0,75/hafta. **Ortalama süre: 20,24 dk** (S9, veri 2025-07-03) [AÖ].
- **Son dönem ortalama:** 38 video / 20,3 M izlenme (S10, pencere belirsiz) → ~534 K/video [H].
- **Son 20 video / medyan:** ölçülemedi.
- **Bilinen outlier:**

| Video | İzlenme [AÖ] | Baz [AÖ] | Outlier | Kaynak |
|---|---|---|---|---|
| "Why Everyone is Leaving New Zealand" | 3,6 M | 452 K (çevresindeki ~10 yüklemenin medyanı) | **8,0x** (kaynağın hesabı) | S11 (tek kaynak, ikinci aramada doğrulanamadı) |

- **Format:** animasyonlu haritalar + anlatıcı sesi (S12) [AÖ].
- **Başlık kalıpları [ÖB]:** "Why Everyone is Leaving X", "The Economy of X is…", "Why X is Collapsing / Booming", "The X Problem". Ülke adı + abartılı yargı.
- **Thumbnail kalıpları [ÖB]:** bayrak veya harita + tek nesne/simge, 2–4 kelime büyük metin, kırmızı ok veya grafik.
- **Hook [ÖB]:** paradoksla açılış ("X zengin görünüyor ama…"), ardından "bu videoda…" vaadi.
- **Tempo [ÖB]:** orta. Grafik, harita ve stok görüntü dönüşümlü; kesme aralığı ölçülmedi.
- **Karakterin rolü [ÖB]:** maskot yok. Ses anlatıcısı alaycı, bilmiş bir "rehber" kişiliği taşıyor.

### 3.3 Business Casual
- **Abone:** 1,1 M (S13) · 1,2 M (2026-10-13, S14) · 1.150.000 (S15) [AÖ].
- **Toplam:** 102,9 M izlenme / 91 video, ort. 1,1 M/video (S13) [AÖ]. Ort./abone ~1,0 [H].
- **Yükleme:** ~3 yıldır yok (S13); 91 video sabit (S14, 2026-10-13) [AÖ]. Kanal açılışı 2016-05 (S13) [AÖ].
- **Süre:** 8–15 dk (S16) / "10 dk altı" (eski Hollanda makalesi, S13 özeti); 40 dk'lık J.P. Morgan belgeseli (S13 özeti) [AÖ]. Kaynaklar çelişiyor.
- **En iyi performans gösteren:** "How Rockefeller Built His Trillion Dollar Oil Empire" (S13, izlenme sayısı yok) [AÖ]. Outlier skoru hesaplanamadı.
- **Kazanan şablon (S13):** "anlatıcılı, sinematik iş-tarihi belgeseli; ünlü para/güç figürü" [AÖ].
- **Başlık kalıpları [ÖB]:** "How X Built His $N Empire", "The Rise and Fall of X", "How One Man…". Kişi + büyük sayı + imparatorluk.
- **Thumbnail kalıpları [ÖB]:** çizilmiş tarihi figür portresi, para/altın objesi, 0–3 kelime, sepya/altın ton.
- **Hook [ÖB]:** dönüm noktası anıyla soğuk açılış, ardından "nasıl buraya geldi" geri dönüşü.
- **Karakterin rolü [ÖB]:** tarihi kişiler karikatür karakter olarak oynuyor; anlatıcı dışarıda.

### 3.4 The Swedish Investor
- **Abone:** ~1,0 M (2026-07, S17) · 1.020.000 (S18) · 967 K, 155 video (2025-05-20, S19) [AÖ].
- **Yükleme sıklığı:** 0,25/hafta. **Ortalama süre 58 dk** (S19). Muhtemelen uzun derleme videolar ortalamayı şişiriyor [T]. Tekil özetler 15–33 dk (S20) [AÖ].
- **Bilinen en iyi video:**

| Video | İzlenme [AÖ] | Tarih | Kaynak | Outlier |
|---|---|---|---|---|
| The Psychology of Money (Morgan Housel), "top 5 takeaways" | 5,4 M, 115.307 beğeni | 2021-02-26 | S20 (ayna sayfa) | Kanal ortalaması yok, hesaplanamadı |
| "The Psychology of Money (by Morgan Housel)" 15:35 | 4,5 M | "3 yıl önce" | S20 (toplayıcı) | Aynı video olabilir |

- **Başlık kalıpları [ÖB]:** "<Kitap adı> (by <Yazar>)", "Top 5 takeaways"; liste vaadi + otorite adı.
- **Thumbnail kalıpları [ÖB]:** kitap kapağı + basit çizgi karakter, az metin, açık zemin.
- **Hook [ÖB]:** kitabın en çarpıcı fikriyle veya kısa bir anekdotla açılış, ardından "5 ders" yol haritası.
- **Karakterin rolü [ÖB]:** basit çizgi karakter kavramları canlandırıyor (yatırımcı, piyasa, "Bay Piyasa"); anlatıcı öğretmen.

### 3.5 OverSimplified (format referansı, finans değil)
- **Abone:** ~9,58 M, günde ~1.000 artış (2026-07 sonu, S21) · 9,6 M (S22) · 9,37 M (S15 dizini, daha eski) [AÖ].
- **Toplam:** ~1,405 Mr izlenme / 33 video (S21) → ort. 42,6 M (S22 ve [H] tutarlı).
- **Süre:** son yüklemelerin ortalaması 19 dk 57 sn (S22) [AÖ].
- **Yükleme:** son kesin tarih 2024-01-19, Second Punic War Part 1 (S24). Son yükleme ~1 yıldan eski (S23, 2026-07-20) [AÖ]. Pasif.

| Video | İzlenme [AÖ] (S22) | Outlier (ort. 42,6 M'ye göre) [H] |
|---|---|---|
| WW2 (Part 1) | ~104 M | 2,4x |
| The Cold War (Part 1) | ~74 M | 1,7x |
| WW2 (Part 2) | ~67 M | 1,6x |

- **Not:** En iyi üç video da **seri bölümü** ve **Part 1'ler en yüksek** [H, n=3]. Seri açılışı merak kapısı işi görüyor.
- **Başlık kalıpları [ÖB]:** "<Olay> - OverSimplified (Part N)": tek olay adı + marka, merak sözcüğü yok. Marka güveni başlık işini yapıyor.
- **Thumbnail kalıpları [ÖB]:** 1–3 imza karakter, büyük duygusal ifade, tek tarihî obje (şapka, bayrak), metin yok veya çok az.
- **Hook [ÖB]:** komik soğuk açılış (karakter şakası), sonra "bağlam" bölümü; ilk 30 sn'de mizah + konu vaadi.
- **Tempo [ÖB]:** şaka ritmi ile hızlı kesme; sesli efekt ve kısa duraklamalarla vuruş.
- **Karakterin rolü [ÖB]:** tarihi kişiler **tekrarlayan, kişiliği abartılmış karakterler** (seri boyunca aynı tasarım). Anlatıcı ekranda değil, ama sesi bir "karakter".

---

## 4. Ortak desenler (5 kanaldan)

| Desen | Kanıt | Güç |
|---|---|---|
| **Uzun format işliyor:** 16–20 dk ortalama | EE 20,24 dk (S9), OS 19:57 (S22), Infographics 16 dk (S5), Mokhbir 16,81 dk (S28) | [AÖ], 4 kaynak; hedefimiz olan 10–20 dk'yı destekliyor |
| **Düşük sıklık + yüksek değer de işliyor:** OverSimplified 33 video, ort. 42,6 M; Business Casual 91 video, ort. 1,1 M | S21, S22, S13 | [AÖ]. Sıklığa karşı kalite: kalite tarafını destekliyor |
| **Kalıcı (evergreen) konular en büyük outlier'ları üretiyor:** ölüm (Infographics), WW2 (OS), Psychology of Money (SI), Rockefeller (BC) | S4, S22, S20, S13 | [AÖ]; güncel haber outlier'ı yalnızca 1 tane (EE NZ, S11) |
| **Konuya kişi, ülke veya varsayım çapası:** "X'in imparatorluğu", "Herkes X'ten gidiyor", "Ya X olursa" | S11, S13, S6 | [AÖ] başlıklar + [ÖB] |
| **Seri yapısı:** Part 1 > Part 2 | S22; referans 01 "Part 5" | [AÖ], n küçük |
| **Kişisel finans "cebine dokun" başlığı tek başına yetmiyor:** "$75,000" videosu kanal ortalamasının ~0,37 katı | S6, S3 | [H], tek örnek |
| **Anlatıcı ekranda yok, ses bir kişilik taşıyor** | 5/5 kanal | [ÖB] |
| **Karakter = olayın oyuncusu, anlatıcı ayrı** (EE hariç) | 4/5 | [ÖB] |
| **Thumbnail: 1–2 karakter, abartılı ifade, tek obje, 0–4 kelime** | 4/5 | [ÖB], ölçülmedi |
| **Hook: soğuk açılış (varsayım, paradoks veya dönüm anı), sonra vaat** | 5/5 | [ÖB], ölçülmedi |

---

## 5. Bizim formatla karşılaştırma (kısa)

- Bizim farkımız: **sabit maskot anlatıcı** (rakiplerin çoğunda anlatıcı görünmez) + **Türkçe** (TR'de animasyonlu finans kanalı bulunamadı) + **haber / geçmiş / gelecek** üçlüsü.
- Rakiplerin kanıtladığı şeyler: uzun animasyon izleniyor; kalıcı konu + kişi veya ülke çapası en büyük outlier'ları üretiyor; seri yapısı geri dönüş sağlıyor.

---

## 6. "Kopyalamama": her desenin özgün karşılığı

| Rakip deseni | Kopya olur (yapma) | Bizim özgün karşılığımız |
|---|---|---|
| Infographics "What if…" senaryo | "What If The Dollar Became Worthless?" çevirisi | **"Senaryo Masası"** bölümü: maskot TR'ye özgü bir varsayımı dener ("Yarın asgari ücret dolar olsa ne olur?"). Başlık "senaryo" diye işaretlenir (yatırım tavsiyesi yok kuralı). |
| Tek kullanımlık temsilci karakterler | Aynı çizgi tipleri ve "sıradan adam" tasarımı | Sabit **yan karakter kadrosu**: maskot + 2–3 TR tipi (esnaf, öğrenci, emekli), bizim çizim dilimizle (kalın kontur, cel-shading, soğuk arka plan + sıcak karakter). |
| EE "Why Everyone is Leaving X" | Aynı kalıbı TR'ye uygulamak ("Herkes Türkiye'den gidiyor") | **Veri-hikâye**: bir TR rakamının peşinden gitmek ("Bir simidin 20 yıllık fiyat yolculuğu"). Ülke yerine nesne veya şehir çapası. |
| Business Casual "How X Built His Empire" | Rockefeller, J.P. Morgan konuları | **TR ve bölge iş tarihi**: Osmanlı Bankası, Galata bankerleri, 1994 ve 2001 krizleri, yerel markaların doğuşu ve çöküşü. Maskot olay yerine "zaman yolculuğu" yapar. |
| Swedish Investor kitap özetleri | Aynı kitapların özetleri | **"Para psikolojisi deneyleri"**: maskot bir yanılgıyı kendi başına yaşar (ör. kayıptan kaçınma), kitap değil durum anlatılır. Kaynak kitaplar açıklamada atıf olarak verilir. |
| OverSimplified komik tarih + seri | Komik tarihi kişi karikatürleri ve aynı mizah ritmi | **Seri sezonları** ("Büyük Krizler, Bölüm 1–3"). Mizah maskotun kişiliğinden gelir (ör. paraya düşkün ama korkak), şaka kalıpları kopyalanmaz. |
| Görünmeyen anlatıcı | — (fark yaratıyoruz) | **Maskot ekranda anlatıcı**: dudak senkronu ve jestlerle izleyiciyle konuşan ev sahibi. İkinci tekil hitap (referans 01'deki gibi). |
| Thumbnail: karakter + tek obje + az metin | Aynı renk paleti veya kompozisyon | **İmza kompozisyon**: maskot her zaman sol 1/3'te, tek "büyük sayı" grafiği (kodla üretilir, ≤4 kelime), marka renk sistemi. 168x94 testi (kalite kapısı). |
| Soğuk açılış hook | Aynı açılış cümle kalıpları | **"Rakamla açılış"**: ilk 5 sn'de büyük sayı grafiği + maskotun tepkisi, 15 sn'de vaat, 30 sn'de ilk ters köşe. |

---

## 7. Viralite modeli için kalibrasyon önerileri

> Uyarı: Kanıt **zayıf**: medyan ölçülemedi, outlier örneği az (n≈6), çoğu [AÖ]. Bu öneriler **[T]**. YouTube API verisi ve kendi Studio verimiz gelince yeniden kalibre edilmeli. `viralite-modeli.md` değiştirilmedi; karar hakem/Niyazi'ye.

| # | Ölçüt | Şimdi | Öneri | Gerekçe (rakip outlier'ları) |
|---|---|---|---|---|
| 1 | Merak boşluğu | 0,20 | **0,20** (aynı) | En büyük outlier'lar ("What happens when you die?" ~19x [H], "Everyone is Leaving NZ" 8,0x) merak sorusu taşıyor. |
| 2 | Kanıtlı talep | 0,15 | **0,15** (aynı) + ölçüm değişikliği | Outlier tabanı "kanal ortalaması" değil, **çevredeki ~10 yüklemenin medyanı** olsun (S11 yöntemi; kanal büyümesini düzeltir). Eşik ≥3 güçlü korunur. |
| 3 | Hook gücü | 0,15 | **0,10** ↓ | Outlier'ı ambalaj (başlık + thumbnail) ve konu belirliyor; hook izlenme süresini etkiliyor ve her konuya yazılabiliyor. Senaryo puanından çıkarılıp metin aşamasında **kalite kapısı** olarak tutulsun. |
| 4 | Kişisel bağ | 0,15 | **0,15** (aynı) | Tek karşı örnek var ("$75,000" ~0,37x): "cebine dokunma" tek başına yetmiyor ama TR izleyicisi için hâlâ önemli [T]. Global veri TR'yi temsil etmiyor, o yüzden düşürülmedi. |
| 5 | Zamanlama | 0,10 | **0,05** ↓ | Bulunan 6 outlier'ın 5'i kalıcı konu (ölüm, WW2, Cold War, Psychology of Money, Rockefeller). Haber bağlantısı bonus olsun, ana sürükleyici değil. |
| 6 | Hikâye gerilimi | 0,10 | **0,15** ↑ | Kazananlar kişi/imparatorluk/savaş/çöküş anlatısı (BC "kişi + imparatorluk" şablonu, OS savaş serileri, EE "herkes gidiyor"). |
| 7 | Görselleştirilebilirlik | 0,10 | **0,10** (aynı) | Formatın temeli; ayırt edici kanıt yok. |
| 8 | Raf ömrü | 0,05 | **0,10** ↑ | En yüksek izlenmeler yıllar sonra da birikiyor (2021 SI 5,4 M; OS ort. 42,6 M / 33 video; BC 3 yıl yüklemesiz 1,1 M ort.). |
| | **Toplam** | 1,00 | **1,00** | |

Ek öneriler:
- **Seri bonusu (+0,5):** Konu Part 1/2/3 serisine bölünebiliyorsa (OS'te Part 1 en yüksek, referans 01 "Part 5").
- **"Kişi / ülke / nesne çapası" kontrolü:** Başlık somut bir özne taşımıyorsa merak boşluğu en fazla 6 puan alsın.
- **TR boşluk notu:** Animasyonlu TR finans rakibi bulunamadığından "rakibe fazla benzeyen açı −1,5" cezası pratikte global kanallara karşı uygulanır. Global başlıkların **doğrudan çevirisi** ceza almalı.

---

## 8. Sonraki ölçümler (veri erişimi açılırsa)

1. YouTube Data API v3 ile 5 kanal × son 30 video: izlenme, süre, yayın tarihi → medyan, yerel medyan outlier, 12 aylık ort./abone.
2. Her kanalın en iyi 5 videosu için thumbnail indirme → yüz/karakter sayısı, obje, kelime sayısı, baskın renk (kodla).
3. İlk 60 sn için `ffmpeg scene>0.3` ile kesme sayısı → bölüm 3'teki tempo [ÖB]/[T] satırlarını gerçek ölçümle değiştirme.
4. TR boşluğunu doğrulama: YouTube'da "ekonomi animasyon", "para tarihi animasyon" aramaları (API `search.list`).

---

## 9. Kaynaklar (hepsine 2026-10-26'da WebSearch ile erişildi; sayfaların kendisi açılamadı, değerler arama özetinden alındı)

| Kod | Kaynak | Sayfadaki veri tarihi |
|---|---|---|
| S1 | https://socialblade.com/youtube/handle/theinfographicsshow/achievements | tarihsiz |
| S2 | https://www.networthspot.com/the-infographics-show/net-worth/ | tarihsiz (2026 sayfası, eski veri olabilir) |
| S3 | https://outlierkit.com/channel/theinfographicsshow | tarihsiz |
| S4 | https://videoexplainers.com/?p=2335 | tarihsiz |
| S5 | https://www.thetvdb.com/series/infographics | tarihsiz / 2020 bölümü |
| S6 | https://socialcounts.org/youtube-video-analytics/-169Ut9JSJk | tarihsiz (video 2019) |
| S7 | https://www.spotterstudio.com/creator-stories/the-infographics-show | tarihsiz |
| S8 | https://socialcounts.org/youtube-live-subscriber-count/UCZ4AMrDcNrfy3X6nsU8-rPg | 2026-07-18 |
| S9 | https://vidiq.com/youtube-stats/channel/UCZ4AMrDcNrfy3X6nsU8-rPg | 2025-07-03 (süre/sıklık) |
| S10 | https://socialpruf.com/youtube/economicsexplained | 2026-06 |
| S11 | https://dev.to/member_2dd946e9/how-i-score-youtube-outliers-without-being-fooled-by-channel-growth-10cn | tarihsiz |
| S12 | https://outlierkit.com/resources/faceless-youtube-channels/ | 2026 (çelişkili satırlar, kullanılmadı) |
| S13 | https://outlierkit.com/channel/businesscasual | tarihsiz |
| S14 | https://www.speakrj.com/audit/report/UC_E4px0RST-qFwXLJWBav8Q/youtube | 2026-10-13 |
| S15 | https://sponsorradar.com/channels/businesscasual · https://sponsorradar.com/channels/oversimplified | tarihsiz |
| S16 | https://faceless.my/youtube/faceless-business-documentary-channels/ | tarihsiz |
| S17 | https://qoruz.com/theswedishinvestor/youtube | 2026-07 |
| S18 | https://sponsorradar.com/channels/theswedishinvestor | tarihsiz |
| S19 | https://vidiq.com/youtube-stats/channel/UCAeAB8ABXGoGMbXuYPmiu2A | 2025-05-20 |
| S20 | https://pt.sudovanilla.org/hashtag/the%20Swedish%20investor · https://wkt-1-d85j.onrender.com/wkt/watch/TJDcGv9OH4Q | tarihsiz (video 2021-02-26) |
| S21 | https://socialcounts.org/youtube-live-subscriber-count/UCNIuvl7V8zACPpTmmNIqP2A | 2026-07 sonu |
| S22 | https://outlierkit.com/channel/oversimplified | tarihsiz |
| S23 | https://creatordb.app/creatorstats/oversimplified/ | 2026-07-20 |
| S24 | https://www.thetvdb.com/series/oversimplified/episodes/10258176 | 2024-01-19 |
| S25 | https://vidiq.com/youtube-stats/channel/UCL8w_A8p8P1HWI3k6PR5Z6w | 2025-04 |
| S26 | https://creatordb.app/creatorstats/twocentspbs/ | 2026-09-25 |
| S27 | https://isitback.com/show/two-cents | tarihsiz |
| S28 | https://vidiq.com/youtube-stats/channel/UC4kRorAXuIkyIX6vwXKaLWg | 2024-11 |
| S29 | https://outlierkit.com/channel/mokhbireqtisadi | tarihsiz |
| S30 | https://en.wikipedia.org/wiki/CGP_Grey (arama özetindeki bilgi kutusu) | tarihsiz |
| S31 | https://sponsorradar.com/channels/visualeconomiken | 2026-07 (son yükleme 2026-07-02) |
| S32 | https://vidiq.com/youtube-stats/channel/UC6AdnJAlvHwlWKGC40-nVUg | 2025-06-05 |
| S33 | https://www.tamindir.com/blog/takip-edilmesi-gereken-youtube-kanallari_75664/ | tarihsiz |
| S34 | https://www.youtube.com/@YaaSonra | sayı yok |
| S35 | https://www.thetvdb.com/series/342315-show | tarihsiz |
| S36 | https://hypeauditor.com/top-youtube-science-technology-turkey/ | 2025-07 |
| S37 | https://vidiq.com/youtube-stats/channel/UCVPMnopSZp2Kl4Bx71qpXDg | tarihsiz |
| S38 | https://vidiq.com/research/youtube-upload-frequency-study/ (genel bağlam: 12+ yükleme/ay kanallarda aylık medyan izlenme büyümesi %2,18, ayda 1'den az yükleyenlerde %0,53; korelasyon) | 2026-07 |

---

## 10. Test: kontrol listesi

- [x] **5 kanal seçildi:** The Infographics Show, Economics Explained, Business Casual, The Swedish Investor, OverSimplified (+ yedek Al Mokhbir Al Eqtisadi).
- [x] **Aday listesi ≥10–15:** 17 aday (9 global, 8 TR) + elenen 6 global isim.
- [x] **Her sayının kaynağı var:** Tüm [AÖ] sayılar S1–S38 koduyla bağlandı; [H] satırlarında girdi sayıları ve kaynakları yazılı; [T] ve [ÖB] açıkça etiketli.
- [x] **Ölçüm/erişim tarihi var:** tüm kaynaklara erişim 2026-10-26. Sayfanın kendi veri tarihi bölüm 9'da; tarihsiz olanlar "tarihsiz" diye işaretlendi.
- [ ] **Son 20 video + kanal medyanı:** **YAPILAMADI.** youtube.com / socialblade.com engelli (proxy 403, DNS ENOTFOUND), YouTube Data API anahtarı yok (googleapis 403 "unregistered callers").
- [ ] **Thumbnail / hook / tempo ölçümü:** **YAPILAMADI.** Videolar açılamadı; bu satırlar [ÖB]/[T].
- [x] **Erişim engelleri yazıldı:** bölüm 0.
- [x] **Kopyalamama bölümü:** her desen için özgün karşılık (bölüm 6).
- [x] **Kalibrasyon önerileri:** ağırlık toplamı 1,00, gerekçeli (bölüm 7); model dosyası değiştirilmedi.
- [x] **Çelişkili veri işaretlendi:** Infographics abone (14,5–16 M), Business Casual süre, Swedish Investor 58 dk ortalama, OutlierKit 2,9 M / 837 K satırı (kullanılmadı), EE NZ outlier (tek kaynak).
