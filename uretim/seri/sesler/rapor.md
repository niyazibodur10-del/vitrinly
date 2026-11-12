# Flip By Vote — karakter sesleri seçimi (ses-yonetmeni, 2026-11-10)

İLERLEME: tamam
**KARAR:** Jake Miller = Kokoro `am_onyx` hız **0.95** · Mike Carter = Kokoro `am_fenrir` hız **1.05** (Kokoro-82M, Apache-2.0, yerel, ücretsiz).
**Kapılar (test-diyalog.wav, sha256 497442c509f2):** ayrışma **9,0 yarım ton** (Jake 91 Hz / Mike 153 Hz) + tını merkezi 1.301 / 2.581 Hz · Whisper satır WER **%0** (kapı ≤%10) · −14,1 LUFS, TP −1,5 dBTP · 23,8 sn / 6 replik.
**Neden:** 9 çift içinde en büyük ayrışma (perde VE tını), WER 0; karakter haritasına uyuyor: Jake koyu, düz (F0 std 2,0 yt = sakin), 161 kpm; Mike parlak, dalgalı (4,0 yt = enerjik), 199 kpm (aceleci).
**Kör dinleme (Niyazi, model adı gizli):** `kor/A.m4a`, `kor/B.m4a`, `kor/C.m4a` — ilk 3 çift; anahtar bu dosyanın en altında. Niyazi farklı seçerse araçta tek parametre değişir.
**Araç:** `tools/ses/diyalog.py` (kullanım aşağıda). Test diyaloğu: `test-diyalog.txt` → `test-diyalog.wav` (+ `.m4a`, `.zaman.json`, `-JAKE/-MIKE.wav/.txt`).
**Risk:** am_onyx Kokoro VOICES.md'de düşük notlu (D) — ölçümde sorun yok (Whisper güveni 0,965, hata 0) ama doğallık kararı Niyazi'nin kör dinlemesinde. Yedek çift: B (am_echo 0.92 + am_fenrir 1.05).

## Aday tablosu (aynı 6 replik; ölçüm `olc.py`, sonuçlar `olcum.json`)
Lisans: Kokoro-82M Apache-2.0 — https://huggingface.co/hexgrad/Kokoro-82M (hafıza: doğrulandı 2026-10-26). Ses dosyaları aynı depoda (`voices/am_*.pt`).

| Çift | Jake (F0 · std · merkez · kpm) | Mike (F0 · std · merkez · kpm) | Ayrışma | WER | Süre | Not |
|---|---|---|---|---|---|---|
| J1-M1 | michael 0.92 · 121 Hz · 3,1 · 2671 · 157 | fenrir 1.05 · 154 · 3,9 · 2572 · 199 | 4,2 yt | 0 | 24,1 | tını merkezi neredeyse aynı → C |
| J1-M2 | michael 0.92 | eric 1.08 · 162 · 3,5 · 1708 · 193 | 5,0 | 1,6 | 24,4 | eric "and→in" |
| J1-M3 | michael 0.92 | puck 1.08 · 127 · 2,6 · 2417 · 207 | **0,8** | 0 | 23,7 | iki ses neredeyse aynı perde |
| J2-M1 | echo 0.92 · 119 · 3,8 · 2243 · 152 | fenrir 1.05 | 4,4 | 0 | 24,5 | yedek → B |
| J2-M2 | echo 0.92 | eric 1.08 | 5,3 | 1,6 | 24,8 | eric "flip it→flip in" |
| J2-M3 | echo 0.92 | puck 1.08 | 1,1 | 0 | 24,2 | ayrışma yetersiz |
| **J3-M1** | **onyx 0.95 · 91 · 2,0 · 1301 · 161** | **fenrir 1.05 · 153 · 3,9 · 2578 · 199** | **9,1** | **0** | 23,8 | **kazanan → A** |
| J3-M2 | onyx 0.95 | eric 1.08 | 10,0 | 1,6 | 24,1 | eric telaffuz |
| J3-M3 | onyx 0.95 | puck 1.08 | 5,9 | 0 | 23,4 | puck 207 kpm, düz (2,6 yt) |

