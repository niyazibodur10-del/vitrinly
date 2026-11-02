# Cue listesi — 2026-10-28-yeni-video S08 (F6)

Kaynak: `06-muzik/cue.json` (`cue-uret.py` ← `animasyon-efekt-cue.json` tahmini=false + `04-ses/sahne-zamanlari.json`). Zaman ekseni = `04-ses/anlatim.wav` (678.195 sn). Kare = 30 fps.
Stem'ler: `stems/muzik-stem.wav`, `stems/sfx-stem.wav` (48 kHz stereo 24-bit, anlatımla örnek örnek aynı uzunluk, 0 noktası = anlatımın 0'ı). Montajda anlatım kaydırılırsa iki stem de aynı kadar kaydırılır.
Abone klik sesi stem'de YOK: `assets/efekt/ozgun-fare-klik.flac`'ı kurgu-editoru AboneOl bileşeniyle görsel tıklamaya ±2 kare yerleştirir (olaylar: 175.547 sn, 305.082 sn, 662.614 sn).

## Müzik bölümleri

| # | Bölüm | Giriş → çıkış | Kare | Parça (lisans) | Ruh hali / tempo | Konuşma altı | Giriş/çıkış sönüşü |
|---|---|---|---|---|---|---|---|
| 1 | B1 mutfak masası | 0:00.00 → 1:23.62 | 0–2509 | happy lofi day — Tarush Singhal (CC0) | merak + sıcak lo-fi, Rhodes · ≈98 BPM [tahmin] | −23 dB | 0.4 / 1.2 sn |
| 2 | B2a beş zarf | 1:22.42 → 2:00.46 | 2473–3614 | Jazz — spring spring (CC0) | hafif, sayan caz · ≈90 BPM [tahmin] | −22 dB | 1.2 / 0.25 sn |
| 3 | B2b faiz zarfı sonrası | 2:14.83 → 2:56.70 | 4045–5301 | Jazz — spring spring (CC0) | aynı caz, yeniden giriş · ≈90 BPM [tahmin] | −22 dB | 2.0 / 1.2 sn |
| 4 | B3 borç defteri | 2:55.50 → 4:32.10 | 5265–8163 | Deliberate Concealment — northivanastan (CC0) | meraklı gerilim, pizzicato + celesta · ≈103 BPM [tahmin] | −22 dB + 3 kHz oyuk | 1.2 / 1.2 sn |
| 5 | B4 zarfın içindeki zarf | 4:30.90 → 6:31.62 | 8127–11749 | 80s Mysterywave — DesertDev (CC0) | yükselen synth gerilimi · ≈80 BPM [tahmin] | −21 dB | 1.2 / 1.2 sn |
| 6 | B5 bir ailenin yapamadığı üç şey | 6:30.42 → 8:48.45 | 11713–15854 | Lofi again — omfgdude (CC0) | düşünceli lo-fi, nefes · yavaş [tahmin] | −22.5 dB | 1.2 / 1.2 sn |
| 7 | B6 açığı kapatmanın üç yolu | 8:47.25 → 10:38.55 | 15818–19156 | The Way It Is — Zane Little Music (CC0) | ileriye bakan, dengeli · orta [tahmin] | −22 dB | 1.2 / 1.2 sn |
| 8 | B7 kapanış | 10:37.35 → 11:18.20 | 19120–20346 | A Small Fire Will Do — trex0n (CC0) | sakin, sıcak kapanış · yavaş [tahmin] | −22 dB | 1.2 / 2.5 sn |

Notlar: S06 kırmızı INTEREST zarfı masaya kaydığı karede müzik 0.25 sn'de **keser** (tek tık), "This household pays its lenders…" cümlesinde aynı caz 2 sn'de geri girer. Konuşma boşluğu ≥0.9 sn olunca müzik +6 dB açılır.

## Shorts müzik yatakları (60 sn, sonda 2 sn sönüş; kurgu kesit uzunluğuna kırpar)

- `stems/shorts-1-muzik-stem.wav` ← `$M/deliberate-concealment-northivanastan.ogg` (konuşma altı −20 dB, mobil)
- `stems/shorts-2-muzik-stem.wav` ← `$A/the-way-it-is-zane-little.mp3` (konuşma altı −20 dB, mobil)

## SFX vuruşları (226 vuruş, 183 görsel olay; hizalama: geçiş whoosh'unda tepe, diğerlerinde ses başlangıcı olay karesinde)

