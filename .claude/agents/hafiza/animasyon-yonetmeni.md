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
- 2026-10-27 (1929 tam video, 24 sahne + 7 dikey + 2 Shorts ek): **Sahne zamanlarını kelime çapasıyla yaz** (`anlar("S05")("ordinary")` — n'inci geçiş, bulunamazsa hata fırlatır); sabit saniye yok → TTS/ses değişince kod kendini günceller, eksik kelime ilk still'de patlar. Aynı çapalar `agiz-gorunur.py` ve `efekt-cue.py`'de (senkron aralıkları + müzik cue'ları) tek formülden.
- 2026-10-27: **Ölçek + konum hatası:** `left = x − yüz·s` hesaplayıp `transformOrigin`'i (0,0) dışında bırakmak s≠1'de figürü kaydırıyor (s=0.42'de Leo ekrandan çıktı). Kural: konum ölçeği origin 0 0; poz "oturma" pop'u iç div'de kendi origin'iyle.
- 2026-10-27: **Kamera kenar koruması** Kamera bileşeninde zorunlu (odak [ekranW/2s, w−ekranW/2s] aralığına kısılır); elle odak verirken plakanın dışı siyah göründü (C19 fx 1300, s 1.02).
- 2026-10-27: Kare denetimi için `video/scripts/kare-ornek.mjs` (tek bundle + tek tarayıcı, renderStill) — 210 kare ≈ 4 dk; CLI `remotion still` kare başına ~6 sn. Her 3 sn'de bir kare + 4'lü kontakt sayfası, iki ofsetle (45 ve 80. kare) → yerleşim çakışmalarını (yazı/levha, yazı/altyazı, Leo/grafik) yakaladı.
- 2026-10-27: Grafikte çift eksen yok (dataviz): Dow + $ değeri → çizgi + ayrı sayaç kartı; TÜFE + alım gücü → çizgi kartı, sonra ayrı "BUYS LIKE" kartı. Kapı renkleri grafikte validator'dan geçen tonla (#3b8de0/#2fae6a/#d9772e, yüzey #0f1626); CVD taban bandı → her seri doğrudan etiketli. Ara verisi olmayan Dow çapaları kesikli çizgiyle ve "anchors only" notuyla.
- 2026-10-27: Rig uyumlu pozlar (kafa a ile hizalı): a, b, C12, C13, C14, C21 (+b-alt ağız, göz kırpma yok). İfade pozları (c, d, e, f, C20) konuşan sunucuda kullanılmaz; klonlarda/dış seste serbest. Konuşan sunucu ölçeği ≤1.1 (kaynak 1680 px).
- 2026-10-27: 9:16 için C22 dikey stüdyo, kapıları yığmaktan (16:9 kırpım + x4) daha iyi: kapılar yan yana okunuyor. Güvenli alan: üst 192, alt 1536, sağ 918 px.
