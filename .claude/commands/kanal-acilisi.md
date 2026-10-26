---
description: Kanal açılış paketi (bir kez, sonra 10 videoda bir gözden geçirme) — kanal kimliği, banner, profil resmi, filigran, kanal açıklaması, oynatma listeleri, fragman planı ve YPP hazırlık listesi
argument-hint: [isteğe bağlı not]
---
Not: $ARGUMENTS

Amaç: kanal sayfasının izleyiciyi aboneye çevirmesi ve YPP incelemesinde özgün, tutarlı bir kanal görünmesi. Alt ajanları yalnız koordinatör çağırır; paralel adımlar tek mesajda.

1. **Paralel:**
   - `youtube-paketleyici` → `docs/kanal-kimligi.md` (ad: Financial Rise, slogan adayları, ses tonu, sütunlar B · Bugün / A · Geçmiş / C · Gelecek, yasaklar), kanal açıklaması, anahtar kelimeler, 3 oynatma listesi + açıklamaları, bağlantılar, kanal fragmanı planı (≤60 sn). Teslim `uretim/kanal-acilisi/kanal-sayfasi.md`.
   - `thumbnail-tasarimcisi` → banner (2560x1440, güvenli alan 1235x338, ≤6 MB), profil resmi (98x98'de okunur), filigran (≥150x150, <1 MB); her biri 2–3 aday, mobil/TV önizlemesi; `docs/kanal-kimligi.md` görsel bölümü (renk, yazı tipi). Karakter görseli gerekirse `gorsel-varlik-sanatcisi` (Canva çağrısını koordinatör yapar). Teslim `uretim/kanal-acilisi/gorseller/`.
   - `monetizasyon-uyum-uzmani` → `docs/ypp-hazirlik.md` (eşikler ve kaynakları, 2 adımlı doğrulama, AdSense, kanal ayarlarında AI beyanı varsayılanı, ilk 5 video için özgünlük planı).
2. `senaryo-yazari` → fragman metni (≤60 sn) → `finans-dogrulayici` ‖ `monetizasyon-uyum-uzmani` → normal hat (F4–F7) kısa üretim.
3. `hakem` → kanal sayfası kapısı (`docs/kalite-kapilari.md`) + karne.
4. Commit + push. Niyazi'ye tek sayfa: görseller, açıklama, oynatma listeleri ve Studio'da yapılacak adımlar. **Kanal ayarlarını Niyazi uygular**; yükleme/yayın yalnız onayla.
