# F3 — Tam metin · S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It"

İLERLEME: v0.1 taslak (rakamlar [R?] yer tutucu; rakam-tablosu.md bekleniyor) → sıradaki: tabloyla eşleme + kapı (§12).
**Kanal:** Toonomy (@toonomy) · **Anlatıcı:** Leo (kurgusal çizgi maskot; bu videoda nakliye ekibi şefi; danışman değil) · **Ses:** Kokoro `am_fenrir` 0.9 (**160 kpm**)
**Sütun:** C · **Yazar:** senaryo-yazari · **Tarih:** 2026-11-04 · **Sürüm:** v0.1
**Rakam kuralı:** ANLATIM'daki her rakam kilitli `03-metin/rakam-tablosu.md` satırından. Tabloda olmayan rakam GÖRSEL'de **`[R?`** ile işaretli. Örnek aile (Okafor) yalnız **kutu** sayar (10 kutu = ailenin örnek serveti); dolar tutarı yok ("illustration, not an average").
**Olgu kuralı (karne 6):** olgu taşıyan her cümlenin kaynak etiketi GÖRSEL'deki **Kaynak:** satırında. Etiketler §7.
**Yazım kuralı (TTS):** ANLATIM'da sayılar yazıyla, rakam GÖRSEL'de. Yayın gününe bağlı zaman sözcüğü yok (H6).
**Kapı betiği:** `03-metin/metin-kontrol.py` (v4, bu klasör; çıktı §12). Zamanlar betikten: kelime ÷ 160 kpm.

---

## 1. İlk 30 sn planı

| Zaman | Ne söylenir | Ne görünür | Amaç |
|---|---|---|---|
| 0:00–0:15 | Hook (S01): 124 T$ → 18 T$ bağış, 54 T$ önce eşte → "Let's follow one family's boxes and see what reaches the kids." | **≤3 sn:** kamyonun arka kapısında "$124 TRILLION" yazan dev kutu; kutunun köşesinden banknot damlar. Sonra kutu ikiye ayrılır (18 bağış / 54 "SPOUSE FIRST" etiketi). | Somut özne (bir ailenin kutuları) + ters köşe + net vaat; logo/intro/"hi guys" YOK |
| 0:15–0:38 | Başlık vaadi: "often called the biggest inheritance in history" + izleyici bağı (mirasçı / ev alıcısı) + videonun sonunda ne öğrenileceği (mirasçı neden daha az ve daha geç alabilir, en büyük sızıntı hangisi) | Ülke haritası → tek ev; "HEIR? HOME BUYER? BOTH?" | Başlık + thumbnail ("WHO GETS IT?") vaadi ilk 30 sn'de karşılanır |
| 0:38–0:55 | Leo kendini nakliye şefi olarak tanıtır, **tez** | Leo kamyon kapısında, elinde pano; tez kamyonun yan yüzüne yazılır | Tez ilk 60 sn'de |

Abone/beğeni çağrısı ilk 60 sn'de **yok**. Abone ol animasyonu 3 kez (ABONE-1…3, §3), sesli abone çağrısı yok.

---

## 2. TAM METİN (iki sütun)

Biçim: `### Sxx · başlangıç–bitiş · süre` + iki sütunlu tablo. GÖRSEL: **Sahne**, **Grafik**, **Leo**, **Ekran**, **Kaynak**, **↺** (yeniden kanca).
**Sabit set:** soğuk mavi akşam yolu; sıcak turuncu nakliye kamyonu (logosuz). Leo = tek tekrar eden karakter (H4). Okafor ailesi **rig'siz**: kapı eşiğinde 4 düz siluet (yüzsüz, ikon) + etiketli kutular; her Okafor karesinde köşe etiketi **"EXAMPLE FAMILY · ILLUSTRATION"** (P2).
**Kutu renkleri (bütün video sabit):** ev kutuları kiremit kırmızı (4) · emeklilik birikimi lacivert (4) · banka birikimi yeşil (2). Her kutunun üstünde "TO: THE KIDS". Leo'nun panosunda 6 satır: LIVING · CARE · SPOUSE · GIVING · HOUSE · TAX & TIME.
**Ölüm soyut (P2):** ölüm hiç gösterilmez; "first parent passes away" anında bir siluet kapı eşiğinden yumuşakça solar, sıcak ışık kalır.

## Bölüm 1 — The Number on the Truck

