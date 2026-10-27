# F3 — Tam metin · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Kanal:** Toonomy (@toonomy) · **Anlatıcı:** Leo (kurgusal çizgi maskot, oyun sunucusu; danışman değil) · **Ses:** Kokoro `am_fenrir` 0.9 (≈143 kelime/dk ölçüldü)
**Sütun:** A (tarih) · **Yazar:** senaryo-yazari · **Tarih:** 2026-10-27 · **Sürüm:** v1 (metin kilidi öncesi; F3 doğrulama + politika denetimine gider)
**Kaynak kodları:** her rakamın yanında `[KOD]` var; liste §7'de. Etiketler: **[D]** birincil kaynakta bu çalışmada okundu · **[H]** `veri/hesap.py` ile hesap · **[AÖ]** arama özeti / ikincil aktarım (doğrulayıcı onayı gerekir).
**Kapı betiği:** `03-metin/metin-kontrol.py` (çıktısı §13'te). Zamanlar betikten gelir: kelime ÷ 143 kpm.

**Yazım kuralı (TTS için):** ANLATIM sütununda bütün sayılar **okunduğu gibi yazıyla** yazılır ("nineteen twenty-nine", "one thousand dollars"). Böylece kelime sayısı = okunan süre, Kokoro'nun rakam okuma belirsizliği de ortadan kalkar. Rakamın kendisi GÖRSEL sütunundadır.

---

## 1. İlk 30 sn planı

| Zaman | Ne söylenir | Ne görünür | Amaç |
|---|---|---|---|
| 0:00–0:03 | "It's September nineteen twenty-nine." | Siyah değil, doğrudan sepya 1929 sokak kartı → **≤3 sn'de kesme** stüdyoya: üç dev kapı ışıkla açılır (H3) | Somut zaman + yer; logo/intro/"hi guys" YOK |
| 0:03–0:09 | "You have one thousand dollars. Three doors: the stock market, a bank, or a shoebox under your bed." | Ekrana "$1,000" düşer; kapılar tek tek yanar: mavi STOCKS, yeşil BANK, kahve SHOEBOX | Somut özne: 1.000 $ + 3 fiziksel kapı |
| 0:09–0:17 | "By nineteen thirty-three, one door is a disaster, one is a gamble, and one is a surprise. Let's play." | Kapıların üstünde üç soru işareti → "DISASTER? / GAMBLE? / SURPRISE?" etiketleri karışık sırayla dönüp durur | **Net vaat** + 3 parçalı açık döngü (hangisi hangisi?) |
| 0:17–0:41 | Leo kendini sunucu ve çizgi karakter olarak tanıtır; "Where was money safe in nineteen twenty-nine?" (P3); "which door won, why it won, and why the same math runs the other way today" | Leo sunucu kürsüsünde; 1929 ↔ 2026 takvim yaprağı | Neden önemli + videonun sonunda ne öğrenileceği (sona kadar açık döngü) |
| 0:41–1:06 | **Tez (Ö1), 0:41–0:50:** "Here's the idea this game will test: a safe place for money isn't really a place. It depends on what prices are doing." → 1.000 $ = 1929'da ~8 aylık ücret [BEA-666] | Tez cümlesi ekranda tek satır → maaş zarfı grafiği G0 | Özgün tez ilk 60 sn'de + kişisel bağ |

Abone/beğeni çağrısı ilk 60 sn'de **yok** (ilk ve tek çağrı 5:12–5:20, ilk büyük ödül S10'dan hemen sonra; betik ölçümü §13).

---

## 2. TAM METİN (iki sütun)

Biçim: her sahne `### Sxx · başlangıç–bitiş · süre` + iki sütunlu tablo. GÖRSEL sütununda: **Sahne** (mekân/kamera), **Grafik** (veri + kaynak), **Leo** (poz/ifade; paket-v1 pozları: konuşma, işaret, şaşkın, düşünen, sevinçli), **Ekran** (ekran yazısı), **Etiket** ("Illustration" gerekip gerekmediği), **↺** (yeniden kanca).
Renk kodu bütün videoda sabit: **mavi = borsa kapısı, yeşil = banka, kahve = ayakkabı kutusu**; sunucu Leo sıcak sahne ışığında, 1929–33 sokakları soğuk sepya.
Leo'nun klonları (Stock Leo, Bank Leo, Box Leo) aynı karakterin renkli yaka kartlı kopyalarıdır; **sunucu Leo hiçbir zaman kaybetmez** (H2).

## Bölüm 1 — The Game

### S01 · 0:00–0:17 · 17 sn · HOOK
| ANLATIM | GÖRSEL |
|---|---|
| It's September nineteen twenty-nine. You have one thousand dollars. Three doors: the stock market, a bank, or a shoebox under your bed. By nineteen thirty-three, one door is a disaster, one is a gamble, and one is a surprise. Let's play. | **Sahne:** 0:00 sepya 1929 New York sokağı (tek kare, yavaş zoom), 0:02'de whoosh ile sıcak ışıklı yarışma stüdyosu; üç dev kapı (mavi/yeşil/kahve). **Leo:** sunucu, kürsü arkasında, kameraya bakan konuşma pozu; "Let's play"de iki eliyle kapıları gösterir. **Ekran:** "$1,000" · "SEPT 1929" · kapı levhaları STOCKS / BANK / SHOEBOX · "DISASTER? GAMBLE? SURPRISE?" **Etiket:** sokak karesi gerçekçi üretilirse "Illustration" (P5); stüdyo muaf. |

### S02 · 0:17–0:41 · 23 sn
| ANLATIM | GÖRSEL |
|---|---|
| I'm Leo, and tonight I'm your host. I'm a cartoon, so nobody in this studio loses real money. The people of nineteen twenty-nine did. Their question was simple: where was money safe in nineteen twenty-nine? By the end, you'll know which door won, why it won, and why the same math runs the other way today. | **Sahne:** stüdyo orta plan; arkada dev takvim yaprağı "1929" çevrilir → bir anlığına "2026" görünür → geri "1929". **Leo:** göğsünü işaret eder ("I'm Leo"), sonra omuz silker gibi gülümser ("I'm a cartoon"). **Ekran:** "WHERE WAS MONEY SAFE IN 1929?" · sonda üç madde belirir: "WHICH DOOR WON · WHY · WHY IT FLIPS TODAY". **↺ 0:32** "By the end, you'll know which door won" (vaat → sona kadar açık döngü). |

### S03 · 0:41–1:06 · 26 sn
| ANLATIM | GÖRSEL |
|---|---|
| Here's the idea this game will test: a safe place for money isn't really a place. It depends on what prices are doing. Now, how big is this thousand dollars? In nineteen twenty-nine, an average full-time worker earned about one thousand four hundred thirty dollars a year. So this is roughly eight months of pay. You don't want to lose it. | **Grafik G0:** maaş zarfı çubuğu "AVG. FULL-TIME PAY, 1929: $1,430/yr" [BEA-666] → 12 ay kutusundan 8'i dolar: "$1,000 ≈ 8 MONTHS" [H]. Kaynak etiketi ekranda: "Source: BEA, NIPA Table 6.6A". **Leo:** tez cümlesinde kameraya bakar, ciddi; maaş kısmında düşünen poz. **Ekran:** önce tez tek satır: "SAFE ISN'T A PLACE. IT DEPENDS ON PRICES." |

### S04 · 1:06–1:35 · 29 sn
| ANLATIM | GÖRSEL |
|---|---|
| Here are the rules. You can't switch doors. You can't see the future. Each door gets a player. Stock Leo takes the blue door. Bank Leo takes the green door. And Box Leo takes the brown one, holding an actual shoebox. The studio audience laughs at Box Leo. Remember that laugh. Door one goes first, and in nineteen twenty-nine, it looks like the smartest choice in the room. | **Sahne:** kural kartları ekrana çakılır (pop SFX). Üç klon sırayla kapılarına yürür; yaka kartları STOCK / BANK / BOX. Box Leo kutuyu kucaklar, seyirci kahkahası SFX. **Leo (sunucu):** işaret pozu, "Remember that laugh"te göz kırpar. **Ekran:** "RULE 1: NO SWITCHING · RULE 2: NO CRYSTAL BALL". **Kritik yol (H4):** 3 klonlu kapı sahnesi F5 testine girer; B planı: tek Leo kapıdan kapıya yürür, klonlar skor tablosunda ikon. **↺ 1:31** "it looks like the smartest choice in the room" (neden? → Bölüm 2). |

## Bölüm 2 — Door One: The Stock Market

