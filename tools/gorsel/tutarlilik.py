#!/usr/bin/env python3
"""Karakter paketi tutarlılık testi (OpenCV).
Kullanım: ~/.finansal-arac/venv/bin/python -I tools/gorsel/tutarlilik.py <paket_klasoru> [--ref a-konusma-kapali.png] [--kontak kontak.jpg]
Yöntem: düz arka planı köşe renginden ayırır -> ön plan maskesi. Maskede renk bölgeleri:
  ten  = turuncu-ten tonu (HSV H 5-25, S>60, V>110)
  sac  = kafa kutusunun üst %35'indeki koyu pikseller (V<90)
  gomlek = kafa altındaki gövdenin koyu, düşük doygunluklu pikselleri (V<70, S<90)
Her bölgenin medyan Lab rengi -> referansa göre ΔE (CIE76). Kafa kutusu (genişlik daralan üst kısım)
için HSV histogram korelasyonu + kafa üstü/merkez/kafa yüksekliği (kadraj sabitliği).
Eşikler: ten ΔE<=8, saç ΔE<=10, gömlek ΔE<=8, kafa hist kor.>=0.80, kafa merkez kayması <=4% genişlik, kafa ölçek farkı <=10%.
"""
import sys, os, glob, json, argparse
import cv2, numpy as np

def fg_mask(img):
    h, w = img.shape[:2]
    corners = np.concatenate([img[:20,:20].reshape(-1,3), img[:20,-20:].reshape(-1,3)])
    bg = np.median(corners, 0)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
    bgl = cv2.cvtColor(bg.reshape(1,1,3).astype(np.uint8), cv2.COLOR_BGR2LAB).astype(np.float32)[0,0]
    d = np.linalg.norm(lab - bgl, axis=2)
    m = (d > 18).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    n, lbl, st, _ = cv2.connectedComponentsWithStats(m)
    if n > 1:
        k = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); m = (lbl == k).astype(np.uint8)
    return m

def head_box(m, skin):
    # kafa: maskenin en üstünden başlayıp ten+saç bölgesinin; genişlik profili omuzda sıçrar
    ys = np.where(m.any(1))[0]; top = ys[0]
    widths = m.sum(1)
    # ilk 40 satırın genişliğinin medyanına göre: genişlik kafa genişliğinin 1.9 katını aşınca omuz
    hw = None; bottom = None
    for y in range(top+10, m.shape[0]):
        w = widths[y]
        if hw is None and y > top + 60: hw = np.median(widths[top+30:top+60])
        if hw is not None and w > 1.9*hw: bottom = y; break
    if bottom is None: bottom = top + 300
    row = m[top:bottom]
    xs = np.where(row.any(0))[0]
    # kafa sütunları: üst 120 satırda maskeli sütunlar
    xs2 = np.where(m[top:top+min(150,bottom-top)].any(0))[0]
    x0, x1 = xs2[0], xs2[-1]
    return int(x0), int(top), int(x1), int(bottom)

def med_lab(img, sel):
    if sel.sum() < 50: return None
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
    v = np.median(lab[sel>0], 0)
    return [float(v[0]*100/255), float(v[1]-128), float(v[2]-128)]

def de(a, b):
    if a is None or b is None: return None
    return float(np.linalg.norm(np.array(a)-np.array(b)))

