# F7 kurgu raporu — 1929-1000-dolar

**Ajan:** kurgu-editoru · **Tarih:** 2026-10-27
**Kod:** `video/src/k1929/kurgu.tsx` (K1929Final, K1929Ilk30-A/B/C, K1929Shorts1/2), `kurgu-veri.ts` (`kurgu_ses.py shorts` üretir) · ses: `08-kurgu/kurgu_ses.py`
**Çıktılar (git dışı, sha256.txt):** `final-16x9.mp4` (234 MB) · `shorts-1.mp4` · `shorts-2.mp4` · git içi: `final.en.srt`, `*-onizleme.mp4`, `kareler/`, `varyant/`

## 0. Ofset — paket için
**Başa boşluk EKLENMEDİ; ofset 0,000 sn.** Final ses anlatim.wav ile 12 pencerede çapraz korelasyonla **0 ms** gecikmeli (`ses_kayma.py`). 09-paket/paket.md §4 bölüm zamanları ve SRT olduğu gibi geçerli; kaydırmaya gerek yok.

## 1. İlk 30 sn — 3 varyant → kazanan B
| Varyant | Ne | İlk görsel değişim | İlk 30 sn olay | Vaat ekranda | Sonuç |
|---|---|---|---|---|---|
| A | animasyon olduğu gibi | 0,5 sn (sert kesme 2,10) | 18 | 25,5 sn ("WHERE WAS MONEY SAFE IN 1929?"); 10,9–13,0 DISASTER?/GAMBLE?/SURPRISE? | elendi: başlıktaki soru ilk 15 sn'de yazılı değil |
| **B** | A + vaat şeridi "CAN YOU / KEEP IT?" 7,9–15,6 sn (başlık sorusu, köşe göstergesinin altında) | 0,5 / 2,10 | 18 | **7,9 sn** | **SEÇİLDİ** |
| C | B + 2 snap punch-in (8,0 sn ×1,07; 20,3 sn ×1,06) | 0,5 / 2,10 | 18 (dedektör farkı yok) | 7,9 sn | elendi: punch-in algılanmıyor kadar küçük, Leo'nun sağ kolunu ve köşe göstergesini kırpıyor; daha büyüğü 1080p kaynağı yumuşatır |
Kanıt: `varyant/ilk30-{A,B,C}-onizleme.mp4` (final miksli), `kareler/ilk30-varyant-A-B-C.jpg`. İlk renderda B şeridi "$1,000" göstergesine biniyordu → top 118→178 px düzeltildi (`kareler/final-9sn-vaat-seridi.png`).
Logo / kanal intro'su: yok. İlk kare = sepya "SEPT 1929" + anlatım (0,03 sn).

**Finalin ilk 30 sn olay/kesme listesi** (`kadans.py`, altyazı bandı hariç, sn): 0,5 · **2,0 (sert kesme 2,10)** · 4,0 · 5,25 · 6,25 · 8,0 · 10,5 · 13,0 · 14,0 · **15,5 (kesme S02)** · 17,5 · 18,5 · 19,5 · 24,5 · 25,5 · 26,75 · 28,25 · 29,75 → **18 olay, 2 sert kesme, en uzun aralık 5,0 sn**.

