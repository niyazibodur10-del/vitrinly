# F8 politika raporu — S08 "If America Earned $5,400 a Month, Here's Its Budget" · monetizasyon-uyum-uzmani · 2026-11-02

İLERLEME: tamam (F8a tam rapor). F8b = yalnız final dosyalar: `python3 -I 09-paket/politika-f8.py --video 08-kurgu/final-16x9.mp4` (koşturma ve sha256 kontrolü hakemde).
**KARAR: ONAY (YEŞİL). KIRMIZI 0 · SARI 0 · zorunlu düzeltme 0.**
sentetik_medya: true
**Gerekçe:** AI anlatıcı sesi ve AI destekli illüstrasyonlar var. K4 tam animasyonu muaf tutuyor, ama beyanın para kazanmaya ve erişime etkisi yok. Kanal emsali 1929 kararı. Bu karar 3 paket için geçerli (uzun + 2 Shorts).
**Kanıt:** `python3 -I 09-paket/politika-f8.py` 2 koşu → `diff` aynı, `SONUC hata=0`. Girdiler: `tam-16x9.mp4` sha256 `380b3ba073b0` (678,2 sn), paket commit b172cbb, metin `89bebe18d3d4`, thumbnail A1 `f8148925a6df` · B1 `a5fc459fa14a` · C1 `ad63f8d5b1f8`.
**Kapılar:** meta veri dili 0/11 · AI satırı 3/3 · vaat↔anlatım 12/12 VAR · lisans 31/31 kayıtlı, NC/ND/SA 0, kanıt sayfası eksik 0 · yeniden kullanılan sahne oranı üst sınır %2,9 (≤ %20), elle doğrulamada gerçek tekrar 0 · dış klip 0.
**Politika dışı not:** uzun açıklamadaki `{BOLUMLER}` belirteci yükleme aracı tarafından "Chapters:" ile doldurulur. `paket-kontrol.py --final` bunu doğrular (paketleyici/hakem).

## Kaynaklar (son kontrol 2026-11-02; alıntılar F2 raporunda)
[K1] support.google.com/youtube/answer/1311392 (inauthentic; AI personası) · [K2] answer/6162278 (reklam dostu, öz beyan kategorileri) · [K3] answer/10835034 (seçim yanlış bilgisi) · [K4] answer/14328491 (değiştirilmiş/sentetik içerik) · [K5] answer/72851 (YPP).

## 1. Test kapısı satırları
| Satır | ✓ | Gerekçe / ölçüm |
|---|---|---|
| Inauthentic / seri üretim değil [K1] | ✓ | Özgün tez ve kendi ölçek hesabı ($1/ay = $1 milyar/yıl). "Aile değil" bölümünde 3 fark, tarihli üç olasılık. 1929 anlatımıyla 5-gram örtüşmesi %0,3 (F3). Leo'nun rolü (ev arkadaşı) ve seti (mutfak) 1929'dan farklı (sunucu/stüdyo). Sonuç tipi "üç olasılık, hüküm izleyicide"; 1929'da "kazanan açıklanır" → aynı durum, aynı sonuç değil. |
| Reused yok [K1] | ✓ | Dış klip 0 (`video/public/kbutce`). Görseller kendi Canva üretimimiz ve kendi kodumuz. Grafikler kamu verisinden (Treasury, OMB, FRED) kendi çizimimiz. |
| AI personası yok (maskot, tavsiye yok) [K1] | ✓ | Meta veride tavsiye deseni 0. Açıklama ve Shorts'ta "Leo is a fictional cartoon character, not a financial adviser" satırı var. Anlatımda S18'deki "an argument for voters, not for a cartoon roommate" tavsiyeyi reddediyor. |
| AI beyanı + açıklama satırı [K4] | ✓ | `sentetik_medya: true` 3/3. "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team." 3/3. "Not financial advice." 3/3. Yasal not metni finans-dogrulayici'nin. |
| Reklam dostu öz beyan yanıtları [K2] | ✓ | §2 |
| Lisans kaydı tam + Content ID itiraz kanıtı | ✓ | `06-muzik/lisans-kontrol.py` → 31 dosya, kayıtsız 0. Bu betiğin [4] adımı → cue'daki 31 dosyanın hepsi kayıtlı. Üçüncü taraf dosyaların hepsi CC0; kanıt sayfaları `assets/lisans-kanit/` altında (oga-*.html, 54 dosya). Kendi ses üretimimiz `ozgun-uret.py` (tohum 5400). |
| Başlık/thumbnail içerikle tutarlı [K2] | ✓ | §3 |
| Yeniden kullanılan sahne oranı ölçüldü | ✓ | §4 |
| Siyaset (seçim ertesi yayın) [K2, K3] | ✓ | Meta veri, pinli yorum ve yedek başlıklarda P1 deseni 0. Seçim sonucu, parti ve kişi yok. Thumbnail'larda parti rengi ya da siyasetçi yüzü yok. |

