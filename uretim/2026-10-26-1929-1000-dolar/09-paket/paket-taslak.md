# F4 — Paket taslağı · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Hazırlayan:** youtube-paketleyici · **Tarih:** 2026-10-27 · **Durum:** TASLAK (F8'de gerçek ses/kurgu zamanları, lisans kaydı ve politika kararıyla kesinleşir)
**Girdiler:** `03-metin/metin.md` (KİLİTLİ, v2), `03-metin/dogrulama.md` §4 (yasal not), `03-metin/politika-denetimi.md` (G4 kırmızı çizgi), `02-senaryo/senaryo-karari.md` (H5), `01-arastirma/rakip-ozet.md` (D4, §4, §6), `uretim/kanal-kimligi/kanal-paketi.json`.
**Thumbnail konseptleri:** `09-paket/thumb-konsept.md` (başlıkla birlikte okunuş orada).
**Kapı betiği:** `09-paket/paket-kontrol.py` → çıktı §8. Etiketler: **[Ö]** betik ölçümü · **[RÖ]** rakip-özet verisi · **[T]** benim yargım/tahminim.

**Kırmızı çizgiler (her metinde uygulandı):** başlıkta yıl sınırı 1929; başlık, thumbnail, açıklama ve Shorts başlıklarında bugüne dönük "paranı nereye koy" hükmü yok ("where to keep your money", "which door wins today", "cash is trash", "banks are safe now" türü 0); tavsiye/emir dili yok; rakip kalıbı ("real reason / true origin / get wrong") yok.

---

## 1. Başlık: 7 aday → 2 elendi → 5 varyant

**Arama ve öneri ayrı düşünüldü.** Bu ilk herkese açık video; abonesi olmayan kanalda trafiğin ilk kaynağı gözatma/öneri olacak [T]. Öneri sistemi başlık + thumbnail ikilisinin CTR'ına ve izlenme süresine bakıyor, bu yüzden **ana başlık merak taşır** (ikinci tekil sahne, hook ile aynı vaat). Arama kelimeleri ("1929 stock market crash", "Great Depression") **açıklamanın ilk satırına, bölümlere ve etiketlere** gider; başlıkta "1929" arama çapası olarak durur.

**Tek vaat testi:** başlık ("$1,000 in 1929, can you keep it?") = thumbnail (kapılar / kutu / borsa grafiği) = ilk 15 sn ("You have one thousand dollars. Three doors… one is a disaster, one is a gamble, one is a surprise"). Üçü aynı oyunu vaat ediyor.

