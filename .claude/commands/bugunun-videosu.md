---
description: Tetik "Bugünün videosu gelsin" — konu seçiminden teslim paketine kadar tam otomatik üretim (1 uzun video + 2 Shorts); Niyazi yalnız bitmiş videoyu onaylar
argument-hint: [isteğe bağlı konu/sütun ipucu]
---
# /bugunun-videosu — koordinatör akışı

Konu/sütun ipucu: $ARGUMENTS (boşsa sütun `docs/yayin-takvimi.md` rotasyonundan, konu sistemden gelir).

**Kim yürütür:** Ana oturumdaki koordinatör, `showrunner`'ın çalışma kurallarıyla yürütür. **Alt ajanları yalnız koordinatör çağırır**, çünkü alt ajanlar alt ajan çağıramaz. "Paralel" yazan adımlarda ajan çağrıları **tek mesajda birlikte** yapılır.
**Niyazi'nin rolü:** Yalnız F10'da bitmiş videoyu onaylar. Senaryo seçimi tamamen ajanlardadır; hakemin senaryo kararı Niyazi'ye sorulmaz.
**Onaysız yapılmaz:** Para harcayan servis (görsel API, image-to-video, ücretli TTS), YouTube'a her türlü yükleme (private dahil), dışarıya mesaj ve geri alınamaz adımlar. Bütçe onayı önceden verilmişse (`docs/uretim-kapasitesi.md` → "Onaylı bütçe") onaylı tavana kadar harcanabilir; tavan aşılacaksa durulur ve Niyazi'ye sorulur.

## 0. Genel kurallar
- **Klasör:** `uretim/<YYYY-MM-DD>-<slug>/`. Slug F2'deki hakem kararından sonra belli olur. O zamana kadar `uretim/<YYYY-MM-DD>-secim/` kullanılır, F2'nin sonunda `git mv` ile yeniden adlandırılır.
- **`durum.md`** (sahibi showrunner/koordinatör) her adımdan sonra güncellenir. Sütunlar: adım | sahip ajan | durum (BEKLİYOR / SÜRÜYOR / GEÇTİ / RED-1 / RED-2 / ESKALASYON) | teslim dosyası | test kanıtı (komut + sonuç) | başlangıç–bitiş saati. Oturum koparsa akış `durum.md`'deki ilk GEÇMEMİŞ adımdan devam eder. Baştan başlanmaz.
- **Teslim kuralı:** Her ajan, protokol (`docs/ajan-protokolu.md`) gereği 2–3 aday, test, eleme ve hafıza dersiyle teslim eder. **Test çıktısı yoksa teslim alınmaz** ve iş geri gönderilir. Bu bir RED turu sayılmaz, ama `durum.md`'ye not edilir.
- **Kalite kapıları:** `docs/kalite-kapilari.md` ve bu dosyadaki "Ek kapılar".
- **Commit:** Her faz sonunda `git add` + commit + push yapılır (konteyner silinir). Mesaj: `<slug>: F<n> <özet>`. 100 MB'ı aşan medya git'e girmez. Saklama yeri `docs/uretim-kapasitesi.md` → "Depolama" bölümüne göre seçilir.
- **Kod yeri:** Remotion sahneleri `video/src/videolar/<slug>/` altında olur (sahibi animasyon-yonetmeni). Ortak bileşenler `video/src/ortak/` altında olur (sahibi uretim-muhendisi).

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
   - `finans-dogrulayici` → 10 senaryonun hepsine risk taraması yapar: doğrulanabilirlik, tavsiye dili, karalama, YouTube finans politikası. Teslim `02-senaryo/on-dogrulama.md`. Kapı: Her senaryoya YEŞİL/SARI/KIRMIZI + gerekçe. KIRMIZI olan senaryo elenir.
3. `hakem` → ilk 3 içinden **tek kazanan + yedek** seçer. Karar **kesindir**, Niyazi'ye sorulmaz. Teslim `02-senaryo/senaryo-karari.md` (kazanan, gerekçe, ilk 3'ün puan tablosu, riskler). Kapı: kazanan KIRMIZI değil; ilk 3 aynı tabloda; her birine "neden kaybedebilir" maddesi yazılmış.
4. Klasör slug'la yeniden adlandırılır, commit atılır.

