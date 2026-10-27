# F4 görsel kol — sahne listesi · 1929-1000-dolar

**Ajan:** gorsel-varlik-sanatcisi · **Tarih:** 2026-10-27 · **Girdi:** `03-metin/metin.md` (KİLİTLİ, 24 sahne, GÖRSEL sütunu), `03-metin/politika-denetimi.md` (G2, G6, B2), `assets/karakter/karakter-karti.md` (taban + düzenleme kilidi).
**Prompt paketi:** `canva-promptlari.md` (C01–C22). **Hazırlık testi:** `hazirlik/` (bkz. §5).

## 1. Kaynak türleri ve kısaltmalar

| Kod | Kaynak | Kim yapar |
|---|---|---|
| **CV-A** | Canva illüstrasyonu, **karaktersiz arka plan plakası** (Leo ayrı katman olarak üstüne konur) | koordinatör Canva'da üretir → ben değerlendirir, keser |
| **CV-L** | Canva **yeni Leo pozu** (taban + düzenleme; düz slate-blue zemin → kesilir) | koordinatör üretir → ben keserim (M4) |
| **KOD** | Remotion'da kodla çizilen grafik / harita / sayaç / kart / ikon / yazı | animasyon-yonetmeni (ben yalnız listelerim) |
| **PK** | Var olan karakter varlığı: `assets/karakter/paket-v1/` (a, b, b-alt, c, d, e, f); kesik hâlleri `05-gorsel/leo/` (M4 yöntemi) | ben keserim, animasyon-yonetmeni kullanır |

Leo pozları: **a** konuşma-kapalı (taban) · **b** "aah" açık ağız (a ile piksel hizalı) · **b-alt** gülümseyerek konuşma · **c** ekran soluna işaret · **d** şaşkın · **e** düşünen · **f** sevinçli. Yeni: **C02** tam boy duruş · **C04** yürüme · **C05** kutuyla yürüme · **C12** iki elle sunum · **C13** kollar kavuşturmuş · **C14** kutuyu göğüste tutma · (seçmeli) **C20** saate bakma · **C21** el sallama. Rig: **C06** göz kırpma · **C07–C11** ağız B, C, E, F, G.

Klonlar (Stock / Bank / Box Leo) **aynı Leo kesiklerinin kopyalarıdır**; farkı yalnız KOD ile eklenen renkli yaka kartı (mavi STOCK, yeşil BANK, kahve BOX) ve sahne. Ayrı bir karakter üretilmez → tutarlılık riski sıfır.

## 2. Temel karar: katmanlı kompozisyon (3 aday, test, eleme)

| Aday | Yöntem | Ölçüt sonucu | Karar |
|---|---|---|---|
| **A** | Karaktersiz arka plan plakası (CV-A) + ayrı Leo kesiği (PK / CV-L) + KOD grafik | Leo her sahnede **aynı piksel kaynaktan** → tutarlılık garanti; konuşan sahnelerde dudak senkronu rig'i (a/b + ağız yamaları) bozulmadan çalışır; bir plaka birden çok sahnede (farklı kadraj/renk notu ile) kullanılır → Canva sayısı en az | **SEÇİLDİ** |
| B | Her sahne için Leo'lu tam illüstrasyon (Canva, sahne içinde Leo) | 24+ üretim; her karede yüz yeniden çizilir (hafıza: sıfırdan üretim kafa kor. 0.45); ağız şekilleri sahne başına yeniden üretilmeli → dudak senkronu imkânsız | ELENDİ (tutarlılık + hak tüketimi) |
| C | "Leo'yu sahneye koy" düzenlemesi (taban + EDIT ONLY CHANGE background) | Yüz tutarlı kalır (düzenleme yöntemi), ama her sahne 1 üretim ve ağız/jest değişimi yine sahne başına yeniden üretim ister | ELENDİ (ana yol olarak); yalnız katman ışık uyumu bozuk çıkan tek bir sahnede yedek |

