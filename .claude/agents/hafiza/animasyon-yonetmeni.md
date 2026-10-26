# animasyon-yonetmeni — hafıza

## Kurallar
- Rhubarb: GitHub sürüm indirmesi ağda kapalı → kaynak koddan derlenir (`tools/kurulum.sh`; CMake 3.28'de CMP0167 politikası koşullu yapılmalı). İngilizce, PocketSphinx, `--dialogFile` ile metin.
- Senkron testi `tools/senkron-testi.py` + `AgizTest` kompozisyonu (9 ağız yüz üzerinde) her teslimde zorunlu; kapı ≤2 kare.
- Hugging Face `trust_remote_code` gerektiren modeller YASAK (güvenlik); yerel ağırlık + bilinen kütüphane (ör. spandrel ile Real-ESRGAN).
- Render tarayıcısı Google Fonts sertifikasına güvenmiyor → fontlar yerel (`video/public/fonts`).
- Ses normalizasyonu render sonrası son stereo dosyada (`tools/render-son.sh`).

## Dersler
- 2026-10-26 (pilot v1, 18.8 sn, 1920x1080, 30 fps, Remotion 4.0.539): dudak senkronu en iyi gecikme 1 kare (33 ms) ✅; blackdetect 0 ✅.
- 2026-10-26: Vektör çizim ağızlar senkron için yeterli ama çizim stiliyle %100 uyumlu değil → karakterin kendi ağız görselleri (E1–E9) gelince değiştir.
- 2026-10-26: Karakter görseli düşük çözünürlüklü sayfadan ×4 büyütüldü (Real-ESRGAN) → yakın planda yumuşak; ≥2048 px tek görsel olmadan yakın plan kullanma.
- 2026-10-26: GrabCut kesme (`tools/karakter/kes.py`) + renk tabanlı kenar temizliği çalıştı, ama bölge koordinatları görsele özel; yeni görselde yeniden ayarlanmalı (artık bu iş gorsel-varlik-sanatcisi'nde).
- 2026-10-26: Tek görselden kol/el hareketi yapılamıyor; jest pozları (E11–E14) ayrı parça olarak gerekli.
- 2026-10-26 (pilot v2): v1 yanlış sesle (Niyazi okuması) render edilmişti. **Render öncesi `video/public/*-ses.wav` kaynağını kontrol et**: karar verilen anlatıcı mı (am_fenrir 0.9), müzik/efekt miksi var mı. Ses değişince PILOT_SURE, sahne sınırları ve kelime tetikleri (`KELIME` sabiti) yeniden hesaplanır; sabit sayı gömme.
- 2026-10-26: Rhubarb'ı müzikli miks yerine temiz anlatım (+müzik girişi kadar baş boşluğu) üzerinde çalıştır: senkron korelasyonu 0.52 vs 0.40 (ikisi de 1 kare gecikme).
