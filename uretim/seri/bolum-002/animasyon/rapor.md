# Bölüm 002 animasyon + senkron raporu (animasyon-yonetmeni, 2026-11-12)
İLERLEME: tamam · **SONUÇ: GEÇTİ** — `teslim/bolum-002.mp4` sha256 **8ba870ac5b0e**, 88,27 sn (88,25 hedef, kare yuvarlama), 1080x1920 30 fps, I −14,0 LUFS / TP −2,6.
| Kapı | Komut → sonuç |
|---|---|
| Yayın + çıktı kapısı | `tools/seri-render.sh FBV-B002 … --public-dir=<symlink dizini>` → GEÇTİ (yer tutucu/hata ayıklama 0) |
| Süre 60–90 | 88,27 sn (diyalog 85,07 + takip kartı) |
| Siyah / donma | `blackdetect d=0.1` + `freezedetect -60dB d=0.5` → 0 / 0 |
| Ağız-ses (piksel) | `../bolum-001/animasyon/agiz-piksel-senkron.py teslim/bolum-002.mp4 animasyon/aralik-tam.json` → 14 yakın (L1+L3), 930 kare, gecikme **0**, r 0,57 · Rhubarb `senkron-testi.py` +1/+1 |
| Altyazı Z1 | `animasyon/altyazi-z1-testi.ts` → **29/29** satır ekran = kilitli metin |
| 20 rastgele kare | `kanit/kontak-rastgele20.jpg`: dikiş 0, açık kesik kenar 0, altyazı güvenli alanda 20/20, BANK metinle aynı ($100 → $40 "Sixty" 10,74 → $24 "each" 30,22) |
| Kapanış 1:1 | `kanit/kapanis-85.33-*-1e1.png`, `takip-87.33-*`: saç kenarı temiz; BANK rozeti yalnız saç üstünde (Z4) |

- Kanca K1: kare 0'da Mike yakın + Brenda sağdan yuvarlanır (kamera out eğrisiyle hareketli), üst bantta önceki seçim (BIKE ✓ "picked"te, oy rozeti yok) + ilerleme şeridi 0–3 sn; "BRENDA" etiketi 2,5 sn. Açılış damgası kapalı (bölüm 2+ kuralı).
- Yeniden kancalar: 24,0 PAT (şaşkın portre + sarsıntı) · 47,95 L3 mekân + saat 2:00→2:45 PM · 58,45 "$90 cash, today?" · 78,4 yazıyor….
- Kapanış: karar kartı 81,0–86,0 ("Take" öncesi boşlukta girer), 84,9 ikili portre + "Ep. 3: YOUR call", takip kartı (yeni profil resmi) 86,05–88,25.
- Z2: kırpma kancada ve yüz ölçeği ≥1,15 çekimde kapalı (Cekim.tsx kapısı). Yeni kod: `tur:"bos"` çekim, sahne başına mekân (`mekan-l3.ts`), prop'lar `nesne` (bisiklet + teker halkası + isim etiketi), `oncekiSecim`, `cip`, `mesaj`; ikon pompa/iç lastik/donut; `damga:false`.
- Stem: `ses-cue.json` (B001 ses kimliği aynen; taslağı ben yazdım, sahibi muzik-ses-tasarimcisi) + `animasyon-efekt-cue.json` (35 olay, 34 kesme, 1 abone) → `bolum-ses.py cevir --sure 88.25 --karar-sure 5 --gorsel` + `miks`. Kütüphanede "flap/pşş/PAT" yok: kutu-tikirti / whoosh-kisa / tezgah-carpma+plak-cizik kullanıldı.
- **Kapak önerisi: 86,00 sn = kare 2580** (`kanit/kapak-onerisi-86.00.png`): karar kartı çıkmış, takip kartı henüz yok, ikisi kameraya. Alternatif kanca karesi 0,5 sn (`kanit/kanca-0.50.png`).
- Disk: render `--public-dir` ile yalnız seri varlıklarının symlink dizininden (bundle 600 MB → 40 MB). Yeniden üretim: `P=/tmp/pub; mkdir -p $P/seri; ln -s $PWD/video/public/fonts $P/fonts; for d in ortak bolum-001 bolum-002; do ln -s $PWD/video/public/seri/$d $P/seri/$d; done; tools/seri-render.sh FBV-B002 uretim/seri/bolum-002/teslim/bolum-002.mp4 --public-dir=$P` (önce stem: yukarıdaki cevir+miks, kopyala `video/public/seri/bolum-002/`).
