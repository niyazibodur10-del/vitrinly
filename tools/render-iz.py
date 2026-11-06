#!/usr/bin/env python3
"""Parça render için değişiklik dedektörü (render-parca.sh --oto çağırır; elle de kullanılabilir).

Kullanım: render-iz.py <yeni_iz_dizini> <eski_iz_dizini> <ornek_araligi> <parca_kare> <toplam_kare>
  İz = kompozisyonun her <ornek_araligi>. karesinin 1/4 ölçekli PNG'si (Remotion --sequence --every-nth-frame).
  element-<i>.png ↔ kare i*ornek_araligi. Çıktı (stdout): değişen parça indeksleri, virgülle ("" = hiçbiri).
  stderr: parça başına en kötü kare ölçümü.

Neden toleranslı karşılaştırma (2026-10-28 ölçümü, uretim-muhendisi): aynı kompozisyon iki kez render edilince
Chromium yazılım rasterleştirmesi (blur filtreli sahneler) 60 örnek karenin 19'unda küçük fark üretti: en çok 40/255,
>24 farklı piksel ≤16, >48 farklı piksel 0. Gerçek değişiklikler: açılış vaat şeridi eklenmesi (Ilk30 A→B) kare başına
881+ piksel >48; 1,07x punch-in (B→C, en ince görsel değişiklik) 32.000+ piksel. Eşik: bir örnek karede
>48 farklı piksel sayısı >= ESIK_PIKSEL (8) ise parça değişmiş sayılır. Elenen: bayt/MD5 karşılaştırma (gürültü yüzünden
her şeyi "değişti" sayar), ortalama fark (küçük altyazı değişikliğini kaçırır).
Sınır: <ornek_araligi> kareden kısa süren değişiklik (ör. 6 kare = 0,2 sn) iki örnek arasına düşerse kaçabilir →
şüphede --yeniden ile o parçayı zorla.
"""
import os, sys
import numpy as np
from PIL import Image

ESIK_FARK, ESIK_PIKSEL = 48, 8


def yukle(d, ad):
    p = os.path.join(d, ad)
    return np.asarray(Image.open(p).convert("RGB")).astype(np.int16) if os.path.isfile(p) else None


def main():
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    yeni, eski, n, parca, toplam = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:6])
    adlar = sorted(f for f in os.listdir(yeni) if f.endswith(".png"))
    if not adlar:
        sys.exit("HATA: yeni iz boş")
    genislik = len(adlar[0].split("-")[-1].split(".")[0])
    parca_sayisi = (toplam + parca - 1) // parca
    degisen = []
    for p in range(parca_sayisi):
        bas, son = p * parca, min((p + 1) * parca, toplam) - 1
        en_kotu, neden = 0, "aynı"
        orn = [i for i in range((bas + n - 1) // n, son // n + 1)]
        if not os.path.isdir(eski) or not orn:
            degisen.append(p); print(f"p{p:04d}: eski iz yok", file=sys.stderr); continue
        for i in orn:
            ad = f"element-{i:0{genislik}d}.png"
            a, b = yukle(yeni, ad), yukle(eski, ad)
            if a is None or b is None or a.shape != b.shape:
                en_kotu, neden = 10**9, f"{ad} eksik/boyut farklı"; break
            k = int((np.abs(a - b).max(2) > ESIK_FARK).sum())
            if k > en_kotu:
                en_kotu, neden = k, f"kare {i * n}: {k} piksel >{ESIK_FARK}"
        if en_kotu >= ESIK_PIKSEL:
            degisen.append(p)
        print(f"p{p:04d} [{bas}-{son}] {'DEĞİŞTİ' if en_kotu >= ESIK_PIKSEL else 'aynı'} ({neden})", file=sys.stderr)
    print(",".join(map(str, degisen)))


if __name__ == "__main__":
    main()
