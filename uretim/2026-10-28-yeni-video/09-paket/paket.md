# F8a — Yayın paketi · S08 "If America Earned $5,400 a Month, Here's Its Budget"

İLERLEME: F8a tamam (metin kesin). F8b bekliyor: gerçek ses/kurgu zamanları (§4), thumbnail finalisti (§1, `veri:thumbnail-ana`), müzik atfı (`06-muzik/atif-satirlari.md`), gerçek dosyalarla `--dry-run` 3/3, `YAYIN.md`.
**Hazırlayan:** youtube-paketleyici · **Tarih:** 2026-11-02 · **Durum:** KESİN METİN (F8a). Değişmeyen metin F8b'de yeniden yazılmaz.
**Girdiler:** `03-metin/metin.md` v1.2 (kilit, sha256 c833cb696030), `rakam-tablosu.md` §6 (yasal not), `dogrulama.md` §3 (Alt-2 "Nearly"), `politika-denetimi.md` §3.3 (sabit yorum nötr), `02-senaryo/senaryo-karari.md` H8, `docs/yayin-takvimi.md`.
**Tek kaynak:** JSON'lar bu dosyadaki `<!-- veri:… -->` bloklarından `paket-uret.py` ile üretilir; `paket-kontrol.py` birebir karşılaştırır (§10). `{MUZIK_*}` belirteçleri `06-muzik/atif-satirlari.md`'den, yoksa görünür yer tutucuyla doldurulur (F8b'de `--final` kipinde hata).
Etiketler: **[Ö]** betik ölçümü · **[T]** yargı.

**Kırmızı çizgiler:** parti/kişi adı yok; "default/crash/collapse" yok; "Just Hit / Just Passed" (WhiteBoard Finance haber-bandı kalıbı) yok; "What's Really Happening" yok; "$7 for $5" yalnız "Nearly" ile (R04 = 6,84); tavsiye/emir dili yok.

---

## 1. Başlık — 7 aday, 5 varyant (önerilen T1)

Arama ve öneri ayrı: B sütunu, seçim ertesi gün; trafik ağırlığı gözatma/öneri [T] → başlık merak + somut özne ("America", "$5,400 a month"). Arama ifadeleri ("US budget", "national debt", "deficit", "interest") açıklamanın ilk satırında, bölümlerde, etiketlerde. **Tek vaat:** başlık ("$5,400 a month → bütçesi") = thumbnail konsepti ("−$2,000/MO", hakem H8) = ilk 15 sn ("Shrink the U.S. government down to one household. It brings home five thousand four hundred dollars a month. It spends about seven thousand four hundred.").

| # | Açı | Başlık | Krk [Ö] | Puan [Ö] | Karar |
|---|---|---|---|---|---|
| T1 | merak | If America Earned $5,400 a Month, Here's Its Budget | 51 | **8.20** | **ÖNERİLEN** (hakem H8; S01 hook'u birebir karşılar) |
| T4 | merak/arama | America's Budget, Shrunk to One Kitchen Table | 45 | 8.10 | yedek 1 (fark 0.10 anlamsız; T1 rakam taşıdığı için önde) |
| T3 | sonuç | America Pays More in Interest Than for Its Military | 51 | 7.50 | yedek 2 (R08/R12 doğrulanmış olgu; Test & Compare'de başlık testi gerekirse ilk aday) |
| T2 | karşıtlık | The US Spends Nearly $7 for Every $5 It Earns. Then What? | 57 | 7.30 | yedek 3 = H8 Alt-2, dogrulama §3 düzeltmesiyle ("Nearly") |
| T7 | sonuç | America's Interest Bill Tripled in Five Years. Why? | 51 | 7.00 | yedek 4 (R19 ×2,99 "roughly tripled") |
| T5 | karşıtlık | A Country Isn't a Family. Its Interest Bill Is. | 47 | 6.50 | ELENDİ: somut özne yok (merak tavanı 6); tezi başlıkta verir, videonun dönüşünü harcar |
| T6 | sonuç | US Interest Payments Just Passed the Military | 45 | 5.30 | ELENDİ: WhiteBoard "Just Hit" kalıbı (benzer_aci −1.5) + yanlış zaman ("just": faiz savunmayı FY2024'te geçti, R21) |

Puan = .30 merak + .20 arama + .20 thumbnail ile okunuş + .20 politika/doğruluk + .10 mobil − kalıp cezası. Ölçüt puanları yargı [T]; toplam ve sıra betikte [Ö] (§10 [2]).

<!-- veri:basliklar -->
```text
If America Earned $5,400 a Month, Here's Its Budget
America's Budget, Shrunk to One Kitchen Table
America Pays More in Interest Than for Its Military
The US Spends Nearly $7 for Every $5 It Earns. Then What?
America's Interest Bill Tripled in Five Years. Why?
```

<!-- veri:basliklar-elenen -->
```text
A Country Isn't a Family. Its Interest Bill Is.
US Interest Payments Just Passed the Military
```

**Başlık–thumbnail birlikte okunuş (KONSEPT düzeyi; finalistler gelince bu tablo yeniden yazılır, eski harfler kalmaz):** T1 geliri söyler ($5,400 a month), thumbnail açığı gösterir (−$2,000/MO) → iki rakam birbirini tekrar etmez, birlikte "gelir 5.400, her ay 2.000 eksik, nereye gidiyor?" sorusunu kurar; videodaki karşılığı 0:03–0:14 ("$5,400 IN" / "$7,400 OUT" / "−$2,000/MO"). T2 thumbnail ile üç rakam yarıştırır (kalabalık) → thumbnail yalnız "−$2,000/MO" ise yedek. Thumbnail metni ≤4 kelime, ölçek kaynağı açıklamada (H8).

<!-- veri:thumbnail-ana -->
```text
```

---

## 2. Açıklamanın ilk 2 satırı (2 versiyon → A)

| Versiyon | Krk [Ö] | Anahtar ilk 150'de | Karar |
|---|---|---|---|
| **A** "The US federal budget and deficit, shrunk to one kitchen table: $5,400 a month in, about $7,400 out. Where does the $2,000 gap go?" | betik §10 [3] | US federal budget + deficit + $5,400, arama ifadesi 5. karakterde | **SEÇİLDİ** |
| B "If the US government were a family earning $5,400 a month, here's its budget: the national debt and interest bill, explained." | 126 | national debt + interest, ama başlığı tekrar eder, "budget" ~65. karakterde | elendi (başlık tekrarı; 1929 dersi) |

---

## 3. Açıklama (uzun video, kesin)

Düzen: hook → anlatı → ölçek notu → "Not financial advice" → `{BOLUMLER}` (araç "Chapters:" basar) → LEGAL NOTE (rakam-tablosu §6 aynen + görsel satırı aynı paragrafta) → SOURCES → MUSIC & SOUND → kanal. Uzun video URL'si yok (yükleme öncesi ID yok).

<!-- veri:aciklama -->
```text
The US federal budget and deficit, shrunk to one kitchen table: $5,400 a month in, about $7,400 out. Where does the $2,000 gap go?

Leo, our cartoon roommate, puts every federal bill in its own envelope: Social Security, Medicare, other health programs, defense, everything else, and interest. Then he opens the interest envelope and finds another one inside: borrowed. We look at why the interest bill roughly tripled in five years, three things a country can do that a family can't, and three ways countries have closed gaps like this before. Possibilities, not a forecast.

Scale: $1 a month here = $1 billion a year for the US government. Budget year: FY2026 (Oct 2025–Sep 2026), Monthly Treasury Statement. Debt figures are debt held by the public.

Not financial advice. For educational purposes only.

{BOLUMLER}

LEGAL NOTE
This video is for education and entertainment only and is not financial, investment, tax or legal advice. Leo is a fictional character. Budget figures: U.S. Treasury Monthly Treasury Statement, fiscal year 2026 (Oct 2025–Sep 2026); debt: Treasury Debt to the Penny, Sep 30 2026; history: OMB Historical Table 7.1; rates: FRED. Scale: $1 a month = $1 billion a year. Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

SOURCES
• U.S. Treasury, Monthly Treasury Statement, FY2026 (Tables 1 and 9): https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/
• U.S. Treasury, Debt to the Penny (debt held by the public, Sep 30, 2026): https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/
• U.S. Treasury, Average Interest Rates on U.S. Treasury Securities: https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/
• OMB, Historical Tables, Table 7.1 (FY2025 Budget): https://www.govinfo.gov/content/pkg/BUDGET-2025-TAB/xls/BUDGET-2025-TAB-8-1.xlsx
• FRED, 10-Year Treasury yield (DGS10): https://fred.stlouisfed.org/series/DGS10
• FRED, 3-Month Treasury bill (DTB3): https://fred.stlouisfed.org/series/DTB3
• FRED, Federal debt held by the public as % of GDP (FYGFGDQ188S): https://fred.stlouisfed.org/series/FYGFGDQ188S
• Robert J. Shiller, U.S. consumer price data (from BLS CPI): http://www.econ.yale.edu/~shiller/data.htm
Charts in this video are our own, built from the data above.

MUSIC & SOUND
{MUZIK_UZUN}

MORE FROM TOONOMY
New animated finance stories every week: https://www.youtube.com/@toonomy

#USBudget #NationalDebt #EconomyExplained
```

---

## 4. Bölümler — metin §4 (betik zamanı; F8b'de gerçek sahne zamanına kayar)

Açan sahneler: S01, S05, S08, S12, S16, S21, S26. Gerçek ses gelince (`04-ses/sahne-zamanlari.json`) her bölüm açan sahnenin `bas` zamanına aşağı yuvarlanır; kurguda ofset varsa (`08-kurgu/kurgu-rapor.md`) hepsi aynı farkla kayar, ilk bölüm 00:00 kalır. Betik §10 [3b] dosya varsa eşleşmeyi ölçer.

<!-- veri:bolumler -->
```text
00:00 One household, $5,400 a month
01:28 Five envelopes
02:53 The loan
04:32 The envelope inside the envelope
06:36 Three things a family can't do
09:06 Three ways to close the gap
11:00 Back to the sentence
```

---

## 5. Etiketler ve hashtag'ler

Etiketler küçük sinyal (eş anlam/yazım varyantı); en özgül önde. Seçim/parti/aday adı yok (P1). "Default", "debt crisis" yok (videonun çerçevesi değil; yanıltıcı meta veri riski, support 2801973).

<!-- veri:etiketler -->
```text
us budget explained, federal budget, us federal budget 2026, national debt, national debt explained, us national debt, federal deficit, budget deficit explained, interest on the national debt, net interest, debt held by the public, debt to gdp, treasury yields, social security, medicare, defense spending, government spending, us economy explained, economics explained, finance animation, animated explainer, toonomy
```

<!-- veri:hashtagler -->
```text
#USBudget #NationalDebt #EconomyExplained
```

**Kategori:** 27 Education · **Dil:** en / en · **Çocuklara özel:** hayır · **Lisans:** standart · **Yerleştirme:** açık.

---

## 6. Shorts paketleri

**Uzun videoya bağlantı:** Related video alanının Data API karşılığı doğrulanmadı → **Studio adımı** (`YAYIN.md`). Açıklamada uzun video başlığı + kanal bağlantısı (URL yer tutucusu yok).

### Shorts 1 — "The interest envelope" (seçildi: a)
| Aday | Başlık | Krk | Karar |
|---|---|---|---|
| **a** | Interest vs. the Military: Which US Bill Is Bigger? | 51 | SEÇİLDİ: yorum sorusu, cevap kesitte (MTS R06 > R08) |
| b | If the US Were a Family, This Is Its Interest Bill | 50 | elendi: kancanın aynısı, bilgi eklemiyor |

<!-- veri:shorts1-baslik -->
```text
Interest vs. the Military: Which US Bill Is Bigger?
```

<!-- veri:shorts1-aciklama -->
```text
Shrink the US budget to one family earning $5,400 a month. Defense: $965. Interest: about $1,050, and it buys nothing. Then the interest envelope turns out to hold another one: borrowed.

Scale: $1 a month here = $1 billion a year for the US government. FY2026 (Oct 2025–Sep 2026), Monthly Treasury Statement.

The whole kitchen table: "If America Earned $5,400 a Month, Here's Its Budget" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS1}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #NationalDebt #USBudget
```

### Shorts 2 — "A family can't do this" (seçildi: a)
| Aday | Başlık | Krk | Karar |
|---|---|---|---|
| **a** | US Debt Was Bigger Than the Economy in 1946. What Happened? | 59 | SEÇİLDİ: soru, arama ifadesi ("US debt 1946"), doğru |
| b | How the US Shrank Its Debt Without Paying It Off | 48 | elendi: yanlış; borcun dolar tutarı büyüdü (R34), küçülen GSYH payı |

<!-- veri:shorts2-baslik -->
```text
US Debt Was Bigger Than the Economy in 1946. What Happened?
```

<!-- veri:shorts2-aciklama -->
```text
In 1946, US debt held by the public was bigger than the whole economy. By 1974 it was under a quarter of it, even though the debt itself grew. The economy grew around it, and prices rose too. A family can't do that. History, not a forecast.

Source: OMB Historical Tables, Table 7.1 (debt held by the public, % of GDP).

The whole kitchen table: "If America Earned $5,400 a Month, Here's Its Budget" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS2}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #NationalDebt #EconomicHistory
```

---

## 7. Pinli yorum (A seçildi)

Tek A/B/C sorusu (1929 F12 dersi; S25 ekranıyla aynı: "ONE LETTER IN THE COMMENTS"). Seçim ertesi nötr (politika-denetimi §3.3): seçenekler metindeki mekanizma adlarıyla, B'de "raise taxes / cut spending" yerine nötr "change the envelopes"; parti, kişi, "who's to blame" yok; bugüne "paranı ne yap" sorusu yok.
- A (seçilen): aşağıdaki blok.
- B (elendi): "Which envelope surprised you most?" — tek harf değil, retention'ı sona çekmiyor; S25 ekranıyla çelişir.
- C (elendi): "Taxes up or spending down?" — partizan zemine çeker (P1, seçim ertesi).

<!-- veri:pinli-yorum -->
```text
One letter only: which possibility do you think will do the most work closing the gap?

A: grow the paycheck
B: change the envelopes
C: let prices rise

(Sources, scale and data notes are in the description.)
```

---

## 8. Uç ekran, kart, oynatma listesi

- **Uç ekran:** S27 köprüsü (metin planı 11:26–11:44, ~18 sn) — **süre F8b'de gerçek sesten ölçülür** (1929'da plan 17 → gerçek 13,2 sn). Öğeler: abone + video "Best for viewer" (kanalda tek diğer video 1929 `BVJwZ1C9R1U`; S06 yayınlanırsa doğrudan o, köprü "5%" notuna bağlanır). Var olmayan videoya söz yok (metin §6 A).
- **Kart:** yok (konuyla bağlantılı yayında video yok). S06 (%5 tahvil) yayınlanınca S14'e (~5:39, "close to five percent") kart.
- **Oynatma listesi:** **B · Bugün → "Money News, Explained"** (kanal-paketi.json'da planlı; bu video listeyi açar → F11'de koordinatör `tools/yayin/kanal.py`, sonra `oynatma_listesi_id`). Shorts → "Money Stories in 60 Seconds | Shorts".

---

## 9. Takvim ve durum alanları

Zaman tek kaynak bu blok (1929 dersi). ABD 1 Kasım'dan beri kış saati → **EST, UTC−5**. Uzun Çar 12:00 ET = 17:00 UTC = 20:00 TRT; Shorts takvim v2'ye göre Çarşamba videosunun Shorts'u Perşembe + Cumartesi 09:00 ET (14:00 UTC). K3 kaçarsa koordinatör `yedek` satırlarını üst satırlara taşır ve `paket-uret.py` yeniden koşar (Pazar videosu → Shorts Pzt + Sal).

<!-- veri:yayin-zamani -->
```text
uzun|2026-11-04T12:00:00-05:00
shorts-1|2026-11-05T09:00:00-05:00
shorts-2|2026-11-07T09:00:00-05:00
yedek-uzun|2026-11-08T12:00:00-05:00
yedek-shorts-1|2026-11-09T09:00:00-05:00
yedek-shorts-2|2026-11-10T09:00:00-05:00
```

- **`durum.sentetik_medya`:** monetizasyon-uyum-uzmani'nin F8 `politika-raporu.md` kararı henüz yok. F3 önerisi `true` (politika-denetimi P4) → paket geçici olarak **true** (1929 emsali); karar gelince `paket-uret.py` sabiti güncellenir. Karar benim değil. AI satırı her durumda açıklamada.
- **`gizlilik` = private + `yayin_zamani`**, `onay.niyazi_onayi` = false.
- **Dosyalar:** `../08-kurgu/final-16x9.mp4`, `../08-kurgu/final.en.srt`, `../08-kurgu/shorts-{1,2}.mp4` — 1929 adlandırması; **F8b'de `ls 08-kurgu` ile doğrulanır** (tahmin değil, varsayım olarak işaretli). Thumbnail: `veri:thumbnail-ana` boş → JSON'da yok; yol thumbnail-tasarimcisi raporundan yazılır.

## 10. Test kapısı (özet; tam çıktı `kapi-cikti.txt`)

`python3 -I paket-uret.py` → `python3 -I paket-kontrol.py` (F8a kipi; F8b'de `--final`) → `tools/yayin/yukle.py --dry-run` iki kipte (gerçek paket: yalnız dosya-yok beklenir; sahte medyalı bayt-aynı kopya: 0 hata).

## 11. Açık işler (F8b)
| İş | Sahibi | Not |
|---|---|---|
| Gerçek sahne zamanları + kurgu ofseti → §4 | ses kolu / kurgu-editoru → paketleyici | betik [3b] |
| Thumbnail finalisti → `veri:thumbnail-ana` + §1 okunuş tablosu | thumbnail-tasarimcisi → paketleyici | yol rapordan |
| Müzik atfı `06-muzik/atif-satirlari.md` (1929 biçimi: kod bloğu + "Shorts N açıklaması: `…`") | muzik-ses-tasarimcisi | `{MUZIK_*}` |
| `sentetik_medya` kesin karar | monetizasyon-uyum-uzmani | `politika-raporu.md` |
| Test & Compare, Related video, uç ekran, SRT, oynatma listesi | koordinatör → `YAYIN.md` Studio | API karşılığı yok |
| Yorum yanıtları | Niyazi onayıyla | `yorum-yanitlari.md` |
