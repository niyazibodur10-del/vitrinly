# monetizasyon-uyum-uzmani — hafıza

## Kurallar
- Kaynaklı politika gerçekleri (son kontrol 2026-11-02; 1311392 son tarihli giriş 2025-07-15):
  - YPP: 1.000 abone + 4.000 saat/12 ay uzun video (Shorts akışı sayılmaz) veya 10 M Shorts/90 gün; 1 Şub 2027'den yeni başvuruya 8.000 saat / 20 M (answer/12843009). Ek: ihtar yok, 2 adımlı doğrulama, AdSense (answer/72851).
  - Inauthentic (eski repetitious): şablonla seri üretim izlenimi; "aynı durum, aynı sonuç". Aynı giriş/çıkış serbest (answer/1311392).
  - AI personası: "human expert providing advice" — sağlık, hukuk, finans, **siyaset** → para kazanamaz. Maskot tavsiye vermez (1311392).
  - Reklam dostu (6162278): hassas olay = istismar etmeyen haber/eğitim uygun; tartışmalı konular listesinde seçim yok; seçim yalnız "harmful misinformation" (ayrıca 10835034).
- Betikler (kopyala, parametre değiştir): F2 `uretim/2026-10-28-yeni-video/02-senaryo/politika-tarama.py` (v2: EN yayın metni + TR blok siyaset/şiddet/AI/1929-format sayımı + önceki metinle 5-gram); F3 `uretim/2026-10-26-1929-1000-dolar/03-metin/politika-denetim.py` (Shorts'u §5 "Okunacak tam metin" satırından okur); F8 `.../09-paket/politika-f8.py` (`--video` final).
- Her betik koşusundan sonra elle ikinci geçiş: Türkçe yapı satırları, karakter anları, ekrana yazılan not/levha, thumbnail metni.
- AI persona sızıntısı: Leo'nun bugüne dönük kuralı ("I believe now", "you should", "your money"). Düzeltme: emir → betimleyici cümle; "uyarı ekle" önerme.
- Meta veri riski metinden ayrı puanlanır: gerçek kişiye suç/kötü çağrışımı (heist, villain), doğrulanmamış pay, nefret kalıbı → metin temizken bile SARI.
- Shorts tek başına okunur; bağlam niteleyicisi kesitte düşerse kapanışı sebep cümlesine çevir.
- F8: vaat↔anlatım eşlemesini anlatımdaki cümleyle yaz; JSON dosya yollarını gerçek dosyayla karşılaştır (politika dışı zorunlu ayrı satır); kare denetimi kontakt sayfası (ffmpeg fps + drawtext + tile), Illustration etiketini 1080p kırpımla doğrula; Shorts 9:16 ayrıca.
- Kaynak metin örtüşmesi (Ö8): kaynağı scratchpad'e indir, 8-gram ölç, repoya koyma.

## Dersler
- Kanal kuralı adayı: ilk 5 videoda "çöküş + Leo kaybeder" tekrarlanmasın; 5 videoluk denetimde Leo sonuç tipi sayılır. Kayıt: 1929 = kazanan açıklanır; 10-28 havuzu (12 senaryo) 12 farklı rol, kaybeden yok.
- 2026-10-27 (1929): F3 [8b] ayrıştırıcı biçim değişince "BULUNAMADI" verdi → yetkili satırdan oku. D-x eklenen cümleyi sonraki 2 cümleyle birlikte oku (kurulum → tersine dönüş katı okumayı düşürür).
- 2026-10-27: 1929 "jump" deyimi + düşüş SFX'i = atlayan bankacı klişesi; görselde düşen kişi yoksa YEŞİL, F3'te işaretle.
- 2026-11-02 (F2, 12 senaryo): 8 YEŞİL / 4 SARI / 0 KIRMIZI. Çıkar çatışması (metni yazan modelin şirketi konu) için YouTube'da kural yok → KIRMIZI'yı kaynakla destekleyemezsin; SARI-yüksek + "bu slotta önerilmez" + beyan metni + hakem tarafsızlık kontrolü yaz, kendi modelini açıkça belirt.
- 2026-11-02: Seçim sonrası günü yayın → "who won" yalnız resmi/AP çağrısına dayansın, "too close to call" yedeği zorunlu; "your money" başlığı siyaset + finans persona riskini birleştirir → "markets".
- 2026-11-02: Hassas olay (ölümlü saldırı) hook'un ilk cümlesindeyse olayı ikinci plana al, fiyatla aç; görsel/kayıp sayısı yok.
