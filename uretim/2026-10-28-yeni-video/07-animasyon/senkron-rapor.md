# F5 animasyon — S08 Kitchen Table Budget (KButce) · animasyon-yonetmeni
**İLERLEME: tamam** · büyük medya (git dışı): `tam-16x9.mp4`, `test-10sn.mp4`, `dikey/*.mp4` → `yeniden-uret.adimlar` F5 satırları.
**Karar:** Kritik yol GEÇTİ. Tüm sahneler kelime çapalı tek kaynak `video/src/videolar/yeni-video/zaman.ts`; SFX/abone cue ve ağız aralıkları aynı fonksiyonlardan (`olay-cikar.mjs`).
**Kapılar (kritik yol, `test-10sn.mp4` 22,9 sn = S01 tamamı + S12 başı/matruşka açılışı):**
- Senkron (ağız görünür aralıklar, 700–3000 Hz): `python3 tools/senkron-testi.py test-10sn.mp4 log/kritik-agiz.json 30 --araliklar 2.25-6.73,9.32-13.06,13.07-22.90 --bant 700-3000` → en iyi 1 kare, GEÇTİ. 9,32–13,06 aralığı tek başına −4 (3,7 sn, kesme başı); 8,3–13,06 → 2 kare, S01 tam sahne → 1 kare (kısa pencere yanılgısı, hafıza kuralı).
- blackdetect (d 0.1, pix_th 0.10) + freezedetect (−60 dB, 1 sn) → 0 olay.
- AgizTest: `kareler/KButceAgizTest-00000.jpg` (poz a) + `KButceAgizTestG05-00000.jpg` (G05k zarf pozu) → 9 şekil iki pozda dikişsiz.
- Efekt cue: `06-muzik/animasyon-efekt-cue.json` 253 olay (kesme 93, pop 77, vurgu 42, sayaç 12, düşme 9, kayma 8, abone 3 …), `tahmini: false`; abone S07@175,55 s (k5266) · S12@305,08 s (k9152) · S26@662,61 s (k19878).

## Yöntem
- Ses: `04-ses/anlatim.wav` (am_fenrir 0.9, 11:18,2), `kelimeler-hizali.json` (metin yazımlı kelimeler), Rhubarb PocketSphinx + `--dialogFile`, tam sahne + sessizlik kapısı (`tools/animasyon/rhubarb-toplu.py`, 29 iş 135 sn).
- Veri: `tools/animasyon/sahne-veri.py` (girdi `07-animasyon/ses-girdi/`: altyazı öbekleri `altyazi-obek.py`, renk `renk.json`) → `veri-sahne.ts`. Grafik rakamları `grafik-veri.py` → `veri-grafik.ts` (rakam-tablosu R01–R35 + OMB T7.1; elle rakam yok; R33 1946/1974 assert).
- Ses gelmeden iskelet (akış 0b): `tahmini-veri.py` (ham TTS cümle zamanı) → tüm çapalar sesten önce doğrulandı; gerçek ses gelince kod değişmeden bağlandı.
- Rig: 1929 bel üstü kesikler + yamalar aynı kırpım kutusunda (200,23,1517x1057); **G05 zarftan-zarf** pozu rig'e eklendi (kafa a ile hizalı) ve `g05-boya.py` ile iki renk varyantı (G05k: dış faiz kırmızı/iç BORROWED mor; G05m: tersi) → matruşka konuşma sürerken.
- Leo masada (G01): ölçek 0,58 ortada (lamba altında), y<810 maskeli; masa nesneleri altyazı bandının (y>930) dışında.
- G08 RED → B planı: G07 hesap makinesi KOD katmanı (ekranda KOD rakam, S05). G04 RED → açılış G05 + KOD zarf.

