# Flip By Vote (@flipbyvote) — Seri İncili (Sezon 1)

> Özet: Jake Miller ve Mike Carter 100 dolarla başlar, hedef 1.000.000 dolar. Her bölüm 60–90 sn, dikey 9:16, 3D görünümlü, Amerikan İngilizcesi, iki karakter diyaloğu. Her bölüm 2–3 seçenekli bir seçim anında biter; kazanan yorum sonraki bölümün başında kullanıcı adıyla gösterilir.
> Kaynak: `docs/seri/konsept.pdf` (11 sayfa), CLAUDE.md "FORMAT DEĞİŞİKLİĞİ" (2026-11-10). Hazırlayan: senaryo-yazari, 2026-11-10.
> Bu dosya her bölüm yazarı, görsel, ses, kurgu ve uyum ajanı için **sabit kural**dır. Değişiklik yalnız koordinatör kararıyla ve tarihli not ile.

İçindekiler: 1 Karakterler · 2 Mekânlar · 3 Sezon omurgası · 4 Para defteri (BANK) · 5 Karar tasarımı · 6 Kazanan fikrin gösterimi · 7 Seçenek dışı fikirler · 8 Platform kuralları · 9 Bölüm şablonu · 10 Süreklilik dosyaları

---

## 1. Karakter kartları

Görünüş ve kıyafet her bölümde sabittir (PDF s. 4). Mevsim değişikliği yalnız eklenti (mont, bere) ile ve gorsel-varlik-sanatcisi onayıyla yapılır.

