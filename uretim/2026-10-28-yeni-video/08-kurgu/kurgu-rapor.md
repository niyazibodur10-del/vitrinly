# F7 kurgu raporu — 2026-10-28-yeni-video (S08 Kitchen Table Budget)

**İLERLEME: tamam** · büyük medya git dışı → `yeniden-uret.adimlar` F7 satırları (miks → yataklar → render-parca / render-son).
**SONUÇ: GEÇTİ.** final 16:9 11:18,2 · −14,0 LUFS / TP −3,3 · siyah/donma 0 · ses kayması 0 ms · abone 4 (klik 0 kare) · SFX kayık 0 · Shorts 57,4 + 41,9 sn.
| Kapı | Sonuç |
|---|---|
| ffprobe final (`403ee6df0af2`) | 1920x1080, 30 fps, H.264 + AAC 48 kHz stereo, 678,20 sn (≥10 dk ✓) |
| ebur128 (son dosya) | final I −14,0 LUFS, TP −3,3 dBTP, LRA 2,0 · sh1 −14,0 / −3,2 · sh2 −13,9 / −3,6 (`log/final-ebur128.txt`, `log/shorts-olcum.txt`) |
| blackdetect + freezedetect (d=2) | final 0 · sh1 0 · sh2 0 |
| Senkron | `ses_kayma.py final-16x9.mp4 anlatim.wav` 12 pencere → maks 0,0 ms (dudak senkronu F5 kapısı aynı eksende geçerli) |
| Altyazı | SRT 240 blok: biçim 0, yazım farkı 0, uzun satır 0; maks 21,8 kr/sn (sınır 25); hiza: akustik p95 5 ms (ses-muhendisi) × kayma 0 ms → ±150 ✓. Whisper WER final %1,3 · sh1 %2,1 · sh2 %0,9 |
| Abone | uzun 4: 175,53 / 305,07 / 449,60 / 662,60 sn; Shorts her biri 1, sonda; klik ses ↔ görsel tık 0,00 kare (6/6) |
| SFX hizası | 183 olay, ilk vuruş görsel olaya ≤0,5 kare + stem ±2 kare dışı 0 → **kayık vuruş 0** (muzik-ses-tasarimcisi'ne iade yok) |
| İlk 30 sn | ilk görsel değişim 0,5 sn (Capitol küçülür) / sert kesme 1,9 sn · 10 olay · vaat ekranda 9,4 sn · logo/intro yok |

## 1. Açılış — 3 varyant → kazanan B
| Varyant | Ne | İlk değişim | İlk 30 sn olay | Vaat yazılı | Karar |
|---|---|---|---|---|---|
| A | animasyon olduğu gibi | 0,5 / kesme 1,9 | 11 | yok (yalnız buzdolabında −$2,000/MO notu 8,5 sn) | elendi: videonun sözü ilk 15 sn'de yazılı değil |
| **B** | A + vaat şeridi "WHERE DOES THE −$2,000 A MONTH GO?" 9,4–13,06 (pencere üstü sol; −$2,000 notu yandıktan, "see where the gap goes" ile) | 0,5 / 1,9 | 10* | **9,4 sn** | **SEÇİLDİ** |
| C | B + başlık yankısı "IF AMERICA EARNED $5,400 A MONTH…" 0,2–1,9 (Capitol planı sağ üst) | 0,5 / 1,9 | 10* | 0,2 + 9,4 | elendi: ilk 2 sn'de anlatım ("Shrink the U.S. government…") ile ikinci bir metin yarışıyor; telefonda küçük; başlığı zaten tıklayan izleyiciye tekrar |
*Dedektör 0,75 sn birleştirme kuralı yüzünden 9,25/10,25'i tek sayıyor; kesme sayısı üçünde aynı. Kanıt: `varyant/ilk30-{A,B,C}-onizleme.mp4` (final miksli), `kareler/ilk30-varyant-A-B-C.jpg`, tam çözünürlük `kareler/final-11sn-vaat.png`.
Final ilk 30 sn olay listesi (`kadans-final.json`): 0,5 · 2,25 · 6,75 · 9,25 · 13,0 · 14,25 · 16,0 · 18,75 · 21,75 · 23,25 (+ 24,18/24,84/26,64 not pop'ları, F5 cue) — en uzun aralık 6,75 sn.

## 2. Kadans ve yeniden kancalar
`kadans-final.json`: 210 olay, ort. 3,23 sn. >10 sn denen 2 aralık elle kontrol: **100,75–112,0** S05 G1 grafiği gerçekten ~10 sn durağandı → kurgu vurgusu eklendi (106,62 "Three envelopes" üç çubuk üstüne köşeli parantez + "3 ENVELOPES"; 109,10 "$3,765 SPENT" sarı çerçeve; yeni rakam yok) → en uzun ≈5 sn. **341,5–356,25** S14 sürekli kayan "CHEAP 1%" şeridi + 344/346/349/351/355'te etiketler → yanlış alarm (`kareler/kadans-341-356sn.jpg`).
Retention haritası 14 kanca (`olcum-kanca.txt`): 12'sinde F5 görsel olayı + SFX var. ↺11 (387,8) vurgusu 386,32 FAMILY çatlağı + plate impact. **↺14 (524,7 "time is what the three possibilities are about") olaysızdı** → kurgu şeridi "TIME = A · B · C" 524,62–527,85 (`kareler/final-526sn-kanca14.jpg`). En uzun kanca aralığı 56,7 sn.

## 3. Ses
Miks = anlatim.wav + muzik-stem (ducking dahil, olduğu gibi) + sfx-stem (olduğu gibi) + 4 abone kliği (`kurgu_ses.py ana`); −14 LUFS render-parca'da. SFX yeniden zamanlanmadı; `kurgu_ses.py dogrula` → `olcum-ses-hiza.txt`. Klik maskeleme (`klik_maske.py`) 4/4 GEÇTİ (RMS artışı 0,00 dB). Shorts yatakları: shorts müzik stem'i (kesit boyu, 1,5 sn sönüş) + ana sfx-stem'in aynı zaman dilimleri (dikey sahneler aynı zaman.ts planı → aynı olay karesi) + klik + köprüde whoosh.

## 4. Abone ol (Niyazi 2026-10-28)
| # | Kare / sn | Taraf | Bağlam | Neden uygun |
|---|---|---|---|---|
| 1 | 5266 / 175,53 | sağ | S07 sonu nefes → S08 "Let's open the loan statement" | ≥60 sn; defter kartı solda |
| 2 | 9152 / 305,07 | **sol** | S12 matruşka doruğu sonrası nefes → S13 | S13'te kırmızı INTEREST zarfı sağ altta → kart sola alındı (`kareler/abone-aday-kontakt.jpg`) |
| 4 (ek) | 13488 / 449,60 | sağ, üst 640 | S18 "Which one is better is an argument for voters…" | tarafsızlık notu; doruk/açıklama değil; S19 doruğundan (454,87) 1,8 sn önce biter; 305→662 arası 6 dk boşluğu böler |
| 3 | 19878 / 662,60 | sol | S26 sonu nefes → S27 köprü | sağda kupa |
Kanıt: `kareler/abone-final-kontakt.jpg`, `kareler/abone-klik-kare38-39.jpg` (kare +38 SUBSCRIBE, +39 SUBSCRIBED; ses başı +39 → 0,00 kare). Shorts: sh1 kare 1541 (52,67 tık), sh2 kare 1107 (38,20 tık), ikisi de köprü kartından önce biter (`kareler/shorts-abone-klik-38-39.jpg`).

## 5. Shorts — 5 aday → 2 (ilk 2 sn testi)
| Aday | İlk 2 sn | Sonuç |
|---|---|---|
| **sh1** ek hook + S06 + S12 + ek kapanış | "If the U.S. were a family earning…" + 0,1 sn başlık yazısı, 1,0 sn "$5,400 / MO IN", 1,2 sn zarf | **GEÇTİ** (rakam + çerçeve 1 sn içinde) |
| **sh2** ek hook + S19 + S16 + S17 + S19 + ek | "In 1946, U.S. debt was bigger…" + 0,1 sn grafik, 0,3 sn ">100% (1946)" | **GEÇTİ** (şaşırtıcı iddia + veri) |
| S12 soğuk açılış | "Envelope five. Interest." bağlamsız | elendi |
| S01 kırpma | güçlü ama dikey kompozisyon yok (16:9 kırpma) + sh1 ile aynı öncül | elendi |
| S13 "why so fat, so fast?" | önceki bağlama muhtaç, dikey yok | elendi |
sh1 57,37 sn (atlanan: "Ships, planes…", "No picture.", "Here's why."); sh2 41,92 sn. Kesit başları altyazı öbeği başında, sonları sonraki öbekten önce. Köprü: sh1 sesli cümle "The whole kitchen table is in the long video." + kart "ALL FIVE ENVELOPES ↓"; sh2 kart "WHERE IT STANDS TODAY ↓" (son 2,4 sn, ek görüntüsü sürer). İlk render'da köprü okunun altyazıya bindiği görüldü → kart y 960, ok ≤1300 (yeniden render). Konuşma bütünlüğü: Whisper eklemeleri ("borrowed", "People", "How?" kaybı) çapraz ilintiyle yanlış alarm (kor ≥0,977, kayma ≤14 ms).
Kontakt: `kareler/shorts-1-kontakt.jpg`, `kareler/shorts-2-kontakt.jpg` (ilk render; düzeltme yalnız köprü kartı konumu).

## 6. Rastgele 10 kare
Tohum 10: 387,84 · 292,36 · 392,32 · 143,09 · 549,93 · 556,80 · 442,83 · 112,35 · 353,85 · 224,61 → kusur yok (`kareler/final-rastgele-10.jpg`).

## 7. Notlar / riskler
- `dikey.tsx` DEk sh2: 6 cümle 5 kesmeye eşleniyor ("How?" ayrı cümle) → "It borrows…" ve "never retires" ek cümlelerinde yazılar bir kayık. Kurguda bu iki ek cümle kullanılmadı (yerine S16/S17); "How?" anında "1 · OWN MONEY" görünüyor (cevap önizlemesi gibi, kabul). animasyon-yonetmeni'ne not.
- SRT: taslağın 22 bloğunun bitişi sonraki boşluğa uzatıldı (`srt_uzat.py`; başlangıçlar akustik, değişmedi). `srt_kontrol.py` ham-Whisper hiza p95 369 ms verir — bilinen sahte fark (cümle başı), kapı akustik hizadır.
- Final pix_fmt yuvj420p (1929 ile aynı hat).
- Paket: `09-paket` `08-kurgu/final.en.srt` bekliyor ✓; bölüm zamanları kaymadı (ofset 0).

Yeniden üretim: `tools/yeniden-uret.sh 2026-10-28-yeni-video` (F7 satırları). Parça render: değişen 7/12 parça (ilk tur 6, düzeltme turu 1).
