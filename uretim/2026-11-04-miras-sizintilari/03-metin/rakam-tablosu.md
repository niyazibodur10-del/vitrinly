# F3 rakam tablosu — S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It" (finans-dogrulayici) · 2026-11-04

İLERLEME: tamam (R01–R27 kilitli; metin gelince F3 doğrulaması = tablo farkı + `[RAKAM?]` + tavsiye dili taraması).
**Kural:** Metin YALNIZ bu tablodaki rakamları, "Güvenli yazım" sütunundaki biçimde kullanır. Tabloda olmayan rakam → `[RAKAM?]` yaz, uydurma.
**Kanıt:** `cd 03-metin/veri && python3 -I hesap.py` → `hesap-cikti.txt` (2 koşu aynı; betik fed3af698f41, kaynaklar.json dcac2f79e70d, çıktı 5a00bf2e4688; `SHA256.txt`). Çift sayım assert'leri: 105+18≈124 · 105+18+54>124 (54 ek kalem değil) · 124−54−18=52 YASAK. Ham DFA yeniden: `curl -sLO https://www.federalreserve.gov/releases/z1/dataviz/download/dfa-{generation-shares,generation-levels,networth-shares}.csv` (son güncelleme 18 Eyl 2026, veri 2026:Q2).
**Etiketler:** [B] birincil kaynak (kurum/şirket bülteni, resmi veri) · [2K] ≥2 bağımsız kaynak · [1K] tek kaynak · [AÖ] arama özeti · [H] hesap · [T] tahmin/yorum.

## 0. Tetik-2 kararı (hakem için): Cerulli 124 T$ BİRİNCİL KAYNAKTA DOĞRULANDI
Cerulli basın bülteni, **5 Aralık 2024, Boston** (cerulli.com/press-releases/cerulli-anticipates-124-trillion-in-wealth-will-transfer-through-2048), kelimesi kelimesine:
- "Cerulli projects that wealth transferred through 2048 will total $124 trillion—$105 trillion is expected to flow to heirs, while $18 trillion will go to charity."
- "Projections of horizontal, or intra-generational, transfers show that $54 trillion will be passed on to spouses **before eventually transferring intergenerationally to heirs and to charities**."
- "Nearly $40 trillion of these spousal transfers will be going to widowed women in the Baby Boomer and older generations…"
→ 54 T$ ayrı bir kayıp ya da ek tutar DEĞİL: aynı paranın varıştan önceki durağı (eşte bekleme). 105 + 18 = 123 ≈ 124 (yuvarlama). **Yedek senaryoya geçiş gerekmez.**
Not (D2 inceltmesi): bülten 54'ün 124'ün "içinde" olduğunu kelimeyle söylemiyor; söylediği, eşe giden paranın sonra mirasçıya/bağışa geçtiği. Bu yüzden metin "inside the 124" demez; "on the way, about 54 trillion stops at a surviving spouse first" der. 124'ten 54 **çıkarılmaz, eklenmez**.

