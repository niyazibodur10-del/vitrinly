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
- 2026-10-26: paket-v1 kafa üst boşluğu dar (saç üstü y≈30–47) → punch-in olur, pan-up olmaz.
- 2026-10-27: Referanssız (ve C01 stil referanslı) dönem plakaları boyamsı çıktı (doku 2,6–5,2 vs Leo 0,6–0,9); Niyazi stil kararıyla kabul, kendi aralarında tek stil şart. Yürüme düzenlemesi yön tutmayabilir → sahneyi yöne uydur.
- 2026-10-27: Ara karar (ör. kazanan plaka) SubagentHandback yerine rapordaki erken karar satırına yazılıp yalnız o dosya commit+push. OCR yok → Canny kenar yoğunluğu + 2× kırpım.
- 2026-10-27: Büyük ara PNG'ler scratchpad'e (koordinatör repo'daki her şeyi commit edebiliyor).
- 2026-11-02 (S08 dalga 1–2 plan): Leo'yu oturtmak için yeni taban üretme; bel üstü rig + alt kenardan taşan masa plakası (masa üst kenarı %62–75) → 0 üretim, rig aynen. Kilit pozlarda "head stays in exactly the same place" → ağız yamaları konuşmaya devam eder.
- 2026-11-02: Matruşka/tekrarlı nesne anı = nesne sayfası (düz slate-blue zemin, 4–5 nesne tek üretim) + KOD tekrar/ölçek; metin RED'i görseli bozmaz. Yeni plaka stilinde "NOT painterly" eki 2 adayla (C01 ref / ref yok) ölçülerek denenir — sonucu bu satıra işle.
- 2026-11-02 (S08 dalga 1): "NOT painterly, NOT photorealistic" eki referanssız da çizgi film verdi (düzlük 64 vs 1929 dönem 26–38) → plaka kilidine kalıcı. Düzenlemede "eyes glance down" yüzü yeniden çizdirdi (kor. 0,70); bakış kamerada kalsın (G05 0,97).
- 2026-11-02: Nesne sayfasında kes-m4 yalnız en büyük bileşeni tutar → nesne başına kırpıp kes. Plaka seçiminde Leo bindirmesi şart: siyah gömlek arkası L farkı (77 vs 67) ve lamba/kafa çakışması yalnız bindirmede görünür.
- 2026-11-02 (S08 dalga 2): "eyes glance down at X" ikinci kez yüzü yeniden çizdirdi (G08 0,76, G04 0,70) → Leo düzenlemelerinde bakış her zaman kamerada, "head, face, eye direction and mouth exactly the same as the first reference" yaz.
