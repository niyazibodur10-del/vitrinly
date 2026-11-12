# monetizasyon-uyum-uzmani — hafıza

## Kurallar
- Kaynaklı politika gerçekleri (son kontrol 2026-11-02; 1311392 son tarihli giriş 2025-07-15):
  - YPP: 1.000 abone + 4.000 saat/12 ay uzun video (Shorts akışı sayılmaz) veya 10 M Shorts/90 gün; 1 Şub 2027'den yeni başvuruya 8.000 saat / 20 M (answer/12843009). Ek: ihtar yok, 2 adımlı doğrulama, AdSense (answer/72851).
  - 1311392 başlığı 2026-11-10'da "Generic or Repetitive Content" (eski repetitious/inauthentic): şablon, "same situation… same outcome", "AI… templates giving the impression of mass production".
  - AI personası: "human expert providing advice" — sağlık, hukuk, finans, **siyaset** → para kazanamaz. Maskot tavsiye vermez (1311392).
  - Reklam dostu (6162278): hassas olay = istismar etmeyen haber/eğitim uygun; tartışmalı konular listesinde seçim yok; seçim yalnız "harmful misinformation" (ayrıca 10835034).
- Betikler (kopyala, parametre değiştir): F2 `uretim/2026-11-04-miras-sizintilari/02-senaryo/politika-tarama.py` (v3: v2 + suç/dolandırıcılık/mağdur kelimeleri + S08 bütçe format işaretleri; argüman: tüm yayımlanmış metin.md); F3 `uretim/2026-10-28-yeni-video/03-metin/politika-denetim.py` (v2: hakem P-kapıları + GÖRSEL + Shorts <<…>> + korku cümlesi niteli/niteliksiz; eski v1 1929 klasöründe); F8 `uretim/2026-11-04-miras-sizintilari/09-paket/politika-f8.py` (v3: v2 + havuz önceki 2 final, dHash adayı 32x18 MAD ≤5 ile doğrulanır, [7] kapanış 4-gram/kalıp sayımı; `--video` final).
- Her betik koşusundan sonra elle ikinci geçiş: Türkçe yapı satırları, karakter anları, ekrana yazılan not/levha, thumbnail metni.
- AI persona sızıntısı: Leo'nun bugüne dönük kuralı ("I believe now", "you should", "your money"). Düzeltme: emir → betimleyici cümle; "uyarı ekle" önerme.
- Meta veri riski metinden ayrı puanlanır: gerçek kişiye suç/kötü çağrışımı (heist, villain), doğrulanmamış pay, nefret kalıbı → metin temizken bile SARI.
- Shorts tek başına okunur; bağlam niteleyicisi kesitte düşerse kapanışı sebep cümlesine çevir.
- F8: vaat↔anlatım eşlemesini anlatımdaki cümleyle yaz; JSON dosya yollarını gerçek dosyayla karşılaştır (politika dışı zorunlu ayrı satır); kare denetimi kontakt sayfası (ffmpeg fps + drawtext + tile), Illustration etiketini 1080p kırpımla doğrula; Shorts 9:16 ayrıca.
- Kaynak metin örtüşmesi (Ö8): kaynağı scratchpad'e indir, 8-gram ölç, repoya koyma.

