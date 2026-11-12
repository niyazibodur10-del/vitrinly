# Göz kırpma elipsleri + ten rengi ölçümü (animasyon-yonetmeni 2026-11-11). Elipsler sklera gövdesinden ölçülüp
# elle düzeltildi (iris kenarda olunca gövde eksik kalıyor). Çıktı → video/src/seri/bolumler/mekan-l1.ts GOZ.
# Çalıştır: ~/.finansal-arac/earshot-venv/bin/python uretim/seri/bolum-001/animasyon/goz-kapak-olc.py
import json,numpy as np
from PIL import Image
G={
 "jake-taban":{"dosya":"seri/bolum-001/karakter/jake-taban.png","gozler":[[485,450,47,27,0],[654.5,437.5,39,25,-5]]},
 "mike-taban":{"dosya":"seri/bolum-001/karakter/mike-taban.png","gozler":[[550,412.5,40,22,5],[698.5,404,32,20,-5]]},
 "jake-dusunceli":{"dosya":"seri/bolum-001/ifade/jake-dusunceli.png","gozler":[[423,596,64,38,10],[686,565,60,42,10]]},
 "mike-heyecanli":{"dosya":"seri/bolum-001/ifade/mike-heyecanli.png","gozler":[[424,571.2,55,37,3],[662.9,571.9,55,36,-5]]},
}
out={}
for ad,c in G.items():
    im=np.asarray(Image.open('video/public/'+c['dosya']).convert('RGB')).astype(float)
    gl=[]
    for cx,cy,rx,ry,a in c['gozler']:
        def ornek(y,w):
            y=int(y); x0=int(cx-w); x1=int(cx+w)
            return np.median(im[y-2:y+3,x0:x1].reshape(-1,3),0)
        ust=ornek(cy-ry-17,rx*0.4); alt=ornek(cy+ry+9,rx*0.5)
        hx=lambda v:'#%02x%02x%02x'%tuple(int(round(x)) for x in v)
        gl.append(dict(cx=cx,cy=cy,rx=rx,ry=ry,aci=a,ten=hx(alt)))
    out[ad]=gl
json.dump(out,open('uretim/seri/bolum-001/animasyon/goz-kapak.json','w'),indent=1)
print(json.dumps(out,indent=0))
