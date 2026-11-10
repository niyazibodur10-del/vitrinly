# YAYIN — S03 "The Great Wealth Transfer Has a Leak" (F8b final, 2026-11-10)

**Durum:** paketler final, üçünde de `onay.niyazi_onayi = false`. Yükleme yalnız Niyazi onayıyla (F11). F7 GEÇTİ (48d36ff): final 781,40 sn, Shorts 41,45 / 43,43 sn. Bölümler 00:00 · 01:46 · 02:35 · 04:58 · 07:09 · 08:13 · 10:42 (kurgu ofseti 0, betik 7/7). `sentetik_medya: true` (politika-raporu.md). `paket-kontrol.py --final` 0 hata; `yukle.py --dry-run` 3/3 0 hata.
**Takvim (EST, UTC−5):** uzun **Çar 2026-11-11 12:00 ET** (17:00 UTC, 20:00 TRT) · Shorts-1 **Per 11-12 09:00 ET** (14:00 UTC) · Shorts-2 **Cmt 11-14 09:00 ET** (14:00 UTC). Paz 11-08 slotu kaçtı (K3, B slotu yerine).

## Komutlar (koordinatör, Niyazi onayından sonra)
1. `python3 uretim/2026-11-04-miras-sizintilari/09-paket/paket-kontrol.py --final` → 0 hata.
2. Liste: "What If…? Future of Money Scenarios" bu videoyla açılır (`tools/yayin/kanal.py`, boş liste açılmaz). Açılmadan önce liste açıklamasındaki "every other Sunday" gün sözü düzeltilmeli.
3. Yükleme, listeye ekleme açılış SONRASINA ertelenmiş olarak:
   `python3 tools/yayin/yukle.py uretim/2026-11-04-miras-sizintilari/teslim/yayin-paketi.json --liste-sonra <WHAT_IF_LISTE_ID>`
   (sonra `yayin-paketi-shorts-1.json` ve `-shorts-2.json`, `--liste-sonra <SHORTS_LISTE_ID>`)
4. Bekçi `tools/yayin/yayin-kontrol.py <teslim/yayin-sonucu.txt>`, her video için 3 kez (koordinatör zamanlar):
   - **yükleme +1 sa:** private + publishAt plana eşit mi
   - **açılış −2 sa:** hâlâ private + publishAt doğru mu (erken public / plan silinmesi = KALDI → koordinatör Niyazi'ye)
   - **açılış +15 dk:** public mi + `--liste-ekle <LISTE_ID> <VIDEO_ID>`
   Uzun: yükleme +1 sa · 11-11 15:00Z · 11-11 17:15Z — Shorts-1: yükleme +1 sa · 11-12 12:00Z · 11-12 14:15Z — Shorts-2: yükleme +1 sa · 11-14 12:00Z · 11-14 14:15Z.

## Yayın sırası kuralı (teşhis §3: 2/2 uzun video erken açıldı)
1. **Planlı videonun görünürlüğüne veya yayın zamanına Studio'dan dokunulmaz.** Plan (private + publishAt) paketle yüklenir; değişiklik gerekirse koordinatör araçla yapar.
2. **Test & Compare ve sabit yorum yalnız video yayına çıktıktan sonra** yapılır (Test & Compare private videoda çalışmaz; denemek görünürlüğü değiştirebilir).
3. **Shorts Related video, Short yayına çıkmadan önce** ve uzun video yayına çıktıktan sonra yapılır.
4. Liste eklemesi `--liste-sonra` ile açılış +15 dk'da bekçi yapar; Studio'dan elle eklenmez.

## Studio adımları (Niyazi), kurala göre sıralı

**Açılıştan ÖNCE (planlıyken yapılabilir):**
- **Altyazı:** `08-kurgu/final.en.srt` (296 blok, F7 teyitli) → Studio → Altyazılar. Görünürlük alanına dokunmadan.
- **Kitle:** "Not made for kids" pakette (`cocuklara_ozel=false`), kontrol yeter.

**ZORUNLU, her Short açılmadan ÖNCE (Shorts-1 için 11-12 14:00Z'den önce, Shorts-2 için 11-14 14:00Z'den önce; uzun video 11-11 17:00Z'de açıldıktan sonra):**
- **Shorts Related video:** Studio → İçerik → Shorts → Short → Ayrıntılar → **Related video** → "The Great Wealth Transfer Has a Leak". Data API'de karşılığı yok (paketlerde `ilgili_video` alanı bunu taşır). **Ekran görüntüsünü koordinatöre gönder** → `durum.md`'ye işlenir. Bu yapılmadan Short açılmamalı; geç kalırsa koordinatör Short'un planını kaydırır (Niyazi değil).

**Açılıştan SONRA (uzun video public olduktan sonra, 11-11 17:00Z+):**
- **Test & Compare:** ana K1 (`09-paket/thumbnail/K1-who-gets-it.jpg`, JSON ile yüklenir) + `K4-keeps-leaking.jpg` + `K3-smaller-later.jpg`, sıra **K1, K4, K3**. Özellik private videoda çalışmaz; açılıştan önce denenmez. Başlık testi yalnız thumbnail testinden sonra (yedek başlık sırası T3, T7).
- **Uç ekran:** **12:55–13:01 (son 6 sn; ABONE-4 kartı 12:55,3'te biter, üstüne binmez)**: Abone + Video **"You Have $1,000 in 1929. Can You Keep It?" (BVJwZ1C9R1U)**. S08 gösterilmez.
- **Sabit yorum:** `paket.md` §7 metnini Niyazi gönderir ve sabitler. İlk 24 saatte yorumlara yanıt (`yorum-yanitlari.md`, her yanıtı Niyazi onaylar ve gönderir).
- **Kontrol:** bölümler görünüyor, altyazı İngilizce, uç ekran doğru videoyu gösteriyor, video listede (bekçi +15 dk).