### S01 · 0:00–0:15 · 15 sn · HOOK
| ANLATIM | GÖRSEL |
|---|---|
| One hundred twenty-four trillion dollars will change hands in America through twenty forty-eight, Cerulli estimates. But eighteen trillion goes to charity, and fifty-four trillion stops at a spouse first. Let's follow one family's boxes and see what reaches the kids. | **Sahne:** 0:00 gece yolu, kamyonun arka kapısı açılır: içinde tek dev kutu "$124 TRILLION · THROUGH 2048". 0:02 kutunun alt köşesinden banknot damlar (H3 ≤3 sn görsel değişim). "charity"de kutudan küçük bir dilim kayar: "$18T → CHARITY"; "spouse"da büyük bir dilim yan şeride ok ile ayrılır: "$54T → SPOUSE FIRST" (kırmızı değil, sarı: kayıp değil, sapma). "one family's boxes"ta dev kutu 10 küçük kutuya bölünür. **Leo:** kamyonun yanında, panoyu kaldırır. **Ekran:** küçük not "Estimate: Cerulli Associates, Dec 2024". **Kaynak:** [K-CER] (124 / 18 / 54 / 2048). **Kritik yol (H4):** damlama + kutu bölünmesi F5 testine girer. |

### S02 · 0:15–0:40 · 25 sn
| ANLATIM | GÖRSEL |
|---|---|
| People often call it the biggest inheritance in history. But that's one number for a whole country, stretched over decades. Maybe you'll inherit something one day. Maybe you're buying a home another family is leaving. Either way, this reaches you. So on this trip, we'll find out why heirs might get less than the headline sounds, and get it later. And which leak is the biggest. | **Sahne:** ABD haritası (düz, sınır çizgisi ince) üstünde binlerce küçük kamyon → kamera tek bir sokağa, tek bir eve iner. "inherit"te kapıda kutu; "buying a home"da kapıdan çıkan kutular ve içeri giren genç siluet (yüzsüz). **Ekran:** "OFTEN CALLED THE BIGGEST INHERITANCE IN HISTORY" (D3) → "HEIR? HOME BUYER? BOTH?" → "LESS? LATER?" + soru işaretli kutu "BIGGEST LEAK = ?" (sona kadar açık döngü). **Kaynak:** [T] ("often called" = yaygın adlandırma, yorum). **↺ 0:38 "And which leak is the biggest"**. |

### S03 · 0:40–0:57 · 17 sn
| ANLATIM | GÖRSEL |
|---|---|
| I'm Leo, a cartoon moving-crew boss. I load one generation's boxes and drive them to the next. Before I start the engine, here's what this road has taught me. An inheritance isn't a number. It's whatever is left at the end of a long road. | **Leo:** kamyon kapısında, nakliye yeleği + pano + omzunda bant rulosu; "cartoon" kelimesinde göz kırpar. **Ekran:** tez kamyonun yan yüzüne boya ile yazılır: "AN INHERITANCE ISN'T A NUMBER. IT'S WHATEVER IS LEFT AT THE END OF A LONG ROAD." **Leo:** tezde ciddi, kameraya bakar; sonra kontağı çevirir (motor SFX). **Kaynak:** — (tez, yorum). |

### S04 · 0:57–1:39 · 42 sn · İLK BÜYÜK ÖDÜL
| ANLATIM | GÖRSEL |
|---|---|
| First, let's read the label on that big number. It's not cash sitting in a vault. It's an estimate of homes, retirement accounts, businesses and savings, added up by a research firm called Cerulli Associates. Nearly one hundred trillion of it comes from baby boomers and older generations. About one hundred five trillion is expected to reach heirs. About eighteen trillion goes to charity. And here's the twist. The fifty-four trillion that stops at a spouse is not extra money. It's already inside the total. So it's not a leak. It's a detour. The money goes to the surviving husband or wife first, and only later to the kids. Remember that word. Detour. | **Sahne:** Leo dev kutunun etiketini büyüteçle okur. **Grafik G1 (kendi grafiğimiz, tek çubuk):** "$124T" çubuğu iki renge bölünür: "~$105T HEIRS" (lacivert) + "~$18T CHARITY" (yeşil) (D2: toplam 123 ≈ 124, yuvarlama notu "figures rounded"). Sonra **sarı bir köşeli ayraç** lacivert bölümün üstüne gelir: "$54T goes to a spouse FIRST — inside the total, not on top" (D2: çıkarma yok, ayrı çubuk yok). Küçük not: "~$100T from Baby Boomers and older (81%)". **Leo:** "detour"da kamyonu yan şeride çevirir, panoya "DETOUR ≠ LEAK" yazar. **Kaynak:** [K-CER] (≈100 / 105 / 18 / 54; "includes homes, accounts…" tanımı [K-CER] yöntem notu, [R?] tablo satırı bekleniyor). |

