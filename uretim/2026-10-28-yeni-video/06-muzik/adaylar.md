# F4 (erken, F6a hazırlığı) — Müzik ve SFX adayları · S08 "If America Earned $5,400 a Month, Here's Its Budget"

İLERLEME: tamam (aday aşaması). Sıradaki: metin kilidi → bölüm sınırlarını `03-metin/metin.md` ile kesinleştir → ses kolu GEÇTİ olunca F6a (20–30 sn dilimde kör dinleme + Whisper WER + seviye).
**KARAR (ön seçim):** yeni ses kimliği **"mutfak masası lo-fi"**: Rhodes/elektrik piyano + yumuşak davul (sıcak, sakin), borç/faiz bölümlerinde pizzicato-celesta merakı ve synth gerilimi, kapanışta akustik sıcaklık. 1929'un swing/ragtime kimliği ve o videoda kullanılan 10 parçanın hiçbiri ilk sırada değil.
**Kapı:** `python3 -I lisans-kontrol.py` → `dosya: 30 · kayıtsız: 0 · yasak lisans: [] · cue kayıtsız: []`, **exit 0** (betik sha 347488d7dcf7). Negatif test: kayıtsız sahte dosya → exit 1. 14 OGA lisans sayfası + CC0 sayfası HTTP 200 (2026-11-02).
**Ölçüm:** ön seçimlerin hepsi konuşma bandı (1–4 kHz) ≤0.12, maske SNR ≥20 dB, telefon bandı ≥0.08 (`olcum-muzik.jsonl`, `olcum-tel-bant.tsv`; aday-olc sha 4953417d53e3, konuşma örneği `uretim/ses-testi/tts/anlatici-v1.m4a` sha e01a13e48372).
**Sınır:** ruh hali etiketleri kaynak sayfa açıklaması + ölçümden [tahmin]; kulak kararı F6a kör dinleme dosyasında verilir. Bölüm zamanları senaryo yapısından (12 dk), metin gelince kayar.
Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[kaynak]** kaynak sayfada okundu · **[tahmin]** yorum.

## Bölüm başına aday listesi

| # | Bölüm (senaryo zamanı) | Ruh hali / tempo [tahmin] | 1. | 2. | 3. | Not |
|---|---|---|---|---|---|---|
| B1 | Kanca + ölçek, tez (0:00–1:15) | merak + sıcak, ~98 BPM sabit yatak | **happy lofi day** (Tarush Singhal, Rhodes) | Chill lofi inspired (omfgdude) | Apple Cider (Zane Little) | İlk 2 sn: buzdolabı uğultusu (ortam) + "shrink" anında whoosh; yatak "kitchen table" kelimesinde girer. happy lofi day'in maske SNR'ı 20.3 dB (listenin en düşüğü): konuşma altında −22…−23 dB |
| B2 | Faturalar (1:15–3:00), ABONE-1 ~2:20 | hafif, sayan, ~90 BPM | **Jazz** (spring spring, 72 sn döngü) | Funky Hip Hop Lofi Jam, lowpass (omfgdude) | Lofi again (omfgdude) | Her fatura zarfı = kâğıt/zarf SFX'i. Lowpass sürüm konuşma bandı 0.013, en güvenli yedek |
| B3 | Kredi kartı / toplam borç (3:00–5:00) | hafif gerilim, meraklı | **Deliberate Concealment** (northivanastan; pizzicato + celesta, 3/4–5/8) | Unsolved Investigation (kanal, CC0) | 80s Mysterywave (kanal, CC0) | Deliberate Concealment konuşma bandı 0.114 (pilot eşiği 0.15 altında, ama celesta orta-üst bantta) → F6a'da 2–4 kHz oyuk + −23 dB |
| B4 | Faiz neden büyüyor (5:00–7:00), ABONE-2 ~6:15 | yükselen gerilim, nabız | **80s Mysterywave** (DesertDev; 1929 finalinde kullanılmadı) | Backup Plan (Zane Little, LRA 6.9 yükselen) | Keeping Cool (Holizna) | "Matruşka zarf" anı: `ozgun-zarf-kule` (3 tık, artan perde) her zarfta. Mysterywave konuşma bandı 0.114 / 21.9 dB, pilotta WER %0 |
| B5 | "Aile değil" farkları (7:00–9:00) | düşünceli, aydınlanan | **Lofi again** (omfgdude, Korg Triton) | Laundry On The Wire (Holizna; ev teması) | Chill lofi inspired | Laundry LRA 12.3 (dinamik): seçilirse sabit bir bölümü döngülenir |
| B6 | Üç olasılık (9:00–11:00) | ileriye bakan, dengeli | **The Way It Is** (Zane Little) | Slowly running (gameassets66; strings + keys + marimba) | Keeping Cool (Holizna) | Slowly running LRA 12.8 / std 6.6: yalnız sakin bölümünden kesit. Üç dalın her biri = `tik-select` + kart çevirme |
| B7 | Tez + kapanış köprüsü (11:00–12:00), ABONE-3 öncesi | sıcak, kapanış | **Apple Cider** (Zane Little, "cozy" [kaynak]) | A Small Fire Will Do (trex0n, sakin döngü) | Laundry On The Wire | Kapanış B1 Rhodes rengine geri döner (kimlik çemberi) |

**Müzikal fikir:** masa başı lo-fi açılış → borç bölümlerinde aynı sıcaklığın altına giren gerilim → "aile değil"de nefes → kapanışta sıcak akustik. Video boyunca buzdolabı uğultusu yalnız sahne geçişlerinde ve konuşmasız anlarda çok kısık (−40 dB altı), "aynı mutfak" hissi.
**Yeni parça sayısı:** 11 yeni CC0 parça indirildi. Kanal havuzu ≥26 lisanslı parça.

