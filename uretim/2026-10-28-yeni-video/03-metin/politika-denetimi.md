# F3 politika denetimi — S08 metin v1.1 · monetizasyon-uyum-uzmani · 2026-11-02

İLERLEME: tamam
**SONUÇ: YEŞİL. KIRMIZI 0 · SARI 0 · zorunlu düzeltme 0.** 2 isteğe bağlı öneri var (§3); metin kilidini bekletmez.
**Hakem P1–P4 (yeniden ölçüldü, Shorts dahil):** P1 GEÇTİ · P2 GEÇTİ · P3 GEÇTİ · P4 karar önerisi `sentetik_medya = true` (kesin karar F8'de).
**Kanıt:** `python3 -I politika-denetim.py metin.md --onceki ../../2026-10-26-1929-1000-dolar/03-metin/metin.md` 2 koşu → `diff` aynı. Girdi metin.md sha256 `89bebe18d3d4` (eb9770a). 27 sahne, 1.856 kelime, 2 Shorts.
**Inauthentic:** 1929 anlatımıyla 5-gram örtüşmesi %0,3 (Ö7 ≤ %10 GEÇTİ). Anlatı, yorum ve eğitim değeri yüksek: kendi ölçek hesabı, "aile değil" bölümünde 3 somut fark, tarihli üç olasılık. Haber okuma ya da liste değil [K1].
**AI personası:** Leo "cartoon roommate"; S18'de "an argument for voters, not for a cartoon roommate" cümlesi tavsiyeyi açıkça reddediyor. Emir kipi ve "your money" 0 [K1].
**İlk 30 sn + başlık:** şok veya küfür 0; başlık ("If America Earned $5,400 a Month…") S01 hook'uyla birebir karşılanıyor [K2].

## Kaynaklar (2026-11-02 kontrolü; F2 raporunda alıntılı)
[K1] answer/1311392 (inauthentic; AI personası finans + siyaset) · [K2] answer/6162278 (reklam dostu; tartışmalı konu listesinde seçim/bütçe yok; harmful misinformation) · [K3] answer/10835034 (seçim yanlış bilgisi) · [K4] answer/14328491 (sentetik beyan; 1929 F8 kararı emsal).

## 1. P1–P4 ölçümü
| Kapı | Betik bulgusu | Değerlendirme | Sonuç |
|---|---|---|---|
| P1 parti / isim / renk / yüz / seçim sonucu | Anlatım 2 ("an argument for voters", "can't vote for a bigger salary"); GÖRSEL 2 (her ikisi "parti/kişi/renk yok (P1)" notu); renk deseni 0; Shorts 0; başlık 0 | İki "vote" geçişi genel ve partizan değil; ikincisi tavsiyeyi reddediyor. Siyasetçi adı yok. Seçim sonucu yok, "who caused it" suçlaması yok. Capitol ve Fed binası yüzsüz, bayraksız ikon [K2, K3]. | GEÇTİ |
| P2 korku dili | 1 cümle ("could this turn into a spiral"), NİTELİ: soru + "It's a possibility" + 3 fren aynı sahnede (S20) | "default", "collapse", "crash" 0. Spiral cümlesinin hemen arkasından karşı kanıt geliyor [K2 güvenilmez içerik]. | GEÇTİ |
| P3 üç olasılık / tavsiye | Anlatımda 2 eşleşme ("dollars borrowed", "safest assets"), Shorts 0, ekranda 0 | A/B/C tarih (1946–74) ve mekanizma olarak sunuluyor; S21'de "not a forecast". Enflasyon dalı varlığa bağlanmıyor (S24 GÖRSEL: "Varlık/altın/yatırım görseli yok"). "safest assets" borç verenlere atfedilmiş bir betimleme ("lenders… treat these bonds as"), öneri değil [K1]. | GEÇTİ |
| P4 AI beyanı | — | Açıklamada "Narration voice is AI-generated" satırı ve yasal not olacak (yasal not finans-dogrulayici'nin). **Öneri `sentetik_medya = true`:** K4 tam animasyonu muaf tutuyor, ama beyanın para kazanmaya etkisi yok ve kanal tutarlılığı 1929 kararıyla korunur. Kesin karar ve açıklama satırının kontrolü F8'de. | GEÇTİ (F8'de teyit) |

## 2. Diğer taramalar
| Tarama | Sonuç |
|---|---|
| Savaş / şiddet görseli | 2 eşleşme. Biri S23'teki yüzsüz "asker" silueti (bütçe kalemi ikonu), diğeri S02'de yanlış alarm. S19 ve S24'teki 2. Dünya Savaşı anışı tarih verisi; görsel olarak yalnız kendi grafiğimiz G5 var [K2]. Uygun. |
| Yayın gününe bağlı zaman sözcüğü | 0 |
| Shorts 1 (130 kelime ≈49 sn) | Tek başına okundu. Ölçek niteleyicisi ("If the U.S. were a family…") var. Anlatımda olmayan cümle yalnız hook ve kapanış ("Interest is the one bill that buys nothing", "The whole kitchen table is in the long video"). Tavsiye yok. GEÇTİ |
| Shorts 2 (104 kelime ≈39 sn) | Niteleyiciler "history" ve "This is history, not a forecast". Bazı anlatım cümleleri kısaltılmış ("The economy grew around it, and prices rose too"). Politika açısından sorun yok. **finans-dogrulayici'ye bilgi:** Shorts'ta "U.S. debt", anlatımda "debt held by the public" deniyor; kesinlik kontrolü onların alanı. GEÇTİ |
| Reklam dostu konu | Sosyal Güvenlik, Medicare ve savunma bütçe kalemleri tartışmalı konular listesinde değil [K2]. Seçim ertesi partizan ısıyı P1 dili düşürüyor. |

## 3. İsteğe bağlı öneriler (senaryo-yazari; zorunlu değil)
1. **S20 "one of the safest assets in the world"** için katı okuma şu: AI maskot belirli bir varlığı "en güvenli" diye anıyor [K1]. Seçenekler: (a) olduğu gibi bırak; cümle borç verenlere atfedilmiş, viralite kaybı 0. (b) "…as one of the safest places to lend money in the world" yaz; risk biraz daha düşük, anlam aynı. (c) "…still line up to buy these bonds" yaz; en nötr hali, fren argümanı biraz zayıflar. **Öneri: (b).** Uygulanmazsa YEŞİL kalır.
2. **Kanal kalıbı:** 1929 ile ortak 5-gram "By the end, you'll know…" (S02 köprüsü). %0,3 risk değil, ama iki videodur aynı köprü kalıbı kullanılıyor. 5 videoluk denetimde 1311392 "template" okuması için sayılacak. Sonraki videoda köprü cümlesi değiştirilsin (bu metinde değişiklik gerekmez).
3. **S25 yorum sorusu** (A/B/C): B (vergi/harcama) seçim ertesi partizan yorum çekebilir. Bu metin sorunu değil; F11 sonrası yorum moderasyonu ve sabit yorum nötr kalsın (koordinatör/paketleyici).
