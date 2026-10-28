# F2 — Viralite sıralaması (viralite-analisti) · 2026-10-27

**Model:** `docs/viralite-modeli.md` **v0.1**. Güven **DÜŞÜK**: ağırlıklar ±0.05 belirsiz, 0.3'ten küçük farklar anlamlı değil.
**Bütün puanlar tahmindir [T].** Hesap elle yapılmadı, `tools/viralite.py` ile yapıldı.
**Girdi:** `02-senaryo/viralite-girdi.json` (11 senaryo; temel puan + kötümser/iyimser aralık) · `viralite-girdi-varyant.json` (3 yargı varyantı) ·
`viralite-outlier.json` (rakip yerel medyan ölçümü, üreten betik `viralite-outlier.py`) · duyarlılık betiği `viralite-duyarlilik.py`.
**Etiketler:** [API] YouTube Data API v3 ölçümü (2026-10-27) · [H] API sayısından hesap · [RÖ] `01-arastirma/rakip-ozet.md` · [KH] `01-arastirma/konu-havuzu.md` · [T] tahmin.

## 0. Sonuç (hakeme)

| Sıra | ID | Çalışma başlığı | Nihai [T] | Aralık (kötümser–iyimser) |
|---|---|---|---|---|
| **1** | **S03** | You Have $1,000 in 1929. Can You Keep It? | **8.40** | 7.70–8.70 |
| **2** | **S01** | The 10% Loan That Built the 1929 Crash | **7.75** | 7.30–8.20 |
| **3** | **S06** | The Best Company of the Dot-Com Era Still Fell 90% | **7.20** | 6.55–7.65 |
| (4) | S04 | Weimar 1923: Who Got Rich While Money Died? | 7.10 | 6.65–7.55 |

- **1. ve 2. sıra sağlam.** S03 ile S01 arasında 0.65, S01 ile 3. sıra arasında 0.55 fark var. 56 ağırlık oynatmasının hiçbirinde ilk ikiden biri ilk 3'ün dışına düşmedi.
- **3. sıra KIRILGAN: hakeme bildirim.** S06 ile S04 arasındaki fark 0.10 (eşik 0.3). Ağırlıklar ±0.05 oynatılınca 56 durumun 12'sinde 3. sıraya S04 geçiyor (§5). Model v0.1 bu ikisini ayıramıyor. S07 (7.00) de aynı bantta. **3. sıra için karar hakemin**; finans-dogrulayici ve monetizasyon-uyum-uzmani raporları bu bandı ayırabilir.
- **S03 ile S01 aynı konu (1929).** İkisi aynı videoya iki ayrı açı. Hakem birini seçerse diğeri aynı araştırmayla hazır bir yedek olur, ama ardışık yayınlanmamalı (Ö5/Ö7). Hakem farklı konuda bir yedek isterse 3. sıradaki S06 veya S04'e bakmalı.
- **Sert eleme henüz uygulanmadı.** Bütün senaryolarda `ana_iddia_dogrulandi=true` geçici. finans-dogrulayici paralel çalışıyor. Onun raporu bir ana iddiayı düşürürse girdi güncellenip betik yeniden çalıştırılır.

## 1. Betik çıktısı (test kapısı: aynı girdi iki kez → aynı sonuç)