## SFX paleti (ilk videodan farklı: mutfak masası Foley'si)
| Olay (senaryo) | 1. | Yedek |
|---|---|---|
| Zarf/fatura açma | `zarf-spring-spring-snd_use_map` | `kagit-rubberduck-paper_02` |
| Fatura masaya / zarf kapanma | `zarf-spring-spring-snd_close_map` | `sayfa-starninjas-book_flip_2` |
| Hesap makinesi ile toplama | `ozgun-hesap-tus-dizi` (5 tuş) | `ozgun-hesap-tus` tekli |
| Buzdolabına yapışkan not | `ozgun-yapiskan-not` | `mutfak-rubberduck-switch_01` |
| Buzdolabı kapağı | `mutfak-rubberduck-microwave_door_open/close` | `assets/efekt/kapi-rubberduck-door_open_01` |
| Kupa / tabak masaya | `mutfak-rubberduck-dishes_02` | `dishes_01` |
| Zarf kulesi büyür (matruşka) | `ozgun-zarf-kule` | `assets/efekt/pop-pluck` ×3 |
| Büyük rakam belirmesi (5.400 / 7.400 / −2.000) | `assets/efekt/ozgun-ka-ching` (gelir), `muhur-impact-plate` (açık) | `pop-drop` |
| Geçiş / ölçek küçültme | `assets/efekt/whoosh-kisa`, `whoosh-uzun`, `riser` | — |
| Abone ol tıklaması | `assets/efekt/ozgun-fare-klik.flac` (kanal kaydında) | — |

SFX ölçümü (`olcum-sfx.jsonl`) [ölçüm]: hepsi tepe −3.0 dBFS. `kagit-rubberduck-paper_01/02` gürültü tabanı −23/−24 dB (kayıt hışırtısı): yalnız konuşmasız anda veya yedek. Diğer CC0 dosyalar ≤−33 dB, kendi sentezlerimiz ≤−100 dB.

## Ölçümler [ölçüm]
| Dosya | Süre sn | LUFS | LRA | TP | Konuşma bandı | Telefon bandı | BPM [tahmin] | Kısa-süre std | Maske SNR dB |
|---|---|---|---|---|---|---|---|---|---|
| happy-lofi-day | 116.4 | −16.2 | 1.7 | −1.0 | 0.071 | 0.211 | 98 | 0.6 | 20.3 |
| chill-lofi-inspired | 123.2 | −16.1 | 8.5 | +0.1 | 0.008 | 0.285 | 105 | 5.2 | 41.4 |
| funky-lofi-jam-lowpass | 189.3 | −18.6 | 2.2 | −5.8 | 0.013 | 0.155 | 85 | 2.6 | 36.9 |
| lofi-again | 87.8 | −19.5 | 3.9 | −0.6 | 0.011 | 0.179 | ? | 1.3 | 33.1 |
| deliberate-concealment | 157.0 | −19.7 | 6.3 | −0.7 | 0.114 | 0.388 | 103 | 2.1 | 34.8 |
| apple-cider | 199.8 | −14.8 | 6.6 | +0.1 | 0.043 | 0.118 | 100 | 4.9 | 31.2 |
| a-small-fire-will-do | 64.0 | −22.1 | 3.4 | −7.3 | 0.004 | 0.181 | ? | 1.2 | 33.9 |
| jazz (spring spring) | 72.0 | −18.7 | 3.9 | −3.4 | 0.064 | 0.177 | 90 | 1.3 | 29.0 |
| slowly-running | 300.5 | −22.6 | 12.8 | −7.0 | 0.002 | 0.212 | ? | 6.6 | 25.8 |
| laundry-on-the-wire | 179.9 | −17.2 | 12.3 | +0.2 | 0.065 | 0.125 | 80 | 4.4 | 35.0 |
| keeping-cool | 153.1 | −11.2 | 4.5 | +0.7 | 0.019 | 0.126 | 83 | 6.6 | 41.1 |
| (kanal) unsolved-investigation / 80s-mysterywave / down-to-business | — | (1929 `olcum-muzik.jsonl`, sha aynı, yeniden ölçülmedi) | | | 0.006 / 0.114 / 0.067 | 0.274 / 0.238 / 0.253 | | | 34.8 / 21.9 / 21.2 |
| (1929 havuzu) backup-plan / the-way-it-is | — | aynı | | | 0.045 / 0.026 | 0.090 / 0.092 | | | 23.8 / 26.8 |

TP > 0 olanlar (chill-lofi, apple-cider, laundry, keeping-cool) kırpılmış master; miks kazancı ~−20 dB olduğundan sorun yok, F6a'da tepe −3 dBFS kuralı uygulanır.

## Yeniden üretim
- Müzik (git dışı): lisans-kaydi.md'deki linklerden indir; zip/orijinal sha256 `orijinal-sha256.txt`, son dosyalar `muzik-sha256.txt`. WAV → `ffmpeg -c:a libvorbis -q:a 5`.
- Efekt: repoda (FLAC). Kendi sentezler: `python3 -I ozgun-uret.py`.
- Ölçüm: `nice python3 -I aday-olc.py muzik ../../ses-testi/tts/anlatici-v1.m4a kaynak/muzik/*`, `python3 -I tel-bant.py <dosyalar>`, `python3 -I aday-olc.py sfx kaynak/efekt/* kaynak/ozgun/*`.