### S05 · 1:35–2:14 · 39 sn
| ANLATIM | GÖRSEL |
|---|---|
| To see why, look at the last eight years. In August nineteen twenty-one, the Dow Jones Industrial Average stood at sixty-three. By September nineteen twenty-nine, it was at three hundred eighty-one. That's six times higher. Ordinary people, not just bankers, were putting their savings in. Many didn't even pay the full price. They put down a part, typically ten percent, and borrowed the rest. Stock Leo walks through the blue door on September third. That day, the Dow closes at three hundred eighty-one point one seven. It's the top. Nobody knows it yet. | **Sahne:** mavi kapı açılır → sepya 1929 borsa salonu dışı, kâğıt şerit (ticker tape) yağmuru. **Grafik G1a (kendi grafiğimiz, mavi):** Dow kapanış çapaları Ağu 1921 = 63 → 3 Eyl 1929 = 381.17, "×6" etiketi [FRH-29]. **Leo (Stock Leo):** sevinçli poz, ticker şeridini havaya atar. **Ekran:** "1921: 63 → 1929: 381" · "TYPICALLY 10% DOWN, 90% BORROWED" [FRH-29] · "SEPT 3, 1929: 381.17". "Source: Federal Reserve History". **Etiket:** sokak/salon gerçekçi ise "Illustration". **↺ 2:12** "Nobody knows it yet" (dramatik ironi; müzik keser). |

### S06 · 2:14–2:48 · 34 sn
| ANLATIM | GÖRSEL |
|---|---|
| For a few weeks, nothing much happens. Then October arrives. On Monday, October twenty-eighth, the Dow falls nearly thirteen percent in a single day. On Tuesday, it falls almost twelve percent more. People will call them Black Monday and Black Tuesday. The borrowed money makes it worse. When prices drop, lenders want their loans covered, so people sell, and prices drop again. By mid-November, the Dow has lost almost half its value. Stock Leo's one thousand dollars is now about five hundred. | **Sahne:** takvim yaprakları hızla kopar (Eyl → Eki). Kırmızı değil, soğuk mavi-gri ton; büyük sayı grafikleri. **Grafik G1b:** iki çubuk "OCT 28: −13% · OCT 29: −12%" [FRH-29]; G1a çizgisi Kasım ortasına "almost half" bandına iner. 1.000 $ sayacı 1,000 → ~500 sayarak düşer [FRH-29, H]. **Leo (Stock Leo):** şaşkın poz, ticker şeridi elinde gevşer (komik ama yetişkin tonda; panik/şiddet görseli yok). **Ekran:** "BLACK MONDAY −13% · BLACK TUESDAY −12%" · "$1,000 → ~$500". |

### S07 · 2:48–3:10 · 21 sn
| ANLATIM | GÖRSEL |
|---|---|
| Half gone in about ten weeks. That hurts. But Stock Leo stays calm. He thinks this is a dip, and dips come back. Over at the green door, Bank Leo is even calmer. His money sits in a bank, with a vault and a marble floor. That's the safe door. Right? | **Sahne:** bölünmüş ekran: solda Stock Leo, kendini rahatlatan nefes; sağda yeşil kapı açılır, mermer zeminli banka içi, dev kasa kapısı. **Leo (Bank Leo):** kollar kavuşturmuş, kendinden emin gülümseme. **Ekran:** "−50% IN ~10 WEEKS" · "Right?" yazısı ekranda hafifçe sallanır. **↺ 3:08** "That's the safe door. Right?" (soru → Bölüm 3). Müzik: tek notalık gerilim vuruşu. |

## Bölüm 3 — Door Two: The Bank

### S08 · 3:10–3:47 · 37 sn
| ANLATIM | GÖRSEL |
|---|---|
| Here's the part that surprises people today. In nineteen twenty-nine, a bank account in America had no federal deposit insurance. If your bank closed, nobody promised you'd get your money back. And there were a lot of banks. When the trouble began, over eight thousand banks belonged to the Federal Reserve System, and nearly sixteen thousand did not. Many were small and local. For a year, Bank Leo is fine. Then, in late nineteen thirty, banks start to fail in waves. Within a few weeks, hundreds close their doors. | **Sahne:** stüdyo; sunucu Leo büyük boş bir "INSURANCE" kutucuğunu işaret eder, kutucuk boş kalır. Sonra ABD haritası: küçük banka noktaları (≈24.000) yanar [FRH-BP]. 1930 sonu: noktalar dalga dalga söner. **Leo (sunucu):** işaret pozu; Bank Leo arka planda gazetesini indirir. **Ekran:** "1929: NO FEDERAL DEPOSIT INSURANCE" [FDIC-BH3] · "8,000+ IN THE FED SYSTEM · ~16,000 OUTSIDE" [FRH-BP]. "Source: Federal Reserve History". |

### S09 · 3:47–4:26 · 39 sn
| ANLATIM | GÖRSEL |
|---|---|
| On December eleventh, nineteen thirty, the fourth-largest bank in New York City, the Bank of United States, stops operating. Picture the street outside. A long line of people, all asking for their money at the same time. Here's the problem. A bank doesn't keep your thousand dollars in a box with your name on it. It lends most of it out. So when everyone comes at once, even a healthy bank can run out of cash. And when one bank falls, people at the next bank get nervous, and the line moves there. | **Sahne:** sepya banka önü, kuyruk (yüzler stilize, gerçek kişi yok; logo/tabela gerçek değil, isim yalnız ekran yazısında). **Mekanizma animasyonu (kendi):** 10 madeni para kasaya girer, 9'u "LOANS" okuyla dışarı akar, 1'i kalır; kuyruk 10 kişi olunca kasa boşalır. Sonra kuyruk ok ile yan bankaya kayar. **Leo (Bank Leo):** kuyrukta, saatine bakar (kol saati sol bilekte). **Ekran:** "DEC 11, 1930: BANK OF UNITED STATES CLOSES" [FRH-BP] · "BANKS LEND MOST DEPOSITS OUT". **Etiket:** kuyruk sahnesi gerçekçi ise "Illustration" (Ö11). **↺ 4:03** "Here's the problem" (mekanizma sorusu). |

### S10 · 4:26–5:12 · 46 sn · İLK BÜYÜK ÖDÜL
| ANLATIM | GÖRSEL |
|---|---|
| Now the score for door two. It isn't one number. It's two. From nineteen thirty to nineteen thirty-three, about nine thousand banks suspended operations. That's more than one bank in three. Some reopened within a few months. Most were closed for good. If your bank was one of them, the FDIC's own numbers show depositors lost about twenty cents of every dollar, on average. For Bank Leo, that's around two hundred dollars gone, and he might wait a long time for the rest. If your bank survived, you kept everything. That's why door two is the gamble. It all depends on which bank you picked, and nobody could see inside. | **Grafik G2 (kendi grafiğimiz, yeşil, birincil veri):** yıllık ticari banka askıya almaları 1921–1933 çubukları: 506 · 366 · 646 · 775 · 617 · 975 · 669 · 498 · 659 · **1,350 · 2,293 · 1,453 · 4,000** [FDIC-BH3 Tablo 5]; 1930–33 çubukları vurgulanır, toplam "≈9,100" [H]. İkinci katman: "LOST BY DEPOSITORS IN SUSPENDED BANKS: ~20¢ PER $1" (1,34 milyar $ / 6,83 milyar $) [FDIC-BH3, H]. "Source: FDIC, A Brief History of Deposit Insurance, Table 5". **Leo (Bank Leo):** kasa önünde, 1.000 $ sayacı ikiye ayrılır: "BANK SURVIVED: $1,000" ‖ "BANK SUSPENDED: ~$800 + WAIT". **Ekran:** "1930–33: ~9,000 BANKS SUSPENDED" · "GAMBLE" damgası (mühür SFX). **↺ 4:29** "It isn't one number. It's two." (iki sonuçlu cevap). |

### S11 · 5:12–5:32 · 20 sn · ABONE (kısa) + yeniden kanca
| ANLATIM | GÖRSEL |
|---|---|
| Quick pause. If you like history played as a game, subscribing helps Leo build the next one. Now, back to the studio. One door is still closed. Box Leo. The one everybody laughed at. He hasn't touched his money once. And something strange is happening to it. | **[ABONE]** küçük alt köşe abone düğmesi animasyonu (3 sn, ses yok; logo animasyonu yok). **Sahne:** stüdyo; spot ışığı kahve kapıya kayar; Box Leo kutuyu kulağına tutup sallar. **Leo (sunucu):** konuşma pozu, sonra kaşlarını kaldırır. **Ekran:** "DOOR 3" · kutunun üstünde "?" **↺ 5:29** "something strange is happening to it". |

## Bölüm 4 — Door Three: The Shoebox

