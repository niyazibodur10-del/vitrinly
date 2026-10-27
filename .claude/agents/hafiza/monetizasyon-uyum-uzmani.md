# monetizasyon-uyum-uzmani — hafıza

## Kurallar
- Kaynaklı politika gerçekleri (erişim 2026-10-26):
  - YPP eşiği: 1.000 abone + son 12 ayda 4.000 geçerli izlenme saati (herkese açık uzun videolar; Shorts akışı saatleri sayılmaz) VEYA 1.000 abone + son 90 günde 10 milyon geçerli Shorts izlenmesi. Ek şartlar: aktif topluluk kuralı ihtarı yok, 2 adımlı doğrulama açık, bağlı AdSense hesabı. 6 ay yükleme/gönderi yoksa para kazanma kapatılabilir. (support.google.com/youtube/answer/72851)
  - 2025-07-15: "repetitious content" → "inauthentic content"; tekrarlayan veya seri üretim (mass-produced) içerik para kazanamaz. Örnekler: karakterlerin tekrar tekrar aynı durumda aynı sonuca vardığı videolar; anlatı/yorum/eğitim değeri olmayan slayt gösterisi, şablon hikâye. Aynı giriş/çıkış serbest, içeriğin çoğu farklıysa. AI ile "kendi icat ettiğin özgün karakteri ve anlatıyı görselleştirmek" izinli örnek. (answer/1311392)
  - AI personası: kendini insan uzman gibi sunup finans/sağlık/hukuk tavsiyesi veren içerik para kazanamaz → maskot tavsiye vermez. (answer/1311392)
  - Reklam dostu kategoriler: uygunsuz dil, şiddet, yetişkin, sarsıcı içerik, zararlı eylem ve güvenilmez içerik, nefret, uyuşturucu, ateşli silah, tartışmalı konular, hassas olaylar, sahtekârlığı kolaylaştırma, çocuk/aile için uygunsuz, tütün, kışkırtıcı/aşağılayıcı. (answer/6162278)

## Dersler
- 2026-10-26: Ajan işe alındı (ik-direktoru kadro denetimi). İlk iş: `docs/monetizasyon.md` paralel araştırma ajanınca yazılıyor; bittiğinde okuyup bu hafızadaki kaynaklı gerçeklerle karşılaştır, çelişki varsa birincil kaynağı yeniden aç.
- 2026-10-27 (F2 ön tarama, 11 senaryo, ilk herkese açık video): `docs/monetizasyon.md` ile birincil sayfalar (1311392, 14328491, 6162278) bugün yeniden açıldı → çelişki yok. Sonuç 5 YEŞİL / 6 SARI / 0 KIRMIZI. Ölçüm betiği `uretim/2026-10-26-secim/02-senaryo/politika-tarama.py` (yayın metni çıkarır; tavsiye/hassas/gerçek kişi desenleri + pilota ve senaryolar arası 5-gram). Sonraki F2'lerde yeniden kullan; iki koşu diff.
- Ders: Betik yalnız tırnak içi İngilizce metni görür; asıl riskler Türkçe yapı satırlarında ve karakter anı notlarında çıktı (S05 savaş bağlamı, S06 "GOOD COMPANY + GOOD PRICE" notu, S11 "DO NOT TOUCH"). Her zaman elle ikinci geçiş yap; karakterin ekrana yazdığı not/levha metni de "tavsiye dili" taramasına girer.
- Ders: AI personası için en sık sızıntı "Leo'nun bugüne dönük kuralı" (I believe now…, picked wrong, cash loses today). Düzeltme kalıbı: emir/kural → betimleyici tarih cümlesi ("That's arithmetic, not a recommendation"; "≠" notu). "Uyarı ekle" düzeltmesi önerme: 1311392 AI persona bölümünde izinli örnek yok.
- Ders: Meta veri riski metin riskinden ayrı puanlanır (6162278 "all portions" — başlık/thumbnail). Weimar + "who got rich" (nefret kalıbı), "ALL the silver" (doğrulanmamış pay), "heist" (gerçek kişiye suç çağrışımı) metin temizken bile SARI.
- Kanal kuralı adayı: ilk 5 videoda "çöküş + Leo kaybeder" tekrarlanmasın (1311392 "disturbing themes (violence or loss)" + "same situation same outcome"); 5 videolık denetimde Leo sonuç tipi sayılacak.
