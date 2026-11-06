# F8a — Thumbnail raporu · S03 · başlık T1 "The Great Wealth Transfer Has a Leak"

İLERLEME: tamam (3 finalist, kapıların hepsi geçti). Yeniden üretim: `THUMB_TMP=<geçici> python3 -I thumb-uret.py` → `cp adaylar/{K1,K3,K4}.jpg` finalist adlarına → `python3 -I thumb-test.py <repo-dışı rakip klasörü> K1 K3 K4`.
**Karar:** Test & Compare sırası **1) K1 · 2) K4 · 3) K3**. Varsayılan (ilk yüklenen) K1: hakem H8 konsepti, paket.md'deki T1 zinciri ("sızıntı var → kime kalıyor?") ve hook H1b'nin sonu ("So what really reaches the kids?") ile aynı vaat.
**Kapılar [Ö]:** 1280x720 JPEG ✅ · ≤2 MB (108–111 KB) ✅ · ≤4 kelime ✅ · 168x94 bölge OCR'ında metnin tamamı okundu ✅ · p5 ≥4,5 ✅ (min 4,66) · süre damgası alanında metin 0 px ✅ · iki koşu aynı (`diff test/uret-1.txt test/uret-2.txt`) ✅.
**Kaynak:** Leo = gorsel-varlik-sanatcisi'nin kafa değişimli kesikleri (`05-gorsel/thumb-leo/`). Yeni Canva üretimi 0, sıfırdan Leo prompt'u yok. Zemin, banknot, bant şeridi, kutu etiketi, pano çizgileri ve metin kodla.
**youtube-paketleyici için:** `paket.md` → `<!-- veri:thumbnail-ana -->` bloğuna `../09-paket/thumbnail/K1-who-gets-it.jpg` yazılır. Test & Compare'in diğer iki dosyası `K4-keeps-leaking.jpg` ve `K3-smaller-later.jpg`; yüklemeden sonra Studio'dan elle eklenir.
Etiketler: **[Ö]** betik ölçümü · **[T]** yargı.

