# F8 — Politika raporu · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Hazırlayan:** monetizasyon-uyum-uzmani · **Tarih:** 2026-10-27 · **Kapsam:** paket.md + 3 `yayin-paketi*.json`, thumbnail finalistleri A2/B1/D1, `07-animasyon/tam-16x9-onizleme.mp4` (+ tam render 1080p kırpımları), `senkron-rapor.md`, `06-muzik/lisans-kaydi.md` + `cue.json`, 9:16 kareleri.
**SONUÇ (FİNAL, F7 sonrası): YEŞİL — KIRMIZI 0 · SARI 0 · zorunlu düzeltme 0 (Z1 kapandı). ONAY: politika açısından yayına uygun.**
Etiketler: **[Ö]** betik ölçümü · **[G]** göz kontrolü (kare) · **[T]** yargı · **[B-Kn]** `docs/monetizasyon.md` birincil kaynak.

**Kaynaklar (erişim 2026-10-26, `docs/monetizasyon.md` 1 günlük → yenileme gerekmedi; F2/F3'te 2026-10-27 yeniden açıldı, çelişki yok):**
K4 kanal para kazanma politikaları https://support.google.com/youtube/answer/1311392 · K5 değiştirilmiş/sentetik içerik https://support.google.com/youtube/answer/14328491 · K6 reklam dostu yönergeler https://support.google.com/youtube/answer/6162278 · YPP https://support.google.com/youtube/answer/72851.

---

## 1. Test kapısı (zorunlu satırlar)

| Kontrol | Durum | Kanıt |
|---|---|---|
| Inauthentic / mass-produced değil | ✓ | Anlatı yayı 8 bölüm (oyun → 3 kapı → dip → kilit → 2026 ters köşesi → tez); 10 veri grafiği kodla, kaynak etiketli; 11 senaryodan hakem seçimi. K4: *"using AI to visualize a unique character"* izinli; *"templated storylines … minimal or no narrative"* yok |
| Reused yok | ✓ | Dış klip 0 [Ö6]; önceki renderlarla kare eşleşmesi %0,0 [Ö5]; kaynak metin 8-gram en yüksek %0,06 (F3) |
| AI personası yok (maskot, tavsiye yok) | ✓ | Meta veri tavsiye/hüküm deseni 0 (11 alan) [Ö1]; Shorts okuma metinleri 0 [Ö3]; açıklamada "Leo, our cartoon host" + "fictional cartoon character, not a financial adviser". K4: *"presents itself as a human expert providing advice"* |
| AI beyanı kararı + açıklama satırı | ✓ | **`sentetik_medya = true` (3 paket, kesin)**; AI satırı 3/3 açıklamada [Ö2]. §4 |
| Reklam dostu öz beyan yanıtları | ✓ | §5 (tümü "None") |
| Lisans kaydı tam + Content ID itiraz kanıtı | ✓ | 38 cue dosyası kayıtlı, NC/ND/SA 0, 23 üçüncü taraf dosyanın 23'ünde kanıt sayfası var, CC BY kullanımı 0 [Ö4]. §6 |
| Başlık/thumbnail içerikle tutarlı | ✓ | 11 vaat ifadesinin 11'i kilitli anlatımda [Ö3] + kare kontrolü [G]. §3 |
| Yeniden kullanılan sahne oranı ölçüldü | ✓ | **%0,0** (632 kare, dHash ≤6/64, iç kural ≤ %20) [Ö5] |

Betik: `09-paket/politika-f8.py` → `politika-f8-cikti.txt` (FİNAL koşu: final-16x9.mp4). **2 koşu sha256 aynı** (`72f887a0…`), exit 0, `SONUC hata=0`. Negatif test: "Why You Should Keep Cash in 2026" → `['keep cash', 'you should']` yakalandı; Shorts 2 başlığı → `[]`.
İlk koşu 2 yanlış alarm verdi (betik hatası, içerik değil): A2 metni anlatımdaki "one **door** is a disaster" cümlesinin kısaltması (eşleme parafraza çevrildi); "lock_01/02/03" grup satırı tek dosya adıyla eşleşmiyordu (kök eşleme eklendi).

## 2. Bulgular

| # | Öğe | Seviye | Bulgu | Kaynak politika | Karar / düzeltme |
|---|---|---|---|---|---|
| P1 | Shorts 2 başlığı "Same Box of Cash, Opposite Result: 1932 vs 2026" | **YEŞİL** | Emir, "you", bugüne dönük hüküm yok; ifadeler okuma metninde birebir (same box / opposite result / 1932 / 2026) ve kapanışta "prices were falling" + "That's arithmetic, not a plan." var. Pencereler farklı uzunlukta (≈3 yıl ↔ 12 ay) ama başlık büyüklük değil yön vaat ediyor; açıklama iki pencereyi açıkça yazıyor. | K4 AI persona (*"financial guidance, investment tips"*); K6 "all portions" | **Katı okuma:** "2026'da nakit kaybeder → nakit tutma" çıkarımı = örtük tavsiye. **Esnek okuma:** fiyat endeksinin yönünü karşılaştıran olgu cümlesi, tavsiye değil. Kaynak desteği: K4 yasak örnekleri "guidance/tips/advice" (eylem önerisi); başlıkta eylem yok → esnek okuma kaynakla destekli. Adaylar: (a) mevcut · (b) "A Box of Cash in 1932 vs 2026: Same Math, Opposite Result" (52 krk, aynı risk, daha uzun) · (c) "Why a Box of Cash Gained Power in 1932" (risk en düşük, 2026 vaadi gider → Shorts'un yarısıyla tutarsız). **(a) kalır.** |
| P2 | Thumbnail A2 "ONE IS A DISASTER" | YEŞİL | Anlatım 0:09 "one door is a disaster" + ekranda "DISASTER?" etiketi; "disaster" mecaz, grafik felaket görüntüsü yok | K6 shocking content | Değişiklik yok |
| P3 | Thumbnail B1 "THE SURPRISE DOOR" + kafa birleştirmesi | YEŞİL | Anlatımda "one is a surprise" + finalde kahve kapıda "SURPRISE" etiketi (10:00) [G]. Kafa değişimi = aynı kurgusal karakterin kendi iki pozu; gerçek kişi yok, gerçek olay değiştirilmiyor → K5 beyan tetiklemez. Kutu cevaba işaret ediyor ama yanıltmıyor | K5; K4 *"deceptive or misleading imagery"* | Değişiklik yok |
| P4 | Thumbnail D1 "EVERY DOOR LOCKED" | YEŞİL | Anlatım 7:33 "every door gets locked" + S17'de üç kapıya zincir/kilit [G, 7:52–7:53 kareleri] + bölüm adı. Gerçek banka adı/logo yok. Not [T]: anlatım aynı bölümde "cash at home is suddenly very useful" diyor — kutu kapısının kilitlenmesi oyun metaforu; metin kilitli ve finans-dogrulayici onaylı, politika riski değil | K4 misleading; K6 | Değişiklik yok |
| P5 | Gerçekçi dönem plakaları | YEŞİL | "Illustration" etiketi 1080p'de okunur (3:20 banka kuyruğu, 8:00 sokak kırpımı) [G]; açıklama "Some scenes are illustrations, not historical footage."; harita "dot positions illustrative", Dow "shape illustrative / anchors only" | K4 *"deceptive or misleading imagery"*; K5 | Değişiklik yok. **F7 kontrolü:** 9:16 S06 kesitindeki bulanık sepya sütun plakasında etiket yok [G, 480p] — plaka bulanık/karartılmış, gerçekçi olay sunmuyor; → **F7 finalde etiket eklendi, doğrulandı (§8)** |
| P6 | Roosevelt | YEŞİL | Yüz yok; radyo ikonu + "NEW PRESIDENT FRANKLIN ROOSEVELT" yazısı [G 7:52]; ağzına söz konmuyor | K5 (gerçek kişi) | Değişiklik yok |
| P7 | "Let's jump to the bottom" (6:06) + düşüş SFX | YEŞİL | 1929 bağlamında "atlayan bankacı" klişesine uzak bir yankı [T]; ama görselde düşen kişi yok, yalnız "THE BOTTOM / JULY 1932" kartı [G]; intihar anılmıyor | K6 controversial issues (*"self-harm, suicide"*) | Değişiklik yok (metin kilitli; kalıp cümle olarak gelecek videolarda kullanılmasın) |
| P8 | Leo'nun görünümü | YEŞİL (izle) | Leo yarı gerçekçi bir erkek çizimi; insan sunucu sanılabilir [T]. Karşı kanıt: her açıklamada "cartoon host / fictional cartoon character", kanal Hakkında'da aynı satır, cel-shading + kalın kontur | K4 AI persona | Değişiklik yok. **Kanal düzeyi öneri (Ö9, koordinatör):** Hakkında metnine "Researched, written and produced by the Toonomy team." satırı (insan editör görünürlüğü); şu an yok |
| Z1 | `yayin-paketi.json` → `dosyalar.thumbnail = ../09-paket/thumbnail-A.png` | **KAPANDI** (F7 sonrası: yol `thumbnail/A2-kapilar.jpg`, dosya var; video/SRT yolları da var) | Dosya yok; finalistler `09-paket/thumbnail/A2-kapilar.jpg`, `B1-kutu.jpg`, `D1-kilitler.jpg`. Ayrıca paket.md §1'deki "başlık–thumbnail okunuşu" eski A/B/C konseptine (elenen "STOCKS −89%") atıf yapıyor | — | youtube-paketleyici: yolu A2'ye çevirip paket-uret + paket-kontrol + dry-run tekrar; §1 notunu A2/B1/D1'e güncelle |

## 3. Vaat ↔ içerik [Ö3 + G]
Başlık T1 (one thousand dollars / 1929 / keep), A2, B1 (+1929 damgası), D1, Shorts 1 başlığı, Shorts 2'nin 4 ifadesi ve niteleyicisi: **11/11 VAR**. Yedek başlıklar ve pinli yorum tavsiye/şok 0. Başlık cevabı vermiyor; thumbnail'lar videoda görünen sahnelerin kendisi.

## 4. AI beyanı kararı (kesin)
- **`durum.sentetik_medya = true`** — uzun + 2 Shorts. Gerekçe: K5 tam animasyonu muaf tutuyor, ama dönem plakaları "resimsi"; video başına "gerçekçi mi?" kararı hata riski taşır, beyanın bedeli sıfır (*"alone won't limit a video's audience or impact its eligibility to earn money"*, K5). Ö9 dürüstlük kanıtı.
- Açıklama satırı (3/3, aynen): "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."
- Elenen: `false` (plakalar K5 "realistic altered event" sınırında; atlanan beyan YPP askısı riski taşır, K5).

## 5. YouTube Studio reklam uygunluğu öz beyanı (önerilen yanıtlar)
Inappropriate language: **None** · Violence: **None** · Adult content: **None** · Shocking content: **None** · Harmful or dangerous acts: **None** · Hateful & derogatory: **None** · Recreational drugs: **None** · Firearms: **None** · Controversial issues: **None** (intihar/öz zarar anılmıyor; P7) · Sensitive events: **None** · Enabling dishonest behavior: **None** · Inappropriate for kids & families: **None** · Incendiary & demeaning: **None** · Tobacco: **None** · Beklenen: tam reklam (yeşil $). Thumbnail/başlık/etiketler aynı yanıtlarla uyumlu (K6 "all portions"). Shorts 1/2 aynı yanıtlar.

## 6. Lisans ve Content ID [Ö4]
- Kurguya giren 38 dosya (10 müzik, 28 SFX): 23 üçüncü taraf CC0 + 15 kendi üretimimiz; CC BY / NC / ND / SA **0** → zorunlu atıf yok; açıklamadaki atıflar gönüllü ve doğru.
- İtiraz kanıtı hazır: her üçüncü taraf dosya için `assets/lisans-kanit/*.html|License.txt` (2026-10-27 kopyası) + CC0 metni + `06-muzik/kaynak/*sha256.txt`. Kendi üretim için `06-muzik/ozgun-uret.py` (tohum 1929) + git geçmişi.
- Risk: "Tension" (Komiku) orta-düşük (sanatçı akış platformlarında; üçüncü kişi kaydı ihtimali). **Yükleme sonrası** Studio → Telif hakkı sekmesi kontrol; iddia gelirse: oga-tension.html + CC0 legalcode ile itiraz (Niyazi onayıyla). CC0, Content ID güvencesi vermez (`docs/monetizasyon.md` §7).

## 7. Özgünlük ve insan katkısı kanıt dosyası (Ö1–Ö12)

| # | Durum | Kanıt |
|---|---|---|
| Ö1 tez | ✓ | "A safe place for money isn't really a place…" 0:41 + 10:08 ekranda "SAFE ISN'T A PLACE." [G] |
| Ö2 kendi grafik | ✓ | 10 grafik kimliği, 7 kaynak etiketli sahne, 4 CSV (`03-metin/veri/`), `video/src/k1929/veri-grafik.ts` |
| Ö3 kaynak listesi | ✓ | Açıklamada 10 tarihli kaynak |
| Ö4 anlatı yayı | ✓ | 8 bölüm, bölüm başlıkları paket.md §4 |
| Ö5 karakter rolü | ✓ | İlk herkese açık video. Leo = sunucu, kaybetmez; klonlar kaybeder/kazanır. 5 video kuralı: sonraki A videosunda "çöküş + klon kaybeder" tekrarlanmasın |
| Ö6 sahne tekrarı | ✓ | %0,0 (önceki renderlar pilot-v1/v2 + test yüklemesi) [Ö5] |
| Ö7 metin tekrarı | ✓ | 6 önceki metne 5-gram %0,0 (F3) |
| Ö8 haber okuma yok | ✓ | 8-gram en yüksek %0,06 (F3) |
| Ö9 insan editör | kısmi | Açıklama + Hakkında AI/maskot satırı var; "insan ekip" satırı Hakkında'da yok (P8 önerisi) |
| Ö10 tavsiye yok | ✓ | Metin (F3) + meta veri (F8) 0 bulgu |
| Ö11 sahte olay yok | ✓ | Illustration etiketi + açıklama notu; Roosevelt yüzsüz |
| Ö12 süreç arşivi | ✓ | `uretim/2026-10-26-1929-1000-dolar/` git'te: konu havuzu (23 konu), 11 senaryo + viralite/doğrulama/politika taraması, hakem kararı (S03 kazanan, S01 yedek, gerekçeli), metin sürümleri + RED-1 düzeltme tablosu, ses/animasyon/müzik betikleri |

**İnsan katkısı / editoryal karar özeti:** özgün karakter Leo (Niyazi'nin karakter sayfası, `assets/karakter/`); özgün "üç kapı" oyun kurgusu; 11 senaryodan eleme (hakem-karar.py, ±0,05 ağırlıkta 30/30 S03); F3'te 2 doğrulama + 1 politika düzeltme turu; görsel üretim payı [Ö elle kare sayımı, 8 sn örnek, 79 kare]: ≈%44 tamamen kodla çizilmiş grafik/harita/kart, kalan kareler Canva plakası + kod rig/kamera/yazı katmanı; dış görüntü 0.

## 8. F7 son fark kontrolü — FİNAL (2026-10-27)
Girdi: `08-kurgu/final-16x9.mp4` (631,63 sn, 1920x1080), `shorts-1.mp4` (49,58 sn), `shorts-2.mp4` (56,04 sn), 1080x1920; `kurgu-rapor.md` (ofset 0,000 sn → bölümler/SRT değişmedi).

| Kontrol | Sonuç |
|---|---|
| `politika-f8.py --video 08-kurgu/final-16x9.mp4` | hata 0, sahne tekrarı **%0,0** (632 kare), dış klip 0; **2 koşu sha256 aynı** (`72f887a0…`, önizleme koşusuyla da aynı) [Ö] |
| Shorts 1 ses (Whisper, `shorts-1-whisper.json`) | onaylı okuma metniyle birebir; kapanış "The brown door won because prices were falling." ✓ [Ö] |
| Shorts 2 ses (`shorts-2-whisper.json`) | onaylı metinle birebir; "…because prices were falling" + "That's arithmetic, not a plan." ✓ [Ö] |
| Shorts 1 niteleyici şerit | "IN A DECADE OF FALLING PRICES" BOX satırıyla 0:39'da ekranda ✓ [G] |
| Shorts 1 S06 "Illustration" | bulanık sepya plakada etiket var (0:09–0:14, 1080p kırpım okunur) ✓ [G] — P5 kapandı |
| Shorts 2 "12 MONTHS TO SEPT 2026 / 2025 → 2026" kartı | "Twelve months later" ile birlikte giriyor (0:21) + "U.S. CPI, not seasonally adjusted" ✓; ekranda "SAME BOX. OPPOSITE RESULT." ve "ARITHMETIC, NOT A PLAN" başlıkları ✓ [G] |
| Köprü kartları | "WHY IT FLIPS TODAY / Full game…" ve "WHO WON 1929? / Full game…" — soru/yönlendirme, tavsiye yok ✓ |
| Paket yolları | 3 JSON'daki video/thumbnail/SRT dosyaları mevcut ✓ |

Bilgi notu (politika değil, finans-dogrulayici alanı): Shorts 2'de 0:39'dan itibaren ana videodaki yan yana grafik (Sept 2022 → Sept 2026, 48 ay, "$1,000 buys like $881") ekranda; anlatım ise 12 aylık %3,7'yi söylüyor. Grafikte pencere etiketi açıkça yazılı, yanıltıcı değil; başlık ("1932 vs 2026") yön karşılaştırması olarak tutarlı.

## 9. Kanal düzeyi notlar (5 videoluk denetime)
- "the same math runs the other way", "Let's play / Thanks for playing", "Let's jump to the bottom" kalıp cümle olmasın.
- Oyun formatı en erken 5 video sonra; "Leo sonuç tipi" tablosu başlatıldı: V1 = sunucu, klon kazanır/kaybeder.
