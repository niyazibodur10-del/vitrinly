# uretim-muhendisi — hafıza

## Kurallar
- Her araç değişikliğinden sonra örnek girdiyle çalıştır, ayrıca BOZUK girdiyle de çalıştır (kayık zaman, eksik kelime, uzun yol): kapı araçları kalması gerekeni kaldırmalı.
- Kurulum testi kısa bir yolda (`ARAC_DIZINI=/root/ktN`) yapılır, sonra silinir; ikinci çalıştırma ≤ 2 sn olmalı (idempotent).
- Süre ölçerken `uptime`/`ps` ile paralel yükü kaydet; sonuçları aralık olarak ver (boşta / yük altında).

## Dersler
- 2026-10-26 (devralınan): Rhubarb kaynak koddan derleniyor; CMake 3.28'de `cmake_policy(SET CMP0167 OLD)` hata verir → `if(POLICY CMP0167)` ile koşullu (`tools/kurulum.sh`).
- 2026-10-26: Render tarayıcısı `/opt/pw-browsers/chromium_headless_shell-*` (Playwright); Google Fonts sertifikası güvenilmiyor → fontlar yerel.
- 2026-10-26: Real-ESRGAN x4 ağırlığı HF `ai-forever/Real-ESRGAN`'dan, spandrel ile yükleniyor (trust_remote_code yok).
- 2026-10-26 (yayın aracı): Google cihaz akışı YouTube için yalnız `youtube`/`youtube.readonly` kapsamı verir → videos.insert/thumbnails.set/playlistItems.insert çalışır, captions.insert (force-ssl) ÇALIŞMAZ. Altyazı: Studio veya `--akis yerel` (masaüstü istemci + PKCE loopback).
- 2026-10-26: videos.insert sayfası (2026-10-15) "unverified projects are not restricted to private" diyor; 2020 kilit duyurusu revision_history'de duruyor, geri alma notu yok → resmi kaynaklar çelişirse tek test yüklemesiyle ölç, iki yolu da (API + manuel paket) hazır tut.
- 2026-10-26: developers.google.com WebFetch'te DNS hatası veriyor; `curl -sL ...?hl=en` + stdlib HTML→metin ile okunuyor. Konsol URL'leri giriş yönlendirmesi verdiği için doğrulanamaz → support.google.com/cloud yardım sayfalarındaki linklerden doğrula.
- 2026-10-26: Ağ protokol kodunu (resumable 308/503 devam) yerel sahte HTTP sunucusuyla test et; urllib için `no_proxy=127.0.0.1` opener kurulmadan ÖNCE ayarlanmalı. Stdlib urllib HTTPS_PROXY'ye uyuyor (erişim testi 6/6).
- 2026-10-26 (hat testi): Kokoro kurulum.sh'a eklendi (py3.12 venv, kokoro/misaki 0.9.4, en_core_web_sm önceden). Sıfırdan kurulum 231–237 sn, ikinci çalıştırma 1,7 sn (`npm ci` damgası + `find_spec`; import kontrolü 12 sn yiyordu).
- 2026-10-26: espeak-ng veri yolu ~160 karakterde kesiliyor → uzun ARAC_DIZINI'nde Kokoro "phontab" hatası. Sembolik bağ çözmez (Python gerçek yolu kullanıyor). Kurulum uzun yolu reddediyor.
- 2026-10-26: Real-ESRGAN tek parça bellek ~9,4 KB/piksel → tam kare OOM; parçalı çıkarım (256 + 16 pay) tepe 1,4 GB, dikiş farkı ort. 0,18/255.
- 2026-10-26: Render ~8–10 kare/sn; concurrency 2→4 yalnız %8; `--gl=swangle` 4,7x yavaş; 6 > nproc reddedilir. Parça render (sıralı + önbellek) PSNR 51,9 dB, ses kayması 0 ms; Remotion ses-only render'ı da kareleri dolaşıyor (~50 kare/sn) → hazır miks varsa `--ses`.
- 2026-10-26: Gizli kapı hataları bulundu: senkron-testi kare sayısı (sr//fps yuvarlaması → NaN), hata-orani sayı normalizasyonu yok (sahte WER), miks.py varsayılanları karardan farklı (35,7 dB) ve /tmp sızıntısı. Ders: "çalışıyor" ≠ "doğru ölçüyor"; kapı araçlarını bilinen-kötü girdiyle sına.
- 2026-10-27 (F0 secim): Yeni açılan konteynerde sayfa önbelleği soğuk → ilk çağrılar 4–40 kat yavaş (Whisper small 44 sn→3,4; medium 136 sn; Kokoro 88→11 sn; compositions 25 sn). "Araç başarısız" raporu gelince önce soğuk yükleme/zaman aşımını ele; çağıranlara ilk çağrıda ≥3 dk zaman aşımı söyle.
- 2026-10-27: `yaziya-dok.py` sessiz hata veriyordu → önce `local_files_only=True` (ağ beklemesi yok), açık hata mesajları, düşük güven (<0,3) halüsinasyon uyarısı (sessizlikte "You", p 0,11).
- 2026-10-27: `render-son.sh` 0,4 sn'den kısa/sessiz render'da loudnorm `-inf` ile düşüyordu (F0'ın 2 karelik test render'ı tam bu durum). Ölçülemezse normalizasyon atlanıp uyarı veriliyor. Ders: kapı testinin kendisini (2 kare) dün tam hat testinde de koşmalıydım — kenar girdisi = gerçek kullanım.
