# F8 — Yayın paketi · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Hazırlayan:** youtube-paketleyici · **Tarih:** 2026-10-27 · **Durum:** KESİN METİN (F8 erken). Politika raporu YEŞİL (Z1 uygulandı: ana thumbnail A2), `sentetik_medya = true` kesin. Bekleyen tek şey: final video + Shorts dosyaları (F7) ile gerçek dry-run.
**Girdiler:** `paket-taslak.md` (F4, eleme gerekçeleri orada), `03-metin/metin.md` (KİLİTLİ), `03-metin/dogrulama.md` §4 (yasal not), `04-ses/sahne-zamanlari.json` (gerçek anlatım zamanları), `06-muzik/atif-satirlari.md`, `docs/yayin-takvimi.md`, `uretim/kanal-kimligi/kanal-paketi.json`.
**Tek kaynak:** JSON paketleri bu dosyadaki `<!-- veri:… -->` bloklarından `paket-uret.py` ile üretilir (elle kopyalama yok); `paket-kontrol.py` ikisini karşılaştırır (§10).
Etiketler: **[Ö]** betik ölçümü · **[T]** benim yargım · **[RÖ]** rakip-özet verisi.

**Kırmızı çizgiler (her metinde):** başlıkta yıl sınırı 1929; bugüne dönük "paranı nereye koy" hükmü yok; tavsiye/emir dili yok; rakip kalıbı ("real reason / true origin / get wrong") yok.

---

## 1. Başlık — 5 varyant (önerilen T1)

Arama ve öneri ayrı: ilk herkese açık video, trafik gözatma/önerili olacak [T] → başlık merak taşır; arama ifadeleri ("1929 stock market crash", "Great Depression") açıklamanın ilk satırında, bölümlerde ve etiketlerde. Tek vaat: başlık ("$1,000 in 1929, can you keep it?") = thumbnail (kapılar / kutu / −89 %) = ilk 15 sn ("You have one thousand dollars. Three doors…").

