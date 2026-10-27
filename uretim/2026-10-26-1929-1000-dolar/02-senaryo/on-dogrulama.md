# F2 — Ön doğrulama / risk taraması (finans-dogrulayici) · 2026-10-27

**Girdi:** `02-senaryo/senaryolar.md` (11 senaryo), `01-arastirma/konu-havuzu.md`.
**Kapsam:** doğrulanabilirlik (ana iddia + kritik `[doğrulanacak]` yerler), yatırım tavsiyesi dili, karalama / yaşayan kişi riski, yanıltıcı bilgi / mit. Reklam uygunluğu (inauthentic, reused, AI beyanı) bu dosyada değil: `monetizasyon-uyum-uzmani`.
**Etiketler:** **[D]** birincil veya resmi kaynakta bu çalışmada okundu · **[AÖ]** arama özeti, 2 veya daha fazla bağımsız sonuç tutarlı, sayfa tam açılmadı · **[H]** betikle yeniden hesap (`hesap.py`, aşağıda) · **[?]** doğrulanamadı, metne girmez veya "tahmin" diye işaretlenir.

## 0. Sonuç: renk tablosu

| ID | Konu | Renk | Tek cümle gerekçe |
|---|---|---|---|
| S01 | 1929 marjin borcu | **YEŞİL** | Ana rakamlar Fed History'de [D]. İki düzeltme var: "10 %" ifadesi "as little as 10 percent" olacak, "25 years" ifadesi "the Dow's price" diye nitelenecek. |
| S02 | 1929→1933 bankalar | **YEŞİL** | Hook'taki üç rakam da FRH'de birebir var [D]. Fed'in rolü tartışmalı, "many economists argue" diliyle verilecek. "Most Americans owned no stocks" cümlesi için kaynak şart. |
| S03 | 1929'da 1.000 $ oyunu | **SARI** | Rakamlar doğru (1.000 $ → 108 $ [H]). Ama "hangi kapı kazandı" ve "nakit bugün kaybeder" kurgusu kişisel tavsiye gibi okunabilir. Banka kapısının kaybı sayısal olarak doğrulanmadı. Getiri karşılaştırması yalnız fiyatla yapılıyor, temettü yok. |
| S04 | Weimar 1923 | **YEŞİL** | Çelişki çözüldü: 1 Rentenmark = 1 trilyon eski mark [D]. Düzeltme: Kasım 1923'te 1 $ = **4,2 trilyon** mark ("one trillion" değil). Poliçe anekdotu tek kaynaklı, "one family's story" diye çerçevelenecek. |
| S05 | 1973 petrol + 2026 | **SARI** | 1973 rakamları FRH'de var [D] (bunlar "posted price"). 2026 savaşı sürüyor. Ekim 2026 Brent rakamı kaynaklar arasında çelişiyor (109,86 $ ile ~100 $). "Almost four times" yanlış, doğrusu ×4,02 [H]. |
| S06 | Cisco 2000 | **YEŞİL** | Zirve, dip ve Aralık 2025 geri dönüşü birden çok kaynakta doğrulandı [D/AÖ]. Alternatif başlık 2 ("Terrible Bet") elenmeli. Bugünkü şirketler (CoreWeave vb.) hakkında tahmin yok. |
| S07 | Black Monday 1987 | **YEŞİL** | Rakamların tamamı FRH'de [D]. "Yeni Zelanda −%60" için FRH dönem vermiyor, bu yüzden "in one day" denmez. Saatlik veri Brady raporundan alınacak, bulunmazsa "moment by moment" denecek. |
| S08 | Hunt kardeşler 1980 | **SARI** | Zirve çelişkisi çözüldü: **49,45 $** (18 Ocak 1980 Londra fiksi). Hook'taki "more than two-thirds of the world's silver" tek kaynaklı ve aykırı bir değer, değiştirilmeli. Başlıktaki "All the World's Silver" abartı. 2026 altın rekoru 5.318 $ doğrulanmadı. Kişiler vefat etmiş ama hukuki sonuçlar kesin dille verilmeli. |
| S09 | Lehman 2008 karşı-olgusal | **SARI** | En yüksek doğrulama yükü bunda (12 `[doğrulanacak]`). Karşı-olgusal bölüm spekülatif. Yaşayan yetkililerin (Fuld, Paulson, Bernanke, Geithner) kararlarına niyet atfetme riski var. "Neden kurtarılmadı" sorusu tartışmalı, iki görüş de verilecek. |
| S10 | Japonya 1989 | **YEŞİL** | Nikkei 38.915,87 → 39.098,68 ve bebeğin 34 yaşı doğrulandı [AÖ/H]. JGB'nin 1996'dan beri en yüksek seviyesi doğrulandı [AÖ]. Saray = Kaliforniya iddiası doğrulanamadı [?], kullanılmaz. 100 trilyon yen batık kredi [?]. |
| S11 | LTCM 1998 | **YEŞİL** | Rakamların tamamı FRH'de [D]. Düzeltme: Shorts'taki "3% mistake wipes you out" hesapça yanlış. 30:1 kaldıraçta %3 düşüş sermayenin %93'ünü siler, tamamı ~%3,2'de gider [H]. Başlıktaki "Nobel-Winning Fund" fonu ödüllü gibi gösteriyor, değiştirilecek. |

