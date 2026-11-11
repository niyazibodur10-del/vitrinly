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
- 2026-11-02: freezedetect (−60 dB, 1 sn) son anahtar kareden sonra duran kart/kamerayı yakalar (tur 1: 19) → Kamera ve grafik zeminine %0,35/sn sürekli itme varsayılan; dikey zemin dahil. Tam render 4 vCPU ≈ 65 dk (12 parça) — kapıdan önce kare kontağıyla bitir, iki tur render pahalı.
- 2026-11-04 (S03 miras iskelet): 31 sahnede elle bileşen yerine **kesme listesi → çekim anahtarı ("ad:param") tek çatı** (`sahneler.tsx` Cekim) + kodla grafik kütüphanesi; 9:16 aynı çekimler `useDikey`. Rakamlar `grafik-veri.py` assert'iyle (R satırında yoksa çıkmaz).
- 2026-11-04: Her kesme +0,9 sn kontak (`kare-listesi.mjs` + kare-ornek, 123 kare ≈3 dk) ≤1 sn giriş ihlallerini yakaladı (4) → grafik başlığı/çerçevesi daima kesme anında (t0) girer, değer kelimede. "U.S."/"U.K." 160 kpm tahmininde cümle bölüyordu → korunur.
- 2026-11-05 (S03 kritik): Canva Leo kesiklerinde ağız yaması hizası yok → konuşma = rig (aynı karakter), Canva Leo yalnız yüzü kadraj dışı aksiyon kesitinde (clipPath ile el+nesne). Ek kayıt .txt'lerinde telaffuz bağlantısı `[x](/ipa/)` var → Rhubarb öncesi ayıkla. Render başladıktan sonra kod düzeltmesi = render'ı durdur, yeniden başlat.
- 2026-11-09: render-parca `--oto-yok` iz kaydetmez → sonraki oto koşu "0 değişen" der ve eski parçaları birleştirir; kod değişince `--yeniden <parça>` (olay karesi//1800) ver. Kadans boşluğu için punch-in olayı (tur "kamera") zaman.ts'te — cue ile görüntü aynı kaynaktan.
- 2026-11-10 (S03 R1): kurgu katmanı (S21Vurgu oku) ile sahne grafiği ayrı dosyada → dikey kare kontağı **final kompozisyondan** (KMirasShorts2) alınır, sahne kompozisyonundan değil; ölçüm = etiket piksellerinin sağ kenarı vs ok x (982→822).
- 2026-11-10: Plan "KOD" dediği nesne yüzü (pano) boş kalmasın → poz görüntü uzayında (Sunucu içi) katman, kâğıt kutusu pikselden ölçülür; yakın planda alt satırlar altyazı bandına (ekran y ≥920) düşmesin diye liste kâğıdın üstüne sıkıştırılır.
- 2026-11-11 (Flip By Vote B001): Dikey dizi = çekim çatısı (`Cekim.tsx` + `mekan-l1.ts`), bölüm yalnız kesme tablosu; 85 sn render 3,3 dk, tek turda geçti. Ağız senkronu **render pikselinden** ölç (`uretim/seri/bolum-001/animasyon/agiz-piksel-senkron.py`, kutuyu karede çizip doğrula: ilk kutu çeneye düştü, r 0,1).
- 2026-11-11: Kodla göz kırpma: maske-PNG ve elips "boş göz" yapar → badem klip + kapalıda tam dolgu + kirpik kavisi; ten rengi göz altından değil yanaktan. Disk dar: bundle 585 MB → `scripts/bundle-kaydet.mjs` ile bir kez, paylaşılan /tmp'yi süpürme.
- 2026-11-11 (B001 tur 2, hakem KALDI): altyazı yazısı daima kilitli metinden (LCS; Whisper yalnız zaman). Göz kapağı = göz altı derisinin aynası + gölge + kontur kirpik; yakın ≥1,15 ve kancada kırpma yok. Saç halesi: kenar bandında renk-dışı pikselleri sil (`sac-hale-temizle.py`). Rozet/kart yüz çakışmasını kutu kesişimiyle ölç.
- 2026-11-11 (ses değişimi, 2 sa sınır): mutlak zamanlı kesme tablosu `animasyon/zaman-esle.py` (eski→yeni kelime çapası) ile 20 dk'da taşındı; sonraki bölümde zamanları baştan satır/kelime çapasıyla yaz.
