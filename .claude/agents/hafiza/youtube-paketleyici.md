# youtube-paketleyici — hafıza

## Kurallar

## Dersler
- 2026-10-26 (kanal kimliği): Karakter sınırını betikle ölç ve yer tutucu payı bırak — açıklama A ilk hâli 1030 krk çıktı; [iş e-postası] gerçek e-postayla ~+18 krk büyür → hedef ≤960.
- 2026-10-26: Tanıtıcı müsaitliği `channels?part=id&forHandle=@x&key=$YOUTUBE_API_KEY` ile ölçülebilir (boş = kanal yok, kesin müsaitlik değil; Studio son kontrol). @financialrise, @financial_rise, @financialriseofficial başka kanallarda.
- 2026-10-26: Eski içerikte "true story" iddialarını kaynakla kontrol et — "Grace Walker" uydurma/yanlış (gerçek: Grace Groner). Gizli/silinmiş videoların izlenme saati YPP'ye zaten sayılmaz (support 72851) → eski uyumsuz videoları gizlemek maliyetsiz.
- 2026-10-26: Kanal ilk 150 karakteri: marka adıyla değil, aranan kavramlarla başla (test: ilk150'de anahtar sayısı; A 9/11, soru-zinciri B 4/11). Açıklama, oynatma listeleri ve fragman aynı 3 sütun adını taşımalı.
- 2026-10-26: Ritim sözü (takvim v2: Wed/Sun) tam tempo 4 hafta art arda tutulmadan yazılmaz; o zamana kadar "every week" dili.
- 2026-10-26 (kanal adı): İki kelimelik "Money/Coin/Cash + Tales/Story" İngilizce adların ~%90'ının @tanıtıcısı dolu (≈110 ad tarandı). Önce ucuz eleme (forHandle 1 birim + RDAP .com, `rdap.verisign.com/com/v1/domain/<ad>.com`, whois/dig yok), sonra yalnız kısa listeye search (100 birim) → 17 arama yetti.
- 2026-10-26: Çakışma testinde aynı adı değil, sesli/yakın yazımı da ara: "Parabull" → Parable (474K), "Toonomy" → Tonomy kripto + Fact Tonomy (290K), "Coinflick" → CoinFlip (kripto ATM, dolandırıcılık listesi). Yakın yazım bir finans/kripto markasıysa ele.
- 2026-10-26: Maskot adını da marka çakışmasına sok: "Ozan" anlamca mükemmeldi ama TR e-para markası. Kanal adı maskot adı olmaz (AI persona politikası); maskot adı yalnız hikâye içinde.
- 2026-10-26: "toon" içeren ad çocuk-içeriği işareti sayılabilir (answer/9528076: animated characters bir faktör, tek başına karar vermez) → kitle ayarı ve yetişkin konu dilini risk tablosuna yaz.
- 2026-10-27 (1929-1000-dolar F4 taslak): Sayıyı betikten ÖNCE yazma. thumb-konsept'e tahmini "5,6 px / ≥17 px" ve başlık puanlarını elle yazdım; betik 7,6 / 14,0 px ve farklı puanlar verdi, tüm metni düzelttim. Sıra: betik → çıktı → metin.
- 2026-10-27: Başlık ↔ açıklama işbölümü: ilk videoda trafik öneri/gözatma ağırlıklı → başlık merak (ikinci tekil + somut özne), açıklamanın ilk paragrafı arama ifadesini bitişik ve ilk 10 karakterde taşır ("The 1929 stock market crash as a game…", 149 krk). İkinci tekil açıklama versiyonu başlığı tekrar edip anahtar ifadeyi 100. karaktere itti → elendi.
- 2026-10-27: Yasal not "aynen" ve AI satırı "birebir" isteniyorsa: notun son cümlesi AI satırının başıysa aynı paragrafta devam ettir (tek metin, iki koşul). Betik ikisini de birebir arasın; yasal notu kaynak dosyadan okusun (elle kopyalama yok).
- 2026-10-27: Thumbnail metin uzunluğu kuralını okunurluk modeliyle savun (kutu 704x324, ≤3 satır, harf genişliği 0,55×yükseklik, ölçek 168/1280, eşik 9 px): rakip 11 kelime/66 krk → 7,6 px (eşik altı); ≤4 kelime → 14–18,5 px. Alt not gerektiren sayıyı ("$108, price only") thumbnail'a koyma; alt notsuz doğru sayıyı seç (Dow −89 %).
- 2026-10-27: Yasaklı kelime taraması kısa metinlerde masum "should" yakalar (pinli yorum bonus sorusu) → soru kalıbı "do you want … ?" kullan; tarama sözcük düzeyinde, G4 anlam okuması ayrıca elle.
- 2026-10-27 (1929-1000-dolar F8): Tek kaynak düzeni: metinler paket.md `veri:` bloklarında, JSON'lar `paket-uret.py` ile üretilir, `paket-kontrol.py` JSON↔md birebir karşılaştırır. Elle JSON kopyası yok → başlık/açıklama sapması imkânsız.
- 2026-10-27: Final dosyalar yokken dry-run'ı iki kipte koş: gerçek paket (yalnız dosya-yok hatası beklenir) + bayt bayt aynı paketin sahte medyalı kopyası (ffmpeg color/anullsrc, doğru süre ve en-boy, 1280x720 png) → metadata/bölüm/süre/zaman kuralları şimdiden 0 hata kanıtlanır.
- 2026-10-27: Bölümleri sahne `bas` zamanına aşağı yuvarla ve betikle "fark −1…0 sn" ölç; kurguda başa boşluk girerse hepsi aynı ofsetle kayar, 00:00 sabit. Yollar `../08-kurgu/…`, `../09-paket/…` → 09-paket ve teslim/ kardeş klasörlerden aynı paket çalışır.
- 2026-10-27: Üçüncü taraf eser adları (müzik atfı) yasaklı-kelime taramasına takılır ("Unsolved Investigation", "Ragtime!") → atıf satırlarını yasal not gibi aynen-muaf tut. Shorts açıklamasına uzun video URL yer tutucusu koyma (yayınlanma riski); başlık + kanal bağlantısı yaz, asıl köprü Studio "Related video".
- 2026-10-27: Uç ekran süresini metin planından değil gerçek sesten ölç (S24 planı 17 sn → gerçek 13,2 sn). ABD kış saati geçiş günü (2026-11-01) 12:00 ET = UTC−5; ofseti tarihe göre yaz.
