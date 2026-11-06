# F2 — Politika ön taraması (monetizasyon-uyum-uzmani) · 2026-10-27

**Girdi:** `02-senaryo/senaryolar.md` (11 senaryo, hepsi sütun A), `01-arastirma/rakip-ozet.md`, `01-arastirma/konu-havuzu.md`, `docs/monetizasyon.md` (2026-10-26, 1 günlük → yenileme gerekmedi; üç ana sayfa bugün yeniden açıldı, çelişki yok).
**Bağlam:** Kanalın muhtemel **ilk herkese açık videosu**. YPP incelemecisi "ana tema, en çok izlenen, en yeni videolar, meta veri ve Hakkında" bölümüne bakar [K4]. Bu video bir süre hem "en yeni" hem "en çok izlenen" olacak, yani kanalın politika kimliğini bu video belirler. Bu yüzden ölçüt katı tutuldu.
**Renk tanımı:** YEŞİL = bilinen politika riski yok, standart kurallarla üretilir. SARI = elenmez, hakeme gerekçeli risk notu + F3'te uygulanacak düzeltme. KIRMIZI = elenir.
**Sınır:** Rakam/olay doğruluğu, karalama ve "not financial advice" metni `finans-dogrulayici`'nin. Burada yalnız platform politikası ve para kazanma uygunluğu var.

## 0. Politika kaynakları

| Kod | Sayfa | URL | Erişim |
|---|---|---|---|
| K4 | Channel monetization policies (inauthentic / reused / AI personas) | https://support.google.com/youtube/answer/1311392 | **2026-10-27** (bugün yeniden açıldı) |
| K5 | Disclosing altered or synthetic content | https://support.google.com/youtube/answer/14328491 | **2026-10-27** (bugün yeniden açıldı) |
| K6 | Advertiser-friendly content guidelines | https://support.google.com/youtube/answer/6162278 | **2026-10-27** (bugün yeniden açıldı) |
| K7 | Spam, deceptive practices & scams (yanıltıcı başlık/thumbnail) | https://support.google.com/youtube/answer/2801973 | 2026-10-26 (`docs/monetizasyon.md` §5) |
| K8 | Misinformation policies (eski/yanlış atfedilmiş görüntü) | https://support.google.com/youtube/answer/10834785 | 2026-10-26 (`docs/monetizasyon.md` §5) |
| M§ | `docs/monetizasyon.md` bölümleri: §3.2 politika cümleleri, §3.4 Ö1–Ö12, §4 sentetik beyan, §5 reklam dostu tablo | repo | 2026-10-26 |

**Bugünkü okumada bu işle ilgili birebir cümleler [K4/K5/K6, 2026-10-27]:**
- K4: *"Videos where characters are put in the same situation over and over again with the same outcome"* (izin yok). *"Content that repeatedly uses disturbing themes (such as violence or loss) without building a cohesive narrative"* (izin yok). Tekrar eden karakterli seri, *"each video has its own storyline, focus, or concept"* ise izinli.
- K4 (AI personası): *"channels that use AI-generated personas to deliver information on sensitive topics"*; örnek *"AI-generated podcast hosts offering financial guidance, investment tips, or wealth management advice"*. Bu bölümde izin verilen örnek yok.
- K4 (unsatisfying): *"realistic visuals tricking viewers into believing a fake celebrity death or natural disaster has occurred"* (izin yok).
- K5: beyan gerekenler arasında *"Generates a realistic scene that didn't actually occur"* ve *"Alters footage of a real event or place"* var. Gerekmeyen örnek: *"Using an AI-generated or altered animation of a missile in a fully animated video"*. Ayrıca *"Disclosing AI content alone won't limit a video's audience or impact its eligibility to earn money."*
- K6: Savaş için *"content that exploits, dismisses, or condones the war is ineligible for monetization"* (Ukrayna notu, 2022-03-23). *"Discussions involving the loss of life or tragedy that are not exploitative or dismissive"* izinli. Kapsam: *"Our policies apply to all portions of your content"*, yani başlık, thumbnail, açıklama ve etiketler dahil.

