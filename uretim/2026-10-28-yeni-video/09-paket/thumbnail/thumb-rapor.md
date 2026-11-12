# F8 — Thumbnail raporu · S08 "If America Earned $5,400 a Month, Here's Its Budget"

İLERLEME: tamam (3 finalist, tüm kapılar geçti). Yeniden üretim: `THUMB_TMP=<geçici> python3 thumb-uret.py` → finalistler `adaylar/{A1,B1,C1}.jpg` kopyası → `python3 thumb-test.py <repo-dışı rakip klasörü> A1 B1 C1`.
**Karar:** Test & Compare sırası **1) A1 · 2) C1 · 3) B1**. Varsayılan (ilk yüklenen) = A1 (hakem H8 konsepti "−$2,000/MO", hook 0:03–0:14 ile birebir).
**Kapılar [Ö]:** 1280x720 ✅ · ≤2 MB (98–111 KB) ✅ · ≤4 kelime ✅ · 168x94 OCR ✅ (aşağıda) · kontrast p5 ≥4,5 ✅ (min 5,01) · süre damgası alanında metin 0 px ✅ · iki koşu aynı sha256 ✅ (yeni betik).
**Yeni Canva üretimi: 0** (2 hak korundu). Metin, levha, LCD ekranı, ışık kodla. Kaynaklar yalnız kabul edilmiş varlıklar.
**youtube-paketleyici için:** `paket.md` → `<!-- veri:thumbnail-ana -->` bloğuna tek satır yaz: `../09-paket/thumbnail/A1-eksi-2000.jpg` (1929 `yayin-paketi.json` biçimi; dosya yolları 09-paket'e göre `../`). Başlık–thumbnail tablosunu (§1) A1/C1/B1 harfleriyle yeniden yaz; sonra `paket-uret.py` → `paket-kontrol.py`. Test & Compare için diğer iki dosya: `C1-faiz-ordu.jpg`, `B1-hesap-makinesi.jpg` (yükleme sonrası Studio'dan elle; API Test & Compare desteklemiyor [T]).
Etiketler: **[Ö]** betik ölçümü · **[T]** yargı.

## Finalistler

| Sıra | Dosya (sha256 ilk 12) | Açı | Metin | Kaynak |
|---|---|---|---|---|
| 1 | `A1-eksi-2000.jpg` (f8148925a6df) | duygu (yakın yüz) | **−$2,000** (kırmızı levha) EVERY MONTH | Plaka `05-gorsel/canva-ham/G06.png` (üstten masa, x1,4, boş ışıklı orta; bulanık) + 1929 `leo/d-saskin.png` (şaşkın). Kod: sıcak ışık, levha, metin |
| 2 | `C1-faiz-ordu.jpg` (ad63f8d5b1f8) | karşıtlık | **INTEREST** (kırmızı levha) **> MILITARY** (koyu levha) | 1929 `leo/C13-kollar-kavusmus.png` gövde + `d-saskin` kafa (satır genişlikleri ±5 px → `kafa_degis`) + `05-gorsel/nesne/G03-zarf-kapali.png` (tek zarf = metindeki "envelope five"). Camgöbeği kod zemin |
| 3 | `B1-hesap-makinesi.jpg` (a5fc459fa14a) | obje | EVERY MONTH (koyu levha, sarı) + hesap makinesi ekranı **−2,000** | `05-gorsel/nesne/G07-hesap-makinesi.png` (x1,92, LCD kodla yeniden boyandı) + 1929 `leo/e-dusunen.png`. Mercan-kırmızı kod zemin |

Canva media ID'leri varlıkların kendi kayıtlarında (`05-gorsel/canva-ham/uretim-kaydi.md`, 1929 `05-gorsel/rapor.md`); thumbnail için yeni ID yok.

**Başlıkla okunuş [T]:** Başlık geliri verir ($5,400). A1 açığı verir (−$2,000 her ay) → "nereye gidiyor?". C1 bütçenin içinden tek şaşırtıcı kalemi verir → "faiz orduyu mu geçti?". B1 aynı açığı nesneyle verir. Hiçbiri başlık rakamını tekrar etmez.
**Doğruluk / politika:** A1, B1 = R03 (açık ~2.000 $/ay, ekran biçimi "−$2,000/MO", metin S01 "about two thousand dollars short"). C1 = R08/R12 (net faiz 1.051,8 > savunma 965,2 milyar $, FY2026; metin "more than its whole military"). Zarf boyut kıyası bilerek kullanılmadı (fark %9; büyük/küçük zarf abartı olurdu). "credit card" / kart görseli yok; "Nearly $7 for $5" thumbnail'da yok (o oran metinde geçmiyor, yalnız Alt-2 başlıkta). Gerçek kişi, logo, bayrak, parti yok. Leo kurgusal; şapka/takım yok (Fred'den ayrışma).

