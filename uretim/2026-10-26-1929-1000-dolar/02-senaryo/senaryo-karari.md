# F2 — Senaryo kararı (hakem) · 2026-10-27

**Slug önerisi: `1929-1000-dolar`** → klasör `uretim/2026-10-26-1929-1000-dolar/` (yeniden adlandırmayı koordinatör yapar).
**KAZANAN: S03 — "You Have $1,000 in 1929. Can You Keep It?"** (Three Doors, One Thousand Dollars)
**YEDEK: S01 — "The 10% Loan That Built the 1929 Crash"** (The Borrowed Ninety Dollars), aynı konu, aynı araştırma.
**Karar kesindir, Niyazi'ye sorulmaz** (Niyazi kararı 2026-10-26). S03 iki taramada SARI, KIRMIZI değil. Aşağıdaki §4 düzeltmeleri **F3 metin kilidinin ön koşuludur**.

Girdi: `senaryolar.md` (senaryo-yazari), `viralite.md` (viralite-analisti, model v0.1), `on-dogrulama.md` (finans-dogrulayici), `politika-on-tarama.md` (monetizasyon-uyum-uzmani), `01-arastirma/konu-havuzu.md`, `01-arastirma/rakip-ozet.md`.
Etiketler: [V] viralite.md · [D] on-dogrulama.md · [P] politika-on-tarama.md · [RÖ] rakip-ozet · [KH] konu-havuzu · [T] hakem tahmini/yargısı.

## 1. Gerekçe (3 madde)
1. **En yüksek ve en sağlam talep + tutma yapısı.** Viralite 8.40, aralık 7.70–8.70. Kötümser puanı bile S01'in temel puanına yakın (7.75). 56 ağırlık oynatmasının hiçbirinde ilk 2'den düşmüyor [V §6]. Konu nişte en çok kanıtlanmış olanı: 1929 üç kanalda ≥10x [V §3]. Hook 9 ve kişisel bağ 9 ile ilk 3'ün en yüksekleri. Sona kadar açık kalan bir döngü var ("which door won… and why the same math runs the other way today"). Bu yapı izlenme süresini taşır, YPP'nin 8.000 saat hedefi için de kritik ölçüt budur.
2. **Kanal kimliği için doğru ilk video.** Leo burada kaybeden değil, oyun sunucusu. Politika uzmanının kanal notu bunu istiyor: "çöküş + Leo kaybeder" kanalın kimliği olmamalı [P §5.1]. S01'de ise Leo kaybeden. Maskot nişte boş bir alan [RÖ §6] ve S03 maskota en doğal rolü veriyor: sunucu + 3 klon. Rakip başlık kalıbı da yok (`benzer_aci` yok [V §2]). Rakipten yalnız "ikinci tekil somut sahne" hook deseni alınıyor, cümleler bize ait.
3. **Riskler düzeltilebilir, ölçüm de bunu gösteriyor.** İki SARI'nın kaynağı aynı: 2026 ters köşesinin tavsiye gibi okunması. Her iki uzman da bunun tek turda YEŞİL'e indiğini yazdı [D S03; P S03-B]. Hakem bileşik puanında (§2) düzeltmelerden önce S01 0.22 önde. Bu fark 0.30 eşiğinin altında, yani eşitlik sayılır, ve eşitliği kural gereği ilk 15 saniye bozar: S03 hook 9, S01 8. Düzeltmeler uygulandıktan sonra S03 8.04 alıyor, S01 7.81. Ağırlıklar ±0.05 oynatıldığında 30 durumun 30'unda kazanan S03. **Karar F3 düzeltmelerinin tutmasına bağlı. Tutmazsa yedek S01 devreye girer (§5).**

## 2. İlk 3: aynı ölçüt tablosu

Bileşik puan = 0.35 × viralite + 0.15 × doğrulama + 0.15 × politika + 0.10 × üretim kolaylığı + 0.15 × kanal kimliği uyumu + 0.10 × özgünlük. Viralite dışındaki puanlar 1–10 arası hakem yargısıdır [T] ve gerekçeleri tablodadır. Betik: `02-senaryo/hakem-karar.py`.

