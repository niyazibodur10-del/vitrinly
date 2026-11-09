#!/usr/bin/env python3
"""Konuşan Leo rig tabanları: gorsel-varlik-sanatcisi poz kesikleri (public/kmiras/poz-M0x.png, 1920x1080) S08 rig kırpım kutusuyla
(SUNUCU_T x200 y23 w1517 h1057) kırpılır; kafa leo-a'ya piksel hizalı olsun diye kutu, ölçülen kafa kaymasıyla (dx, dy) kaydırılır
→ S08 ağız/göz yamaları (public/kbutce) değişmeden oturur. Ölçüm: yüz bölgesi (x620–860, y150–420) ±12 px tarama, en düşük ortalama fark.
Kullanım (repo kökü): python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/rig-poz.py"""
from pathlib import Path
import numpy as np
from PIL import Image
KOK = Path(__file__).resolve().parents[3]; P = KOK / "video/public"
a = np.asarray(Image.open(P / "kbutce/leo-a.png").convert("RGBA")).astype(int)
for ad in ("M04", "M05", "M06", "M07", "M17"):
    im = Image.open(P / f"kmiras/poz-{ad}.png").convert("RGBA")
    best = None
    for dy in range(-12, 13):
        for dx in range(-12, 13):
            c = np.asarray(im.crop((200 + dx, 23 + dy, 200 + dx + 1517, 23 + dy + 1057))).astype(int)
            m = (a[150:420, 620:860, 3] > 200) & (c[150:420, 620:860, 3] > 200)
            e = np.abs(a[150:420, 620:860, :3] - c[150:420, 620:860, :3])[m].mean() if m.sum() > 1000 else 999
            if best is None or e < best[0]:
                best = (e, dx, dy)
    e, dx, dy = best
    im.crop((200 + dx, 23 + dy, 200 + dx + 1517, 23 + dy + 1057)).save(P / f"kmiras/leo-{ad}.png")
    print(ad, f"hata {e:.1f} dx {dx} dy {dy}")
