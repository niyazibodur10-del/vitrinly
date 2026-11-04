# F8a-erken — Yayın paketi taslağı · S03 "The Leaky Moving Truck" (sütun C)

İLERLEME: F4 taslak tamam (2026-11-04). Bekleyen (betik BEKL listesi, `kapi-cikti.txt`): F3 `03-metin/metin.md` §4 bölüm adları + `rakam-tablosu.md` yasal not ve kaynaklar (`{KAYNAK_F3}`), D4 kararı (Shorts 2 asıl/yedek), thumbnail finalisti, `06-muzik/atif-satirlari.md`, `politika-raporu.md` (`sentetik_medya`), F7 dosyaları + gerçek sahne zamanları (F8b). Yeniden üretim: `python3 -I paket-uret.py && python3 -I paket-kontrol.py`.
**Hazırlayan:** youtube-paketleyici · **Tarih:** 2026-11-04 · **Durum:** TASLAK (metin kilidinden önce). F8a'da yalnız F3'ün değiştirdiği satırlar güncellenir; F8b'de yalnız bölüm zamanları ve dosyalar.
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

**Başlık–thumbnail birlikte okunuş (konsept H8; finalistler F8a'da thumbnail-tasarimcisi'nden):**
| Başlık | + "WHO GETS IT?" · "$124T" | Not |
|---|---|---|
| T1 | sızıntı var → peki kime kalıyor? İki parça tek soru zinciri, tekrar yok | önerilen eşleşme |
| T3 | "Where will it go?" + "Who gets it?" = aynı soru iki kez | T3 devreye girerse thumbnail metni sızıntı/kutu görseline döner (thumbnail-tasarimcisi) |
| T7 | zaman (when) + kişi (who): iki ayrı soru, ikisi de videoda cevaplı | Test & Compare başlık adayı |
Thumbnail'da "Bank of America" yok (H8); "$124T" küçük etiket, başlıkta $ yok → rakam tekrarı yok.

<!-- veri:thumbnail-ana -->
```text
```

---

## 2. Açıklamanın ilk 2 satırı (2 versiyon → A)

| Versiyon | Krk [Ö] | Anahtar ilk 150'de | Karar |
|---|---|---|---|
| **A** "The great wealth transfer, explained: about $124 trillion is set to pass down in the US through 2048, Cerulli estimates. What reaches the kids?" | 143 | great wealth transfer (konum 4), $124 trillion, 2048, Cerulli (D1 atıf + dönem) | **SEÇİLDİ** |
| B "Boomer inheritance and the great wealth transfer: follow one family's share of the $124 trillion and count what leaks out before the kids." | 138 | boomer inheritance + great wealth transfer, ama atıf ve dönem yok (D1 ihlali), "leaks" başlığı tekrarlar | elendi |

---

## 3. Açıklama (uzun video, taslak; F3 rakam-tablosu ile kesinleşir)