## 1. Sonuç tablosu

| ID | Konu | Renk | Ana risk (tek satır) | Kaynak | F3'e önerilen düzeltme |
|---|---|---|---|---|---|
| S01 | 1929 marjin borcu | **YEŞİL** | Tarihî sahnelerin "arşiv fotoğrafı" gibi görünmesi (Ö11) | K5, K8, M§4 | Gerçekçi sahnede "Illustration" etiketi; intihar miti yok (zaten yok) |
| S02 | 1929 → 1933 bankalar | **YEŞİL** | Bugünkü bankalar için korku dili ("is your bank safe?") | K6, K7, M§5 | 2023 bölümü mekanizma dilinde; belirli bir bankanın bugün batacağı ima edilmez |
| S03 | 1929'da 1.000 $, üç kapı | **SARI (düşük)** | "Paranı nerede tut" çerçevesi + 2026 ters köşesi → AI maskotun kişisel finans yönlendirmesi izlenimi; format seri yapılırsa "aynı durum, aynı sonuç" | K4 (AI personası; generic/repetitive), M§3.4 Ö5/Ö10 | Seçenek B (aşağıda) |
| S04 | Weimar 1923 | **SARI (düşük)** | "Who got rich" başlığı + Weimar bağlamı → tarihî nefret söylemi kalıbına (suçlu bir grup arama) açık; Nazi/Hitler yakınlığı | K6 (hateful & derogatory; sensitive), K7, M§5 | Seçenek A (aşağıda) |
| S05 | 1973 petrol + 2026 | **SARI** | Süren 2026 İran savaşı bağlamı (hassas olay + tartışmalı konu) ve "yine olacak" yanıltıcı okuma riski | K6 (sensitive events, war), K7, M§5 | Seçenek A (aşağıda) |
| S06 | Cisco 2000 | **SARI (düşük)** | Leo'nun "now I believe: good company + good price" kuralı = AI personasının yatırım ipucu vermesi; alternatif 2 "Terrible Bet"; güncel şirket (CoreWeave) adı | K4 (AI personası), K7 | Seçenek B (aşağıda) |
| S07 | Black Monday 1987 | **YEŞİL** | Güncel "Black Monday" korkusuna bağlanırken yakın çöküş ima etmek (yanıltıcı) | K7, K4 (shock value) | Bugün bağı "possibility" + devre kesiciler mekanizması |
| S08 | Hunt kardeşler 1980 | **SARI (düşük)** | Gerçek, tanınabilir kişiler "heist" çerçevesinde; başlık/thumbnail "ALL the World's Silver" doğrulanmış paydan büyük vaat | K7 (misleading title/thumbnail), K5 (gerçek kişi), K6 | Seçenek A (aşağıda) |
| S09 | Lehman 2008 "what if" | **SARI** | Karşı-olgusal sahneler gerçekçi çizilirse olmamış olayın gerçekçi gösterimi; spekülasyonun eğitsel dayanağı | K5, K4 (deceptive imagery), K8 | Seçenek A (aşağıda) |
| S10 | Japonya 1989 | **YEŞİL** | Kurgusal "Yuki" gerçek kişi gibi algılanmamalı; kültürel klişe | K5, K4 | "Yuki is a fictional character" ekranda ilk görünüşte |
| S11 | LTCM 1998 | **YEŞİL** | "30:1 — DO NOT TOUCH" notu tavsiye gibi okunabilir (çok düşük) | K4 (AI personası) | Not "30:1 — ONE BAD MONTH" gibi betimleyici olsun |

**Sayım:** YEŞİL 5 (S01, S02, S07, S10, S11) · SARI 6 (S03, S04, S05, S06, S08, S09) · **KIRMIZI 0** → elenen senaryo yok.
**İlk video için politika güvenliği sıralaması (bilgi, karar hakemin):** S07 ≈ S02 > S01 > S10 > S11 > S03 > S04 ≈ S06 ≈ S08 > S09 > S05. Senaryo yazarının 1. adayı S03, Seçenek B ile YEŞİL'e iner. Düzeltme metin aşamasında tek turda yapılabilir.

