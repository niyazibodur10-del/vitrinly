# F7 kurgu raporu — 2026-11-04-miras-sizintilari (S03 The Great Wealth Transfer Has a Leak)

**İLERLEME: tamam (kurgu)** · büyük medya git dışı → `yeniden-uret.adimlar` F7 satırları.
**SONUÇ (tur 3, 2026-11-10): GEÇTİ.** RIG etiketi kaldırıldı (554d69c), final + 2 Shorts yeniden render, kapılar yeniden ölçüldü (§6). Aşağıdaki tur 1 notu tarihsel:
**Tur 1 SONUÇ: RED (tek madde, animasyon kaynaklı).** Kurgu kapılarının hepsi geçti; ancak animasyonda `rig.ts` `YER_TUTUCU_RIG = true` her Leo planına kırmızı hata ayıklama etiketi basıyor ("RIG: S08 Leo kesiği…", `sahneler.tsx:69`). Final ve iki Shorts'ta görünüyor → yayınlanamaz. Düzeltme animasyon-yonetmeni'nde; sonra `render-parca.sh` yalnız Leo içeren parçaları, `render-son.sh` Shorts'u yeniden üretir (kurgu kodu değişmez).
| Kapı | Sonuç |
|---|---|
| ffprobe final (`e08e065ef7af`) | 1920x1080, 30 fps, H.264 + AAC 48 kHz stereo, 781,40 sn (≥10 dk) |
| ebur128 (son dosya) | final −14,0 LUFS / TP −3,2 / LRA 2,0 · sh1 −14,0 / −3,7 · sh2 −14,0 / −3,8 |
| Siyah/donma | final 0 · sh1 0 · sh2 0 |
| Senkron | `ses_kayma.py` 12 pencere → 0,0 ms (anlatim.wav ekseni; dudak senkronu F5 kapısı geçerli) |
| SRT | 296 blok, biçim 0, yazım farkı 0, maks 21,0 kr/sn (20 blok bitişi uzatıldı, `srt_uzat.py`); hiza = akustik × kayma 0 ms |
| WER (small.en) | final %1,2 · sh1 %1,0 (Cerulli→"cerule") · sh2 %2,7 ("Taxes." silmesi; ses var, kor 0,983) |
| Abone | uzun 4: tık 105,77 / 429,03 / 579,20 / 773,10 sn; Shorts sonda 1'er (tık 38,03 / 40,03); klik ↔ görsel tık 6/6'da 0,00 kare |
| SFX | 168 olay, kayık vuruş 0 (`olcum-ses-hiza.txt`) |
| İlk 30 sn | ilk görsel değişim 2,0 sn, 9 olay, vaat 6,9 sn ("HAS A LEAK. HOW BIG?"), logo/intro yok |

## 1. Açılış — 3 varyant → B
Kaynak animasyonda kamyon 0–9,45 sn tek plan; dedektör ilk olayı 4,25 sn'de buldu (sınır ≤3). A: olduğu gibi → elendi (4,25 sn). **B: sağ üst şerit "THE GREAT WEALTH TRANSFER" 2,0 sn + "HAS A LEAK. HOW BIG?" 6,9 sn → ilk değişim 2,0, 9 olay — SEÇİLDİ.** C: B + 0–9,45 yavaş itme → elendi (kamyonun kendi büyümesinin üstüne binip 4,25'teki olayı yuttu, 8 olay). Kanıt `log/ilk30-varyant.txt`, `varyant/ilk30-*-onizleme.mp4`, `kareler/ilk30-varyant-A-B-C.jpg`.

## 2. Kadans — S21 boşluğu (507–520)
Ekranda yalnız vergi başlığı vardı. Kurgu vurgusu (yeni rakam yok): 506,95 "A TYPICAL FAMILY ↓" etiketi → 509,3–512,3 zeminden vergi çizgisine uzayan ölçü oku → 512,3 "THE TAX LINE" → (513,44 animasyon medyan etiketi) → 515,0 medyan çubuğuna halka → 519,92 animasyonun "DOZENS OF TIMES HIGHER" okuyla biter. Elle en uzun aralık ~3 sn (`kareler/kadans-s21-507-520.jpg`; dedektör sürekli büyüyen oku ve alt banttaki halkayı saymadığı için 12,75 sn diyor). Etiket ilk render'da iki satırlı altyazıya biniyordu → y 680 (tek parça yeniden render). Aynı vurgu Shorts 2'nin S21 kesitinde dikey yerleşimle var. Tüm video: 225 olay, ort. 3,47 sn.

