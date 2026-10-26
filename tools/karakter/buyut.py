#!/usr/bin/env python3
"""Görsel büyütme: kırp -> Real-ESRGAN x4 (spandrel, yerel ağırlık, trust_remote_code yok) -> RGB PNG.

Kullanım: buyut.py <girdi> <cikis.png> <x0,y0,x1,y1 | tam> [agirlik.pth] [--parca 256] [--pay 16]
  agirlik varsayılanı: $ARAC_DIZINI/RealESRGAN_x4.pth (~/.finansal-arac).
Parçalı (tile) çıkarım: görüntü --parca px karelere bölünür, her kare --pay px komşu bağlamıyla işlenir, pay kırpılıp
birleştirilir (dikiş izi yok). Neden: tek parça çıkarımda bellek ~9,4 KB/girdi pikseli + 0,45 GB ölçüldü
(256² → 1,2 GB); 1920x1080 tek parça ≈ 19 GB → 15 GB konteynerde OOM (2026-10-26). Parçalı tepe bellek ≈ 1,3 GB.
Hız (4 vCPU): ~0,5 sn / 1000 girdi pikseli [ölçüm: docs/uretim-hatti-testi.md].
"""
import argparse, os
import numpy as np, torch, spandrel
from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("girdi"); ap.add_argument("cikis"); ap.add_argument("kutu")
    ap.add_argument("agirlik", nargs="?",
                    default=os.path.join(os.environ.get("ARAC_DIZINI", os.path.expanduser("~/.finansal-arac")), "RealESRGAN_x4.pth"))
    ap.add_argument("--parca", type=int, default=256); ap.add_argument("--pay", type=int, default=16)
    a = ap.parse_args()
    img = Image.open(a.girdi).convert("RGB")
    if a.kutu != "tam":
        img = img.crop(tuple(int(v) for v in a.kutu.split(",")))
    m = spandrel.ModelLoader().load_from_file(a.agirlik).eval()
    s = m.scale
    x = np.asarray(img).astype(np.float32) / 255
    h, w = x.shape[:2]
    y = np.zeros((h * s, w * s, 3), np.float32)
    P, Y = a.parca, a.pay
    with torch.no_grad():
        for r0 in range(0, h, P):
            for c0 in range(0, w, P):
                r1, c1 = min(r0 + P, h), min(c0 + P, w)
                a0, b0, a1, b1 = max(r0 - Y, 0), max(c0 - Y, 0), min(r1 + Y, h), min(c1 + Y, w)
                t = torch.from_numpy(np.ascontiguousarray(x[a0:a1, b0:b1])).permute(2, 0, 1)[None]
                o = m(t).clamp(0, 1)[0].permute(1, 2, 0).numpy()
                y[r0 * s:r1 * s, c0 * s:c1 * s] = o[(r0 - a0) * s:(r1 - a0) * s, (c0 - b0) * s:(c1 - b0) * s]
    Image.fromarray((y * 255).round().astype(np.uint8)).save(a.cikis)
    print(img.size, "->", y.shape)


if __name__ == "__main__":
    main()