Düzen: hook → anlatı → örnek notu → "Not financial advice" → `{BOLUMLER}` → LEGAL NOTE (+ AI ve görsel satırı aynı paragrafta) → SOURCES (`{KAYNAK_F3}` = F3'ün eklediği birincil kaynaklar; D4–D6 düşerse yalnız Cerulli kalır) → MUSIC & SOUND → kanal. Uzun video URL'si yok. "Three ways / possibilities" yok (K1).

<!-- veri:yasal-not -->
```text
This video is for education and entertainment only and is not financial, investment, tax or legal advice. Leo is a fictional character, and the Okafor family is an illustration, not a real household. Wealth transfer figures: Cerulli Associates estimates through 2048 (December 2024). Figures are for the US unless stated otherwise. Narration voice is AI-generated.
```

<!-- veri:aciklama -->
```text
The great wealth transfer, explained: about $124 trillion is set to pass down in the US through 2048, Cerulli estimates. What reaches the kids?

Leo, our cartoon moving-crew boss, loads one example family's boxes onto a truck marked TO: THE KIDS and follows them down a long road. Some of the money is spent along the way, on a long life and on care. Some goes to charity. A big part stops at a spouse first, so it arrives later, not never. Then there is the house, and there are taxes and time. At the end of the road, Leo opens the truck and reads the inventory: what actually arrived, and when.

The Okafor family is an illustration, not a real household. Figures are for the US unless stated otherwise.

Not financial advice. For educational purposes only.

{BOLUMLER}

LEGAL NOTE
{YASAL_NOT} Visuals are AI-assisted illustrations animated by our team.

SOURCES
• Cerulli Associates, "Cerulli Anticipates $124 Trillion in Wealth Will Transfer Through 2048" (Dec 5, 2024): https://www.cerulli.com/press-releases/cerulli-anticipates-124-trillion-in-wealth-will-transfer-through-2048
{KAYNAK_F3}
Charts in this video are our own, built from the sources above.

MUSIC & SOUND
{MUZIK_UZUN}

MORE FROM TOONOMY
New animated finance stories every week: https://www.youtube.com/@toonomy

#GreatWealthTransfer #Inheritance #FinanceExplained
```

---

## 4. Bölümler — TASLAK (senaryo yapısı zamanları; F3 metin §4 adları birebir alır, F8b gerçek sahne `bas`'ına kayar)

<!-- veri:bolumler -->
```text
00:00 The number everyone quotes
01:30 One family's truck
03:30 The cost of care
05:45 Two detours: a spouse and charity
08:00 The biggest box: the house
10:30 Taxes and time
12:00 The truck arrives
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

## 6. Shorts paketleri

**Uzun videoya köprü (kanal dersi 2):** Data API v3 `videos` kaynağında "related video" alanı **yok** [D: developers.google.com/youtube/v3/docs/videos, 2026-11-04; yazılabilir alanlar snippet/status/localizations/recordingDetails/paidProductPlacementDetails]. Bu yüzden Shorts JSON'larında `ilgili_video` alanı (başlık + `video_id: null`) taşınır; araç bunu henüz tanımıyor → dry-run "bilinmeyen alan" UYARISI verir (hata değil) → **uretim-muhendisi talebi:** `talep-uretim-muhendisi.md`. Uygulama Studio'da (YAYIN.md), uzun video herkese açık olduktan sonra, Short'un yayın saatinden önce. Her iki Short da cevabı uzun videoda olan soruyla biter (kesit F7'de kurgu-editoru).

### Shorts 1 — "What reaches the kids?" (seçildi: a)
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| **a** | The Great Wealth Transfer: What Actually Reaches the Kids? | 58 | SEÇİLDİ: arama kavramı + açık soru; cevap yalnız uzun videoda |
| b | Why Might Heirs See Far Less Than the Headline Number? | 54 | elendi: "far less" D2 ile çelişir (eş payı geç gelir, kaybolmaz) |

<!-- veri:shorts1-baslik -->
```text
The Great Wealth Transfer: What Actually Reaches the Kids?
```

<!-- veri:shorts1-aciklama -->
```text
About $124 trillion is set to pass down in the US through 2048, Cerulli estimates. But $18 trillion of it goes to charity, and $54 trillion goes to a spouse first. So what reaches the kids, and when?

Source: Cerulli Associates, December 2024.

The whole road, box by box: "The Great Wealth Transfer Has a Leak" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS1}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #GreatWealthTransfer #Inheritance
```

### Shorts 2 — asıl: "Are the heirs ready?" (D4 teyidine bağlı) · yedek: "A spouse first"
| Aday | Başlık | Krk [Ö] | Karar |
|---|---|---|---|
| **a** | Are the Heirs Ready to Run the Family's Giving? | 47 | SEÇİLDİ (D4 teyit edilirse): ankette sorulan şeyle birebir |
| b | Wealthy Parents Doubt Their Kids. Where Does the Money Go? | 58 | elendi: anket "bağışı yönetmeye hazır mı" sorusunu genel "çocuklarından şüphe"ye büyütür |
| **yedek** | Why Does So Much Inheritance Stop at a Spouse First? | 52 | D4 düşerse (senaryo-karari D4: Shorts 2 kancası çıkar) → bloklar `shorts2-yedek-*` asıl bloklara taşınır |

<!-- veri:shorts2-baslik -->
```text
Are the Heirs Ready to Run the Family's Giving?
```

<!-- veri:shorts2-aciklama -->
```text
In a Bank of America survey, 47% of wealthy Americans said the next generation is ready to run the family's giving, down from 55% the time before. And about $18 trillion of the great wealth transfer is expected to go to charity. So where does the money go instead?

Sources: Bank of America Private Bank, Study of Wealthy Americans; Cerulli Associates, December 2024.

The whole road, box by box: "The Great Wealth Transfer Has a Leak" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS2}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inheritance #GreatWealthTransfer
```

<!-- veri:shorts2-yedek-baslik -->
```text
Why Does So Much Inheritance Stop at a Spouse First?
```

<!-- veri:shorts2-yedek-aciklama -->
```text
Of the roughly $124 trillion expected to pass down in the US through 2048, Cerulli estimates $54 trillion goes to a spouse first. That money isn't gone. It's delayed. So when does it reach the kids, and how much of it is left?

Source: Cerulli Associates, December 2024.

The whole road, box by box: "The Great Wealth Transfer Has a Leak" on our channel, https://www.youtube.com/@toonomy

{MUZIK_SHORTS2}

Not financial advice. For educational purposes only. Leo is a fictional cartoon character, not a financial adviser.
Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team.

#Shorts #Inheritance #GreatWealthTransfer
```

---

## 7. Pinli yorum (A seçildi)

K1: "üç olasılık" kapanışı ve A/B/C üçlü yapısı bu videoda yok → soru Leo'nun envanter listesine bağlanır (kapanış sahnesiyle aynı nesne), tek soru, numarayla yanıt (tek tuş, yorum sayısı). Kişisel miras/servet sorusu yok (mahremiyet, ölüm konusu ağır; P2). Sızıntı adları F3 metniyle birebir (betik BEKL).
- **A (seçilen):** aşağıdaki blok — liste 1–6, "which surprised you most?".
- B (elendi): "Will your generation inherit more or less than it expects?" — kişisel finans tahmini ister, tavsiye zincirine açılır (P1).
- C (elendi): "What's one thing you hope stays in the truck?" — duygusal ama ölüm/kayıp çağrışımı (P2), yanıtlaması zor.

<!-- veri:pinli-yorum -->
```text
Leo's inventory list has six leaks. Which one surprised you most? Reply with its number.

