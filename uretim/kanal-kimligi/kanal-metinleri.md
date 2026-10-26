# Kanal kimliği — metin paketi v1 (youtube-paketleyici, 2026-10-26)

Makine okunur sürüm: `uretim/kanal-kimligi/kanal-paketi.json` (API ile uygulanabilir alanlar). **YouTube'da hiçbir şey değiştirilmedi**; uygulama Niyazi onayıyla.
Etiketler: **[D]** doğrulandı (kaynak, 2026-10-26 erişim) · **[AÖ]** arama özeti · **[ÖB]** ön bilgi, bu oturumda doğrulanmadı · **[T]** tahmin · **[ölçüm]** betikle ölçüldü.

## Test kapısı özeti [ölçüm]
| Kontrol | Sonuç |
|---|---|
| Kanal açıklaması uzunluğu | **950** karakter (yer tutucu 32 karakterlik e-postayla değişince 968) ≤ 1000 |
| İlk 150 karakterde anahtar kelime | 9/11 (animated, finance, financial, money, news, history, crash, scenario, what if) |
| Anahtar kelimeler | **419** karakter / 25 ifade ≤ 500; çok kelimeli ifadeler tırnaklı, tırnaklar çift, tekrar 0 |
| Oynatma listesi başlık/açıklama | başlık 21–41 / 150, açıklama 255–377 / 5000; her açıklamada beyan var |
| Yasaklı/clickbait ifadeler (get rich, millionaire, passive income, financial freedom, rags to riches, secret, shocking, guarantee, make money, unbelievable, change your life …) | **0** (tüm pakette) |
| Beyanlar | "Educational content, not financial advice." ✔ · "Narration voice is AI-generated." ✔ · [iş e-postası] ✔ · yayın ritmi ✔ |
| `<` `>` karakteri (API açıklamada reddeder [ÖB]) | yok |
| JSON geçerli | ✔ |

---

## 1. Kanal açıklaması (kazanan: Aday A)

```text
Animated finance stories: today's money news explained, history's biggest financial crashes, and "what if" scenarios for the future of money.

Financial Rise turns complex money events into animated stories you can follow, told by our cartoon narrator:
• Money News, Explained: interest rates, inflation, bank failures and market moves, broken down while they are still news.
• The Collapse: the 1929 crash, Weimar hyperinflation, tulip mania, Lehman and other moments that reshaped money.
• What If…: plausible scenarios about the dollar, AI, banks and the economy. Scenarios, not predictions.

Every video is researched and fact-checked, with sources in its description.

New long videos every Tuesday, Friday and Sunday, plus Shorts.

Educational content, not financial advice. We never tell you what to buy or sell.
Narration voice is AI-generated. The narrator is a cartoon character, not a financial advisor.

Business inquiries: [iş e-postası]
```

**Neden böyle:** İlk satır arama önizlemesinde görünen kısım; marka adı zaten başlıkta göründüğü için ilk 150 karakter adla değil, aranan kavramlarla (animated finance, money news explained, financial crashes, what if scenarios) doluyor. Üç madde = üç sütun = üç oynatma listesi adı (tutarlı vaat). "We never tell you what to buy or sell" ve "The narrator is a cartoon character, not a financial advisor" satırları, YouTube'un "AI Personas Related to Sensitive Topics" kuralına (kendini insan uzman gibi sunup finans tavsiyesi veren YZ personası) karşı açık bir ayrım koyar (`docs/ogrenme/ortak-dersler.md`, support.google.com/youtube/answer/1311392).

**Ritim satırı uyarısı:** Takvimin geçiş planına göre 1–2. haftada tam tempo yok (`docs/yayin-takvimi.md` §3). Tam tempoya (3 uzun/hafta) gelene kadar şu satır kullanılsın, sonra kazanan satıra geçilsin:
`New animated finance stories every week, plus Shorts.` (Söz verip tutmamak abone güvenini düşürür [T].)

### Elenen adaylar
| Aday | Uzunluk | İlk 150'de anahtar | Neden elendi |
|---|---|---|---|
| B: soru zinciri ("Why do economies collapse? What really happened in 1929? …") | 492 | 4/11 | Merak güçlü ama önizlemede "finance/financial/news/history" yok → arama eşleşmesi zayıf; sütun yapısını anlatmıyor. |
| C: marka-önce ("Financial Rise is an animated channel about money…") | 435 | 6/11 | İlk 20 karakter adı tekrarlıyor (başlıkta zaten var), kuru liste tonu; "cartoon narrator, not an advisor" ayrımı yok. |
| A'nın ilk hâli | 1030 | 9/11 | 1000 sınırını aştı → kısaltıldı (Lehman Brothers → Lehman, tekrarlar atıldı). |

