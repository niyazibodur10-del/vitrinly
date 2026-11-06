# F3 rakam tablosu — S08 "If America Earned $5,400 a Month" (finans-dogrulayici) · 2026-11-02

İLERLEME: tamam (tablo kilitli; metin gelince F3 doğrulaması = tablo farkı + `[RAKAM?]` + tavsiye dili taraması).
**Kural:** Metin YALNIZ bu tablodaki rakamları, "Güvenli yazım" sütunundaki biçimde kullanır. Tabloda olmayan rakam → `[RAKAM?]` yaz, uydurma.
**Kapsam ve seçimler (karar):** (1) Bütçe yılı her yerde **FY2026 = Oct 2025–Sep 2026**, kaynak **Monthly Treasury Statement (MTS)**. (2) **D5 → halkın elindeki borç (debt held by the public) seçildi** (gerekçe §4). Toplam borç 40,17 T$ metne girmez. (3) **D3 → faiz = MTS net faiz 1.051,8 milyar $**. BEA 1.328,8 ve "brüt faiz ~1,4 T$" metne girmez.
**Ölçek (D1):** federal **milyar $/yıl = hane $/ay**. Ekranda tek satır: **"Scale: $1 a month here = $1 billion a year for the US government."** Stok (borç) için ölçek sesli anlatılmaz, **"years of income"** ile verilir (§4).
**Etiketler:** [B] birincil veri (betikle üretildi) · [2K] ≥2 bağımsız kaynak · [1K] tek kaynak · [AÖ] arama özeti · [H] hesap · [T] tahmin. Kanıt: `python3 -I veri/hesap.py` → `veri/hesap-cikti.txt` (betik sha256 81a3e21f6701, çıktı 3c78b936e560, mts9.json 535ca6d506ad, debt_to_penny.json c37b9e273277). Ham veri yeniden: `veri/indir.sh`.

