# F2 ön doğrulama — 12 senaryo risk taraması (finans-dogrulayici) · 2026-11-02

İLERLEME: tamam (12 senaryo puanlandı; [doğrulanacak] maddeler çözüldü; Fed 28 Eki kararı eklendi; ilk 5 için rakam tablosu taslağı §4).
**Özet:** YEŞİL 3 (S01, S06, S08) · SARI 7 (S02, S04, S05, S07, S09, S10, S11) · KIRMIZI 2 (S03 çıkar çatışması; S12 bayat rakam + şiddet).
**Hook'ta yanlış çıkan 4 rakam/ifade (F3'ten önce düzeltilmeli):** S06 "This October… first time" → ilk %5 üstü kapanış **16 Eyl 2026** (FRED DGS10 5,01) · S05 H2 "21/23 in the months that followed" → pencere seçimden **1 ay önce–2 ay sonra** (Deutsche Bank) · S11 "rupee lost about six percent" → **~%5** (dolar/rupi +%5,3) · S12 "Brent about 115" → Ekim'de **115–135 $** arası, 27 Eki 123,10 $.
**Fed 28 Eki 2026 (doğrulandı, birincil):** hedef aralık **%3,75–4,00 sabit**, oy **10–2**; Lisa D. Cook ve Beth M. Hammack 25 bp **artış** istedi. Önceki adım: 16 Eyl 2026 +25 bp (12–0). Piyasa Aralık artışını fiyatlıyor (CME FedWatch ~%85 [AÖ]). Kaynak: federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm + FRED `DFEDTARU` (4,00, 28 Eki–1 Kas).
**Ağ:** FRED fredgraph.csv, Treasury Fiscal Data API, federalreserve.gov ve Yale/Shiller açık → çoğu rakam **birincil veriden betikle** yeniden üretildi. Betik/veri: scratchpad (`fred/*.csv`, `mts1.json`, `mts9.json`, `shiller/ie_data.xls`); komutlar §5.
**Karar bu dosyada verilmez** (hakem). Etiketler: [B] birincil veri · [2K] ≥2 bağımsız kaynak · [1K] tek kaynak zinciri · [AÖ] arama özeti · [H] hesap · [T] tahmin.

