# Üretim hattı testi (2026-10-26, uretim-muhendisi)

Niyazi'nin "her işlemi kontrol et, testini yap" isteği üzerine bu konteynerde hattın her aracı küçük girdiyle gerçekten çalıştırıldı.
Etiketler: **[Ö]** bu konteynerde ölçüldü, **[H]** ölçümden hesap, **[T]** tahmin.
Ortam: 4 vCPU, 15,7 GB RAM, takas yok, disk 252 GB (20–23 GB boş), Remotion 4.0.539, Python 3.13 (venv) + 3.12 (kokoro-venv).
**Ölçüm notu:** testlerin bir kısmında başka ajanlar aynı 4 çekirdekte paralel iş yapıyordu (kanal görselleri betiği %150 CPU).
Bu yüzden süreler aralık olarak verildi: düşük değer = CPU boşken, yüksek değer = paralel yük altında.
Test çıktıları repo dışında: `/tmp/claude-0/.../scratchpad/hat-testi/`.

## Test tablosu

| # | Araç | Komut (özet) | Sonuç | Süre [Ö] | Düzeltme |
|---|---|---|---|---|---|
| 1a | `tools/kurulum.sh` (sıfırdan) | `ARAC_DIZINI=/root/kt3 tools/kurulum.sh` | ✅ exit 0, Kokoro dahil, TTS üretti | 231–237 sn | **Kokoro ortamı eklendi** (python3.12 venv, torch CPU, `kokoro==0.9.4`, `misaki[en]==0.9.4`, spaCy `en_core_web_sm` önceden kurulu, HF ağırlıkları önceden indiriliyor); Whisper medium.en + small.en önceden indiriliyor; Rhubarb derleme çıktısı log'a |
| 1b | `tools/kurulum.sh` (ikinci kez) | `tools/kurulum.sh` | ✅ idempotent | **1,7–1,9 sn** (önce 14,3 sn, ilk sürümde her seferinde `npm ci` ~20 sn) | `npm ci` yalnız package-lock değişince (damga `node_modules/.kurulum-kilit`); paket kontrolü import yerine `find_spec` |
| 1c | kurulum: uzun yol | scratch altındaki 93 karakterlik `ARAC_DIZINI` | ❌ → ✅ | — | espeak-ng veri yolu ~160 karakterde kesiliyor: Kokoro `phontab: No such file` verdi (yol 174 karakter). Kısa yolda çalıştı. Betik artık uzun yolu baştan reddediyor |
| 2a | `tools/ses/tts.py` am_fenrir 0.9 | 3 cümle (46 kelime) | ✅ 18,5 sn ses | 27–28 sn (model yükleme ~12 sn dahil) | — |
| 2b | `tts.py` 1 dk | 10 satır, 159 kelime → 60,3 sn ses | ✅ | 42 sn boşta / 80 sn yük altında (sentez RTF 0,5 / 1,1) | — |
| 2c | `tools/ses/tts-son.sh` | ham → 48 kHz mono + m4a | ✅ −14,2 LUFS, TP −1,5 dBTP, LRA 2,1 (m4a −14,2 / −1,4) | 3,1 sn | — |
| 3a | `tools/ses/temizle.sh` | pembe gürültü eklenmiş kayıt | ✅ −25,6 → −14,2 LUFS, TP −1,0, 48 kHz mono | 3,3 sn | Başlıktaki eski yol (`tools/ses-temizle.sh`) düzeltildi |
| 3b | `tools/ses/yaziya-dok.py` | 60 sn TTS, medium.en / small.en | ✅ kelime zamanlı JSON | medium 61–112 sn, small 26–40 sn | — (small ile medium kelime başlangıç farkı ort. 40 ms, p95 80 ms; WER aynı) |
| 3c | `tools/ses/hata-orani.py` | pilot + 60 sn TTS | ❌ → ✅ WER %2,5 → %0 | 0,04 sn | Sayı normalizasyonu: "one hundred and fifty" ↔ "150" sahte hata sayılıyordu (finans metninde WER kapısını şişirir). Rakam → kelime, yıl, %, $ ve "billion" sırası iki tarafta aynı |
| 3d | `tools/ses/ses-olc.py` | pilot anlatımı | ✅ f0 153 Hz, 143 kpm | 2,2 sn | — |
| 3e | `tools/ses/miks.py` | TTS + CC0 müzik + 2 efekt | ❌ → ✅ | 7,9 sn | (1) Varsayılan −12/9 dB konuşma altı farkı **35,7 dB** veriyordu (hedef 18–24) → varsayılan, pilotta seçilen −6/6 yapıldı → **22,9 dB**. (2) Geçici WAV'lar `/tmp`'de kalıyordu (12 dk ≈ 0,8 GB/çalıştırma) → çıkışta siliniyor |
| 3f | `tools/ses/birlestir.py` | 3 parçalı plan | ❌ → ✅ 6,5 sn çıktı | 0,35 sn | Ana/düzeltme yolları betiğe gömülüydü (pilot dosyası) → `--ana/--duzeltme/--kaynak`; tanımsız kaynak ve geçersiz aralık hatası |
| 3g | `tools/ses/efekt-uret.py` | scratch klasör | ✅ 3 FLAC, 48 kHz stereo | 0,7 sn | — |
| 4a | Rhubarb 1.14.0 | pilot anlatımı (+1 sn baş boşluğu), `--dialogFile` | ✅ 73 ağız işareti | 7,6 sn / 14,1 sn ses; 17 sn / 61 sn ses | — |
| 4b | `tools/senkron-testi.py` | pilot ses, pilot mp4, 60 sn TTS | ❌ → ✅ pilot 1 kare (0,57), 60 sn: 2 kare (sınırda) | 0,3 sn | Kare sayısı `len//(sr//fps)` yanlıştı → son karelerde boş dilim, korelasyon NaN ("gecikme 0'da nan"), en iyi gecikme NaN'lar arasından seçiliyordu. Düzeltildi + çıkış kodu (KALDI=1). 0,2 sn kaydırılmış çizelge → KALDI (doğru) |
| 5a | `npx tsc --noEmit` | video/ | ✅ | 3,1 sn | — |
| 5b | `npm run lint` (eslint + tsc) | video/ | ❌ → ✅ | 3 sn | `Sahneler.tsx`: kullanılmayan `sure` parametresi (davranış değişmedi) |
| 5c | `npx remotion compositions` | | ✅ Pilot, **PilotDikey (1080x1920)**, AgizTest | 5,7 sn | — |
| 5d | `tools/render-son.sh Pilot` | 14,1 sn, 423 kare | ✅ h264 1920x1080 30 fps, AAC 48 kHz stereo, −13,8 LUFS, TP −1,8 | 49–64 sn (render ~8–10 kare/sn) | Eşzamanlılık varsayılanı `nproc` (6 → Remotion reddediyor), süre dökümü, `trap` ile geçici klasör temizliği, ek bayrak geçişi (`--frames=` vb.) |
| 5e | 9:16 Shorts | `tools/render-son.sh PilotDikey` | ❌ yoktu → ✅ 1080x1920 render | 36 sn | `video/src/ortak/DikeyKesit.tsx` (kirp / dolgu modu, kesit başlangıcı) + `PilotDikey` test kompozisyonu. Gerçek Shorts kurgusu (hook, dikey altyazı) kurgu-editoru'nun |
| 5f | `tools/render-parca.sh` (yeni) | Pilot, 150 karelik 3 parça | ✅ 423 kare, tam render'a karşı PSNR 51,9 dB, ses kayması 0 ms, −13,8 LUFS | ilk 79 sn, önbellekten 24 sn, 1 parça yeniden 47 sn, `--ses` ile 9 sn | Yeni: düzeltme turunda yalnız değişen parça render edilir |
| 5g | Sürüm sabitleme | `npx remotion versions` | ✅ "All packages have the correct version" | — | `@remotion/fonts`, `@remotion/media` `^4.0.539` → `4.0.539` (package.json + lock) |
| 6a | `tools/karakter/buyut.py` | 256² ve 512² kırpım, Real-ESRGAN x4 | ❌ → ✅ | 256²: 35–62 sn; 512²: 114 sn | Tek parça çıkarımda bellek ~9,4 KB/piksel (256² → 1,2 GB) → 1920x1080 ≈ 19 GB → **OOM**. Parçalı (tile) çıkarım eklendi: tepe 1,4 GB, dikiş farkı ort. 0,18/255. `tam` kutusu ve varsayılan ağırlık yolu |
| 6b | `tools/karakter/kes.py` + `kenar-temizle.py` | pilot portresi | ✅ alfa çıktı | 8,3 sn + 0,9 sn | — (koordinatlar pilot görseline özel; bilinen sınır) |
| 6c | `tools/gorsel/tutarlilik.py` | `assets/karakter/paket-v1` | ❌ → ✅ 7/7 GEÇTİ | 3,4 sn | Başlıktaki `python3 -I` sistem Python'unda cv2 yok → venv Python yazıldı |
| 7a | `tools/viralite.py` | `ornek-senaryolar.json` ×2 + `--dokuman` | ✅ iki çalıştırma aynı, doküman tutarlı | 0,07 sn | — |
| 7b | `tools/kadro-kontrol.py` | | ✅ 17/17, GEÇTİ | 0,04 sn | — |
| 8a | `tools/yayin/test_yayin.py` | | ✅ 26 test OK | 2,5 sn | Testler `/tmp`'de sahte token klasörü bırakıyordu → `tearDown`'da siliniyor |
| 8b | `yukle.py ... --dry-run` | `uretim/ses-testi/yayin-paketi.json` | ✅ 0 hata, 1 uyarı (14 sn < 10 dk, beklenen) | 0,25 sn | — |
| 8c | `yukle.py ... --manuel-paket <scratch>` | | ✅ YAYIN.md, SRT, thumbnail, video | 0,23 sn | — |
| 9 | `tools/disk-durum.sh` (yeni) | rapor / `--temizle` | ✅ | 0,5 sn | Yeni: disk/RAM raporu, <5 GB uyarısı, güvenli temizlik |
| 10a | SRT üretimi | `tools/altyazi-uret.py` (yeni) | ❌ genel araç yoktu (pilot SRT'si elle gruplanmıştı) → ✅ 3 blok, 42 karakter/satır | 0,05 sn | Yeni: senaryo metni + Whisper → SRT + Remotion `captionChunks` JSON; WER > 0'da da hizalar (bozuk girdi testi geçti) |
| 10b | Gömülü kelime kelime altyazı | render'ın sesinden Whisper → `tools/altyazi-hiza.py` (yeni) | ✅ 26/26 eşleşme, ort. 9 ms, maks 40 ms; 0,2 sn kaydırılmış → KALDI | 0,05 sn | Yeni kapı aracı (hakem için) |

## Darboğazlar
1. **Render** (CPU): Pilot benzeri sahnelerde ~8–10 kare/sn [Ö]. `--concurrency` 2 → 4 yalnız ~%8 kazandırdı. `--gl=swangle` 4,7 kat yavaş (300 kare 155 sn, varsayılan 33 sn) → kullanılmaz. `--x264-preset=veryfast` %8 hızlı ama kalite/boyut değişiyor → elendi. Paralel parça render elendi (Remotion zaten tüm çekirdekleri kullanıyor). Çözüm: düzeltme turlarında `tools/render-parca.sh`.
2. **Paralel ajan yükü**: aynı 4 çekirdekte başka iş varken TTS 2,2 kat, Whisper ~1,8 kat yavaşladı [Ö]. CPU ağır adımlar (render, Whisper, TTS, Real-ESRGAN) aynı anda başlatılmamalı.
3. **Whisper medium.en**: 60 sn ses için 61–112 sn. small.en 2,3–2,8 kat hızlı ve bu örnekte WER aynı. Model seçimi ses-muhendisi'nin kararı; öneri: taslak ölçümlerde small.en, son kelime zamanlarında medium.en.
4. **Real-ESRGAN tam kare**: 1920x1080 büyütme ≈ 15 dk [H]. Yalnız karakter parçalarında kullanılmalı.

## Kapasite tahmini: 10–14 dk video, makine süresi (ölçümden hesap [H])
| Adım | Ölçülen hız | 10 dk | 12 dk | 14 dk |
|---|---|---|---|---|
| Kurulum (yeni konteyner) | 231–237 sn (apt paketleri ve HF modelleri önbellekteyken) | ~4–6 dk (indirmeler dahil [T]) | aynı | aynı |
| TTS (Kokoro) | RTF 0,5 boşta / 1,1 yük altında + 12 sn yükleme | 5–11 dk | 6–13 dk | 7–16 dk |
| tts-son + miks | ~0,17 / ~0,36 × gerçek süre | ~2 / ~4 dk | ~2 / ~4 dk | ~3 / ~5 dk |
| Whisper medium.en | RTF 1,0–1,85 | 10–19 dk | 12–22 dk | 14–26 dk |
| Rhubarb | RTF 0,28–0,54 | 3–5 dk | 3,5–6,5 dk | 4–8 dk |
| **Render 16:9** (render-son) | 8–10 kare/sn + ~10 sn sabit yük | **30–38 dk** | **36–45 dk** | **42–53 dk** |
| Render 2 Shorts (2×60 sn) | aynı hız | ~6–8 dk | ~6–8 dk | ~6–8 dk |
| Düzeltme turu (1 bölüm, render-parca) | 1 parça (60 sn) + birleştirme | ~4–6 dk (`--ses` ile) | aynı | aynı |
| **Toplam makine süresi (render dahil)** | | **~65–90 dk** | **~75–105 dk** | **~85–125 dk** |

- Render süresi pilot karmaşıklığında ölçüldü. Gerçek videoda büyük bitmap'ler ve kamera hareketi daha yavaş olabilir. Pilot v1'de 5,4 kare/sn ölçülmüştü: 12 dk ≈ 66 dk [T, üst sınır].
- Bellek yeterli: tepe kullanım render ~2,5 GB (sistem geneli), Whisper medium 2,0 GB, TTS 1,4 GB, Real-ESRGAN (parçalı) 1,4 GB [Ö]. 15,7 GB'ta iki ağır iş aynı anda bile sığar, sınır CPU'dur.
- Disk yeterli: video başına ara dosya ≈ 2 GB [H]: render ham ~0,45 GB (render-son siler) + final ~0,45 GB + miks ara WAV ~0,8 GB (artık siliniyor) + 150–200 görsel × ~2,5 MB. 20 GB boşla tek oturumda ~8 video sığar. Konteyner her oturumda sıfırlandığı için düzenli temizlik gerekmiyor. `tools/disk-durum.sh` 5 GB altında uyarır, `--temizle` yalnız geçici dosyaları siler.
- Ara dosyalar: render geçici klasörü `$TMPDIR` (trap ile silinir), parça render önbelleği `~/.finansal-arac/parca/<Id>/`, pip önbelleği `~/.cache/pip` (0,8 GB), modeller `~/.cache/huggingface` (2,2 GB), üretim çıktıları `uretim/<klasör>/` (WAV ve final mp4 git dışı).

## Açık noktalar (başka ajanlara)
- **animasyon-yonetmeni**: 60 sn'lik TTS'te dudak senkronu 2 kare çıktı (kapı sınırı). Uzun videoda bölüm bölüm ölçülmeli. Gerekirse ağız çizelgesine −1 kare ofset verilmeli.
- **kurgu-editoru**: Shorts için dikey altyazı katmanı gerekli. `DikeyKesit mod="kirp"` 16:9'a göre yerleştirilmiş altyazıyı kırpar. SRT ve altyazı verisi `tools/altyazi-uret.py` ile, kapı ölçümü `tools/altyazi-hiza.py` ile yapılır.
- **ses-muhendisi**: Whisper model seçimi (yukarıdaki 3. madde). Yeni `hata-orani.py` sayıları normalize ediyor, eski WER raporları biraz yüksek çıkmış olabilir.
- Tamamen boş bir konteynerde (apt paketleri, HF modelleri ~1,9 GB, npm önbelleği yokken) kurulum süresi ölçülmedi. Tahmin ~6 dk [T].
