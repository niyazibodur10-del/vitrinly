# F3 — Tam metin · S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It"

İLERLEME: tamam (v1.0: rakam-tablosu R01–R27 ile eşlendi, açık [R?] 0, kapı GEÇTİ §12) → finans-dogrulayici ‖ monetizasyon-uyum-uzmani.
**Kanal:** Toonomy (@toonomy) · **Anlatıcı:** Leo (kurgusal çizgi maskot; bu videoda nakliye ekibi şefi; danışman değil) · **Ses:** Kokoro `am_fenrir` 0.9 (**160 kpm**)
**Sütun:** C · **Yazar:** senaryo-yazari · **Tarih:** 2026-11-04 · **Sürüm:** v1.0
**Rakam kuralı:** ANLATIM'daki her rakam kilitli `03-metin/rakam-tablosu.md` satırından. Tabloda olmayan rakam GÖRSEL'de **`[R?`** ile işaretlenir (v1.0'da 0). Örnek aile (Okafor) yalnız **kutu** sayar (10 kutu = ailenin örnek serveti); dolar tutarı yok ("illustration, not an average").
**Olgu kuralı (karne 6):** olgu taşıyan her cümlenin kaynak etiketi (R-kodu, [ÖRNEK] veya [T]) GÖRSEL'deki **Kaynak:** satırında; eşleme §7.
**Yazım kuralı (TTS):** ANLATIM'da sayılar yazıyla, rakam GÖRSEL'de. Yayın gününe bağlı zaman sözcüğü yok (H6).
**Kapı betiği:** `03-metin/metin-kontrol.py` (v4, bu klasör; çıktı §12). Zamanlar betikten: kelime ÷ 160 kpm.

---

## 1. İlk 30 sn planı

| Zaman | Ne söylenir | Ne görünür | Amaç |
|---|---|---|---|
| 0:00–0:15 | Hook (S01): 124 T$ → 18 T$ bağış, 54 T$ önce eşte → "Let's follow one family's boxes and see what reaches the kids." | **≤3 sn:** kamyonun arka kapısında "$124 TRILLION" yazan dev kutu; kutunun köşesinden banknot damlar. Sonra kutu ikiye ayrılır (18 bağış / 54 "SPOUSE FIRST" etiketi). | Somut özne (bir ailenin kutuları) + ters köşe + net vaat; logo/intro/"hi guys" YOK |
| 0:15–0:40 | Başlık vaadi: "often called the biggest inheritance in history" + izleyici bağı (mirasçı / ev alıcısı) + videonun sonunda ne öğrenileceği (mirasçı neden daha az ve daha geç alabilir, en büyük sızıntı hangisi) | Ülke haritası → tek ev; "HEIR? HOME BUYER? BOTH?" | Başlık + thumbnail ("WHO GETS IT?") vaadi ilk 30 sn'de karşılanır |
| 0:40–0:57 | Leo kendini nakliye şefi olarak tanıtır, **tez** | Leo kamyon kapısında, elinde pano; tez kamyonun yan yüzüne yazılır | Tez ilk 60 sn'de |

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
| One hundred twenty-four trillion dollars is expected to pass down in America by twenty forty-eight, Cerulli estimates. But eighteen trillion goes to charity. Fifty-four trillion stops at a spouse first. So let's count what reaches the kids in one family. | **Sahne:** 0:00 gece yolu, turuncu kamyonun arka kapısı açılır: içinde tek dev kutu "$124T · CERULLI EST. · THROUGH 2048". 0:02 kutunun alt köşesinden banknot damlar (H3 ≤3 sn görsel değişim). "charity"de küçük bir dilim kayar: "$18T → CHARITY". "spouse"da kamyon yan şeride sinyal verir, sarı tabela: "$54T → SPOUSE FIRST (a stop, not a loss)" (D2: ayrı çubuk/çıkarma yok). "one family"de dev kutu 10 küçük kutuya bölünür. **Leo:** kamyonun yanında panoyu kaldırır. **Ekran:** küçük not "Estimate: Cerulli Associates, Dec 2024". **Kaynak:** R01, R03, R04. **Kritik yol (H4):** damlama + kutu bölünmesi F5 testine girer. |

### S02 · 0:15–0:40 · 25 sn
| ANLATIM | GÖRSEL |
|---|---|
| People often call it the biggest inheritance in history. But that's one number for a whole country, stretched over decades. Maybe you'll inherit something one day. Maybe you're buying a home another family is leaving. Either way, this reaches you. So on this trip, we'll find out why heirs might get less than the headline sounds, and get it later. And which leak is the biggest. | **Sahne:** ABD haritası üstünde küçük kamyonlar → kamera tek sokağa, tek eve iner. "inherit"te kapıda kutu; "buying a home"da kapıdan çıkan kutular, içeri giren genç siluet (yüzsüz). **Ekran:** "OFTEN CALLED THE BIGGEST INHERITANCE IN HISTORY" (D3) → "HEIR? HOME BUYER? BOTH?" → "LESS? LATER?" + soru işaretli kutu "BIGGEST LEAK = ?" (sona kadar açık döngü; başlık + thumbnail "WHO GETS IT?" vaadi burada). **Kaynak:** [T] ("often called" yorum, R27c). **↺ 0:38 "And which leak is the biggest"**. |

### S03 · 0:40–0:57 · 17 sn
| ANLATIM | GÖRSEL |
|---|---|
| I'm Leo, a cartoon moving-crew boss. I load one generation's boxes and drive them to the next. Before I start the engine, here's what this road has taught me. An inheritance isn't a number. It's whatever is left at the end of a long road. | **Leo:** kamyon kapısında; nakliye yeleği, pano, omzunda bant rulosu; "cartoon"da göz kırpar. **Ekran:** tez kamyonun yan yüzüne boyayla yazılır: "AN INHERITANCE ISN'T A NUMBER. IT'S WHATEVER IS LEFT AT THE END OF A LONG ROAD." Tezde Leo ciddi, kameraya bakar; sonra kontak (motor SFX). **Kaynak:** — (tez). |

### S04 · 0:57–1:41 · 45 sn · İLK BÜYÜK ÖDÜL
| ANLATIM | GÖRSEL |
|---|---|
| First, let's read the label on that big number. It's not cash sitting in a vault. It's a forecast from a research firm called Cerulli Associates, made in late twenty twenty-four. Nearly one hundred trillion of it comes from baby boomers and older generations. About one hundred five trillion is expected to reach heirs. About eighteen trillion is expected to go to charity. And here's the twist. The fifty-four trillion that stops at a spouse isn't extra money, and it isn't lost. It's a stop on the way. The money goes to the surviving husband or wife first, and later moves on, to the kids or to charity. So it's not a leak. It's a detour. Remember that word. | **Sahne:** Leo dev kutunun etiketini büyüteçle okur: "FORECAST · CERULLI · DEC 2024". **Grafik G1 (tek çubuk):** "$124T" → "~$105T HEIRS" (lacivert) + "~$18T CHARITY" (yeşil), not "figures rounded". Küçük not: "~$100T from Baby Boomers and older (81%)". **Spouse ayrı gösterim (D2/R04):** çubuğa ne eklenir ne çıkarılır; çubuğun üstünden geçen yolda sarı durak tabelası "SPOUSE FIRST · ~$54T STOP HERE ON THE WAY" ve ok tekrar aynı çubuğa döner. **Leo:** "detour"da kamyonu yan şeride çevirir, panoya "DETOUR ≠ LEAK". **Kaynak:** R01, R02, R03, R04, R06. |

### S05 · 1:41–1:51 · 9 sn
| ANLATIM | GÖRSEL |
|---|---|
| But one number for a whole country hides what happens inside one home. To see the real leaks, we need one family, and one truck. | **Sahne:** kamera haritadan tek eve iner, kapıda 4 siluet. **Ekran:** "ONE FAMILY. ONE TRUCK." **↺ 1:46 "To see the real leaks, we need one family"**. Sahne sonu 1,5 sn nefes → **ABONE-1**. |

## Bölüm 2 — Loading the Okafors

### S06 · 1:51–2:27 · 37 sn
| ANLATIM | GÖRSEL |
|---|---|
| Meet the Okafors. They're an example family, made up for this trip. Two parents, two grown kids, and everything they own, packed into ten boxes. Four boxes for the house. Four for retirement savings. Two for money in the bank. Each box is one tenth of the family's wealth. There are no dollar signs, on purpose. This is an illustration, not an average. On the side of every box, I write the same address. To: the kids. Moving rule number one: label everything. Moving rule number two: check the bottom of every box. We'll see how that goes. | **Sahne:** kapı eşiğinde 4 düz siluet (yüzsüz) + köşe etiketi "EXAMPLE FAMILY · ILLUSTRATION" (P2, H4: rig'siz). Kutular kamyona yüklenir: 4 kiremit HOUSE, 4 lacivert RETIREMENT, 2 yeşil BANK. **Ekran:** "10 BOXES = ALL THEIR WEALTH · ILLUSTRATION, NOT AN AVERAGE". **Leo:** her kutuya keçeliyle "TO: THE KIDS". **Kaynak:** [ÖRNEK] (`veri/kutu-hesap.py`). |

