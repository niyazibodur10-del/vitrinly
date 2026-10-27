# F5 kritik yol testi — senkron ve animasyon raporu · 1929-1000-dolar

**Ajan:** animasyon-yonetmeni · **Tarih:** 2026-10-27 · **Kompozisyonlar:** `K1929Kritik` (19,7 sn, 1920x1080, 30 fps, 591 kare), `K1929AgizTest`
**Kod:** `video/src/k1929/` (Sunucu rig, Klon, ortak: kapı ışığı/altyazı/doku, KritikTest, AgizTest1929) · **Hazırlık:** `07-animasyon/hazirla.py` (`video/public/k1929/` ve `video/src/k1929/veri.ts` buradan üretilir; public klasörü git dışı)
**Render:** `tools/render-son.sh K1929Kritik …/07-animasyon/kritik-test.mp4` (git dışı, 12 MB; 77,8 sn duvar) · önizleme `kritik-test-onizleme.mp4` (720p, git içinde)

## İçerik (ses = anlatim.wav'dan iki parça)
| Zaman | Kaynak | Ne var |
|---|---|---|
| 0,0–2,1 | S01 0,0–2,1 | C15 sepya sokak, yavaş zoom 1,00→1,07, "SEPT 1929" büyük yazı, **Illustration** etiketi |
| 2,1–8,0 | S01 2,1–8,0 | beyaz flaş + yatay kayma ile C01 stüdyo (kamera 1,10→1,14 itme); konuşan Leo rig'i (a) sağda, **"Three doors"ta C12 sunum pozuna geçiş** (5 karelik oturma); "$1,000" ortada sayaç gibi dolar → köşe göstergesine küçülür (+SEPT 1929); kapı levhaları STOCKS / BANK / SHOEBOX kelimesi söylenince ışıkla yanar |
| 8,0–18,5 | S04 62,0–72,5 | **3 Leo klonu** sağdan girer, kapılarına yürür (C04 ×2, C05 ×1; varınca C02 duruş), yaka kartları + isim balonları; "laughs" kelimesinde kahve kapıya punch-in 1,42×, Box Leo büzülür, "HA!" yazıları |
| 18,5–19,7 | S04 72,5–73,7 | bulanık C03 önünde yakın plan Leo, "Remember that laugh" + **tek göz kırpma** (C06 yarım yama) |
Altyazı: kelime kelime, 1–3 kelime, kapı renkleriyle anahtar kelime (stock/blue = mavi, bank/green = yeşil, shoebox/brown/box = kahve, sayılar sarı).

## Kalite kapıları (ölçüm: `kapi-olcumleri.txt`)
| Kapı | Sonuç |
|---|---|
| Dudak senkronu, ekranda konuşan ağız (2,1–8,0 sn, render sesi) | **−1 kare** (33 ms), kor. 0,46 → GEÇTİ |
| Dudak senkronu, tam sahne Rhubarb (sahne-zamanlari.json) | S01 **0** · S04 **0** · S02 +1 · S03 +1 · S05 +2 · S11 +1 · S13 +1 → hepsi GEÇTİ |
| Dudak senkronu, test videosunun tamamı (birleşik çizelge) | −4 kare → KALDI (açıklama aşağıda; ekranda ağız olmayan bölgeden geliyor) |
| AgizTest karesi | `kareler/agiz-test.jpg` — 9 şekil Leo'nun kendi yüzünde; hale yok |
| blackdetect (d=0,1, pix_th=0,10) | **0** |
| freezedetect (1 sn) | donma yok |
| Titreme/sıçrama (kare-kare fark) | medyan 0,66; sıçramaların hepsi planlı (63 flaş-kesme, 117/119 sayaç küçülme + poz geçişi, 240 kesme, 499–506 punch-in, 555 kesme) |
| Ses | −13,9 LUFS (render-son) |
| Kenar | klon/sunucu kesiklerinde saçak yok (kare 13,5 ve 17,0 sn 2× kırpım) |

