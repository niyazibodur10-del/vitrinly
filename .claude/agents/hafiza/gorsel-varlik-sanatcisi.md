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
- 2026-10-27 (1929-1000-dolar F4 plan): Düz zeminli Canva pozlarında kesme kazananı **M4 = Lab renk anahtarı (köşe zemin rengi, ΔE rampa 14–30) + kenar arındırma (un-premultiply)**: kenar artığı 0.000–0.001, saçak 0. GrabCut saç uçlarında mavi saçak bırakıyor (artık 0.13–0.18). Betik `uretim/2026-10-26-1929-1000-dolar/05-gorsel/hazirlik/kes-test.py`; eski `tools/karakter/kes.py` düz zemin için gereksiz.
- 2026-10-27: Delik doldurmada `floodFill(0,0)` bel üstü kadrajda kol–gövde arası zemini de doldurur (kollar alt kenara değiyor) → yalnız kenara değmeyen ve <400 px delikleri doldur. "Saçak" ölçümü (alfa>0,5 iken zemine ΔE<12) bu hatayı 9.240 px ile yakaladı: her kesme betiğinde bu ölçüm zorunlu.
- 2026-10-27: Az Canva hakkıyla tutarlılık = **katmanlı plan** (karaktersiz plaka + Leo kesiği + KOD grafik). 24 sahne → çekirdek 19 üretim (8 plaka, 5 kritik yol, 6 rig kanal varlığı), seçmeli 3. Leo'lu sahne başı illüstrasyon elendi (yüz kayar, dudak senkronu olmaz). Klonlar = aynı kesik + KOD yaka kartı.
- 2026-10-27: Prompt paketini elle yazma: kilit blokları karakter kartından birebir alan üretici (`05-gorsel/araclar/prompt-uret.py`) + denetim betiği (`prompt-kontrol.py`, negatif kontrolle) → kilit kayması sıfır. Plaka prompt'larına "no man in a black shirt" + harf/rakam/tabela yasağı. Varsayım (C01'de doğrulanacak): sayfa referansı plakaya Leo'yu sokar → plakalar referanssız.
- 2026-10-27: a↔b kesik farkı yalnız ağız/çene kutusunda (x 866–1023, y 303–414; dışı ince kontur gürültüsü) → rig ağız yaması güvenli. ESRGAN 160² kırpım 38,8 sn duvar (yükleme dahil); büyük ara PNG'leri scratchpad'e yaz — koordinatörün ara kaydı repodaki her şeyi commit edebiliyor.
