# Kadro ve skill denetimi — 2026-10-26 (ik-direktoru)

**Ana hedef:** kanalın para kazanması (YouTube Partner Programı'na kabul + sürdürülebilir gelir).
**Kapsam:** 17 ajan, 6 komut, kalite kapıları, skill referansları, dosya yolu referansları.
**Yöntem:** `python3 tools/kadro-kontrol.py` + ek referans betiği (ajan/komut/doküman içindeki her `eklenti:skill` adını kurulu eklenti skill'leri ve oturum skill listesiyle, her `docs/ tools/ assets/ video/ .claude/` yolunu diskle karşılaştırır; betik `tools/` dışında tutuldu, `tools/kadro-kontrol.py`'ye eklenmesi uretim-muhendisi'ne talep edildi).

## 1. Bulgular ve düzeltmeler

| Ajan / dosya | Sorun | Düzeltme |
|---|---|---|
| Tüm ekip | **YouTube para kazanma politikalarının sahibi yok** (inauthentic/mass-produced, reused, AI personası, sentetik içerik beyanı, reklam dostu yönergeler, Content ID). AI ses + AI görsel + otomatik hat → en büyük gelir riski sahipsiz. | `monetizasyon-uyum-uzmani` işe alındı (F2 ön tarama, F3 metin, F8 paket, her 5 videoda kanal denetimi, `docs/ypp-hazirlik.md`). |
| bugunun-videosu.md ↔ ortak-dersler.md | `durum.sentetik_medya` kararı iki farklı sahipte yazılıydı (youtube-paketleyici / "hakem/finans-dogrulayici"). | Tek sahip: monetizasyon-uyum-uzmani karar verir, youtube-paketleyici pakete yazar, hakem kontrol eder. İki dosya da güncellendi. |
| 8 ajan (trend-avcisi, kanal-analisti, senaryo-yazari, viralite-analisti, kurgu-editoru, thumbnail-tasarimcisi, youtube-paketleyici, + yeni ajan) | `marketing-skills:youtube-full` "YouTube SEO, hook, retention, CTR kalıpları" diye bağlanmıştı. Skill aslında **veri aracı** (yt-dlp, youtube-transcript-api, RSS: arama, transkript, kanal listesi); SEO/retention kuralı vermez. Yanlış beklenti = yanlış karar. | Her ajanda açıklama gerçek işlevine göre düzeltildi (rakip transkripti, RSS listesi). Ders ortak-dersler'e yazıldı. |
| Tüm skill referansları | Var olmayan skill adı | **0 hata.** 40+ benzersiz skill adı ve `remotion-best-practices` alt dalları (captions, create, multimedia, maps, render, studio, upgrade, markup) doğrulandı. |
| showrunner | `tools` içinde `Agent`: alt ajanlar alt ajan çağıramaz; akış "alt ajanları yalnız koordinatör çağırır" diyor. | `Agent` çıkarıldı; "kuralları ana oturumdaki koordinatör uygular" notu eklendi. Para kazanma hedefi ve F12 geri besleme görevi eklendi. |
| trend-avcisi | Çıktı yolu `uretim/<klasör>/konu-havuzu.md` + "≥20 konu"; akış `01-arastirma/` + "≥15". Edit aracı yok (hafıza dersini güvenli eklemek için gerekli). | Yol ve sayı akışla hizalandı (≥15, hedef 20); Edit eklendi; "hassas olay" işareti (reklam uygunluğu) ve yayın sonrası dersleri okuma eklendi. |
| finans-dogrulayici | Edit yok; çıktı `dogrulama.md` (F2 dosyası belirsiz); "YouTube finans politikası" sınırı yeni ajanla çakışırdı. | Edit eklendi; F2 `02-senaryo/on-dogrulama.md`, F3 `03-metin/dogrulama.md`; sınır netleştirildi (iddia doğruluğu / tavsiye / karalama / yasal not burada; para kazanma politikası yeni ajanda). |
| viralite-analisti | Çıktı `viralite-puanlari.md`; akış `02-senaryo/viralite.md`. | Hizalandı; kalibrasyon girdisi `yayin-sonrasi/` raporlarına bağlandı. |
| ses-yonetmeni, ses-muhendisi | Çıktılar `ses/…`, `ses/rapor.md`; akış `04-ses/…`, `04-ses/ses-rapor.md`. | Hizalandı. |
| gorsel-varlik-sanatcisi | `2d-duzenleme-promptlari.md` yolsuz; `assets/karakter/parcalar/` yok; rapor yolu `gorsel/`. | Tam yol yazıldı; `parcalar/` "ilk rig işinde oluşturulur, mevcut paket `paket-v1/`" notu; `05-gorsel/rapor.md`; sahne yeniden kullanımı kaydı (özgünlük) eklendi. |
| muzik-ses-tasarimcisi | Lisans kaydı `muzik/lisanslar.md`; akış `06-muzik/lisans-kaydi.md`. CC0 parçaların üçüncü kişilerce Content ID'ye kaydedilme riski yazılı değildi. | Hizalandı; Content ID itiraz kanıtı kuralı eklendi. |
| animasyon-yonetmeni | Rapor yolu `test/`; akış `07-animasyon/`. | Hizalandı. |
| kurgu-editoru | Çıktı `final/`, Shorts "2–3"; akış `08-kurgu/`, 2 Shorts. Retention kuralı ölçülebilir değildi. | Hizalandı; ilk görsel değişim ≤3 sn, intro yok, retention haritasına bağlı vurgu; Shorts → uzun video köprüsü; dış görüntü yasağı (reused). |
| senaryo-yazari | Retention genel ifadeydi; özgünlük ve AI personası kuralı yoktu; çıktı yolları yok. | "İlk 30 sn planı" + "retention haritası" zorunlu; ilk 60 sn abone çağrısı yok; özgünlük ve maskot kuralı; `02-senaryo/`, `03-metin/` yolları. |
| kanal-analisti | Yayın sonrası analiz tek cümleydi; CTR/AVD verisinin mevcut API ile alınamadığı yazılı değildi. | 48 sa / 7 g / 28 g rapor şablonu, "sonraki video için 3 ders", YPP ilerlemesi; veri erişimi notu (Data API yalnız herkese açık sayılar; CTR/AVD/tutma = YouTube Analytics API `yt-analytics.readonly`, şimdilik Studio dışa aktarımı). |
| thumbnail-tasarimcisi | Rakip thumbnail karşılaştırması isteniyor ama WebFetch yok; kanal görselleri sahipsiz. | WebSearch/WebFetch eklendi (i.ytimg.com 2026-10-26'da erişilebilir); banner/profil/filigran ölçüleri (YouTube resmi sayfası) ve içerikle tutarlılık kuralı. |
| youtube-paketleyici | Kanal sayfası (paralel oturumda `tools/yayin/kanal.py` ve `uretim/kanal-kimligi/` oluştu; ajan ona bağlandı), `docs/kanal-kimligi.md`, topluluk, Shorts → uzun bağlantısı sahipsiz; test kapısında `--dry-run` yoktu. | Kapsam genişletildi; `--dry-run` test kapısına eklendi; yorum yanıtları yalnız Niyazi onayıyla. |
| hakem | YPP politika ve retention kapıları yoktu. | Son kontrole iki kapı eklendi; senaryo kararında politika ön taraması (KIRMIZI elenir). |
| uretim-muhendisi | "`tools/README` yerine" ifadesi var olmayan dosya gibi okunuyordu. | Yeniden yazıldı; bekleyen araç talepleri eklendi (Analytics API kapsamı, sahne benzerlik ölçümü, kadro-kontrol'e skill/yol doğrulaması). |
| showrunner, kalite-kapilari | `docs/kanal-kimligi.md` referansı var, dosya yok ve sahibi yoktu. | Sahibi youtube-paketleyici; `/kanal-acilisi` komutu oluşturur. |
| komutlar | `video-uret`, `yeni-video`, `senaryo-onayla` yeni ajan ve F12'yi bilmiyordu; kanal açılışı akışı yoktu. | Güncellendi; yeni `/kanal-acilisi` komutu. |
| ajan-karnesi | Kural tetikleyen ajan var mı? | Yok (puanlar 8 ve 9; diğerleri puansız). İşten çıkarma/uyarı yok. |
| hafıza dosyaları | 17/17 vardı, biçim doğru. | Yeni ajanın hafızası kaynaklı politika gerçekleriyle tohumlandı (18/18). |

**Bilinçli olarak kalan "yok" yollar** (planlanmış çıktılar, sahibi ve oluşturma adımı yazılı): `docs/monetizasyon.md` (paralel araştırma ajanı yazıyor), `docs/ypp-hazirlik.md` (monetizasyon-uyum-uzmani, `/kanal-acilisi`), `docs/kanal-kimligi.md` (youtube-paketleyici, `/kanal-acilisi`), `assets/karakter/parcalar/` (gorsel-varlik-sanatcisi, ilk rig), `video/src/ortak/` (uretim-muhendisi, ilk ortak bileşen).

## 2. İşe alım kararları (para kazanma odaklı boşluk analizi)

| Boşluk | Karar | Gerekçe |
|---|---|---|
| YPP uygunluk ve politika uyumu | **AL: `monetizasyon-uyum-uzmani`** | En büyük gelir riski. Kanal düzeyi (şablon tekrarı, YPP hazırlığı) + video düzeyi (3 teslim) iş; finans-dogrulayici'ye eklemek F3'te darboğaz ve uzmanlık karışımı, hakem'e eklemek bağımsızlığı bozar. Dış örnek: VoltAgent `compliance-auditor` (kanıt toplama, kontrol kapsaması, denetim izi) — YouTube'a özgü örnek dış koleksiyonda yok, alan uzmanlığıyla uyarlandı. |
| İzlenme süresi / retention | Mevcut ajana ekle (senaryo-yazari + kurgu-editoru) | Sahipleri zaten onlar; eksik olan ölçülebilir kapıydı → "Retention (metin)" ve "Retention (kurgu)" kapıları. |
| Yayın sonrası analitik → geri besleme, A/B thumbnail | Mevcut ajana ekle (kanal-analisti + viralite-analisti; F12) | Veri kaynağı ve kalibrasyon zinciri aynı; ayrı ajan çakışırdı. Test & Compare Studio'da elle (API karşılığı doğrulanmadı). |
| Topluluk yönetimi, pinli yorum, Shorts → uzun huni | Mevcut ajana ekle (youtube-paketleyici; Shorts köprüsü kurgu-editoru) | Pinli yorum zaten oradaydı; yorum yanıtı dışarıya mesajdır → yalnız taslak, gönderim Niyazi onaylı. YPP öncesi yorum hacmi küçük. |
| Kanal kimliği / branding | Mevcut ajana ekle (metin: youtube-paketleyici; görsel: thumbnail-tasarimcisi) + `/kanal-acilisi` | Tek seferlik iş + 10 videoda bir gözden geçirme; ayrı ajan boşta kalırdı. |
| Gelir çeşitlendirme (sponsor, affiliate) | **ALMA (şimdi)** | YPP öncesi kitle küçük; finans affiliate'leri tavsiye/çıkar çatışması riski taşır. YPP kabulünden sonra monetizasyon-uyum-uzmani + finans-dogrulayici değerlendirir (ücretli tanıtım beyanı dahil). |

## 3. Kalite kapıları (eklenenler)
Politika ön taraması (F2), Retention (metin), YPP politika (metin, F3), Retention (kurgu), **YPP politika (video, F8)**, Kanal düzeyi özgünlük (her 5 videoda), Yayın sonrası analiz, Kanal sayfası; Thumbnail'e "içerikle tutarlı", Paket'e "Not financial advice + Narration voice is AI-generated + atıflar" eklendi. Teslim paketine `politika-raporu.md` girdi (12 → 13 dosya).

Kaynaklar (erişim 2026-10-26): YPP eşikleri support.google.com/youtube/answer/72851 · para kazanma politikaları (inauthentic, reused, AI personası) answer/1311392 · reklam dostu yönergeler answer/6162278 · kanal görseli ölçüleri answer/10456525.
"Yeniden kullanılan sahne ≤ %20" bir **iç kuraldır**, YouTube'un sayısı değildir.

## 4. Test çıktısı

`python3 tools/kadro-kontrol.py` (düzeltmelerden sonra):
```
OK   (18 ajanın hepsi: frontmatter, protokol satırı, hafıza, skill bölümü, çalışma şekli, Skill aracı)
ajan sayısı: 18 | hafıza dosyası: 18 | sahipsiz hafıza: yok
CLAUDE.md'de geçmeyen ajan: ['monetizasyon-uyum-uzmani']
SONUÇ: KALDI
```
KALDI nedeni yalnız CLAUDE.md: proje talimat dosyasını ik-direktoru değiştirmez (yapılandırma). Koordinatörün uygulaması gereken yama (bölüm 6) uygulanınca GEÇTİ olur.
Referans betiği: skill adı hatası **0**; yol uyarıları yalnız yukarıdaki planlanmış 5 çıktı.

## 5. Kalan riskler
1. **Tam otomatik hat + AI ses + AI görsel** YPP incelemesinde "mass-produced" görünebilir. Politika AI'yi yasaklamıyor; özgün karakter, kaynaklı araştırma, yorum ve video başına farklı anlatı şart. Kanıt dosyası (politika-raporu) bu yüzden zorunlu. Sonuç YouTube'un insan incelemesine bağlıdır; garanti yoktur.
2. **CTR/AVD/tutma verisi otomatik alınamıyor:** YouTube Analytics API kapsamı (`yt-analytics.readonly`) yükleme tokenında yok. Eklenmesi Niyazi'nin bir kez yeniden yetki vermesini ister (uretim-muhendisi talebi). O zamana kadar Studio dışa aktarımı.
3. **Sahne benzerlik ölçüm aracı yok** (algısal hash) → ilk videolarda oran elle sayılır; araç uretim-muhendisi'nde bekliyor.
4. `docs/monetizasyon.md` henüz yok (paralel ajan). Gelince monetizasyon-uyum-uzmani hafızasındaki kaynaklı gerçeklerle karşılaştırılmalı.
5. CC0 müzik bile üçüncü kişi Content ID iddiası alabilir; itiraz kanıtı hazır tutulur ama iddia süresince gelir bekletilebilir.
6. **Kanalda eski konseptten 4 kısa video yayında** (2025-07, `uretim/kanal-kimligi/mevcut-durum.md`; "Shocking Story" tarzı başlıklar). YPP incelemesi kanalı bütün olarak görür; monetizasyon-uyum-uzmani başvurudan önce tut / liste dışı / gizli önerir, karar Niyazi'nin. @tanıtıcı "finansialrise" yazımı kanal adıyla (Financial) uyuşmuyor — marka tutarlılığı için Niyazi'ye not (Studio'da değişir).
7. Yeni ajan bu oturumda alt ajan türü olarak görünmez: koordinatör genel amaçlı ajana `.claude/agents/monetizasyon-uyum-uzmani.md` dosyasını okutarak çalıştırır.

## 6. Koordinatöre: CLAUDE.md yaması (uygulanması önerilir)
- "Ekip (17): …" → "Ekip (18): …, ik-direktoru, monetizasyon-uyum-uzmani."
- Akış madde 3 (F2): "`viralite-analisti` (ilk 3) ‖ `finans-dogrulayici` (risk taraması) ‖ `monetizasyon-uyum-uzmani` (politika ön taraması) → `hakem`".
- Madde 4 (F3): "→ `finans-dogrulayici` ‖ `monetizasyon-uyum-uzmani` → metin kilidi".
- Madde 8 (F8): "… ‖ `viralite-analisti` → `monetizasyon-uyum-uzmani` (`politika-raporu.md`)".
- Madde 11'den sonra: "12. **F12 Yayın sonrası** (48 sa / 7 g / 28 g): `kanal-analisti` performans raporu → `viralite-analisti` kalibrasyon; dersler sonraki videoya."
- Ürün bölümüne: "Ana hedef: para kazanma (YPP kabulü + sürdürülebilir gelir)." Parça komutlara `/kanal-acilisi`.