### S05 · 1:39–1:48 · 9 sn
| ANLATIM | GÖRSEL |
|---|---|
| But one number for a whole country hides what happens inside one home. To see the real leaks, we need one family, and one truck. | **Sahne:** kamera haritadan tek bir eve iner, kapıda 4 siluet. **Ekran:** "ONE FAMILY. ONE TRUCK." **↺ 1:44 "To see the real leaks, we need one family"**. Sahne sonu 1,5 sn nefes → **ABONE-1**. |

## Bölüm 2 — Loading the Okafors

### S06 · 1:48–2:17 · 29 sn
| ANLATIM | GÖRSEL |
|---|---|
| Meet the Okafors. They're an example family, made up for this trip. Two parents, two grown kids, and everything they own, packed into ten boxes. Four boxes for the house. Four for retirement savings. Two for money in the bank. Each box is one tenth of the family's wealth. There are no dollar signs on purpose. This is an illustration, not an average. On the side of every box, I write the same address. To: the kids. | **Sahne:** kapı eşiğinde 4 düz siluet (iki büyük, iki genç yetişkin; yüzsüz) + köşe etiketi "EXAMPLE FAMILY · ILLUSTRATION" (P2, H4). Kutular tek tek kamyona yüklenir: 4 kiremit (HOUSE), 4 lacivert (RETIREMENT), 2 yeşil (BANK). **Ekran:** "10 BOXES = 100% OF THEIR WEALTH · ILLUSTRATION, NOT AN AVERAGE". **Leo:** her kutuya keçeli kalemle "TO: THE KIDS" yazar. **Kaynak:** [ÖRNEK] (kurgusal). |

### S07 · 2:17–2:32 · 15 sn
| ANLATIM | GÖRSEL |
|---|---|
| My clipboard has six stops between here and there. Some stops take boxes. One stop takes none, but it costs years. And the stop everyone fears the most turns out to be one most trucks drive right past. Let's roll. | **Sahne:** Leo panoyu kameraya gösterir: LIVING · CARE · SPOUSE · GIVING · HOUSE · TAX & TIME. Yol haritası animasyonu: 6 durak tabelası yol boyunca dizilir. Kamyon yola çıkar (motor + korna SFX). **↺ 2:25 "And the stop everyone fears the most"** (Bölüm 6'ya kadar açık döngü). |

## Bölüm 3 — Living and Care

### S08 · 2:32–3:09 · 37 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop one is good news. Living a long time. In America, a person who reaches sixty-five can expect, on average, around twenty more years of life. That's a lot of groceries, heating bills, doctor visits, and trips to see the grandkids. And that's exactly what retirement savings are for. They were built to be spent. So I cross out two boxes. Label: spent on living. Is that a leak? Not really. That's the boxes doing their job. But it shows something the big number leaves out. A forecast counts money before it's lived on. A family counts it after. | **Sahne:** durak 1 tabelası "LIVING". Kamyonun arkasında iki lacivert kutu yavaş yavaş açılır, içinden market poşeti, ısıtıcı faturası, tren bileti (torun ziyareti) çıkar. **Grafik:** yaşam süresi çubuğu "65 → ~85" [R? SSA, 65 yaşında kalan ortalama ömür; tablo satırı bekleniyor]. **Leo:** panoda LIVING satırına "−2" yazar, iki kutuya "SPENT ON LIVING" damgası. **Ekran:** "A FORECAST COUNTS MONEY BEFORE IT'S LIVED ON." **Kaynak:** [K-SSA] [R?] (≈20 yıl) · son iki cümle [T]. |

### S09 · 3:09–3:16 · 7 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop two is the one families talk about the least. And it's the reason I carry this tape. | **Sahne:** durak 2 tabelası sisli yoldan belirir: "CARE". **Leo:** omzundaki bant rulosunu sallar. **↺ 3:09 "Stop two is the one families talk about the least"**. |

### S10 · 3:16–3:56 · 40 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop two is care. As people get older, many need help with daily life. Getting dressed. Cooking. Taking medicine on time. A U.S. government office for long-term care says a person turning sixty-five has about a seventy percent chance of needing some kind of long-term care later in life. Women, on average, need it for longer than men. A lot of that care happens at home, often from family. But when it means a nursing home, the bill is big. A national survey by Genworth and CareScout put the median cost of a private room at about one hundred twenty-eight thousand dollars a year, in twenty twenty-four. | **Sahne:** ev içi silüet sahneleri (yüzsüz): düğme ilikleyen el, ocak, ilaç kutusu. **Grafik G2:** 10 küçük insan ikonundan 7'si renklenir: "~70% OF PEOPLE TURNING 65 WILL NEED SOME LONG-TERM CARE" [R? ACL] · yanında "WOMEN 3.7 YRS · MEN 2.2 YRS (average need)" [R? ACL] · sonra fatura kartı "NURSING HOME, PRIVATE ROOM: ~$127,750 / YEAR (2024 national median)" [R? CareScout 2024]. **Kaynak:** [K-ACL] (%70; kadın > erkek) · [K-GCS] (127.750 $, 2024) · "a lot of care happens at home" [K-ACL] [R? tablo satırı] . |