## 2. SARI bulgular: düzeltme seçenekleri ve öneri

Her bulguda 2–3 seçenek var. Politika riski ve viralite kaybı karşılaştırıldı, biri önerildi. Viralite etkisi [T] (tahmin); puanlamayı `viralite-analisti` yapar.

### S03 — Three Doors (SARI, düşük)
**Bulgu 1: AI personası / kişisel finans yönlendirmesi.** 9:30–11:00'daki ters köşe "bugün ayakkabı kutusu kaybeder" diyor. Shorts kancası "Most people picked wrong" ve 15–30 sn köprüdeki "Where do I keep my money?" sorusuyla birlikte izleyiciye bugün için "doğru kapı" önerisi gibi okunabilir. K4 bu bölümde izinli örnek vermiyor ve *"financial guidance"* örneğini sayıyor.
- **Katı okuma:** Leo, AI sesli ve AI görselli bir persona. Para saklama yeri hakkında bugüne dönük hüküm vermek "financial guidance" sayılır.
- **Esnek okuma:** Leo insan uzman gibi sunulmuyor (*"presents itself as a human expert"* şartı karşılanmıyor). Tarih simülasyonu eğitseldir.
- Katı okuma varsayıldı. Esnek okumayı destekleyen bir izinli örnek kaynakta yok.

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| A: 2026 ters köşesini tamamen çıkar, video 1933'te biter | En düşük | Yüksek: sona kadar açık "twist" döngüsü ölür |
| **B (öneri):** Ters köşe kalır ama **mekanizma cümlesi** olur: "In 1929 prices fell, so cash gained power. In 2026 prices rise, so cash loses power. That's arithmetic, not a recommendation." Shorts kancası "In 1929, most people would have picked the wrong door." olur. Köprüdeki "Where do I keep my money?" yerine "Where was money safe in 1929?" | Düşük | Düşük: twist ve oyun aynen kalır |
| C: Sona "this isn't advice" uyarısı ekle, metin aynı kalsın | Orta: uyarı etiketi personayı uygun hale getirmez (`docs/monetizasyon.md` §3.2 [AÖ-A8]) | Yok |

**Bulgu 2: seri şablon riski.** Senaryo, "aynı oyun 1923 / 1973 / 2008'e uyarlanabilir" diyor. K4: *"characters are put in the same situation over and over again with the same outcome"*. Bu ilk video için sorun değil, kanal kuralı olarak not edildi: oyun formatı tekrar edilirse Leo'nun rolü, kapı sayısı ve sonuç her seferinde farklı olur, iki kullanım arasında ≥5 video bırakılır (Ö5). Bunu her 5 videoda bir kanal denetiminde ölçerim.

### S04 — One Loaf of Bread (SARI, düşük)
**Bulgu:** Çalışma başlığı "Who Got Rich While Money Died?" Weimar 1923 bağlamında "suçlu kazanan grup" sorusu, tarihte belirli bir topluluğu hedef gösteren propaganda kalıbıyla örtüşür. Yorum alanı da bu yöne kayabilir. Senaryo kazananları kategori olarak (borçlular, sanayi grupları, mal sahipleri) doğru veriyor. Risk metinde değil, **meta veri ile ilk izlenimde**. K6 başlık ve thumbnail'ı da kapsar (*"all portions of your content"*). Nefret söylemi bölümü bir grubu aşağılayan ya da hedef gösteren içeriği reklama uygun saymaz [K6, M§5]. Hitler'e tek cümle ve Nazi görseli yasağı senaryoda zaten var (iyi).

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| **A (öneri):** Başlık alternatif 1 olsun ("One Dollar, One Trillion Marks: Germany in 1923") ya da "Who Won When Germany's Money Died?" yerine mekanizma başlığı seçilsin. Metinde kazananlar ilk anıldıkları yerde **ekonomik rol** olarak tanımlansın ("people who owed money", "big exporters"). Etnik veya dinî grup hiçbir yerde anılmasın. Yorumlar ilk 48 saat elle denetlensin | Düşük | Orta-düşük: "who got rich" merak kancası thumbnail'a değil hook'a taşınır |
| B: Başlık aynı kalsın, yalnız metinde kategori dili kullanılsın | Orta: risk meta veride kalır | Yok |
| C: "Kazananlar" bölümü çıkarılsın | En düşük | Yüksek: senaryonun özgün tezi (Ö1) gider |

