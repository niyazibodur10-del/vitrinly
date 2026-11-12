# F8 politika raporu — S03 "The Great Wealth Transfer Has a Leak" · monetizasyon-uyum-uzmani · 2026-11-10

İLERLEME: tamam (F8a tam rapor, girdi `07-animasyon/tam-16x9.mp4`). F8b = final dosyalar hazır olunca: `python3 -I 09-paket/politika-f8.py --video 08-kurgu/final-16x9.mp4` + Shorts 9:16 kontakt sayfası (hakem). Değişmeyen satırlar "F8a ile aynı" olarak geçer.
**KARAR: ONAY (YEŞİL). KIRMIZI 0 · SARI 0 · zorunlu düzeltme 0 · öneri 2 · kanal notu 3.**
sentetik_medya: true
**Gerekçe:** Anlatıcı sesi AI (Kokoro TTS), illüstrasyonlar AI destekli (Canva). Beyanın para kazanmaya ve erişime etkisi yok; kanal emsali 1929 ve S08. 3 paket için geçerli (uzun + 2 Shorts).
**Kanıt:** `python3 -I 09-paket/politika-f8.py` (v3) 2 koşu → `diff` AYNI, `SONUC hata=0` (`log/politika-f8-1.txt`, `-2.txt`). sha256: betik `fb6f3d537844` · video `da07cfd7ce50` (781,4 sn) · metin `22ba68b7750c` · paket.md `31bd34264715` · yayin-paketi `61545ed3f5ad` / shorts-1 `46f8757d47e5` / shorts-2 `909d7d66293e` · K1 `623027240f81` · K4 `6bf2d245ba41` · K3 `5509f04fce40`.
**Kapılar:** meta veri dili 0/11 · AI satırı 3/3 · vaat↔anlatım 13/13 VAR · lisans 45/45 kayıtlı, NC/ND/SA 0, kanıt eksik 0 · yeniden kullanılan sahne: dHash üst sınır %26,9 → 2. aşama doğrulanmış **%0,0** (≤ %20) · dış klip 0 · kapanış 4-gram örtüşmesi 0/0.
**Hakeme not (politika dışı):** `tam-16x9.mp4` 508–513 sn'de "US FEDERAL ESTATE TAX STARTS: $15M PER PERSON (2026)" başlığı kadrajın üstünden kesik (kamera kayması). Final dosyada kontrol edilmeli (animasyon-yonetmeni / kurgu-editoru).

## Kaynaklar (son tam kontrol 2026-11-04, F2; değişiklik yok. Alıntılar hafızada ve F2/F3 raporlarında)
[K1] support.google.com/youtube/answer/1311392 (inauthentic: "mass-produced, generic, repetitive"; AI personası: "human expert providing advice… finances") · [K2] answer/6162278 (reklam dostu, öz beyan kategorileri) · [K4] answer/14328491 (değiştirilmiş/sentetik içerik) · [K5] answer/72851 (YPP).

## 1. Test kapısı satırları
| Satır | ✓ | Gerekçe / ölçüm |
|---|---|---|
| Inauthentic / seri üretim değil [K1] | ✓ | 6 duraklı özgün model (kutu/kamyon), kaynaklı veri (Cerulli, Fed SCF/DFA, IRS, CareScout), tek tez ("headline gerçek ama lumpy ve gecikmeli"). Leo'nun rolü (nakliye şefi) ve seti (yol) 1929 (stüdyo) ve S08'den (mutfak) farklı. Sonuç tipi "envanter + iki koşullu cümle"; 1929 "kazanan açıklanır", S08 "A/B/C" → aynı durum, aynı sonuç yok. Tüm metin ortak 4-gram: 1929 ile 1, S08 ile 6. |
| Reused yok [K1] | ✓ | Dış klip 0 (`video/public/kmiras`). Görseller kendi Canva üretimimiz, grafikler kendi kodumuz (kamu verisinden). |
| AI personası yok [K1] | ✓ | Meta veride tavsiye deseni 0. Leo kendini "cartoon moving-crew boss" diye tanıtıyor. S29: "This isn't a forecast for any family, and it isn't a plan." Shorts açıklamalarında "not a financial adviser" var. Öneri Ö1. |
| AI beyanı + açıklama satırı [K4] | ✓ | `sentetik_medya: true` 3/3; "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team." 3/3; "Not financial advice." 3/3. |
| Reklam dostu öz beyan [K2] | ✓ | §2 |
| Lisans tam + Content ID kanıtı | ✓ | cue'daki 45 dosya (8 müzik bloğu + 201 vuruş + 2 Shorts yatağı) kayıtlı. Üçüncü taraf dosyaların hepsi CC0; kanıt HTML'leri `assets/lisans-kanit/` (76 html). Earshot SFX kendi üretimimiz (28 dosya). Atıf satırları açıklamada (`06-muzik/atif-satirlari.md`, rubberduck dahil). |
| Başlık/thumbnail içerikle tutarlı [K2] | ✓ | §3 |
| Yeniden kullanılan sahne oranı ölçüldü | ✓ | §4 |
| Siyaset | ✓ | P1 deseni meta veri, pinli yorum ve yedek başlıklarda 0. Metinde yasa adı yok. Yalnız IRS kaynak URL'sinin adresinde "one-big-beautiful-bill" geçiyor: resmî kaynak adresi, yorum değil → risk yok. |

