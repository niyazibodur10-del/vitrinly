# F4 — Müzik ve SFX adayları · 1929-1000-dolar ("You Have $1,000 in 1929. Can You Keep It?")

**Sahip:** muzik-ses-tasarimcisi · **Tarih:** 2026-10-27 · **Girdi:** `03-metin/metin.md` (KİLİTLİ, 8 bölüm, ≈11:54)
**Lisans kaydı:** `06-muzik/lisans-kaydi.md`. Bu dosyadaki her aday orada kayıtlı. NC/ND/SA yok.
**Zamanlama:** F6'da kesin kelime zamanlarıyla (`04-ses/kelimeler.json`) cue listesi + ducking'li stem'ler hazırlanacak. Bu belgedeki bölüm sınırları metnin 143 kpm tahmini.
Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[kaynak]** kaynak sayfada okundu · **[tahmin]** yorum.

## Test kapısı (F4: "her dosya lisans kaydında, NC/ND yok") — **GEÇTİ** [ölçüm]
`python3 06-muzik/lisans-kontrol.py` → `dosya: 55 · kayıtsız: 0 [] · yasak lisans (kayıt bölümünde): []`, exit 0. İki koşu aynı sonucu verdi. Negatif test: kayıtsız sahte dosya eklenince exit 1 verdi, yani kontrol gerçekten yakalıyor. Lisans linkleri 2026-10-27'de HTTP 200 döndü. Kayıtta 3 CC BY (atıf metni hazır), geri kalanı CC0 ya da kendi üretimimiz.

## Özet: bölüm başına ön seçim (F6'da miksli dilim WER'i ile kesinleşir)

Müzikal fikir: **swing motifi**. Açılış 1920'ler swing'i (oyun şovu + dönem) ile başlıyor. 2026 ters köşesinde aynı deyimin modern hali (electro swing) geliyor: "aynı kapı, bugüne taşındı" müzikte de duyuluyor. Arada dönem rengi (rag) → gerilim → dip → kilit → sıcak kapanış.

