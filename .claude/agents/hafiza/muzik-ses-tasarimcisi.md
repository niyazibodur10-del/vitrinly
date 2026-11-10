# muzik-ses-tasarimcisi — hafıza

## Kurallar
- Lisans kapısı: lisans-kontrol betiği (uzun video `06-muzik/lisans-kontrol.py`; dizi `uretim/seri/ses-kimligi/lisans-kontrol.py`) + negatif test (sahte kayıtsız dosya → exit 1). OGA lisansı sayfadaki `license-name'>` alanından; çoklu lisanslı (SA/GPL karışık) ve zinciri doğrulanamayan "PD" yüklemeyi ele.
- Aday ölçümü: `aday-olc.py muzik` + `tel-bant.py` (miras-sizintilari/06-muzik). Ölçüt: konuşma bandı (1–4 kHz) ≤0.15, maske ≥20 dB, telefon bandı ≥0.08.
- WER kapısı cümle bazında: `tools/ses/cumle-whisper.py` ×3 (anlatım/müzik/tam) + `cumle-wer.py`; tam dosya Whisper ±6–8 kelime gürültülü.
- SFX vuruş noktası: whoosh = zarf tepesi, diğerleri ilk örnek > tepe·0.1. earshot `timeline --cues` apex hizalı whoosh'ta onset'i −40…−55 ms "near" gösterir: tasarım gereği, ±2 kare içinde.
- Seviye: her bölümün müzik−konuşma farkını render/miks sonrası ölç (hedef 21–23 dB); çok dinamik parçada (LRA >9) duck'ı ölçüme göre bir kez düzelt.
- Ağ: pixabay/incompetech/freesound engelli; kenney.nl 403 (kanıt kopyaları `assets/lisans-kanit/`); OGA, archive.org, raw.githubusercontent erişilir. Medya (wav) git dışı; md/json/betik + kanıt commit.

## Dersler
- 2026-10-27: Kendi sentez yatakları enerjiyi 150 Hz altına yığıyor → 200–1000 Hz harmonik katman şart. Kör dinleme dosyasında `-stream_loop -ss` çoklu girdi çöker: önce her alıntıyı ayrı wav'a çöz.
- 2026-10-27: Yüksek vuruşları (zil, mühür) cümle sonu boşluğuna (`son+0.02`) koy; SFX −11…−21 dB kazançla WER bozulmuyor.
- 2026-11-02: 253 olayın hepsine ses = yorucu; boş öneri/abone sessiz, kısa whoosh ≥10 sn arayla. OGA ogg float >0 dBFS olabilir → tepe normalizasyonu numpy f32.
- 2026-11-04: Kulaksız ruh hali için `tools/earshot rank` (CLAP) eleme hızlandırır; gerilim sorgusu hep "no match" → ölçümle seç. Content ID: Apple Loops/GarageBand döngülü veya AI şüpheli parça ilk sıraya girmez.
- 2026-11-05: f6.py v3 (kullanılan kesitin LUFS'u + en sabit 40 sn ofset) 8 bölümün 7'sini ilk koşuda 21.7–22.8 dB'e koydu.
- 2026-11-10 (Flip By Vote ses kimliği): Tamamı kendi sentez (`uretim/seri/ses-kimligi/uret.py`, numpy/scipy, earshot venv) + earshot SFX. Ham sentez döngüler konuşma bandına 0.42–0.56 enerji koydu → FFT sıfır faz "yatak_eq" (1.2–3.8 kHz −12 dB) + düşük KS parlaklığı ile 0.06'ya indi, maske ~20 dB. CLAP sentezi "chiptune" diye etiketliyor: karar ölçümle, kör dinleme Niyazi/hakeme açık.
- 2026-11-10: Tık/klik gibi yüksek krestli SFX'te 100 ms RMS kuralı tepeyi 0 dBFS üstüne itti → kazanca tepe tavanı (diyalog tepesi −3 dB) ekle. diyalog.py ilk satırın parantez boşluğunu dosya başına uygulamıyor (BAS 0.15) → metindeki "0.2 sn SLAM, 0.6 ilk replik" sığmaz; `en_az` çapası + ses-yonetmeni'ne baş dolgusu notu.
- 2026-11-10: Dizi cue'su satır kimliğine göreli (`bolum-ses.py cevir`) → ses kilidi değişse de tek komutla yeniden çevrilir; Whisper kelime çapası yanlış duyulursa ("scratched"→"scratch") harf oranı yedeğine düşer, raporda say.