Ö7 notu: Pilot okuma metni de Weimar ("loaf of bread", "wheelbarrows") kullanıyor. Hook ile pilot arasında 5-gram örtüşmesi %0 (aşağıdaki test). Pilot hiç herkese açık olmadı (`uretim/ses-testi/yayin-sonucu.txt`: 2026-10-26 private test yüklemesi, aynı gün silindi). Eski 4 video gizli (`uretim/kanal-kimligi/mevcut-durum.md`). Bu yüzden kanal düzeyinde tekrar riski yok.

### S05 — Two Price Tags (SARI)
**Bulgu 1: hassas olay / savaş.** 2026-02-28'den beri süren İran savaşı (`01-arastirma/konu-havuzu.md` A2) ve 1973'ün kendisi de bir savaşa bağlı. K6: savaşı *"exploits, dismisses, or condones"* içerik para kazanamaz. Saygılı ve sömürmeyen tartışma izinli. Senaryo savaşı hook, başlık ve thumbnail'dan çıkarmış (iyi). Ama süren bir çatışmaya atıfla yayınlanan video, otomatik reklam uygunluk sınıflandırmasında sınırlı reklam alma ihtimali taşır [T]. Ayrıca Orta Doğu siyaseti tartışmalı konu alanına girer [K6, M§5].
**Bulgu 2: yanıltıcı okuma.** "What 1973 Tells Us About Now" + 2026 karşılaştırması "yine olacak" diye okunursa yanıltıcı meta veri olur [K7] ve tahmin dili `finans-dogrulayici`'ye gider.
**Bulgu 3: ilk video kimliği.** İlk herkese açık videonun güncel bir savaşın petrol etkisi etrafında dönmesi kanalı "haber yorumu" gibi konumlar. B sütunu riski (haber okuma, Ö8) ilk izlenime taşınır [K4: incelemeci ana temaya bakar].

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| **A (öneri):** 2026 bölümünde savaş hiç anılmasın, yalnız fiyat ve faiz rakamları kalsın ("oil went above $120 in 2026"). 1973 savaşı tek cümle, görselsiz. Başlık alternatif 1 ("From $2.90 to $11.65: The Oil Shock of 1973"). Thumbnail'da silah, bayrak, harita yok | Düşük | Orta: güncel bağ zayıflar, ama talep zaten güncel petrol bağından geliyor (konu havuzu A2) |
| B: Senaryo olduğu gibi kalsın, savaş tek cümle bağlam | Orta | Yok |
| C: Bu konu ilk video yerine B sütununa (güncel) taşınsın | İlk video için en düşük | Konu sütun değiştirir |
İlk video için tercih sırası: S05'i ilk 3'e almamak ya da A ile almak. Seçilirse öz beyan anketinde "sensitive events" sorusu dürüst ve gerekçeli yanıtlanır (F8).