## 2. YouTube Studio reklam uygunluğu öz beyanı (önerilen; uzun + 2 Shorts)
| Kategori [K2] | Yanıt | Not |
|---|---|---|
| Uygunsuz dil | None | küfür 0 (F3 + F8) |
| Yetişkin içerik / Şiddet / Sarsıcı | None | Ölüm soyut: ebeveyn vefatı yüzsüz silüet, kayıp görüntüsü yok. Bakımevi sahneleri yüzsüz koridor. |
| Zararlı eylemler ve güvenilmez içerik | None | Tahminler "forecast/estimate" diye etiketli. Vergi kaçınma yöntemi yok. |
| Nefret / kışkırtıcı-aşağılayıcı | None | Kuşak suçlaması yok (P2). Din kurumları eşit sayılıyor. |
| Uyuşturucu, ateşli silah, tütün | None | — |
| Tartışmalı konular | None | Miras, vergi ve yaşlı bakımı listede yok. |
| Hassas olaylar | None | — |
| Sahtekârlığı kolaylaştırma | None | — |
| Aile için uygunsuz | None | `cocuklara_ozel=false` ("Not made for kids"). |
**Öneri:** tüm kategorilerde "None". İçerikle birebir tutarlı; şişirme yok.

## 3. Vaat ↔ içerik (betik [3], kilitli anlatım cümlesiyle)
| Öğe | Videodaki karşılığı |
|---|---|
| T1 "…Has a Leak" | S2 "which leak is the biggest", S5 "to see the real leaks" |
| Thumbnail K1 "WHO GETS IT?" + $124T | S1 "let's count what reaches the kids"; S28 "For a few families, the truck is a whole convoy. For most, it's a few boxes, and they come late." |
| Thumbnail K4 "IT KEEPS LEAKING" | S14 "It gives the other leaks more time"; S30 "I'm going to need more tape" |
| Thumbnail K3 "SMALLER. LATER." | S2 "less than the headline sounds, and get it later" |
| Yedek T3/T4/T5/T7 | 4/4 VAR. T5 "Ever" = metinde "often called the biggest inheritance in history" (niteli). |
| Açıklama "later, not never" | S13 "It isn't a leak at all"; S14 "The detour doesn't take any boxes" |
| Shorts-1 "Spouse First" / Shorts-2 "If Not Taxes…" | Okuma metninde birebir. Shorts-2'de "most American families" + "federal estate tax" niteleyicisi var (F3 Z2 uygulanmış). |
| Pinli yorum 6 durak | S7–S22 durak adlarıyla birebir |
Elle kontrol (3 thumbnail): şok imgesi yok, banknotlar genel çizim (portre/gerçek desen yok), gerçek kişi ve logo yok.