## 1. Bütçe (FY2026, MTS Table 9 / Table 1, 30 Eyl 2026 kaydı)
| # | Değer | Birim | Tarih | Birincil kaynak | Durum | Güvenli yazım (sesli) | Ekran |
|---|---|---|---|---|---|---|---|
| R01 | 5.403,3 | milyar $ gelir | FY2026 | MTS T9 [B]; CBO/AAF ">5,4 T$" [2K] | doğrulandı | "brings home five thousand four hundred dollars a month" / "about 5.4 trillion dollars a year" | $5,400/mo · $5.4T |
| R02 | 7.395,8 | milyar $ gider | FY2026 | MTS T9 [B]; AAF "nearly 7,4 T$" [2K] | doğrulandı | "spends **about** seven thousand four hundred" ("about" zorunlu) / "nearly 7.4 trillion" | ~$7,400/mo · $7.4T |
| R03 | 1.992,5 | milyar $ açık | FY2026 | MTS [B]; CBO 1,993 T$, AAF 2,0 T$ [2K] | doğrulandı | "about two thousand dollars short every month" / "almost two trillion dollars" | −$2,000/MO · $2T |
| R04 | 1,369 | gider/gelir oranı | FY2026 | [H] R02/R01 | doğrulandı | "for every five dollars in, nearly seven go out" (**6,84**; "$7 for every $5" = yuvarlama, sesli "nearly") | $5 in → ~$7 out |
| R05 | %26,9 | açık/gider | FY2026 | [H] | doğrulandı | "about a quarter of everything it spends is borrowed" | ~1/4 |
| R06 | 1.051,8 | milyar $ **net faiz** | FY2026 | MTS T9 [B]; AAF/Fox "≈1 T$+" [2K] | doğrulandı | "its interest bill: about one thousand fifty dollars a month" / "over a trillion dollars a year" | $1,050/mo |
| R07 | %19,5 (1/5,14) | net faiz / gelir | FY2026 | [H] | doğrulandı | "about one in every five dollars it brings in" | 1 in 5 |
| R08 | 965,2 | milyar $ savunma (National Defense) | FY2026 | MTS T9 [B] | doğrulandı | "interest now costs more than the entire military" — tercihen "more than defense" ($965/mo) | $965/mo |
| R09 | 1.667,1 | milyar $ Sosyal Güvenlik | FY2026 | MTS T9 [B] | doğrulandı | "Social Security: about one thousand six hundred seventy a month" — biggest bill | $1,667/mo |
| R10 | 1.072,6 | milyar $ Medicare | FY2026 | MTS T9 [B] | doğrulandı | "Medicare: about one thousand seventy" | $1,073/mo |
| R11 | 1.025,6 | milyar $ Health (Medicaid dahil, Medicare hariç) | FY2026 | MTS T9 [B] | doğrulandı | "other health programs, mostly Medicaid: about one thousand twenty-five" ("mostly Medicaid" [T]: fonksiyon tanımı; yoksa "other health programs") | $1,026/mo |
| R12 | 3. sıra | net faiz, fonksiyon bazında (SS > Medicare > **net faiz** > Health > savunma) | FY2026 | [H] R06–R11 | doğrulandı | "interest is now the third-biggest bill, after Social Security and Medicare" | sıralı çubuk |
| R13 | 694,2 / 416,2 | milyar $ Income Security / Veterans | FY2026 | MTS T9 [B] | doğrulandı | gerekirse "$694" / "$416" a month | — |
| R14 | 2.845,5 / 1.754,3 / 381,4 / 173,2 | milyar $ gelir: bireysel gelir vergisi / bordro (SS+Medicare) vergisi / kurumlar vergisi / gümrük | FY2026 | MTS T9 [B] | doğrulandı | "about $2,850 from income tax, $1,750 from payroll taxes, $380 from companies, $170 from tariffs" (gümrük konusu siyasi → yalnız rakam, yorum yok) | gelir zarfları |
| R15 | 5.234,6 / 7.010,0 / 1.775,4 | milyar $ FY2025 gelir/gider/açık | FY2025 | MTS T9 prior FYTD [B] | doğrulandı | "a year earlier the gap was about $1,775 a month" | — |
| R16 | +%8,4 | net faiz yıllık artış (970,4 → 1.051,8) | FY25→FY26 | MTS [B,H]. **CBO %11** (zamanlama düzeltmeli) — çelişki | doğrulandı (MTS ölçüsüyle) | "up about eight percent in a year". Kaynak çelişkisi yüzünden tercihen yüzde vermeden "and it's still growing" | — |
| R17 | ~6,2 | % açık / GSYH | FY2026 | [H] MTS açık / BEA GSYH (Q4'25–Q3'26 SAAR ort. 32,24 T$, FRED GDP) | **tahmin** [H] | yalnız "about six percent of the whole economy" + ekranda "est." | "~6% of GDP (est.)" |

## 2. Faiz faturasının tarihi (D3, grafik 2 — MTS net faiz, mali yıl)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R18 | 240,7 · 262,8 · 324,7 · 375,6 · 344,7 · 352,3 · 475,1 · 659,2 · 881,7 · 970,4 · 1.051,8 | milyar $ net faiz | FY2016…FY2026 | MTS T9 her 30 Eyl [B] | doğrulandı | grafik başlığı: "US net interest, fiscal years 2016–2026 (Monthly Treasury Statement)" | çizgi/çubuk |
| R19 | ×2,99 | net faiz FY2021 (352,3) → FY2026 | 5 yıl | [H] | doğrulandı | "the interest bill roughly **tripled in five years**" (hane: $352 → $1,052/mo) | $352 → $1,052 |
| R20 | %8,7 → %19,5 | net faiz / gelir | FY2021 → FY2026 | [H] MTS | doğrulandı | "from under one in ten dollars to about one in five" | — |
| R21 | FY2024 | net faiz savunmayı ilk geçtiği yıl (881,7 > 874,0; MTS fonksiyon bazında, FY2016+ penceresi) | FY2024 | MTS [B]; "now exceeds defense" [2K] | doğrulandı (MTS ölçüsü) | "since 2024, interest has cost more than defense" — "first time ever" **deme** (pencere FY2016+) | — |