## 2. Kanal anahtar kelimeleri (`brandingSettings.channel.keywords`)

```text
"Financial Rise" "animated finance" "finance explained" "money news explained" "financial news" "financial history" "economic history" "stock market crash" "1929 crash" hyperinflation "Weimar Germany" "financial crisis" "bank collapse" "economic bubbles" "what if scenarios" "future of money" "economy explained" inflation "interest rates" recession "federal reserve" "stock market" crypto "finance animation" economics
```

Format [D]: boşlukla ayrılmış liste; toplam sınır 500 karakter (anahtar kelime başına değil); tırnaksız/kaçışsız tırnaklar kesilmeye yol açabilir ([YouTube Data API — channels](https://developers.google.com/youtube/v3/docs/channels)).
Not [ÖB]: kanal anahtar kelimelerinin sıralamaya etkisi küçüktür; asıl iş video başlığı/açıklaması ve izlenme sinyalleri. Bu alanın işi YouTube'a nişi doğru tanıtmak.

| Aday | Uzunluk | Karar |
|---|---|---|
| A: geniş finans terimleri ("personal finance", investing, "financial education") | 188 | Elendi: "personal finance/investing" bizi bütçe-yatırım tavsiyesi kanallarıyla eşler; içerikle uyuşmaz, tavsiye algısı yaratır. |
| **B: sütun odaklı** (+ "financial news", "stock market", crypto eklendi) | **419** | **Kazanan**: üç sütunun arama ifadeleri + format (animated finance). |
| C: marka/format ("cartoon finance", "finance for beginners") | 145 | Elendi: arama hacmi düşük ifadeler [T]; "for beginners" kitle vaadi içerikle kanıtlanmadı. |

Eski anahtar kelimeler (wealth stories, billionaire mindset, rags to riches, how to get rich, passive income, secret millionaires) **tamamen kaldırılır**: hem yeni konumlandırmaya hem reklam dostu/YMYL güvenli tona aykırı.

## 3. Varsayılan dil ve ülke
- **Varsayılan dil: `en`** (şu an boş). Video ve metin dili İngilizce; kanal başlığı/açıklamasının dili olarak işaretlenir [D: `defaultLanguage` = snippet başlık/açıklama dili].
- **Ülke: `TR` kalsın. Değiştirme önerilmez.** Gerekçe:
  - Ülke alanı kanalın ilişkili olduğu ülkedir [D: API "the country with which the channel is associated"]; YPP/AdSense ödeme hesabı, vergi bilgisi (ABD vergi formu dahil) ve ödeme adresi gerçek ikamet ülkesine göre doldurulur [ÖB]. Niyazi Türkiye'de yaşıyor → TR doğru beyan. Yanlış ülke, AdSense adres/kimlik doğrulamasında (PIN mektubu, kimlik) uyuşmazlık ve hesap askıya alma riski doğurur [ÖB].
  - Kitle erişimi ülke alanına bağlı değil: İngilizce videolar global öneri sistemine girer; reklam geliri izleyicinin coğrafyasına göre oluşur, kanal ülkesine göre değil [ÖB].
  - YPP Türkiye'de kullanılabilir [ÖB]; başvuru öncesi Studio → Para kazanma ekranında teyit edilir.

## 4. Oynatma listesi yapısı (5 liste)
Sıra kanal ana sayfasındaki raf sırasıdır. Başlık sütun adını taşır (videonun başlığıyla aynı kelime ailesi → oturum süresi ve arama).
| # | Liste | İçine giren | Ne zaman açılır |
|---|---|---|---|
| 1 | Money News, Explained | B sütunu (Salı) | İlk B videosuyla |
| 2 | The Collapse: Financial History Explained | A sütunu (Pazar) | İlk A videosuyla |
| 3 | What If…? Future of Money Scenarios | C sütunu (Cuma) | İlk C videosuyla |
| 4 | Money Stories in 60 Seconds \| Shorts | Tüm Shorts | İlk Shorts'la |
| 5 | Start Here: Best of Financial Rise | Her sütunun en iyi videosu (+ fragman) — "abone olmayan" ana sayfa rafı | 3 sütun da yayında olunca (en erken 3. video) |

Kural: **boş liste herkese açık yayınlanmaz** (boş raf kanalı yarım gösterir [T]). JSON'daki listeler ilgili ilk video yüklenince oluşturulur. Bir video yalnız kendi sütun listesine (+ uygun görülürse Start Here'e) girer. Konu kesişen 3+ video birikince (ör. enflasyon/hiperenflasyon) tematik liste eklenir; şimdilik açılmaz.

#### 1. Money News, Explained
```text
This week's biggest money news, explained with animation: interest rate decisions, inflation reports, bank failures, big mergers and market moves. What happened, why it happened and what it could mean for everyday people, in plain English. New episodes every Tuesday.

Educational content, not financial advice. Narration voice is AI-generated.
```

#### 2. The Collapse: Financial History Explained
```text
The biggest financial crashes, bubbles and collapses in history, told as animated stories: the 1929 stock market crash, Weimar hyperinflation, tulip mania, Lehman Brothers, FTX and more. Step inside each crisis, see how it unfolded and what it teaches us about money today. New episodes every Sunday.

Educational content, not financial advice. Narration voice is AI-generated.
```

#### 3. What If…? Future of Money Scenarios
```text
Animated what-if scenarios about the future of money: What if the dollar lost its reserve status? What if AI replaced millions of jobs? What if your bank went digital-only? Each episode explores a plausible scenario step by step. These are scenarios, not predictions. New episodes every Friday.

Educational content, not financial advice. Narration voice is AI-generated.
```

#### 4. Money Stories in 60 Seconds | Shorts
```text
Short animated money stories from Financial Rise: one surprising fact from financial history, the news or a future scenario in under a minute. Each Short links to the full video.

Educational content, not financial advice. Narration voice is AI-generated.
```

#### 5. Start Here: Best of Financial Rise
```text
New to Financial Rise? Start with these animated finance stories: one great financial crash, one money news story explained and one what-if scenario about the future. Updated as new favourites appear.

Educational content, not financial advice. Narration voice is AI-generated.
```

Elenen yapılar: (a) yalnız 3 sütun listesi — Shorts ve yeni ziyaretçi rafı eksik kalıyor; (b) konu bazlı listeler (Inflation, Crypto, Banks) — ilk ayda her listede 1 video olur, boş görünür. Tematik listeler 3+ videoda eklenecek.

## 5. Kanal fragmanı (abone olmayanlar için, ~48 sn)
**Kazanan: Aday A — "kanca önce".** 102 kelime; am_fenrir 0.9 hızında (pilotta ölçülen 143 kelime/dk) + cümle araları + 3 sn giriş/çıkış ≈ **48,6 sn** [ölçüm + T]. Anlatıcı: kanalın kararlaştırılmış YZ sesi (Kokoro `am_fenrir` 0.9).

| Zaman (yaklaşık) | Görüntü | Anlatım (EN) |
|---|---|---|
| 0–6 sn | Pilot v2 sabah odası → birikim destesi erir, fincan gelir | Imagine waking up one morning, and your savings are worth less than a cup of coffee. |
| 6–11 sn | Pilot v2: yüze yakınlaşma → 1923 kartı + "GERMANY" mührü | Sounds impossible? In 1923, in Germany, that's exactly what happened. |
| 11–17 sn | Maskot konuşma planı (rig + dudak senkronu), logo belirir | This is Financial Rise. We turn the biggest money stories into animated stories you'll actually remember. |
| 17–21 sn | İlk A videosunun en güçlü sahnesi (çöküş) | The crashes that wiped out a generation's savings. |
| 21–26 sn | İlk B videosundan haber/grafik sahnesi | The money news everyone is talking about, explained in plain English. |
| 26–31 sn | İlk C videosundan senaryo sahnesi | And bold what-if scenarios. What if the dollar lost its crown? |
| 31–38 sn | Hızlı 3'lü montaj, büyük sayı grafikleri | No jargon. No hype. Just how money really works, and why it matters to you. |
| 38–48 sn | Maskot + "TUE · FRI · SUN" kartı + abone butonu; altta küçük yazı: "Educational content, not financial advice" | New videos every Tuesday, Friday and Sunday. Subscribe, and see your wallet a little differently. |

- **Malzeme:** 0–11 sn hazır (`uretim/ses-testi/pilot/pilot-v2.mp4`, metin `okuma-metni.md` P01–P02; aynı ses/hız). 11–17 sn ve 31–48 sn için `okuma-metni.md` P03–P05'ten uyarlanmış yeni satırlar TTS ile üretilir. 17–31 sn **ilk üç videodan** (her sütundan bir) birer kesit ister → fragman **3 sütun da yayınlandıktan sonra** üretilir. O zamana kadar abone olmayanlar için öne çıkan video = en iyi tutma oranlı ilk video (`fragman_video_id: null`, video yüklenince doldurulur).
- **Kurallar:** ilk 5 saniyede kanca (selamlama yok), kanal vaadi tek cümle, üç sütun adıyla birebir, ritim söylenir, tavsiye/kazanç vaadi yok. Tam tempo yoksa son satır "New animated stories every week." olur. Yüklemede altered/synthetic beyanı video bazında kararlaştırılır (animasyon muaf olabilir; YZ ses beyanı açıklamada).

| Aday | Ölçüm | Karar |
|---|---|---|
| **A: kanca önce + 3 sütun montajı** | 102 kelime ≈ 48,6 sn; 3 sütun ✔, ritim ✔, kanca ilk 6 sn ✔ | **Kazanan** |
| B: maskot kameraya selam ("Hi! I'm your guide to the world of money…") | 26 kelime ≈ 15 sn | Elendi: ilk saniyede kanca yok; karakterin adı yok; maskotu "rehber/uzman" gibi sunması YZ persona kuralına yaklaşır. |
| C: anlatımsız en iyi anlar montajı | — | Elendi: kanalın ne yaptığını ve ritmini söylemiyor; 3+ video gerektiriyor, ses kimliğini göstermiyor. |

## 6. Eski 4 videonun kaderi — öneri: **dördünü de gizliye (private) al; silme.**
Kontrol [D]: açıklamalar API ile okundu (2026-10-26).
| Video | Sorun | Karar |
|---|---|---|
| uAzvo7kCbg4 — "Grace Walker's True Story" | **Yanlış bilgi.** Açıklama: "a quiet third-grade teacher in small-town Iowa … over $9 million". Böyle bir kişiye ait kayıt bulunamadı [AÖ]. Gerçek vaka **Grace Groner**: Illinois, Abbott Laboratories'te 43 yıl sekreter, 1935'te 3 hisse (toplam $180), ~$7 milyonu Lake Forest College'a bıraktı, 2010'da 100 yaşında öldü [AÖ: [Wikipedia](https://en.wikipedia.org/wiki/Grace_Groner), [NBC News](https://www.nbcnews.com/news/amp/wbna35729174), [NBC Chicago](https://nbcchicago.com/news/local/woman-reveals-millionaire-status-after-donating-millions-to-lake-forest-college/1868787)]. Ad, meslek, eyalet ve tutar yanlış, üstelik "True Story" deniyor. Kanalın kendi compound interest videosu "Grace Groner" diyor → iç çelişki. | **Hemen gizli** (en yüksek öncelik) |
| Xc4WFq4HEnY — Ronald Read (1:47) | Olgu büyük ölçüde doğru (Vermont, benzin istasyonu/hademe, ~$8M mülk; [Wikipedia](https://en.wikipedia.org/wiki/Ronald_Read_(philanthropist)), [Today](https://www.today.com/today/amp/tdna1201)) ama "Shocking", "how to get rich", "passive income" etiketleri; eski "gizli milyoner" tonu. | Gizli |
| TKAthZZZ71k — Compound Interest (2:19) | "Builds Millionaires", "retire with millions" vaadi; YMYL/tavsiye tonuna yakın. | Gizli |
| wt7aEJ5YvRE — Chris Gardner (4:02) | Motivasyon/"rags to riches" türü, "It will change your life"; finans sütunlarıyla ilgisiz. | Gizli |

Gerekçe:
- **YPP incelemesi kanala bütün olarak bakar** [D: [YPP yardım sayfası](https://support.google.com/youtube/answer/72851), "review your channel as a whole"]; üçüncü taraf rehberlere göre özellikle ana tema, en çok izlenen ve en yeni videolar, yanıltıcı başlık/thumbnail kontrol edilir [AÖ]. 1:47–4:02 süreli, farklı temalı, clickbait başlıklı 4 video yeni kanalın "ana teması" ile çelişir ve en çok izlenen videolar listesinin başında kalır (yeni videolar onları geçene kadar).
- **Kayıp yok:** YPP izlenme saatine yalnız herkese açık uzun videolar sayılır; gizli/liste dışı/silinmiş videoların saatleri zaten sayılmaz [D: aynı sayfa]. Toplam 48 izlenme ≈ ihmal edilebilir saat [H].
- **Neden silme değil:** Gizli almak geri alınabilir (protokol: geri alınamaz adımdan kaçın); beğeni/yorum kaydı korunur; Grace Walker videosu herkese kapalı olunca yanlış bilgi riski ortadan kalkar. İleride istenirse silinir.
- **Neden "liste dışı" değil:** Liste dışı video bağlantıyla hâlâ izlenebilir; yanlış bilgi videosu için yetersiz.
- **Zamanlama:** Yeni konumlandırmanın ilk videosu yayınlanmadan önce yapılmalı; YPP başvurusu inceleme sürecindeyken kanalda büyük değişiklik yapılmaması önerilir [AÖ].
- **Not:** Eski Grace Walker açıklamasındaki abone bağlantısı da bozuk biçimde (`@UC1XHl…`) yazılmış; gizli alınınca önemi kalmaz.

## 7. @tanıtıcı — öneri: **@TheFinancialRise** (yedek: @FinancialRiseTV)
"@finansialrise" kanal adıyla (Financial Rise) uyuşmuyor; izleyici doğru yazınca kanalı bulamaz.

**Müsaitlik kontrolü [ölçüm, API `channels?forHandle=`, 2026-10-26]** — kanal bulunmayanlar "boş":
| Tanıtıcı | Durum |
|---|---|
| @financialrise | **Alınmış** — başka bir "financialrise" kanalı (2023, 42 video, 39 abone) |
| @financial_rise | **Alınmış** — başka bir "Financial Rise" kanalı (19 video) |
| @financialriseofficial | **Alınmış** — başka bir "Financial Rise" kanalı (0 video) |
| @thefinancialrise | boş → **önerilen** (16 karakter, okunuşu doğal, marka adının tamamı) |
| @financialrisetv | boş → yedek 1 |
| @financialrisehq | boş → yedek 2 |
| @financial-rise | boş ama **elendi**: @financial_rise ile karışır |
| @financialriseexplained | boş ama elendi: 22 karakter, yazması/söylemesi uzun |
API'de kanal çıkmaması tanıtıcının kesin alınabilir olduğunu garanti etmez (rezerve tanıtıcılar olabilir) → son kontrol Studio'daki anlık müsaitlik göstergesi.

**Kurallar [D: [Change, view, or hide your handle](https://support.google.com/youtube/answer/15920820) (arama özeti üzerinden), [Learn about YouTube handles](https://support.google.com/youtube/answer/11585688)]:**
- 14 günlük dönemde **en fazla 2 kez** değiştirilebilir. Eski tanıtıcı **14 gün** sizin için tutulur; bu sürede eski ve yeni URL ikisi de çalışır; sonra başkası alabilir.
- 3–30 karakter; harf/rakam, alt çizgi, tire, nokta (başta/sonda olamaz); büyük-küçük harf duyarsız; URL veya telefon numarasına benzeyemez. YouTube tanıtıcıyı geri alma/değiştirme hakkını saklı tutar.
- Uygulama: Studio → Özelleştirme → Profil → Tanıtıcı → Yayınla (Niyazi yapar; API ile değiştirilemez).
- Eski @finansialrise'a bağlantı veren önemli bir yer yok (2 abone; tek kullanım eski video açıklamaları, onlar da gizlenecek) → 14 gün sonra serbest kalması sorun değil.

**Koordinatöre ek risk (marka, benim alanım dışı):** YouTube'da en az 3 başka "Financial Rise" adlı kanal var (yukarıda). Adla aramada karışma riski [T]. Ad Niyazi kararı; bilgi olarak iletildi — logo/banner ve tanıtıcıda ayırt edicilik önemli.

## Riskler
- Ritim satırı tam tempoya gelmeden yayınlanırsa söz tutulmaz → geçiş satırı kullanılmalı.
- Oynatma listesi başlık/açıklama sınırları (150/5000) API belgesindeki bilinen değerlerdir [ÖB]; kanal açıklaması 1000 karakter sınırı üçüncü taraf kaynaklı [AÖ: [Influencer Marketing Hub](https://influencermarketinghub.com/youtube-character-limits/)].
- YPP eşikleri ve inceleme ölçütleri resmi metinden kısmen okunabildi; ayrıntılar `docs/monetizasyon.md` (paralel yazılıyor) ile uyumlandırılmalı.
