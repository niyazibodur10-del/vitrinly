# gorsel-varlik-sanatcisi — hafıza

## Kurallar
- Leo tutarlılığı = taban + "EDIT … ONLY CHANGE …" (ref [taban, sayfa MAHZHpeQGdM]); kafa kor. 0,84–0,96. Sıfırdan kilit prompt → 0,45 (yasak).
- Prompt paketi elle yazılmaz: kilitleri karttan birebir alan `prompt-uret.py` + negatif kontrollü `prompt-kontrol.py` (son sürüm `uretim/2026-10-28-yeni-video/05-gorsel/araclar/`).
- Katmanlı plan: karaktersiz plaka + Leo kesiği + KOD yazı/rakam. Leo'lu sahne illüstrasyonu yok (yüz kayar, dudak senkronu olmaz).
- Düz zeminde kesme = M4 v2 (`araclar/kes-m4.py`: Lab anahtar + arındırma + kapalı delik d_med>6 doldur); raporda saçak + kapalı delik listesi zorunlu.
- Rig yaması = fark maskesi +11 px, Gauss 4,5, 6 px rampa (`rig-yama.py`); hiza şekli doğrulamaz → 4× ağız yakın planı göz incelemesi şart. G=B kalıcı ('f/v' 2 denemede çizilmedi).
- Tam boy indirme `tools/gorsel/canva-indir.md` (doğal 1680x944). Ölçüm `tools/gorsel/tutarlilik.py` (düz zemin); stil vekili `stil-olcum.py`.
- Önce ucuz deterministik düzeltme (ten Lab eşleme `ten-esle.py`, Reinhard `sepya-esle.py`), sonra hak harca. Aynalama yasak (saat sağa geçer).
- Plaka/prop'ta yazı yasağı + "no man in a black shirt"; sayfa referansı plakaya Leo sokar → plakalar sayfasız.

