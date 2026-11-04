#!/usr/bin/env python3
"""cue.json → cue-listesi.md (insan okur; kurgu-editoru). Deterministik."""
import json, os
B = os.path.dirname(os.path.abspath(__file__)); c = json.load(open(f"{B}/cue.json")); fps = c["fps"]
mmss = lambda t: f"{int(t // 60)}:{t % 60:05.2f}"
L = ["# Cue listesi — 2026-10-28-yeni-video S08 (F6)", "",
     f"Kaynak: `06-muzik/cue.json` (`cue-uret.py` ← `animasyon-efekt-cue.json` tahmini=false + `04-ses/sahne-zamanlari.json`). Zaman ekseni = `04-ses/anlatim.wav` ({c['toplam_sn']} sn). Kare = {fps} fps.",
     "Stem'ler: `stems/muzik-stem.wav`, `stems/sfx-stem.wav` (48 kHz stereo 24-bit, anlatımla örnek örnek aynı uzunluk, 0 noktası = anlatımın 0'ı). Montajda anlatım kaydırılırsa iki stem de aynı kadar kaydırılır.",
     "Abone klik sesi stem'de YOK: `assets/efekt/ozgun-fare-klik.flac`'ı kurgu-editoru AboneOl bileşeniyle görsel tıklamaya ±2 kare yerleştirir (olaylar: " +
     ", ".join(f"{a['t']} sn" for a in c["atlanan"] if a["tur"] == "abone") + ").", "", "## Müzik bölümleri", "",
     "| # | Bölüm | Giriş → çıkış | Kare | Parça (lisans) | Ruh hali / tempo | Konuşma altı | Giriş/çıkış sönüşü |", "|---|---|---|---|---|---|---|---|"]
for i, m in enumerate(c["muzik"], 1):
    L.append(f"| {i} | {m['ad']} | {mmss(m['bas'])} → {mmss(m['son'])} | {round(m['bas'] * fps)}–{round(m['son'] * fps)} | {m['kaynak']} | {m['ruh']} · {m['tempo']} | −{m['duck']} dB{' + 3 kHz oyuk' if m.get('oyuk') else ''} | {m.get('giris', 1.2)} / {m.get('cikis', 1.2)} sn |")
L += ["", "Notlar: S06 kırmızı INTEREST zarfı masaya kaydığı karede müzik 0.25 sn'de **keser** (tek tık), \"This household pays its lenders…\" cümlesinde aynı caz 2 sn'de geri girer. Konuşma boşluğu ≥0.9 sn olunca müzik +6 dB açılır.",
      "", "## Shorts müzik yatakları (60 sn, sonda 2 sn sönüş; kurgu kesit uzunluğuna kırpar)", ""]
for s in c["shorts"]:
    L.append(f"- `stems/{s['ad']}-muzik-stem.wav` ← `{s['dosya']}` (konuşma altı −{s['duck']} dB, mobil)")
L += ["", f"## SFX vuruşları ({len(c['sfx'])} vuruş, {len({s['t_olay'] for s in c['sfx']})} görsel olay; hizalama: geçiş whoosh'unda tepe, diğerlerinde ses başlangıcı olay karesinde)", "",
      "| Olay zamanı | Kare | Olay | Dosya | Dosya başı (sn) | Kazanç dB |", "|---|---|---|---|---|---|"]
for s in c["sfx"]:
    L.append(f"| {mmss(s['t_olay'])} | {s['kare_olay']} | {s['olay']} ({s['oneri']}) | `{s['dosya'].split('/')[-1]}` | {s['t']} | {s['db']} |")
L += ["", f"## Sessiz bırakılan olaylar ({len(c['atlanan'])})", "", "| t | tür | öneri | neden |", "|---|---|---|---|"]
L += [f"| {a['t']} | {a['tur']} | {a['oneri']} | {a['neden']} |" for a in c["atlanan"]]
open(f"{B}/cue-listesi.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
