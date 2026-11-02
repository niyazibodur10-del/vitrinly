# YAYIN — S08 "If America Earned $5,400 a Month, Here's Its Budget" (F8b — metin kesin)

**Durum:** paketler hazır, `onay.niyazi_onayi = false`. Yükleme yalnız Niyazi onayıyla (F11). Bölümler gerçek sahne zamanında (00:00 · 01:23 · 02:56 · 04:31 · 06:31 · 08:47 · 10:37; final 11:18,2), müzik atfı CC0 teşekkür satırı. **Kalan:** `08-kurgu/` final dosyaları (F7) gelince `paket-kontrol.py --final` + gerçek `--dry-run` 3/3; `politika-raporu.md` `sentetik_medya` kararı (şu an true).
**Takvim (EST, UTC−5):** uzun Çar 2026-11-04 12:00 ET (17:00 UTC, 20:00 TRT) · Shorts-1 Per 11-05 09:00 ET · Shorts-2 Cmt 11-07 09:00 ET. K3 kaçarsa: Paz 11-08 12:00 / Pzt 11-09 / Sal 11-10 09:00 ET (`paket.md` `veri:yayin-zamani` yedek satırları → `paket-uret.py`).

## Komutlar (koordinatör, Niyazi onayından sonra)
1. `python3 uretim/2026-10-28-yeni-video/09-paket/paket-kontrol.py --final` → 0 hata
2. `python3 tools/yayin/yukle.py uretim/2026-10-28-yeni-video/teslim/yayin-paketi.json` (sonra shorts-1, shorts-2)
3. Oynatma listesi "Money News, Explained" bu videoyla açılır: `tools/yayin/kanal.py` (boş liste açılmaz) → video eklenir.

## Studio adımları (API karşılığı yok / doğrulanmadı)
- **Test & Compare:** ana A1 (`09-paket/thumbnail/A1-eksi-2000.jpg`, JSON ile yüklenir) + `C1-faiz-ordu.jpg` + `B1-hesap-makinesi.jpg`, sıra A1, C1, B1. Başlık testi yalnız thumbnail testinden sonra (yedek: T4, sonra T3).
- **Altyazı:** `08-kurgu/final.en.srt` (ad F7 sonrası `ls 08-kurgu` ile teyit; paket bu adı bekler) → Studio → Altyazılar.
- **Uç ekran:** son **15 sn** (11:03–11:18, S27 gerçek ses): Abone + Video "Best for viewer".
- **Shorts Related video:** her Short'un yayın saatinden önce Studio → Short → Ayrıntılar → Related video → "If America Earned $5,400 a Month, Here's Its Budget".
- **Sabit yorum:** `paket.md` §7 metni Niyazi gönderir ve sabitler; yanıt taslakları `yorum-yanitlari.md`.
- **Kitle:** "Not made for kids" (paket `cocuklara_ozel=false`); AI beyanı paket `sentetik_medya` (monetizasyon-uyum-uzmani kararı).