## 2. Tüm video kadansı
`kadans-final.json`: 242 olay, ortalama aralık 2,6 sn. Dedektörün >10 sn dediği 2 aralık (81,0–92,3 ve 93,5–112,0) elle kare kontrolüyle **yanlış alarm**: grafik çizgisi/etiket (86,4 · 90,9 · 92,4) ve sürekli şerit yağmuru altında yazı kartları (99,9 · 102,9 · 107,4 · 110,0) → gerçek aralık ≤6,5 sn (`kareler/kadans-81-109sn.jpg`). Sürekli hareket yükselen kenar üretmediği için dedektör muhafazakâr.
Yeniden kancalar (gerçek ses): ↺1 28,3 · ↺2 77,5 · ↺3 113,7 · ↺4 163,8 · ↺5 212,8 · ↺6 231,8 · ↺7 284,0 · ↺8 338,0 · ↺9 368,1 · ↺10 396,9 · ↺11 451,9 · ↺12 521,2 · ↺13 592,9 — hepsinde görsel olay + ses vurgusu var (5, 7, 8, 10, 13'ün sesi bu turda eklendi). En uzun kanca aralığı 71,7 sn (↺12→↺13) ≤90 ✓.

## 3. Ses — müzik stem olduğu gibi, SFX izi görsele yeniden hizalandı
F6 `sfx-stem.wav`'daki 53 vuruş kelime zamanına bağlıydı; F5 görsel olay listesiyle (`animasyon-efekt-cue.json`) + kare kontrolüyle (`kareler/ses-kontrol-1/2.jpg`) karşılaştırınca 20+ vuruş görselden 0,4–3 sn kayıktı (örn. S06 −13 % çubuğu ses 122,28 / görüntü 125,08; S17'de 3 kapıya kilit inerken sessiz, kilit sesleri 476–478'de haritanın üstünde; 488,2 sayaç sesi boş ekranda).
**Adaylar:** A) F6 stem'i olduğu gibi (elendi: görünür ses-görüntü kayması) · B) F6 stem + yalnız ek vuruş (elendi: kayık vuruşlar kalır) · **C) F6 dosya/kazançları korunup zaman görsel olaya taşınır + 40 ek vuruş (SEÇİLDİ)**. Plan: `sfx-kurgu-plan.json` (92 vuruş: F6'dan 52 — 30'u yeniden zamanlandı, 1'i atıldı (106,3 kapı sesi, ekranda kapı yok) — + 40 ek; hepsi assets/efekt ve 06-muzik/kaynak, lisans-kaydi.md'de kayıtlı). Ek vuruşlar −16…−24 dB (konuşma altı).