### S07 · 2:27–2:42 · 15 sn
| ANLATIM | GÖRSEL |
|---|---|
| My clipboard has six stops between here and there. Some stops take boxes. One stop takes none, but it costs years. And the stop everyone fears the most turns out to be one most trucks drive right past. Let's roll. | **Sahne:** Leo panoyu gösterir: LIVING · CARE · SPOUSE · GIVING · HOUSE · TAX & TIME. 6 durak tabelası yol boyunca dizilir; kamyon yola çıkar (motor + korna SFX). **↺ 2:35 "And the stop everyone fears the most"** (Bölüm 6'ya kadar açık). |

## Bölüm 3 — Living and Care

### S08 · 2:42–3:23 · 41 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop one is good news. Living a long time. In America, a sixty-five-year-old can expect, on average, about twenty more years of life. That's a lot of groceries, heating bills, doctor visits, and trips to see the grandkids. And that's exactly what retirement savings are for. They were built to be spent. So I cross out two boxes. Label: spent on living. Is that a leak? Not really. That's the boxes doing their job. But it shows something the big number leaves out. A forecast counts money before it's lived on. A family counts it after. And honestly, a long life is the best kind of leak there is. | **Sahne:** durak tabelası "LIVING". İki lacivert kutu açılır, içinden market poşeti, ısıtma faturası, tren bileti (torun ziyareti) çıkar. **Grafik:** zaman şeridi "AGE 65 → ~20 MORE YEARS (US average)" (ondalık yok, R14). **Leo:** panoda LIVING "−2", kutulara "SPENT ON LIVING" damgası. **Ekran:** "A FORECAST COUNTS MONEY BEFORE IT'S LIVED ON." **Kaynak:** R14 · son iki cümle [T] · kutular [ÖRNEK]. |

### S09 · 3:23–3:30 · 7 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop two is the one families talk about the least. And it's the reason I carry this tape. | **Sahne:** sisli yoldan tabela belirir: "CARE". **Leo:** bant rulosunu sallar. **↺ 3:23 "Stop two is the one families talk about the least"**. |

### S10 · 3:30–4:08 · 38 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop two is care. As people get older, many need help with daily life. Getting dressed. Cooking. Taking medicine on time. U.S. government researchers estimate that more than half of Americans turning sixty-five will, at some point, need serious long-term care. About one in five will need it for more than five years. Sometimes that help comes from family, at home. Sometimes it means a nursing home. And that bill is big. In the U.S., a private room in a nursing home has a median cost of about one hundred thirty thousand dollars a year, says a twenty twenty-five survey by CareScout. | **Sahne:** ev içi siluet kareleri (yüzsüz): düğme ilikleyen el, ocak, ilaç kutusu. **Grafik G2:** 100 insan ikonundan 56'sı renklenir: "56% OF AMERICANS TURNING 65 — SERIOUS LONG-TERM CARE (HHS/ASPE est.)" · 22'si koyu: "MORE THAN 5 YEARS: 22%" (R16) · fatura kartı "NURSING HOME, PRIVATE ROOM: $129,575 / YEAR · US MEDIAN, CareScout 2025" (R13). **Kaynak:** R16, R13 · "sometimes family" [T, rakamsız]. |

