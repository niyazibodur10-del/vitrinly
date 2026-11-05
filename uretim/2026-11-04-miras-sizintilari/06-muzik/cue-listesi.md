# Cue listesi — 2026-11-04-miras-sizintilari S03 (F6a müzik; SFX bölümü F6b'de dolar)

Kaynak: `06-muzik/cue.json` (`cue-uret.py` ← `animasyon-efekt-cue.json` tahmini=false + `04-ses/sahne-zamanlari.json`). Zaman ekseni = `04-ses/anlatim.wav` (781.388 sn). Kare = 30 fps.
Stem'ler: `stems/muzik-stem.wav`, `stems/sfx-stem.wav` (48 kHz stereo 24-bit, anlatımla örnek örnek aynı uzunluk, 0 noktası = anlatımın 0'ı). Montajda anlatım kaydırılırsa iki stem de aynı kadar kaydırılır.
Abone klik sesi stem'de YOK: `assets/efekt/ozgun-fare-klik.flac`'ı kurgu-editoru AboneOl bileşeniyle görsel tıklamaya ±2 kare yerleştirir (olaylar: ).

## Müzik bölümleri

| # | Bölüm | Giriş → çıkış | Kare | Parça (lisans) | Ruh hali / tempo | Konuşma altı | Giriş/çıkış sönüşü |
|---|---|---|---|---|---|---|---|
| 1 | B1 yola çıkış (Bölüm 1: The Number on the Truck) | 0:00.00 → 1:46.25 | 0–3187 | Wasteland Caravan — vitalezzz (CC0) | merak + yola çıkış, akustik/elektro gitar · ≈171 BPM ölçüm, yarım tempo hissi [tahmin] | −22 dB | 0.4 / 1.2 sn · ofset 203.0 |
| 2 | B2 Okafor ailesi (Bölüm 2) | 1:46.25 → 2:35.21 | 3187–4656 | Sunny Side Up — Pro Sensory (CC0) | sıcak aile, hafif caz-pop · ≈84 BPM [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 85.0 |
| 3 | B3 yaşam ve bakım (Bölüm 3) | 2:35.21 → 4:58.97 | 4656–8969 | Insistent — yd (CC0) | ciddi, seyrek, karanlık-sessiz · sabit yatak [tahmin] | −19 dB | 1.2 / 1.2 sn · ofset 23.0 |
| 4 | B4 sapma ve bağış (Bölüm 4) | 4:58.97 → 7:09.53 | 8969–12886 | Remember this shadow — Komiku (CC0) | yol değiştiren, meraklı · ≈86 BPM [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 49.0 |
| 5 | B5 en ağır kutu: ev (Bölüm 5) | 7:09.53 → 8:13.93 | 12886–14818 | The road we use to travel when we were kids — Komiku (CC0) | nostalji, ev, sıcak · ≈87 BPM [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 88.0 |
| 6 | B6 vergi durağı (Bölüm 6) | 8:13.93 → 10:42.75 | 14818–19283 | Lone Scavenger — vitalezzz (CC0) | hafif gerilim, gitar · ≈171 BPM ölçüm [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 136.0 |
| 7 | B7 varış + envanter (Bölüm 7) | 10:42.75 → 12:39.95 | 19283–22798 | Wasteland Caravan — vitalezzz (CC0) | varış, açılışa dönüş (kitap ayracı) · ≈171 BPM ölçüm [tahmin] | −22 dB | 1.2 / 1.2 sn · ofset 60.0 |
| 8 | B8 tez + köprü (S30–S31) | 12:39.95 → 13:01.39 | 22798–23442 | Joy Ride — Pro Sensory (CC0) | sıcak kapanış · ≈90 BPM [tahmin] | −22 dB | 1.2 / 2.0 sn · ofset 45.0 |

Notlar: bölüm sınırları sahne kesmelerinde (`04-ses/sahne-zamanlari.json`), geçişler 1.2 sn eşit güçte. B7 = B1 parçasının başka kesiti (yola çıkış ↔ varış). Ofset = parçada başlangıç saniyesi (en sabit 40 sn pencere). Konuşma boşluğu ≥0.9 sn olunca müzik +6 dB açılır.

## Shorts müzik yatakları (60 sn, sonda 2 sn sönüş; kurgu kesit uzunluğuna kırpar)

- `stems/shorts-1-muzik-stem.wav` ← `$M/remember-this-shadow-komiku.mp3` (konuşma altı −20 dB, mobil)
- `stems/shorts-2-muzik-stem.wav` ← `$M/lone-scavenger-vitalezzz.mp3` (konuşma altı −20 dB, mobil)

## SFX vuruşları (0 vuruş, 0 görsel olay; hizalama: geçiş whoosh'unda tepe, diğerlerinde ses başlangıcı olay karesinde)

| Olay zamanı | Kare | Olay | Dosya | Dosya başı (sn) | Kazanç dB |
|---|---|---|---|---|---|

## Sessiz bırakılan olaylar (0)

| t | tür | öneri | neden |
|---|---|---|---|
