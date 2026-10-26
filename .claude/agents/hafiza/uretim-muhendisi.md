# uretim-muhendisi — hafıza

## Kurallar

## Dersler
- 2026-10-26 (devralınan): Rhubarb kaynak koddan derleniyor; CMake 3.28'de `cmake_policy(SET CMP0167 OLD)` hata verir → `if(POLICY CMP0167)` ile koşullu (`tools/kurulum.sh`).
- 2026-10-26: Render tarayıcısı `/opt/pw-browsers/chromium_headless_shell-*` (Playwright); Google Fonts sertifikası güvenilmiyor → fontlar yerel.
- 2026-10-26: Real-ESRGAN x4 ağırlığı HF `ai-forever/Real-ESRGAN`'dan, spandrel ile yükleniyor (trust_remote_code yok).
- 2026-10-26: `tools/ses/temizle.sh` başlık yorumundaki yol eski (`tools/ses-temizle.sh`) — düzeltilecek.
- 2026-10-26 (yayın aracı): Google cihaz akışı YouTube için yalnız `youtube`/`youtube.readonly` kapsamı verir → videos.insert/thumbnails.set/playlistItems.insert çalışır, captions.insert (force-ssl) ÇALIŞMAZ. Altyazı: Studio veya `--akis yerel` (masaüstü istemci + PKCE loopback).
- 2026-10-26: videos.insert sayfası (2026-10-15) "unverified projects are not restricted to private" diyor; 2020 kilit duyurusu revision_history'de duruyor, geri alma notu yok → resmi kaynaklar çelişirse tek test yüklemesiyle ölç, iki yolu da (API + manuel paket) hazır tut.
- 2026-10-26: developers.google.com WebFetch'te DNS hatası veriyor; `curl -sL ...?hl=en` + stdlib HTML→metin ile okunuyor. Konsol URL'leri giriş yönlendirmesi verdiği için doğrulanamaz → support.google.com/cloud yardım sayfalarındaki linklerden doğrula.
- 2026-10-26: Ağ protokol kodunu (resumable 308/503 devam) yerel sahte HTTP sunucusuyla test et; urllib için `no_proxy=127.0.0.1` opener kurulmadan ÖNCE ayarlanmalı. Stdlib urllib HTTPS_PROXY'ye uyuyor (erişim testi 6/6).