## 3. Faiz neden büyüyor (D6) — yalnız mekanizma + bu rakamlar
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R22 | 1,424 → 3,518 | % ortalama faiz, **pazarlanabilir** Hazine borcu (Total Marketable) | Oca 2022 (dip) → Eyl 2026 | Treasury "Average Interest Rates on U.S. Treasury Securities" [B] | doğrulandı | "the average rate on its debt went from about one and a half percent in early 2022 to about three and a half today" ("today" yerine "by September 2026" — H7 kayma kuralı) | 1.4% → 3.5% |
| R23 | 4,98 | % 10 yıllık Hazine getirisi | 29 Eki 2026 | FRED DGS10 [B] | doğrulandı (seviye oynak) | "new ten-year borrowing costs **close to five percent**" (tarihli: "in late October") | ~5% (Oct 2026) |
| R24 | 4,00 | % 3 aylık bono (DTB3) | 29 Eki 2026 | FRED [B] | doğrulandı | "even short-term borrowing costs about four percent" | ~4% |
| R25 | %3,75–4,00 | Fed hedef aralığı, 28 Eki'de sabit | 28 Eki 2026 | federalreserve.gov + FRED DFEDTARU [B] | doğrulandı | yalnız gerekirse tek cümle: "the Fed's rate is between 3.75 and 4 percent" | — |
| R26 | ~71 | ay, pazarlanabilir borcun ortalama vadesi | Haz 2026 | JEC Monthly Debt Update [1K, AÖ] | **doğrulanamadı (tek kaynak)** | rakamsız kullan: "its debt doesn't come due all at once; old loans roll over a few at a time" | — |
| R27 | ~%22 | bonoların pazarlanabilir borç içindeki payı | 31 Tem 2026 | Treasury refunding aktarımı [AÖ] | **doğrulanamadı** | metne girmez | — |
| — | Mekanizma | eski düşük faizli borç vadesinde yüksek faizle yenilenir → ortalama faiz yükselir → fatura büyür | — | [T] mekanizma, R22 ile desteklenir | — | "every time an old cheap loan comes due, it's replaced with a more expensive one" | — |

## 4. Borç — D5 kararı: halkın elindeki borç
**Adaylar:** A) halkın elindeki 32,43 T$ · B) toplam 40,17 T$ · C) ikisi ayrı etiketli. **Seçilen A.** (1) Net faiz (R06) büyük ölçüde halkın elindeki borca ödenir; toplam borcun ~7,75 T$'lık kısmı devletin kendi fonlarına borcu (faiz hükümetin içinde döner) → A faizle aynı elma. (2) 1946 tarihi (R33) OMB'de aynı seriyle (held by the public). (3) Sonuç "6 yıllık gelir" gibi temiz. B elendi: faizle tutarsız ölçü; C elendi: D5 karıştırmayı yasaklıyor, iki rakam izleyiciyi yorar.
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R28 | 32,43 | trilyon $ halkın elindeki borç | 30 Eyl 2026 (FY sonu) | Debt to the Penny [B] | doğrulandı | "debt held by the public: about thirty-two trillion dollars" | $32.4T "debt held by the public, Sep 30 2026" |
| R29 | 6,00 | yıl (borç / yıllık gelir) | FY2026 | [H] R28/R01 | doğrulandı | "it owes about **six years** of its entire income" | 6 years of income |
| R30 | ~389.000 | $ hane ölçeğinde borç (yıllık hane geliri 64.840 $ × 6) | FY2026 | [H] | doğrulandı | "on a $5,400-a-month income, that's a balance of about three hundred ninety thousand dollars" | ~$389K |
| R31 | ~%3,2 | ima edilen ortalama maliyet (R06/R28) | FY2026 | [H] | doğrulandı (yaklaşık) | **"credit card" demeyin** — kart faizi ~%20+; bu ~%3. Analoji: "a giant loan" / "a mortgage-sized balance". "Card balance" kullanılırsa ekranda "but at about 3–3.5%, not card rates" zorunlu | — |
| R32 | 97,4 | % halkın elindeki borç / GSYH | Q2 2026 | FRED FYGFGDQ188S [B] | doğrulandı | "close to the size of the whole economy" / "about ninety-seven percent" | ~97% of GDP |
| R32b | 32,71 | trilyon $ halkın elindeki borç (son kayıt) | 29 Eki 2026 | Debt to the Penny [B] | doğrulandı | metinde kullanmayın (FY etiketi bozulur); yalnız açıklamada "as of" ile | — |
| ✗ | 40,17 / ~482.000 / %121,2 | toplam borç / hane / toplam borç-GSYH | 30 Eyl 2026 / Q2 2026 | Debt to the Penny, FRED GFDEGDQ188S [B] | doğru ama **seçilmedi** | metne girmez (D5) | — |