## 4. Test kapıları
| Kapı | Sonuç |
|---|---|
| ffprobe final | 1920x1080, 30 fps, H.264 + AAC 48 kHz, **631,63 sn (10:31,6)**, **18.949 kare** ✓ |
| 18.945/18.949 kare farkı | kök neden `render-parca.sh` son muxtaki `-shortest` (parçalar ve birleşik görüntü 18.949; ffmpeg tamponu son 4 kareyi kesiyordu) → `-t <görüntü süresi>` ile düzeltildi, test: 18.949 ✓ |
| Loudness (ebur128, son dosya) | final **−14,0 LUFS, TP −2,2 dBTP, LRA 2,0** · Shorts 1 −14,0 / −3,4 · Shorts 2 −14,0 / −3,6 ✓ |
| blackdetect (d 0,1, pix 0,10) | final 0 · Shorts 0 / 0 ✓ |
| freezedetect (2 sn, n 0,003) | final 0 · Shorts 1 0 · Shorts 2 0 (ilk render'da köprü kuyruğunda 53,6 sn donma → yavaş itme eklendi) ✓ |
| WER (render sesi, small.en, tools/ses/hata-orani.py) | final **%0,87 (15/1726)** vs anlatım-tek %0,93 (16) → fark −0,06 puan ✓ · Shorts 1 %0,8 (1/127) · Shorts 2 %0,0 (0/136) — kilitli Shorts metnine göre |
| Altyazı hizası | final ses ↔ anlatim.wav gecikme 0 ms (12 pencere, kor. 0,986–0,996) + akustik hiza (tools/ses/hiza-dogrula.py) baş p95 **7 ms**, son p95 15 ms ✓ ±150. Shorts: Whisper kelime başı − beklenen medyan −6 / +3 ms. Bilgi: ham Whisper'la doğrudan kıyas p95 448 ms çıkar — Whisper cümle başı kelimesini önceki sessizliğe yayıyor (örn. "Quick" 268,44 vs akustik 269,38), kapı için kullanılmadı |
| SRT (`srt_kontrol.py`) | `final.en.srt` = 04-ses taslağı, değişiklik gerekmedi: 228 blok, biçim hatası 0, çakışma 0, satır ≤42, ≤2 satır, süre 0,7–7 sn, metin = referans (yazım farkı 0). Bilgi: 16 blok 21–24 karakter/sn (TTS hızı; konuşmaya bağlı) |
| Rastgele 10 kare (tohum 1929) | `kareler/rastgele-10.jpg`: 17,4 / 18,4 / 154,8 / 209,3 / 360,7 / 393,9 / 417,3 / 484,7 / 496,9 / 526,0 — Leo tutarlı, yazı kesilmesi yok, "Illustration" etiketleri sepya plakalarda var, altyazı okunur ✓ |
| Shorts süre / format | Shorts 1 **49,57 sn**, Shorts 2 **56,03 sn** (≤60 ✓), 1080x1920, 30 fps |
| Shorts güvenli alan | eklediğim katmanlar: Illustration etiketi (40, 205), niteleyici şerit y 1210–1310 x 60–920, köprü kartı x 70–882, y 1130–1330 (üst 192, alt 1536, sağ 918 sınırları içinde) ✓ |

## 5. Shorts — 4 aday → 2
İlk 2 sn testi: (a) ilk kelimeler bağlam olmadan bir bahis/çelişki söylüyor mu, (b) ilk karede okunur metin + karakter, (c) kesit kendi içinde kapanıyor mu, (d) 9:16 varlık hazır mı (0–2 puan).
| Aday | İlk 2 sn | a | b | c | d | Top. |
|---|---|---|---|---|---|---|
| **S1 "Pick a door"** (hook ek kaydı) | "In 1929, the smartest-looking door…" + yazı + Leo + 3 kapı | 2 | 2 | 2 | 2 | **8 ✓** |
| **S2 "Same box, opposite result"** (hook ek kaydı) | "A shoebox of cash gained power in 1932…" + yazı | 2 | 2 | 2 | 2 | **8 ✓** |
| S3 banka kuyruğu (S09 212,8–) | "Here's the problem…" — önceki sahneye muhtaç | 0 | 1 | 2 | 0 | 3 ✗ |
| S4 kilitler (S17–S18) | "But the game isn't over…" — bağlam ister | 0 | 2 | 1 | 0 | 3 ✗ |

**Shorts 1** (49,57 sn): hook (Sh1Ek 0–3,96; 1,40 sn'de snap punch-in ×1,05 → ilk görsel değişim 1,5 sn) → S01 2,10–8,03 → S06 145,45–149,30 ("NOV 1929" ✓, bulanık C16 plakasında "Illustration" etiketi eklendi) → S10 230,12–240,35 → S16 419,77–438,65 (**"IN A DECADE OF FALLING PRICES" şeridi BOX satırıyla 434,31'de** kurgu katmanında; özgün şerit "decade." 441,0'da, kesit dışındaydı) → kapanış (Sh1Ek 4,30–9,62) "The brown door won because prices were falling. Why that flips today is in the full video." + köprü kartı "WHY IT FLIPS TODAY / Full game: $1,000 in 1929 ↓" (son 3,9 sn).
**Shorts 2** (56,03 sn): hook (Sh2Ek 0–6,66) → S12 301,45–316,30 → S20 528,13–543,95 ("12 MONTHS TO SEPT 2026 / 2025 → 2026" kartı "Twelve" ile birlikte girer) → **atlama kesmesi** S20 546,94–548,45 ("They just buy less", banknot görseli üstünde; "Nothing was stolen…" çıkarıldı) → S21 565,17–579,75 → sessiz köprü kuyruğu 2,6 sn "WHO WON 1929? / Full game: $1,000 in 1929 ↓".
Sahne başları altyazı öbeği başına oturtuldu (ilk render'da S20 başında önceki cümlenin "TWENTY-FIVE." kelimesi 2 kare görünüyordu). Ses: Shorts müzik stem'i kesite kırpıldı, son 2 sn sönüş; efektler ana videodaki dosya/kazançla (buzzer −15, skor zili −18, mühür −12, sayaçlar −21, kapı pop −20).

## 6. Riskler / başka ajanlara notlar
1. **animasyon-yonetmeni:** S18 488,0–489,2 sn arası boş lacivert ekran (yazı gelmeden önce ~1 sn); kara kare değil, blackdetect geçer ama ölü an. Dikey sahnelerde `Kaynak` etiketi alt-sağ köşede (Shorts arayüzünün altında kalır) — kaynaklar açıklamada.
2. Shorts 1 S10 kesitinin ilk ~4 sn'si yalnız "DOOR 2: THE SCORE" başlığı (grafik 18 sn'de gelir) — en zayıf an; bir sonraki dikey sahnede grafik daha erken girmeli.
3. Altyazı 16 blokta >21 karakter/sn (TTS temposu); bölmek zamanı değiştirmez, YouTube CC için kabul.
4. Shorts'ta anlatım kesitleri ana videonun aynası olduğundan "reused" değil ama 2 Shorts'un ikisinde de Leo hook'u aynı stüdyo kadrajında; 3. Shorts'ta farklı açılış kadrajı önerilir.
