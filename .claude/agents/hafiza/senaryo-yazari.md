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
- 2026-11-02 (F3 S08): Kilitli `rakam-tablosu.md` gelmeden yazma; gelince "güvenli yazım" sütununu aynen kullan (about 1,050; "credit card" yok; tek kaynak rakamsız). Metin önce yazılıp sonra 40 eski→yeni betikle eşlendi → sıradaki F3'te tabloyu bekle/oku, sonra yaz.
- 2026-11-02: F3 betiği v3 `uretim/2026-10-28-yeni-video/03-metin/metin-kontrol.py`: sayı-kelime ayrıştırıcı + tabloyla tam değer eşleşmesi (1000 kuvveti ölçek, yıllar ayrı), ABONE-n çapa/konum, H7, tablo yasakları. Mantis karşılaştırması yanlış GEÇTİ veriyordu (1025≈1) → tam değer.
- 2026-11-02: "Biggest first" gibi sıralama iddiası rakamlarla çelişti (faiz 3. sırada) → sıra/üstünlük cümlesini tablodaki sıralama satırıyla kontrol et.
- 2026-11-02 (RED-1): "By the end, you'll know…" vaat köprüsü 1929 ve S08'de kullanıldı → sonraki videoda farklı kalıp (soru, sahne ya da karşıtlık). Ortalama/öncelik iddiaları koşullu yaz ("as long as…", "can't skip", "many", "every" değil).
- 2026-11-04 (F2 A/C, 12 senaryo): `senaryo-kontrol.py` v3 (`uretim/2026-11-04-miras-sizintilari/02-senaryo/`, `--sutun A,C`): çalışma başlığında çıplak $/yıl yasak, 2 Shorts "?" ile biter, A'da tarih→gelecek satırı, yayımlanmış Leo rolleri/açılışları yasak → sonraki F2'de bunu kullan. 8 sayfayı WebFetch ile okuyup hook rakamlarını onlardan aldım; Wikipedia rakamları tutarsızsa (Bangladeş 951/851/~1 milyar) hook'a "nearly" + [doğrulanacak].
- 2026-11-04 (F3 S03): Tablo gelmeden birincil kaynakları kendim okudum (Cerulli, IRS, ACL), sonra tablo 6 iddiayı değiştirdi (%70→%56, "inside total" yasak, "more than half"→"about half") → taslağı R-koduyla yaz, tabloda "güvenli yazım" sütununu aynen al. Betik v4 (bu klasör): kaynak etiketi + K1 + yıl ≤2100.
- 2026-11-04: Okafor gibi örnek aile = **kutu** sayısı (≤12, dolar yok) → uydurma rakam riski 0, betik atlar; kutu aritmetiği `veri/kutu-hesap.py` assert + yasak kalıp taraması (meta bölümler hariç tut).
- 2026-11-04 (RED-1): Kapanış köprüsünü "…a story for another X" ile bitirme (1929, S08, S03 = 3. tekrar) → soruyla biten köprü. "Vergi" deme: hangisi olduğunu yaz ("estate tax"); emeklilik hesabından mirasçıya gelir vergisi düşer (R28). "Most feared" tipi kaynaksız üstünlük → "sounds the scariest".
- 2026-11-04: Rakamlı hook'lar ilk koşuda 42 kelimede kaldı → "early reports say" gibi atıfları koru, sıfat/zarf at ("today", "that day"). Sıralı iki sahne ("trucks ↔ one laptop") paradoksu hem hook hem thumbnail hem Shorts'a taşıyor.