### S11 · 4:08–4:50 · 42 sn
| ANLATIM | GÖRSEL |
|---|---|
| Why does this one leak so much? Because Medicare, the health insurance for older Americans, generally doesn't pay for long-term custodial care. That means help with daily life, not hospital treatment. And if Medicaid, the program for people with low income, ends up paying, states are required to try to recover those costs from the estate later. The same government researchers estimate that about one in seven people turning sixty-five could pay one hundred thousand dollars or more out of their own pocket for this kind of care. For the Okafors, I cross out one box. Label: care. In a different family, it could be zero boxes. Or it could be four. | **Sahne:** iki kapı: "MEDICARE" önünde levha "LONG-TERM CUSTODIAL CARE: GENERALLY NOT COVERED"; "MEDICAID" kapısından çıkan bir el, kamyondaki yeşil kutuya "ESTATE RECOVERY" etiketi yapıştırır (mekanizma; eylem önerisi yok, P1/R25). **Grafik:** 7 ikondan 1'i kırmızı "~1 IN 7: $100K+ OUT OF POCKET (est., 2020 dollars)" (R17). **Leo:** CARE "−1"; iki hayalet kamyon: 0 kutu ve 4 kutu kaybı ("IT VARIES A LOT"). **Kaynak:** R25, R17 · kutular [ÖRNEK]. **↺ 4:08 "Why does this one leak so much?"** |

### S12 · 4:50–5:09 · 18 sn
| ANLATIM | GÖRSEL |
|---|---|
| And this is where my job gets messy. The care box has a soft bottom. I tape it. Then a different corner starts to drip. So I tape that one too. Okay. That's a two-tape stop. Two stops down, three boxes gone. And notice something. Nobody did anything wrong. | **Karakter anı (H4, kritik yol):** Leo kutunun dibini bantlar (bant SFX), para başka köşeden damlar, ikinci bant, kameraya döner. **Ekran:** "TAPE USED: 2" · pano "−3". **Kaynak:** [ÖRNEK]. |

## Bölüm 4 — The Detour and the Gift

### S13 · 5:09–5:48 · 39 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop three looks like the biggest leak on the whole list. It isn't a leak at all. When the first parent passes away, the truck doesn't go to the kids. It turns around and parks across the street, at the surviving husband or wife. Cerulli puts this stop at about fifty-four trillion dollars. Nearly forty trillion of that is expected to go to widowed women from the boomer and older generations. For the kids, nothing changes on paper. Their names are still on the boxes. But now the boxes live with one parent, and they have to last for the rest of that parent's life. | **Sahne:** kavşakta sinyal SFX, tabela "SPOUSE FIRST". Eşikteki iki büyük siluetten biri yumuşakça solar, sıcak ışık kalır (P2: ölüm soyut). Kamyon karşı kaldırıma yanaşır. **Grafik:** sarı durak tabelası "~$54T STOPS HERE FIRST · ~$40T OF IT TO WIDOWED WOMEN" (124 çubuğuyla aritmetik yok, R04/R05). **Kaynak:** R04, R05. **↺ 5:09 "Stop three looks like the biggest leak on the whole list"**. |

### S14 · 5:48–6:32 · 44 sn · DORUK-1 (sızıntı 3 ters köşesi)
| ANLATIM | GÖRSEL |
|---|---|
| Now look at my clipboard. How many boxes did we lose at stop three? Zero. Nothing leaked. The kids just wait. But here's the part the headline hides. While the boxes sit in that one home, the first two stops keep working. More years of living. Maybe another round of care. To be fair, boxes can also grow while they wait, if the money is invested. But a box that is being spent can't grow much. The detour doesn't take any boxes. It gives the other leaks more time. Think of it like a relay race. The baton goes to the partner first. The kids are the last runners, waiting at the far end of the track. | **Sahne:** pano SPOUSE "−0" + kum saati "+YEARS". Kamyon park hâlinde, takvim yaprakları uçar; LIVING ve CARE tabelaları kamyonun önünden **ikinci kez** geçer. "grow"da bir kutu hafifçe büyür, sonra açılıp harcanırken küçülür (adil karşılaştırma). **Grafik:** bayrak yarışı pisti: koşucu 1 → koşucu 2 (eş) → pistin ucunda bekleyen iki genç siluet. **Leo:** bayrağı kaldırır. **Kaynak:** [T] (mekanizma; D2: durak/gecikme). ABONE bu sahnenin üstüne gelmez (H5). **↺ 5:56 "But here's the part the headline hides"**. |

### S15 · 6:32–6:39 · 7 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop four is the only part of the headline that truly skips the kids. And it happens on purpose. | **Sahne:** tabela "GIVING", üstünde küçük kalp. **↺ 6:32 "Stop four is the only part of the headline that truly skips the kids"**. |

### S16 · 6:39–7:11 · 32 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop four is giving. Cerulli expects about eighteen trillion dollars to go to charity. Schools. Hospitals. Churches, mosques and temples. Research. The causes people cared about all their lives. This one is easy to talk about, because it's a choice, not an accident. In our example, the Okafors give one box to the school where they met. I cross it out with a smile. Label: given. It's still a box that won't ride in the kids' truck. But nobody at the school calls it a leak. | **Sahne:** kamyon isimsiz bir okulun önünde; yeşil kutu kapıya bırakılır, pencerelerde el sallayan siluetler. Okul/hastane/ibadethane ikonları eşit boyutta (P2). **Grafik:** S04 çubuğundaki "~$18T CHARITY" parlar: "THE ONE PART THAT SKIPS HEIRS" (R03). **Leo:** GIVING "−1", gülümser. **Kaynak:** R03 · kutular [ÖRNEK]. |

### S17 · 7:11–7:30 · 19 sn
| ANLATIM | GÖRSEL |
|---|---|
| And this stop may change shape. In a Bank of America survey of wealthy Americans, people with millions to invest, forty-seven percent said the next generation is ready to take on the family's giving. In twenty twenty-four, it was fifty-five percent. Fewer parents are sure who will carry that box next. | **Grafik G3 (iki çubuk):** "55% (2024) → 47% (2026)" · altında zorunlu nitelik: "BofA Private Bank survey · 1,431 people with $3M+ investable assets" (R09, koordinatör (5)). **Leo:** kutuyu iki genç siluetten hangisine vereceğini bilemeden tutar. **Kaynak:** R09 · son cümle [T]. Sahne sonu 1,5 sn nefes → **ABONE-2**. |

## Bölüm 5 — The Heaviest Box

