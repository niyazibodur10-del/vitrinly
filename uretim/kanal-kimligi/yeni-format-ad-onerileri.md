# Yeni format için kanal ve seri adı önerileri (youtube-paketleyici, 2026-11-10)

**İLERLEME: tamam.** Hiçbir platformda hesap açılmadı, ad değiştirilmedi. Kullanıcı adını almak ve YouTube'da adı değiştirmek Niyazi'nin işi (Studio ve uygulamalar).
**Öneri:** kanal **You Call The Flip** · tanıtıcı **@youcalltheflip** (IG, YT, TT). Seri adı **"$100 → $1M"**. Yedek: **Hundo to Million** · @hundotomillion.
**Kapı:** ilk 5 adayın üç platformdaki kullanıcı adı iki ayrı koşuda da BOŞ çıktı [ölçüm]. Beşinin .com alan adı da kayıtsız (RDAP 404) [ölçüm]. Marka taraması yalnız arama özetine dayanıyor [AÖ], hukuki görüş değil.

Etiketler: **[ölçüm]** bu oturumda betikle ölçüldü (2026-11-10). **[AÖ]** web arama özeti, birincil kaynak açılmadı. **[T]** tahmin veya yorum. **[ÖB]** ön bilgi, bu oturumda doğrulanmadı.
Durum sözlüğü: **BOŞ** = bu adda profil yok, müsait görünüyor. **DOLU** = bu adda profil var. **belirsiz** = yöntem karar veremedi.
Kesinlik notu: BOŞ, "kayıt kesin alınır" demek değildir. Kapatılmış, askıya alınmış veya platformca ayrılmış adlar da "bulunamadı" görünür. Kesin cevabı hesap açma ekranı verir.

## 1. Yöntem ve doğrulama
Betik: `uretim/kanal-kimligi/ad-kontrol.py` (`python3 -I ad-kontrol.py <ad> …`, `YOUTUBE_API_KEY` gerekir). Varsayılan curl istemcisiyle çalışır, kimlik taklidi yok. İstekler arasında 4 sn bekler.

| Platform | Ayırt eden sinyal | Doğrulama: var olan hesap (instagram, nasa) / rastgele ad (qzxv8k2lmpwq9rt) |
|---|---|---|
| Instagram `instagram.com/<ad>/` | Varsa HTTP 200, `og:title` = "… (@ad) • Instagram photos and videos" ve `og:type=profile`. Yoksa HTTP 200, `og:title` yok, sayfada `PolarisErrorRoot` var. **302 giriş yönlendirmesi = belirsiz**: 8 sn arayla 3 deneme yapılır, sonra öyle bırakılır. | instagram ve nasa DOLU, rastgele ad BOŞ (beklenen sonuç) |
| YouTube `youtube.com/@<ad>` | Data API `channels?forHandle=@ad` totalResults (1 birim) **ve** web HTTP kodu (200/404). İkisi uyuşmazsa belirsiz. | youtube DOLU, rastgele ad BOŞ (API 0, web 404) |
| TikTok `tiktok.com/@<ad>` | Sayfadaki `"statusCode"`: 0 = var, 10221 = kullanıcı yok, 10222 = gizli hesap (dolu sayılır). Sayfa başlığı ayırt etmiyor, ikisinde de "TikTok - Make Your Day". | tiktok DOLU, rastgele ad BOŞ |
| .com | Verisign RDAP: 404 = kayıt yok | — |

Instagram'ın oturumsuz isteğe verdiği yanıt ilk 2 istekte ayırt ediciydi. Yoğun sorguda 302 (giriş sayfası) gelmeye başladı. O adlar "belirsiz" diye yazıldı. Tahmin yapılmadı.

## 2. Uzun liste: 32 ad tarandı [ölçüm, 2026-11-10]
Fikir eksenleri: **K** = izleyici yönetir, **P** = $100'dan $1M'a, **A** = al-sat ("flip"). "hundo", ABD gençlik argosunda "100" demek.