```
$ python3 tools/viralite.py uretim/2026-10-26-1929-1000-dolar/02-senaryo/viralite-girdi.json   # 1. ve 2. çalıştırma
Viralite modeli v0.1 | ağırlık toplamı = 1.00 | puanlar TAHMİNDİR [T]

| Sıra | ID | Başlık | Ağırlıklı | Bonus | Ceza | Nihai | Not |
|---|---|---|---|---|---|---|---|
| 1 | S03 | You Have $1,000 in 1929. Can You Keep It? | 8.40 | +0.00 | −0.00 | **8.40** | - |
| 2 | S01 | The 10% Loan That Built the 1929 Crash | 7.45 | +0.30 | −0.00 | **7.75** | seri +0.3 |
| 3 | S06 | The Best Company of the Dot-Com Era Still Fell 90% | 7.20 | +0.00 | −0.00 | **7.20** | - |
| 4 | S04 | Weimar 1923: Who Got Rich While Money Died? | 7.10 | +0.00 | −0.00 | **7.10** | - |
| 5 | S07 | The Day Stocks Fell 22.6%, and Why Nothing Broke | 7.00 | +0.00 | −0.00 | **7.00** | - |
| 6 | S09 | What If Lehman Brothers Had Been Saved in 2008? | 6.65 | +0.00 | −0.00 | **6.65** | - |
| 7 | S02 | The 1929 Crash Was Only the First Domino | 7.40 | +0.30 | −1.50 | **6.20** | seri +0.3; benzer_aci −1.5 |
| 8 | S10 | Japan's 1989 Bubble Took 34 Years to Heal | 6.15 | +0.00 | −0.00 | **6.15** | - |
| 9 | S11 | The Nobel-Winning Fund That Lost 44% in a Month | 5.95 | +0.00 | −0.00 | **5.95** | - |
| 10 | S08 | The Brothers Who Tried to Buy All the World's Silver | 7.40 | +0.00 | −1.50 | **5.90** | benzer_aci −1.5 |
| 11 | S05 | When Oil Quadrupled: What 1973 Tells Us About Now | 6.55 | +0.00 | −1.50 | **5.05** | benzer_aci −1.5 |

$ diff v1.txt v2.txt && echo "diff: fark yok"; sha256sum v1.txt v2.txt
diff: fark yok
85897fcfa6419825f929e87788ce05f27efd876e003a06a3b0b8a8e8d8aab0e3  v1.txt
85897fcfa6419825f929e87788ce05f27efd876e003a06a3b0b8a8e8d8aab0e3  v2.txt

$ python3 -c "...assert sum(v.AGIRLIK.values())==Decimal('1.00')..."
assert OK: toplam 1.00

$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md
Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
```
Duyarlılık betiği de iki kez çalıştırıldı, `diff` sonucu fark yok (§5).

## 2. Ölçüt puanları (temel; parantezde kötümser–iyimser aralık) [T]

Ağırlıklar: merak 0.20 · talep 0.15 · hook 0.10 · kişisel 0.15 · zamanlama 0.10 · hikâye 0.15 · görsel 0.10 · raf 0.05.

| ID | Merak | Talep | Hook | Kişisel | Zaman | Hikâye | Görsel | Raf | Seri | Benzerlik |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 7 (6–8) | 9 | 8 | 6 (5–7) | 7 (6–8) | 7 | 8 | 9 | evet | yok |
| S02 | 7 (6–8) | 9 | 7 | 7 | 7 | 7 | 7 (6–8) | 9 | evet | **benzer_aci** |
| S03 | 8 (7–9) | 9 | 9 (8–9) | 9 (8–9) | 7 (6–8) | 8 (7–8) | 9 | 8 | hayır | yok |
| S04 | 7 (6–8) | 4 (3–5) | 8 | 7 | 7 (6–8) | 8 | 9 | 9 | hayır | yok |
| S05 | 6 | 6 (5–7) | 6 | 8 | 9 (8–9) | 5 (4–6) | 7 | 6 | hayır | **benzer_aci** |
| S06 | 8 (7–8) | 7 (6–8) | 8 | 6 (5–7) | 9 | 6 (5–7) | 7 | 7 | hayır | yok |
| S07 | 8 (7–8) | 4 (3–5) | 8 | 5 | 7 | 9 (7–9) | 8 | 8 | hayır | yok |
| S08 | 8 (7–9) | 8 (7–8) | 8 | 4 (3–4) | 5 | 9 | 9 | 9 | hayır | **benzer_aci** |
| S09 | 7 | 7 (6–8) | 7 | 5 | 6 | 7 (6–8) | 7 | 8 | hayır | yok |
| S10 | 7 | 4 (4–5) | 8 | 6 | 5 | 5 (4–6) | 8 | 8 | hayır | yok |
| S11 | 7 | 4 (4–5) | 7 (6–7) | 3 | 4 | 8 | 8 | 8 | hayır | yok |

Her başlıkta somut özne var (yıl, ülke, kişi, kurum ya da nesne), bu yüzden merak tavanı (≤6) hiçbir senaryoya uygulanmadı.
S06'da şirketin adı başlıkta bilerek saklanıyor. "The Best Company of the Dot-Com Era" belirli bir kurumu gösterdiği için somut sayıldı.

