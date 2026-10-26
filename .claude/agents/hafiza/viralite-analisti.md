# viralite-analisti — hafıza

## Kurallar
- Hesap yalnız `tools/viralite.py` ile; ağırlıklar betikte tek yerde (`OLCUTLER`), doküman tablosu onunla aynı olmalı; ağırlık toplamı 1.00 assert.
- Model v0.1'in tüm ağırlıkları TAHMİN [T]; güven DÜŞÜK, ±0.05 belirsizlik; 0.3 puandan küçük sıralama farkı anlamsız.
- "Somut özne yoksa merak ≤6" tavanı ağırlıklandırmadan önce uygulanır.

## Dersler
- 2026-10-26 (v0 → v0.1): kalibrasyon verisi rakip-analizi v1 (5 global kanal, ≈6 outlier, üçüncü taraf/arama özeti). Kanıtlı talep ağırlığı 0.15 korundu, ölçüm yerel medyan tabanına alındı.
- 2026-10-26: Yeniden kalibrasyon tetikleri: (1) YouTube API ile rakip verisi → outlier'ların ölçüt puanlarıyla korelasyonu; (2) kendi kanalımızda ≥5 video → tahmin/gerçek sıralama karşılaştırması, ≥10 videoda ağırlık ayarı; her kalibrasyon sürüm artırır (v0.2…).