### S18 · 7:30–7:42 · 11 sn
| ANLATIM | GÖRSEL |
|---|---|
| Let's check the clipboard. Living, minus two. Care, minus one. The detour, zero, but more time. Giving, minus one. Six boxes still on board, and the heaviest one is next. | **Sahne:** kamyonun içi, kalan 6 kutu; 4 kiremit kutu en dipte. **Leo:** panoyu okur, her satırda tik SFX. **↺ 7:39 "and the heaviest one is next"**. **Kaynak:** [ÖRNEK]. |

### S19 · 7:42–8:26 · 45 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop five is the house. For the Okafors, it's four boxes out of ten. And across the country, it's a big box too. Fed data shows baby boomers own about two-fifths of all the real estate held by American households. But a house has a problem the other boxes don't have. You can't cut it in half. Two kids, one house. One wants to keep it. The other needs the cash. If neither can buy the other out, the house goes up for sale. And selling has its own costs. Agent fees. Repairs that were put off for years. Property taxes and bills while it sits empty. Sometimes the house was sold years earlier, to pay for stop two. | **Sahne:** 4 kiremit kutu birbirine yapışık, tek parça ev maketi. **Grafik:** tek çubuk "BOOMERS: ~41% OF US HOUSEHOLD REAL ESTATE (Fed DFA, Q2 2026)" (R23). İki genç siluet maketi iki yandan çeker, maket bölünmez (gag). Tek "SOLD" kartı (H7: satılık tabelalar sokağı YOK). Fatura kartları uçar: "AGENT FEES · REPAIRS · PROPERTY TAX & BILLS" (rakamsız, R27f). Son cümlede sepya geri dönüş: ev CARE durağında satılırken. **Kaynak:** R23 · satış/bölüşme mekanizması [T, rakamsız] · kutular [ÖRNEK]. H7: ev bölümü S19+S20 ≤90 sn. |

### S20 · 8:26–8:40 · 14 sn
| ANLATIM | GÖRSEL |
|---|---|
| None of this takes a whole box. It takes a slice. And every house sold on this road is a house someone else gets to buy. Maybe you. Oh, and there's my third drippy corner. More tape. | **Sahne:** kiremit kutudan ince dilim kesilir "−A SLICE"; kapıdan genç bir siluet anahtarla girer (S02'deki ev alıcısı vaadi kapanır). **Leo:** üçüncü köşeyi bantlar, rulo incelmiş. **Ekran:** "TAPE USED: 3". **Kaynak:** [ÖRNEK]. |

## Bölüm 6 — The Leak Everyone Fears

### S21 · 8:40–9:30 · 50 sn
| ANLATIM | GÖRSEL |
|---|---|
| Stop six is the one everybody fears. Taxes. So let's read the sign on this stop. As of twenty twenty-six, the U.S. federal estate tax only starts above fifteen million dollars per person. Now compare that with a typical family. For families headed by someone sixty-five to seventy-four, the median net worth was about four hundred ten thousand dollars in twenty twenty-two, the Fed found. The tax line is dozens of times higher than that. So for most families, the federal estate tax never comes into play. The Okafors drive right past this stop. Some states have their own estate or inheritance taxes, with their own rules. And other countries draw the line in different places. In the U.K., as of twenty twenty-six, inheritance tax generally starts above three hundred twenty-five thousand pounds. | **Sahne:** ürkütücü gişe "TAX" (gölgeli, gök gürültüsü SFX) → Leo tabelayı okur, gürültü kesilir. **Grafik G4:** dikey çizgi "US FEDERAL ESTATE TAX STARTS: $15M PER PERSON (2026)" (R18) · çok aşağıda küçük çubuk "MEDIAN NET WORTH, AGES 65–74: ~$410K (Fed SCF, 2022 dollars)" (R19; "dozens of times" = 37x [H], sesli rakam yok). Not: "Some states have their own taxes." (R20, rakamsız). Küçük UK kartı "UK: £325,000 threshold (2026)" (R26). Bariyer kalkar, kamyon geçer. **Kaynak:** R18, R19, R20, R26. P1: yasa değişikliği, parti, politikacı yok. **↺ 8:40 "Stop six is the one everybody fears"**. |

### S22 · 9:30–9:54 · 24 sn
| ANLATIM | GÖRSEL |
|---|---|
| That's the surprise of this whole road. The leak people fear the most is one most trucks never hit. For most families, the leaks that matter are the quiet ones. Living. Care. And time. Quick question before the last stop. Which leak did you think was the biggest before this trip? Tell me in the comments. I'm curious how many people picked taxes. | **Sahne:** Leo panoda TAX "−0 (for this family)", LIVING ve CARE satırlarının altını çizer. **Ekran:** "THE LOUD LEAK IS SMALL. THE QUIET LEAKS ARE BIG." (S07 döngüsü kapanır). **Kaynak:** [T] (R18/R19 çıkarımı). |

### S23 · 9:54–10:00 · 6 sn
| ANLATIM | GÖRSEL |
|---|---|
| Which brings us to the last sign on stop six. It isn't a cost. It's a clock. | **Sahne:** gişenin arkasında dev bir yol saati. **↺ 9:54 "Which brings us to the last sign on stop six"**. |

### S24 · 10:00–10:57 · 57 sn
| ANLATIM | GÖRSEL |
|---|---|
| Put the long life and the detour together, and the boxes arrive late. The kids on the label might have grey hair of their own by then. You can see it in Cerulli's numbers. In the first ten years, Gen X is expected to inherit the most, about fourteen trillion dollars. But over the whole stretch to twenty forty-eight, millennials end up with the biggest share, about forty-six trillion. A lot of this money reaches people in the middle of their lives, not at the start. And waiting has a quiet cost of its own. Even at the Fed's two percent inflation target, a dollar loses about a third of its buying power over twenty years. Money that arrives when you're starting out might help with a first home, or a first business. Money that arrives later often goes somewhere else. Your own retirement. Your own kids. Same boxes. Different job. | **Sahne:** "TO: THE KIDS" etiketindeki iki genç siluetin saçı zaman atlamasıyla griye döner. **Grafik G5:** "FIRST 10 YEARS: GEN X ~$14T (MOST)" → "THROUGH 2048: MILLENNIALS ~$46T (MOST)" (R08). Sonra 1 $ banknotu yavaşça solar: "2% A YEAR × 20 YEARS → $1 BUYS ~$0.67" (R21, [H]). **Ekran:** iki yol işareti "STARTING OUT → FIRST HOME / BUSINESS" ve "LATER → OWN RETIREMENT / OWN KIDS". **Kaynak:** R08, R21 · "middle of their lives" ve son 6 cümle [T]. **↺ 10:55 "Same boxes. Different job."** |

