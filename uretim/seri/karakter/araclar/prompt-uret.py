#!/usr/bin/env python3
"""Flip By Vote · canva-promptlari.md üretici (gorsel-varlik-sanatcisi, 2026-11-10).
Kilit blokları (JAKE/MIKE/STİL) YALNIZ burada tanımlıdır; her prompt bunları birebir birleştirir (elle kopyalama kayması yok).
Yerleşik kontrol: kilit birebir var mı, yasak kelime (stüdyo/marka adı, hex) yok mu, oran cümlesi aspectRatio ile uyumlu mu.
Kullanım: python3 -I prompt-uret.py ../canva-promptlari.md   ·   negatif test: python3 -I prompt-uret.py --negatif"""
import sys, re

STYLE = ("STYLE LOCK: original stylized 3D animated-feature look, clean high-quality CG render, soft global illumination, "
         "gentle subsurface scattering on skin, appealing slightly stylized proportions (head a little larger than realistic, "
         "large expressive eyes, simplified rounded forms), smooth matte fabric with subtle weave texture, soft contact shadows. "
         "No outlines, no cel-shading, not a 2D drawing, not photorealistic, not claymation. "
         "Original character design, not resembling any existing cartoon character, celebrity or real person.")
JAKE = ("JAKE LOCK (identical in every image): Jake Miller, an original 26-year-old American man, slim average build, "
        "light warm skin, oval face with a defined jaw, short dark-brown hair (short on the sides, neat slightly longer top "
        "brushed to his right), straight dark-brown eyebrows, calm warm-brown eyes, short light even stubble on jaw, chin and "
        "upper lip (not a full beard). Outfit never changes: plain navy-blue pullover hoodie with the hood down, front kangaroo "
        "pocket and two light-grey drawstrings, no print and no logo; beige chino pants; plain white low-top sneakers. "
        "No glasses, no hat, no jewelry, no watch. Body language: calm, analytical, composed.")
MIKE = ("MIKE LOCK (identical in every image): Mike Carter, an original 27-year-old American man, a little taller and broader "
        "than his friend Jake (athletic build, about 6 feet tall), fair skin with a light warm flush on the cheeks, slightly square face, messy tousled "
        "light-brown (dark-blond) hair, medium length on top falling loosely over the forehead, shorter sides, bright blue eyes, "
        "clean-shaven. Outfit never changes: red-and-black buffalo-check flannel shirt (large even squares) worn unbuttoned and "
        "open over a plain white crew-neck T-shirt, flannel sleeves rolled up to just below the elbows; dark-indigo slim jeans; "
        "brown leather lace-up boots. No glasses, no hat, no jewelry, no watch. Body language: energetic, playful, confident.")
STYLE_SET = ("STYLE LOCK: original stylized 3D animated-feature environment, clean high-quality CG render, soft global "
             "illumination, slightly exaggerated rounded shapes, tidy simplified detail, believable materials, not photorealistic, "
             "not a 2D drawing. Palette: cool, slightly desaturated background tones with warm pools of practical light "
             "(warm-colored characters will be composited in front).")
NOTXT = ("No text, no letters, no numbers, no labels, no signs, no brand logos, no badges, no license plates, no watermark, "
         "no color swatches.")
NOPPL = "EMPTY SET: no people, no characters, no animals, no mannequins, no pictures of faces."
SAFE = ("VERTICAL 9:16 FRAME RULES: camera at natural eye level; keep the central vertical band (middle 60% of the width) "
        "open and uncluttered from 35% to 85% of the frame height, where two characters will be composited later; put busy "
        "detail at the sides and in the upper background; the bottom 25% of the frame is a calm low-detail area (captions and "
        "app interface will cover it); extend the scenery naturally past every edge (room for slow push-in and pan).")
BG_SHEET = "plain flat light neutral-grey studio background, even soft frontal lighting, identical light on every figure, no dramatic shadows"
BG_CUT = "plain flat medium slate-blue background, evenly lit, no shadows on the background"
L169, P916 = "LANDSCAPE_16_9", "PORTRAIT_9_16"
J_SAYFA, M_SAYFA = "MAHajKKbhbM", "MAHajPZXWbU"  # J-A, M-A kabul (2026-11-10)
ORAN = {L169: "16:9 landscape.", P916: "Vertical 9:16 portrait."}

