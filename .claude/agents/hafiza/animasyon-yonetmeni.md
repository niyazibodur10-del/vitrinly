# animasyon-yonetmeni — hafıza

## Kurallar
- Rhubarb kaynaktan derlenir (`tools/kurulum.sh`); İngilizce, PocketSphinx, `--dialogFile`; **temiz anlatım + tam sahne** üzerinde çalıştır, sonra kes; her çizelgeye sessizlik kapısı (≥100 ms = X, `tools/animasyon/sessizlik_kapisi.py`).
- Senkron kapısı: `tools/senkron-testi.py --araliklar agiz-gorunur.json --bant 700-3000` (ağız görünür aralıklar + tam sahne) + `AgizTest` karesi; ≤2 kare. <1,5 sn aralık güvenilmez → komşusuyla oku. Konuşan yakın planı Whisper'ın geç olduğu bölgeye koyma.
- Render öncesi `video/public/*-ses.wav` kaynağını kontrol et (am_fenrir 0.9). Sahne zamanları **kelime çapasıyla** (`anlar("S05")("word")`), sabit saniye yok; aynı çapalar agiz-gorunur + efekt-cue'da.
- Rig: yama alfası taban kesik silüetiyle çarpılır; konuşan sunucu yalnız kafası a ile hizalı pozlarla (a, b, C12, C13, C14, C21), ölçek ≤1.1; ifade pozları konuşmasız anlarda.
- Ölçek+konum: transformOrigin 0 0 ile konumla; pop iç div'de. Kamera kenar koruması zorunlu (odak plakada kısılır).
- Geçişin arkasında daima içerik; boş kare blackdetect düşürür. Düzeltme turunda `render-parca.sh` yalnız değişen parça.
- Kare denetimi `video/scripts/kare-ornek.mjs` (3 sn'de bir, iki ofset, kontakt) — yazı/levha/altyazı/Leo çakışmalarını yakalar. Kare-fark taraması (320x180 gri, eşik max(6×medyan,8)) sıçrama için.
- Grafik: çift eksen yok; renkler #3b8de0/#2fae6a/#d9772e, yüzey #0f1626; her seri doğrudan etiketli; ara verisi olmayan çapalar kesikli + not.
- 9:16: dikey stüdyo plakası kırpımdan iyi; güvenli alan üst 192, alt 1536, sağ 918 px.
- Hız ölçüsü: render ≈5,4–7,6 kare/sn (4 vCPU); still CLI ~6 sn/kare → toplu bundle.

## Dersler
- 2026-10-27: Yürüyüş tek poz + zıplama (2 adım/sn, |sin| 9 px, ±1,4°, %1,2 squash, varışta 0,2 sn oturma) okunur; poz değiştirerek adım kayma yapar. Aynalama yok (saat bileği).
- 2026-10-26: Tek görselden kol/el hareketi olmaz → jest pozları ayrı parça; düşük çözünürlüklü büyütülmüş kaynakla yakın plan yapma (≥2048 px).
- 2026-11-02 (S08 KButce): **Tek kaynak `zaman.ts`** (saf TS; sahne kodu + `olay-cikar.mjs` esbuild ile cue/ağız aralığı üretir) — 3 ayrı formül (sahne/agiz-gorunur/efekt-cue) yerine; `yap()` kesme sırası denetimi + `"five|$5"` alternatif çapa. Ses gelmeden ham TTS cümle zamanıyla tüm çapalar doğrulandı.
- 2026-11-02: Tek Leo düzenleme görseli (G05) kraft piksel tonuyla (H 24–46°, ten hariç) iki renge boyanınca matruşka konuşan yakın planda çözüldü; yeni Canva hakkı gerekmedi. Plaka yazıları yakın planda kadraj dışına taşar → yazılar ekran uzayında.
