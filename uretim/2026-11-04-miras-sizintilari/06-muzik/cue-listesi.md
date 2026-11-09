# Cue listesi — 2026-11-04-miras-sizintilari S03 (F6a müzik; SFX bölümü F6b'de dolar)

Kaynak: `06-muzik/cue.json` (`cue-uret.py` ← `animasyon-efekt-cue.json` tahmini=false + `04-ses/sahne-zamanlari.json`). Zaman ekseni = `04-ses/anlatim.wav` (781.388 sn). Kare = 30 fps.
Stem'ler: `stems/muzik-stem.wav`, `stems/sfx-stem.wav` (48 kHz stereo 24-bit, anlatımla örnek örnek aynı uzunluk, 0 noktası = anlatımın 0'ı). Montajda anlatım kaydırılırsa iki stem de aynı kadar kaydırılır.
Abone klik sesi stem'de YOK: `assets/efekt/ozgun-fare-klik.flac`'ı kurgu-editoru AboneOl bileşeniyle görsel tıklamaya ±2 kare yerleştirir (olaylar: 105.696 sn, 428.981 sn, 773.049 sn).

## Müzik bölümleri

| # | Bölüm | Giriş → çıkış | Kare | Parça (lisans) | Ruh hali / tempo | Konuşma altı | Giriş/çıkış sönüşü |
|---|---|---|---|---|---|---|---|
| 1 | B1 yola çıkış (Bölüm 1: The Number on the Truck) | 0:00.00 → 1:46.25 | 0–3187 | Wasteland Caravan — vitalezzz (CC0) | merak + yola çıkış, akustik/elektro gitar · ≈171 BPM ölçüm, yarım tempo hissi [tahmin] | −22 dB | 0.4 / 1.2 sn · ofset 203.0 |
| 2 | B2 Okafor ailesi (Bölüm 2) | 1:46.25 → 2:35.21 | 3187–4656 | Sunny Side Up — Pro Sensory (CC0) | sıcak aile, hafif caz-pop · ≈84 BPM [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 85.0 |
| 3 | B3 yaşam ve bakım (Bölüm 3) | 2:35.21 → 4:58.97 | 4656–8969 | Insistent — yd (CC0) | ciddi, seyrek, karanlık-sessiz · sabit yatak [tahmin] | −19 dB | 1.2 / 1.2 sn · ofset 23.0 |
| 4 | B4 sapma ve bağış (Bölüm 4) | 4:58.97 → 7:09.53 | 8969–12886 | Remember this shadow — Komiku (CC0) | yol değiştiren, meraklı · ≈86 BPM [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 49.0 |
| 5 | B5 en ağır kutu: ev (Bölüm 5) | 7:09.53 → 8:17.88 | 12886–14936 | The road we use to travel when we were kids — Komiku (CC0) | nostalji, ev, sıcak · ≈87 BPM [tahmin] | −22 dB | 1.2 / 0.05 sn · ofset 88.0 |
| 6 | B6 vergi durağı (Bölüm 6) | 8:18.88 → 10:42.75 | 14966–19283 | Lone Scavenger — vitalezzz (CC0) | hafif gerilim, gitar · ≈171 BPM ölçüm [tahmin] | −22 dB | 2.0 / 1.2 sn · ofset 136.0 |
| 7 | B7 varış + envanter (Bölüm 7) | 10:42.75 → 12:39.95 | 19283–22798 | Wasteland Caravan — vitalezzz (CC0) | varış, açılışa dönüş (kitap ayracı) · ≈171 BPM ölçüm [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 60.0 |
| 8 | B8 tez + köprü (S30–S31) | 12:39.95 → 13:01.39 | 22798–23442 | Joy Ride — Pro Sensory (CC0) | sıcak kapanış · ≈90 BPM [tahmin] | −22 dB | 1.2 / 2.0 sn · ofset 45.0 |

Notlar: bölüm sınırları sahne kesmelerinde (`04-ses/sahne-zamanlari.json`), geçişler 1.2 sn eşit güçte. B7 = B1 parçasının başka kesiti (yola çıkış ↔ varış). Ofset = parçada başlangıç saniyesi (en sabit 40 sn pencere). Konuşma boşluğu ≥0.9 sn olunca müzik +6 dB açılır.

## Shorts müzik yatakları (60 sn, sonda 2 sn sönüş; kurgu kesit uzunluğuna kırpar)

- `stems/shorts-1-muzik-stem.wav` ← `$M/remember-this-shadow-komiku.mp3` (konuşma altı −20 dB, mobil)
- `stems/shorts-2-muzik-stem.wav` ← `$M/lone-scavenger-vitalezzz.mp3` (konuşma altı −20 dB, mobil)

## SFX vuruşları (201 vuruş, 168 görsel olay; hizalama: geçiş whoosh'unda tepe, diğerlerinde ses başlangıcı olay karesinde)

| Olay zamanı | Kare | Olay | Dosya | Dosya başı (sn) | Kazanç dB |
|---|---|---|---|---|---|
| 0:00.10 | 3 | S01 kamyon arka kapısı açılır, dev kutu $124T (metal kapı + sürgü) | `kamyon-ggbotnet-car_trunk_open.flac` | 0.0478 | -18 |
| 0:00.10 | 3 | S01 kamyon arka kapısı açılır, dev kutu $124T (metal kapı + sürgü) | `es-toggle-latch.flac` | 0.3979 | -22 |
| 0:01.60 | 48 | S01 kutunun köşesinden banknot damlar (≤3 sn görsel değişim) (damla / kâğıt) | `es-drip-drop.flac` | 1.5895 | -18 |
| 0:01.60 | 48 | S01 kutunun köşesinden banknot damlar (≤3 sn görsel değişim) (damla / kâğıt) | `para-owlishmedia-money_33.flac` | 1.4951 | -24 |
| 0:09.50 | 285 | S01 dilim kayar: $18T → CHARITY (kâğıt kayma) | `es-swipe-paper.flac` | 9.3066 | -24 |
| 0:10.36 | 311 | S01 kesme: kamyon yan şeride sinyal: sarı tabela (kısa whoosh) | `es-whoosh-whip.flac` | 10.1546 | -27 |
| 0:11.92 | 358 | S01 sinyal + SPOUSE FIRST tabelası (sinyal tık-tık) | `es-click-thock.flac` | 11.9179 | -20 |
| 0:11.92 | 358 | S01 sinyal + SPOUSE FIRST tabelası (sinyal tık-tık) | `es-click-thock.flac` | 12.2679 | -20 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.0969 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.1769 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.2569 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.3369 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.4169 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.4969 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.5769 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.6569 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.7369 | -24 |
| 0:15.11 | 453 | S01 dev kutu 10 kutuya bölünür (karton pop ×10) | `es-knock-wood.flac` | 15.8169 | -24 |
| 0:16.48 | 494 | S02 kesme: ABD haritası, küçük kamyonlar (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 16.0812 | -26 |
| 0:16.78 | 503 | S02 ekran yazısı: OFTEN CALLED THE BIGGEST INHERITANCE IN HISTORY (hafif pop) | `es-ui-pop-soft.flac` | 16.7683 | -25 |
| 0:29.35 | 880 | S02 ekran yazısı: HEIR? HOME BUYER? BOTH? (hafif pop) | `es-ui-pop-soft.flac` | 29.3393 | -25 |
| 0:31.00 | 930 | S02 kesme: Leo kamyon kapısında (kısa whoosh) | `es-whoosh-tight.flac` | 30.7981 | -27 |
| 0:33.96 | 1019 | S02 ekran yazısı: LESS? LATER? (hafif pop) | `es-ui-pop-soft.flac` | 33.9503 | -25 |
| 0:37.36 | 1121 | S02 soru işaretli kutu sallanır (gizem tını) | `es-shimmer.flac` | 37.3596 | -27 |
| 0:39.17 | 1175 | S03 kesme: Leo kamyon kapısında (yelek, pano, bant) (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 38.7762 | -26 |
| 0:39.47 | 1184 | S03 isim etiketi LEO · MOVING CREW BOSS (hafif pop) | `es-ui-pop-soft.flac` | 39.4633 | -25 |
| 0:39.86 | 1196 | S03 Leo göz kırpar (tık) | `es-click-soft.flac` | 39.858 | -21 |
| 0:48.94 | 1468 | S03 tez yazısı boyanır (fırça / sprey) | `es-swipe-paper.flac` | 48.7446 | -24 |
| 0:53.58 | 1607 | S03 kontak: motor çalışır (motor SFX) | `motor-looneybits-startengine.flac` | 53.4976 | -20 |
| 0:54.18 | 1625 | S04 kesme: Leo büyüteçle dev kutunun etiketini okur (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 53.7822 | -26 |
| 1:05.17 | 1955 | S04 kesme: grafik G1: tek çubuk $124T (kısa whoosh) | `es-whoosh-whip.flac` | 64.9636 | -27 |
| 1:10.56 | 2117 | S04 çubuk dolar: ~$105T HEIRS (lacivert) (yükselen tık) | `es-zip-up.flac` | 70.551 | -25 |
| 1:14.43 | 2233 | S04 ~$18T CHARITY (yeşil) dilimi (pop) | `es-pop-0.flac` | 74.4338 | -21 |
| 1:17.70 | 2331 | S04 kesme: Leo: here's the twist (kısa whoosh) | `es-whoosh-tight.flac` | 77.5051 | -27 |
| 1:19.67 | 2390 | S04 sarı tabela SPOUSE FIRST · ~$54T STOP (tabela tok) | `es-knock-desk.flac` | 79.6526 | -19 |
| 1:26.55 | 2596 | S04 ok çubuğa geri döner (whoosh kısa) | `es-whoosh-whip.flac` | 86.3426 | -25 |
| 1:27.76 | 2633 | S04 punch-in: SPOUSE FIRST tabelasına (kısa whoosh / tık) | `es-whoosh-whip.flac` | 87.5576 | -25 |
| 1:34.74 | 2842 | S04 pano: DETOUR ≠ LEAK (keçeli kalem) | `kalem-owlishmedia-stationery_04.flac` | 94.1677 | -22 |
| 1:37.46 | 2924 | S05 kesme: harita → kamera tek eve iner (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 97.0652 | -26 |
| 1:43.62 | 3109 | S05 ekran yazısı: ONE FAMILY. ONE TRUCK. (hafif pop) | `es-ui-pop-soft.flac` | 103.6103 | -25 |
| 1:46.25 | 3187 | S06 kesme: kapı eşiğinde 4 düz siluet + EXAMPLE FAMILY etiketi (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 105.8492 | -26 |
| 1:55.45 | 3463 | S06 4 kiremit HOUSE kutusu yerine oturur (karton tok ×4) | `es-knock-wood.flac` | 115.4339 | -21 |
| 1:55.45 | 3463 | S06 4 kiremit HOUSE kutusu yerine oturur (karton tok ×4) | `es-knock-wood.flac` | 115.5839 | -21 |
| 1:55.45 | 3463 | S06 4 kiremit HOUSE kutusu yerine oturur (karton tok ×4) | `es-knock-wood.flac` | 115.7339 | -21 |
| 1:55.45 | 3463 | S06 4 kiremit HOUSE kutusu yerine oturur (karton tok ×4) | `es-knock-wood.flac` | 115.8839 | -21 |
| 1:57.12 | 3514 | S06 4 lacivert RETIREMENT kutusu (karton tok ×4) | `es-knock-wood.flac` | 117.1079 | -21 |
| 1:57.12 | 3514 | S06 4 lacivert RETIREMENT kutusu (karton tok ×4) | `es-knock-wood.flac` | 117.2579 | -21 |
| 1:57.12 | 3514 | S06 4 lacivert RETIREMENT kutusu (karton tok ×4) | `es-knock-wood.flac` | 117.4079 | -21 |
| 1:57.12 | 3514 | S06 4 lacivert RETIREMENT kutusu (karton tok ×4) | `es-knock-wood.flac` | 117.5579 | -21 |
| 1:59.00 | 3570 | S06 2 yeşil BANK kutusu (karton tok ×2) | `es-knock-wood.flac` | 118.9819 | -21 |
| 1:59.00 | 3570 | S06 2 yeşil BANK kutusu (karton tok ×2) | `es-knock-wood.flac` | 119.1319 | -21 |
| 2:00.54 | 3616 | S06 ekran yazısı: 10 BOXES = ALL THEIR WEALTH (hafif pop) | `es-ui-pop-soft.flac` | 120.5283 | -25 |
| 2:03.66 | 3710 | S06 ekran yazısı: ILLUSTRATION, NOT AN AVERAGE (hafif pop) | `es-ui-pop-soft.flac` | 123.6533 | -25 |
| 2:08.02 | 3841 | S06 kesme: Leo her kutuya TO: THE KIDS yazar (kısa whoosh) | `es-whoosh-whip.flac` | 127.8216 | -27 |
| 2:11.16 | 3935 | S06 keçeli: TO: THE KIDS (keçeli kalem) | `kalem-owlishmedia-stationery_04.flac` | 130.5857 | -22 |
| 2:12.23 | 3967 | S06 ekran yazısı: RULE 1: LABEL EVERYTHING (hafif pop) | `es-ui-pop-soft.flac` | 132.2223 | -25 |
| 2:15.01 | 4050 | S06 ekran yazısı: RULE 2: CHECK THE BOTTOM (hafif pop) | `es-ui-pop-soft.flac` | 134.9973 | -25 |
| 2:18.58 | 4157 | S06 kesme: Leo kameraya: we'll see (kısa whoosh) | `es-whoosh-tight.flac` | 138.3841 | -27 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 141.678 | -21 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 141.928 | -21 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 142.178 | -21 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 142.428 | -21 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 142.678 | -21 |
| 2:21.68 | 4250 | S07 pano satırları sırayla yazılır ×6 (kalem tık ×6) | `es-click-soft.flac` | 142.928 | -21 |
| 2:29.42 | 4483 | S07 punch-in: TAX tabelasına (kısa whoosh / tık) | `es-whoosh-whip.flac` | 149.2176 | -25 |
| 2:34.06 | 4622 | S07 kamyon kalkar (motor + korna) | `kamyon-ggbotnet-car_horn.flac` | 154.0004 | -24 |
| 2:34.06 | 4622 | S07 kamyon kalkar (motor + korna) | `kamyon-ggbotnet-car_engine_start_up.flac` | 154.2608 | -24 |
| 2:35.21 | 4656 | S08 kesme: durak tabelası LIVING (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 154.8102 | -26 |
| 2:42.30 | 4869 | S08 zaman şeridi uzar: ~20 MORE YEARS (yükselen tık) | `es-zip-up.flac` | 162.293 | -25 |
| 2:54.37 | 5231 | S08 kesme: kutular: 2 kutuya SPENT ON LIVING damgası (kısa whoosh) | `es-whoosh-tight.flac` | 174.1741 | -27 |
| 2:56.40 | 5292 | S08 SPENT ON LIVING damgası ×2 (damga thud ×2) | `es-impact-punch.flac` | 176.3956 | -20 |
| 2:56.40 | 5292 | S08 SPENT ON LIVING damgası ×2 (damga thud ×2) | `es-impact-punch.flac` | 176.7956 | -20 |
| 3:05.07 | 5552 | S08 kesme: ekran: ONE COUNTRY-WIDE TOTAL ≠ ONE FAMILY'S BOXES (D-1) (kısa whoosh) | `es-whoosh-whip.flac` | 184.8636 | -27 |
| 3:14.14 | 5824 | S09 kesme: sisli yoldan CARE tabelası belirir (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 193.7462 | -26 |
| 3:14.64 | 5839 | S09 CARE tabelası sisten çıkar (rüzgâr / sis) | `es-whoosh-yukselen.flac` | 193.6726 | -24 |
| 3:19.75 | 5993 | S10 kesme: Leo: stop two is care (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 199.3572 | -26 |
| 3:30.90 | 6327 | S10 56 ikon renklenir: 56% (tıkırtı) | `es-typing-run.flac` | 210.8954 | -23 |
| 3:38.17 | 6545 | S10 22 ikon koyulaşır: >5 YEARS 22% (tık) | `es-click-soft.flac` | 218.165 | -21 |
| 3:41.42 | 6643 | S10 kesme: evde aile / huzurevi siluetleri (kısa whoosh) | `es-whoosh-tight.flac` | 221.2201 | -27 |
| 3:51.34 | 6940 | S10 fatura kartı sayacı $129,575 (yazar kasa) | `ozgun-ka-ching.flac` | 231.3399 | -18 |
| 3:59.06 | 7172 | S11 kesme: Leo: why does this one leak so much? (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 238.6592 | -26 |
| 4:01.30 | 7239 | S11 levha: LONG-TERM CUSTODIAL CARE: GENERALLY NOT COVERED (levha tok) | `es-knock-desk.flac` | 241.2866 | -19 |
| 4:08.64 | 7459 | S11 punch-in: MEDICARE levhasına (kısa whoosh / tık) | `es-whoosh-whip.flac` | 248.4376 | -25 |
| 4:12.07 | 7562 | S11 MEDICAID levhası (levha tok) | `es-knock-desk.flac` | 252.0606 | -19 |
| 4:17.08 | 7712 | S11 el ESTATE RECOVERY etiketi yapıştırır (etiket yapışma) | `bant-owlishmedia-stationery_27.flac` | 256.8174 | -20 |
| 4:21.43 | 7843 | S11 kesme: grafik: 7 ikondan 1'i kırmızı (kısa whoosh) | `es-whoosh-tight.flac` | 261.2311 | -27 |
| 4:24.26 | 7928 | S11 7'de 1 ikon kırmızı: $100K+ (ding) | `es-mallet-glock.flac` | 264.2597 | -21 |
| 4:32.68 | 8180 | S11 kesme: pano CARE −1 (kısa whoosh) | `es-whoosh-whip.flac` | 272.4776 | -27 |
| 4:35.39 | 8262 | S11 CARE −1 kalem çizgisi (keçeli çizgi) | `kalem-owlishmedia-stationery_04.flac` | 274.8148 | -22 |
| 4:41.28 | 8438 | S12 kesme: kasa içi: Leo (M09) (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 280.8812 | -26 |
| 4:45.64 | 8569 | S12 bant 1 çekilir (koli bandı çekme) | `bant-owlishmedia-stationery_26.flac` | 285.4556 | -16 |
| 4:47.05 | 8612 | S12 başka köşeden damla (damla) | `es-drip-plink.flac` | 287.0489 | -18 |
| 4:49.21 | 8676 | S12 bant 2 çekilir (koli bandı çekme) | `bant-owlishmedia-stationery_26.flac` | 289.0216 | -16 |
| 4:50.56 | 8717 | S12 ekran yazısı: TAPE USED: 2 (hafif pop) | `es-ui-pop-soft.flac` | 290.5543 | -25 |
| 4:55.38 | 8861 | S12 kesme: pano −3 (kısa whoosh) | `es-whoosh-tight.flac` | 295.1811 | -27 |
| 4:59.27 | 8978 | S13 sinyal (sinyal tık-tık) | `es-click-thock.flac` | 299.2719 | -20 |
| 4:59.27 | 8978 | S13 sinyal (sinyal tık-tık) | `es-click-thock.flac` | 299.6219 | -20 |
| 5:09.27 | 9278 | S13 kesme: kamyon karşı kaldırıma yanaşır (kısa whoosh) | `es-whoosh-whip.flac` | 309.0676 | -27 |
| 5:25.00 | 9750 | S13 kesme: Leo kutulardaki isimleri gösterir (kısa whoosh) | `es-whoosh-tight.flac` | 324.8011 | -27 |
| 5:34.83 | 10045 | S14 kesme: pano: SPOUSE −0 + kum saati +YEARS (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 334.4322 | -26 |
| 5:39.28 | 10178 | S14 SPOUSE −0 yazılır (kalem tık) | `es-click-soft.flac` | 339.277 | -21 |
| 5:39.88 | 10196 | S14 kum saati +YEARS döner (kum saati) | `es-notify-wood.flac` | 339.8722 | -22 |
| 5:45.00 | 10350 | S14 kesme: park hâlinde kamyon, takvim yaprakları; LIVING/CARE ikinci kez (kısa whoosh) | `es-whoosh-whip.flac` | 344.7926 | -27 |
| 5:49.60 | 10488 | S14 LIVING / CARE tabelaları ikinci kez geçer (whoosh ×2) | `es-whoosh-tight.flac` | 349.4051 | -25 |
| 5:49.60 | 10488 | S14 LIVING / CARE tabelaları ikinci kez geçer (whoosh ×2) | `es-whoosh-tight.flac` | 349.9051 | -25 |
| 6:00.28 | 10808 | S14 kesme: Leo: more time (kısa whoosh) | `es-whoosh-tight.flac` | 360.0811 | -27 |
| 6:06.61 | 10998 | S14 bayrak eşe geçer (bayrak devri) | `es-swish-soft.flac` | 366.3674 | -23 |
| 6:13.22 | 11197 | S15 kesme: GIVING tabelası, küçük kalp (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 372.8222 | -26 |
| 6:13.72 | 11212 | S15 kalp parlar (sıcak tını) | `es-mallet-celesta.flac` | 373.7169 | -22 |
| 6:19.72 | 11391 | S16 kesme: Leo: stop four is giving (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 379.3192 | -26 |
| 6:25.55 | 11567 | S16 ikon SCHOOLS (tik) | `es-hover-tick.flac` | 385.5509 | -22 |
| 6:26.58 | 11597 | S16 ikon HOSPITALS (tik) | `es-hover-tick.flac` | 386.5779 | -22 |
| 6:27.80 | 11634 | S16 ikon CHURCHES (tik) | `es-hover-tick.flac` | 387.7929 | -22 |
| 6:29.75 | 11693 | S16 ikon RESEARCH (tik) | `es-hover-tick.flac` | 389.7489 | -22 |
| 6:37.80 | 11934 | S16 kesme: kamyon okulun önünde, yeşil kutu kapıya (kısa whoosh) | `es-whoosh-whip.flac` | 397.5966 | -27 |
| 6:43.91 | 12117 | S16 GIVEN etiketi (keçeli kalem) | `kalem-owlishmedia-stationery_04.flac` | 403.3417 | -22 |
| 6:50.54 | 12316 | S17 kesme: grafik G3: iki çubuk (sol-orta) (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 410.1402 | -26 |
| 6:57.88 | 12536 | S17 çubuk 2026: 47% (tık) | `es-click-soft.flac` | 417.878 | -21 |
| 7:04.48 | 12734 | S17 çubuk 2024: 55% (geri bakış) (tık) | `es-click-soft.flac` | 424.478 | -21 |
| 7:05.96 | 12779 | S17 kesme: Leo kutuyu iki siluet arasında tutar (sol) (kısa whoosh) | `es-whoosh-tight.flac` | 425.7621 | -27 |
| 7:11.22 | 12937 | S18 pano satırı LIVING tik (tik) | `es-hover-tick.flac` | 431.2199 | -22 |
| 7:12.65 | 12980 | S18 pano satırı CARE tik (tik) | `es-hover-tick.flac` | 432.6499 | -22 |
| 7:14.07 | 13022 | S18 pano satırı DETOUR tik (tik) | `es-hover-tick.flac` | 434.0719 | -22 |
| 7:16.00 | 13080 | S18 pano satırı GIVING tik (tik) | `es-hover-tick.flac` | 436.0019 | -22 |
| 7:17.27 | 13118 | S18 kesme: kamyonun içi: 6 kutu, 4 kiremit dipte (kısa whoosh) | `es-whoosh-whip.flac` | 437.0696 | -27 |
| 7:21.35 | 13241 | S19 kesme: 4 kiremit kutu yapışık: tek parça ev maketi (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 440.9532 | -26 |
| 7:28.97 | 13469 | S19 çubuk dolar ~41% (yükselen tık) | `es-zip-up.flac` | 448.961 | -25 |
| 7:35.64 | 13669 | S19 kesme: Leo: you can't cut it in half (kısa whoosh) | `es-whoosh-tight.flac` | 455.4421 | -27 |
| 7:45.83 | 13975 | S19 SOLD kartı çakılır (tabela tok) | `es-knock-desk.flac` | 465.8206 | -19 |
| 7:48.89 | 14067 | S19 kesme: fatura kartları uçar (kısa whoosh) | `es-whoosh-whip.flac` | 468.6876 | -27 |
| 7:50.86 | 14126 | S19 fatura kartı AGENT (kâğıt) | `es-swipe-paper.flac` | 470.6666 | -24 |
| 7:52.08 | 14163 | S19 fatura kartı REPAIRS (kâğıt) | `es-swipe-paper.flac` | 471.8906 | -24 |
| 7:54.21 | 14226 | S19 fatura kartı PROPERTY (kâğıt) | `es-swipe-paper.flac` | 474.0166 | -24 |
| 8:01.57 | 14447 | S20 kesme: kiremit kutudan ince dilim: −A SLICE (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 481.1702 | -26 |
| 8:03.58 | 14507 | S20 dilim kesilir (maket bıçağı) | `bant-owlishmedia-stationery_27.flac` | 483.3194 | -19 |
| 8:09.30 | 14679 | S20 anahtar şıngırtısı (anahtar) | `kilit-rubberduck-lock_01.flac` | 489.2446 | -21 |
| 8:12.53 | 14776 | S20 bant 3 (koli bandı (incelmiş rulo)) | `bant-owlishmedia-stationery_08.flac` | 492.2397 | -16 |
| 8:13.93 | 14818 | S21 kesme: ürkütücü gişe TAX (gölgeli) (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 493.5352 | -26 |
| 8:14.13 | 14824 | S21 gök gürültüsü (gök gürültüsü) | `es-impact-deep.flac` | 494.1316 | -16 |
| 8:24.38 | 15131 | S21 eşik çizgisi iner: $15M PER PERSON (tok vuruş) | `es-knock-desk.flac` | 504.3676 | -19 |
| 8:26.88 | 15206 | S21 punch-in: eşik çizgisi (kısa whoosh / tık) | `es-whoosh-whip.flac` | 506.6766 | -25 |
| 8:33.44 | 15403 | S21 küçük çubuk ~$410K belirir (küçük tık) | `es-hover-tick.flac` | 513.4379 | -22 |
| 8:39.92 | 15598 | S21 aradaki boşluk oku: DOZENS OF TIMES HIGHER (yükselen whoosh) | `es-whoosh-yukselen.flac` | 518.9496 | -24 |
| 8:42.90 | 15687 | S21 punch-in: taban: medyan çubuğu (kısa whoosh / tık) | `es-whoosh-whip.flac` | 522.6976 | -25 |
| 8:47.64 | 15829 | S21 bariyer kalkar (bariyer + motor) | `es-toggle-latch.flac` | 527.6379 | -21 |
| 8:47.64 | 15829 | S21 bariyer kalkar (bariyer + motor) | `kamyon-ggbotnet-car_engine_start_up.flac` | 527.7418 | -25 |
| 8:53.26 | 15998 | S21 emeklilik kutusu: TAXED AS INCOME etiketi (etiket tap) | `es-tap-table.flac` | 533.2539 | -20 |
| 8:59.21 | 16176 | S21 kesme: not: some states have their own taxes (kısa whoosh) | `es-whoosh-tight.flac` | 539.0081 | -27 |
| 9:12.64 | 16579 | S21 UK kartı: £325,000 (pop) | `es-pop-0.flac` | 552.6398 | -21 |
| 9:15.82 | 16675 | S22 kesme: Leo: the surprise of this whole road (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 555.4272 | -26 |
| 9:17.99 | 16740 | S22 ekran yazısı: THE LOUD LEAK IS SMALL. (hafif pop) | `es-ui-pop-soft.flac` | 557.9793 | -25 |
| 9:23.27 | 16898 | S22 ekran yazısı: THE QUIET LEAKS ARE BIG. (hafif pop) | `es-ui-pop-soft.flac` | 563.2623 | -25 |
| 9:26.77 | 17003 | S22 LIVING altı çizilir (keçeli çizgi) | `kalem-owlishmedia-stationery_04.flac` | 566.1977 | -22 |
| 9:27.72 | 17032 | S22 CARE altı çizilir (keçeli çizgi) | `kalem-owlishmedia-stationery_04.flac` | 567.1457 | -22 |
| 9:28.72 | 17062 | S22 TIME altı çizilir (keçeli çizgi) | `kalem-owlishmedia-stationery_04.flac` | 568.1477 | -22 |
| 9:29.52 | 17086 | S22 kesme: Leo yakın: yorum sorusu (kısa whoosh) | `es-whoosh-whip.flac` | 569.3176 | -27 |
| 9:35.22 | 17257 | S22 ekran yazısı: WHICH LEAK DID YOU PICK? ↓ COMMENTS (hafif pop) | `es-ui-pop-soft.flac` | 575.2123 | -25 |
| 9:39.70 | 17391 | S23 kesme: gişenin arkasında dev yol saati (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 579.3062 | -26 |
| 9:44.10 | 17523 | S23 saat tik-tak başlar (saat tik) | `es-hover-tick.flac` | 584.0979 | -22 |
| 9:45.29 | 17559 | S24 kesme: Leo: boxes arrive late (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 584.8912 | -26 |
| 9:48.46 | 17654 | S24 saçlar griye döner (zaman atlaması) | `es-riser-build.flac` | 587.6184 | -25 |
| 9:53.84 | 17815 | S24 GEN X ~$14T (first 10 years) çubuğu (tık) | `es-click-soft.flac` | 593.838 | -21 |
| 10:02.18 | 18065 | S24 MILLENNIALS ~$46T (through 2048) çubuğu (yükselen tık) | `es-zip-up.flac` | 602.169 | -25 |
| 10:09.77 | 18293 | S24 kesme: Leo: middle of their lives (kısa whoosh) | `es-whoosh-tight.flac` | 609.5751 | -27 |
| 10:17.56 | 18527 | S24 banknot solar, sayaç $1.00 → $0.67 (inen ton) | `es-zip-down.flac` | 617.557 | -22 |
| 10:24.74 | 18742 | S24 kesme: iki yol işareti: STARTING OUT / LATER (kısa whoosh) | `es-whoosh-whip.flac` | 624.5376 | -27 |
| 10:35.99 | 19080 | S24 kesme: Leo yakın: same boxes, different job (kısa whoosh) | `es-whoosh-tight.flac` | 635.7881 | -27 |
| 10:39.23 | 19177 | S25 kamyon viraja girer (lastik + motor) | `kamyon-ggbotnet-car_engine_start_up.flac` | 639.1348 | -24 |
| 10:42.75 | 19283 | S26 kesme: kapılar açılır, Leo panoyu okur (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 642.3582 | -26 |
| 10:42.96 | 19289 | S26 kamyon kapıları açılır (metal kapı) | `kamyon-ggbotnet-car_trunk_open.flac` | 642.9028 | -18 |
| 10:47.28 | 19418 | S26 LOADED: 10 sütunu (tok) | `es-knock-desk.flac` | 647.2666 | -19 |
| 10:48.91 | 19467 | S26 şelale adımı 1 (inen tık) | `es-zip-down.flac` | 648.91 | -22 |
| 10:50.89 | 19527 | S26 şelale adımı 2 (inen tık) | `es-zip-down.flac` | 650.892 | -22 |
| 10:52.77 | 19583 | S26 şelale adımı 3 (tık (kayıp yok)) | `es-click-soft.flac` | 652.766 | -21 |
| 10:56.30 | 19689 | S26 şelale adımı 4 (inen tık) | `es-zip-down.flac` | 656.3 | -22 |
| 10:58.23 | 19747 | S26 şelale adımı 5 (inen tık) | `es-zip-down.flac` | 658.223 | -22 |
| 11:00.57 | 19817 | S26 şelale adımı 6 (tık (kayıp yok)) | `es-click-soft.flac` | 660.569 | -21 |
| 11:04.38 | 19932 | S26 INCOME TAX: −SLIVER (ince taralı dilim) (ince tık) | `es-hover-tick.flac` | 664.3829 | -22 |
| 11:07.66 | 20030 | S26 DELIVERED: 6 − SLICE − SLIVER, LATER (vuruş) | `es-impact-punch.flac` | 667.6626 | -19 |
| 11:12.84 | 20185 | S26 ikiye bölünür: ≈3 EACH (pop ×2) | `es-pop-0.flac` | 672.8398 | -21 |
| 11:12.84 | 20185 | S26 ikiye bölünür: ≈3 EACH (pop ×2) | `es-pop-0.flac` | 672.9898 | -21 |
| 11:17.58 | 20327 | S27 kesme: iki genç siluet kutuları içeri taşır (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 677.1792 | -26 |
| 11:24.77 | 20543 | S27 ekran yazısı: USED, NOT LOST (hafif pop) | `es-ui-pop-soft.flac` | 684.7633 | -25 |
| 11:28.98 | 20669 | S27 kesme: üç hayalet kamyon yan yana (kısa whoosh) | `es-whoosh-whip.flac` | 688.7756 | -27 |
| 11:31.62 | 20749 | S27 boş kasa → Okafor (6) → konvoy (pop ×3) | `es-pop-0.flac` | 691.6198 | -21 |
| 11:31.62 | 20749 | S27 boş kasa → Okafor (6) → konvoy (pop ×3) | `es-pop-0.flac` | 691.7698 | -21 |
| 11:31.62 | 20749 | S27 boş kasa → Okafor (6) → konvoy (pop ×3) | `es-pop-0.flac` | 691.9198 | -21 |
| 11:35.53 | 20866 | S27 punch-in: konvoy (kısa whoosh / tık) | `es-whoosh-whip.flac` | 695.3236 | -25 |
| 11:40.26 | 21008 | S27 punch-in: dolu konvoy (kısa whoosh / tık) | `es-whoosh-whip.flac` | 700.0576 | -25 |
| 11:46.92 | 21208 | S28 kesme: kamera Okafor evinden yükselir, haritaya (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 706.5202 | -26 |
| 11:49.96 | 21299 | S28 100 haneden 2'si turuncu (tık ×2) | `es-click-soft.flac` | 709.96 | -20 |
| 11:49.96 | 21299 | S28 100 haneden 2'si turuncu (tık ×2) | `es-click-soft.flac` | 710.16 | -20 |
| 11:58.64 | 21559 | S28 ayrı panel DFA: TOP 10% ≈ 69% (yükselen tık) | `es-zip-up.flac` | 718.637 | -25 |
| 12:05.77 | 21773 | S28 BOTTOM 50% ≈ 2% (küçük tık) | `es-hover-tick.flac` | 725.7689 | -22 |
| 12:08.05 | 21841 | S28 ekran yazısı: THE HEADLINE IS REAL. IT'S JUST LUMPY. (hafif pop) | `es-ui-pop-soft.flac` | 728.0383 | -25 |
| 12:24.38 | 22331 | S29 kesme: yol haritası (tek yol) (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 743.9812 | -26 |
| 12:33.59 | 22608 | S29 ekran yazısı: NOT A FORECAST. NOT A PLAN. A MAP. (hafif pop) | `es-ui-pop-soft.flac` | 753.5783 | -25 |
| 12:39.95 | 22798 | S30 kesme: Leo kamyon yanında: $124T (sahne geçişi (yumuşak whoosh)) | `es-whoosh-gecis.flac` | 759.5502 | -26 |
| 12:50.47 | 23114 | S30 kesme: Leo boş kutuyu bırakır, ince ruloyu omzuna atar (sol-orta) (kısa whoosh) | `es-whoosh-tight.flac` | 770.2661 | -27 |
| 12:52.40 | 23172 | S30 rulo omza (karakter anı) (kısa müzik vurgusu) | `es-mallet-glock.flac` | 772.3997 | -22 |
| 12:56.35 | 23290 | S31 kiremit kutu parlar (sıcak tını) | `es-mallet-celesta.flac` | 776.3439 | -22 |

## Sessiz bırakılan olaylar (86)

| t | tür | öneri | neden |
|---|---|---|---|
| 0 | kesme | whoosh | yerine 0.12 sn içindeki anlamlı olay |
| 12.991 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 14.86 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 24.019 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 26.225 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 37.06 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 45.212 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 48.838 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 59.14 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 65.466 | pop | boş | kural: ses yok |
| 79.265 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 92.909 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 94.74 | yazi | hafif pop | önceki SFX'e <0.12 sn |
| 102.276 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 105.696 | abone | klik (kurgu-editoru ortak bileşeni) | kural: ses yok |
| 113.96 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 132.132 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 140.649 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 141.38 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 142.68 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 153.659 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 158.214 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 164.227 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 177.97 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 190.103 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 197.221 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 204.446 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 208.376 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 226.46 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 240.899 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 276.62 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 285.405 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 290.464 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 296.827 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 298.974 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 304.52 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 305.82 | vurgu | yumuşak pad (vuruş yok) | kural: ses yok (müzik kesme / vuruşsuz) |
| 314.325 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 318.282 | pop | boş | kural: ses yok |
| 339.279 | yazi | hafif pop | önceki SFX'e <0.12 sn |
| 342.818 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 352.57 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 364.542 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 368.98 | pop | boş | kural: ses yok |
| 377.469 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 381.238 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 385.453 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 402.074 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 405.087 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 428.981 | abone | klik (kurgu-editoru ortak bileşeni) | kural: ses yok |
| 429.531 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 448.568 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 460.542 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 465.133 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 477.108 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 484.711 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 490.25 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 492.53 | yazi | hafif pop | önceki SFX'e <0.12 sn |
| 497.581 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 497.881 | vurgu | MÜZİK KES | kural: ses yok (müzik kesme / vuruşsuz) |
| 499.606 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 522.723 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 529.757 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 547.33 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 563.172 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 582.296 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 587.76 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 593.12 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 617.059 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 630.269 | pop | boş | kural: ses yok |
| 638.933 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 647.179 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 679.156 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 701.389 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 709.362 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 727.948 | kesme | whoosh | yerine 0.12 sn içindeki anlamlı olay |
| 730.981 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 736.684 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 747.451 | vurgu | boş | kural: ses yok |
| 751.03 | vurgu | boş | kural: ses yok |
| 753.288 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 764.32 | pop | boş | kural: ses yok |
| 765.544 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
| 773.049 | abone | klik (kurgu-editoru ortak bileşeni) | kural: ses yok |
| 773.599 | kesme | sahne geçişi (yumuşak whoosh) | whoosh aralığı <4.0 sn |
| 777.5 | kesme | kısa whoosh | whoosh aralığı <10.0 sn |
