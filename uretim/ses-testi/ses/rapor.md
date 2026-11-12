# Ses testi v1 — rapor (2026-10-26)

Ham: `assets/ses-ham/ses-testi-v1.m4a` (iPhone Sesli Notlar, AAC 48 kHz mono, 76.4 sn).
Temiz: `temiz-v1.m4a` (çalışma kopyası `temiz-v1.wav`, git dışı). Zincir: `tools/ses-temizle.sh`.
Önce/sonra örneği: `once-sonra.m4a` (ilk ~11 sn ham, 1 sn sessizlik, aynı bölüm temiz).

## Ölçümler (ffmpeg ebur128 + astats)
| | Ham | Temiz | Hedef |
|---|---|---|---|
| Ortalama ses yüksekliği | −15.3 LUFS | −14.1 LUFS | −14 ±1 ✅ |
| Tepe | +0.7 dBFS (kırpma riski) | −1.0 dBFS | ≤ −1 ✅ |
| Gürültü tabanı | −37.0 dB | −58.3 dB | belirgin uğultu yok ✅ (−21 dB iyileşme) |
| Dinamik aralık (LRA) | 3.9 LU | 3.5 LU | — |

## Anlaşılırlık (Whisper medium.en, metne göre kelime hata oranı)
- Ham: **%11.7** (14/120) · Temiz: **%10.0** (12/120) → temizlik anlaşılırlığı bozmadı, hafif iyileştirdi.
- Karşılaştırma: aynı okumanın telefon dikte metni %2.5 (farklı tanıyıcı, kıyas için).
- Hatalar (temiz): Financial→"finance our" (kanal adı!), crashes→"crushes", scenarios→"scams", charts→"cards",
  complicated→"companies", truth→"threat", here→"where". "wheelbarrows" iki kez okunmuş (ikincisi tekrar; kurgu kesecek).

## Değerlendirme
Teknik kalite hedefleri geçti. Anlaşılırlık kabul edilebilir ama geliştirilebilir: hataların çoğu 5 ses üzerinde
toplanıyor — /æ/ (crash, Financial), /θ/ (truth), "ch" (charts), vurgulu hece (scenarios, complicated).
Çözüm metin tarafında da var: senaryo-yazari bu kelimeleri az kullanır veya kolay eşanlamlısını seçer;
kanal adı her videoda geçeceği için "Financial Rise" telaffuzu ayrıca çalışılmalı.

## v2 — düzeltme kaydıyla birleştirme (2026-10-26)
Düzeltme: `assets/ses-ham/ses-testi-v1-duzeltme.m4a` (58.9 sn). R1 üç kez, R2–R4 birer kez okunmuş.
Okumaların ayrı ayrı Whisper sonucu:
- R1 "Welcome to Financial Rise": 3 okumanın 3'ü doğru (güven 0.69 → 0.98 → 0.997). **3. okuma kullanıldı.**
- R2: crashes→"gracious", bold→"balls", scenarios→"rose" → eskisinden kötü, **eski kayıt korundu.**
- R3: charts ve complicated düzeldi ama "No" düşmüş, jargon→"kargan" → toplamda kazanç yok, **eski kayıt korundu.**
- R4 "Just the truth…": "truth" doğru (güven 0.96) → **kullanıldı** (yavaş okunmuş; tempo farkı dinlenip karar verilecek).

Birleştirme: sessiz noktalardan (−50 dB altı enerji) kesildi, 12 ms fade, sonra tek loudnorm geçişi.
Çıktı: `birlesik-v2.m4a` (79.7 sn) · −13.9 LUFS · tepe −1.0 dBFS.

Hata oranı (Whisper medium.en): v1 %10.0 → birleştirilmiş varyant ilk ölçümde %8.3, son dosyada %10.0.
Whisper aynı sese ±2 kelime oynuyor; bu yüzden tek sayıya değil tekrar eden hatalara bakılmalı:
- **Kalıcı düzeldi:** "Financial Rise" (artık her ölçümde doğru).
- **Kararsız:** "truth" (bir ölçümde doğru, bir ölçümde "root").
- **Hâlâ hatalı:** crashes, bold, scenarios, charts, complicated.
- Ölçüm hatası sayılabilir: "worth less"→"worthless" (aynı ses), "wheelbarrows" (yavaş okunduğu için iki kelimeye bölünüyor).

Sonuç: kanal adı sorunu çözüldü. Kalan 5 kelime için senaryo tarafında kolay eşanlamlı kullanılacak
(crashes→"market crashes" yerine "collapses"? test edilecek, charts→"graphs", complicated→"confusing", scenarios→"possibilities").
