# F2 — 11 senaryo (senaryo-yazari) · 2026-10-27

**Video:** stok videosu, **sütun A** (tarihin büyük finans çöküşleri) · kanalın muhtemelen ilk herkese açık videosu · hedef slot Pazar 2026-11-01 12:00 ET (yetişmezse stok, 2026-11-08).
**Kanal:** Toonomy (@toonomy) · anlatıcı **Leo** (kurgusal çizgi maskot; uzman/danışman değil, kişiye özel tavsiye vermez, gelecek "possibility" diye sunulur).
**Girdi:** `01-arastirma/konu-havuzu.md` (A1–A17), `01-arastirma/rakip-ozet.md` (D1–D5), `docs/monetizasyon.md` §3.4 Ö1–Ö12, §5; `docs/viralite-modeli.md`; karakter kartı v2.
**Karar bu dosyada verilmez:** sıralama viralite-analisti, risk taraması finans-dogrulayici + monetizasyon-uyum-uzmani, seçim hakem. Sonda yalnız editör gözüyle ön sıralamam ve "neden kaybedebilir" notlarım var.

## 0. Etiketler, rakam kuralı, ortak kurallar

- **[FRH]** Federal Reserve History makalesi, bu çalışmada WebFetch ile okundu (2026-10-27): 1929 (`/essays/stock-market-crash-of-1929`), Büyük Buhran (`/essays/great-depression`), 1930–31 banka panikleri, 1973 petrol şoku, 1987, LTCM.
- **[PBS]** PBS Commanding Heights, "The German Hyperinflation, 1923" (okundu 2026-10-27). **[ABA]** ABA Journal, "A tale of two silver markets" (okundu 2026-10-27).
- **[KH-Ax]** konu havuzundaki kaynaklı veri (trend-avcisi, 2026-10-27). **[RÖ]** rakip-ozet ölçümü (kanal-analisti, 2026-10-27).
- **[AÖ]** arama özeti (WebSearch, 2026-10-27; kaynak sayfa açılmadı, link verildi). **[doğrulanacak]** yeni rakam, F3'te finans-dogrulayici'ye. **[T]** benim tahminim/yorumum. **[H]** kaynaklı rakamdan benim hesabım.
- **Çelişki bulundu:** Hunt gümüş zirvesi KH-A12'de 48,70 $, ABA'da 49,45 $ (18 Ocak 1980). Hook'ta "about forty-nine" kullanıldı; kesin rakamı finans-dogrulayici seçer. Rentenmark oranı PBS'te "nine zeros… one billion old Marks"; yaygın anlatımda 1 Rentenmark = 1 trilyon kâğıt mark [doğrulanacak]. Metinde hangisi doğrulanırsa o kullanılır.
- **Telaffuz kuralı (hook ve anlatım):** crash/crashes, charts, complicated, scenarios, truth, bold yok (`senaryo-kontrol.py` hook'larda grep'ler). Başlıkta "Crash" serbest (seslendirilmez, arama kelimesi).
- **Kalıp kuralları:** rakibin "Most people think… but" cümlesi aynen yok; "real reason / true origin / get wrong" başlıkta yok (medyan skor 0,55 [RÖ §4]). Pilot açılışı ("Imagine waking up… cup of coffee") ve "Welcome to…" tekrar edilmez. Hook'ta kanal adı, logo, "hi guys", abone çağrısı yok.
- **Hook süresi:** seçilen hook ≤40 kelime ≈ 15–16 sn (TTS `am_fenrir` 0,9 ≈ 144 kpm, pilot ölçümü `uretim/ses-testi/tts/rapor.md`). Rakamlar sesli okununca uzar ("twenty-two point six"); metinde rakamlı hook'lar ses-yonetmeni ölçümüyle kısaltılır.
- **Ortak yapı kuralları (her senaryo):** 0–15 sn somut kanca + vaat → 15–30 sn neden önemli + sonunda ne öğrenilecek → her ≤90 sn'de yeniden kanca (↺) → ilk büyük ödülden sonra (~4–6. dk) kısa abone cümlesi → anlatı yayı kurulum/çatışma/dönüm/sonuç (Ö4) → sonda tez cümlesi (Ö1) + uç ekran köprüsü. Hedef süre 12 dk ≈ 1.750 kelime (aralık 10,5–13,5 dk).
- **Hedef süre gerekçesi:** rakip veri 10–15 dk'da ceza göstermiyor, medyan skor 1,11 [RÖ §3]. İlk video için tutmayı korumak öncelikli. 15+ dk sonra denenir [T].

---