## 4. Yeniden kullanılan sahne oranı (önceki 2 final: 1929 + S08; iç kural ≤ %20)
- 1. aşama 1 fps dHash ≤6/64: 781 karenin 210'u aday → **üst sınır %26,9**. Adaylar yalnız 27 kaynak kareye bağlanıyor (çoğu 1929'un 213–231, 252, 315, 550. saniyeleri ve S08'in 418–421. saniyeleri). Hepsi ortak lacivert vinyet zeminli az detaylı kartlar.
- 2. aşama (v3'te eklendi): aday çiftler 32x18 gri ortalama mutlak farkla doğrulanır, eşik 5/255. Pozitif kontrol (aynı plan, 0,2 sn ara) 2,8; yanlış alarmlarda en düşük değer 6,6 → **doğrulanmış %0,0**.
- Elle doğrulama: 12 aday kare + 6 kaynak kare kontakt sayfasında açıldı, en düşük farklı 4 çift ayrıca yan yana bakıldı (SCHOOLS ↔ DOOR TWO, kutular ↔ BANK, vergi çizgisi ↔ DOOR 2). **Hepsi bu videoya özgü.** Ortak olan yalnız kanalın grafik zemini (marka dili; yeniden kullanılan içerik değil).

## 5. Özgünlük ve insan katkısı kanıt dosyası (YPP incelemesi / itiraz için)
| Kanıt | Yer |
|---|---|
| Özgün karakter: Leo (Niyazi'nin karakter sayfasından 2D maskot), bu videoda nakliye şefi rolünde, yeni set (yol + kamyon). | `assets/karakter/karakter-karti.md`, `05-gorsel/leo/` |
| Özgün araştırma ve senaryo: 12 aday senaryo, kaynaklı rakam tablosu, doğrulama raporu | `02-senaryo/senaryolar.md`, `03-metin/rakam-tablosu.md`, `03-metin/dogrulama.md` |
| Editoryal kararlar: hakem S03'ü seçti, S01 yedek (D1–D6, P1–P3, K1, H1–H8). F3'te Z1 (kapanış kalıbı) ve Z2 (Shorts niteleyicisi) uygulandı. | `02-senaryo/senaryo-karari.md`, `02-senaryo/politika-on-tarama.md`, `03-metin/politika-denetimi.md` |
| Kendi kodumuzla grafik ve animasyon: 31 sahnenin 19'unda kodla çizilen grafik/kart/pano [metin GÖRSEL sütunu, grep]. Kutu oranları `03-metin/veri/kutu-hesap.py`'den. Rhubarb dudak senkronlu rig, Remotion kurgusu. | `video/src/videolar/miras-sizintilari/` (grafik.tsx, sahneler.tsx, rig.ts) |
| AI destekli görseller: Canva `generate-image`, kendi promptlarımız, karakter referansı | `05-gorsel/canva-promptlari.md`, `05-gorsel/rapor.md` |
| Ses: AI TTS (beyanlı), CC0 müzik ve efekt, earshot ile kendi efektlerimiz | `04-ses/`, `06-muzik/lisans-kaydi.md` |
| Önceki videolardan yeniden kullanılan sahne: doğrulanmış %0,0 (üst sınır %26,9) | §4 |

## 6. Öneriler (zorunlu değil) ve kanal notları
- **Ö1 (youtube-paketleyici / finans-dogrulayici):** uzun açıklamanın yasal notunda "Leo is a fictional cartoon character." var, ama Shorts'taki ", not a financial adviser" eki yok. Seçenekler: (a) **Önerim:** ekle (3 paket aynı dil, persona savunması güçlenir, viralite etkisi 0). (b) Olduğu gibi bırak (S29 cümlesi yeterli). Metin finans-dogrulayici'nin.
- **Ö2 (Content ID):** risk düşük-orta parçalar Pro Sensory ("Sunny Side Up", "Joy Ride"). Talep gelirse itiraz kanıtı `assets/lisans-kanit/oga-sunny-side-up-updated-version.html` / `oga-joy-ride.html` + CC0 linki. İtirazı yalnız Niyazi onayıyla koordinatör yapar.
- **Kanal notu (5 videoluk denetimde sayılacak):** (1) Kapanış: soru köprüsü, "story/game for another…" yok, 4-gram 0. (2) Son satırda nesneyle şaka ("keeps finding envelopes" S08 ↔ "need more tape" S03): 2 videoda var, tekrar sınırında değil. Tek harf/rakamla yorum çağrısı da 2 videodur var (S08 "one letter", S03 "Reply with its number"). (3) Leo ifadesi: ana thumbnail K1 kuşkulu, S08 A1'in şaşkın yüzünden farklı. K4 (Test & Compare 2.) şaşkın, S08 ile aynı tip. Politika riski yok, CTR/tek tiplik konusu (thumbnail-tasarimcisi, teşhis b5).
