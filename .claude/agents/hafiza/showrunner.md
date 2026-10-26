# showrunner — hafıza

## Kurallar

## Dersler
- 2026-10-26 (günlük video akışı tasarımı): Tahmin yerine tek ölçülebilir adımı ölç → `Pilot` render 18,8 sn = 110,7 sn (~5,5× gerçek süre, 4 vCPU); 12 dk video ≈ 66 dk render. Kapasite tablolarını [Ö]/[H]/[T] ayrımıyla yaz.
- 2026-10-26: Akış yazmadan önce paralel çalışan ajanların yeni dosyalarını kontrol et (`git status`). `tools/yayin/` şeması video başına ayrı paket (`tur: uzun|shorts`) istiyordu; kendi uydurduğum birleşik JSON şemasını araca uydurmak zorunda kaldım. Sözleşme aracın `SEMA`sıdır.
- 2026-10-26: Kritik yol ~9–18 saat [T], 1 numaralı darboğaz animasyon sahne kodlaması (F5). Haftada 3'e geçmeden önce sahne şablon kütüphanesi + 60 sn P2 uçtan uca test şart; geçiş planı 1 → 2 → 3/hafta.
- 2026-10-26: 12 dk 1080p video ≈ 450 MB [H] → git'e girmez (100 MB sınırı). Teslim depolaması her planda baştan çözülmeli.
- 2026-10-26: Ajan-adı denetim betiği ilk sürümde tek kelimelik adları (hakem, showrunner) kaçırdı → betiği her zaman bir negatif testle (sahte ajan adı) sına.