def sheet(lock, ad, oran=L169, yerlesim=None):
    yer = yerlesim or ("LAYOUT: left 40% of the image is a full-body turnaround in a relaxed neutral standing pose, arms down at the "
        "sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. Right 60% "
        "is a neat 3 x 2 grid of six head-and-shoulders portraits, all the same size and same front-facing angle, showing: neutral, "
        "warm smile, surprised, worried, excited, thoughtful (hand on chin only in thoughtful).")
    return (f"{STYLE}\n{lock}\nCHARACTER MODEL SHEET of {ad} only, one character, nobody else. {yer} Same face, same hair, same "
            f"outfit, same colors and same proportions in every figure; only the facial expression changes in the portraits.\n"
            f"BACKGROUND: {BG_SHEET}.\n{NOTXT} {ORAN[oran]}")

def taban(lock, ad, yon):
    return (f"{STYLE}\n{lock}\nThe reference image is the model sheet of {ad}; the face, hair and outfit must match it exactly.\n"
            f"SHOT: waist-up portrait of {ad} alone, body and head turned about 20 degrees toward frame-{yon}, eyes looking toward "
            f"frame-{yon} at someone just off-screen at eye level, relaxed neutral expression, mouth gently closed, arms relaxed and "
            f"out of frame below; top of the head at 18% of the frame height, body continues past the bottom edge, centered.\n"
            f"BACKGROUND: {BG_CUT}.\n{NOTXT} {ORAN[P916]}")

def edit(ad, kiyafet, degisim):
    return (f"EDIT the first reference image. Keep EVERYTHING identical: same man ({ad}), same face, same hair, same {kiyafet}, "
            f"same framing and camera distance, same body position, head stays in exactly the same place and angle, same eye "
            f"direction, same plain slate-blue background, same lighting and same stylized 3D render style. The second reference "
            f"is the character model sheet; the face must match it. ONLY CHANGE: {degisim} No text, no logos. {ORAN[P916]}")

def plate(sahne, isik):
    return f"{STYLE_SET}\nSCENE: {sahne}\nLIGHT: {isik}\n{NOPPL}\n{SAFE}\n{NOTXT} {ORAN[P916]}"

J_KIY = "navy hoodie with grey drawstrings, same stubble"
M_KIY = "open red-and-black buffalo-check flannel over the white T-shirt, rolled sleeves, clean-shaven face"
AGIZ = ("mouth open mid-word in a relaxed talking shape: jaw dropped slightly, lips in a soft open oval, a little of the upper "
        "teeth visible, NOT smiling, NOT shouting; the rest of the face (eyes, eyebrows, cheeks) unchanged.")

C = []
def ekle(i, grup, sira, refs, ar, prompt, not_=""):
    C.append(dict(id=i, grup=grup, sira=sira, refs=refs, ar=ar, prompt=prompt, not_=not_))

# 1 karakter sayfaları
ekle("J-A", "Jake sayfası", "1 (dalga 1)", "yok", L169, sheet(JAKE, "Jake Miller"), "tek görselde dönüş + 6 ifade (iç tutarlılık aynı üretimde)")
ekle("M-A", "Mike sayfası", "1 (dalga 1)", "yok", L169, sheet(MIKE, "Mike Carter"), "J-A ile paralel")
_TURN = ("LAYOUT: full-body turnaround only, three figures side by side, large and evenly spaced, relaxed neutral standing pose, arms "
         "down at the sides: front view, exact side profile facing right, back view; all three the same height, feet on one baseline. "
         "No expression portraits.")
ekle("J-B", "Jake sayfası", "yedek-1 (J-A elenirse)", "yok", L169, sheet(JAKE, "Jake Miller", yerlesim=_TURN),
     "bölünmüş yol: önce yalnız dönüş (yüz daha büyük), ifadeler sonra J-B2 düzenlemesiyle")
ekle("J-B2", "Jake sayfası", "yedek-1 devamı", "[J-B kazanan]", L169,
     "EDIT the reference image into an expression sheet of the same man: keep the same face, hair, stubble, navy hoodie, render style, "
     "background and lighting. Replace the three full-body figures with a neat 3 x 2 grid of six head-and-shoulders portraits, all the "
     "same size and front-facing angle, showing: neutral, warm smile, surprised, worried, excited, thoughtful (hand on chin only in "
     "thoughtful). Only the facial expression changes. " + NOTXT + " 16:9 landscape.", "yalnız J-B seçilirse")
