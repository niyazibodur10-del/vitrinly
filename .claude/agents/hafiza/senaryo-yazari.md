# senaryo-yazari — hafıza

## Kurallar
- Telaffuz kuralı (Niyazi onayı 2026-10-26): seslendirmede zor kelimelerden kaçın, kolay eşanlamlısı: charts→graphs, complicated→confusing, scenarios→possibilities, truth→facts (gerekmedikçe), crashes→collapses/falls. Ayrıca "bold" sorunlu çıktı (Whisper "balls").
- Kanal adı "Financial Rise" her videoda geçer; yeni anlatıcı (TTS) ile okunuşu ses-yonetmeni testinde doğrulanır.
- İngilizce B2, kısa cümle, az deyim; ~140–150 kelime/dk; ≥10 dk → ≥1.500 kelime.

## Dersler
- 2026-10-26 (ses testi, Whisper ölçümü): hatalar 5 ses grubunda toplandı — /æ/ (crash, Financial), /θ/ (truth), "ch" (charts), çok heceli vurgu (scenarios, complicated). Metinde bu kelimeleri azaltmak ses işlemeden daha etkili.
- 2026-10-26: Anlatıcı yapay zekâ sesine geçerse telaffuz listesi TTS ölçümüne göre gevşetilebilir; ses-yonetmeni'nin `tts-rapor.md`'sini kontrol et.
- 2026-10-27 (F2, ilk video 11 senaryo): Kanal adı artık **Toonomy**, anlatıcı **Leo** ("Financial Rise" kuralı geçersiz). Hook ölçüsü: seçilen hook ≤40 kelime (TTS fenrir 0,9 ≈144 kpm → ~15 sn); rakamlar sesli okununca uzar, rakamlı hook'ta 36–38 kelimeyi hedefle. Betik: `uretim/2026-10-26-secim/02-senaryo/senaryo-kontrol.py` (başlık ≤60, hook ≤40 + yasak kelime, açı türü/sütun sayımı) — sonraki F2'lerde aynen kullan; ilk koşuda 1 hook 42 kelimeyle kaldı.
- 2026-10-27: Rakamları senaryo aşamasında birincil kaynaktan çek: Federal Reserve History makaleleri (1929, Great Depression, 1973, 1987, LTCM) WebFetch'te açılıyor ve en temiz sayı kaynağı; PBS Weimar ve ABA Journal (Hunt) da açık. Konu havuzu rakamı ile birincil kaynak çelişebilir (Hunt zirvesi 48,70 vs 49,45; Rentenmark "nine zeros") → hook'ta "about" kullan, çelişkiyi dosyada işaretle.
- 2026-10-27: Rakip özetinden kalıplar: "real reason/true origin/get wrong" başlıkta yok (medyan 0,55); "Most people think… but" aynen yok; yerine Leo'nun yanılgısı ("I used to think…") veya ikinci tekil somut sahne ("It's September 1929. You have…"). Güçlü konuya (1929) birden çok açı yazmak hakeme seçenek verir ve sonraki A slotlarına stok bırakır.
- 2026-10-27: Ö5 için her senaryoda Leo'ya olay içinde bir rol ver (borçlu, dedektif, oyun sunucusu, muhabir, deneyci…) ve gerçek kişileri Leo'ya canlandırma; rol tablosunu dosyada tut (sonraki videolarda tekrar kontrolü için).
