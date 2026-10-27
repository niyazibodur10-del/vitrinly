# F3 — Metin doğrulama (finans-dogrulayici) · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Denetlenen:** `03-metin/metin.md` v1 (commit a2e6d26) · **Tarih:** 2026-10-27 · paralel: `monetizasyon-uyum-uzmani` (`politika-denetimi.md` okundu, çakışma yok, bkz. §4).
**Sonuç: KAPI GEÇTİ (doğrulanamayan rakam yok) · METİN KİLİDİ İÇİN RED-1: 6 zorunlu DÜZELT, 0 ÇIKAR, 3 isteğe bağlı öneri.** Hepsi tek turda uygulanabilir, hiçbiri yedek senaryoya (S01) geçiş tetiği değil. Metni ben değiştirmedim; kesin metin §3'te (eski → yeni).

Etiketler: **[D]** birincil kaynak bu çalışmada açıldı/okundu · **[D2]** iki bağımsız kaynakta doğrulandı · **[H]** benim betiğimle bağımsız yeniden hesap (`dogrulama-hesap.py`) · **[AÖ]** ikincil kaynak / arama özeti.

## 0. Kaynaklar (bu turda açılanlar, erişim 2026-10-27)
| Kod | Kaynak | Ne doğrulandı |
|---|---|---|
| FRH-29 | federalreservehistory.org/essays/stock-market-crash-of-1929 | 63→381 "six-fold"; 381.17 (3 Eyl); "nearly 13" / "nearly 12 percent"; "almost half" (Kasım ortası); 41.22 (8 Tem 1932), "89 percent below its peak"; Kasım 1954; "typically 10 percent"; "In September 1929, stock prices gyrated, with sudden declines and rapid recoveries" |
| FRH-BP | …/essays/banking-panics-1930-31 | "over 8,000 … nearly 16,000"; "Within a few weeks, hundreds of banks suspended operations"; "December 11, the fourth-largest bank in New York City, Bank of United States, ceased operations"; "About one-third of these organizations reopened within a few months" (**bağlam: Sekizinci Bölge cümlesinin hemen ardından** — ulusal oran değil) |
| FRH-GD | …/essays/great-depression | "From the fall of 1930 through the winter of 1933, the money supply fell by nearly 30 percent." |
| FDIC-BH3 | FDIC, *A Brief History of Deposit Insurance*, Bölüm 3 PDF (`curl` + `pdftotext`) | Tablo 5 (13/13 satır CSV ile aynı [H]); dipnot 15 "Some of the suspended banks were reorganized or restored to solvency and resumed operations"; otel notları; "By March 4, Inauguration Day, every state in the Union had declared a bank holiday"; tatil "to commence on March 6"; "About 4,000 banks never reopened"; Banking Act 16 Haziran 1933; 1 Ocak 1934, 2.500 $; "Only nine insured banks and 52 uninsured licensed banks suspended operations during 1934"; "widespread attempts to convert deposits to cash" |
| FDIC-DI | fdic.gov/resources/deposit-insurance | "Your deposits are automatically insured to at least $250,000 at each FDIC-insured bank." 2026'da yasalaşmış limit değişikliği bulunmadı (yalnız teklifler: Hagerty-Alsobrooks, Lucas) [AÖ] |
| FRED | `CPIAUCNS` canlı CSV | Repodaki iki CSV ile **165/165 gözlem aynı** (Eki 2025 boş: BLS o ayı yayımlamadı, kaynakta da boş) |
| BLS | bls.gov/news.release/archives/cpi_10142026.htm | "increased 3.7 percent over the last 12 months to an index level of 336.940", 14 Ekim 2026 |
| BEA | BEA'nın kendi toplu dosyası `apps.bea.gov/national/Release/TXT/NipaDataA.txt` + DBnomics API (T6.3A, T6.5A, T6.6A) | 1929 ücret toplamı 50.460 M$ (A034RC, **BEA sitesinden**) ÷ 35.286 bin FTE (T6.5A) = **1.430 $** = T6.6A satır 1 (1.430). 1930 = 1.392 |
| HUL | Hulbert, "25 Years to Bounce Back? Try 4½", NYT 26 Nis 2009 (HNN kopyası; NYT ücretli) | "would have been back to a break-even by late 1936"; "Nov. 23, 1954"; dipte temettü verimi "close to 14 percent" |
| SHILLER | Shiller `ie_data.xls` (S&P Composite aylık fiyat, temettü, TÜFE) — `dogrulama-cikti/shiller_check.py` | **Bağımsız yeniden hesap:** Eyl 1929'dan reel toplam getiri başa baş **Kasım 1936**; nominal fiyat başa baş Eyl 1954 [H] |
| BMS | FRED `COMBNKTTL` (Banking and Monetary Statistics 1914–1941) | ticari banka sayısı Haz 1929 24.026 → Haz 1933 14.440 |
| BDT | Borowiecki, Dzieliński, Tepper, "The Great Margin Call" (SDU DP 1/2022, EHR 2022) dipnot 13 | "Margin requirements rose from as low as 10-20 percent up to 40-50 percent by the middle of 1929" (Smiley-Keehn 1988, Rappoport-White 1994'e atıfla) |
| WIKI | en.wikipedia.org/wiki/Wall_Street_crash_of_1929 [AÖ] | 28 Eki −12,82 % (260,64), 29 Eki −11,73 % (230,07); Eylül sonu zirveden −%10; 13 Kas ara dip 198,60 |

## 1. Test kapısı (betik, iki koşu aynı)
```
$ cd 03-metin && python3 -I dogrulama-kontrol.py metin.md      # 2 koşu → diff yok, sha256 10dbb0236966b750…
Sayım: ANLATIM 122 · Shorts 3 · GÖRSEL benzersiz 93
Eşlenmeyen (ANLATIM+Shorts+GÖRSEL): 0        → exit 0
$ python3 -I dogrulama-hesap.py <fdic3.txt>                     # 2 koşu → sha256 36871e96d746… (aynı)
$ python3 -I shiller_check.py <xlrd> ie_data.xls               # 2 koşu → md5 610b0996… (aynı)
```
Çıktılar: `dogrulama-cikti/{kontrol-cikti.txt, hesap-cikti.txt, shiller-cikti.txt}`. `dogrulama-kontrol.py` yazıyla yazılmış sayıları ("one thousand four hundred thirty", "nineteen thirties", "thirteen and a half") ayrıştırıyor; GÖRSEL sütunundaki rakamları zaman damgası/kaynak kodu temizlendikten sonra çıkarıyor; her değeri aşağıdaki iddia ID'sine eşliyor. "Y" = yapısal sayı (kural 1/2, "three doors", Bölüm 5, Tablo 5).
Yazarın `veri/hesap.py`'si de çalıştırıldı: iki koşu aynı, `hesap-cikti.txt` ile birebir. Benim betiğim ondan bağımsız yazıldı ve aynı değerleri verdi (108,14 · −21,39 % · 1.272 · −27,17 % · 1.373 · +13,52 % · 881 · +3,74 % · 964 · 19,57 % · 9.096).

## 2. İddia tablosu (metindeki her rakam, tarih, olay)
| ID | İddia (sahne) | Kaynak | Durum | Not / düzeltme |
|---|---|---|---|---|
| T01 | Oyun dönemi Eyl 1929 → Mar 1933 (S01 vd.) | FRH-29, FDIC-BH3 | DOĞRU | — |
| C01 | 1.000 $ (oyun tutarı) | kurgu | DOĞRU (Y) | — |
| C02 | 1929 ortalama tam zamanlı ücret ≈1.430 $/yıl; "roughly eight months" (S03, G0) | BEA T6.6A satır 1 + BEA A034RC ÷ T6.5A [D2, H] = 1.430; 1000/1430×12 = 8,4 | DOĞRU | Açık risk (2) kapandı: pay BEA'nın kendi sitesinden, sonuç aynı |
| C03 | Ağu 1921 Dow 63; "last eight years" (S05) | FRH-29 [D]; Ağu 1921→Eyl 1929 = 8,1 yıl [H] | DOĞRU | — |
| C04 | Eyl 1929 381; "six times higher" (S05) | FRH-29 "six-fold" [D]; ×6,05 [H] | DOĞRU | — |
| C05 | 3 Eyl 1929 kapanış 381,17 = zirve (S05) | FRH-29 [D], HUL [AÖ] | DOĞRU | — |
| C06 | "They put down a part, typically ten percent" (S05) + ekran "TYPICALLY 10% DOWN, 90% BORROWED" | FRH-29 "typically 10 percent" ↔ BDT: 1928 sonundan itibaren 40–50 %'ye çıktı (Smiley-Keehn, Rappoport-White) | **DÜZELT (D-1)** | Kaynaklar çelişiyor; akademik birincil derlemeler daha güvenilir. Sahnede tarih Eylül 1929 → "typically 10" o an için yanlış. F2'de önerdiğim "as little as" kullanılmamış (hafıza dersi) |
| C06b | "For a few weeks, nothing much happens. Then October arrives." (S06) | FRH-29: "In September 1929, stock prices gyrated, with sudden declines and rapid recoveries"; WIKI: Eylül sonu −%10; 28 Eki öncesi kapanış 298,97 = zirveden **−21,6 %** [H] | **DÜZELT (D-2)** | Rakam değil ama yanlış olgu: Kara Pazartesi'den önce düşüş zaten ~%22 |
| C07 | 28 Eki "nearly thirteen", 29 Eki "almost twelve percent"; Black Monday/Tuesday adları (S06, G1b) | FRH-29 [D] + WIKI −12,82 / −11,73 [D2] | DOĞRU | — |
| C08 | Kasım ortası "almost half", ~500 $; "about ten weeks"; ekran −50 % | FRH-29 [D]; 13 Kas 198,60 → 521 $; 3 Eyl→13 Kas = 10,1 hafta [H] | DOĞRU | — |
| C10 | 1930 sonu dalga dalga iflas; "Within a few weeks, hundreds close" (S08) | FRH-BP birebir + FDIC-BH3 "wave of bank failures during the last few months of 1930" [D2] | DOĞRU | — |
| C11 | 8.000+ üye, ~16.000 üye değil; "small and local" (S08) | FRH-BP [D]; FDIC-BH3 "small, rural banks" | DOĞRU | — |
| C12 | 11 Ara 1930, NYC'nin 4. büyük bankası Bank of United States (S09) | FRH-BP birebir [D]; FDIC-BH3 "one of the nation's largest banks based in New York City" (uyumlu) | DOĞRU | Kapanmış kurum, olgusal ifade → karalama riski yok |
| C13 | 1930–33 "about nine thousand banks suspended"; G2 yıllık çubuklar 506…4.000; ≈9.100 | FDIC-BH3 Tablo 5 [D], CSV=PDF 13/13 [H]; toplam 9.096 | DOĞRU | Tablo ticari bankalar; "suspended" terimi doğru (dipnot 15) |
| C14 | "more than one bank in three" (S10) | 9.096 / ~24.000 (FRH-BP) = 37,9 %; / 24.026 (BMS Haz 1929) = 37,9 %; BMS net düşüş Haz 1929→Haz 1933 = 9.586 (%39,9) [D2, H] | DOĞRU | Açık risk (3) kapandı: payda 27.288'e kadar çıksa da >1/3; net düşüş tekrar-askıya-alma şüphesinden bağımsız teyit |
| C15 | "the FDIC's own numbers show depositors lost about twenty cents of every dollar, on average" (S10, G2) | Tablo 5 sütun 3 ÷ sütun 2, 1930–33: 1.336.533 / 6.830.223 = **19,57 %** [D, H]; sütun 1–3 kaynağı "FDIC" | DOĞRU | Okuma doğru: payda askıya alınan bankaların mevduatı (sütun 2), sütun 4 değil. Dolar ağırlıklı ortalama; yıllık 28,4 / 23,1 / 23,8 / 15,0 %. "If your bank was one of them … on average" koşullu çerçeve doğru |
| C16 | ~200 $ kayıp / ~800 $ kalan (S10, S16, G4) | [H] 196 / 804 | DOĞRU | — |
| C16b | "If your bank survived, you kept everything." (S10) + skor tablosu "Maybe all of it" (S16) + "So Box Leo wins nineteen twenty-nine" (S19) | Tablo 5 sütun 4 → askıya alınan bankalardaki mevduat, tüm ticari mevduatın 1930–33 bileşik **≈%22**'si; **≈%78**'i hayatta kalan bankalardaydı; ortalama banka dolarının beklenen kaybı ≈%4,3 [H] | **DÜZELT (D-4)** | Rakamlar doğru ama karşılaştırma eksik: hayatta kalan bankadaki para da deflasyonla kutudaki nakit kadar alım gücü kazandı. Söylenmezse izleyici deflasyon kazancını yalnız "evde nakit"e ait sanar (yanıltıcı karşılaştırma) |
| C17 | TÜFE Eyl 1929→Tem 1932 −21 %; 1.000 $ ≈ 1.270 $ (S12, S16, G3: 17,3 / 13,6) | FRED canlı = repo CSV [D]; −21,39 %, 1.272 [H] | DOĞRU | "twelve hundred seventy" yuvarlama 1.272 → kabul |
| C18 | Para arzı "nearly thirty percent", 1930 sonbaharı → 1933 kışı (S13) | FRH-GD birebir [D] | DOĞRU | Dönem ve ölçü (para arzı, fiyat değil) doğru eşlenmiş (D2 tuttu) |
| C19 | 8 Tem 1932 41,22; −89 %; 108 $ "price only, before dividends"; reel ≈138 $ (S15, S16) | FRH-29 "89 percent below its peak" [D]; 108,14 / 137,6 [H] | DOĞRU | D1 tuttu |
| C20 | Dow fiyatı Kasım 1954'te 1929 zirvesine döndü (S15) | FRH-29 [D]; HUL "Nov. 23, 1954"; Shiller S&P fiyat Eyl 1954 [H] | DOĞRU | D6 tuttu ("The Dow's price") |
| C21 | Temettü + düşen fiyatlarla başa baş "late 1936"; "seven years" (S15, G1 notu "Hulbert, NYT 2009") | HUL [AÖ] + **Shiller verisiyle bağımsız yeniden hesap: Kasım 1936** [H]; HUL TÜFE notu "18 % lower" ↔ FRED Eyl 1929 17,3 → Kas 1936 14,0 = −19,1 % (tutarlı); Eyl 1929→Kas 1936 = 7,2 yıl | DOĞRU | Açık risk (1) kapandı: ikincil kopya, birincil veriyle tekrar üretildi. "one well-known analysis" çerçevesi uygun (Hulbert "average stock" kullanıyor, Dow değil — çerçeve bunu taşıyor) |
| C22 | "Some reopened within a few months. Most were closed for good." (S10) | FRH-BP "one-third … within a few months" **Sekizinci Bölge bağlamında**, 1930–31; FDIC-BH3 dipnot 15 "Some … resumed operations" + "About 4,000 banks never reopened" | **DÜZELT (D-3)** | Açık risk (4): "within a few months" ve "most" 1930–33 ulusal düzeye genellenemiyor. "Some reopened / thousands never did" iki kaynakla birebir destekli |
| C23 | 1929'da federal mevduat sigortası yoktu (S08) | FDIC-BH3 (sigorta 1 Ocak 1934) [D] | DOĞRU | — |
| C24 | Kış 1933 panik eyaletten eyalete; Washington'da otel notları; 4 Mart'a kadar her eyalette tatil (S18) | FDIC-BH3 birebir [D] | DOĞRU | — |
| C25 | Tatilden sonra "about four thousand banks never reopen" (S18, ~4,000) | FDIC-BH3 "About 4,000 banks never reopened" [D] | DOĞRU | Nüans: FDIC aynı bölümde 1934'te "more than 900" lisanssız bankanın tasfiyeye girdiğini yazıyor; ifade FDIC'in kendi cümlesi, kabul |
| C26 | "Two days later" 6 Mart ulusal tatil; Haziran 1933 yasa (ekran 16 Haz); 1 Ocak 1934; 2.500 $/mudi (S18, S22) | FDIC-BH3 [D]; 4→6 Mart = 2 gün [H] | DOĞRU | — |
| C27 | 1934'te yalnız 9 sigortalı banka askıya alındı (S19, ekran) | FDIC-BH3 [D] | DOĞRU (anlatım) · **DÜZELT görsel (D-5)** | G2'de 1933 çubuğu (tüm ticari bankalar, 4.000) yanına "9 insured" çubuğu = elma-armut. 1934 toplamı 61 (9 sigortalı + 52 sigortasız lisanslı) |
| C30 | Eyl 2025→Eyl 2026 TÜFE +3,7 % NSA (S20, G5a) | BLS 14 Eki 2026 [D] + FRED 336,940/324,800 = +3,74 % [H] | DOĞRU | D4 tuttu |
| C31 | 1.000 $ ≈ 964 $ (S20) | [H] | DOĞRU | — |
| C32 | Eyl 1929→Mar 1933 −27 %; Eyl 2022→Eyl 2026 +13,5 %; G5: 72,8 / 113,5; 1.373 / 881 (S21) | FRED [D], [H] −27,17 / +13,52 | DOĞRU | İsteğe bağlı öneri Ö-1 (pencere uzunlukları 42 ay / 48 ay) |
| C33 | FDIC "at least $250,000 at each insured bank" (S22) | FDIC-DI birebir [D] | DOĞRU | İsteğe bağlı Ö-2 |
| C34 | Uç ekran: "a time when prices rose so fast that people's savings melted in a single year" (S24) | F2 S04 doğrulaması (Almanya 1923, PBS + Rentenmark oranı) [D] | DOĞRU | İsim verilmiyor, genel ifade |
| C35 | Shorts 1 hook: "In nineteen twenty-nine, most people would have picked the wrong door." | Kaynak yok. C16b hesabı: banka kapısını seçen mevduat dolarlarının ≈%78'i hayatta kalan bankadaydı ve kutuyla aynı alım gücü kazancını aldı → "çoğu insan yanlış kapıyı seçerdi" savunulamaz | **DÜZELT (D-6)** | Koordinatörün sorusu: genelleme doğrulanamıyor, büyük olasılıkla yanlış. Politika uzmanının yedek önerisiyle uyumlu yazım §3'te |
| — | Niteliksel: "ordinary people … savings" (S05), margin call mekanizması (S06), mevduatın çoğu kredi olarak dışarıda (S09), nakde çevirme (S13), kutunun tuzakları (S14) | FRH-29 "ordinary people", FDIC-BH3 "convert deposits to cash" | DOĞRU | — |
| — | Mit taraması (`suicide|jump from|window|leap`) | grep | 0 | — |

**Sayım:** 37 iddia satırı · DOĞRU 31 · DÜZELT 6 (D-1…D-6) · ÇIKAR 0 · doğrulanamayan 0.

## 3. Değişiklik listesi (senaryo-yazari uygular; kesin metin)

**D-1 · S05 marjin (zorunlu).** Seçenekler: A "sometimes as little as" (önerilen; F2 S01 kararıyla aynı dil) · B sayısız · C dönem nitelemeli.
- ANLATIM eski: "Many didn't even pay the full price. They put down a part, typically ten percent, and borrowed the rest."
- ANLATIM yeni (A): "Many didn't even pay the full price. They put down part of it, sometimes as little as ten percent, and borrowed the rest."
  (B: "…They put down part of it and borrowed the rest." · C: "…Earlier in the decade, some put down as little as ten percent and borrowed the rest.")
- GÖRSEL ekran eski: "TYPICALLY 10% DOWN, 90% BORROWED" [FRH-29] → yeni: "PART DOWN, REST BORROWED · SOMETIMES ONLY 10% DOWN" [FRH-29; Borowiecki et al. 2022]
- §8 satır 5 eski "typically ten percent … %10" → yeni "sometimes as little as ten percent … ≥%10 (1929 ortasında tipik 40–50 %)".

**D-2 · S06 Eylül–Ekim (zorunlu).**
- ANLATIM eski: "For a few weeks, nothing much happens. Then October arrives."
- ANLATIM yeni: "For a few weeks, prices swing up and down, with sudden drops and quick recoveries. Then October arrives." (FRH-29 "gyrated, with sudden declines and rapid recoveries"; +8 kelime ≈ +3 sn)
- GÖRSEL ek not: "G1a/G1b çizgisi 3 Eyl ile 28 Eki arasında düz çizilmez; dalgalı ve aşağı eğimli (28 Eki öncesi ≈299, sayı etiketi yok)."

**D-3 · S10 yeniden açılma (zorunlu).**
- ANLATIM eski: "Some reopened within a few months. Most were closed for good."
- ANLATIM yeni: "Some reopened later. Thousands never did." (FDIC-BH3 dipnot 15 + "About 4,000 banks never reopened"; −4 kelime)
- §8 satır 37 kaynak notu buna göre güncellenir.

**D-4 · Banka kapısının iyi sonucu (zorunlu; S12'deki sürprizi bozmamak için S16 ve S19'a).**
- S16 ANLATIM eski: "Bank Leo: a question mark. Maybe all of it, maybe around eight hundred, maybe still waiting."
- S16 ANLATIM yeni: "Bank Leo: a question mark. Maybe all of it, buying just as much as Box Leo's. Maybe around eight hundred, maybe still waiting." (+6 kelime)
- S16 GÖRSEL G4 BANK alt satırı eski: "if your bank suspended: avg. ~$800 left" → yeni: iki satır "if your bank survived: same as the box" · "if your bank suspended: avg. ~$800 left" [FDIC-BH3, H]
- S19 ANLATIM eski: "So Box Leo wins nineteen twenty-nine."
- S19 ANLATIM yeni: "So Box Leo wins nineteen twenty-nine: the same gain in buying power, without the gamble." (+9 kelime)

**D-5 · S19 G2 1934 çubuğu (zorunlu, yalnız görsel; anlatım aynı).**
- GÖRSEL eski: "1933 çubuğu 4,000 → 1934 çubuğu "9 insured" (neredeyse görünmez çubuk) [FDIC-BH3]"
- GÖRSEL yeni: "1933 çubuğu 4,000 → 1934 çubuğu "61" (aynı seri: tüm askıya almalar), içinde ayrı renkli dilim "9 insured" [FDIC-BH3 s.31: 9 sigortalı + 52 sigortasız lisanslı]". Ekran yazısı "1934: 9 INSURED BANKS SUSPENDED" aynı kalır.

**D-6 · Shorts 1 hook (zorunlu).** Seçenekler: A (önerilen) · B politika uzmanının yedeği · C.
- eski: "In nineteen twenty-nine, most people would have picked the wrong door."
- yeni (A): "In nineteen twenty-nine, the smartest-looking door was the worst one." (11 kelime, süre aynı; borsa −89 % = en kötü kapı, C19)
  (B: "In nineteen twenty-nine, the smartest-looking door was the wrong one." — kabul edilebilir ama "wrong" bankayı da kapsıyormuş gibi okunabilir · C: "In nineteen twenty-nine, the door everyone laughed at did best on safety.")
- §11 P2 satırı ve §5 "Politika" notu yeni cümleyle güncellenir. `monetizasyon-uyum-uzmani` B1'de kendi yedeği olarak aynı yapıyı önerdi → politika rengi değişmez.

**İsteğe bağlı öneriler (kapıyı etkilemez):**
- **Ö-1 (S21):** 1929–33 penceresi 42 ay, 2022–26 penceresi 48 ay. Rakamlar doğru ve tarihler söyleniyor; yine de "side by side" için eşit pencere istenirse: "From March twenty twenty-three to September twenty twenty-six, prices rose about eleven and a half percent." (+11,63 % [H]); G5 113,5 → 111,6, 881 → 896 olarak yeniden hesaplanmalı. Ya da G5 x eksenine "42 months / 48 months" etiketi.
- **Ö-2 (S22):** 1934 tavanı "per depositor"; bugünkü cümle FDIC'in birebir ifadesi olduğu için doğru. Kıyas netliği için ekran: "$2,500 per depositor (1934) → at least $250,000 per depositor, per insured bank (today)".
- **Ö-3 (§7 kaynak listesi / açıklama):** HUL satırına "replicated with Shiller data: real total-return break-even Nov 1936" notu; BEA-666 durumu "[D] BEA toplu dosyasıyla teyit edildi"; açıklama kaynak listesine "Borowiecki, Dzieliński & Tepper (2022)" eklenir (D-1 A seçilirse).

**Süre etkisi:** D-2 +8, D-3 −4, D-4 +15 kelime → +19 kelime ≈ +8 sn (1.678 → ≈1.697, kapı 1.544–1.888 içinde). Shorts 1 değişmez (11 kelime).
**Yeniden ölçüm:** düzeltilmiş metinde `python3 -I dogrulama-kontrol.py metin.md` → eşlenmeyen 0 olmalı (D-6 A ve D-3 yeni sayı getirmiyor; Ö-1 seçilirse betikteki eşlemeye 2023/11.5 eklenir).

## 4. Tavsiye dili, karalama, yanıltıcı bilgi, yasal not
- **Tavsiye dili:** anlatım + Shorts'ta `should|must|need to|buy|invest|guarantee|recommend|keep your cash` → 0 (yalnız S06 "so people sell" — betimleyici). Bugüne dönük hüküm yok; 2026 bölümü ölçülmüş veri (BLS) + mekanizma ("That's arithmetic, not a plan."). Geleceğe dair tahmin yok, bu yüzden "scenario" etiketi gereken cümle yok. **YEŞİL.**
- **Karalama / kişi:** Roosevelt yalnız olgusal eylem (FDIC-BH3); Bank of United States 1930'da kapanmış kurum, olgusal ifade; yaşayan kişi yok. **YEŞİL.**
- **Yanıltıcı bilgi (YouTube misinformation / dolandırıcılık):** kesin kazanç vaadi, "risk-free", şema yok. Kalan yanıltıcılık riskleri D-1, D-2, D-4, D-6 ile kapanıyor. **Düzeltmelerle YEŞİL.**
- **Politika denetimiyle çakışma:** B1 (Shorts 1 kapanış satırı "The brown door won because prices were falling…") olgusal olarak doğru (C17) ve D-6 ile uyumlu. B2 (Illustration etiketleri) benim alanım dışında, çelişki yok.
- **FTC:** sponsor/ortaklık yok → FTC açıklaması gerekmiyor. Ortaklık bağlantısı eklenirse açıklamanın ilk satırlarına "Contains affiliate links / #ad" zorunlu.

**Açıklama için yasal not (F8'de `youtube-paketleyici` aynen kullanır):**
> This video is for education and entertainment only. It is not financial, investment, tax or legal advice. Leo is a fictional cartoon character, not a financial adviser. The "three doors" game is a simplified illustration of history: past results do not predict future results, and nothing here is a recommendation to buy, sell or hold any asset. Stock figures are price-only unless stated; inflation figures are U.S. CPI (BLS). Some scenes are illustrations, not historical footage. Sources are listed below. Narration voice is AI-generated.

## 5. Elenen yaklaşımlar
1. **Yazarın §8 rakam tablosunu kabul etmek** — elendi: tablo tamdı ama C06 (marjin) ve C35 (Shorts hook) "doğru" görünüyordu; ikisi de tek kaynağa/kaynaksız genellemeye dayanıyordu.
2. **Yalnız ANLATIM'daki rakamları taramak** — elendi: G2'nin 1934 çubuğu (D-5) yalnız GÖRSEL sütununda.
3. **Hulbert'i ikincil kaynak diye çıkarmak** — elendi: Shiller verisiyle aynı sonuç (Kasım 1936) yeniden üretildi; çıkarmak doğru bir nüansı silerdi.
4. **"Most were closed for good" için alt sınır hesabı (%71)** — elendi: FRH-BP'deki "one-third" ulusal değil bölgesel bağlamda; hesap bu varsayıma dayanıyordu. Sayısız ve iki kaynakla birebir destekli yazım seçildi.

## 6. Riskler
- WIKI günlük kapanışları [AÖ]; anlatımda yalnız FRH-29'un yuvarlak değerleri kullanılıyor, D-2 sayı eklemiyor.
- Hulbert "average stock", Shiller S&P Composite; Dow'a özgü toplam getiri başa başı hesaplanmadı. Metin "one well-known analysis" dediği için kabul.
- F4 sonrası metin değişirse bu dosyadaki kontrol betiği yeniden çalıştırılmalı.

## 7. RED-1 sonrası yeniden doğrulama (2026-10-27) — **GEÇTİ**
**Denetlenen:** `metin.md` v2 (commit d874c1b, §14 değişiklik tablosu). Metni değiştirmedim.

| Madde | Kontrol (grep, metin.md) | Sonuç |
|---|---|---|
| D-1 | S05 ANLATIM "sometimes as little as ten percent" ✓ · ekran "PART DOWN, REST BORROWED · SOMETIMES ONLY 10% DOWN" + BDT ✓ · §7 BDT satırı, §8 satır 5 "≥%10 (1929 ortasında tipik %40–50)" ✓ · eski "typically ten"/"TYPICALLY 10"/"90%" yalnız §14 "Eski" sütununda | birebir |
| D-2 | S06 "prices swing up and down, with sudden drops and quick recoveries" ✓ · görsel not "dalgalı, aşağı eğimli, ≈299, sayı etiketi yok" ✓ | birebir |
| D-3 | S10 "Some reopened later. Thousands never did." ✓ · §8 satır 37 kaynak notu ✓ · "within a few months"/"closed for good" yalnız §14'te | birebir |
| D-4 | S16 "buying just as much as Box Leo's" ✓ · G4 iki alt satır ✓ · S19 "the same gain in buying power, without the gamble" ✓ · Shorts 1 tam metninde S16 cümlesi dahil ✓ | birebir |
| D-5 | S19 G2 1934 çubuğu "61" + "9 insured" dilimi, FDIC-BH3 s.31 (9 + 52 = 61 [H]) ✓ | birebir |
| D-6 | Shorts 1 hook "the smartest-looking door was the worst one." ✓ · §11 P2 güncel ✓ · "most people" yalnız §10 editör notu ve §11 eski metin alıntısında (okunmuyor) | birebir |
| Ö-1 | G5 x ekseni "42 MONTHS" ‖ "48 MONTHS": Eyl 1929→Mar 1933 = 42 ay, Eyl 2022→Eyl 2026 = 48 ay [H] | DOĞRU, kabul. Anlatımı değiştirmeme gerekçesi (yeni rakam getirmemek) yerinde |
| Ö-2 | S22 ekran "$2,500 per depositor (1934) → at least $250,000 per depositor, per insured bank (today)" | DOĞRU (FDIC-BH3 + FDIC-DI "per depositor, per insured bank, for each account ownership category"; "at least" korunmuş) |
| Ö-3 | §7: HUL'a Shiller/Kasım 1936 notu ✓ · BEA-666 "[D] BEA toplu dosya" ✓ · BDT eklendi, açıklama listesi 9 kaynak + HUL ✓ · BDT satırındaki "%10–20'ye kadar düşük, 1929 ortasında %40–50" kaynağın dipnot 13 ifadesiyle aynı | DOĞRU |
| Shorts 1 kesinti | S06 "By mid-November, the Dow has lost almost half its value." çıkarıldı → "Stock Leo's … now about five hundred" kaldı | Olgusal hata yok (C08: Kasım ortası ≈521 $). **Not (kapıyı etkilemez):** sesli tarih kalmadığı için 9:16'da −50 % sayacının yanında "NOV 1929" etiketi korunmalı (kurgu-editoru), yoksa "now" izleyiciye belirsiz |
| Shorts 2 kesinti | S20 "Nothing was stolen. The bills are all there." çıkarıldı | Rakam/olgu içermiyor; anlam kaybı yok. **Not (önceden var, kapıyı etkilemez):** kesit "Twelve months later" ile başlıyor ve 1929–32 cümlesinin hemen ardından geliyor; hook "In twenty twenty-six" ve sonraki cümle "year to September twenty twenty-six" ile çözülüyor. 9:16'da G5a "12 MONTHS TO SEPT 2026" kartı bu cümle başlarken ekranda olmalı |

**Test kapısı (betik, 2 koşu):** `dogrulama-kontrol.py` eşleme tablosuna eklendi: `≈299` → C06b (D-2), `61` → C27 (D-5), `42`/`48` → C32 (Ö-1); "Thousands" (S10) → C22/C25 (önceden yanlışlıkla C01'e düşüyordu). Betik artık Shorts'un "Okunacak tam metin" satırlarını da tarıyor (Shorts sayımı 3 → 36).
```
$ python3 -I dogrulama-kontrol.py metin.md   # 2 koşu → exit 0, cmp aynı, sha256 f8ee8b5f1ab51f6b…
Sayım: ANLATIM 123 · Shorts 36 · GÖRSEL benzersiz 96
Eşlenmeyen (ANLATIM+Shorts+GÖRSEL): 0
```
v1 çıktısıyla fark: ANLATIM'a yalnız "Thousands" (D-3) eklendi; GÖRSEL'e yalnız ≈299, 61, 42, 48 (dördü de benim verdiğim değerler) ve değişiklik etiketlerinden gelen yapısal küçük sayılar (D-2, D-4, D-5, RED-1 → Y). "90%" görselden çıktı (D-1). **Yeni ve kaynaksız rakam: 0.** Çıktı: `dogrulama-cikti/kontrol-cikti.txt`.

**Tavsiye/karalama taraması:** değişen cümlelerde `should|must|buy|invest|guarantee|recommend` yok; D-4 "without the gamble" geçmişe dönük betimleme (1929–33), bugüne hüküm değil. Yasal not (§4) değişmeden geçerli.

**Karar: GEÇTİ** — 6/6 zorunlu düzeltme birebir, 3/3 isteğe bağlı karar doğru, Shorts kesintileri olgusal açıdan temiz. Metin kilidine finans doğrulama engeli yok. İki 9:16 tarih etiketi notu F7'de `kurgu-editoru`'na gider.