ekle("M-B", "Mike sayfası", "yedek-1 (M-A elenirse)", "yok", L169, sheet(MIKE, "Mike Carter", yerlesim=_TURN), "J-B ile aynı mantık; ifadeler M-B2 = J-B2 metni, 'navy hoodie' yerine 'open buffalo-check flannel over white T-shirt'")
_DIK = ("LAYOUT: top half is a full-body turnaround (front view, exact side profile facing right, back view, same height, one "
        "baseline); bottom half is a 3 x 2 grid of six head-and-shoulders portraits, same size and angle: neutral, warm smile, "
        "surprised, worried, excited, thoughtful.")
ekle("J-C", "Jake sayfası", "3 (yalnız A ve B ikisi de kalırsa)", "yok", P916, sheet(JAKE, "Jake Miller", P916, _DIK), "dikey sayfa; figürler küçük → yüz ölçümü zayıf")
ekle("M-C", "Mike sayfası", "3 (yalnız A ve B ikisi de kalırsa)", "yok", P916, sheet(MIKE, "Mike Carter", P916, _DIK), "")

# 2 ikili
ekle("D-A", "İkili", "1 (dalga 2)", f"[{J_SAYFA}, {M_SAYFA}]", P916,
     f"{STYLE}\n{JAKE}\n{MIKE}\nThe first reference is Jake's model sheet, the second is Mike's model sheet; both faces, hair and outfits "
     f"must match their sheets exactly.\nSHOT: full-body two-shot of the two friends standing side by side facing the camera with a small "
     f"gap between them (not touching, not overlapping): Jake on the left, hands in his hoodie pocket, small calm smile; Mike on the right, "
     f"slightly taller, hands on his hips, big confident grin. Both full figures visible from shoes to hair with margin around them, feet "
     f"on one baseline at 88% of the frame height.\nBACKGROUND: {BG_SHEET}.\n{NOTXT} {ORAN[P916]}",
     "boy/oran referansı + kesilebilir (zeminde ayrı iki figür)")
ekle("D-B", "İkili", "2", f"[{J_SAYFA}, {M_SAYFA}]", P916,
     f"{STYLE}\n{JAKE}\n{MIKE}\nThe first reference is Jake's model sheet, the second is Mike's; faces, hair and outfits must match exactly.\n"
     f"SHOT: waist-up two-shot, the friends standing shoulder to shoulder with a small gap, turned slightly toward each other, Mike on the "
     f"right mid-laugh pointing a thumb at Jake, Jake on the left raising one eyebrow; heads at the same height band (top of heads at 20% "
     f"of the frame), bodies continue past the bottom edge.\nBACKGROUND: {BG_CUT}.\n{NOTXT} {ORAN[P916]}",
     "diyalog iki-çekimi tabanı; D-A geçerse yalnız yedek hakla")
ekle("D-C", "İkili", "3 (mekânlar kilitlendikten sonra, isteğe bağlı)", f"[<G kazanan>, {J_SAYFA}, {M_SAYFA}]", P916,
     f"{STYLE}\n{JAKE}\n{MIKE}\nThe first reference is the garage set; keep the set, camera and light. The second and third references are "
     f"Jake's and Mike's model sheets; faces, hair and outfits must match exactly.\nSHOT: the two friends standing in the open center of the "
     f"garage, Jake on the left, Mike on the right, full figures, facing camera.\n{NOTXT} {ORAN[P916]}",
     "3 referans bağlayıcıda denenmedi (risk); afiş/tanıtım görseli")

# 3 mekânlar
G_A = ("the friends' home base: a lived-in suburban two-car garage seen from inside, looking toward a half-open roll-up garage door at "
       "the back that shows a sunny driveway and a strip of blue sky. Concrete floor with a few faint old oil stains. Left wall: long "
       "wooden workbench with a pegboard of hand tools, a clamp work lamp. Right wall: grey metal shelving with plain unmarked cardboard "
       "boxes and secondhand finds (an old bicycle, a vintage radio, a desk lamp, a box fan). Back left corner: a worn mustard-yellow "
       "armchair. A blank whiteboard leaning on the shelves. Center floor kept clear.")