### S11 · 3:56–4:28 · 32 sn
| ANLATIM | GÖRSEL |
|---|---|
| Why does this one leak so much? Because Medicare, the health insurance for older Americans, generally doesn't pay for long stays of this kind of daily care. So in many cases the bill is paid from savings first. Medicaid, the program for people with low income, can step in, but usually only after most of a person's own savings are used up. For the Okafors, I cross out one box. Label: care. In a different family, it could be zero boxes. Or it could be four. | **Sahne:** iki kapı: "MEDICARE"nin önünde "LONG STAYS OF DAILY CARE: GENERALLY NOT COVERED" levhası; "MEDICAID" kapısının önünde "AFTER MOST SAVINGS ARE USED UP" levhası (mekanizma, tavsiye yok, P1). Bir yeşil kutu kapı aralığından içeri itilir. **Leo:** panoya CARE "−1"; sonra ekrana iki hayalet kamyon: biri 0 kutu, biri 4 kutu kaybıyla ("IT VARIES A LOT"). **Kaynak:** [K-MCR] (Medicare uzun süreli bakımı genellikle karşılamaz) · [K-MCD] (Medicaid gelir/varlık şartı) [R? tablo satırı] · Okafor [ÖRNEK]. |

### S12 · 4:28–4:42 · 14 sn
| ANLATIM | GÖRSEL |
|---|---|
| And this is where my job gets messy. The care box has a soft bottom. I tape it. Then a different corner starts to drip. So I tape that one too. Okay. That's a two-tape stop. | **Karakter anı (H4, kritik yol):** Leo kutunun dibini bantlar (bant SFX), para başka köşeden damlar, Leo ikinci bandı çeker, bakar, kameraya döner. **Ekran:** panoda "TAPE USED: 2". **Kaynak:** — (gag). |

## Bölüm 4 — The Detour and the Gift

### S13 · 4:42–5:13 · 31 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop three looks like the biggest leak on the whole list. It isn't a leak at all. When the first parent passes away, the truck doesn't go to the kids. It turns around and parks across the street, at the surviving husband or wife. Cerulli puts this detour at about fifty-four trillion dollars. Nearly forty trillion of that is expected to go to widowed women from the boomer and older generations. One reason is simple: on average, women live longer than men. | **Sahne:** kamyon kavşakta yan yola döner (sinyal SFX), "SPOUSE FIRST" tabelası. Kapı eşiğindeki iki büyük siluetten biri yumuşakça solar; sıcak ışık kalır (P2, ölüm soyut). Kamyon karşı kaldırıma, aynı evin yanındaki kapıya yanaşır. **Grafik:** S04'teki sarı ayraç geri gelir: "$54T SPOUSE FIRST · ~$40T TO WIDOWED WOMEN". **Kaynak:** [K-CER] (54 / ≈40) · "women live longer" [K-SSA] [R?]. **↺ 4:42 "Stop three looks like the biggest leak on the whole list"**. |

### S14 · 5:13–5:47 · 34 sn · DORUK-1 (sızıntı 3 ters köşesi)
| ANLATIM | GÖRSEL |
|---|---|
| Now look at my clipboard. How many boxes did we lose at stop three? Zero. Nothing leaked. The kids just wait. But here's the part the headline hides. While the boxes sit in that one home, the first two stops keep working. More years of living. Maybe another round of care. The detour doesn't take any boxes. It gives the other leaks more time. Think of it like a relay race. The baton goes to the partner first. The kids are the last runners, waiting at the far end of the track. | **Sahne:** panoda SPOUSE satırına "−0" + yanına kum saati ikonu "+YEARS". Kamyon park hâlinde, takvim yaprakları uçar; LIVING ve CARE tabelaları kamyonun önünden **ikinci kez** geçer (döngü animasyonu). **Grafik:** bayrak yarışı pisti: koşucu 1 (siluet, ebeveyn) → koşucu 2 (eş) → pistin ucunda bekleyen iki genç siluet. **Leo:** çubuğu (baton) havaya kaldırır. **Kaynak:** [T] (mekanizma yorumu; D2: eş payı gecikme, kayıp değil). ABONE bu sahnenin üstüne gelmez (H5). |

### S15 · 5:47–5:54 · 7 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop four is the only part of the headline that truly skips the kids. And it happens on purpose. | **Sahne:** durak 4 tabelası "GIVING", tabelanın üstünde küçük kalp. **↺ 5:47 "Stop four is the only part of the headline that truly skips the kids"**. |