**H4 kritik yol — 3 klonlu kapı sahnesi (S04):** A = C01 stüdyo plakası + C04 yürüme kesiği ×2 (Stock, Bank) + C05 kutuyla yürüme kesiği ×1 (Box), sırayla soldan kapılara kayar (KOD: x-öteleme + 2 karelik dikey zıplama + hafif ölçek), yaka kartları KOD. B (elendi) = tek Canva karesinde 3 Leo: aynı karede 3 yüz → yüzler birbirinden de ayrışır, ölçülemez. **B planı** (metinde): tek Leo kapıdan kapıya yürür, klonlar skor tablosunda ikon (C04 tek kopya).

## 3. Sahne tablosu (24/24 sahne bir kaynağa atandı)

Kısaltma: **Sh1/Sh2** = Shorts 1 / Shorts 2 kesitinde kullanılır (9:16 gerekir). **İll.** = ekranda "Illustration" etiketi (P5/B2; Canva 1929–33 mekân karesi görünürken).

| Sahne | Zaman | Görsel ihtiyacı (GÖRSEL sütunundan) | CV-A plaka | Leo katmanı | KOD | İll. | 9:16 |
|---|---|---|---|---|---|---|---|
| S01 | 0:00–0:17 | 0:00 sepya 1929 NY sokağı (yavaş zoom) → 0:02 whoosh → stüdyo, 3 dev kapı; "Let's play"de iki elle kapıları gösterir | **C15** sokak · **C01** stüdyo geniş | a/b (konuşma) → **C12** sunum (Let's play) | "$1,000", "SEPT 1929", kapı levhaları, kapı ışık yanması, DISASTER?/GAMBLE?/SURPRISE? dönen etiketler | Evet (yalnız 0:00–0:02 sokak karesi) | **Sh1** (kapı tanıtımı) |
| S02 | 0:17–0:41 | stüdyo orta plan, arkada dev takvim yaprağı 1929↔2026 | **C03** stüdyo orta (boş ekran) | a/b ("I'm Leo"; göğüs işareti pozu yok → konuşma pozu; **c** aynalanarak kullanılmaz, saat sol bilekte kalmalı) → **b-alt** ("I'm a cartoon") | takvim yaprağı (ekranda), 3 madde | Hayır | — |
| S03 | 0:41–1:06 | tez satırı + maaş grafiği G0 | **C03** | a/b ciddi → **e** (maaş kısmı) | tez yazısı, **G0** maaş çubuğu + 12 ay kutusu, kaynak etiketi | Hayır | — |
| S04 | 1:06–1:35 | kural kartları; 3 klon kapılara yürür; Box Leo kutuyu kucaklar; sunucu işaret + göz kırpar | **C01** | klonlar: **C04** ×2 + **C05** ×1 · sunucu: **c** + **C06** göz kırpma | kural kartları (pop), yaka kartları STOCK/BANK/BOX, yürüme hareketi | Hayır | — |
| S05 | 1:35–2:16 | mavi kapı açılır → sepya borsa salonu dışı, ticker şerit yağmuru; G1a | **C16** borsa dışı (kapı içinden görünür) | Stock Leo: **f** sevinçli (ön plan, bel üstü) | kapı açılma maskesi, ticker tape parçacıkları, **G1a**, ekran yazıları, kaynak | Evet | — |
| S06 | 2:16–2:53 | takvim yaprakları koparılır; G1a/G1b; sayaç 1,000→500 | (yok — grafik sahnesi; arka plan C16 karartılmış/bulanık) | Stock Leo: **d** şaşkın | takvim kopması, **G1a** dalgalı iniş, **G1b** iki çubuk, sayaç | Hayır (C16 bulanık arka plan görünürse Evet) | **Sh1** (son cümle: sayaç 1,000→~500) |
| S07 | 2:53–3:15 | bölünmüş ekran: solda Stock Leo nefes; sağda banka içi (mermer, dev kasa) | sol: C16 (karartılmış) · sağ: **C17** banka içi | sol: **e** · sağ Bank Leo: **C13** kollar kavuşturmuş | bölme çizgisi, "−50% IN ~10 WEEKS", sallanan "Right?" | Evet (banka içi) | — |
| S08 | 3:15–3:52 | stüdyo; sunucu boş "INSURANCE" kutusunu işaret eder; ABD haritası banka noktaları yanar/söner | **C03** | sunucu: **c** işaret · Bank Leo arka planda gazete indirir → küçük **C13** (gazete yok; B: gazete KOD ikonu) | INSURANCE kutusu, **ABD haritası** ~24.000 nokta + dalga dalga sönme, ekran yazıları, kaynak | Hayır | — |
| S09 | 3:52–4:31 | sepya banka önü kuyruk (stilize yüzler, tabela yok); para mekanizması; kuyruk yan bankaya kayar | **C18** banka önü kuyruk | Bank Leo: **C20** saate bakma (seçmeli; yoksa **e** düşünen) | **madeni para mekanizması** (10 para, 9 LOANS), kuyruk oku, ekran yazıları | Evet | — |
| S10 | 4:31–5:15 | G2 çubuk grafiği; kasa önünde sayaç ikiye ayrılır; GAMBLE damgası | **C17** banka içi (kasa önü; grafik bölümünde bulanık) | Bank Leo: **d** → **e** | **G2** (1921–33 çubukları), mudi kaybı katmanı, bölünen sayaç, GAMBLE damgası, kaynak | Evet (C17 görünürken) | **Sh1** (G2 + "≈9,000 SUSPENDED") |
| S11 | 5:15–5:35 | abone düğmesi (3 sn); stüdyo, spot kahve kapıya; Box Leo kutuyu kulağına tutup sallar | **C01** | sunucu: a/b → kaş kaldırma = **d** · Box Leo: **C14** kutuyu tutma (KOD: kulağa doğru döndürme + sallama) | abone düğmesi animasyonu, spot ışığı, "DOOR 3", "?" | Hayır | — |
| S12 | 5:35–6:10 | G3 TÜFE; dükkân vitrininde fiyat etiketleri küçülür; banknotlar parlar | **C19** 1930'lar dükkân vitrini (etiketsiz, yazısız) | Box Leo: **C14** + yüz **d** → **f** geçişi yerine C14 tek poz + KOD parıltı | **G3** + ikinci eksen, **fiyat etiketleri** (KOD, vitrin üstüne), banknot parıltısı | Evet | **Sh2** (G3 kesiti) |
| S13 | 6:10–6:47 | G3b para arzı; haritada binlerce kutu belirir, banka noktaları söner | **C03** (giriş) | sunucu: **e** → a/b | **G3b** iki sütun, **ABD haritası** + kutu ikonları, "ONE BOX ✓ · A COUNTRY OF BOXES ✗" | Hayır | — |
| S14 | 6:47–7:12 | 4 tuzak kartı (0% INTEREST, FIRE, THEFT, JOB LOSS); Box Leo kutuya sarılır, gözleri kısılır | (yok — kart sahnesi; arka plan C01 bulanık) | Box Leo: **C14** (KOD: göz kısma yerine hafif kafa eğme; B: **e**) | 4 tuzak kartı + ikonlar (çizgi alev, gölge el, uçan banknot), "NOT SO FAST" | Hayır | — |
| S15 | 7:12–8:02 | G1 tam Dow grafiği + 1.000 $ çizgisi + 1954/1936 notları | **C03** (ekranda grafik) veya düz grafik zemini | Stock Leo: **e** düşünen, ciddi | **G1 tam**, zorunlu alt not "Price only, before dividends.", 1954/1936 notu, ekran yazıları | Hayır | — |
| S16 | 8:02–8:34 | G4 skor tablosu, sunucu sunum pozunda | **C03** | sunucu: **C12** sunum | **G4 skor tablosu** (3 sütun, BANK "?" + 2 alt satır, şerit "IN A DECADE OF FALLING PRICES") | Hayır | **Sh1** (dikey skor kartı + şerit) |
| S17 | 8:34–8:42 | üç kapıya zincir + asma kilit iner | **C01** | sunucu: **d** şaşkın | zincir + kilit ×3 (KOD, kapı koordinatlarına), "MARCH 1933" | Hayır | — |
| S18 | 8:42–9:37 | ABD haritası griye döner; otel notu kartı; Roosevelt yalnız radyo silueti; Bank Leo kilitli kapıda; Box Leo arka planda bakkala yürür | **C17** banka içi (kasa kapısı + KOD zincir = "kilitli kapı") · **C15** sokak (Box Leo yürür) | Bank Leo: **e** · Box Leo: **C05** (küçük ölçek, sokakta) | **harita** eyalet eyalet gri, otel notu kartı, radyo silueti (yüz yok, G6), ekran yazıları | Evet (C15/C17 görünürken) | — |
| S19 | 9:37–9:57 | G2 devamı (1934 = 61, 9 insured dilimi); kahve kapı raylarda kayar, takvim 1933→2026 | **C01** | sunucu: **b-alt** muzip gülüş (el ovuşturma yok → B: b-alt) | **G2 devamı**, kapı kayma (C01'den kahve kapı kırpımı KOD ile kaydırılır), takvim | Hayır | — |
| S20 | 9:57–10:23 | modern soğuk mavi stüdyo; banknotlar grafik yanında küçülür; Box Leo merakla bakar | **C03** (KOD renk notu: soğuk mavi) | Box Leo: **e** düşünen (H2: aşağılanma yok) | küçülen banknot yığını, **G5a**, kaynak | Hayır | **Sh2** (S20 iki parça) |
| S21 | 10:23–10:53 | G5 ayna grafiği iki panel; sunucu iki paneli iki eliyle tutar gibi | **C03** | sunucu: **C12** sunum (iki el açık) | **G5** iki panel, 42/48 MONTHS etiketi, "SAME BOX. OPPOSITE RESULT.", "ARITHMETIC, NOT A PLAN" | Hayır | **Sh2** (üst-alt panel) |
| S22 | 10:53–11:06 | yeşil kapı; 1934 kilidi modern kilide dönüşür | **C01** (yeşil kapıya punch-in) | sunucu: **c** işaret | kilit dönüşümü, ekran yazısı | Hayır | — |
| S23 | 11:06–11:38 | stüdyo geniş plan, 3 kapı + final etiketleri; tavanda termometre/ok | **C01** | sunucu: a/b sıcak | final etiketleri DISASTER/GAMBLE/SURPRISE, termometre/ok, tez satırı | Hayır | — |
| S24 | 11:38–11:54 | ışıklar kısılır; sağda uç ekran boşluğu; dördüncü kapı silueti; el sallar | **C01** (KOD: karartma + 4. kapı silueti) | sunucu: **C21** el sallama (seçmeli; yoksa **b-alt**) | uç ekran boş alanları, 4. kapı silueti, "THANKS FOR PLAYING" | Hayır | — |

**Kontrol:** 24/24 sahnenin her birinde en az bir kaynak atanmış (betikle sayıldı, §6). Gerçek kişi yüzü yok (Roosevelt yalnız KOD siluet), tabela/logo yok (Bank of United States adı yalnız KOD ekran yazısı), kuyrukta ağlayan yüz yakın planı yok (politika G2).

## 4. Canva üretim sayısı ve gerekçesi

| Grup | Id | Adet | Kullanıldığı sahne sayısı | Gerekçe |
|---|---|---|---|---|
| P0 kritik yol (F5 testi) | C01–C05 | 5 | C01: 10 sahne · C03: 9 sahne · C02→C04→C05: S04, S18 + B planı | Konuşan Leo (PK a/b kesikleri hazır, §5) + C03 plaka; 3 klon sahnesi = C01 + tam boy taban + 2 yürüme pozu |
| P1 rig (kanal varlığı, bir kez) | C06–C11 | 6 | tüm konuşan sahneler (≈14 sahne) + sonraki videolar | Göz kırpma + 5 ağız (B, C, E, F, G); A/X = a, D = b, H = C. Bir kez üretilir, `assets/karakter/` altına girer; sonraki videolarda 0 üretim |
| P2 jest pozları | C12–C14 | 3 | C12: S01, S16, S21 · C13: S07, S08 · C14: S11, S12, S14 | Metnin istediği ve paket-v1'de olmayan 3 jest |
| P3 dönem plakaları | C15–C19 | 5 | C15: S01, S18 · C16: S05–S07 · C17: S07, S10, S18 · C18: S09 · C19: S12 | Her biri metnin GÖRSEL sütununda adı geçen bir mekân; iki tanesi 2–3 sahnede yeniden kullanılır |
| P4 seçmeli | C20–C22 | 3 | C20: S09 · C21: S24 · C22: Sh1/Sh2 dikey zemin | Hak yeterse; yoksa B (e / b-alt / C03'ten 9:16 kırpım) |
| **Toplam** | | **çekirdek 19 (P0–P3) + seçmeli 3 = en çok 22** | | Yeniden deneme payı: en çok 5 (kabul ölçütünü geçmeyen her üretime 1 tekrar). **Kötü durum tavanı 27.** |

Elenen sayı stratejisi: sahne başına 1 Leo'lu illüstrasyon (≈24–30 üretim, rig yok) ve referans videodaki gibi ~4 sn'de bir yeni illüstrasyon (≈180) — Canva aylık hakkı ve tutarlılık için elendi. Görsel tempo (her 5–10 sn'de değişim, kalite kapısı Retention) aynı plakada **kamera kadrajı (geniş / orta / punch-in), Leo poz değişimi ve KOD grafik** ile sağlanır: 8 plaka × ortalama 3 kadraj + 14 Leo pozu + ≥12 grafik.

**Özgünlük (Ö6):** C01, C03, C15–C19 bu videoya özgü yeni üretim. Önceki videodan aynen yeniden kullanılan sahne görseli: **0** (kanalın ilk videosu). Karakter varlıkları (paket-v1, rig C02/C04–C14) muaf sınıfta; `rapor.md`'de listelenecek.

## 5. 16:9 ve 9:16 güvenli alan

- **Kaynak boyut:** Canva doğal 1680x944 → `tools/gorsel/canva-indir.md` yoluyla 1920x1080 export. Kamera hareketi için plaka prompt'larında **kenarlarda %10 taşma payı** istenir (önemli öğe merkez %80'de). Punch-in ≤1.15× doğrudan; >1.15× (S22 yeşil kapı, S19 kahve kapı, Shorts kapı kırpımları) → `tools/karakter/buyut.py` x4 (yalnız gereken kırpım; tam plaka ≈13 dk CPU, §5 ölçümü).
- **Leo katman yerleşimi (16:9):** sunucu Leo **sol veya sağ üçte birde**, bel üstü, alt kenardan taşar (kesik bel çizgisi kadraj dışında). Grafikler karşı üçte ikide. Kafa üstü boşluğu dar (hafıza): Leo katmanında pan-up yok, punch-in yüz merkezli.
- **Kapı koordinatları:** C01 geldiğinde üç kapının dikdörtgenini ölçüp `05-gorsel/plakalar/C01-kapilar.json` olarak veririm (zincir, ışık, açılma maskesi, kayma için).
- **Shorts işaretli sahneler:** S01, S06, S10, S16 (Sh1) · S12, S20, S21 (Sh2).
  - 9:16 = 1080x1920. 16:9 karenin merkez dikey şeridi genişliğin %31,6'sı → kapı sahnesi sığmaz: **kapılar C01'den ayrı ayrı kırpılıp (x4 büyütme) dikey yığılır** (metin §5: üstte mavi, ortada yeşil, altta kahve) — KOD.
  - Grafik sahneleri (G1b sayaç, G2, G4, G3, G5a, G5) 9:16'da KOD ile yeniden dizilir (vektör, kayıpsız).
  - Leo kesiği 9:16'da alt üçte birde, kafa üst güvenli alanın altında (YouTube Shorts arayüzü: üst ~%10 ve alt ~%20 başlık/düğmeler; sağ kenar ~%15 düğme sütunu) → yazı ve yüz bu bölgelerin dışında.
  - Arka plan 9:16: C22 (seçmeli dikey stüdyo) yoksa C03'ün merkez kırpımı (607x1080 → 1080x1920, ×1,78) bulanık + karartılmış zemin olarak; netlik gerektiren öğe konmaz.

## 6. Hazırlık hattı testi (paket-v1 ile, 2026-10-27)

Betik: `hazirlik/kes-test.py` (3+1 kesme adayı, ölçüm, yeşil önizleme). Komut: `~/.finansal-arac/venv/bin/python -I hazirlik/kes-test.py <poz.png> hazirlik/<ad>`.

| Poz | M1 renk anahtarı (artık / saçak px) | M2 GrabCut | M3 GrabCut + arındırma | **M4 renk anahtarı + arındırma** |
|---|---|---|---|---|
| a-konusma-kapali | 0.074 / 0 | 0.137 / 256 | 0.066 / 48 | **0.001 / 0** |
| c-isaret | 0.078 / 0 | 0.181 / 147 | 0.076 / 1 | **0.001 / 0** |
| e-dusunen | 0.079 / 0 | 0.127 / 256 | 0.073 / 66 | **0.000 / 0** |
| f-sevincli | 0.079 / 99 | 0.163 / 562 | 0.111 / 161 | **0.000 / 99** |

Artık = maske sınırının 3 px iç halkasında zemine ΔE<25 piksel oranı; saçak = alfa>0,5 iken zemin renginde kalan piksel. **Kazanan M4** (renk anahtarı + kenar arındırma). Görsel kontrol `hazirlik/*/kesme-kontak.jpg`, `hazirlik/sac-kenari-1e1-x3.jpg`: M2/M3 saç ucunda mavi saçak; M4 temiz. f-sevincli'deki 99 px: yumruk parmak arası küçük kapalı zemin cebi (<400 px, delik doldurma eşiği) — yeşilde 1:1 görünmüyor; kabul, C-pozlarında eşik 150 px'e çekilecek.
**Negatif kontrol:** ilk sürümde delik doldurma, kol–gövde arasındaki zemini de dolduruyordu; saçak ölçümü bunu **9.240 px** ile yakaladı (yeşil önizlemede mavi şerit) → ölçüm hatayı görüyor; düzeltme: yalnız kenara değmeyen ve <400 px delikler doldurulur.
**Elenen:** `tools/karakter/kes.py` (pilot portresine özel sabit bölgeler; düz zemin için gereksiz), M2 GrabCut (saçak), M3 (M4'ten kötü, 5× yavaş).
**Büyütme:** `buyut.py` 160x160 yüz kırpımı → 640x640, 38,8 sn duvar (19,6 sn CPU, `nice 10`, model yükleme dahil); çizgiler net, ten düz (`hazirlik/esrgan-yuz-x4.png`). Tam 1680x944 plaka tahmini ≈13 dk (0,5 sn/1000 px [ölçüm, docs/uretim-hatti-testi.md]) → yalnız punch-in kırpımlarına uygulanır, TTS/render ile aynı anda koşturulmaz.