| # | Bölüm (metin zamanı) | Ruh hali / tempo | Ön seçim | 2. | 3. | Not |
|---|---|---|---|---|---|---|
| B1 | Oyun şovu açılışı, S01–S04 (0:00–1:35) | oyunbaz, parlak swing | **Catchy Swing** (Doge, CC0) | Ragtime! Jazz (CC0) | Electro Swing type (CC0) → B7'ye ayrıldı | İlk 3 sn sepya kart müziksiz/oda tonu, kapılar açılınca swing girer (kapı-ışık SFX'iyle aynı karede) |
| B2 | Borsa kapısı, S05–S07 (1:35–3:15) | 1929 coşkusu → çöküş | **Ragtime! Jazz** (CC0; coşku, S05) → 2:14 "Nobody knows it yet"te **müzik keser** → **nabız yatağı** (kendi üretimimiz, S06 çöküş) | Osanpo Rag (CC BY 4.0) | 80s Mysterywave (pilot, CC0) | 3:13 "Right?" → `ozgun-gerilim-vurus` (metindeki "tek notalık gerilim vuruşu") |
| B3 | Banka paniği, S08–S11 (3:15–5:35) | yükselen panik | **Tension** (Komiku, CC0) | Backup Plan (Zane Little, CC0) | nabız yatağı (kendi) | Tension'ın LRA'sı 9.8: yükselen yapı panik kurgusuna uyuyor. F6'da ducking'le sabitlenecek. S11 abone anı: müzik 1 ölçü açılır |
| B4 | Kutu, S12–S14 (5:35–7:12) | muzip, sıcak, "beklenmedik" | **The Fridge is Hungry** (congusbongus, CC0) | Black Tea Rag (CC BY 4.0) | Osanpo Rag (CC BY 4.0) | Riskli nokta: ton (tracker sesi çocuksu kaçabilir). Kör dinlemede ikinci sıra (Black Tea Rag, honky-tonk 1929 rengi) güçlü rakip. İnsan kulağı kararı → hakem/Niyazi |
| B5 | Dip, Temmuz 1932, S15–S17 (7:12–8:42) | ağır, buruk | **At the end of hope** (Emma_MA, CC0) | dip drone (kendi) | Cold Silence (CC0) | Cold Silence "rahatsız edici" [kaynak]. Korku tonu kanal tonundan (merak + sıcaklık) sapıyor → 3. sıra |
| B6 | Mart 1933 kilit, S18–S19 (8:42–9:57) | mekanik gerilim, saat | **kilit-saat 100 BPM** (kendi) | Unsolved Investigation (pilot, CC0) | Tension (B3'te kullanılırsa elenir) | Zincir + asma kilit ×3 SFX bu yatağın ölçü başlarına oturtulacak. Radyo cızırtısı (Roosevelt silueti) altta |
| B7 | 2026 ters köşe, S20–S22 (9:57–11:06) | modern, hızlı, ironik | **Electro Swing type** (G_P, CC0) | The Way It Is (Zane Little, CC0) | Down to Business (pilot, CC0) | Swing motifinin modern dönüşü |
| B8 | Kapanış, S23–S24 (11:06–11:54) | sıcak, düşündürücü, umutlu | **Piano & Drums, positive melancholy** (Dizzy Crow, CC0) | Happy moments (CC0) | A New Start (CC0, 22 sn) | A New Start'ın konuşma bandı payı 0.246 (çok yüksek). Yalnız konuşma bittikten sonraki uç ekran kuyruğunda kullanılabilir |

Bu videoda **9 farklı parça** kullanılıyor, 7'si pilot dışı yeni parça. Kanal havuzu 3'ten **≥15 lisanslı parçaya** çıktı (`docs/monetizasyon.md` §7: "havuz ≥10" önerisi karşılandı).

## Ölçümler [ölçüm] (`aday-olc.py`, ham çıktı `olcum-muzik.jsonl`)
Yöntem: ebur128 (LUFS, LRA, TP) ve 16 kHz spektrum. **Konuşma bandı** = 1–4 kHz enerji payı (pilot eşiği ≤0.15). **Maske SNR** = müzik, konuşmanın 21 LU altına çekilip 30 sn anlatım örneğiyle (pilot `anlatici-v1.m4a`, −14.2 LUFS) karıştırıldığında konuşmalı karelerde 1–4 kHz konuşma/müzik oranının medyanı (yüksek = güvenli). **Kısa-süre std** = 3 sn ses yüksekliği dalgalanması (yatak için düşük iyi). BPM otokorelasyon tahmini, "?" = güvenilmez (alt sınıra yapıştı).

| Dosya | Süre sn | LUFS | LRA | TP dBTP | Konuşma bandı | Merkez Hz | BPM [tahmin] | Kısa-süre std dB | Maske SNR dB |
|---|---|---|---|---|---|---|---|---|---|
| catchy-swing-doge.ogg | 60.0 | -17.6 | 2.8 | -0.2 | 0.02 | 157 | ? | 1.0 | 31.8 |
| ragtime-jazz-tarush-singhal.mp3 | 111.9 | -18.0 | 3.8 | -0.5 | 0.087 | 404 | 103.4 | 1.3 | 20.7 |
| electro-swing-type-gp.mp3 | 82.3 | -11.3 | 1.9 | -0.0 | 0.047 | 388 | 69.8 | 0.7 | 22.1 |
| osanpo-rag-yubatake.ogg | 198.3 | -16.8 | 3.2 | 0.0 | 0.066 | 590 | 69.8 | 1.1 | 22.1 |
| black-tea-rag-decimnet.mp3 | 96.0 | -14.2 | 2.7 | -1.4 | 0.075 | 550 | 89.6 | 1.0 | 20.1 |
| tension-komiku.mp3 | 201.0 | -17.7 | 9.8 | -0.1 | 0.018 | 130 | ? | 3.5 | 34.8 |
| backup-plan-zane-little.ogg | 192.0 | -12.5 | 6.9 | 0.3 | 0.045 | 394 | 120.0 | 4.5 | 23.8 |
| fridge-is-hungry-congusbongus.ogg | 189.2 | -13.6 | 3.8 | 1.1 | 0.016 | 125 | ? | 1.4 | 31.4 |
| at-the-end-of-hope-emma-ma.mp3 | 183.0 | -15.7 | 3.1 | -2.8 | 0.038 | 285 | 107.1 | 4.4 | 29.0 |
| cold-silence-eponasoft.ogg | 354.9 | -18.1 | 6.8 | -4.4 | 0.012 | 144 | 109.1 | 3.6 | 30.8 |
| positive-melancholy-dizzy-crow.ogg | 64.0 | -11.6 | 4.5 | 0.5 | 0.019 | 280 | ? | 1.6 | 25.8 |
| happy-moments-centurion.ogg | 76.8 | -22.2 | 8.9 | -3.2 | 0.05 | 547 | 150.0 | 2.7 | 23.1 |
| a-new-start-wolfgang.ogg | 22.0 | -26.3 | 8.6 | -5.9 | **0.246** | 657 | 66.7 | 2.9 | 22.5 |
| the-way-it-is-zane-little.mp3 | 148.0 | -13.0 | 8.5 | -0.9 | 0.026 | 247 | 171.4 | 3.1 | 26.8 |
| (pilot) enerji-down-to-business-zane-little.mp3 | 45.3 | -13.6 | 6.8 | 0.0 | 0.067 | 791 | ? | 6.1 | 21.2 |
| (pilot) gerilim-80s-mysterywave-desertdev.ogg | 298.0 | -12.8 | 2.1 | -1.0 | 0.114 | 437 | 80.0 | 5.0 | 21.9 |
| (pilot) merak-unsolved-investigation-isaiah658.ogg | 48.0 | -21.0 | 2.3 | -9.2 | 0.006 | 262 | 120.0 | 0.8 | 34.8 |
| ozgun-yatak-nabiz-90bpm.flac | 64.0 | -15.7 | 2.0 | -3.0 | 0.001 | 78 | 89.6 | 0.7 | 39.9 |
| ozgun-yatak-dip-drone.flac | 60.0 | -15.4 | 7.8 | -3.0 | 0.0 | 131 | ? | 3.0 | 62.1 |
| ozgun-yatak-kilit-saat-100bpm.flac | 48.0 | -14.4 | 0.1 | -3.0 | 0.001 | 103 | 100.0 | 0.0 | 57.6 |
| ~~acid-detective-obscure-music.mp3~~ (elendi) | 175.6 | -6.9 | 7.5 | **+1.2** | 0.032 | 289 | 136.4 | **7.8** | 35.1 |
| ~~countdown-myocardial-infarction-gresser.mp3~~ (elendi: lisans) | 75.1 | -13.7 | 3.6 | 0.3 | 0.047 | 325 | 80.0 | 1.2 | 22.2 |

Okuma:
- Ön seçimlerin hepsi konuşma bandında ≤0.09, maske SNR ≥20 dB. Pilotta WER %0 veren Mysterywave'in değerleri (0.114 / 21.9 dB) bu aralıkta [ölçüm + pilot kıyası].
- En riskli ön seçim **Ragtime! Jazz** (0.087, 20.7 dB). Piyano melodisi orta bantta. F6'da konuşma altında −22…−24 dB'ye çekilmeli ve 2–4 kHz'de hafif oyuk açılmalı.
- TP > 0 olan dosyalar (Fridge, Positive Melancholy, Backup Plan) kırpılmış master. Miks kazancı −20 dB civarında olduğu için sorun çıkarmaz. Yine de F6'da tepe −3 dBFS'e indirilecek (pilot kuralı).
- **Kendi yataklarımızın zayıf yanı:** enerjinin %75–99'u 150 Hz altında. Telefon bandında (300 Hz–4 kHz) payları 0.00–0.04 (Catchy Swing 0.09, At the end of hope 0.23) [ölçüm]. Yani telefon hoparlöründe büyük ölçüde yalnız saat tıkırtısı duyulur. Bu yüzden B6'da kilit-saat **tek başına değil**, Unsolved Investigation'ın altına katman olarak önerilir. Nabız, B2'nin çöküş bölümünde (8–30 sn) kısa süreli kullanılır.

## Kör dinleme dosyaları (`dinleme/*.m4a`, her biri 3 × 20 sn, müzik konuşmanın 21 LU altında, −14.4 LUFS)
Anlatım örneği pilot sesi (bu videonun anlatımı henüz hazır değil). Sıra karıştırıldı. Anahtar `dinleme/anahtar.json`'da: **dinlemeden önce açmayın**.
`b1-oyun-sovu.m4a`, `b2-borsa-kapisi.m4a`, `b3-banka-panigi.m4a`, `b4-kutu.m4a`, `b5-dip-1932.m4a`, `b6-mart-1933-kilit.m4a`, `b7-2026-ters-kose.m4a`, `b8-kapanis.m4a`.
**Sınır:** Ben dinleyemiyorum. Ton uygunluğu yargıları kaynak açıklamaları, tür ve ölçüme dayanıyor [tahmin]. B4 (Fridge ve Black Tea Rag) ile B1 (Catchy Swing ve Ragtime) için insan kulağı belirleyici: hakem veya Niyazi 2 dakikada dinleyebilir.

## SFX adayları [ölçüm: `olcum-sfx.jsonl`, `olcum-sfx-tepe.txt`]
"Taban" = en sessiz %10 karenin tepeye göre seviyesi. −40 dB'den kötü olan kayıtlarda hışırtı duyulabilir. Sürekli sesler (buzzer, radyo) için bu ölçüt anlamsız.

| Görev (metindeki yeri) | Ön seçim | Alternatif(ler) | Gerekçe |
|---|---|---|---|
| Kapılar ışıkla açılır (S01, 0:03) | `ozgun-kapi-isik-acilis` (1.6 sn: süpürme + Do-Mi-Sol-Do parıltı) | `kapi-rubberduck-door_open_01` (taban −112 dB, temiz), `kapi-kenney-doorOpen_1/2` (taban −37/−39 dB, hışırtılı) | Oyun şovu kapısı ahşap kapı değil, ışık/parıltı sesi ister. Ahşap kapı katman olarak eklenebilir |
| Oyun şovu "ding" (doğru, kapı seçimi, ödül) | `ozgun-ding-oyunsovu`, `ozgun-ding-ding-dogru` | `ding-pwl-bell_ding1` (taban −80 dB) | Fupi "correct bell" elendi: merkez 138 Hz (alt uğultu) ve taban −13 dB |
| Buzzer / "yanlış" (S10 "GAMBLE", S20 ters köşe) | `ozgun-buzzer-yanlis` (0.75 sn, 92+97.5 Hz sapmalı testere) | — | OGA'da "buzzer" aramasında 0 sonuç çıktı. Tek aday kendi üretimimiz |
| Kural kartları pop (S04) | pilot `pop-pluck`, `pop-drop` (Kenney CC0) | — | Pilotta doğrulandı |
| Seyirci kahkahası (S04 "The studio audience laughs at Box Leo") | `kahkaha-nocturnal-vanguard-group_giggling` (CC0, 5.5 sn, taban −51 dB) | `alkis-leezh-applause-CCBY` (CC BY 3.0, 7.7 sn, atıf gerekli) | **Açık:** CC0 stüdyo kahkahası bulunamadı. Giggling küçük bir grup sesi. F6'da 3 kopya, ±2 yarım ton ve 30–80 ms kaydırmayla "kalabalık" yapılacak. Yetmezse YouTube Ses Kütüphanesi'nden (Studio'da ses efektleri) bir kahkaha efekti Niyazi tarafından indirilebilir [tahmin: kütüphanede kahkaha efekti var, doğrulanmadı] |
| Sayaç tıkı / sayı sayacı (büyük sayı grafikleri) | `ozgun-sayac-tikirti` (18/sn, sonda yavaşlar), `ozgun-saat-tik/tok` | `tik-bart-tick1/2` (taban −26/−29 dB → hışırtılı), `tik-bart-ticking_clock-dongu` (8 sn döngü) | Kendi tıklarımız temiz (taban −48 dB, tek tık) |
| Tek notalık gerilim vuruşu (S07 3:13, S17) | `ozgun-gerilim-vurus` (2.6 sn: düşen bas + La/Si♭ küme) | pilot `riser` önünde | Metnin istediği vuruş |
| Mühür "GAMBLE" (S10) | pilot `muhur-impact-punch` (Kenney CC0) | `kasa-kapisi-rubberduck-metal_slam_01` | Pilotta doğrulandı |
| Banka kasası kapısı (S07 sağ panel, S08–S09) | `kasa-kapisi-rubberduck-metal_open_01` / `metal_close_01` | `ozgun-kasa-kilit` (çark tıkırtısı + sürgü) | Gerçek metal kayıt daha inandırıcı. Kendi sentezimiz çark/şifre anı için |
| Rüzgâr + düşüş tonu (S14 "Let's jump to the bottom") | `ozgun-ruzgar-dusus` (2.8 sn, 880→110 Hz) | pilot `whoosh-uzun` | Metindeki "SFX: rüzgâr + düşüş tonu" birebir |
| Zincir + asma kilit ×3 (S18 üç kapı) | `zincir-rubberduck-chain_01/02/03` + `kilit-rubberduck-lock_01/02` (taban −106…−111 dB) | `kilit-kenney-metalLatch`, `ozgun-kasa-kilit` | Her kapıya farklı zincir dosyası (tekrar hissi olmasın). Kilit sesi zincirin 150–250 ms sonrasına |
| Radyo (S18 Roosevelt radyo silueti) | `ozgun-radyo-cizirti` (3 sn döngü, 300–3200 Hz hışırtı + çıtırtı + 60 Hz uğultu) | — | Anlatım sürerken −30 dB altına çekilir. Konuşma bandında olduğu için yalnız konuşma boşluğunda yükselir |
| Para / ka-ching (ödül anları, S10 "ilk büyük ödül") | `ozgun-ka-ching` | `para-kenney-handleCoins`, `para-rubberduck-item_coins_01`, pilot `para-coin-drop`, `para-kenney-chips-stack-1` | — |
| Geçiş whoosh / riser | pilot `whoosh-kisa`, `whoosh-uzun`, `riser` (kendi üretimimiz) | — | Pilotta doğrulandı |

## YouTube Ses Kütüphanesi (Audio Library) notu
- **API ile indirilemez.** YouTube Data API'nin Audio Library uç noktası yok. Kütüphane yalnız YouTube Studio → Ses Kütüphanesi'nde, oturum açmış kanal sahibine açık [genel bilgi; `docs/monetizasyon.md` §7 kaynağı B-K15 kütüphanenin Content ID açısından güvenli olduğunu söylüyor].
- **Seçenek (Niyazi, isteğe bağlı, ≈10 dk):** Studio → Ses Kütüphanesi → filtre "Atıf gerekmez", ruh hali "Funny/Bright" (B1/B4), "Dramatic/Dark" (B3/B5) ve "Inspirational" (B8). Her biri için 1 parça indirip `06-muzik/kaynak/yal/` altına koyarsa, F6'da aynı ölçümle (maske SNR, konuşma bandı) aday listesine girer. Content ID güvencesi en yüksek yol budur. Lisans kanıtı için kütüphane satırının ekran görüntüsü de `assets/lisans-kanit/` altına konmalı.
- Gelmezse plan değişmez: CC0 ve kendi üretimimiz ile ilerlenir, itiraz kanıtı hazır.

## Content ID risk özeti ve itiraz kanıtı
- **Sıfır risk:** kendi üretimimiz (3 yatak + 12 SFX, `ozgun-uret.py` ile yeniden üretilebilir; git geçmişi oluşturma kanıtı).
- **Düşük:** OGA'daki oyun jam CC0 parçaları (Catchy Swing, Ragtime! Jazz, Electro Swing, Fridge, At the end of hope, Positive Melancholy, Happy moments) ve Kenney/rubberduck SFX. Sayfalarında iddia/şikâyet notu yok [ölçüm: sayfa taraması].
- **Orta-düşük:** sanatçının akış platformlarında da dağıttığı parçalar (Komiku "Tension", Zane Little "Backup Plan" / "The Way It Is"). Web aramasında talep raporu çıkmadı [arama özeti]. Ama dağıtıcı üzerinden üçüncü kişi kaydı mümkün [tahmin].
- **İtiraz paketi (talep gelirse):** `lisans-kaydi.md` satırı + `assets/lisans-kanit/oga-<slug>.html` (2026-10-27 kopyası) + CC0 lisans metni + `kaynak/muzik-sha256.txt` ile dosya eşleşmesi. Hak iddia edenin kaydı CC0 eserin kendisiyse itiraz "public domain / CC0" gerekçesiyle yapılır. Kaydı bir remiks ya da cover ise parça değiştirilir (monetizasyon-uyum-uzmani F8'de son kontrolü yapar).

## Elenenler (gerekçeli)
Ayrıntı `lisans-kaydi.md` → "Değerlendirilip alınmayan". Kısaca: Countdown to Myocardial Infarction (lisans zinciri doğrulanamadı: FreePD kapandı, Wayback ağda engelli). Acid Detective (+1.2 dBTP kırpılmış master, 7.8 dB dalgalanma). Eric Matyas parçaları (soundimage özel lisansıyla çakışma). CC BY-SA parçalar (polka loopları, The Heist, Imminent Threat, Bank Heist). Karışık lisanslı parçalar. 1920'ler 78'lik kayıtları (Content ID riski). Fupi correct bell (uğultu). bart tıkları (hışırtı, kendi tıkımız temiz).

## F6 için açık işler
1. Bu videonun gerçek anlatımı (`04-ses/anlatim.wav`) üstünde her ön seçimle 20–30 sn miksli dilim → Whisper WER (anlatım-tek ±2 kelime) + konuşma varken/yokken seviye farkı (hedef −18…−24 dB).
2. B1 ve B4 için insan kulağı (kör dosyalar hazır). Sonuç gelmezse ölçüm sıralaması geçerli.
3. Kahkaha katmanı (giggling ×3) ya da YAL efekti.
4. Kazanan parçalar `assets/muzik/`e (≤5 MB) kopyalanacak ve `assets/LISANSLAR.md`'ye işlenecek. CC BY kullanılırsa atıf metni youtube-paketleyici'ye verilecek (açıklama).
5. Stem'ler: `06-muzik/stems/muzik-stem.wav`, `sfx-stem.wav` + `cue-listesi.md`. Son normalizasyon `tools/render-son.sh`'de yapılır.

## Dosyalar
- `adaylar.md` (bu dosya), `lisans-kaydi.md`
- `ozgun-uret.py` (kendi SFX/yataklarımız), `aday-olc.py` (ölçüm)
- `olcum-muzik.jsonl`, `olcum-sfx.jsonl`, `olcum-sfx-tepe.txt`, `efekt-sha256.txt`
- `kaynak/muzik/` (14 aday, ≈45 MB): 8 küçük dosya koordinatörün ara kaydıyla (010a37c) repoda. Geri kalan 6 dosya (ragtime-jazz, tension, at-the-end-of-hope, cold-silence, happy-moments, the-way-it-is) `.gitignore` ile **git dışı**; URL + sha256 ile yeniden indirilebilir (`kaynak/muzik-sha256.txt`, `kaynak/orijinal-sha256.txt`)
- `kaynak/efekt/` (26 CC0/CC BY efekt, 2.6 MB), `kaynak/ozgun/` (15 kendi üretimimiz, 5.6 MB)
- `dinleme/` (8 kör dinleme dosyası + anahtar)