## Adaylar ve eleme
- Matruşka (S12, kilit an): (A) Leo G05 boyalı varyantlar + punch-in (konuşma sürer) · (B) kuşbakışı KOD zarf zinciri (punch-in kademeli) · (C) image-to-video — ücretli/onaysız, ELENDİ. **Seçilen: A+B birlikte** (A ile açılış/ters renk konuşan yakın plan, B ile 4 kademeli "içinde içinde" kulesi); dikeyde B kule yukarı yükselir.
- Leo masa yerleşimi: ölçek 0,82 sol üçte bir (buzdolabı boş kalır, lamba çakışması yok ama Leo kenarda) vs 0,58 orta (lamba altında, masa önü nesnelere yer) → 0,58 orta seçildi; yakın plan kamera ile (×1,48).
- Zarf renklendirme: CSS `mix-blend-mode: color` + maske (KOD) vs ayrı renkli Canva üretimi (hak harcar) → KOD seçildi (tek kesik, 7 renk).
- Palet: zarf renkleri senaryo sabiti (mavi/yeşil/açık yeşil/gri/kırmızı/mor/kraft); dataviz validator açık yeşil↔yeşil normal görüş ΔE 9–12 (KALDI) → her zarf/dilim doğrudan etiketli (ikincil kodlama); sıralı çubukta yalnız faiz renkli, diğerleri nötr.
- Ağız seti: 1929 rig yamaları (karakterin kendi ağızları, AgizTest'te dikişsiz) tek aday — Kurallar (1929 geçti).

## Tam video ve dikey — GEÇTİ
- `tam-16x9.mp4` 678,2 sn, sha256 380b3ba073b0 (`tools/render-parca.sh KButceTam`, 12 parça, 3873 sn).
- Senkron: `senkron-testi.py tam-16x9.mp4 rhubarb/tum-kapili.json 30 --araliklar <agiz-gorunur 40 aralık, 236,5 sn> --bant 700-3000` → en iyi 1 kare GEÇTİ (`log/senkron-tam.txt`; tek sapma S01 9,32–13,06 −4 = kısa pencere, yukarıda).
- Siyah/donma (blackdetect d0.1 + freezedetect −60 dB 1 sn): tur 1 → 19 donma (1,0–1,23 sn, kamera son anahtar kareden sonra duran kartlar) → Kamera/GrafikZemin/DZemin'e %0,35/sn sürekli itme → tur 2 **0** (`log/siyah-donma-tam.txt`).
- Kadans (`1929 08-kurgu/kadans.py`): 210 olay, ort. 3,23 sn; tur 1'deki 5 boşluk >10 sn → 9 çapalı olayla 2'ye indi: S05 grafik (100,8 sn, 11,3 sn: dilimler büyüyor) ve S14 konveyör (341,5 sn, 14,8 sn: sürekli akan şeritler; ölçer sürekli hareketi olay saymaz). İkisinde de ekran dolu (grafik/konveyör + Leo yok ama içerik hareketli); yalnız arka plan + altyazı kalan an yok (her kesme içerikli, kontakt sayfaları).
- Abone (cue, gerçek ses): S07 175,547 sn k5266 · S12 305,082 sn k9152 · S26 662,614 sn k19878 (koordinatör notundaki 175,581/305,081/662,426 tahmini veriden; S26 +0,19 sn).
- Dikey: `KButceD-S06/S12/S16/S17/S19`, `KButceD-Sh1Ek/Sh2Ek` (kurgu-editoru keser; her kesmede grafik/nesne ≤1 sn, kontakt `kareler/dikey-S12-kontakt.jpg`). Render + kapı: D-S12 34,2 sn, Sh1Ek 12,1, Sh2Ek 15,0 → siyah/donma 0 (`log/dikey-kapi.txt`, tur 1'de 2 donma → DZemin itmesi); ek senkron Sh1 1 kare, Sh2 1 kare (kor. 0,67). S06/S16/S17/S19 dikey yalnız kare örneğiyle denetlendi (render kurgu kesitiyle).

## Sonraki ajanlara
- kurgu-editoru: abone bileşeni alanı sağ alt boş (S07/S12/S26 sonları); sahne kompozisyonları `KButce-Sxx`, tam `KButceTam`; S16 "LIKE IF…" sessiz etkileşim yazısı sol altta (y 720), abone ile çakışmaz.
- muzik-ses-tasarimcisi: cue dosyası gerçek ses ekseninde; S06 "five" anında müzik kesilir (olay `kay`).
