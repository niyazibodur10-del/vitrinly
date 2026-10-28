# F3 — Metin politika denetimi · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Denetçi:** monetizasyon-uyum-uzmani · **Tarih:** 2026-10-27 · **Denetlenen:** `03-metin/metin.md` v1 (commit 3662eab) · paralel: `finans-dogrulayici` (`dogrulama.md`).
**RED-1 sonrası (v2, commit d874c1b): YEŞİL · KIRMIZI 0 · SARI 0 (§9).** İlk tur: SARI (düşük) → 2 düzeltmeyle YEŞİL. Ana anlatımın sesine dokunan düzeltme yok. Düzeltmeler Shorts 1'in kapanış satırı ve kesitine, bir de GÖRSEL sütunundaki iki etikete dokunuyor. Metni ben değiştirmedim; öneriler `senaryo-yazari`'ye gider.

Etiketler: **[B-Kn]** birincil kaynak (YouTube Yardım Merkezi, **2026-10-27'de WebFetch ile yeniden açıldı**, aşağıda alıntılı) · **[Ö]** ölçüm (betik) · **[T]** yargı/tahmin.

## 0. Kaynaklar (erişim 2026-10-27)
| Kod | Sayfa | Bu denetimde kullanılan cümle (birebir) |
|---|---|---|
| K4 | Channel monetization policies — https://support.google.com/youtube/answer/1311392 | "This includes any content that presents itself as a human expert providing advice to viewers" · "AI-generated podcast hosts offering financial guidance, investment tips, or wealth management advice" · "Videos where characters are put in the same situation over and over again with the same outcome" · "Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value" · Reused: "without adding significant original commentary, substantive modifications, or educational or entertainment value." |
| K5 | Disclosing altered or synthetic content — https://support.google.com/youtube/answer/14328491 | Beyan gerekir: "Alters footage of a real event or place." · "Generates a realistic scene that didn't actually occur." · Gerekmez: "Using an AI-generated or altered animation of a missile in a fully animated video" |
| K6 | Advertiser-friendly content guidelines — https://support.google.com/youtube/answer/6162278 | "Our policies apply to all portions of your content (video, Short, or live stream, thumbnail, title, description, and tags)." · "Content that may upset, disgust, or shock viewers may not be suitable for advertising." · Sensitive events: "civil emergencies, natural disasters, public health emergencies," · Controversial issues: "…self-harm, suicide" |

`docs/monetizasyon.md` (2026-10-26) bugünkü sayfalarla karşılaştırıldı ve çelişki bulunmadı. Dosya 30 günden yeni, güncelleme gerekmiyor.

## 1. Test (betik, iki koşu aynı)
```
$ cd 03-metin && python3 -I politika-denetim.py metin.md --kaynak <FRH×3 + FDIC×2 metni> \
    --onceki ses-testi/{okuma-metni.md,duzeltme-metni.md,tts/anlatici-v1-metin.txt,pilot/pilot-v1.en.srt,pilot/pilot-v2.en.srt} kanal-kimligi/kanal-metinleri.md
iki koşu: diff → fark yok · sha256 37ce6184c2484a8f… (ikisi aynı)
Sahne: 24 · anlatım kelime: 1731 (tireler ayrı) · ekran yazısı: 53 · Shorts: 2
[1] Tavsiye/uzman dili: 2 eşleşme, ikisi de "arithmetic, not a plan" (anlatım S21 + ekran) · persona-dışı beyan: "I'm a cartoon", "your host"
[2] Küfür: tüm 0 · ilk 30 sn 0 | şok/hassas: tüm 3 ("disaster" ×2 [hook + ekran], "panic" ×1 [S18]) · ilk 30 sn 1 ("disaster")
[3] Gerçek kişi/kurum: Roosevelt 1 · Bank of United States 2 · FDIC 4 · Federal Reserve 5 · Dow 6
[4] Illustration: gerçekçi-aday 6 sahne → VAR: S01, S05, S09, S18 · YOK: S07 (banka içi, mermer), S12 (vitrin)
[5] Ö2: grafik kimliği 10 (G0, G1, G1a, G1b, G2, G3, G3b, G4, G5, G5a) · "Source:" taşıyan grafik sahnesi 7 · CSV 4
[6] Ö7 5-gram: 6 önceki metnin hepsine %0.0 (0/1745) · metin içi 6-gram ≥3 tekrar: "the same math runs the other way" ×3
[7] Ö8 8-gram (kaynak metinler): FDIC-BH3 %0.00 · FDIC-DI %0.00 · FRH-29 %0.00 · FRH-BP %0.06 (1/1715: "the fourth largest bank in new york city") · FRH-GD %0.00
[8] Shorts 1: 140 kelime ≈59 sn · tavsiye 0 · "o on yıl / fiyatlar düşüyordu" niteleyicisi (hook dışı): YOK
    Shorts 2: 139 kelime ≈58 sn · tavsiye yalnız "not a plan" · niteleyici: "prices were falling" VAR
```
Betik: `03-metin/politika-denetim.py`. Kaynak metinler (FRH ×3 HTML, FDIC PDF + sayfa) bugün `curl` ile indirildi ve `pdftotext`/HTML ayıklamasıyla metne çevrildi. Repoya girmedi, çünkü telifli metin; yeniden üretim komutu betiğin başında yazılı. Betik yalnız sözcük desenlerine bakıyor. Bu yüzden bütün sahneleri (anlatım + GÖRSEL + Shorts) ayrıca elle okudum. Aşağıdaki B1 bulgusu ve S20–S22 okuması bu elle geçişten çıktı (hafıza dersi).

## 2. Bulgular
| # | Bulgu | Renk | Kaynak politika | Düzeltme önerisi |
|---|---|---|---|---|
| B1 | **Shorts 1 bağlamından kopuk okunuyor.** Kesit S16'daki skor tablosunda "…twelve hundred seventy" ile bitiyor. Hemen ardından gelen "Every result on this board belongs to that decade. A decade when prices were falling." cümlesi dışarıda kalıyor. Tek başına izlenen Short'ta AI maskot şunu söylemiş oluyor: borsa 108 $, banka "?", ayakkabı kutusu kazandı. Kapanış "why it flips today" bunu ima ediyor ama sebebi (fiyatların düştüğü on yıl) hiç söylenmiyor. Short ayrı bir içerik olarak değerlendirilir, ana videonun bağlamı ona taşınmaz. | **SARI (düşük)** | K6 "all portions … Short" · K4 "AI-generated … hosts offering financial guidance" (katı okuma: "nakdi kutuda tut" yönlendirmesi izlenimi) | **Önerilen: Seçenek B** (§3.1). Kapanış satırı + S10 kesitinin son cümlesi |
| B2 | **"Illustration" etiketi iki sahnede eksik.** S07 banka içi (mermer zemin, dev kasa) ve S12 dükkân vitrini, Canva ile gerçekçi/resimsi üretilebilir (stil kararı 2026-10-26). Etiket yalnız S01, S05, S09 ve S18'de var. | **SARI (düşük)** | K5 "Generates a realistic scene that didn't actually occur." · Ö11 (`docs/monetizasyon.md` §3) | **Önerilen: Seçenek A** (§3.2). İki GÖRSEL hücresine etiket satırı. Ses etkisi yok |
| G1 | Hook'ta "one door is a **disaster**" (ilk 30 sn) | YEŞİL | K6 shocking: "may upset, disgust, or shock". Burada yatırım sonucu için mecaz, görsel şok öğesi yok (ekranda yalnız "DISASTER?" etiketi) | Yok. F8: thumbnail'da kan, ceset, çöküş felaketi görseli olmayacak (soyut kapı/grafik) |
| G2 | Hassas olay / tartışmalı konu: Büyük Buhran. Metinde yoksulluk sahnesi, ekmek kuyruğu, intihar ve "pencereden atlayan bankacı" miti yok (betik: suicid/jump/window/leap/starv/breadline = 0). "Panic jumps from state to state" (S18) tarihî betimleme, grafik değil. S14'teki "JOB LOSS" kartı soyut (uçan banknotlar). | YEŞİL | K6 sensitive events listesi (sivil acil durum, doğal afet, salgın, terör) 1929–33 ekonomik krizini kapsamıyor; controversial issues "self-harm, suicide" → 0 eşleşme | Yok. Görsel kola not: S09 kuyruğunda ve S18'de çaresizlik/ağlayan yüz yakın planı kullanılmasın (stilize yüzler zaten yazılı) |
| G3 | AI personası: Leo kendini 0:17'de "I'm a cartoon, so nobody in this studio loses real money" diye tanıtıyor. Rolü sunucu. Uzmanlık iddiası, birinci tekil kural ya da emir yok (should/must/need to/recommend/advisor/expert = 0) | YEŞİL | K4 "presents itself as a human expert providing advice": iki koşul da yok (insan uzman değil, tavsiye yok) | Yok |
| G4 | **S20–S22 örtük çıkarım** (elle okuma): S20 kutu 2026'da alım gücü kaybediyor → S22 "deposits are insured to at least $250,000". Arka arkaya izlenince "bugün banka kapısı güvenli" çıkarımı yapılabilir. **Katı okuma:** bu bir para saklama yönlendirmesidir. **Esnek okuma:** iki cümle de kaynaklı kamu bilgisi (BLS, FDIC); 2026 için kazanan kapı ilan edilmiyor, borsa kapısı bugüne taşınmıyor, kişiye özel bir şey yok, hemen ardından "That's arithmetic, not a plan." geliyor ve S23 sonucu kurala bağlıyor ("It depends on what prices are doing, and on the rules around each door"). | YEŞİL | K4'ün örnekleri "financial guidance, investment tips, or wealth management advice", yani yönlendiren içerik. Metinde yönlendiren cümle yok. Katı okumayı geçersiz kılan şey bir uyarı etiketi değil, ölçülebilir olgu: emir kipi 0, 2026 için "hangi kapı" hükmü 0 | Metin değişmez. **F8 kırmızı çizgisi:** başlık, thumbnail, açıklama ve Shorts başlıklarında "where to keep your money (today/2026)", "which door wins today", "cash is trash" ya da "banks are safe now" gibi bugüne dönük hüküm **olmayacak** (K6 "all portions") |
| G5 | "That's arithmetic, not a plan." (S21 + ekran) bir uyarı etiketi mi (P4 yasağı)? Değil. Cümle mekanizmanın sonucu olarak geliyor ve F2'de önerilen kalıpla aynı ("…not a recommendation"). Ayrı bir "this isn't advice" cümlesi yok. | YEŞİL | K4 (AI persona bölümünde "uyarıyla izinli" örneği yok, bu yüzden etiket tek başına çözüm sayılmaz). Burada etiket değil, olgu cümlesi | Yok |
| G6 | Gerçek kişi/kurum: Roosevelt yalnız radyo silueti + ekran yazısı (gerçekçi yüz yok). Bank of United States (1930'da kapandı) yalnız ekran yazısı, logo/tabela yok. Söylenmemiş söz yok | YEŞİL | K5 "Makes a real person appear to say or do something they didn't do" → uygulanmıyor | Yok. Karalama/doğruluk: finans-dogrulayici |
| G7 | Abone çağrısı "subscribing helps Leo build the next one" (5:16). Ödül vaadi ya da yanıltıcı teşvik yok | YEŞİL | K6 / spam (2801973) teşvik kalıbı yok | Yok |
| G8 | Çocuksu ton / "made for kids" algısı: oyun formatı, ama anlatım yetişkin (Fed, FDIC, para arzı, temettü nüansı) | YEŞİL | `docs/monetizasyon.md` K10 | F8: kitle ayarı "No, it's not made for kids" (gerekçe: yetişkin finans/tarih eğitimi) |

## 3. Düzeltme seçenekleri ve eleme

### 3.1 B1 — Shorts 1 bağlam niteleyicisi
| Seçenek | Değişiklik | Politika riski | Viralite / süre [T] |
|---|---|---|---|
| A | S16 kesitini "…twelve hundred seventy. Every result on this board belongs to that decade." ile bitir, S10'un son cümlesini çıkar | Düşük | Süre ≈60 sn (sınırda). Kesit sonu düz bir cümle, kapanışın merakı zayıflar |
| **B (öneri)** | Kapanış satırını sebep cümlesine çevir + S10 kesitinin son cümlesini çıkar (metin.md §5'teki yedek kısaltma) | Düşük: sebep ("prices were falling") sesli olarak söyleniyor | Kayıp yok: "why that flips today" merakı kalıyor. 140 → **135 kelime ≈57 sn** |
| C | Yalnız görsel: 9:16 skor kartında "IN A DECADE OF FALLING PRICES" şeridi korunur, metin aynı kalır | Orta: sesli metinde ve otomatik altyazıda sebep yok | Kayıp yok |

**Seçilen: B** (+ C'deki şerit, ek önlem olarak görsel kolda zaten var: G4). A süreyi zorluyor ve kapanışı düzleştiriyor. C tek başına sesli içeriği düzeltmiyor.

**Kesin metin (eski → yeni), `metin.md` §5 Shorts 1:**
- Kapanış satırı: **eski** "Why the brown door won, and why it flips today, is in the full video." → **yeni** "The brown door won because prices were falling. Why that flips today is in the full video."
- Kesit: **eski** "S10 4:26–4:39 ("Now the score for door two… more than one bank in three", 31)" → **yeni** "S10 4:26–4:36 ("Now the score for door two… suspended operations", 24)"
- Kelime/süre satırı: **eski** "hook 11 + kesitler 114 + kapanış 15 = 140 kelime → ≈59 sn" → **yeni** "hook 11 + kesitler 107 + kapanış 17 = 135 kelime → ≈57 sn"
- 9:16 notuna ekle: "Skor kartında 'IN A DECADE OF FALLING PRICES' şeridi korunur (politika B1)."

### 3.2 B2 — "Illustration" etiketi
| Seçenek | Değişiklik | Politika riski | Maliyet |
|---|---|---|---|
| **A (öneri)** | S07 ve S12 GÖRSEL hücrelerine etiket satırı | Düşük | Ses etkisi yok, yalnız görsel kol |
| B | §2 başındaki biçim notuna genel kural: "Canva ile gerçekçi üretilen her 1929–33 mekân karesine 'Illustration'" | Düşük, ama sahne bazında gözden kaçabilir | Yok |
| C | S07 ve S12'yi düz grafik/ikon sahnesine çevir (etiket gerekmez) | En düşük | Görsel zenginlik kaybı. S07 bölünmüş ekranın yarısı |

**Seçilen: A** (+ B, aynı satırda kural olarak). Etiketi kurgu-editoru sahne sahne uyguluyor, bu yüzden sahnede yazılı olmalı. C gereksiz bir kalite kaybı.

**Kesin metin (eski → yeni), `metin.md` §2:**
- S07 GÖRSEL, sonuna: **eski** "…Müzik: tek notalık gerilim vuruşu." → **yeni** "…Müzik: tek notalık gerilim vuruşu. **Etiket:** banka içi gerçekçi üretilirse "Illustration" (Ö11)."
- S12 GÖRSEL, sonuna: **eski** "…"$1,000 BUYS LIKE $1,272"." → **yeni** "…"$1,000 BUYS LIKE $1,272". **Etiket:** vitrin gerçekçi üretilirse "Illustration" (Ö11)."
- §2 biçim notunda (satır 28): **eski** "**Etiket** ("Illustration" gerekip gerekmediği)" → **yeni** "**Etiket** ("Illustration" gerekip gerekmediği; kural: Canva ile gerçekçi/resimsi üretilen her 1929–33 mekân karesi etiketlenir, stüdyo ve düz grafik muaf)"

## 4. `sentetik_medya` ön kararı
**Ön karar: `durum.sentetik_medya = true`** (Studio → "AI use" = Yes). Kesin kararı F8'de bitmiş videoya göre veririm.
- **Katı okuma:** S01, S05, S09 ve S18'deki sepya 1929–33 sokak, borsa önü ve banka kuyruğu kareleri Canva ile gerçekçi üretilirse, gerçek bir olayın (Bank of United States'in kapanışı, 1933 banka tatili) "olmamış gerçekçi sahnesi" sayılır. K5: "Generates a realistic scene that didn't actually occur." → beyan gerekir.
- **Esnek okuma:** Stüdyo ve maskot sahneleri "fully animated" sayılır, bu yüzden beyan gerekmez (K5 füze örneği).
- Video karışık olduğu ve stil kararı gerçekçiliğe izin verdiği için katı okuma uygulanır. Bedeli sıfır: K5'e göre beyan tek başına para kazanmayı etkilemez (`docs/monetizasyon.md` §4).
- Açıklama satırı (F8, youtube-paketleyici): *"Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."* Ekranda etiket: §3.2'deki 6 sahne.

## 5. Ö1–Ö12: metin aşamasında ölçülebilenler
| Ö | Kontrol | Durum | Kanıt |
|---|---|---|---|
| Ö1 | Özgün tez başta ve sonda | ✓ | "a safe place for money isn't really a place. It depends on what prices are doing" 0:41 ve 11:19 (metin-kontrol.py). Wikipedia özetinde olmayan iki yorum var: "one shoebox looks safe; a whole country of shoeboxes made the banks weaker" (S13) ve 1930'lar ile 2026'nın aynı ölçekli aynası (G5) |
| Ö2 | ≥3 kendi veri grafiği + ekran kaynağı + veri dosyası | ✓ | G0 (BEA), G1 (FRH), G2 (FDIC T5), G3 (FRED), G3b (FRH), G5/G5a (FRED/BLS) → 6 veri grafiği + G4 infografik. 7 grafik sahnesinde "Source:" var. 4 CSV `03-metin/veri/` |
| Ö3 | ≥5 kaynak açıklamada | ✓ (F8'e devir) | metin.md §7: 8 kaynak + HUL |
| Ö4 | Anlatı yayı (liste değil) | ✓ | 8 bölüm: kurulum (oyun) → çatışma (3 kapı) → dönüm (Temmuz 1932 dibi, Mart 1933 kilidi, 2026 ters köşesi) → sonuç (tez). K4 "minimal or no narrative" kalıbı yok |
| Ö5 | Karakter rolü (son 5 video) | ✓ | İlk herkese açık video, karşılaştırılacak önceki video yok. Kayıt: Leo = sunucu (kaybetmez). Kaybeden klonlar Stock Leo (−89 %, yalnız fiyat) ve kısmen Bank Leo; kazanan Box Leo, yalnız o on yıl için. **5 videoluk denetim notu:** sonraki A videosunda "çöküş + klon kaybeder" sonucu tekrarlanmasın, oyun formatı en erken 5 video sonra (P6) |
| Ö6 | Sahne tekrarı ≤ %20 | — | F8'de ölçülür (önceki video yok, %0 beklenir) |
| Ö7 | Önceki metinlerle 5-gram ≤ %10 | ✓ | 6 önceki metnin hepsine %0.0. Metin içi tekrar: "the same math runs the other way" ×3 (S02 vaadi, S21 karşılığı, Shorts 2 hook'u), bilinçli geri çağırma. **Kanal kuralı:** bu cümle ve "Let's play / Thanks for playing" kanalın sabit sloganı yapılmasın. Aynı giriş/çıkış K4'e göre serbest, ama gövdedeki kalıp cümle 5 videoluk denetimde sayılacak |
| Ö8 | Kaynak metni okuma yok (8-gram ≈0) | ✓ | 5 kaynak metinde en yüksek %0.06 (tek tanımlayıcı ifade: "the fourth largest bank in New York City") |
| Ö9 | İnsan editör / maskot / AI ses beyanı | ◐ | Videoda var ("I'm a cartoon"). Açıklama ve Hakkında satırı F8'de kontrol edilecek |
| Ö10 | Tavsiye/uzman dili yok | ✓ | 0 bulgu ("not a plan" mekanizma cümlesi hariç). G3–G5 |
| Ö11 | Gerçekçi sahnede "Illustration" | ◐ → ✓ | B2 düzeltmesiyle 6/6 |
| Ö12 | Süreç arşivi | ✓ | 11 senaryo, eleme, hakem kararı, metin v1, hesap/veri betikleri git'te |

## 6. F2 düzeltmeleri yeniden ölçüm (P1–P6, H2)
| Madde | Ölçüm | Sonuç |
|---|---|---|
| P1 mekanizma cümlesi | S21: "In the early nineteen thirties, cash gained power because prices were falling. In twenty twenty-six, prices are rising, so the same math runs the other way. That's arithmetic, not a plan." 2026 için hüküm/emir yok | ✓ |
| P2 Shorts kancası | Shorts 1 hook birebir ("would have", geçmiş). Shorts 2 mekanizma dili. Kalan risk B1 (kapanış) | ✓ (B1 ile) |
| P3 köprü sorusu | S02 "where was money safe in nineteen twenty-nine?" + "why the same math runs the other way today" | ✓ |
| P4 uyarı etiketi yok | "this isn't advice/disclaimer" kalıbı 0 | ✓ |
| P5 sentetik + Illustration | §4 ön karar true. Etiket 4/6 → B2 ile 6/6 | ◐ → ✓ |
| P6 format tekrarı | Uç ekran köprüsü "a game for another night" yeni bir *oyun* videosu sözü vermiyor (yanıltıcı uç ekran yok) | ✓ (showrunner kuralı) |
| H2 Box Leo 2026 anı | S20: banknotlar grafik yanında küçülüyor, Box Leo merakla bakıyor; aşağılanma/kayıp ifadesi yok. Sunucu hiçbir sahnede kaybetmiyor | ✓ |

**F2 SARI (S03) → F3 durumu:** P1–P3 metinde tuttu. Kalan iki SARI düşük ve düzeltilebilir (B1, B2). İkisi de yedek senaryoya geçiş tetiği değil (`senaryo-karari.md` §5).

## 7. Devirler (benim alanım dışı)
- **finans-dogrulayici:** Shorts 1 hook'undaki "most people would have picked the wrong door" bir genelleme. Kaynağı ve "most people" çerçevesinin savunulabilirliği onun alanında. Yanlışsa önerim "In nineteen twenty-nine, the smartest-looking door was the wrong one." (aynı politika rengi).
- **kurgu-editoru:** Shorts süreleri tireli sayıları ayrı sayınca Shorts 1 ≈60 sn, Shorts 2 ≈63 sn (betik [8]). Politika sorunu değil, iç ≤60 sn kuralı için gerçek TTS süresiyle ölçülmeli.
- **gorsel-varlik-sanatcisi / animasyon-yonetmeni:** 9:16 G4 kartında "IN A DECADE OF FALLING PRICES" şeridi zorunlu (B1). §3.2 etiketleri.
- **youtube-paketleyici / thumbnail-tasarimcisi (F8):** G4 kırmızı çizgisi (bugüne dönük "nereye koy" hükmü yok) · G1 (şok görsel yok) · G8 (made for kids = No) · §4 açıklama satırı.

## 8. Kapı
| Kapı maddesi | Sonuç |
|---|---|
| Her bulgunun politika kaynağı (URL + erişim tarihi) var | ✓ (§0, 2026-10-27) |
| KIRMIZI bulgu yok | ✓ (0) |
| SARI bulgular kesin metin önerisiyle (eski → yeni) | ✓ (B1: 4 satır, B2: 3 satır) |
| Benzerlik betikle ölçüldü (Ö7 ≤ %10) | ✓ (%0.0) |
| **YPP politika (metin) kapısı** | **GEÇTİ (koşullu):** KIRMIZI yok. B1 ve B2 metin kilidinden önce senaryo-yazari tarafından uygulanmalı. Uygulanınca yeniden ölçüm: betik [4] etiketsiz = 0, [8] Shorts 1 niteleyici = VAR |

## 9. RED-1 sonrası yeniden denetim (2026-10-27, metin v2, commit d874c1b)
**Sonuç: YEŞİL · KIRMIZI 0 · SARI 0.** B1 ve B2 birebir uygulanmış. Yeni hook (D-6), D-4 eklemesi ve Shorts 2 kesintisi yeni bir politika riski açmıyor. Metne dokunmadım. Kaynaklar §0'dakilerle aynı (K4, K5, K6; erişim 2026-10-27, bu turda politika metni değişmedi).

### 9.1 Test (betik, 2 koşu)
```
$ python3 -I politika-denetim.py metin.md --kaynak <FRH×3 + FDIC×2> --onceki <§1'deki 6 dosya>
iki koşu: exit 0 / 0 · diff → fark yok · sha256 11508cb9938d0d27…
[1] tavsiye: 2 (ikisi de "arithmetic, not a plan", anlatım + ekran) · persona-dışı beyan 4
[2] küfür 0 (ilk 30 sn 0) · şok/hassas 3 (disaster ×2, panic ×1; v1 ile aynı)
[4] Illustration: S01, S05, S07, S09, S12, S18 → 6/6 VAR · etiketsiz gerçekçi-aday 0
[6] Ö7 5-gram: 6 önceki metne %0.0 (0/1769)
[7] Ö8 8-gram: en yüksek %0.06 (frhbp, 1/1738; v1 ile aynı ifade)
[8b] Shorts 1: 16 cümle · 135 birim ≈56.6 sn · niteleyici "prices were falling" VAR · tavsiye 0
     Shorts 2: 14 cümle · 140 birim ≈58.7 sn · niteleyici VAR · tavsiye 1 ("not a plan", mekanizma cümlesi)
     ana anlatımda olmayan cümle: yalnız hook + kapanış (S1: 3, S2: 2) → kesitlerde gizli yeni metin yok
```
**Betik değişikliği:** kesit ayrıştırıcısı ([8]) v2'deki tek satırlık kesit biçimini okuyamadı. S06/S10 "BULUNAMADI" verdi ve Shorts 1'i 126 kelime gösterdi. Bunun için [8b] eklendi: yetkili metin olarak §5'teki "Okunacak tam metin" (<<…>>, TTS'e giden metin) okunuyor. Cümleler köken kontrolünden geçiyor (ana anlatımda var mı, yoksa yeni kayıt mı), ayrıca süre, niteleyici ve tavsiye ölçülüyor. [8b]'nin sayıları senaryo-yazari'nın `metin-kontrol.py` sonucuyla aynı çıktı (135 / 140 birim). [8] çapraz kontrol olarak duruyor; bu turdaki "BULUNAMADI" biçim kaynaklı, metin hatası değil.

### 9.2 Uygulama kontrolü (eski → yeni, `politika-denetimi.md` §3)
| Madde | Beklenen | v2'de | Sonuç |
|---|---|---|---|
| B1 kapanış | "The brown door won because prices were falling. Why that flips today is in the full video." | §5 Shorts 1, birebir | ✓ |
| B1 S10 kesiti | "…suspended operations" ile biter | birebir. "more than one bank in three" kesitte yok (tam metin) | ✓ |
| B1 9:16 şerit | "IN A DECADE OF FALLING PRICES" skor kartında korunur | §5 9:16 notu birebir. S16 G4'te ana videoda da var | ✓ |
| B1 kelime/süre | ≈57 sn | 135 birim ≈56.6 sn. Yazar, D-4'ün +6 kelimesini S06 kesitinden düşerek dengelemiş | ✓ |
| B2 S07 | "**Etiket:** banka içi gerçekçi üretilirse "Illustration" (Ö11)." | birebir | ✓ |
| B2 S12 | "**Etiket:** vitrin gerçekçi üretilirse "Illustration" (Ö11)." | birebir | ✓ |
| B2 §2 genel kural | "kural: Canva ile gerçekçi/resimsi üretilen her 1929–33 mekân karesi etiketlenir, stüdyo ve düz grafik muaf" | §2 biçim notu birebir · §11 P5 6/6 | ✓ |

### 9.3 Yeni metnin politika okuması
| # | Değişiklik | Katı okuma | Esnek okuma | Karar |
|---|---|---|---|---|
| R1 | **Shorts 1 hook (D-6):** "In nineteen twenty-nine, the smartest-looking door was the worst one." | Short tek başına izlenince AI maskot "borsa en kötü kapı" diyor. Bu bir yatırım genellemesi gibi okunabilir (K4 "investment tips") | Cümle geçmiş zamanda ve bir yılla ("in nineteen twenty-nine") sınırlı; emir yok, bugüne dönük hüküm yok. "Worst" ölçülmüş bir tarih sonucu: 1.000 $ → ≈108 $ (aynı Short'ta S16 skoru). "Smartest-looking" de 1929 algısını betimliyor, izleyiciye bir şey söylemiyor | **YEŞİL.** K4'teki örneklerin hepsi yönlendirme ("guidance, tips, advice"). Katı okumayı geçersiz kılan ölçülebilir olgu: Short'ta emir kipi 0, yıl niteleyicisi 2 (hook + "nineteen thirty"), kapanışta sebep cümlesi ve "flips today" ile tersine dönme vaadi var. v1 hook'u ("most people would have picked") geçmiş kipiyle zaten YEŞİL'di; yeni hook kişiye yönelik "you/most people" çerçevesini de kaldırıyor, yani risk düştü |
| R2 | **D-4, S19:** "So Box Leo wins nineteen twenty-nine: the same gain in buying power, without the gamble." | "Nakit, riski olmadan aynı kazancı verir" diye genellenirse nakit tutma yönlendirmesi olur | Cümle 1929–33 oyununun skorunu veriyor (özne Box Leo, yıl sınırı var). Hemen ardından "Now let's do something unfair. Let's take his winning door and move it to today." geliyor ve S20–S21 sonucu 2026 için ters çeviriyor ("…the same math runs the other way. That's arithmetic, not a plan."). Yani cümle bir hüküm değil, tersine dönüşün kurulumu. Ayrıca bu cümle Shorts'a girmiyor ([8b] köken listesi) | **YEŞİL.** Doğruluk (bankanın hayatta kaldığı senaryoda "same gain" denkliği) finans-dogrulayici'nin alanı ve onun D-4 önerisi. Politika açısından bu cümle Box Leo'nun kazancını ölçülü hale getiriyor ("aynı kazanç, kumarsız" = banka kapısı da kazanabilirdi), yani tek kazanan anlatısını yumuşatıyor |
| R3 | **Shorts 2 kesintisi:** S20'den "Nothing was stolen. The bills are all there." çıkarıldı | Bağlam kaybı nakit hakkında olumsuz bir hükmü sertleştirir mi? | Çıkan cümleler dramatik vurgu, niteleyici değil. Niteleyiciler yerinde: hook (1932 ↔ 2026), "prices were falling", "prices are rising", "not a plan". "They just buy less" "the thousand dollars"a bağlanıyor, mekanizma aynı kalıyor. Tavsiye taraması değişmedi (1 = "not a plan") | **YEŞİL.** Not (politika değil, anlaşılırlık): Short'ta S12'nin 1932 cümlesinden hemen sonra "Twelve months later" geliyor. Bu kesit v1'de de aynıydı. Sesli olarak bir sonraki cümle ("year to September twenty twenty-six") ve G5a kartı ("12 MONTHS TO SEPT 2026") bunu düzeltiyor. **kurgu-editoru:** atlama kesmesinde "2025 → 2026" takvim kartı kesimle aynı karede görünsün. Engel değil |

### 9.4 Kapı (RED-1 sonrası)
| Kapı maddesi | Sonuç |
|---|---|
| B1/B2 birebir uygulandı | ✓ (7/7 satır, §9.2) |
| Betik [4] etiketsiz gerçekçi sahne = 0 · [8] Shorts 1 niteleyici = VAR | ✓ / ✓ |
| Yeni metinde tavsiye/emir dili yok (yeni: 5 cümle) | ✓ (0) |
| Ö7 ≤ %10 · Ö8 ≈0 | ✓ (%0.0 · %0.06) |
| KIRMIZI 0 · SARI 0 | ✓ |
| **YPP politika (metin) kapısı** | **GEÇTİ (koşulsuz).** Metin kilidine politika engeli yok. F8 devirleri §7 ve G4 kırmızı çizgisi geçerli. Ek F8 notu: Shorts 1 başlığı ve açıklaması hook'taki yıl sınırını korusun ("stocks are the worst door" gibi yılsız bir başlık olmasın, K6 "all portions") |