### S06 — Leo's Wrong Belief (SARI, düşük)
**Bulgu 1: AI personasının yatırım ipucu vermesi.** 9:00'da "Here's what I believe now" ve kapanış notu "GOOD COMPANY + GOOD PRICE" (karakter anı) birinci tekil, bugüne dönük bir **yatırım kuralı**. K4'ün örneği tam olarak *"investment tips"*. Katı okuma varsayıldı (S03'teki gerekçeyle).
**Bulgu 2:** Alternatif 2 "Cisco 2000: When a Great Company Was a Terrible Bet" gerçek bir şirket üzerine yatırım hükmü. Betik "terrible bet" kelimesini yakaladı. Elenmesi öneriliyor.
**Bulgu 3:** Bugün bölümünde güncel bir şirket adı (CoreWeave) "balon" bağlamında anılıyor. Karalama ve tahmin `finans-dogrulayici`'nin. Benim açımdan bu, yatırım yönlendirmesi izlenimini artırıyor.

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| A: Leo'nun yanılgı çerçevesi tamamen çıkarılsın, üçüncü tekil anlatım | En düşük | Yüksek: senaryonun özgün açısı (karakter içi gerilim) gider |
| **B (öneri):** Yanılgı kalsın ama **tarih dersi** olarak bitsin: not "GREAT COMPANY ≠ GREAT PRICE (2000)" (betimleyici, emir değil). "Here's what I believe now" yerine "Here's what 2000 actually shows." Güncel şirket adı çıkarılsın, "any boom" sorusu genel kalsın. Alternatif 2 başlık elensin | Düşük | Düşük: karakter anı (notu yırtma) aynen kalır |
| C: Metin aynı kalsın, sona uyarı eklensin | Orta (S03-C gerekçesi) | Yok |

### S08 — The Silver Heist (SARI, düşük)
**Bulgu 1: yanıltıcı başlık/thumbnail.** "The Brothers Who Tried to Buy All the World's Silver" ve thumbnail "ALL THE SILVER". Hook ise "by one count, more than two-thirds" diyor. Kaynaktaki %69'un dünya arzının mı yoksa bir borsa stokunun/sözleşmelerinin mi payı olduğu `finans-dogrulayici` doğrulamasına bağlı. Meta veri doğrulanmış paydan büyük vaat verirse K7 (*"misleading titles, thumbnails"*) riski doğar.
**Bulgu 2: gerçek kişiler + suç çerçevesi.** "Heist" (soygun) gerçek kişilere suç isnadı çağrıştırır. Senaryo "villain" kelimesini zaten yasaklıyor, siluet kullanıyor (iyi). K5: gerçek bir kişinin yapmadığı şeyi yapıyor gibi gerçekçi gösterilmesi beyan gerektirir ve karalama riski taşır.

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| **A (öneri):** Başlık alternatif 1 ya da "How Two Brothers Cornered the Silver Market" (doğrulanmış ifade). Thumbnail metni "6 → 49" ya da "CORNERED". "Heist" yalnız görsel gramer (bölüm kartları) olarak kalsın, başlık, thumbnail ve anlatımda "heist/steal" yok. Kardeşler siluet; mahkeme sonucu yalnız doğrulanmış biçimde | Düşük | Düşük-orta: "ALL" kelimesinin şok etkisi kaybolur |
| B: Başlık aynı, açıklamada "by one count" notu | Orta: başlık tek başına değerlendirilir [K6 kapsam cümlesi] | Yok |

### S09 — Rewind the Weekend (SARI)
**Bulgu 1: olmamış olayın gerçekçi gösterimi.** Üç "take" olmamış sonuçları canlandırıyor. Canva çıktısı "gerçekçi/resimsi" olabildiği için (CLAUDE.md stil kararı) gerçekçi bir "Lehman rescued" manşeti, borsa ekranı ya da kalabalık sahnesi K5'teki *"Generates a realistic scene that didn't actually occur"* koşuluna girer. Kesilmiş Shorts'ta (bağlamsız 55 sn) "Lehman kurtarıldı" görüntüsü K4'ün *"deceptive or misleading imagery or narratives"* maddesine ve K8 (bağlamından koparılmış içerik) riskine dönüşür.
**Bulgu 2: eğitsel dayanak.** Karşı-olgusal kısım spekülatif. K4, anlatının *"well-researched"* olmasını ister. Ekonomist görüşleri kaynaklı değilse bölüm "yorumsuz hayal" gibi okunur. Rakam yükü `finans-dogrulayici`'de.
**Bulgu 3: gerçek kişi ve kurum.** Gerçek yetkililer canlandırılmıyor, logo yok (iyi). "Karton kutulu çalışanlar" sahnesi tanınmaz figürlerle kalmalı.