### Belirsiz ölçütlerde 3 gerekçe (iyimser / temel / kötümser), yalnız sıralamayı etkileyenler
- **S03 merak (9/8/7).** İyimser: ikinci tekil + para + yıl, izleyici kendini yerleştiriyor (öz-referans etkisi, `marketing-psychology`), soru başlıkta açık. Temel: güçlü, ama "Can you keep it?" cevabı tahmin edilebilir ("hayır"); merakı asıl üç kapı thumbnail'ı taşır. Kötümser: "oyun" formatı ilk videoda kanal kimliği oturmadan çocuksu okunabilir.
- **S01 kişisel bağ (7/6/5).** İyimser: borçla alım bugün de var (marjin, kaldıraçlı ürünler, "buy now pay later": Grant Rudow 4,8x [RÖ §1]). Temel: genç izleyicinin çoğu marjin kullanmıyor. Bağ mekanizma üzerinden kuruluyor, cepten değil. Kötümser: "10%" başlıkta faiz oranı gibi okunabilir, vaat bulanıklaşır.
- **S06 talep (8/7/6).** İyimser: tezin aynısı ("harika şirket, kötü fiyat") Casual Finance'in Nifty Fifty videosunda 8,2x [API][H]; AI balonu köprüsü New Money'de 28x [RÖ D2]. Temel: konu düzeyinde ölçülmüş tek ≥3x var ve o da komşu bir konuda (1973 Nifty Fifty, Cisco değil). Kötümser: "AI vs dot-com" kalıbında Infographics yalnız 1,45x [RÖ D2]; Cisco'ya özel video ölçülmedi (arama kotası dolu).
- **S06 hikâye (7/6/5).** Gerilim Leo'nun kendi inancında, dışarıda bir kötü adam yok. Kötümser okumada "fiyat/kâr makası" anlatısı soyut kalıyor.
- **S04 talep (5/4/3).** Weimar'da 12 ayın en iyisi 48 K ve yerel medyanda 1,29x [API]. Markets of the Past'in Weimar videosu 38,9 K, kanal medyanının altında [RÖ D2]. Hiperenflasyon kategorisinin medyan skoru 0,65 [RÖ D2]. Wikipedia +%17 [KH]. Çapa tablosuna göre "işleniyor ama outlier yok" = 3–4.
- **S07 hikâye (9/9/7).** Saat saat gerilim en güçlü yapı. Kötümser durum: saatlik veri bulunamazsa vaat "moment by moment"a düşer ve gerilim azalır (senaryo risk notu).

### Rakip benzerlik kararları (model v0.1 cezası; ilk 3'ü etkileyen yargılar)
Model metni Türkçe dönem için yazıldı ("TR'ye taşıyor", "doğrudan çeviri"). Kanal artık İngilizce yayın yapıyor. Bu yüzden şöyle yorumladım: `benzer_aci` = rakibin başlık kalıbını ya da tez kurgusunu İngilizcede aynen tekrar etmek; `dogrudan_ceviri` = global bir başlığın birebir ya da neredeyse birebir kopyası. Model metninin v0.2'de buna göre düzeltilmesini öneriyorum (§8).
- **S02 → benzer_aci.** Tez ve kurgu ("bilinen 1929 hikâyesi eksik, çöküş bir semptomdu, asıl yıkım sonra geldi") son 12 ayda iki rakipte birebir işlendi: Markets of the Past "The True Origin of The Great Depression: What Historians Get Wrong" (hook: "The crash was a symptom", 7,6x [API]) ve Uncover Things "1929 WASN'T THE REAL CAUSE" (199 K [RÖ D4]). Bu kalıbın 119 videoda medyan skoru 0,55 [RÖ §4]. Başlık kalıptan kaçıyor, kurgu kaçmıyor. **Varyant:** ceza olmasa S02 7.70 alıp 2. sıraya çıkardı (§6). Bu, ilk 3'ü etkileyen en büyük tek yargı.
- **S08 → benzer_aci.** Çalışma başlığı "The Brothers Who Tried to Buy All the World's Silver", bu konunun tek güçlü outlier'ının başlığıyla aynı çekirdeği taşıyor: Investigate Money "They Bought Nearly All the World's Silver. It Ended in Disaster" (30,8x [API]). Thumbnail metni "ALL THE SILVER" da aynı. **Varyant:** alternatif 2 başlığıyla ("Silver Thursday: The Day the Hunt Brothers Fell") ceza kalkıyor, merak 7'ye iniyor ve S08 7.20 alarak 3. sıradaki bantla eşitleniyor (§6).
- **S05 → benzer_aci.** "What 1973 Tells Us About Now", The Economist'in "Energy crisis: what can 1973 teach us?" başlığının (437 K [KH ölçüm]) neredeyse aynısı.
- **S06 → yok.** Senaryo-yazari Infographics "AI vs dot-com" riskini işaretlemişti. Başlıkta AI yok; açı tek bir şirket artı Leo'nun yanılgısı. Rakibin kurgusu (genel balon karşılaştırması) taşınmıyor. Nifty Fifty tezi aynı ama dönem, şirket ve başlık farklı. Bu yüzden kanıt olarak kullanıldı, ceza verilmedi.
- **S01, S03, S04, S07, S09, S10, S11 → yok.** En yakın rakip başlıkları §3'te; hiçbiri kalıp ya da kurgu olarak taşınmıyor.

