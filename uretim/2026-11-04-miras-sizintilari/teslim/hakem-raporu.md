# F9 Hakem raporu — S03 "The Great Wealth Transfer Has a Leak" + 2 Shorts · 2026-11-10

**KARAR: KALDI (yalnız Shorts-2).** Uzun video ve Shorts-1'deki her kapıyı kendim ölçtüm, hepsi GEÇTİ; bu iki dosyaya dokunulmayacak. Shorts-2'nin dikey vergi grafiğinde ölçülen 2 yerleşim hatası var (aşağıda RED-1). Shorts-2'nin yalnız yeniden render edilmesi gerekiyor.
**Slot:** uzun Çar 11-11 17:00 UTC korunuyor, Shorts-2 Cmt 11-14 14:00 UTC (3,5 gün pay). Düzeltmeden sonra hakemde yalnız fark kontrolü yapılacak: Sh2 sha256, ebur128, 21–26 sn ve 7–12 sn kontaktları, abone/klik.
**Gerekçe:**
1. **Uzun + Sh1 teknik kapıları kurgu raporuyla birebir.** Final sha256 2ceb894f2bb5 (kurgu kaydıyla aynı), 781,40 sn, −14,0 LUFS / TP −3,2, siyah 0, donma 0. Senkron 1 kare. SRT 296 blok, sorun 0, hiza 0 ms. Abone 4/1/1, klik 0 kare. SFX 12/12 ±2 kare. `politika-f8 --video final` → hata 0 (doğrulanmış tekrar %0,0). 40 rastgele kare + OCR: hata ayıklama ya da yer tutucu yazı 0.
2. **Shorts-2 kapıdan kaldı (kare kontrolü, ölçüm).** (a) 21,0–25,5 sn: sarı kesikli vergi çizgisi "MEDIAN NET WORTH, AGES 65–74: ~$410K" etiketinin ortasından geçiyor ("~$4¦0K"). Şort'un ana rakamı 4,5 sn boyunca okunmuyor. 16:9'da aynı grafik doğru: etiket çizginin solunda. (b) 7,5–11,5 sn: başlığın 2. satırı "PERSON (2026)" politika şeridinin ("US FEDERAL ONLY · STATE & OTHER COUNTRIES DIFFER") altında kalıyor, iki metin üst üste biniyor. Kanıt: `09-paket/hakem-log/sh2-410k.jpg`, `sh2-410k-seri.jpg`, `sh2-7-11sn.jpg`, `sh2-grafik-ust.jpg`.
3. **Başlık (T1) yeterli, yanıltıcı değil** (koordinatörün sorusu, gerekçe §Başlık).

## RED-1 düzeltme listesi (Shorts-2; render yalnız Sh2)
| # | Sahip | Ne | Kabul ölçütü |
|---|---|---|---|
| R1 | animasyon-yonetmeni (`grafik.tsx` G4 dikey) | Medyan etiketi dikeyde çizgiyle çakışmasın: etiketi çizginin soluna/altına al veya 2 satıra böl ("MEDIAN NET WORTH, 65–74" / "~$410K") | 21–26 sn kontaktında "~$410K"nın hiçbir pikseli çizginin üstünde değil, 168 px genişlikte okunuyor |
| R2 | kurgu-editoru (Sh2 politika şeridi) | 7,5–11,5 sn planında şerit başlığın altına insin (S21 için yaptığın konum kuralı bu plana uygulanmamış) ya da başlık tek satıra sığsın | 7–12 sn kontaktında şerit ile başlık arasında ≥8 px boşluk; altyazıya binmiyor |
| R3 | kurgu-editoru | Sh2'yi yeniden render et, `sha256.txt` + `kapi` satırlarını güncelle (LUFS, abone 1, klik 0 kare, WER) | Sh2 −14 ±1 LUFS, abone 1 sonda, kare kontrolü temiz |