Puanlama (betik, ağırlıklar §8'de): merak 0.30 (viralite modeli ölçüt 1 + somut özne tavanı), arama 0.20, thumbnail ile okunuş 0.20, politika/doğruluk 0.20, mobil kesilme 0.10. Ölçüt puanları benim yargım [T]; betik yalnız uzunluk, kelime kontrolü ve toplamı hesaplar [Ö].

| # | Açı | Başlık | Krk [Ö] | Puan [Ö/T] | Karar |
|---|---|---|---|---|---|
| T1 | merak | You Have $1,000 in 1929. Can You Keep It? | 41 | **8.50** | **ÖNERİLEN (sabit, H5)** |
| T2 | karşıtlık | Stocks, a Bank or a Shoebox: Who Survived 1929? | 47 | 7.90 | yedek 1 (hakemin örnek alternatifi; soru işaretli) |
| T4 | sonuç / arama (soru işaretsiz) | Surviving the 1929 Crash With $1,000: Three Doors | 49 | 7.70 | yedek 2 = **soru işaretsiz alternatif (H5)**; arama ağırlıklı ("1929 crash") |
| T3 | karşıtlık (soru işaretsiz) | Stocks, a Bank or a Shoebox: $1,000 Through 1929 | 48 | 7.60 | yedek 3 (soru işaretsiz, kapıları sayan) |
| T7 | sonuç | $1,000 in 1929: The Door Everyone Laughed At Won | 48 | 7.10 | yedek 4 (cevaba yakın; yalnız CTR düşükse) |
| T5 | merak | 1929: The Smartest Door Was the Worst One | 41 | 6.80 | **ELENDİ** |
| T6 | sonuç | The Shoebox That Beat the Stock Market in 1929 | 46 | 6.40 | **ELENDİ** |

**Neden T1 (önerilen):** hakem başlığı sabit istiyor (H5; Test & Compare'de tek değişken thumbnail). Bağımsız gerekçe: en somut iki özne ($1,000 + 1929), ikinci tekil hitap izleyiciyi oyuna sokuyor, hook'un ilk cümlesiyle aynı vaat. 41 karakter, mobilde kesilmeden okunur. Hiçbir thumbnail metnini tekrar etmiyor. Soru işareti kalıbının medyanı 0,91 [RÖ §4], hafif eksi; ama "You have $X in [year]" kalıbının rakipte ölçülmüş karşılığı yok [V §2], yani özgünlük kazancı bu eksiyi dengeliyor [T].
**T2 (yedek 1):** üç kapıyı başlıkta sayıyor, merak "kim?" sorusunda; thumbnail A ile birlikte okunursa kapıları iki kez anlatır (tekrar), B ve C ile iyi. Soru işaretli.
**T4 (yedek 2, soru işaretsiz):** hakemin istediği **soru işaretsiz** alternatif (soru işareti kalıbının medyanı 0,91 [RÖ §4]). Arama tarafı en güçlü ("1929 crash" + "surviving"); "Crash" başlıkta serbest (seslendirilmiyor; senaryo kuralı). Öneri tarafında merakı T1'den zayıf [T]. F12'de CTR düşük çıkarsa ilk denenecek başlık budur.
**T3 (yedek 3):** soru işaretsiz ikinci seçenek; kapıları sayar, merak T2'den zayıf. Thumbnail A ile birlikte kapıları iki kez anlatır.
**T7 (yedek 4):** cevaba yakın (kutu kazanıyor), merakı azaltır. Doğru: videoda stüdyo seyircisi Box Leo'ya gülüyor ve "Box Leo wins nineteen twenty-nine" deniyor. Yalnız F12'de "izleyici neyin videosu olduğunu anlamıyor" verisi gelirse.

**Elenenler:**
- **T5 — "1929: The Smartest Door Was the Worst One":** (1) para nesnesi yok; "door" thumbnail A dışında bağlamsız, viralite modelinin somut özne tavanına takılıyor (merak ≤6). (2) Shorts 1 kancasıyla neredeyse aynı cümle → uzun video ile Short aynı vaadi iki kez harcar.
- **T6 — "The Shoebox That Beat the Stock Market in 1929":** (1) politika: "cash beats stocks" okuması, K4/G4 katı okumasına en yakın başlık; yıl sınırı var ama "beat the stock market" yatırım arama niyetini çeker. (2) Cevabı veriyor → merak düşer. (3) Yanlış kitle (yatırım ipucu arayan) → düşük tutma riski [T].

<!-- veri:basliklar -->
```text
You Have $1,000 in 1929. Can You Keep It?
Stocks, a Bank or a Shoebox: Who Survived 1929?
Stocks, a Bank or a Shoebox: $1,000 Through 1929
Surviving the 1929 Crash With $1,000: Three Doors
$1,000 in 1929: The Door Everyone Laughed At Won
```

<!-- veri:basliklar-elenen -->
```text
1929: The Smartest Door Was the Worst One
The Shoebox That Beat the Stock Market in 1929
```

---

## 2. Açıklamanın ilk 2 satırı: 2 versiyon

| Versiyon | Metin | Krk [Ö] | Anahtar kelime ilk 150'de [Ö] | Karar |
|---|---|---|---|---|
| A (ikinci tekil, başlığı yineler) | It's 1929 and you have $1,000. Stocks, a bank or a shoebox: which door keeps your money through the stock market crash and the Great Depression? | 144 | 1929 · stock market crash · Great Depression (3/3); "1929 stock market crash" ifadesi bitişik değil | elendi |
| **B (anahtar kelime önde + oyun)** | The 1929 stock market crash as a game: you have $1,000 and three doors. Stocks, a bank or a shoebox. Which one gets you through the Great Depression? | 149 | 1929 stock market crash (bitişik, 4. karakterde) · Great Depression (3/3) | **SEÇİLDİ** |

**Gerekçe:** başlık zaten ikinci tekil merakı taşıyor; A onu tekrar ediyor ve arama ifadesini ("stock market crash") 100. karaktere itiyor. B arama ifadesini en başa koyuyor (arama sonucu parçacığı ve "daha fazla" öncesi görünen alan), oyun vaadini de koruyor. İkisi de 150 karakterin içinde, kelime ortasında kesilmiyor [Ö]. "Gets you through" yalnız 1929–33 için; bugüne hüküm yok.

---

## 3. Açıklama taslağı (uzun video)

Yer tutucular F8'de doldurulur: bölüm zamanları (kurgu-editoru'nun gerçek zamanları), müzik/SFX atıfları (`06-muzik/lisans-kaydi.md`), oynatma listesi bağlantısı (liste ilk videoyla açılır). Yasal not `03-metin/dogrulama.md` §4'ten **aynen**; son cümlesi ("Narration voice is AI-generated.") istenen AI satırının başı olduğu için satır aynı paragrafta devam ediyor, böylece iki koşul da tek metinde sağlanıyor.

<!-- veri:aciklama -->
```text
The 1929 stock market crash as a game: you have $1,000 and three doors. Stocks, a bank or a shoebox. Which one gets you through the Great Depression?

Leo, our cartoon host, sends one player through each door, from the September 1929 market peak to the March 1933 bank holiday, using real data: the Dow, bank suspensions and consumer prices. Then we move the winning door to 2026 to see why the same math runs the other way.

Not financial advice. For educational purposes only.

CHAPTERS
0:00 The game: $1,000 and three doors
1:35 Door 1: The stock market
3:15 Door 2: The bank
5:35 Door 3: The shoebox
7:12 The bottom: July 1932
8:42 March 1933: every door locked
9:57 The twist: the same door in 2026
11:06 What the game really tests

SOURCES
• Federal Reserve History, "Stock Market Crash of 1929": https://www.federalreservehistory.org/essays/stock-market-crash-of-1929
• Federal Reserve History, "Banking Panics of 1930–31": https://www.federalreservehistory.org/essays/banking-panics-1930-31
• Federal Reserve History, "The Great Depression": https://www.federalreservehistory.org/essays/great-depression
• FDIC, A Brief History of Deposit Insurance in the United States, ch. 3, Table 5: https://www.fdic.gov/resources/publications/brief-history-of-deposit-insurance/book/brief-history-deposit-insurance-3.pdf
• FDIC, Deposit Insurance: https://www.fdic.gov/resources/deposit-insurance
• U.S. Bureau of Labor Statistics, CPI-U (CPIAUCNS), via FRED: https://fred.stlouisfed.org/series/CPIAUCNS
• U.S. Bureau of Labor Statistics, CPI news release, October 14, 2026: https://www.bls.gov/news.release/archives/cpi_10142026.htm
• U.S. Bureau of Economic Analysis, NIPA Table 6.6A, wages and salaries per full-time equivalent employee, 1929 (via DBnomics): https://db.nomics.world/BEA/NIPA-T60600A
• Borowiecki, Dzieliński & Tepper, "The Great Margin Call", Economic History Review (2022)
• Mark Hulbert, "25 Years to Bounce Back? Try 4½", The New York Times, April 26, 2009 (reprinted by History News Network): https://www.historynewsnetwork.org/article/79770
Charts in this video are our own, built from the data above.

LEGAL NOTE
This video is for education and entertainment only. It is not financial, investment, tax or legal advice. Leo is a fictional cartoon character, not a financial adviser. The "three doors" game is a simplified illustration of history: past results do not predict future results, and nothing here is a recommendation to buy, sell or hold any asset. Stock figures are price-only unless stated; inflation figures are U.S. CPI (BLS). Some scenes are illustrations, not historical footage. Sources are listed below. Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

MUSIC & SOUND
[YER TUTUCU: 06-muzik/lisans-kaydi.md → parça adı · sanatçı · lisans · bağlantı, her dosya için bir satır]

MORE FROM TOONOMY
The Collapse: Financial History Explained: [YER TUTUCU: oynatma listesi bağlantısı]
Subscribe for new animated finance stories every week: https://www.youtube.com/@toonomy

#GreatDepression #StockMarketCrash #FinancialHistory
```

**Not (yasal not ↔ kaynak sırası):** yasal notta "Sources are listed below." yazıyor, ama kaynaklar notun **üstünde**. Notu değiştirmek finans-dogrulayici'nin metnine dokunmak olur; bu yüzden F8'de iki seçenek var: (a) LEGAL NOTE bloğunu SOURCES'ın üstüne taşımak, (b) doğrulayıcıdan "listed in this description" onayı almak. **Önerim (a)**; F8'de uygulanır, ilk 2 satırı etkilemez. Bu taslakta okunurluk için kaynaklar önde bırakıldı.

**Bölümler:** `metin.md` §4'teki 8 bölüm, betik zamanları (143 kpm). F8'de kurgu-editoru'nun gerçek zamanlarıyla değiştirilir; kurallar (0:00 ile başlar, ≥3 bölüm, her bölüm ≥10 sn, artan sıra) betikle şimdiden ölçüldü [Ö].

---

## 4. Etiketler ve hashtag'ler

Etiketler aramada küçük bir sinyal (yazım varyantları ve eş anlamlılar için); asıl iş başlık + açıklamada [T]. Sıra önemli: en özgül olan önde. Bugüne dönük yatırım ifadesi ("cash vs stocks", "where to keep money") **bilerek yok** (K6 "all portions… tags").

<!-- veri:etiketler -->
```text
1929 stock market crash, stock market crash 1929, great depression, great depression explained, 1929 crash, wall street crash of 1929, black tuesday, bank runs, bank failures 1930s, bank holiday 1933, fdic history, deflation explained, dow jones 1929, financial history, economic history, stock market history, animated history, finance animation, toonomy
```

<!-- veri:hashtagler -->
```text
#GreatDepression #StockMarketCrash #FinancialHistory
```
Hashtag seçimi: YouTube açıklamadaki ilk 3 hashtag'i başlığın üstünde gösterir. İkisi konu (arama hacmi olan olay adları), biri sütun/kanal kategorisi. `#1929` düşünüldü: tek başına sayı, sayfa başka konulara dağılıyor [T] → elendi.

---

## 5. Shorts paketleri (her biri uzun videoya "related video")

**"İlgili video" bağlantısı:** Shorts'un "Related video" alanının Data API'de karşılığı bu turda doğrulanmadı → F10'da `YAYIN.md`'ye **Studio adımı** olarak yazılır: Studio → Short → Details → "Related video" → uzun video. Açıklamadaki bağlantı ek önlemdir (Shorts açıklamasındaki bağlantı tıklanabilir değil olabilir; asıl kanal related video alanı) [T].

### Shorts 1 — "Pick a door" (kanca: "In nineteen twenty-nine, the smartest-looking door was the worst one.")
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| a | $1,000 in 1929: Which Door Would You Pick? | 42 | **SEÇİLDİ**: etkileşim sorusu (yorum), kancayı tekrar etmiyor, yıl sınırı var |
| b | In 1929, the Smartest-Looking Door Was the Worst | 48 | elendi: kancanın aynısı (ilk 2 sn zaten söylüyor), başlık ek bilgi vermiyor |

<!-- veri:shorts1-baslik -->
```text
$1,000 in 1929: Which Door Would You Pick?
```

<!-- veri:shorts1-aciklama -->
```text
It's 1929 and you have $1,000: the stock market, a bank or a shoebox under your bed. Here's the scoreboard by July 1932, and why falling prices decided it.

Full game, all three doors from 1929 to 1933 plus the 2026 twist: [YER TUTUCU: uzun video bağlantısı]

Sources: Federal Reserve History; FDIC, A Brief History of Deposit Insurance; U.S. BLS CPI via FRED (CPIAUCNS). Stock figure is price only, before dividends.

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #GreatDepression #FinancialHistory
```

### Shorts 2 — "Same box, opposite result" (kanca: "A shoebox of cash gained power in nineteen thirty-two…")
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| a | Same Box of Cash, Opposite Result: 1932 vs 2026 | 47 | **SEÇİLDİ**: videonun kendi mekanizma cümlesi; karşılaştırma, hüküm değil |
| b | Why Cash Got Stronger in 1932 (and Weaker in 2026) | 50 | elendi: "cash weaker in 2026" tek başına "cash is trash" okumasına en yakın (G4 kırmızı çizgisi) |

Not: Shorts 2'nin içeriği 2026 karşılaştırması olduğu için başlıkta "2026" doğru ve gerekli; yasak olan bugüne dönük **hüküm** ("keep/move your cash"). Monetizasyon-uyum-uzmani F8'de bu başlığa özellikle baksın.

<!-- veri:shorts2-baslik -->
```text
Same Box of Cash, Opposite Result: 1932 vs 2026
```

<!-- veri:shorts2-aciklama -->
```text
From September 1929 to July 1932, U.S. consumer prices fell about 21%, so a shoebox of cash bought more. In the 12 months to September 2026, prices rose 3.7%. Same box, opposite result. That's arithmetic, not a plan.

The full 1929 game, with all three doors: [YER TUTUCU: uzun video bağlantısı]

Sources: U.S. BLS CPI-U (CPIAUCNS) via FRED; BLS CPI news release, October 14, 2026 (not seasonally adjusted).

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inflation #FinancialHistory
```

---

## 6. Pinli yorum taslağı (2 aday)

| Aday | Metin özeti | Karar |
|---|---|---|
| **A** | "Eylül 1929, geleceği göremiyorsun: hangi kapı, neden?" + bonus "sıradaki oyun hangi kriz olsun?" | **SEÇİLDİ**: videonun kuralıyla aynı ("You can't see the future"), cevaplaması kolay (tek kelime + neden), tartışma kapıları arasında kalıyor; bonus soru seri talebini ölçer (F12 girdisi) |
| B | "Hangisi daha çok şaşırttı: üç bankadan biri mi, kutunun alım gücü mü?" | elendi: izleyicinin videoyu sonuna kadar izlemiş olmasını varsayıyor; yorum eşiği yüksek |

Bugüne dönük "paranı şimdi nerede tutuyorsun?" sorusu **bilerek yok**: yorumları kişisel yatırım tartışmasına çeker ve AI maskotlu kanalda tavsiye ortamı yaratır (K4 katı okuma) [T].

<!-- veri:pinli-yorum -->
```text
It's September 1929 and you can't see the future. Which door do you walk through: the stock market, the bank or the shoebox? Tell us why in one sentence.

Bonus: which money crisis from history do you want Leo to turn into the next game?

(Sources and data notes are in the description.)
```

---

## 7. Uç ekran ve oynatma listesi önerisi

- **Oynatma listesi:** "The Collapse: Financial History Explained" (`kanal-paketi.json`, sütun A). Liste bu videoyla açılır (boş liste kuralı); F11'de `tools/yayin/kanal.py`. Shorts'lar ayrıca "Money Stories in 60 Seconds | Shorts" listesine. "Start Here: Best of Toonomy" ilk 3 sütunun her birinden bir video olunca açılır (şimdi değil).
- **Uç ekran (son ~17 sn, metin S24):** kanalın başka herkese açık videosu yok → **abone öğesi + "Best for viewer" video öğesi**. Leo'nun sağ tarafı uç ekran kutuları için boş (metinde planlı). Weimar videosu yayınlanınca uç ekran o videoya çevrilir (metin §6 B sürümü, ses yeniden üretimi gerekir).

---

## 8. Test kapısı (betik)

Betik: `09-paket/paket-kontrol.py` (bu dosyadaki ve `thumb-konsept.md`'deki `<!-- veri:… -->` bloklarını okur; etiket sayımı `tools/yayin/yayin_paket.py` → `etiket_uzunlugu` ile, yani yükleme aracıyla aynı kural; yasal not `03-metin/dogrulama.md` §4'ten okunup birebir aranır).

Çıktı aşağıya betik çalıştırıldıktan sonra eklendi (§8.1).

### 8.1 Çıktı (2026-10-27; iki koşu, `diff` fark yok, sha256 324437d2db31f6bf…)

```
$ python3 uretim/2026-10-26-1929-1000-dolar/09-paket/paket-kontrol.py   # exit 0
== paket-kontrol.py ==
[1] Başlıklar (≤60 krk, 1929, yasaklı 0, bugüne dönük 0)
  OK   41 krk · You Have $1,000 in 1929. Can You Keep It?
  OK   47 krk · Stocks, a Bank or a Shoebox: Who Survived 1929?
  OK   48 krk · Stocks, a Bank or a Shoebox: $1,000 Through 1929
  OK   49 krk · Surviving the 1929 Crash With $1,000: Three Doors
  OK   48 krk · $1,000 in 1929: The Door Everyone Laughed At Won
  OK   41 krk · 1929: The Smartest Door Was the Worst One
  OK   46 krk · The Shoebox That Beat the Stock Market in 1929
[2] Başlık puanı = .30 merak + .20 arama + .20 thumb + .20 politika + .10 mobil (mobil: ≤45 krk 10, ≤50 9, ≤60 7)
       T1 8.50 · You Have $1,000 in 1929. Can You Keep It?
       T2 7.90 · Stocks, a Bank or a Shoebox: Who Survived 1929?
       T4 7.70 · Surviving the 1929 Crash With $1,000: Three Doors
       T3 7.60 · Stocks, a Bank or a Shoebox: $1,000 Through 1929
       T7 7.10 · $1,000 in 1929: The Door Everyone Laughed At Won
       T5 6.80 · 1929: The Smartest Door Was the Worst One
       T6 6.40 · The Shoebox That Beat the Stock Market in 1929
  OK   en yüksek puan T1 (önerilen başlıkla tutarlı)
  OK   en düşük 2 = T5, T6 (elenenlerle tutarlı)
[3] Açıklama
       ilk paragraf 149 krk
  OK   ilk 150 krk içinde: 1929 stock market crash
  OK   ilk 150 krk içinde: Great Depression
  OK   ilk 150 krk içinde: $1,000
  OK   ilk paragraf ≤150 krk (kesilmeden okunur)
  OK   açıklama 3143/5000 bayt
  OK   açıklamada < > yok
  OK   "Not financial advice" var
  OK   AI satırı birebir var
  OK   yasal not (dogrulama.md §4) birebir var
  OK   bölümler 8 adet, 0:00 ile başlıyor, artan, her biri ≥10 sn
  OK   bölümler metin.md §4 ile birebir (zamanlar F8'de gerçek sesle güncellenir)
  OK   kaynak satırı 10 (9 + Hulbert = 10 beklenir)
  OK   Hulbert kaynağı var
       yer tutucu: 06-muzik/lisans-kaydi.md → parça adı · s, oynatma listesi bağlantısı
  OK   açıklama yasaklı/clickbait/tavsiye: 0
[4] Etiketler ve hashtag'ler
  OK   etiketler 19 adet, 373/500 (YouTube sayımı)
  OK   etiket yasaklı: 0
  OK   hashtagler: ['#GreatDepression', '#StockMarketCrash', '#FinancialHistory']
  OK   açıklama aynı 3 hashtag ile bitiyor
[5] Shorts
  OK   shorts1 başlık 42 krk · $1,000 in 1929: Which Door Would You Pick?
  OK   shorts1 yasaklı/clickbait/tavsiye: 0
  OK   shorts1 AI satırı + Not financial advice
  OK   shorts1 uzun videoya bağlantı yeri var (+ Studio related video adımı)
  OK   shorts1 hashtag: ['#Shorts', '#GreatDepression', '#FinancialHistory']
  OK   shorts2 başlık 47 krk · Same Box of Cash, Opposite Result: 1932 vs 2026
  OK   shorts2 yasaklı/clickbait/tavsiye: 0
  OK   shorts2 AI satırı + Not financial advice
  OK   shorts2 uzun videoya bağlantı yeri var (+ Studio related video adımı)
  OK   shorts2 hashtag: ['#Shorts', '#Inflation', '#FinancialHistory']
  OK   shorts1 başlığında bugün yok
[6] Pinli yorum
  OK   soru soruyor
  OK   tavsiye/clickbait/bugüne dönük: 0
[7] Thumbnail metni (≤4 kelime) + 168x94 okunurluk modeli (eşik ≥9 px büyük harf)
  OK   A: "ONE IS A DISASTER" · 4 kelime · 2 satır · büyük harf 141 px → 168x94'te 18.5 px
  OK   B: "THE SURPRISE DOOR" + damga ['1929'] · 4 kelime · 2 satır · büyük harf 107 px → 168x94'te 14.0 px
  OK   C: "STOCKS −89%" · 2 kelime · 2 satır · büyük harf 141 px → 168x94'te 18.5 px
       alternatifler ve rakip karşılaştırması (kapı değil, bilgi):
       A1: "PICK A DOOR" · 3 kelime · 2 satır · büyük harf 141 px → 168x94'te 18.5 px
       B2: "1929'S SURPRISE WINNER" · 3 kelime · 3 satır · büyük harf 94 px → 168x94'te 12.3 px
       C2: "$1,000 → $108" · 2 kelime · 2 satır · büyük harf 141 px → 168x94'te 18.5 px
       RAKIP-AILE1: "THE TRUE ORIGIN OF THE GREAT DEPRESSION: WHAT HISTORIANS GET WRONG" · 11 kelime · 3 satır · büyük harf 58 px → 168x94'te 7.6 px · bulgu [('clickbait', 'TRUE ORIGIN'), ('clickbait', 'GET WRONG'), ('clickbait', 'WHAT HISTORIANS')]
SONUÇ: 0 hata
```

**Okuma:**
- Başlık: 7/7 aday ≤60 krk ve 1929 içeriyor; puan sırası önerilen (T1) ve elenen (T5, T6) kararlarıyla tutarlı. Ölçüt puanları yargıdır [T]; betik yalnız tutarlılığı ve toplamı ölçer.
- Açıklama: ilk paragraf 149 krk, üç anahtar kelime içinde; yasal not birebir; AI satırı birebir; 10 kaynak; 3.143/5.000 bayt (lisans atıfları ve liste bağlantısı için ~1.800 bayt pay).
- Etiketler 373/500 (yükleme aracının sayım fonksiyonuyla).
- Yasaklı/clickbait/tavsiye: tüm metinlerde 0 (yasal notun "buy, sell or hold" cümlesi bilerek muaf). İlk koşuda pinli yorumda "should" (bonus soru) yakalandı → "do you want Leo to…" diye değiştirildi; betik sözcük düzeyinde bakar, anlam okuması elle yapıldı (G4 listesi).
- Thumbnail: 3 seçilen metin ≤4 kelime, model okunurluğu 14,0–18,5 px (eşik 9); rakip Aile 1 metni 7,6 px → eşik altı (karar gerekçesi, `thumb-konsept.md` §0).

## 9. Riskler ve F8'e açık işler
| Risk / iş | Sahibi | Not |
|---|---|---|
| Bölüm zamanları betik tahmini (143 kpm) | kurgu-editoru → youtube-paketleyici (F8) | TTS duraklamaları süreyi uzatır; F8'de gerçek zamanlarla değişir, betik yeniden koşar |
| Yasal not "Sources are listed below" ↔ kaynaklar notun üstünde | youtube-paketleyici (F8) | Öneri: LEGAL NOTE bloğunu SOURCES üstüne taşımak (§3 not) |
| Müzik/SFX atıfları | muzik-ses-tasarimcisi → youtube-paketleyici | `06-muzik/lisans-kaydi.md` gelince yer tutucu dolar |
| `durum.sentetik_medya` | monetizasyon-uyum-uzmani | F3 ön kararı true; F8 `politika-raporu.md` kararı pakete işlenir (karar benim değil) |
| Shorts "related video" API'de doğrulanmadı | koordinatör (`YAYIN.md` Studio adımı) | Studio → Short → Details → Related video |
| Shorts 2 başlığında "2026" | monetizasyon-uyum-uzmani (F8) | Karşılaştırma, hüküm değil; özel bakış istendi |
| Thumbnail C rakip Aile 1'e benzeyebilir | thumbnail-tasarimcisi (F8) | Yan yana testte karışırsa yedek fikir: Bank Leo kilitli kapı + "MARCH 1933" |
| Okunurluk eşiği (9 px) model varsayımı | thumbnail-tasarimcisi (F8) | Gerçek 168x94 küçültmeyle doğrulanır |
| "Made for kids" | monetizasyon-uyum-uzmani / youtube-paketleyici | `durum.cocuklara_ozel = false` (G8: yetişkin finans/tarih eğitimi) |
| Kategori | youtube-paketleyici (F8) | Öneri `27` Education (tarih + finans eğitimi; 25 News & Politics değil) |