## Dersler
- Kanal kuralı adayı: ilk 5 videoda "çöküş + Leo kaybeder" tekrarlanmasın; 5 videoluk denetimde Leo sonuç tipi sayılır. Kayıt: 1929 = kazanan açıklanır; 10-28 havuzu (12 senaryo) 12 farklı rol, kaybeden yok.
- 2026-10-27 (1929): ayrıştırıcı "BULUNAMADI" → yetkili satırdan oku; eklenen cümleyi sonraki 2 cümleyle oku; deyim+SFX klişesi görselde yoksa YEŞİL.
- 2026-11-02 (F2, 12 senaryo): 8 YEŞİL / 4 SARI / 0 KIRMIZI. Çıkar çatışması (metni yazan modelin şirketi konu) için YouTube'da kural yok → KIRMIZI'yı kaynakla destekleyemezsin; SARI-yüksek + "bu slotta önerilmez" + beyan metni + hakem tarafsızlık kontrolü yaz, kendi modelini açıkça belirt.
- 2026-11-02: Seçim sonrası günü yayın → "who won" yalnız resmi/AP çağrısına dayansın, "too close to call" yedeği zorunlu; "your money" başlığı siyaset + finans persona riskini birleştirir → "markets".
- 2026-11-02 (F3 S08): YEŞİL, zorunlu 0. Hakem P-kapılarını betikte ayrı bölüm yap; korku kelimesini cümle düzeyinde "niteli/niteliksiz" say (yalnız kelime sayımı yanlış alarm). Köprü kalıbı "By the end, you'll know" 2 videoda tekrar → 5 videoluk denetimde say.
- 2026-11-02 (F8a S08): ONAY, hata 0. dHash koyu/bulanık arka planlarda yanlış alarm veriyor (%2,9 → elle 4/4 özgün) → eşleşen kareleri her zaman çıkarıp bak, "üst sınır" ve "doğrulanmış" ayrı yaz. Lisans eşlemesinde grup yazımını aç (paper_01/02/03).
- 2026-11-04 (F2, 12 senaryo): 9 YEŞİL / 3 SARI / 0 KIRMIZI. 5-gram %0 iken fikir tekrarı olabilir → yayımlanmış metinde tezi grep'le (S06 ↔ S08 satır 85/124). Suç belgeseli 6162278'de "can earn"; sınır "how to gain unauthorized access" + intihar (Controversial listesi) → bunları zorunlu madde yaz.
- 2026-11-04: Kapanış kalıbı "üç olasılık" 9/12 senaryoda + S08'de → 5 videoluk denetimde kapanış tipini say; F2'de kanal düzeyi not olarak ver.
- 2026-11-04 (F3 S03): YEŞİL, zorunlu 2. Uç ekran köprüsü 3 videoda aynı kalıp ("a story/game for another X") → F3'te önceki metinlerin son sahnesini ayrıca karşılaştır. ABD'ye özgü eşik içeren Shorts'a "American/US federal" niteleyicisi zorunlu.
- 2026-11-10 (F8 S03): ONAY, hata 0. dHash üst sınır %26,9 (ortak lacivert grafik zemini) → 2. aşama 32x18 MAD ≤5 (pozitif 2,8 / yanlış alarm min 6,6) doğrulanmış %0. Kapıyı doğrulanmış orana bağla, üst sınırı ayrıca yaz.
- 2026-11-10: Kanal kalıp adayları (5 videoluk denetimde say): son satırda nesne şakası (S08/S03), tek harf/rakamla yorum çağrısı (S08/S03), thumbnail şaşkın yüz (S08 A1/S03 K4).
- 2026-11-10 (Flip By Vote format, `uretim/seri/politika-format.md`): çok platformda IG/TikTok yardım sayfaları WebFetch'te boş döner → transparency.meta.com, about.fb.com, tiktok.com/community-guidelines kullan. Meta AI etiketi "realistic-sounding audio" → TTS'li çizgi filmde de AÇIK; TikTok'ta otomasyon yasağı → otomatik yanıt yok.
- 2026-11-10: Çizgi film + oyun/oyuncak = YouTube "made for kids" riski → yorumlu formatta her zaman MFK=false ve çocuk etkinliği seçeneği yok; sabit CTA'yı bölüme özgü soruya çevir (yem + şablon riskini birlikte düşürür).
- 2026-11-12 (Flip By Vote B002): sıfır oy anlatımında suçlama yerine doğruluğa bak; veri kaynağı okunamayan kanal (IG hikâye anketi) varsa "No votes" doğrulanmamış iddia → kontrol ya da "No comments". CC BY atfında lisans URI + değişiklik beyanı zorunlu (§3(a)(1)); yalnız "(CC BY 4.0)" yetmez.