### Seri bonusu
- **S01 ve S02: evet.** 1929 → 1933 doğal olarak iki bağımsız bölüme ayrılıyor: çöküş ve marjin (S01), bankalar ve para arzı (S02). İkisinin de kendi doruğu var (marjin matematiği / 1933 banka tatili). S01 yapısı S02'ye köprüyü zaten bırakıyor. **Varyant:** bonus olmasa S01 7.45 alır ve yine 2. kalır (§6).
- **S03: hayır.** "Aynı oyun 1923/1973/2008'de" bir **format serisi**, konunun bölünmesi değil. Model tanımı yalnız konunun bölünmesini ödüllendiriyor. Format serisinin kanal için değeri gerçek (geri dönen izleyici) [T]. v0.2'de ayrı ele alınmalı.

## 3. Kanıt: her senaryo için en yakın rakip outlier

Ölçüm: `viralite-outlier.py` → `viralite-outlier.json` [API][H]. Skor = izlenme ÷ hedef hariç çevredeki 10 uzun (≥4 dk) yüklemenin medyanı (model v0.1 yerel medyan tanımı). Yalnız `videos`, `channels` ve `playlistItems` uç noktaları kullanıldı (arama kotasına dokunulmadı).

| Senaryo | En yakın video (kanal, abone) | Yayın | İzlenme | Yerel medyan | Skor | Kanıt gücü |
|---|---|---|---|---|---|---|
| S01/S02/S03 (1929) | The Great Depression of 1929: When the Dream Collapsed (SLICE History, 301 B) | 2025-11-02 | 540.465 | 13.989 | **38,6x** | ≥10x |
| S01/S02/S03 | The Crash Pattern They Ignored in 1929 Is Back — And 2026 Is Next (The Money Files, 4,8 B) | 2025-12-18 | 22.351 | 1.300 | **17,2x** | ≥10x (küçük kanal) |
| S01/S02/S03 | The Great Depression in 12 Minutes (Casual Economics, 93 B) | 2025-03-19 | 3.135.409 | 199.763 | **15,7x** | ≥10x (12 ay dışı) |
| S02 (açı) | The True Origin of The Great Depression: What Historians Get Wrong (Markets of the Past, 99,9 B) | 2026-07-09 | 422.514 | 55.507 | **7,6x** | ≥3x, ceza gerekçesi |
| S02 (banka kaçışı) | 1907: The Day Americans Couldn't Get Their Money Back (Investigate Money) | 2025-12-25 | 58.996 | 32.098 | 1,8x | outlier yok |
| S03 (açı) | Konu düzeyinde yukarıdaki 1929 kanıtı. Açı düzeyinde ikinci tekil somut sahne hook'u n=3 [RÖ D5, ALT]: Mayfair 349 B, Skibbereen 231 B, stat 130 B. "You have $X in year" başlığına ölçülmüş outlier yok | — | — | — | — | konu ≥10x, açı yok |
| S04 | Karl and Anna: A Year Inside the Weimar Hyperinflation (Independent Financial Historian, 37,8 B) | 2026-02-28 | 48.445 | 37.481 | 1,3x | outlier yok |
| S05 | The 1973 Stock Market Crash that Nobody Remembers (Casual Finance, 425 B) | 2025-10-03 | 1.285.679 | 157.063 | **8,2x** | ≥3x, komşu konu |
| S05 | Why The Oil Crisis is Way Worse Than You Think (Asian Boss, 4,17 M) | 2026-04-03 | 1.573.859 | 727.032 | 2,2x | — |
| S06 (tez) | The 1973 Stock Market Crash that Nobody Remembers (Nifty Fifty: "harika şirket, aşırı fiyat") | 2025-10-03 | 1.285.679 | 157.063 | **8,2x** | ≥3x, aynı tez |
| S06 (konu) | AI Bubble vs Dot Com Crash (The Infographics Show) [RÖ D2] | 2026-07-18 | 610.622 | 420.083 (son 20) | 1,45x | — |
| S07 | Black Monday: The Biggest Crash EVER! (Finance Bureau, 129 B) | 2026-10-22 | 46.565 | 97.132 | **0,48x** | outlier yok; video ölçümde 5 günlük, karşı kanıt olarak zayıf |
| S08 | They Bought Nearly All the World's Silver. It Ended in Disaster (Investigate Money, 26 B) | 2026-07-18 | 312.451 | 10.147 | **30,8x** | ≥10x, tek kanal |
| S08 | How Two Oil Tycoon Bought Too Much Silver… (History Meets Finance, 149 B) | 2025-07-05 | 50.522 | 105.555 | 0,48x | karşı kanıt |
| S09 | The 2008 Financial Crisis Explained Like You're 5 (Fred - Money Historian, 5 B) | 2026-03-04 | 245.402 | 21.231 (n=5) | **11,6x** | ≥10x ama komşu n=5, zayıf |
| S09 | The 2008 Financial Crisis Explained Using Bananas (MonkeyExplains, 248 B) | 2025-11-07 | 212.529 | 454.615 | 0,47x | karşı kanıt |
| S10 | The Economic Crisis We Learned Nothing From (How Business Worked, 299 B) | 2025-12-17 | 414.245 | 240.296 | 1,7x | outlier yok |
| S11 | The Most Dangerous Hedge Fund in History (Hamish Hodder, 391 B) | 2025-11-15 | 1.037.719 | 428.709 | 2,4x | outlier yok |