| Olay zamanı | Kare | Olay | Dosya | Dosya başı (sn) | Kazanç dB |
|---|---|---|---|---|---|
| 0:00.00 | 0 | S01 Capitol silüeti tam ekran, küçülmeye başlar (alçalan whoosh) | `whoosh-uzun.flac` | 0.0 | -18 |
| 0:01.90 | 57 | S01 Capitol → masadaki ev maketi (pop) + Leo masaya oturur (tahta tık / sandalye) | `tik-click.flac` | 1.8999 | -19 |
| 0:03.31 | 99 | S01 maaş zarfı masaya düşer ($5,400 IN) (kâğıt düşme) | `sayfa-starninjas-book_flip_2.flac` | 2.9935 | -18 |
| 0:03.80 | 114 | S01 sayaç 0→5,400 (0,8 sn) (tıkırtı + ding) | `ozgun-sayac-tikirti.flac` | 3.8 | -19 |
| 0:03.80 | 114 | S01 sayaç 0→5,400 (0,8 sn) (tıkırtı + ding) | `ding-pwl-bell_ding1.flac` | 4.5625 | -21 |
| 0:07.36 | 221 | S01 not yapışır: $7,400 OUT (yapışkan not tap) | `ozgun-yapiskan-not.flac` | 7.3549 | -15 |
| 0:08.52 | 256 | S01 kırmızı −$2,000/MO notu yanıp söner (alarm tik ×3) | `tik-click.flac` | 8.5199 | -17 |
| 0:08.52 | 256 | S01 kırmızı −$2,000/MO notu yanıp söner (alarm tik ×3) | `tik-click.flac` | 8.7699 | -17 |
| 0:08.52 | 256 | S01 kırmızı −$2,000/MO notu yanıp söner (alarm tik ×3) | `tik-click.flac` | 9.0199 | -17 |
| 0:13.06 | 392 | S02 kesme: masa orta, Leo (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 12.8622 | -25 |
| 0:19.94 | 598 | S02 araba ikonu + CAR LOANS (pop) | `pop-pluck.flac` | 19.94 | -20 |
| 0:20.78 | 623 | S02 ev ikonu + MORTGAGES (pop) | `pop-pluck.flac` | 20.78 | -20 |
| 0:24.18 | 725 | S02 not: FASTEST BILL? (yapışkan not tap) | `ozgun-yapiskan-not.flac` | 24.1749 | -15 |
| 0:24.84 | 745 | S02 not: WHY? (yapışkan not tap) | `ozgun-yapiskan-not.flac` | 24.8349 | -15 |
| 0:26.64 | 799 | S02 üç not A · B · C (tap ×3) | `tik-select.flac` | 26.64 | -18 |
| 0:26.64 | 799 | S02 üç not A · B · C (tap ×3) | `tik-select.flac` | 26.76 | -18 |
| 0:26.64 | 799 | S02 üç not A · B · C (tap ×3) | `tik-select.flac` | 26.88 | -18 |
| 0:30.24 | 907 | S03 kesme: Leo yakın: I'm Leo (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 30.0412 | -25 |
| 0:30.54 | 916 | S03 isim etiketi LEO (hafif pop) | `pop-pluck.flac` | 30.539 | -20 |
| 0:37.22 | 1117 | S03 = işareti + $1 billion a year (ding) | `ding-pwl-bell_ding1.flac` | 37.1825 | -21 |
| 0:45.66 | 1370 | S03 kesme: masa geniş, Leo (kısa whoosh) | `whoosh-kisa.flac` | 45.4642 | -27 |
| 0:49.19 | 1476 | S03 kırmızı tez notu buzdolabına çarpar (tok tap / slap) | `ozgun-yapiskan-not.flac` | 49.1869 | -15 |
| 0:57.49 | 1725 | S04 kesme: kuşbakışı masa: PAYDAY (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 57.2952 | -25 |
| 0:58.48 | 1754 | S04 maaş zarfı masaya düşer $5,400 (kâğıt düşme) | `sayfa-starninjas-book_flip_2.flac` | 58.1545 | -18 |
| 1:05.50 | 1965 | S04 şerit: PAYCHECK TAXES (kâğıt çekme) | `kagit-rubberduck-paper_03.flac` | 65.4534 | -21 |
| 1:07.00 | 2010 | S04 şerit: COMPANY TAXES (kâğıt çekme) | `kagit-rubberduck-paper_03.flac` | 66.9534 | -21 |
| 1:08.54 | 2056 | S04 şerit: PAYROLL TAXES (kâğıt çekme) | `kagit-rubberduck-paper_03.flac` | 68.4934 | -21 |
| 1:13.00 | 2190 | S04 kesme: masa orta, Leo zarfları dizer (kısa whoosh) | `whoosh-kisa.flac` | 72.8012 | -27 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 79.635 | -24 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 79.755 | -24 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 79.875 | -24 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 79.995 | -24 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 80.115 | -24 |
| 1:19.94 | 2398 | S04 6 zarf yelpaze gibi dizilir (kart dağıtma ×6) | `sayfa-starninjas-book_flip_1.flac` | 80.235 | -24 |
| 1:21.76 | 2453 | S04 kırmızı zarf kenara çekilir (?) (gizem tını) | `ding-pwl-bell_ding1.flac` | 81.7225 | -25 |
| 1:23.02 | 2491 | S05 kesme: masa orta, Leo + hesap makinesi (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 82.8242 | -25 |
| 1:25.28 | 2558 | S05 mavi zarf SOCIAL SECURITY düşer (kalın zarf thud) | `zarf-spring-spring-snd_close_map.flac` | 84.9056 | -16 |
| 1:31.71 | 2751 | S05 hesap makinesi $1,667 (tuş tıkırtısı) | `ozgun-hesap-tus-dizi.flac` | 91.6923 | -16 |
| 1:34.60 | 2838 | S05 kesme: grafik G1: gelir çubuğu dolar (kısa whoosh) | `whoosh-kisa.flac` | 94.3982 | -27 |
| 1:35.86 | 2876 | S05 yeşil dilim MEDICARE $1,073 (pop) | `pop-pluck.flac` | 95.86 | -20 |
| 1:36.08 | 2882 | S05 açık yeşil zarf HEALTH (zarf thud) | `zarf-spring-spring-snd_close_map.flac` | 95.7056 | -16 |
| 1:41.74 | 3052 | S05 sayaç SPENT $3,765 (tıkırtı + ding) | `ozgun-sayac-tikirti.flac` | 101.74 | -19 |
| 1:41.74 | 3052 | S05 sayaç SPENT $3,765 (tıkırtı + ding) | `ding-pwl-bell_ding1.flac` | 102.5025 | -21 |
| 1:52.06 | 3362 | S06 kesme: kuşbakışı: gri DEFENSE zarfı (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 111.8582 | -25 |
| 1:52.78 | 3383 | S06 gri DEFENSE zarfı düşer (thud) | `muhur-impact-punch.flac` | 112.7567 | -18 |
| 1:55.47 | 3464 | S06 etiket SHIPS (tik) | `tik-click.flac` | 115.4709 | -19 |
| 1:55.70 | 3471 | S06 etiket PLANES (tik) | `tik-click.flac` | 115.6999 | -19 |
| 1:56.02 | 3481 | S06 etiket SALARIES (tik) | `tik-click.flac` | 116.0199 | -19 |
| 1:56.60 | 3498 | S06 etiket BASES (tik) | `tik-click.flac` | 116.5999 | -19 |
| 1:57.67 | 3530 | S06 $965 (pop) | `pop-pluck.flac` | 117.674 | -20 |
| 2:00.46 | 3614 | S06 kırmızı zarf masaya kayar (müzik kesilir) (MÜZİK KES + tek tık) | `tik-select.flac` | 120.46 | -14 |
| 2:03.96 | 3719 | S06 5 dolardan biri kırmızıya döner (ding) | `ding-pwl-bell_ding1.flac` | 123.9225 | -21 |
| 2:04.58 | 3737 | S06 INTEREST yazısı (tek tık) | `tik-click.flac` | 124.5799 | -19 |
| 2:07.66 | 3830 | S06 kesme: grafik G1b: sıralı çubuk (kısa whoosh) | `whoosh-kisa.flac` | 127.4622 | -27 |
| 2:07.96 | 3839 | S06 çubuklar sırayla dolar, INTEREST 3. sırada parlar (tıkırtı ×5) | `ozgun-hesap-tus.flac` | 127.955 | -18 |
| 2:07.96 | 3839 | S06 çubuklar sırayla dolar, INTEREST 3. sırada parlar (tıkırtı ×5) | `ozgun-hesap-tus.flac` | 128.075 | -18 |
| 2:07.96 | 3839 | S06 çubuklar sırayla dolar, INTEREST 3. sırada parlar (tıkırtı ×5) | `ozgun-hesap-tus.flac` | 128.195 | -18 |
| 2:07.96 | 3839 | S06 çubuklar sırayla dolar, INTEREST 3. sırada parlar (tıkırtı ×5) | `ozgun-hesap-tus.flac` | 128.315 | -18 |
| 2:07.96 | 3839 | S06 çubuklar sırayla dolar, INTEREST 3. sırada parlar (tıkırtı ×5) | `ozgun-hesap-tus.flac` | 128.435 | -18 |
| 2:13.98 | 4019 | S06 INTEREST > DEFENSE (vuruş) | `muhur-impact-plate.flac` | 133.982 | -19 |
| 2:19.20 | 4176 | S06 kesme: grafik: 5 dolardan 1'i (kısa whoosh) | `whoosh-kisa.flac` | 139.0022 | -27 |
| 2:24.60 | 4338 | S06 BUYS NOTHING damgası (damga thud) | `muhur-impact-punch.flac` | 144.5767 | -18 |
| 2:25.78 | 4373 | S06 NO ROAD (tik) | `tik-click.flac` | 145.7799 | -19 |
| 2:26.22 | 4387 | S06 NO CHECK (tik) | `tik-click.flac` | 146.2199 | -19 |
| 2:26.64 | 4399 | S06 NO SHIP (tik) | `tik-click.flac` | 146.6399 | -19 |
| 2:30.48 | 4514 | S07 kesme: kuşbakışı: EVERYTHING ELSE zarfı (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 150.2782 | -25 |
| 2:30.63 | 4519 | S07 kahve zarf EVERYTHING ELSE düşer (thud) | `muhur-impact-punch.flac` | 150.6027 | -18 |
| 2:33.06 | 4592 | S07 etiket VETERANS (tik) | `tik-click.flac` | 153.0599 | -19 |
| 2:33.74 | 4612 | S07 etiket ROADS (tik) | `tik-click.flac` | 153.7399 | -19 |
| 2:34.42 | 4633 | S07 etiket FOOD (tik) | `tik-click.flac` | 154.4199 | -19 |
| 2:35.38 | 4661 | S07 etiket SCIENCE (tik) | `tik-click.flac` | 155.3799 | -19 |
| 2:36.14 | 4684 | S07 etiket PARKS (tik) | `tik-click.flac` | 156.1399 | -19 |
| 2:36.78 | 4703 | S07 etiket COURTS (tik) | `tik-click.flac` | 156.7799 | -19 |
| 2:41.64 | 4849 | S07 kesme: terazi: gider ↔ gelir (kısa whoosh) | `whoosh-kisa.flac` | 161.4382 | -27 |
| 2:45.10 | 4953 | S07 terazi gider tarafına yatar (~$7,400 OUT) (ahşap gıcırtı + thud) | `muhur-impact-punch.flac` | 165.0767 | -18 |
| 2:52.10 | 5163 | S07 −$2,000 / MO kırmızı (alarm tik) | `tik-click.flac` | 172.0999 | -17 |
| 2:52.10 | 5163 | S07 −$2,000 / MO kırmızı (alarm tik) | `tik-click.flac` | 172.2999 | -17 |
| 2:53.00 | 5190 | S07 kesme: masa orta: LOAN BOOK (kısa whoosh) | `whoosh-kisa.flac` | 172.7972 | -27 |
| 2:55.00 | 5250 | S07 LOAN BOOK masaya kayar, +$2,000 satırı (kitap kayma + kalem) | `sayfa-starninjas-book_flip_3.flac` | 174.7279 | -18 |
| 2:56.34 | 5290 | S08 LOAN BOOK açılır (kitap açılma) | `sayfa-starninjas-book_flip_3.flac` | 176.0679 | -18 |
| 3:02.40 | 5472 | S08 sayfalar masadan yere akar (kâğıt yağmuru) | `sayfa-starninjas-book_flip_2.flac` | 182.0795 | -20 |
| 3:02.40 | 5472 | S08 sayfalar masadan yere akar (kâğıt yağmuru) | `sayfa-starninjas-book_flip_3.flac` | 182.3779 | -22 |
| 3:03.44 | 5503 | S08 kesme: grafik G2: bakiye (kısa whoosh) | `whoosh-kisa.flac` | 183.2462 | -27 |
| 3:03.94 | 5518 | S08 sayaç ~$389,000 (tıkırtı + ding) | `ozgun-sayac-tikirti.flac` | 183.944 | -19 |
| 3:03.94 | 5518 | S08 sayaç ~$389,000 (tıkırtı + ding) | `ding-pwl-bell_ding1.flac` | 184.7065 | -21 |
| 3:14.34 | 5830 | S08 kesme: Leo yakın: pahalı değil (kısa whoosh) | `whoosh-kisa.flac` | 194.1452 | -27 |
| 3:30.86 | 6326 | S08 ok: cepten cebe (whoosh kısa) | `whoosh-kisa.flac` | 210.6622 | -23 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.175 | -18 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.295 | -18 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.415 | -18 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.535 | -18 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.655 | -18 |
| 3:39.18 | 6575 | S09 6 yıl kutusu sırayla dolar ($64,800 ×6) (tık ×6) | `ozgun-hesap-tus.flac` | 219.775 | -18 |
| 3:49.02 | 6871 | S09 kesme: masa orta: defter uzar (kısa whoosh) | `whoosh-kisa.flac` | 228.8192 | -27 |
| 3:49.52 | 6886 | S09 +$2,000 satırı (kalem) | `kagit-rubberduck-paper_03.flac` | 229.4734 | -21 |
| 3:52.49 | 6975 | S10 WHO HOLDS THE LOAN? (kapı zili) | `pop-drop.flac` | 232.486 | -20 |
| 3:55.29 | 7059 | S10 alacaklı ikonu (americans) (kapı zili / pop) | `pop-drop.flac` | 235.294 | -20 |
| 3:57.26 | 7118 | S10 alacaklı ikonu (pension) (kapı zili / pop) | `pop-drop.flac` | 237.264 | -20 |
| 3:58.51 | 7155 | S10 alacaklı ikonu (banks) (kapı zili / pop) | `pop-drop.flac` | 238.513 | -20 |
| 4:00.50 | 7215 | S10 alacaklı ikonu (foreign) (kapı zili / pop) | `pop-drop.flac` | 240.496 | -20 |
| 4:04.02 | 7321 | S10 alacaklı ikonu (federal) (kapı zili / pop) | `pop-drop.flac` | 244.02 | -20 |
| 4:05.31 | 7359 | S10 kesme: Leo yakın: IOU (kısa whoosh) | `whoosh-kisa.flac` | 245.1092 | -27 |
| 4:07.88 | 7436 | S10 IOU fişi (kâğıt) | `kagit-rubberduck-paper_03.flac` | 247.8334 | -21 |
| 4:13.94 | 7618 | S11 kesme: iki kredi başvurusu (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 253.7442 | -25 |
| 4:18.64 | 7759 | S11 DENIED damgası (aile) (damga thud) | `muhur-impact-punch.flac` | 258.6167 | -18 |
| 4:22.54 | 7876 | S11 APPROVED damgası (hane) (damga thud) | `muhur-impact-punch.flac` | 262.5167 | -18 |
| 4:24.20 | 7926 | S11 kesme: buzdolabı: soru notu (kısa whoosh) | `whoosh-kisa.flac` | 263.9992 | -27 |
| 4:24.40 | 7932 | S11 soru notu yapışır (slap) | `ozgun-yapiskan-not.flac` | 264.3919 | -15 |
| 4:28.56 | 8057 | S11 spot ışık kırmızı zarfa (gizem tını) | `ding-pwl-bell_ding1.flac` | 268.5225 | -25 |
| 4:31.75 | 8152 | S12 kırmızı INTEREST zarfı masaya kayar (kâğıt kayma) | `kagit-rubberduck-paper_03.flac` | 271.7024 | -21 |
| 4:36.02 | 8281 | S12 punch-in Leo + zarf (whoosh kısa) | `whoosh-kisa.flac` | 275.8272 | -23 |
| 4:37.12 | 8314 | S12 zarf açılır: içinden mor zarf (Leo G05) (zarf yırtma / kâğıt) | `zarf-spring-spring-snd_use_map.flac` | 276.9862 | -16 |
| 4:40.44 | 8413 | S12 BORROWED etiketi pop (pop) | `pop-pluck.flac` | 280.44 | -20 |
| 4:45.64 | 8569 | S12 çubuğun kırmızı faiz kısmı dolar: 53% OF THE GAP (yükselen ton) | `riser.flac` | 285.037 | -24 |
| 4:55.48 | 8864 | S12 kesme: kuşbakışı masa, matruşka başlar (whoosh) | `whoosh-kisa.flac` | 295.2782 | -23 |
| 4:55.85 | 8875 | S12 matruşka 1: mor zarftan kırmızı zarf çıkar + punch-in (kâğıt + tık) | `kagit-rubberduck-paper_04.flac` | 295.7719 | -22 |
| 4:55.85 | 8875 | S12 matruşka 1: mor zarftan kırmızı zarf çıkar + punch-in (kâğıt + tık) | `tik-click.flac` | 295.9259 | -20 |
| 5:00.16 | 9005 | S12 matruşka 2: kırmızıdan mor zarf + punch-in (kâğıt + tık) | `kagit-rubberduck-paper_04.flac` | 300.0839 | -22 |
| 5:00.16 | 9005 | S12 matruşka 2: kırmızıdan mor zarf + punch-in (kâğıt + tık) | `tik-click.flac` | 300.2379 | -20 |
| 5:02.90 | 9087 | S12 matruşka 3 + punch-in (kâğıt + tık (hızlanan)) | `kagit-rubberduck-paper_04.flac` | 302.8259 | -22 |
| 5:02.90 | 9087 | S12 matruşka 3 + punch-in (kâğıt + tık (hızlanan)) | `tik-click.flac` | 302.9799 | -20 |
| 5:03.80 | 9114 | S12 matruşka 4 + punch-in (kâğıt + tık (hızlanan)) | `kagit-rubberduck-paper_04.flac` | 303.7259 | -22 |
| 5:03.80 | 9114 | S12 matruşka 4 + punch-in (kâğıt + tık (hızlanan)) | `tik-click.flac` | 303.8799 | -20 |
| 5:05.63 | 9169 | S13 kesme: masa orta: şişman kırmızı zarf (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 305.4342 | -25 |
| 5:16.02 | 9481 | S13 kesme: grafik G3a: ortalama faiz (kısa whoosh) | `whoosh-kisa.flac` | 315.8222 | -27 |
| 5:22.30 | 9669 | S13 SEP 2026 ~3.5% (termometre yükselir) (yükselen ton) | `riser.flac` | 321.697 | -24 |
| 5:26.08 | 9782 | S13 kesme: grafik G3b: net faiz çubukları FY16–26 (kısa whoosh) | `whoosh-kisa.flac` | 325.8822 | -27 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.375 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.475 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.575 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.675 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.775 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.875 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 326.975 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 327.075 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 327.175 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 327.275 | -18 |
| 5:26.38 | 9791 | S13 11 çubuk sırayla (tık ×11) | `ozgun-hesap-tus.flac` | 327.375 | -18 |
| 5:28.68 | 9860 | S13 ~3× IN 5 YEARS (vuruş) | `muhur-impact-plate.flac` | 328.68 | -19 |
| 5:36.24 | 10087 | S13 FY2026 çubuğu yanıp söner (tik ×2) | `tik-click.flac` | 336.2399 | -17 |
| 5:36.24 | 10087 | S13 FY2026 çubuğu yanıp söner (tik ×2) | `tik-click.flac` | 336.4399 | -17 |
| 5:37.53 | 10126 | S14 kesme: Leo yakın (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 337.3342 | -25 |
| 5:54.08 | 10622 | S14 CHEAP 1% düşer → NEW 5% (etiket kopma + tık) | `kagit-rubberduck-paper_04.flac` | 354.0059 | -20 |
| 5:54.08 | 10622 | S14 CHEAP 1% düşer → NEW 5% (etiket kopma + tık) | `tik-click.flac` | 354.1799 | -20 |
| 5:56.34 | 10690 | S14 kesme: grafik G4: yeni faizler (kısa whoosh) | `whoosh-kisa.flac` | 356.1422 | -27 |
| 6:05.57 | 10967 | S15 kesme: gösterge: ortalama faiz tırmanır (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 365.3722 | -25 |
| 6:07.08 | 11012 | S15 ibre yükselir (yükselen ton) | `riser.flac` | 366.477 | -24 |
| 6:19.88 | 11397 | S15 RATE × BALANCE notu (slap) | `ozgun-yapiskan-not.flac` | 379.8789 | -15 |
| 6:21.27 | 11438 | S15 kesme: kuşbakışı: CAN'T SKIP (kısa whoosh) | `whoosh-kisa.flac` | 381.0682 | -27 |
| 6:23.38 | 11501 | S15 CAN'T SKIP damgası (damga) | `muhur-impact-punch.flac` | 383.3567 | -18 |
| 6:26.32 | 11590 | S15 FAMILY yazısı çatlar (cam çatlama) | `muhur-impact-plate.flac` | 386.32 | -19 |
| 6:31.02 | 11731 | S16 kesme: kart: 1 · OWN MONEY (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 390.8212 | -25 |
| 6:31.17 | 11735 | S16 1 · IT BORROWS IN ITS OWN MONEY (pop) | `pop-pluck.flac` | 391.169 | -20 |
| 6:43.51 | 12105 | S16 kesme: buzdolabı: soru notuna tik (kısa whoosh) | `whoosh-kisa.flac` | 403.3112 | -27 |
| 6:46.90 | 12207 | S16 yeşil tik (A5 kapanır) (doğru ding) | `ding-pwl-bell_ding1.flac` | 406.8625 | -21 |
| 6:49.70 | 12291 | S16 banknotlar çoğalır, sepet küçülür (fotokopi vınlaması) | `riser.flac` | 409.094 | -24 |
| 6:53.68 | 12410 | S16 INFLATION (vuruş) | `muhur-impact-plate.flac` | 413.68 | -19 |
| 6:54.70 | 12441 | S16 kesme: Leo yakın (kısa whoosh) | `whoosh-kisa.flac` | 414.5032 | -27 |
| 6:58.21 | 12546 | S17 2 · IT NEVER RETIRES (pop) | `pop-pluck.flac` | 418.206 | -20 |
| 7:04.46 | 12734 | S17 takvim sonsuz çevrilir (kâğıt çevirme) | `kagit-rubberduck-paper_03.flac` | 424.4134 | -21 |
| 7:05.22 | 12757 | S17 kesme: masa orta: IOU takla (kısa whoosh) | `whoosh-kisa.flac` | 425.0222 | -27 |
| 7:05.92 | 12778 | S17 IOU fişleri takla atar (kâğıt hışırtı) | `kagit-rubberduck-paper_03.flac` | 425.8734 | -21 |
| 7:12.46 | 12974 | S17 PAY IT ALL BACK? üstü çizilir (kalem çizme) | `kagit-rubberduck-paper_03.flac` | 432.4134 | -21 |
| 7:13.98 | 13019 | S17 KEEP PAYING THE INTEREST? (pop) | `pop-pluck.flac` | 433.98 | -20 |
| 7:18.49 | 13155 | S18 kesme: kart: 3 · GIVE ITSELF A RAISE (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 438.2952 | -25 |
| 7:18.64 | 13159 | S18 3 · IT CAN GIVE ITSELF A RAISE (pop) | `pop-pluck.flac` | 438.643 | -20 |
| 7:24.28 | 13328 | S18 maaş zarfına kadran (yukarı/aşağı) (kadran tık-tık) | `tik-click.flac` | 444.2799 | -17 |
| 7:24.28 | 13328 | S18 maaş zarfına kadran (yukarı/aşağı) (kadran tık-tık) | `tik-click.flac` | 444.4799 | -17 |
| 7:25.94 | 13378 | S18 makas zarfı keser (makas) | `kagit-rubberduck-paper_03.flac` | 445.8934 | -21 |
| 7:33.50 | 13605 | S18 Leo gülümser (omuz silker) (hafif tını) | `ding-pwl-bell_ding1.flac` | 453.4625 | -25 |
| 7:34.87 | 13646 | S19 kesme: masa orta, Leo (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 454.6752 | -25 |
| 7:37.74 | 13732 | S19 çizgi çizilmeye başlar, >100% (1946) (çizim sesi) | `kagit-rubberduck-paper_03.flac` | 457.6954 | -21 |
| 7:50.42 | 14113 | S19 ~23% (1974) etiketi (ding) | `ding-pwl-bell_ding1.flac` | 470.3825 | -21 |
| 7:51.62 | 14149 | S19 kesme: grafik: borç $ çubuğu (kısa whoosh) | `whoosh-kisa.flac` | 471.4212 | -27 |
| 7:55.48 | 14264 | S19 $242B → $344B çubuğu yükselir (yükselen ton) | `riser.flac` | 474.877 | -24 |
| 8:01.45 | 14444 | S19 maaş zarfı büyür (şişme) | `riser.flac` | 480.849 | -24 |
| 8:03.09 | 14493 | S19 kesme: Leo yakın (kısa whoosh) | `whoosh-kisa.flac` | 482.8892 | -27 |
| 8:07.80 | 14634 | S20 kesme: grafik G5 devam: ~97% (Q2 2026) (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 487.5982 | -25 |
| 8:11.46 | 14744 | S20 ayrı nokta ~97% (FRED) (ding) | `ding-pwl-bell_ding1.flac` | 491.4225 | -21 |
| 8:16.24 | 14887 | S20 sarmal dönmeye başlar (dönen whoosh) | `whoosh-uzun.flac` | 496.063 | -22 |
| 8:27.16 | 15215 | S20 kesme: üç fren ikonu (kısa whoosh) | `whoosh-kisa.flac` | 506.9622 | -27 |
| 8:28.46 | 15254 | S20 fren 1 OWN CURRENCY (fren tık) | `tik-click.flac` | 508.4599 | -19 |
| 8:30.64 | 15319 | S20 fren 2 LONG LOANS (fren tık) | `tik-click.flac` | 510.6399 | -19 |
| 8:38.10 | 15543 | S20 fren 3 LENDERS' TRUST (fren tık) | `tik-click.flac` | 518.0999 | -19 |
| 8:41.09 | 15633 | S20 kesme: Leo yakın (kısa whoosh) | `whoosh-kisa.flac` | 520.8962 | -27 |
| 8:47.85 | 15836 | S21 kesme: masa orta: üç olasılık (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 527.6532 | -25 |
| 8:49.08 | 15872 | S21 not A · GROW (tap) | `tik-click.flac` | 529.0799 | -19 |
| 8:58.83 | 16165 | S21 kesme: buzdolabı: A · B · C dolar (kısa whoosh) | `whoosh-kisa.flac` | 538.6302 | -27 |
| 9:00.34 | 16210 | S21 not B · CHANGE THE ENVELOPES (tap) | `tik-click.flac` | 540.3399 | -19 |
| 9:00.76 | 16223 | S21 not C · LET PRICES RISE (tap) | `tik-click.flac` | 540.7599 | -19 |
| 9:02.00 | 16260 | S22 A · GROW THE PAYCHECK (düdük) | `ozgun-duduk.flac` | 541.9964 | -20 |
| 9:05.34 | 16360 | S22 maaş öne geçer (koşu whoosh) | `whoosh-uzun.flac` | 545.165 | -22 |
| 9:15.36 | 16661 | S22 kesme: Leo yakın: GROWTH vs RATE (kısa whoosh) | `whoosh-kisa.flac` | 555.1592 | -27 |
| 9:15.66 | 16670 | S22 GROWTH vs RATE (hakem düdüğü) | `ozgun-duduk.flac` | 555.6504 | -20 |
| 9:22.90 | 16887 | S22 borç defteri öne geçer (olumsuz vuruş) | `ozgun-gerilim-vurus.flac` | 562.9 | -18 |
| 9:25.40 | 16962 | S22 kırmızı zarf şişer (şişme) | `riser.flac` | 564.797 | -24 |
| 9:26.63 | 16999 | S23 kesme: kuşbakışı: B · CHANGE THE ENVELOPES (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 566.4362 | -25 |
| 9:30.36 | 17111 | S23 CUT SPENDING + makas (makas) | `kagit-rubberduck-paper_03.flac` | 570.3134 | -21 |
| 9:38.02 | 17341 | S23 silüet (retirees) (pop) | `pop-pluck.flac` | 578.021 | -20 |
| 9:38.78 | 17363 | S23 silüet (patients) (pop) | `pop-pluck.flac` | 578.78 | -20 |
| 9:39.50 | 17385 | S23 silüet (soldiers) (pop) | `pop-pluck.flac` | 579.5 | -20 |
| 9:39.70 | 17391 | S23 silüet (students) (pop) | `pop-pluck.flac` | 579.7 | -20 |
| 9:40.48 | 17414 | S23 kesme: masa orta: slow and loud (kısa whoosh) | `whoosh-kisa.flac` | 580.2832 | -27 |
| 9:47.37 | 17621 | S24 kesme: kart: C · LET PRICES RISE (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 587.1672 | -25 |
| 9:47.51 | 17625 | S24 C · LET PRICES RISE (pop) | `pop-pluck.flac` | 587.515 | -20 |
| 9:51.58 | 17747 | S24 banknotlar küçülür (büzülme) | `pop-drop.flac` | 591.58 | -20 |
| 9:58.58 | 17957 | S24 kesme: 1946: PRICES +18% (kısa whoosh) | `whoosh-kisa.flac` | 598.3822 | -27 |
| 10:01.78 | 18053 | S24 +18% (1946) (ding) | `ding-pwl-bell_ding1.flac` | 601.7425 | -21 |
| 10:09.36 | 18281 | S24 market fişi uzar (yazarkasa fişi) | `ozgun-ka-ching.flac` | 609.3599 | -17 |
| 10:10.06 | 18302 | S24 kesme: Leo yakın: zarf geri şişer (kısa whoosh) | `whoosh-kisa.flac` | 609.8622 | -27 |
| 10:18.48 | 18554 | S24 kırmızı zarf şişer + OLD DEBT SHRINKS · NEW RATES RISE (şişme) | `riser.flac` | 617.877 | -24 |
| 10:20.52 | 18616 | S25 kesme: buzdolabı: A B C + LUCK (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 620.3262 | -25 |
| 10:24.30 | 18729 | S25 + LUCK notu (tap) | `tik-click.flac` | 624.2999 | -19 |
| 10:31.74 | 18952 | S25 kesme: kart: ONE LETTER IN THE COMMENTS (kısa whoosh) | `whoosh-kisa.flac` | 631.5402 | -27 |
| 10:31.94 | 18958 | S25 A · B · C → ONE LETTER IN THE COMMENTS (pop ×3) | `pop-pluck.flac` | 631.938 | -20 |
| 10:31.94 | 18958 | S25 A · B · C → ONE LETTER IN THE COMMENTS (pop ×3) | `pop-pluck.flac` | 632.088 | -20 |
| 10:31.94 | 18958 | S25 A · B · C → ONE LETTER IN THE COMMENTS (pop ×3) | `pop-pluck.flac` | 632.238 | -20 |
| 10:37.95 | 19138 | S26 kesme: buzdolabı: tez notu + 3 tik (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 637.7512 | -25 |
| 10:43.52 | 19306 | S26 tik 1 (tik) | `tik-click.flac` | 643.5199 | -19 |
| 10:44.56 | 19337 | S26 tik 2 (tik) | `tik-click.flac` | 644.5599 | -19 |
| 10:46.52 | 19396 | S26 tik 3 (tik) | `tik-click.flac` | 646.5199 | -19 |
| 10:52.34 | 19570 | S26 kesme: masa geniş: lamba kısılır (kısa whoosh) | `whoosh-kisa.flac` | 652.1422 | -27 |
| 11:01.82 | 19855 | S26 kırmızı zarftan iç zarf kenarı görünür (kâğıt) | `kagit-rubberduck-paper_03.flac` | 661.7734 | -21 |
| 11:03.16 | 19895 | S27 kesme: masa orta: bir sayı (sahne geçişi (yumuşak whoosh)) | `whoosh-kisa.flac` | 662.9662 | -25 |
| 11:13.08 | 20192 | S27 not pencereden uçar (kâğıt uçuşu) | `sayfa-starninjas-book_flip_2.flac` | 672.7625 | -20 |
| 11:13.08 | 20192 | S27 not pencereden uçar (kâğıt uçuşu) | `sayfa-starninjas-book_flip_3.flac` | 673.0609 | -22 |

## Sessiz bırakılan olaylar (70)

| t | tür | öneri | neden |
|---|---|---|---|
| 6.725 | kesme | whoosh | whoosh aralığı <10.0 sn |
| 9.32 | kesme | boş | kural: ses yok |
| 16.028 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 21.761 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 33.859 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 40.883 | pop | boş | kural: ses yok |
| 48.992 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 53.125 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 57.593 | pop | kasa ding | önceki SFX'e <0.12 sn |
| 100.808 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 101.34 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 119.658 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 125.704 | pop | boş | kural: ses yok |
| 133.482 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 144.01 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 159.31 | pop | boş | kural: ses yok |
| 167.46 | pop | boş | kural: ses yok |
| 175.547 | abone | klik (kurgu-editoru bileşeni) | kural: ses yok |
| 176.097 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 189.14 | pop | boş | kural: ses yok |
| 197.54 | pop | boş | kural: ses yok |
| 201.866 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 204.68 | pop | boş | kural: ses yok |
| 212.636 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 212.736 | pop | boş | kural: ses yok |
| 218.88 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 224.42 | pop | boş | kural: ses yok |
| 232.286 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 235.194 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 248.78 | vurgu | boş | kural: ses yok |
| 267.105 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 281.449 | kesme | boş | kural: ses yok |
| 288.544 | kesme | boş | kural: ses yok |
| 305.082 | abone | klik (kurgu-editoru bileşeni) | kural: ses yok |
| 316.52 | pop | boş | kural: ses yok |
| 329.96 | pop | boş | kural: ses yok |
| 342 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 344.9 | pop | boş | kural: ses yok |
| 346.28 | pop | boş | kural: ses yok |
| 356.74 | pop | boş | kural: ses yok |
| 362.34 | pop | boş | kural: ses yok |
| 375.543 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 384.071 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 407.7 | etkilesim | (sessiz) | kural: ses yok |
| 407.815 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 409.197 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 418.056 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 430.118 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 447.31 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 457.542 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 480.098 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 495.838 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 502.42 | vurgu | boş | kural: ses yok |
| 505.49 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 533.96 | pop | boş | kural: ses yok |
| 541.853 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 551.61 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 558.944 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 569.354 | pop | boş | kural: ses yok |
| 574.78 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 585.44 | vurgu | boş | kural: ses yok |
| 605.773 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 628.172 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 638.149 | pop | boş | kural: ses yok |
| 647.342 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 657.08 | vurgu | boş | kural: ses yok |
| 662.614 | abone | klik (kurgu-editoru bileşeni) | kural: ses yok |
| 670.349 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 671.56 | kamera | boş | kural: ses yok |
| 672.683 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