### S12 · 5:32–6:07 · 35 sn
| ANLATIM | GÖRSEL |
|---|---|
| Box Leo's thousand dollars never changes. Same stack of bills, every morning. But the world around the box does change. Prices are falling. Not just a few prices. The average price of what families buy. The official price index shows it. From September nineteen twenty-nine to July nineteen thirty-two, consumer prices fell by about twenty-one percent. So the same thousand dollars now buys what about one thousand two hundred seventy dollars bought in nineteen twenty-nine. Box Leo did nothing, and his money got stronger. | **Grafik G3 (kendi grafiğimiz, kahve, birincil veri):** ABD TÜFE aylık, Eyl 1929 = 17.3 → Tem 1932 = 13.6 → Mar 1933 = 12.6 (FRED `CPIAUCNS`, BLS) [FRED-CPI]; ikinci eksen: 1.000 $'ın 1929 fiyatlarıyla alım gücü 1,000 → 1,272 → 1,373 [H]. "Source: BLS CPI via FRED (CPIAUCNS)". **Sahne:** dükkân vitrininde genel fiyat etiketleri tek tek küçülür (ürün ikonları temsili; tek tek ürün fiyatı iddiası yok). **Leo (Box Leo):** kutudaki banknotlar hafifçe parlar, Box Leo şaşkın → sevinçli. **Ekran:** "PRICES −21% (SEPT 1929 → JULY 1932)" · "$1,000 BUYS LIKE $1,272". |

### S13 · 6:07–6:44 · 37 sn
| ANLATIM | GÖRSEL |
|---|---|
| Why were prices falling? Fewer jobs meant less spending. And money itself was shrinking. Federal Reserve History says the money supply fell by nearly thirty percent from the fall of nineteen thirty to the winter of nineteen thirty-three. Less money for the same goods means lower prices. Here's the strange part. While banks were failing, people across the country did exactly what Box Leo did. They pulled cash out and kept it at home. One shoebox looks safe. A whole country of shoeboxes made the banks weaker. | **Grafik G3b (kendi):** "MONEY SUPPLY: −~30% (FALL 1930 → WINTER 1933)" basit iki sütun [FRH-GD]. **Sahne:** harita üzerinde binlerce minik kutu belirir, her kutu belirdiğinde bir banka noktası söner (mekanizma görseli). **Leo (sunucu):** düşünen poz → "Here's the strange part"ta kameraya döner. **Ekran:** "ONE BOX ✓ · A COUNTRY OF BOXES ✗" (sayısız) [FDIC-BH3: "widespread attempts to convert deposits to cash"]. "Source: Federal Reserve History; FDIC". **↺ 6:27** "Here's the strange part" (iç ters köşe). |

### S14 · 6:44–7:09 · 25 sn
| ANLATIM | GÖRSEL |
|---|---|
| So Box Leo is the champion? Not so fast. A shoebox has its own traps. It earns nothing. It can burn. It can be stolen. And if you lose your job, you spend it, bill by bill, until the box is empty. Box Leo still has to survive the hardest moment of the whole game. Let's jump to the bottom. | **Sahne:** dört tuzak kartı hızla çevrilir: "0% INTEREST" · "FIRE" (çizgi alev ikonu) · "THEFT" (gölge el) · "JOB LOSS" (banknotlar tek tek uçar). **Leo (Box Leo):** kutuya sarılır, gözleri kısılır. **Ekran:** "NOT SO FAST". **↺ 7:03** "survive the hardest moment… Let's jump to the bottom" → Bölüm 5. SFX: rüzgâr + düşüş tonu. |

## Bölüm 5 — The Bottom: July 1932

### S15 · 7:09–7:59 · 50 sn
| ANLATIM | GÖRSEL |
|---|---|
| July eighth, nineteen thirty-two. The Dow closes at forty-one point two two. From the top, that's a fall of about eighty-nine percent. Stock Leo's thousand dollars is now about one hundred and eight dollars. That's price only, before dividends. Even with falling prices, it buys only what about one hundred thirty-eight dollars bought in nineteen twenty-nine. Dividends did help, but look at the gap. So how long until he's back to one thousand? There are two answers, and they're far apart. The Dow's price didn't get back to its nineteen twenty-nine peak until November nineteen fifty-four. Counting dividends and falling prices, one well-known analysis puts the break-even point much earlier, in late nineteen thirty-six. Still, that's seven years of waiting. | **Grafik G1 tam (kendi, mavi):** Dow çapaları 63 (1921) → 381.17 (3 Eyl 1929) → ~yarı (Kas 1929) → **41.22 (8 Tem 1932)** → 381 (Kas 1954) [FRH-29]; 1.000 $ çizgisi 1,000 → ~500 → **108** [H]; gri ikinci çizgi "in 1929 prices: ~$138" [FRED-CPI, H]. Zorunlu alt not: **"Price only, before dividends."** (D1). 1954 noktasında küçük not: "Price index. With dividends + falling prices: break-even ~late 1936 (Hulbert, NYT 2009)" [HUL]. **Leo (Stock Leo):** düşünen poz, ciddi (aşağılanma yok). **Ekran:** "JULY 8, 1932: 41.22" · "−89%" · "$1,000 → $108 (PRICE ONLY)" · "BACK TO $1,000? ANSWER 1: 1954 (PRICE) · ANSWER 2: ~LATE 1936 (DIVIDENDS + FALLING PRICES)". **↺ 7:36** "So how long until he's back to one thousand?" (iki cevap). |

### S16 · 7:59–8:29 · 29 sn
| ANLATIM | GÖRSEL |
|---|---|
| Here's the scoreboard in July nineteen thirty-two. Stock Leo: about one hundred and eight dollars, on price alone. Bank Leo: a question mark. Maybe all of it, maybe around eight hundred, maybe still waiting. Box Leo: one thousand dollars that buy like twelve hundred seventy. Every result on this board belongs to that decade. A decade when prices were falling. That's what made a pile of cash look so clever. | **Grafik G4 skor tablosu (kendi infografik):** üç sütun, renk kodlu. STOCK: "$108 (price only)" [FRH-29, H] · BANK: **risk simgesi "?"** + alt satır "if your bank suspended: avg. ~$800 left" [FDIC-BH3, H] (D3: tek bir "kesin" rakam yok, koşullu ortalama) · BOX: "$1,000 = $1,272 of 1929 goods" [FRED-CPI, H]. Tablonun altında şerit: "IN A DECADE OF FALLING PRICES" (D7). **Leo (sunucu):** sunum pozu, skor tablosunun yanında. |

### S17 · 8:29–8:37 · 8 sn · yeniden kanca
| ANLATIM | GÖRSEL |
|---|---|
| But the game isn't over. It ends in March nineteen thirty-three. And March is when every door gets locked. | **Sahne:** üç kapıya sırayla zincir + asma kilit iner (metal SFX ×3). **Leo (sunucu):** şaşkın poz. **Ekran:** "MARCH 1933". **↺ 8:35** "every door gets locked". |

## Bölüm 6 — March 1933: Every Door Locked

