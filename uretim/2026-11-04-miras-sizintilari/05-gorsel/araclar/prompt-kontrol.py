#!/usr/bin/env python3
"""canva-promptlari.md denetimi · S03 miras (gorsel-varlik-sanatcisi, 2026-11-04; S08 sürümünden: id M, tavan 20, Leo bakış/kıyafet kilidi, Dalga satırı). Çıkış 0 = GEÇTİ.
Kurallar: (1) id'ler G01..Gnn sıralı, tekil, toplam ≤ TAVAN; (2) Leo'lu (CV-L): kartın EDIT kimlik çekirdeği + sayfa cümlesi birebir,
referansta sayfa MAHZHpeQGdM ve taban MAHZHqW0_Uo, saat sol bilek, kafa sabit cümlesi; (3) plaka (CV-A) / nesne (PROP): STYLE LOCK birebir +
düz çizgi film eki (NOT painterly/photorealistic) + EMPTY SCENE/siyah gömlekli adam yasağı; plakada taşma veya Shorts arayüzü kuralı,
nesnede düz slate-blue zemin; (4) hepsi: yazı/logo/banknot/bayrak yasağı, aspectRatio, Kabul, Kullanım; (5) <Gxx|Gyy … media id>
yer tutucusu yalnız önceki id'leri gösterir; (6) prompt'ta tırnak içinde ekrana yazdırılacak metin/rakam yok."""
import re, sys, pathlib
TAVAN = 20
KOK = pathlib.Path(__file__).resolve().parents[4]
kart = (KOK / "assets/karakter/karakter-karti.md").read_text()
bl = re.findall(r"```\n(.*?)```", kart, re.S)
EDIT = next(b for b in bl if b.startswith("EDIT the first reference image"))
KIMLIK = EDIT.split(" same framing and camera distance")[0]
SAYFA_CUMLE = "The second reference is the character model sheet; the face must match it."
STYLE = "STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows"
md = pathlib.Path(sys.argv[1]).read_text()
parcalar = re.split(r"^### (M\d\d) · ", md, flags=re.M)[1:]
hatalar, satirlar, gorulen = [], [], []
for i in range(0, len(parcalar), 2):
    cid, govde = parcalar[i], parcalar[i + 1]
    m = re.search(r"```prompt\n(.*?)```", govde, re.S)
    p = m.group(1) if m else ""
    tur = re.search(r"\*\*Tür:\*\* (.*)", govde).group(1)
    refs = re.search(r"\*\*Referanslar:\*\* (.*)", govde).group(1)
    k = [("prompt bloğu var", bool(p.strip()))]
    leolu = tur.startswith("CV-L")
    if leolu:
        k += [("EDIT kimlik çekirdeği birebir", KIMLIK in p), ("sayfa cümlesi birebir", SAYFA_CUMLE in p),
              ("ref sayfa + taban", "MAHZHpeQGdM" in refs and "MAHZHqW0_Uo" in refs),
              ("saat sol bilek (sağ yok)", ("wristwatch on his left wrist" in p or "wristwatch on left wrist" in p) and "right wrist" not in p),
              ("kafa sabit (rig)", "head stays in exactly the same place" in p),
              ("bakış kamerada (yüz kilidi)", "eye direction and mouth exactly the same as the first reference" in p and "looking straight at the camera" in p),
              ("aşağı/yana bakış yok", re.search(r"glanc|look(s|ing)? (down|away|at the box|at the clipboard)|eyes (look(s|ing)? (down|away|at)|drop)", p) is None),
              ("kıyafet eki (yelek/şapka yok)", "no vest, no hat" in p)]
    else:
        k += [("STYLE LOCK birebir", STYLE in p), ("düz çizgi film eki", "NOT painterly" in p and "NOT photorealistic" in p),
              ("EMPTY SCENE + siyah gömlekli adam yasağı", "EMPTY SCENE" in p and "no man in a black shirt" in p)]
        if tur.startswith("PROP"):
            k.append(("düz slate-blue zemin (M4)", "#3E5A7E" in p))
        else:
            k.append(("taşma / Shorts arayüzü kuralı", "central 80%" in p or "bottom 35%" in p))
    yasak = ("No text", "no logos") if leolu else ("No text", "no logos", "no banknotes", "no flags")  # Leo: kartın kapanış cümlesi
    k.append(("yazı/logo(/banknot/bayrak) yasağı", all(s in p for s in yasak)))
    k.append(("ekrana metin/rakam yazdırma yok", re.search(r"['\"][^'\"]*\d[^'\"]*['\"]|\$\d", p) is None))
    k.append(("aspectRatio", re.search(r"\*\*aspectRatio:\*\* \S+", govde) is not None))
    k.append(("Kabul satırı", "**Kabul:**" in govde))
    k.append(("Kullanım satırı", "**Kullanım:**" in govde))
    k.append(("Dalga satırı", "**Dalga:**" in govde))
    for grup in re.findall(r"<(M\d\d(?:\|M\d\d)*)[^>]*media id>", refs):
        for ref in grup.split("|"):
            k.append((f"yer tutucu {ref} önceden", ref in gorulen))
    gorulen.append(cid)
    bas = [a for a, ok in k if not ok]
    etiket = "LEO " if leolu else ("PROP" if tur.startswith("PROP") else "PLK ")
    satirlar.append(f"{cid}  {etiket} {len(k)-len(bas)}/{len(k)}  {'GEÇTİ' if not bas else 'KALDI: ' + '; '.join(bas)}")
    hatalar += [f"{cid}: {b}" for b in bas]
beklenen = [f"M{n:02d}" for n in range(1, len(gorulen) + 1)]
if gorulen != beklenen: hatalar.append(f"id sırası {gorulen} != {beklenen}")
if len(gorulen) > TAVAN: hatalar.append(f"üretim sayısı {len(gorulen)} > tavan {TAVAN}")
print("\n".join(satirlar))
leo = sum(" LEO " in s for s in satirlar); prp = sum(" PROP " in s for s in satirlar)
print(f"\nToplam {len(gorulen)} prompt (Leo'lu {leo}, nesne {prp}, plaka {len(gorulen)-leo-prp}) · tavan {TAVAN} · id sırası {'GEÇTİ' if gorulen == beklenen else 'KALDI'}")
print("KAPI:", "GEÇTİ" if not hatalar else "KALDI\n" + "\n".join(hatalar))
sys.exit(1 if hatalar else 0)