| # | Aday (görünen ad) | Tanıtıcı | IG | YT | TT | Eksen | Not |
|---|---|---|---|---|---|---|---|
| 1 | **You Call The Flip** | youcalltheflip | BOŞ | BOŞ | BOŞ | K+A | kısa listeye |
| 2 | **Hundo to Million** | hundotomillion | BOŞ | BOŞ | BOŞ | P | kısa listeye (hundotomil de BOŞ/BOŞ/BOŞ) |
| 3 | **Call The Flip** | calltheflip | BOŞ | BOŞ | BOŞ | K+A | kısa listeye |
| 4 | **Hundo Flip** | hundoflip | BOŞ | BOŞ | BOŞ | P+A | kısa listeye |
| 5 | **Flip By Vote** | flipbyvote | BOŞ | BOŞ | BOŞ | K+A | kısa listeye |
| 6 | The Million Flip | themillionflip | BOŞ (2. denemede; 1. denemede 302) | BOŞ | BOŞ | P+A | HGTV'nin "Flip to a Million" dizisine çok yakın [AÖ] |
| 7 | Vote The Flip | votetheflip | BOŞ | BOŞ | BOŞ | K+A | "Flip By Vote" ile aynı, emir kipi daha zayıf |
| 8 | Choose The Flip | choosetheflip | BOŞ | BOŞ | BOŞ | K+A | "Call"dan uzun ve daha düz |
| 9 | Comment To Flip | commenttoflip | BOŞ | BOŞ | BOŞ | K+A | "comment to win" kalıbı: Meta'nın etkileşim avcılığı (engagement bait) sinyaline benziyor [T] |
| 10 | The Flip Vote | theflipvote | BOŞ | BOŞ | BOŞ | K+A | ad gibi değil, özellik gibi duruyor |
| 11 | Your Move Bros | yourmovebros | BOŞ | BOŞ | BOŞ | K | parayı ve al-satı çağrıştırmıyor |
| 12 | Deal By Vote | dealbyvote | BOŞ | BOŞ | BOŞ | K | "deal" daha az genç işi |
| 13 | Million By Vote | millionbyvote | belirsiz (302) | BOŞ | BOŞ | K+P | IG belirsiz, uzun |
| 14 | Flip to Million | fliptomillion | BOŞ | DOLU | DOLU | P+A | elendi, HGTV dizisi de var |
| 15 | 100 to Mil | 100tomil | DOLU | BOŞ | BOŞ | P | elendi (IG dolu) |
| 16 | 100 to Million | 100tomillion | DOLU | DOLU | DOLU (gizli) | P | elendi |
| 17 | Hundred to Million | hundredtomillion | DOLU | DOLU | DOLU | P | elendi |
| 18 | Hundo Hustle | hundohustle | DOLU | DOLU | DOLU | P | elendi; "hustle" ayrıca YMYL'de spam çağrışımı taşıyor |
| 19 | You Flip It | youflipit | DOLU | BOŞ | BOŞ | K+A | elendi (IG dolu) |
| 20 | Flip Vote | flipvote | DOLU | BOŞ | BOŞ | K+A | elendi (IG dolu) |
| 21 | Jake and Mike | jakeandmike | DOLU | DOLU | DOLU | karakter | elendi |
| 22–32 | Flip Choice, Flip Crew, Million Move, Flip100, Flip Squad, Flip With Us, Hundred Flip, Your Flip | flipchoice, flipcrew, millionmove, flip100, flipsquad, flipwithus, hundredflip, yourflip | — | — | — | — | hepsi en az bir platformda DOLU, elendi |

Bulgu: "100/hundred/million + to" kalıbındaki düz adların hepsi alınmış. Boş kalan adlar ya "izleyici seçer" fiilini taşıyor ya da "hundo" argosunu kullanıyor.

## 3. Marka ve çakışma riski (ABD) [AÖ, hukuki görüş değil]
- **"Flip"**: tek başına çok sayıda USPTO kaydı var (yazılım, giyim, reklam vb.). ABD'de Gen Z'ye yönelik bir sosyal alışveriş uygulamasının adı da "Flip". Bileşik adlarda ("You Call The Flip") ayırt edicilik ifadeden gelir. **Risk: düşük–orta** [T]. ABD'de "flip" ayrıca ev al-satını (house flipping) çağrıştırır. Bu, konseple uyumlu.
- **HGTV "Flip to a Million"**: iki ekibin mülk al-satıyla 1 milyon dolara ulaşmaya çalıştığı bir realite dizisi. Kavram aynı. "Flip to Million" ve "The Million Flip" bu yüzden **orta–yüksek risk**, ilk 5'e alınmadı.
- **"HUNDO"**: Sınıf 41'de (eğlence) canlı kayıtlar var. Hundo Exchange (fantezi spor uygulaması, Reg. 6988472) ve THE HUNDO (Shift Events, Reg. 7613611). "Hundo to Million" ve "Hundo Flip" bileşik ve farklı hizmet olsa da **risk: orta** [T]. Yayından önce USPTO TSDR'de birebir arama önerilir.
- "You Call The Flip", "Call The Flip", "Flip By Vote", "Hundo Flip", "Hundo to Million": aramada aynı adlı bir marka, dizi veya kanal çıkmadı [AÖ].
- Kanal adında "millionaire", "rich", "trading", "invest" yok. Seri hesap işi değil al-sat hikâyesi. Bu, finans tavsiyesi ve "kolay para" algısını (YMYL/spam) azaltır [T].