| Seçenek | Politika riski | Viralite kaybı [T] |
|---|---|---|
| **A (öneri):** Her "take" sahnesi **açıkça stilize** olsun (çizgi film, renk filtresi, ekranda kalıcı "TAKE 2 · HYPOTHETICAL" bandı). Gerçekçi manşet, gazete ya da haber kanalı ekranı üretilmesin. Shorts'ta bant kesilmesin. Her take'te en az 1 kaynaklı ekonomist görüşü ekranda | Düşük | Düşük |
| B: Karşı-olgusal take'ler yalnız grafik/diyagram olsun (sahne yok) | En düşük | Orta: görsel çeşitlilik düşer |
| C: Senaryo olduğu gibi, AI use = Yes beyanıyla | Orta: beyan para kazanmayı etkilemez [K5] ama yanıltıcı görsel riskini kapatmaz [K4] | Yok |
Ayrıca konu doymuş (rakip özeti D2). Bu bir politika riski değil, `viralite-analisti`'nin alanı.

## 3. YEŞİL senaryolarda standart koşullar (F3/F4'te uygulanır)
- **S01:** 1929 Manhattan ve broker sahneleri "resimsi" üretilirse arşiv fotoğrafı sanılmamalı → ekranda "Illustration" etiketi [K8, Ö11]. "Pencereden atlayan bankacı" miti ve intihar yok [K6 controversial issues, M§5]. Bugün bağı (FINRA marjin borcu) "don't use margin" tavsiyesine dönmesin, mekanizma kalsın [K4].
- **S02:** "The bank down the street" ve 2023 banka çöküşleri bölümünde bugünkü belirli bir banka için çöküş imaları yok [K7]. Kuyruk sahnesinde dram var, sarsıcı görsel yok [K6].
- **S07:** Bugün bağı "Ekim 2026 Black Monday korkusu" yakında çöküş beklentisi gibi sunulmasın: "possibility" dili, devre kesici mekanizması [K7]. Fed açıklaması Leo tarafından **belge olarak** okunur. Gerçek yetkili (Greenspan) canlandırılmaz, ağzına söz konmaz [K5].
- **S10:** Yuki ilk göründüğü anda "fictional" diye tanıtılır (hook zaten "would" kipinde) [K5]. Japon kültürü klişe kostümle çizilmez [K6 hateful/derogatory, düşük]. Saray–Kaliforniya iddiası doğrulanmazsa başlık ve thumbnail'a girmez [K7].
- **S11:** Laboratuvar notu "DO NOT TOUCH" emir kipinden betimleyiciye çevrilir [K4]. Nobel ödüllü gerçek kişiler canlandırılmaz.

## 4. Ö1–Ö12 özgün katkı ön değerlendirmesi (`docs/monetizasyon.md` §3.4)

✓ = senaryoda karşılanıyor · ◐ = koşullu (F3/F4'te kanıt gerekir) · — = bu aşamada ölçülemez (F8'de ölçülür)

| Ö | Kontrol | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 | S11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ö1 | Özgün tez | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ö2 | ≥3 kendi veri grafiği, birincil veri | ◐ seri kodları | ◐ seri kodları | ◐ banka oranı | ◐ aylık seri | ◐ FRED | ◐ hisse verisi lisansı | ✓ FRH çapaları | ◐ LBMA/COMEX lisansı | ◐ FRED | ◐ Nikkei verisi lisansı | ✓ FRH |
| Ö3 | ≥5 kaynak | ✓ | ✓ | ✓ | ◐ | ✓ | ◐ [AÖ] ağırlıklı | ✓ | ◐ | ◐ | ◐ [AÖ] ağırlıklı | ✓ |
| Ö4 | Anlatı yayı | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ö5 | Karakter rolü farklı | ✓ borçlu | ✓ dedektif | ✓ sunucu + klonlar | ✓ işçi | ✓ zaman yolcusu | ✓ yanılan | ✓ muhabir | ✓ plan ustası | ✓ yönetmen | ✓ tanık | ✓ deneyci |
| Ö6 | Sahne tekrarı ≤ %20 | — ilk video | — | — | — | — | — | — | — | — | — | — |
| Ö7 | Metin tekrarı ≤ %10 (pilota karşı) | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 | ✓ %0 |
| Ö8 | Haber okuma yok | ✓ | ✓ | ✓ | ✓ | ◐ 2026 bölümü | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ö9 | İnsan editör / maskot / AI ses beyanı | kanal düzeyi (Hakkında + açıklama satırı); senaryodan bağımsız | | | | | | | | | | |
| Ö10 | Tavsiye/uzman dili yok | ✓ | ✓ | ◐ (S03-B) | ✓ | ✓ | ◐ (S06-B) | ✓ | ✓ | ✓ | ✓ | ◐ not dili |
| Ö11 | Gerçekçi sahte olay yok | ◐ Illustration | ◐ Illustration | ✓ stüdyo | ✓ | ✓ | ✓ | ◐ Illustration | ◐ siluet | ◐ (S09-A) | ◐ Yuki fictional | ✓ |
| Ö12 | Süreç arşivi | ✓ git'te (`uretim/2026-10-26-1929-1000-dolar/`) | | | | | | | | | | |