### JAKE MILLER, 26, "hesaplayan"
| Alan | Kural |
|---|---|
| Görünüş | Kısa koyu kahverengi saç, hafif sakal, kahverengi gözler. Lacivert kapüşonlu sweatshirt, bej pantolon. Cebinde kalem. |
| Ses | Orta-pes, sakin, yavaş (~150 kelime/dk hedef). Cümle sonunda perde düşer, kuru ve düz anlatım. Bağırmaz. En büyük tepkisi tek kaş kaldırmak. Aday: Kokoro `am_michael` 0.95 (kanalın ölçülmüş sakin sesi). Karar ses-yonetmeni'nde. |
| Mizah | Deadpan. Kısa, kelimesi kelimesine düzeltmeler ("Air is free." → "Tires aren't."). Abartıyı tek kelimeyle söndürür. Fiziksel komedi yapmaz, ona maruz kalır. |
| Tekrar eden laflar | "Let me run the numbers." · "Slow. But safe." · "That's a no from the spreadsheet." · İmza cümlesi (PDF'ten): **"A price tag is just a number. Value is what somebody actually pays."** Bu cümle en fazla 10 bölümde bir kullanılır. |
| Alışkanlık | Her parayı buzdolabındaki beyaz tahtaya ("THE BOARD") yazar. Düşünürken kalemi tahtaya vurur. Mike'a takılırken ona "Hype Man" der. |
| Zayıf yön | Fazla düşünür, riskten kaçar, fırsatı kaçırır. Tekrar eden şaka: "The deal's gone." |
| Büyüme yayı | Rakamlar "yeterince iyi" olduğunda hızlı davranmayı öğrenir. |

### MIKE CARTER, 27, "fırsatı gören"
| Alan | Kural |
|---|---|
| Görünüş | Dağınık kumral saç, mavi gözler. Kırmızı-siyah ekose gömlek, beyaz tişört, koyu kot. Telefonu hep elinde. |
| Ses | Daha tiz, hızlı (~170 kelime/dk hedef), parlak. Cümle sonunda perde yükselir. Cümle ortasında güler. Aday: Kokoro `am_fenrir` 1.0 (ölçülmüş daha enerjik ses) veya `am_puck`. Karar ses-yonetmeni'nde. İki ses kör testte birbirinden açıkça ayrılmalı. |
| Mizah | Coşku, abartı, nesnelere isim koyma ("Meet Brenda." = bisiklet), fiziksel komedi (tezgâha vurur, kameraya eğilir). |
| Tekrar eden laflar | **"Hear me out."** (her bölümde en fazla 1) · "Easy money." (arkasından iş hep zorlaşır) · "Trust the vibe." · İmza cümlesi (PDF'ten): **"Jake, we don't need more money. We need guts."** Bu cümle en fazla 10 bölümde bir kullanılır. |
| Alışkanlık | Jake'e takılırken ona "Spreadsheet" der. Aldığı her eşyaya isim verir. Sonuçlanmış her satışta kameraya "ding" işareti yapar. |
| Zayıf yön | Aceleci, aşırı özgüvenli, fazla öder, kontrol etmeden alır. |
| Büyüme yayı | Almadan önce kontrol etmeyi öğrenir; cesaretini kaybetmez. |

### İlişki dinamiği
- **Jake hesaplar, Mike fırsatı görür.** Komedi de çatışma da bu zıtlıktan çıkar (PDF s. 4).
- **Kimse hep haklı değildir.** Her 10 bölümlük aşamada "haklı çıkan" oranı yaklaşık yarı yarıya olur. Mesaj "temkinli olan hep kazanır" ya da "cesur olan hep kazanır" olmamalı. `sezon-takip.md`'de sayılır.
- Kavgalar paraya ve karara dairdir; kişiliğe hakaret yoktur. Her tartışma "biz" ile kapanır.
- Kural: büyük kararı ikisi tek başına vermez. "No move without a vote" = izleyici oyu. Bu, formatın hikâye içi gerekçesidir.
- Dördüncü duvar: yalnız seri tanıtımında, kazanan kartında ve son CTA'da kameraya bakarlar.

---

## 2. Tekrar eden mekânlar (en fazla 5; aynı anda en fazla 4 aktif)

Her mekân bir kez üretilir. Sabit 2–3 kamera açısı ve değişen prop katmanlarıyla tekrar kullanılır. Telefon ekranı (ilan kartı, mesaj, harita) mekân değildir, grafik katmandır.

| Kod | Mekân | Ne için | Sabit açılar | İlk kullanım |
|---|---|---|---|---|
| L1 | **THE KITCHEN (HQ)**: küçük apartman mutfağı. Tezgâh (100 dolar burada çarpılır), iki tabure, buzdolabında beyaz tahta "THE BOARD" (BANK ve hedef $1,000,000 yazılı), pencere | Açılış, kararlar, final CTA. Her bölümde kullanılabilir | A geniş tezgâh ikili çekim · B buzdolabı tahtası yakın · C tezgâh üstü insert (para, telefon) | Bölüm 1 |
| L2 | **THE CAR**: Jake'in küçük, eski hatchback'i, logosuz. İç mekân ön koltuklar + dış yan görünüş | Yolculuk, telefonda pazarlık, alıcı bekleme | A ön camdan ikili · B dış yan · C torpido insert | 1–10 arası |
| L3 | **THE DRIVEWAY**: banliyö evi önü, katlanır masalı garaj satışı. Alıcı buluşmalarında aynı sokak, prop'lar değişir | Garaj satışları, alım-satım buluşmaları | A geniş masa · B ikili + satıcı · C ürün insert | 1–10 arası |
| L4 | **THE GARAGE**: kiralık küçük garaj. Tezgâh, delikli pano, büyüyen eşya yığını (prop katmanı ilerlemeyi gösterir) | Tamir, boya, envanter | A tezgâh · B yığın geniş · C el/alet insert | Aşama 2 (11+) |
| L5 | **THE SHOP**: küçük depo. Raflar, masa, paketleme istasyonu | Şirketleşmeden sonra ana iş yeri. Açılınca L4 emekliye ayrılır | A raf koridoru · B masa · C paketleme | Aşama 4 (31+) |

Yasak: tek bölümlük yeni mekân. Gerekirse L3 sokağı ya da L1 kapı önü varyasyonu kullanılır. Yeni mekân yalnız aşama geçişinde ve koordinatör onayıyla açılır.

---

## 3. Sezon omurgası (100 bölüm, PDF s. 6'daki 10 aşama)

Hikâyede geçen süre yaklaşık 2–3 yıldır. Atlamalar ekranda zaman kartıyla gösterilir ("4 days later", "3 months later"). Gerçekçiliği bu sağlar. BANK aralıkları **tasarım hedefidir** [tahmin]. İzleyici kararlarıyla ± sapar; aşama hedefi tutmazsa omurga uyarlanır, rakam zorlanmaz.

| Bölüm | Aşama | Hikâye çekirdeği | Tipik karar türü | Gerçek hata/kayıp örneği | BANK hedef aralığı [tahmin] | Mekân |
|---|---|---|---|---|---|---|
| 01–10 | İlk 100 dolar | Garaj satışları, bisiklet, elektronik, ilk alım-satım | Hangi ürün, ne kadar pazarlık, nerede satış | Gelmeyen alıcı; parça masrafı planı aşar | $100 → $300–600 | L1 L2 L3 |
| 11–20 | Küçük ticaretten düzene | İkinci el ürünler, toplu alımlar, büyük pazarlıklar, defter düzeni | Toplu lot mu tek ürün mü, hangi platform | Lotun yarısı satılmaz; depo karmaşası | → $1.500–3.000 | +L4 |
| 21–30 | Büyük fırsatlar | Açık artırmalar, motosikletler (ruhsat/evrak), tamir, riskli kararlar | Teklif tavanı, tamir mi olduğu gibi mi | Artırmada fazla teklif; tamir bütçesi aşılır | → $5.000–10.000 | L1–L4 |
| 31–40 | İlk işletme | Depo, ilk yarı zamanlı çalışan, tedarikçi, şirket kuruluşu | Kiralama, işe alım, tedarikçi seçimi | Kira + maaş nakdi sıkıştırır | → $15.000–30.000 (şirket nakdi) | +L5, L4 kapanır |
| 41–50 | Büyük çöküş | Kötü sipariş, borç, güven sorunu (Jake–Mike gerilimi), yeniden başlama | Kurtarma yolu | Büyük stok kaybı; BANK sert düşer | ↓ $2.000–6.000 | L1 L5 |
| 51–60 | Dijital büyüme | E-ticaret, viral içerik, reklam, iadeler, operasyon | Kanal, reklam mı organik mi, iade politikası | İade dalgası; reklam boşa gider | → $20.000–50.000 | L1 L5 |
| 61–70 | Kendi markaları | Ürün geliştirme, üretim, lansman, kalite krizi | Ürün seçimi, üretici, lansman zamanı | Kalite hatası, geri çağırma maliyeti | → $60.000–150.000 (iniş çıkışlı) | L1 L5 |
| 71–80 | Rekabet | Ekip kurma, fiyat savaşı, büyük sipariş, nakit akışı | Fiyat kırmak mı, büyük siparişi almak mı | Büyük sipariş nakdi kilitler | → $150.000–300.000 (nakit dipleri görünür) | L1 L5 |
| 81–90 | Yatırım ve risk | Yatırımcı, sözleşme, sırlar, şirketi satma teklifi | Teklifi kabul/ret/pazarlık (hikâye kararı, yatırım tavsiyesi değil) | Kötü maddeli sözleşme tuzağı | → $250.000–500.000. Teklif "OFFER: $X" diye ayrı gösterilir, BANK'a eklenmez | L1 L5 |
| 91–100 | Milyon dolarlık eşik | Dağıtım anlaşması, operasyon krizi, sezon finalinde büyük karar | Finalin yönü | Operasyon krizi çözümsüz kalır | Zirve $700.000–950.000 | L1 L5 |

Sezon finali: 1 milyona ulaşmak yerine büyük fırsat + çözülmemiş kriz (PDF s. 6). Ana hedef ve karakter kimlikleri korunur, olaylar izleyici kararlarıyla değişir.

---

## 4. Para defteri kuralı (BANK)

1. **Her bölümde ekranda `BANK: $X`.** Sabit yer: üst-sol güvenli alan (platform arayüzünün altında kalmaz). Değişim animasyonu: artışta yeşil `+$X` ve "ding", azalışta kırmızı `−$X` ve "thud". THE BOARD'da da aynı rakam yazar; ikisi asla çelişmez.
2. **BANK = nakit** (cep + hesap). Elde tutulan ürün nakit değildir. İsteğe bağlı küçük "STASH" ikonları alış maliyetiyle gösterilir (2. bölümden itibaren).
3. **Gizli para yok.** Her işlem gösterilir: alış fiyatı, ek maliyetler (parça, boya, benzin, araç kirası, platform ücreti, satış vergisi), satış fiyatı. Bölüm sonu BANK = önceki BANK ± gösterilen işlemler. Kontrol: `uretim/seri/defter.csv` ve bölüm metnindeki BANK sütunu.
4. **Fiyat gerçekçiliği:** her fiyat ABD ikinci el piyasasında gerçekçi bir aralıkta olmalı. Dayanak satılmış ilanlar, perakende fiyat sayfaları ve güncel platform ücret sayfalarıdır; her fiyat için ≥2 kaynak. Kayıt yeri `uretim/seri/fiyat-referans.md`. **finans-dogrulayici her bölümü yayından önce onaylar.** Kaynaksız fiyat `[RAKAM?]` diye işaretlenir ve kullanılmaz.
5. **Abartılı kazanç yok.** Aşama 1'de tek bir alım-satımın net kârı, kaynakla gösterilmedikçe alış+masrafın yaklaşık 1 katını geçmez. Satış süresi gerçekçidir (gün–hafta), zaman kartıyla gösterilir. Karakterin tahmini ("double our money!") vaat değildir; diğer karakter hemen sorgular.
6. **Kayıp ve hata gerçek:** her 10 bölümlük aşamada kararların en az ~4'te 1'i başa baş ya da zararla biter [tasarım kuralı]. Hatalar paraya mal olur: gelmeyen alıcı, yanlış parça, düşük teklif, iade.
7. **Yatırım yok:** BANK hisse, kripto, bahis, piyango ya da benzeri araçlara asla girmez. Hikâye mal alım-satımı ve işletme üzerinedir. Vergi aşama 4'ten itibaren hikâyede "vergi payı ayırdılar" düzeyinde geçer; kişiye özel vergi bilgisi verilmez.
8. **Seçim anı BANK'a uyar:** BANK'ın karşılayamayacağı seçenek sunulmaz. Borç yalnız aşama 5'te hikâye sonucu olarak görünür; izleyiciye yüksek faizli borç seçeneği sunulmaz.

---

## 5. Karar tasarımı kuralları

1. **Her bölüm 2–3 net seçenekle biter.** Ekran etiketi en fazla 3 kelime + fiyat ("ROAD BIKE $80"). Etiket **isimdir, harf ya da numara değildir.** "Comment A or B" biçimi oylama yemi (vote baiting) sayılır, bu yüzden kullanılmaz.
2. **Eşit cazibe testi** (her seçenek için yazılı olarak doldurulur): 1 açık artı + 1 açık bedel (aloud söylenir) + farklı bir değer (hız / güvenlik / merak / emek). Tipik dağılım: Mike'ın seçeneği, Jake'in seçeneği, ikisini de geren joker. Yazar her seçeneği tek cümleyle savunamıyorsa seçenek değiştirilir.
3. **Hiçbir seçenek tehlikeli, yasa dışı ya da etik dışı değildir.** Yasak liste:
   - Para ürünleri: kumar, bahis, piyango, kripto, hisse, kredi kartı, payday kredi.
   - Ürünler: sahte ürün, karaborsa bilet, geri çağrılmış ürün, kask ve araç koltuğu gibi güvenlik ekipmanı, alkol, tütün, vape, silah, ilaç, takviye, hayvan.
   - Davranışlar: alıcıya ürünün durumu hakkında yalan, izinsiz mülke girme, çöp konteynerinden alma, gece tek başına yabancıyla buluşma, tehlikeli gösteri (stunt).
   - Kişiler ve markalar: gerçek kişiler ve gerçek markaların kötülenmesi.
   Buluşmalar gündüz ve kalabalık yerde yapılır; bu tavsiye olarak değil, karakterlerin rutini olarak gösterilir.
4. **Sonuç zarfı:** her seçeneğin gerçekçi sonucu (yön + BANK aralığı) yayından **önce** bölüm metnine yazılır ve kilitlenir. Kazanan seçenek, yorumlara bakılarak cezalandırılmaz ya da ödüllendirilmez. Güven kuralı budur (PDF s. 3: seçimin sonucu ekranda görünmeli).
5. Seçim anı bir **duygusal çatışmayla** gelir (ikisi aynı anda paraya uzanır, kapı çalar, ilan "2 dk önce" güncellenir). Kuru bir menü yeterli değildir.
6. Son replik her bölümde aynıdır: iki karakter kameraya döner, **"What should we do? Tell us in the comments."** Ardından 2–3 sn "Ep. N drops tomorrow" kartı.

---

## 6. Kazanan fikrin gösterimi

- **Pencere:** yayından sonra ~24 sa (PDF s. 3, 7). Instagram ana karar alanıdır; TikTok ve YouTube yorumları destekleyici havuzdur.
- **Seçim ölçütü (sırayla):** (1) kapı: kural 5.3'e uyar, BANK karşılar, karakterle tutarlı; (2) destek: beğeni + yanıt; (3) özgünlük ve hikâyeye katkı; (4) yazım kalitesi. Eşitlikte ilk yazan kazanır. Karar ve gerekçe `bolum-NNN/kazanan.md`'ye yazılır.
- **Ekran:** sonraki bölümün başında **3–5 sn'lik kart**, ilk aksiyon çekiminin ÜSTÜNE bindirilir. 2 sn'lik kanca bozulmaz; kart ayrı bir ölü an değildir.
  - Biçim: `@kullaniciadi decided: THE BIKE`, isteğe bağlı ≤8 kelimelik yorum alıntısı. Yalnız herkese açık kullanıcı adı yazılır; profil fotoğrafı kullanılmaz. Platform ikonu küçük gösterilir.
  - Karakterler kararı bir replikle kabul eder ("Okay. The bike it is."). Böylece izleyici kararının hikâyeyi değiştirdiğini duyar.
  - Kullanıcı adı uygunsuzsa ya da kişisel bilgi içeriyorsa kart "A viewer decided: …" olur.
- Kazanan yoruma kısa yanıt (koordinatör/sistem, Niyazi kalıcı izni): "You're in Ep. N." gibi. Ödül, hediye ya da vaat yoktur.
- Açıklamada ve bio'da şeffaflık satırı yer alır: "Comments may be shown on screen with your username."

## 7. Seçenek dışı yaratıcı fikirler

- Seçenek dışı bir fikir, §6'daki kapıdan geçer ve desteği en yüksek seçenekten belirgin biçimde fazlaysa **kazanabilir**. Kart: `@user had a better idea: …`.
- **Kısmi alım:** menüden bir seçenek kazanır, ama seçenek dışı bir fikir ayrıntı olarak eklenir ("+ @user's twist: sell the games one by one"). Bu yolla izleyiciye en fazla 1 kredi/bölüm verilir.
- Sınır: omurgayı kıran fikir (ör. 5. bölümde depo kiralamak) ertelenir. Erteleme ekranda söylenir ("Not yet, @user. Maybe later.") ve uygun aşamada geri çağrılır. Fikir sahibi kredi alır.
- Hiçbir zaman alınmayan fikirler: §5.3 yasak listesindekiler, gerçek kişiye ya da markaya alay, kişisel bilgi, cinsel ya da şiddet içerik, hukuki risk.

## 8. Platform kuralları

- **Etkileşim yemi yok** (Meta "engagement bait": oy, yorum, tepki, paylaşım ve etiketleme amaçlı açık istek dağıtımı düşürülür. [arama özeti + Meta Transparency sayfası, 2026-11-10]). Yasak: "comment X", "comment A/B", "like if", "tag a friend", "share to unlock", "Part 2 at 1,000 comments". Serbest olan tek kalıp, hikâyeye gerçekten yön veren açık uçlu soru: "What should we do? Tell us in the comments."
- **Hediye, ödül, çekiliş yok.** "Comment to win" yok. YouTube'un yarışma ve teşvik (incentivization) kuralları bu yüzden devreye girmez.
- **Yatırım tavsiyesi yok.** Karakterler çizgi film karakteridir, uzman ya da danışman değildir. İzleyiciye "you should …" para tavsiyesi vermezler. Açıklamada "Fiction. Not financial advice." satırı bulunur.
- **Yapay zekâ beyanı:** sesler ve görseller yapay zekâ ile üretilirse açıklamada "Voices are AI-generated" satırı bulunur. Platform etiketleri (IG AI info, YouTube altered/synthetic, TikTok AI-generated) için karar monetizasyon-uyum-uzmani'ndedir.
- **Özgünlük:** her bölüm yeni bir olay ve yeni bir karar içerir. Aynı sahne görseli birebir tekrar kullanılmaz (mekân aynı, kompozisyon/prop/ifade farklı). Tanıtım cümlesi her bölümde aynen tekrarlanmaz; bölüm 2'den itibaren tanıtım ≤4 sn'lik "Day N · BANK $X" kartına iner.
- Çocuklara yönelik değil (genel kitle, "made for kids" = hayır).

## 9. Bölüm şablonu (60–90 sn, ~170–200 kelime)

| Zaman | Vuruş |
|---|---|
| 0–2 sn | Aksiyon + ses efekti + ilk replik (hareket eden nesne: para, kapı, ürün) |
| 0–5 sn | (Bölüm 2+) kazanan kartı, aksiyonun üstüne bindirilir + kabul repliği |
| 5–25 sn | Kararın sonucu başlar: maliyet görünür, BANK değişir |
| 25–60 sn | Gelişme + komplikasyon (alıcı, kusur, pazarlık); en az 1 şaka / ~10 sn |
| 60–80 sn | Yeni ikilem + seçeneklerin artı/bedeli |
| son 6–8 sn | İkisi kameraya döner, seçim kartı, CTA; ardından "Ep. N drops tomorrow" |

Kural: her bölümde en az 1 BANK değişimi olur ya da değişmeme nedeni söylenir. Her karakterin imza cümlesi en fazla 1 kez geçer. Süre metin-kontrol betiğiyle ölçülür (`bolum-001/veri/metin-kontrol.py`, kopyala + parametrele). Telaffuz yasakları: charts, complicated, scenarios, truth, crashes, bold. Replikte rakam yerine yazıyla sayı.

## 10. Süreklilik dosyaları
- `uretim/seri/defter.csv`: bolum, olay, tutar, bank_sonra, fiyat_ref. Her bölümde 1+ satır.
- `uretim/seri/fiyat-referans.md`: fiyat aralığı ve kaynaklar (finans-dogrulayici).
- `uretim/seri/sezon-takip.md`: kim haklı çıktı, kullanılan imza cümleleri, açılan/kapanan hikâye ipleri, ertelenen izleyici fikirleri.
- `uretim/seri/bolum-NNN/`: `metin.md`, `veri/satirlar.py` (tek kaynak), `kazanan.md`.
