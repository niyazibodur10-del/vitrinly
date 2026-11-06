# Yapay zekâ anlatıcı + müzik/efekt: test raporu (2026-10-26, ses-muhendisi)

Niyazi kararı: anlatıcı artık ücretsiz, ticari kullanıma açık bir yapay zekâ sesi; videoya ücretsiz kütüphaneden müzik ve efekt eklenecek.
Test metni: pilot açılış metni (120 kelime, `anlatici-v1-metin.txt`, okuma-metni.md'deki P01–P05 paragrafları).
Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[kaynak]** birincil kaynaktan doğrulandı · **[tahmin]** yorum veya çıkarım.

## Sonuç
- **Kazanan:** Kokoro-82M `am_michael`, hız 0.95, cümle bazlı üretim ve doğal duraklamalar. Dosyalar: `anlatici-v1.wav` (48 kHz mono, git dışı), `anlatici-v1.m4a` (192k).
- **Yedek:** Kokoro `am_fenrir`, hız 0.9. Daha parlak ve daha enerjik; michael fazla sakin bulunursa bu kullanılır.
- **Müzik:** ana alt müzik "Unsolved Investigation" (CC0). Gerilim bölümleri için "80s Mysterywave" (CC0), giriş/kapanış için "Down to Business" (CC0).
- **Efekt:** whoosh ×2 ve riser kendi üretimimiz. Pop/tık ve mühür vuruşu Kenney'den (CC0). Klavye, daktilo ve madeni para OpenGameArt'tan (CC0).
- **Örnek miks:** `miks-ornek.m4a`: **−13.9 LUFS, true peak −3.7 dBTP, LRA 2.0** [ölçüm]. Müzik konuşmanın altında medyan **21.7 dB** aşağıda. Miksin üstünde Whisper hata oranı **%0**.

## A) Anlatıcı sesi

### Adaylar ve lisans
| Motor | Lisans | Durum |
|---|---|---|
| Kokoro-82M (11 erkek ses: am_michael, am_fenrir, am_puck, am_onyx, am_echo, am_eric, am_liam, bm_george, bm_fable, bm_lewis, bm_daniel) | Apache-2.0 ağırlıklar + sesler [kaynak: HF model kartı `license: apache-2.0`; VOICES.md'de CC BY sütunu yalnız Japonca/Fransızca seslerde var] | yerel, ücretsiz |
| Piper `en_US-joe-medium` | veri seti CC0 [kaynak: MODEL_CARD] | aday |
| Piper `en_US-john-medium`, `norman-medium`, `bryce-medium` | veri seti public domain [kaynak: MODEL_CARD] | aday |
| Piper `en_US-ryan-high` | veri seti **CC BY-NC-SA 4.0** | ticari değil, **baştan elendi** |
| Piper `en_GB-northern_english_male` (CC-BY-SA), `en_GB-alan` (lisans belirsiz) | — | elendi |
Piper motoru (piper-tts 1.8) GPL-3.0'dır. Bu yalnız aracın lisansı; ürettiği ses GPL kapsamına girmez [tahmin, yaygın yorum]. `trust_remote_code` gerektiren model kullanılmadı.

### Test 1: tek parça üretim, hız 1.0 (15 aday + insan kıyası) [ölçüm]
WER = Whisper medium.en kelime hata oranı (120 kelime). kpm = kelime/dk. f0 = perde ortalaması. f0 std = perde değişkenliği (yarım ton; düşük değer monoton demek). Merkez = spektral merkez (yüksek = parlak, düşük = koyu). Güven = Whisper ortalama kelime olasılığı.

| Aday | WER | kpm | f0 Hz | f0 std | Merkez Hz | Güven | Kokoro notu [kaynak] | Karar |
|---|---|---|---|---|---|---|---|---|
| am_michael | 0.0 | 167 | 117 | 3.32 | 1912 | 0.970 | C+ (B kalite, saatlerce veri) | **finalist** |
| am_fenrir | 0.0 | 211 | 138 | 3.62 | 1810 | 0.966 | C+ | **finalist** |
| am_puck | 0.8 | 221 | 114 | 3.13 | 1651 | 0.963 | C+ | finalist |
| am_echo | 0.0 | 205 | 112 | 3.00 | 1571 | 0.968 | D (dakikalarca veri) | elendi: düşük not |
| am_liam | 0.0 | 218 | 134 | 3.51 | 1894 | 0.970 | D | elendi: düşük not |
| am_eric | 0.0 | 232 | 157 | 3.16 | 1662 | 0.971 | D | elendi: en hızlı, en az duraklama (6), yüksek perde |
| am_onyx | 0.8 | 213 | 86 | **1.46** | **1054** | 0.962 | D | elendi: monoton ve boğuk, "enerjik" değil |
| bm_george | 0.8 | 174 | 139 | 2.81 | 1867 | 0.975 | C | elendi: "We'll" → "We" |
| bm_fable | 0.8 | 204 | 120 | 3.64 | 1892 | 0.970 | C | elendi: "We'll" → "We" |
| bm_lewis | 0.8 | 168 | 94 | 4.24 | 1679 | 0.959 | D+ | elendi: "We'll" → "We" |
| bm_daniel | 0.8 | 211 | 122 | 2.26 | 1684 | 0.965 | D | elendi: "We'll" → "We", düz tonlama |
| piper_bryce | 0.8 | 137 | 138 | 2.76 | 1853 | 0.961 | — | elendi (aşağıda) |
| piper_joe | 1.7 | 178 | 109 | 5.20 | 1514 | 0.962 | — | elendi: carried→carry, cost→costs |
| piper_john | 1.7 | 154 | 122 | 3.53 | 2245 | 0.947 | — | elendi: bubbles→baubles, bold→bull |
| piper_norman | 1.7 | 181 | 113 | 3.23 | 1544 | 0.942 | — | elendi: "what if"→"witted" |
| *(kıyas) Niyazi birleşik v2* | 10.0 | 94 | 106 | 2.21 | 2060 | 0.883 | — | — |

Eleme gerekçeleri:
- **İngiliz aksanlı (bm_) sesler:** 4 sesin 4'ünde de "We'll look at" ifadesi "We look at" diye duyuluyor. Bu sistematik bir telaffuz hatası. Ayrıca küresel genç kitle için Amerikan anlatıcı daha güvenli [tahmin].
- **Piper:** içerik kelimelerinde hata var (bubbles, bold, what if, carried) ve güven en düşük grupta (0.942–0.962). Modeller "medium" kalite, 22 kHz (bant 11 kHz'te kesiliyor).
- **Kokoro D notlu sesler:** model sahibinin notu az eğitim verisini gösteriyor. Uzun videoda (10+ dk) tını tutarsızlığı riski var [tahmin, nota dayanarak].
- Hiçbir aday 150 kelime/dk hedefinde değil: Kokoro tek parça üretimde çok hızlı (~205–230). Çözüm aşağıda.

### Test 2: cümle bazlı üretim + duraklama + hız taraması (finalistler) [ölçüm]
`tools/ses/tts.py` metni cümlelere böler ve aralara duraklama ekler: cümle 0.30 sn, soru 0.40, "..." 0.55, paragraf 0.65.

| Aday | Hız | Süre sn | kpm | f0 Hz | f0 std | Güven | "Financial" güveni | Not |
|---|---|---|---|---|---|---|---|---|
| am_michael | 0.9 | 48.6 | 146 | 121 | 3.29 | 0.966 | 0.89 | |
| am_michael | **0.95** | 47.0 | 151 | 122 | 3.30 | **0.975** | 0.85 | |
| am_michael | 1.0 | 45.7 | 155 | 121 | 3.27 | 0.971 | 0.72 | "No" → "videos" |
| am_michael | 1.1 | 43.5 | 163 | 121 | 3.30 | 0.960 | **0.45** | "No" → "videos" |
| am_fenrir | 0.9 | 43.5 | 163 | 153 | 4.38 | 0.963 | 0.79 | |
| am_fenrir | 1.0 | 41.0 | 173 | 153 | 4.37 | 0.963 | 0.86 | |
| am_fenrir | 1.1 | 39.0 | 182 | 153 | 4.36 | 0.958 | — | "We'll" düştü |
| am_puck | 0.9 / 1.0 / 1.1 | 42.9 / 40.1 / 37.9 | 167 / 178 / 188 | 125 | 3.5 | 0.963–0.972 | 0.67 (0.9) | hep hızlı |
| michael+fenrir karışımı | 0.9 / 1.0 | 45.6 / 43.0 | 156 / 165 | 137 | 3.9 | 0.971 | — | "No" → "news" / "It's" |

Bulgular:
- **Hız perdeyi değiştirmiyor**, yalnız tempoyu değiştiriyor (f0 her hızda sabit) → hız ayarı tınıyı bozmuyor.
- **Hız arttıkça kanal adının tanınma güveni düşüyor** (0.89 → 0.85 → 0.72 → 0.45). Kanal adı her videoda geçeceği için kazanan ayarı 0.95.
- "No boring charts." cümlesinin başı 3 varyantta "news/videos" diye duyuldu. Neden benim kırpmamdı: cümle başında 5 ms pay bırakılıyordu, bu da yumuşak /n/ başlangıcını kesiyordu. Pay 30 ms'ye çıkınca hata kayboldu (v2 testi, aşağıda).
- İzole kanal adı testi ("Welcome to Financial Rise! This is Financial Rise…"): 3 finalistte de doğru tanındı, güven 0.68–0.98.

### Test 3: düzeltilmiş araç + pilot paragrafları (nihai aday) [ölçüm]
| Aday | Süre | kpm | WER | Güven | Düşük güvenli kelime |
|---|---|---|---|---|---|
| **am_michael 0.95 (kazanan)** | 49.4 sn | 144 | **%0** | 0.964 | 3 |
| am_michael 1.0 | 48.0 sn | 148 | %0 | 0.964 | 5 ("financial" 0.41) |
| am_fenrir 0.9 (yedek) | 45.9 sn | 155 | %0 | 0.967 | 2 |
Not: 144 kelime/dk bu kısa metindeki paragraf duraklamalarını da içeriyor. 10 dakikalık metinde paragraf oranı düşük olacağı için hedef 150'ye yaklaşır; gerekirse `--paragraf 0.5` [tahmin].

### Kazananın son dosyası `anlatici-v1.wav` / `.m4a` [ölçüm]
| Ölçüm | Değer | Hedef |
|---|---|---|
| Ses yüksekliği (ebur128) | −14.1 LUFS (m4a −14.2) | −14 ±1 ✅ |
| True peak | −1.5 dBTP (m4a −1.4) | ≤ −1 ✅ |
| LRA | 1.9 LU | — |
| Gürültü tabanı (cümle arası 14 boşluğun RMS'i) | dijital sessizlik (−∞); astats RMS trough −89 dB | uğultu yok ✅ |
| Whisper medium.en | WER %0 (120/120), ort. güven 0.962 | ✅ |
| Biçim | 48 kHz mono 24-bit WAV, 49.36 sn; m4a AAC 192k | ✅ |
Zincir (`tools/ses/tts-son.sh`): highpass 70 Hz → hafif de-ess → kompresör (2.5:1, −24 dB) → kazanç → sınırlayıcı (−2 dBFS) → 2 geçişli doğrusal loudnorm (−14, TP −1.5).
Kompresör eklenmesinin nedeni: ilk denemede Kokoro'nun tepe/ortalama oranı ~23 dB çıktı. Doğrusal loudnorm, TP sınırını korumak için −14.9 LUFS'ta kaldı. TP −1.5 seçilmesinin nedeni: AAC kodlaması tepeyi −1.0'dan −0.9'a taşıdı.
Gürültü giderme uygulanmadı: TTS çıktısı zaten temiz, gereksiz işlem artefakt yapar.

Kelime zamanlı transkript (altyazı ve Rhubarb dudak senkronu girdisi): `anlatici-v1-kelimeler.json` (118 kelime, s/e/p alanları).
Cümle zaman çizelgesi (kurgu ve efekt yerleştirme için): `anlatici-v1.zaman.json`.

### Dinleme örnekleri `adaylar/` (hepsi −14 LUFS'a eşitlenmiş, AAC 96k)
01–08 tek parça (michael, fenrir, puck, onyx, eric, george, piper joe, piper john) · **10 KAZANAN** michael 0.95 · 11 michael 1.0 · **12 YEDEK** fenrir 0.9 · 13 michael+fenrir karışımı.
13 numara eski kırpma payıyla (5 ms) üretildi, "No" hatası o yüzden. Karışım ses kimseyle paylaşılmayan özgün bir tını verir; ileride değerlendirilebilir.

**Sınır:** Ben dinleyemiyorum. Tını seçimi ölçülebilir göstergelere ve model sahibinin notlarına dayanıyor. "Sıcak, güven veren, enerjik" yargısının son sözü insan kulağında: Niyazi ve hakem 10 ile 12'yi dinleyip karar vermeli.
Göstergelerin yorumu [tahmin]: michael 121 Hz bariton, yani sıcak ve güven veren. Perde değişkenliği 3.3 yarım ton, Niyazi'nin kendi okumasındaki 2.2'den daha canlı. Fenrir 153 Hz ve 4.4 yarım ton ile daha genç ve enerjik ama daha az "güven veren".

## B) Müzik ve efekt
Erişim: OpenGameArt ve kenney.nl açık. archive.org araması gürültülü sonuç verdi (podcastler, lisans etiketleri tutarsız), kullanılmadı. Yalnız CC0 alındı; CC-BY'ye gerek kalmadı.
Ayrıntılı lisans kaydı: `assets/LISANSLAR.md`. Lisans sayfalarının o günkü kopyaları: `assets/lisans-kanit/`.

### Müzik adayları [ölçüm]
"Konuşma bandı" = 1–4 kHz enerji payı (yüksekse anlatımı maskeler). "Fark" = aynı anlatımla miks edildiğinde konuşma altında müzik farkı (K-ağırlıklı, medyan). WER = miks üstünde Whisper.

| Parça (CC0) | Süre | LUFS / LRA | Konuşma bandı | Fark dB | WER | Karar |
|---|---|---|---|---|---|---|
| Unsolved Investigation (isaiah658) | 48 sn, kesintisiz döngü | −21.0 / 2.3 | 0.01 | 21.7 | 0 | **ana alt müzik**: "diyalog altında kalsın diye" bestelenmiş [kaynak: açıklama], gizem tonu 1923 kancasına uyuyor |
| 80s Mysterywave (DesertDev) | 4:58 | −12.8 / 2.1 | 0.12 | 22.7 | 0 | **seçildi**: uzun, sabit, modern synth gerilim; kriz bölümleri |
| Down to Business (Zane Little Music) | 45 sn | −13.6 / 6.8 | 0.06 | 22.9 | 0 | **seçildi**: "business 80's synth", giriş/kapanış enerjisi |
| Tension (Komiku) | 3:21 | −17.7 / 9.8 | 0.02 | 26.0 | 0 | yedek, indirilmedi (boyut; dinamik aralık yüksek) |
| Continued Investigation (section31) | 3:00 | −12.8 / 7.4 | 0.23 | 27.0 | 0 | elendi: konuşma bandı yoğun, yazarın ilk denemeleri |
| Investigation (wipics) | 27 sn | −12.5 / 4.4 | **0.31** | 22.7 | 0 | elendi: konuşma bandını en çok dolduran; döngüde boşluk |
| The Y Files (TAD) | 58 sn | −16.2 / 15.1 | 0.11 | — | — | elendi: bilinen dizi temasının parodisi → melodi benzerliği ve Content ID riski |
| Midnight Drive, Chill Lofi | — | — | — | — | — | elendi: tempo/dinamik dalgalanma (8.5–11 dB), tona uymuyor |
Müzik dosyaları toplam 8.1 MB (≤5 MB/parça ✅; Mysterywave 11.9 MB MP3'ten Vorbis q3'e çevrildi → 4.3 MB).

### Efektler [ölçüm: süre, SNR, gürültü tabanı]
| Görev | Seçilen | Neden / elenen |
|---|---|---|
| Whoosh | `whoosh-kisa` (0.45 sn), `whoosh-uzun` (0.9 sn), `riser` (1.6 sn): **kendi sentezimiz** (`tools/ses/efekt-uret.py`) | Lisans riski sıfır. Frekans taraması (430 → 2270 → 850 Hz) ve soldan sağa pan ölçümle doğrulandı. Elenen: "Air whoosh" (SNR 19.6 dB, gürültülü 5 sn döngü), "Swishes" (0.1–0.2 sn kılıç sesi) |
| Pop/tık | `pop-pluck`, `pop-drop`, `tik-select`, `tik-click` (Kenney) | temiz, kısa (0.02–0.06 sn aktif) |
| Mühür vuruşu | `muhur-impact-punch` (SNR 57 dB), `muhur-impact-plate` (Kenney) | "impactWood/Soft" gürültü tabanı yüksek (−40 dB) |
| Yazı sesi | `yazi-klavye` (SM7B kaydı, SNR 64 dB), `yazi-daktilo` (SNR 52 dB) | daktilo telefonla kaydedilmiş; kısa vuruşta yeterli |
| Bonus (para) | `para-coin-drop` (SNR 95 dB) | finans temasına uygun |
Hepsi 48 kHz FLAC, tepe −3 dBFS'e eşitlendi; toplam 736 KB.

### Content ID riski [tahmin]
- CC0 parçaların hak sahibi yoktur, ama üçüncü kişiler zaman zaman CC0 müziği Content ID'ye kaydettirebiliyor. Haksız talep gelirse itiraz için kaynak URL'leri ve lisans sayfası kopyaları `assets/lisans-kanit/` altında duruyor.
- OpenGameArt oyun müziği kütüphanesi. Pixabay/YouTube Audio Library'ye göre YouTube'da daha az kullanılıyor; çakışma ihtimali düşük ama sıfır değil.
- Önlem: açıklamaya gönüllü atıf satırı (`LISANSLAR.md`). Videoyu yayımlamadan önce "liste dışı" yükleyip Content ID taraması beklenebilir (yükleme Niyazi onaylı).
- En düşük risk kendi üretimimiz. Efektlerin bir kısmı zaten öyle. Müziğin de ileride kendi üretimimiz olması (ör. lisanslı yerel müzik modeli) ayrı bir iş olarak değerlendirilebilir.

## C) Örnek miks `miks-ornek.m4a` (54.4 sn, stereo AAC 192k) [ölçüm]
İçerik: 2 sn müzik girişi, ardından kazanan anlatım ve 3 sn kapanış; altta Unsolved Investigation, ducking'li. 8 efekt kullanıldı: giriş whoosh'u, "1923"te daktilo, "wheelbarrows"ta para, "Welcome" öncesi riser + mühür, iki "No…"da pop, "So..."da kısa whoosh. Zamanlar `anlatici-v1.zaman.json`dan alındı.
Araç: `tools/ses/miks.py` (yatak −20 LUFS, sidechain 2:1, son stereo dosyada 2 geçişli loudnorm).

| Ölçüm (son dosyada ebur128) | Değer | Hedef |
|---|---|---|
| Ses yüksekliği | **−13.9 LUFS** | −14 ±1 ✅ |
| True peak | **−3.7 dBTP** | ≤ −1 ✅ |
| LRA | 2.0 LU | — |
| Konuşma altında müzik farkı (medyan / p10–p90) | **21.7 dB** / 15.4–25.0 | −18…−24 ✅ (medyan) |
| Miks üstünde Whisper WER | **%0**, güven 0.970 | anlaşılırlık korunuyor ✅ |
Ayar denemeleri: yatak −6/−9 dB ve duck 6/9 kombinasyonları denendi; medyan farklar 21.4 / 27.8 / 24.4 / 30.8 dB. −6/6 seçildi: aralığın ortası, müzik duyulur kalıyor.
p10 = 15.4 dB, yani cümle uçlarında müzik kısa anlarda 15 dB'ye kadar yaklaşıyor (sidechain release 450 ms). Kurguda rahatsız ederse `--duck-db 8`.

## D) Riskler

### YouTube "AI Personas Related to Sensitive Topics" kuralı [kaynak]
Kaynak: support.google.com/youtube/answer/1311392, 2026-10-26 erişim. Kural metni: kendini insan uzman gibi sunarak sağlık, hukuk, **finans** veya siyaset konusunda tavsiye veren yapay zekâ personası kullanan kanallar **para kazanamaz**. Örnek: *"AI-generated podcast hosts offering financial guidance, investment tips, or wealth management advice"*.
Aynı sayfada izin verilenler: *"using AI to visualize a unique character and narrative you invented"*. Sayfada bu bölümün yürürlük tarihi görünmüyor; "Temmuz 2026" bilgisini doğrulayamadım. Aynı sayfadaki "inauthentic content" (seri üretim, şablon) kuralının tarihi 15 Temmuz 2025.

Bizim önlemlerimiz:
1. **Karakter açıkça çizgi film maskotu**: gerçekçi insan değil, "uzman, danışman, finansçı" unvanı kullanılmaz, "ben bir yatırım uzmanıyım" gibi cümle yok. (senaryo-yazari + finans-dogrulayici kontrol listesine)
2. **Tavsiye yok, anlatı var**: "al/sat/şuna yatır" yok. Gelecek "senaryo" diye sunulur. Videoda ve açıklamada "not financial advice / educational entertainment" notu bulunur.
3. **Şeffaflık**: açıklamaya "Narration: synthetic AI voice (Kokoro TTS). Character and story are original." satırı. YouTube'un sentetik içerik sayfasına göre (answer/14328491) açıklama zorunluluğu gerçekçi içerik için. Bizim animasyonumuz gerçekçi değil, ama "AI use = Yes" işaretlemek "tek başına izlenmeyi veya para kazanmayı etkilemez" [kaynak]. **Öneri: işaretlensin** (karar youtube-paketleyici + Niyazi).
4. **Seri üretim görüntüsünden kaçınma** (inauthentic content): her video ayrı araştırma ve özgün metin, insan onayı (Niyazi). Aynı intro serbest ama gövde her videoda farklı.

### Diğer riskler
- **Ses tanınırlığı [tahmin]:** Kokoro am_michael ücretsiz ve popüler, başka kanallarda da duyulabilir, bu da özgünlük algısını zayıflatır. Önlem: karakter, müzik ve efekt imzası özgün. Gerekirse özgün karışım ses (13) ayrıca test edilir.
- **Uzun metin tutarlılığı:** pilot 49 sn. 10 dakikalık metinde tını ve tempo kayması henüz ölçülmedi. İlk tam metinde `ses-olc.py` ile dakika dakika f0/kpm kontrolü yapılmalı.
- **Telaffuz:** Kokoro misaki G2P sözlük dışı kelimede espeak'e düşer. Özel isimler ve rakamlar ("1923", şirket adları) her metinde Whisper ile kontrol edilmeli. Gerekirse metinde fonetik yazım kullanılır (`[Kokoro](/kˈOkəɹO/)` sözdizimi).
- **Alan sınırı:** müzik/efekt seçimi ve miks normalde `muzik-ses-tasarimcisi`nin alanı. Bu iş koordinatör ataması ile yapıldı; o ajanın gözden geçirmesi önerilir.

## Kalıcı araçlar (`tools/ses/`)
- `tts.py`: Kokoro cümle bazlı seslendirme. Duraklama, hız, ses karışımı (`a+b`) parametreleri var; `.zaman.json` çıkarır.
- `tts-son.sh`: TTS → 48 kHz mono, −14 LUFS, TP −1.5 (+ isteğe bağlı m4a).
- `ses-olc.py`: perde (YIN), perde değişkenliği, spektral merkez, kelime/dk, Whisper güveni.
- `miks.py`: anlatım + ducking'li müzik + efekt → stereo m4a. Son dosyada loudnorm; konuşma/müzik farkını ölçer.
- `efekt-uret.py`: kendi whoosh/riser efektlerimiz (tekrarlanabilir).
Yeniden üretim:
```
tools/ses/tts.py uretim/ses-testi/tts/anlatici-v1-metin.txt ham.wav --ses am_michael --hiz 0.95
tools/ses/tts-son.sh ham.wav uretim/ses-testi/tts/anlatici-v1.wav uretim/ses-testi/tts/anlatici-v1.m4a
```
(Kokoro ortamı: `pip install kokoro soundfile`, Python 3.12, torch CPU.)
