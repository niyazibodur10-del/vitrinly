# F4 (erken, F6a hazırlığı) — Müzik ve SFX adayları · S03 "The Biggest Inheritance Ever, and Why Heirs Might Miss It"

İLERLEME: tamam (aday aşaması). Sıradaki: metin kilidi → bölüm sınırlarını `03-metin/metin.md` ile kesinleştir → ses kolu GEÇTİ olunca F6a (20–30 sn dilimde kör dinleme + Whisper WER + seviye). F6b: `animasyon-efekt-cue.json` gelince SFX.
**KARAR (ön seçim):** yeni ses kimliği **"yoldaki nakliye kamyonu"**: akustik/elektro gitar yol müziği (vitalezzz, Komiku) + sıcak, hafif caz-pop (Pro Sensory); sızıntı bölümlerinde seyrek, karanlık-sessiz yatak (yd "Insistent"). 1929 (swing/ragtime) ve S08 (mutfak lo-fi) paletinden hiçbir parça ilk sırada değil. S08'den yalnız 2 kanıtlı parça yedekte: Deliberate Concealment (B3/B6), The Way It Is (B7).
**Kapı:** `python3 -I lisans-kontrol.py` → `dosya: 27 · kayıtsız: 0 · yasak lisans: [] · cue kayıtsız: []`, **exit 0** (betik sha 51295990f8b7, S08 v2'nin kopyası). Negatif test: kayıtsız sahte dosya → exit 1. 15 OGA kaynak sayfası + CC0 sayfası HTTP 200 (2026-11-04).
**Ölçüm:** ön seçimlerin hepsi konuşma bandı (1–4 kHz) ≤0.13, maske SNR ≥22 dB, telefon bandı ≥0.15 (`olcum-muzik.jsonl`, `olcum-tel-bant.tsv`; aday-olc sha 4953417d53e3, konuşma örneği `uretim/ses-testi/tts/anlatici-v1.m4a` sha e01a13e48372). Ruh hali ipucu: `tools/earshot rank` (CLAP, 3 sorgu: sıcak yol / gerilim / nostalji; `log/rank-*.txt`) — ipucu, kanıt değil.
**Sınır:** kulaksız seçim; ruh hali etiketleri [tahmin] (kaynak sayfa + CLAP + ölçüm). Kulak kararı F6a kör dinlemede. Bölüm zamanları senaryo yapısından (14 dk), metin gelince kayar.
Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[kaynak]** kaynak sayfada okundu · **[tahmin]** yorum.

## Bölüm başına aday listesi
| # | Bölüm (senaryo zamanı) | Ruh hali / tempo [tahmin] | 1. | 2. | 3. | Not |
|---|---|---|---|---|---|---|
| B1 | Kanca + ölçek + tez (0:00–1:30) | merak + yola çıkış, hafif gerilim | **Wasteland Caravan** (vitalezzz, gitar; maske 26.9 dB) | Lone Scavenger (vitalezzz) | Remember this shadow (Komiku) | İlk ≤3 sn: motor çalışma (`motor-looneybits-startengine`) + damla; yatak "one family's share" cümlesinde girer |
| B2 | Okafor ailesi + Sızıntı 1 uzun yaşam (1:30–3:30), ABONE-1 ~3:00 | sıcak, aile, hafif caz-pop | **Sunny Side Up** (Pro Sensory; CLAP "sıcak" 2.) | Joy Ride (Pro Sensory; std 0.5, en sabit yatak) | Country (Pro Sensory) | Sunny Side Up TP +0.8 (kırpık master) → F6a'da tepe −3 dBFS kuralı |
| B3 | Sızıntı 2 bakım (3:30–5:45) | ciddi, seyrek gerilim | **Insistent** (yd; konuşma bandı 0.003, "dark and quiet" [kaynak]) | Lone Scavenger (vitalezzz) | Deliberate Concealment (S08 kanıtlı yedek) | Insistent LRA 16.8 (dinamik): yalnız sabit kesit döngülenir; ölçüt bölüm farkı 21–23 dB |
| B4 | Sızıntı 3–4 eş + bağış, "detour" (5:45–8:00), ABONE-2 ~7:30 | yol değiştiren, meraklı, hafif hareketli | **Remember this shadow** (Komiku; konuşma bandı 0.014, maske 36.1) | Country (Pro Sensory; std 0.9) | Midnight Cruiser (Zane Little; funk yol) | Remember std 6.1 → sakin kesit seçilir. "Detour" anında kamyon el freni + kısa whoosh |
| B5 | Sızıntı 5 ev (8:00–10:30) | nostalji, ev, sıcak | **The road we use to travel when we were kids** (Komiku; maske 49.2 dB, CLAP "nostalji" 1.) | Sunset Plains (Yoiyami; Content ID/üretim riski orta) | Remember this shadow | Paletin "kimlik" parçası: çocukluk yolu = iki kuşak arasındaki yol |
| B6 | Sızıntı 6 vergi + zaman, varış + envanter (10:30–13:00) | yükselen gerilim → varışta çözülme | **Lone Scavenger** (vitalezzz) → varışta B5 parçasına geçiş | Insistent (yd) | Mysterious Clock (OwlishMedia; "zaman" teması, LRA 12.9, Content ID riski orta) | Varış: motor kapanma + kapı. Envanter çizikleri = `bant/para` değil kalem çizgisi (F6b earshot) |
| B7 | Tez + bant gag'i + ABONE-3 + köprü (13:00–14:00) | sıcak kapanış | **Joy Ride** (Pro Sensory) | The Way It Is (S08 kanıtlı yedek) | Sunny Side Up | Kapanış B2 rengine döner (aile çemberi) |

**Müzikal fikir:** kamyon yola çıkar (gitar yol müziği) → aile sahnesinde sıcak caz-pop → sızıntılarda müzik seyrekleşir, yalnız karanlık yatak kalır → ev bölümünde "çocukluk yolu" nostaljisi → varışta gerilim çözülür → kapanışta sıcak. Motor uğultusu yalnız sahne geçişlerinde ve konuşmasız anlarda çok kısık (−40 dB altı), "aynı kamyon" hissi.
**Shorts:** Shorts 1 yatağı Wasteland Caravan, Shorts 2 yatağı Insistent (her ikisi de uzun videoda farklı kesit).

## SFX paleti (önceki iki videodan farklı: nakliye kamyonu + bant + sızıntı)
| Olay (senaryo) | 1. | Yedek |
|---|---|---|
| Bant gag'i ("more tape") | `bant-owlishmedia-stationery_26` (CLAP z +5.3) | `stationery_08`, kısa kopma `stationery_27` |
| Kutudan damlayan para / sızıntı | earshot `drip/drop` + `para-owlishmedia-money_33` (banknot) | `drip/plink`, `para-owlishmedia-money_34` |
| Bozuk para dökülmesi | `para-lordtomorrow-coinsplash` | `para-owlishmedia-money_14` |
| Kamyon çalışır / durur | `motor-looneybits-startengine`, `kamyon-ggbotnet-car_engine_turning_off` | `kamyon-ggbotnet-car_engine_start_up` |
| Kapak / kapı (yükleme, varış) | `kamyon-ggbotnet-car_trunk_open`, `car_door_close` | `car_door_open`, `assets/efekt/kapi-rubberduck-door_open_01` |
| "Detour" / durak | `kamyon-ggbotnet-car_parking_brake` | `car_horn` (yalnız konuşmasız anda) |
| Ölçek kartı / büyük rakam | kanal `assets/efekt/whoosh-*`, `riser`, `ozgun-ka-ching` | earshot `swish` (apex hedefli) |
| Abone ol tıklaması | `assets/efekt/ozgun-fare-klik.flac` (kanal kaydında) | — |
SFX ölçümü (`olcum-sfx.jsonl`) [ölçüm]: GGBotNet paketi 64 kb/s telefon kaydı; `car_engine_loop` taban −8.5 dB (sürekli döngü, beklenen), `car_door_open` −30.5 dB → yalnız konuşmasız anda. OwlishMedia/LordTomorrow ≤−32 dB.

## Ölçümler [ölçüm] (seçilen 11 + elenen 12; S08 yedekleri S08 `olcum-muzik.jsonl`'de, sha aynı, yeniden ölçülmedi)
| Dosya | Süre sn | LUFS | LRA | TP | Konuşma bandı | Telefon bandı | BPM [tahmin] | Kısa-süre std | Maske SNR dB |
|---|---|---|---|---|---|---|---|---|---|
| wasteland-caravan-vitalezzz | 262.4 | −13.1 | 3.7 | −0.1 | 0.037 | 0.411 | 171 | 3.0 | 26.9 |
| lone-scavenger-vitalezzz | 192.5 | −12.9 | 5.4 | −0.2 | 0.057 | 0.392 | 171 | 2.4 | 22.1 |
| remember-this-shadow-komiku | 213.1 | −14.2 | 4.7 | −0.2 | 0.014 | 0.179 | 86 | 6.1 | 36.1 |
| the-road-we-used-to-travel-komiku | 140.3 | −16.8 | 8.4 | −0.3 | 0.034 | 0.716 | 87 | 2.7 | 49.2 |
| insistent-yd | 128.7 | −19.6 | 16.8 | −5.6 | 0.003 | 0.156 | 150 | 7.5 | 33.6 |
| sunny-side-up-pro-sensory | 143.1 | −11.3 | 6.1 | +0.8 | 0.046 | 0.204 | 84 | 2.6 | 22.9 |
| joy-ride-pro-sensory | 90.7 | −16.1 | 1.6 | −3.1 | 0.035 | 0.165 | 90 | 0.5 | 23.1 |
| country-pro-sensory | 158.7 | −13.3 | 2.9 | +0.3 | 0.024 | 0.417 | 109 | 0.9 | 27.5 |
| sunset-plains-yoiyami | 329.7 | −16.1 | 4.6 | −3.4 | 0.021 | 0.522 | 176 | 2.6 | 33.3 |
| midnight-cruiser-zane-little | 144.4 | −13.0 | 2.2 | −1.6 | 0.095 | 0.385 | 67 | 0.7 | 23.0 |
| mysterious-clock-owlishmedia | 94.9 | −18.9 | 12.9 | −1.8 | 0.128 | 0.376 | 109 | 5.7 | 25.1 |
| *elenen:* drive / freeway-fumes / detour (Zane Little) | | | | | 0.253 / 0.212 / 0.171 | | | | 15.2 / 16.6 / 19.4 |
| *elenen:* down-the-river (Komiku) / investigation (wipics) | | | | | 0.198 / 0.309 | | | | 15.0 / 15.5 |
| *elenen:* empty-stretch / road-trip / desert-travel / banjo-something / desert-settlement / exploration / investigation (Umplix) | | | | | 0.131 / 0.075 / 0.021 / 0.118 / 0.100 / 0.003 / 0.081 | tel. exploration 0.063 | | | 23.8 / 22.0 / 25.5 / 20.2 / 18.9 / 37.6 / 45.3 |
Eleme gerekçeleri: `lisans-kaydi.md` → "Değerlendirilip alınmayanlar".

## Yeniden üretim
- Müzik (git dışı): `lisans-kaydi.md` linklerinden indir; orijinal sha256 `orijinal-sha256.txt`, son dosyalar `muzik-sha256.txt`. WAV → `ffmpeg -c:a libvorbis -q:a 5`.
- Efekt (git dışı): OGA zip/dosyaları indir → `python3 -I efekt-hazirla.py <girdi> kaynak/efekt/<ad>.flac` (son sha `efekt-sha256.txt`).
- Ölçüm: `nice python3 -I aday-olc.py muzik ../../ses-testi/tts/anlatici-v1.m4a kaynak/muzik/*`, `python3 -I tel-bant.py kaynak/muzik/*`, `python3 -I aday-olc.py sfx kaynak/efekt/*`, `tools/earshot rank "<sorgu>" kaynak/muzik/`.
