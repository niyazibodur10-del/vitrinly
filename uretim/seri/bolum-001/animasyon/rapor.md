# Bölüm 001 animasyon + senkron raporu (animasyon-yonetmeni, 2026-11-11)
İLERLEME: tamam · **SONUÇ: GEÇTİ** — `teslim/bolum-001.mp4` sha256 8588a182aeba, 1080x1920, 30 fps, 2550 kare = 85,00 sn, h264+aac 48 kHz.
| Kapı | Komut → sonuç |
|---|---|
| Şablon kapısı (yer tutucu/hata ayıklama 0) | `tools/seri-render.sh FBV-B001 …` → kapı GEÇTİ, çıktı kapısı GEÇTİ, I −14,0 LUFS / TP −2,5 dBTP |
| Süre 60–90 | 85,0 sn (diyalog 78,77 + karar kartı + sonda takip kartı) |
| Siyah / donmuş kare | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=1` → 0 / 0 |
| Ağız-ses (PİKSEL, render'ın kendi sesi) | `animasyon/agiz-piksel-senkron.py teslim/bolum-001.mp4 animasyon/aralik-tam.json` → 15 yakın çekim, 1189 kare, gecikme **0 kare**, r 0,58 |
| Ağız-ses (Rhubarb çizelgesi) | `tools/senkron-testi.py … rhubarb/{JAKE,MIKE}.json --bant 700-3000` → +1 / +1 kare GEÇTİ |
| Kritik yol testi | `kanit/test-15sn.mp4` (0–15 sn, 2 konuşmacı + ağız + altyazı + tahta) → piksel gecikme 0, blackdetect 0 |
| 20 rastgele kare | `kanit/kontak-rastgele20.jpg` (seed 20261111; kareler `kanit/rastgele/kareler.txt`): dikiş 0, açık kesik kenar 0, altyazı güvenli alanda (y ≤1440, x ≤890) 20/20, BANK $100 20/20 |
| Ağız seti | `kanit/agiz-test.jpg` (kapalı/yarı/açık × 2); <2 kare cue: Jake 9→0, Mike 11→0 (`kanit/agiz-test.json`) |

## Ne yapıldı
- Çekim çatısı (`video/src/seri/Cekim.tsx`, `Rig.tsx`, `Proplar.tsx`, `Ikonlar.tsx`, `bolumler/mekan-l1.ts`): kesme listesi tek tabloda (`bolum-001.ts`, 34 kesme, ort. 2,5 sn).
- Ağız: Rhubarb → 3 durum, <2 kare cue öncekine katılır, durum sınırına ortalı 2 karelik alfa karışımı (gecikme yok).
- Göz kırpma: kodla badem biçimli ten kapak + kirpik kavisi, kişi başına 3–5 sn, 4 kare (0,55/1/0,9/0,45); elipsler `animasyon/goz-kapak-olc.py`.
- J06 gag: ses kilitli → "Tires aren't." sert punch-in (×1,24, 0,08 sn) + satır sonrası 0,27 sn Jake tutuşu + 0,4 sn Mike endişeli portre.
- Kapanış: karar kartı 74,45–81,45 (soru, isim+fiyat seçenekleri, harf yok, "Tell us in the comments 👇"), 78,59'da ikili kameraya bakış + "Ep. 2: YOUR call"; takip kartı 81,5–85,0 (tek kez, kartla çakışmaz).
- Şablon düzeltmesi: karar kartındaki A/B/C harfleri (incil §5.1) ve "Ep. N drops tomorrow" (incil §5.7) kaldırıldı.
- Görsel olay çizelgesi `animasyon-efekt-cue.json` (30 SFX olayı + 1 abone + 33 kesme, kare doğru) → `bolum-ses.py cevir --gorsel … --sure 85` + `miks` ile stem'ler yenilendi (muzik-ses-tasarimcisi'nin aracı, parametre dışında değişiklik yok).

## Elenenler
- Göz kapağı v1 (maskeden PNG yama): maske kutu sınırına taştı, düz renk "boş göz" → elendi. v2 SVG elips: yapıştırma gibi → elendi. v3 badem + kirpik kavisi, kapalıda tam dolgu → seçildi.
- Takip kartı varsayılan yer (karar kartından önce, 70,6 sn): imza repliğinin (J12) üstüne biniyordu → sona alındı.
- "Kare donar" (metin): freezedetect düşürür → donma yerine %5 itme + nefes + göz kırpma.
- Sabit "You do" anında portreye kesme: portrede ağız oynamaz → YOU DECIDE yazısı "You"da, portre satır bitince (sessiz).

## Yeniden üretim
`cp uretim/seri/bolum-001/ses/bolum-001.wav video/public/seri/bolum-001/diyalog.wav` (sha 289da660bbd0) → stem: `cd uretim/seri/bolum-001 && python3 ../ses-kimligi/bolum-ses.py cevir ses-cue.json ses/bolum-001.zaman.json veri/satirlar.py --kelimeler ses/kelimeler.json --sure 85 --karar-sure 7 --gorsel animasyon-efekt-cue.json -o ses-cue.mutlak.json && ~/.finansal-arac/earshot-venv/bin/python ../ses-kimligi/bolum-ses.py miks ses-cue.mutlak.json ses/bolum-001.wav ses-miks` → stem'leri `video/public/seri/bolum-001/`'e kopyala → `tools/seri-render.sh FBV-B001 uretim/seri/bolum-001/teslim/bolum-001.mp4` (≈3,3 dk).