| # | Açı | Başlık | Krk [Ö] | Puan [Ö/T] | Karar |
|---|---|---|---|---|---|
| T1 | merak | You Have $1,000 in 1929. Can You Keep It? | 41 | **8.50** | **ÖNERİLEN** (hakem H5: sabit; Test & Compare'de tek değişken thumbnail) |
| T2 | karşıtlık | Stocks, a Bank or a Shoebox: Who Survived 1929? | 47 | 7.90 | yedek 1 |
| T4 | sonuç/arama | Surviving the 1929 Crash With $1,000: Three Doors | 49 | 7.70 | yedek 2 = soru işaretsiz alternatif; F12'de CTR düşükse ilk denenecek |
| T3 | karşıtlık | Stocks, a Bank or a Shoebox: $1,000 Through 1929 | 48 | 7.60 | yedek 3 |
| T7 | sonuç | $1,000 in 1929: The Door Everyone Laughed At Won | 48 | 7.10 | yedek 4 (cevaba yakın) |
| T5 | merak | 1929: The Smartest Door Was the Worst One | 41 | 6.80 | ELENDİ: para nesnesi yok (somut özne tavanı); Shorts 1 kancasıyla aynı vaat |
| T6 | sonuç | The Shoebox That Beat the Stock Market in 1929 | 46 | 6.40 | ELENDİ: "cash beats stocks" okuması (G4 en yakın); cevabı veriyor; yatırım-ipucu kitlesi çeker |

Puan = .30 merak + .20 arama + .20 thumbnail ile okunuş + .20 politika + .10 mobil. Ölçüt puanları yargı [T]; toplam ve sıra betikte [Ö].

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

**Başlık–thumbnail birlikte okunuş (finalistler, `thumbnail/thumb-rapor.md`; Test & Compare sırası A2, B1, D1; ana dosya A2):**
| Thumbnail | Metin | T1 ile birlikte okunuş | Videodaki karşılığı |
|---|---|---|---|
| **A2** `thumbnail/A2-kapilar.jpg` (ana) | ONE IS A DISASTER | Başlık soruyu sorar ("can you keep it?"), görsel bahsi koyar (üç kapı, biri felaket) → merak "hangisi?"; metin başlığı tekrar etmiyor | 0:09 "one door is a disaster" (ilk 15 sn = tek vaat) |
| **B1** `thumbnail/B1-kutu.jpg` | THE SURPRISE DOOR + "1929" damgası | Başlık para + yıl, görsel duygu (şaşkın Leo + kutu) → "sürpriz kapı hangisi?"; 1929 damgası başlığın çapasını tekrarlar (ikincil, 9,4 px) | anlatım "one is a surprise", 10:00 "SURPRISE" etiketi |
| **D1** `thumbnail/D1-kilitler.jpg` | EVERY DOOR LOCKED | Başlık "keep it?" sorusuna görsel cevap değil, gerilim: tüm kapılar kilitli → "o zaman para nerede?" | 7:33 bölüm adı "March 1933: every door locked", S17 zincir/kilit |
Elenen konsept C "STOCKS −89%" (F4) finale girmedi. T2/T3 (kapıları sayan) A2 ile kapıları iki kez anlatır → yedek başlık devreye girerse B1/D1 ile eşleştirilir. Üç metin ≤4 kelime, OCR ve 168x94 okunurluk thumbnail-tasarimcisi'nin ölçümünde (thumb-rapor.md); betik §10 [7] aynı metinleri okunurluk modeliyle tekrar ölçer.

<!-- veri:thumb-metin-secilen -->
```text
A2|ONE IS A DISASTER
B1|THE SURPRISE DOOR|1929
D1|EVERY DOOR LOCKED
```

---

## 2. Açıklamanın ilk 2 satırı (2 versiyon → B)

| Versiyon | Krk [Ö] | Anahtar ilk 150'de | Karar |
|---|---|---|---|
| A "It's 1929 and you have $1,000. Stocks, a bank or a shoebox: which door keeps your money through the stock market crash and the Great Depression?" | 144 | 3/3 ama "1929 stock market crash" bitişik değil, "stock market crash" ~100. karakterde; başlığı tekrar eder | elendi |
| **B** "The 1929 stock market crash as a game: you have $1,000 and three doors. Stocks, a bank or a shoebox. Which one gets you through the Great Depression?" | 149 | bitişik arama ifadesi 4. karakterde + Great Depression + $1,000 | **SEÇİLDİ** |

---

## 3. Açıklama (uzun video, kesin)

Düzen kararı (F4'teki açık iş): **LEGAL NOTE, SOURCES'ın üstüne taşındı** → yasal nottaki "Sources are listed below." artık doğru; notun metnine dokunulmadı. Bölümler `{BOLUMLER}` yer tutucusundan yükleme aracı tarafından "Chapters:" başlığıyla basılır (`metadata.bolumler`, §4). Oynatma listesi bağlantısı yok (liste bu videoyla açılır, bağlantı yükleme öncesi yok) → kanal bağlantısı; liste `oynatma_listesi_id` ile eklenir. Müzik satırları `06-muzik/atif-satirlari.md`'den aynen (zorunlu CC BY atfı yok; gönüllü teşekkür).

<!-- veri:aciklama -->
```text
The 1929 stock market crash as a game: you have $1,000 and three doors. Stocks, a bank or a shoebox. Which one gets you through the Great Depression?

Leo, our cartoon host, sends one player through each door, from the September 1929 market peak, through Black Monday and Black Tuesday (October 28–29, 1929), to the March 1933 bank holiday, using real data: the Dow, bank suspensions and consumer prices. Then we move the winning door to 2026 to see why the same math runs the other way.

Not financial advice. For educational purposes only.

{BOLUMLER}

LEGAL NOTE
This video is for education and entertainment only. It is not financial, investment, tax or legal advice. Leo is a fictional cartoon character, not a financial adviser. The "three doors" game is a simplified illustration of history: past results do not predict future results, and nothing here is a recommendation to buy, sell or hold any asset. Stock figures are price-only unless stated; inflation figures are U.S. CPI (BLS). Some scenes are illustrations, not historical footage. Sources are listed below. Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

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

MUSIC & SOUND
Music (CC0, OpenGameArt.org): "Catchy Swing" by Doge · "Ragtime! Jazz" by Tarush Singhal · "Tension" by Komiku · "The Fridge is Hungry" by congusbongus · "At the end of hope" by Emma_MA · "Unsolved Investigation" by isaiah658 · "Electro Swing type" by G_P · "Piano & Drums, positive melancholy" by Dizzy Crow
Sound effects (CC0): Kenney (kenney.nl), rubberduck, Nocturnal_Vanguard, PWL; additional music and sound design by Toonomy.

MORE FROM TOONOMY
New animated finance stories every week: https://www.youtube.com/@toonomy

#GreatDepression #StockMarketCrash #BlackTuesday
```

---

## 4. Bölümler — gerçek anlatım zamanlarından

Kaynak: `04-ses/sahne-zamanlari.json` (anlatim.wav, 631,63 sn). Her bölüm, o bölümü açan sahnenin gerçek `bas` zamanına (aşağı yuvarlanmış saniye) oturur; betik eşleşmeyi ölçer (§10 [3b]).

| Bölüm | Açan sahne | Sahne `bas` (sn) [Ö] | Zaman |
|---|---|---|---|
| The game: $1,000 and three doors | S01 | 0.00 | 00:00 |
| Door 1: The stock market | S05 | 79.71 | 01:19 |
| Door 2: The bank | S08 | 166.50 | 02:46 |
| Door 3: The shoebox | S12 | 286.47 | 04:46 |
| The bottom: July 1932 | S15 | 372.71 | 06:12 |
| March 1933: every door locked | S18 | 453.96 | 07:33 |
| The twist: the same door in 2026 | S20 | 522.88 | 08:42 |
| What the game really tests | S23 | 592.86 | 09:52 |

**KAYDIRMA UYARISI (kurgu-editoru → youtube-paketleyici):** zamanlar anlatım dosyasının 0 noktasına göredir. F7'de final videonun başına boşluk/soğuk açılış eklenirse veya sahneler arasına süre girerse **tüm bölümler aynı farkla kayar**; ilk bölüm yine **00:00** kalır (YouTube kuralı). F7 sonrası: `08-kurgu/kurgu-rapor.md`'deki ofset → bu blok güncellenir → `paket-uret.py` + `paket-kontrol.py` + `yukle.py --dry-run` yeniden koşar. Final video süresi 631,6 sn'den farklıysa betik uyarır.

<!-- veri:bolumler -->
```text
00:00 The game: $1,000 and three doors
01:19 Door 1: The stock market
02:46 Door 2: The bank
04:46 Door 3: The shoebox
06:12 The bottom: July 1932
07:33 March 1933: every door locked
08:42 The twist: the same door in 2026
09:52 What the game really tests
```

---

## 5. Etiketler ve hashtag'ler

Etiketler küçük sinyal (yazım varyantı/eş anlam); en özgül önde. Bugüne dönük yatırım ifadesi bilerek yok.

**2026-10-28 "Black" terimleri kararı (Niyazi sorusu):**
| Aday | Videoda var mı | Karar | Gerekçe |
|---|---|---|---|
| "Black Monday" / "Black Tuesday" (28–29 Eki 1929) | EVET, anlatım + ekran yazısı 02:11 (`final.en.srt`), dogrulama C07 [D] | **eklendi**: etiket (`black tuesday 1929`, `black monday 1929`), açıklama 2. paragraf, hashtag `#BlackTuesday` (`#FinancialHistory` yerine) | olayın gerçek adları; 29 Eki 2026 = 97. yıl dönümü |
| "Black Thursday" (24 Eki 1929) | HAYIR (anlatım 28 Eki'den başlar) | **yalnız etiket** (`black thursday 1929`); açıklama/hashtag'de yok | aynı çöküş haftasının adı, etiket konuyu doğru tanımlar; ama videoda işlenmeyen bir günü açıklamada vaat etmeyiz |
| "October 1929 crash" | EVET (Ekim çöküşü S06) | etiket | eş anlamlı arama ifadesi |
| "Black Friday" | HAYIR (27 Kas 2026 alışveriş günü; 1929 ile ilgisi yok) | **ELENDİ** | hashtag politikası (support 6390658): "Don't add hashtags that are not directly related to the video" → kaldırma riski; spam/yanıltıcı uygulamalar politikası (2801973) yanıltıcı meta veriyi yasaklar; YouTube "policy myths" (2011): ilgisiz etiket "misleading metadata" ihtarı alabilir; etiketlerin keşifteki rolü zaten "minimal" (support 146402). Getirisi ~0, riski kanal düzeyi (YPP öncesi). Ayrı video fikri trend-avcisi stokuna. |

<!-- veri:etiketler -->
```text
1929 stock market crash, stock market crash 1929, great depression, great depression explained, 1929 crash, wall street crash of 1929, black tuesday, black tuesday 1929, black monday 1929, black thursday 1929, october 1929 crash, bank runs, bank failures 1930s, bank holiday 1933, fdic history, deflation explained, dow jones 1929, financial history, economic history, stock market history, animated history, finance animation, toonomy
```

<!-- veri:hashtagler -->
```text
#GreatDepression #StockMarketCrash #BlackTuesday
```

**Kategori:** 27 Education · **Dil:** en / en · **Çocuklara özel:** hayır (yetişkin finans/tarih eğitimi) · **Lisans:** standart YouTube · **Yerleştirme:** açık.

---

## 6. Shorts paketleri

**Uzun videoya bağlantı:** Shorts "Related video" alanının Data API karşılığı doğrulanmadı → **Studio adımı** (`YAYIN.md`): uzun video 1 Kasım'da herkese açık olunca, her Short'un yayın saatinden önce Studio → Short → Ayrıntılar → **Related video** → "You Have $1,000 in 1929. Can You Keep It?". Açıklamaya uzun videonun URL'si yazılmadı: video ID yüklemeden önce yok, yer tutucu metnin yanlışlıkla yayınlanma riski var. Onun yerine uzun videonun **başlığı + kanal bağlantısı** (sabit, bozulmaz) [T]. Shorts açıklama bağlantıları zaten tıklanabilir olmayabilir; asıl köprü Related video.

### Shorts 1 — "Pick a door" (seçildi: a)
| Aday | Başlık | Krk | Karar |
|---|---|---|---|
| **a** | $1,000 in 1929: Which Door Would You Pick? | 42 | SEÇİLDİ: yorum sorusu, kancayı tekrar etmiyor |
| b | In 1929, the Smartest-Looking Door Was the Worst | 48 | elendi: kancanın aynısı |

<!-- veri:shorts1-baslik -->
```text
$1,000 in 1929: Which Door Would You Pick?
```

<!-- veri:shorts1-aciklama -->
```text
It's 1929 and you have $1,000: the stock market, a bank or a shoebox under your bed. Here's the scoreboard by July 1932, and why falling prices decided it.

Full game, all three doors from 1929 to 1933 plus the 2026 twist: "You Have $1,000 in 1929. Can You Keep It?" on our channel, https://www.youtube.com/@toonomy

Sources: Federal Reserve History; FDIC, A Brief History of Deposit Insurance; U.S. BLS CPI via FRED (CPIAUCNS). Stock figure is price only, before dividends.
Music: "Catchy Swing" by Doge (CC0, OpenGameArt.org).

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #GreatDepression #FinancialHistory
```

### Shorts 2 — "Same box, opposite result" (seçildi: a)
| Aday | Başlık | Krk | Karar |
|---|---|---|---|
| **a** | Same Box of Cash, Opposite Result: 1932 vs 2026 | 47 | SEÇİLDİ: karşılaştırma, hüküm değil |
| b | Why Cash Got Stronger in 1932 (and Weaker in 2026) | 50 | elendi: "cash weaker in 2026" → "cash is trash" okumasına yakın |

"2026" bu Short'un içeriği (karşılaştırma) olduğu için doğru; hüküm yok. Monetizasyon-uyum-uzmani'nin F8'de özel bakması istendi.

<!-- veri:shorts2-baslik -->
```text
Same Box of Cash, Opposite Result: 1932 vs 2026
```

<!-- veri:shorts2-aciklama -->
```text
From September 1929 to July 1932, U.S. consumer prices fell about 21%, so a shoebox of cash bought more. In the 12 months to September 2026, prices rose 3.7%. Same box, opposite result. That's arithmetic, not a plan.

The full 1929 game, with all three doors: "You Have $1,000 in 1929. Can You Keep It?" on our channel, https://www.youtube.com/@toonomy

Sources: U.S. BLS CPI-U (CPIAUCNS) via FRED; BLS CPI news release, October 14, 2026 (not seasonally adjusted).
Music: "Electro Swing type" by G_P (CC0, OpenGameArt.org).

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inflation #FinancialHistory
```

---

## 7. Pinli yorum (A seçildi; B elendi: videonun sonunu izlemiş olmayı varsayıyor)

Bugüne dönük "paranı şimdi nerede tutuyorsun?" sorusu bilerek yok (yorumları kişisel yatırım tartışmasına çeker). Yorumların yanıt taslakları: `yorum-yanitlari.md` (gönderimi Niyazi onaylar).

<!-- veri:pinli-yorum -->
```text
It's September 1929 and you can't see the future. Which door do you walk through: the stock market, the bank or the shoebox? Tell us why in one sentence.

Bonus: which money crisis from history do you want Leo to turn into the next game?

(Sources and data notes are in the description.)
```

---

## 8. Uç ekran, kart, oynatma listesi

- **Uç ekran:** son sahne S24 gerçek başlangıcı **10:18.4**, anlatım sonu 10:31.6 → uç ekran **~13 sn** (YouTube 5–20 sn; metin planı 17 sn idi, gerçek ses kısaldı). Öğeler: **abone** + **video: "Best for viewer"** (kanalda başka herkese açık video yok). Leo'nun sağı boş (S24 planı). F7'de video sonu uzarsa uç ekran 20 sn'ye kadar genişletilir. Weimar videosu yayınlanınca video öğesi ona çevrilir.
- **Kart:** yok (tek video; kanal içi hedef yok). İkinci A videosu yayınlanınca kart S14'e (≈5:52–6:12, kutu bölümünün kapanışı, bölüm geçişi öncesi) konur.
- **Oynatma listesi:** **A · Geçmiş → "The Collapse: Financial History Explained"** (bu video listeyi açar; F11'de `tools/yayin/kanal.py`, sonra `oynatma_listesi_id` pakete). Shorts → "Money Stories in 60 Seconds | Shorts". "Start Here" 3 sütundan birer video olunca.

---

## 9. Takvim ve durum alanları

- **Slot (takvim v2, Pazar 12:00 ET, A sütunu):** en yakın uygun Pazar **2026-11-01 12:00 ET**. ABD 1 Kasım 02:00'de kış saatine geçer → 12:00 **EST (UTC−5)** = 17:00 UTC = **20:00 TRT**. Şart: hakem ONAY + Niyazi onayı slottan ≥3 sa önce (01.11 17:00 TRT). Yetişmezse yedek **2026-11-08 12:00 ET** (aynı ofset) — koordinatör `yayin_zamani`'yı değiştirir.
- **Shorts:** Shorts-1 **Pzt 2026-11-02 09:00 ET** (14:00 UTC, 17:00 TRT), Shorts-2 **Sal 2026-11-03 09:00 ET**. Uzun video kayarsa Shorts da aynı farkla kayar (uzun videodan önce asla).
- **`durum.sentetik_medya` = true (KESİN):** monetizasyon-uyum-uzmani'nin kararı, `09-paket/politika-raporu.md` §4 (3 paket). Karar benim değil; pakete işlendi. Açıklamadaki AI satırı her durumda kalır.
- **`gizlilik` = private + `yayin_zamani`** (planlı yayın), `onay.niyazi_onayi` = false (F10'a kadar).
- **Dosya yolları** `../08-kurgu/…` (SRT: `final.en.srt`) ve `../09-paket/thumbnail-A.png` biçiminde: `09-paket/` ve `teslim/` kardeş klasör olduğu için paket iki yerden de aynı dosyaları bulur. Ana thumbnail **`../09-paket/thumbnail/A2-kapilar.jpg`** (politika raporu Z1); B1 ve D1 Studio'da Test & Compare'e eklenir (API'de karşılığı yok → `YAYIN.md` Studio adımı).

## 10. Test kapısı

Betikler: `paket-uret.py` (bloklar → 3 JSON), `paket-kontrol.py` (metin kuralları + JSON tutarlılığı + bölüm↔sahne eşleşmesi), `tools/yayin/yukle.py --dry-run` (3 paket). Gerçek final dosyalar F7'de geleceği için dry-run iki kipte koşuldu: (1) gerçek paketler → yalnız "video/thumbnail yok" hataları beklenir; (2) aynı paketlerin geçici kopyası, ffmpeg ile üretilmiş sahte 16:9 631,6 sn / 9:16 57 sn video + 1280x720 thumbnail ile → metadata, bölüm, süre, Shorts ve zamanlama kuralları 0 hata olmalı. Çıktılar `kapi-cikti.txt`'de.

### 10.1 Çıktı özeti (tam çıktı `kapi-cikti.txt`, 2026-10-27)
- **2026-10-28 "Black" terimleri güncellemesi (§5 karar tablosu):** `paket-uret.py` → `paket-kontrol.py` **0 hata** (etiket 23 adet 457/500, hashtag `#GreatDepression #StockMarketCrash #BlackTuesday`, ilk paragraf 149 krk değişmedi); `yukle.py --dry-run` 09-paket + teslim 6/6 **0 hata 0 uyarı** (10/7/7). Başlık ve Shorts metinleri değişmedi; teslim/ JSON'ları 09-paket ile aynı. Yükleme yok.
- **GERÇEK dry-run (F7 final, ofset 0):** `final-16x9.mp4` 1920x1080 631,6 sn, `final.en.srt` 228 blok, A2 thumbnail; `shorts-1.mp4` 1080x1920 49,6 sn; `shorts-2.mp4` 1080x1920 56,0 sn → **3 paket 0 hata 0 uyarı (10/7/7), exit 0**. SRT yolu `altyazi.srt` → `final.en.srt` (kurgu adı) düzeltildi. `paket-kontrol.py` 0 hata (sha256 `320251ea…`, değişmedi). Studio adımları: `YAYIN.md`.
- **Z1 sonrası yeniden koşu (politika raporu YEŞİL):** ana thumbnail `thumbnail/A2-kapilar.jpg` (1280x720 jpeg, 131 KB, araç ölçümü). `paket-kontrol.py` 0 hata, 2 koşu sha256 aynı (`320251ea…`); [7] finalist metinleri A2 18,5 px · B1 14,0 px · D1 16,8 px (eşik 9); [8] JSON thumbnail = A2 ve dosya var. Dry-run kip 1: thumbnail artık OK, yalnız video/SRT yok (F7); kip 2: 3 paket 0 hata 0 uyarı (10/7/7). Aşağıdaki maddeler ilk koşudur.
- `paket-kontrol.py`: **0 hata, exit 0**; 2 koşu sha256 aynı (`130d7ce7…`). Başlıklar 41–49 krk; ilk paragraf 149 krk, 3 anahtar ilk 150'de; yasal not + AI satırı birebir; LEGAL NOTE kaynakların üstünde; müzik atfı aynen; yer tutucu 0; 8 bölümün her biri açan sahnenin gerçek `bas` zamanının ≤1 sn önünde (fark −0,47…−0,96 sn, aşağı yuvarlama); etiketler 373/500; Shorts başlık 42/47 krk; pinli yorum yasaklı 0; JSON ↔ paket.md birebir (başlık, açıklama, bölüm, etiket, zaman, `sentetik_medya` true, onay false).
- İlk koşu 1 hata verdi: müzik atfındaki eser adları ("Unsolved **Invest**igation", "Ragtime**!** Jazz") tavsiye/clickbait desenine takıldı → atıf satırları yasal not gibi aynen-muaf yapıldı (üçüncü taraf eser adı değiştirilemez).
- `yukle.py --dry-run`, kip 1 (gerçek paketler): yalnız beklenen dosya-yok hataları (uzun: video/thumbnail/SRT; Shorts: video), metadata kontrolleri geçti, exit 2.
- `yukle.py --dry-run`, kip 2 (bayt bayt aynı paketler + sahte medya): **3 paket 0 hata 0 uyarı** (uzun 10, Shorts 7+7 kontrol); tam açıklama 3.370 / 782 / 771 bayt; bölümler kurallara uygun; SRT 228 blok 631,6 sn; publishAt 2026-11-01T17:00Z / 11-02T14:00Z / 11-03T14:00Z; `containsSyntheticMedia: true`. Ağ çağrısı yok, yükleme yok.
- **F7 sonrası tekrar:** gerçek dosyalarla kip 1 → 0 hata olmalı (Shorts ≤60 sn ve dikey, final ≥600 sn, son bölüm video süresinden önce).

## 11. Açık işler
| İş | Sahibi | Not |
|---|---|---|
| Final video, SRT, 2 Shorts | kurgu-editoru (F7) | gelince gerçek dry-run 0 hata koşulur; ofset varsa §4 kayar |
| Test & Compare (A2, B1, D1) | koordinatör → `YAYIN.md` Studio adımı | ana dosya A2 JSON'da |
| Shorts Related video, uç ekran, SRT, oynatma listesi | koordinatör → `YAYIN.md` Studio adımları | API karşılığı doğrulanmadı |
| Yorum yanıtları | Niyazi onayı ile | `yorum-yanitlari.md` |
