---
description: Seçimi yapılmış veya yarım kalmış bir üretimi ilk geçmemiş adımdan (F3–F10) teslim paketine kadar sürdürür; yeni video için /bugunun-videosu
argument-hint: [üretim klasörü]
---
Klasör: $ARGUMENTS (boşsa `durum.md`'sinde teslim edilmemiş adım bulunan en son `uretim/` klasörü).

Bu komut `.claude/commands/bugunun-videosu.md` akışının **F3–F10** fazlarını yürütür. Kullanıldığı durumlar: `/yeni-video` ile seçimi yapılmış bir üretimi sürdürmek, oturum koptuktan sonra devam etmek, Niyazi'nin "şunu değiştir" talebinden sonra yeniden üretmek. `durum.md`'deki ilk GEÇMEMİŞ adımdan başla, geçmiş adımları tekrarlama.

Kısaca:
- F3: `senaryo-yazari` tam metin + Shorts kancaları → `finans-dogrulayici` → metin kilidi.
- F4: (`ses-yonetmeni` TTS → `ses-muhendisi`) ‖ `gorsel-varlik-sanatcisi` (Canva prompt paketi → koordinatör Canva `generate-image` çağrıları → ajan değerlendirmesi) ‖ `muzik-ses-tasarimcisi` ‖ `thumbnail-tasarimcisi` + `youtube-paketleyici` taslakları.
- F5: `animasyon-yonetmeni`, önce 10–20 sn kritik yol testi (≤2 kare senkron).
- F6: `muzik-ses-tasarimcisi` miksi, F5 ile paralel.
- F7: `kurgu-editoru` final 16:9 + SRT + 2 Shorts.
- F8: `thumbnail-tasarimcisi` (3 varyant) ‖ `youtube-paketleyici` (`yayin-paketi.json`) ‖ `viralite-analisti`.
- F9: `hakem` son kontrol.
- F10: `teslim/` paketi + `YAYIN.md` → Niyazi'ye sun → **DUR**.

Araç sorunu her aşamada `uretim-muhendisi`'ne gider. RED döngüsü en fazla 2 tur sürer, sonra koordinatöre eskalasyon. Ek para harcayan adım yalnız onaylı bütçe tavanı içinde yapılır (`docs/uretim-kapasitesi.md`); Canva aboneliği içindeki görsel üretimi ek harcama sayılmaz. Final video git'e girmez; depolama önerisi (Niyazi onayı bekliyor) `bugunun-videosu.md` bölüm 3'te.
YouTube'a yükleme (F11) yalnız Niyazi "yayınla/yükle" deyince yapılır, `tools/yayin/` aracıyla (sahibi `uretim-muhendisi`).
