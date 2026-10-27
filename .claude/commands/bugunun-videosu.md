---
description: Tetik "Bugünün videosu gelsin" — konu seçiminden teslim paketine kadar tam otomatik üretim (1 uzun video + 2 Shorts); Niyazi yalnız bitmiş videoyu onaylar
argument-hint: [isteğe bağlı konu/sütun ipucu]
---
# /bugunun-videosu — koordinatör akışı

Konu/sütun ipucu: $ARGUMENTS (boşsa sütun `docs/yayin-takvimi.md` rotasyonundan, konu sistemden gelir).

**Kim yürütür:** Ana oturumdaki koordinatör, `showrunner`'ın çalışma kurallarıyla yürütür. **Alt ajanları yalnız koordinatör çağırır**, çünkü alt ajanlar alt ajan çağıramaz. "Paralel" yazan adımlarda ajan çağrıları **tek mesajda birlikte** yapılır.
**Ana hedef:** kanalın para kazanması (YouTube Partner Programı'na kabul + sürdürülebilir gelir). Bu yüzden her video politika kapısından (monetizasyon-uyum-uzmani, F2/F3/F8) ve retention kapısından geçer; yayından sonra performans verisi sonraki videoya geri beslenir (F12).
**Niyazi'nin rolü:** Yalnız F10'da bitmiş videoyu onaylar. Senaryo seçimi tamamen ajanlardadır; hakemin senaryo kararı Niyazi'ye sorulmaz.
**Görsel ve ses kaynağı (Niyazi kararları 2026-10-26):** Sahne ve thumbnail görselleri Canva bağlayıcısıyla üretilir (Niyazi'nin aboneliği, ek ücret yok; ücretli görsel API kullanılmaz). Canva çağrılarını (`mcp__Canva__*`) koordinatör veya araç erişimi olan ajan yapar; ajanlar prompt'u ve değerlendirmeyi hazırlar. Anlatıcı sesi ücretsiz yapay zekâ sesidir (TTS); Niyazi'nin okuması yedek yoldur (`/senaryo-onayla`, `/ses-isle`).
**Onaysız yapılmaz:** Para harcayan servis (ücretli görsel API, image-to-video, ücretli TTS), YouTube'a her türlü yükleme (private dahil), dışarıya mesaj ve geri alınamaz adımlar. Bütçe onayı önceden verilmişse (`docs/uretim-kapasitesi.md` → "Onaylı bütçe") onaylı tavana kadar harcanabilir; tavan aşılacaksa durulur ve Niyazi'ye sorulur.

## 0. Genel kurallar
- **Klasör:** `uretim/<YYYY-MM-DD>-<slug>/`. Slug F2'deki hakem kararından sonra belli olur. O zamana kadar `uretim/<YYYY-MM-DD>-secim/` kullanılır, F2'nin sonunda `git mv` ile yeniden adlandırılır.
- **`durum.md`** (sahibi showrunner/koordinatör) her adımdan sonra güncellenir. Sütunlar: adım | sahip ajan | durum (BEKLİYOR / SÜRÜYOR / GEÇTİ / RED-1 / RED-2 / ESKALASYON) | teslim dosyası | test kanıtı (komut + sonuç) | başlangıç–bitiş saati. Oturum koparsa akış `durum.md`'deki ilk GEÇMEMİŞ adımdan devam eder. Baştan başlanmaz.
- **Teslim kuralı:** Her ajan, protokol (`docs/ajan-protokolu.md`) gereği 2–3 aday, test, eleme ve hafıza dersiyle teslim eder. **Test çıktısı yoksa teslim alınmaz** ve iş geri gönderilir. Bu bir RED turu sayılmaz, ama `durum.md`'ye not edilir.
- **Kalite kapıları:** `docs/kalite-kapilari.md` ve bu dosyadaki "Ek kapılar".
- **Commit:** Her faz sonunda `git add` + commit + push yapılır (konteyner silinir). Mesaj: `<slug>: F<n> <özet>`. 100 MB'ı aşan medya git'e girmez. Final video ve Shorts dosyaları git'e girmez (`.gitignore`); depolama bölüm 3'teki öneriye göre (Niyazi onayı bekliyor).
- **Kod yeri:** Remotion sahneleri `video/src/videolar/<slug>/` altında olur (sahibi animasyon-yonetmeni). Ortak bileşenler `video/src/ortak/` altında olur (sahibi uretim-muhendisi; klasör ilk ortak bileşenle oluşturulur).

## 1. RED → düzeltme döngüsü ve eskalasyon
1. Kapıdan kalan iş, **düzeltme listesiyle** (hangi ölçüm, beklenen ve ölçülen değer) aynı ajana geri döner. Durum `RED-1` olur.
2. İkinci kez kalırsa durum `RED-2` olur, son düzeltme turu yapılır.
3. Üçüncü kez kalırsa, yani **2 düzeltme turu sonra hâlâ kalıyorsa**, iş **koordinatöre eskalasyon** olur. Ajan üçüncü kez denemez. Koordinatör sırayla şunları dener:
   a. **Kök neden araç mı?** Öyleyse `uretim-muhendisi` çağrılır.
   b. **Kapsamı küçült:** Sorunlu sahne B planına geçer (grafik ağırlıklı sahne, karaktersiz illüstrasyon, kamera hareketi). Kalite kapısı gevşetilmez.
   c. **Senaryo kaynaklıysa** (doğrulanamayan iddia, görselleştirilemeyen yapı) hakemin **yedek senaryosuna** geçilir ve F3'ten devam edilir.
   d. **Yayın slotu kaçacaksa** `docs/yayin-takvimi.md` → "Gecikme" kuralı uygulanır (stoktaki video slota girer) ve Niyazi'ye tek satır bilgi verilir.
   e. Aynı ajan son 3 videoda en az 2 kez eskalasyona düştüyse veya iş sahipsiz kaldıysa `ik-direktoru`'na bildirilir (`docs/ajan-karnesi.md` notu).
4. Kapıdan geçmeyen hiçbir iş bir sonraki faza geçmez. **Kötü video yayına çıkmaz, geç çıkar.**

## 2. Akış

### F0 — Açılış (paralel)
| Ajan | İş | Teslim | Kapı |
|---|---|---|---|
| koordinatör (showrunner kuralları) | Bugünün tarihi, hedef yayın slotu ve sütun (`docs/yayin-takvimi.md`), stok durumu, klasör, `durum.md` | `durum.md` | Slot + sütun + stok satırı yazıldı |
| `uretim-muhendisi` | Ortam kurulumu (`tools/kurulum.sh`): Remotion, Rhubarb, Kokoro, Whisper, ffmpeg. `Pilot` kompozisyonunun 2 karelik test render'ı | `00-ortam/ortam-raporu.md` | Araç/kurulum kapısı: hatasız kurulum, kompozisyonlar listeleniyor, test render var |

### F1 — Araştırma (paralel)
| Ajan | İş | Teslim | Kapı |
|---|---|---|---|
| `trend-avcisi` | Sütuna ağırlık veren konu havuzu (≥15 konu; 3 sütundan da aday), kaynaklı | `01-arastirma/konu-havuzu.md` | Konu havuzu: her konuda ≥2 bağımsız kaynak, linkler açılıyor |
| `kanal-analisti` | `docs/rakip-analizi.md` 14 günden eskiyse günceller (değilse atlar ve not düşer). Yayın varsa kendi kanalımızın son videolarının 7/28 gün verisini çıkarır | `01-arastirma/rakip-ozet.md` | Rakip analizi: her sayının kaynağı ve ölçüm tarihi var |

### F2 — Senaryo ve seçim (Niyazi onayı YOK)
1. `senaryo-yazari` → **en az 10 senaryo** yazar (hook, yapı, karakter anı, sütun, görselleştirme notu). Teslim `02-senaryo/senaryolar.md`. Kapı: Senaryolar (en az 5 farklı açı türü).
2. **Paralel:**
   - `viralite-analisti` → `tools/viralite.py` ile hepsini puanlar ve **ilk 3'ü** bırakır. Teslim `02-senaryo/viralite.md`. Kapı: Viralite (betik 2 kez çalışıp aynı sonuç).
   - `finans-dogrulayici` → 10 senaryonun hepsine risk taraması yapar: doğrulanabilirlik, tavsiye dili, karalama, yanıltıcı bilgi. Teslim `02-senaryo/on-dogrulama.md`. Kapı: Her senaryoya YEŞİL/SARI/KIRMIZI + gerekçe. KIRMIZI olan senaryo elenir.
   - `monetizasyon-uyum-uzmani` → 10 senaryoya para kazanma/reklam uygunluğu ön taraması: reklam dostu kategoriler (hassas olay, sarsıcı içerik, tartışmalı konu), şablon tekrarı (önceki videolarla aynı yapı/sonuç), AI personası, gerçekçi sahte olay riski. Teslim `02-senaryo/politika-on-tarama.md`. Kapı: Her senaryoya YEŞİL/SARI/KIRMIZI + politika kaynağı. KIRMIZI olan senaryo elenir.
3. `hakem` → ilk 3 içinden **tek kazanan + yedek** seçer. Karar **kesindir**, Niyazi'ye sorulmaz. Teslim `02-senaryo/senaryo-karari.md` (kazanan, gerekçe, ilk 3'ün puan tablosu, riskler). Kapı: kazanan iki taramada da KIRMIZI değil; ilk 3 aynı tabloda; her birine "neden kaybedebilir" maddesi yazılmış.
4. Klasör slug'la yeniden adlandırılır, commit atılır.

### F3 — Tam metin ve doğrulama (sıralı)
1. `senaryo-yazari` → tam İngilizce metin: anlatım + GÖRSEL sütunu (sahne başına) + 2 Shorts için kanca/kesit önerisi. Teslim `03-metin/metin.md`. Kapı: Metin (≥1.500 kelime, ±%10, ilk 15 sn'de net vaat, en geç 90 sn'de bir yeniden kanca) + Retention (metin): ilk 30 sn planı ve retention haritası var, ilk 60 sn'de abone çağrısı yok.
2. **Paralel:** `finans-dogrulayici` → metindeki tüm rakam, tarih ve olayları doğrular; yasal notu ve "scenario" dilini denetler. Teslim `03-metin/dogrulama.md`. Kapı: Doğrulama (doğrulanamayan rakam kalmadı). ‖ `monetizasyon-uyum-uzmani` → metni para kazanma politikalarına göre denetler (anlamlı anlatı/yorum, maskot tavsiye vermiyor, ilk 30 sn ve başlıkta reklam dostu dil, önceki metinlerle kalıp tekrarı). Teslim `03-metin/politika-denetimi.md`. Kapı: YPP politika (metin) — KIRMIZI bulgu yok. RED gelirse metin senaryo-yazari'ye döner, düzeltilmiş metin ikisinden de yeniden geçer.
3. **Metin kilidi.** Bundan sonra metin değişirse ses, animasyon ve kurgu yeniden üretilir. Bu yüzden değişiklik yalnız RED düzeltmesi için yapılır.

### F4 — Üretim kolları (dört kol paralel; metin kilidinden hemen sonra)
| Kol | Ajan | İş | Teslim | Kapı |
|---|---|---|---|---|
| Ses | `ses-yonetmeni` → sonra `ses-muhendisi` | TTS okuma metni (telaffuz düzeltmeleri) → Kokoro ile anlatım (`tools/ses/tts.py`) → son işlem (`tools/ses/tts-son.sh`), Whisper kelime zamanları | `04-ses/anlatim.wav`, `04-ses/kelimeler.json`, `04-ses/ses-rapor.md` | Anlatıcı sesi (TTS): WER ≤ %10, kanal adı doğru. Ses: −14 LUFS ±1, TP ≤ −1 dBTP |
| Görsel | `gorsel-varlik-sanatcisi` (+ koordinatör Canva çağrıları) | GÖRSEL sütunundan sahne listesi → Canva prompt paketi → koordinatör Canva `generate-image` ile üretir → ajan sahne illüstrasyonlarını (16:9 + 9:16 güvenli alan), karakter pozlarını değerlendirir, kontakt sayfası, üretim kaydı (prompt + Canva media ID) | `05-gorsel/sahne-listesi.md`, `05-gorsel/canva-promptlari.md`, `05-gorsel/sahneler/`, `05-gorsel/kontakt.png` | Görsel varlık: karakter kartına uygun, sahne ≥1920x1080, kesme artığı yok |
| Müzik | `muzik-ses-tasarimcisi` | Sütuna ve tona göre müzik/SFX adayları + lisans kaydı (zamanlama F6'da) | `06-muzik/lisans-kaydi.md`, `06-muzik/adaylar.md` | Müzik/SFX: her dosya lisans kaydında, NC/ND yok |
| Paket taslağı | `thumbnail-tasarimcisi` + `youtube-paketleyici` (paralel) | 3 thumbnail konsepti (taslak) + 5 başlık varyantı, açıklama taslağı, etiketler, Shorts başlıkları | `09-paket/thumb-konsept.md`, `09-paket/paket-taslak.md` | Taslak: başlık ≤60 karakter, thumbnail metni ≤4 kelime |

Görsel kol **ek para harcamaz**: Canva bağlayıcısı Niyazi'nin mevcut aboneliğindeki aylık yapay zekâ hakkını kullanır. Stil gerçekçi/resimsi olabilir; şart karakterin her sahnede tutarlı olmasıdır. Aylık Canva hakkı biterse, tam çözünürlüklü dosya alınamazsa veya tutarlılık kapısı geçmezse sahneler B planına geçer: kodla çizilen grafik/harita/sayaç sahneleri + mevcut karakter varlıkları. Kullanılan Canva üretim sayısı ve B planına geçen sahneler Niyazi'ye F10'da raporlanır. Ücretli görsel API veya image-to-video onaysız açılmaz.

### F5 — Animasyon (ses kolu ve görsel kol GEÇTİ olunca)
`animasyon-yonetmeni`:
1. Rhubarb ağız zamanları üretilir.
2. **Önce 10–20 sn'lik kritik yol testi** yapılır: konuşan karakter + en zor sahne. Kapı: `tools/senkron-testi.py` ≤2 kare, `AgizTest` karesi.
3. Test geçerse tüm sahneler kodlanır (16:9) ve iki Shorts kesiti için 9:16 kompozisyonlar hazırlanır.

Teslim `07-animasyon/test-10sn.mp4`, `07-animasyon/senkron-rapor.md`, `video/src/videolar/<slug>/`. Test geçmeden tam sahne kodlamasına başlanmaz.

### F6 — Müzik miksi (F5 ile paralel; ses kolu GEÇTİ olunca)
`muzik-ses-tasarimcisi` → kesin kelime zamanlarına göre cue listesi + ducking'li müzik/SFX stem'leri hazırlar. Teslim `06-muzik/cue-listesi.md`, `06-muzik/stems/`. Kapı: Müzik/SFX (miksli dilimde WER bozulmadı, seviye ölçümü yapıldı).

### F7 — Kurgu ve render
`kurgu-editoru` (F5 + F6 GEÇTİ):
1. Ana video (16:9) birleştirilir, tempo ve geçişler kurulur, kelime kelime gömülü altyazı eklenir, SRT çıkarılır. Render `tools/render-son.sh` ile yapılır.
2. **2 Shorts** hazırlanır (9:16, ≤60 sn). Her biri **kendi hook'uyla** açılır (ilk 2 sn), aynı sahnelerden yeniden kadrajlanır. Kancayı taşıyacak sahne eksikse koordinatöre "ek sahne" talebi iletilir; koordinatör bunu animasyon-yonetmeni'ne (gerekirse gorsel-varlik-sanatcisi'ne) verir. Shorts için 3–5 aday bölüm seçilir, ilk 2 sn testinden geçen 2 tanesi kalır.

Teslim `08-kurgu/final-16x9.mp4`, `08-kurgu/altyazi.srt`, `08-kurgu/shorts-1.mp4`, `08-kurgu/shorts-2.mp4`, `08-kurgu/kurgu-rapor.md`. Kapı: Kurgu, Altyazı, Ses (son dosyada), Retention (kurgu: ilk görsel değişim ≤3 sn, kanal intro'su yok) ve aşağıdaki Shorts kapısı.

### F8 — Son paket (paralel)
| Ajan | İş | Teslim | Kapı |
|---|---|---|---|
| `thumbnail-tasarimcisi` | Render karelerinden **3 thumbnail varyantı** (A/B/C, 1280x720) | `09-paket/thumbnail-A.png`, `09-paket/thumbnail-B.png`, `09-paket/thumbnail-C.png`, `09-paket/thumb-rapor.md` | Thumbnail: 168x94'te okunuyor, metin ≤4 kelime |
| `youtube-paketleyici` | Son başlık + 4 yedek, açıklama (kaynaklar, yasal not, lisans atıfları, AI ses notu), SEO, etiketler, hashtag'ler, **gerçek zamanlardan bölümler**, pinli yorum, Shorts paketleri. Yayın paketleri yükleme aracının şemasında yazılır (bkz. bölüm 3) | `09-paket/paket.md`, `09-paket/yayin-paketi.json`, `09-paket/yayin-paketi-shorts-1.json`, `09-paket/yayin-paketi-shorts-2.json` | Paket: başlık ≤60 karakter, bölümler gerçek zamanlara denk. Yayın paketi kapısı: `--dry-run` 0 hata |
| `viralite-analisti` | Bitmiş paketin (başlık + thumbnail + ilk 15 sn) **viralite puanı**, F2 tahminiyle fark | `09-paket/viralite-son.md` | Viralite: betik 2 kez çalışıp aynı sonuç |
| `monetizasyon-uyum-uzmani` | Paket + final video politika denetimi: başlık/thumbnail içerikle tutarlı, AI beyanı kararı (`durum.sentetik_medya`) ve açıklama satırı, reklam uygunluğu öz beyan yanıtları, lisans kaydı + Content ID itiraz kanıtı, reused/dış görüntü yok, özgünlük ve insan katkısı kanıtı, yeniden kullanılan sahne oranı. Taslak paketler F8 içinde ona gider, kararı youtube-paketleyici pakete işler | `09-paket/politika-raporu.md` | YPP politika kapısı (`docs/kalite-kapilari.md`) |

### F9 — Hakem son kontrol
`hakem` → bütün kapıları **kendisi yeniden ölçer** (ffprobe, ebur128, `tools/senkron-testi.py`, altyazı hizası, thumbnail küçültme, lisans kaydı, yasal not, Shorts kapısı, YPP politika kapısı, retention kapısı). Karneyi doldurur. Teslim `hakem-raporu.md`: ONAY veya RED + düzeltme listesi. RED alan iş ilgili ajana döner (bölüm 1'deki döngü), sonra yeniden F9 yapılır.

### F10 — Teslim paketi ve Niyazi'ye sunum → DUR
Koordinatör `teslim/` klasörünü kurar (bkz. bölüm 3), `YAYIN.md`'yi yazar, commit/push eder ve Niyazi'ye **tek sayfa** sunar:
- Video başlığı, sütun, süre, hedef yayın slotu (ET + TRT).
- Viralite puanı (F2 tahmini → son), ilk 3 senaryonun puanları ve kazananın neden seçildiği (bilgi amaçlı, onay sorulmaz).
- Hakem kararı ve kapı tablosunun özeti.
- Riskler (doğrulama, politika, B planına geçen sahneler, Canva AI hakkı kullanımı, varsa onaylı harcama).
- Final video dosyası (bölüm 3'teki depolama önerisine göre Niyazi'ye dosya olarak gönderilir; git'te yalnız önizleme + metadata).
- **Niyazi'nin yapacağı tek şey:** "Videoyu izle; `yayınla` ya da `şunu değiştir: …` de."

Niyazi'den yanıt gelmeden yayın adımına geçilmez.

### F11 — Yayın (yalnız Niyazi'nin açık onayıyla)
- Niyazi "yayınla / yükle / onay" derse koordinatör `teslim/` içindeki üç paketin (`yayin-paketi.json`, `yayin-paketi-shorts-1.json`, `yayin-paketi-shorts-2.json`) `onay.niyazi_onayi` alanını `true`, `onay.tarih` alanını bugünün tarihi yapar. Sonra **uretim-muhendisi'nin aracını** her paket için çağırır: `python3 tools/yayin/yukle.py uretim/<klasör>/teslim/<paket>.json`. Kurulum ve cihaz kodu adımları `docs/yayin-kurulumu.md`'de. Bu akış aracı yalnız çağırır, kendi yükleme kodunu yazmaz. Aracın arayüzü değişirse kaynak araçtır (`tools/yayin/`), bu dosya ona uydurulur.
- Varsayılan: ana video **private + yayin_zamani** (takvim slotu). Shorts takvimdeki kendi slotlarına zamanlanır. Thumbnail A yüklenir; B ve C, YouTube Studio "Test & Compare" için `YAYIN.md`'de Niyazi'ye bırakılır (API'de karşılığı doğrulanmadı).
- Cihaz akışı altyazı (SRT) yükleyemez (`docs/yayin-kurulumu.md`). SRT, `YAYIN.md`'deki adımla Studio'dan eklenir.
- OAuth tanımlı değilse, denetim kilidi çıkarsa ya da araç hata verirse `python3 tools/yayin/yukle.py <paket> --manuel-paket` ile Studio klasörü üretilir ve elle yükleme adımları Niyazi'ye verilir.
- Yükleme çıktısı (video ID'leri, planlanan saatler) `teslim/yayin-kaydi.json`'a yazılır. `docs/yayin-takvimi.md` stok tablosu güncellenir. Kararı `c-level-skills:decision-logger` biçimiyle `durum.md` sonuna yaz.
- Niyazi "şunu değiştir" derse değişiklik ilgili ajana gider (bölüm 1'deki döngü), F9 ve F10 tekrarlanır.
- `YAYIN.md`'deki Studio adımları: SRT yükleme, Shorts'a "ilgili video" olarak uzun videonun bağlanması, uç ekran, oynatma listesi, reklam uygunluğu öz beyan yanıtları (`politika-raporu.md`), Test & Compare (B ve C).

### F12 — Yayın sonrası geri besleme (48 saat, 7 gün, 28 gün)
| Ajan | İş | Teslim | Kapı |
|---|---|---|---|
| `kanal-analisti` | Gösterim, CTR, AVD ve ortalama izlenme yüzdesi, ilk 30 sn tutma ve düşüş noktaları (sahneye eşlenmiş), trafik kaynakları (Shorts → uzun dahil), abone kazanımı, Test & Compare sonucu, YPP ilerlemesi | `yayin-sonrasi/performans-<48s\|7g\|28g>.md` | Yayın sonrası analiz kapısı: her sayının kaynağı (API / Studio dışa aktarımı) ve tarihi var; "sonraki video için 3 ders" yazıldı |
| `viralite-analisti` | 7 ve 28 gün verisiyle tahmin–gerçek karşılaştırması, model kalibrasyonu | `yayin-sonrasi/kalibrasyon.md` | Viralite: betik 2 kez çalışıp aynı sonuç |
| `youtube-paketleyici` | (Niyazi onayıyla) yorum yanıtları; düşük CTR'de (kanal-analisti önerisiyle) başlık/thumbnail değişikliği önerisi — değişiklik yalnız Niyazi onayıyla yayına girer | `yayin-sonrasi/paket-guncelleme.md` | Öneri gerekçeli ve veriye bağlı |
Dersler sonraki videonun F1'ine girer (trend-avcisi, senaryo-yazari, kurgu-editoru, thumbnail-tasarimcisi bu raporları okur). Her 5 videoda bir `monetizasyon-uyum-uzmani` kanal düzeyi özgünlük denetimi ve `docs/ypp-hazirlik.md` güncellemesi yapar.

## 3. Teslim paketi: `uretim/<tarih>-<slug>/teslim/`
| Dosya | Kaynak |
|---|---|
| `final-16x9.mp4` | kurgu-editoru (F7) |
| `shorts-1.mp4`, `shorts-2.mp4` | kurgu-editoru (F7) |
| `thumbnail-A.png`, `thumbnail-B.png`, `thumbnail-C.png` | thumbnail-tasarimcisi (F8) |
| `altyazi.srt` | kurgu-editoru (F7) |
| `yayin-paketi.json` (uzun video), `yayin-paketi-shorts-1.json`, `yayin-paketi-shorts-2.json` | youtube-paketleyici (F8) |
| `politika-raporu.md` | monetizasyon-uyum-uzmani (F8) |
| `hakem-raporu.md` | hakem (F9) |
| `YAYIN.md` | koordinatör (F10): tek sayfa özet |

**Final video depolama — öneri (Niyazi onayı bekliyor):** 12 dk final video ~450 MB'tır [H] ve GitHub'ın dosya başına 100 MB sınırını aşar; konteyner de oturum sonunda silinir. Öneri:
- Final video (ve Shorts) teslimde **Niyazi'ye dosya olarak gönderilir**; Niyazi onaylayıp YouTube'a yüklenince **YouTube'daki video arşiv sayılır**.
- `uretim/<klasör>/` altında git'e yalnız küçük önizleme (ör. `teslim/onizleme-*.mp4`, düşük çözünürlük, <25 MB) + metadata (`yayin-paketi*.json`, `YAYIN.md`, `hakem-raporu.md`, thumbnail'lar, SRT) girer.
- `.gitignore`: `uretim/**/final/*.mp4`, `uretim/**/teslim/*.mp4`, `uretim/**/08-kurgu/*.mp4` (önizlemeler `!uretim/**/*onizleme*.mp4` ile hariç). Ayrıntı: `docs/uretim-kapasitesi.md` bölüm 6, satır 5.
- Onay gelene kadar geçici olarak böyle çalışılır (git zaten 100 MB üstü dosyayı kabul etmez, `.gitignore` geri alınabilir); Niyazi başka bir yer (Drive, Git LFS vb.) seçerse bu bölüm güncellenir.

**Yayın paketi şeması** yükleme aracının sözleşmesidir: `tools/yayin/yayin_paket.py` → `SEMA` (`"sema": "yayin-paketi/1"`). Her video için **ayrı paket** yazılır (`"tur": "uzun"` ya da `"shorts"`). Dosya yolları paketin klasörüne göredir. Alanlar: `dosyalar.video`, `dosyalar.thumbnail`, `dosyalar.altyazilar`, `metadata.baslik`, `metadata.aciklama`, `metadata.etiketler`, `metadata.bolumler`, `metadata.kategori_id`, `durum.gizlilik`, `durum.yayin_zamani` (saat dilimli ISO 8601), `durum.cocuklara_ozel`, `durum.sentetik_medya`, `onay.niyazi_onayi`, `onay.tarih`. `onay.niyazi_onayi` F10'a kadar **false** kalır; araç false iken yüklemeyi reddeder. Kategori youtube-paketleyici'nin kararıdır; sentetik medya beyanı (`durum.sentetik_medya`) monetizasyon-uyum-uzmani'nin kararıdır (`politika-raporu.md`), youtube-paketleyici pakete işler.

## 4. Ek kapılar (bu akışa özgü)
| Aşama | Test | Geçme ölçütü |
|---|---|---|
| Shorts | ffprobe + ilk 2 sn kare + altyazı güvenli alanı | 1080x1920, ≤60 sn, ilk 2 sn'de kendi kancası, metin alt %20'ye ve sağ kenar düğmelerine binmiyor, −14 LUFS ±1 |
| Ön doğrulama | 10 senaryo tablosu | her senaryoda YEŞİL/SARI/KIRMIZI + gerekçe |
| Yayın paketi | `python3 tools/yayin/yukle.py <paket> --dry-run` (3 paket) | 0 hata; adı geçen her dosya `teslim/` içinde; yayın zamanı takvim slotuna denk; başlık ≤60 karakter; `onay.niyazi_onayi` false |
| Teslim paketi | dosya listesi | bölüm 3'teki 13 dosyanın hepsi yerel diskte var (final mp4'ler git'e girmez, önizleme girer), hakem ONAY |

## 5. Ajan çağrı sırası (özet)
```
F0  koordinatör ‖ uretim-muhendisi
F1  trend-avcisi ‖ kanal-analisti
F2  senaryo-yazari → (viralite-analisti ‖ finans-dogrulayici ‖ monetizasyon-uyum-uzmani) → hakem   [Niyazi onayı yok]
F3  senaryo-yazari → (finans-dogrulayici ‖ monetizasyon-uyum-uzmani)                  [metin kilidi]
F4  (ses-yonetmeni → ses-muhendisi) ‖ gorsel-varlik-sanatcisi ‖ muzik-ses-tasarimcisi ‖ (thumbnail-tasarimcisi ‖ youtube-paketleyici: taslak)
F5  animasyon-yonetmeni (10–20 sn test → tam)  ‖  F6 muzik-ses-tasarimcisi (miks)
F7  kurgu-editoru (16:9 + 2 Shorts)
F8  thumbnail-tasarimcisi ‖ youtube-paketleyici ‖ viralite-analisti → monetizasyon-uyum-uzmani (politika raporu)
F9  hakem → F10 Niyazi'ye teslim → DUR → F11 yalnız onayla: tools/yayin/yukle.py (uretim-muhendisi aracı)
F12 yayın sonrası 48 sa / 7 g / 28 g: kanal-analisti → viralite-analisti (+ youtube-paketleyici öneri) → dersler sonraki videoya
Her aşamada araç sorunu → uretim-muhendisi. 2 RED sonrası → koordinatör eskalasyonu; tekrarlayan sorun → ik-direktoru.
```

## Sessiz üretim (Niyazi kararı 2026-10-27)
Tetikten sonra Niyazi'ye ara mesaj, rapor veya soru yok; yalnız zorunlu erişim izni istenir. İş arka planda F10'a kadar sürer, Niyazi'ye yalnız bitmiş teslim verilir.