ekle("G-A", "Garaj (incil L4, bölüm 11+)", "bölüm 11 öncesi", "yok", P916, plate(G_A,
     "cool daylight spilling in from the garage door, warm light from the clamp lamp and a string of warm bulbs across the ceiling beams."))
ekle("G-B", "Garaj (incil L4, bölüm 11+)", "bölüm 11 öncesi (B)", "yok", P916, plate(
     "the same kind of lived-in suburban garage, reverse angle: looking at the inner back wall with a long wooden workbench, a pegboard "
     "of hand tools, a large blank whiteboard mounted above the bench, plain unmarked cardboard boxes stacked at the sides, an old bicycle "
     "hanging on wall hooks, a worn mustard-yellow armchair at the right. Center floor kept clear.",
     "cool fluorescent tube light from above, warm pool from a clamp lamp on the workbench."), "plan/oy sahneleri için (beyaz tahtaya KOD yazı)")
ekle("G-C", "Garaj (incil L4, bölüm 11+)", "sonraki ay (gece sürümü)", "[G kazanan]", P916,
     "EDIT the reference image. Keep the same garage, same camera, same objects and same 3D render style. ONLY CHANGE: it is night; "
     "the garage door shows a dark blue night sky, the warm ceiling bulbs and the clamp lamp are the main light, deeper cool shadows. "
     "No people. " + NOTXT + " Vertical 9:16 portrait.", "kriz/gece bölümleri; 12'lik pakete dahil değil")
P_A = ("a sunny American suburban residential street on a Saturday morning, seen from the sidewalk at eye level, the street and "
       "sidewalk receding into the distance. Modest one-story houses with trees; on several front lawns and driveways stand garage-sale "
       "folding tables full of secondhand items (table lamps, a toaster, vinyl records in plain sleeves, toys, old electronics, a "
       "clothes rack, a bicycle leaning on a table). Price stickers are blank colored dots. The sidewalk in the center is clear.")
ekle("P-A", "Garage sale sokağı (incil L3)", "L3 gerekince (B)", "yok", P916, plate(P_A,
     "bright warm morning sun from the side, cool blue shade under the trees and on the far houses."))
ekle("P-B", "Garage sale sokağı (incil L3)", "L3 gerekince ilk", "yok", P916, plate(
     "a single suburban driveway garage sale up close: an open garage behind, two long folding tables in an L shape covered with "
     "secondhand items (lamps, a toaster, an old game console with no logos, records in plain sleeves, a box of tools, a clothes rack), "
     "a blank cardboard sign on an easel, blank colored-dot price stickers. The driveway space in front of the tables is clear.",
     "warm morning sun, cool blue shadow inside the open garage."), "pazarlık sahneleri (alıcı-satıcı)")
A_A = ("inside the friends' old, well-loved compact car (a generic early-2000s hatchback, no brand badges), camera mounted on the dashboard "
       "looking back at the two empty front seats side by side, steering wheel at the lower left foreground edge, worn grey fabric seats "
       "with headrests, a coffee cup in the holder, a phone mount without a phone, a small crack in the dashboard plastic. Through the rear "
       "and side windows: a passing suburban street, slightly blurred.")
ekle("A-A", "Arkadaşların arabası (incil L2)", "bölüm gerektirince", "yok", P916, plate(A_A,
     "warm late-afternoon sun through the side windows, cool shade inside the cabin roof."),
     "iki koltuk iki-çekim; bel üstü kesikler koltuk önüne, alt gövdeyi ön konsol/direksiyon örter")
ekle("A-B", "Arkadaşların arabası (incil L2)", "bölüm gerektirince (B)", "yok", P916, plate(
     "inside the same kind of old compact hatchback (no brand badges), camera on the passenger side dashboard looking at the empty "
     "driver seat alone, steering wheel in the lower foreground, driver side window showing a passing suburban street slightly blurred, "
     "worn grey fabric seat, a coffee cup in the holder.",
     "warm late-afternoon sun through the side window, cool shade on the roof liner."), "tek çekim (Mike sürerken)")
K_A = ("a small rented apartment kitchen-dining nook in the evening, camera at seated eye level directly across a simple square "
       "wooden table: the tabletop runs across the bottom 30% of the frame and continues past the bottom edge; on it only a closed laptop "
       "at one side, two mugs and a notepad with blank pages. Behind the table the central area is open, no chairs visible there (seated "
       "characters will be composited later, their lower bodies hidden by the table). Background: compact kitchen counters with a "
       "few dishes, an open shelf with plain jars, a small window showing a dusky blue city sky with soft distant lights.")