### S01 — The Borrowed Ninety Dollars (1929, follow the money)
- **Sütun:** A (KH-A1)
- **Açı türü:** Follow the money (mekanizma)
- **Çalışma başlığı:** The 10% Loan That Built the 1929 Crash
- **Alternatif 1:** How Borrowed Money Turned 1929 Into a Disaster
- **Alternatif 2:** 1929: Follow One Borrowed Dollar to the Bottom
- **Vaat:** 1929'un yukarı çıkışını da aşağı düşüşünü de aynı motorun (borçla hisse alma) sürdüğünü bir "borç doları"nı takip ederek göstermek.
- **Hook varyantları:**
  - H1 (soru + nesne): "In 1929, you could buy a hundred dollars of stock with just ten dollars of your own. The other ninety was a loan. Today, we follow that borrowed ninety dollars, and watch it pull the whole market down."
  - H2 (şok rakam): "From 1921 to 1929, the Dow went from 63 to 381. Three years later it was at 41. Up and down, the same engine was running: borrowed money. Let's follow it." (elendi: vaat net ama özne soyut "engine"; ilk 3 sn'de izleyicinin elinde bir nesne yok)
  - H3 (karakter anı): Leo'nun avucuna 10 $ konur, broker 100 $'lık hisse senedi yığını uzatır: "Ten dollars of mine. Ninety of someone else's. In 1929, this was normal." (elendi: sahne güçlü ama vaat yok; H1'in görseli olarak kullanılıyor)
  - **Seçilen: H1.** Test: somut özne (10 $ + borç 90 $) ✓, vaat ("follow… watch it pull the market down") ✓, ilk cümle tek başına anlaşılır ✓. H3 görsel olarak H1'in altına.
- **Hook (kelimesi kelimesine, 0–15 sn):** "In 1929, you could buy a hundred dollars of stock with just ten dollars of your own. The other ninety was a loan. Today, we follow that borrowed ninety dollars, and watch it pull the whole market down."
- **15–30 sn köprü:** Neden önemli: borçla alım bugün de var (marjin hesapları, kaldıraçlı ürünler). Sonunda: "why a 10% fall could wipe out 100% of your money in 1929, and the one rule that changed after it."
- **Yapı (12 dk, ↺ = yeniden kanca):**
  1. 0:00–1:30 Kanca + "10 $'lık hisse" mantığı (10 % peşinat [FRH]). ↺ 1:20 "So who lent the other ninety, and why were they so happy to?"
  2. 1:30–3:30 Parayı kim verdi: bankalar, brokerlar, şirketler (borç zinciri şeması). ↺ 2:50 "There was one number that made lenders feel safe. It was about to flip."
  3. 3:30–5:30 Yükseliş: Dow 63 → 381 (Ağustos 1921 → Eylül 1929) [FRH]. Fed'in 2 Şubat 1929 mektubu ve Ağustos'ta %6 iskonto [FRH]. ↺ 4:40 "Now watch what the same loan does when prices go the other way." **İlk büyük ödül** (marjin matematiği: %10 düşüş = peşinatın %100'ü [H]) → 5:20 kısa abone cümlesi.
  4. 5:30–7:30 Ters motor: marjin çağrısı → zorunlu satış → daha çok düşüş. 28 Ekim ~%13, 29 Ekim ~%12 [FRH]. ↺ 6:50 "But the market had fallen before. Why didn't it bounce back this time?"
  5. 7:30–9:30 Kasım ortası değerin yarısı [FRH], 1932'de 41,22 (zirveden −%89) [FRH]. Borç zincirinin bankalara sıçraması (S02'ye köprü bırakmadan tek cümle). ↺ 8:50 "It took 25 years to get back. And one rule changed forever."
  6. 9:30–11:00 Sonra ne değişti: marjin kuralları (1934 Securities Exchange Act ile Fed'e marjin yetkisi [doğrulanacak]). Bugün borçla yatırım verisi (FINRA marjin borcu [doğrulanacak]). Tavsiye yok, mekanizma.
  7. 11:00–12:00 Tez + Leo'nun sonucu + uç ekran köprüsü.
- **Leo'nun rolü (bu videoya özgü, Ö5):** **Borçlanan kişi.** 1929 sokağında 10 $ ile 100 $'lık hisse alır, sonra marjin çağrısı telgrafını o alır. Anlatıcı değil, olayın içindeki oyuncu.
- **Akılda kalan karakter anı:** Leo'ya telgraf gelir: "MORE MONEY BY NOON." Ceplerini ters çevirir, içinden yalnız bir düğme düşer.
- **Kendi veri grafikleri (Ö2, ≥3):**
  1. Dow 1921–1954 log ölçek, üç işaretli nokta (63 / 381,17 / 41,22 / 1954'te geri dönüş) — veri: Fed History çapaları [FRH] + aylık seri için Shiller S&P Composite (Yale, kamuya açık) [doğrulanacak].
  2. Marjin matematiği animasyonu: 10 $ peşinat + 90 $ borç; fiyat −%5, −%10, −%20'de kalan özsermaye [H, kaynak: %10 peşinat FRH].
  3. Brokers' loans 1926–1929 (borçla alım hacmi) — NBER Macrohistory Database [doğrulanacak, seri kodu F3'te].
  4. (yedek) 24–29 Ekim günlük düşüş sütunları [FRH: 13 % ve 12 %].
- **Özgün tez (Ö1):** "1929 wasn't just a story of greed. It was a loan that only worked while prices went up, and the same loan forced people to sell on the way down."
- **Bugünle bağ:** Ekim 2026 "Black Monday" korkusu [KH-A1, B1]; borçla alım bugün de var (FINRA marjin verisi, [doğrulanacak]). Tahmin yok, yalnız mekanizma karşılaştırması.
- **Görselleştirme notu:** Soğuk sepya 1929 Manhattan sokağı + sıcak ışıklı Leo. "Borç doları" kırmızı konturlu, her sahnede ekranda yaşayan tek nesne (izleyici takip eder). Marjin çağrısı = telgraf animasyonu.
- **Thumbnail fikri:** Leo bir elinde küçük 10 $, diğerinde devasa kırmızı "LOAN" etiketli para yığını; arkada düşen kırmızı çizgi. Metin: "10% DOWN" (2 kelime).
- **Shorts kancası:** "In 1929, ten dollars bought you a hundred dollars of stock. Here's how a ten percent drop took all of it." (marjin matematiği sahnesi, ~45 sn)
- **Risk notu:** Reklam: YEŞİL-SARI; intihar miti yok [monetizasyon §5]. Doğrulanabilirlik: ana iddialar FRH'de; brokers' loans serisi ve 1934 yasası [doğrulanacak]. Tavsiye riski: "borçla yatırım yapmayın" gibi kişisel tavsiye cümlesi yerine "here's what happened" dili.

### S02 — The Second Domino (1929 → 1933, mit yıkma)
- **Sütun:** A (KH-A1)
- **Açı türü:** Mit yıkma
- **Çalışma başlığı:** The 1929 Crash Was Only the First Domino
- **Alternatif 1:** Why America's Banks, Not Stocks, Made the Depression
- **Alternatif 2:** 1929 to 1933: How a Market Fall Became a Depression
- **Vaat:** "Borsa çöktü → Buhran geldi" kısa hikâyesinin eksik yarısını, yani 1930–33 banka paniklerini ve para arzının erimesini göstermek.
- **Hook varyantları:**
  - H1 (soru): "If the stock market falls, should someone with zero stocks be scared? In 1929, most Americans owned no stocks. Many still lost their savings. How?" (elendi: "many lost their savings" için sayı yok [doğrulanacak]; vaat dolaylı)
  - H2 (şok rakam): "By mid-November 1929, stocks had lost almost half their value. But the bigger damage came later, and it started at the bank down the street. Today: how America's money supply shrank by nearly 30 percent, and why."
  - H3 (karakter anı): Leo elinde banka cüzdanıyla kuyrukta, kapıya "CLOSED" levhası asılır. "December 11, 1930. This bank just closed. It was the fourth-largest bank in New York City." (elendi: güçlü sahne ama izleyici neden bu bankayı umursasın henüz bilmiyor; 3. bölümün açılışı yapıldı)
  - **Seçilen: H2.** Test: somut özne (borsa yarı değer + "the bank down the street") ✓, vaat ("how money supply shrank… and why") ✓, rakamlar FRH ✓. H1'in sorusu 15–30 sn köprüye taşındı.
- **Hook (kelimesi kelimesine, 0–15 sn):** "By mid-November 1929, stocks had lost almost half their value. But the bigger damage came later, and it started at the bank down the street. Today: how America's money supply shrank by nearly 30 percent, and why."
- **15–30 sn köprü:** "Most Americans didn't own stocks [doğrulanacak oran]. So why did the fall reach everyone?" Sonunda: "the three steps from a stock market fall to empty factories, and the one fix America added in 1933."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + kısa hikâye ("crash → Depression") ve neden eksik. ↺ 1:15 "To see the missing part, we need to leave Wall Street."
  2. 1:30–3:30 1930 sonu: banka panikleri, Caldwell iflasları, yüzlerce banka [FRH]; Bank of United States 11 Aralık 1930 [FRH]. ↺ 3:00 "A bank closing is bad. But here's what it does to money that isn't even in that bank."
  3. 3:30–5:30 Mekanizma: banka kapanınca para "yok olur" (mevduat → kredi zinciri, kesirli rezerv animasyonu). Para arzı 1930 sonbaharı–1933 kışı ~%30 düştü, fiyatlar da benzer [FRH]. **İlk büyük ödül** → 5:15 kısa abone cümlesi. ↺ 5:20 "So who was supposed to stop this?"
  4. 5:30–7:30 Fed'in rolü: Friedman & Schwartz (1963) yorumu [FRH] — "many economists argue" dili; karşı görüşler bir cümle. ↺ 7:00 "By March 1933, the whole system stopped."
  5. 7:30–9:30 Mart 1933 banka tatili, sistemin çöküşü [FRH]. İşsizlik [doğrulanacak, BLS/Lebergott]. ↺ 9:00 "Then one small promise changed bank runs forever."
  6. 9:30–11:00 Mevduat sigortası / FDIC [FRH: reform listesi; tarih ve tavan doğrulanacak]. Bugün: 2023 banka çöküşleri bu kuralın sınırını nasıl gösterdi [doğrulanacak].
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Dosyayı yeniden açan dedektif.** Panoya iplerle "Wall Street" kartını değil, "Main Street bank" kartını bağlar; her bölümde bir domino taşı ekler.
- **Akılda kalan karakter anı:** Leo banka kuyruğunda öne geldiği anda kepenk iner; elinde kalan banka cüzdanını izleyiciye çevirir: "This is a promise. Today it's just paper."
- **Kendi veri grafikleri (Ö2):**
  1. Para arzı 1929–1933 (M2 ya da Friedman–Schwartz para stoku) — NBER Macrohistory / FRED arşiv serisi [doğrulanacak seri kodu]; çapa: ~%30 düşüş [FRH].
  2. Yıllık banka askıya almaları 1921–1933 (1921–28 toplamı <1.000, zirve 1933 [FRH]); yıllık sayılar Fed Board "Banking and Monetary Statistics" (1943) [doğrulanacak].
  3. ABD TÜFE 1929–1933 deflasyonu — BLS CPI-U, FRED `CPIAUCNS` (1913'ten beri) [doğrulanacak değerler].
  4. Domino şeması: borsa düşüşü → banka paniği → kredi daralması → fiyat düşüşü → işsizlik (kendi çizimimiz).
- **Özgün tez (Ö1):** "A stock market fall hurts people who own stocks. A banking collapse hurts everyone. 1929 became the Great Depression because the second one was allowed to happen."
- **Bugünle bağ:** Mevduat sigortası neden var; bugünkü "banka güvenli mi?" sorusu. 2026 faiz artışları bağlamı tek cümle [KH-B2].
- **Görselleştirme notu:** Domino taşları videonun omurgası (her bölüm bir taş). Para "buharlaşır" metaforu: kasadaki banknotlar sis olup uçar. Soğuk mavi banka holleri, sıcak Leo.
- **Thumbnail fikri:** Leo kapanmış banka kapısının önünde, elinde banka cüzdanı; arkada devrilen dev domino üstünde "1929". Metin: "THE BANKS FELL NEXT" (4 kelime).
- **Shorts kancası:** "In 1929 most people owned zero stocks. So why did they lose everything? It wasn't Wall Street." (domino sahnesi)
- **Risk notu:** YEŞİL. Yorum tartışmalı (para politikası okulları) → "many economists argue", tek doğru gibi sunulmaz (finans-dogrulayici). Başlık doğru: "only the first domino" iddiası FRH ile tutarlı. Monetizasyon: intihar/yoksulluk sahnesi yok.

### S03 — Three Doors, One Thousand Dollars (1929, ikinci tekil oyun)
- **Sütun:** A (KH-A1)
- **Açı türü:** İkinci tekil sahne / interaktif seçim (kişisel finans)
- **Çalışma başlığı:** You Have $1,000 in 1929. Can You Keep It?
- **Alternatif 1:** Survive 1929 With $1,000: Every Choice Has a Trap
- **Alternatif 2:** Stocks, a Bank or a Shoebox: Who Survived 1929?
- **Vaat:** İzleyiciyi 1929'a 1.000 $ ile koyup üç seçeneğin (borsa, banka, ayakkabı kutusu) 1933'e kadar ne olduğunu oyun gibi yaşatmak; sonunda bugünle ters köşe.
- **Hook varyantları:**
  - H1 (ikinci tekil sahne): "It's September 1929. You have one thousand dollars. Three doors: the stock market, a bank, or a shoebox under your bed. By 1933, one door is a disaster, one is a gamble, and one is a surprise. Let's play."
  - H2 (şok rakam): "Put a thousand dollars into stocks at the 1929 top, and by 1932 you have about a hundred and eight. Put it in a bank, and you might lose access to all of it. So where do you hide it?" (elendi: iki sonucu baştan verip merakı harcıyor; "surprise" kapısı yok)
  - H3 (soru): "Where would you hide a thousand dollars in 1929?" + Leo üç kapı önünde. (elendi: kısa ve temiz ama vaat yok, özne zayıf)
  - **Seçilen: H1.** Test: somut özne (1.000 $, üç fiziksel kapı) ✓, vaat (1933'e kadar oyna, üç farklı sonuç) ✓, açık döngü 3 parçalı (hangisi felaket/kumar/sürpriz) ✓. Rakip deseni "ikinci tekil somut sahne" [RÖ D5] ile uyumlu, cümleleri bize ait.
- **Hook (kelimesi kelimesine, 0–15 sn):** "It's September 1929. You have one thousand dollars. Three doors: the stock market, a bank, or a shoebox under your bed. By 1933, one door is a disaster, one is a gamble, and one is a surprise. Let's play."
- **15–30 sn köprü:** Neden önemli: "Where do I keep my money?" her kuşağın sorusu; 1929 bu sorunun en sert sınavı. Sonunda: "which door won, why it won, and why the same door would lose today." (bugünle ters köşe vaadi = sona kadar açık döngü)
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca; 1.000 $'ın 1929'daki değeri (ortalama yıllık ücret karşılaştırması [doğrulanacak]). Üç Leo klonu üç kapıya girer. ↺ 1:20 "Door one looks like the smart choice. Everyone in 1929 thinks so."
  2. 1:30–3:30 Kapı 1 (borsa): Eylül 1929 zirve 381,17 → Kasım ortası değerin yarısı [FRH]. 1.000 $ → ~500 $ [H]. ↺ 3:00 "Half gone. But at least the bank door is safe. Right?"
  3. 3:30–5:30 Kapı 2 (banka): 1930 sonu panikler, Bank of United States [FRH]; mevduat sigortası yok. **İlk büyük ödül:** "safe" bankanın neden güvenli olmadığı. → 5:15 kısa abone cümlesi. ↺ 5:20 "And the shoebox? Everyone laughs at shoebox Leo. Wait."
  4. 5:30–7:30 Kapı 3 (ayakkabı kutusu): deflasyon; fiyatlar ~%30 düştü [FRH] → aynı 1.000 $ daha çok şey alır [H]. Ama: hırsızlık, faizsizlik, işsizlikte erime (nüans). ↺ 7:00 "So the shoebox wins? Not so fast. Let's check 1932."
  5. 7:30–9:30 Dip: Temmuz 1932 Dow 41,22 → borsa kapısı ~108 $ [H, FRH]; 1954'e kadar dönüş yok [FRH]. Banka kapısı: kapanan banka olasılığı [doğrulanacak yıllık askıya alma oranı]. Skor tablosu. ↺ 9:00 "Now the twist. Take the winning door and move it to 2026."
  6. 9:30–11:00 Ters köşe: bugün fiyatlar düşmüyor, artıyor. ABD Eylül 2026 TÜFE yıllık %3,7 [KH-B2] → ayakkabı kutusu bugün değer kaybeder [H]. 1933'ten sonra eklenen mevduat sigortası. "The right door depends on the decade." (tavsiye değil)
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Oyun sunucusu + üç klon oyuncu.** Sunucu Leo kuralları anlatır, üç küçük Leo klonu (borsa Leo, banka Leo, kutu Leo) kapılara girer. Rol: yarışma programı.
- **Akılda kalan karakter anı:** Kutu Leo herkes batarken kibirle kutusunu sallar; 2026 bölümünde kutudaki banknotlar yavaşça küçülür ve Leo'nun kibri yüzünde donar.
- **Kendi veri grafikleri (Ö2):**
  1. "Üç kapı yarışı": 1.000 $'ın üç yolu Eylül 1929–Mart 1933 (borsa: Dow çapaları [FRH] + Shiller aylık [doğrulanacak]; kutu: TÜFE ile reel değer, FRED `CPIAUCNS` [doğrulanacak]; banka: askıya alma oranı [doğrulanacak]).
  2. Nakdin satın alma gücü: 1929–33 (deflasyon) ile 2022–26 (enflasyon) yan yana — BLS CPI [doğrulanacak değerler; 2026 Eylül %3,7 KH-B2].
  3. Yıllık banka askıya almaları 1921–1933 [FRH çapaları + doğrulanacak seri].
  4. Skor tablosu (bölüm sonlarında güncellenen kendi infografiğimiz).
- **Özgün tez (Ö1):** "In 1929, the safest-looking door was the most dangerous one, and the silliest one won. The lesson isn't 'use a shoebox.' It's that safety depends on what prices are doing."
- **Bugünle bağ:** 2026 enflasyonu (%3,7) ile 1930'lar deflasyonu ters ayna; "nakit güvenli mi?" sorusu herkesin cebinde. 29 Ekim yıldönümü [KH-A1].
- **Görselleştirme notu:** Yarışma stüdyosu (sıcak sahne ışığı) ile 1929–33 sokakları (soğuk, sepya) arasında gidiş geliş = doğal görsel değişim noktaları. Üç renkli kapı (mavi borsa, yeşil banka, kahve kutu) bütün grafiklerde aynı renk kodu.
- **Thumbnail fikri:** Leo üç kapının önünde şaşkın; kapılarda "STOCKS / BANK / SHOEBOX", ayakkabı kutusu parlıyor. Metin: "$1,000 IN 1929" (3 kelime).
- **Shorts kancası:** "You have $1,000 in 1929. Pick a door. Most people picked wrong." (üç kapı seçimi + sonuç, ~55 sn) · 2. Shorts: "Why cash under the bed won in 1932, and loses today."
- **Risk notu:** YEŞİL-SARI. Kişisel finans çerçevesi → tavsiye dili riski: "you should keep cash" asla; oyun tarih simülasyonu, sonda "this isn't advice for today" yerine mekanizma cümlesi (Ö10). Banka kapısının sonucu (kaybedilen mevduat oranı) [doğrulanacak] — bulunamazsa "you might lose access" dili. Seri potansiyeli: aynı oyun 1923 / 1973 / 2008'e uyarlanabilir, ama Ö5/Ö7 nedeniyle ardışık değil [T].

### S04 — One Loaf of Bread (Weimar 1923, sayısal gerilim + kim kazandı)
- **Sütun:** A (KH-A3)
- **Açı türü:** Sayısal gerilim (bir rakamın tırmanışı)
- **Çalışma başlığı:** Weimar 1923: Who Got Rich While Money Died?
- **Alternatif 1:** One Dollar, One Trillion Marks: Germany in 1923
- **Alternatif 2:** How Germany's Money Lost Everything in One Year
- **Vaat:** Markın dolara karşı 4–5'ten 1 trilyona gidişini sayaçla yaşatmak ve kaybedenlerin yanında kazananları (borçlu sanayi devleri) göstermek.
- **Hook varyantları:**
  - H1 (şok rakam): "In 1914, one US dollar bought about four German marks. In November 1923, it bought one trillion. Most people lost everything. A few got very rich. Today: how money died, and who walked away with the pieces." (elendi: güçlü ama "lost everything" genelleme; özne ülke düzeyinde soyut)
  - H2 (karakter/nesne anı): "A German saver paid into a life insurance policy from 1903. Years of payments. When it paid out during the 1923 inflation, the money bought one loaf of bread. Today: how a country's money died, and who got rich anyway."
  - H3 (soru): "Can money just stop being money?" (elendi: vaat yok, özne yok)
  - **Seçilen: H2.** Test: somut özne (bir sigorta poliçesi → bir somun ekmek, PBS'te birebir) ✓, vaat ("how… died, and who got rich") ✓, pilot'un "cup of coffee" kancasından farklı ✓. H1'in rakamları 15–30 sn köprüde.
- **Hook (kelimesi kelimesine, 0–15 sn):** "A German saver paid into a life insurance policy from 1903. Years of payments. When it paid out during the 1923 inflation, the money bought one loaf of bread. Today: how a country's money died, and who got rich anyway."
- **15–30 sn köprü:** 1914'te 1 $ = 4–5 mark, Kasım 1923'te 1 trilyon [PBS]. Neden önemli: para bir sözdür; söz bozulunca kim öder? Sonunda: "the three groups who won, and the trick that stopped it in weeks."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + sayaç (ekranın köşesinde canlı "marks per dollar" sayacı başlar). ↺ 1:20 "To understand the counter, go back to 1914."
  2. 1:30–3:30 1914–1922: fiyatlar 1914–1919 ikiye katlandı, 1922'de beş ayda yine ikiye [PBS]; savaş borcu ve para basma. ↺ 3:00 "Then, in 1923, the counter stopped walking and started running."
  3. 3:30–5:30 1923 günlük hayat: maaş sabah 11'de, bankalar 11'de kapanıyor [PBS]; yumurta "100 million" (Thomas Mann) [PBS]. **İlk büyük ödül:** neden para basmak durmadı [doğrulanacak: Ruhr işgali + tazminat]. → 5:15 abone cümlesi. ↺ 5:20 "Now flip the camera. Somebody was smiling."
  4. 5:30–7:30 Kazananlar: Krupp, Thyssen, Stinnes gibi sanayi grupları "survived it well", ihracat kolaylaştı [PBS]; borçlular (borcunu değersiz parayla ödeyenler) [doğrulanacak]; mal sahipleri (elmas, sanat, mülk) [PBS]. Kaybedenler: tasarrufçular, emekliler. ↺ 7:00 "So how do you stop a counter running at this speed?"
  5. 7:30–9:30 Rentenmark (Kasım 1923): sıfırları silmek, toprak ve fabrika ipoteği arkası — PBS'e göre "a fiction" ama çalıştı [PBS]. Oran çelişkisi doğrulanır. ↺ 9:00 "It worked. But the people who lost their savings never got them back."
  6. 9:30–11:00 Sonuç ve bugün: tasarruf sınıfının kaybı; siyasi sonuç tek cümle (sembol yok). 2026 ABD TÜFE %3,7 [KH-B2] — "3.7 is not a trillion; the question is who pays for a promise."
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Fabrika işçisi / koşucu.** Maaşını sabah 11'de alıp dükkâna koşan, fiyatın yolda değiştiğini gören kişi. Anlatıcı değil, saatle yarışan biri.
- **Akılda kalan karakter anı:** Leo maaşıyla fabrikadan çıkar, dükkâna koşar; kapıya vardığında etiketteki sayı gözünün önünde değişir. Leo nefes nefese saate bakar.
- **Kendi veri grafikleri (Ö2):**
  1. Mark/dolar 1914–1923 log ölçek — çapalar [PBS]; aylık seri: Bresciani-Turroni / Young (1925) tabloları [doğrulanacak].
  2. "Sıfır sayacı": banknot üstündeki sıfır sayısı (1.000-billion Mark note [PBS]) → Rentenmark'la silinen sıfırlar [PBS / çelişki doğrulanacak].
  3. Kazananlar/kaybedenler bilançosu: borçlu vs tasarrufçu, 1914 borcu 1923 markıyla [H, PBS çapaları].
  4. (yedek) Fiyatların ikiye katlanma süresi 1914–1923 [PBS + doğrulanacak].
- **Özgün tez (Ö1):** "Hyperinflation doesn't destroy wealth evenly. It moves it, from people who saved money to people who owed money, in one brutal year."
- **Bugünle bağ:** 2026 enflasyon %3,7 ve Fed artırımı [KH-B2]; Kasım 1923 Rentenmark'ın 103. yılı, Pazar slotuna denk [KH-A3].
- **Görselleştirme notu:** Ekranın köşesinde video boyunca yaşayan sayaç (sayısal gerilim) — her bölümde basamak atlar. Sıcak fabrika ışığı vs soğuk gri Berlin sokağı. Nazi sembolü/görseli asla.
- **Thumbnail fikri:** Leo elinde dev bir banknot yığını ve tek bir somun ekmek; üstte "1,000,000,000,000". Metin: "ONE TRILLION MARKS" (3 kelime).
- **Shorts kancası:** "This insurance policy took twenty years of payments. In 1923 it bought one loaf of bread." (poliçe sahnesi)
- **Risk notu:** YEŞİL-SARI (KH-A3). Politik bağ (Hitler'in yükselişi) en fazla bir cümle, görsel yok. Pilot kancasıyla Ö7 metin tekrarı: hook ve köprü pilotla ortak 5-gram içermemeli (F3'te ölçülür). Rentenmark oranı çelişkisi [doğrulanacak].

### S05 — Two Price Tags (1973 oil shock, bugünle paralel)
- **Sütun:** A (KH-A2)
- **Açı türü:** Bugünle paralel
- **Çalışma başlığı:** When Oil Quadrupled: What 1973 Tells Us About Now
- **Alternatif 1:** From $2.90 to $11.65: The Oil Shock of 1973
- **Alternatif 2:** The 1973 Oil Shock and the Price You Pay Today
- **Vaat:** 1973 petrol şokunun sıradan cüzdana iki dalgada (fiyat sıçraması, sonra yerleşen enflasyon) nasıl vurduğunu ve 2026'yla hangi noktada benzeyip benzemediğini göstermek.
- **Hook varyantları:**
  - H1 (şok rakam + bugün): "In October 1973, a barrel of oil cost $2.90. By January 1974, it cost $11.65. Almost four times more. In 2026, oil went above $120. Today: what 1973 did to ordinary wallets, and what it tells us now."
  - H2 (ikinci tekil sahne): "You pull into a gas station. The sign says: sorry, no gas today. That was America in the winter of 1973." (elendi: tabela iddiası için kaynak yok [doğrulanacak]; vaat yok)
  - H3 (soru): "Why does a fight over oil far away make your groceries cost more?" (elendi: güçlü kişisel soru ama 2026 savaş bağlamını ilk saniyeye çekiyor → reklam riski)
  - **Seçilen: H1.** Test: somut özne (bir varil petrol, iki fiyat etiketi) ✓, vaat ✓, rakamlar FRH + KH ✓. Savaş kelimesi hook'ta yok (reklam dostu).
- **Hook (kelimesi kelimesine, 0–15 sn):** "In October 1973, a barrel of oil cost $2.90. By January 1974, it cost $11.65. Almost four times more. In 2026, oil went above $120. Today: what 1973 did to ordinary wallets, and what it tells us now."
- **15–30 sn köprü:** Neden önemli: petrol her fiyatın içinde (taşıma, gıda, plastik). Sonunda: "the second wave that hurt more than the first, and the three ways 2026 is different from 1973."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + iki etiket. ↺ 1:20 "To see why the price jumped so fast, go to October 19, 1973."
  2. 1:30–3:30 Ambargo: 19 Ekim 1973 OAPEC, Mart 1974'te kalktı ama fiyat kaldı [FRH]. Savaş tek cümle bağlam, görselsiz. ↺ 3:00 "The embargo ended in five months. The price never went back. Why?"
  3. 3:30–5:30 Birinci dalga: benzin, kuyruk, ısınma [doğrulanacak KH-A2 K3 HISTORY]. **İlk büyük ödül:** "oil shock = a tax nobody voted for" (para akış şeması: cüzdandan petrol ihracatçısına) [T, mekanizma]. → 5:15 abone cümlesi. ↺ 5:20 "Bad. But the second wave was worse, and it lasted ten years."
  4. 5:30–7:30 İkinci dalga: enflasyon yerleşti; toptan fiyatlar 1973 ortasında yıllık %10+ [FRH]; altın 35 $ → 1970'ler sonu 455 $ [FRH]; TÜFE 1965–1982 [doğrulanacak FRED]. ↺ 7:00 "How do you stop inflation that has moved in? Someone tried something painful."
  5. 7:30–9:30 Volcker şoku: faizlerin yükselmesi (KH-A2 K4) [doğrulanacak oranlar]; resesyon bedeli. ↺ 9:00 "So is 2026 the same movie? Here's the side-by-side."
  6. 9:30–11:00 2026 karşılaştırması: Brent Nisan zirvesi 126,41 $, 16 Ekim 109,86 $; Fed Eylül artırımı 3,75–4,00 %; TÜFE %3,7 [KH 0.3, B2]. Benzerlik ve farklar (ekonominin petrol yoğunluğu [doğrulanacak]). "Possibilities", tahmin yok.
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **İki etiketli zaman yolcusu.** Elinde iki fiyat etiketi (1973 ve 2026) taşır, iki dönem arasında kapıdan geçer; karşılaştırmayı o yapar.
- **Akılda kalan karakter anı:** Leo 1973 benzin kuyruğunda arabasını iterek ilerler, sonra bir kapıdan 2026'ya geçip aynı pompaya bakar ve iki etiketi yan yana tutar.
- **Kendi veri grafikleri (Ö2):**
  1. Petrol 1972–1974 basamağı (2,90 $ → 11,65 $ [FRH]) — aylık seri FRED `WTISPLC` [doğrulanacak].
  2. 1973 ile 2026 petrol eğrisi, şok başlangıcı = 100 endeksli — FRED `WTISPLC` + 2026 Brent kaynakları [KH-B2] [doğrulanacak 2026 aylık değerleri].
  3. ABD TÜFE yıllık 1965–1982 + Fed faizi — FRED `CPIAUCSL`, `FEDFUNDS` [doğrulanacak].
  4. (yedek) Altın 35 $ → 455 $ [FRH].
- **Özgün tez (Ö1):** "An oil shock is a tax nobody voted for. 1973 shows the second blow, inflation that settles in, hurts longer than the first."
- **Bugünle bağ:** En güçlü güncel bağ (Brent 110 $, Fed artırımı) [KH-A2, B2]; ambargonun 53. yılı.
- **Görselleştirme notu:** 1970'ler renk paleti (turuncu-kahve, film greni) vs 2026 (soğuk mavi). İki etiket her bölümde ekranda. Savaş, silah, yıkım görseli asla.
- **Thumbnail fikri:** Leo iki elinde iki fiyat etiketi ($2.90 / $11.65), arkada dev petrol varili. Metin: "4X IN 3 MONTHS" (4 kelime).
- **Shorts kancası:** "Oil went from $2.90 to $11.65 in three months. Here's the part that hurt for ten years."
- **Risk notu:** **SARI** — süren 2026 savaşı (KH-A2 hassas). Savaş yalnız bağlam cümlesi, hook/başlık/thumbnail'da yok; monetizasyon-uyum-uzmani bakmalı. Gelecek kısmı "possibility" dili. 1973 → 2026 karşılaştırması "yine olacak" gibi okunmamalı (yanıltıcı başlık riski).

### S06 — Leo's Wrong Belief (Cisco 2000, karakter içi gerilim)
- **Sütun:** A (KH-A4)
- **Açı türü:** Leo'nun kendi yanılgısı (karakter içi gerilim)
- **Çalışma başlığı:** The Best Company of the Dot-Com Era Still Fell 90%
- **Alternatif 1:** It Took Cisco 25 Years to Get Back to 2000
- **Alternatif 2:** Cisco 2000: When a Great Company Was a Terrible Bet
- **Vaat:** "Balon = saçma şirketler" inancını Leo'nun kendi yanılgısı üzerinden yıkmak: dünyanın en değerli şirketi gerçek bir işti, yine de ~%90 düştü ve 25 yıl bekledi.
- **Hook varyantları:**
  - H1 (Leo'nun yanılgısı): "I used to think the dot-com bubble was about silly companies. I was wrong. In March 2000, the world's most valuable company was a real business. Its stock fell about ninety percent. Here's why it took 25 years to recover."
  - H2 (şok rakam): "Cisco built the machines that ran the internet. In March 2000, it was briefly the most valuable company in the world. Then its stock fell about 90 percent." (elendi: iyi ama şirket adı ilk saniyede genç izleyiciye tanıdık değil [T]; karakter yok)
  - H3 (soru): "Can a great company be a bad investment?" (elendi: tavsiye diline yakın, vaat yok)
  - **Seçilen: H1.** Test: somut özne ("the world's most valuable company" + ~%90) ✓, vaat ("why it took 25 years") ✓, Leo'nun yanılgısı rakip özetindeki "I used to believe…" özgün karşılığı [RÖ §6] ✓.
- **Hook (kelimesi kelimesine, 0–15 sn):** "I used to think the dot-com bubble was about silly companies. I was wrong. In March 2000, the world's most valuable company was a real business. Its stock fell about ninety percent. Here's why it took 25 years to recover."
- **15–30 sn köprü:** Neden önemli: "good company = good stock" en yaygın düşünce hatası [T]. Sonunda: "the one number that separates a great business from a great price, and why it matters in every boom."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + Leo'nun yapışkan notu "GOOD COMPANY = GOOD STOCK". ↺ 1:20 "Let me show you the company first. You'll like it."
  2. 1:30–3:30 Cisco ne yapıyordu (internet yönlendiricileri), büyüme. 27 Mart 2000 zirve, ~550–620 milyar $ değer (kaynaklara göre değişiyor) [AÖ]. ↺ 3:00 "Real products, real profits. So what could go wrong?"
  3. 3:30–5:30 Fiyat ile kâr arasındaki makas (F/K mantığı, pizza dilimi metaforu) [doğrulanacak 2000 F/K]. **İlk büyük ödül:** fiyat geleceğin kaç yılını peşin ödüyordu. → 5:15 abone cümlesi. ↺ 5:20 "Then the future arrived. Just slower than the price said."
  4. 5:30–7:30 Düşüş: Nasdaq 10 Mart 2000 5.048 → Ekim 2002 ~−%78 [KH-A4]; Cisco 8 Ekim 2002 8,12 $ [AÖ]. Şirket batmadı, büyümeye devam etti [doğrulanacak gelir verisi]. ↺ 7:00 "Here's the strangest part: the business kept growing, and the stock kept waiting."
  5. 7:30–9:30 25 yıllık bekleyiş: Aralık 2025 kapanış 80,25 $ > 80,06 $ (2000 zirvesi) [AÖ: sherwood.news]; enflasyona göre hâlâ altında [AÖ]. ↺ 9:00 "So was I completely wrong? Partly. Here's what I believe now."
  6. 9:30–11:00 Bugün: AI dönemi tartışması (CoreWeave, Ekim 2026) [KH-A4, B1] — tek şirket hakkında tahmin yok; "the question to ask in any boom" çerçevesi.
  7. 11:00–12:00 Tez + Leo notu yırtıp yenisini yazar + uç ekran.
- **Leo'nun rolü (Ö5):** **Yanılan inanan.** 2000'deki "heyecanlı Leo" ile 2026'daki "düşünen Leo" konuşur; videonun gerilimi Leo'nun kendi fikrinin çökmesi.
- **Akılda kalan karakter anı:** Leo monitörüne yapıştırdığı "GOOD COMPANY = GOOD STOCK" notunu yırtar, yerine "GOOD COMPANY + GOOD PRICE" yazar.
- **Kendi veri grafikleri (Ö2):**
  1. Cisco hisse 2000–2025 (zirve → 2002 dibi → 2025 geri dönüş) — çapalar [AÖ]; seri: şirket/borsa kamu verisi [doğrulanacak lisans].
  2. Nasdaq Composite 1995–2015 — FRED `NASDAQCOM` [doğrulanacak; çapalar KH-A4].
  3. Cisco gelir/kâr ile hisse fiyatı ayrışması 2000–2025 — şirket 10-K raporları (SEC EDGAR) [doğrulanacak].
- **Özgün tez (Ö1):** "A bubble isn't only silly companies going to zero. It's great companies priced as if the future arrives tomorrow."
- **Bugünle bağ:** AI balonu tartışması nişin en sıcak sorusu [KH-A4, B1, RÖ D2]. Yalnız soru sorulur, tahmin yok.
- **Görselleştirme notu:** İki Leo (2000: gözlerinde dolar işareti, renkli 90'lar arka planı; 2026: sakin, soğuk mavi oda) ayna sahneleri. Fiyat-kâr makası iki ayrı balon olarak çizilir.
- **Thumbnail fikri:** Leo yırtılmış yapışkan notla; arkada kırmızı −90% düşüşü ve yeşil uzun düz çizgi. Metin: "25 YEARS TO RECOVER" (3 kelime).
- **Shorts kancası:** "The most valuable company on Earth in 2000 wasn't a joke. It still fell 90%."
- **Risk notu:** YEŞİL. **Viralite riski:** `benzer_aci` (Infographics "AI vs dot-com" [KH-A4]) — başlıkta AI yok, açı tek şirket + Leo yanılgısı, yine de analist değerlendirir. Cisco gerçek şirket: karalama yok, yalnız kamuya açık fiyat; bugünkü şirketler için "batacak" denmez (finans-dogrulayici). Cisco rakamları [AÖ] → F3'te birincil kaynak şart. "Terrible bet" alternatif başlığı tavsiye çağrışımı yapabilir; elenebilir.

### S07 — Six Hours in October (Black Monday 1987, saat saat gerilim)
- **Sütun:** A (KH-A14)
- **Açı türü:** Saat saat gerilim + ters köşe sonuç
- **Çalışma başlığı:** The Day Stocks Fell 22.6%, and Why Nothing Broke
- **Alternatif 1:** Black Monday 1987: The Worst Day in Stock Market History
- **Alternatif 2:** October 19, 1987: The Day Every Market Fell at Once
- **Vaat:** Tarihin en büyük günlük düşüşünü saat saat yaşatıp asıl sürprizi açmak: neden 1929 gibi bir felakete dönmedi, ve paniği durduran tek cümle.
- **Hook varyantları:**
  - H1 (şok rakam + ters köşe): "On October 19, 1987, the US stock market fell 22.6 percent. In one day. Worse than any single day in 1929. And yet, no depression followed. Today: the hour-by-hour story, and the one sentence that calmed the panic."
  - H2 (ikinci tekil sahne): "It's Monday morning, October 19, 1987. You're on the floor of the New York Stock Exchange. By lunch, the whole room is shouting." (elendi: sahne iyi ama rakam ve vaat yok; ilk sahne olarak 0:30'da kullanılır)
  - H3 (soru): "Can a stock market lose a fifth of its value in a day, and the economy just shrug?" (elendi: "shrug" deyim; rakam yuvarlak; vaat zayıf)
  - **Seçilen: H1.** Test: somut özne (bir gün, %22,6, 1929'la kıyas) ✓, iki açık döngü (saat saat hikâye + "one sentence") ✓, rakam FRH ✓.
- **Hook (kelimesi kelimesine, 0–15 sn):** "On October 19, 1987, the US stock market fell 22.6 percent. In one day. Worse than any single day in 1929. And yet, no depression followed. Today: the hour-by-hour story, and the one sentence that calmed the panic."
- **15–30 sn köprü:** Neden önemli: "Ekim 2026'da yine Black Monday konuşuluyor" [KH-A14]; büyük düşüşten sonra ne olduğunu düşüşün kendisi değil tepki belirler. Sonunda: "why the biggest fall did the least damage."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + ikinci tekil borsa salonu sahnesi. ↺ 1:20 "To understand Monday, start on Friday."
  2. 1:30–3:30 Öncesi: Ağustos 1987'ye 7 ayda +%44 [FRH]; 14 Ekim kayıplar, 16 Ekim Cuma −%4,6 (rekor puan) [FRH]; 17 Ekim Baker'ın dolar açıklaması [FRH]. ↺ 3:00 "Then came the weekend, and a new kind of selling machine."
  3. 3:30–5:30 Pazartesi saat saat: portföy sigortası ve programlı satış zinciri (makineler birbirini tetikler) [KH-A14; saatlik veri doğrulanacak]. Kapanış −508 puan, −%22,6 [FRH]. Yeni Zelanda −%60 [FRH]. **İlk büyük ödül:** zincirleme satış mekanizması. → 5:15 abone cümlesi. ↺ 5:20 "Tuesday morning, the system almost froze. Here's why."
  4. 5:30–7:30 Salı: takas uyumsuzluğu (hisse 3 gün, opsiyon 1 gün → nakit sıkışması) [FRH]. ↺ 7:00 "Then, before the market opened, one sentence came out."
  5. 7:30–9:30 20 Ekim: Fed'in "readiness to serve as a source of liquidity" açıklaması [FRH, tam metin doğrulanacak]; New York'un 10 büyük bankası menkul kıymet firmalarına kredisini neredeyse ikiye katladı [FRH]. İki seansta kaybın %57'si geri [FRH]. ↺ 9:00 "So why did 1929 take 25 years, and 1987 less than two?"
  6. 9:30–11:00 1987 vs 1929: mevduat kaçışı yok (Kohn 2006) [FRH], <2 yılda yeni zirve vs 1954 [FRH]. Devre kesiciler %7/13/20 [FRH] — bugün aynı gün ne olurdu (possibility).
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Borsa salonundan canlı yayın yapan radyo muhabiri.** Kulaklık, mikrofon, saat damgalı "live" bantlar; olayı içeriden anlık aktarır.
- **Akılda kalan karakter anı:** Leo kâğıt yağmuru altında mikrofonu tutarken arkasındaki tabela durmadan kırmızı akar; sonra Salı sabahı sessiz salonda tek bir kâğıdı (Fed açıklaması) yüksek sesle okur.
- **Kendi veri grafikleri (Ö2):**
  1. En kötü günler sıralaması: 19 Ekim 1987 −%22,6, 28 Ekim 1929 ~−%13, 29 Ekim 1929 ~−%12 [FRH] + 16 Mart 2020 [doğrulanacak].
  2. Ülke ülke düşüş haritası (Yeni Zelanda −%60 [FRH]; diğerleri [doğrulanacak]).
  3. Toparlanma süresi: 1929 (1954'e kadar) vs 1987 (<2 yıl) [FRH] — iki yatay çubuk.
  4. (yedek) Ekim 1987 günlük Dow, 14–23 Ekim [FRH çapaları + doğrulanacak seri].
- **Özgün tez (Ö1):** "The scariest fall in market history did the least damage, because this time someone promised to lend within a day. How big a fall is matters less than what happens next."
- **Bugünle bağ:** Ekim 2026 "Black Monday fears" haberleri [KH-B1 K1]; devre kesiciler bugün var [FRH]. 39. yıldönümü yeni geçti.
- **Görselleştirme notu:** Ekranın üstünde akan saat damgası (09:30 … 16:00) = saat saat gerilim. 1980'ler borsa salonu (kâğıt, telefon, CRT ekran), soğuk yeşil-mavi ekran ışığı vs sıcak Leo.
- **Thumbnail fikri:** Leo mikrofonla şok içinde, arkasında dev kırmızı "−22.6%". Metin: "ONE DAY" (2 kelime).
- **Shorts kancası:** "In 1987, the stock market lost 22.6% in one day. Then one sentence stopped the panic."
- **Risk notu:** YEŞİL. Saatlik veri bulunamazsa "hour by hour" vaadi "moment by moment / day by day" olur (yanıltıcı başlık riski yok çünkü başlıkta saat yok). Kanıtlı talep orta (alaka medyanı 68 K, 12 ayın en iyisi 47 K [KH-A14]).

### S08 — The Silver Heist (Hunt brothers 1980, kahraman/kötü adam)
- **Sütun:** A (KH-A12)
- **Açı türü:** Kahraman/kötü adam (soygun filmi yapısı)
- **Çalışma başlığı:** The Brothers Who Tried to Buy All the World's Silver
- **Alternatif 1:** How Two Billionaires Cornered Silver, and Lost It
- **Alternatif 2:** Silver Thursday: The Day the Hunt Brothers Fell
- **Vaat:** İki Teksaslı kardeşin gümüşü "satın alıp" fiyatı kontrol etme planını soygun filmi gibi anlatmak: plan, ekip, kural değişikliği, çöküş.
- **Hook varyantları:**
  - H1 (şok rakam): "In January 1979, silver cost six dollars an ounce. A year later, it hit about forty-nine. Behind that jump: two Texas brothers who controlled, by one count, more than two-thirds of the world's silver. Then they lost it. Here's how."
  - H2 (karakter anı): Leo bir kasaya gümüş külçe taşır, zemin çatırdar: "What if you bought so much silver that you became the price?" (elendi: vaat net değil, özne "you")
  - H3 (soru): "Can you buy so much of something that you own its price?" (elendi: soyut, rakam yok)
  - **Seçilen: H1.** Test: somut özne (iki Teksaslı kardeş, gümüş, 6 $ → ~49 $) ✓, vaat ("then they lost it, here's how") ✓, rakam ABA ✓ (zirve çelişkisi "about" ile yumuşatıldı).
- **Hook (kelimesi kelimesine, 0–15 sn):** "In January 1979, silver cost six dollars an ounce. A year later, it hit about forty-nine. Behind that jump: two Texas brothers who controlled, by one count, more than two-thirds of the world's silver. Then they lost it. Here's how."
- **15–30 sn köprü:** Neden önemli: altın 2026'da rekordan ~%22 düştü [KH-B3]; "zirveden düşüş" emtianın kalıcı dersi. Sonunda: "the rule change that ended the plan in one week, and why borrowing against a rising price is a trap that closes from both sides."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + "The Plan" başlık kartı (soygun filmi bölüm kartları). ↺ 1:20 "Every heist starts with a reason. Theirs was 1973."
  2. 1:30–3:30 1973'ten itibaren gümüş ve soya biriktirme [ABA]; neden gümüş (enflasyon korkusu, 1970'ler [FRH 1973 bağlantısı]). ↺ 3:00 "Buying was the easy part. Here's the clever part."
  3. 3:30–5:30 Kaldıraç: yükselen gümüşü teminat gösterip borçlanma → daha çok alım [ABA]. 1979'da 6 $ → 32 $ [ABA]. **İlk büyük ödül:** kendini besleyen döngü şeması. → 5:15 abone cümlesi. ↺ 5:20 "Then the referee walked onto the field."
  4. 5:30–7:30 18 Ocak 1980 zirve (49,45 $ ABA / 48,70 $ KH — doğrulanacak), %69+ kontrol [ABA]; 21 Ocak borsanın alım kuralları "in effect required the Hunts to sell" [ABA]. ↺ 7:00 "When the price turned, the clever part turned too."
  5. 7:30–9:30 Marjin çağrıları, 27 Mart 1980 Silver Thursday, 10,80 $ [ABA]; iflasa giden yol [ABA]. Sonrası (dava/ceza) [doğrulanacak]. ↺ 9:00 "Could anyone pull this off today? And look at gold."
  6. 9:30–11:00 Bugün: emtia pozisyon limitleri [doğrulanacak]; altın 29 Ocak 2026 rekoru 5.318 $ → 5 Ekim 4.157 $ [KH-B3]. Tahmin yok, "same trap, different metal" mekanizma karşılaştırması.
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Soygun filminin anlatıcısı ve "plan tahtası" ustası.** Tebeşir tahtasında planı çizer, her bölüm kartını o açar; kardeşleri canlandırmaz (gerçek kişi; siluet).
- **Akılda kalan karakter anı:** Leo tahtadaki planın üstüne "RULE CHANGE" yazılı kırmızı bir kâğıt yapıştırıldığını görür, tebeşiri yavaşça bırakır: "That's not in the plan."
- **Kendi veri grafikleri (Ö2):**
  1. Gümüş 1979–1980 (6 $ → 32 $ → ~49 $ → 10,80 $) [ABA]; günlük seri LBMA/COMEX [doğrulanacak].
  2. Dünya gümüş arzında kontrol payı pastası (%69+) [ABA].
  3. Kaldıraç döngüsü şeması (fiyat ↑ → teminat ↑ → borç ↑ → alım ↑; ters yönde marjin çağrısı) [ABA mekanizması, kendi çizimimiz].
  4. 1980 gümüş ile 2026 altın, zirve = 100 endeksli [ABA + KH-B3].
- **Özgün tez (Ö1):** "The Hunts didn't lose because silver fell. Silver fell because they had borrowed against it, and a rising price you borrow against can turn on you overnight."
- **Bugünle bağ:** Altının 2026 rekorundan %22 düşüşü [KH-B3]; YouTube'da konu yeni yükseliyor (312 K, 2026-07) [KH-A12].
- **Görselleştirme notu:** Soygun filmi grameri: bölüm kartları ("THE PLAN / THE CREW / THE TWIST / THE FALL"), tebeşir tahtası, parlayan gümüş külçeler (soğuk metalik) vs sıcak Leo. Gerçek kişiler siluet veya karikatürsüz temsili figür.
- **Thumbnail fikri:** Leo gümüş külçe dağının tepesinde, külçeler kayıyor; arkada 6 → 49 grafiği. Metin: "THEY BOUGHT ALL THE SILVER" (5 kelime → kısaltma: "ALL THE SILVER", 3 kelime).
- **Shorts kancası:** "Two brothers bought more than two-thirds of the world's silver. Then the rules changed in one day."
- **Risk notu:** YEŞİL. Gerçek kişiler (vefat etmiş): yalnız belgeli olaylar, "villain" kelimesi kullanılmaz, karalama yok; mahkeme/ceza bilgisi [doğrulanacak]. Zirve rakamı çelişkisi. Kanıtlı talep düşük-orta (Wikipedia 126/gün, alaka medyanı 3 K, ama 12 ayda 312 K'lık video [KH-A12]).

### S09 — Rewind the Weekend (Lehman 2008, karşı-olgusal "ya olsaydı")
- **Sütun:** A (KH-A17)
- **Açı türü:** Karşı-olgusal tarih ("ya öyle olsaydı")
- **Çalışma başlığı:** What If Lehman Brothers Had Been Saved in 2008?
- **Alternatif 1:** The Weekend Lehman Died: Three Ways It Could've Gone
- **Alternatif 2:** Lehman 2008: One Failed Rescue That Changed the World
- **Vaat:** Lehman'ın son hafta sonunu üç farklı kararla yeniden oynatıp her birinin olası sonucunu kaynaklı tartışmalarla göstermek.
- **Hook varyantları:**
  - H1 (karar anı): "In September 2008, over one weekend, the talks to save Lehman Brothers failed. On Monday, it filed for bankruptcy. Today, we replay that weekend three times, with three different choices, to see what might have changed."
  - H2 (şok rakam): "Lehman Brothers borrowed about thirty dollars for every dollar it had." (elendi: 30:1 [doğrulanacak]; vaat yok)
  - H3 (ikinci tekil): "It's Sunday night. You have to decide: save a bank with public money, or let it fall." (elendi: izleyiciyi gerçek yetkililerin yerine koyuyor, yanlış atıf riski; vaat yok)
  - **Seçilen: H1.** Test: somut özne (Lehman, hafta sonu, iflas) ✓, vaat ("replay three times") ✓, dil "might have" (senaryo/possibility kuralı) ✓.
- **Hook (kelimesi kelimesine, 0–15 sn):** "In September 2008, over one weekend, the talks to save Lehman Brothers failed. On Monday, it filed for bankruptcy. Today, we replay that weekend three times, with three different choices, to see what might have changed."
- **15–30 sn köprü:** Neden önemli: "too big to fail" tartışması her krizde geri gelir; özel kredi için "yeni 2008 mi?" soruları [KH-A17, AÖ]. Sonunda: "which choice economists still argue about, and what the 'yes' would have cost."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + gerçek zaman çizelgesi (15 Eylül 2008 iflas [KH-A17]). ↺ 1:20 "Before we rewind, you need to know why one bank mattered so much."
  2. 1:30–3:30 Konut balonu, kaldıraç (30:1 [doğrulanacak]), bağlantılar [KH-A17 K1, K2]. ↺ 3:00 "Now, the weekend. Here's what actually happened."
  3. 3:30–5:30 Gerçek hafta sonu: alıcı arayışı ve çöküşü [doğrulanacak: Barclays/BoA ayrıntıları]; Pazartesi iflas, sonraki günlerde piyasa stresi [doğrulanacak]. **İlk büyük ödül:** neden kurtarılmadı (yetki/teminat tartışması [doğrulanacak]). → 5:15 abone cümlesi. ↺ 5:20 "Rewind one: a buyer says yes."
  4. 5:30–7:30 Geri sarma 1: özel alıcı (ne değişirdi, ne değişmezdi — konut kayıpları yine var) [T, kaynaklı ekonomist görüşleri doğrulanacak]. ↺ 7:00 "Rewind two: the government pays."
  5. 7:30–9:30 Geri sarma 2: kamu kurtarması (ahlaki tehlike, bedel) — "possibility" dili. ↺ 9:00 "Rewind three: nobody helps anyone. Not just Lehman."
  6. 9:30–11:00 Geri sarma 3: hiç müdahale yok (1930'larla köprü, S02 mekanizması tek cümle) + gerçekte ne yapıldı (sonraki kurtarmalar [doğrulanacak]). Bugün: özel kredi sorusu, tahminsiz.
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Film yönetmeni / geri sarma kumandası.** Bir montaj odasında kumandayla hafta sonunu geri sarar, her seferinde farklı bir "take" çeker.
- **Akılda kalan karakter anı:** Leo geri sarma tuşuna basınca karton kutularla binadan çıkan çalışanlar geri yürüyerek binaya girer (temsili, tanınmaz figürler).
- **Kendi veri grafikleri (Ö2):**
  1. Case-Shiller ABD ev fiyat endeksi 2000–2012 — FRED `CSUSHPINSA` [doğrulanacak].
  2. Bankalar arası stres göstergesi (TED spread) Eylül–Ekim 2008 — FRED `TEDRATE` (arşiv) [doğrulanacak].
  3. ABD işsizlik oranı 2007–2010 — FRED `UNRATE` [doğrulanacak].
  4. (yedek) Lehman kaldıraç oranı vs geleneksel banka [doğrulanacak].
- **Özgün tez (Ö1):** "Saving Lehman might have softened one week, but not the losses underneath. The real choice that weekend wasn't 'crisis or no crisis.' It was who would pay for it."
- **Bugünle bağ:** Özel kredi endişesi "yeni 2008 mi?" [KH-A17, AÖ]; kurtarma tartışması her krizde.
- **Görselleştirme notu:** Montaj odası (sıcak lamba, film şeritleri) vs 2008 New York (soğuk cam kuleler). Her "take" ayrı renk filtresi (take 1 mavi, take 2 yeşil, take 3 kırmızı) → görsel değişim garantisi.
- **Thumbnail fikri:** Leo elinde dev geri sarma kumandası, arkada Lehman benzeri jenerik kule (logo yok) ikiye bölünmüş. Metin: "WHAT IF?" (2 kelime).
- **Shorts kancası:** "What if someone had saved Lehman Brothers in 2008? Here are three possible endings."
- **Risk notu:** **SARI-düşük.** Karşı-olgusal kısım spekülatif → ekonomist görüşleri kaynaklı, "possibility" dili, gerçekçi sahte haber görseli yok (Ö11). Gerçek yetkililer canlandırılmaz; logo yok. Konu doymuş [KH-A17, RÖ D2] → açı farklılığına dayanıyor; çok sayıda rakam henüz [doğrulanacak] (finans-dogrulayici yükü yüksek).

### S10 — The 34-Candle Cake (Japan 1989, uzun gölge)
- **Sütun:** A (KH-A13)
- **Açı türü:** Uzun gölge (insan ömrüyle ölçülen zaman)
- **Çalışma başlığı:** Japan's 1989 Bubble Took 34 Years to Heal
- **Alternatif 1:** The Stock Market That Made Japan Wait 34 Years
- **Alternatif 2:** Japan 1989: How a Booming Economy Got Stuck
- **Vaat:** 1989'un son haftasında doğan bir bebeğin hayatı boyunca Japon borsasının neden geri dönmediğini ve bir balonun asıl bedelinin düşüş değil sonraki on yıllar olduğunu göstermek.
- **Hook varyantları:**
  - H1 (şok rakam): "On December 29, 1989, Japan's stock index closed at 38,915. If you bought that day, you waited more than 34 years to get back to even." (elendi: güçlü ama soyut "you bought"; tavsiye çağrışımı)
  - H2 (insan zaman çizelgesi): "A baby born in Tokyo in the last week of 1989 would turn thirty-four before Japan's stock market got back to that week's level. Thirty-four years. Today: how a booming economy got stuck, and what finally changed."
  - H3 (iddia): "In 1989, the land under Tokyo's Imperial Palace was said to be worth more than all of California." (elendi: iddia [doğrulanacak], başlıkta doğrulanamayan iddia riski; 2. bölüme taşınır, doğrulanırsa)
  - **Seçilen: H2.** Test: somut özne (Tokyo'da bir bebek, 34 yıl) ✓, vaat ✓, rakam [AÖ: 38.915,87 → 22 Şubat 2024] ✓ (F3'te birincil).
- **Hook (kelimesi kelimesine, 0–15 sn):** "A baby born in Tokyo in the last week of 1989 would turn thirty-four before Japan's stock market got back to that week's level. Thirty-four years. Today: how a booming economy got stuck, and what finally changed."
- **15–30 sn köprü:** Neden önemli: "stocks always come back fast" inancı; Japonya faizleri bugün 1996'dan beri en yüksek [KH-A13 K3]. Sonunda: "the hidden thing that kept Japan stuck for decades, and why it matters for every bubble."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + bebek "Yuki" (kurgusal) doğar; zaman çizgisi başlar. ↺ 1:20 "To see why Yuki's whole life fit inside one recovery, look at what her parents saw in 1989."
  2. 1:30–3:30 1980'ler balonu: hisse + arsa [KH-A13]; Saray iddiası doğrulanırsa. ↺ 3:00 "Then, in 1990, the music stopped. But slowly."
  3. 3:30–5:30 Düşüş + banka kötü kredileri (~100 trilyon yen silindi [AÖ, doğrulanacak]). **İlk büyük ödül:** "zombi" kredi mekanizması (batık borcu gizlemek → yeni yatırım yok) [doğrulanacak kaynak]. → 5:15 abone cümlesi. ↺ 5:20 "Yuki is ten. The market is still far below. And prices start to fall."
  4. 5:30–7:30 Deflasyon zihniyeti, sıfır faiz [doğrulanacak]; Yuki'nin hayatından anlar (okul, ilk iş). ↺ 7:00 "Yuki turns 34. Something finally moves."
  5. 7:30–9:30 22 Şubat 2024 kapanış 39.098,68 > 38.915,87 [AÖ]. Ne değişti (şirket reformları, zayıf yen [doğrulanacak]). ↺ 9:00 "And now, in 2026, Japan faces a new test."
  6. 9:30–11:00 2026: 10 yıllık tahvil ~%3, 1996'dan beri en yüksek [KH-A13 K3]; zayıf yen. Possibility dili.
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **34 yıllık yolda rehber.** Kurgusal "Yuki"nin hayatı boyunca yanında yürüyen, her doğum gününde borsa çizgisine bakan rehber. Leo hikâyenin kahramanı değil, tanığı.
- **Akılda kalan karakter anı:** 2024'te Leo, 34 mumlu doğum günü pastasını Yuki'ye uzatır; arka planda borsa çizgisi tam o anda eski zirveyi geçer.
- **Kendi veri grafikleri (Ö2):**
  1. Nikkei 225, 1985–2026 (zirve 38.915,87 → 2024 aşımı) — FRED `NIKKEI225` [doğrulanacak; çapalar AÖ].
  2. Japonya konut fiyat endeksi — BIS, FRED `QJPN628BIS` [doğrulanacak].
  3. Japonya 10 yıllık tahvil faizi 1990–2026 — FRED `IRLTLT01JPM156N` + Trading Economics 2026 [KH-A13 K3].
  4. "Yuki'nin hayat çizgisi": yaş ile Nikkei'nin 1989 zirvesine uzaklığı (kendi infografiğimiz) [H].
- **Özgün tez (Ö1):** "The real cost of a bubble isn't the fall. It's the decades of fear and hidden bad debt that come after it."
- **Bugünle bağ:** Japon faizi 30 yılın zirvesinde [KH-A13]; "piyasa hep hızla döner" inancına karşı örnek.
- **Görselleştirme notu:** İnsan ömrü = zaman ölçeği (yaş sayacı ekranda). 1989 neon Tokyo (sıcak pembe) → 1990'lar soğuk gri → 2024 aydınlık. Mevsim değişimleri görsel değişim noktası. Gerçek kişi yok; Yuki kurgusal ve öyle sunulur.
- **Thumbnail fikri:** Leo 34 mumlu pastayla, arkada 34 yıllık düz-düşük çizgi ve sonunda yukarı ok. Metin: "34 YEARS" (2 kelime).
- **Shorts kancası:** "If you were born the week Japan's stock market peaked, you'd be 34 before it came back."
- **Risk notu:** YEŞİL. Kurgusal karakter (Yuki) gerçek kişi gibi sunulmamalı (Ö11). Saray–Kaliforniya iddiası [doğrulanacak]; doğrulanmazsa kullanılmaz. Kanıtlı talep orta (alaka medyanı 104 K, 12 ayın en iyisi 414 K [KH-A13]). Rakamlar şimdilik [AÖ] → F3'te Nikkei Inc./Japan Times birincil.

### S11 — The 30-to-1 Tower (LTCM 1998, deney/simülasyon)
- **Sütun:** A (KH-A15)
- **Açı türü:** Deney/simülasyon (Leo modeli kendisi test eder)
- **Çalışma başlığı:** The Nobel-Winning Fund That Lost 44% in a Month
- **Alternatif 1:** LTCM: When Genius Math Met One Bad Summer
- **Alternatif 2:** $30 of Debt for Every $1: How LTCM Almost Broke Wall St
- **Vaat:** Dahilerin modelinin neden çöktüğünü Leo'nun masa üstünde kurduğu "30'a 1 kule" deneyiyle göstermek; kaldıraç küçük hatayı nasıl dev kayba çevirir.
- **Hook varyantları:**
  - H1 (şok rakam): "One fund earned 43 percent in 1995. Its team included two Nobel winners. In August 1998, it lost 44 percent in one month. Fourteen firms then put in 3.6 billion dollars to contain it. Today: what the math missed."
  - H2 (Leo deneyi): Leo 1 $'lık tuğlanın üstüne 30 borç tuğlası dizer, hafifçe dokunur: "This is how a genius fund was built." (elendi: görsel çok iyi ama sözlü vaat yok; H1'in görseli)
  - H3 (soru): "What happens when the smartest people in finance are wrong for just one month?" (elendi: "smartest" ölçülemez, rakam yok)
  - **Seçilen: H1.** Test: somut özne (fon, iki Nobel, %44, 14 firma) ✓, vaat ("what the math missed") ✓, tüm rakamlar FRH ✓.
- **Hook (kelimesi kelimesine, 0–15 sn):** "One fund earned 43 percent in 1995. Its team included two Nobel winners. In August 1998, it lost 44 percent in one month. Fourteen firms then put in 3.6 billion dollars to contain it. Today: what the math missed."
- **15–30 sn köprü:** Neden önemli: kaldıraç küçük ihtimalleri büyük felakete çevirir; 2026 özel kredi/kaldıraç endişesi [KH-A15, T]. Sonunda: "the one assumption in the model that broke, and why 30-to-1 turns a small mistake into a huge one."
- **Yapı (12 dk):**
  1. 0:00–1:30 Kanca + 30'a 1 kule. ↺ 1:20 "First, how did they make 40 percent a year?"
  2. 1:30–3:30 Strateji: küçük fiyat farklarından kazanç, matematik modeller [FRH]; getiriler 20/43/41/17 % [FRH]. ↺ 3:00 "Small gains need big size. Here's how big."
  3. 3:30–5:30 Kaldıraç: 1997 sonu ~30 $ borç / 1 $ sermaye [FRH]; Leo'nun kule deneyi (%1, %2, %3 kayıpta sermaye) [H]. **İlk büyük ödül.** → 5:15 abone cümlesi. ↺ 5:20 "The model said a month like August 1998 almost never happens. Then August 1998 happened."
  4. 5:30–7:30 1998 Rusya krizi [KH-A15], Ağustos'ta −%44, 21 Ağustos büyük kayıp, 2 Eylül yatırımcı mektubu [FRH]. ↺ 7:00 "Now the problem wasn't LTCM. It was everyone they owed."
  5. 7:30–9:30 18–23 Eylül: NY Fed toplantıları, Buffett grubunun teklifi (12:30 son saat), akşam 6'da 14 firmanın 3,625 milyar $ ile %90'ı alması; Fed kendi parasını koymadı [FRH]. ↺ 9:00 "So did the geniuses learn the lesson? And did Wall Street?"
  6. 9:30–11:00 Sonrası (fon 1999 sonu kapandı [FRH]); "model riski" dersi; 2026 kaldıraç sorusu (possibility).
  7. 11:00–12:00 Tez + uç ekran.
- **Leo'nun rolü (Ö5):** **Laboratuvar deneycisi.** Önlüklü Leo masa üstünde kule kurar, "model"ini zar/yazı-tura ile test eder, deney sonucunu not defterine yazar.
- **Akılda kalan karakter anı:** Leo 30 katlı kuleye tüyle dokunur, kule yıkılır; Leo yüzündeki tozla not defterine "30:1 — DO NOT TOUCH" yazar.
- **Kendi veri grafikleri (Ö2):**
  1. LTCM yıllık getiri 1994–1997 + Ağustos 1998 −%44 [FRH].
  2. Kaldıraç simülasyonu: 30:1'de varlık değerindeki %1–%4 düşüşün sermayeye etkisi [H, FRH oranı].
  3. Kurtarma yapısı: 14 firma, 3,625 milyar $, %90 sahiplik; ortaklara %10 [FRH].
  4. (yedek) 2 Eylül → 23 Eylül 1998 zaman çizelgesi [FRH].
- **Özgün tez (Ö1):** "LTCM's math wasn't stupid. It was right most of the time, and 30-to-1 leverage meant being wrong once was enough."
- **Bugünle bağ:** 2026 özel kredi/kaldıraç tartışması [KH-A15 tahmin; KH elenenler "özel kredi" kaynak eksik] → bağ zayıf [T].
- **Görselleştirme notu:** Beyaz laboratuvar (soğuk) + sıcak lamba altında Leo; kule, zar, yazı-tura objeleri. 1998 Wall Street toplantı odası temsili (gerçek kişi yüzü yok).
- **Thumbnail fikri:** Leo önlüklü, sallanan dev para kulesinin önünde; üstte "30:1". Metin: "30 TO 1" (3 kelime).
- **Shorts kancası:** "With 30-to-1 leverage, a 3% mistake wipes you out. A Nobel-winning fund learned this in 1998."
- **Risk notu:** YEŞİL. Rakip benzerliği: Hamish Hodder "The Most Dangerous Hedge Fund in History" 1,04 M [KH-A15] → başlık kalıbı farklı tutuldu. Kanıtlı talep: tek güçlü 12 ay videosu; Wikipedia −%33 [KH-A15]. Alternatif 2 "Wall St" kısaltması aramada zayıf olabilir.

---

## 1. Açı türü çeşitliliği (kapı: ≥5 farklı açı türü)

| ID | Konu | Sütun | Açı türü | Kanıt (bu dosyada) |
|---|---|---|---|---|
| S01 | 1929 marjin borcu | A | Follow the money (mekanizma) | "borç doları" tüm video boyunca takip edilen nesne |
| S02 | 1929 → 1933 bankalar | A | Mit yıkma | "crash → Depression" kısa hikâyesi eksik yarısıyla düzeltiliyor |
| S03 | 1929'da 1.000 $ | A | İkinci tekil sahne / interaktif seçim | "You have…", üç kapı oyunu |
| S04 | Weimar 1923 | A | Sayısal gerilim | ekranda video boyu tırmanan mark/dolar sayacı |
| S05 | 1973 petrol | A | Bugünle paralel | iki etiket 1973/2026, 6. bölüm karşılaştırma |
| S06 | Cisco 2000 | A | Leo'nun kendi yanılgısı | Leo'nun inancı çöküyor, not yırtılıyor |
| S07 | Black Monday 1987 | A | Saat saat gerilim + ters köşe | saat damgalı canlı yayın, "nothing broke" sonucu |
| S08 | Hunt kardeşler 1980 | A | Kahraman/kötü adam (soygun) | soygun filmi bölüm kartları |
| S09 | Lehman 2008 | A | Karşı-olgusal tarih | üç "take" geri sarma |
| S10 | Japonya 1989 | A | Uzun gölge (insan ömrü ölçeği) | kurgusal bebeğin 34 yılı |
| S11 | LTCM 1998 | A | Deney/simülasyon | Leo'nun 30:1 kule deneyi |

**Sonuç:** 11 senaryo, **11 farklı açı türü** (kapı ≥5), **11/11 A** (kapı ≥7 A). 1929 talebin en yoğun olduğu konu olduğu için [KH-A1, RÖ D2] üç ayrı açıyla girdi (S01–S03). Hakem yalnız birini seçmeli, diğer ikisi sonraki A slotları için yedek.

## 2. Leo'nun rol tablosu (Ö5: aynı durum/aynı sonuç yok)

| ID | Leo'nun rolü | Leo'nun durumu | Leo'nun sonucu |
|---|---|---|---|
| S01 | Borçlanan oyuncu | 1929 sokağında borçla alım | marjin çağrısı, cepler boş |
| S02 | Dedektif | dosya panosu, domino | davayı Main Street'te çözer |
| S03 | Oyun sunucusu + 3 klon | yarışma stüdyosu | "kazanan" klonun 2026'da kaybetmesi |
| S04 | Fabrika işçisi/koşucu | saatle yarış | fiyat yolda değişir |
| S05 | Zaman yolcusu | iki dönem, iki etiket | karşılaştırmayı yapar, hüküm vermez |
| S06 | Yanılan inanan | kendi fikriyle yüzleşir | fikrini değiştirir |
| S07 | Radyo muhabiri | borsa salonundan canlı | tek cümleyi okur |
| S08 | Soygun anlatıcısı | plan tahtası | planın bozulmasını izler |
| S09 | Film yönetmeni | montaj odası | üç son çeker |
| S10 | Rehber/tanık | 34 yıllık yol | pasta anı |
| S11 | Deneyci | laboratuvar | kule yıkılır, ders yazar |

Hiçbir senaryoda Leo uzman/danışman gibi konuşmuyor, "you should buy/sell" yok (Ö10). Gerçek kişiler (Hunt'lar, Fed yetkilileri, Lehman yöneticileri) Leo tarafından canlandırılmıyor.

## 3. Ortak sahne/metin tekrarı önlemi (Ö6–Ö7)
- Bu kanalın ilk videosu: karşılaştırılacak önceki metin yalnız pilot/ses testi metni (`uretim/ses-testi/okuma-metni.md`). Pilotun kanca cümleleri ("Imagine waking up…", "cup of coffee", "No boring charts") hiçbir hook'ta yok (S04 bilerek "loaf of bread" + poliçe ile kuruldu).
- Kapanış cümlesi kalıbı her senaryoda tez cümlesine bağlı, ortak bir "outro" cümlesi yok.

## 4. Kendi ön sıralamam (editör gözü, karar değil) ve "neden kaybedebilir"

`roast` mantığıyla her birinin en zayıf noktasını yazdım. Puanlamayı viralite-analisti yapar.

| Sıra | ID | Neden güçlü [T] | Neden kaybedebilir |
|---|---|---|---|
| 1 | S03 | Nişin en büyük talebi (1929) [KH-A1] + ikinci tekil sahne [RÖ D5] + kişisel finans bağı + sona kadar açık "twist" döngüsü + maskot için doğal rol (sunucu) | Oyun formatı tarih derinliğini azaltabilir; "shoebox kazandı" yanlış anlaşılıp tavsiye gibi okunabilir; banka kapısının sonucu için sayı [doğrulanacak] |
| 2 | S07 | Tek rakam (%22,6) çok güçlü, tüm rakamlar FRH, ters köşe sonuç, güncel "Black Monday" korkusu | Talep 1929'un altında [KH-A14]; saatlik veri bulunamazsa vaat zayıflar |
| 3 | S01 | Mekanizma açısı + 1929 talebi, rakip "follow the dollar" karşılığı [RÖ §6] | Marjin anlatısı bilinir; S03'le aynı konu |
| 4 | S04 | Somut nesne (poliçe → ekmek), kazananlar açısı taze, Kasım yıldönümü | Hiperenflasyon kategorisi rakipte düşük (medyan 0,65 [RÖ D2]); pilotla tema yakınlığı |
| 5 | S10 | Çok güçlü insan ölçeği kancası, güncel faiz bağı | Rakamların çoğu [AÖ]; Japonya talebi orta |
| 6 | S08 | En iyi hikâye gerilimi (soygun), emtia bağı | Talep kanıtı zayıf (alaka medyanı 3 K) |
| 7 | S02 | Önemli ve doğru tez | "bilinen hikâye yanlış" kalıbı aşınmış [RÖ D1]; soyut mekanizma (para arzı) görsel olarak zor |
| 8 | S06 | Leo'nun yanılgısı güçlü karakter anı, AI gündemi | `benzer_aci` riski; Cisco rakamları [AÖ]; genç izleyiciye Cisco tanıdık değil |
| 9 | S05 | En zamanlı | Savaş bağlamı → reklam SARI; saf 1973 araması zayıf [KH-A2] |
| 10 | S09 | Yeni açı, doymuş konuda fark | Spekülatif, çok sayıda [doğrulanacak], konu doymuş |
| 11 | S11 | Tüm rakamlar FRH, güçlü görsel deney | Niş, Wikipedia ilgisi düşüyor, tek rakip videosunun gölgesinde |

## 5. Elenen konu/açı fikirleri (bu turda yazılmadı)
| Fikir | Neden elendi |
|---|---|
| Tulip mania, FTX, Enron, South Sea | Arz doygun, 12 ayda talep kanıtı yok [RÖ D2]; görev notu da doymuş diyor |
| Madoff | Talep güçlü ama "too good to be true" açısı nişte çok işlenmiş; Aralık yıldönümüne saklanabilir [KH-A6] |
| Black Wednesday / Soros | Siyasi kutuplaşma ve komplo çerçevesi riski [KH-A16]; ilk video için gereksiz risk |
| Zimbabwe | İnsani acı merkezde (hassas) [KH-A11] |
| Railway Mania | Kanıtlı talep yok (alaka medyanı 57) [KH-A5] |
| Dot-com "AI vs dot-com" genel karşılaştırma | Infographics'te iki kez işlendi → `benzer_aci` [KH-A4]; yerine S06 tek şirket açısı |
| "Leo 1929'da banker" | Gerçek bankacı intihar mitine yakınlık riski [monetizasyon §5] |

---

## Test (kapı: ≥10 senaryo, ≥5 açı türü, ≥7 A, başlık ≤60 karakter, hook ≤40 kelime ve telaffuz listesi temiz)

Komut: `python3 uretim/2026-10-26-secim/02-senaryo/senaryo-kontrol.py uretim/2026-10-26-secim/02-senaryo/senaryolar.md`

**1. koşu:** S06 hook 42 kelime → KALDI (kapı ≤40). Düzeltme: "still" çıkarıldı, "to come back" → "to recover" (40 kelime). 
**Son koşu (2026-10-27, çıkış kodu 0; iki koşu `diff` ile aynı):**

```
| ID | Alan | Metin | Karakter | Kelime | Yasak kelime | Sonuç |
|---|---|---|---|---|---|---|
| S01 | Çalışma başlığı | The 10% Loan That Built the 1929 Crash | 38 | — | — | GEÇTİ |
| S01 | Alternatif 1 | How Borrowed Money Turned 1929 Into a Disaster | 46 | — | — | GEÇTİ |
| S01 | Alternatif 2 | 1929: Follow One Borrowed Dollar to the Bottom | 46 | — | — | GEÇTİ |
| S01 | Hook | (seçilen) | — | 38 | yok | GEÇTİ |
| S02 | Çalışma başlığı | The 1929 Crash Was Only the First Domino | 40 | — | — | GEÇTİ |
| S02 | Alternatif 1 | Why America's Banks, Not Stocks, Made the Depression | 52 | — | — | GEÇTİ |
| S02 | Alternatif 2 | 1929 to 1933: How a Market Fall Became a Depression | 51 | — | — | GEÇTİ |
| S02 | Hook | (seçilen) | — | 37 | yok | GEÇTİ |
| S03 | Çalışma başlığı | You Have $1,000 in 1929. Can You Keep It? | 41 | — | — | GEÇTİ |
| S03 | Alternatif 1 | Survive 1929 With $1,000: Every Choice Has a Trap | 49 | — | — | GEÇTİ |
| S03 | Alternatif 2 | Stocks, a Bank or a Shoebox: Who Survived 1929? | 47 | — | — | GEÇTİ |
| S03 | Hook | (seçilen) | — | 39 | yok | GEÇTİ |
| S04 | Çalışma başlığı | Weimar 1923: Who Got Rich While Money Died? | 43 | — | — | GEÇTİ |
| S04 | Alternatif 1 | One Dollar, One Trillion Marks: Germany in 1923 | 47 | — | — | GEÇTİ |
| S04 | Alternatif 2 | How Germany's Money Lost Everything in One Year | 47 | — | — | GEÇTİ |
| S04 | Hook | (seçilen) | — | 40 | yok | GEÇTİ |
| S05 | Çalışma başlığı | When Oil Quadrupled: What 1973 Tells Us About Now | 49 | — | — | GEÇTİ |
| S05 | Alternatif 1 | From $2.90 to $11.65: The Oil Shock of 1973 | 43 | — | — | GEÇTİ |
| S05 | Alternatif 2 | The 1973 Oil Shock and the Price You Pay Today | 46 | — | — | GEÇTİ |
| S05 | Hook | (seçilen) | — | 38 | yok | GEÇTİ |
| S06 | Çalışma başlığı | The Best Company of the Dot-Com Era Still Fell 90% | 50 | — | — | GEÇTİ |
| S06 | Alternatif 1 | It Took Cisco 25 Years to Get Back to 2000 | 42 | — | — | GEÇTİ |
| S06 | Alternatif 2 | Cisco 2000: When a Great Company Was a Terrible Bet | 51 | — | — | GEÇTİ |
| S06 | Hook | (seçilen) | — | 40 | yok | GEÇTİ |
| S07 | Çalışma başlığı | The Day Stocks Fell 22.6%, and Why Nothing Broke | 48 | — | — | GEÇTİ |
| S07 | Alternatif 1 | Black Monday 1987: The Worst Day in Stock Market History | 56 | — | — | GEÇTİ |
| S07 | Alternatif 2 | October 19, 1987: The Day Every Market Fell at Once | 51 | — | — | GEÇTİ |
| S07 | Hook | (seçilen) | — | 38 | yok | GEÇTİ |
| S08 | Çalışma başlığı | The Brothers Who Tried to Buy All the World's Silver | 52 | — | — | GEÇTİ |
| S08 | Alternatif 1 | How Two Billionaires Cornered Silver, and Lost It | 49 | — | — | GEÇTİ |
| S08 | Alternatif 2 | Silver Thursday: The Day the Hunt Brothers Fell | 47 | — | — | GEÇTİ |
| S08 | Hook | (seçilen) | — | 40 | yok | GEÇTİ |
| S09 | Çalışma başlığı | What If Lehman Brothers Had Been Saved in 2008? | 47 | — | — | GEÇTİ |
| S09 | Alternatif 1 | The Weekend Lehman Died: Three Ways It Could've Gone | 52 | — | — | GEÇTİ |
| S09 | Alternatif 2 | Lehman 2008: One Failed Rescue That Changed the World | 53 | — | — | GEÇTİ |
| S09 | Hook | (seçilen) | — | 36 | yok | GEÇTİ |
| S10 | Çalışma başlığı | Japan's 1989 Bubble Took 34 Years to Heal | 41 | — | — | GEÇTİ |
| S10 | Alternatif 1 | The Stock Market That Made Japan Wait 34 Years | 46 | — | — | GEÇTİ |
| S10 | Alternatif 2 | Japan 1989: How a Booming Economy Got Stuck | 43 | — | — | GEÇTİ |
| S10 | Hook | (seçilen) | — | 37 | yok | GEÇTİ |
| S11 | Çalışma başlığı | The Nobel-Winning Fund That Lost 44% in a Month | 47 | — | — | GEÇTİ |
| S11 | Alternatif 1 | LTCM: When Genius Math Met One Bad Summer | 41 | — | — | GEÇTİ |
| S11 | Alternatif 2 | $30 of Debt for Every $1: How LTCM Almost Broke Wall St | 55 | — | — | GEÇTİ |
| S11 | Hook | (seçilen) | — | 39 | yok | GEÇTİ |

Senaryo sayısı: 11 (kapı ≥10) · farklı açı türü: 11 (kapı ≥5) · A sütunu: 11 (kapı ≥7)
  S01: A · Follow the money
  S02: A · Mit yıkma
  S03: A · İkinci tekil sahne / interaktif seçim
  S04: A · Sayısal gerilim
  S05: A · Bugünle paralel
  S06: A · Leo'nun kendi yanılgısı
  S07: A · Saat saat gerilim + ters köşe sonuç
  S08: A · Kahraman/kötü adam
  S09: A · Karşı-olgusal tarih
  S10: A · Uzun gölge
  S11: A · Deney/simülasyon
KAPI: GEÇTİ
```

**Ek elle kontroller:**
- [x] Telaffuz listesi: tırnak içindeki tüm İngilizce metinlerde (hook, varyant, köprü, tez, Shorts) `grep -oE '"[^"]*"' | grep -iE 'charts?|complicated|scenarios?|truth|crash(es|ed)?|bold'` → yalnız Türkçe not satırları ("Crash" başlık açıklaması, "crash → Depression" alıntısı, pilot "No boring charts" alıntısı); seslendirilecek metinde 0.
- [x] Her hook'ta somut özne + vaat testi senaryo içinde yazılı; elenen varyantlar gerekçesiyle dosyada.
- [x] Abone çağrısı hiçbir hook/köprüde yok; yapılarda ilk büyük ödülden sonra (~5:15) planlı.
- [x] Her yapıda yeniden kancalar (↺) ≤90 sn aralıkla: 1:15–1:20, 2:50–3:00, 4:40/5:20, 6:50–7:00, 8:50–9:00 ve bölüm geçişleri (en uzun boşluk ~90 sn; F3 metin aşamasında kelime zamanıyla yeniden ölçülür).
- [x] Uydurma rakam yok: her rakam [FRH]/[PBS]/[ABA]/[KH]/[AÖ] etiketli; yeni ve kaynağı açılmamış rakamlar **[doğrulanacak]** (68 etiket). Çelişkiler (Hunt zirvesi, Rentenmark oranı) §0'da.
- [x] Ö1 tez (11/11), Ö2 ≥3 grafik + veri kaynağı (11/11), Ö4 anlatı yayı (7 bölüm), Ö5 rol tablosu (§2), Ö10 tavsiye dili yok.
- [ ] Açık: FRED seri kodları ve NBER serileri bu turda açılmadı (F3'te finans-dogrulayici + veri dosyası). [AÖ] rakamlar (Cisco, Nikkei) F3'te birincil kaynakla değiştirilmeli.

Kaynak linkleri (bu turda okunan/aranan): [Fed History 1929](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) · [Fed History Great Depression](https://www.federalreservehistory.org/essays/great-depression) · [Fed History 1930–31 panics](https://www.federalreservehistory.org/essays/banking-panics-1930-31) · [Fed History 1973](https://www.federalreservehistory.org/essays/oil-shock-of-1973-74) · [Fed History 1987](https://www.federalreservehistory.org/essays/stock-market-crash-of-1987) · [Fed History LTCM](https://www.federalreservehistory.org/essays/ltcm-near-failure) · [PBS Weimar](https://www.pbs.org/wgbh/commandingheights/shared/minitextlo/ess_germanhyperinflation.html) · [ABA Journal Hunt](https://www.abajournal.com/magazine/article/panic-1893-hunt-brothers-1980) · [AÖ] [Sherwood News Cisco](https://sherwood.news/markets/after-a-quarter-century-cisco-surpasses-dot-com-bubble-closing-high) · [AÖ] [Cisco heritage 2000 market cap](https://heritage.cisco.com/2000_marketcap/) · [AÖ] [Japan Times Nikkei record](https://www.japantimes.co.jp/business/2024/02/22/markets/japan-stocks-hits-record-high/) · [AÖ] [Nippon.com Nikkei](https://www.nippon.com/en/japan-data/h01927/nikkei-index-sets-first-record-high-since-1989.html)
