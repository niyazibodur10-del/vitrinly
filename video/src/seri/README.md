# Flip By Vote — dikey dizi şablonu (`video/src/seri/`)

Bir bölüm = **tek veri dosyası** (`bolumler/bolum-XXX.ts`) + varlıklar (`video/public/seri/bolum-XXX/`).
Çıktı 1080x1920, 30 fps, 60–90 sn. Sahibi: uretim-muhendisi (altyapı); sahne/kurgu verisi animasyon-yonetmeni + kurgu-editoru.

## Yeni bölüm (adım adım)
1. **Ses** (ses-yonetmeni): `~/.finansal-arac/kokoro-venv/bin/python tools/ses/diyalog.py <metin.txt> video/public/seri/bolum-XXX/diyalog.wav`
   (Jake `am_onyx` 0.95, Mike `am_fenrir` 1.05). Çıktı: `diyalog.wav`, `diyalog.zaman.json`, `diyalog-JAKE/MIKE.wav/.txt`.
   `diyalog.zaman.json` → `video/src/seri/bolumler/bolum-XXX.satirlar.json` olarak **olduğu gibi** kopyalanır
   (`{"sesler","sure","satirlar":[{"no","konusmaci":"JAKE","bas","bitis","metin"}]}`; `kelimeler:[{k,bas,bitis}]` opsiyonel).
   Kelime zamanı: ses-yonetmeni'nin Whisper `kelimeler.json`'u (`{"words":[{"w","s","e"}]}`) `bolum-XXX.kelimeler.json` olarak kopyalanır ve
   `satirDosyasi(satirlarJson, kelimelerJson)` ile birleşir (kelime orta noktasına göre satıra atanır). Verilmezse kelimeler satır içinde
   harf sayısına göre dağıtılır (yaklaşık).
2. **Ağız** (yalnız "yama" yolu): `python3 -I tools/seri/agiz-cue.py video/public/seri/bolum-XXX/diyalog.wav video/src/seri/bolumler/bolum-XXX.satirlar.json video/src/seri/bolumler/bolum-XXX.agiz.json`
   (satır başına Rhubarb; varsa konuşmacı izi `diyalog-<KONUSMACI>.wav` kullanılır → sızma yok). Rhubarb deterministik değil → JSON git'e girer.