### S25 · 10:57–11:01 · 4 sn
| ANLATIM | GÖRSEL |
|---|---|
| So, how many boxes are left when the doors finally open? | **Sahne:** son viraj; ufukta "TO: THE KIDS" yazan ev. **↺ 10:57 "how many boxes are left when the doors finally open"**. |

## Bölüm 7 — Arrival

### S26 · 11:01–11:30 · 30 sn · DORUK (varış envanteri)
| ANLATIM | GÖRSEL |
|---|---|
| The truck stops. I open the doors, and I read my clipboard out loud. Loaded: ten boxes. Stop one, living: minus two. Stop two, care: minus one. Stop three, the detour: minus zero, plus a few years. Stop four, giving: minus one. Stop five, the house: minus a slice. Stop six, taxes: minus zero, for this family. Delivered: six boxes, minus a slice, years later than planned. Split between two kids, that's about three boxes each, a little less. | **Sahne (K1 varış):** kapılar açılır, Leo panoyu yüksek sesle okur; her satırın üstü çizilir. **Grafik G6 (Okafor şelalesi, tek şelale, "EXAMPLE FAMILY · ILLUSTRATION"):** 10 → −2 LIVING → −1 CARE → 0 SPOUSE (+YEARS, sarı saat) → −1 GIVING → −slice HOUSE → 0 TAX → **6 − slice, LATER** → 2'ye bölünür "≈3 EACH". D2: şelale 124'ten değil, ailenin 10 kutusundan başlar. **Kaynak:** [ÖRNEK] (`veri/kutu-hesap.py` assert). |

### S27 · 11:30–12:04 · 34 sn
| ANLATIM | GÖRSEL |
|---|---|
| Is that a sad story? Look at the list again. A long life. Care when it was needed. A gift they chose. That's not a family that lost its money. It's a family that used it. And remember, this is one example. A family with smaller savings might arrive with no boxes at all. A very wealthy family might pay a real bill at stop six, and still arrive with a full truck. The point of the list isn't to judge anyone. It's to see where the boxes actually went. | **Sahne:** iki genç siluet kutuları içeri taşır, birinin elinde yüzsüz aile fotoğrafı çerçevesi. Ardından üç hayalet kamyon yan yana: boş kasa · Okafor (6) · uzun konvoy (TAX gişesinde durur, sonra geçer). **Kaynak:** [T] (rakamsız karşılaştırma). **↺ 11:30 "Is that a sad story?"** |

### S28 · 12:04–12:45 · 40 sn
| ANLATIM | GÖRSEL |
|---|---|
| Now zoom out, back to that giant number. Cerulli expects about half of it, around sixty-two trillion dollars, to come from just two percent of households. The wealthiest ones. And Fed data tells a similar story about the wealth households hold. The top ten percent hold about two-thirds of it. The bottom half holds about two percent. So the headline is real. It's just lumpy. For a few families, the truck is a whole convoy. For most, it's a few boxes, and they come late. That's why two people can read the same headline and both be right. One sees a convoy. The other sees a few boxes. | **Sahne:** kamera Okafor evinden yükselir, haritaya döner. **Grafik G7 ("bölünmüş tablo" kartı, K1):** 100 hanelik ızgarada 2 hane turuncu → "$124T: ~HALF (~$62T) FROM 2% OF HOUSEHOLDS" (R07; "more than half" yok, R27d). Ayrı panel (aynı ekranda toplanmaz, DFA ≠ Cerulli): "US HOUSEHOLD WEALTH, Q2 2026: TOP 10% ≈ 69% · BOTTOM 50% ≈ 2%" (R24). Başlık: "THE HEADLINE IS REAL. IT'S JUST LUMPY." Haritada birkaç konvoy, çok sayıda küçük kamyon. **Kaynak:** R07, R24. |

### S29 · 12:45–13:02 · 17 sn
| ANLATIM | GÖRSEL |
|---|---|
| Could this road change? It could. If care keeps getting more expensive, stop two may grow. If tax laws change, stop six may move. This isn't a forecast for any family, and it isn't a plan. It's a map of where the boxes tend to go. | **Sahne:** yol haritası; CARE tabelası kesik çizgiyle hafifçe büyür; TAX tabelası kesik çizgiyle kayıp geri gelir. Dallanan yol YOK (K1: tek yol). **Ekran:** "NOT A FORECAST. NOT A PLAN. A MAP." **Kaynak:** [T] (koşullu; parti/politikacı yok, P1). **↺ 12:45 "Could this road change?"** |

### S30 · 13:02–13:17 · 15 sn · TEZ
| ANLATIM | GÖRSEL |
|---|---|
| So the next time someone says one hundred twenty-four trillion dollars, picture the truck. An inheritance isn't a number. It's whatever is left at the end of a long road. And on this road, I'm going to need more tape. | **Sahne:** kamyonun yan yüzündeki tez yazısı yakın plan. **Karakter anı (H4):** Leo boş kutuyu bırakır, incecik kalmış bant rulosunu omzuna atar, kameraya: "I'm going to need more tape." Kısa müzik vurgusu. **Kaynak:** R01. Sahne sonu 1,5 sn nefes → **ABONE-3**. |

### S31 · 13:17–13:28 · 11 sn · KÖPRÜ
| ANLATIM | GÖRSEL |
|---|---|
| There's one box we only opened for a minute. The house. What happens to a whole neighborhood when many houses change hands at once is a story for another road. | **Sahne:** kiremit kutu kamyonda tek başına parlar; kamera yola döner, ufukta ışıkları yanan mahalle silueti (satılık tabelası YOK, H7). **Uç ekran:** genel merak köprüsü (yayında olmayan videoya söz yok). |

---

## 3. Retention haritası

Zamanlar §12 betik ölçümünden (160 kpm). A = açılan, K = kapanan merak döngüsü.