1: a long life
2: the cost of care
3: a spouse first
4: charity
5: the house
6: taxes and time

(Sources and notes are in the description. The Okafor family is an example, not a real household.)
```

---

## 8. Uç ekran, kart, oynatma listesi

- **Uç ekran:** kapanış köprüsü (ABONE-3 kartından sonra; H5), süre F8b'de gerçek sesten (son sahne `bas` → toplam; 5–20 sn). Öğeler: Abone + Video "Best for viewer". Var olmayan videoya söz yok (S04 "evler" yayında değil).
- **Kart:** S04 yayınlanınca "the house" bölümüne kart (H7 seri devamı). Şimdilik yok.
- **Oynatma listesi:** **C · Gelecek → "What If…? Future of Money Scenarios"**: bu video listeyi açar (boş liste yok) → F11'de koordinatör `tools/yayin/kanal.py`, sonra `oynatma_listesi_id`. Shorts → "Money Stories in 60 Seconds | Shorts".

---

## 9. Takvim ve durum alanları

ABD kış saati (EST, UTC−5). Uzun Paz 2026-11-08 12:00 ET = 17:00 UTC = 20:00 TRT; Pazar videosunun Shorts'u Pzt + Sal 09:00 ET (14:00 UTC; takvim v2). K3 kaçarsa (senaryo-karari §5) koordinatör `yedek` satırlarını üste taşır, `paket-uret.py` yeniden koşar: Çar 11-11 12:00 + Per 11-12 / Cmt 11-14 09:00 ET.

<!-- veri:yayin-zamani -->
```text
uzun|2026-11-08T12:00:00-05:00
shorts-1|2026-11-09T09:00:00-05:00
shorts-2|2026-11-10T09:00:00-05:00
yedek-uzun|2026-11-11T12:00:00-05:00
yedek-shorts-1|2026-11-12T09:00:00-05:00
yedek-shorts-2|2026-11-14T09:00:00-05:00
```

- **`durum.sentetik_medya`:** karar monetizasyon-uyum-uzmani'nin (`09-paket/politika-raporu.md`, F8). Henüz yok → geçici **true** (1929 ve S08 emsali); karar gelince `paket-uret.py` `SENTETIK` sabiti güncellenir, betik karşılaştırır. AI ses satırı her durumda açıklamada.
- **`gizlilik` = private + `yayin_zamani`**, `onay.niyazi_onayi` = false (üç pakette).
- **Dosyalar:** `../08-kurgu/final-16x9.mp4`, `../08-kurgu/final.en.srt`, `../08-kurgu/shorts-{1,2}.mp4` (S08 adlandırması, varsayım; F8b'de `ls 08-kurgu` ile teyit).

## 10. Test kapısı
`python3 -I paket-uret.py` → `python3 -I paket-kontrol.py` (taslak kipi; F8b `--final`) → `tools/yayin/yukle.py --dry-run` iki kipte (gerçek: yalnız dosya-yok; sahte medyalı bayt-aynı kopya: 0 hata). Çıktı: `kapi-cikti.txt`.

## 11. Açık işler
| İş | Sahibi | Not |
|---|---|---|
| Bölüm adları (metin §4), yasal not + `{KAYNAK_F3}` (rakam-tablosu), sızıntı adları (pinli yorum), Shorts metinleri | senaryo-yazari / finans-dogrulayici (F3) → paketleyici F8a | betik BEKL → birebir |
| D4 (%47/%55) teyidi → Shorts 2 asıl/yedek | finans-dogrulayici | düşerse yedek bloklar |
| Thumbnail finalisti → `veri:thumbnail-ana` | thumbnail-tasarimcisi | konsept H8 |
| Müzik atfı | muzik-ses-tasarimcisi | `06-muzik/atif-satirlari.md` |
| `sentetik_medya` | monetizasyon-uyum-uzmani | `politika-raporu.md` |
| `ilgili_video` alanı SEMA + YAYIN çıktısı | uretim-muhendisi | `talep-uretim-muhendisi.md` |
| Gerçek sahne zamanları, F7 dosyaları, uç ekran süresi, SRT terim taraması | F8b paketleyici | `--final` |
| Related video, uç ekran, SRT, Test & Compare, sabit yorum | koordinatör → Niyazi (Studio) | `YAYIN.md` (F8b) |
| Kanal: "What If…" liste açıklamasındaki "New episodes every other Sunday" gün sözü, tempo 4 hafta tutulmadan yazılmaz kuralıyla çelişiyor | koordinatör (kanal paketi) | liste açılmadan önce düzeltilmeli |