### S16 · 5:54–6:27 · 32 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop four is giving. Cerulli estimates that about eighteen trillion dollars goes to charity. Schools. Hospitals. Churches, mosques and temples. Research. The causes people cared about all their lives. This one is easy to talk about, because it's a choice, not an accident. In our example, the Okafors give one box to the school where they met. I cross it out with a smile. Label: given. It's still a box that won't ride in the kids' truck. But nobody at the school calls it a leak. | **Sahne:** kamyon bir okulun önünde durur (genel bina, isimsiz); bir yeşil kutu kapıya bırakılır, pencerelerden küçük el sallayan siluetler. Okul/hastane/ibadethane ikonları (genel, sembolsüz değil ama eşit boyutta, P2). **Grafik:** S04 çubuğundaki "~$18T CHARITY" bölümü parlar: "THE ONE PART THAT SKIPS HEIRS" (D2). **Leo:** panoda GIVING "−1", gülümser. **Kaynak:** [K-CER] (18) · Okafor [ÖRNEK]. Sahne sonu 1,5 sn nefes → **ABONE-2**. |

## Bölüm 5 — The Heaviest Box

### S17 · 6:27–7:05 · 38 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop five is the heaviest box on the truck. The house. For the Okafors, it's four boxes out of ten. And a house has a problem the other boxes don't have. You can't cut it in half. Two kids, one house. One of them wants to keep it. The other one needs the cash. If neither can buy the other out, the house goes up for sale. And selling has its own costs. Agent fees. Repairs that were put off for years. Property taxes and bills while it sits empty. Sometimes the house was sold years earlier, to pay for stop two. | **Sahne:** kamyonun içinde 4 kiremit kutu birbirine yapışık (tek parça ev maketi gibi). İki genç siluet maketin iki yanından tutar, maket ortadan çekilir ama bölünmez (gag). Tek bir "SOLD" kartı (H7: satılık tabelalar sokağı YOK, tek ev, tek kart). Fatura kartları uçar: "AGENT FEES · REPAIRS · PROPERTY TAX & BILLS" (rakamsız). Son cümlede geriye sarma: aynı ev daha önce CARE durağında satılırken (soluk sepya). **Kaynak:** mekanizma [T] (rakam yok, D5) · Okafor [ÖRNEK]. H7: ev bölümü ≤90 sn (S17+S18). |

### S18 · 7:05–7:13 · 8 sn
| ANLATIM | GÖRSEL |
|---|---|
| None of this takes a whole box. It takes a slice. And then I find my third drippy corner. More tape. | **Sahne:** kiremit kutudan ince bir dilim kesilir ("−A SLICE"). **Leo:** üçüncü köşeyi bantlar, bant rulosu belirgin incelmiştir. **Ekran:** "TAPE USED: 3". **Kaynak:** [ÖRNEK]. |

## Bölüm 6 — The Leak Everyone Fears

### S19 · 7:13–7:53 · 40 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop six is the one everybody fears. Taxes. So let's read the sign on this stop. In America, the federal estate tax only applies to estates worth more than fifteen million dollars per person, as of twenty twenty-six. A married couple can usually pass on about thirty million dollars before it applies. The Okafors are nowhere near that line. Their truck drives right past this stop. And they're not unusual. Only a tiny share of estates pay any federal estate tax at all, about one in a thousand. Some states have their own estate or inheritance taxes, with lower lines, so the map isn't the same everywhere. | **Sahne:** büyük, ürkütücü gümrük gişesi "TAX" (gölgeli, gök gürültüsü SFX) → Leo tabelayı okur, gök gürültüsü kesilir. **Grafik G3:** dikey çizgi "FEDERAL ESTATE TAX STARTS: $15M PER PERSON (2026)" [R? IRS] · "~$30M FOR A MARRIED COUPLE" [R? IRS taşınabilirlik] · Okafor kutuları çizginin çok altında. Sonra 1.000 küçük kutudan 1'i kırmızı: "≈1 IN 1,000 ESTATES PAYS" [R? JCT/TPC]. Küçük not: "U.S. federal rules, as of 2026. Some states differ." (D5). Gişenin bariyeri kalkar, kamyon geçer. **Kaynak:** [K-IRS] (15 M $, 2026) · [K-IRS] [R?] (≈30 M $ çift) · [K-TPC] [R?] (≈1/1.000) · eyalet vergileri [K-TPC] [R?]. P1: yasa değişikliği, parti, politikacı anılmaz. |

