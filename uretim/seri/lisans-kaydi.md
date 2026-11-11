# Flip By Vote — ses lisans kaydı (dizi geneli)

Sahibi: muzik-ses-tasarimcisi. Kural (`politika-format.md` §6): **yalnız CC0 ve kendi üretimimiz**. CC BY dahil atıf isteyen, NC/ND/SA, platform müzik kütüphanesi (IG/TikTok/YouTube sesleri) YASAK.
Kayıtta olmayan dosya kurguya giremez. Kapı: `python3 uretim/seri/ses-kimligi/lisans-kontrol.py` (çıkış 0 = GEÇTİ; `video/public/seri/ortak/` altındaki her ses dosyası + bölüm cue'larındaki her dosya burada olmalı).
Atıf: hiçbir dosya atıf istemez → açıklamaya müzik satırı gerekmez (TikTok kısa açıklaması için uygun). Content ID: kendi sentezimiz hiçbir veri tabanında kayıtlı değil; CC0 dosyalar (Kenney, OGA) için kanıt sayfaları `assets/lisans-kanit/` altında.
Yeniden üretim (kendi üretim, deterministik, 2 koşu sha256 aynı 2026-11-10): `cd uretim/seri/ses-kimligi && ~/.finansal-arac/earshot-venv/bin/python uret.py aday && ./earshot-uret.sh aday && ~/.finansal-arac/earshot-venv/bin/python yayinla.py`

## Lisans bağlantıları (2026-11-10 açıldı: HTTP 200)
- CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (kopya `assets/lisans-kanit/cc0-1.0-legalcode.html`)
- earshot MIT (Leon Lin, commit 591fa3e): https://raw.githubusercontent.com/Leonxlnx/earshot/591fa3e/LICENSE (kopya `assets/lisans-kanit/earshot-591fa3e-LICENSE.txt`). `fit/*` reçeteleri CC0 Freesound kayıtlarının ölçülmüş yapısı, örnek içermez: kopya `assets/lisans-kanit/earshot-591fa3e-CREDITS_FIT.md`
- Kenney Interface Sounds CC0: https://kenney.nl/assets/interface-sounds (2026-11-10'da ağdan 403; 2026-10-26 kopyası `assets/lisans-kanit/kenney-interface-sounds-License.txt`)
- OGA "Coin Drop" CC0: https://opengameart.org/content/coin-drop (200, `license-name'>CC0`; kopya `assets/lisans-kanit/oga-coin-drop.html`)

## Müzik (`video/public/seri/ortak/muzik/`, 48 kHz stereo FLAC)
| Dosya | sha256 (12) | Kaynak | Lisans | Yazar | Tarih | Atıf | Bölüm 001 kullanımı (sn) |
|---|---|---|---|---|---|---|---|
| `jingle-flip.flac` (1,8 sn seri damgası) | f8bcc251eaf5 | Kendi üretim: `uretim/seri/ses-kimligi/uret.py` → `jingle-a` (sentez, tohum 11) | Bizim | Flip By Vote | 2026-11-10 | yok | 0,00–1,80 · 78,82–80,62 |
| `dongu-strut-112.flac` (8 ölçü dikişsiz döngü) | 8728869b394c | Kendi üretim: `uret.py` → `dongu-a` (tohum 21) | Bizim | Flip By Vote | 2026-11-10 | yok | 0,00–35,05 |
| `dongu-hustle-124.flac` (8 ölçü dikişsiz döngü) | 914b99359eda | Kendi üretim: `uret.py` → `dongu-b` (tohum 22) | Bizim | Flip By Vote | 2026-11-10 | yok | 35,53–61,99 |
| `gerilim-saat-96.flac` (8 ölçü dikişsiz döngü) | 3d6fb6a2de10 | Kendi üretim: `uret.py` → `gerilim-a` (tohum 31) | Bizim | Flip By Vote | 2026-11-10 | yok | 61,99–78,57 |

## Efekt (`video/public/seri/ortak/sfx/`)
| Dosya | sha256 (12) | Kaynak | Lisans | Yazar | Tarih | Atıf | Bölüm 001 kullanımı (sn) |
|---|---|---|---|---|---|---|---|
| `tezgah-carpma.flac` | 7367658cf3d9 | earshot `knock/desk` + 0,55·`cut_hit/punch` (seed 7) katmanı: `earshot-uret.sh` + `yayinla.py` | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 0,00 |
| `tahta-kalem-kisa.flac` | bd90aa0a1898 | Kendi üretim: `uret.py` → `sfx-tahta-kisa` (tohum 41) | Bizim | Flip By Vote | 2026-11-10 | yok | 7,21 · 12,13 |
| `tahta-kalem-uzun.flac` | 3caf3e52279f | Kendi üretim: `uret.py` → `sfx-tahta-uzun` (tohum 42) | Bizim | Flip By Vote | 2026-11-10 | yok | 30,44 |
| `plak-cizik.flac` | 4bbb7643a10c | Kendi üretim: `uret.py` → `sfx-plak-cizik` (tohum 43) | Bizim | Flip By Vote | 2026-11-10 | yok | 35,05 |
| `kutu-tikirti.flac` | e1b468587a2f | Kendi üretim: `uret.py` → `sfx-kutu-tikirti` (tohum 44) | Bizim | Flip By Vote | 2026-11-10 | yok | 54,70 |
| `tik.flac` | d27b48b028f6 | earshot `fit/tick/domino` seed 7 (reçete: Freesound 329098 Macif, CC0, örnek yok) | Kendi üretim (MIT kod; CC0 türev) | Flip By Vote / earshot | 2026-11-10 | yok | 12,59–13,19 (6×) |
| `swipe.flac` | 283973b7a7fd | earshot `swipe/flick` seed 7 | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 17,30 |
| `ding.flac` | 9edea6264d28 | earshot `pro_notify/ding_2045` seed 7 | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 58,26 · 78,59 |
| `pop-yumusak.flac` | f6374e5f7789 | earshot `ui_pop/soft` seed 7 | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 41,42 · 47,35 · 47,70 · 60,67 |
| `whoosh-kart.flac` | 360b8c91237f | earshot `whoosh_fast/tight` seed 7 | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 16,04 · 24,60 · 37,50 · 53,51 · 74,47 |
| `gerilim-dusus.flac` | fe78b684764d | earshot `pro_sub_drop/soft` seed 7 | Kendi üretim (MIT kod) | Flip By Vote / earshot | 2026-11-10 | yok | 62,02 |
| `ka-ching.flac` (= `assets/efekt/ozgun-ka-ching.flac`) | c046cef2a0ec | Kendi üretim: `uretim/2026-10-26-1929-1000-dolar/06-muzik/ozgun-uret.py` | Bizim | Toonomy | 2026-10-27 | yok | şablon BANK artışı (bölüm 001'de yok) |
| `coin-drop.flac` (= `assets/efekt/para-coin-drop.flac` ← `coin_drop.ogg`) | f72b2c836c8a | https://opengameart.org/content/coin-drop | CC0 1.0 | Vinrax | 2026-10-26 | yok | şablon BANK azalışı (bölüm 001'de yok) |
| `fare-klik.flac` (= `assets/efekt/ozgun-fare-klik.flac`) | aefdd84f3839 | Kendi üretim: `tools/ses/fare-klik-uret.py` (tohum 1929) | Bizim | Toonomy | 2026-10-28 | yok | 71,87 (abone klik) |
| `pop-pluck.flac` (= `assets/efekt/pop-pluck.flac` ← Kenney `pluck_001.ogg`) | a5ae0d791865 | https://kenney.nl/assets/interface-sounds | CC0 1.0 | Kenney | 2026-10-26 | yok | 4,60 · 48,76 · 49,14 · 49,58 |
| `whoosh-kisa.flac` (= `assets/efekt/whoosh-kisa.flac`) | 9d91958b40cf | Kendi üretim: `tools/ses/efekt-uret.py` | Bizim | Toonomy | 2026-10-26 | yok | şablon kart girişi (bölüm 001 stem'inde değil) |

Not: Bölüm 001 zamanları `uretim/seri/bolum-001/ses-cue.mutlak.json` (ses kilidi `bolum-001.wav` 289da660bbd0). Şablon efektleri bölüm 001'de stem'de; bölüm tanımında `ses.sablonSfx: false`.

## TTS — karakter sesleri (ses-yonetmeni, 2026-11-11; hakem ŞY-1)
**Kapsam notu:** Bu kaydın başındaki "yalnız CC0, CC BY yasak" kuralı müzik ve SFX içindir (`politika-format.md` §6). Karakter sesleri Niyazi'nin 2026-11-11 kör dinleme kararıyla CC BY 4.0'dır; atıf satırı zorunludur. `lisans-kontrol.py` müzik/SFX tablolarını denetler, bu bölüm onun dışındadır. §6'yı güncellemek monetizasyon-uyum-uzmani'nin işi (hakem notu).
Kullanım: Bölüm 001 ve sonrası. Kilit `uretim/seri/bolum-001/ses/kilit.json` (`bolum-001.wav` sha 1d0d8235acd4). Yerel üretim, ücretsiz, ses klonlama yok (yalnız hazır katalog sesleri).

| Bileşen | Lisans | Kaynak URL (erişim 2026-11-11) | Kanıt (alıntı + kopya, sha256 ilk 12) |
|---|---|---|---|
| Pocket TTS kodu (pip `pocket-tts` 4.0.1) | MIT | https://github.com/kyutai-labs/pocket-tts (LICENSE: https://raw.githubusercontent.com/kyutai-labs/pocket-tts/main/LICENSE) | "Permission is hereby granted, free of charge, to any person obtaining a copy of this software…" → `assets/lisans-kanit/tts-pocket-tts-kod-LICENSE.txt` (23f18e03dc49) |
| Pocket TTS ağırlıkları (`kyutai/pocket-tts-without-voice-cloning`, varsayılan `english`; kapısız) | CC BY 4.0 | https://huggingface.co/kyutai/pocket-tts-without-voice-cloning | Model kartı başlığı "license: cc-by-4.0". Yasak kullanımlar: izinsiz ses taklidi/klonlama, üretimi gerçek kayıt gibi sunmak (bizde yok, AI beyanı var) → `assets/lisans-kanit/tts-pocket-tts-model-karti.md` (c01f4a60dca7) |
| Jake sesi `george` = VCTK p315 (`hf://kyutai/tts-voices/vctk/p315_023_enhanced.wav`) | CC BY 4.0 | https://huggingface.co/kyutai/tts-voices (vctk/) · veri seti https://datashare.ed.ac.uk/handle/10283/3443 | tts-voices README: "From the Voice Cloning Toolkit dataset, licensed under the Creative Commons License: Attribution 4.0 International." → `assets/lisans-kanit/tts-kyutai-tts-voices-README.md` (47c610f38e0e). Edinburgh DataShare sayfası: "Creative Commons Attribution 4.0 International Public License" → `assets/lisans-kanit/tts-vctk-datashare-10283-3443.html` (2b1dc190f83a). Ses → kaynak eşlemesi (paket kodu `pocket_tts/utils/utils.py`): `assets/lisans-kanit/tts-pocket-tts-ses-kaynaklari.txt` (d80481190dab) |
| Mike sesi `marius` = Unmute gönüllü ses bağışı `voice-donations/Selfie.wav` | CC0 | https://huggingface.co/kyutai/tts-voices (voice-donations/) | README: "Voices of volunteers submitted through our Unmute Voice Donation Project, licensed as CC0." → aynı README kopyası (47c610f38e0e) + eşleme dosyası (d80481190dab) |

Lisans metinleri: CC BY 4.0 `assets/lisans-kanit/cc-by-4.0-legalcode.html` · CC0 `assets/lisans-kanit/cc0-1.0-legalcode.html`.
**Açıklamadaki atıf (CC BY 4.0 şartı, üç platform):** "Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0)." Bölüm 001'de `uretim/seri/bolum-001/teslim/platform-metinleri.md` ve `teslim/yayin-paketi.json` içinde var (üretici `paket/paket-uret.py`; hakem-raporu.md Paket satırı 3/3). Ses değişirse (VCTK dışı bir ses seçilirse) VCTK kısmı düşer. `marius` CC0 olduğu için atıf gerekmez.
Kullanılmayan ve yasak Pocket sesleri: `jean` (EARS, CC BY-NC), `cosette` (Expresso, CC BY-NC). `tools/ses/gercekci_tts.py` izinli liste dışını reddeder.

## Değerlendirilip alınmayan
| Aday | Neden |
|---|---|
| `dongu-c` "Porch Shuffle" (kendi üretim) | konuşma bandı 0,104 (en yüksek), LRA 3,3, CLAP "sitcom" eşleşmesi en düşük (z +2,6) |
| `gerilim-b` "Sneaky pizz" (kendi üretim) | konuşma bandı 0,131, CLAP "alarm clock" (gerilim değil dikkat dağıtıcı) |
| `gerilim-c` "Heartbeat drone" (kendi üretim) | telefon bandı payı 0,055 < 0,08 → telefonda duyulmaz |
| `jingle-b`, `jingle-c` (kendi üretim) | konuşma bandı 0,54 / 0,70 (jingle-a 0,29); ilk replik altında maskeleme riski daha yüksek |