## Test kapısı [Ö]

`python3 thumb-uret.py` (iki koşu, 6 adayın sha256'sı aynı) · `python3 thumb-test.py <rakip> A1 B1 C1` (thumb-test.py 35aef6fe6baa, thumb-uret.py 26ec6a326595).

| Ölçüt | A1 | C1 | B1 | Eşik |
|---|---|---|---|---|
| Dosya | 111 KB | 98 KB | 105 KB | ≤2 MB |
| Kelime | 3 | 2 (+ ">") | 3 | ≤4 |
| 168x94 büyük harf yüksekliği (min) | 16,9 px | 13,5 px | 13,0 px | ≥9 |
| OCR tam boyut | 4/4 | 0/2 (araç) | 2/4 | taban |
| OCR 168x94 tam kare (psm 11) | 2/4 | 0/2 | 3/4 | — |
| OCR 168x94 metin bölgesi (psm 11) | 2/4 (+ levha satırı psm 7: "$2,000") | **2/2** | **4/4** | bölgede tamamı |
| Kontrast metin ↔ zemin/levha, p5 | 5,01 / 7,51 / 5,33 | 5,01 / 17,07 | 11,61 / 11,82 | ≥4,5 |
| Dolgu ↔ kontur (WCAG) | 17,07 (koyu yazı, beyaz kontur) | levha | levha | ≥4,5 |
| Süre damgası alanında metin | 0 | 0 | 0 | 0 |
| Rakipten renk farkı (en yakın / rakip ort.) | 117 CrashCourse / 137 | 114 Fred / 141 | 105 Finance Economist / 132 | — |

OCR notu: tesseract psm 11 kırmızı levhadaki "−$2,000" satırını 168x94'te atlıyor; aynı satırın kırpımı psm 7'de "$2,000" okunuyor (eksi işareti OCR'da düşüyor, `test/mobil-168x94-finalist.png`'de gözle okunuyor). C1 tam karede 0/2: Leo + düz zemin sayfa bölütlemesini bozuyor, metin bölgesinde 2/2. Bu yüzden `thumb-test.py`'ye bölge OCR'ı ve "$→S" düzeltmesi eklendi.
Zemin rengi: üçü de açık/doygun (sıcak masa, camgöbeği, mercan). 1929'daki üç koyu lacivert tekrarı yok. Fred deseninden (açık mavi gök, üstte siyah metin, sağda işaret eden maskot) ayrışıyor: Leo işaret etmiyor, metin levhalı. Rakip ızgarası repo dışında (`<geçici>/rakip/rakip-yan-yana*.jpg`; 8 rakip `i.ytimg.com` mqdefault).

## Elenenler

| Aday | Neden |
|---|---|
| A2 ALWAYS $2,000 SHORT | "ALWAYS" p5 3,41 (<4,5) ve aşırı genelleme: FY2025 açığı ~1.775 $/ay (R15), "her zaman 2.000" doğru değil |
| B2 SHORT AGAIN | B1 ile aynı ölçüm; "again" geçmiş yıllara dair kanıtsız ima, "EVERY MONTH" metnin kendi cümlesi |
| C2 INTEREST > MILITARY (tek satır) | 168x94 büyük harf 11,7 px (C1'de 13,5–16,9); tek satır uzun |
| İlk C taslağı (küçük MILITARY + büyük INTEREST zarfı) | MILITARY etiketi 168x94'te 5,6 px; zarf boyut farkı gerçek farkı (%9) abartıyordu |
| İlk A/B taslakları | A: G06 kupası ve lamba metnin arkasında (p5 1,08–2,9) → kadraj masanın boş ortasına alındı. B: beyaz/sarı yazı mercan zeminde p5 2,97 → koyu levha |

## Riskler
- A1 ile CrashCourse "Deficits and Debt" ikisi de turuncu (renk farkı 117, ort. 137); yüz + kırmızı levha ayırıyor [T].
- C1 açısı başlıktan farklı bir merak kurar. Test & Compare kazanırsa video başında faiz/ordu karşılaştırmasının geç geldiği (metin ~orta) izleme süresini etkileyebilir; F12'de kontrol edilmeli [T].
