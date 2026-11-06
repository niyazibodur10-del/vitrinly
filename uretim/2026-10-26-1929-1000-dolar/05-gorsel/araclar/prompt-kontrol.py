#!/usr/bin/env python3
"""canva-promptlari.md denetimi (gorsel-varlik-sanatcisi). Çıkış kodu 0 = GEÇTİ.
Kurallar: (1) id'ler C01..Cnn sıralı ve tekil; (2) Leo'lu prompt (CV-L/RIG): kartın CHARACTER LOCK paragrafı birebir (taban)
veya EDIT kimlik çekirdeği + 'second reference is the character model sheet' birebir (düzenleme), referanslarda sayfa MAHZHpeQGdM;
(3) karaktersiz plaka (CV-A): STYLE LOCK cümlesi birebir + 'no man in a black shirt' + 'EMPTY SCENE'; (4) hepsi: yazı/logo yasağı,
aspectRatio, Kabul satırı, Kullanım satırı; (5) yer tutucu <Cxx media id> yalnız daha önceki bir id'yi gösterir."""
import re, sys, pathlib
KOK = pathlib.Path(__file__).resolve().parents[4]
kart = (KOK / "assets/karakter/karakter-karti.md").read_text()
bl = re.findall(r"```\n(.*?)```", kart, re.S)
LOCK = next(b for b in bl if b.startswith("CHARACTER LOCK")).split("\nSHOT:")[0].strip()
EDIT = next(b for b in bl if b.startswith("EDIT the first reference image"))
KIMLIK = EDIT.split(" same framing and camera distance")[0]
SAYFA_CUMLE = "The second reference is the character model sheet; the face must match it."
STYLE = "STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows"
md = pathlib.Path(sys.argv[1]).read_text()
parcalar = re.split(r"^### (C\d\d) · ", md, flags=re.M)[1:]
hatalar, satirlar, gorulen = [], [], []
for i in range(0, len(parcalar), 2):
    cid, govde = parcalar[i], parcalar[i + 1]
    m = re.search(r"```prompt\n(.*?)```", govde, re.S)
    p = m.group(1) if m else ""
    tur = re.search(r"\*\*Tür:\*\* (.*)", govde).group(1)
    refs = re.search(r"\*\*Referanslar:\*\* (.*)", govde).group(1)
    k = []
    leolu = tur.startswith(("CV-L", "RIG"))
    if leolu:
        if "taban" in tur.split("(")[0]:
            k.append(("kart CHARACTER LOCK birebir", LOCK in p))
        else:
            k.append(("EDIT kimlik çekirdeği birebir", KIMLIK in p))
            k.append(("sayfa cümlesi birebir", SAYFA_CUMLE in p))
        k.append(("sayfa referansı MAHZHpeQGdM", "MAHZHpeQGdM" in refs))
        k.append(("saat sol bilek", "wristwatch on the left wrist" in p or "wristwatch on left wrist" in p))
    else:
        k.append(("STYLE LOCK birebir", STYLE in p))
        k.append(("EMPTY SCENE + siyah gömlekli adam yasağı", "EMPTY SCENE" in p and "no man in a black shirt" in p))
        k.append(("%80 taşma kuralı", "central 80%" in p))
    k.append(("yazı/logo yasağı", re.search(r"no text", p, re.I) is not None and re.search(r"no logos", p, re.I) is not None))
    k.append(("aspectRatio", re.search(r"\*\*aspectRatio:\*\* \S+", govde) is not None))
    k.append(("Kabul satırı", "**Kabul:**" in govde))
    k.append(("Kullanım satırı", "**Kullanım:**" in govde))
    for ref in re.findall(r"<(C\d\d) media id>", refs):
        k.append((f"yer tutucu {ref} önceden", ref in gorulen))
    gorulen.append(cid)
    bas = [a for a, ok in k if not ok]
    satirlar.append(f"{cid}  {'LEO ' if leolu else 'PLK '} {len(k)-len(bas)}/{len(k)}  {'GEÇTİ' if not bas else 'KALDI: ' + '; '.join(bas)}")
    hatalar += [f"{cid}: {b}" for b in bas]
beklenen = [f"C{n:02d}" for n in range(1, len(gorulen) + 1)]
if gorulen != beklenen: hatalar.append(f"id sırası {gorulen} != {beklenen}")
print("\n".join(satirlar))
leo = sum(1 for s in satirlar if " LEO " in s); print(f"\nToplam {len(gorulen)} prompt (Leo'lu {leo}, plaka {len(gorulen)-leo}) · id sırası {'GEÇTİ' if gorulen == beklenen else 'KALDI'}")
print("KAPI:", "GEÇTİ" if not hatalar else "KALDI\n" + "\n".join(hatalar))
sys.exit(1 if hatalar else 0)
