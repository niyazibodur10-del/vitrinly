# F4 görsel kol — değerlendirme raporu · 1929-1000-dolar

**Ajan:** gorsel-varlik-sanatcisi · **Tarih:** 2026-10-27 · **Üretim:** koordinatör, Canva `generate-image` (Niyazi'nin aboneliği, ek ücret yok) · **Prompt'lar:** `canva-promptlari.md` §4 (birebir)
**Kontakt sayfaları:** `kontakt-dalga1.jpg` (referans sayfa + taban a + C02 kesik + C06–C11 yüzler + C01 kutular + C01 içinde Leo), `kontakt-dalga2.jpg` (C16–C19 içinde Leo + rig yama testi)

## Özet kararlar

| Id | Karar | Ana ölçüm |
|---|---|---|
| C01 stüdyo 3 kapı | **KABUL** | kapı H medyanı mavi 220° / yeşil 94° / kahve 18° (aralıklarda); 3 levha boş (iç kenar yoğunluğu 0,0003); yazı yok; öğeler merkez %80'de |
| C02 Leo tam boy | **KABUL** | kafa HSV kor. 0,88 (ölçeklenmiş 0,880); ten/saç/gömlek ΔE 2,3/0,4/1,5; liste 9/9; M4 v2 kesik saçak 0 |
| C06 göz kırpma | **KABUL** | bölge dışı fark %0,56; kafa kor. 0,91; yama geri kurma hatası 6,3 |
| C07 ağız B | **KABUL** | bölge dışı %0,50; kor. 0,88; dikiş %3,4 |
| C08 ağız C | **KABUL** | bölge dışı %0,18; kor. 0,85; dikiş %1,4 |
| C09 ağız E | **KABUL** | bölge dışı %0,61; kor. 0,88 |
| C10 ağız F | **KABUL** | bölge dışı %0,63; kor. 0,92 |
| C11 ağız G | **RED** (şekil) | hiza geçti (%0,28, kor. 0,90) ama **üst dişler görünmüyor** — kapalı nötr ağız; 'f/v' okunmuyor |
| C16 borsa dışı | **KABUL** (stil notu) | yazı yok; şeritler boş; bina jenerik |
| C17 banka içi | **KABUL** (stil + kadraj notu) | yazı yok; kasa sağ yarıda tam görünür |
| C18 banka önü kuyruk | **KABUL** (stil notu) | ön plan boş; yüzler küçük/stilize; levha boş |
| C19 vitrin | **KABUL** (stil notu) | etiketler boş; ürün markasız |

Canva kullanımı (bu video, şu ana kadar): **12 üretim** (dalga 1: 5, dalga 2: 7) · kabul 11 · tekrar gereken 1 (C11). Plan tavanı 27.

## Dalga 1

### Test yöntemi (araçlar)
- Kimlik/renk: `tools/gorsel/tutarlilik.py` (taban = paket-v1 a) → `tutarlilik-dalga1-2.json`.
- Rig hizası: `araclar/rig-yama.py` — |Cxx − a| > 30 fark maskesi, beklenen bölge (göz x830–1060 y175–275 / ağız x830–1050 y280–440) dışındaki ham fark oranı (kabul ≤ %1), yama kutusu kenarında dikiş, a-kesik + yama ile kaynağın yeniden kurulması → `rig/rig-yamalar.json`.
- C01: `araclar/c01-kapilar.py` (HSV segmentasyon, levha iç kenar yoğunluğu = yazı vekili; OCR kurulu değil → ayrıca 2× büyütülmüş kırpımlarla göz incelemesi) → `kapilar/C01-kapi-koordinatlari.json`.
- Stil vekil metrikleri: `araclar/stil-olcum.py` → `stil-olcum-cikti.txt`.
- Kesme: `araclar/kes-m4.py` (M4 v2, aşağıda) → `leo/C02-tam-boy-kesme.json`.
- Çözünürlük: `cozunurluk.txt` — 12 dosyanın tümü 1920x1080 (Canva doğal 1680x944'ten yeniden örnekleme; gerçek ayrıntı 1680 genişlik düzeyinde).

### C01 — KABUL
- Kapılar (1920x1080 tuval, piksel): `kapilar/C01-kapi-koordinatlari.json`

| Kapı | Dış kasa xyxy (±15 px, zemin ışığı payı) | Panel bbox xywh (kesin) | Medyan H / S | Levha iç alanı xyxy (KOD yazı) |
|---|---|---|---|---|
| mavi (sol) | 480, 307, 763, 751 | 524, 344, 197, 404 | 220° / 202 | 523, 241, 719, 290 |
| yeşil (orta) | 822, 318, 1073, 750 | 851, 345, 195, 402 | 94° / 187 | 850, 241, 1046, 290 |
| kahve (sağ) | 1130, 299, 1415, 750 | 1175, 344, 196, 403 | 18° / 223 | 1175, 241, 1371, 291 |

- Levha çerçeveleri (altın): mavi 513,231–729,300 · yeşil 840,231–1056,300 · kahve 1165,231–1381,301. İç alan 196x49 px; KOD yazı yüksekliği ≤ 34 px önerilir.
- Kapı tokmakları ~ (703,565), (1029,565), (1354,565). Zemin çizgisi y≈750; Leo ayak tabanı y≈750–900 arası (sahne önü boş: x 192–470 ve 1430–1728).
- Yazı/insan: yok (levhalar, arka plan şehir silüeti ve seyirci şeridi 1:1 incelendi). Üst/alt kenar koyu (vinyet) — pan-up'ta karanlık; sorun değil.
- Not: kahve kapı H 18° → "pas/turuncu-kahve" okunuyor (aralık içinde). Metinde "brown door" — istenirse KOD'da yalnız bu kapı maskesine S×0,85, V×0,9 (daha çikolata). Zorunlu değil.
- Stil: kontur + cel-shading; Leo kesiği yan yana uyumlu (kontakt alt satır). Stil metriği: düzlük %67,7 (Leo %61–71).

### C02 — KABUL
- Kontrol listesi 9/9: saç (hacimli, yana), kaş, kahve göz, kısa sakal+bıyık, siyah gömlek, açık yaka, kıvrık kol, **saat sol bilekte** (izleyicinin sağı), koyu gri chino, beyaz ayakkabı. Ayaklar kadrajda (bbox 791,49–1132,1052; figür 1003 px ≈ %93 yükseklik).
- Kimlik: kafa kor. 0,88 (kafa taban ölçeğine ×2,03 büyütülünce 0,880) ≥ 0,80; ten ΔE 2,3, saç 0,4, gömlek 1,5.
- Kesme: **M4 v2** `leo/C02-tam-boy.png` (RGBA 1920x1080). Kenar artığı 0,0075, saçak 0.
  - Aday karşılaştırması: M1 (anahtar) artık 0,124 · M2 GrabCut 0,129 · M3 GrabCut+arındırma 0,0187 · M4 v1 0,0188 **ama sol uylukta ~1,6k px delik** (koyu gri pantolon zemine ΔE<14; v1 yalnız <400 px kapalı delikleri dolduruyordu; saçak ölçümü yakalamadı çünkü delik alfa<0,5). **M4 v2**: kapalı delik, medyan zemin uzaklığı >6 ise doldurulur (gerçek zemin cebi ≈0–3) → delik kapandı, yeşil önizlemede temiz.
- Sınır: tam boy figür 1003 px → ≥2048 px karakter kuralı karşılanmıyor (Canva doğal tavanı). Kullanım küçük ölçekli (S04 klonlar, S18) olduğu için yeterli; yakın plan için paket-v1 bel üstü kullanılır.
- **C04 açılabilir** (referans [MAHZMdkmnN0, MAHZHpeQGdM]).

### C06–C08 rig (dalga 1) ve C09–C11 (dalga 2) — yamalar
Yamalar `rig/` altında, 1920x1080 tuval koordinatında; `leo/a-konusma-kapali.png` (M4 kesik) ya da paket-v1 a üstüne `konum_xy`'ye bindirilir. Alfa: fark maskesi +11 px, 4,5 px Gauss, kutu kenarında 6 px rampa ile 0.

| Yama | Rhubarb | konum_xy | boyut | Bölge dışı ham fark | Dikiş halkası | Kafa kor. | Karar |
|---|---|---|---|---|---|---|---|
| `goz-kapali-C06.png` | göz kırpma | 816,161 | 247x128 | %0,56 | %12,5* | 0,91 | KABUL |
| `agiz-B-C07.png` | B | 816,266 | 241x188 | %0,50 | %3,4 | 0,88 | KABUL |
| `agiz-C-C08.png` | C (+H) | 829,267 | 199x158 | %0,18 | %1,4 | 0,85 | KABUL |
| `agiz-E-C09.png` | E | 816,266 | 248x188 | %0,61 | %4,8 | 0,88 | KABUL |
| `agiz-F-C10.png` | F | 816,266 | 248x188 | %0,63 | %5,0 | 0,92 | KABUL |
| `agiz-notr-C11.png` | (G değil) | 816,266 | 220x187 | %0,28 | %3,2 | 0,90 | **RED (G)**; yedek nötr ağız |

\* C06 dikiş halkası kaş/kulak konturundan geçiyor (alt-piksel kontur kayması); alfa kenarda 0 olduğu için görünür dikiş yok — yeşil zeminli geri kurma testinde (kontakt-dalga2 alt bölüm) göz yok. Bölge dışı farkın tamamı ince kontur gürültüsü (3x3 açma sonrası %0,07–0,49).
- Şekil incelemesi: B dişler birleşik hafif açık ✓; C orta açık, üst-alt diş görünür ✓ (ağız köşeleri tabandaki yarım gülümseme kadar yukarıda — taban a ile süreklilik için kabul); E yuvarlak 'oh' ✓; F büzük ✓; göz kırpma iki göz kapalı, kaş/ağız değişmedi ✓.
- **C11 RED:** 4× yakın planda üst dişler hiç görünmüyor, alt dudak yalnız hafif ileri; 'f/v' yerine kapalı nötr ağız. Rig geçici eşleme: **G → B** (`agiz-B-C07`), tekrar gelene kadar. `agiz-notr-C11` gülümsemesiz kapalı ağız olarak yedek (ciddi cümlelerde X/A alternatifi; animasyon-yonetmeni kararı).
- **C11 tekrar prompt'u (aday A, önerilen; referans [MAHZHqW0_Uo, MAHZHpeQGdM]):** kart düzenleme kalıbı birebir + `ONLY CHANGE: the mouth makes the 'f' sound: the upper front teeth are clearly visible and rest on top of the lower lip, the lower lip is tucked slightly inward under the upper teeth, a thin white row of upper teeth shows between the moustache and the lower lip; jaw barely lowered; NOT smiling, mouth corners neutral. No text, no logos.`
  **Aday B (A da kalırsa):** referans [MAHZMeBO7dI (C07, dişler zaten görünür), MAHZHpeQGdM]: `ONLY CHANGE: the lower lip moves up and tucks under the upper front teeth so the upper teeth press on the lower lip and the lower teeth are hidden; NOT smiling.` Hiza yine a'ya karşı ölçülür.

## Dalga 2 — dönem plakaları C16–C19

### Stil değerlendirmesi (koordinatör notu: "resimsi/gerçekçi")
Vekil metrikler (`stil-olcum-cikti.txt`):

| Görsel | kontur % | düzlük % | doku std | doygunluk |
|---|---|---|---|---|
| Leo C02 / a | 1,15 / 0,61 | 61 / 71 | 0,94 / 0,57 | 23 / 25 |
| C01 stüdyo | 0,26 | 67,7 | 0,78 | 206 |
| C16 | 1,98 | 25,6 | 5,15 | 36 |
| C17 | 1,57 | 26,0 | 4,09 | 48 |
| C18 | 1,03 | 37,5 | 2,63 | 40 |
| C19 | 1,78 | 34,6 | 3,43 | 63 |

- Okuma: dönem plakalarında **çizgi konturu var** (kontur oranı Leo'dan bile yüksek) ama yüzeyler boyamsı (doku 3–7× fazla, düz alan yarıda) → "boyanmış animasyon arka planı + cel karakter" dili (klasik 2D dizi üretimi). Fotogerçekçi değil.
- Leo kesiği bindirme testi (`kontakt-dalga2.jpg`): sıcak, düz boyalı Leo soğuk sepya zeminden net ayrışıyor (referans-analizi kuralı: soğuk arka plan + sıcak karakter). Kenar/ölçek/ışık çatışması yok; C16'da en dramatik, en boyamsı plaka — hâlâ uyumlu.
- Niyazi stil kararı (2026-10-26): görseller referanstan daha gerçekçi/resimsi olabilir; şart Leo'nun tutarlılığı ve video içinde tek stil. Dört dönem plakası **kendi aralarında tek stil** (aynı sepya palet, kontur, doku 2,6–5,2); stüdyo (C01/C03) ayrı "dünya" ve geçiş anlatı içinde (mavi kapı geçmişe açılır). Bu yüzden **KABUL**; kabul ölçütündeki "kalın kontur + cel-shading" maddesi bu dört plakada Niyazi kararı gereği esnetildi — açık risk olarak hakeme yazıldı.
- Birleştirici öneri (KOD, animasyon-yonetmeni/kurgu): tüm plakalara ortak hafif kâğıt grenı + vinyet; dönem plakalarında Leo'ya ince soğuk rim ışığı yok (sıcak kalsın).
- **"Illustration" etiketi zorunlu**: C15–C19 görünür olduğu her sahnede (S01 0:00–0:02, S05, S07, S09, S12, S18) — politika denetimi B2 ile 6/6 planlı; bu plakalar resimsi olduğu için etiket şart, atlanamaz.
- Hakem RED derse tekrar prompt düzeltmesi (STYLE LOCK yerine): `STYLE LOCK: flat 2D TV-cartoon background, bold dark outlines, flat cel-shaded colors with simple 2-tone shadows, simplified shapes, minimal texture, NOT painterly, NOT photorealistic, same art style as the reference image.` + referans [MAHZMVzdpqQ (C01)] + "use only the drawing style of the reference, not its colors, doors or stage". Risk: C01 referansı mavi/kapı öğelerini sızdırabilir; 4 ek üretim.

### Plaka bazında
- **C16 KABUL:** şeritler boş (2× kırpım incelendi), harf/rakam yok; bina jenerik neoklasik (gerçek borsa cephesinin kopyası değil; arka plandaki kule 1920'ler NY silüeti tipi, marka değil). Sol üçte bir merdiven boş (Leo yeri). Yalnız S05 kapı maskesi içinde ve S06/S07 karartılmış zemin.
- **C17 KABUL:** kasa kapısı merkezi ≈ (1570, 517), dış yarıçap ≈ 270 px (bbox ≈ 1300–1840 × 247–787; Hough iç halka r=217). **Not:** kasanın sağ kenarı merkez %80 sınırını (x 1728) ~110 px aşıyor → bu plakada sağa pan yok; punch-in kasaya doğru yapılırsa merkez x≈1570 alınmalı; S07 sağ panel kırpımı (sağ yarı) sorunsuz. Kemer üstü süs taşı ve menteşe plakası yazısız (2× incelendi).
- **C18 KABUL:** kuyruk orta mesafede, yüzler küçük ve stilize, ağlayan/çaresiz yüz yok (G2); kapı üstü levha boş (2× kırpımda yalnız taş lekesi); ön plan sağ üçte bir boş (Bank Leo bel üstü yeri, kontakt). Kuyruktaki figürler siyah ceketli ama şapkalı/paltolu, Leo'ya benzemiyor.
- **C19 KABUL:** etiketler boş, kavanoz/kutu markasız; vitrin x≈1215–1790. **Sh2 9:16 kırpımı merkezde değil:** x 1200–1807 (607 px şerit) vitrini kapsar.

## Elenenler
- C11 (ağız G) — şekil yanlış (diş yok). Tekrar: yukarıdaki aday A, sonra B.
- Kesme M1/M2/M3 ve M4 v1 (C02) — artık/delik nedeniyle; kazanan M4 v2.

## Lisans / üretim kaynağı
Tümü Canva AI (`generate-image`), Niyazi'nin Canva hesabı, 2026-10-27; prompt = `canva-promptlari.md` §4 ilgili blok; media id'ler `canva-ham/uretim-kaydi.md` ve `canva-promptlari.md` §5. Türev dosyalar (kesik, yama, kapı JSON) bu ajanın betikleriyle üretildi.

## Özgünlük
C01, C16–C19 bu videoya özgü yeni üretim; önceki videodan yeniden kullanılan sahne görseli 0. Rig yamaları ve C02 kanal karakter varlığı (muaf sınıf).

## Teslim — animasyon-yonetmeni
- `leo/C02-tam-boy.png` (C04/C05 gelene kadar S04 klonları duruş pozu)
- `rig/goz-kapali-C06.png`, `rig/agiz-{B-C07,C-C08,E-C09,F-C10}.png`, `rig/agiz-notr-C11.png` + `rig/rig-yamalar.json` (konumlar). Rhubarb: A,X = a (taban) · B = C07 · C,H = C08 · D = paket-v1 b · E = C09 · F = C10 · G = geçici C07 (C11 tekrarına kadar).
- `kapilar/C01-kapi-koordinatlari.json` (levha iç alanları KOD yazı için).
