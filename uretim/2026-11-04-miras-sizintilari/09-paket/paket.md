# F8a-erken — Yayın paketi taslağı · S03 "The Leaky Moving Truck" (sütun C)

İLERLEME: tamam (F8b, 2026-11-10). F7 GEÇTİ (48d36ff): final 781,40 sn = anlatım 781,388 sn → kurgu ofseti 0, bölümler değişmedi (betik [3b] 7/7); Shorts 41,45 / 43,43 sn; uç ekran ABONE-4 kartından sonra 12:55,3–13:01,4 (6,1 sn); `sentetik_medya: true` = politika-raporu.md. `paket-kontrol.py --final` 0 hata · 0 bekleyen; `yukle.py --dry-run` 3/3 0 hata (`kapi-cikti.txt`). Açık: `ilgili_video` araç desteği (talep) → YAYIN.md zorunlu Studio adımı.
**Hazırlayan:** youtube-paketleyici · **Tarih:** 2026-11-04, güncelleme 2026-11-09 · **Durum:** KESİN METİN (F3 kilitli metin v1.1). F8b'de yalnız bölüm zamanları, uç ekran ve dosyalar.
**Girdiler:** `02-senaryo/senaryolar.md` S03, `senaryo-karari.md` §4 (D1–D6, P1–P3, K1, H1b, H6, H8), `on-dogrulama.md` (Cerulli), `01-arastirma/kanal-ozet.md` (3 ders), `docs/viralite-modeli.md` v0.2, `docs/yayin-takvimi.md`, `uretim/kanal-kimligi/kanal-paketi.json`.
**Doğrulanan kaynak (WebFetch 2026-11-04):** Cerulli basın bülteni, 5 Ara 2024, "Cerulli Anticipates $124 Trillion in Wealth Will Transfer Through 2048": toplam 124 T$, mirasçılara 105 T$, bağışa 18 T$, eşlere 54 T$ (eş payı toplamın içinde → D2: gecikme, kayıp değil).
**Tek kaynak:** JSON'lar `<!-- veri:… -->` bloklarından `paket-uret.py` ile üretilir; `paket-kontrol.py` birebir karşılaştırır. `{MUZIK_*}` ve `{KAYNAK_F3}` görünür yer tutucu → `--final` kipinde hata.
Etiketler: **[Ö]** betik ölçümü · **[T]** yargı · **[D]** doğrulanmış kaynak.