**KIRMIZI yok, 11 senaryonun hiçbiri elenmiyor.** 7 YEŞİL, 4 SARI. SARI senaryo seçilirse aşağıdaki düzeltmeler F3 metin kilidinin ön koşuludur.
**Risk sıralaması (düşükten yükseğe):** S07 ≈ S11 < S02 < S01 < S10 < S06 < S04 < S03 < S08 < S05 < S09.

---

## 1. Senaryo yazarının iki çelişkisi: çözüm

### 1a. Hunt gümüş zirvesi: 48,70 $ mı 49,45 $ mı?
| Rakam | Ne olduğu | Kaynak | Güvenilirlik |
|---|---|---|---|
| **49,45 $** | Londra günlük fiksi, **18 Ocak 1980**. Analistlerin bugün referans aldığı resmi zirve | ABA Journal [D]; Bloomberg aktarımı (Scottsdale Mint, Bloomberg Línea) [AÖ]; LBMA, gün içi Londra verisinin olmadığını teyit etmiş [AÖ] | Yüksek, 3 bağımsız kaynak |
| 50,35 $ / 50,36 $ | COMEX gün içi zirve, 18 Ocak 1980 | CME Group; NYT ve 1982 SEC raporu (aktarım) [AÖ] | Yüksek, ama gün içi değer |
| 48,70 $ | COMEX **kapanışı, 17 Ocak 1980** (bir önceki gün). Zirve değil | about.ag tablosu [AÖ]; KH-A12 bunu zirve diye almış | Doğru rakam ama yanlış etiketlenmiş |

**Karar:** Metinde **"$49.45 an ounce, on January 18, 1980"** kullanılacak (referans fiyat). Hook'ta yuvarlak söylenmek istenirse "nearly fifty dollars" doğrudur, çünkü COMEX gün içinde 50 $'ı geçti. "About forty-nine" de doğru, kalabilir. Grafik etiketi: "London fix". 48,70 $ hiçbir yerde "zirve" diye geçmez. KH-A12'deki "48,70 $ ile zirve" ifadesi düzeltilmeli (trend-avcisi'ne not).
Hesap [H]: 6 $ → 49,45 $ = ×8,2. 49,45 $ → 10,80 $ = −%78,2.

### 1b. Rentenmark: 1 = 1 milyar mı, 1 trilyon eski mark mı?
| Kaynak | Söylediği | Değerlendirme |
|---|---|---|
| PBS Commanding Heights [D] | "Nine zeros were struck… one Rentenmark was equal to one billion old Marks" | **Yanlış (ölçek hatası).** Almanca "Billion" = 10¹² = İngilizce *trillion*. PBS metni Almanca ölçeği çevirmeden aktarmış. |
| Wikipedia "Rentenmark" → Ahamed, *Lords of Finance* (2009) s. 184–189 [D] | "set by Schacht on November 20 to a rate of one Rentenmark to equal one trillion (10¹²) old marks… one United States dollar to equal 4.2 Rentenmarks" | Doğru, kitap kaynaklı |
| Alman kaynakları (DHM LeMO, Börsen-Zeitung arama sonuçları) [AÖ] | "1 Billion : 1", "4,2 Bill. Papiermark = 1 Dollar", "1 Dollar = 4,20 Rentenmark" | Doğru, Alman ölçeğiyle |
| İç tutarlılık [H] | 1914: 1 $ = 4,2 M. 20 Kas 1923: 1 $ = 4,2×10¹² M. 1:10¹² oranında 1 $ = **4,2 RM**, yani savaş öncesi kurla aynı. 1:10⁹ oranında 1 $ = 4.200 RM olurdu, bu da hiçbir kaynakla uyuşmuyor. | Trilyon oranı kendi içinde tutarlı, milyar tutarsız |

**Karar:** **1 Rentenmark = 1 trillion (1,000,000,000,000) old paper marks**, **20 Kasım 1923**'te sabitlendi (Rentenmark 15 Kasım 1923'te çıktı). **Twelve zeros** silindi, nine değil. PBS bu konuda kaynak gösterilmez. Hikâyenin geri kalanı için PBS kullanılabilir.
**Bağlı düzeltme (S04):** "In November 1923, one dollar bought one trillion marks" ifadesi **"more than four trillion marks"** olmalı (resmi kur, 20 Kasım 1923: 4,2 trilyon). PBS'teki "one trillion" yuvarlanmış veya erken bir tarihin kuru. Thumbnail metni "ONE TRILLION MARKS" kalabilir, ama yalnız Rentenmark oranını anlatıyorsa ("1 new mark = 1 trillion old").

---

## 2. Senaryo senaryo bulgu tablosu (kritik iddialar)

Durum: **doğru** / **düzeltilmeli** / **doğrulanamadı**.

