> **GEÇERSİZ (2026-11-11):** Kokoro kilidi. Bölüm sesi Pocket TTS (JAKE george, MIKE marius) ile yeniden üretildi; yerini `kilit.json` aldı.

# Bölüm 001 ses kilidi (ses-yonetmeni, 2026-11-10)
İLERLEME: tamam · **KİLİTLİ** — çift A: JAKE `am_onyx` 0.95 · MIKE `am_fenrir` 1.05 (`tools/ses/diyalog.py` varsayılanı)
| Kapı | Sonuç |
|---|---|
| Süre 60–90 sn (88 sn kesme eşiği) | **78,77 sn** — kesme gerekmedi (J04+M05 yerinde) |
| Whisper WER ≤ %5 | **%2,8** (176 kelime, 5 sayım: two/to + buy/by eşsesli, scratched→scratch /t/+/d/ birleşmesi, "Free"/"Slow" tam dosya silmesi — satır tek başına doğru) |
| −14 LUFS | **−14,2 LUFS**, TP −1,5 dBFS |
| Kelime zamanlı transkript | `kelimeler.json` (small.en) · referans `referans.txt` (= kilitli metin, diff boş) |
| Rhubarb (konuşmacı başına) | JAKE 236 cue, 13/13 satır; MIKE 170 cue, 12/12 satır; karşı konuşmacının satırında açık ağız 0 |

## Kilit sha256 (ilk 12)
- girdi `../bolum.txt` 945ea3c4fe4b · TTS kopyası `bolum-tts.txt` c34705bae369
- `bolum-001.wav` **289da660bbd0** (48 kHz mono 24-bit; git dışı, kopyası `bolum-001.m4a`)
- `bolum-001-JAKE.wav` a3df05d72d2d · `bolum-001-MIKE.wav` 07311fff8a0a (ana dosyayla aynı uzunluk/zaman)
Kokoro tam deterministik değil (yeniden üretimde satır zamanı ≤9 ms kayar) → bu sha'lar kilit; yeniden üretilirse zaman JSON + Rhubarb + transkript birlikte yenilenir.

## Dosyalar
`bolum-001.zaman.json` (satır: no, konusmaci, bas, bitis, metin) · `bolum-001-JAKE/MIKE.txt` · `rhubarb/JAKE.json`, `rhubarb/MIKE.json` (zamanlar ana eksende, ofset 0) · `kelimeler.json`

## Telaffuz düzeltmeleri (yalnız `bolum-tts.txt`, metin değişmedi)
- S5 "Two." → `[Two](/tʰˈu/)`: düz hâli satır tek başına da "Do" (seçenek numarası kayboluyordu). Varyantlar: /tʰˈuː/! = aynı; "Number two" metni değiştirir → elendi.
- S6 "gem" → `[gem](/ʤˈɪm/)`: düz /ʤˈɛm/, /ʤˈɛːm/, +2 vurgu, /ʤˈɛəm/ hepsi "jam"; /ʤˈeɪm/ "dime"; /ʤˈɪm/ "gem" (tek başına + tam dosya).
- "scratched discs" /t/+/d/ birleşmesi düzeltilmez (hafıza kuralı), anlam kaybı yok.

## Yeniden üretim (başka çift seçilirse `--ses` ile)
```
cd uretim/seri/bolum-001/ses; P=~/.finansal-arac/kokoro-venv/bin/python; V=~/.finansal-arac/venv/bin/python; R=~/.finansal-arac/rhubarb/build/rhubarb/rhubarb
$P ../../../../tools/ses/diyalog.py bolum-tts.txt bolum-001.wav [--ses JAKE=am_echo:0.92]
$V ../../../../tools/ses/yaziya-dok.py bolum-001.wav kelimeler.json small.en && python3 ../../../../tools/ses/hata-orani.py referans.txt kelimeler.json
for k in JAKE MIKE; do ffmpeg -y -i bolum-001-$k.wav -ar 16000 -ac 1 -c:a pcm_s16le /tmp/$k.wav; $R -q --dialogFile bolum-001-$k.txt -f json /tmp/$k.wav -o rhubarb/$k.json; done
```