### S18 · 8:37–9:31 · 55 sn
| ANLATIM | GÖRSEL |
|---|---|
| Winter, nineteen thirty-three. Panic jumps from state to state. Visitors who come to Washington for the new president's first day find notes in their hotel rooms: checks from out-of-town banks won't be accepted. By March fourth, every state has declared a bank holiday. Two days later, the new president, Franklin Roosevelt, closes every bank in the nation. Good banks and bad banks, all shut. Bank Leo stands at a locked door. For a few days, cash at home is suddenly very useful, and Box Leo is the only player holding any. When the holiday ends, about four thousand banks never reopen. Then, in June nineteen thirty-three, a new law creates federal deposit insurance. It starts on January first, nineteen thirty-four, and covers up to two thousand five hundred dollars per depositor. | **Sahne:** ABD haritası eyalet eyalet griye döner (4 Mart'a kadar) [FDIC-BH3]; otel odası kapı altı notu kartı "OUT-OF-TOWN CHECKS NOT ACCEPTED" [FDIC-BH3]; "MARCH 6: NATIONWIDE BANK HOLIDAY" [FDIC-BH3]. Roosevelt gerçekçi yüzle çizilmez; yalnız radyo silueti + ekran yazısı (K5). **Leo (Bank Leo):** kilitli kapıda; Box Leo arka planda bakkala yürür. **Ekran:** "~4,000 BANKS NEVER REOPENED" [FDIC-BH3] · "JUNE 16, 1933: BANKING ACT" · "JAN 1, 1934: DEPOSITS INSURED UP TO $2,500" [FDIC-BH3]. **Etiket:** gerçekçi sokak/bakkal karesi → "Illustration". |

### S19 · 9:31–9:47 · 16 sn
| ANLATIM | GÖRSEL |
|---|---|
| In nineteen thirty-four, only nine insured banks suspended. The gamble door finally gets a lock that works. So Box Leo wins nineteen twenty-nine. Now let's do something unfair. Let's take his winning door and move it to today. | **Grafik G2 devamı:** 1933 çubuğu 4,000 → 1934 çubuğu "9 insured" (neredeyse görünmez çubuk) [FDIC-BH3]. **Sahne:** Box Leo'nun kahve kapısı raylar üstünde kayar, takvim "1933 → 2026" döner. **Leo (sunucu):** muzip gülüş, el ovuşturma. **Ekran:** "1934: 9 INSURED BANKS SUSPENDED". **↺ 9:46** "move it to today" → Bölüm 7. |

## Bölüm 7 — The Twist: Same Door, 2026

### S20 · 9:47–10:13 · 26 sn
| ANLATIM | GÖRSEL |
|---|---|
| Same shoebox. Same thousand dollars. Start in September twenty twenty-five. Twelve months later, U.S. consumer prices are three point seven percent higher. That's the official number for the year to September twenty twenty-six. So the thousand dollars now buys what about nine hundred sixty-four dollars bought a year earlier. Nothing was stolen. The bills are all there. They just buy less. | **Sahne:** modern soğuk mavi stüdyo; aynı kutu. **Mekanizma görseli (H2):** kutudaki banknotlar yanında küçük bir grafikle **yavaşça küçülür**; Box Leo kayıp/aşağılanma ifadesi değil, merakla grafiğe bakar (düşünen poz). **Grafik G5a:** "CPI, 12 MONTHS TO SEPT 2026: +3.7% (not seasonally adjusted)" [BLS-0926] · "$1,000 → buys like $964" [FRED-CPI, H]. "Source: BLS". |

### S21 · 10:13–10:43 · 30 sn
| ANLATIM | GÖRSEL |
|---|---|
| Now put the two periods side by side. From September nineteen twenty-nine to March nineteen thirty-three, prices fell about twenty-seven percent. From September twenty twenty-two to September twenty twenty-six, prices rose about thirteen and a half percent. Same box. Opposite result. In the early nineteen thirties, cash gained power because prices were falling. In twenty twenty-six, prices are rising, so the same math runs the other way. That's arithmetic, not a plan. | **Grafik G5 (kendi grafiğimiz, birincil veri, ayna):** iki panel aynı ölçekte, başlangıç = 100: **1929–33** TÜFE 100 → 72.8 (−27.2%) ve **2022–26** TÜFE 100 → 113.5 (+13.5%) [FRED-CPI, H]; altında 1.000 $'ın alım gücü 1,373 ‖ 881 [H]. "Source: BLS CPI via FRED (CPIAUCNS)". **Leo (sunucu):** iki paneli iki eliyle tutar gibi, ciddi. **Ekran:** "SAME BOX. OPPOSITE RESULT." · "ARITHMETIC, NOT A PLAN". |

### S22 · 10:43–10:57 · 13 sn
| ANLATIM | GÖRSEL |
|---|---|
| The bank door changed too. That lock from nineteen thirty-four is still there. Today, the FDIC says deposits are insured to at least two hundred fifty thousand dollars at each insured bank. | **Sahne:** yeşil kapı; 1934 asma kilidi parlayarak modern kilide dönüşür. **Ekran:** "$2,500 (1934) → $250,000 (TODAY, per FDIC-insured bank)" [FDIC-BH3, FDIC-DI]. **Leo (sunucu):** işaret pozu. Not: bugüne dönük hüküm yok, yalnız kuralın değiştiği bilgisi (P1). |

## Bölüm 8 — What the Game Really Tests

### S23 · 10:57–11:29 · 32 sn
| ANLATIM | GÖRSEL |
|---|---|
| So, which door was safe? In nineteen twenty-nine, the door that looked smart hurt the most. The door everyone laughed at came out on top. Not because a shoebox is clever, but because of one thing outside all three doors: what prices were doing in that decade. That's the idea we started with. A safe place for money isn't really a place. It depends on what prices are doing, and on the rules around each door. | **Sahne:** stüdyo geniş plan; üç kapı yan yana, üstlerinde final etiketleri: mavi "DISASTER", yeşil "GAMBLE", kahve "SURPRISE" (hook'taki döngü kapanır). **↺ 10:57** "So, which door was safe?" (final cevabı açar). Kapıların dışında, tavanda dev bir termometre/ok: "PRICES ↓ (1930s)" ↔ "PRICES ↑ (2026)". **Leo (sunucu):** kameraya bakan konuşma pozu, sıcak. **Ekran:** tez (Ö1, son): "SAFE ISN'T A PLACE. IT DEPENDS ON PRICES." |

### S24 · 11:29–11:44 · 16 sn · uç ekran köprüsü
| ANLATIM | GÖRSEL |
|---|---|
| Falling prices made a shoebox the winner. But history also has a time when prices rose so fast that people's savings melted in a single year. That's a game for another night. I'm Leo. Thanks for playing. | **Uç ekran (son 17 sn):** stüdyo ışıkları kısılır; sağda uç ekran kutuları için boş alan (video öğesi + abone öğesi). Kapıların arkasında bir sonraki "oyun" için kapalı dördüncü kapı silueti (yazısız). **Leo (sunucu):** el sallar. **Ekran:** "THANKS FOR PLAYING". Köprü notu: §6. |

---

## 3. Retention haritası

Zamanlar §13 betik ölçümünden (143 kpm). "Döngü" = açılan (A) / kapanan (K) merak döngüsü.

| Zaman | Açılan / kapanan merak döngüsü | Yeniden kanca (↺) | Görsel değişim notu |
|---|---|---|---|
| 0:00 | **A1** hangi kapı felaket / kumar / sürpriz? | hook | ≤3 sn: sepya sokak → stüdyo + 3 kapı |
| 0:17 | A3 "Where was money safe in 1929?" (A1'in çerçevesi) | — | takvim yaprağı 1929↔2026 |
| 0:32 | **A2** neden aynı matematik bugün ters işler? (sona kadar açık) | **↺1** "By the end, you'll know which door won" | üç madde ekranda |
| 0:41 | A4 tez ortaya konur (oyun bunu test edecek) | — | tez satırı → maaş grafiği G0 |
| 1:31 | A5 neden en akıllı seçim gibi görünüyor? | **↺2** "smartest choice in the room" | klonlar kapılara yürür |
| 1:35–2:12 | A5 kapanır (6 kat yükseliş, borç) | — | G1a, ticker yağmuru |
| 2:12 | A6 dramatik ironi: zirve, kimse bilmiyor | **↺3** "Nobody knows it yet" | müzik keser |
| 2:14–2:48 | A6 kapanır (Ekim düşüşleri, ~500 $) | — | takvim kopması, G1b sayaç |
| 3:08 | A1 kısmi kapanış (borsa = felaket adayı) · A7 "banka güvenli mi?" | **↺4** "That's the safe door. Right?" | bölünmüş ekran → banka içi |
| 4:03 | A8 kuyruk neden sağlam bankayı bile batırır? | **↺5** "Here's the problem" | kuyruk + mekanizma animasyonu |
| 4:29 | A9 skor "tek sayı değil, iki" | **↺6** "It isn't one number. It's two." | G2 çubuk grafiği |
| 4:26–5:12 | **İlk büyük ödül:** A7 + A8 + A9 kapanır; banka = kumar | — | "GAMBLE" damgası |
| 5:12 | kısa abone çağrısı (1 cümle) | — | alt köşe düğme (3 sn) |
| 5:29 | A10 kutunun parasına garip bir şey oluyor | **↺7** "something strange is happening to it" | spot kahve kapıya |
| 5:32–6:27 | A10 kapanır (deflasyon, 1,272) | — | G3 TÜFE grafiği, etiketler küçülür |
| 6:27 | A11 iç ters köşe: bir ülke dolusu kutu bankaları zayıflattı | **↺8** "Here's the strange part" | harita kutuları, G3b |
| 7:03 | A12 kutu şampiyon mu? en zor an | **↺9** "survive the hardest moment" | tuzak kartları |
| 7:36 | A13 borsa 1.000 $'a ne zaman döner? iki cevap | **↺10** "So how long until he's back to one thousand?" | G1 tam + 1954 / 1936 notları |
| 7:59–8:29 | **A1 tam kapanır:** skor tablosu · A12, A13 kapanır | — | G4 skor tablosu |
| 8:35 | A14 her kapı kilitleniyor | **↺11** "every door gets locked" | zincir + kilit ×3 |
| 8:37–9:47 | A14 kapanır (banka tatili, FDIC 1934) | — | harita griye, otel notu kartı |
| 9:46 | A2'ye giriş: kazanan kapıyı bugüne taşı | **↺12** "move it to today" | kapı raylarla 2026'ya |
| 9:47–10:57 | **A2 kapanır:** aynı kutu, ters sonuç (P1 mekanizma cümlesi) | — | soğuk mavi stüdyo, G5a, G5 ayna |
| 10:57 | final cevabı: hangi kapı güvenliydi? | **↺13** "So, which door was safe?" | final etiketleri kapılarda |
| 11:19 | A4 kapanır: tez doğrulanır | — | tez satırı tekrar |
| 11:29 | **A15 (uç ekran):** fiyatlar çok hızlı yükselirse? | köprü cümlesi | dördüncü kapı silueti, uç ekran |

**Yeniden kanca aralıkları (betik):** §13 tablosu; en uzun aralık 71 sn (kapı ≤90). Not: TTS duraklamaları süreyi uzatabilir; F4'te gerçek ses zamanlarıyla kurgu-editoru yeniden ölçer (85 sn üstü aralık çıkarsa ↺ öncesine görsel vurgu eklenir).

---

## 4. YouTube bölümleri (chapters)

Betik ölçümü zamanlarıyla (≥10 sn, ilk 0:00, ≥3 bölüm). Montaj sonrası `kurgu-editoru` gerçek ses zamanlarıyla günceller.

```
0:00 The game: $1,000 and three doors
1:35 Door 1: The stock market
3:10 Door 2: The bank
5:32 Door 3: The shoebox
7:09 The bottom: July 1932
8:37 March 1933: every door locked
9:47 The twist: the same door in 2026
10:57 What the game really tests
```

---

## 5. Shorts kancaları ve kesit önerileri (2 adet, her biri ≤60 sn, 9:16)

### Shorts 1 — "Pick a door" (P2 kancası)
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "In nineteen twenty-nine, most people would have picked the wrong door."
- **Kesit (ana video betik zamanları):** S01 kapı tanıtımı 0:02–0:09 ("You have one thousand dollars… under your bed", 18 kelime) → S06 2:40–2:48 ("By mid-November… about five hundred", 20) → S10 4:26–4:39 ("Now the score for door two… more than one bank in three", 31) → S16 7:59–8:18 ("Here's the scoreboard… twelve hundred seventy", 45).
- **Kapanış satırı (yeni kayıt):** "Why the brown door won, and why it flips today, is in the full video."
- **Kelime / süre:** hook 11 + kesitler 114 + kapanış 15 = **140 kelime → ≈59 sn** (143 kpm). 60 sn'yi aşarsa S10 kesitinin son cümlesi ("That's more than one bank in three.") çıkar → ≈56 sn.
- **9:16 notu:** kapılar dikey yığılır (üstte mavi, ortada yeşil, altta kahve), skor tablosu dikey kart.
- **Politika:** "wrong door" yalnız 1929 için, geçmiş zaman ("would have"). Bugüne dönük hüküm yok (P2).

### Shorts 2 — "Same box, opposite result"
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "A shoebox of cash gained power in nineteen thirty-two. In twenty twenty-six, the same math runs the other way."
- **Kesit (ana video betik zamanları):** S12 5:49–6:03 ("From September nineteen twenty-nine… bought in nineteen twenty-nine", 34 kelime) → S20 9:52–10:13 ("Twelve months later… They just buy less", 51) → S21 10:29–10:43 ("Same box. Opposite result… not a plan", 35).
- **Kelime / süre:** hook 19 + kesitler 120 = **139 kelime → ≈58 sn**.
- **9:16 notu:** G5 ayna grafiği dikeyde üst-alt panel.
- **Politika:** mekanizma dili, "should/keep cash" yok; son cümle "That's arithmetic, not a plan." (P1, P2).

---

## 6. Uç ekran köprüsü (2 sürüm, seçilen: A)
- **A (seçilen, metinde):** "Falling prices made a shoebox the winner. But history also has a time when prices rose so fast that people's savings melted in a single year. That's a game for another night." → Var olmayan bir videoya söz vermez (K7 yanıltıcı meta veri riski yok), ama doğal merak (yüksek enflasyon) bırakır. Kanalın ilk herkese açık videosu olduğu için uç ekranda yalnız abone öğesi + "en uygun video" öğesi.
- **B (yedek, S04 Weimar yayınlandığında güncellenir):** "…Ten years earlier, in Germany, prices didn't fall. They ran. That game is waiting on the screen right now." → Ancak hedef video yayındaysa kullanılır (metin kilidinden sonra değişirse yalnız S24 sesi yeniden üretilir).

---

## 7. Kaynak listesi (kodlar)

| Kod | Kaynak | Ne için | Durum |
|---|---|---|---|
| FRH-29 | Federal Reserve History, "Stock Market Crash of 1929" — https://www.federalreservehistory.org/essays/stock-market-crash-of-1929 (erişim 2026-10-27) | 63 (Ağu 1921), 381.17 (3 Eyl 1929), "almost half" (Kasım ortası), 41.22 (8 Tem 1932), Kasım 1954, "typically 10 percent", Black Monday ~13%, Black Tuesday ~12% | [D] bu çalışmada okundu |
| FRH-BP | Federal Reserve History, "Banking Panics of 1930–31" — https://www.federalreservehistory.org/essays/banking-panics-1930-31 | 11 Aralık 1930 Bank of United States (NYC'nin 4. büyük bankası), "over 8,000 … nearly 16,000", "hundreds of banks suspended" | [D] |
| FRH-GD | Federal Reserve History, "The Great Depression" — https://www.federalreservehistory.org/essays/great-depression | para arzı "nearly 30 percent" (1930 sonbaharı–1933 kışı) | [D] |
| FDIC-BH3 | FDIC, *A Brief History of Deposit Insurance in the United States*, Bölüm 3 (W. Isaac), Tablo 5 — https://www.fdic.gov/resources/publications/brief-history-of-deposit-insurance/book/brief-history-deposit-insurance-3.pdf | yıllık askıya almalar 1921–33, mudi kayıpları, 4 Mart 1933 tüm eyaletlerde tatil, 6 Mart ulusal tatil, ~4.000 banka açılmadı, 16 Haziran 1933 Banking Act, 1 Ocak 1934 sigorta 2.500 $, 1934'te 9 sigortalı banka, "widespread attempts to convert deposits to cash" | [D] PDF metni çıkarıldı (`pdftotext`), veri `veri/fdic-tablo5-askiya-alma-1921-1933.csv` |
| FDIC-DI | FDIC, Deposit Insurance — https://www.fdic.gov/resources/deposit-insurance | "insured to at least $250,000 at each FDIC-insured bank" | [D] |
| FRED-CPI | FRED, `CPIAUCNS` (BLS CPI-U, NSA, 1982-84=100) — https://fred.stlouisfed.org/series/CPIAUCNS | Eyl 1929 17.3, Tem 1932 13.6, Mar 1933 12.6; Eyl 2022 296.808, Eyl 2025 324.800, Eyl 2026 336.940 | [D] CSV indirildi, `veri/cpi-*.csv` |
| BLS-0926 | BLS CPI haber bülteni, 14 Ekim 2026 — https://www.bls.gov/news.release/archives/cpi_10142026.htm | +3.7%, 12 ay, Eylül 2026, NSA (D4) | [D/AÖ] on-dogrulama.md; FRED serisiyle tutarlı (336.940/324.800 = +3.74%) [H] |
| BEA-666 | BEA NIPA Tablo 6.6A satır 1, "Wages and salaries per full-time equivalent employee", 1929 = 1,430 $ (DBnomics yansısı, revizyon 2024-09-27) — https://db.nomics.world/BEA/NIPA-T60600A | 1.000 $ ≈ 8 aylık ücret (D5) | [D] DBnomics sayfası okundu; BEA'nın kendi sitesi açılmadı → doğrulayıcı teyidi önerilir |
| HUL | M. Hulbert, "25 Years to Bounce Back? Try 4½", The New York Times, 26 Nisan 2009 (HNN kopyası) — https://www.historynewsnetwork.org/article/79770 | temettü + deflasyonla başa baş "late 1936"; Dow fiyatı 23 Kasım 1954 (D6 nüansı) | [AÖ] ikincil kopya okundu, NYT ücretli duvar; metinde "one well-known analysis" diye çerçevelendi |
| H | `03-metin/veri/hesap.py` → `veri/hesap-cikti.txt` | 108 $, 1,272, 1,373, 964, 881, −21.4%, −27.2%, +13.5%, ~20¢/1 $, ~800 $, ≈9.100, >1/3, 8 ay | betik, iki koşu aynı (§13) |

Açıklamaya gidecek kaynak listesi (Ö3, ≥5): FRH-29, FRH-BP, FRH-GD, FDIC-BH3, FDIC-DI, FRED-CPI, BLS-0926, BEA-666 (8 kaynak) + HUL.

---

## 8. Rakam tablosu (doğrulayıcı için: metindeki her rakam → kaynak)

| # | Anlatımdaki ifade (sahne) | Değer | Kaynak | Etiket |
|---|---|---|---|---|
| 1 | "one thousand four hundred thirty dollars a year" (S03) | 1,430 $ | BEA-666 | [D] |
| 2 | "roughly eight months of pay" (S03) | 1000/1430×12 = 8.4 | H | [H] |
| 3 | "August nineteen twenty-one … sixty-three" (S05) | 63 | FRH-29 | [D] |
| 4 | "three hundred eighty-one … six times higher" (S05) | 381 / ×6 | FRH-29 ("six-fold") | [D] |
| 5 | "typically ten percent" (S05) | %10 | FRH-29 | [D] |
| 6 | "September third … three hundred eighty-one point one seven" (S05) | 381.17 | FRH-29 | [D] |
| 7 | "October twenty-eighth … nearly thirteen percent" (S06) | ~%13 | FRH-29 | [D] |
| 8 | "almost twelve percent more" (S06) | ~%12 | FRH-29 | [D] |
| 9 | "mid-November … almost half … about five hundred" (S06) | ~500 $ | FRH-29 + H | [D/H] |
| 10 | "about ten weeks" (S07) | 3 Eyl → Kasım ortası ≈ 10,5 hafta | FRH-29 + H | [H] |
| 11 | "over eight thousand … nearly sixteen thousand" (S08) | 8,000+ / ~16,000 | FRH-BP | [D] |
| 12 | "no federal deposit insurance" (S08) | — | FDIC-BH3 (sigorta 1934'te başladı) | [D] |
| 13 | "December eleventh, nineteen thirty … fourth-largest bank in New York City" (S09) | 11 Ara 1930 | FRH-BP | [D] |
| 14 | "about nine thousand banks suspended" (S10) | 9,096 | FDIC-BH3 Tablo 5 + H | [D/H] |
| 15 | "more than one bank in three" (S10) | 9,096 / ~24,000 = %38 | FDIC-BH3 + FRH-BP + H | [H] (iki kaynak birleşimi; doğrulayıcı onayı) |
| 16 | "about twenty cents of every dollar, on average" (S10) | 1,336,533 / 6,830,223 = %19.6 | FDIC-BH3 Tablo 5 + H | [H] |
| 17 | "around two hundred dollars" / "around eight hundred" (S10, S16) | 196 / 804 | H | [H] |
| 18 | "might wait a long time for the rest" (S10) | sayısız | D3 sayısız dil | — |
| 19 | "nearly thirty percent … fall of nineteen thirty to winter of nineteen thirty-three" (S13) | ~%30 | FRH-GD | [D] |
| 20 | "September nineteen twenty-nine to July nineteen thirty-two … about twenty-one percent" (S12) | −21.4% | FRED-CPI + H | [D/H] |
| 21 | "one thousand two hundred seventy" / "twelve hundred seventy" (S12, S16) | 1,272 | H | [H] |
| 22 | "July eighth, nineteen thirty-two … forty-one point two two" (S15) | 41.22 | FRH-29 | [D] |
| 23 | "about eighty-nine percent" (S15) | −89.2% | H | [H] |
| 24 | "about one hundred and eight dollars … price only, before dividends" (S15, S16) | 108 $ | FRH-29 + H | [H] (D1) |
| 25 | "price didn't get back … until November nineteen fifty-four" (S15) | Kasım 1954 | FRH-29 | [D] (D6) |
| 26 | "late nineteen thirty-six … seven years" (S15) | ~1936 sonu; Eyl 1929→1936 sonu ≈ 7 yıl | HUL + H | [AÖ] |
| 27 | "By March fourth, every state … bank holiday" (S18) | 4 Mart 1933 | FDIC-BH3 | [D] |
| 28 | "Two days later … closes every bank" (S18) | 6 Mart 1933 | FDIC-BH3 | [D] |
| 29 | "about four thousand banks never reopen" (S18) | ~4,000 | FDIC-BH3 | [D] |
| 30 | "June nineteen thirty-three … January first, nineteen thirty-four … two thousand five hundred" (S18) | 16 Haz 1933 / 1 Oca 1934 / 2,500 $ | FDIC-BH3 | [D] |
| 31 | "only nine insured banks suspended" (S19) | 9 | FDIC-BH3 | [D] |
| 32 | "three point seven percent … year to September twenty twenty-six" (S20) | +3.7% NSA | BLS-0926, FRED-CPI | [D] (D4) |
| 33 | "nine hundred sixty-four dollars" (S20) | 964 | H | [H] |
| 34 | "fell about twenty-seven percent" (Eyl 1929→Mar 1933) (S21) | −27.2% | FRED-CPI + H | [H] |
| 35 | "rose about thirteen and a half percent" (Eyl 2022→Eyl 2026) (S21) | +13.5% | FRED-CPI + H | [H] |
| 36 | "at least two hundred fifty thousand dollars at each insured bank" (S22) | 250,000 $ | FDIC-DI | [D] |
| 37 | "Some reopened within a few months. Most were closed for good." (S10) | sayısız | FRH-BP ("About one-third … reopened within a few months, but the majority were liquidated" — 1930–31 dalgası); FDIC-BH3 (1933: ~4.000 banka hiç açılmadı) | [D] (1930–33'e genelleme: doğrulayıcı onayı) |
| 38 | "notes in their hotel rooms: checks from out-of-town banks won't be accepted" (S18) | — | FDIC-BH3 ("Visitors arriving in Washington … found notices in their hotel rooms that checks drawn on out-of-town banks would not be honored") | [D] |

Kullanılmayan / bilerek çıkarılan: FRH'nin "fiyatlar ~%30 düştü" ifadesi (D2: yerine TÜFE kesin değeri); işsizlik oranı (FRH sayı vermiyor → sayısız bile kullanılmadı); "pencereden atlayan bankacılar" miti (grep 0, §13).

---

## 9. Telaffuz notları (ses-yonetmeni için; Kokoro am_fenrir 0.9)

- **Yasak listesi (telaffuz kuralı):** charts, complicated, scenarios, truth, crash/crashes, bold → anlatımda **0** (betik §13). "Crash" yerine "fall / drop / the top"; 1929 olayının adı yalnız ekran yazısında ve başlıkta yok.
- **Sayılar yazıyla yazıldı.** Kokoro'ya metin aynen verilir. Kontrol edilecek okunuşlar (Whisper ile): "nineteen twenty-nine", "twenty twenty-five/six", "three hundred eighty-one point one seven", "forty-one point two two", "three point seven percent".
- **Özel adlar:** "Dow Jones Industrial Average" (tam ad yalnız S05'te bir kez; sonra "the Dow" — /daʊ/; espeak "doe" okursa `[Dow](/dˈW/)` fonetik yazım), "Bank of United States" (resmî adında "the" yok; doğru), "Franklin Roosevelt" (/ˈroʊzəvɛlt/; espeak "roos-" okursa `[Roosevelt](/ɹˈOzəvˌɛlt/)`), "FDIC" (harf harf: "F-D-I-C"; TTS'e "F D I C" diye ver), "Federal Reserve".
- **Leo:** /ˈliːoʊ/ — tek heceye düşmemeli.
- **Duraklamalar:** "Right?" (S07), "Not so fast." (S14), "Same box. Opposite result." (S21) — soru/nokta duraklaması korunur; `tts.py` "..." kullanılmadı (0.55 sn fazla uzun).
- **Riskli /æ/ ve "ch":** "stack" (S12), "champion" (S14), "chase" kullanılmadı; "champion" Whisper'da düşük güven verirse "the winner" ile değiştirilir (anlam aynı, metin kilidi dışı küçük ses düzeltmesi olarak ses-yonetmeni not eder).
- **Shorts hook'ları** ayrı kayıt: aynı ses/hız.

---

## 10. Zor bölümlerin 2 versiyonu ve eleme

### Açılış (0–15 sn)
| Versiyon | Metin | Kelime | Vaat sonu (kelime → sn) | Somut özne | Karar |
|---|---|---|---|---|---|
| **A (seçilen)** | F2'de hakemin onayladığı hook, kelimesi kelimesine (H3) | 39 | 37. kelime → ≈15.5 sn | 1.000 $ + 3 fiziksel kapı | **Seçildi:** 3 parçalı döngü (disaster/gamble/surprise) açık; H3 "kelimesi kelimesine kalabilir" |
| B | "September nineteen twenty-nine. You have one thousand dollars and three doors: … By nineteen thirty-three, one door is a disaster, one is a gamble, one is a surprise." | 37 | 37 → ≈15.5 sn | aynı | Elendi: yalnız 2 kelime kısa, "It's" ve "and one" ritmi kaybolunca ikinci tekil sahne hissi zayıflıyor; kazanç <1 sn |
| C (şok rakam) | "One thousand dollars in nineteen twenty-nine. One door turns it into about one hundred and eight dollars. One door might take a fifth of it. And one door makes it worth more. Which is which?" | 36 | 36 → ≈15 sn | 1.000 $ + 3 sonuç | Elendi: iki sonucu baştan harcıyor (F2 H2 ile aynı sorun), "surprise" merakı ölüyor |

### Orta nokta (ilk büyük ödül + abone, S10–S11)
| Versiyon | Fark | Kelime | Kanca | Karar |
|---|---|---|---|---|
| **A (seçilen)** | Banka kapısı FDIC Tablo 5 ile **koşullu** rakam (askıya alınan bankada ~20¢/1 $), "gamble" vaadi korunur; abone 1 cümle + hemen ↺3 | 110+47 | ↺6 4:29, ↺7 5:29 | **Seçildi:** D3 sayıyla karşılandı ama rakam tek "kayıp oranı" gibi sunulmuyor (koşullu ortalama) → skor tablosunda "?" kalır, yarış dengesi bozulmaz |
| B | Sayısız: "you might lose access to your savings, sometimes for years" + abone ayrı sahne | ≈80+47 | ↺7 ≈5:20 | Elendi: birincil veri bulunduğu halde kullanmamak H1'i (her kapı ≥1 birincil veri) zayıflatır; "sometimes for years" için kaynak yok |

### Kapanış (S21–S24)
| Versiyon | Fark | Kelime | Döngü kapanışı | Karar |
|---|---|---|---|---|
| **A (seçilen)** | P1 + R2-A birleşimi: "cash gained power because prices were falling … the same math runs the other way. That's arithmetic, not a plan." + FDIC kuralı bilgisi + tez tekrarı + köprü | 72+32+76+37 | A1, A2, A4 kapanır; A15 açılır | **Seçildi:** bugüne hüküm yok, mekanizma var; twist korunuyor |
| B | R2-C: "This is a history game, not a plan…" ile açılan kapanış | ≈ aynı | A2 kapanır | Elendi: "not a plan" uyarıyla açılınca etiket gibi duruyor (P4'e yakın); mekanizma cümlesi sonra gelince twist zayıflıyor |

**Acımasız editör turu (yapılan kesintiler):** "Here's something most people today don't know" → "Here's the part that surprises people today" (doğrulanamaz genelleme); "millions of people pulled cash" → "people across the country" (sayı kaynaksız); "Even Stock Leo can't get cash" çıkarıldı (borsanın tatilde kapalılığı kaynaklanmadı); "Box Leo got richer" → "his money got stronger" (zenginlik değil alım gücü); "the only player who can buy groceries" → "the only player holding any [cash]" (abartı); "crash" 0'a indirildi; "Dividends helped a bit" → "Dividends did help" (Hulbert: dipte temettü verimi ~%14 [AÖ]; "more than most people think" doğrulanamaz genelleme olduğu için o da çıkarıldı); "Bread, rent, shoes" → "The average price of what families buy" (TÜFE kalem bazında kaynaklanmadı); "Congress creates" → "a new law creates" (yasayı Kongre geçirdi, Roosevelt imzaladı).

---

## 11. D / P / H düzeltmeleri — nerede uygulandı

| Madde | İstenen | Nerede / nasıl | Durum |
|---|---|---|---|
| D1 | 1.000 → ~500 (Kasım) → ~108 (Tem 1932); "price only, before dividends" alt notu | S06 ("about five hundred"), S15 anlatım "That's price only, before dividends" + G1 zorunlu alt not; S16 "on price alone" + G4 "(price only)" | ✓ |
| D2 | "%30 fiyat düşüşü" yok; TÜFE kesin değer | S12: FRED `CPIAUCNS` Eyl 1929→Tem 1932 −21.4% ("about twenty-one percent"); S21: Eyl 1929→Mar 1933 −27.2%. FRH "~%30" yalnız **para arzı** için kendi dönemiyle (S13) | ✓ |
| D3 | Banka kaybı FDIC/Fed'den; yoksa sayısız | **Bulundu:** FDIC Tablo 5 → askıya alınan bankalarda mudi kaybı 1930–33 %19.6 [H]; "on average", koşullu ("if your bank was one of them"); skor tablosunda risk simgesi "?" + koşullu alt satır (S10, S16, G2, G4). Bekleme süresi sayısız ("might wait a long time") | ✓ |
| D4 | "3.7%, 12 months ending September 2026, NSA" (BLS) | S20 anlatım "three point seven percent… the official number for the year to September twenty twenty-six"; G5a ekran "+3.7% (not seasonally adjusted)" [BLS-0926] | ✓ |
| D5 | 1929'da 1.000 $'ın değeri BLS/Census; yoksa çıkar | BEA NIPA T6.6A satır 1 (1,430 $/yıl) → "roughly eight months of pay" (S03, G0). Not: BLS/Census değil BEA (aynı resmî istatistik ailesi); doğrulayıcı BEA sitesinden teyit etmeli | ✓ (teyit notu) |
| D6 | "The Dow's price didn't get back… until 1954" + temettü/deflasyon nüansı | S15: "The Dow's price didn't get back to its nineteen twenty-nine peak until November nineteen fifty-four. Counting dividends and falling prices, one well-known analysis puts the break-even point much earlier, in late nineteen thirty-six." [FRH-29, HUL] | ✓ |
| D7 | Her kapı sonucu "o on yıl, fiyatlar düşüyordu" gerekçesine bağlı; sonda kişisel çağrı yok; R2 seçeneklerinden biri | S16 "Every result on this board belongs to that decade. A decade when prices were falling." + G4 şeridi; S21 R2-A ("In the early nineteen thirties, cash gained power because prices were falling…"); S23 "what prices were doing in that decade". Kişisel çağrı yok (betik: tavsiye kalıbı 0) | ✓ |
| P1 | 2026 ters köşesi mekanizma cümlesi | S21: "…so the same math runs the other way. That's arithmetic, not a plan." S20/S22 yalnız ölçülen olgu, bugüne hüküm yok | ✓ |
| P2 | Shorts: "In 1929, most people would have picked the wrong door." 2. Shorts mekanizma dili | §5 Shorts 1 hook birebir (sayılar yazıyla); Shorts 2 "…gained power in nineteen thirty-two. In twenty twenty-six, the same math runs the other way." | ✓ |
| P3 | "Where was money safe in 1929?" + "why the same math runs the other way today" | S02 birebir | ✓ |
| P4 | Uyarı etiketiyle kapatma yasak | "this isn't advice" / disclaimer cümlesi yok (betik: 0); yasal not yalnız açıklamada (paketleyici) | ✓ |
| P5 | `sentetik_medya = true` + "Narration voice is AI-generated"; gerçekçi 1929–33 sahnelerine "Illustration" | GÖRSEL sütununda S01, S05, S09, S18'de "Illustration" etiketi; stüdyo muaf. `sentetik_medya` ve açıklama satırı F8 paketleyici/monetizasyon işi → durum notu | ✓ (metin payı) / F8'e devredildi |
| P6 | Oyun formatı ≥5 video tekrar yok (kanal kuralı, showrunner) | Metin dışı; §12 Leo rol tablosuna "oyun sunucusu, 3 kapı, kazanan: kutu" kaydı. Uç ekran köprüsü yeni bir *oyun* sözü vermiyor ("a game for another night" mecaz) → showrunner'a not: sonraki video oyun formatı olmamalı, köprü cümlesi buna uygun | ✓ (not) |
| H1 | Her kapıda ≥1 birincil veri; ≥3 kendi veri grafiği; yetişkin ton | Borsa: G1 (FRH Dow çapaları) · Banka: G2 (FDIC Tablo 5) · Kutu: G3 (FRED CPIAUCNS) · ayrıca G0 (BEA), G3b (FRH para arzı), G4 skor, G5 ayna (FRED) → **6 veri grafiği + 1 infografik**, hepsinde ekran kaynak etiketi; veri dosyaları `03-metin/veri/` | ✓ |
| H2 | Kutu Leo'nun 2026 anı mekanizma görseli, aşağılanma yok; sunucu kaybetmez | S20 GÖRSEL: banknotlar grafik yanında küçülür, Box Leo merakla bakar (düşünen poz); sunucu Leo hiçbir sahnede kaybeden değil (F2'deki "kibri yüzünde donar" anı bilerek çıkarıldı) | ✓ |
| H3 | Hook kelimesi kelimesine; ilk görsel değişim ≤3 sn | S01 = F2 hook birebir; 0:02'de sokak → stüdyo kesmesi (F7'de ölçülür) | ✓ |
| H4 | 3 klonlu kapı sahnesi F5 kritik yol testine; B planı | S04 GÖRSEL notu (kritik yol + B planı) | ✓ (not) |
| H5 | Başlık sabit, 3 thumbnail Test & Compare, soru işaretsiz yedek başlık | Metin dışı (F8). Metin başlıkla tutarlı: "$1,000", "1929", "keep it?" sorusu S16/S23'te cevaplanıyor | ✓ (F8'e devredildi) |

---

## 12. Leo rol kaydı (Ö5)

| Video | Leo'nun rolü | Durum | Sonuç |
|---|---|---|---|
| 1929-1000-dolar (bu) | Oyun sunucusu + 3 klon oyuncu (izleyici adına) | 1929–33, üç kapı | Sunucu kaybetmez; kazanan kapı = kutu (yalnız o on yıl için); 2026'da aynı kutu alım gücü kaybeder (mekanizma) |

---

## 13. Test kapısı sonuçları

Komut: `cd 03-metin && python3 -I metin-kontrol.py metin.md` (iki koşu `diff` → fark yok, sha256 aynı) · ham çıktı: `03-metin/kapi-cikti.txt`.
Hesap betiği: `cd 03-metin/veri && python3 -I hesap.py` (iki koşu `diff` → fark yok) · çıktı `veri/hesap-cikti.txt`.


Hız varsayımı: 143 kpm (am_fenrir 0.9 ölçümü). Sahne sayısı: 24.

| Sahne | Başlangıç–bitiş | Süre sn | Kelime |
|---|---|---|---|
| S01 | 0:00–0:17 | 17 | 41 |
| S02 | 0:17–0:41 | 23 | 56 |
| S03 | 0:41–1:06 | 26 | 61 |
| S04 | 1:06–1:35 | 29 | 68 |
| S05 | 1:35–2:14 | 39 | 93 |
| S06 | 2:14–2:48 | 34 | 82 |
| S07 | 2:48–3:10 | 21 | 51 |
| S08 | 3:10–3:47 | 37 | 89 |
| S09 | 3:47–4:26 | 39 | 93 |
| S10 | 4:26–5:12 | 46 | 110 |
| S11 | 5:12–5:32 | 20 | 47 |
| S12 | 5:32–6:07 | 35 | 84 |
| S13 | 6:07–6:44 | 37 | 87 |
| S14 | 6:44–7:09 | 25 | 60 |
| S15 | 7:09–7:59 | 50 | 120 |
| S16 | 7:59–8:29 | 29 | 70 |
| S17 | 8:29–8:37 | 8 | 19 |
| S18 | 8:37–9:31 | 55 | 131 |
| S19 | 9:31–9:47 | 16 | 38 |
| S20 | 9:47–10:13 | 26 | 61 |
| S21 | 10:13–10:43 | 30 | 72 |
| S22 | 10:43–10:57 | 13 | 32 |
| S23 | 10:57–11:29 | 32 | 76 |
| S24 | 11:29–11:44 | 16 | 37 |

**Toplam kelime:** 1678 · **tahmini süre:** 11:44 (11.7 dk) · kapı ≥1500 ve hedef 12 dk ±%10 = 1544–1888 kelime → GEÇTİ
  (Not: tireli sayı kelimesi 52 adet; tireler ayrı sayılırsa 1730 birim ≈ 12:06 — üst sınır tahmini.)

**İlk 15 sn (35 kelime):** "It's September nineteen twenty-nine. You have one thousand dollars. Three doors: the stock market, a bank, or a shoebox under your bed. By nineteen thirty-three, one door is a disaster, one is a gamble, and"
  somut özne (thousand dollars + door) ve vaat (disaster/gamble) ilk 15 sn içinde: GEÇTİ · 'surprise' kelime sırası: 39
  İlk 30 sn kanal tanıtımı/abone kalıbı: 0 GEÇTİ

**Yeniden kancalar (↺):**

| # | Sahne | İfade | Zaman | Önceki kancadan aralık sn | Sonuç |
|---|---|---|---|---|---|
| hook | S01 | It's September nineteen twenty-nine | 0:00 | 0 | GEÇTİ |
| ↺1 | S02 | By the end, you'll know which door won | 0:32 | 32 | GEÇTİ |
| ↺2 | S04 | it looks like the smartest choice in the room | 1:31 | 59 | GEÇTİ |
| ↺3 | S05 | Nobody knows it yet | 2:12 | 41 | GEÇTİ |
| ↺4 | S07 | That's the safe door. Right? | 3:08 | 55 | GEÇTİ |
| ↺5 | S09 | Here's the problem | 4:03 | 55 | GEÇTİ |
| ↺6 | S10 | It isn't one number. It's two. | 4:29 | 26 | GEÇTİ |
| ↺7 | S11 | something strange is happening to it | 5:29 | 61 | GEÇTİ |
| ↺8 | S13 | Here's the strange part | 6:27 | 57 | GEÇTİ |
| ↺9 | S14 | survive the hardest moment | 7:03 | 37 | GEÇTİ |
| ↺10 | S15 | So how long until he's back to one thousand? | 7:36 | 32 | GEÇTİ |
| ↺11 | S17 | every door gets locked | 8:35 | 59 | GEÇTİ |
| ↺12 | S19 | move it to today | 9:46 | 71 | GEÇTİ |
| ↺13 | S23 | So, which door was safe? | 10:57 | 71 | GEÇTİ |
| köprü | S24 | Falling prices made a shoebox the winner (uç ekran) | 11:29 | 32 | GEÇTİ |

  Kanca sayısı: 13 ↺ + hook + köprü · en uzun aralık 71 sn (kapı ≤90)

**Abone çağrısı:** 1 adet · S11 @ 5:16
  ilk 60 sn'de yok ve ilk büyük ödülden (S10, bitiş 5:12) sonra: GEÇTİ

**Telaffuz yasak listesi** (charts, complicated, scenarios, truth, crash*, bold) anlatım+Shorts: 0 → GEÇTİ
**Tavsiye kalıbı taraması** (25 desen): 0 eşleşme → GEÇTİ
  ek: should/must/need to: 0
**Mit taraması** (suicide|jump from|window|leap): 0 → GEÇTİ
**Tez (Ö1)** "a safe place for money isn't really a place": S03 @ 0:44–0:47, S23 @ 11:19–11:23 · başta (cümle ≤60 sn'de biter) ✓ · sonda (son 90 sn) ✓

**YouTube bölümleri (betik zamanı):**
```
0:00 The Game
1:35 Door One: The Stock Market
3:10 Door Two: The Bank
5:32 Door Three: The Shoebox
7:09 The Bottom: July 1932
8:37 March 1933: Every Door Locked
9:47 The Twist: Same Door, 2026
10:57 What the Game Really Tests
```
  ilk 0:00, ≥3 bölüm, aralar ≥10 sn: GEÇTİ

**Shorts hook'ları:** "In nineteen twenty-nine, most people would have picked the wrong door." = 11 kelime · "A shoebox of cash gained power in nineteen thirty-two. In twenty twenty-six, the same math runs the other way." = 19 kelime · "Why the brown door won, and why it flips today, is in the full video." = 15 kelime
**Ö7 5-gram örtüşmesi** vs `ses-testi/okuma-metni.md`: 0.0% (0/1745) → GEÇTİ
**Ö7 5-gram örtüşmesi** vs `ses-testi/tts/anlatici-v1-metin.txt`: 0.0% (0/1745) → GEÇTİ

**Sahne başlığı zamanları betikle uyumlu:** GEÇTİ

**KAPI: GEÇTİ**

### Özet tablo

| Kapı | Ölçüm | Sonuç |
|---|---|---|
| Metin: kelime/süre | 1.678 kelime ≈ 11:44 (143 kpm); ≥1.500 ve 12 dk ±%10 (1.544–1.888) | GEÇTİ |
| Metin: ilk 15 sn net vaat | ilk 35 kelimede 1.000 $ + 3 kapı + disaster/gamble; 'surprise' 39. kelime (~16 sn) | GEÇTİ |
| Metin/Retention: ≤90 sn yeniden kanca | 13 ↺ + hook + köprü, en uzun aralık 71 sn | GEÇTİ |
| Retention: ilk 30 sn planı + retention haritası | §1 ve §3 var | GEÇTİ |
| Retention: ilk 60 sn abone yok | tek çağrı 5:16 (S11), ilk büyük ödülden (S10) sonra | GEÇTİ |
| Retention: ilk 30 sn kanal tanıtımı/logo yok | kalıp taraması 0 | GEÇTİ |
| Telaffuz listesi | charts/complicated/scenarios/truth/crash*/bold = 0 | GEÇTİ |
| Tavsiye kalıbı (P1, P4) | 25 desen + should/must/need to = 0 | GEÇTİ |
| Mit (intihar/pencere) | 0 | GEÇTİ |
| Ö1 tez başta ve sonda | 0:41–0:50 ve 11:19 | GEÇTİ |
| Ö2 / H1 ≥3 kendi veri grafiği, her kapıda birincil veri | G1 FRH · G2 FDIC · G3 FRED (+G0, G3b, G4, G5) | GEÇTİ (§11) |
| Ö7 5-gram örtüşmesi (önceki metinler) | %0,0 / %0,0 | GEÇTİ |
| Bölümler | 8 bölüm, 0:00'dan, aralar ≥10 sn | GEÇTİ |
| Shorts ≤60 sn | Shorts 1: 140 kelime ≈59 sn · Shorts 2: 139 kelime ≈58 sn | GEÇTİ |
| D1–D7, P1–P6, H1–H5 | §11 tablosu (17/17 uygulandı; P5/P6/H4/H5'in metin dışı kısmı F5/F8'e not) | GEÇTİ |

**Açık riskler (doğrulayıcı/politika için):** (1) HUL [AÖ] ikincil kopya — NYT birincil sayfası ücretli; (2) BEA-666 DBnomics yansısından, BEA sitesi açılmadı; (3) "more than one bank in three" iki kaynağın birleşimi [H]; (4) "Some reopened… Most were closed for good" 1930–31 ifadesinin 1930–33'e genellemesi; (5) TTS duraklamaları gerçek süreyi uzatabilir (üst tahmin ≈12:06) — kanca aralıkları F7'de gerçek sesle yeniden ölçülmeli.