## 1. Senaryo risk tablosu
| ID | Ana rakamlar doğrulanabilir mi | Tavsiye riski | Karalama riski | Bayatlama | Durum | Koşul / düzeltme |
|---|---|---|---|---|---|---|
| S01 Çin AI | 480 milyar $ + ~%40 [2K: Reuters aktarımı; Futurism, TT, NewsBytes, FourWeekMBA]; %42/%57 Goldman [1K: Reuters]; F/K 250→100 [1K: TT], "~100x" [2K] | düşük (üç olasılık) | düşük (Unitree −%50 olgu; CoreWeave yalnız "termometre") | orta: ABD tarafı 28–30 Eki bilançolarıyla güncellenmeli | **YEŞİL** | "top tech stocks" → "China's STAR Fifty tech index" (480 milyar $ endeksin kaybı, tüm AI hisseleri değil). Zirve Temmuz/Haziran kaynaklara göre değişiyor → "since this summer". F/K 250 tek zincir → "at one point" + ekranda "Reuters". %57 hacim tek zincir → "Goldman Sachs estimates". |
| S02 AI borcu | ~%15 getiri [2K: Barron's 15,06 %, Crypto Briefing, Fool]; "9,675 %" **ihraç getirisi**, kupon değil (kuponlar %9,625 / %9,75 — SEC 8-K) | düşük | **orta**: tek şirket tahvili hikâyenin omurgası | orta | **SARI** | "kupon 9,675 sabit" yanlış → "sold at a yield of about nine point seven". Karşı kanıt şart: genel ABD yüksek getirili spread **%3,26** (29 Eki, FRED `BAMLH0A0HYM2`) — piyasa geneli sakin, CoreWeave aykırı. FRED bu seriyi yalnız **2023-10-31'den** veriyor → "2000 telekom" grafiği bu seriden çizilemez. Ives %5–10 = görüş, olgu değil. |
| S03 Anthropic S-1 | [1K: Fortune] | **yüksek** (halka arz öncesi) | **yüksek** (metni Anthropic modeli yazıyor → tarafsızlık şüphesi) | düşük | **KIRMIZI** | Seçilmemeli. Seçilirse açıklamada çıkar beyanı + dış doğrulayıcı gerekir (monetizasyon/hakem). |
| S04 Gümrük iadesi | ~130 milyar $ [1K: MTN←Bloomberg]; MTS FY2026 net gümrük geliri **173,2 milyar $** (FY2025 194,9) [B] | düşük | düşük-orta (Costco/FedEx davaları "iddia" diye) | düşük | **SARI** | CBP/mahkeme birincil kaynağı F3'te şart. Davalar "lawsuits allege" dili; sonuç yok. Siyasi denge. |
| S05 Ara seçim | 21/23 **yanlış pencere** [Money.com←Deutsche Bank: "one month before… to two months after"]; Shiller: 1950–2018 midterm Kas→Kas ort. fiyat **17/18 pozitif** (1986 ≈ %0,0) [B,H]; günlük kapanışla 1950'den beri hiç negatif değil [AÖ: Fool] | **orta-yüksek** (geçmiş getiri = "al" sinyali gibi okunabilir) | orta (siyasi) | **yüksek**: seçim 3 Kas, sonuç F7'de | **SARI** | H2'yi kullanma veya: "Since 1950, the S&P 500 was higher a year after almost every midterm. Past results don't predict this one." Her tarih grafiğinde "price only, not a forecast". Parti adı/renk yok. |
| S06 %5 tahvil → mortgage | Tamamı FRED [B]: DGS10 ilk ≥%5 kapanış 15–16 Eyl 2026; zirve **%5,31 (5 Eki)**; 1 Eki **%5,24** (senaryo "5,3" → "about five point two"); 22 Eki 4,96; önceki ≥%5: **Tem 2007**; tüm zaman zirve %15,84 (30 Eyl 1981). Mortgage 7,40 (8 ve 15 Eki 2026) / 6,27 (16 Eki 2025) [B: Freddie Mac], taksit [H] ✓ | düşük ("lock now" yok) | yok | düşük-orta (seviye oynak; kavram kalıcı) | **YEŞİL** | Hook: "This October" → **"This fall"** (veya "In September"). Köprü "the Fed can cut and your rate can still go up" → Fed şu an **artırıyor**; örnek olarak doğrulanmış 2024 vakası: Fed 18 Eyl 2024 indirdi, DGS10 3,65 → **4,79 (13 Oca 2025)** [B]. Spread şimdi ~2,3 puan vs 2000–19 ort. 1,76 [B,H]. |
| S07 Konut | NAR [B, tek yayıncı] (bu turda yeniden okunmadı) | orta ("wait/buy" çağrışımı) | yok | düşük | **SARI** | Doygunluk; medyan karışım etkisi [T] olarak etiketli kalmalı. |
| S08 Bütçe = hane | MTS FY2026 [B]: gelir **5.403,3**, gider **7.395,8**, açık **1.992,5** milyar $ → hane 5.400 / **~7.390** $ [H] ✓ | düşük | orta (siyasi suçlama riski) | düşük | **YEŞİL** | `GFDEGDQ188S` **1966'da başlıyor** → "1946 sonrası düşüş" için başka seri (OMB Historical Table 7.1) gerekir. `A091RC1Q027SBEA` = BEA faiz **ödemeleri** (Q3 2026 SAAR 1.328,8 milyar) ≠ MTS **net faiz** (1.051,8) → aynı ekranda karıştırma. |
| S09 Volcker | Fed funds "record 20 percent in late 1980" [FRH]; aylık zirve %19,1 (Haz 1981), günlük %22,36 (22 Tem 1981) [B FRED]; prime %21,5 [Wiki←NBER]; CPI 1979 Ara/Ara **%13,3**, yıllık ort. ~%11,3 [B,H]; işsizlik %10,8 (Kas 1982) [B+FRH]. Traktör: FRH "Farmers protested at the Fed's headquarters" + Shull (2005) "tractors… blockading the Eccles Building" [2K, **tarih yok**] | düşük | orta (gerçek kişi; yargı izleyicide) | düşük | **SARI** | "Farmers drove tractors to his door" → **"Farmers drove tractors to the Fed's headquarters"** (Şubat 1979 traktör yürüyüşü Volcker'dan önce; tarihi bağlama). "more than eleven percent" yıllık ortalama olarak doğru; "twenty percent" → "about twenty percent". |
| S10 1 T$ tatil | NRF tahmini [1K] | düşük | yok | orta (4 Kas için erken) | **SARI** | Tahmin olduğu sesli söylenmeli ("expected"); reel hesap CPI ile betikle. |
| S11 Rupi 100 | DEXINUS 2 Oca 90,19 → 23 Eki 94,94 [B] = dolar +%5,3 / rupi **−%5,0** [H]; 14 Eki 95,15 [B] ✓ | düşük (döviz tahmini yok) | düşük | orta | **SARI** | "about six percent" → **"about five percent"**. 70 milyar $ rezerv harcaması türetilmiş [AÖ] → kullanılmaz. |
| S12 115 $ petrol | Brent [B FRED]: 1 Eki 114,82; 2 Eki **135,51**; 22–27 Eki 125–128 → hook rakamı bayat/yanlış; benzin 4,269 $ (26 Eki) [B] | düşük | düşük | **çok yüksek** | **KIRMIZI** | Saldırı/ölüm hassas + rakam günde ±%5 oynuyor. Seçilirse yalnız yayın günü rakamı. |

## 2. Tavsiye dili ve karalama — ortak yeniden yazımlar (senaryo-yazari seçer)
| Riskli kalıp | Güvenli A | Güvenli B | Güvenli C |
|---|---|---|---|
| "So which number should you watch?" (S02) | "So which number do analysts watch?" | "Here's the number that tells the story." | "One number explains most of this." |
| "what happens to your money now" (S05 başlık) | "What Happens Next? Markets After the Midterms" | "What Stocks Did After Past Midterms" | (aynı başlık + ilk 30 sn'de "not advice, just history") |
| CoreWeave "is in trouble / will fail" türevi | "its bonds are pricing in more risk" | "lenders now demand about fifteen percent" | "one company's bonds, used as a thermometer" |
| "Is America next?" (S01) | soru olarak kalabilir; sonuç "three possibilities", tarih/oran vaadi yok | — | — |
**Yasal not (açıklama, her senaryo):** "This video is for education and entertainment only and is not financial, investment, tax or legal advice. Leo is a fictional character. Figures are from the sources listed below as of [date]; past performance does not predict future results. Narration voice is AI-generated."

## 3. Çözülen [doğrulanacak] maddeleri
| Madde | Sonuç | Kaynak |
|---|---|---|
| S05 21/23 | Rakam var ama pencere 3 aylık (seçim −1 ay → +2 ay), "stock market", Deutsche Bank. "Months that followed" **yanlış** | money.com/midterm-elections-stock-market-2026 (verbatim) |
| S09 %20 | Doğru (yaklaşık): FRH "record high of 20 percent in late 1980"; aylık %19,1 | FRH anti-inflation-measures; FRED FEDFUNDS/DFF |
| S09 traktör | Olay var (Shull 2005, Wikipedia; FRH "farmers protested at the Fed"), tarih belirsiz | yukarıda |
| S08 bütçe kalemleri | Sosyal Güvenlik 1.667,1 · Medicare 1.072,6 · Sağlık 1.025,6 · **Net faiz 1.051,8** · Savunma 965,2 milyar $ (FY2026). Net faiz > savunma ✓ | Fiscal Data MTS Table 9, 2026-09-30 |
| S08 borç | Toplam 40,17 T$ / halkın elindeki 32,43 T$ (30 Eyl 2026) | Debt to the Penny API |
| FRED kodları | 14 kodun hepsi indirildi ve güncel (DGS10, MORTGAGE30US, DFF, DFEDTARU, BAMLH0A0HYM2*, A091RC1Q027SBEA*, GFDEGDQ188S*, SP500*, CPIAUCSL, FEDFUNDS, UNRATE, DEXINUS, DCOILBRENTEU, GASREGW). *Sınırlar: HY spread 2023+, GFDEGDQ 1966+, SP500 yalnız son 10 yıl (2016-10-31+) → uzun seri Shiller | fredgraph.csv |
| Big Tech capex 700 milyar $+ | [2K arama özeti: Sherwood, Yahoo; aralık 700–745]. 28–30 Eki bilançoları sonrası F3'te şirket bazında yeniden ara | AÖ |

## 4. İlk 5 için rakam tablosu taslağı (F3 `03-metin/rakam-tablosu.md` buradan kopyalanır)
Sütunlar: değer | birim | tarih | birincil kaynak | güvenli yazım | ekran/sesli.

**S01**
| Değer | Birim | Tarih | Kaynak | Güvenli yazım | Ekran / sesli |
|---|---|---|---|---|---|
| ~480 | milyar $ piyasa değeri kaybı, STAR 50 | Tem→26 Eki 2026 | Reuters (TT, Futurism aktarımı) [2K] | "China's STAR Fifty tech index lost about $480 billion in value" | $480B / "about four hundred eighty billion dollars" |
| ~40 | % düşüş | aynı | aynı [2K] | "fell about forty percent since this summer" | −40% / "about forty percent" |
| ~250 → ~100 | F/K (kat) | zirve → Eki 2026 | Reuters←TT [1K: 250]; [2K: ~100] | "at one point about 250 times profits; now about 100" | 250x→100x |
| ~30 | Nasdaq 100 F/K | Eki 2026 | TT [1K] | "about thirty times" — F3'te 2. kaynak yoksa düşür | 30x |
| 42 / 57 | % (piyasa değeri / işlem hacmi; A+H hisseleri) | Eki 2026 | Goldman Sachs, Reuters aktarımı [1K] | "Goldman Sachs estimates…" | 42% / 57% + "Goldman Sachs est." |
| ~50 | % Unitree halka arzdan beri düşüş | Eki 2026 | TT [1K] | F3'te borsa verisiyle teyit; yoksa çıkar | — |
| >700 | milyar $ 2026 capex (4 şirket) | Eki 2026 | Sherwood, Yahoo [2K AÖ] → bilanço sonrası güncelle | "more than seven hundred billion dollars" | $700B+ |
| ~15 | % CoreWeave 2032 tahvil getirisi (gün içi) | 13 Eki 2026 | Barron's/Crypto Briefing/Fool [2K] | "lenders demanded about fifteen percent" | ~15% |

**S06**
| Değer | Birim | Tarih | Kaynak | Güvenli yazım | Ekran / sesli |
|---|---|---|---|---|---|
| 5,01 | % 10 yıllık getiri (kapanış) — ilk ≥5 | 16 Eyl 2026 | FRED DGS10 [B] | "this fall it went above five percent" | 5% |
| 5,31 | % zirve | 5 Eki 2026 | FRED [B] | "peaked around five point three" | 5.3% |
| 4,98 | % | 29 Eki 2026 | FRED [B] | "back near five percent" (yayın günü güncelle) | ~5% |
| Tem 2007 | önceki ≥%5 | 19 Tem 2007 (5,04) | FRED [B] | "first time since 2007" / "almost twenty years" | 2007 |
| 15,84 | % tüm zaman zirvesi | 30 Eyl 1981 | FRED [B] | "nearly sixteen percent in 1981" | 15.8% |
| 7,40 / 6,27 | % 30 yıllık sabit mortgage (Freddie Mac PMMS) | 15 Eki 2026 / 16 Eki 2025 | FRED MORTGAGE30US [B] | "about seven point four vs six point three a year earlier" | 7.4% / 6.27% |
| 2.077 / 1.851 / 226 | $/ay anapara+faiz, 300 bin $, 30 yıl | aynı | [H] (NAR ile aynı) | "about $226 more a month, before taxes and insurance" | +$226/mo |
| ~2,3 | puan mortgage–10y farkı (ort. 2000–19: 1,76) | 29 Eki 2026 | FRED [B,H] | "the gap is wider than usual" | 2.3 pts |
| 3,75–4,00 | % Fed hedef aralığı; 28 Eki sabit (10–2), 16 Eyl +0,25 | 28 Eki 2026 | federalreserve.gov [B] | "the Fed held its rate at 3.75 to 4 percent" | 3.75–4% |
| 3,65 → 4,79 | % DGS10, Fed indirim sonrası | 17 Eyl 2024 → 13 Oca 2025 | FRED [B] | "in 2024 the Fed cut, and the ten-year rose by more than one point" | — |

**S02** (S01 tablosundaki CoreWeave + capex satırları geçerli, ek:)
| Değer | Birim | Tarih | Kaynak | Güvenli yazım | Ekran / sesli |
|---|---|---|---|---|---|
| ~9,7 | % **ihraç getirisi** (kupon değil) | Haz 2026 | TradingNews + stock3 [2K] | "sold at a yield of about nine point seven percent" | ~9.7% |
| 9,625 / 9,75 | % kuponlar (2032 / 2031 notları) | — | SEC 8-K (9,75) [B]; 9,625 [AÖ] | ekranda yalnız gerekirse | — |
| 3,26 | % ABD HY OAS (piyasa geneli) | 29 Eki 2026 | FRED BAMLH0A0HYM2 [B] | "the overall junk-bond market is still calm" | 3.3% |
| 5–10 | % gerçekleşmeyebilecek proje (Ives görüşü) | Eki 2026 | Yahoo [1K, görüş] | "one analyst guesses…" | ekranda "opinion" |

**S05**
| Değer | Birim | Tarih | Kaynak | Güvenli yazım | Ekran / sesli |
|---|---|---|---|---|---|
| 21/23 | ara seçim dönemi, piyasa yükselişi, **seçim −1 ay → +2 ay** | 2026 öncesi | Deutsche Bank (Money.com) [1K] | yalnız pencereyle birlikte veya hiç | ekranda pencere notu |
| 17/18 | 12 ay sonra S&P fiyatı yüksek (Kas ort.→Kas ort.) | 1950–2018 | Shiller ie_data [B,H] (1986 ≈ 0) | "almost every midterm since 1950" | "price only" |
| 3,75–4,00 / Aralık | Fed aralığı; sonraki toplantı 8–9 Ara [AÖ: tarih kaynaklara göre 9 Ara] | 28 Eki 2026 | federalreserve.gov [B] | "next Fed meeting in December" | — |
| 1,99 | trilyon $ FY2026 açık | 30 Eyl 2026 | MTS [B] | "about two trillion dollars" | $2T |

**S08**
| Değer | Birim | Tarih | Kaynak | Güvenli yazım | Ekran / sesli |
|---|---|---|---|---|---|
| 5.403,3 / 7.395,8 / 1.992,5 | milyar $ gelir / gider / açık | FY2026 (Eki 2025–Eyl 2026) | MTS Table 1 [B] | "about 5.4 trillion in, 7.4 trillion out" | $5.4T / $7.4T |
| 5.400 / ~7.390 / ~1.990 | $/ay hane ölçeği | aynı | [H] ölçek 1 $ = 1 milyar $/12 ay | "If its income were $5,400 a month…" + ekranda ölçek notu | $5,400 / $7,400 |
| 1.051,8 | milyar $ net faiz (= hanede ~1.050 $/ay; gelirin %19,5'i) | FY2026 | MTS Table 9 [B,H] | "about one in every five dollars it brings in" | $1,050/mo |
| 965,2 / 1.667,1 / 1.072,6 / 1.025,6 | milyar $ savunma / Sos. Güv. / Medicare / Sağlık | FY2026 | MTS Table 9 [B] | "interest now costs more than defense" | — |
| 40,17 / 32,43 | trilyon $ toplam / halkın elindeki borç | 30 Eyl 2026 | Debt to the Penny [B] | hane: ~482 bin $ (toplam) veya ~389 bin $ (halk); hangisi seçilirse etiketle | "$482K card balance" |
| 121,2 | % borç/GSYH (toplam kamu borcu) | Q2 2026 | FRED GFDEGDQ188S [B] (1966+) | "about 121 percent of the economy" | 121% |

## 5. Test kapısı ve kanıt
- FRED: `curl fredgraph.csv?id=<14 kod>` → hepsi HTTP 200; analiz `python3` (scratchpad `fred/`), DGS10 sha256 F3'te raporlanır.
- MTS: `curl -g api.fiscaldata.treasury.gov/.../mts_table_1|9?filter=record_date:eq:2026-09-30` → Year-to-Date 5.403.326.758.960 / 7.395.799.983.313 / 1.992.473.224.352.
- Midterm: `xlrd` Shiller ie_data.xls (son satır 2023.09) → 1950–2018 17/18.
- Taksit: standart annüite formülü → 2.077 / 1.851 / fark 226.
- Kapı: §4'teki her rakamın birimi + tarihi + kaynağı var; [1K] satırlar F3'te 2. kaynak yoksa metinden çıkar.