3. **Görseller** `video/public/seri/bolum-XXX/` (sahne arka planları 1080x1920; ayrı karakter katmanı, ifade ve ağız yaması opsiyonel).
4. **Veri dosyası** `bolumler/bolum-XXX.ts`: `demo.ts`'yi kopyala; `id: "FBV-B0XX"`, `no`, `sure` (60–90), `sahneler` (0'dan `sure`'ye
   boşluksuz), `bank`, `ses`, `karar` (+ bölüm 2'den itibaren `kazananYorum`). Tipler: `tipler.ts` (yorumlu).
5. **Kayıt**: `bolumler/index.ts` → `BOLUMLER` listesine bir satır. Root otomatik kaydeder (Studio'da `FlipByVote` klasörü).
6. **Render**: `tools/seri-render.sh FBV-B0XX uretim/seri/bolum-XXX/final.mp4` (yayın modu, kapılı).
   Taslak/kanıt: `--taslak` (yer tutucu serbest), `--kilavuz` (güvenli alan çizgileri; yalnız taslakla). Hızlı bakış: `--onizleme`.

## Bileşenler
| Dosya | Ne yapar |
|---|---|
| `SahneKarti.tsx` | Arka plan + karakter katmanları; yavaş zoom/pan (`kamera.zoom/kay`) × konuşmacıya punch-in; sahne sınırları sert kesme. Kadraj görselin dışına taşmaz. |
| ağız yolları (`agizYolu`, bölüm veya sahne düzeyi) | **yama**: karakterin `agiz` kutusuna Rhubarb A–H/X karesi (eksik şekil en yakına düşer). **ifade**: `ifadeler` (`notr`, `konusur`, + sahne `ifadeler[]` atamaları). **kamera**: ağız yok, kamera konuşana kayar (ölçek 1,28, 0,35 sn). |
| `Altyazi.tsx` | ≤4 kelimelik öbek, kelime söylenince belirir; o anki kelime konuşmacı renginde (Jake `#4DA8FF`, Mike `#FF5A4E`) + ad hapı. |
| `BankSayaci.tsx` | Sol üst "BANK: $100"; `bank.olaylar[{t, deger}]` → 0,9 sn sayma, renk parlaması, "+$X/−$X" etiketi, ses (artış ka-ching, düşüş bozuk para; `ses:false` sessiz). |
| `Kartlar.tsx` | Açılış damgası (1,8 sn, "FLIP BY VOTE · EP. N" + logo), kazanan yorum kartı (3–5 sn, varsayılan 1,8 sn'de), karar kartı (5–8 sn, `karar.bas` ile taşınır: soru, isim+fiyat seçenekleri (harf yok, incil §5.1), "Tell us in the comments 👇", `karar.kapanis` anında "Ep. N+1: YOUR call" (gün sözü yok, §5.7)), geçici logo. |
| `../ortak/AboneOl.tsx` | Dikey takip kartı ("FOLLOW → ✓ FOLLOWING", @flipbyvote). Varsayılan: karar kartından 0,4 sn önce biter (1 kez). `abone:false` kapatır, `abone.bas` taşır. Eski kullanım piksel-aynı (2026-11-10 cmp). |
| `Bolum.tsx` | Katmanları ve sesi birleştirir: diyalog + `ses.muzik` (vars. 0,18) + `ses.sfx` stem'i + şablon efektleri (`ses.sablonSfx:false` ile kapanır — stem'de varsa çift olmasın). |

**Logo:** `Bolum.logo` yoksa geçici logo (mavi/kırmızı yarım para + ✓) kullanılır; temiz ve yayınlanabilir, yer tutucu sayılmaz. Gerçek logo gelince `logo: "seri/ortak/logo.png"`.

## Çekim çatısı (animasyon-yonetmeni 2026-11-11, bölüm 001'den itibaren)
Sahnede `cekim` alanı varsa `Cekim.tsx` çizer (yoksa eski `SahneKarti`). Çekim anahtarları: `genis` · `yakin:kim` · `portre:kim:ifade` ·
`ikiPortre` · `tahta`. Mekân + rig seti `bolumler/mekan-l1.ts` (`Bolum.mekan`): plakalar, ikili/tekli yerleşim (yerlesim.json), ağız yamaları
(3 durum), göz elipsleri. `Rig.tsx`: taban + ağız (Rhubarb → `ucDurumAgiz`, <2 kare birleşir, sınıra ortalı 2 karelik alfa karışımı) +
kodla göz kırpma (3–5 sn, 4 kare) + nefes (ölçek ≥1, alt kenara yaslı → kesik kenar içeri girmez). `Proplar.tsx` + `Ikonlar.tsx`: banknot,
ilan kartı, telefon, tahta yazısı (tik ile sıfır ekleme), köşe tahta, ikon sırası, büyük yazı. Kamera: `kamera.zoom/kay` + `vurus` (punch-in)
+ `sarsinti`. Örnek: `bolumler/bolum-001.ts` (kesme listesi tek tablo). Görsel olay çizelgesi `uretim/seri/bolum-NNN/animasyon-efekt-cue.json`
→ `uretim/seri/ses-kimligi/bolum-ses.py cevir --gorsel` (stem'deki SFX görsel olay karesine oturur).
Karar kartı: `karar.bas` / `karar.kapanis` ("Ep. N: YOUR call"); takip kartı `abone.bas/ust`; açılış damgası `damgaUst`.
Kontrol: `video/scripts/bundle-kaydet.mjs <dizin>` + `BUNDLE=<dizin> node scripts/kare-ornek.mjs` (bundle ~585 MB, disk dar).
Kapı notu: `tools/seri/kapi.py` yalnız bölüm dosyasındaki düz yolları sayar; `mekan-l1.ts` birleştirilmiş yolları denetlenmez (uretim-muhendisi'ne).

## Güvenli alan (1080x1920)
Platform arayüzü (Reels/TikTok/Shorts) üstü, altı ve sağ kenarı kapatır. Platformlar organik içerik için resmi piksel değeri yayımlamıyor;
kaynaklar farklı (arama özeti 2026-11-10: Shorts reklam şablonu üst 288 / alt 672 / sağ 192; TikTok ölçümü üst ~130 / alt ~480 / sağ ~150;
IG Reels alt ~%20–35). **Seçilen:** üst 250, alt 480 (%25), sol 60, sağ 190 → içerik kutusu x 60–890, y 250–1440 (`sabitler.ts GUVENLI`).
Bantlar: BANK y 270 · kartlar y 400–1110 · altyazı y 1150–1420. Yayından önce gerçek uygulamada bir kez önizleme önerilir.

## Kapılar
1. `tools/seri/kapi.py <Id> [--taslak]` (render'dan önce, seri-render.sh çağırır): şablon kodunda console/debugger/TODO ve ekrana çıkabilecek
   "debug/placeholder/test/lorem" yazısı; bölüm verisinde `yerTutucu` ve TODO/TBD dizgisi (yayında KALDI); veride geçen her `seri/...` varlığı mevcut mu.
2. Remotion içi `dogrula.ts` (ilk karede hata fırlatır): yayında yer tutucu (yayılımla gelen dahil), süre 60–90, karar 5–8 sn / 2–3 seçenek,
   yorum kartı 3–5 sn, satır/sahne zaman tutarlılığı, ağız yolunun gerektirdiği veri, kılavuz yasağı.
3. `seri-render.sh` çıktı kapısı: 1080x1920, 30 fps, kare sayısı = süre, h264 + aac 48 kHz, ebur128 I/TP (render-son: −14 LUFS).
Yer tutucular yalnız veride `{ yerTutucu: "blok" | "figur" | "agiz", renk }` ile işaretlenir; ekranda yazı içermez.

## Render ölçümü (2026-11-10, 4 vCPU; paralel ajan yükü vardı)
| Aday | Girdi | Süre |
|---|---|---|
| tam render c4 (**seçildi**, varsayılan) | 20 sn demo | 30,8–42,2 sn (yük 4–11) |
| tam render c2 | 20 sn demo | 37,7 sn (yük ~5) |
| tam render c4 | 90 sn demo (yer tutucu) | 118,6 sn ≈ 2,0 dk, tepe bellek ~1,6 GB |
| tam render c4 | 90 sn, gerçek 1080x1920 Canva PNG'leri (L1-A/B, T-J, T-M) | 282,5 sn ≈ 4,7 dk (yük 6→13), ~2,35 GB |
| parça render (`render-parca.sh`, 2×c2) | — | elendi: 90 sn'de tam render 10 dk sınırının çok altında; önceki ölçümde kazanç −%7 (hafıza) |

## Demo
`FBV-Demo` (20 sn; S1 yama, S2 ifade, S3 kamera; kazanan yorum + BANK 100→85 + takip + karar) ve `FBV-Demo90` (ölçüm; 17 sn blok ×5,
ses `diyalog90.wav` = `diyalog.wav` 17 sn'ye doldurulup 5 kez). Sesi yeniden üret: `demo.ts` başlığı. Yayın kapısı ikisini de reddeder (beklenen).