Ö2 notu: FRED'deki bazı seriler üçüncü taraf telifli (ör. Nikkei, hisse fiyatları). Grafiği kendimiz çizsek de veri kullanım koşulu `finans-dogrulayici` + F4'te `gorsel-varlik-sanatcisi` ile kontrol edilmeli. Ekranda kaynak etiketi her durumda olmalı.

## 5. Kanal düzeyi notlar (ilk video olduğu için)
1. **Tema: "kayıp" yoğunluğu.** 11 senaryonun hepsi çöküş. K4: *"repeatedly uses disturbing themes (such as violence or loss) without building a cohesive narrative"*. Senaryolar anlatı yayı taşıdığı için bu video için risk yok. Ama ilk 5 videonun hepsi "çöküş + Leo kaybeder" olursa ana tema "kayıp formülü" gibi görünür. Öneri `showrunner`'a: ilk 5 videoda en az 1 B ve 1 C sütunu. Leo'nun sonucu 5 videoda ≥3 farklı tipte olsun (kaybeden / çözen / tanık / yanılan…). S01 seçilirse Leo "kaybeden" olur. Sonraki A videosunda Leo kaybeden olmamalı.
2. **Sentetik beyan (ön karar, F8'de kesinleşir):** Hepsinde `durum.sentetik_medya = true` ve açıklamada "Narration voice is AI-generated" satırı (M§4 kararı). Gerekçe: Canva'nın resimsi çıktısı tarihî olayları (1929 sokağı, 1987 salonu, 2008 kulesi) gerçekçi gösterebilir. K5 *"realistic scene that didn't actually occur"* ve *"alters footage of a real event"* sınırına video başına karar vermek hata riski taşır. Beyan para kazanmayı etkilemez [K5]. S09 ve S01/S02/S07 için bu karar zorunlu, diğerleri için ihtiyati.
3. **Öz beyan anketi (ön tahmin):** S01, S02, S03, S04, S06, S07, S08, S10, S11 → tüm kategorilerde "None" beklenir. S05 → savaş tek cümle, grafik içerik yok: büyük olasılıkla "None", ama sınırlı reklam ihtimali [T]. S04 → Nazi sembolü yoksa "None". Kesin yanıtlar F8'de bitmiş videoya göre verilir.
4. **Gerçek kişi/kurum:** S06 (Cisco), S08 (Hunt), S09 (Lehman), S11 (LTCM). Logo, gerçekçi yüz ve ağza söz konması yok [K5]. Karalama denetimi `finans-dogrulayici`'nin.

## 6. Test

**Komut:** `python3 uretim/2026-10-26-1929-1000-dolar/02-senaryo/politika-tarama.py uretim/2026-10-26-1929-1000-dolar/02-senaryo/senaryolar.md uretim/ses-testi/okuma-metni.md`
Betik her senaryonun yayınlanacak İngilizce metnini (başlık + 2 alternatif, hook, köprü, tez, Shorts, thumbnail metni) çıkarıyor. Tavsiye/uzman dili, hassas kelime ve gerçek kişi/kurum adlarını sayıyor. Pilot okuma metniyle ve senaryolar arasında 5-gram örtüşmesini ölçüyor. **İki koşu `diff` ile aynı** (çıkış AYNI).

```
| ID | Kelime | Tavsiye/uzman dili | Hassas kelime | Gerçek kişi/kurum | Pilot 5-gram | En yakın senaryo 5-gram |
|---|---|---|---|---|---|---|
| S01 | 149 | — | disaster | — | 0.0 % | 1.4 % (S06) |
| S02 | 156 | — | — | — | 0.0 % | 0.0 % (S11) |
| S03 | 147 | picked wrong | disaster | — | 0.0 % | 0.0 % (S11) |
| S04 | 128 | — | died | — | 0.0 % | 0.0 % (S11) |
| S05 | 128 | — | — | — | 0.0 % | 0.0 % (S11) |
| S06 | 132 | terrible bet | — | cisco | 0.0 % | 1.6 % (S01) |
| S07 | 131 | — | — | — | 0.0 % | 0.0 % (S11) |
| S08 | 145 | — | — | hunt | 0.0 % | 0.0 % (S11) |
| S09 | 128 | — | died | lehman | 0.0 % | 0.0 % (S11) |
| S10 | 124 | — | — | — | 0.0 % | 0.0 % (S11) |
| S11 | 136 | — | — | ltcm, nobel | 0.0 % | 0.0 % (S10) |

Senaryo sayısı: 11 · pilot 5-gram sayısı: 114
En yüksek senaryo çifti örtüşmesi: 1.6 % (S01–S06)
İç kural Ö7: pilot örtüşmesi ≤ 10 %
Ö7 sonucu: GEÇTİ
```

**Betiğin göremediklerini elle kontrol ettim** (yapı satırları Türkçe, betik yalnız İngilizce yayın metnini tarıyor):
- [x] Savaş: S05 yapı 2 ve 6 (2026 İran savaşı bağlamı) → SARI. Başka senaryoda savaş bağlamı yok.
- [x] İntihar/ölüm sahnesi: hiçbirinde yok. S01 ve elenen "Leo 1929'da banker" fikri intihar mitinden bilerek uzak tutulmuş.
- [x] Nefret sembolü: S04 Nazi görseli yasak (senaryoda yazılı). Başlık riski → SARI.
- [x] "died" eşleşmeleri: S04 "Money Died", S09 "Lehman Died" mecaz; insan ölümü değil, sarsıcı içerik sayılmaz [K6]. "disaster" (S01 alternatif başlık, S03 hook) mecaz, gerçek afet görseli yok.
- [x] Tavsiye eşleşmeleri: S03 "picked wrong" ve S06 "terrible bet" → SARI düzeltmeleri. Ek elle bulgu: S06 "Here's what I believe now" + "GOOD COMPANY + GOOD PRICE", S11 "DO NOT TOUCH" (betikte desen var ama not metni tırnak içinde değil).
- [x] Her senaryoda renk + politika kaynağı (URL + erişim tarihi, §0 ve §1 "Kaynak" sütunu): **11/11**. KIRMIZI: 0.

**Kapı:** her senaryoda YEŞİL/SARI/KIRMIZI + politika kaynağı (URL + tarih) → **GEÇTİ**. KIRMIZI = 0, eleme yok. 6 SARI hakeme gerekçeli risk olarak geçiyor. Kazanan SARI ise önerilen seçenek F3'te `senaryo-yazari`'ye düzeltme olarak gider ve F3 politika denetiminde yeniden ölçülür.

**Elenen yaklaşımlar:** (1) "Uyarı cümlesi ekle" tipi düzeltmeler (S03-C, S06-C) önerilmedi: K4'ün AI personası bölümünde izinli örnek yok ve etiket personayı uygun hale getirmiyor (M§3.2 [AÖ-A8]). (2) S05'i KIRMIZI yapmak düşünüldü, yapılmadı: K6 sömürmeyen savaş tartışmasına açıkça izin veriyor (*"not exploitative or dismissive"*), risk "sınırlı reklam" düzeyinde.
