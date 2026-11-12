# Bölüm 002 · politika denetimi (monetizasyon-uyum-uzmani, 2026-11-12)
İLERLEME: tamam. Girdi: `metin.md` v1, `veri/satirlar.py` sha256 ce442ec7599f.
**KARAR: DÜZELT.** Replikler politika açısından temiz. KIRMIZI 0. **Zorunlu 2:**
- **Z1:** "No votes" iddiası 3 platformda doğrulanmalı. IG hikâye anketi okunamadı.
- **Z2:** CC BY 4.0 ses atıf satırına lisans bağlantısı ve değişiklik beyanı eklenmeli.
Önerilen 1 (Ö1). Metin değiştirilmedi.
Kaynaklar `uretim/seri/politika-format.md` §8'de; bu denetimde 2026-11-10 alıntıları kullanıldı (hız kuralı). CC BY 4.0 metni yerelden okundu (`assets/lisans-kanit/cc-by-4.0-legalcode.html`).

## Özel sorular
| Konu | Bulgu | Karar |
|---|---|---|
| "No votes, so I picked." + "Next time, you decide. Please." | **Suçlama yok.** Sıfır oy Mike'ın aceleciliğine şaka olarak bağlanıyor, izleyici kusurlu gösterilmiyor. "Please" bir rica; ödül, tehdit, suçluluk ("you ignored us") ya da "comment X" yok. Meta tanımı "explicitly request engagement (votes, shares, comments…)" [B-4]: replikte yorum ya da oy isteği yok, yalnız karar daveti var. YouTube "It's okay to ask viewers to… comment" [B-1]. | YEŞİL |
| **Doğruluk** (Z1) | `bolum-001/kazanan.md`: YouTube 0 yorum, IG 0 izleyici yorumu. Ama **"Hikâye anketi verisi API'den okunamıyor"** ve TikTok için "paylaşım bilgisi yok" yazıyor. CLAUDE.md'ye göre hikâye anketi oyları da sayılır. "No votes" ve ekrandaki "0 votes" rozeti doğrulanmamış bir sayı. Yanlışsa oy veren izleyiciye ekranda yanlış bilgi verilmiş olur ve formatın güven kuralı bozulur (PDF s. 3). | **Z1** |
| "Take the ninety, hold out, or counter?" + "Tell us in the comments." | Seçenekleri adıyla soran bölüme özgü bir tavsiye sorusu. `politika-format.md` §1 seçenek B'ye birebir uyuyor. Meta 2017 istisnası: "ask people for… advice, or recommendations" [B-5]. Kartta harf/numara yok. "counter" bir pazarlık terimi, finans tavsiyesi değil. | YEŞİL |
| "Brenda" | **Brenda alıcı değil, bisikletin adı** (M01 "Meet Brenda!", S1 isim etiketi). Alıcılar adsız ("a guy"). Soyadı, gerçek kişi, ünlü ya da marka göndermesi yok. Seri incilindeki "nesnelere isim koyma" kuralıyla uyumlu. İnsan adının cansız nesneye verilmesi YouTube taciz kuralının kapsamına girmiyor [T: hedef kişi yok]. | YEŞİL |
| AI satırı | "Fiction. Not financial advice. Voices and visuals are AI-generated." 3/3 platformda var. Platform AI etiketleri AÇIK (format §3). | YEŞİL |
| Anonim kalma satırı | "We may show winning comments… Prefer to stay anonymous? Just say so in your comment." YT, IG, TikTok ve sabit yorumda var (4/4). Teşvik dili yok. | YEŞİL |
| Ses atfı (Z2) | "Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0)." CC BY 4.0 §3(a)(1) şunları istiyor: "include the text of, or the URI or hyperlink to, this Public License" ve "indicate if You modified the Licensed Material". Mevcut satırda ikisi de yok. VCTK üreticisi (CSTR, University of Edinburgh) da yazılmamış. | **Z2** |

## Diğer kontroller (elle, 31 replik + §6 paket)
- Kişiye yönelik tavsiye 0. "Trust the vibe" ve "Fast. And safe." karakter sözü; izleyiciye "you should" denmiyor. Yatırım, kumar ve kripto 0. Şok ve küfür 0. Gerçek marka 0: telefon, mesaj ve seri no ekranı logosuz.
- "SERIAL CHECK ✓ not reported stolen": rutin bir karakter davranışı; gerçek bir servis adı yok. YEŞİL.
- Alıcı buluşması gündüz, kalabalık sokakta (G2) → incil §5.3 ile uyumlu.
- Başlıklar T1–T3 içerikle tutarlı. T3 "Was he right?" sorusu bölüm 3'te yanıtlanıyor; yanıltıcı vaat yok.
- Hashtag'lerde "kids" ve #Shorts yok → MFK riski artmıyor (format §2). Gün sözü yok ("Ep. 3: YOUR call").
- Şablon: B001 ile 5-gram örtüşmesi %0,0 (betik). Sabit kalıp oranı %13 (≤%20). Sonuç tipi henüz yok (ilk sonuç bölüm 3'te) → kural 2 sayımı bölüm 3'te başlar.
- Sondaki takip kartı: düz bir çağrı, ödül ya da aldatma yok. TikTok kuralı yalnız "manipulate… into inflating likes or follows" yasaklıyor [B-7]. YEŞİL.

## Düzeltmeler
| # | Satır | Kaynak | Öneri (seçenekler → seçilen) | Tür |
|---|---|---|---|---|
| Z1 | M01 "No votes, so I picked." · S1 rozeti "0 votes" · YT/IG açıklama "Nobody voted last time" / "No votes last time" · T3 | Format güven kuralı (PDF s. 3); YouTube aldatıcı uygulamalar [B-1] | (a) **Seçilen:** render'dan önce Niyazi IG uygulamasında hikâye anketini kontrol etsin. Anket yoksa ya da 0 oy varsa metin aynen kalır. Kontrolü koordinatör `kazanan.md`'ye yazar. (b) Kontrol yapılamazsa replik "No comments, so I picked.", rozet "0 comments", açıklama "Nobody commented last time" olur (süre değişmez). (c) Anket oyu varsa kazanan anketten seçilir ve S1/M01 yeniden yazılır. | zorunlu |
| Z2 | §6 her üç platformdaki "Voices: …" satırı | CC BY 4.0 §3(a)(1)(B)(C) | → `Voices: Kyutai Pocket TTS; Jake's voice synthesized from the VCTK corpus (CSTR, University of Edinburgh). CC BY 4.0: creativecommons.org/licenses/by/4.0`. YouTube'da ek satır: `Sources: huggingface.co/kyutai/pocket-tts-without-voice-cloning · datashare.ed.ac.uk/handle/10283/3443`. Üretici betik (`bolum-001/paket/paket-uret.py`) ve `uretim/seri/lisans-kaydi.md` satır 56 aynı şekilde güncellenir. Yayındaki Bölüm 1 açıklaması da 30 gün içinde düzeltilir (§6(b) iyileştirme süresi). | zorunlu |
| Ö1 | S1 rozeti "0 votes" (ilk 3 sn) | Politika değil, viralite | Yeni izleyiciye "kimse izlemiyor" sinyali veriyor (yazar K2'yi aynı gerekçeyle eledi). Rozeti kaldır, sözlü replik yeterli. | önerilen |
