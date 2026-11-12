---
description: Seçimi yapılmış veya yarım kalmış bir üretimi ilk geçmemiş adımdan (F3–F10) teslim paketine kadar sürdürür; yeni video için /bugunun-videosu
argument-hint: [üretim klasörü]
---
Klasör: $ARGUMENTS (boşsa `durum.md`'sinde teslim edilmemiş adım bulunan en son `uretim/` klasörü).

Bu komut `.claude/commands/bugunun-videosu.md` akışının **F3–F10** fazlarını yürütür. Kullanıldığı durumlar: `/yeni-video` ile seçimi yapılmış bir üretimi sürdürmek, oturum koptuktan sonra devam etmek, Niyazi'nin "şunu değiştir" talebinden sonra yeniden üretmek. `durum.md`'deki ilk GEÇMEMİŞ adımdan başla, geçmiş adımları tekrarlama.

Kısaca:
Hız kuralları (kritik yol, erken başlatma tablosu, faz hedef süreleri, token kuralları): `bugunun-videosu.md` bölüm 0b. Kesintiden sonra `durum.md` + ajan raporlarındaki İLERLEME bloğundan devam et; biten ajanı yeniden çağırma.
- F3: (`senaryo-yazari` tam metin + Shorts kancaları + `ABONE-n` anları ‖ `finans-dogrulayici` rakam tablosu) → (`finans-dogrulayici` ‖ `monetizasyon-uyum-uzmani`) ‖ görsel dalga 1 ‖ animasyon iskeleti → metin kilidi.
- F4: (`ses-yonetmeni` TTS → `ses-muhendisi`) ‖ `gorsel-varlik-sanatcisi` (Canva prompt paketi → koordinatör Canva `generate-image` çağrıları → ajan değerlendirmesi) ‖ `muzik-ses-tasarimcisi` ‖ `thumbnail-tasarimcisi` + `youtube-paketleyici` taslakları.
- F5: `animasyon-yonetmeni`, önce 10–20 sn kritik yol testi (≤2 kare senkron; ses kolu GEÇTİ + test sahneleri yeter), sonra tüm sahneler + 9:16 + `animasyon-efekt-cue.json` (SFX ve abone anları).
- F6: `muzik-ses-tasarimcisi` F6a müzik yatağı (F5 ile paralel) → F6b SFX stem (görsel olay zamanlarından).
- F7: `kurgu-editoru` final 16:9 + SRT + abone animasyonu (uzun 3–4, Shorts ≤1) + 2 Shorts.
- F8: F8a erken paket (görsel kol GEÇTİ olunca: `thumbnail-tasarimcisi` ‖ `youtube-paketleyici` ‖ `viralite-analisti` → `monetizasyon-uyum-uzmani`) + F8b fark kontrolü (F7 sonrası, ≤10 dk).
- F9: `hakem` son kontrol (F9a video kapıları F8b ile paralel, F9b paket + karar; YPP politika, retention ve abone kapıları dahil).
- F10: `teslim/` paketi + `YAYIN.md` → Niyazi'ye sun → **DUR**.

Araç sorunu her aşamada `uretim-muhendisi`'ne gider. RED döngüsü en fazla 2 tur sürer, sonra koordinatöre eskalasyon. Ek para harcayan adım yalnız onaylı bütçe tavanı içinde yapılır (`docs/uretim-kapasitesi.md`); Canva aboneliği içindeki görsel üretimi ek harcama sayılmaz. Final video git'e girmez; depolama önerisi (Niyazi onayı bekliyor) `bugunun-videosu.md` bölüm 3'te.
Yayından sonra F12 (48 sa / 7 g / 28 g): `kanal-analisti` performans raporu → `viralite-analisti` kalibrasyon; dersler sonraki videoya.
YouTube'a yükleme (F11) yalnız Niyazi "yayınla/yükle" deyince yapılır, `tools/yayin/` aracıyla (sahibi `uretim-muhendisi`).