### S01 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| 1929'da 100 $'lık hisse 10 $ peşinatla alınabiliyordu | FRH: marjin hesapları, alıcılar fiyatın ~%10'unu peşin ödeyip kalanı borçlanabiliyordu [D] | düzeltilmeli (nüans) | Marjin oranları broker ve hisseye göre değişiyordu, %10 alt sınırdı. Hook: "you could buy… with **as little as** ten dollars of your own". |
| Dow 63 (Ağu 1921) → 381,17 (3 Eyl 1929) → 41,22 (Tem 1932, −%89) | FRH [D]; ×6,05 ve −%89,2 [H] | doğru | — |
| 28 Ekim ~−%13, 29 Ekim ~−%12 | FRH [D] | doğru | — |
| Kasım ortasında değerin yarısı gitti | FRH [D] | doğru | — |
| "It took 25 years to get back" | FRH: Kasım 1954 [D] | düzeltilmeli | Bu yalnız **nominal fiyat endeksi** için geçerli. Temettü ve 1930'lar deflasyonu hesaba katılınca toparlanma çok daha kısa (literatürde tartışılıyor, F3'te kaynaklanacak). Metin: "**The Dow's price** didn't get back to its 1929 peak until 1954". |
| %10 düşüş peşinatın %100'ünü siler | [H]: −%5 → 5 $ kalır, −%10 → 0, −%20 → −10 $ | doğru | — |
| Fed 2 Şubat 1929 mektubu, Ağustos'ta %6 iskonto | FRH [D] | doğru | — |
| 1934 Securities Exchange Act ile Fed'e marjin yetkisi | Genel bilgi (Reg T, Bölüm 7) [?] | doğrulanacak (F3) | Birincil: SEC / Fed Reg T sayfası. |
| Brokers' loans serisi, FINRA marjin borcu | [?] | doğrulanacak (F3) | NBER seri kodu ve FINRA aylık tablo, tarihiyle. |
**Tavsiye dili:** "the one rule that changed" mekanizma anlatımı olarak uygun. Yasak: "never buy on margin". Güvenli yazım seçenekleri aşağıda (§3, R1).

### S02 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Kasım ortasında hisseler değerinin yarısını kaybetti | FRH 1929 [D] | doğru | — |
| Para arzı ~%30 küçüldü | FRH Great Depression: "from the fall of 1930 through the winter of 1933, the money supply fell by nearly 30 percent" [D] | doğru | Dönem belirtilmeli ("from late 1930 to early 1933"). Friedman–Schwartz'ın 1929–33 için "about a third" rakamı başka bir pencere. İkisi karıştırılmaz. |
| Bank of United States, 11 Aralık 1930 | FRH 1930–31 paniği (senaryo yazarı okudu) | doğru | Elenen H3'teki "fourth-largest bank in NYC" iddiası [?]. Kullanılırsa kaynak şart. |
| "Most Americans didn't own stocks" | Galbraith ~%1 (ikincil aktarım) [AÖ, tek] | doğrulanamadı | F3'te birincil kaynak (Galbraith 1954 veya NYSE / Census tahmini). Bulunmazsa yalnız "most Americans" (sayısız) bırakılır, bu yaygın kabul görüyor. |
| Fed'in rolü (Friedman & Schwartz) | FRH kaynakçada [D] | doğru, ama yorum | "Many economists argue" dili. Karşı görüş tek cümle (Temin: talep şoku). |
| FDIC: tarih ve tavan | Genel bilgi: Banking Act Haziran 1933, sigorta 1 Ocak 1934, 2.500 $ [?] | doğrulanacak (F3) | FDIC tarih sayfası. |
| 2023 banka çöküşleri bağlantısı | [?] | doğrulanacak | Tek cümle, FDIC kaynaklı. |

### S03 — SARI
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Borsa kapısı: 1.000 $ → Kasım 1929'da ~500 $ → 1932 dibinde ~108 $ | FRH çapaları [D]; 1.000×41,22/381,17 = 108 $ [H] | doğru, nüanslı | Yalnız fiyat, temettü yok. Ekranda "price only, before dividends" alt notu olmalı. |
| Ayakkabı kutusu: fiyatlar ~%30 düştü, 1.000 $ daha çok şey alır | FRH: para arzıyla "equivalent amount" (1930 sonbaharı–1933) [D] | düzeltilmeli | Tüketici fiyatları için FRED `CPIAUCNS`'ten tam değer alınmalı (yıllık ortalama 1929→1933 düşüş yaklaşık dörtte bir civarında [?]). "Prices fell by roughly a quarter" gibi bir ifade, F3'te seriyle kesinleşir. "%30" yalnız FRH'nin genel fiyat ifadesiyle ve dönemiyle birlikte kullanılabilir. |
| Banka kapısı: kayıp oranı | [?] | doğrulanamadı | FDIC tarihi / Fed "Banking and Monetary Statistics" serisinde askıya alınan banka mevduatı ve mudi kaybı. Bulunmazsa "you might lose access to your savings, sometimes for years" dili (sayısız). |
| ABD Eylül 2026 TÜFE yıllık %3,7 | BLS CPI bülteni 14 Ekim 2026 [D/AÖ, bls.gov + dol.gov kopyası] | doğru | "%3,7, 12 months ending September 2026, not seasonally adjusted". |
| 1.000 $'ın 1929 değeri (ortalama yıllık ücret) | [?] | doğrulanacak | BLS / Census tarih tablosu. |
**Neden SARI:** Oyunun sonucu ("the silliest door won") ve 2026 sürprizi ("cash loses today") birlikte izlenince "nakitte durma, şuna yatır" gibi okunabilir. Bu, YouTube'un zararlı/yanıltıcı finans içeriği açısından değil, **tavsiye dili** açısından risk. Çözüm: her kapı sonucu "in that decade, because prices were falling" gerekçesiyle bağlanır. Sonda kişisel çağrı yok. Güvenli yazımlar §3, R2'de. Bu düzeltmelerle F3'te YEŞİL'e iner.