ekle("K-A", "ESKİ mutfak masası (incil L1 ile değişti)", "kullanma", "yok", P916, plate(K_A,
     "warm pendant lamp hanging above the table, cool blue dusk light from the window."),
     "masa üstü kadraj %62–75'te (Leo dersi): bel üstü kesik masa arkasına oturur, 0 ek üretim")
ekle("K-B", "ESKİ mutfak masası (incil L1 ile değişti)", "kullanma", "yok", P916, plate(
     "the same kind of small apartment kitchen-dining nook in the evening, establishing three-quarter high angle: a simple square "
     "wooden table with two mismatched empty chairs, a closed laptop, two mugs, a notepad with blank pages, compact kitchen counters, an "
     "open shelf with plain jars, a small window with a dusky blue city sky.",
     "warm pendant lamp above the table, cool blue dusk light from the window."), "kuruluş çekimi")

# 4 L1 THE KITCHEN (seri incili §2; bölüm 1'in tek mekânı)
L1_SAFE = ("VERTICAL 9:16 FRAME RULES: camera at natural eye level; the front edge of the countertop sits at 68-72% of the frame height "
           "and the counter continues past the bottom edge; the central 60% of the width between 22% and 70% of the frame height is open "
           "kitchen space (two waist-up characters will be composited standing behind the counter, their lower bodies hidden by it); busy "
           "detail only at the sides and top; extend the scenery naturally past every edge (room for slow push-in and pan).")
L1_ORTAK = ("a small, lived-in American apartment kitchen, the friends' home base, on a bright morning: muted blue-grey cabinets, a "
            "light wood countertop, a small window with soft morning sky and a fire escape outside, a tall white fridge with a large "
            "blank white dry-erase board on its door")
def l1(sahne, kural):
    return (f"{STYLE_SET}\nSCENE: {sahne}\nLIGHT: warm morning sun from the window, soft cool fill in the shadows.\n{NOPPL}\n{kural}\n"
            f"{NOTXT} The whiteboard is completely blank. {ORAN[P916]}")
ekle("L1-A", "L1 Mutfak · A geniş tezgâh ikili", "1 (bölüm 1)", "yok", P916, l1(
     L1_ORTAK + ". Camera across the breakfast counter at standing chest height, straight-on. The countertop runs across the bottom of "
     "the frame and is clear except a ceramic mug and a small fruit bowl at the far left edge. Behind it: open kitchen floor space, the "
     "stove and cabinets, the window on the left, the fridge with the blank whiteboard at the right edge.", L1_SAFE),
     "S1, S3–S8; masa/tezgâh dersi: bel üstü taban kesiği tezgâh arkasına oturur")
ekle("L1-B", "L1 Mutfak · B buzdolabı tahtası", "2 (bölüm 1)", "yok", P916, l1(
     L1_ORTAK + ". Closer angle on the fridge: the fridge door fills the right half of the frame; the large blank white whiteboard is "
     "mounted on it with its top at 18% and bottom at 58% of the frame height, a marker on a small tray, a few plain round magnets. The "
     "left half is an open area of kitchen wall and counter edge where one waist-up character will be composited.",
     "VERTICAL 9:16 FRAME RULES: camera at natural eye level, straight-on to the fridge door (whiteboard not skewed, flat rectangle); "
     "bottom 25% of the frame is calm low-detail lower fridge and floor; extend the scenery past every edge."),
     "S2, S4 tahta; yazılar KOD (THE BOARD, $100, $1,000,000)")
ekle("L1-C", "L1 Mutfak · C tezgâh insert", "3 (önce KOD: L1-A tezgâh kırpımı + büyütme; yetmezse)", "yok", P916, l1(
     "extreme close-up of the light wood countertop of " + L1_ORTAK[2:] + ". Low camera just above the counter surface, shallow depth of "
     "field: the counter surface fills the lower 60% of the frame with an empty clear spot in the center (a hand and a bill will be "
     "composited there later), a ceramic cereal bowl with a spoon at the right edge, the kitchen and window softly blurred behind.",
     "VERTICAL 9:16 FRAME RULES: keep the empty counter spot between 45% and 70% of the frame height, centered; extend past every edge."),
     "S1 SLAM insert, S7 banknot yakın; banknot KOD")