| Zaman | Açılan / kapanan merak döngüsü | Yeniden kanca (↺) | Görsel değişim notu |
|---|---|---|---|
| 0:00 | **A1** kızlara/çocuklara ne varır? (ters köşe: 18 bağış, 54 önce eş) | hook | ≤3 sn: dev kutu → damlama → yan şerit → 10 kutu |
| 0:38 | **A2** en büyük sızıntı hangisi? (sona kadar açık); başlık/thumbnail vaadi ("biggest inheritance", "less, later") | ↺1 | harita → tek ev, "LESS? LATER?" |
| 0:51 | A3 tez test edilecek | — | tez kamyon yüzünde |
| 0:57–1:41 | **İlk büyük ödül:** 124'ün etiketi (105/18, boomer ~100); 54 = durak, kayıp değil | — | G1 tek çubuk + sarı durak tabelası |
| 1:46 | A4 tek ailede sızıntılar | ↺2 | "ONE FAMILY. ONE TRUCK." |
| 1:51 | **ABONE-1** (ödülden sonra nefes) | — | profil + Subscribe + tık |
| 2:35 | **A5** korkulan durak (Bölüm 6'ya kadar) | ↺3 | 6 durak tabelası |
| 2:42–3:23 | Sızıntı 1: ~20 yıl, −2 kutu | — | kutudan market poşeti |
| 3:23 | A6 bakım + bant | ↺4 | sisli CARE tabelası |
| 3:30–4:50 | Sızıntı 2: %56 / %22 / ~130 bin $; Medicare/Medicaid geri tahsil; 1/7 | ↺5 "Why does this one leak so much?" (4:08) | G2 ikon ızgarası, iki kapı |
| 4:50 | Karakter anı: iki bant | — | bant gag'i (kritik yol) |
| 5:09 | A7 "en büyük görünen" durak | ↺6 | kavşak, sinyal |
| 5:48–6:32 | **DORUK-1:** 0 kutu kaybı, ama süre → diğer sızıntılar yeniden çalışır | ↺7 "the part the headline hides" (5:56) | kum saati, bayrak yarışı |
| 6:32 | A8 bilerek atlanan pay | ↺8 | GIVING kalbi |
| 6:39–7:30 | Sızıntı 4: 18 T$, −1; BofA %55 → %47 | — | okul kapısı, G3 |
| 7:30 | **ABONE-2** (bağış + anket ödülünden sonra nefes, ara özet başında) | — | profil + Subscribe + tık |
| 7:39 | A9 en ağır kutu | ↺9 | pano ara özeti |
| 7:42–8:40 | Sızıntı 5: ~%41 gayrimenkul, bölünmeyen ev, dilim; S02 ev alıcısı vaadi kapanır | — | maket çekişmesi, SOLD kartı |
| 8:40 | A5 doruğa | ↺10 | gişe, gök gürültüsü |
| 8:40–9:54 | **A5 kapanır:** 15 M$ eşik vs ~410 bin $ medyan; UK; "loud leak small"; yorum sorusu | — | G4 dikey çizgi, bariyer kalkar |
| 9:54 | A10 saat | ↺11 | dev yol saati |
| 10:00–10:57 | Zaman: Gen X ilk 10 yıl, Millennial 46; %2 → 0,67 | ↺12 "Same boxes. Different job." | gri saç gag'i, solan banknot |
| 10:57 | A11 kaç kutu kaldı? | ↺13 | son viraj |
| 11:01–11:30 | **DORUK (varış):** 6 − dilim, geç, ≈3'er; **A1 kapanır** | — | G6 Okafor şelalesi |
| 11:30 | A12 bu kötü mü? | ↺14 | üç hayalet kamyon |
| 12:04–12:45 | **A2 kapanır:** bölünmüş tablo (~yarısı %2'den; DFA %69/%2) | — | G7 ızgara kartı |
| 12:45 | A13 yol değişir mi? (koşullu, dallanmasız) | ↺15 | kesik çizgili tabelalar |
| 13:02 | A3 kapanır: tez + "more tape" | — | tez yakın plan, rulo omza |
| 13:17 | **ABONE-3** (tezden sonra, köprüden önce nefes) | — | profil + Subscribe + tık |
| 13:17 | **A14 (uç ekran):** mahalle | köprü | ışıklı mahalle silueti |

**En uzun ↺ aralığı 74 sn** (betik §12; hedef ≤75).

**ABONE satırları (animasyon-yonetmeni zamanı, kurgu-editoru yerleştirir; çapa = animasyonun başladığı nefesten hemen sonraki cümle). Zamanlar §12'den:**

| # | Zaman (betik) | Çapa cümlesi | Neden bu an |
|---|---|---|---|
| ABONE-1 | 1:51 (S05 sonu / S06 başı) | "Meet the Okafors." | İlk büyük ödül (124'ün etiketi, 54 = durak) + ↺2'den sonra nefes; ≥60 sn |
| ABONE-2 | 7:30 (S17 sonu / S18 başı) | "Let's check the clipboard." | Bağış + anket ödülünden sonra; DORUK-1'in (sızıntı 3 ters köşesi) üstünde değil (H5) |
| ABONE-3 | 13:17 (S30 sonu / S31 başı) | "There's one box we only opened for a minute." | Tez + "more tape" anından sonra, köprü cümlesinden önce; varış/şelale üstünde değil (H5) |

Sesli abone/beğeni çağrısı yok. Tek sesli etkileşim: S22 yorum sorusu ("Which leak did you think was the biggest…?"), ABONE ile çakışmaz.
**Not:** TTS duraklamaları gerçek süreyi uzatabilir; F7'de `kurgu-editoru` gerçek ses zamanlarıyla yeniden ölçer.

---

## 4. YouTube bölümleri (chapters)

Betik zamanları (§12). Montaj sonrası `kurgu-editoru` gerçek ses zamanlarıyla günceller.

```
0:00 The number on the truck
1:51 Loading the Okafors
2:42 Living and care
5:09 The detour and the gift
7:30 The heaviest box
8:40 The leak everyone fears
11:01 Arrival
```

---

## 5. Shorts kancaları ve kesit önerileri (2 adet, her biri ≤60 sn, 9:16)

### Shorts 1 — "The detour"
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "One hundred twenty-four trillion dollars is expected to pass down in America by twenty forty-eight."
- **Kesit:** S01 (rakam) → S13 (eş durağı, kısaltılmış) → S14 ilk 4 cümle → kapanış sorusu. Cevap (sapma sırasında LIVING/CARE yeniden çalışır, varışta kaç kutu kalır) yalnız uzun videoda.
- **9:16 notu:** kamyon dikey kadrajda yan şeride döner; sarı tabela "$54T STOPS AT A SPOUSE FIRST" (124 ile aritmetik yok, R04). **Kaynak:** R01, R04, R05. Politika: tek ölçülmüş olgu, ölüm soyut.
- **Okunacak tam metin (betik bunu sayar):** <<One hundred twenty-four trillion dollars is expected to pass down in America by twenty forty-eight. That's an estimate from Cerulli Associates. But here's the twist. About fifty-four trillion of it doesn't go to the kids first. It stops at a surviving husband or wife. Nearly forty trillion of that goes to widowed women. So is that a leak? No. It isn't lost. The truck just takes a detour, and the kids wait. But the wait isn't free. Something keeps happening to the boxes while they sit in that one home. So how many boxes are left when the truck finally reaches the kids?>>

### Shorts 2 — "The leak people fear"
- **Kendi hook'u (yeni kayıt, 0–3 sn):** "Here's the leak people fear most when money is passed down. Taxes."
- **Kesit:** S21 (vergi eşiği + medyan servet) → S22 ilk iki cümle → kapanış sorusu. Cevap (sessiz sızıntılar: yaşam, bakım, zaman) yalnız uzun videoda.
- **9:16 notu:** gişe bariyeri dikeyde; "US federal, 2026" ve "Fed SCF, 2022 dollars" satırları altta sabit. **Kaynak:** R18, R19. Tavsiye yok; cevap (sessiz sızıntılar) yalnız uzun videoda.
- **Okunacak tam metin (betik bunu sayar):** <<Here's the leak people fear most when money is passed down. Taxes. So let's read the sign. As of twenty twenty-six, the U.S. federal estate tax only starts above fifteen million dollars per person. Now look at a typical family. For families headed by someone sixty-five to seventy-four, the median net worth was about four hundred ten thousand dollars in twenty twenty-two, the Fed found. The tax line is dozens of times higher. So for most families, the scary stop is just a sign by the road. Then where does the money really go on the way to the kids?>>

---

## 6. Uç ekran köprüsü (2 sürüm, seçilen: A)
- **A (seçilen, S29):** "There's one box we only opened for a minute. The house… a story for another road." → Genel merak köprüsü; S04 (mahalle postacısı) seri devamına doğal geçiş, yayında olmayan videoya söz vermez.
- **B (elenen):** "Next time, we follow the house box down a street full of for-sale signs." → S04 yayında değil (yanıltıcı söz) + H7 görsel örtüşmesi.

---

## 7. Rakam ve olgu tablosu (metindeki her rakam/olgu → `rakam-tablosu.md` satırı)

| Satır | Metindeki kullanım (güvenli yazım) | Sahne |
|---|---|---|
| R01 | 124 T$ "is expected to pass down in America by twenty forty-eight, Cerulli estimates" | S01, S30, Shorts 1 |
| R02 / R03 | ≈105 heirs / ≈18 charity ("the one part that skips heirs") | S01, S04, S16 |
| R04 / R05 | 54 "stops at a spouse first… a stop on the way" / ≈40 widowed women | S01, S04, S13, Shorts 1 |
| R06 | "nearly one hundred trillion… boomers and older" | S04 |
| R07 | "about half… around sixty-two trillion… two percent of households" | S28 |
| R08 | Gen X ≈14 (ilk 10 yıl, en çok) · Millennials ≈46 (2048'e kadar, en çok) | S24 |
| R09 | %47 ← %55 (2024); ekranda 1.431 kişi, ≥3 M$ | S17 |
| R13 | özel oda medyan ≈130 bin $/yıl (US, CareScout 2025) | S10 |
| R14 | "about twenty more years" (65 yaşında) | S08 |
| R16 | "more than half" (%56) ciddi LTC · "about one in five" (%22) >5 yıl | S10 |
| R17 | "about one in seven… one hundred thousand dollars or more out of pocket" (2020 $ ekranda) | S11 |
| R18 | 15 M$ kişi başı, "As of twenty twenty-six, the U.S. federal…" | S21, Shorts 2 |
| R19 | 65–74 medyan ≈410 bin $ (2022), "dozens of times" | S21, Shorts 2 |
| R20 | eyalet vergileri rakamsız | S21 |
| R21 | Fed %2 hedefi → 20 yılda ≈1/3 alım gücü | S24 |
| R23 | boomer ≈2/5 hane gayrimenkulü (Fed DFA) | S19 |
| R24 | üst %10 ≈2/3, alt %50 ≈%2 (Fed DFA, ayrı panel) | S28 |
| R25 | Medicare custodial karşılamaz; Medicaid mirastan geri tahsil | S11 |
| R26 | UK 325.000 £ (2026) | S21 |
| [ÖRNEK] | Okafor 10 kutu: −2, −1, 0, −1, −dilim, 0 → 6 − dilim, ≈3'er | S06–S26 (`veri/kutu-hesap.py`) |
| [T] | tez, mekanizma çıkarımları, ev satış maliyet kalemleri (rakamsız) | etiketli sahneler |
Kullanılmayan: R10, R11, R12, R15, R22 (bilinçli; R12 reklam algısı, R22 DFA/Cerulli kıyas yasağına yakın).

---

## 8. Telaffuz notları (ses-yonetmeni; Kokoro am_fenrir 0.9)
- Kontrol edilecek: **Cerulli** (che-ROO-lee; Kokoro yanlış okursa metinde "Cerulli Associates" yerine "the research firm Cerulli" kalır, gerekirse fonetik "Che-roo-lee" yalnız TTS girdisinde), **Okafor** (oh-KAH-for), **Genworth**, **CareScout**, **Medicaid / Medicare**, **millennials**, **inheritance**. Yasak liste (charts, complicated, scenarios, truth, crash*, bold) betikle 0.
- "U.S." noktalı. Sayılar yazıyla; "twenty forty-eight" ve "twenty twenty-four" Amerikan okunuşu.

---

## 9. Zor bölümlerin 2 versiyonu ve eleme

| Bölüm | Versiyon A (seçilen) | Versiyon B / C (elenen) | Ölçüm / gerekçe |
|---|---|---|---|
| Hook (H1) | **H1d** (39 kelime): rakam + ters köşe (18 bağış, 54 önce eş) + "So let's count what reaches the kids in one family." | **H1b** (38): aynı ters köşe, "So what really reaches the kids?" — somut özne yok (aile yok), vaat soru biçiminde. **H1c** (34): "…it's a forecast… and it leaks. Let's follow one family's share" — ters köşe yok (hakem: hook 7'nin nedeni). | Test "ilk 15 sn net vaat + somut özne": H1d 5/5 anahtar (trillion, charity, spouse, family, kids) ilk 40 kelimede; H1b 4/5 (family yok); H1c 3/5. R01 yazımı ("is expected to pass down… by") üçünde de uygulandı. H1d seçildi (H1b'nin ters köşesini korur + vaat ekler). |
| Açılış S02–S04 | Vaat (S02) → Leo + tez (S03, 0:51–0:57) → etiket ödülü (S04) | Önce etiket ödülü, sonra Leo + tez | B'de tez 1:40'a kayıyor (H2 ≤60 sn kalır), başlık vaadi 30 sn'yi geçiyor. A seçildi. |
| Orta nokta S13–S14 | Eş = 0 kutu, ama süre → LIVING/CARE tekrar çalışır + "boxes can also grow… if invested" adil cümlesi + bayrak yarışı | Eş durağını "en büyük sızıntı" gibi kurup sonra düzeltmek ("Fifty-four trillion gone? Not quite.") | B ilk dinleyişte çift sayım izlenimi bırakıyor (D2 riski, Shorts kesitinde bağlamsız kalır). A tek ölçülmüş olguya (R04) dayanır, ters köşe = kayıp değil gecikme. A seçildi. |
| Kapanış S26–S31 | Varış envanteri → "used, not lost" → bölünmüş tablo → koşullu tek yol → tez + "more tape" → ABONE-3 → köprü | Tez → bölünmüş tablo → köprü (gag yok) | B'de tez son 90 sn dışına düşüyor ve karakter anı kayboluyor; A'da tez 13:07 (son 21 sn), K1 grep 0. A seçildi. |

---

## 10. D / P / K / H düzeltmeleri — nerede uygulandı

| Kod | Uygulama | Yer |
|---|---|---|
| D1 | "Cerulli estimates… by twenty forty-eight"; "Bank of America says" yok (betik yasak kalıbı 0); BofA yalnız R09 anketinde | S01, S04, Shorts 1 |
| D2 (+ tablo inceltmesi, koordinatör (1)) | 54 = "a stop on the way", "isn't extra money, and it isn't lost"; "inside the total" YOK; çıkarma/ekleme yok; şelale ailenin 10 kutusundan; `veri/kutu-hesap.py` assert + yasak kalıp taraması 0 | S01, S04, S13, S14, S26, Shorts 1 |
| D3 | "People often call it the biggest inheritance in history" | S02 |
| D4 | %47 ← %55 R09 ile; ekranda "1,431 people with $3M+ investable assets" (koordinatör (5)); sesli "people with millions to invest" | S17 |
| D5 | Vergi "As of twenty twenty-six, the U.S. federal…"; eyalet rakamsız; UK tek cümle R26; Kanada/Avustralya yok; probate/estate sayısı yok | S21 |
| D6 | Dunham/"mirage" kullanılmadı (R12 kısmen + reklam algısı) | — |
| R14/R16/R27e | "about twenty more years"; %70 yerine ASPE "more than half" (%56) | S08, S10 |
| R07/R27d | "about half … two percent of households" | S28 |
| R21 | "future dollars" yok; enflasyon yalnız Fed %2 hedefi + 20 yıl hesabı | S24 |
| P1 | "you should / set up a trust / gift it now / estate plan" 0 (betik); Medicaid yalnız mekanizma; parti/politikacı 0 | S11, S21, S29 |
| P2 | Okafor rig'siz siluet + "EXAMPLE FAMILY · ILLUSTRATION"; ölüm soyut (solan siluet); kuşak suçlaması yok | S06, S13, S26 |
| P3 | Açıklama yasal notu R11 §11 metniyle → youtube-paketleyici / monetizasyon-uyum-uzmani | §11 |
| K1 | Üç olasılık yok: varış envanteri + tek şelale + bölünmüş tablo kartı; gelecek yalnız 2 koşullu cümle, dallanma yok; betik K1 grep 0 | S26–S29 |
| H2 | Tez 0:51–0:57 ve 13:07–13:13 | S03, S30 |
| H3 | Tanıtım yok, vaat ≤15 sn, ilk görsel değişim ≤3 sn, ↺ en uzun 74 sn | §1, §3 |
| H4 | Tek karakter Leo; bant gag'i 3 kez (S12, S20, S30); damlama F5 kritik yol | S01, S12, S20, S30 |
| H5 | ABONE 1:51 / 7:30 / 13:17; ilk 60 sn'de yok; DORUK-1 ve varış üstünde değil | §3 |
| H6 | Yayın gününe bağlı sözcük 0 (betik) | tümü |
| H7 | Ev bölümü S19+S20 = 59 sn (≤90); satılık tabelalar sokağı yok | S19–S20 |
| H8 | Başlık/thumbnail "WHO GETS IT?" paketleyicide; thumbnail'da "Bank of America" yok | §11 |

---

## 11. Leo rol kaydı ve sonraki ajanlara notlar
- **Rol:** nakliye ekibi şefi (pano + bant rulosu). 1929 (oyun sunucusu) ve S08 (ev arkadaşı) açılış/kapanış kalıpları tekrar edilmedi (5-gram §12). Kendini uzman sunmaz; "isn't a forecast… isn't a plan" (S29).
- **finans-dogrulayici:** açık [R?] yok; 50 sayı tabloyla eşleşti (§12). Olgu cümleleri GÖRSEL "Kaynak:" satırında R-kodlu. Tablo dışı nitel olgular [T] etiketli (ev satış maliyeti kalemleri, "sometimes family").
- **monetizasyon-uyum-uzmani:** S11 Medicaid geri tahsil cümlesi mekanizma (R25 güvenli yazım aynen); S22 yorum sorusu ("I'm curious how many people picked taxes") persona riski düşük ama kontrol edin.
- **youtube-paketleyici:** açıklama yasal notu = rakam-tablosu §11 metni (Okafor kurgusal, AI ses satırı); sabit yorum adayı S22 sorusu.
- **ses-yonetmeni:** §8 telaffuz listesi (Cerulli, Okafor, CareScout, Medicaid, millennials).

---

## 12. Test kapısı sonuçları
