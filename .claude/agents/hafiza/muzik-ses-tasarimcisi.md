# muzik-ses-tasarimcisi — hafıza

## Kurallar

## Dersler
- 2026-10-26 (devralınan, erişim testi): pixabay, incompetech, freesound ağda engelli; archive.org, opengameart.org, kenney.nl, freemusicarchive.org erişilebilir (HTTP 200). Kevin MacLeod (incompetech) parçaları CC BY → atıf gerekir [genel bilgi, kaynak sitede doğrulanmadı].
- 2026-10-26: Mono anlatım + stereo müzik miksinde ölçüm son stereo dosyada yapılmalı (~+3 LU fark).
- 2026-10-27 (1929-1000-dolar F4): OGA arama filtresi lisansı süzmüyor → her sayfanın `field-name-field-art-licenses` bloğundan lisansı tek tek oku (betik: sayfadaki "license-name" alanı). Çoklu lisans listeli (SA/GPL karışık) parçaları ele, CC0 varken gereksiz belirsizlik.
- 2026-10-27: Üçüncü kişinin yüklediği "PD" parça (örn. FreePD kaynaklı "Countdown to Myocardial Infarction") lisans zinciri doğrulanamazsa ELE. FreePD kapandı. web.archive.org ağda engelli, `archive.org/wayback/available` API'si yalnız kopyanın varlığını gösterir, içeriği göstermez.
- 2026-10-27: Kendi sentez yataklarımız (numpy) enerjinin %75–99'unu 150 Hz altına koyuyor. Telefon bandı (300 Hz–4 kHz) payı ≤0.04 → telefonda neredeyse duyulmuyor. Yatak üretirken 200–1000 Hz'de harmonik/pad katmanı şart. Ölçüt: telefon bandı payı ≥0.08 (Catchy Swing 0.09). Kendi yatağı tek başına değil, CC0 parçanın altına katman olarak kullan.
- 2026-10-27: Kör dinleme dosyalarında ffmpeg'de `-stream_loop -1 -ss` kullanan birden çok mp3/flac girdi "Invalid data" ile çöküyor. Önce her alıntıyı ayrı wav'a çöz (çıkış tarafında -ss), sonra karıştır. Maske ölçütü: müzik −21 LU'da, konuşmalı karelerde 1–4 kHz konuşma/müzik medyanı; ön seçimlerin hepsi ≥20 dB, konuşma bandı ≤0.09.
- 2026-10-27: Müzikal fikir bölümleri birbirine bağlar: açılış swing → 2026 ters köşede electro swing ("aynı kapı bugüne"). Buzzer ve stüdyo kahkahası için CC0 bulunamadı (OGA "buzzer" 0 sonuç). Buzzer kendi sentezimizle çözüldü. Kahkaha için giggling ×3 katman ya da YAL efekti gerekiyor. Lisans kapısı betiği: `uretim/2026-10-26-1929-1000-dolar/06-muzik/lisans-kontrol.py` (negatif testli).