## 5. Üç olasılık ve tarih (D4, D7, P3)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R33 | %106,1 → %23,2 | halkın elindeki borç / GSYH (zirve → dip) | 1946 → 1974 | OMB Historical Table 7.1 (FY2025 Bütçesi) [B]. Not: GSYH payı baskıdan baskıya ±1–2 puan değişir (1940: 51,6 / 52,4 / 53,1) | doğrulandı | "after World War II, debt was bigger than the whole economy; by the mid-1970s it was under a quarter of it" (106,1'i ondalıklı söyleme) | ">100% (1946) → ~23% (1974), OMB" |
| R34 | 241,9 → 343,7 | milyar $ halkın elindeki borç (nominal) | 1946 → 1974 | OMB T7.1 [B] | doğrulandı | "the debt itself didn't shrink; it actually grew. The economy grew faster" | $242B → $344B |
| R35 | %18,1 / %8,8 | TÜFE Ara/Ara enflasyon | 1946 / 1947 | Shiller CPI (BLS CPI-U kaynaklı) [B,H]; BLS 1946 %18,1 ile aynı [2K] | doğrulandı | "prices jumped about eighteen percent in 1946 alone, quietly shrinking what the debt was worth" — enflasyon dalı **hiçbir varlığa bağlanmaz** (P3) | 1946: +18% prices |
| R36 | ~%3,5 | yıllık ort. enflasyon | Haz 1946 → Haz 1974 | Shiller CPI [B,H] | doğrulandı | gerekirse "about three and a half percent a year for nearly thirty years" | — |
| — | Default/"debt spiral" | — | — | [T] | — | yalnız "some economists worry it could…"; karşı kanıt: "it borrows in its own currency" + "its debt comes due over years, not all at once" (rakamsız, R26) | — |

## 6. Yasaklı / dikkat listesi (metin taramasında aranacak)
- "credit card" + faiz oranı birlikte (R31) · "first time ever" (R21) · "today/this week/just" (H7) · "7 for every 5" rakamın "nearly"siz kullanımı (R04) · toplam borç 40 T$ / 482K / %121 (D5) · BEA 1,33 T$ veya "1.4 trillion interest" (D3) · "default will/is coming", "you should / protect your money / buy gold" (D7, P3) · parti/başkan/aday adı (P1).
- **Yasal not (açıklama):** "This video is for education and entertainment only and is not financial, investment, tax or legal advice. Leo is a fictional character. Budget figures: U.S. Treasury Monthly Treasury Statement, fiscal year 2026 (Oct 2025–Sep 2026); debt: Treasury Debt to the Penny, Sep 30 2026; history: OMB Historical Table 7.1; rates: FRED. Scale: $1 a month = $1 billion a year. Narration voice is AI-generated."

## Kaynaklar
MTS: api.fiscaldata.treasury.gov (mts_table_1, mts_table_9) · Debt to the Penny ve Average Interest Rates: fiscaldata.treasury.gov · OMB T7.1: govinfo.gov/content/pkg/BUDGET-2025-TAB/xls/BUDGET-2025-TAB-8-1.xlsx · FRED: GDP, DGS10, DTB3, DFEDTARU, FYGFGDQ188S, GFDEGDQ188S · Shiller ie_data.xls (econ.yale.edu/~shiller) · İkinci kaynak (arama): CBO publication 61882, americanactionforum.org "U.S. Treasury FY 2026 Deficit Totaled $2 Trillion", foxbusiness.com · Vade: JEC Monthly Debt Update (Eki 2026) [AÖ].
