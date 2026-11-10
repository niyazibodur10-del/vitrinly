# uretim-muhendisi — hafıza

## Kurallar
- Her araç değişikliğinden sonra örnek girdiyle VE bozuk/kenar girdiyle çalıştır (kayık zaman, eksik kelime, uzun yol, 2 karelik render): "çalışıyor" ≠ "doğru ölçüyor".
- Kurulum testi kısa yolda (`ARAC_DIZINI=/root/ktN`) yapılır, sonra silinir; ikinci çalıştırma ≤ 2 sn (idempotent). Kurulu kontrolü python import değil damga + dosya testi.
- Süre ölçerken `uptime` ile paralel yükü kaydet; aralık ver (boşta / yük altında). Ağır ölçümden önce paralel ajanın ≥2 dk boşta kalmasını bekle.
- Eşzamanlılık = nproc varsayma; bu VM'de 2 iş parçacığı doyuyor (Whisper 2, render 2×c2, Rhubarb 2×2, TTS 2 süreç).
- Paylaşılan fonksiyonu değiştirirken eski davranışı adlı sürüm olarak tut (`norm_eski`), kilitli betiği ona bağla, `cmp` ile kanıtla.
- Kapı araçlarında çıkış kodu 2 = kullanım hatası (KALDI=1 ile karışmasın). `while read` içindeki komutlara `</dev/null`; pkill -f yerine PID.
- Scratch'te geliştir; commit öncesi `git status`/`git show --stat HEAD` (paralel ajan ara kaydı yarım dosyayı süpürebilir).
- Yeniden üretim tarifini temiz worktree + boş önbellekte uçtan uca koşmadan "hazır" deme. Uzun arka plan işinde timeout 7200000.

## Ortam gerçekleri
- Rhubarb kaynak koddan; CMake 3.28'de CMP0167 `if(POLICY)` ile koşullu. Render tarayıcısı `/opt/pw-browsers/chromium_headless_shell-*`; fontlar yerel.
- Real-ESRGAN x4: HF `ai-forever/Real-ESRGAN` + spandrel; parçalı çıkarım (256+16) tepe 1,4 GB. espeak-ng yolu ~160 karakterde kırılır → kısa ARAC.
- YouTube cihaz akışı yalnız `youtube` kapsamı → captions.insert çalışmaz (Studio veya `--akis yerel`). developers.google.com için curl `?hl=en`.
- urllib HTTPS_PROXY'ye uyar; yerel sahte sunucu testinde `no_proxy=127.0.0.1` opener'dan ÖNCE.
- Soğuk sayfa önbelleği ilk çağrıları 4–40x yavaşlatır (Whisper medium 136 sn) → "araç başarısız" raporunda önce zaman aşımını ele; ilk çağrıda ≥3 dk.
- Chromium blur'lu render, Kokoro, Rhubarb deterministik değil → parça önbelleğinde toleranslı iz; yeniden üretim kaynağı git'teki m4a.
- Render ~8–10 kare/sn; `--gl=swangle` 4,7x yavaş. Ses-only render da kareleri dolaşır → hazır miks varsa `--ses`.

## Dersler
- 2026-10-27: kısa/sessiz render loudnorm -inf → atla+uyarı; senkron-testi aralık modu, yeni ölçüm eski elle ölçümle çapraz doğrulanır.
- 2026-10-28: Kurulum v2 (uv + paralel + tools/gereksinim sabit sürüm) temiz önbellekte 407 → 111 sn; SessionStart kancası kurar, bulut önbelleğe alır.
- 2026-10-28: Yeniden üretim tarifi temiz worktree'de 2 gizli hata buldu (stdin yutma, git dışı müzik); Shorts bit-aynı, final PSNR 68,8 dB.
- 2026-11-02 (earshot): Seyrek kullanılan ağır araç (2,5 GB) → senkron değil ayrık arka plan işi (`setsid nohup`, flock, damga en son) + sarmalayıcı (`tools/earshot`) ilk kullanımda bekler/kurar. Ölçüm: kurulum.sh dönüşü 0,9 sn; temiz kurulum 19 sn (sıcak uv), soğuk uv venv 34 sn + model ~16 sn; kurulu 0,2 sn.
- 2026-11-02: Disk %85 (6 GB boş) → büyük kurulumlara boş alan eşiği (earshot 4 GB, `ES_MIN_GB`), aşılırsa atla + uyarı, ana kurulumu düşürme. Temiz testte taşınan kopyaları diff'le doğrulayıp sil.
- 2026-11-03 (kanal fabrikası): kanala özel sabitler tek dosyada (`kanal.json` + stdlib `tools/kanal_ayar.py`; Remotion JSON import ile okur). Başka ajanın yama listesi olan dosyalara (ajan .md) dokunma, önce `eski` dizgilerini doğrula. Global sed'i heredoc içinde EOF'lu metinle yazma → betiği dosyaya yaz.
- 2026-11-03: token önceliği "ilk kaynak" değil "geçerli ilk kaynak" olmalı (ortam düşükse dosya). Oturum ortamındaki PY/TTS_PY başka ARAC gösterebilir → test betiği ARAC_DIZINI'nden türetir.
- 2026-11-04 (F0): hafızadaki "geçerli ilk kaynak" kuralı koda girmemişti; ortam tokenı düşünce cihaz akışına düşüyordu → hafızaya yazılan düzeltmeyi grep ile kodda doğrula, birim testiyle kilitle.
- 2026-11-04: disk 3,8 GB → 15 GB: en büyük sızıntı yarıda kalan render'ların /tmp/remotion-webpack-bundle-* (290 MB/adet); geniş /tmp süpürmesi izinsiz → `find -mmin +1440` ile yalnız bayatlar (`disk-durum.sh --temizle`).
- 2026-11-09 (kanal-analisti F12 teşhisi): 2/2 uzun video planlanandan erken public oldu (1929 6 sa, S08 29 sa), 4/4 Shorts zamanında; yükleme anında publishAt doğruydu. → Yükleme +1 sa ve açılış −2 sa'da `privacyStatus/publishAt` API kontrolü teslim kapısı; sapmada koordinatöre. Analytics kapsamı (`yt-analytics.readonly`) eklenmeden CTR/AVD ölçülemiyor (`uretim/2026-11-04-miras-sizintilari/01-arastirma/teshis-11-09.md`).
- 2026-11-09: kök neden "ayrıştıran değişken"le kurulur (Shorts aynı API adımıyla zamanında açıldı → API elendi); görünürlük geçmişi API'de yok → bekçi + niyet kaydı.
- 2026-11-09: kapsam sorusunu dokümandan sonra canlı denemeyle kapat (device/code'a kapsam yolla, YOKLAMA YAPMA → invalid_scope). Zamanlanmış betik asla etkileşimli yetki başlatmaz (`sessiz_yetki`); OAuth yoksa API anahtarı yedek.
- 2026-11-10 (Flip By Vote şablonu): Remotion veri kapısını calculateMetadata'da fırlatma → `remotion compositions` tüm kanalı kırar; kapı bileşende ilk karede + render öncesi grep (`tools/seri/kapi.py`). Ortak bileşene prop eklerken eski kompozisyon karesini `cmp` ile bit-aynı kanıtla.
- 2026-11-10: dikey 90 sn tam render c4: yer tutucu 2,0 dk, gerçek 1080x1920 PNG'ler 4,7 dk (yük 6–13) → parça render gereksiz. c4 > c2. Format/ses kararı değişince (am_onyx/am_fenrir) demo sesi ses-yonetmeni'nin aracıyla üret, kendi kopyanı tutma.