### S20 · 7:53–8:06 · 13 sn
| ANLATIM | GÖRSEL |
|---|---|
| That's the surprise of this whole road. The leak people fear the most is one most trucks never hit. For most families, the leaks that matter are the quiet ones. Living. Care. And time. | **Sahne:** Leo panoda TAX satırına "−0 (for this family)" yazar, sonra LIVING, CARE satırlarının altını çizer. **Ekran:** "THE LOUD LEAK IS SMALL. THE QUIET LEAKS ARE BIG." (A3 kapanır: korkulan durak). **Kaynak:** [T] (S19 olgusundan çıkarım; "most trucks" = ≈1/1.000 satırına bağlı). |

### S21 · 8:06–8:12 · 6 sn
| ANLATIM | GÖRSEL |
|---|---|
| Which brings us to the last sign on stop six. It isn't a cost. It's a clock. | **Sahne:** gişenin arkasında yol kenarında dev bir saat. **↺ 8:06 "Which brings us to the last sign on stop six"**. |

### S22 · 8:12–9:02 · 50 sn
| ANLATIM | GÖRSEL |
|---|---|
| Put the long life and the detour together, and the boxes arrive late. The kids on the label might have grey hair of their own by then. You can see it in Cerulli's numbers. In the ten years after twenty twenty-four, it expects Gen X to receive about fourteen trillion dollars, and millennials about eight trillion. Over the whole stretch to twenty forty-eight, millennials end up with the most, about forty-six trillion. In other words, a lot of this money reaches people in the middle of their lives, not at the start. And that changes what the money does. Money that arrives when you're starting out might help with a first home, or a first business. Money that arrives later often goes somewhere else. Your own retirement. Your own kids. Same boxes. Different job. | **Sahne:** "TO: THE KIDS" etiketindeki iki genç siluetin saçları zaman atlamasıyla griye döner (yumuşak gag). **Grafik G4:** iki kuşak çubuğu, iki dönem: "2024–2034: GEN X ~$14T · MILLENNIALS ~$8T" → "THROUGH 2048: MILLENNIALS ~$46T (MOST)" [R? Cerulli]. **Ekran:** iki yol işareti "STARTING OUT → FIRST HOME / BUSINESS" ve "LATER → OWN RETIREMENT / OWN KIDS". **Kaynak:** [K-CER] (14 / 8 / 46) · "middle of their lives" [T] · son 6 cümle [T]. **↺ 9:01 "Same boxes. Different job."** |

### S23 · 9:02–9:06 · 4 sn
| ANLATIM | GÖRSEL |
|---|---|
| So, how many boxes are left when the doors finally open? | **Sahne:** kamyon son viraja girer, ufukta "TO: THE KIDS" yazan ev. **↺ 9:03 "how many boxes are left when the doors finally open"**. |

## Bölüm 7 — Arrival

### S24 · 9:06–9:36 · 30 sn · DORUK (varış envanteri)
| ANLATIM | GÖRSEL |
|---|---|
| The truck stops. I open the doors, and I read my clipboard out loud. Loaded: ten boxes. Stop one, living: minus two. Stop two, care: minus one. Stop three, the detour: minus zero, plus a few years. Stop four, giving: minus one. Stop five, the house: minus a slice. Stop six, taxes: minus zero, for this family. Delivered: six boxes, minus a slice, years later than planned. Split between two kids, that's about three boxes each, a little less. | **Sahne (K1 varış sahnesi):** kapılar açılır, Leo panoyu yüksek sesle okur; her satırda ilgili kutu çizgisi ekranda üstü çizilir. **Grafik G5 (Okafor şelalesi, tek şelale, "EXAMPLE FAMILY · ILLUSTRATION"):** 10 → −2 LIVING → −1 CARE → 0 SPOUSE (+YEARS, sarı saat) → −1 GIVING → −slice HOUSE → 0 TAX → **6 − slice, LATER** → 2 kişiye bölünür "≈3 EACH". D2: şelale 124'ten değil, ailenin kendi 10 kutusundan başlar. **Kaynak:** [ÖRNEK] (kutu aritmetiği `veri/hesap.py` assert). |

### S25 · 9:36–10:04 · 28 sn
| ANLATIM | GÖRSEL |
|---|---|
| Is that a sad story? Look at the list again. A long life. Care when it was needed. A gift they chose. That's not a family that lost its money. It's a family that used it. And remember, this is one example. A family with smaller savings might arrive with no boxes at all. A very wealthy family might pass stop six with a much bigger bill, and still arrive with a full truck. | **Sahne:** iki genç siluet kutuları içeri taşır, birinin elinde aile fotoğrafı çerçevesi (yüzsüz). Sonra yan yana üç hayalet kamyon: boş kasa · Okafor (6) · konvoy gibi uzun kamyon (TAX gişesinde durur, sonra geçer). **Kaynak:** [T] (örnek karşılaştırma; rakamsız). |