## Dersler
- 2026-10-26: Kaynak sayfa çözünürlüğü düşük; ≥2048 px yakın plan için ESRGAN x4 (spandrel, yerel, `trust_remote_code` yasak) yine yumuşak.
- 2026-10-26: "talking/mouth open" gülümseme üretir; şekli tarif et ("tall oval 'aah', NOT smiling"). Canva 5 paralel iş sorunsuz, iş başı 20–40 sn.
- 2026-10-27: Referanssız (ve C01 stil referanslı) dönem plakaları boyamsı çıktı (doku 2,6–5,2 vs Leo 0,6–0,9); Niyazi stil kararıyla kabul, kendi aralarında tek stil şart. Yürüme düzenlemesi yön tutmayabilir → sahneyi yöne uydur.
- 2026-10-27: Ara karar (ör. kazanan plaka) SubagentHandback yerine rapordaki erken karar satırına yazılıp yalnız o dosya commit+push. OCR yok → Canny kenar yoğunluğu + 2× kırpım.
- 2026-10-27: Büyük ara PNG'ler scratchpad'e (koordinatör repo'daki her şeyi commit edebiliyor).
- 2026-11-02 (S08 dalga 1–2 plan): Leo'yu oturtmak için yeni taban üretme; bel üstü rig + alt kenardan taşan masa plakası (masa üst kenarı %62–75) → 0 üretim, rig aynen. Kilit pozlarda "head stays in exactly the same place" → ağız yamaları konuşmaya devam eder.
- 2026-11-02: Matruşka/tekrarlı nesne anı = nesne sayfası (düz slate-blue zemin, 4–5 nesne tek üretim) + KOD tekrar/ölçek; metin RED'i görseli bozmaz. Yeni plaka stilinde "NOT painterly" eki 2 adayla (C01 ref / ref yok) ölçülerek denenir — sonucu bu satıra işle.
- 2026-11-02 (S08 dalga 1): "NOT painterly, NOT photorealistic" eki referanssız da çizgi film verdi (düzlük 64 vs 1929 dönem 26–38) → plaka kilidine kalıcı. Düzenlemede "eyes glance down" yüzü yeniden çizdirdi (kor. 0,70); bakış kamerada kalsın (G05 0,97).
- 2026-11-02: Nesne sayfasında kes-m4 yalnız en büyük bileşeni tutar → nesne başına kırpıp kes. Plaka seçiminde Leo bindirmesi şart: siyah gömlek arkası L farkı (77 vs 67) ve lamba/kafa çakışması yalnız bindirmede görünür.
- 2026-11-02 (S08 dalga 2): "eyes glance down at X" ikinci kez yüzü yeniden çizdirdi (G08 0,76, G04 0,70) → Leo düzenlemelerinde bakış her zaman kamerada, "head, face, eye direction and mouth exactly the same as the first reference" yaz.
- 2026-11-04 (S03 dalga 1 plan): Thumbnail Leo'su ayrı üretilmez → video düzenleme pozu (kafa sabit) + thumb-uret kafa değişimi; thumbnail Canva 0. Metin kostüm isterse (yelek) kart kilidi kazanır, rol nesneyle (pano/bant) anlatılır.
- 2026-11-04: Tekrarlayan set aracı (kamyon) = tek nesne sayfası + KOD hareket; plakaya gömülü sürüm yalnız kilit sahnede 2. aday. Negatif kontrolde sed kalıbı prompt'a birebir uymazsa sahte GEÇTİ → `cmp` ile değişikliği doğrula.
- 2026-11-05 (S03 dalga 1a): Kafa-sabit + "eyes looking straight at the camera" kalıbı 4/4 geçti (kor. 0,87–0,92, kayma ≤1,4 px; kol yukarıda M07 dy +5 → ofset). Kasa içi gibi ahşap/doku isteyen plakada referanssız prompt resimsi çıktı (kontur 0,06) → stil-olcum'a kontur ≥1,0 ekle, çizgi film nesne sayfasını referans ver.
- 2026-11-05: Kafa değişiminde maske alt sınırı sert kesilirse çene altında ton basamağı → 40 px rampa (`kafa-degis.py`). Elli ifade kafası (e-dusunen) taşınmaz: el kolsuz kalır.
- 2026-11-05 (S03 dalga 1b/2): Zemine yakın pastel/lila nesne M4'te silinir → dışbükey zarf köşe keser; dikdörtgen dolgu + ΔE<12 zemin temizliği çalıştı. Yapraklı dış mekân plakaları düzlük 43–47 verir (boyamsı değil) → "tolere" yaz, son hakkı harcama. Hook entegre plaka kesik bindirmeden iyi (gece ışığı).
- 2026-11-10 (seri tur 2): "eyes toward frame-right" iki tabanda da sola baktı → yönü prompt'a bırakma, asimetrik kimlik öğesi olmayan karakteri aynala. Lacivert giysi + slate-blue zemin M4'ü bozar (ΔE 7,6) → `uretim/seri/karakter/araclar/kes-gc.py`; sonraki tabanlarda zemin rengi giysiye zıt seçilsin. Yarı ağız = DIS akış ara karesi (`agiz-yama.py`); sayfa portresi tezgâh arkasına konmaz, yalnız ekstrem yakın plan.
- 2026-11-11 (seri AG): kafa-sabit EDIT 3D'de de tuttu (fark %0,56, bölge dışı ≤%0,24) → ağız yamasında `--siluet` zorunlu (yama kutusu ham zemini taşır). Rhubarb C/E açık, B/F/G/H yarı, X/A kapalı → yarı %60, açık %33.
- 2026-11-11 (Z3b): saçağa yalnız ab boyamak (L korunur) kızıl/bordo leke yapar → yasak. Kenar = yabancı piksel sil + alfa kapama/açma + kontur σ5 (saç) + en yakın temiz iç rengi (`uretim/seri/karakter/araclar/ifade-kenar.py`); teslim öncesi 1:1 yeşil kırpım zorunlu.