## Kapı tablosu (her satır benim ölçümüm; log `09-paket/hakem-log/`)
| Kapı | Komut → sonuç | Log |
|---|---|---|
| Bütünlük | sha256 final 2ceb894f2bb5 · sh1 e7f7bd2cfa55 · sh2 a60d40f882af · srt a6518aa9bf44 = `08-kurgu/sha256.txt`; teslim/ mp4'ler sembolik bağ | — |
| Süre / format | ffprobe 1920x1080 / 1080x1920 ×2, 30 fps, H.264 + AAC 48 kHz st · 781,40 / 41,45 / 43,43 sn (≥10 dk ✓, Shorts ≤60 ✓) | ffprobe.txt |
| Ses | ebur128: final −14,0 LUFS / TP −3,2 · sh1 −14,0 / −3,7 · sh2 −14,0 / −3,8 | ses-siyah.txt |
| Siyah / donma | blackdetect d0,5: 0/0/0 · freezedetect d2: final 0, sh2 0, **sh1 1** (34,23–36,23 sn, tam 2,0 sn). "BIGGEST LEAK = ?" kartı sabit, altyazı değişiyor → boşluk değil, risk notu (kurgu "0" yazmış: eşik sınırı) | olcum-*.txt, sh1-donma-34sn.jpg |
| Dudak senkronu | `senkron-testi.py final tum-kapili.json 30 --araliklar <40 aralık, 179,1 sn> --bant 700-3000` → 1 kare GEÇTİ (40 aralığın 3'ü ±3, hepsi ≤2,5 sn pencere) | senkron-final.txt |
| Altyazı | 296 blok: biçim/çakışma 0, ≤2 satır, maks 42 kr, maks 21,0 kr/sn · kilitli metinde olmayan kelime 0 (2.238 kelime) · hiza 296/296, maks 0 ms | srt-tarama.txt |
| WER (örneklem, sha aynı) | 2 rastgele 60 sn pencere (tohum 20261110: 125,35 / 215,40), 314 kelime: ham 26 farkın 23'ü rakam yazımı → gerçek ~3 (%1,0); kurgu %1,2; benim↔kurgu fark 3 kelime | wer-orneklem.txt |
| Rastgele kare (hata ayıklama / yer tutucu) | 40 kare (final 30 + Sh1 5 + Sh2 5, tohum 1110) + tesseract OCR: RIG/DEBUG/TODO/PLACEHOLDER/undefined/NaN/{} 0. Kod taraması `RIG:\|YER_TUTUCU\|DEBUG\|PLACEHOLDER` 0. **Sh2'de 2 yerleşim hatası** (RED-1) | ocr-rastgele.txt, rastgele-final-30.jpg, rastgele-shorts-10.jpg |
| İlk 30 sn | 0,1 sn kamyon kapısı açılır ($124T), 2,0 sn "THE GREAT WEALTH TRANSFER" şeridi, ilk sert kesme 10,4 sn · intro/logo yok · vaat ilk 15 sn'de | ilk3sn.jpg, ilk30-sahne.txt |
| Abone (sayı) | Düğme kutusu kırmızı→gri: uzun **4** (104,8 · 428,0 · 578,0 · 772,0; ilki ≥60 sn) · sh1 **1** (37–39 / 41,45, sonda) · sh2 **1** (39–41 / 43,43, sonda) | abone-say.txt |
| Abone (klik) | Final ↔ kurgu klikli miks 0,0 ms; klik başı görsel tıkta −0,10…+0,10 kare (4/4), kazanç −12,2 dBFS (S08'de −17'ydi, hakem notu uygulandı) · Shorts yatakta şablon +0,05 kare, yatak↔final 0,0 ms (2/2) | klik-hiza.txt |
| SFX hizası (earshot) | `earshot timeline` 2 rastgele 30 sn pencere (180,3 / 266,73), cue = yerleştirilmiş SFX (cue.json): 12 vuruşun 11'inde onset ≤63 ms (≤2 kare); 272,68 whoosh "tepe" hizalı (onset −102 ms = yükseliş başı) → stem çapraz ilinti: tepe 272,680 = kesme → 0 kare. **12/12 ±2**. İlk koşudaki 6 NO HIT, `atlanan` listesindeki SFX'siz kesmelerdi (whoosh aralığı <10 sn kuralı) | es-sfx-*.txt, whoosh-272.txt, es-*.txt |
| Thumbnail | K1/K3/K4 1280x720, 110–113 KB · 168x94'te üçü de okunur · ≤4 kelime · K1 "$124T" = Cerulli tahmini (video 0:00) | thumb-168x94-x2.png |
| Paket | `paket-kontrol.py --final` (a310f30 sonrası) → 96 OK, 0 hata, exit 0 · `yukle.py --dry-run` 3/3 0 hata (09-paket + teslim/). Uyarı ×2: `ilgili_video` alanı API'de yok → Studio adımı (YAYIN.md'de var) · uç ekran 775,4–781,4 (6 sn), ABONE-4 kartı 775,3'te bitiyor (kare 23154+105) → çakışma yok | paket-kontrol-final.txt, dry-run*.txt |
| YPP politika (video) | `politika-f8.py --video 08-kurgu/final-16x9.mp4` → SONUC hata=0 · AI beyanı 3/3, `sentetik_medya` true · vaat↔anlatım hepsi VAR · lisans 45, kayıtsız/NC/ND/SA 0 · tekrar dHash üst sınır %25,2 → 2. aşama doğrulanmış %0,0 · dış klip 0 · G4 başlık kesiği (politika notu) finalde düzelmiş: 508–513 sn başlık çizginin altında, kadraj içinde (`g4-508-513.jpg`, `final-410k.jpg`) | politika-f8-final.txt |

