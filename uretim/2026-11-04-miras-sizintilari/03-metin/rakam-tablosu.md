# F3 rakam tablosu — S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It" (finans-dogrulayici) · 2026-11-04

İLERLEME: 1. parti (R01–R12, kritik) kilitli · sıradaki: sızıntı 1/2/5/6 + dağılım + hesap.py assert.
**Kural:** Metin YALNIZ bu tablodaki rakamları, "Güvenli yazım" sütunundaki biçimde kullanır. Tabloda olmayan rakam → `[RAKAM?]` yaz, uydurma.
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
| R07 | 62 / %2 | trilyon $ (toplamın >%50'si) / hanelerin payı; HNW+UHNW | → 2048 | Cerulli [B] | doğrulandı | "more than half of it is expected to come from just two percent of households" | >50% from 2% of households |
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