**−4 kare açıklaması:** S04 tam sahne çizelgesi 5 sn pencerelerle ölçüldüğünde 56,0: +1 · 59,0: −1 · **62,0: −5 · 65,0: −5 · 68,0: −4** · 71,0: +1 · 74,0: 0. Sapma yalnız "Stock/Bank/Box Leo takes the … door" cümlelerinde (62–70 sn); Whisper kelime zamanları da aynı bölgede enerji başlangıcından 0,13–0,25 sn geç (`04-ses/kelimeler.json`). Bu aralıkta ekranda sunucunun ağzı **yok** (klonlar yürür, dış ses) → izleyicinin göreceği bir senkron hatası yok. Test videosu bu bölgeyi seçtiği için tüm-video ölçümü −4 çıktı. Kalıcı çözüm önerisi aşağıda.

## Adaylar ve eleme
**Rhubarb çalıştırma (S04 parçası, aynı ölçüm):** A parça (−5) · B parça + 0,5 sn boşluk (−5) · C tam sahne + kesme (−5) · D tam sahne + boşluk (−5) · E phonetic tanıyıcı (−5, kor. 0,35 en düşük). Beşi aynı → sapma araçtan değil, bu cümlelerin akustiğinden (veya ölçüm yanlılığından). **Seçilen:** PocketSphinx + `--dialogFile` (kor. en yüksek); üretimde **tam sahne** üzerinde çalıştırılıp kesilir (sahne sınırında bağlam kaybı yok).
**Sessizlik kapısı (yeni, `sessizlik_kapisi.py`):** Rhubarb cümle sonlarında ağzı sessizlikte 5–8 kare açık tutuyordu (ör. S04 1,57–1,93 sn sessizlikte C). ≥100 ms sessiz aralıklar X yapıldı; korelasyon 0,48 → 0,50, ekranda "sessizlikte konuşan ağız" kalmadı.
**Ağız seti:** Rhubarb eşlemesi rig-yamalar.json `rhubarb_eslesme` (G = C07 kalıcı). İlk AgizTest'te B–H yamalarında yüz kenarında **mavi hale** çıktı (yama kutusu Canva zemin piksellerini taşıyordu) → yama alfası taban a silüetiyle çarpıldı; ikinci AgizTest temiz. C12 sunum pozunda yamalar dikişsiz (kare 150/160 4× kırpım); **c-isaret pozu yamalarla uyumsuz** (kafa farkı göz 55,7 / ağız çevresi 43,5 vs C12 12,6 / 8,4) → c ancak konuşmasız anlarda kullanılır.
**Klon yürüyüşü:** A tek yürüme pozu + adım zıplaması/eğim/ezilme-uzama (SEÇİLDİ: akıcı, tutarlılık %100) · B C04↔C02 poz değişimiyle "adım" (elendi: ayak konumları farklı, yerinde kayma ve sıçrama yapar) · C image-to-video (elendi: ücretsiz yerel araç yok, ücretliler Niyazi onayı ister; 3 klonda yüz tutarlılığı riski). Aynalama yok (saat sol bilekte).
**B planı (tek Leo kapıdan kapıya):** gerekmedi; 3 klon sahnesi okunur ve tutarlı.

## Riskler / sonraki adım notları
1. **Punch-in 1,42×** (C01 kahve kapı) 1920 genişlikli plakada hafif yumuşak; finalde bu kırpım `tools/karakter/buyut.py` x4 ile büyütülmeli (gorsel-varlik-sanatcisi kuralı: >1,15×).
2. Senkron kapısının ölçüm penceresi: tam video yerine **ekranda konuşan ağız aralıkları** (ve tam sahne) ölçülmeli; `tools/senkron-testi.py`'ye aralık listesi + formant bandı (700–3000 Hz) seçeneği önerisi → uretim-muhendisi.
3. Klon yaka kartı yazısı 1080p'de küçük (16 px); okunurluk isim balonuyla sağlanıyor.
4. Sahne sesleri (seyirci kahkahası, whoosh, pop) F6 miksine bırakıldı; zaman damgaları: flaş 2,1 sn, kapı ışıkları 4,94 / 5,92 / 6,62 sn (S01 zamanı), kahkaha "laughs" 70,76 sn.
