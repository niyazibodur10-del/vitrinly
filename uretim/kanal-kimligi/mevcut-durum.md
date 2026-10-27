# Kanalın mevcut durumu (API ile okundu, 2026-10-26, koordinatör)

- Ad: **Financial Rise** · tanıtıcı: **@finansialrise** (yazım: "finansial", s ile) · hesap 2013-09-11 · ülke TR · varsayılan dil yok
- İstatistik: 2 abone, 48 görüntüleme, 4 video · uzun yükleme izni: allowed · para kazanma: kapalı · çocuklara özel değil
- Oynatma listesi: yok · banner: var (eski)
- Anahtar kelimeler (eski): wealth stories, financial freedom, billionaire mindset, rags to riches, how to get rich, passive income, secret millionaires …
- Açıklama (eski, özet): "real stories of wealth, success, and financial freedom … self-made millionaires, janitors who died rich … New videos every week."

## Yayındaki eski videolar (hepsi public, 2025-07)
| id | süre | izlenme | başlık |
|---|---|---|---|
| Xc4WFq4HEnY | 1:47 | 26 | The Janitor Who Secretly Died a Millionaire  Ronald Read's Shocking Story |
| uAzvo7kCbg4 | 2:25 | 7 | She Was Just a Teacher... But She Died a Multi-Millionaire  Grace Walker's True Story |
| TKAthZZZ71k | 2:19 | 10 | Compound Interest: The Quiet Force That Builds Millionaires \| Start Now |
| wt7aEJ5YvRE | 4:02 | 5 | Chris Gardner's Unbelievable Journey – From Homeless Father to Wall Street Legend |

API ile değiştirilebilir: açıklama, anahtar kelimeler, ülke, varsayılan dil, banner (channelBanners.insert, ≥2048x1152, ≤6 MB, 16:9), kanal fragmanı, oynatma listeleri.
API ile değiştirilemez: profil fotoğrafı, kanal adı, @tanıtıcı (Studio).

## Uygulandı (2026-10-26, Niyazi talimatı "ayarların tamamını sen yap")
- Açıklama (905 karakter, kanal-paketi.json), anahtar kelimeler (25 ifade), varsayılan dil `en` → channels.update ✅ (API okumasında ~15 sn sonra göründü).
- Ülke **TR** bırakıldı: YPP uygunluğu kanal ülkesine bağlı ve içerik üreticinin programın açık olduğu ülkede yaşaması şart (support.google.com/youtube/answer/2976814, answer/72851). Videolarda coğrafi kısıt yok → küresel yayın; reklam geliri izleyicinin ülkesine göre.
- Oynatma listeleri: ilgili ilk video yüklenince açılacak (boş liste yok). Banner: görsel hazır olunca. Eski 4 video: Niyazi kararı bekleniyor (öneri gizli).
- Eski 4 video **gizliye alındı** (Niyazi onayı 2026-10-26, videos.update status.privacyStatus=private; kontrol okumasında 4/4 private). Geri almak: Studio'da görünürlük → Herkese açık.
- **Ad değişti:** Toonomy · @toonomy (Niyazi, Studio). Maskot: Leo. Açıklama + anahtar kelimeler Toonomy/Leo ile güncellendi; **banner yüklendi** (TOONOMY, "NEW VIDEOS EVERY WEEK"; bannerExternalUrl yenilendi). Profil fotoğrafı (`profil-800.png`) Niyazi Studio'dan yükleyecek.
- 2026-10-27: Hakkında'ya "Researched, written and produced by the Toonomy team." eklendi (hakem ŞY-1, Ö9), API ile uygulandı.