# 5 konuşma tabanı + ağız
ekle("T-J", "Konuşma tabanı Jake", "1 (dalga 2)", f"[{J_SAYFA}]", P916, taban(JAKE, "Jake Miller", "right"), "Mike'a bakar (kadraj sağı); ikili kadrajda Jake solda")
ekle("T-M", "Konuşma tabanı Mike", "1 (dalga 2)", f"[{M_SAYFA}]", P916, taban(MIKE, "Mike Carter", "left"), "Jake'e bakar (kadraj solu); ikili kadrajda Mike sağda")
ekle("AG-J", "Ağız açık Jake", "1 (dalga 3)", f"[<T-J media>, {J_SAYFA}]", P916, edit("Jake", J_KIY, AGIZ), "tek görsel: açık durum; ara kare KOD alfa karışımı")
ekle("AG-M", "Ağız açık Mike", "1 (dalga 3)", f"[<T-M media>, {M_SAYFA}]", P916, edit("Mike", M_KIY, AGIZ), "")
ekle("GK-J", "Göz kırpma Jake", "yedek-2", f"[<T-J media>, {J_SAYFA}]", P916,
     edit("Jake", J_KIY, "both eyelids fully closed in a natural blink, eyebrows relaxed, mouth unchanged."), "yedek hak kalırsa")

YASAK = ["pixar", "dreamworks", "disney", "illumination entertainment", "sony pictures", "#"]
def kontrol(c):
    h = []
    p, low = c["prompt"], c["prompt"].lower()
    for y in YASAK:
        if y in low: h.append(f"yasak: {y}")
    if c["ar"] == P916 and "9:16" not in p: h.append("oran cümlesi yok")
    if c["ar"] == L169 and "16:9" not in p: h.append("oran cümlesi yok")
    if "Jake" in c["grup"] or c["grup"] == "İkili":
        if not p.startswith("EDIT") and c["grup"] != "İkili" and JAKE not in p: h.append("JAKE kilidi birebir değil")
    if "Mike" in c["grup"] and "arabası" not in c["grup"] and not p.startswith("EDIT") and MIKE not in p: h.append("MIKE kilidi birebir değil")
    if c["grup"] == "İkili" and not (JAKE in p and MIKE in p): h.append("ikili kilit eksik")
    if (c["id"][0] in "GPAK" or c["id"].startswith("L1")) and not p.startswith("EDIT") and NOPPL not in p: h.append("NOPPL yok")
    if not p.startswith("EDIT") and "STYLE LOCK" not in p: h.append("stil kilidi yok")
    return h

def negatif():
    import copy
    c = copy.deepcopy(next(x for x in C if x["id"] == "J-A")); c["prompt"] = c["prompt"].replace("navy-blue", "black") + " like Pixar"
    h = kontrol(c); assert "JAKE kilidi birebir değil" in h and "yasak: pixar" in h, h
    c = copy.deepcopy(next(x for x in C if x["id"] == "G-A")); c["prompt"] = c["prompt"].replace(NOPPL, "").replace("9:16", "")
    h = kontrol(c); assert "NOPPL yok" in h and "oran cümlesi yok" in h, h
    print("negatif test GEÇTİ (4 bozulma yakalandı)")

if __name__ == "__main__":
    if "--negatif" in sys.argv: negatif(); sys.exit()
    hata = {c["id"]: kontrol(c) for c in C if kontrol(c)}
    if hata: print(hata); sys.exit(1)
    out = []
    for c in C:
        out.append(f"### {c['id']} · {c['grup']} · sıra {c['sira']}\n- aspectRatio: `{c['ar']}` · referans: {c['refs']}"
                   f"{(' · not: ' + c['not_']) if c['not_'] else ''} · {len(c['prompt'])} karakter\n```\n{c['prompt']}\n```\n")
    hedef = open(sys.argv[1]).read()
    bas, son = "<!-- PROMPTLAR:BAŞ -->", "<!-- PROMPTLAR:SON -->"
    yeni = re.sub(re.escape(bas) + ".*?" + re.escape(son), lambda m: bas + "\n" + "\n".join(out) + son, hedef, flags=re.S)
    open(sys.argv[1], "w").write(yeni)
    print(f"{len(C)} prompt yazıldı, kontrol 0 hata")
