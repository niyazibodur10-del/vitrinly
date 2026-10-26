# gorsel-varlik-sanatcisi — hafıza

## Kurallar

## Dersler
- 2026-10-26 (devralınan, pilot): karakter sayfası 1254x1254 / 2D sayfa 1536x1024; tek poz ~100x300 px → ×4 büyütme bile yakın planda yumuşak. Yüksek çözünürlüklü tek görseller (E0, E1–E9 ağızlar, E11–E14 jestler) Niyazi'den/üretimden gelmeli.
- 2026-10-26: GrabCut (`tools/karakter/kes.py`) bulanık arka planlı büste iyi çalıştı; sağ kenarda renk tabanlı temizlik (`kenar-temizle.py`) gerekti. Koordinatlar görsele özel.
- 2026-10-26: Real-ESRGAN x4 (spandrel, yerel ağırlık) güvenli; `trust_remote_code` isteyen modeller yasak.
- 2026-10-26 (Canva): `generate-image` yalnız media id verir; thumbnail URL imzalı (boyut değişince 403). Tam boy yolu: çalışma tuvali `DAHZHv3mU9w`'ye `add_page`+`insert_fill`+commit → `export-design png 1920x1080` → hemen curl. Doğal boyut 1680x944 (1920 = yeniden örnekleme). Adımlar `tools/gorsel/canva-indir.md`.
- 2026-10-26: Tutarlılık için kazanan = taban poz + "EDIT … ONLY CHANGE …" (referans [taban, karakter sayfası]). 6 düzenlemede kafa hist kor. 0.84–0.96, gövde piksel hizalı (%0,2). Sıfırdan aynı kilit prompt → kor. 0.45, yüz değişiyor. Her yeni sahne/poz bir tabandan düzenlenmeli.
- 2026-10-26: "talking/mouth open" gülümseyen ağız üretir; dudak senkronu için şekli tarif et ("tall oval 'aah', NOT smiling"). Canva'da bir ifade/poz düzenlemesi ~20–40 sn, paralel 5 iş sorunsuz.
- 2026-10-26: Ölçüm `tools/gorsel/tutarlilik.py` (düz arka plan maskesi + ten/saç/gömlek Lab ΔE + kafa HSV hist kor.) negatif kontrolle doğrulandı (gömlek/ten-saç rengi bozulunca KALDI). Sahne görsellerinde (dolu arka plan) maske çalışmaz → yüz kırpıp karşılaştırma gerekir.
- 2026-10-26: Paketin kafa üst boşluğu dar (saç üstü y≈30–47/1080); kamera punch-in için yeterli, pan-up için değil. Gerekirse tabanı "more headroom" ile yeniden üret.