Ayrışma = |12·log2(F0_Mike/F0_Jake)|; merkez = spektral ağırlık merkezi (Hz, tını parlaklığı). WER = satır satır Whisper small.en, `hata-orani.py` normu (çift WER'i 6 satır toplamı, 65 kelime; 1 hata = %1,6 normalize sayımda). Tüm çiftler −13,9…−14,2 LUFS, TP −1,5.

## Elenenler (tek satır)
- **am_eric (M2):** 3 çiftin 2'sinde telaffuz hatası (and→in, flip it→flip in) — "aceleci" Mike için en riskli ses.
- **am_puck (M3):** michael/echo ile 0,8–1,1 yt (ayırt edilemez); onyx ile de 207 kpm + düz tonlama (2,6 yt), enerji fenrir'den düşük.
- **am_michael (J1):** fenrir ile tını merkezi aynı bant (2671 / 2572 Hz) — eski anlatıcı çifti, perde farkı 4,2 yt'de kaldı.
- **am_echo (J2):** geçerli yedek; ayrışma 4,4 yt, onyx'in yarısı.
- Ön tarama (`tarama/`, hız 1.0): am_adam düşük değişkenlik (1,4 yt Mike satırında) ve VOICES.md en düşük not → aday dışı; am_liam fenrir'e çok yakın (146 Hz, merkez 1993) → fenrir'in yedeği sayıldı, denenmedi.

## Ek testler (kazanan)
- **Tutarlılık** (aynı replik 3 kez, `tarama/tut-*`): onyx 88,2–88,3 Hz, 4,40 sn ×3; fenrir 144,4–144,8 Hz, 2,95 sn ×3.
- **Whisper kelime güveni** (konuşmacı izi, small.en): onyx 0,965 · echo 0,973 · michael 0,976 · fenrir 0,907 (düşük p: "100", "and" — metin doğru). İzlerin sonunda "What?/thanks for watching" Whisper'ın sessizlik uydurması (bilinen), ses hatası değil.
- **Araç determinizmi** (2 koşu): satır zamanları en çok 9 ms, süre 23,815 / 23,806 sn — Kokoro'nun bilinen küçük belirsizliği; bölüm sesi bir kez üretilip kilitlenir.
- **İz doğruluğu:** JAKE+MIKE izleri ana dosyayla aynı uzunlukta, çakışan örnek 0, toplam − ana ≤ 0,0011 (10 ms rampa kenarları).
- **Rhubarb** (JAKE izi 16 kHz + `--dialogFile`): 73 ağız işareti, 4,8 sn; Mike satırları boyunca Jake'te X dışı işaret 0 → karakter başına ayrı dudak senkronu çalışıyor.

## Araç: `tools/ses/diyalog.py`
```
~/.finansal-arac/kokoro-venv/bin/python tools/ses/diyalog.py bolum.txt 04-ses/diyalog.wav
   [--ses JAKE=am_onyx:0.95 --ses MIKE=am_fenrir:1.05] [--bosluk JAKE=0.42 --bosluk MIKE=0.22] [--ham]
```
- Girdi: `JAKE: metin` / `MIKE: metin` satırları; `MIKE (0.1): …` o satırdan önceki boşluğu elle verir (lafı kesme, uzun sessizlik). `#` yorum. misaki işareti `[kelime](/IPA/)` geçerli, JSON/txt'de düz yazıya döner. Yeni karakter: `--ses AD=am_x:1.0`.
- Çıkış: `diyalog.wav` (48 kHz mono 24-bit, −14 LUFS, TP ≤−1,5; `tts-son.sh` zinciri) · `diyalog.zaman.json` (`satirlar: no, konusmaci, bas, bitis, metin`) · `diyalog-JAKE.wav` / `-MIKE.wav` (aynı uzunluk, öteki sessiz → Rhubarb) · `diyalog-JAKE.txt` / `-MIKE.txt` (Rhubarb `--dialogFile`).
- Boşluk (sahne yönetimi): Jake yanıtlarken 0,42 sn (düşünür), Mike yanıtlarken 0,22 sn (lafı kapar), aynı konuşmacı 0,45, satır içi cümle 0,28 / !? sonrası 0,32, baş 0,15 son 0,30.
- Seviye: konuşmacıların etkin RMS'i eşitlenir (onyx/fenrir farkı ±1,2 dB), sonra tek zincir. RNNoise/`temizle.sh` TTS'te kullanılmaz (temiz kaynakta artefakt).
- Hız: 6 replik ~17 sn (4 vCPU). 90 sn'lik bölüm ≈ 1 dk.

## Bölüm uzunluğu notu (senaryo-yazari'ya)
Test diyaloğu: 65 kelime → 23,8 sn = **164 kpm toplam** (boşluklar dahil). 60–90 sn bölüm ≈ **165–245 kelime** diyalog (anlatıcı/efekt payı ayrıca).

## Yeniden üretim (wav'lar git dışı)
```
cd uretim/seri/sesler; P=~/.finansal-arac/kokoro-venv/bin/python
$P ../../../tools/ses/diyalog.py test-diyalog.txt test-diyalog.wav
# adaylar: --ses JAKE=<am_michael:0.92|am_echo:0.92|am_onyx:0.95> --ses MIKE=<am_fenrir:1.05|am_eric:1.08|am_puck:1.08> → aday/Jx-My.wav
~/.finansal-arac/venv/bin/python olc.py aday/J?-M?.wav   # → olcum.json (~2 dk)
```

## Kör dinleme anahtarı (Niyazi dinlemeden önce açmasın)
A = J3-M1 (onyx 0.95 + fenrir 1.05) · B = J2-M1 (echo 0.92 + fenrir 1.05) · C = J1-M1 (michael 0.92 + fenrir 1.05)