## 2. YouTube Studio reklam uygunluğu öz beyanı (önerilen yanıtlar; uzun + 2 Shorts)
| Kategori [K2] | Yanıt | Not |
|---|---|---|
| Uygunsuz dil | None | küfür 0 (F3 + F8) |
| Yetişkin içerik | None | — |
| Şiddet | None | 2. Dünya Savaşı yalnız tarih verisi (S19, S24). Savaş görseli yok; "asker" yüzsüz bütçe ikonu. |
| Sarsıcı içerik | None | — |
| Zararlı eylemler ve güvenilmez içerik | None | "Spiral" niteli bir olasılık olarak geçiyor, aynı sahnede 3 karşı kanıt var. Kaynaklar açıklamada. |
| Nefret / kışkırtıcı-aşağılayıcı | None | — |
| Uyuşturucu, ateşli silah, tütün | None | — |
| Tartışmalı konular | None | Bütçe ve borç bu listede yok (liste: istismar, intihar, kürtaj vb.). |
| Hassas olaylar | None | — |
| Sahtekârlığı kolaylaştırma | None | — |
| Aile için uygunsuz | None | "Not made for kids" (`cocuklara_ozel=false`). Hedef kitle genel/genç yetişkin; çocuklara yönelik değil. |
**Öneri:** tüm kategorilerde "None". Yanıtlar içerikle birebir tutarlı; yanlış öz beyan uzun vadede güven puanını düşürür, bu yüzden şişirme yok.

## 3. Vaat ↔ içerik (betik [3], kilitli anlatım cümlesiyle)
| Öğe | Videodaki karşılığı |
|---|---|
| T1 başlık "$5,400 a Month… Budget" | S01 "five thousand four hundred dollars a month… kitchen table" |
| Thumbnail A1 (ana) "−$2,000 EVERY MONTH" | S07 "every single month… about two thousand dollars short" |
| Thumbnail C1 "INTEREST > MILITARY" | S06 "pays its lenders more than it pays for its whole military" |
| Thumbnail B1 "EVERY MONTH −2,000" | S07 (A1 ile aynı) |
| Yedek başlıklar T2–T5 | 4/4 VAR. T5'teki "tripled" = S13 "roughly tripled". Bu "roughly" niteleyicisi başlıkta yok; rakam doğruluğu finans-dogrulayici'de. |
| Shorts-1 "Interest vs. the Military" / Shorts-2 "1946… What Happened?" | Okuma metninde var; Shorts-2'de "history, not a forecast" niteleyicisi var |
| Pinli yorum A/B/C | S22–S24 olasılık adlarıyla birebir |
Elle kontrol (3 thumbnail montajı): şok imgesi yok. Leo tutarlı kurgusal karakter; gerçek kişi değil. Zarf görseli nötr.

