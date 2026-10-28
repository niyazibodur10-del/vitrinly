# senaryo-yazari — hafıza

## Kurallar
- Telaffuz (Niyazi 2026-10-26): charts→graphs, complicated→confusing, scenarios→possibilities, truth→facts, crashes→collapses/falls; "bold" de yok (Whisper "balls"). Hata grupları: /æ/, /θ/, "ch", çok heceli vurgu → kelimeyi metinde değiştir.
- Kanal **Toonomy**, anlatıcı **Leo** (maskot, danışman değil). İngilizce B2, kısa cümle; **160 kpm**, ≥10 dk → **≥1.750 kelime**. Hook ≤40 kelime (~15 sn); rakamlı hook 36–38.
- F2 betiği: önceki videonun `02-senaryo/senaryo-kontrol.py` (başlık ≤60, hook ≤40 + yasak kelime, açı/sütun sayımı). F3 betiği: `uretim/2026-10-26-1929-1000-dolar/03-metin/metin-kontrol.py` (kpm=160; kelime, ilk 15 sn, ↺ aralıkları, abone, yasak/tavsiye grep, tez, Shorts ≤140 birim, 5-gram).
- **Zaman betikten:** anlatımı yaz → `metin-kontrol.py --yaz` → kanca/tez zamanlarını betikten al. Kanca aralığı hedef ≤75 sn. Kanca GÖRSEL'de `↺ m:ss "ifade"`.
- ANLATIM'da sayılar yazıyla ("nineteen twenty-nine"); tireli sayı kelimeleri süreyi ~%3 uzatır.
- RED düzeltmesi betikle (eski→yeni listesi, her eski tam 1 eşleşme). Düzeltme sonrası ↺ zamanları, retention haritası, abone notu, bölümler ve Shorts süresi aynı turda eşlenir.
- Kaynaksız genelleme yok ("most people…", "millions of people"); Shorts hook'u ölçülmüş tek olguya bağlanır. Karşılaştırmada öteki seçeneğin iyi sonucu da söylenir.
- Leo'ya her senaryoda olay içinde rol ver, gerçek kişiyi canlandırma; rol tablosu dosyada (Ö5).

## Dersler
- 2026-10-27: Birincil kaynaklar açık: Fed History makaleleri (WebFetch), FRED CSV (curl), FDIC PDF (pdftotext), BEA via DBnomics. Konu havuzu ile birincil kaynak çelişirse "about" + dosyada işaretle.
- 2026-10-27: Rakip kalıpları: "real reason/true origin/get wrong", "Most people think… but" yok; yerine Leo'nun yanılgısı ya da ikinci tekil somut sahne. Güçlü konuya birden çok açı yazmak hakeme seçenek ve stok verir.
- 2026-10-27 (F3): Uç ekran köprüsü olmayan videoya söz vermez (genel merak köprüsü). Doğrulayıcı önerisi yeni rakam getiriyorsa görsel/etiket yolunu seç; GÖRSEL'e "(Ö-1)", "§14" gibi etiket yazma (betik sayı sanıyor).
- 2026-10-28 (F2 B slotu, 12 senaryo): `senaryo-kontrol.py` v2 (`uretim/2026-10-28-yeni-video/02-senaryo/`) kalıp başlık, eski açılış, ≥2 elenen hook, Shorts, risk, sonuçtan bağımsızlık ve farklı Leo rolü kontrol ediyor → sonraki F2'de bunu kullan. İlk koşuda 2 başlık 61–62 kr kaldı: "Is Not What It Seems" gibi kısa kalıp yaz.
- 2026-10-28: Takvim olayına (Fed, seçim) bağlı konu → iki dallı yapı veya "tez karardan bağımsız" cümlesi; F7'de yalnız 1 cümle güncellenir. Haber hook'u yazmadan önce 4–6 kaynak sayfasını WebFetch ile oku (TT/Fortune/NAR/MTN açık, NPR 503); rakamsız varyantı yedek tut.