**Kırmızı çizgiler:** başlıkta çıplak $ rakam ve yıl yok (kanal dersi 1: Rakam/$ 0,95x, Yıl 0,95x); "Bank of America says" yok (D1); "biggest … ever" yalnız elenen çalışma başlığında (D3); "124 − 54 − 18" çıkarması yok (D2); "you should / set up a trust / gift it now" yok (P1); kuşak suçlaması yok (P2); "three possibilities / Possibility A/B/C / scenario one" yok (K1, pinli yorum dahil); "this week / today / tonight" yok (H6; T7'deki "Just Not" zaman anlamı taşımaz); rakip çekirdeği "What Happens When … Boomers Are Gone" yok (AJ Osborne 953x outlier → benzer_aci −1.5).

---

## 1. Başlık — 7 aday, 5 varyant (önerilen T1)

**Arama ve öneri ayrı:** C sütunu, zaman bağı yok; 3 aboneli kanalda ilk izlenme aramadan ve kalıcı sorgudan gelir (senaryo-karari §1.2) → başlıkta aranan kavram ("Great Wealth Transfer") + merak boşluğu ("Has a Leak"). Öneri tarafı (gözat): thumbnail "WHO GETS IT?" + Leo + delikli kutu sorusu. Talebe en yakın arama başlığı T3 (Alt-1) yedek.
**Tek vaat:** başlık ("transfer sızdırıyor") = thumbnail ("WHO GETS IT?" + küçük "$124T", H8) = ilk 15 sn (H1b: "…Cerulli estimates. But eighteen trillion goes to charity, and fifty-four trillion stops at a spouse first. So what really reaches the kids?").
**Yakın gelecek bağı (kanal dersi 1):** izleyici mirasçı/ev alıcısı (15–30 sn köprüsü); T1'de "transfer" süren bir olay, T7'de doğrudan izleyicinin zamanı. Test & Compare'de başlık testi açılırsa T7 ilk rakip.

| # | Açı | Başlık | Krk [Ö] | Puan [Ö] | Karar |
|---|---|---|---|---|---|
| T1 | merak | The Great Wealth Transfer Has a Leak | 36 | **8.40** | **ÖNERİLEN**: aranan kavram ilk 25 krk'de, kısa (mobilde tam), thumbnail sorusuyla zincir: sızıntı → kime kalıyor? |
| T3 | sonuç/arama | Where Will the Boomers' Money Actually Go? | 42 | 7.70 | yedek 1 = H8 Alt-1 (talebe en yakın); thumbnail da soru → çift soru, birlikte okunuş zayıf |
| T4 | karşıtlık | The Great Wealth Transfer Is Smaller Than It Sounds | 51 | 7.40 | yedek 2 = Alt-2; "smaller" mirasçı açısından doğru (105 < 124 [D]) ama itiraz çeker |
| T7 | sonuç | The Boomers' Money Is Coming. Just Not When You Think. | 54 | 7.30 | yedek 3; izleyicinin yakın geleceğine en iyi bağ (eş önce → gecikme, D2'ye sadık); "not when you think" klişeye yakın |
| T5 | karşıtlık | The Biggest Inheritance Ever, and Why Heirs Might Miss It | 57 | 6.90 | yedek 4 = çalışma başlığı; "Ever" D3 (yorum) + "Miss It" kayıp ima eder (D2 gecikme der) |
| T2 | merak | Your Parents' Money Is Taking the Long Way to You | 49 | 6.60 | ELENDİ: arama kavramı yok; "to you" thumbnail'ın "WHO GETS IT?" sorusunu önden cevaplıyor (vaat çakışması); herkesin mirası var varsayımı |
| T6 | merak | What Happens to Boomer Money Before It Reaches the Kids? | 56 | 6.00 | ELENDİ: "what happens" çerçevesi güçlü (%28) ama AJ Osborne outlier çekirdeğini taşıyor (benzer_aci −1.5) |

Puan = .30 merak + .20 arama + .20 thumbnail ile okunuş + .20 politika/doğruluk + .10 mobil (≤45:10 · ≤50:9 · ≤60:7) − kalıp cezası (S08 ile aynı formül). Ölçüt puanları [T], toplam ve sıra betikte [Ö] (`paket-kontrol.py` [2]). Arama puanı yargı: Google Trends 429, YouTube `totalResults` talep ölçüsü değil (hafıza 2026-10-28).

<!-- veri:basliklar -->
```text
The Great Wealth Transfer Has a Leak
Where Will the Boomers' Money Actually Go?
The Great Wealth Transfer Is Smaller Than It Sounds
The Boomers' Money Is Coming. Just Not When You Think.
The Biggest Inheritance Ever, and Why Heirs Might Miss It
```

<!-- veri:basliklar-elenen -->
```text
Your Parents' Money Is Taking the Long Way to You
What Happens to Boomer Money Before It Reaches the Kids?
```

**Başlık–thumbnail birlikte okunuş.** Ana: `thumbnail/K1-who-gets-it.jpg` (ifade şaşkın → kuşkulu, ec41405; teşhis a2). Test & Compare sırası **K1, K4, K3** (`thumbnail/thumb-rapor.md`); yalnız video açıldıktan sonra kurulur. Okunuş:
| Başlık | + "WHO GETS IT?" · "$124T" | Not |
|---|---|---|
| T1 | sızıntı var → peki kime kalıyor? İki parça tek soru zinciri, tekrar yok | önerilen eşleşme |
| T3 | "Where will it go?" + "Who gets it?" = aynı soru iki kez | T3 devreye girerse thumbnail metni sızıntı/kutu görseline döner (thumbnail-tasarimcisi) |
| T7 | zaman (when) + kişi (who): iki ayrı soru, ikisi de videoda cevaplı | Test & Compare başlık adayı |
Thumbnail'da "Bank of America" yok (H8); "$124T" küçük etiket, başlıkta $ yok → rakam tekrarı yok.