### S26 · 10:04–10:25 · 21 sn
| ANLATIM | GÖRSEL |
|---|---|
| Now zoom out, back to that giant number. Cerulli says more than half of it, about sixty-two trillion dollars, comes from just two percent of households, the wealthiest families. So the headline is real. It's just lumpy. For a few families, the truck is a whole convoy. For most, it's a few boxes, and they come late. | **Sahne:** kamera Okafor evinden yükselir, haritaya döner. **Grafik G6 ("bölünmüş tablo" kartı, K1):** 100 hanelik ızgarada 2 hane altın değil **turuncu** (palet: kamyon rengi) → çubuk "$124T": "~$62T FROM 2% OF HOUSEHOLDS" / "THE REST FROM 98%". Altında: "THE HEADLINE IS REAL. IT'S JUST LUMPY." Haritadaki kamyonların birkaçı konvoy, çoğu tek küçük kamyon. **Kaynak:** [K-CER] (62 / %2 / "more than half"). |

### S27 · 10:25–10:42 · 17 sn
| ANLATIM | GÖRSEL |
|---|---|
| Could this road change? It could. If care keeps getting more expensive, stop two may grow. If tax laws change, stop six may move. This isn't a forecast for any family, and it isn't a plan. It's a map of where the boxes tend to go. | **Sahne:** yol haritası tekrar görünür; CARE tabelası hafifçe büyür (kesik çizgi = "may"); TAX tabelası kesik çizgiyle başka yere kayıp geri gelir. Dallanan yol YOK (K1: tek yol). **Ekran:** "NOT A FORECAST. NOT A PLAN. A MAP." **Kaynak:** [T] (koşullu, "could/may/if"; parti/politikacı yok P1). |

### S28 · 10:42–10:57 · 15 sn · TEZ
| ANLATIM | GÖRSEL |
|---|---|
| So the next time someone says one hundred twenty-four trillion dollars, picture the truck. An inheritance isn't a number. It's whatever is left at the end of a long road. And on this road, I'm going to need more tape. | **Sahne:** kamyonun yan yüzündeki tez yazısı (S03) yakın plan. **Karakter anı (H4):** Leo boş kutuyu bırakır, incecik kalmış bant rulosunu omzuna atar, kameraya bakar: "I'm going to need more tape." Kısa müzik vurgusu. **Kaynak:** [K-CER] (124, hook rakamı). Sahne sonu 1,5 sn nefes → **ABONE-3**. |

### S29 · 10:57–11:09 · 11 sn · KÖPRÜ
| ANLATIM | GÖRSEL |
|---|---|
| There's one box we only opened for a minute. The house. What happens to a whole neighborhood when many houses change hands at once is a story for another road. | **Sahne:** kiremit kutu kamyonun içinde tek başına parlar; kamera yola döner, ufukta ışıkları yanan bir mahalle silueti (satılık tabelası YOK, H7). **Uç ekran:** genel merak köprüsü (yayında olmayan videoya söz yok; S04 yayınlanınca uç ekran öğesi o olur, ses değişmez). |

---

## 3. Retention haritası

(v0.1: zamanlar betik ölçümünden sonra güncellenir.)

---

## 4. YouTube bölümleri (chapters)

(betik çıktısından)

---

## 5. Shorts kancaları ve kesit önerileri (2 adet, her biri ≤60 sn, 9:16)

### Shorts 1 — "The detour"
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "One hundred twenty-four trillion dollars will change hands in America through twenty forty-eight."
- **Kesit:** S01 (rakam) → S13 (eş sapması, kısaltılmış) → S14 ilk 7 cümle → kapanış sorusu. Cevap (sapma sırasında LIVING/CARE yeniden çalışır, varışta kaç kutu kalır) yalnız uzun videoda.
- **9:16 notu:** kamyon dikey kadrajda yan şeride döner; sarı ayraç "$54T SPOUSE FIRST · inside the total".
- **Okunacak tam metin (betik bunu sayar):** <<One hundred twenty-four trillion dollars will change hands in America through twenty forty-eight. That's an estimate from Cerulli Associates. But here's the twist. About fifty-four trillion of it doesn't go to the kids first. It stops at a husband or wife. Nearly forty trillion of that goes to widowed women. So is that a leak? No. Nothing is lost. The truck just takes a detour, and the kids wait. But the wait isn't free. Something happens to the boxes while they sit in that one home. So how many boxes are left when the truck finally reaches the kids?>>

