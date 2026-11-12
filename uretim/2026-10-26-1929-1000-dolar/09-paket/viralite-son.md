# F8 — Son viralite puanı (viralite-analisti) · 2026-10-27

**Video:** S03 "You Have $1,000 in 1929. Can You Keep It?" · final 10:31,6 · ilk 30 sn varyant B · paket T1 + A2/B1/D1.
**Model:** `docs/viralite-modeli.md` **v0.1**. Güven **DÜŞÜK** (±0.05 ağırlık; 0.3'ten küçük fark anlamsız). **Bütün puanlar tahmindir [T].**
Hesap `tools/viralite.py` ile yapıldı. Girdi: `09-paket/viralite-son-girdi.json`. Başlık kalıbı ölçümü: `viralite-baslik-kalip.py` → ham veri `viralite-baslik-ham.json`.
Etiketler: [API] YouTube Data API v3 (2026-10-27) · [H] API'den hesap · [Ö] dosya/ölçüm (F7/F8 raporları) · [RÖ] rakip-ozet.md · [T] tahmin.

## 0. Sonuç
| | F2 (senaryo) | F8 (bitmiş paket T1+A2) | Aralık F8 (kötümser–iyimser) |
|---|---|---|---|
| Nihai [T] | **8.40** | **8.40** | 7.55–8.70 |

- **Puan değişmedi.** F2'deki yargılar bitmiş üründe tutuldu. Değişen tek şey güven: hook, görsel ve başlık-thumbnail-hook tek vaat zinciri artık tahmin değil, ölçülmüş ürün özelliği [Ö]. Alt aralık F2'deki 7.70'ten 7.55'e indi, çünkü talebe ilk kez kötümser 8 verdim (açı düzeyinde ölçülmüş outlier yok; aşağıya bakın).
- **Test & Compare sırası: A2, B1, D1 ONAYLANDI** (sabit başlık T1, tek değişken thumbnail). Gerekçe §4'te.
- Model v0.1 üç thumbnail'ı birbirinden **ayıramıyor**: A2 ile diğerleri arasında 0.20 fark var, eşik 0.3. Seçimi bu yüzden YouTube'un testine bırakıyoruz. Model sürümü artmadı (kendi kanalımızdan henüz veri yok).

## 1. Betik çıktısı (test kapısı)
```
$ python3 tools/viralite.py uretim/2026-10-26-1929-1000-dolar/09-paket/viralite-son-girdi.json   # 1. ve 2. çalıştırma
Viralite modeli v0.1 | ağırlık toplamı = 1.00 | puanlar TAHMİNDİR [T]

| Sıra | ID | Başlık | Ağırlıklı | Bonus | Ceza | Nihai | Not |
|---|---|---|---|---|---|---|---|
| 1 | K1-T1+A2 | T1 You Have $1,000 in 1929. Can You Keep It? + A2 ONE IS A DISASTER | 8.40 | +0.00 | −0.00 | **8.40** | - |
| 2 | K2-T1+D1 | T1 + D1 EVERY DOOR LOCKED | 8.20 | +0.00 | −0.00 | **8.20** | - |
| 3 | K3-T1+B1 | T1 + B1 THE SURPRISE DOOR | 8.20 | +0.00 | −0.00 | **8.20** | - |
| 4 | K4-T2+B1 | T2 Stocks, a Bank or a Shoebox: Who Survived 1929? + B1 | 8.20 | +0.00 | −0.00 | **8.20** | - |
| 5 | K5-T4+B1 | T4 Surviving the 1929 Crash With $1,000: Three Doors + B1 | 8.00 | +0.00 | −0.00 | **8.00** | - |

$ diff v1.txt v2.txt && echo "diff: fark yok"; sha256sum v1.txt v2.txt
diff: fark yok
ea3265d96e71fe311ddeda37dfc7694587563ec6cbd90a132034310e1b16e4ed  v1.txt
ea3265d96e71fe311ddeda37dfc7694587563ec6cbd90a132034310e1b16e4ed  v2.txt

$ ağırlık toplamı assert
assert OK: toplam 1.00
$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md
Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
$ F2 referansı (02-senaryo/viralite-girdi.json, aynı betik)
| 1 | S03 | You Have $1,000 in 1929. Can You Keep It? | 8.40 | +0.00 | −0.00 | **8.40** | - |

$ python3 02-senaryo/viralite-duyarlilik.py 09-paket/viralite-son-girdi.json   # 2 koşu, diff yok
1) Ağırlık ±0.05 testi: 56 durum | ilk 3 KÜMESİ değişen: 0 | yalnız sırası değişen: 0
2) Puan aralığı: K1 7.55/8.40/8.70 · K2 7.55/8.20/8.50 · K3 7.35/8.20/8.50 · K4 7.35/8.20/8.50 · K5 7.35/8.00/8.30
3) Çapraz test: her biri kötümser, diğerleri iyimser olunca küme değişiyor → kombinasyonlar arası fark modelin çözünürlüğünün altında
```
`viralite-baslik-kalip.py` de iki kez çalıştırıldı, aynı ham veriyle aynı sha256 çıktı (51eac3ce…9b57).

## 2. Ölçüt puanları: F2 ile F8 (temel; parantezde kötümser–iyimser) [T]
| Ölçüt (ağırlık) | F2 | F8 | Bitmiş üründeki kanıt |
|---|---|---|---|
| Merak 0.20 | 8 (7–9) | **8 (7–9)** | T1 soruyu soruyor, A2 bahsi koyuyor (üç "?" kapı, "ONE IS A DISASTER"). İzleyicinin aklında kalan soru "hangisi?" oluyor. F2'deki çekince ("cevap tahmin edilebilir: hayır") hâlâ geçerli, bu yüzden 9 değil. Koyu lacivert thumbnail koyu temada az öne çıkabilir (thumb-rapor riski). |
| Talep 0.15 | 9 | **9 (8–9)** | Konu düzeyinde 1929 ≥10x, 3 kanalda [API]. Açı düzeyinde ise "you + $N + yıl" başlık iskeletinin 12 ayda **hiç örneği yok** (n=0, §3). Kanıtsız ama ayrışan bir iskelet → kötümser 8. |
| Hook 0.10 | 9 (8–9) | **9 (8–9)** | İlk 15 sn'de somut sahne, ikinci tekil hitap, bahis ve 3 kapı var. "one door is a disaster" 0:09'da [Ö]. Vaat şeridi "CAN YOU KEEP IT?" 7,9 sn'de, ilk 30 sn'de 18 olay ve 2 sert kesme var (kurgu-rapor). Bu yapı rakiplerin "somut sahne" hook desenine uyuyor (D5, n=3). Eksi tarafı: konuşma hızı ilk 30 sn'de **168 kelime/dk** [Ö: 84 kelime], rakip bandı 175–225 [RÖ D5] → kötümser 8. |
| Kişisel bağ 0.15 | 9 (8–9) | 9 (8–9) | $1,000 + "your bed" + 2026 köprüsü videoda var. |
| Zamanlama 0.10 | 7 (6–8) | 7 (6–8) | 29 Ekim yıldönümünden 3 gün sonra yayın (1 Kasım). Hakem bu riski kabul etti; değişiklik yok. |
| Hikâye 0.15 | 8 (7–8) | 8 (7–8) | 13 yeniden kanca var, en uzun aralık 71,7 sn [Ö]. S18'de 488–489 sn arasında ~1 sn ölü an var (kurgu riski 1), puanı düşürecek kadar değil. |
| Görsel 0.10 | 9 | 9 | Leo 10 rastgele karede tutarlı, black/freeze 0 [Ö]. |
| Raf 0.05 | 8 | 8 | Eylül 2026 TÜFE köprüsü sonu tarihliyor; ana gövde kalıcı. |
Seri: hayır · somut özne: var (merak tavanı yok) · rakip benzerlik: yok (T1 "real reason / true origin" kalıbı taşımıyor) · ana iddia: doğrulandı (F3 kilidi).
**Kombinasyonlar yalnız merak ölçütünde ayrıştırıldı** (hook, kişisel bağ ve hikâye videoya ait, thumbnail onları değiştirmiyor):
- **A2 8 (7–9):** Merak boşluğu ile seçim mimarisi birlikte çalışıyor: 3 seçenek, biri felaket (`marketing-psychology`: curiosity gap + kayıptan kaçınma). Thumbnail'daki vaat videonun 0:09'da söylediği cümle; bu da izlenme süresini korur.
- **D1 7 (7–8):** En güçlü kayıp/tehlike sinyali bu. Ama karşılığı geç geliyor (7:33 ve 8:42 bölümleri), bu yüzden ilk dakikada beklenti boşa düşebilir. Test'in ölçtüğü izlenme süresi payında risk.
- **B1 7 (6–8):** Yüz duygusu en güçlü olan bu. Ama kutunun elde ve "SURPRISE" ile görünmesi sürpriz kapının kutu olduğunu ele veriyor; merak boşluğu kısmen kapanıyor.
- **T2 + B1 7, T4 + B1 6 (6–7):** T2 de yıl + soru taşıyor, fakat kapıları sayıyor ve para nesnesi yok. T4'te soru yok ve "Surviving" yarı cevap veriyor. T4, CTR düşük çıkarsa yedek olarak kalır (paket.md).

## 3. Rakip outlier konumu
**Konu (F2'den, değişmedi) [API][H]:** 1929/Great Depression konusunda 12 ay içinde ≥10x üç video var: SLICE History 38,6x · The Money Files 17,2x · Casual Economics 15,7x (12 ay dışı). Markets of the Past 7,6x ölçüldü ama onun kurgusu ("what historians get wrong") bizde yok.
**Başlık kalıbı (yeni ölçüm; 30 kanal, 2.394 uzun video, 2025-10-20..2026-10-20, yerel medyan ≥1.000):**

| Kalıp | n / kanal | Medyan skor | ≥3x | Diğerleri |
|---|---|---|---|---|
| Tüm havuz | 2394 / 30 | 0.98 | %14 | — |
| Soru işareti | 181 / 24 | 0.90 | %17 | 0.98 / %14 |
| İkinci tekil (you/your) | 192 / 19 | 0.91 | %14 | 0.98 / %15 |
| Dolar tutarı ($N) | 89 / 17 | 0.85 | %9 | 0.98 / %15 |
| Yıl | 112 / 18 | 0.95 | %20 | 0.98 / %14 |
| **T1 iskeleti: you + $N + yıl** | **0 / 0** | — | — | — |
| you + soru | 14 / 7 | 1.66 | %29 | (n küçük; "Are You Afraid of the Dark?" gibi dizi adları karışıyor) |

Yorum: T1'in parçalarının hiçbiri tek başına anlamlı bir artı ya da eksi değil. Medyanlar 0.85–0.95 ile 0.98 arasında, ≥3x oranları ters yönde oynuyor. **Başlığı değiştirmek için veri yok.** İskeletin hiç örneği olmaması iki yöne okunabilir: nişte ayrışıyor ama kanıtsız. Kanal listesi kanal-analisti'nin 39 kanalı; bir kısmı niş dışı (ör. Dial-Up Days film kanalı), bu yüzden kanıt gücü orta-zayıf.
**Thumbnail [RÖ D4]:** Nişte maskotlu outlier yok. A2/B1/D1 "çizgi karakter + tek nesne + ≤4 kelime" ailesinde duruyor; ailenin tipik rengi koyu lacivert + sarı. Ayrışma karakter ve kapı/oyun dilinden geliyor, renkten gelmiyor.

## 4. Test & Compare kararı — A2, B1, D1 onaylandı
Kurallar (support.google.com/youtube/answer/16391400): en çok 3 varyant; kazanan **izlenme süresi payı** ile seçilir; **sonuç belirsiz çıkarsa ilk yüklenen varsayılan olur**; başlık + thumbnail kombinasyonu da test edilebilir. Test yalnız masaüstü Studio'dan kurulur, "gelişmiş özellikler" açık olmalı, gizli/planlı video test edilemez. Test sırasında başlık/thumbnail değişirse test durur.
1. **A2 ilk sırada.** Yeni bir kanalda gösterim sayısı az olacağı için sonucun "belirsiz" çıkma olasılığı yüksek [T]. Belirsiz sonuçta ilk varyant kalıcı oluyor, yani ilk sıraya en iyi ön tahmin konmalı: A2 (merak en yüksek ve vaadi en erken karşılanan).
2. **Başlık sabit (T1), tek değişken thumbnail.** Hakem H5'i destekliyorum. Az gösterimde değişken sayısını artırmak testin gücünü düşürür. Ayrıca başlık+thumbnail kombinasyonu test edilirse kazananın neden kazandığı ayrıştırılamaz ve kalibrasyon verisi kirlenir.
3. **B1 ile D1'in sırası işlevsel değil** (üçü aynı anda yayında). B1'i 2. tutuyorum, çünkü A2'ye en uzak varyant B1 (yüz ağırlıklı); A2–D1 en yakın çift (dHash 29, aynı stüdyo). Varyantlar ne kadar farklıysa sonucun belirsiz çıkma riski o kadar düşük.
4. **Sıradaki test (ilk test bitince, ayrı test):** kazanan thumbnail sabit, T1 ile T4 karşılaştırılır. Böylece başlık değişkeni ayrı ölçülür. 7 günlük CTR, kanal ortalamasının belirgin altındaysa T4 öne alınır (paket.md'deki yedek kuralı).
5. **Uygulama notu (koordinatör / uretim-muhendisi):** Test & Compare için API yok; Studio'dan masaüstünde kurulmalı. Video planlı (gizli) yüklendiği için test **ancak yayın anında veya sonrasında** başlatılabilir. Yayından önce kanalda gelişmiş özelliklerin açık olduğu kontrol edilmeli. Bu adım Niyazi'nin yayın onayı kapsamındadır.

## 5. Shorts (model v0.1 Shorts için tanımlı değil, puan verilmedi)
- **Shorts 1** "In 1929, the smartest-looking door was the worst one." Bağlamsız bir çelişki ve ilk karede yazı + Leo var; bu iyi. Zayıf an 14–18 sn, yalnız "DOOR 2: THE SCORE" başlığı görünüyor (kurgu riski 2, kare kontrolünde doğrulandı). Swipe riski en yüksek yer burası [T].
- **Shorts 2** "A shoebox of cash gained power in 1932…" Merakı daha soyut, 2026'ya köprü kuruyor; yatırım-ipucu kitlesi çekme riski düşük, çünkü cevap videoda.
- Test & Compare Shorts'ta yok. Shorts verisi kalibrasyona yalnız "kaydırmadan izleme oranı + uzun videoya geçiş" olarak girer (aşağıda).

## 6. Kalibrasyon planı (F12, 48 sa / 7 g / 28 g)
Modele girecek metrikler (`analytics-tracking`): gösterim TO (merak + thumbnail) · ortalama izlenme yüzdesi ve 30 sn tutma (hook, hikâye) · görüntüleme/gösterim (toplam) · Test & Compare sonucu ve varyant payları. Şart: `yt-analytics.readonly` kapsamı (henüz yok, bir kez yeniden yetki gerekiyor). Test & Compare sonucu ve TO bu kapsam olmadan Studio ekran görüntüsüyle de alınabilir.
Tahmin kaydı (yanlışlanabilir olsun diye): A2 kazanır ya da sonuç belirsiz çıkar [T, güven düşük]. B1 kazanırsa "yüz duygusu > merak boşluğu" dersi çıkar ve thumbnail için merak ölçütünün gerekçesi v0.2'de yeniden yazılır. 1 video ile ağırlık değişmez (kural: ≥5 videoda sıralama karşılaştırması, ≥10'da ağırlık ayarı).
