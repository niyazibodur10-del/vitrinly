# Bölüm 001 görsel varlıkları (gorsel-varlik-sanatcisi, 2026-11-10)
Kaynak: Canva AI (Niyazi aboneliği). Ham dosyalar ve prompt'lar `uretim/seri/karakter/` altında. Bütün kareler 1080x1920. Sayısal yerleşim `yerlesim.json` içinde.

| Dosya | Ne | Kaynak (media ID) |
|---|---|---|
| plaka/L1-A.png | Mutfak, tezgâh ardı geniş çekim (S1, S3–S8) | MAHajNE3GRU |
| plaka/L1-A-tezgah-on.png | Tezgâh, kâse ve kupa ön katmanı (RGBA). Karakterlerin ÜSTÜNE konur. | L1-A'dan türetildi |
| plaka/L1-B.png | Buzdolabı ve boş beyaz tahta (S2, S4; yazılar KOD ile) | MAHajDYp1b8 |
| karakter/jake-taban.png | Jake, bel üstü, ağız kapalı, kadraj soluna (Mike'a) bakıyor. RGBA. | MAHajBqI-Qs |
| karakter/mike-taban.png | Mike, bel üstü, ağız kapalı, AYNALI, kadraj sağına (Jake'e) bakıyor. RGBA. | MAHajIzpXBs (aynalandı) |
| ifade/<kim>-<ifade>.png | 6 ifade × 2 karakter: notr, gulen, saskin, endiseli, heyecanli, dusunceli. RGBA, ten tabana eşlendi, Mike aynalı. | J-A MAHajKKbhbM / M-A MAHajPZXWbU |
| agiz/ | Ağız yamaları kapalı / yari / acik. AG-J ve AG-M gelince eklenecek. | — |

## Yerleşim kuralları
- **Ekran yönü:** ikili çekimde Mike SOLDA, Jake SAĞDA (birbirlerine bakarlar). Tekli çekimler arasında kesme yapılınca bakışlar karşılıklı tutar.
- **Katman sırası:** plaka → (ikilide önce Mike, sonra Jake) → `L1-A-tezgah-on.png`. Tezgâh çizgisi y=1186.
- **Kesik kollar:** tabanların kol kenarları düz kesik (Mike'ın sağ kesiği y≥924'ten, Jake'in sağ kesiği y≥1063'ten başlıyor). Kesik kenar ya kadraj kenarına yaslanmalı ya da tezgâhın altında kalmalı. `yerlesim.json` değerleri bu kurala göre hesaplandı (ikilide açıkta kalan kesik pikseli 0).
- **İkili:** Mike ölçek 0,55 (0,141), Jake ölçek 0,58 (454,141), Jake önde.
- **Tekli:** karakter ölçek 1 (0,0). Plaka 1,25 yakınlaştırılır, çapa noktası Jake için (760,1186), Mike için (320,1186); tezgâh ön katmanı aynı dönüşümle.
- **İfade portreleri** yalnız ekstrem yakın plan olarak kullanılır: ölçek 1,3, `yerlesim.json` içindeki `ifade_tekli.konum`. Arka plan L1-A 1,6× yakınlaştırılmış ve bulanık (σ6), tezgâh katmanı yok. Tezgâh arkasına baş-omuz olarak KONMAZ (dev kafa gibi görünür, test edildi). Kullanım yerleri: tepki tutuşları ve kameraya bakış anları (S2, S8). Bu karelerde ağız kıpırdamaz.
- **L1-B'de karakter yok:** tabanların kesik kenarı buzdolabının önünde açıkta kalır. L1-B tahta insert'i olarak kullanılır; konuşma L1-A'da geçer.
- **Konuşma:** taban + `agiz/` yaması (konum yamanın JSON'unda). Rhubarb eşlemesi: X ve A → kapalı; B, C, E, F, G, H → yari; D → acik. Geçiş alfa karışımıyla 2 kare. Ağız yalnız tekli ve ikili tabanlarda oynar.
- **Işık:** karakterler düz stüdyo ışığında, plaka sıcak sabah güneşinde. İstenirse karakter katmanına hafif sıcak ton (kurgu/animasyon kararı).