<!-- veri:thumbnail-ana -->
```text
../09-paket/thumbnail/K1-who-gets-it.jpg
```

---

## 2. Açıklamanın ilk 2 satırı (2 versiyon → A)

| Versiyon | Krk [Ö] | Anahtar ilk 150'de | Karar |
|---|---|---|---|
| **A** "The great wealth transfer, explained: Cerulli estimates $124 trillion will pass down in the US through 2048. How much inheritance reaches the kids?" | 147 | great wealth transfer (konum 4) + inheritance (teşhis a1), $124 trillion, 2048, Cerulli (D1) | **SEÇİLDİ** (2026-11-09: "inheritance" eklendi; "in inheritance" denmedi çünkü 124'ün 18'i bağış, R03) |
| B "Boomer inheritance and the great wealth transfer: follow one family's share of the $124 trillion and count what leaks out before the kids." | 138 | boomer inheritance + great wealth transfer, ama atıf ve dönem yok (D1 ihlali), "leaks" başlığı tekrarlar | elendi |

---

## 3. Açıklama (uzun video, kesin; yasal not `rakam-tablosu.md` §11 birebir, kaynaklar R01–R28 birincil kaynakları)

Düzen: hook → anlatı → örnek notu → "Not financial advice" → `{BOLUMLER}` → LEGAL NOTE (+ AI ve görsel satırı aynı paragrafta) → SOURCES (`{KAYNAK_F3}` = F3'ün eklediği birincil kaynaklar; D4–D6 düşerse yalnız Cerulli kalır) → MUSIC & SOUND → kanal. Uzun video URL'si yok. "Three ways / possibilities" yok (K1).

<!-- veri:yasal-not -->
```text
This video is for education and entertainment only and is not financial, investment, legal or tax advice. Figures are estimates or survey results as of the dates shown (US unless stated); future amounts are projections, not predictions. The Okafor family is fictional. Leo is a fictional cartoon character. Narration voice is AI-generated.
```

<!-- veri:aciklama -->
```text
The great wealth transfer, explained: Cerulli estimates $124 trillion will pass down in the US through 2048. How much inheritance reaches the kids?

Leo, our cartoon moving-crew boss, loads one example family's boxes onto a truck marked TO: THE KIDS and follows them down a long road. Some of the money is spent along the way, on a long life and on care. Some goes to charity. A big part stops at a spouse first, so it arrives later, not never. Then there is the house, and there are taxes and time. At the end of the road, Leo opens the truck and reads the inventory: what actually arrived, and when.

The Okafor family is an illustration, not a real household. Figures are for the US unless stated otherwise.

Not financial advice. For educational purposes only.

{BOLUMLER}

LEGAL NOTE
{YASAL_NOT} Visuals are AI-assisted illustrations animated by our team.

SOURCES
• Cerulli Associates, "Cerulli Anticipates $124 Trillion in Wealth Will Transfer Through 2048" (Dec 5, 2024): https://www.cerulli.com/press-releases/cerulli-anticipates-124-trillion-in-wealth-will-transfer-through-2048
• Bank of America Private Bank, 2026 Study of Wealthy Americans (press release, Sep 30, 2026)
• CareScout (Genworth), 2025 Cost of Care Survey: https://investor.genworth.com/news-events/press-releases/detail/1054
• ASPE (HHS), long-term services and supports brief (Aug 2022): https://www.govinfo.gov/content/pkg/GOVPUB-HE-PURL-gpo212746/pdf/GOVPUB-HE-PURL-gpo212746.pdf
• Medicare.gov, Nursing home care: https://www.medicare.gov/coverage/nursing-home-care
• Medicaid.gov, Estate recovery: https://www.medicaid.gov/medicaid/eligibility-policy/estate-recovery
• IRS, tax inflation adjustments for tax year 2026: https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill
• IRS, Retirement topics: Beneficiary: https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-beneficiary
• Federal Reserve, Survey of Consumer Finances 2022 (Federal Reserve Bulletin, Oct 2023): https://www.federalreserve.gov/publications/files/scf23.pdf
• Federal Reserve, Distributional Financial Accounts: https://www.federalreserve.gov/releases/z1/dataviz/dfa/
• GOV.UK, Inheritance Tax: https://www.gov.uk/inheritance-tax
Charts in this video are our own, built from the sources above.

MUSIC & SOUND
{MUZIK_UZUN}

MORE FROM TOONOMY
New animated finance stories every week: https://www.youtube.com/@toonomy

#GreatWealthTransfer #Inheritance #FinanceExplained
```

---

## 4. Bölümler — gerçek sahne zamanları (`04-ses/sahne-zamanlari.json`, toplam 781,388 sn = 13:01,4; kurgu ofseti 0, koordinatör 2026-11-09). Adlar `03-metin/metin.md` §4 birebir

Açan sahneler S01, S06, S08, S13, S18, S21, S26 → her bölüm sahnenin `bas`'ına aşağı yuvarlanır (betik [3b], fark −1…0). F7 sonrası `kurgu-rapor.md` ofseti ≠ 0 ise hepsi aynı farkla kayar, 00:00 sabit.

<!-- veri:bolumler -->
```text
00:00 The number on the truck
01:46 Loading the Okafors
02:35 Living and care
04:58 The detour and the gift
07:09 The heaviest box
08:13 The tax stop
10:42 Arrival
```

---

## 5. Etiketler ve hashtag'ler

En özgül önde; eş anlam ve yazım varyantları. Kuşak suçlayan ("boomers ruined…") ve korku ("inheritance tax trap") etiketi yok. Popüler terimler F8b'de SRT'de aranır (hafıza kuralı; `paket-kontrol.py` [4] `SRT_TERIM`).

<!-- veri:etiketler -->
```text
great wealth transfer, great wealth transfer explained, baby boomer inheritance, boomer wealth transfer, inheritance explained, intergenerational wealth transfer, generational wealth, wealth transfer, inheritance, heirs, baby boomers, cerulli, long term care costs, estate tax explained, spouse inheritance, charitable giving, personal finance explained, economics explained, finance animation, animated explainer, toonomy
```

<!-- veri:hashtagler -->
```text
#GreatWealthTransfer #Inheritance #FinanceExplained
```

**Kategori:** 27 Education · **Dil:** en / en · **Çocuklara özel:** hayır ("toon" adı riski: kitle ayarı açıkça "not made for kids") · **Lisans:** standart · **Yerleştirme:** açık.

---

## 6. Shorts paketleri (F3 metin §5 kesitleri: Shorts 1 "The detour", Shorts 2 "The leak people fear")

**Uzun videoya köprü (kanal-ozet ders 2, teşhis a4):** Data API v3 `videos` kaynağında "related video" alanı **yok** [D: developers.google.com/youtube/v3/docs/videos, 2026-11-04]. Shorts JSON'larında `ilgili_video` alanı taşınır (dry-run "bilinmeyen alan" UYARISI; talep `talep-uretim-muhendisi.md`, henüz uygulanmadı). Uygulama **Niyazi'nin zorunlu Studio adımı, Short açılmadan ÖNCE** (`YAYIN.md`). Her iki Short da cevabı yalnız uzun videoda olan soruyla biter (metin §5). D4 (%47/%55) Shorts'a girmedi; önceki "Are the Heirs Ready…" taslağı kaldırıldı.

### Shorts 1 — "The detour" (seçildi: a)
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| **a** | Why Does So Much Inheritance Stop at a Spouse First? | 52 | SEÇİLDİ: kesitin tek olgusu (R04 $54T eş) + açık soru; akışta somut, aramada "inheritance" |
| b | The Great Wealth Transfer: What Actually Reaches the Kids? | 58 | elendi: kesitin olgusunu (eş durağı) söylemiyor, uzun başlığa fazla yakın |

<!-- veri:shorts1-baslik -->
```text
Why Does So Much Inheritance Stop at a Spouse First?
```

<!-- veri:shorts1-aciklama -->
```text
About $124 trillion is expected to pass down in the US through 2048, Cerulli estimates. About $54 trillion of it is expected to stop at a surviving husband or wife first, nearly $40 trillion of that with widowed women. That money isn't lost. It's delayed. So how many boxes are left when the truck finally reaches the kids?

Source: Cerulli Associates, December 2024.

The whole road, stop by stop: "The Great Wealth Transfer Has a Leak" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS1}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inheritance #GreatWealthTransfer
```

### Shorts 2 — "The leak people fear" (seçildi: a)
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| **a** | If Not Taxes, Where Does the Inheritance Really Go? | 51 | SEÇİLDİ: kesitin kapanış sorusuyla birebir; cevap (sessiz sızıntılar) yalnız uzun videoda |
| b | The Estate Tax Line vs. a Typical Family's Wealth | 49 | elendi: soru yok, kesitin cevabını başlıkta verir; "vergi" korku etiketi gibi okunabilir |

<!-- veri:shorts2-baslik -->
```text
If Not Taxes, Where Does the Inheritance Really Go?
```

<!-- veri:shorts2-aciklama -->
```text
Taxes sound like the scariest leak when money is passed down. But as of 2026, the US federal estate tax only starts above $15 million per person. For families headed by someone 65 to 74, median net worth was about $410,000 in 2022. So where does the money really go on the way to the kids?

US federal only; state rules and other countries differ. Sources: IRS, 2026 inflation adjustments; Federal Reserve, Survey of Consumer Finances 2022 (2022 dollars).

The whole road, stop by stop: "The Great Wealth Transfer Has a Leak" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS2}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inheritance #EstateTax
```

---

## 7. Pinli yorum (A seçildi)

K1: "üç olasılık" kapanışı ve A/B/C üçlü yapısı bu videoda yok → soru Leo'nun clipboard'undaki altı durağa bağlanır (metin v0.1 dili: "six stops", tabelalar LIVING/CARE/…/GIVING/TAX), tek soru, numarayla yanıt. Altısına "leak" denmez: 3. durakta "Nothing leaked" (D2). Kişisel miras/servet sorusu yok (mahremiyet, ölüm konusu ağır; P2). Sızıntı adları F3 metniyle birebir (betik BEKL).
- Teşhis a7 "Which leak surprised you most?" önerdi; "leak" yerine "stop" kalır (3. durak "Nothing leaked", D2), soru biçimi aynı.
- **A (seçilen):** aşağıdaki blok — durak 1–6, "which surprised you most?" (ilk sürüm "six leaks" metinle çelişti, betik yakaladı → düzeltildi).
- B (elendi): "Will your generation inherit more or less than it expects?" — kişisel finans tahmini ister, tavsiye zincirine açılır (P1).
- C (elendi): "What's one thing you hope stays in the truck?" — duygusal ama ölüm/kayıp çağrışımı (P2), yanıtlaması zor.

<!-- veri:pinli-yorum -->
```text
Leo's clipboard has six stops between the parents and the kids. Which one surprised you most? Reply with its number.

1: a long life
2: care
3: a spouse first
4: giving
5: the house
6: taxes

(Sources and notes are in the description. The Okafor family is an example, not a real household.)
```

---

## 8. Uç ekran, kart, oynatma listesi

- **Uç ekran:** **12:55,3–13:01,4 = 6,1 sn** [Ö] (final 781,40 sn; başlangıç = ABONE-4 kartının bitişi 775,30 sn: tık 773,10 − 1,3 + 3,5 sn kart süresi, `08-kurgu/log/kapi-tur3.txt` + `AboneOl.tsx`; S31 köprüsü 773,60'ta başlar ama kartla çakışmaz). Studio'da son 6 sn. Öğeler: Abone + video **"You Have $1,000 in 1929. Can You Keep It?" (BVJwZ1C9R1U)** (teşhis a6). S08 gösterilmez; var olmayan videoya söz yok. Açılıştan sonra kurulur.
- **Kart:** S04 yayınlanınca "the house" bölümüne kart (H7 seri devamı). Şimdilik yok.
- **Oynatma listesi:** **C · Gelecek → "What If…? Future of Money Scenarios"**. Bu video listeyi açar (boş liste yok): koordinatör `tools/yayin/kanal.py` ile listeyi açar, ekleme `yukle.py --liste-sonra <LISTE_ID>` ile açılış SONRASINA ertelenir (`yayin-kontrol.py --liste-ekle`, açılış +15 dk). Shorts → "Money Stories in 60 Seconds | Shorts", aynı yolla.

---

## 9. Takvim ve durum alanları

ABD kış saati (EST, UTC−5). **Paz 11-08 slotu kaçtı (K3)** → stok kuralıyla B slotunun yerine **Çar 2026-11-11 12:00 ET = 17:00 UTC = 20:00 TRT** (koordinatör 2026-11-09). Çarşamba videosunun Shorts'u Per + Cmt 09:00 ET (14:00 UTC; takvim v2). Bir kez daha kayarsa koordinatör `yedek` satırlarını üste taşır, `paket-uret.py` yeniden koşar (Paz 11-15 / Pzt 11-16 / Sal 11-17).

<!-- veri:yayin-zamani -->
```text
uzun|2026-11-11T12:00:00-05:00
shorts-1|2026-11-12T09:00:00-05:00
shorts-2|2026-11-14T09:00:00-05:00
yedek-uzun|2026-11-15T12:00:00-05:00
yedek-shorts-1|2026-11-16T09:00:00-05:00
yedek-shorts-2|2026-11-17T09:00:00-05:00
```

- **`durum.sentetik_medya`: true** = monetizasyon-uyum-uzmani kararı (`politika-raporu.md`, 2026-11-10); betik karşılaştırır. AI ses satırı açıklamada.
- **`gizlilik` = private + `yayin_zamani`**, `onay.niyazi_onayi` = false (üç pakette).
- **Dosyalar (F7, `ls 08-kurgu` ile teyitli):** `../08-kurgu/final-16x9.mp4` (1920x1080, 781,40 sn), `../08-kurgu/final.en.srt` (296 blok), `../08-kurgu/shorts-1.mp4` (1080x1920, 41,45 sn), `../08-kurgu/shorts-2.mp4` (1080x1920, 43,43 sn).

## 10. Test kapısı
`python3 -I paket-uret.py` → `python3 -I paket-kontrol.py` (taslak kipi; F8b `--final`) → `tools/yayin/yukle.py --dry-run` iki kipte (gerçek: yalnız dosya-yok; sahte medyalı bayt-aynı kopya: 0 hata). Çıktı: `kapi-cikti.txt`.

## 11. Açık işler
| İş | Sahibi | Not |
|---|---|---|
| F7 dosyaları (`ls 08-kurgu`), kurgu ofseti → bölüm kayması, uç ekran süresi, SRT terim taraması, gerçek dry-run 3/3 | kurgu-editoru → paketleyici F8b | `paket-kontrol.py --final` |
| `sentetik_medya` | monetizasyon-uyum-uzmani | `politika-raporu.md` |
| `ilgili_video` alanı SEMA + YAYIN çıktısı | uretim-muhendisi | `talep-uretim-muhendisi.md` (açık) |
| Related video (Short açılmadan önce), Test & Compare, uç ekran, SRT, sabit yorum | Niyazi (Studio) | `YAYIN.md` |
| Kanal: "What If…" liste açıklamasındaki "New episodes every other Sunday" gün sözü (tempo 4 hafta kuralı; bu video da Çarşamba açılıyor) | koordinatör (kanal paketi) | liste açılmadan önce düzeltilmeli |