## Finalistler
| Sıra | Dosya (sha256 ilk 12) | Açı | Metin | Kaynak |
|---|---|---|---|---|
| 1 | `K1-who-gets-it.jpg` (5256b742022b) | duygu + soru | **WHO / GETS / IT?** (sarı, lacivert kontur) + kutu etiketinde **$124T** | `thumb-leo/K1-M06-saskin.png` (M06 kiremit kutu + d-saskin kafa), ×0,80. Kod: koyu camgöbeği zemin + sıcak ışık, kutu köşesinden sola dökülen 4 banknot, kraft etiket |
| 2 | `K4-keeps-leaking.jpg` (6bf2d245ba41) | mizah / eylem (bant gag'i) | **IT KEEPS** + **LEAKING** (lacivert levha) | `thumb-leo/K4-M05-saskin.png` (M05 bant + yeşil kutu), ×0,68. Kod: tuğla-mercan zemin, sağ köşede çapraz eski bant, sol köşede yarık ve dökülen banknotlar |
| 3 | `K3-smaller-later.jpg` (5509f04fce40) | karşıtlık | **SMALLER.** (lacivert, beyaz kontur) + **LATER.** (kırmızı levha) | `thumb-leo/K3b-M04-notr.png` (M04 pano + a kafası), ×0,74 + `nesne/M02-kiremit.png` (büyük) + `nesne/M02-kiremit-yarik.png` (küçük, bantlı). Panoda 6 durak çizgisi, kayıplı 3'ü kırmızı çizik |

**Elenen:** K4b (`K4b-M05-gulumser`): 168x94'te gülümseme nötr okunuyor, "sızıntı" duygusunu taşımıyor; metin ve kapılar K4 ile aynı [T]. K2 kamyon: varlık üretilemedi (koordinatör kararı). Metin alternatiflerinin elemesi F4 maketinde yapıldı (`konseptler.md` §3).
**Başlıkla okunuş (T1) [T]:** K1 başlığın açtığı soruyu kişiye bağlıyor (sızıntı → kime?). K4 başlığı tekrar etmeden sızıntının sürdüğünü gösteriyor; "leak" kelimesi ikisinde de var ama biri olay, öteki süreklilik. K3 sonucu veriyor (daha küçük, daha geç), başlık nedenini soruyor. T3 başlık seçilirse K1 çift soru olur, o zaman sıra K4 · K3 · K1.
**Doğruluk / politika:** $124T = Cerulli tahmini, 2048'e kadar [D, paket.md]; etikette atıf yok, "Bank of America" yazmıyor (H8). K3'teki kutu oranı `03-metin/veri/kutu-hesap.py`'den: 10 kutu yükleniyor, 6 kutu teslim ediliyor. Alan oranı 0,6, kenar oranı √0,6 = 0,7746 (290 → 225 px); abartı yok. "LATER." eş durağının bir gecikme olduğunu söylüyor, kayıp değil (D2). Banknotlar genel çizim: yazı, portre, gerçek para deseni yok. Gerçek kişi, logo, ev veya FOR SALE tabelası yok (H7, rakip klişesi). Leo kurgusal; şapka ve ceket yok (Fred/Marcus ayrışması).

## Test kapısı [Ö]
`python3 -I thumb-uret.py` (sha256 betik 86e171bc6861, iki koşu aynı) · `python3 -I thumb-test.py <rakip> K1 K3 K4` (thumb-test v3 8a6c43edfc74: v2 + kelime kutusu başına psm 7). Çıktılar: `test/uret-1.txt`, `test/test-cikti.txt`, `test/olcum-adaylar.json`, `test/ocr-168x94-finalist.json`, `test/rakip-benzerlik.json`, `test/mobil-168x94-finalist.png`.

| Ölçüt | K1 | K4 | K3 | Eşik |
|---|---|---|---|---|
| Dosya | 108 KB | 109 KB | 111 KB | ≤2 MB |
| Kelime | 4 (3 + $124T) | 3 | 2 | ≤4 |
| 168x94 büyük harf (min) | 15,4 px | 16,9 px | 13,5 px | ≥9 |
| OCR tam boyut (psm 11) | 3/4 | 3/3 | 1/2 (araç) | taban |
| OCR 168x94 tam kare | 3/4 | 3/3 | 0/2 | — |
| **OCR 168x94 metin bölgesi** | **4/4** | **3/3** | **2/2** | tamamı |
| OCR 168x94 kelime kırpımı psm 7 | 2/4 ("GETS", "IT"; "$124T" → "1241") | 3/3 | 2/2 | — |
| Kontrast metin ↔ zemin, p5 (min) | 7,06 (etiket: kraft üstünde lacivert) | 4,66 | 5,01 | ≥4,5 |
| Dolgu ↔ kontur (WCAG) | 13,03 | 18,81 | 18,81 | ≥4,5 |
| Süre damgası alanında metin | 0 | 0 | 0 | 0 |
| En yakın rakip renk farkı / rakip ortalaması | 96,5 Damon Cassidy / 146 | 98,6 Damon Cassidy / 135 | 107 Prof. Blackwood / 144 | — |
| Finalistler arası renk farkı | K1–K3 176 · K1–K4 124 · K3–K4 135 | | | ayrışma |

OCR notu: K3 tam karede 0/2 okunuyor; açık zemin, Leo ve kutular sayfa bölütlemesini bozuyor (S08 C1'de de aynı oldu). Metin bölgesinde ve psm 7'de 2/2. K1'deki "$124T" etiketi psm 7'de "1241" okunuyor, bölge OCR'ında "124T" tam. İlk sürümde etiket 112 px'ti ve süre damgası alanına 816 px taşıyordu; etiket 136 px'e büyütülüp yukarı alındı, taşma 0 oldu. Rakip benzerliği: en yakın rakip farkı 96–107, rakip ortalaması 135–146; finaller rakip kümesinden ayrışıyor. Rakip ızgarası repo dışında.