### F3 — Tam metin ve doğrulama (sıralı)
1. `senaryo-yazari` → tam İngilizce metin: anlatım + GÖRSEL sütunu (sahne başına) + 2 Shorts için kanca/kesit önerisi. Teslim `03-metin/metin.md`. Kapı: Metin (≥1.500 kelime, ±%10, ilk 15 sn'de net vaat, en geç 90 sn'de bir yeniden kanca).
2. `finans-dogrulayici` → metindeki tüm rakam, tarih ve olayları doğrular; yasal notu ve "scenario" dilini denetler. Teslim `03-metin/dogrulama.md`. Kapı: Doğrulama (doğrulanamayan rakam kalmadı). RED gelirse metin senaryo-yazari'ye döner, düzeltilmiş metin yeniden doğrulanır.
3. **Metin kilidi.** Bundan sonra metin değişirse ses, animasyon ve kurgu yeniden üretilir. Bu yüzden değişiklik yalnız RED düzeltmesi için yapılır.

### F4 — Üretim kolları (dört kol paralel; metin kilidinden hemen sonra)
| Kol | Ajan | İş | Teslim | Kapı |
|---|---|---|---|---|
| Ses | `ses-yonetmeni` → sonra `ses-muhendisi` | TTS okuma metni (telaffuz düzeltmeleri) → Kokoro ile anlatım (`tools/ses/tts.py`) → son işlem (`tools/ses/tts-son.sh`), Whisper kelime zamanları | `04-ses/anlatim.wav`, `04-ses/kelimeler.json`, `04-ses/ses-rapor.md` | Anlatıcı sesi (TTS): WER ≤ %10, kanal adı doğru. Ses: −14 LUFS ±1, TP ≤ −1 dBTP |
| Görsel | `gorsel-varlik-sanatcisi` | GÖRSEL sütunundan sahne listesi → sahne illüstrasyonları (16:9 + 9:16 güvenli alan), karakter pozları, kontakt sayfası, lisans/üretim kaydı | `05-gorsel/sahne-listesi.md`, `05-gorsel/sahneler/`, `05-gorsel/kontakt.png` | Görsel varlık: karakter kartına uygun, sahne ≥1920x1080, kesme artığı yok |
| Müzik | `muzik-ses-tasarimcisi` | Sütuna ve tona göre müzik/SFX adayları + lisans kaydı (zamanlama F6'da) | `06-muzik/lisans-kaydi.md`, `06-muzik/adaylar.md` | Müzik/SFX: her dosya lisans kaydında, NC/ND yok |
| Paket taslağı | `thumbnail-tasarimcisi` + `youtube-paketleyici` (paralel) | 3 thumbnail konsepti (taslak) + 5 başlık varyantı, açıklama taslağı, etiketler, Shorts başlıkları | `09-paket/thumb-konsept.md`, `09-paket/paket-taslak.md` | Taslak: başlık ≤60 karakter, thumbnail metni ≤4 kelime |

Görsel kol **para harcar** (görsel API). Onaylı bütçe yoksa veya tavan aşılacaksa sahneler B planına geçer: kodla çizilen grafik/harita/sayaç sahneleri + mevcut karakter varlıkları. Durum Niyazi'ye F10'da raporlanır. Onaysız harcama yapılmaz.

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

Teslim `08-kurgu/final-16x9.mp4`, `08-kurgu/altyazi.srt`, `08-kurgu/shorts-1.mp4`, `08-kurgu/shorts-2.mp4`, `08-kurgu/kurgu-rapor.md`. Kapı: Kurgu, Altyazı, Ses (son dosyada) ve aşağıdaki Shorts kapısı.

### F8 — Son paket (paralel)
| Ajan | İş | Teslim | Kapı |
|---|---|---|---|
| `thumbnail-tasarimcisi` | Render karelerinden **3 thumbnail varyantı** (A/B/C, 1280x720) | `09-paket/thumbnail-A.png`, `09-paket/thumbnail-B.png`, `09-paket/thumbnail-C.png`, `09-paket/thumb-rapor.md` | Thumbnail: 168x94'te okunuyor, metin ≤4 kelime |
| `youtube-paketleyici` | Son başlık + 4 yedek, açıklama (kaynaklar, yasal not, lisans atıfları, AI ses notu), SEO, etiketler, hashtag'ler, **gerçek zamanlardan bölümler**, pinli yorum, Shorts paketleri, `yayin-paketi.json` | `09-paket/paket.md`, `09-paket/yayin-paketi.json` | Paket: başlık ≤60 karakter, bölümler gerçek zamanlara denk; JSON şema kapısı |
| `viralite-analisti` | Bitmiş paketin (başlık + thumbnail + ilk 15 sn) **viralite puanı**, F2 tahminiyle fark | `09-paket/viralite-son.md` | Viralite: betik 2 kez çalışıp aynı sonuç |

### F9 — Hakem son kontrol
`hakem` → bütün kapıları **kendisi yeniden ölçer** (ffprobe, ebur128, `tools/senkron-testi.py`, altyazı hizası, thumbnail küçültme, lisans kaydı, yasal not, Shorts kapısı). Karneyi doldurur. Teslim `hakem-raporu.md`: ONAY veya RED + düzeltme listesi. RED alan iş ilgili ajana döner (bölüm 1'deki döngü), sonra yeniden F9 yapılır.

### F10 — Teslim paketi ve Niyazi'ye sunum → DUR
Koordinatör `teslim/` klasörünü kurar (bkz. bölüm 3), `YAYIN.md`'yi yazar, commit/push eder ve Niyazi'ye **tek sayfa** sunar:
- Video başlığı, sütun, süre, hedef yayın slotu (ET + TRT).
- Viralite puanı (F2 tahmini → son), ilk 3 senaryonun puanları ve kazananın neden seçildiği (bilgi amaçlı, onay sorulmaz).
- Hakem kararı ve kapı tablosunun özeti.
- Riskler (doğrulama, politika, B planına geçen sahneler, harcanan bütçe).
- **Niyazi'nin yapacağı tek şey:** "Videoyu izle; `yayınla` ya da `şunu değiştir: …` de."

Niyazi'den yanıt gelmeden yayın adımına geçilmez.

### F11 — Yayın (yalnız Niyazi'nin açık onayıyla)
- Niyazi "yayınla / yükle / onay" derse koordinatör, **uretim-muhendisi'nin `tools/yayin/` aracıyla** `teslim/yayin-paketi.json`'u yükler. Aracın komutu ve parametreleri aracın kendi README'sinde tanımlıdır. Bu akış onu yalnız çağırır, kendi yükleme kodu yazmaz.
- Varsayılan: ana video **private + publishAt** (takvim slotu). Shorts takvimdeki kendi slotlarına zamanlanır. Thumbnail A yüklenir; B ve C, YouTube Studio "Test & Compare" için `YAYIN.md`'de Niyazi'ye bırakılır (API'de karşılığı doğrulanmadı).
- Araç yoksa veya API projesi denetimden geçmediyse (yüklemeler private'a kilitli) bu durum Niyazi'ye bildirilir ve elle yükleme adımları `YAYIN.md`'de verilir.
- Yükleme çıktısı (video ID'leri, planlanan saatler) `teslim/yayin-kaydi.json`'a yazılır. `docs/yayin-takvimi.md` stok tablosu güncellenir. Kararı `c-level-skills:decision-logger` biçimiyle `durum.md` sonuna yaz.
- Niyazi "şunu değiştir" derse değişiklik ilgili ajana gider (bölüm 1'deki döngü), F9 ve F10 tekrarlanır.
- Yayından 7 ve 28 gün sonra `kanal-analisti` performans verisini çıkarır. Bu veri `viralite-analisti` kalibrasyonuna girer.

## 3. Teslim paketi: `uretim/<tarih>-<slug>/teslim/`
| Dosya | Kaynak |
|---|---|
| `final-16x9.mp4` | kurgu-editoru (F7) |
| `shorts-1.mp4`, `shorts-2.mp4` | kurgu-editoru (F7) |
| `thumbnail-A.png`, `thumbnail-B.png`, `thumbnail-C.png` | thumbnail-tasarimcisi (F8) |
| `altyazi.srt` | kurgu-editoru (F7) |
| `yayin-paketi.json` | youtube-paketleyici (F8) |
| `hakem-raporu.md` | hakem (F9) |
| `YAYIN.md` | koordinatör (F10): tek sayfa özet |

`yayin-paketi.json` asgari şeması (yükleme aracıyla sözleşme; değişiklik uretim-muhendisi ile birlikte yapılır):
```json
{
  "surum": 1,
  "slug": "…",
  "uzun": {
    "dosya": "final-16x9.mp4", "baslik": "…", "aciklama": "…", "etiketler": ["…"],
    "kategori_id": "27", "dil": "en", "altyazi": "altyazi.srt",
    "thumbnail": "thumbnail-A.png", "thumbnail_yedek": ["thumbnail-B.png", "thumbnail-C.png"],
    "gizlilik": "private", "yayin_zamani_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "cocuklara_yonelik": false, "sentetik_icerik_beyani": false, "bolumler": [["0:00", "…"]]
  },
  "shorts": [
    {"dosya": "shorts-1.mp4", "baslik": "…", "aciklama": "…", "etiketler": ["…"], "yayin_zamani_utc": "…", "ilgili_video": "uzun"},
    {"dosya": "shorts-2.mp4", "baslik": "…", "aciklama": "…", "etiketler": ["…"], "yayin_zamani_utc": "…", "ilgili_video": "uzun"}
  ]
}
```
Kategori (27 = Education) ve sentetik içerik beyanı youtube-paketleyici'nin kararıdır. Bu değerler örnektir.

## 4. Ek kapılar (bu akışa özgü)
| Aşama | Test | Geçme ölçütü |
|---|---|---|
| Shorts | ffprobe + ilk 2 sn kare + altyazı güvenli alanı | 1080x1920, ≤60 sn, ilk 2 sn'de kendi kancası, metin alt %20'ye ve sağ kenar düğmelerine binmiyor, −14 LUFS ±1 |
| Ön doğrulama | 10 senaryo tablosu | her senaryoda YEŞİL/SARI/KIRMIZI + gerekçe |
| Yayın paketi | JSON ayrıştırma + dosya varlığı | JSON geçerli, adı geçen her dosya `teslim/` içinde, yayın zamanı takvim slotuna denk, başlık ≤60 karakter |
| Teslim paketi | dosya listesi | bölüm 3'teki 9 dosyanın hepsi var, hakem ONAY |

## 5. Ajan çağrı sırası (özet)
```
F0  koordinatör ‖ uretim-muhendisi
F1  trend-avcisi ‖ kanal-analisti
F2  senaryo-yazari → (viralite-analisti ‖ finans-dogrulayici) → hakem          [Niyazi onayı yok]
F3  senaryo-yazari → finans-dogrulayici                                       [metin kilidi]
F4  (ses-yonetmeni → ses-muhendisi) ‖ gorsel-varlik-sanatcisi ‖ muzik-ses-tasarimcisi ‖ (thumbnail-tasarimcisi ‖ youtube-paketleyici: taslak)
F5  animasyon-yonetmeni (10–20 sn test → tam)  ‖  F6 muzik-ses-tasarimcisi (miks)
F7  kurgu-editoru (16:9 + 2 Shorts)
F8  thumbnail-tasarimcisi ‖ youtube-paketleyici ‖ viralite-analisti
F9  hakem → F10 Niyazi'ye teslim → DUR → F11 yalnız onayla: tools/yayin/ (uretim-muhendisi aracı)
Her aşamada araç sorunu → uretim-muhendisi. 2 RED sonrası → koordinatör eskalasyonu; tekrarlayan sorun → ik-direktoru.
```