| Ölçüt | **S03** Three Doors | **S01** Borrowed $90 | **S06** Leo's Wrong Belief |
|---|---|---|---|
| Viralite nihai [V] (aralık) | **8.40** (7.70–8.70) | 7.75 (7.30–8.20), seri +0.3 dahil | 7.20 (6.55–7.65), kırılgan (S04 ile fark 0.10) |
| İlk 15 sn (hook) [V] | **9**: ikinci tekil sahne, 3 parçalı açık döngü | 8: somut nesne (10 $ + 90 $ borç) | 8: Leo'nun yanılgısı |
| Doğrulama [D] | SARI → düzeltmeyle YEŞİL · önce 6 / sonra 8 | **YEŞİL** · 9 (2 nüans düzeltmesi) | YEŞİL · 8 (Cisco rakamları [AÖ], F3'te birincil kaynak gerekiyor) |
| Politika [P] | SARI-düşük → B ile YEŞİL · önce 7 / sonra 8 | **YEŞİL** · 9 | SARI-düşük → B ile düşük · önce 7 / sonra 8 |
| Üretim kolaylığı [T] | 6: stüdyo + 3 Leo klonu + 3 kapı + 1929–33 sokakları; çok karakterli kare Canva tutarlılığı için en riskli | **8**: tek sokak, telgraf, "borç doları" nesnesi | 7: iki Leo (2000/2026), ofis; hisse verisi lisansı ◐ [P Ö2] |
| Kanal kimliği uyumu [T] | **8**: Leo sunucu, kaybeden değil; maskot rolü doğal; risk: oyun tonu çocuksu okunabilir | 6: Leo kaybeden (kanal notu [P §5.1]); marjin anlatısı standart | 6: Leo'nun rolü iyi (yanılan), ama A sütununun "büyük çöküş" vaadine en uzak senaryo |
| Özgünlük (rakibe benzerlik) [V §2, RÖ §6] | **9**: kalıp yok; "You have $X in [year]" başlığına ölçülmüş rakip yok | 7: "follow the dollar" rakip-özetin önerdiği karşılık, ama marjin her 1929 belgeselinde var | 7: Nifty Fifty videosuyla aynı tez (8,2x); "AI vs dot-com" komşuluğu |
| **Bileşik, önce** (betik) | 7.59 | **7.81** | 7.07 |
| **Bileşik, düzeltme sonrası** (betik) | **8.04** | 7.81 | 7.22 |
| Leo'nun sonucu (Ö5) | sunucu; "kazanan" kutu klonu 2026'da değer kaybeder | kaybeden: marjin çağrısı, cepler boş | fikrini değiştirir |
| Karar | **KAZANAN** | **YEDEK** | 3. (elendi) |

### Test çıktısı (aynı girdi iki kez → aynı sonuç)
```
$ python3 -I hakem-karar.py   # 1. ve 2. çalıştırma
[once] S01 7.81 | S03 7.59 | S06 7.07  → kazanan S03 (eşit (<0.30), hook belirledi)
[sonra] S03 8.04 | S01 7.81 | S06 7.22  → kazanan S03 (eşit (<0.30), hook belirledi)
[once] ±0.05 ağırlık, 30 durum → kazanan sayısı: S01=9, S03=21
[sonra] ±0.05 ağırlık, 30 durum → kazanan sayısı: S03=30
$ diff h1.txt h2.txt → fark yok · sha256 her ikisi c4544f46df5827e1…
```
**Dürüst okuma:** Bugünkü renklerle S03 kesin bir kazanan değil. Ağırlık oynatmalarının 9/30'unda S01'in farkı 0.30'u geçiyor ve S01 kazanıyor. Bu 9 durumun tamamında ağırlık viralite, kimlik ya da özgünlükten alınıp doğrulama, politika ya da üretime verilmiş (betikle listelendi). S03 ancak zorunlu düzeltmeler uygulanınca 30/30 sağlam kazanan oluyor. Bu yüzden düzeltmeler isteğe bağlı değil, F3 kapısı. Yedeğe geçiş tetikleri de §5'te ölçülebilir şekilde yazıldı.

## 3. Neden kaybedebilir (şeytanın avukatı, her biri için)

`roast` 5 açısı elle uygulandı: eleştirmen, savunucu, analist, araştırmacı, izleyici. Skill çağrılmadı, çünkü giriş soruları alt ajanda yanıtlanamıyor.

### S03 (kazanan) neden kaybedebilir
1. **Tavsiye okuması (izleyici + eleştirmen).** "Kutu kazandı, bugün nakit kaybeder" birlikte izlenince AI maskotun para yönlendirmesi gibi görünür. K4 bu konuda izinli örnek vermiyor [P]. Kanalın ilk videosu politika kimliğini belirler. → **Panzehir:** §4 P1–P3, D7. Uyarı etiketi tek başına sorunu çözmez [P S03-C].
2. **Banka kapısının sayısı yok (analist).** Mevduat kaybı oranı doğrulanmadı [D]. Skor tablosunda banka kapısı sayısız kalırsa üç kapının "yarışı" dengesizleşir. → Sayısız dil kabul edilebilir ("you might lose access… sometimes for years"), yeter ki bu kapının vaadi "gamble" olarak kalsın. Sayı uydurulmaz.
3. **Çocuksu ton (eleştirmen).** Oyun formatı tarih derinliğini zayıflatıp ilk videoda kanalı "çocuk içeriği" gibi gösterebilir [V §5]. Bu ayrıca "made for kids" sınıflandırma riski demek [T]. → Her kapı bölümünde en az 1 birincil veri olacak, ≥3 kaynak etiketli grafik (Ö2), yetişkin anlatım tonu. Leo'nun klonları komik olabilir, anlatı ciddi kalır.
4. **Tahmin edilebilir cevap (izleyici).** "Hayır, tutamazsın" baştan belli. Merakı thumbnail'daki üç kapı ve "surprise" kapısı taşımak zorunda. Başlık soru işaretiyle bitiyor ve bu kalıbın medyan skoru 0,91 [RÖ §4]: hafif eksi. → Başlık/thumbnail testi F8'de (Test & Compare).
5. **Üretim zorluğu (araştırmacı).** Aynı karede üç tutarlı Leo, Canva'nın en zayıf noktası. → Klonları tek tek üretip Remotion'da katman olarak birleştirmek (2D rig kopyalanabilir). Bu sahne F5 kritik yol testine zorunlu olarak girer (§4 H4).
6. **Seri şablon riski.** Aynı oyun 1923/1973/2008'de tekrarlanırsa "aynı durum, aynı sonuç" olur [P, K4] → kanal kuralı §4 P6.
**Sağ kaldı mı?** Evet, şartlı. 1, 2 ve 6 için kaynaklı panzehir var. 3, 4 ve 5 uygulama riski, F3/F5/F8 kapılarında ölçülecek.

### S01 (yedek) neden kaybedebilir
1. "Bunu biliyorum" etkisi: marjin her 1929 belgeselinin standart parçası [V].
2. Başlıktaki "10%" faiz gibi okunabilir, merak yanlış yere gider [V]. Thumbnail'daki "10% DOWN" bunu çözmek zorunda.
3. Leo kaybeden. İlk video olursa "kayıp formülü" kimliği başlar [P §5.1]. Sonraki A videosunda Leo kaybeden olamaz.
4. Kişisel bağ dolaylı (6): genç izleyicinin çoğu marjin kullanmıyor.

### S06 (3.) neden kaybedebilir, ve neden yedek değil
1. 4. sıradaki S04 ile fark yalnız 0.10. Model v0.1 bu ikisini ayıramıyor (12/56 [V §6]).
2. Cisco'nun bütün rakamları [AÖ]. SEC EDGAR'dan birincil kaynak ve hisse verisi lisansı gerekiyor, F3 yükü sıfırdan.
3. AI gündemi soğursa zamanlama puanı (9) çöker. Stok video için bu risk.
4. Genç izleyici Cisco'yu tanımayabilir. Tek şirket, A sütununun "büyük çöküş" vaadine uzak.
5. "Here's what I believe now" + "GOOD COMPANY + GOOD PRICE" = AI personasının yatırım ipucu vermesi [P S06].

## 4. Zorunlu F3 düzeltme listesi (S03, metin kilidinin ön koşulu)

`senaryo-yazari` uygular. `finans-dogrulayici` ve `monetizasyon-uyum-uzmani` F3'te her maddeyi yeniden ölçer. Hedef: iki raporda da **YEŞİL**.

**Doğrulama ([D] S03 + §3 R2):**
- **D1.** Borsa kapısı: 1.000 $ → Kasım 1929 ortası ~500 $ → Temmuz 1932 ~108 $ (1.000 × 41,22 / 381,17 [H]). Ekranda ve grafikte **"price only, before dividends"** alt notu olacak.
- **D2.** Ayakkabı kutusu: "%30 fiyat düşüşü" bu haliyle kullanılmaz. Tüketici fiyatlarındaki düşüş FRED `CPIAUCNS`'ten kesin değerle verilir (1929→1933; "roughly a quarter" gibi, seriyle kesinleşir). FRH'nin "~%30" ifadesi yalnız kendi dönemiyle (1930 sonbaharı–1933 kışı) ve kendi bağlamıyla kullanılabilir.
- **D3.** Banka kapısı: kayıp/askıya alınan mevduat oranı FDIC tarihi ya da Fed "Banking and Monetary Statistics" (1943) kaynağından alınacak. **Bulunamazsa sayısız dil**: "you might lose access to your savings, sometimes for years". Skor tablosunda banka kapısına rakam yazılmaz, yerine risk simgesi konur. Sayı uydurulmaz.
- **D4.** 2026 enflasyonu: "3.7%, 12 months ending September 2026, not seasonally adjusted" (BLS, 14 Ekim 2026).
- **D5.** 1.000 $'ın 1929'daki değeri (ortalama yıllık ücret) BLS veya Census tarih tablosundan. Kaynak yoksa cümle çıkar.
- **D6.** "1954'e kadar dönüş yok" ifadesi → "**The Dow's price** didn't get back to its 1929 peak until 1954" + temettü ve deflasyon nüansı tek cümle ([D] S01 düzeltmesiyle aynı).
- **D7.** Her kapının sonucu "**in that decade, because prices were falling**" gerekçesine bağlanır. Sonda kişisel çağrı yok. R2'deki A/B/C seçeneklerinden biri kullanılır.

**Politika ([P] S03, Seçenek B):**
- **P1.** 2026 ters köşesi mekanizma cümlesi olacak, ör.: "In 1929 prices fell, so cash gained power. In 2026 prices rise, so cash loses power. That's arithmetic, not a recommendation." Senaryo yazarı bunu ya da R2-A'yı seçer, ama cümle bugüne dönük bir hüküm vermez.
- **P2.** Shorts kancası "Most people picked wrong." → "**In 1929, most people would have picked the wrong door.**" 2. Shorts ("…and loses today") aynı mekanizma diliyle yeniden yazılır.
- **P3.** 15–30 sn köprüsündeki "Where do I keep my money?" → "**Where was money safe in 1929?**" Köprünün vaadi "why the same door would lose today" → "why the same math runs the other way today".
- **P4.** Uyarı etiketiyle kapatmak (Seçenek C) **yasak**: etiket personayı uygun hale getirmez [P].
- **P5.** `sentetik_medya = true` ön kararı ve açıklamada "Narration voice is AI-generated" satırı [P §5.2]. 1929–33 sokak sahneleri gerçekçi üretilirse ekranda "Illustration" etiketi olacak (Ö11). Stüdyo sahneleri bundan muaf.
- **P6.** Kanal kuralı (`showrunner`'a): oyun formatı en erken 5 video sonra tekrar edilebilir. Tekrarda Leo'nun rolü, kapı sayısı ve sonuç farklı olur. Bunu `monetizasyon-uyum-uzmani` her 5 videoda bir denetler.

**Hakem ekleri (kanal kimliği / üretim):**
- **H1.** Tarih derinliği: her kapı bölümünde ≥1 birincil kaynaklı veri, toplamda ≥3 kendi veri grafiği ekranda kaynak etiketiyle (Ö2). Oyun tonu yalnız görselde, anlatım yetişkin tonda.
- **H2.** Kutu Leo'nun 2026 anı kayıp ya da aşağılanma gibi değil, mekanizma görseli gibi verilir (banknotlar küçülür, grafik yanında). Sunucu Leo kaybetmez.
- **H3.** Hook kelimesi kelimesine kalabilir (≤40 kelime ✓). Hook ilk 15 sn'de vaadi veriyor. İlk görsel değişim ≤3 sn olmalı (stüdyo → kapılar), bu retention kapısı için F7'de ölçülür.
- **H4.** F5 kritik yol testine (10–20 sn) **3 Leo klonlu kapı sahnesi** zorunlu girer. Tutarlılık kapısı geçmezse B planı: tek Leo kapıdan kapıya yürür, klonlar yalnız skor tablosunda ikon olur.
- **H5.** F8 (`youtube-paketleyici` + `thumbnail-tasarimcisi`): başlık sabit kalır, 3 thumbnail Test & Compare ile denenir [V §7]. Soru işaretsiz bir alternatif başlık (ör. alternatif 2 "Stocks, a Bank or a Shoebox: Who Survived 1929?") pakette yedek olarak durur.

## 5. Yedek (S01): ne zaman kullanılır
**Neden S01, neden farklı konu değil:** Yedeğin işi aynı slotu kurtarmak (hedef 2026-11-01). S01 aynı 1929 FRH araştırmasını kullanıyor ve iki taramada da YEŞİL, yani F3'e en hızlı dönen seçenek. S06 farklı konu olurdu ve kanal çeşitliliği açısından cazip. Ama F3 araştırmasına sıfırdan başlamak gerekir (Cisco birincil kaynak, hisse verisi lisansı), politika SARI kalır ve zamanlaması bozulabilir. 3. sıradaki S06 ile S04'ün ayrımı da güvenilir değil.
**Yedeğe geçiş tetikleri (herhangi biri):**
1. F3'te 2 düzeltme turundan sonra `finans-dogrulayici` ya da `monetizasyon-uyum-uzmani` S03'ü hâlâ YEŞİL'e indiremezse (CLAUDE.md eskalasyon kuralı).
2. F5 kritik yol testinde hem kapı sahnesi hem H4'teki B planı görsel tutarlılık kapısından kalırsa.
3. D3 sonrası doğrulayıcı skor tablosunun yanıltıcı olduğuna karar verirse (sayısız dil yetmezse).
**S01 kullanılırsa zorunlu düzeltmeler:** hook'ta "with **as little as** ten dollars of your own"; "The Dow's price didn't get back… until 1954"; tavsiye cümleleri yerine R1 seçenekleri; 1934 Reg T ve FINRA marjin verisi birincil kaynaktan; gerçekçi sokak sahnelerinde "Illustration" etiketi; intihar miti yok. Kanal kuralı: sonraki A videosunda Leo kaybeden olmaz.
**S03 yayınlanırsa S01'in durumu:** havuza döner. S03'ten hemen sonra yayınlanmaz (aynı konu, Ö5/Ö7). En erken 4 video sonra ve F12 7. gün verisi 1929 talebini doğrularsa S02 ile birlikte "1929 dizisi" olarak değerlendirilir. **S06 ve S04** sonraki A/C stok adayları olarak kalır.

## 6. Riskler (karar düzeyi)
| Risk | Olasılık [T] | Etki | Önlem / sahibi |
|---|---|---|---|
| F3 düzeltmeleri twist'i öldürür, tutma düşer | düşük | orta | P1 mekanizma cümlesi twist'i korur [P: viralite kaybı düşük] · senaryo-yazari |
| Banka kapısı sayısız kalır | orta | düşük-orta | D3 sayısız dil + "gamble" vaadi · finans-dogrulayici |
| 3 klon sahnesi Canva'da tutarsız | orta | orta | H4 kritik yol + B planı · animasyon-yonetmeni, gorsel-varlik-sanatcisi |
| Çocuksu ton / made-for-kids algısı | düşük-orta | yüksek (ilk video) | H1, yetişkin anlatım; F8'de "made for kids = hayır" gerekçeli · monetizasyon-uyum-uzmani |
| Model v0.1 güveni düşük (bütün viralite puanları tahmin) | — | — | F12 kalibrasyonu; `yt-analytics.readonly` kapsamı gerekli [V §7] · koordinatör |
| 29 Ekim yıldönümü geçmiş olacak (yayın 1 Kasım) | kesin | düşük | Stok/raf ömrü uzun, yıldönümü hook'ta kullanılmıyor |
| Slot 2026-11-01'e yetişmez | orta | düşük | Takvim kuralı: 2026-11-08 · koordinatör |

## 7. Karar kaydı (decision log)
- **Karar:** S03 kazanan, S01 yedek, slug `1929-1000-dolar`. **Karar veren:** hakem. **Tarih:** 2026-10-27. **Geri dönüş koşulu:** §5 tetikleri.
- **Değerlendirilen seçenekler:** (a) S03 şartlı (düzeltmelerle) **seçildi**; (b) S01, risk en düşük, ama kanal kimliği ve viralite eksi, bileşikte eşit bantta ve hook'ta kaybetti; (c) S06, kırılgan 3. sıra, F3 yükü ağır.
- **Varsayımlar:** F3 düzeltmeleri bir turda yapılabilir (iki uzmanın görüşü); viralite v0.1 sıralaması yön olarak doğru.
