# Bölüm 001 paket raporu (youtube-paketleyici, 2026-11-11)
İLERLEME: tamam · **SONUÇ: GEÇTİ**
| Kapı | Komut → sonuç |
|---|---|
| Paket kapısı (politika satırları birebir ×4, yasak kalıp, sınırlar, kanal.py dogrula) | `python3 uretim/seri/bolum-001/paket/paket-uret.py` → 0 hata; negatif test (satır eksik + "drops tomorrow" + 61 krk) 4/4 yakalandı |
| YouTube dry-run | `python3 tools/yayin/yukle.py uretim/seri/bolum-001/teslim/yayin-paketi.json --dry-run` → 0 hata, 1 uyarı (yayin_zamani yok = yer tutucu); planlı kopya (12:00 ET) → 0 hata, publishAt 17:00Z |
| Kapak determinizmi | `kapak.py bolum-001.mp4 81.6 20 860 … --olcek 1.12` 2 koşu → sha256 5ef165ca582b aynı; video sha256 8588a182aeba |
| Kapak güvenli alanı | metin alt sınırı 1597 ≤ 1615 (4:5 y 285–1635; 3:4 y 240–1680 kapsar); 200 px ızgara önizlemesinde "$100 → $1,000,000" okunur |

## Adaylar ve eleme
**Başlık (YouTube Shorts, ≤60):**
1. ✔ `$100 to $1,000,000 — You Make Every Move · Ep. 1` (48 krk, sonuç). Kapakla aynı vaat. Politika §7.4 YEŞİL. Seri kimliği bölümden bölüme taşınıyor.
2. `Bike, Dresser, or Mystery Box? You Pick Our First Flip` (54, merak). Güçlü ama yalnız bu bölüme ait; IG/TikTok ilk satırına taşındı.
3. `Two Friends. $100. You Decide Everything. (Ep. 1)` (49). Yedek / A-B.
4. ✘ `We Have $100. You Decide How We Get to $1M` (karşıtlık). "We" gerçek kişilerin gerçek denemesi gibi okunuyor; kurguyu gizleyen aldatıcı başlık riski var (B-1). Elendi.
5. ✘ `$100, Three Flips, Zero Say: You Call It · Ep. 1`. Belirsiz, aranan ifade yok. Elendi.

**Kapak karesi:**
- ✔ **D (81,6 sn):** ikili portre, kameraya bakış. Mike sırıtıyor, Jake elini çenesine koymuş, ikisi zıt duyguda. Kart yok, aydınlık.
- A (79,0): aynı poz, ama karar kartının karartması yüzleri soluk bırakıyor. Elendi.
- B (62,95): geniş plan, banknot görünüyor; yüzler 200 px ızgarada çok küçük kalıyor. Elendi.
- C (0,4): kanal damgası ile kendi yazımız çakışıyor. Elendi.

**Açıklama ilk satırı:** YouTube'da durum cümlesi ("Jake & Mike start with $100…") kullanıldı: kurgu karakterleri ilk 10 kelimede adıyla geçiyor. IG/TikTok'ta merak sorusu kullanıldı. Soru videodakiyle birebir (B01 + B02, betik `bolum.txt`'de arıyor).

## Kararlar
- Kategori 24 Entertainment: kurgu dizi, eğitim videosu değil.
- `sentetik_medya=true`: politika-format.md §3 ("altered/synthetic = Yes" önerisi). Kararı monetizasyon-uyum-uzmani verdi, ben yalnız uyguladım.
- made for kids false, dil en, onay false.
- Shorts paketinde thumbnail yok. yukle.py 1280x720 istiyor; Shorts'ta özel kapak API'den doğrulanmadı.
- Profil önerisi: `GeciciLogo` (Kartlar.tsx) 800 px'e çevrildi (`profil.py`). Videodaki takip kartının avatarıyla aynı.

## Risk
1. Yayın saati [T]: kanal verisi yok. 7 bölümde kanal-analisti verisiyle bakılmalı.
2. Bölüm 2 üretimi 24 saatlik pencereyle aynı saate yetişmeyebilir; takvim kararı koordinatörde.
3. Banner görseli yok, yalnız metni hazır. Eski TOONOMY banner'ı kaldırılmalı.

## Yeniden üretim
`python3 uretim/seri/bolum-001/paket/paket-uret.py && python3 uretim/seri/bolum-001/paket/kapak.py uretim/seri/bolum-001/teslim/bolum-001.mp4 81.6 20 860 uretim/seri/bolum-001/teslim/kapak --olcek 1.12 && python3 uretim/seri/bolum-001/paket/profil.py uretim/kanal-kimligi/flipbyvote-profil-800.png`