def analyze(path):
    img = cv2.imread(path); H, W = img.shape[:2]
    m = fg_mask(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    Hh, S, V = hsv[...,0], hsv[...,1], hsv[...,2]
    skin = ((Hh>=5)&(Hh<=25)&(S>60)&(V>110)&(m>0)).astype(np.uint8)
    x0,y0,x1,y1 = head_box(m, skin)
    hb = np.zeros_like(m); hb[y0:y1, x0:x1] = 1
    hair = ((V<90)&(m>0)&(hb>0)).astype(np.uint8); hair[y0+int(0.35*(y1-y0)):] = 0
    face_skin = skin & hb
    body = np.zeros_like(m); body[y1+40:, :] = 1
    shirt = ((V<70)&(S<90)&(m>0)&(body>0)).astype(np.uint8)
    head = img[y0:y1, x0:x1]
    hh = cv2.calcHist([cv2.cvtColor(head, cv2.COLOR_BGR2HSV)], [0,1], (m[y0:y1,x0:x1]*255), [30,32], [0,180,0,256])
    cv2.normalize(hh, hh)
    return dict(path=path, size=(W,H), head=(x0,y0,x1,y1), hist=hh,
                skin=med_lab(img, face_skin), hair=med_lab(img, hair), shirt=med_lab(img, shirt),
                fg_area=float(m.mean()))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('dir'); ap.add_argument('--ref', default='a-konusma-kapali.png')
    ap.add_argument('--kontak', default=None); ap.add_argument('--kart', default=None, help='referans karakter sayfası (kontakta ilk kare)'); ap.add_argument('--json', default=None)
    a = ap.parse_args()
    files = sorted(f for f in glob.glob(os.path.join(a.dir, '*.png')))
    res = {os.path.basename(f): analyze(f) for f in files}
    r = res[a.ref]; rx0,ry0,rx1,ry1 = r['head']; rW = r['size'][0]
    rows = []; allok = True
    print(f"{'dosya':24} {'çöz.':10} {'tenΔE':>6} {'saçΔE':>6} {'gömΔE':>6} {'kafaKor':>7} {'merkez%':>7} {'ölçek%':>7}  sonuç")
    for n, x in res.items():
        x0,y0,x1,y1 = x['head']
        cor = float(cv2.compareHist(r['hist'], x['hist'], cv2.HISTCMP_CORREL))
        dc = abs(((x0+x1)/2 - (rx0+rx1)/2))/rW*100
        sc = abs((y1-y0)/(ry1-ry0)-1)*100
        dsk, dh, dsh = de(r['skin'],x['skin']), de(r['hair'],x['hair']), de(r['shirt'],x['shirt'])
        checks = [x['size'][0]>=1920 and x['size'][1]>=1080, dsk is not None and dsk<=8, dh is not None and dh<=10,
                  dsh is not None and dsh<=8, cor>=0.80]
        ok = all(checks); allok &= ok
        fr = 'kadraj-ok' if (dc<=4 and sc<=10) else 'kadraj-kaydı'
        f = lambda v: 'yok' if v is None else f"{v:.1f}"
        print(f"{n:24} {x['size'][0]}x{x['size'][1]:<5} {f(dsk):>6} {f(dh):>6} {f(dsh):>6} {cor:7.2f} {dc:7.1f} {sc:7.1f}  {'GEÇTİ' if ok else 'KALDI'} {fr}")
        rows.append(dict(dosya=n, cozunurluk=x['size'], ten_dE=dsk, sac_dE=dh, gomlek_dE=dsh, kafa_hist_kor=cor,
                         kafa_merkez_kayma_yuzde=dc, kafa_olcek_fark_yuzde=sc, gecti=ok, kafa_kutusu=x['head']))
    if a.json:
        json.dump(rows, open(a.json,'w'), ensure_ascii=False, indent=1)
    if a.kontak:
        thumbs = []
        for n, x in res.items():
            im = cv2.imread(x['path']); x0,y0,x1,y1 = x['head']
            cv2.rectangle(im, (x0,y0), (x1,y1), (0,255,255), 4)
            t = cv2.resize(im, (640,360)); cv2.rectangle(t,(0,0),(640,34),(0,0,0),-1)
            cv2.putText(t, n, (8,25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            # kafa yakın plan
            hc = cv2.resize(cv2.imread(x['path'])[y0:y1, x0:x1], (300,360))
            thumbs.append(np.hstack([t, hc]))
        if a.kart:
            k = cv2.imread(a.kart); kh, kw = k.shape[:2]; s_ = min(940/kw, 360/kh)
            k = cv2.resize(k, (int(kw*s_), int(kh*s_))); tile = np.full((360,940,3), 40, np.uint8)
            oy, ox = (360-k.shape[0])//2, (940-k.shape[1])//2; tile[oy:oy+k.shape[0], ox:ox+k.shape[1]] = k
            cv2.putText(tile, 'REFERANS', (8,25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)
            thumbs.insert(0, tile)
        cols = 2; pad = np.zeros_like(thumbs[0])
        while len(thumbs) % cols: thumbs.append(pad)
        grid = np.vstack([np.hstack(thumbs[i:i+cols]) for i in range(0, len(thumbs), cols)])
        cv2.imwrite(a.kontak, grid, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print('TOPLAM:', 'TÜMÜ GEÇTİ' if allok else 'ELENEN VAR')

if __name__ == '__main__':
    main()