### S04 — YEŞİL (düzeltmeyle)
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| 1903'ten itibaren ödenen sigorta poliçesi tek bir somun ekmeğe yetti | PBS: "insurance policy in 1903… a 20-year policy… cashed it in and bought a single loaf of bread" [D] | doğru, tek kaynak | Tek bir ailenin anısı. Hook: "**One German family** paid into…" veya "**One man's** father…". Genelleme yapılmaz. |
| 1914'te 1 $ = 4–5 mark | PBS [D]; resmi kur 4,2 [AÖ] | doğru | "about four" uygun. |
| Kasım 1923'te 1 $ = 1 trilyon mark | PBS "one trillion" [D]; resmi 4,2 trilyon (20 Kas 1923) [D, Wikipedia/Ahamed + Alman kaynakları] | düzeltilmeli | "more than four trillion marks" (bkz. §1b). |
| Rentenmark oranı | §1b | düzeltilmeli → çözüldü | 1 : 1 trilyon, 12 sıfır. |
| Maaş saat 11'de, bankalar 11'de kapanıyor; Thomas Mann'ın yumurtası 100 milyon | PBS [D] | doğru | Mann alıntısı edebi bir metin, "as the writer Thomas Mann recalled" diye verilecek. |
| Krupp, Thyssen, Stinnes "survived it well" | PBS (Farben de listede) [D] | doğru | Abartılmaz: "profited" değil, "came through it well, some even grew". Stinnes'in büyümesi için ek kaynak F3'te. |
| Borçlular kazandı (mekanizma) | Ders kitabı mekanizması [?] | doğrulanacak (yumuşak) | Mekanizma anlatımı olarak serbest. Rakam verilirse kaynak şart. |
| Ruhr işgali + tazminat → para basma | [?] | doğrulanacak | Ana akım tarih, F3'te tek kaynak yeter. Tazminatın payı tartışmalı, "one big reason" dili. |
**Karalama:** Krupp/Thyssen bugün de yaşayan şirket markaları (thyssenkrupp). "Condoned the inflation" ifadesi PBS'te var, ama "caused" ya da "profiteered" denmez. Siyasi bağ en fazla bir cümle (zaten planlı).

### S05 — SARI
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Ekim 1973'te 2,90 $ → Ocak 1974'te 11,65 $ | FRH [D] | doğru, nüanslı | Bunlar Suudi hafif ham petrolünün **posted price**'ı, piyasa fiyatı değil. Grafikte "posted price" yazılmalı. FRED `WTISPLC` başka seri, iki seri karıştırılmaz. |
| "Almost four times more" | ×4,02 [H] | düzeltilmeli | "about four times as much" / "roughly quadrupled". |
| Ambargo 19 Ekim 1973 – Mart 1974 | FRH [D] | doğru | — |
| Altın 35 $ → 455 $ | FRH (senaryo) | doğru (FRH) | Tarihi belirtilmeli (1980 başı ortalaması mı, zirve mi). F3'te FRH cümlesiyle. |
| "In 2026, oil went above $120" | AP: Haziran Brent vadelisi 30 Nisan'da 125,36 $; Dated Brent spot 3 Nisan'da 141,37 $ (Trading Economics) [AÖ] | doğru | Hangi ölçü olduğu söylenmeli ("Brent futures topped $125 in April"). KH'deki 126,41 $ [?], kullanılırsa kaynak. |
| Brent 16 Ekim 2026 = 109,86 $ | MercoPress "touches $110" (gün içi) [AÖ]. Kalshi piyasa olasılıkları ~100–102 $'a işaret ediyor | doğrulanamadı / çelişkili | Kapanış fiyatı ICE veya EIA verisinden alınmalı. Yoksa "around $100 to $110 in October" denir ya da cümle çıkarılır. |
| Fed Eylül 2026 artırımı, 3,75–4,00 % | federalreserve.gov basın bülteni 16 Eyl 2026 [D] | doğru | — |
| TÜFE %3,7 | BLS [D] | doğru | — |
**Neden SARI:** Süren savaş (hassas olay) ve "1973 = 2026" paralelinin tahmin gibi okunma riski. Başlıktaki "What 1973 Tells Us About Now" tahmin vaadi taşıyabilir. Daha güvenli: "…and What's Different Now". Savaşın kendisi monetizasyon-uyum-uzmani'nin alanı. Benim payım: 2026 rakamlarının ikisi teyitsiz.

### S06 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Mart 2000'de dünyanın en değerli şirketi | Cisco Heritage: 27 Mart 2000, 569 milyar $ (gün içi 82 $) [D]; diğer kaynaklar ~555 milyar $ [AÖ] | doğru | Değer aralığı "over half a trillion dollars" diye söylenir, tek rakam verilmez. "Briefly" eklenmeli. |
| Zirve kapanışı 80,06 $ (27 Mart 2000) | Bespoke / Bloomberg aktarımı [AÖ, 3+ kaynak] | doğru | — |
| ~%90 düştü | 80,06 → 8,12 $ (gün içi dip) = −%89,9 [H]. Kapanış dibi F3'te | doğru | "about ninety percent" uygun. |
| 25 yıl sonra geri döndü: 10 Aralık 2025 kapanışı 80,25 $ | Birden çok kaynak (Yahoo/Bloomberg, Seeking Alpha, EBSCO) [AÖ]. 80,82 $ gün içi değer | doğru | "Its **share price**" denmeli. Temettüler (2011'den beri) dahil edilince toparlanma daha erken, enflasyona göre hâlâ altında. Bu nüans videoda bir cümleyle verilmeli, yoksa yanıltıcı olur. |
| Nasdaq 5.048 → Ekim 2002 −%78 | KH-A4 [AÖ] | doğrulanacak (F3) | FRED `NASDAQCOM`. |
| 2000 F/K oranı | [?] | doğrulanacak | Rakam bulunamazsa mekanizma (pizza dilimi) rakamsız anlatılır. |
**Tavsiye ve karalama:** Alternatif 2 "When a Great Company Was a Terrible Bet" **elenmeli**, çünkü yatırım hükmü veriyor. Bugünkü AI şirketleri (CoreWeave dahil) için "will crash / bubble" hükmü yok, yalnız "the question to ask". CoreWeave'in CDS gibi rakamları kullanılırsa birincil kaynak gerekir (KH'de ikincil). Cisco hakkında yalnız kamuya açık fiyat ve 10-K verisi.

