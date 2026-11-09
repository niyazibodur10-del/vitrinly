# F5 — senkron ve sahne raporu · animasyon-yonetmeni (S03 miras, metin v1.1, ses 13:01)

İLERLEME: tamam. **SONUÇ: GEÇTİ** — tam 16:9 (`tam-16x9.mp4` 781,4 sn, sha256 f6ea0a2589cc) + 9:16 (7 dosya `dikey/`).
- Tam: siyah+donma 0 (`log/siyah-donma-tam.txt`) · senkron 40 aralık 179 sn → 1 kare GEÇTİ (`log/senkron-tam.txt`; 3 kısa aralık ±3 = <2,6 sn pencere) · kadans 217 olay, ort. 3,6 sn, >10 sn boşluk 1 (S21 G4 507–520 sn, iki punch-in arası; `log/kadans-tam.txt`).
- 9:16: D-Sh1 36,7 / D-Sh2 20,0 / D-S01/S13/S14/S21/S22 — siyah+donma 0, ilk görsel olay ≤4 sn (S01 8,25 sn: kamyon itmesi sürekli, kadans eşiği altı), Shorts senkron 1 kare GEÇTİ ×2 (`log/dikey-kapi.txt`).
- Efekt cue son hâl: `06-muzik/animasyon-efekt-cue.json` tahmini=false, 254 olay (124 kesme, 7 punch-in, 3 abone).
- ABONE (gerçek ses): 1) k3171 = 1:45,70 (S05 sonu) · 2) k12869 = 7:08,98 (S17 sonu) · 3) k23191 = 12:53,05 (S30 sonu); 16:9 sağ alt 3,5 sn boş.
**Kapılar (kritik yol, `test-10sn.mp4` 27,4 sn = S01 tamamı + S12 bant gag'i "okay"+1,6 sn):**
- Senkron (ağız görünür 3 aralık, 7,7 sn, 700–3000 Hz): `python3 tools/senkron-testi.py test-10sn.mp4 log/kritik-agiz.json 30 --araliklar 12.99-14.86,16.47-20.60,25.65-27.35 --bant 700-3000` → en iyi 2 kare, korelasyon 0,52 → GEÇTİ (sınırda; `log/senkron-kritik.txt`). Tüm kesit: 2 kare GEÇTİ.
- blackdetect (d=0.1, pic_th=0.98) = 0 · freezedetect (−60 dB, 1 sn) = 0 (test-10sn).
- AgizTest karesi: `kareler/KMirasAgizTest-00000.jpg` (9 şekil, S08 Leo rig'i = Canva'daki aynı Leo).
- Abone (gerçek ses): ABONE-1 k3171 (1:45,70, S05 sonu) · ABONE-2 k12869 (7:08,98, S17 sonu) · ABONE-3 k23191 (12:53,05, S30 sonu). 3,5 sn boyunca 16:9 sağ alt (x 1192–1864, y 682–810) boş: `kareler/kontak-abone.jpg` (6 kare, kırmızı kutu = alan).
- Efekt cue: `06-muzik/animasyon-efekt-cue.json` `tahmini: false`, 246 olay (124 kesme, 3 abone), zaman.ts sha256 → `node 07-animasyon/olay-cikar.mjs`.
- ≤1 sn giriş: 123 kesme +0,9 sn kontağı (`kareler/kontak-giris-1..4.jpg`) — her grafik başlık/çerçeveyle kesmede girer; yalnız-zemin karesi yok.

## Ne yapıldı (iskelet → gerçek)
- Ses: `tools/animasyon/rhubarb-toplu.py` (31 sahne + 2 ek, PocketSphinx + dialogFile, 189 sn; ek metinlerinden telaffuz bağlantıları ayıklandı `rhubarb/ek/`) → `07-animasyon/altyazi-obek.py` (557 öbek, `renk.json` anahtar kelimeler) → `tools/animasyon/sahne-veri.py` → `veri-sahne.ts`. Çapalar metin v1.1'e göre güncellendi (S08, S13, S21, S26).
- Metin v1.1 görsel farkları: S08 ekran "ONE COUNTRY-WIDE TOTAL ≠ ONE FAMILY'S BOXES" (D-1) · G2 kaynak "2022" · "ESTATE RECOVERY (AGE 55+)" · S21 yeni kart "ESTATE TAX ≠ THE ONLY TAX" (R28, rakamsız) · S22 pano "ESTATE TAX −0 · INCOME TAX: A SLIVER" · S26 şelale TAX sütunu ESTATE 0 + INCOME TAX sliver → "6 − SLICE − SLIVER". `grafik-veri.py` R28 kaynak satırı (23 kaynak, assert GEÇTİ).
- Görseller: M08 (yol) ve M09 (kasa içi) plaka; gorsel-varlik-sanatcisi kesikleri (M01 arka-açık/yan kamyon, M05 bant, M04/M07) `ham-kesik.py` ile public/kmiras'a (gerçek kesik varsa o, yoksa geçici renk anahtarı). Kutu kayıp sırası sahne-listesi.md ile hizalandı (CARE ve GIVING yeşil → S18'de 4 kiremit + 2 lacivert).
- S12 bant gag'i: M05 kesiğinin el+kutu kısmı (yüz kadraj dışı → anlatım sürerken hareketsiz ağız görünmez) + iki köşeden damla + 2. bant; konuşan anlar rig.

## Elenen
- Kritik testte M04/M05 Leo'yu tam kadraj konuşturmak: kesiklerde ağız yaması hizası yok → konuşma anları S08 rig'iyle (aynı karakter, kafa hizalı a pozu); Canva Leo yalnız ağzı görünmeyen aksiyon kadrajında.
- Kritik testi 20 sn'ye kırpmak için S12'yi "I tape it"ten başlatmak: gag'in kurulumu (soft bottom) kaybolur; 27,4 sn kabul edildi.

## Açık / sonraki ajana not
- Senkron 2 kare (S08'de 1) — tam render ölçümünde tekrar bakılır; 3'e çıkarsa Rhubarb çizelgesine −1 kare ofset adayı test edilir.
- Plaka gelmeyen kesmeler "YER TUTUCU" etiketli M08/M09 plakası (harita, ev içi, okul, gişe sahnesi M11–M18 dalga 1b/2). Kesme kadansı: S26 (30 sn şelale), S21 (23 sn), S11 (20 sn) — plakalar gelince ek kesme.
- 9:16: `KMirasD-Sh1` (36,6 sn) / `KMirasD-Sh2` (20,0 sn) ek kayıtlar + dikey S01/S13/S14/S21/S22; Shorts ABONE (sonda, alt orta 1150–1304) alanı son cümlede (soruKutu) boş.
