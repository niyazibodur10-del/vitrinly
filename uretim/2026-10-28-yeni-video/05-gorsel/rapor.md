# F4 görsel kol — rapor · S08 Kitchen Table Budget
**İLERLEME:** biten = dalga 1–2 değerlendirme + kesikler + animasyon varlık listesi · sıradaki = (isteğe bağlı) G08b tek tekrar → değerlendirme; metin kilidinden sonra GÖRSEL sütunu eşlemesi (yeni üretim tavanı: kalan 1–2) · yarım = yok · büyük medya yok.
**Karar:** metinden bağımsız temel varlıklar planlandı; çekirdek 8 + seçmeli 2 üretim, tavan 12 (tekrar payı 2). Leo masada = mevcut rig + masa plakası (yeni oturan taban yok).
**Kapı:** `python3 -I araclar/prompt-kontrol.py canva-promptlari.md` → 10/10 GEÇTİ (çıktı `araclar/prompt-kontrol-cikti.txt`; girdi sha256 47c654a91b14); negatif kontrol (saat sağ bilek, "NOT painterly" silme, banknot yasağı silme, prompt'a "$7,400") → KALDI (exit 1); 2 koşu aynı (çıktı sha256 ce67eaf65211).
**Erken karar satırı (mutfak kazananı G01|G02):** **G01 = MAHZvHhbFqQ** (2026-11-02). Dalga 2'de G06/G09/G10 referansı budur. G04 RED (tekrar önerilmez, aşağıda).

## Plan
| Id | Varlık | Tür | Dalga | Kritik yol |
|---|---|---|---|---|
| G01 / G02 | Mutfak masası orta plan, 2 aday (C01 stil ref / referanssız) | plaka | 1 | evet (H4) |
| G03 | Zarf nesne sayfası (kapalı, açık, yığın, kâğıt) | nesne | 1 | evet (matruşka) |
| G04 / G05 | Leo zarfı açar / zarftan zarf çıkarır (kafa sabit, rig uyumlu) | Leo düzenleme | 1 | evet |
| G06 | Kuşbakışı fatura masası | plaka | 2 | — |
| G07 | Kumbara, kasa, boş kredi kartı, hesap makinesi, işaretsiz para | nesne | 2 | — |
| G08 | Leo hesap makinesi | Leo düzenleme | 2 | — |
| G09 / G10 | Dikey mutfak (Shorts) / buzdolabı boş notlar | plaka seçmeli | 2 | — |

## Yeniden kullanım ve özgünlük
- Yeniden kullanılan yalnız karakter varlıkları (muaf sınıf): paket-v1 a/b, 1929 `rig/` yamaları, 1929 `leo/` jest kesikleri (c, d, e, f, C02, C04, C12, C13, C20, C21). Önceki videodan yeniden kullanılan **sahne görseli: 0**; tüm plakalar bu videoya özgü.
- Rakip ayrışması: Fred - Money Historian maskotu silindir şapka + takım elbise; Leo'da şapka/ceket/kravat yok (kabul listesinde), mekân ev mutfağı.
- Politika (P1): plakalarda bayrak, banknot, parti rengi, yüz yok; rakam/etiket yalnız KOD.

## Değerlendirme yöntemi (dalga dönünce)
Leo'lu: `tools/gorsel/tutarlilik.py` (taban a; kafa kor. ≥0,84) + `araclar/rig-yama.py` kafa bölgesi hizası + 4× yüz incelemesi · plaka/nesne: `araclar/stil-olcum.py` (düzlük ≥%50, doku ≤2,0 hedef), 2× kırpımda yazı taraması (Canny levha yoğunluğu) · kesme: `araclar/kes-m4.py` (saçak + kapalı delik listesi) · kontakt sayfası (sayfa + a + yeni + Leo bindirme).

## Dalga 1 değerlendirme (2026-11-02) — kontakt `kontakt-dalga1.jpg`
| Id | Karar | Ölçüm (komut → sonuç) |
|---|---|---|
| G01 mutfak A (C01 stil ref) | **KABUL, kazanan** | `stil-olcum.py` düzlük 64,1 / doku 0,92 / kontur 1,05 (Leo 71 / 0,57) → çizgi film; masa üstü y 810 (%75,0, sınırda); Leo arkası L medyan 77 vs gömlek 29; notlar 5 boş, yazı/tabela/bayrak yok |
| G02 mutfak B (referanssız) | ELENDİ | düzlük 63,7 / doku 0,96 (stil eşit); masa %73,6; orta alan daha sade (kenar 0,013 vs 0,027) ama Leo arkası L 67 → siyah gömlek zemine karışıyor |
| G03 zarf sayfası | **KABUL** | nesne başına M4 (kırpımla; tek görselde M4 en büyük bileşeni tutuyor): artık 0, saçak 0, delik yok; düzlük 88,6; yazı/pul yok |
| G04 zarfa bakar | **RED** | `tutarlilik.py` kafa kor. **0,70** (ten ΔE 3,9); kenar bindirmesi: kafa ölçeği büyümüş + aşağı kaymış, gözler yana-aşağı → rig ağızları oturmaz |
| G05 zarftan zarf çıkarır | **KABUL** | kor. 0,97, ΔE ten/saç/gömlek 1,5/1,1/2,0, merkez %0,1, faz korelasyonu kayması (−0,4; 0,4) px → rig ağız/göz yamaları aynı konumda; saat sol bilek; M4 artık 0,0004, saçak 0 (kol–gövde arası 3,3k px zemin cebi d_med 2,7 doğru olarak zemin) |
Girdi sha256 (ilk 12): G01 28a0004ed24c · G02 3c036a6eec14 · G03 c742a1859daf · G04 7b02f1d75a24 · G05 a56a7431dc3a.

**Bulgu:** düz çizgi film eki ("flat colors … NOT painterly, NOT photorealistic") referanssız bile boyamsı kaymayı önledi (1929 dönem plakaları düzlük 26–38 → burada 64). C01 stil referansı ek fark yaratmadı.

**animasyon-yonetmeni'ne (F5 kritik yol):**
- Plaka `canva-ham/G01.png`; masa üst kenarı y=810. Leo (`a` kesiği + rig) masanın ARKASINDA: Leo katmanını y<810'da maskele (gövde masa kenarında kesilir, eller masa altında).
- **Lamba çakışması:** lamba başlığı x≈780–1140, y≈30–245. Leo ölçek 0,82 ve ortada → kafa lambanın önüne biniyor (kontakt üst satır, kötü). Çözüm: ölçek ≤0,58 ortada (kafa lamba altında, ışık üstüne düşer) **veya** 0,82 ölçekte Leo merkezi x≤640 (sol üçte bir; buzdolabı notları sağda boş kalır, `c-isaret` ile işaret edilir).
- Matruşka: `leo/G05-zarftan-zarf.png` (kafa a ile hizalı → konuşma sürer) + `nesne/G03-zarf-kapali.png`, `G03-zarf-acik.png`, `G03-zarf-yigini.png`, `G03-kagit.png` (RGBA, KOD ölçek/tekrar; "INTEREST" vb. KOD yazı). G05'teki iç zarf ön (adres) yüzü düz kraft okunur. "Açar" anı için G04 yerine: KOD ile `G03-zarf-acik` açılış animasyonu + Leo `d-saskin`.

**G04 düzeltilmiş prompt (yalnız istenirse; önerilmez, tavandan 1 hak):** referans [MAHZHqW0_Uo, MAHZHpeQGdM], kart düzenleme kalıbı birebir + `ONLY CHANGE: he holds an open plain kraft-brown paper envelope with both hands at chest height, flap up, tilted slightly toward the camera so its empty inside is visible; his head, face, eye direction and mouth are exactly the same as in the first reference image (eyes look at the camera, mouth closed); torso stays in the same place; the envelope is completely blank with no writing; the black wristwatch on his left wrist stays visible. No text, no logos.` (Neden: "eyes glance down" modeli yüzü yeniden çizmeye itti; G05'te bakış kameraya → kor. 0,97.)

**Canva kullanımı:** 5 / tavan 12 (dalga 2 çekirdek 3 + seçmeli 2 → 10; tekrar payı 2).

## Dalga 2 değerlendirme (2026-11-02) — kontakt `kontakt-dalga2.jpg`
Girdi sha256: G06 4dcce72803fa · G07 c433103eb6f7 · G08 3a1f950bd346 · G09 47736b054221 · G10 491b73276e68. Stil (`stil-olcum.py`, düzlük/doku): G06 63,7/1,07 · G09 70,8/0,73 · G10 72,7/0,57 · G07 89,2/0,43 → hepsi G01 ailesi (tek stil).
| Id | Karar | Ölçüm |
|---|---|---|
| G06 kuşbakışı masa | **KABUL** | orta alan x560–1400 y320–1000 boş (Canny 0,0); kâğıtlar/zarf boş; üst ortada lamba başlığı (y 0–290) → KOD nesneleri y≥320 |
| G07 ev nesneleri | **KABUL** | nesne başına M4: artık 0–0,002, saçak 0; kart iç yüzü zemine yakın (d_med 10) → kapalı delik doğru dolduruldu; yazı/rakam/logo yok |
| G08 hesap makinesi | **RED** | `tutarlilik.py` kafa kor. **0,76** (ten 3,4, ölçek %3,4); kenar bindirmesi: kafa öne eğik, yüz uzamış — G04 ile aynı neden ("eyes glance down") |
| G09 dikey mutfak | **KABUL** | 1080x1920; masa üstü y 1151 (%59,9; hedef 58–66); lamba alt kenarı y≈560 |
| G10 buzdolabı | **KABUL** | not kutuları xywh: (823,203,201,204) (1333,210,196,197) (1079,337,193,194) (938,583,197,199) (1261,583,189,193); magnetler boş |

**G08b tek tekrar prompt'u (önerilen, 11/12; referans [MAHZHqW0_Uo, MAHZHpeQGdM], kart düzenleme kalıbı birebir):** `ONLY CHANGE: he holds a chunky pocket calculator in his left hand at chest height and taps it with his right index finger; his head, face, eye direction and mouth are exactly the same as in the first reference image (eyes look at the camera, mouth closed); torso stays in the same place; the calculator display is blank and the buttons have no markings; the black wristwatch on his left wrist stays visible. No text, no logos.` (G05'te bakış kameradayken kor. 0,97.) Yine kalırsa B planı: `a` + `nesne/G07-hesap-makinesi.png` KOD katmanı (masada), ek hak harcanmaz.

## animasyon-yonetmeni varlık listesi (S08, metinden bağımsız; tümü 1920x1080 tuval koordinatı)
| Varlık | Dosya | Kullanım / not |
|---|---|---|
| Mutfak ana plaka | `canva-ham/G01.png` | Leo masada konuşur; masa üstü y=810, Leo katmanı y<810 maskeli; lamba x780–1140 y30–245 → Leo ölçek ≤0,58 ortada veya 0,82'de merkez x≤640 |
| Dikey mutfak (Shorts) | `canva-ham/G09.png` (1080x1920) | masa üstü y=1151; Leo kafa üstü y≥580 (lamba altı); üst %15 / alt %35 sade |
| Kuşbakışı masa | `canva-ham/G06.png` | faturalar/zarflar/kart KOD ile y 320–1000, x 560–1400 |
| Buzdolabı notları | `canva-ham/G10.png` | not kutuları yukarıda; KOD yazı (ör. gelir/gider) ≤150 px satır |
| Leo zarftan zarf | `leo/G05-zarftan-zarf.png` | matruşka doruğu; kafa a ile hizalı → rig ağız/göz yamaları aynı konum |
| Zarflar | `nesne/G03-zarf-kapali.png`, `G03-zarf-acik.png`, `G03-zarf-yigini.png`, `G03-kagit.png` | matruşka tekrar/ölçek, kule, fatura etiketleri KOD |
| Ev nesneleri | `nesne/G07-kumbara.png`, `G07-kasa.png`, `G07-kart.png`, `G07-hesap-makinesi.png`, `G07-para.png` | gelir/birikim, borç, kredi kartı bölümü; ekran/kart boş (KOD rakam) |
| Konuşma + rig | `assets/karakter/paket-v1/a`, `b`; `uretim/2026-10-26-1929-1000-dolar/05-gorsel/rig/` (`rig-yamalar.json`, G=B) | tüm konuşan sahneler |
| Jestler (1929 kesikleri) | `uretim/2026-10-26-1929-1000-dolar/05-gorsel/leo/` c-isaret, d-saskin, e-dusunen, f-sevincli, C12, C13, C20, C21, C02, C04 | buzdolabına işaret (c), faiz tepkisi (d), "aile değil" (e), üç olasılık (C12), kapanış (C21) |
| (bekliyor) Leo hesap makinesi | G08b veya B planı | ölçek hesabı anı |
Özgünlük: sahne plakalarının tamamı (G01, G06, G09, G10) bu videoya özgü; önceki videodan yeniden kullanılan sahne görseli 0. Karakter kesikleri/rig muaf sınıf.
