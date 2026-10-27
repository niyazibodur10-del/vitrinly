#!/usr/bin/env python3
"""Plakayı hedef plakaların renk istatistiğine eşler (Lab ortalama/std aktarımı, Reinhard) — referans setin
ortalaması kullanılır. C15 (renkli sonbahar) → C16–C19 sepya ailesine. Kullanım: python -I sepya-esle.py <girdi> <cikis> <ref1> [ref2...]"""
import sys, cv2, numpy as np, json
def st(p):
    l = cv2.cvtColor(cv2.imread(p), cv2.COLOR_BGR2LAB).astype(np.float32).reshape(-1, 3); return l.mean(0), l.std(0)
src = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2LAB).astype(np.float32)
refs = [st(p) for p in sys.argv[3:]]; tm = np.mean([r[0] for r in refs], 0); ts = np.mean([r[1] for r in refs], 0)
sm, ss = src.reshape(-1, 3).mean(0), src.reshape(-1, 3).std(0)
out = (src - sm) / ss * ts + tm
cv2.imwrite(sys.argv[2], cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR))
print(json.dumps({"kaynak_ort": sm.round(1).tolist(), "hedef_ort": tm.round(1).tolist(), "hedef_std": ts.round(1).tolist()}))