## 4. Yeniden kullanılan sahne oranı (iç kural ≤ %20; YouTube'un sayısı değil)
- Yöntem: 1 fps dHash (≤6/64 bit). Bu video 678 geçerli kare; havuz: pilot v1/v2, test yüklemesi, 1929 final (632 kare).
- Ölçülen eşleşme 20 kare = **%2,9 (üst sınır)**. Eşleşen saniyeler: 58, 319, 367, 418–424, 496–502…
- Elle doğrulama: 58, 319, 420 ve 497. saniyelerin kareleri çıkarılıp bakıldı (`PAYDAY` masası, `~1.4%` kartı, `NO LAST PAYDAY` kartı, faiz↔borç döngüsü). **Dördü de bu videoya özgü.** Eşleşmenin sebebi koyu, bulanık mutfak arka planının düşük kontrastı (dHash yanlış alarmı). Gerçek yeniden kullanım ≈ %0; giriş/çıkış ve ortak `AboneOl` bileşeni kural gereği hariç.
- F8b: final dosyada aynı komut `--video 08-kurgu/final-16x9.mp4` ile koşar. Eşleşme %20'yi geçmezse satır "F8a ile aynı" olarak geçer.

## 5. Özgünlük ve insan katkısı kanıt dosyası (YPP incelemesi / itiraz için)
| Kanıt | Yer |
|---|---|
| Özgün karakter: Leo (Niyazi'nin karakter sayfasından türetilmiş 2D maskot, kanala özgü). Bu videoda "bütçe tutan ev arkadaşı" rolünde. | `assets/karakter/karakter-karti.md`, `05-gorsel/leo/` |
| Özgün araştırma ve senaryo: 12 aday senaryo; kaynaklı rakam tablosu R01–R36 (Treasury MTS, Debt to the Penny, OMB 7.1, FRED, Shiller) | `02-senaryo/senaryolar.md`, `03-metin/rakam-tablosu.md`, `03-metin/metin.md` |
| Editoryal kararlar: hakem S08'i seçti, S06 yedek. Eleme gerekçeleri: S03 çıkar çatışması, S12 hassas olay. Düzeltme kapıları D/P/H uygulandı. | `02-senaryo/senaryo-karari.md`, `02-senaryo/politika-on-tarama.md`, `03-metin/politika-denetimi.md` |
| Kendi kodumuzla üretilen grafik ve animasyon: 27 sahnenin 8'inde kendi veri grafiği (G1–G5 vb.), plan süresinin 265/705 sn'si ≈ %38 [metin planı]. 25/27 sahnede kodla üretilmiş ekran yazısı. Rhubarb dudak senkronlu rig ve Remotion kurgusu tamamen kodda. | `video/src/videolar/yeni-video/`, `07-animasyon/grafik-veri.py`, `07-animasyon/senkron-rapor.md` |
| AI destekli görseller: Canva `generate-image`, kendi promptlarımız, referans karakter sayfası | `05-gorsel/canva-promptlari.md`, `05-gorsel/rapor.md` |
| Ses: AI TTS (Kokoro am_fenrir, beyanlı), CC0 müzik ve efekt + kendi üretimimiz efektler | `04-ses/`, `06-muzik/lisans-kaydi.md` |
| Önceki videolardan yeniden kullanılan sahne oranı: üst sınır %2,9, doğrulanmış ≈ %0 | §4 |

## 6. Risk notu (hakeme bilgi; SARI değil)
- Yayın seçimin ertesi günü (4 Kas). Pinli A/B/C sorusundaki B seçeneği partizan yorum çekebilir. F11 sonrası yorum moderasyonu yapılmalı; kanal yanıtları nötr kalmalı (`09-paket/yorum-yanitlari.md`).
- Content ID: tüm müzik CC0. Risk "orta-düşük" olarak işaretlenen parça "The Way It Is" (Zane Little; sanatçı Bandcamp'te de yayınlıyor). Talep gelirse itiraz kanıtı `assets/lisans-kanit/oga-the-way-it-is.html` ve CC0 linki. İtirazı yalnız Niyazi onayıyla koordinatör yapar.
