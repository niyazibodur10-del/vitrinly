# gorsel-varlik-sanatcisi — hafıza

## Kurallar

## Dersler
- 2026-10-26 (devralınan, pilot): karakter sayfası 1254x1254 / 2D sayfa 1536x1024; tek poz ~100x300 px → ×4 büyütme bile yakın planda yumuşak. Yüksek çözünürlüklü tek görseller (E0, E1–E9 ağızlar, E11–E14 jestler) Niyazi'den/üretimden gelmeli.
- 2026-10-26: GrabCut (`tools/karakter/kes.py`) bulanık arka planlı büste iyi çalıştı; sağ kenarda renk tabanlı temizlik (`kenar-temizle.py`) gerekti. Koordinatlar görsele özel.
- 2026-10-26: Real-ESRGAN x4 (spandrel, yerel ağırlık) güvenli; `trust_remote_code` isteyen modeller yasak.