### S07 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| 19 Ekim 1987: −508 puan, −%22,6 | FRH [D]; önceki kapanış ~2.248 [H] | doğru | — |
| 1929'daki her günden kötü | FRH: 28 Ekim ~%13 [D] | doğru | — |
| 7 ayda +%44 (Ağustos 1987'ye) | FRH [D] | doğru | — |
| 16 Ekim −%4,6 | FRH [D] | doğru | "Record point drop" ifadesi için ek kaynak gerekir, yoksa yalnız yüzde verilir. |
| Yeni Zelanda −%60 | FRH: dönem belirtmemiş [D] | düzeltilmeli | "**in the months that followed**" (F3'te dönemle birlikte kaynaklanacak). "That day" asla denmez. |
| Takas uyumsuzluğu "hisse 3 gün, opsiyon 1 gün" | FRH dipnot 10: hisse geliri için 2 gün bekleme, opsiyon/vadeli 1 gün [D] | düzeltilmeli | Gün sayısı FRH dipnotuna göre verilir veya "stocks paid days later, futures demanded cash the next morning" denir. |
| Fed 20 Ekim açıklaması: "affirmed today its readiness to serve as a source of liquidity…" | FRH [D] | doğru | Tam metin federalreserve.gov / FRASER'dan alınacak. |
| 10 büyük NY bankası kredisini ~ikiye katladı; iki seansta kaybın %57'si geri geldi | FRH [D]; 288/508 = %57 [H] | doğru | — |
| 2 yıldan kısa sürede yeni zirve; devre kesiciler 7/13/20 | FRH [D] | doğru | — |
| Saat saat seyir | [?] | doğrulanacak | Brady Commission raporu (1988) ve SEC raporu. Bulunmazsa vaat "moment by moment" olur. |
| 16 Mart 2020 karşılaştırması | [?] | doğrulanacak | S&P 500 −%12 civarı, F3'te birincil. |

### S08 — SARI
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Ocak 1979'da 6 $, Aralık 1979'da 32 $ | ABA [D] | doğru | — |
| Zirve "about forty-nine" | §1a | doğru | Kesin rakam 49,45 $ (18 Oca 1980, Londra fiksi). |
| "Controlled, by one count, more than two-thirds of the world's silver" | ABA: ">69 percent of the world's silver supply", tanımsız [D]. En yaygın tahmin: **hükümetler dışındaki dünya arzının ~üçte biri** (APMEX, Sunshine Profits; ~195 milyon ons) [AÖ]. Spokesman-Review: ~%20 [AÖ] | **düzeltilmeli** | Tek kaynaklı ve aykırı rakam hook'ta kullanılmaz. Güvenli yazım seçenekleri §3, R3'te. |
| 21 Ocak 1980 kural değişikliği satışa zorladı | ABA [D] | doğru | Ayrıntı: Comex "liquidation only" kuralı. F3'te CFTC / Senato raporundan. |
| 27 Mart 1980, 10,80 $ | ABA [D]; −%78,2 [H] | doğru | — |
| Dava / ceza | Ölüm ilanı aktarımı: CFTC ile ömür boyu emtia işlem yasağı ve 10 milyon $ ceza (CFTC manipülasyon iddia etti) [AÖ]. 1988 Minpeco jüri kararı [?] | doğrulanacak | "A jury later found…" cümlesi yalnız mahkeme kaydı veya NYT 1988 kaynağıyla kurulur. "Criminals / thieves / fraud" denmez. Bunun bir medeni dava ve idari yaptırım olduğu söylenir. |
| Kardeşler vefat etmiş mi | Nelson Bunker Hunt (2014, AP aktarımı) [AÖ]. William Herbert Hunt 9 Nisan 2024'te 95 yaşında öldü [AÖ]. Lamar Hunt (ortak yatırımcı) 2006 [?] | doğru | Ölmüş kişiler karalama davası açamaz, ama aile şirketleri ve torunlar yaşıyor. Belgeli olay dışına çıkılmaz. |
| Altın 29 Oca 2026 rekor 5.318 $ → 5 Eki 4.157 $ (−%22) | KH-B3: PriceGold.net (ikincil). Aramada rekor 28–29 Ocak, 5.405–5.602 $ arası (spot/fiks farkı) [AÖ]. 5.318 $ bulunamadı | düzeltilmeli | Ölçüye göre düşüş %21,8 ile %25,8 arası [H]. Metin: "**more than 20 percent below its January record**". Kesin rakam LBMA PM fiksinden alınır. |
**Başlık:** "Tried to Buy All the World's Silver" abartı, çünkü hiçbir kaynak "hepsi" demiyor. Seçenekler: "The Brothers Who Tried to Corner the World's Silver" (51 kr.) / "How Two Brothers Cornered Silver, and Lost It". Thumbnail'daki "ALL THE SILVER" da aynı sorunu taşıyor: "6 → 50" veya "SILVER THURSDAY".
**Çerçeve:** "Heist / soygun" yalnız iç format etiketi olarak kalır. Seslendirilen metinde "steal, heist, villain" yok (manipülasyon bir jüri ve CFTC kararına dayanıyor, hırsızlık değil).

### S09 — SARI
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| 15 Eylül 2008 iflas başvurusu, hafta sonu kurtarma görüşmeleri çöktü | KH-A17 [AÖ]; genel kabul | doğru (F3'te birincil) | Mahkeme dosyası / Fed History. |
| ~30:1 kaldıraç | [?] (Valukas raporu ~30,7x, 2007 sonu, bilgi) | doğrulanacak | Brüt / net kaldıraç farkı (10-K'daki net oran daha düşük) belirtilmeli. |
| Barclays/BoA ayrıntıları, "neden kurtarılmadı" | [?] | doğrulanamadı (şimdilik) | Tartışmalı bir konu. Yetkililerin "yasal yetkimiz yoktu" açıklaması ile Ball (2018) gibi "seçimdi" diyen eleştiri birlikte verilir. Tek görüş "gerçek" diye sunulmaz. |
| Karşı-olgusal sonuçlar | [T] | spekülatif | Her "take" kaynaklı ekonomist görüşüne dayanmalı. "Would have" değil "might have"; ekranda "possibility" etiketi. |
**Yaşayan kişi riski:** Dick Fuld, Hank Paulson, Ben Bernanke, Tim Geithner hayatta. Kararlarına niyet atfeden cümleler ("they let it die to teach a lesson") karalama riski taşır. Yalnız kamuya açık beyanları alıntılanır. 12 `[doğrulanacak]` ile doğrulama yükü en yüksek senaryo bu. Hakem bunu seçerse F3 süresi uzar.

### S10 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Nikkei 29 Aralık 1989 kapanışı 38.915,87; 22 Şubat 2024 kapanışı 39.098,68 | Bloomberg, Business Standard (Reuters), Quartz, birden çok kaynak [AÖ]. Japan Times sayfası ücretli duvarda | doğru | F3'te Nikkei Inc. resmi verisi veya FRED `NIKKEI225`. |
| 1989'un son haftasında doğan bebek 34 yaşında | [H]: 25–29 Ara 1989 doğum → 22 Şub 2024'te 34 yaş | doğru | — |
| 34 yıl bekleme | Endeks fiyat seviyesi | doğru, nüanslı | Temettü dahil toplam getiri daha erken toparlandı. Metin "the **index** got back to that level" demeli. |
| JGB 10 yıllık ~%3, 1996'dan beri en yüksek | Trading Economics (1 ve 15 Eyl 2026, %3,02) [AÖ, 2+ kaynak] | doğru | Ekim seviyesi F3'te güncellenir. |
| Saray arazisi = tüm Kaliforniya | Yaygın ama birincil kaynak yok (CNBC'ye atıf, tarihsiz) [?] | **doğrulanamadı** | Kullanılmaz. İlla kullanılacaksa "a famous claim at the time said…" diye, sayısız, ekranda "claim" etiketiyle. Tercihim: çıkarmak. |
| ~100 trilyon yen batık kredi silindi | [?] | doğrulanacak | FSA / BoJ kaynağı. Bulunmazsa "trillions of yen". |
| Yuki kurgusal | — | — | Ekranda "fictional" etiketi (Ö11). |

### S11 — YEŞİL
| İddia | Kaynak | Durum | Düzeltme |
|---|---|---|---|
| Getiriler 1994–97: 20/43/41/17 % | FRH [D] (net/brüt belirtilmemiş) | doğru | "reported returns" dili. |
| İki Nobel ödüllü (Merton, Scholes, 1997) | FRH "two Nobel laureates" [D] | doğru | — |
| Ağustos 1998'de −%44 | FRH [D] | doğru | — |
| 1997 sonu 1 $ sermayeye ~30 $ borç | FRH (Loomis 1998) [D] | doğru | — |
| 14 firma 3,625 milyar $, %90 pay; Fed kendi parasını koymadı; Buffett teklifi 12:30 son saat | FRH [D] | doğru | Hook'taki "3.6 billion" uygun. |
| "Fund closed end of 1999" | FRH: 1999 sonunda son para iade edildi, kapanış tarihi yok [D] | düzeltilmeli | "By the end of 1999, the rescuers had their money back". |
| Shorts: "With 30-to-1 leverage, a 3% mistake wipes you out" | [H]: 30 borç + 1 sermaye = 31 varlık. %3 düşüş sermayenin %93'ünü siler, tamamı %3,23'te gider | **düzeltilmeli** | "…a drop of **just over 3%** wipes you out" veya "a 3% drop wipes out over 90% of your money". |
| Başlık: "The Nobel-Winning Fund…" | Ödülü fon değil ortaklar aldı | düzeltilmeli | "The Fund With Two Nobel Winners Lost 44% in a Month" (51 kr.) / "Two Nobel Winners, One Fund, a 44% Loss in a Month". |
**Yaşayan kişiler:** Meriwether, Merton, Scholes hayatta. "Arrogant / greedy" gibi karakter yargısı yok, "the model assumed…" dili kullanılacak.

---

## 3. Riskli cümleler: güvenli yeniden yazım seçenekleri (senaryo-yazari seçer)

| # | Riskli | Seçenek A | Seçenek B | Seçenek C |
|---|---|---|---|---|
| R1 (S01) | (kaçınılacak) "Never buy stocks with borrowed money." | "In 1929, that loan only worked while prices went up." | "Borrowing magnified every move, both up and down." | "After 1929, regulators decided how much buyers could borrow." |
| R2 (S03) | "The shoebox won. Today, cash loses, so…" | "In the early 1930s, cash gained value because prices were falling. In 2026, prices are rising, so the same math runs the other way." | "Which door was safest depended on one thing: what prices were doing in that decade." | "This is a history game, not a plan. The point is the mechanism: falling prices helped cash, rising prices hurt it." |
| R3 (S08 hook) | "…controlled, by one count, more than two-thirds of the world's silver" | "…who piled up an estimated third of the world's privately held silver" | "…who built one of the biggest silver positions in history, around two hundred million ounces by some estimates" | "…who held so much silver that the exchange changed its rules" (sayısız, en güvenli) |
| R4 (S06 alt. 2) | "When a Great Company Was a Terrible Bet" | "Cisco 2000: A Great Company at a Sky-High Price" | "It Took Cisco 25 Years to Get Back to 2000" (alternatif 1 zaten var) | "The Best Company of 2000, and a 25-Year Wait" |
| R5 (S05 başlık) | "What 1973 Tells Us About Now" | "The 1973 Oil Shock, and What's Different in 2026" | "When Oil Quadrupled: The 1973 Shock Explained" | "From $2.90 to $11.65: The Oil Shock of 1973" (alternatif 1) |
| R6 (S11 Shorts) | "a 3% mistake wipes you out" | "a drop of just over 3% wipes you out" | "a 3% drop erases more than 90% of your money" | "at 30-to-1, being wrong by about 3% is enough" |

## 4. Mit ve yanıltıcı bilgi kontrolü
- **1929 "pencereden atlayan bankacılar":** Hiçbir senaryoda yok. FRH bu konuya hiç değinmiyor [D]. "Leo 1929'da banker" fikri haklı olarak elendi. F3'te yapılacak grep: `suicide|jump(ed)? from|window|leap` → 0 olmalı.
- **"25 / 34 yıl toparlanma" (S01, S03, S06, S10):** Hepsi nominal fiyat endeksi. Temettü ve enflasyon hesaba katılmadan söylenirse yanıltıcı olur. Her birinde "price" kelimesi veya ekranda kısa bir not şart (ortak kural önerisi, `ortak-dersler`).
- **Weimar "el arabasıyla para":** Senaryoda yok. Kullanılırsa fotoğraf/anı kaynağı gerekir.
- **"Hiperenflasyon Hitler'i getirdi" tek nedenli anlatı (S04):** Tarihçiler 1923 ile 1933 arasında Büyük Buhran'ı da sayar. Tek cümle ve "one of the factors" dili.
- **Tulip mania:** Elendi. Zaten mit tartışmalı bir konu.

## 5. Yasal not taslağı (açıklama için, F8'de youtube-paketleyici kullanır; tüm senaryolar)
> This video is for education and entertainment only. It is not financial, investment, tax or legal advice, and Leo is a fictional cartoon character, not a financial adviser. Historical returns do not predict future results. Any discussion of the future is a possible scenario, not a forecast. Sources are listed below. Narration voice is AI-generated.

Sponsor ya da ortaklık yok, bu yüzden FTC açıklaması gerekmiyor. Ortaklık bağlantısı eklenirse "#ad / affiliate link" satırı zorunlu.

## 6. Test kanıtı

**6a. Kapı: her senaryoda renk + gerekçe.** §0 tablosunda 11/11 satır var, her satırda renk ve gerekçe dolu. §2'de her senaryonun bulgu tablosu var.

**6b. Çelişkiler kaynaklı çözüldü.** §1a: 49,45 $ (ABA + Bloomberg aktarımı + LBMA notu; 48,70 $ = 17 Ocak COMEX kapanışı). §1b: 1 : 10¹² (Ahamed 2009, Alman kaynakları, iç tutarlılık hesabı; PBS'teki ölçek hatası gösterildi).

**6c. Hesaplar betikle (iki koşu `diff` ile aynı):** `python3 -I <scratchpad>/hesap.py`
```
1929 Dow 381.17->41.22: -89.2%, $1000->$108
1929 Dow 63->381.17: x6.05
Marjin %10: ... -5/-10/-20 fiyat -> kalan özsermaye: [5.0, 0.0, -10.0]
Petrol 2.90->11.65: x4.02
Altin 35->455: x13.0
Cisco 80.06->8.12 (gun ici dip): -89.9%
Nikkei 38915.87->39098.68: +0.47%
Bebek 1989-12-25 / 12-29 -> 2024-02-22 yas: 34 / 34
Weimar: oran 1e+12; Rentenmark 1:1e12 -> 1$=4.2 RM | PBS 1e9 olsa 1$=4200 RM (yanlis)
Altin rekor 5318/5405/5502/5602 -> 4157: -21.8% / -23.1% / -24.4% / -25.8%
Gumus 6->49.45: x8.2 ; 49.45->10.80: -78.2%
LTCM 30:1: varlik -3.00% -> sermaye -93%; tam silinme ~ -3.23%
1987: 508/0.226 -> onceki kapanis ~2248; 288/508 = %57
```

**6d. `[doğrulanacak]` sayımı** (`awk`, senaryo bölümleri): S01 6 · S02 8 · S03 8 · S04 6 · S05 8 · S06 5 · S07 5 · S08 5 · S09 12 · S10 8 · S11 0 = **71** senaryo içinde. Dosyanın tamamında 76 (§0 ve notlar dahil). Senaryo yazarının bildirdiği sayı 68, fark etiket yazım biçimlerinden geliyor. Bu turda kritik olanlar çözüldü: iki çelişki, Cisco, Nikkei, TÜFE, Fed, JGB, 2026 petrolü, Hunt payı. Geri kalanlar F3'te seçilen senaryo için tek tek tabloya girer. **F3 kapısı:** metindeki her rakam regex ile çıkarılıp tabloyla karşılaştırılır, doğrulanamayan rakam metinde kalmaz.

**Elenen yaklaşımlar:** (1) Sırf `[doğrulanacak]` sayısına göre renk vermek. Elendi, çünkü S11'de 0 etiket olmasına rağmen hesap hatası çıktı, S08'de az etiket olmasına rağmen hook'taki rakam aykırıydı. (2) Senaryonun kendi risk notunu kabul etmek. Elendi, çünkü S08 "YEŞİL" yazıyordu ama hook'taki pay rakamı ve başlıktaki abartı nedeniyle SARI.

## Kaynaklar (bu çalışmada okunan / aranan)
- [Fed History — 1929](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) · [Great Depression](https://www.federalreservehistory.org/essays/great-depression) · [1987](https://www.federalreservehistory.org/essays/stock-market-crash-of-1987) · [LTCM](https://www.federalreservehistory.org/essays/ltcm-near-failure) — okundu [D]
- [PBS Commanding Heights — German Hyperinflation 1923](https://www.pbs.org/wgbh/commandingheights/shared/minitextlo/ess_germanhyperinflation.html) — okundu [D]
- [Wikipedia — Rentenmark (Ahamed 2009 kaynaklı)](https://en.wikipedia.org/wiki/Rentenmark) — okundu · [DHM LeMO Währungsreform 1923](https://www.dhm.de/lemo/kapitel/weimarer-republik/innenpolitik/waehrungsreform-1923) · [Börsen-Zeitung](https://www.boersen-zeitung.de/konjunktur-politik/vor-90-jahren-das-ende-der-deutschen-hyperinflation) — arama özeti
- [ABA Journal — Hunt brothers](https://www.abajournal.com/magazine/article/panic-1893-hunt-brothers-1980) — okundu [D] · [Scottsdale Mint / Bloomberg](https://www.scottsdalemint.com/articles/2025/bloomberg-asks-when-will-silver-top-its-hunt-brothers-high/) · [Bloomberg Línea](https://www.bloomberglinea.com/mercados/cual-es-el-verdadero-record-de-la-plata-el-debate-resurge-mientras-el-precio-se-dispara/) · [about.ag](https://www.about.ag/SilverHigh.htm) · [APMEX](https://learn.apmex.com/learning-guide/history/silver-thursday-the-hunt-brothers-scheme/) · [Spokesman-Review](https://www.spokesman.com/stories/1998/feb/15/hunts-downfall-set-stage-for-buffett-silver/) · [W. Herbert Hunt ölüm ilanı](https://peoplenewspapers.com/?p=288116) · [N. Bunker Hunt AP](https://www.manufacturing.net/chemical-processing/news/13145886/infamous-oilman-dies-at-88)
- [Cisco Heritage — 2000 market cap](https://heritage.cisco.com/2000_marketcap/) — okundu [D] · [Yahoo/Bloomberg — Cisco record](https://finance.yahoo.com/news/cisco-systems-inc-csco-shares-174059535.html) · [Seeking Alpha](https://seekingalpha.com/article/4852748-cisco-returns-to-dot-com-highs)
- [BLS CPI Eylül 2026](https://www.bls.gov/news.release/archives/cpi_10142026.htm) · [Fed basın bülteni 16 Eyl 2026](https://federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)
- [Trading Economics — Brent](https://tradingeconomics.com/commodity/brent-crude-oil/news/533397) · [Kalshi Brent 16 Eki](https://kalshi.com/markets/kxbrentw/brent-oil/kxbrentw-26oct1617) · [Trading Economics — JGB](https://tradingeconomics.com/japan/government-bond-yield/news/583704)
- [Bloomberg — Nikkei 2024](https://www.bloomberg.com/news/articles/2024-02-22/nikkei-225-heads-to-close-above-record-high-reached-in-1989) · [Business Standard](https://www.business-standard.com/world-news/japan-s-nikkei-stock-index-breaks-its-1989-record-surges-to-all-time-high-124022200344_1.html)
- [SD Bullion — 2026 altın](https://sdbullion.com/gold-prices-2026) (rekor tarih/fiyat aralığı)
- Saray–Kaliforniya iddiası: birincil kaynak bulunamadı ([global-macro-monitor](https://global-macro-monitor.com/2017/03/30/qotd-tokyos-real-estate-bubble-of-the-1980s/), ikincil).