## 4. İlk 5 (sıralı)
| # | Kanal görünen adı | IG / YT / TT kullanıcı adı | Gerekçe | Ana risk |
|---|---|---|---|---|
| 1 | **You Call The Flip** | @youcalltheflip (üçünde de) | İki çekirdek fikir tek cümlede: izleyici karar verir (you call) ve al-sat (flip). Slogan ("You control it") ve her bölümün kapanış CTA'sıyla aynı şeyi söylüyor. 14 karakter, sesli söylenince yazımı açık. | "flip" kelimesi jenerik ve Flip uygulamasıyla aynı. Bileşik olduğu için düşük–orta. |
| 2 | **Hundo to Million** | @hundotomillion (üçünde de; kısa yedek @hundotomil da boş) | $100'dan $1M'a hedefini en net anlatan ad. "Hundo" ABD gençlik argosu, akılda kalıyor. Seri adı olarak da çalışıyor. | Sınıf 41'de HUNDO kayıtları var (orta). "İzleyici yönetir" fikri adda değil, slogana kalıyor. |
| 3 | **Call The Flip** | @calltheflip | 1. adayın en kısa hali (11 karakter). İzleyiciye emir kipi: "sen karar ver". | "Call" tek başına bahis veya opsiyon ("call option") çağrıştırabilir [T]. |
| 4 | **Hundo Flip** | @hundoflip | 9 karakterle en kısa aday. $100 ve al-sat birlikte. Logo ve profil resminde iyi durur. | HUNDO markası (orta). Hedef ($1M) ve izleyici kontrolü adda yok. |
| 5 | **Flip By Vote** | @flipbyvote | Mekanik apaçık: bir sonraki al-satı oy belirler. | "Vote" ABD'de siyasi çağrışım taşır. Yorum mekaniği "oy" değil "fikir"; fark yanlış beklenti yaratabilir. |

**Önerilen eşleşme:** kanal **You Call The Flip** + seri adı **$100 → $1M** (bölüm adı biçimi: "$100 → $1M · Ep. 7"). Yedek eşleşme: kanal **Hundo to Million** + slogan "You don't just watch the story. You control it."

## 5. Niyazi için sonraki adımlar (onaylı, dışarıda)
1. Seçilen adı **önce Instagram'da** (ana kanal), aynı gün TikTok'ta, sonra YouTube'da alın. Alım sırası, kısa sürede başkası kapma riskine göre belirlendi.
2. YouTube: Studio'da ad ve tanıtıcı değişir (API desteklemiyor). Eski @toonomy tanıtıcısı serbest kalır [ÖB, Studio'da teyit]. `kanal-paketi.json` açıklaması, anahtar kelimeleri ve banner'ı yeni formata göre yeniden yazılmalı (ayrı iş).
3. Yayından önce USPTO Trademark Search'te seçilen adla birebir arama yapılmalı. Ticari kullanım (marka, ürün) düşünülüyorsa avukat görüşü alınmalı.
4. Jake Miller ve Mike Carter çok yaygın gerçek adlar. Açıklamalarda "fictional characters" notu önerilir [T].

## Kaynaklar [AÖ]
- HGTV "Flip to a Million": https://www.hgtv.com/shows/flip-to-a-million
- HUNDO (Hundo Exchange): https://trademarks.justia.com/owners/hundo-exchange-inc-4776611 · THE HUNDO: https://markinton.com/trademark/the-hundo-98460871
- Million Dollar Flips (terk edilmiş başvuru): https://trademark.justia.com/875/41/million-dollar-87541923.html
- Flip sosyal alışveriş uygulaması: https://www.builtinla.com/2022/07/20/flip-raises-60m-series-b-hiring
- FLIP USPTO kayıtları (örnek): https://trademarks.justia.com/982/28/flip-98228214.html