## 3. Abone ve klik (hakem notu: kısık)
Kazanç −17 → −12 dB (+5). Konuşmanın üstünde earshot "mouse click" yine bulamadı (z +1,0 → +1,2; maskeleniyor). Bu yüzden 3 cue anında kart 1,2–1,3 sn erkene alındı: tık her birinde 0,73 sn'lik nefese düşüyor. Nefeste earshot z −0,6 → +1,6, en yakın etiket "scroll wheel tick"; RMS +0,6…+4,2 dB. klik_maske'nin "KALDI"sı RMS ≤1 dB kuralı: konuşma yok, maskelenen anlatım yok.
4. nokta: S23 geçişi (tık 579,20 "taxes." / "Which" arası; S24 doruğu ve "It's a clock" 584,1'den önce biter), 429→773 arasındaki 344 sn'lik boşluğu böler. Taraf: 1–3 sağ (cue: sağ alt boş), 4 sol. ABONE-3'te kart sağdaki kamyonun gövdesine biniyor; Leo solda olduğu için kabul edildi. Kanıt `kareler/final-rastgele-abone.jpg` (son 4 kare = tık karesi).

## 4. Shorts — 5 aday → 2 (ilk 2 sn testi)
| Aday | İlk 2 sn | Karar |
|---|---|---|
| **sh1** ek tam okuma (S01·S13·S14 özeti) → "So how many boxes are left when the truck finally reaches the kids?" | $124T kutusu 0 sn + ×1,06 snap 1,5 sn (ilk olay 1,5) | GEÇTİ — 41,45 sn |
| **sh2** ek kanca → S21 "Taxes… the Fed found" (496,55–519,70) → ek kapanış "Then where does the money really go…?" | TAX tabelası + 1,45 sn "THE SCARIEST LEAK?" pop (ilk render'da snap algılanmadı, ilk olay 4,75 → 1,5) | GEÇTİ — 43,43 sn |
| D-S01 soğuk açılış | ilk olay 8,25 sn | elendi |
| S22 "Which leak did you think was the biggest?" | bağlamsız açılış | elendi |
| S14 "How many boxes did we lose? Zero." | cevabı Short'un içinde veriyor (köprü zayıf) + sh1 ile aynı öncül | elendi |
İkisi de cevabı yalnız uzun videoda olan bir soruyla bitiyor (teşhis a4). Kuyruk 4,8 sn sessiz ve altyazısız (yavaş itme): abone 0,1–2,7 sn (y 1330, "BIGGEST LEAK = ?" altında) → köprü kartı "THE ANSWER IS IN THE FULL VIDEO / The Great Wealth Transfer Has a Leak ↓" (y 1220–1490, güvenli alan). sh2'de sabit politika satırı "US FEDERAL ONLY · STATE & OTHER COUNTRIES DIFFER" (metin §5 Z2) bütün kesitte var. Kontakt: `kareler/shorts-{1,2}-kontakt.jpg`.

## 5. Notlar
- RED: yukarıdaki RIG etiketi (animasyon-yonetmeni). Shorts kaynağındaki ek kayıtlarda da var.
- Dikey S21'de animasyonun "MEDIAN NET WORTH" etiketi altyazı bandına biniyor (513–519); animasyon-yonetmeni'ne not.
- Disk: oturum ortasında kök bölüm %100 doldu (eski Remotion paketleri); koordinatör temizledi, iş sonunda 6,3 GB boş.
- Rastgele 10 kare (tohum 11) RIG etiketi dışında kusursuz (`log/rastgele-10-kare.txt`).

## 6. Tur 3 (2026-11-10) — RIG düzeltmesi sonrası
- Render: KMirasFinal render-parca 13/14 parça (Leo her bölümde) + başlık düzeltmesi 2/14; Shorts render-son. sha: `sha256.txt`.
- Kapılar (`log/kapi-tur3.txt`): final 781,40 sn, −14,0 LUFS / TP −3,2, siyah/donma 0, kayma 0,0 ms · sh1 41,45 sn −14,0/−3,7 · sh2 43,43 sn −14,0/−3,8 · WER final %1,2 · sh1 %1,0 · sh2 %2,7 · abone 4+1+1, tık ↔ klik 0,00 kare (`kareler/abone-klik-kare38-39.jpg`: +38 SUBSCRIBE, +39 SUBSCRIBED).
- 30 rastgele kare (tohum 30; final 20 + 2 başlık karesi, Shorts 10): `kareler/kontrol-final-20-rastgele.jpg`, `kareler/kontrol-shorts-10-rastgele.jpg` → hata ayıklama / yer tutucu yazı 0. Kod taraması `RIG:|YER_TUTUCU|DEBUG|PLACEHOLDER` (miras-sizintilari + ortak) = 0.
- **G4 başlığı kesikti (politika raporu, 508–513):** neden animasyonun S21'deki iki ×1,08 punch-in'i, başlık çizginin üstündeydi (y 30–160). Düzeltme `grafik.tsx` G4: yalnız 16:9 ve eyalet olmayan planda başlık çizginin altına (`taban − H + 22`); dikey/eyalet aynı. Kurgu etiketim "THE TAX LINE" y 330'a indi. Yalnız 8. parça (+ izin kararsız saydığı 11.) yeniden render; 509,5/510,2/510,8/511,5 karelerinde başlık tam.
- Shorts 2 politika şeridi S21 kesitinde punch-in'li başlığa biniyordu → bölüme göre konum (ek planları y 196, S21 y 400 kırmızı çizginin altı); alt konum altyazıya binince reddedildi (`kareler/shorts-2-politika-seridi.jpg`). İlk olay 1,5 sn korunuyor.
