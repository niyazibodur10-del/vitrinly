# Kanal adı kararı — v1 (youtube-paketleyici, 2026-10-26)

**Öneri: kanal adı `Toonomy` · tanıtıcı `@toonomy` · maskot anlatıcının adı `Emre`.**
**Yedek: `Moneta Tales` · `@monetatales`.**
YouTube'da hiçbir şey değiştirilmedi. Değişikliği Studio'da Niyazi yapar (API'de kanal adı/tanıtıcı alanı yok).

Etiketler: **[ölçüm]** bu oturumda API/RDAP/betikle ölçüldü (2026-10-26) · **[D]** birincil kaynak açıldı ve okundu · **[AÖ]** arama özeti · **[ÖB]** ön bilgi, bu oturumda doğrulanmadı · **[T]** tahmin · **[bilinmiyor]**.

Ölçüm yöntemi:
- Tanıtıcı: `channels?forHandle=@<ad>&part=id,snippet,statistics` (1 birim). Boş dönmesi "bu tanıtıcıda kanal yok" demek; kesin müsaitliği Studio son adımda söyler.
- Aynı ad çakışması: `search?type=channel&q=<ad>&maxResults=10` (100 birim) + sonuç kanallarının `channels?id=` istatistiği. "AYNI": harf/rakam dışındaki karakterler atılınca ad birebir aynı. "BENZER": aranan ad, kanal adının içinde geçiyor.
- .com: Verisign RDAP (`rdap.verisign.com/com/v1/domain/<ad>.com`). 404 = kayıt yok, 200 = kayıtlı. whois ve dig kurulu değil, bu yüzden RDAP kullanıldı.
- Okunurluk: Liberation Sans Bold'da 100 pt piksel genişliği (göreli karşılaştırma için).
- Kota: 17 arama (≈1.700 birim) + ≈140 tanıtıcı sorgusu (≈140 birim). Ham çıktılar commit'lenmedi; komutlarla yeniden üretilebilir.

---

## 0. İsim brifi (adaylardan önce yazıldı)
- **Vaat:** karmaşık para olaylarını takip edilebilir animasyonlu hikâyelere çevirmek. Kapsam bugün (haber), dün (çöküşler) ve yarın (senaryolar).
- **Hissettirmesi gereken:** merak, netlik, güven, oyunbazlık. Hırs ya da "zengin ol" değil.
- **Adın yapması gereken:** animasyon/hikâye ile parayı ya da ekonomiyi tek kelimede ima etmek. Kişi veya uzman izlenimi vermemek. Tek bir sütuna kilitlenmemek. ≤20 karakter, banner'da tek satır.
- **Yasaklar:** rich, millionaire, wealth, money hack, passive income, guru, coach, advisor, pro, "Dr./Prof.", "Ask …". Kanal adı maskotun adı olmayacak (AI personası politikası, bkz. §5).

## 1. Uzun liste — 24 temsilci aday (toplam ≈110 ad tarandı) [ölçüm]
| # | Aday | Strateji | @tanıtıcı | .com | Hızlı eleme |
|---|---|---|---|---|---|
| 1 | Financial Rise (mevcut) | tanımlayıcı | başkasında (@financialrise vb.) | — | ≥3 aynı adlı kanal; "rise" = zenginleşme çağrışımı |
| 2 | Animated Money | tanımlayıcı | dolu (2.060 abone, 52 video) | kayıtlı | doğrudan çakışma |
| 3 | Finance Tales | tanımlayıcı | **boş** | kayıtlı | jenerik, tescili zayıf |
| 4 | Story of Money | tanımlayıcı | dolu | kayıtlı | jenerik |
| 5 | Money Explained (tür) | tanımlayıcı | — | — | rakip kalıbı (Economics Explained) |
| 6 | Monetoon | uydurma | dolu (18 abone) | boş | tanıtıcı yok |
| 7 | Fintoon | uydurma | dolu (1.150 abone) | kayıtlı | çakışma |
| 8 | Econimate | uydurma | dolu (18.800 abone) | kayıtlı | güçlü çakışma |
| 9 | Moneyverse | uydurma | dolu (14.000 abone) | kayıtlı | güçlü çakışma |
| 10 | Cartoonomics | uydurma | dolu (150 abone) | kayıtlı | çakışma, uzun |
| 11 | **Toonomy** | uydurma (toon + economy) | **boş** | **boş** | kısa listeye |
| 12 | Coinimation | uydurma | **boş** | boş | kısa listeye |
| 13 | Coinflick | uydurma (coin + flick = film) | **boş** | kayıtlı | kısa listeye |
| 14 | Moneta Tales | metafor/köken (Moneta = "money" kelimesinin Latince kökü) | **boş** | **boş** | kısa listeye |
| 15 | Fiat Tales | metafor (fiat money) | **boş** | boş | kısa listeye |
| 16 | Nickel Tales | metafor | **boş** | boş | kısa listeye |
| 17 | Pocket Change | deyim/metafor | **boş** | kayıtlı | kısa listeye |
| 18 | Paper Trail | deyim/metafor | **boş** | kayıtlı | kısa listeye |
| 19 | Banknotes | kelime oyunu (bank + notes) | **boş** | kayıtlı | kısa listeye |
| 20 | Parabull | TR köken (para) + bull, "parable" sesi | dolu (0 abone) | kayıtlı | kısa listeye (@parabulltv boş) |
| 21 | Boom & Bust | metafor | **boş** | kayıtlı | RT'nin "Boom Bust" finans programı [ÖB]; çöküşe kilitli |
| 22 | Mint Condition | deyim | **boş** | kayıtlı | aynı adlı R&B grubu [ÖB]; koleksiyon çağrışımı |
| 23 | Ka-Ching | ses taklidi | **boş** | kayıtlı | "para kazan" çağrışımı (spam/YMYL) |
| 24 | Money with Ozan / Ozan Explains | maskot adlı | **boş** | boş | kanal adı = AI persona riski; "Ozan" ayrıca TR'de bir e-para/fintek markası [ÖB] |

Taranan öteki adlar (tanıtıcısı dolu ya da .com'u kayıtlı olanlar; hepsi elendi): Cashtoon, Finimation, MoneyLore, CoinTales, MarketTales, DollarTales, MintTales, PennyTales, MoneyUnfolded, LedgerLane, TheMoneyMap, CoinChronicles (1.200 abone), MoneyRewind, PennyPlot, Coinlore, TheMoneyStory, CashCartoons, TheLedger, MoneyMotion, MoneyTimeline, TheCoinStory, PennyDrop, DimeStories, TickerTales, MoneyMatinee (207 abone), Mintory, TheMoneyReel, Moneyscope, Tickertoon, MoneyFables, FiscalFables, Mintline, Moneyquake, Buckstory, Coinmotion, MoneyOdyssey, Moneyloop, Ledgerly, Monetales, Cointoon, Coinverse, Moneymation, Econotoons, Finanimate, Coinrama, WalletTales, SmallChange, LedgerLore, MoneyMyth, Dollaroo, Moneybard, Moneyfold (2.730 abone), FiatFables, Coinstory, DollarDiaries, Tickerfable, MarginNotes, PettyCash, Moneta, MoneyClock, ThenNowNext, Moneysaga, Coinsaga, Ledgersaga, TwoBits, BearTales, Akche, MoneyParables, Toonomics, Moneytoon(s), Animonomics, Coinreel, Econlore, Storymint (9 aynı adlı kanal), CopperTales, BullionTales, Coinloom.
**Bulgu:** "Money/Coin/Cash + Tales/Story" kalıbındaki iki kelimelik İngilizce adların neredeyse hepsinin tanıtıcısı alınmış. Ayırt edici ve tescil edilebilir ad yalnız uydurma veya köken-metafor stratejisinden çıkıyor.

## 2. Kısa liste — çakışma testi (YouTube Data API, 2026-10-26) [ölçüm]
Arama `type=channel`, ilk 10 sonuç. "En büyük aynı/benzer" sütunu, aynı ya da benzer adlı kanallar içinde en çok aboneye sahip olanı gösterir.

**1. tur (6 aday): 4'ü elendi**
| Aday | AYNI | BENZER | En büyük aynı/benzer | Ad dışı kanal gürültüsü | Karar |
|---|---|---|---|---|---|
| Pocket Change | 3 | 7 | Pocket Change Reselling Podcast, 534 abone | — | ❌ 10 sonucun 10'u bu ad |
| Paper Trail | 2 | 8 | arelle's paper trail, 5.690 abone; **@papertrailexplainers** var | — | ❌ 10 sonucun 10'u bu ad |
| Banknotes | 1 | 2 | Banknotes (@bankreacts), 5.960 abone | Ahmed Hisham Banknote, 283.000 abone (koleksiyon) | ❌ arama banknot koleksiyonculuğuna gidiyor |
| Parabull | 1 | 4 | PARABULLS, 50 abone | **Parable: Free History Documentaries, 474.000 abone** | ❌ sesli aramada "parable" ile karışıyor |
| Coinflick | 1 (13 abone, 0 video) | 2 | Coin Flicks, 5 abone | — | kısa listede kaldı |
| Moneta Tales | 0 | 3 | moneta, 7 abone | "Moneta Vault, History of Money" (1 abone) ve @moneta_history (4 abone) aynı nişte | kısa listede kaldı |

**2. tur (yeni adaylar)**
| Aday | AYNI | BENZER | En büyük aynı/benzer | Not | Karar |
|---|---|---|---|---|---|
| **Toonomy** | **0** | **0** | — (yakın ad: Toonomic, 1 abone, 1 video) | "Toonomy finance" araması da 0 aynı, 0 benzer | ✅ |
| Toonomics | 4 | 1 | Toonomics (@toonnomics), 156 abone, 112 video | tanıtıcı dolu | ❌ |
| Coinimation | 1 | 0 | Coinimation, 97 abone, 5 video | — | ⚠️ |
| Fiat Tales | 0 | 0 | — | sonuçlarda FIAT Japan Official (4.950 abone) | ⚠️ |
| Nickel Tales | 0 | 0 | — (Nickel Stories, 5 abone) | — | ✅ |
| Storymint | 9 | 1 | StoryMint, 16.300 abone | — | ❌ |

**Kesin kısa liste (6):** Toonomy, Moneta Tales, Nickel Tales, Coinflick, Fiat Tales, Coinimation.

## 3. Finalistler — ilk 3 tablo
| Ölçüt | **Toonomy** (kazanan) | **Moneta Tales** (yedek) | Nickel Tales |
|---|---|---|---|
| Uzunluk | **7 karakter**, 3 hece | 12 karakter, 5 hece | 12 karakter, 4 hece |
| @tanıtıcı | **@toonomy boş** [ölçüm]. Yedekler @toonomytv ve @toonomyhq da boş | @monetatales boş [ölçüm] | @nickeltales boş [ölçüm] |
| YouTube aynı ad / benzer | **0 / 0** | 0 / 3 (hepsi ≤7 abone, ama aynı "para tarihi" nişinde) | 0 / 0 |
| .com | **toonomy.com kayıtsız** [ölçüm, RDAP 404] | monetatales.com kayıtsız [ölçüm] | nickeltales.com kayıtsız [ölçüm] |
| Web/marka çakışması | Tam yazımla web sonucu ve tescilli marka bulunamadı [AÖ]. Yakın yazımlı **Tonomy (TONO)** bir kripto kimlik token'ı [AÖ]. YouTube'da "Tonomy" araması 290.000 aboneli **Fact Tonomy** kanalını getiriyor [ölçüm] | **MONETA Money Bank** (Çek bankası, Prag borsasında) ve finans hizmetleri sınıfında "MONETA" ABD markası (seri no. 86036884) [AÖ]. Bizim sınıfımız eğitim/eğlence (41), yine de finans bağlamında kalabalık | Bariz marka bulunamadı [ÖB] |
| Anlam / vaat | toon (animasyon) + economy (ekonomi). Adın kendisi "animasyonla ekonomi" diyor. Üç sütunu da kapsıyor | "Para"nın kökeni (Juno Moneta tapınağı darphanesi) + hikâyeler. Güçlü "hakkında" hikâyesi var ama tarih sütununa yaslanıyor | Nickel = 5 sent. ABD'ye özgü, "küçük para" çağrışımı. Büyük krizleri anlatan kanala zayıf geliyor |
| WIPO ayırt edicilik | **Uydurma / ima eden**, en güçlü sınıf | ima eden (Latince kelime + jenerik "tales") | keyfi + jenerik |
| Telaffuz / yazım | "TOO-nuh-mee". Duyan "Toonomy" ya da "Tonomy" yazabilir (⚠️) | "mo-NEH-ta" / "mo-NAY-ta" belirsiz; "Monetta" ya da "Moneda" yazılabilir | kolay |
| YMYL / spam çağrışımı | yok | yok | yok |
| Uzman/kişi izlenimi | yok (kavram adı) | yok | yok |
| Büyümeye açık mı | ✅ ekonominin her konusu | ⚠️ tarih ağırlıklı | ⚠️ |
| Okunurluk (100 pt genişlik) | **446 px**. 800 px profil dairesinin %80'ine 143 pt'ye kadar sığıyor | 630 px (101 pt) | 574 px (111 pt) |
| Çocuk içeriği algısı | ⚠️ "toon" + çizgi maskot, iki çocuk çekiciliği işareti (bkz. §6) | düşük | düşük |
| **Sonuç** | **Kazanan** | **Yedek** | Elendi: anlamı vaadi taşımıyor, ABD'ye özgü |

Kısa listeden elenenler:
- **Coinflick:** kripto ATM şirketi **CoinFlip**'e görsel ve sesli olarak çok yakın. Tayvan dolandırıcılık veritabanı "COINFLIP" adını ve benzerlerini dolandırıcılık listesinde tutuyor [AÖ]. Finans kanalı için güven kaybı ve kripto spam çağrışımı.
- **Fiat Tales:** FIAT ünlü bir otomobil markası (sulandırma/çağrışım riski) ve sonuçlarda FIAT Japan çıkıyor [ölçüm]. "Fiat" genç ve genel kitlede anlaşılmayabilir, kripto topluluğunda ise "fiat"a karşı söylemi çağrıştırıyor [T].
- **Coinimation:** aynı adlı bir kanal var (97 abone) [ölçüm]. 11 karakter. "Coin" kripto okunuyor [T].

## 4. Kazanan gerekçesi — neden Toonomy
1. **Aramada sahiplenilebilir.** YouTube'da aynı ya da benzer adlı kanal sayısı 0 [ölçüm]. Tanıtıcı ve .com boş [ölçüm]. Financial Rise'ın 3+ aynı adlı kanalla yaşadığı karışma sorunu tamamen kalkıyor.
2. **Ad vaadi taşıyor ama tarif etmiyor.** Thumbnail ve başlık "animasyonlu finans hikâyesi" der, ad da aynı şeyi tek kelimede söyler. Tek vaat, üç temas noktası. "Economy" geniş bir kavram, bu yüzden haber, tarih ve gelecek sütunlarının hepsine uyuyor.
3. **Politika açısından temiz.** Kişi adı değil, uzman unvanı değil, "zengin ol" çağrışımı yok. AI persona maddesinin hedef aldığı "insan uzman tavsiye veriyor" algısından uzak [D: support.google.com/youtube/answer/1311392, `docs/monetizasyon.md` §3.2].
4. **Görsel olarak en kısa finalist.** 7 karakter, Financial Rise'ın yarısı (446 px'e karşı 672 px). Profil dairesinde, filigranda ve küçük thumbnail köşesinde okunuyor. "OO" harfleri göz ya da madeni para olarak logoya dönüşebilir (thumbnail-tasarimcisi'ne not).
5. **Tescil edilebilir sınıfta.** Uydurma kelime, WIPO ölçeğinin en güçlü ucu. Tam yazımla bir marka kaydı bulunamadı [AÖ]. Derin hukuki arama yapılmadı.

### Kazananın riskleri ve önlemleri
| Risk | Seviye | Önlem |
|---|---|---|
| **Tonomy/Fact Tonomy karışması.** Sesli duyan "Tonomy" yazarsa kripto token ya da 290 bin aboneli kanal çıkar | Orta-düşük [T] | Tam yazım her yerde. Shorts kapanış kartında ve fragmanda adı yazılı göster ("T-O-O-N-O-M-Y" seslendirme gerekmez). Logo "OO"yu vurgulasın |
| **Çocuk içeriği algısı.** YouTube ve FTC ölçütlerinde "animated characters or cartoon figures" bir işaret ve meta veri hedef kitleyi gösteriyor. Ancak *"Animated content that appeals to everyone"* genel izleyici örneği olarak sayılıyor ve tek işaret karar vermiyor [D: support.google.com/youtube/answer/9528076] | Düşük-orta [T] | Kanal ve video kitlesi "Hayır, çocuklara özel değil" (mevcut ayar). Konular yetişkin (enflasyon, banka iflası). Açıklama ilk satırı "finance" ile başlıyor. Çocuk diliyle başlık yok |
| Tam yazımla marka kaydı aranmadı | [bilinmiyor] | Kanal büyürse USPTO ve EUIPO'da sınıf 41 için "TOONOMY" ön araması (Niyazi, ücretsiz) |
| "Toon" kelimesi bazı yetişkinlere hafif gelebilir | Düşük [T] | The Infographics Show gibi yetişkin izleyicili animasyon kanalları var (`docs/rakip-analizi.md` G1). Ton başlık ve thumbnail'den gelir |

## 5. Maskot anlatıcının adı: **Emre**
- **Neden:** Türkçede "dost, arkadaş" anlamına gelir; halk ozanı Yunus Emre'yi de çağrıştırır [ÖB]. Rol tanımına tam oturuyor: bilgili bir arkadaş, danışman değil. İki hece, İngilizce konuşan biri "EM-ray" ya da "EM-ree" der, ikisi de anlaşılır. Karakterin kökeniyle uyumlu (`assets/karakter/karakter-karti.md`: 30'larının başında Türk erkek).
- **Kurallar (AI personası, [D] answer/1311392):** "Dr.", "Prof.", "Coach", "Advisor" unvanı yok. Kanal adı maskot değil. Açıklama ve Hakkında'da "Emre is a fictional cartoon character, not a financial advisor." Emre senaryoda anlatır, soru sorar, şaşırır. "You should buy…" demez.
- **Elenen maskot adları:** Ozan (anlamı mükemmel, "ozan" = hikâye anlatıcısı, ama TR'de aynı adlı bir e-para/fintek markası var [ÖB]; finans kanalında karışıklık yaratır), Kaan ("Khan" okunur, hükümdar çağrışımı otoriter), Can (İngilizcede "can" kelimesi), Efe ve Kerem (yedek).
- [ÖB] Emre yaygın bir ad, bariz bir finans markası bilinmiyor. @emre tanıtıcısı bir kişide (önemsiz, maskot için tanıtıcı açılmayacak).

## 6. YouTube ad ve tanıtıcı kuralları (kaynaklı kontrol)
| Kural | Durum | Kaynak |
|---|---|---|
| Kanal adı **14 günde en fazla 2 kez** değiştirilebilir | Bir kez, son haliyle değiştir. Yedek hakkı yanlışlık için kalsın | [D] support.google.com/youtube/answer/2657964 |
| Ad değişince **doğrulama rozeti kalkar** | Kanalda rozet yok (2 abone) → etkisi yok | [D] answer/2657964 |
| Yeni adın her yerde görünmesi **birkaç gün sürebilir** | Fragman ve banner yayınını buna göre planla | [D] answer/2657964 |
| Ad çevirileri varsa önce silinmeli | Kanalda çeviri yok [ÖB] | [D] answer/2657964 |
| Tanıtıcı **14 günde en fazla 2 kez** değiştirilebilir | Bir kez | [D] answer/2657964 |
| Tanıtıcı 3–30 karakter. Harf, rakam, `_`, `-`, `.`, `·` kullanılabilir; ayırıcı başta veya sonda olamaz. Büyük/küçük harf duyarsız. URL ya da telefon numarası gibi görünemez | `toonomy` uygun | [D] support.google.com/youtube/answer/11585688 |
| Tanıtıcı kanalın yeni URL'si olur (youtube.com/@toonomy). **Eski özel URL'ler çalışmaya devam eder** | 2013 hesabının eski bağlantıları kırılmaz | [D] answer/11585688 |
| Eski tanıtıcının (@finansialrise) ne kadar süre ayrılacağı | Sayfa belirtmiyor → [bilinmiyor]. Eski tanıtıcının bir süre ayrılı kaldığı [ÖB] | answer/11585688 |
| Tanıtıcı satılamaz veya devredilemez. YouTube geri alabilir | — | [D] answer/11585688 |
| Kanal adı ve tanıtıcı API'de değiştirilemez | Studio'da Niyazi | `mevcut-durum.md` |

## 7. Studio'da adım adım değiştirme (Niyazi, masaüstü)
Önce: bu dosyadaki öneriyi onayla. Ad ve tanıtıcıyı **aynı oturumda bir kez** değiştir.
1. studio.youtube.com'a kanal hesabıyla gir.
2. Sol menü → **Özelleştirme** (Customization) → **Profil** (Profile) sekmesi.
3. **Ad** alanına `Toonomy` yaz (büyük T, geri kalanı küçük).
4. **Tanıtıcı** alanına `toonomy` yaz ve müsaitlik işaretini bekle. Alınmışsa sırayla `toonomytv`, sonra `toonomyhq` dene (ikisi de 2026-10-26'da boştu).
5. Sağ üstten **YAYINLA** (Publish).
6. Kontrol: youtube.com/@toonomy açılıyor mu, ad "Toonomy" mu? (Her yerde görünmesi birkaç gün sürebilir.)
7. Aynı ekranda profil fotoğrafını yeni logoyla değiştir. Bu, thumbnail-tasarimcisi işi; mevcut `profil-800.png` ve `banner-2560x1440.jpg` eski adı taşıyorsa yenilenir.
8. Bana (koordinatör) "değişti" de. Koordinatör `kanal-paketi.json`'u §8'deki taslakla günceller, `python3 tools/yayin/kanal.py uretim/kanal-kimligi/kanal-paketi.json` fark raporunu gösterir ve onayınla `--uygula --onayli` çalıştırır.
**Yapma:** Aynı gün ikinci bir deneme ismi yayınlama (14 günde 2 hak). Google hesabının adını değiştirme (kanal adından ayrı) [ÖB].

## 8. kanal-paketi.json için taslak blok (dosya değiştirilmedi)
Yalnız adın geçtiği alanlar değişiyor. Ölçüm [ölçüm]: açıklama 905 → **906** karakter (≤1000), ilk 150 karakter aynı (9/11 anahtar korunuyor). Anahtar kelimeler 419 → **410** karakter (≤500). Yasaklı kelime eklenmedi.

```json
{
  "aciklama": "Animated finance stories: today's money news explained, history's biggest financial crashes, and \"what if\" scenarios for the future of money.\n\nToonomy turns complex money events into animated stories you can follow, told by Emre, our cartoon narrator:\n• Money News, Explained: interest rates, inflation, bank failures and market moves, broken down while they are still news.\n• The Collapse: the 1929 crash, Weimar hyperinflation, tulip mania, Lehman and other moments that reshaped money.\n• What If…: plausible scenarios about the dollar, AI, banks and the economy. Scenarios, not predictions.\n\nEvery video is researched and fact-checked, with sources in its description.\n\nNew animated finance stories every week, plus Shorts.\n\nEducational content, not financial advice. We never tell you what to buy or sell.\nNarration voice is AI-generated. Emre is a fictional cartoon character, not a financial advisor.",
  "anahtar_kelimeler": "Toonomy \"animated finance\" \"finance explained\" \"money news explained\" \"financial news\" \"financial history\" \"economic history\" \"stock market crash\" \"1929 crash\" hyperinflation \"Weimar Germany\" \"financial crisis\" \"bank collapse\" \"economic bubbles\" \"what if scenarios\" \"future of money\" \"economy explained\" inflation \"interest rates\" recession \"federal reserve\" \"stock market\" crypto \"finance animation\" economics",
  "oynatma_listeleri (yalnız değişen 2 liste)": [
    {
      "baslik": "Money Stories in 60 Seconds | Shorts",
      "aciklama": "Short animated money stories from Toonomy: one surprising fact from financial history, the news or a future scenario in under a minute. Each Short links to the full video.\n\nEducational content, not financial advice. Narration voice is AI-generated."
    },
    {
      "baslik": "Start Here: Best of Toonomy",
      "aciklama": "New to Toonomy? Start with these animated finance stories: one great financial crash, one money news story explained and one what-if scenario about the future. Updated as new favourites appear.\n\nEducational content, not financial advice. Narration voice is AI-generated."
    }
  ]
}
```
Ayrıca güncellenecek: `kanal-metinleri.md` §1 açıklama metni, `docs/monetizasyon.md` K9 maddesi (@tanıtıcı → @toonomy), video açıklama şablonundaki kanal adı, fragman senaryosu (senaryo-yazari), logo/banner/filigran (thumbnail-tasarimcisi). Hepsi ad onaylandıktan sonra.

## 9. Doğrulanması gerekenler (bu çalışma kesinleştiremez)
- **Marka:** USPTO ve EUIPO'da "TOONOMY" sınıf 41/38 ön araması (ücretsiz, Niyazi). Şu an yalnız [AÖ].
- **Tanıtıcı:** Studio'daki müsaitlik işareti son söz.
- **Alan adı:** toonomy.com 2026-10-26'da kayıtsızdı [ölçüm]. Satın almak para harcamak demek → yalnız Niyazi kararıyla.
- **Sosyal medya (X/Instagram/TikTok) kullanıcı adları:** ölçülmedi [bilinmiyor].
- **Ana dili İngilizce olan biriyle sesli test:** "Toonomy" deyip yazdırma (Tonomy karışmasını ölçmek için, 5 kişi).