### Shorts 2 — "The leak people fear"
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "Here's the leak people fear most when money is passed down. Taxes."
- **Kesit:** S19 (vergi eşiği) → S20 ilk iki cümle → kapanış sorusu. Cevap (sessiz sızıntılar: yaşam, bakım, zaman) yalnız uzun videoda.
- **9:16 notu:** gişe bariyeri dikeyde; "U.S. federal rules, as of 2026" satırı altta sabit.
- **Okunacak tam metin (betik bunu sayar):** <<Here's the leak people fear most when money is passed down. Taxes. So let's read the sign. In America, the federal estate tax only applies to estates worth more than fifteen million dollars per person, as of twenty twenty-six. A married couple can usually pass on about thirty million before it applies. Only about one in a thousand estates pays any federal estate tax at all. So for most families, the scary stop is just a sign by the road. Then where does the money really go on the way to the kids?>>

---

## 6. Uç ekran köprüsü (2 sürüm, seçilen: A)
- **A (seçilen, S29):** "There's one box we only opened for a minute. The house… a story for another road." → Genel merak köprüsü; S04 (mahalle postacısı) seri devamına doğal geçiş, yayında olmayan videoya söz vermez.
- **B (elenen):** "Next time, we follow the house box down a street full of for-sale signs." → S04 yayında değil (yanıltıcı söz) + H7 görsel örtüşmesi.

---

## 7. Rakam ve olgu tablosu (metindeki her rakam/olgu → kaynak etiketi → `rakam-tablosu.md` satırı)

| Etiket | Kaynak | Metindeki kullanım | Tablo satırı |
|---|---|---|---|
| [K-CER] | Cerulli Associates basın bülteni, 5 Ara 2024 ("Cerulli Anticipates $124 Trillion in Wealth Will Transfer Through 2048") | 124 / 2048 / ≈105 heirs / ≈18 charity / 54 spouse / ≈40 widowed women / ≈100 (%81) boomers+older / ≈62 (%2 hane, ">50%") / Gen X 14 + Millennials 8 (10 yıl) / Millennials 46 (2048'e kadar) | [R?] |
| [K-SSA] | SSA dönem/kohort yaşam tablosu | 65 yaşında ≈20 yıl; kadın > erkek | [R?] |
| [K-ACL] | ACL / HHS LongTermCare "How much care will you need" | ≈%70; kadın 3,7 yıl / erkek 2,2 yıl; bakımın çoğu evde | [R?] |
| [K-GCS] | Genworth & CareScout Cost of Care Survey 2024 (Mart 2025) | özel oda medyan 127.750 $/yıl (2024) | [R?] |
| [K-MCR] | Medicare.gov "Long-term care" | uzun süreli gündelik (custodial) bakımı genellikle karşılamaz | [R?] |
| [K-MCD] | Medicaid.gov uygunluk | gelir/varlık şartı ("after most savings are used up") | [R?] |
| [K-IRS] | IRS Rev. Proc. 2025-32 / IRS "Estate tax" | 15 M $ kişi başı (2026); çift ≈30 M $ (taşınabilirlik) | [R?] |
| [K-TPC] | JCT / Tax Policy Center | ≈1/1.000 terekenin federal emlak vergisi ödemesi; eyalet vergileri | [R?] |
| [ÖRNEK] | Kurgusal Okafor ailesi | 10 kutu: 4 ev, 4 emeklilik, 2 banka; −2, −1, 0, −1, −dilim, 0 → 6 − dilim, ≈3 her biri | `veri/hesap.py` |
| [T] | Yorum | tez, mekanizma çıkarımları | — |

---

## 8. Telaffuz notları (ses-yonetmeni; Kokoro am_fenrir 0.9)
- Kontrol edilecek: **Cerulli** (che-ROO-lee; Kokoro yanlış okursa metinde "Cerulli Associates" yerine "the research firm Cerulli" kalır, gerekirse fonetik "Che-roo-lee" yalnız TTS girdisinde), **Okafor** (oh-KAH-for), **Genworth**, **CareScout**, **Medicaid / Medicare**, **millennials**, **inheritance**. Yasak liste (charts, complicated, scenarios, truth, crash*, bold) betikle 0.
- "U.S." noktalı. Sayılar yazıyla; "twenty forty-eight" ve "twenty twenty-four" Amerikan okunuşu.

---

## 9. Zor bölümlerin 2 versiyonu ve eleme
(§12 ölçümünden sonra doldurulur.)

---

## 10. D / P / K / H düzeltmeleri — nerede uygulandı
(§12 ölçümünden sonra doldurulur.)

---

## 11. Leo rol kaydı ve sonraki ajanlara notlar
(§12 ölçümünden sonra doldurulur.)

---

## 12. Test kapısı sonuçları
(betik çıktısı)
