#!/usr/bin/env python3
"""Ses yeniden kilitlenince görsel zamanları taşır (animasyon-yonetmeni 2026-11-11, Pocket TTS geçişi).
Eski ve yeni ses için her satırın metin kelimeleri Whisper zamanlarına LCS ile hizalanır (zaman.ts ekranKelimeleri ile
aynı mantık); çapalar = satır başı/sonu + kelime başı/sonu (eski → yeni). Ara zamanlar parça parça doğrusal eşlenir.
Kullanım: python3 zaman-esle.py <eski_zaman> <eski_kelime> <yeni_zaman> <yeni_kelime> t1 t2 ...  → yeni zamanlar
Modül olarak: esleyici(...) → f(t)."""
import json, re, sys, bisect

def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower().replace("’", "").replace("'", ""))

def satir_kelimeleri(zaman, kelime):
    S = zaman["satirlar"]; W = kelime["words"]
    sahip = []
    for w in W:
        en, d = -1, -1e9
        for i, s in enumerate(S):
            o = min(w["e"], s["bitis"]) - max(w["s"], s["bas"])
            if o > d: d, en = o, i
        sahip.append(en)
    out = []
    for i, s in enumerate(S):
        ks = [{"k": w["w"].strip(), "bas": min(max(w["s"], s["bas"]), s["bitis"]), "bitis": max(min(w["e"], s["bitis"]), s["bas"])} for wi, w in enumerate(W) if sahip[wi] == i]
        metin = s["metin"].split()
        n, m = len(metin), len(ks)
        L = [[0] * (m + 1) for _ in range(n + 1)]
        for a in range(n - 1, -1, -1):
            for b in range(m - 1, -1, -1):
                L[a][b] = L[a + 1][b + 1] + 1 if norm(metin[a]) and norm(metin[a]) == norm(ks[b]["k"]) else max(L[a + 1][b], L[a][b + 1])
        es = [None] * n; a = b = 0
        while a < n and b < m:
            if norm(metin[a]) and norm(metin[a]) == norm(ks[b]["k"]): es[a] = b; a += 1; b += 1
            elif L[a + 1][b] >= L[a][b + 1]: a += 1
            else: b += 1
        z = [[0, 0] for _ in metin]; a = 0
        while a < n:
            if es[a] is not None: z[a] = [ks[es[a]]["bas"], ks[es[a]]["bitis"]]; a += 1; continue
            j = a
            while j < n and es[j] is None: j += 1
            a0 = z[a - 1][1] if a > 0 else s["bas"]; a1 = ks[es[j]]["bas"] if j < n else s["bitis"]
            top = sum(len(x) + 1 for x in metin[a:j]); t = a0
            for q in range(a, j):
                d = (len(metin[q]) + 1) / top * max(0, a1 - a0); z[q] = [t, t + d]; t += d
            a = j
        out.append((s, z))
    return out

def esleyici(ez, ek, yz, yk):
    E = satir_kelimeleri(json.load(open(ez)), json.load(open(ek)))
    Y = satir_kelimeleri(json.load(open(yz)), json.load(open(yk)))
    assert len(E) == len(Y)
    cift = []
    for (es, ezs), (ys, yzs) in zip(E, Y):
        assert es["metin"] == ys["metin"]
        cift += [(es["bas"], ys["bas"]), (es["bitis"], ys["bitis"])]
        for a, b in zip(ezs, yzs): cift += [(a[0], b[0]), (a[1], b[1])]
    cift = sorted(set(cift))
    # monoton yap (aynı eski zamana tek yeni)
    xs, ys_ = [], []
    for x, y in cift:
        if xs and x - xs[-1] < 1e-6: continue
        if ys_ and y < ys_[-1]: y = ys_[-1]
        xs.append(x); ys_.append(y)
    def f(t):
        if t <= xs[0]: return max(0.0, t + (ys_[0] - xs[0])) if t > 0 else t
        if t >= xs[-1]: return t + (ys_[-1] - xs[-1])
        i = bisect.bisect_right(xs, t) - 1
        x0, x1, y0, y1 = xs[i], xs[i + 1], ys_[i], ys_[i + 1]
        return y0 + (t - x0) / (x1 - x0) * (y1 - y0)
    return f

if __name__ == "__main__":
    f = esleyici(*sys.argv[1:5])
    print(" ".join(f"{f(float(t)):.3f}" for t in sys.argv[5:]))