**Talep puanlarının çapa karşılığı:** 1929 (S01–S03) aynı konuda ≥10x ve ≥2 kanal → **9** (10 verilmedi: kazananlar ya belgesel ya "bugünle bağ" açısında, bizim açılarımızın birebir kanıtı yok). S08 ≥10x ama tek kanal, diğer kanalda 0,48x → **8**. S06 aynı tez ≥3x tek kanal → **7**. S09 ≥10x ama komşu sayısı 5 ve karşı örnek 0,47x → **7**. S05 komşu konu ≥3x → **6**. S04, S07, S10 ve S11'de outlier yok, aramada ilgi var → **4**.

**Önemli yeni bulgu (rakip-ozet'i düzeltiyor):** Markets of the Past'in Great Depression videosu son-20 medyanına göre 4,4x [RÖ], **yerel medyana göre 7,6x** [API]. Bunun nedeni kanalın büyümesi: son 20 video ortalamayı yukarı çekiyor. Yerel medyan tanımı kanalın büyümesini düzeltiyor, eski videoları haksız yere küçültmüyor. Model v0.1'in yöntem seçimi bu örnekte doğrulandı.

## 4. Eleme turları: 11 → 5 → 3

**Tur 1, 11 → 5 (nihai puan, betik çıktısı).** Kalanlar: S03, S01, S06, S04, S07. Elenenler, her biri için tek cümle:
- **S09 (6.65):** Konu çok doymuş (2008'de 31 video [RÖ D2]) ve tek güçlü kanıtın komşu sayısı 5; karşı-olgusal açı kişisel bağı ve hikâye gerilimini sulandırıyor.
- **S02 (6.20):** Tez Markets of the Past (7,6x) ve Uncover Things'te birebir işlendi (`benzer_aci` −1.5); ceza olmasa 2. olurdu, yani başka bir kurguyla yeniden yazılırsa geri dönebilir.
- **S10 (6.15):** Ölçülmüş outlier yok (1,7x) ve 34 yıllık yavaş yay gerilimi düşük; güçlü hook tek başına taşımıyor.
- **S11 (5.95):** Kişisel bağ en düşük (hedge fon kaldıracı genç izleyicinin cebine dokunmuyor), tek güçlü rakip videosu 2,4x'te kaldı.
- **S08 (5.90):** Çalışma başlığı konunun tek outlier'ının (30,8x) başlık çekirdeğini taşıyor (`benzer_aci` −1.5); "Silver Thursday" başlığıyla 7.20'ye çıkıp 3. sıra bandına giriyor (hakeme not).
- **S05 (5.05):** Başlık The Economist'in 1973 başlığının neredeyse aynısı (`benzer_aci`); süren savaş bağlamı reklam riskini SARI'ya çekiyor (senaryo risk notu).

**Tur 2, 5 → 3 (finans doğrulama riski + puan).** finans-dogrulayici raporu paralel hazırlanıyor ve bu dosya yazılırken elimde değildi. Bu yüzden risk filtresi senaryoların kendi risk notlarıyla uygulandı. Hakem nihai raporla tekrar bakmalı.
- **S04 (7.10), 4. sırada tutuldu:** puan farkı S06'dan 0.10 (anlamsız) ve ağırlık testinde 12/56 durumda 3. sıraya geçiyor; Rentenmark oranı çelişkisi [doğrulanacak] küçük ama açık bir risk. **Hakem 3. sıra için S04'ü S06 ile eşdeğer saymalı.**
- **S07 (7.00), elendi:** hikâye gücü en yüksek olanlardan, ama konuda ölçülmüş outlier yok (12 ayın en iyisi 47 K; en taze video 5 günde 0,48x, erken veri) ve "hour by hour" vaadi saatlik verinin bulunmasına bağlı.
- **Kalan 3: S03, S01, S06.** S06'nın finans riski: Cisco rakamları şimdilik [AÖ]; F3'te SEC EDGAR / borsa birincil kaynağı şart. finans-dogrulayici bu rakamları doğrulayamazsa 3. sıra S04'e geçer.

## 5. İlk 3: neden kazanabilir / neden kaybedebilir

### 1 — S03 · You Have $1,000 in 1929. Can You Keep It? · 8.40 (7.70–8.70)
- **Neden kazanabilir:** Nişin en kanıtlı konusu (1929: 3 kanalda ≥10x [API]) ile en yüksek kişisel bağ bir arada ("paramı nerede tutarım?" sorusu, sonda 2026 enflasyonuyla ters köşe). Hook üç parçalı açık döngü kuruyor ("one disaster, one gamble, one surprise"); rakiplerde tutan ikinci tekil somut sahne desenine uyuyor [RÖ D5]. Görsel olarak en güçlü (üç renkli kapı, stüdyo ve sokak geçişleri) ve Leo burada doğal bir rol buluyor (sunucu + 3 klon). Kötümser okumada bile (7.70) 2. sıranın temel puanının üstünde.
- **Neden kaybedebilir:** (1) Oyun formatı ilk videoda kanalı "çocuk içeriği" gibi gösterebilir ve tarih derinliği zayıflayabilir [T]. (2) "Shoebox kazandı" tavsiye gibi okunabilir (monetizasyon ve tavsiye dili riski). (3) Banka kapısının sonucu için oran yok [doğrulanacak]; bulunamazsa "you might lose access" diline düşer ve skor tablosu bulanıklaşır. (4) "You have $X in [year]" başlığının nişte ölçülmüş bir outlier'ı yok: açı kanıtı hook deseninden geliyor, başlık deseninden değil. (5) Cevap tahmin edilebilir ("hayır, tutamazsın"); merakı thumbnail'daki üç kapı taşımalı.

### 2 — S01 · The 10% Loan That Built the 1929 Crash · 7.75 (7.30–8.20)
- **Neden kazanabilir:** Aynı 1929 talebi, rakip-özetin önerdiği özgün "follow the dollar" mekanizması [RÖ §6] ve tamamı Fed History'den kaynaklı bir omurga (en düşük doğrulama riski olanlardan). "Borç doları" ekranda yaşayan tek nesne olduğu için izlemesi kolay; telgraf sahnesi akılda kalıyor. S02 ile doğal bir seri oluşturuyor.
- **Neden kaybedebilir:** (1) Marjin anlatısı 1929 belgesellerinin standart parçası; "bunu biliyorum" tepkisi [T]. (2) Başlıktaki "10%" faiz oranı gibi okunabilir (aslında peşinat), merak yanlış yere gidebilir; thumbnail'daki "10% DOWN" bunu çözmeli. (3) Kişisel bağ dolaylı: izleyicilerin çoğu marjin kullanmıyor. (4) S03 ile aynı konu, ikisi aynı slota yarışıyor.

### 3 — S06 · The Best Company of the Dot-Com Era Still Fell 90% · 7.20 (6.55–7.65) — KIRILGAN
- **Neden kazanabilir:** En sıcak gündem (AI balonu, CoreWeave; Wikipedia 3,0× [KH]). Tezin aynısı Nifty Fifty videosunda 8,2x getirdi [API]. Başlık bir merak boşluğu kuruyor ("hangi şirket?"). Leo'nun yanılgısıyla açılış, rakiplerdeki "Most people think…" kalıbının özgün bir karşılığı [RÖ §6].
- **Neden kaybedebilir:** (1) S04 ile fark 0.10; model ikisini ayıramıyor. (2) Cisco rakamları [AÖ]: birincil kaynak gelmezse vaat ("25 yılda döndü") sallanır. (3) Hikâye gerilimi içeride; dışarıda bir kötü adam ya da dönüm anı yok. (4) Genç izleyici Cisco'yu tanımayabilir [T]. (5) AI gündemi soğursa zamanlama puanı (9) hızla düşer: stok video için risk. (6) A sütununun "büyük çöküş" vaadine en uzak senaryo (bir şirket, bir hisse).

## 6. Duyarlılık testi (`viralite-duyarlilik.py`, 2 çalıştırma, diff: fark yok)

```
Temel ilk 3: ['S03', 'S01', 'S06']  (model v0.1, ağırlık toplamı 1.00)
  S03 − S01 = 0.65
  S01 − S06 = 0.55
  S06 − S04 = 0.10  (anlamlı değil, <0.3)
  S04 − S07 = 0.10  (anlamlı değil, <0.3)

1) Ağırlık ±0.05 testi: 56 durum | ilk 3 KÜMESİ değişen: 12 | yalnız sırası değişen: 0
  merak −0.05 → hikaye/gorsel/raf +0.05                 : ilk 3 = ['S03', 'S01', 'S04']
  talep −0.05 → hook/kisisel/hikaye/gorsel/raf +0.05    : ilk 3 = ['S03', 'S01', 'S04']
  zamanlama −0.05 → kisisel/hikaye/gorsel/raf +0.05     : ilk 3 = ['S03', 'S01', 'S04']
  (12 satırın tamamı betik çıktısında; yukarıda gruplanarak gösterildi)

2) Puan aralığı (kötümser / temel / iyimser nihai):
  S03: 7.70 / 8.40 / 8.70     S01: 7.30 / 7.75 / 8.20     S06: 6.55 / 7.20 / 7.65
  S04: 6.65 / 7.10 / 7.55     S07: 6.35 / 7.00 / 7.15     S09: 6.35 / 6.65 / 6.95
  S02: 5.90 / 6.20 / 6.50     S10: 6.00 / 6.15 / 6.45     S11: 5.85 / 5.95 / 6.10
  S08: 5.40 / 5.90 / 6.10     S05: 4.65 / 5.05 / 5.35

3) Çapraz test (hedef kötümser, diğer hepsi iyimser):
  S03 kötümser → ilk 3 = ['S01', 'S03', 'S06']  (küme aynı)
  S01 kötümser → ilk 3 = ['S03', 'S06', 'S04']  (KÜME DEĞİŞTİ)
  S06 kötümser → ilk 3 = ['S03', 'S01', 'S04']  (KÜME DEĞİŞTİ)

SONUÇ: ağırlık testine göre sıralama KIRILGAN (kural: ±0.05 ağırlıkta ilk 3 kümesi değişirse kırılgan).
```
**Okuma:** Kırılganlık yalnız 3. sırada (S06 ↔ S04). S06; merak, talep ve zamanlama ağırlığından besleniyor. S04 ise hikâye, görsel ve raf ömründen. Ağırlık hangi tarafa kayarsa 3. sıra o tarafa gidiyor. S03 en sert çapraz testte bile ilk 2'de kalıyor. S01 kötümser okunduğunda ilk 3'ten düşüyor, ama bunun için S01'in her belirsiz ölçütte kötümser, diğer herkesin iyimser olması gerekiyor (uç senaryo).

**Yargı varyantları** (`viralite-girdi-varyant.json`, sıralamaya girmez):
```
| 1 | S02-cezasiz | The 1929 Crash Was Only the First Domino | 7.40 | +0.30 | −0.00 | **7.70** | seri +0.3 |
| 2 | S01-serisiz | The 10% Loan That Built the 1929 Crash | 7.45 | +0.00 | −0.00 | **7.45** | - |
| 3 | S08-alt2 | Silver Thursday: The Day the Hunt Brothers Fell | 7.20 | +0.00 | −0.00 | **7.20** | - |
```
→ S02'nin cezası kaldırılırsa S02 2. sıraya geçer (S01 7.75 ile fark 0.05, anlamsız). S01 seri bonusu olmadan da 2. sırada kalır. S08 başlığı değişirse 3. sıra bandına (7.0–7.2) girer.

## 7. Kalibrasyon planı (bu video yayınlanınca, F12)
- **Modele girdi olacak metrikler** (`analytics-tracking` mantığı: her ölçüte bir gözlenebilir metrik): merak + thumbnail → **gösterim TO (CTR)**, ilk 7 gün, gözatma + önerilen kaynak ayrı; hook → **ilk 30 sn tutma %**; hikâye gerilimi → **ortalama izlenme süresi (AVD) / süre** ve tutma eğrisindeki ↺ noktalarında düşüş; kişisel bağ → yorum oranı + abone dönüşümü (1.000 izlenme başına); talep + zamanlama → 28 günlük izlenme ve arama trafiği payı.
- **Ön koşul:** CTR, AVD ve tutma verisi için `yt-analytics.readonly` kapsamı henüz yok (CLAUDE.md). Niyazi'nin bir kez yeniden yetki vermesi gerekiyor; koordinatör planlamalı. Bu olmadan F12 kalibrasyonu yalnız herkese açık izlenmeyle yapılabilir.
- **Tahmin kaydı (sonradan karşılaştırma için):** S03 seçilirse beklenen sıra şöyle: CTR tarafı orta-yüksek (merak 8), ilk 30 sn tutma yüksek (hook 9). Gerçek sıralama ≥5 videoda tahmine karşı Spearman ile karşılaştırılır; ≥10 videoda ağırlıklar ayarlanır (v0.2…).
- **Başlık/thumbnail testi (F8 önerisi, `ab-test-setup`):** YouTube Studio "Test & Compare" ile 3 thumbnail. S03 için tek değişken thumbnail olmalı (başlık sabit kalır): (a) üç kapı + "$1,000 IN 1929", (b) Leo yakın plan + parlayan kutu, (c) rakip Aile 1 tipi uzun metin. Başarı metriği izlenme süresi payı (Studio'nun kendi ölçütü). Ölçüm penceresi Studio'nun karar vermesine kadar; erken durdurma yok.

## 8. Açık noktalar ve model notları
- **Model v0.1 metni Türkçe dönem için yazılmış** (benzerlik cezası "TR'ye taşıma" ve "çeviri" diye tanımlı). Kanal İngilizce. Bu turda §2'deki yorumla uygulandı. v0.2'de ceza tanımı "İngilizce rakip başlık kalıbı / kurgusu" diye yeniden yazılmalı. Ağırlık değişikliği yok, çünkü kendi verimiz yok.
- **Kalibrasyon tetiği 1 kısmen karşılandı:** API ile yerel medyan ölçümü artık yapılabiliyor (17 video). Ağırlık korelasyonu için n çok küçük; ağırlıklar değişmedi.
- **Ölçülemedi:** Cisco'ya özel rakip videoları (arama kotası dolu, `search` kullanılmadı); outlier videoların transkripti bu turda indirilmedi (yt-dlp bot kontrolü [RÖ §0]); hook kanıtı rakip-özetteki 8 transkriptten alındı.
- **Sert eleme bekliyor:** finans-dogrulayici ve monetizasyon-uyum-uzmani raporları geldiğinde `ana_iddia_dogrulandi` ve risk notları güncellenip betik yeniden çalıştırılmalı (2 kez + diff).
