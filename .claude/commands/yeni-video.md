---
description: Yalnız seçim aşaması (F0–F2) — araştırma → en az 10 senaryo → eleme → hakem kazananı seçer; tam üretim için /bugunun-videosu
argument-hint: [isteğe bağlı konu veya sütun]
---
Konu/sütun ipucu: $ARGUMENTS (boşsa sütun `docs/yayin-takvimi.md` rotasyonundan gelir).

**Tam otomatik üretim isteniyorsa** (ör. Niyazi "Bugünün videosu gelsin" dediyse) bu komutu değil `/bugunun-videosu`'nu çalıştır.

Bu komut yalnız `.claude/commands/bugunun-videosu.md`'nin **F0–F2** fazlarını yürütür. Kullanıldığı yerler: stok video için önceden konu seçmek, haber sütununa erken hazırlık, araştırma denemesi.
- F0: klasör `uretim/<tarih>-secim/` + `durum.md` ‖ (gerekirse) `uretim-muhendisi` ortam kurulumu.
- F1: `trend-avcisi` ‖ `kanal-analisti`.
- F2: `senaryo-yazari` (en az 10 senaryo) → `viralite-analisti` ‖ `finans-dogrulayici` ‖ `monetizasyon-uyum-uzmani` → `hakem` kazanan + yedek.

Senaryo kararı **ajanlarındır, Niyazi'ye onaya sunulmaz** (Niyazi kararı 2026-10-26). Bitince klasörü slug'la yeniden adlandır, `durum.md`'de F3'ü BEKLİYOR yap, commit + push et ve Niyazi'ye bilgi amaçlı 3 satır özet ver: kazanan, puan, sütun. Üretime devam etmek için `/video-uret <klasör>` çalıştırılır; akış F3'ten sürer.
Kapılar, RED döngüsü (en fazla 2 tur, sonra koordinatöre eskalasyon) ve kurallar `bugunun-videosu.md` ile aynıdır.
