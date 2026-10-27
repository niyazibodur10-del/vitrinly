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
- 2026-10-27 (1929 F5 kritik yol, K1929Kritik 19,7 sn): **Rig yamalarının alfasını taban kesiğin silüetiyle çarp** — Canva yama kutuları çene/kulak kenarında zemin pikseli taşıyor, AgizTest'te mavi hale yaptı. Bel üstü pozlar (a, b, C12…) aynı kadrajdaysa yamalar dikişsiz geçer; **c-isaret gibi paket-v1 pozları kafa hizasında değil** → yalnız konuşmasız anlarda. Poz uyumunu yama öncesi kafa bölgesi farkıyla ölç (C12 8–13 / c 35–56).
- 2026-10-27: Rhubarb cümle sonunda ağzı sessizlikte 5–8 kare açık tutuyor → **sessizlik kapısı** (≥100 ms sessizlik = X; `07-animasyon/sessizlik_kapisi.py`) her çizelgeye uygulanır. Rhubarb'ı **tam sahne** üzerinde çalıştır, sonra kes.
- 2026-10-27: `senkron-testi.py` kısa pencerede yanıltıcı: aynı çizelge S04 tam sahnede 0, 62–70 sn penceresinde −5 (Whisper da orada 0,13–0,25 sn geç). 5 aday (parça/boşluk/tam sahne/phonetic) hep −5 → araç değil bölge. Kapıyı **ekranda ağzın göründüğü aralıklarda + tam sahnede** ölç; tek parçalı test videosu seçerken konuşan yakın planı bu tür bölgeye koyma.
- 2026-10-27: Tek yürüme pozu + adım zıplaması (2 adım/sn, |sin| zıplama 9 px, ±1,4° eğim, %1,2 ezilme-uzama, varışta 0,2 sn oturma) klon yürüyüşünü okunur kılıyor; poz değiştirerek adım (C04↔C02) yerinde kayma yapar. Kesikler sola yürüyorsa sağdan gir, aynalama yok (saat bileği).
- 2026-10-27: Test render 591 kare 4 vCPU'da 78 sn (≈7,6 kare/sn). Kare-kare fark taraması (320x180 gri, eşik max(6×medyan,8)) titreme/plansız sıçrama için hızlı ve yeterli; sıçramaları planlı kesmelerle eşle.