## Başlık (T1 "The Great Wealth Transfer Has a Leak"): yeterli, yanıltıcı değil
- **Doğru:** SRT'de "great wealth transfer" 0 kez geçiyor. Anlatım konuyu "Cerulli … one hundred twenty-four trillion" diye kuruyor (124 ×3, Cerulli ×6, inheritance ×5, baby boomers ×2).
- **Neden yanıltıcı değil:** (1) "Great Wealth Transfer", Cerulli'nin 124 T$ / 2048 tahmininin yaygın adı. Video bu tahmini 0:00'da kamyondaki $124T kutusuyla açıyor. (2) Terim ekranda var: 2,0–9,45 sn "THE GREAT WEALTH TRANSFER" şeridi (`kurgu.tsx:41`), hook'un tam üstünde. Shorts köprü kartı da tam başlığı yazıyor. (3) Açıklamanın ilk cümlesi tanımı veriyor: "The great wealth transfer, explained: Cerulli estimates $124 trillion…". (4) "Has a Leak" vaadi karşılanıyor: "leak" anlatımda 13 kez geçiyor, yapı 6 duraklık sızıntı listesi ("To see the real leaks…", "the leaks that matter are the quiet ones"). Videonun ters köşesi (eş = "relay, not a leak") vaadi çürütmüyor, inceltiyor. `politika-f8` [3] T1 VAR.
- **Kalan risk (RED değil):** Terim sesli söylenmediği için otomatik altyazı ve arama dökümünde yok. Bir sonraki videoda başlık kavramı ilk 30 sn'de bir kez sesli geçsin (senaryo-yazari; ortak ders).

## Riskler
1. **Leo'nun panosu boş.** 40 rastgele karenin ~8'inde Leo boş beyaz bir pano tutuyor. Plan "6 durak satırı KOD" idi (`05-gorsel/canva-promptlari.md` M04/M09), kodda bu katman yok, liste ayrı tam ekran Pano grafiğinde gösteriliyor. Yazı içermediği için kapı ihlali değil, ama bitmemiş görünebilir. Sonraki videoda animasyon-yonetmeni plan sapmasını raporda yazsın.
2. Sh1 34,2–36,2 sn: 2,0 sn sabit soru kartı, değişen tek şey altyazı. Shorts temposunda en uzun durağan an bu.
3. Senkronda 3 kısa pencere ±3 kare (2–2,5 sn, Rhubarb kısa pencere yanılgısı). Toplam 1 kare.

## Seçenekler
(a) **KALDI, yalnız Sh2 düzeltilir.** Seçildi: kapı ölçümle kaldı ve ana rakam okunmuyor. Düzeltme yalnız Sh2'yi etkiliyor, uzun video slotu korunuyor. (b) ONAY + şart. Reddedildi: hata dosyanın içinde, Studio adımıyla kapatılamaz.