## 1. Başlık rakamı ve kırılımı (Cerulli, Ara 2024) — KRİTİK
| # | Değer | Birim | Tarih/dönem | Birincil kaynak | Durum | Güvenli yazım (sesli) | Ekran |
|---|---|---|---|---|---|---|---|
| R01 | 124 | trilyon $ (ABD, nominal projeksiyon) | 2024 sonu → **2048** | Cerulli bülteni 5 Ara 2024 [B]; ThinkAdvisor 9 Ara 2024, NBC [2K] | doğrulandı | "about one hundred twenty-four trillion dollars is expected to pass down in America by twenty forty-eight, Cerulli Associates estimates" (BofA aktarırsa: "a figure cited by Bank of America"). **"Bank of America says" yasak.** "is changing hands" yerine "is expected to" (projeksiyon) | $124T · "Cerulli est., through 2048" |
| R02 | 105 | trilyon $ mirasçılara | → 2048 | Cerulli [B] | doğrulandı | "about one hundred five trillion is expected to reach heirs" | $105T → heirs |
| R03 | 18 | trilyon $ bağışa | → 2048 | Cerulli [B] | doğrulandı | "about eighteen trillion is expected to go to charity" — başlık rakamının mirasçıya gitmeyen kısmı olarak söylenebilir | $18T → charity |
| R04 | 54 | trilyon $ eşe (yatay/kuşak içi) | → 2048 | Cerulli [B] | doğrulandı | "about fifty-four trillion is expected to stop at a surviving spouse first, before it moves on" → **gecikme/durak, kayıp değil**. "leaks to the spouse", "minus 54" yasak | $54T: spouse first (detour) |
| R05 | ~40 | trilyon $ (R04'ün içinden) dul kadınlara, boomer ve daha yaşlı kuşak | → 2048 | Cerulli [B] | doğrulandı | "nearly forty trillion of that goes to widowed women" | ~$40T of $54T |
| R06 | ~100 / %81 | trilyon $ / toplamın payı; kaynağı boomer + daha yaşlı kuşak | → 2048 | Cerulli [B] | doğrulandı | "nearly a hundred trillion comes from baby boomers and older generations" | ~$100T · 81% |
| R07 | 62 / %2 | trilyon $ (toplamın >%50'si) / hanelerin payı; HNW+UHNW | → 2048 | Cerulli [B] | doğrulandı | "**about half** of it is expected to come from just two percent of households" (62/124 = tam %50,0 → "more than half" yazılmaz, hesap.py) | ~half ($62T) from 2% of households |
| R08 | 46 / 14 / 85 | trilyon $: Millennial (25 yıl) / Gen X (ilk 10 yıl) / Gen X + Millennial toplam | → 2048 / → ~2034 | Cerulli [B] | doğrulandı | gerekirse "millennials are expected to inherit the most, about forty-six trillion" | — |

## 2. Bağış sızıntısı (BofA Private Bank Study of Wealthy Americans 2026) — KRİTİK
| # | Değer | Birim | Tarih | Birincil kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R09 | %47 (2026) ← %55 (2024) | "yeni kuşak ailenin hayır işlerini üstlenmeye hazır" diyen varlıklı Amerikalı | anket 8 Oca–5 Şub 2026; bülten **30 Eyl 2026** | BofA/PRNewswire bülteni 30 Eyl 2026 (finviz kopyası) [B]; Fortune 6 Eki 2026 [2K] | doğrulandı | "in a Bank of America survey of wealthy Americans, forty-seven percent said the next generation is ready to take on the family's giving, down from fifty-five percent in twenty twenty-four". Örneklem nitelemesi zorunlu: "wealthy" = **≥3 M$ yatırılabilir varlık** (konut hariç), 1.431 kişi, Escalent. "Americans" diye genelleme yasak | 55% (2024) → 47% (2026) · "BofA survey, 1,431 people with $3M+ investable assets" |
| R10 | %65 ← %76 | "çocuklarım bağış taahhüdümü paylaşıyor" | 2026 / 2024 | aynı [B]; Fortune [2K] | doğrulandı | opsiyonel: "sixty-five percent, down from seventy-six" | — |
| R11 | %89 | 2025'te bağış yapan varlıklı Amerikalı | 2025 | BofA bülteni [B, AÖ özeti + Fortune yok → 1K] | doğrulandı (1K) | opsiyonel; kullanılırsa aynı örneklem nitelemesi | — |

## 3. Dunham "mirage" alıntısı (D6)
| # | Değer | Kaynak | Durum | Güvenli yazım |
|---|---|---|---|---|
| R12 | "Great Wealth Mirage" | InvestmentNews 5 Eki 2026: Salvatore M. Capizzi, EVP, Dunham & Associates Investment Counsel [1K; makale birincil kâğıda link vermiyor] | **kısmen** (alıntı ikincil, kâğıt bulunamadı) | Ad + şirket söylenmez (yatırım firması pazarlama metni; reklam algısı). Kullanılacaksa: "Some analysts have even called it a possible 'wealth mirage'" — ekranda kaynak "InvestmentNews, Oct 2026". Dunham kâğıdındaki rakamlar (1 M$ portföy 34. yılda biter vb.) **metne girmez** (tek ikincil kaynak, model varsayımlı) |

## 4. Sızıntı 1 — uzun yaşam (para yaşayarak harcanır)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R14 | ~20 (19,7 dönem / 20,5 kohort) | yıl, 65 yaşından sonra kalan ortalama ömür (ABD, tüm nüfus) | 2024 / 2021–25'te 65 olanlar | CDC "Mortality in the US, 2024" 19,7 [AÖ: CBS + HealthLeaders, 2K ikincil; cdc.gov ağdan kapalı] · ASPE Ağu 2022 brifi 20,5 (kohort projeksiyonu) [B] | doğrulandı (iki ölçü, biri seçilmez) | "a sixty-five-year-old today can expect, on average, about twenty more years" — 19,7 ya da 20,5 ondalığı yazılmaz | "~20 more years at 65 (avg.)" |

## 5. Sızıntı 2 — bakım (en büyük ve en az konuşulan)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R13 | 355 $/gün = **129.575 $/yıl** (≈10.800 $/ay) | huzurevi **özel oda**, ulusal **medyan** | 2025 verisi (Tem–Kas 2025), yayın 2 Mar 2026 | CareScout (Genworth) 2025 Cost of Care Survey bülteni [B]; BusinessWire + Skilled Nursing News [2K] | doğrulandı | "a private room in a US nursing home now has a median cost of about one hundred thirty thousand dollars a year" — "median" ve "US" zorunlu; "average" yasak | $129,575/yr · "US median, CareScout 2025" |
| R15 | 114.975 $/yıl (315 $/gün) · 74.400 $/yıl (6.200 $/ay) | yarı özel oda · assisted living, ulusal medyan | 2025 | CareScout [B] | doğrulandı | opsiyonel: "a shared room, about one hundred fifteen thousand; assisted living, about seventy-four thousand" | — |
| R16 | %56 · %22 | 65'e giren Amerikalıların ciddi LTSS (uzun süreli bakım) ihtiyacı yaşayacak payı · 5 yıldan uzun ihtiyaç | 2021–25 kohortu, ASPE Ağu 2022 (mikrosimülasyon) | ASPE (HHS) [B]. **Çelişki:** ACL/LongTermCare.gov "almost 70%" (= *herhangi* bir bakım, eski model) → metne girmez | doğrulandı (ASPE ölçüsü) | "US government researchers estimate that more than half of Americans turning sixty-five will at some point need serious long-term care" — **projeksiyon** dili ("estimate") zorunlu | "56% (HHS/ASPE est.)" |
| R17 | 120.900 $ ort. · %37 cepten · %14 ≥100.000 $ cepten | 65'teki kişi başı gelecek LTSS maliyeti (2020 $) | ASPE 2022 | ASPE [B] | doğrulandı | opsiyonel: "about one in seven could pay a hundred thousand dollars or more out of pocket" (2020 doları → "in today's money" denmez) | "14% pay $100K+ (est., 2020 $)" |
| R25 | Medicare uzun süreli **bakımı (custodial) karşılamaz** · Medicaid: 55+ yaşta bakım ödemeleri için devlet **mirastan geri tahsil etmek zorunda** | — | güncel | medicare.gov "Nursing home care" [B]; medicaid.gov "Estate recovery" [B] | doğrulandı | "Medicare generally doesn't pay for long-term custodial care. And if Medicaid pays, states are required to try to recover those costs from the estate later." — tavsiye değil mekanizma; "spend down / hide assets / gift it" yasak | — |

## 6. Sızıntı 5 — ev (≤90 sn, H7)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R23 | %41,3 · 20,5 T$ | boomer'ların ABD hane gayrimenkulündeki payı · tutar | 2026:Q2 | Fed DFA (hesap.py) [B] | doğrulandı | "baby boomers own about two-fifths of all the real estate held by American households" | "~41% of US household real estate (Fed, Q2 2026)" |
Ev satışı, bakım için ev satma, kardeşler arası bölüşme: **rakamsız** anlatılır (birincil kaynaklı oran yok).

## 7. Sızıntı 6 — vergi ve zaman
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R18 | 15.000.000 $ (2025: 13.990.000) | kişi başı federal emlak vergisi muafiyeti (basic exclusion) | **2026 ölümleri** | IRS haber bülteni 2026 enflasyon ayarlamaları [B]; KPMG Rev. Proc. 2025-32 [2K] | doğrulandı | "As of twenty twenty-six, the US federal estate tax only starts above fifteen million dollars per person" — "as of 2026" + "US federal" zorunlu; yasa değişikliği anılırsa parti/politikacı adı yok (P1). Vergi oranı, kaç estate'in ödediği **metne girmez** (birincil sayı yok) | "$15M per person (US federal, 2026)" |
| R19 | 409.900 $ (65–74) · 335.600 $ (75+) medyan; ortalamalar 1,79 M / 1,62 M (4,4x / 4,8x) | aile net serveti, **2022 doları** | SCF 2022 (Fed Bulletin Eki 2023) | Fed SCF [B] | doğrulandı | "for the typical family headed by someone sixty-five to seventy-four, net worth was about four hundred ten thousand dollars in twenty twenty-two" → "so for most families, the federal estate tax never comes into play" ([H] 15 M ≈ 37x medyan; sesli yalnız "dozens of times"). "Typical" = medyan; "average" yazılmaz | "Median, ages 65–74: ~$410K (Fed SCF 2022)" |
| R28 | miras kalan **vergi ertelemeli emeklilik hesabından** (geleneksel IRA/401(k)) çekilen para mirasçının **gelir vergisine** tabi | — | güncel | IRS "Retirement topics – Beneficiary": "Beneficiaries must include any taxable distributions they receive in their gross income." [B] | doğrulandı (F3 doğrulama turunda eklendi) | "the estate tax skips most families, but money left in some retirement accounts can still be taxed as income when the kids take it out" — oran/tutar yok; "10-year rule" vb. ayrıntı yok | — |
| R20 | eyalet vergileri | — | — | yalnız nitel: "some states have their own estate or inheritance taxes" [T, birincil sayı yok] | rakamsız | eyalet sayısı **yazılmaz** | — |
| R21 | %2 → 20 yılda 1 $ ≈ 0,67 $ alım gücü (24 yılda 0,62) | [H] Fed uzun dönem hedefi %2 (federalreserve.gov FAQ) | — | [B] hedef + [H] | hesap | "even at the Fed's two percent target, a dollar loses about a third of its buying power over twenty years" — 124 T$'ın nominal mi reel mi olduğu Cerulli bülteninde **yazmıyor** → "124 is in future dollars" **denmez** | "2%/yr × 20 yrs → $1 ≈ $0.67" |

## 8. Bölünmüş tablo kartı (K1 kapanış, tek kart)
| # | Değer | Birim | Tarih | Kaynak | Durum | Güvenli yazım | Ekran |
|---|---|---|---|---|---|---|---|
| R24 | üst %10 = %68,9 · üst %1 = %32,5 · alt %50 = %2,3 | ABD hane net serveti payı | 2026:Q2 | Fed DFA (hesap.py) [B] | doğrulandı | "the top ten percent of US households hold about two-thirds of household wealth; the bottom half, about two percent" | 3 çubuk, "Fed DFA, Q2 2026" |
| R22 | boomer %52,5 (97,4 T$) · Gen X %25,7 · Millennial %11,2 · Silent %10,7 | net servet payı, kuşak | 2026:Q2 | Fed DFA [B] | doğrulandı | "boomers hold about half of all US household wealth" | — |
| R07 | ~%50 (62 T$) / %2 hane | (yukarıda) | | | | kart başlığı: "big for a few, smaller and later for most" [T] | |
**Kıyas yasağı:** DFA 97,4 T$ (bugünkü stok) ile Cerulli 100 T$ (2048'e kadar akış, büyüme dahil) yan yana konmaz / birbirinden çıkarılmaz.

## 9. Uluslararası satır (D5)
| # | Değer | Kaynak | Durum | Güvenli yazım |
|---|---|---|---|---|
| R26 | Birleşik Krallık: 325.000 £ eşik, standart oran %40; eşe/bağışa bırakılan kısım genelde vergisiz | gov.uk/inheritance-tax [B] | doğrulandı | opsiyonel tek cümle: "In the UK, for example, inheritance tax generally starts above three hundred twenty-five thousand pounds" ("as of 2026"). Kanada/Avustralya: **cümle çıkar** (bu turda birincil kaynak açılmadı) |

## 10. Metne girmez / yasak ifadeler
| # | İfade | Neden |
|---|---|---|
| R27a | "124 − 54 − 18 = 52", "only 52 trillion reaches the kids", eşe gideni "leak/lost" | D2 çift sayım (hesap.py assert) |
| R27b | "Bank of America says/finds 124 trillion" (Fortune manşeti bile böyle) | rakam Cerulli'nin |
| R27c | "the biggest handover ever" (kesin) | yorum → "often called the biggest…" |
| R27d | "more than half from 2%" | 62/124 = %50,0 → "about half" |
| R27e | "almost 70% will need long-term care" | ACL eski/geniş ölçü; ASPE %56 seçildi |
| R27f | ölüm vergisini ödeyen estate sayısı/oranı, eyalet sayısı, probate/avukat ücreti yüzdesi | birincil kaynak yok → rakamsız |
| R27g | Dunham modelinden rakamlar (34. yıl, 2,6 M$ gıda) | tek ikincil kaynak, model |

## 11. Tavsiye dili güvenli yazımlar (senaryo-yazari seçer)
- "you should set up a trust / gift it now / buy long-term care insurance" → (a) "some families choose to talk about this early" (b) "planners often say the conversation matters more than the paperwork" (c) mekanizmayı söyle, eylem söyleme.
- "Don't let the government take it" → (a) "this is how the rules work in the US as of 2026" (b) çıkar.
- Yasal not (açıklama, P3): "This video is for education and entertainment only and is not financial, investment, legal or tax advice. Figures are estimates or survey results as of the dates shown (US unless stated); future amounts are projections, not predictions. The Okafor family is fictional. Leo is a fictional cartoon character. Narration voice is AI-generated." Sponsor/affiliate yok → FTC satırı gerekmez.
