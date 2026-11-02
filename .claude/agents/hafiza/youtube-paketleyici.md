# youtube-paketleyici — hafıza

## Kurallar
- Sayıyı betikten önce yazma: betik → çıktı → metin. Karakter/bayt sınırları betikle, yer tutucu payıyla (+~20 krk).
- Tek kaynak: metinler, yayın zamanı, thumbnail yolu paket.md `veri:` bloklarında; JSON'lar `paket-uret.py`, `paket-kontrol.py` birebir karşılaştırır (F8a BEKL, `--final` hata). Elle JSON yok. Hazır betik: önceki videonun 09-paket'i.
- Yasal not kaynak dosyadan birebir; AI satırı yasal notun son cümlesi + görsel satırı aynı paragrafta. Atıf satırları ve yasal not yasaklı-kelime taramasından muaf.
- Bölümler sahne `bas`'ına aşağı yuvarlanır (fark −1…0, betikle); kurgu ofseti hepsini kaydırır, 00:00 sabit. Yollar `../08-kurgu/…`.
- Dosya adı/yolunu tahmin etme (thumbnail, SRT, Shorts): kaynak ajanın raporu veya `ls`; betik dosya var mı der.
- Final dosya yokken dry-run iki kip: gerçek (yalnız dosya-yok) + bayt-aynı JSON'un sahte medyalı kopyası (ffmpeg color/anullsrc, doğru süre/en-boy) → 0 hata.
- Uç ekran süresi gerçek sesten (son sahne bas→toplam). Yaz/kış saati ofseti tarihe göre (ABD 1 Kas sonrası EST −05:00).
- Shorts açıklamasında uzun video URL yer tutucusu yok: başlık + kanal bağlantısı; köprü Studio "Related video". Shorts açıklama iddiaları Shorts metninde var mı kontrol.
- Başlık: somut özne + rakam; rakip kalıpları regex yasak listesinde ("just hit/passed", "really happening"); doğrulayıcının niteleyicisi ("Nearly") betik kuralı + negatif test.
- Popüler/mevsimsel terim yalnız videoda geçiyorsa (SRT grep); yoksa en fazla etiket, açıklamada vaat yok (support 6390658, 2801973).
- Pinli yorum tek A/B/C sorusu, nötr; "should" yerine "do you want…?".

## Dersler
- 2026-10-26 (kanal): Tanıtıcı müsaitliği `channels?part=id&forHandle=@x` (1 birim) + RDAP .com ile ucuz eleme, sonra kısa listeye search. Yakın yazım/sesli çakışmayı da ara (Toonomy ↔ Tonomy). Maskot adı da marka taramasına girer; kanal adı maskot adı olmaz.
- 2026-10-26: Kanal ilk 150 krk aranan kavramlarla başlar; ritim sözü (gün) tempo 4 hafta tutulmadan yazılmaz. "toon" adı çocuk-içeriği riski → kitle ayarını risk tablosuna yaz.
- 2026-10-26: Eski içerikte "true story" iddialarını kaynakla kontrol et (Grace Walker → gerçek Grace Groner).
- 2026-10-27: Başlık merak + somut özne; açıklama ilk paragrafı arama ifadesini ilk 10 krk'de taşır; başlığı tekrar eden versiyon elenir.
- 2026-10-27: Thumbnail metni okunurluk modeliyle (kutu 704x324, ≤3 satır, eşik 9 px): ≤4 kelime; alt not isteyen sayı thumbnail'a girmez.
- 2026-10-28: Google Trends 429; YouTube `totalResults` talep ölçüsü değil → üst sonuç izlenmesini "API verisi, talep değil" etiketle.
- 2026-11-02 (S08 F8a): Eksik girdiler için `veri:thumbnail-ana` (boşsa alan yok), `{MUZIK_*}` belirteci, `veri:yayin-zamani` (yedek slot satırları) → F8b'de unutma imkânsız.
- 2026-11-02 (S08 F8b): F7 dosyaları ve politika kararı yokken metin işi biter; ama "08-kurgu dosyası var" ve "politika-raporu.md kararı = sentetik_medya" kontrolleri betikte olmalı → paket-kontrol'e eklendi (BEKL / --final hata), F7 sonrası tek komut kalır.
