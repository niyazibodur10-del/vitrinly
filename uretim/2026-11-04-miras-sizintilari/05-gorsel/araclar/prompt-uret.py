#!/usr/bin/env python3
"""canva-promptlari.md üretici · S03 Miras sızıntıları / Leaky Moving Truck (gorsel-varlik-sanatcisi, 2026-11-04).
S08 sürümünden türetildi: kilit blokları karakter kartından BİREBİR alınır (elle kopyalama kayması yok).
Değişen: id öneki M; Leo düzenlemelerinde bakış/yüz kilidi (hafıza 2026-11-02: "eyes glance down" yüzü bozuyor) +
kıyafet ek yasağı (nakliye yeleği metinde var ama kart "Outfit never changes" → yelek/şapka/eldiven yok);
thumbnail Leo pozları aynı üretimden (kafa sabit → thumb-uret kafa değişimi). Banknot = KOD SVG (hiç üretilmez).
Kullanım: python3 -I prompt-uret.py ../canva-promptlari.md"""
import re, sys, pathlib
KOK = pathlib.Path(__file__).resolve().parents[4]
kart = (KOK / "assets/karakter/karakter-karti.md").read_text()
bloklar = re.findall(r"```\n(.*?)```", kart, re.S)
TABAN = next(b for b in bloklar if b.startswith("CHARACTER LOCK"))
EDIT_KAL = next(b for b in bloklar if b.startswith("EDIT the first reference image")).strip()
STYLE = "STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows"
assert "<tek değişiklik>" in EDIT_KAL and STYLE in TABAN
SAYFA, TABAN_ID, C01 = "MAHZHpeQGdM", "MAHZHqW0_Uo", "MAHZMVzdpqQ"
DUZ = "flat colors, simplified shapes, minimal texture, NOT painterly, NOT photorealistic, consistent line weight, the look of a 2D animated TV-series background"
NOTXT = "No text, no letters, no numbers, no signage, no logos, no banknotes, no flags, no watermark."
NOPPL = "EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt."
TASMA = "Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom)."
BOS_ZEMIN = "plain flat slate-blue background (#3E5A7E), evenly lit, no shadows on the wall"
# Leo düzenleme sabitleri (rig ağız/göz yamaları + yüz tutarlılığı)
YUZ = ("his head stays in exactly the same place, size and angle; head, face, eye direction and mouth exactly the same as the first reference "
       "(eyes looking straight at the camera, mouth closed and neutral); torso stays in the same place")
KIYAFET = "no vest, no hat, no gloves, no jacket"
SAAT = "the black wristwatch on his left wrist stays visible"
KUTU_RENK = {"red": "brick-red (#B4452F)", "navy": "navy-blue (#2B4A7C)", "green": "leaf-green (#3C8C55)"}

def edit(degisim):
    return EDIT_KAL.replace("<tek değişiklik>", f"{degisim}; {YUZ}; {SAAT}; {KIYAFET}")

def plaka(sahne, isik, ekstra="", oran="16:9 landscape.", tasma=TASMA):
    return (f"{STYLE}, {DUZ}.\nSCENE: {sahne}\nLIGHT AND PALETTE: {isik}\n{NOPPL}{(' ' + ekstra) if ekstra else ''}\n"
            f"{tasma}\n{NOTXT} {oran}")

def prop(nesneler, duzen="Objects are evenly spaced in one row"):
    return (f"{STYLE}, {DUZ}.\nPROP SHEET: {nesneler} {duzen} with clear empty background between them, "
            f"nothing overlapping, nothing touching the frame edges, front-on product-sheet layout, warm soft key light, only a faint contact shadow.\n"
            f"BACKGROUND: {BOS_ZEMIN}.\n{NOPPL}\n{NOTXT} 16:9 landscape.")

L169, P916 = "LANDSCAPE_16_9", "PORTRAIT_9_16"
K_LEO = ("`tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4 "
         "(rig ağız/göz yamaları aynı konuma oturmalı; `araclar/rig-yama.py` hizası + 4× ağız yakın planı göz incelemesi), ölçek farkı ≤%10; "
         "kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); "
         "bakış kamerada, ağız kapalı nötr; yelek/şapka/eldiven/ceket yok; M4 kesme artığı ≤0.01, saçak ≤150 px")
K_PLAKA = ("1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 + 2× kırpım incelemesinde harf/rakam/logo/tabela yazısı/banknot/bayrak yok; "
           "önemli öğe merkez %80'de; `araclar/stil-olcum.py` düzlük ≥%50, doku std ≤2,0 (S08 G01 64,1 / 0,92); Leo `a` kesiği bindirmesinde siyah gömlek arkası L ≥70 "
           "(S08: 77 geçti, 67 zayıf) ve ışık uyumu (soğuk zemin + sıcak karakter)")
K_PROP = ("düz slate-blue zemin (köşe zemin ΔE yayılımı <6); nesneler birbirine ve kenara değmez; 1:1 + 2× incelemede yazı/rakam/logo/plaka yazısı yok; "
          "nesne başına kırpıp M4 (`araclar/kes-m4.py`, tek görselde yalnız en büyük bileşeni tutar): artık ≤0.01, saçak ≤150 px; düzlük ≥%50")

C = []
def ekle(i, ad, oncelik, tur, refs, kullanim, kabul, prompt, ar=L169, not_="", dalga="1a"):
    C.append(dict(id=i, ad=ad, oncelik=oncelik, tur=tur, refs=refs, kullanim=kullanim, kabul=kabul, prompt=prompt, ar=ar, not_=not_, dalga=dalga))

LEO_REF = f"[{TABAN_ID}, {SAYFA}]"
TRUCK = ("a medium-size box moving truck with a warm orange (#E8782A) cargo box and a matching orange cab, dark grey bumpers, black tyres, "
         "round headlights; plain smooth panels with no brand, no writing, no stripes with text, and a blank licence plate")

# ================= Dalga 1a · F5 kritik yol (H4: bant gag + damlama) + thumbnail Leo pozları · bağımlılık yok =================
ekle("M01", "Kamyon nesne sayfası (yan kapalı, arka kapılar açık, arka kapalı)", "P0", "PROP nesne sayfası", "yok",
     "Tekrarlanan set öğesi: S01/S26 arka kapılar açık, S07/S13/S21/S29 yolda yan görünüş (KOD hareket + yansıtma serbest: kamyonda yazı/saat yok), "
     "S04 sapma, S27/S28 hayalet kamyon ve konvoy (KOD saydamlık/tekrar), Shorts 1 dikey dönüş",
     K_PROP + "; üç görünüşte aynı turuncu (Lab ΔE ≤6 birbirine), plaka boş, logo/şerit yazısı yok; açık kasa içi boş ve sıcak aydınlık (dev kutu KOD ile yerleşir)",
     prop(f"three separate views of the same vehicle, {TRUCK}: (1) side view facing right, all doors closed; (2) rear view with both rear swing doors opened wide "
          "to the sides, the empty cargo bay visible inside with plain plywood walls and a warm interior light; (3) rear view with both rear doors closed.",
          duzen="The three views are evenly spaced in one row"),
     not_="Kamyon tek kaynak: tüm sahnelerde aynı kesik kullanılır (sahne başına ayrı kamyon üretmek tutarlılığı bozar). M10 bu görselin media id'sini referans alır.")
ekle("M02", "Taşıma kutuları sayfası (3 sabit renk + yarık dipli + açık)", "P0", "PROP nesne sayfası", "yok",
     "Okafor'un 10 kutusu (KOD çoğaltma; kiremit HOUSE ×4, lacivert RETIREMENT ×4, yeşil BANK ×2), 'TO: THE KIDS' etiketi KOD yazı; S01 dev kutu (ölçek), "
     "S08 açılan kutu, S12/S20 yarık köşe (KOD damlama kaynağı), S19 kiremit kutular, S26 varış; thumbnail K3 büyük/küçük kutu",
     K_PROP + f"; renkler metindeki sabitlere yakın (Lab ΔE ≤12: kiremit #B4452F, lacivert #2B4A7C, yeşil #3C8C55; aşarsa KOD Lab renk eşleme); "
              "ön yüzler düz ve boş (KOD etiket alanı ≥ 260x160 px)",
     prop(f"five separate cardboard moving boxes of the same size and shape, each seen from a slight three-quarter front angle: "
          f"(1) a closed {KUTU_RENK['red']} painted cardboard box; (2) a closed {KUTU_RENK['navy']} painted cardboard box; "
          f"(3) a closed {KUTU_RENK['green']} painted cardboard box; (4) a closed {KUTU_RENK['red']} box whose bottom front corner is split open with a small dark gap "
          f"and a sagging soft bottom; (5) an open {KUTU_RENK['navy']} box with its top flaps folded outward, empty inside. "
          "Every box has a flat plain front face, completely blank: no writing, no labels, no arrows, no symbols, no logos, no tape markings."))
ekle("M03", "Küçük nesneler sayfası (bant rulosu dolu/ince, pano, keçeli, büyüteç)", "P0", "PROP nesne sayfası", "yok",
     "S09 bant rulosu, S12/S20 bant sayacı yanındaki rulo (KOD incelir), S30 ince rulo; Leo panosu boş yüz (6 durak satırı KOD); S06 keçeli; S04 büyüteç "
     "(M17 seçmeli Leo pozu yoksa KOD ile Leo'nun eline bindirilir)",
     K_PROP + "; pano kâğıdı düz beyaz ve boş (KOD 6 satır için ≥ 300x380 px), bant kahverengi koli bandı (M05/M07 elindeki bantla Lab ΔE ≤10)",
     prop("five separate objects: (1) a big full roll of shiny brown packing tape; (2) the same kind of roll almost used up, very thin, mostly the cardboard core visible; "
          "(3) a brown hardboard clipboard with a silver clip holding one blank white sheet of paper, seen straight from the front; (4) a thick black felt-tip marker "
          "with its cap off; (5) a round magnifying glass with a dark wooden handle. The paper is completely blank: no lines, no writing.")),
ekle("M04", "Leo panoyu göğüs hizasında tutar (nakliye şefi ana pozu)", "P0 (kilit poz)", "CV-L düzenleme (kol değişimi)", LEO_REF,
     "En çok kullanılan konuşma pozu: S01 panoyu kaldırır, S03 tanıtım + tez, S07 6 durak, S18 sayım, S22, S26 varış envanteri (KOD satır üstü çizgi); "
     "thumbnail K3 (envanter listesi; şüpheli ifade = thumb-uret kafa değişimi)",
     K_LEO + "; pano kâğıdı düz, boş, kameraya dönük (KOD 6 satır: LIVING · CARE · SPOUSE · GIVING · HOUSE · TAX & TIME); pano kafayla çakışmaz (üst kenar çene altında)",
     edit("he holds a brown hardboard clipboard with both hands at chest height, tilted slightly toward the camera so its blank white sheet faces the viewer; "
          "the sheet is completely blank with no writing and no lines; the clipboard stays below his chin and does not cover his face"),
     not_="Kafa sabit → rig ağız/göz yamaları konuşmada aynen çalışır (S08 G05: kor. 0,97, kayma <1 px). Metindeki 'nakliye yeleği' kart kilidi nedeniyle UYGULANMAZ; rol pano + bant + kamyonla anlatılır.")
ekle("M05", "Leo kutu köşesini bantlar (bant gag'i)", "P0 (kilit poz)", "CV-L düzenleme (kol değişimi)", LEO_REF,
     "S12 bakım kutusu (yeşil; S11 'ESTATE RECOVERY' kutusuyla aynı, sayım tutarlı: kalan 6 = 2 lacivert + 4 kiremit), S20 üçüncü köşe (KOD Lab ton kaydırma "
     "yeşil → kiremit, kutu maskesi renkten), F5 kritik yol testi; thumbnail K4 (kafa değişimi + KOD banknot)",
     K_LEO + "; kutu yeşil (#3C8C55'e Lab ΔE ≤12), yazısız; bant şeridi kutunun üst ön köşesinde; kutu alt kenardan taşar (bel üstü kadraj korunur); "
             "eller ve rulo yüze değmez",
     edit(f"a closed {KUTU_RENK['green']} cardboard moving box stands in front of him at the bottom of the frame, its lower part cut off by the bottom edge; "
          "with his left hand he holds a big roll of brown packing tape and with his right hand he presses a fresh strip of brown tape across the top front corner "
          "of the box; the box is completely blank with no writing"),
     not_="Damlayan para görselde YOK: banknot = KOD SVG parçacık (H4 B planı aynı zamanda ana plan; metin RED'inde görsel değişmez, gerçek para tasarımı riski yok).")
ekle("M06", "Leo kiremit kutuyu göğsünde tutar, kutunun dip köşesi yarık", "P0 (kilit poz)", "CV-L düzenleme (kol değişimi)", LEO_REF,
     "S01/S12 damlama anı (KOD banknot yarıktan düşer), S17 kutuyu kime vereceğini bilemez, S27; **thumbnail K1** (kafa değişimi `d-saskin` + KOD damlama)",
     K_LEO + "; kutu kiremit (#B4452F'e Lab ΔE ≤12), yazısız; sağ alt köşe yarığı görünür ve kol/elle örtülmez (KOD damlama çıkış noktası); kutu çene altında",
     edit(f"he holds a closed {KUTU_RENK['red']} cardboard moving box against his chest with both arms, the top of the box below his chin; the bottom right corner "
          "of the box is split open with a small dark gap and a sagging soft bottom, nothing falling out; the box is completely blank with no writing"),
     not_="B planı (kalırsa): 1929 `leo/C14-kutu-gogus.png` (kor. 0,94, düz kraft kutu) + KOD yarık + Lab renk eşleme. Ölçüm C14 ile yan yana.")
ekle("M07", "Leo neredeyse bitmiş bant rulosunu omuz hizasında gösterir", "P0 (kilit poz)", "CV-L düzenleme (kol değişimi)", LEO_REF,
     "S30 kapanış repliği 'I'm going to need more tape' (H4 karakter anı), S09 rulo sallama (KOD salınım), S03 omuzda bant",
     K_LEO + "; rulo ince (karton göbek belirgin), omuz hizasında ve yüzün dışında (kafa bölgesiyle kesişim 0 px)",
     edit("his right hand holds up an almost used-up roll of brown packing tape (very thin, mostly the cardboard core visible) at shoulder height beside his right "
          "shoulder, showing it to the camera; the roll stays clear of his face; his left arm stays down as before"))
ekle("M08", "Akşam yolu geniş plan (ana yol plakası)", "P0", "CV-A karaktersiz plaka", "yok",
     "Sabit set 'soğuk mavi akşam yolu': S01 (kamyon kesiği + Leo bindirme = hook adayı A), S07 6 durak tabelası (KOD), S09 sis (KOD), S13 kavşak/sinyal, "
     "S15, S23 yol saati (M16), S25 son viraj, S29 (KOD kesik çizgi); 9:16 orta şerit Shorts 1 B planı",
     K_PLAKA + "; yol kenarı (sol üçte bir) düz ve boş (KOD tabelalar), yolda araç yok; ufuk çizgisi y %40–50; kamyon kesiği (M01) ölçeğine uygun şerit genişliği",
     plaka("a quiet two-lane country road at blue dusk on the edge of a small town, wide shot from the road shoulder at standing eye level. The road starts wide "
           "in the lower foreground and curves gently toward the horizon on the right. The left third of the frame is a flat, empty grassy road shoulder "
           "(road signs will be added later). Low rolling hills, a few far-away small houses with warm lit windows and a line of bare roadside trees near the horizon. "
           "The road surface is empty: no cars, no trucks.",
           "cool deep-blue and teal dusk sky with a thin band of warm orange glow at the horizon; cool blue-grey road and fields; small warm window lights; "
           "gentle contrast, cinematic."))
ekle("M09", "Kamyon kasasının içi (bant gag'i seti)", "P0", "CV-A karaktersiz plaka", "yok",
     "S12 bant gag'i (F5 kritik yol: Leo M05 alt kenardan kesik, yeşil kutu önünde), S18 kalan 6 kutu (KOD dizilir), S20 üçüncü köşe",
     K_PLAKA + "; orta %40 genişlik bel üstü yüksekliğinde boş (Leo bindirmesi), zemin alt kenardan taşar; arka kapı açıklığında yalnız mavi akşam yolu; "
              "lamba/kiriş Leo kafasıyla çakışmaz (kafa bölgesi x 620–1060, y 40–330 sade)",
     plaka("inside the empty cargo bay of a moving truck, seen from the front of the cargo bay looking toward the open rear doors. Plain light plywood walls "
           "with horizontal wooden slats and a few loose grey moving blankets folded on the floor at the sides; a single warm caged ceiling lamp near the front. "
           "The plywood floor runs past the bottom edge of the frame. The central 40% of the width is open and uncluttered from the floor up "
           "(a character will be composited there later). Through the open rear doors at the back: a cool blue dusk road and sky.",
           "warm amber interior light on the walls and the open centre; cool blue dusk light coming through the rear doors; cool background, warm centre; cinematic."))
# ================= Dalga 1b · rakamsız, RED riski düşük sahneler (M10 ← M01) =================
ekle("M10", "Gece yolu: kamyon arka kapıları açık (hook entegre plaka)", "P0 (aday)", "CV-A karaktersiz plaka", "[MAHZ9uk7YSQ] (M01 kamyon sayfası; yalnız kamyon tasarımı)",
     "S01 HOOK ilk 3 sn (aday B; aday A = M08 + M01 kesiği), S03 Leo kamyon kapısında, S26 varış (kapılar açılır KOD maske)",
     K_PLAKA + "; kamyon M01 ile aynı (turuncu Lab ΔE ≤8, kapı/teker biçimi kontaktta yan yana); kasa içi boş ve sıcak (dev kutu KOD); sağ üçte bir ön plan boş "
              "(Leo M04 alt kenardan kesik); 9:16 orta şerit (x 656–1264) kasa açıklığını içerir",
     plaka(f"a quiet two-lane road at night; low camera at bumper height, straight-on behind a parked truck: the same orange moving truck as in the "
           f"reference image ({TRUCK}) stands on the road shoulder in the centre-left of the frame, seen from the rear, both rear swing doors opened wide, "
           "the empty cargo bay glowing with warm interior light. The right third of the frame is open road shoulder in the foreground (a character will be "
           "composited there later). Far hills and a few warm house lights on the horizon.",
           "cool deep-blue night road and sky; warm golden light spilling out of the open cargo bay onto the road; cool background, warm centre; cinematic.",
           "Use only the truck design from the reference image (shape and orange color); do not copy its plain background or its layout."),
     dalga="1b",
     not_="Hook 2 aday kuralı (kilit sahne): A = M08 yolu + M01 arka-açık kesiği (KOD gölge), B = bu entegre plaka. Karar: kamyon tutarlılığı (ΔE) + entegrasyon (gölge/ışık) + 168 px önizlemede okunurluk.")
ekle("M11", "Okafor evi önü, akşam (siluetler KOD)", "P1", "CV-A karaktersiz plaka", "yok",
     "S05 kapıda 4 siluet (KOD SVG, yüzsüz, 'EXAMPLE FAMILY · ILLUSTRATION'), S06 yükleme (kamyon M01 kesiği garaj yolunda), S13 karşı kaldırım, "
     "S20 genç siluet anahtarla girer, S25 ufuktaki ev (KOD ölçek), S27 kutular içeri",
     K_PLAKA + "; kapı eşiği ve verandası boş ve sıcak aydınlık (4 siluet için ≥ 360 px genişlik); garaj yolu boş; kapı numarası/posta kutusu yazısı/tabela yok "
              "(H7: satılık tabelası YOK)",
     plaka("a modest two-story suburban family house at blue dusk, seen straight-on from the street at standing eye level. A wide front porch with an open front "
           "door and a warm lit doorway in the centre; a short empty driveway on the right side leading to the street; a small front lawn and one tree. "
           "The porch and the doorway are empty and clear. No house number, no mailbox writing, no yard signs.",
           "cool blue dusk sky and cool blue-grey house walls; warm golden light from the open doorway and two windows falling on the porch; cool background, warm centre."))
ekle("M12", "Gişe 'TAX' durağı, gece (boş tabela)", "P1", "CV-A karaktersiz plaka", "yok",
     "S21 vergi durağı (ürkütücü → sakin: KOD ışık/gök gürültüsü, 'TAX' tabela yazısı KOD), bariyer kalkar (KOD bariyer maskesi), S23 gişe arkası yol saati (M16), "
     "Shorts 2 (9:16 orta şerit; altta sabit kaynak satırları için alt %35 sade)",
     K_PLAKA + "; tabela panosu büyük, düz ve boş (KOD 'TAX' için ≥ 500x150 px); bariyer kolu yazısız (yalnız kırmızı-beyaz şerit); 9:16 orta şerit (x 656–1264) "
              "kabin + bariyeri içerir",
     plaka("a lonely single-lane toll booth on a dark country road at night, seen straight-on from the approaching lane at standing eye level. A small booth on "
           "the right with a lit window, a long red-and-white striped barrier arm lowered across the lane, and a large blank rectangular sign panel mounted on a "
           "gantry above the lane (the panel is completely empty on purpose). Dark storm clouds above, the road continuing past the barrier into the distance.",
           "cool dark blue and violet night palette, slightly ominous; one warm lamp over the booth window; the empty sign panel faintly lit; cool background, warm centre."))
ekle("M13", "Gündelik yaşam nesneleri sayfası (S08/S10/S14)", "P1", "PROP nesne sayfası", "yok",
     "S08 iki lacivert kutudan çıkanlar (market poşeti, fatura, tren bileti), S10 ilaç kutusu (KOD ikon kareleriyle), S14 kum saati '+YEARS'",
     K_PROP + "; fatura ve bilet tamamen boş (rakam KOD yok — bu sahnede rakam yalnız grafik), ilaç kutusu bölmelerinde harf yok",
     prop("five separate objects: (1) a brown paper grocery bag with a baguette, leafy greens and apples sticking out; (2) a folded plain white paper bill; "
          "(3) a small plain paper train ticket; (4) a seven-compartment weekly pill organizer in soft pastel colors with closed lids; (5) an hourglass with "
          "golden sand and a dark wooden frame. All paper is completely blank: no writing, no lines, no symbols."))
# ================= Dalga 2 · metin kilidinden sonra (GÖRSEL sütunu farkına göre) =================
ekle("M14", "Koridor: iki özdeş kapı (MEDICARE / MEDICAID levhaları KOD)", "P2 (kilit sonrası)", "CV-A karaktersiz plaka", "yok",
     "S11 iki kapı mekanizması (levha yazıları ve 'ESTATE RECOVERY' etiketi KOD; eylem önerisi yok, P1/R25)",
     K_PLAKA + "; iki kapı simetrik, levhalar boş ve düz (KOD yazı için ≥ 360x90 px); bayrak/mühür/kurum amblemi yok",
     plaka("a plain, clean public-office hallway seen straight-on: two identical closed wooden doors side by side in the centre, each with a blank rectangular "
           "plaque above it (the plaques are completely empty on purpose), a pale floor and a simple bench at the far left.",
           "cool blue-grey walls and floor; soft warm light from a ceiling lamp between the two doors; cool background, warm centre."),
     dalga="2")
ekle("M15", "İsimsiz okul önü, gündüz sonu", "P2 (kilit sonrası)", "CV-A karaktersiz plaka", "yok",
     "S16 bağış durağı: yeşil kutu kapıya bırakılır (M02 kesiği), pencerelerde el sallayan siluetler KOD; okul/hastane/ibadethane eşit ikonları KOD (P2)",
     K_PLAKA + "; okul adı/tabela/bayrak direği/bayrak yok; giriş merdiveni boş (kutu + Leo için)",
     plaka("a small friendly brick schoolhouse with big windows and a short flight of front steps leading to a wide open double door, seen straight-on from the "
           "sidewalk in late afternoon; a few trees, a low fence. No school name, no sign, no flagpole.",
           "soft cool blue-grey sky and shadows; warm late-sun light on the brick front and the steps; cool background, warm centre."),
     dalga="2")
ekle("M16", "Nesne sayfası 2 (kutu-ev maketi, rakamsız yol saati, boş takvim, boş çerçeve)", "P2 (kilit sonrası)", "PROP nesne sayfası", "yok",
     "S19 bölünmeyen ev (4 kiremit kutudan ev maketi; iki siluet çeker KOD), S23 dev yol saati (kadranda rakam YOK, akrep/yelkovan KOD döner), "
     "S14 uçan takvim yaprakları, S27 aile fotoğraf çerçevesi (içi KOD siluet)",
     K_PROP + "; saat kadranı rakamsız (yalnız çentik), takvim yaprakları boş, çerçeve içi boş; maket kutuları M02 kiremit tonunda (Lab ΔE ≤10)",
     prop(f"four separate objects: (1) a small house model built from four stacked {KUTU_RENK['red']} cardboard moving boxes with a simple folded cardboard roof; "
          "(2) a tall old-fashioned roadside clock on a dark green pole, its round white face with only tick marks and two hands, no numerals; "
          "(3) a tear-off wall calendar pad with completely blank pages; (4) an empty wooden picture frame with a plain cream inside. "
          "No writing, no numbers anywhere."),
     dalga="2")
ekle("M17", "Leo büyüteçle okur (seçmeli)", "P3 seçmeli", "CV-L düzenleme (kol değişimi)", LEO_REF,
     "S04 dev kutunun etiketini okur ('FORECAST · CERULLI · DEC 2024' KOD). B planı: M04 pano pozu + M03 büyüteç KOD bindirme",
     K_LEO + "; mercek göğüs hizasında, yüzle kesişim 0 px; mercek içi düz (KOD büyütme efekti)",
     edit("his right hand holds a round magnifying glass with a dark wooden handle at chest height in front of him, the lens facing the camera and clear of his face; "
          "his left arm stays down as before"),
     dalga="2")
ekle("M18", "Dikey akşam yolu (Shorts 1, seçmeli)", "P3 seçmeli", "CV-A karaktersiz plaka (9:16)", "[MAHZ9lpnUVY] (M08 kabul edilen yol)",
     "Shorts 1 'The detour': kamyon (M01 kesiği) dikeyde yan şeride döner, sarı tabela KOD. B planı: M08 orta şerit ×1,78 (yumuşak)",
     "1080x1920'ye uygun dikey oran; ön planda insan yok; yazı yok; M08 ile aynı yol/palet (kontaktta yan yana); üst %15 ve alt %35 sade (Shorts arayüzü)",
     plaka("the same road as the reference image (same dusk palette, same hills and drawing style) in a tall vertical frame: the road runs from the bottom centre "
           "up toward the horizon and splits gently into a side lane curving to the right; empty road, no vehicles.",
           "same palette as the reference: cool deep-blue and teal dusk, thin warm orange band at the horizon.",
           oran="9:16 portrait.", tasma="Keep the top 15% and bottom 35% of the frame calm and simple (vertical video interface)."),
     ar=P916, dalga="2")

# ================= Tekrar payı 1/2 · M09 RED düzeltmesi (dalga 1b ile birlikte) =================
ekle("M19", "Kamyon kasasının içi — M09 düzeltmesi (M01 çizim diliyle)", "P0 (düzeltme 1/2)", "CV-A karaktersiz plaka", "[MAHZ9uk7YSQ] (M01 kamyon sayfası; açık kasa içinin çizim dili)",
     "M09 yerine: S12 bant gag'i (F5 kritik yol), S18 kalan 6 kutu, S20 üçüncü köşe",
     K_PLAKA + "; kontur ≥%1,0 (M01 2,1; M09 0,06 → RED nedeni), düzlük ≥%50 (M09 41,0), doku ≤1,2 (M09 1,84); ahşap damarı yok; "
              "orta %40 genişlik boş, zemin alt kenardan taşar; kafa bölgesi x 620–1060, y 40–330 sade",
     plaka("inside the empty cargo bay of the same orange moving truck as in the reference image, seen from the front of the cargo bay looking toward the open "
           "rear doors. Walls made of large flat plain plywood panels in one light tan tone with simple darker tan shadow shapes, each panel edge drawn with a bold dark "
           "outline, no wood grain, no texture; two thin grey metal rails along each wall; a single warm caged ceiling lamp near the front. The flat plywood floor runs past "
           "the bottom edge of the frame. The central 40% of the width is open and uncluttered from the floor up (a character will be composited there later). "
           "Through the open rear doors at the back: a simple cool blue dusk road and sky drawn with flat colors.",
           "warm amber interior light as flat cel-shaded areas on the walls and the open centre; cool blue dusk light through the rear doors; cool background, warm centre.",
           "Match the drawing style of the open cargo bay in the reference image: bold dark outlines, flat colors, 2-tone shading; do not copy its plain background or layout."),
     dalga="1b", not_="M09 (MAHZ9o5EtLA) RED: stil-olcum kontur 0,06 / düzlük 41,0 / doku 1,84 → resimsi, Leo'nun kalın konturuyla uyuşmuyor. Tekrar payı 1/2 kullanıldı; kalan 1.")

if __name__ == "__main__":
    # ---------- yazdır ----------
    tavan_cekirdek = sum(1 for c in C if "seçmeli" not in c["oncelik"])
    o = [f"""# F4 görsel kol — Canva prompt paketi · S03 The Leaky Moving Truck (miras sızıntıları)

**Ajan:** gorsel-varlik-sanatcisi · **Tarih:** 2026-11-04 · **Metin:** `03-metin/metin.md` v1.1 kilitli (sha256 22ba68b7750c) · **Üreten:** koordinatör (`mcp__Canva__generate-image`)
**Kaynak kilit:** `assets/karakter/karakter-karti.md` düzenleme bloğu. Bu dosya `araclar/prompt-uret.py` ile kartın kod bloğundan **birebir** üretildi; elle düzenleme yapma, betiği değiştirip yeniden üret. Denetim §6.
**Bütçe:** çekirdek 16 (M01–M16) + seçmeli 2 (M17, M18) + tekrar payı 2 (M19 = 1. kullanım) → **tavan 20**. Kullanılan: 9 (dalga 1a). Thumbnail için ayrı Canva üretimi **0** (Leo pozları bu paketten, zeminler KOD; §2). Ek ücret yok (Niyazi'nin Canva AI hakkı).

## 1. Koordinatör için çalışma sırası (kopyala-yapıştır)
1. Her üretim: `generate-image` → `prompt` = ```prompt bloğu **aynen**; `reference_asset_ids` = "Referanslar" satırındaki id'ler **bu sırayla** (Leo'lu: 1. taban `MAHZHqW0_Uo`, 2. karakter sayfası `MAHZHpeQGdM`); referans "yok" ise referans verme; `aspect_ratio` = belirtilen değer.
2. Dalga 1a kararları `05-gorsel/rapor.md` ve `canva-ham/uretim-kaydi.md`'de: 8 KABUL, M09 RED → M19. Referans id'ler prompt'lara yazıldı (yer tutucu kalmadı).
3. Tam çözünürlük: `tools/gorsel/canva-indir.md` (sayfa başlığı = Mxx) → `05-gorsel/canva-ham/Mxx.png` (M18: 1080x1920). Media id + tarih `canva-ham/uretim-kaydi.md`'ye.

| Dalga | İşler (paralel ≤5) | Bağımlılık | Amaç |
|---|---|---|---|
| **1a** | **M04, M05, M06, M07, M09** → sonra **M01, M02, M03, M08** | yok (hazır id'ler) | F5 kritik yol (H4): S01 hook + S12 bant gag'i + S30 replik; thumbnail K1/K3/K4 Leo pozları |
| 1b | M10, M11, M12, M13, **M19** | id'ler yazılı (M01 = MAHZ9uk7YSQ) | hook aday B, ev, gişe, gündelik nesneler + M09 düzeltmesi |
| 2 | M14, M15, M16 (+ seçmeli M17, M18) | metin v1.1 kilitli (22ba68b7750c): plaka ihtiyacı değişmedi (fark yalnız KOD etiket/rakam/zaman) | GÖRSEL sütununun kalanı |

**F5 kritik yol için en az:** M04 + M05 + M09 + M01 + M02 + M08 (S01 hook aday A ve S12 bant gag'i tam kurulur). Konuşma = mevcut rig (paket-v1 `a` + 1929 `rig/` ağız/göz yamaları); kafa sabit pozlarda yamalar aynen oturur. Banknot damlaması = KOD SVG parçacık (görselde para yok). B planı: M05/M06 kalırsa 1929 `leo/C14-kutu-gogus.png` + KOD yarık/bant.

## 2. Yeniden kullanılan karakter varlıkları ve thumbnail eşlemesi
- Yeni üretim YOK (kanal karakter varlığı = özgünlük muaf sınıfı): paket-v1 a/b + 1929 `rig/` (B, C/H, E, F, G=B, göz kırpma), 1929 `leo/`: c-isaret (S04 grafik, S22 altını çizer), d-saskin (S21 gişe korkusu), e-dusunen (S29), f-sevincli (S16 gülümser yerine yedek), C05 kutuyla yürüme (S06 yükleme, tam boy), C13 kollar kavuşmuş (S27), C14 kutu göğüste (yedek), C21 el sallar (köprü).
- **Kıyafet:** metindeki "nakliye yeleği" UYGULANMAZ (kart: "Outfit never changes"); her Leo prompt'unda "no vest, no hat, no gloves, no jacket". Rol pano + bant + kamyonla okunur.
- **Thumbnail (09-paket K1–K4) aynı üretimden, kafa değişimiyle** (`thumb-uret.py` v2; bel üstü pozlar kafa satırı ±5 px): K1 = **M06** + kafa `d-saskin` + KOD damlama + teal zemin · K3 = **M04** + M02 büyük/küçük kutu (KOD ölçek, küçük kutuya M02 yarık + M03 bant şeritleri) + sarı zemin · K4 = **M05** + kafa (a ya da e) + KOD banknot · K2 (koşan Leo) kafa-sabit düzenlemeyle üretilemez → K4 tercih (konseptlerde K2/K4'ten yalnız biri finale girer). thumbnail-tasarimcisi'nin sıfırdan "CHARACTER LOCK + SHOT" prompt'ları ölçülmüş kurala göre yüzü kaydırır (kor. 0,45) → kullanılmamalı. Kaynak 1680 px: 1,3× kırpımda bile ≥1280 px (büyütme gerekmez).

## 3. Tasarım kararları (aday → eleme)
| Konu | Adaylar | Seçilen | Gerekçe |
|---|---|---|---|
| Kamyon | (A) her sahnede plakaya gömülü kamyon · (B) tek kamyon nesne sayfası + KOD hareket | B (+ hook için entegre aday) | Kamyon ~12 sahnede tekrar eder; ayrı üretimler biçim/renk kayar. Kesik + KOD sürüş/sinyal/hayalet/konvoy |
| S01 hook ilk 3 sn | (A) M08 yol + M01 arka-açık kesiği · (B) M10 entegre plaka (ref M01) | **ikisi de üretilir, ölçümle elenir** | Kilit sahne = 2 aday kuralı; A tutarlılıkta, B ışık/gölge entegrasyonunda güçlü |
| Leo nakliye şefi | (A) yelekli yeni taban · (B) kart kıyafeti + nesne (pano/bant/kutu) düzenlemeleri | B | A kart kilidini ve tüm rig yamalarını bozar; B'de kafa sabit → dudak senkronu sürer |
| Leo bakışı | (A) kutuya/panoya aşağı bakış · (B) bakış kamerada | B | "eyes glance down" iki kez yüzü yeniden çizdirdi (kor. 0,70 / 0,76) |
| Damlayan para | (A) görsele çizdir · (B) KOD SVG banknot parçacığı | B | Animasyonlu, gerçek para tasarımı yok, renk/ölçek kodda; plaka yasağı (no banknotes) korunur |
| Okafor ailesi | (A) çizilmiş karakterler · (B) KOD düz siluet + etiketli kutular | B | H4 + P2 (yüzsüz, "EXAMPLE FAMILY · ILLUSTRATION" köşe etiketi) |
| Harita, grafikler, pist | (A) Canva · (B) KOD SVG | B | Rakam ve harita doğruluğu koddan; metin RED'inde görsel değişmez |
| Tabela/levha/etiket yazısı | (A) modele yazdır · (B) boş yüzey + KOD | B | AI harfleri bozuk; rakamlar `rakam-tablosu.md`'den |

## 4. Ortak kilitler (her prompt'ta birebir)
- **Leo düzenleme** (M04–M07, M17): kartın `EDIT the first reference image … ONLY CHANGE: …` kalıbı birebir + "{YUZ}" + saat sol bilek + "{KIYAFET}".
- **Plakalar** (M08–M12, M14, M15, M18): `STYLE LOCK` + düz çizgi film eki (S08'de referanssız düzlük 64 = çizgi film) + `EMPTY SCENE … no man in a black shirt` + yazı/banknot/bayrak yasağı + taşma kuralı. Palet: soğuk mavi akşam + sıcak merkez (Leo'nun siyah gömleği sıcak/açık zeminde ayrışır).
- **Nesne sayfaları** (M01–M03, M13, M16): aynı stil kilidi + düz slate-blue zemin `#3E5A7E` (M4 kesme) + yazı yasağı. Kutu renkleri sabit: kiremit `#B4452F`, lacivert `#2B4A7C`, yeşil `#3C8C55`.
- **16:9 / 9:16 güvenli alan:** plakalarda önemli öğe merkez %80; Shorts için orta şerit x 656–1264 (1680 genişlikte) kabulde ölçülür; dikey ek plaka yalnız M18 (seçmeli).

"""]
    o.append("## 5. Prompt'lar\n\n")
    for c in C:
        o.append(f"### {c['id']} · {c['ad']} · {c['oncelik']}\n")
        o.append(f"- **Dalga:** {c['dalga']}\n- **Tür:** {c['tur']}\n- **Referanslar:** {c['refs']}\n- **aspectRatio:** {c['ar']}\n- **Kullanım:** {c['kullanim']}\n- **Kabul:** {c['kabul']}\n")
        if c["not_"]: o.append(f"- **Not:** {c['not_']}\n")
        o.append("\n```prompt\n" + c["prompt"].strip() + "\n```\n\n")
    o.append("""## 6. Denetim ve kayıt
- `python3 -I araclar/prompt-kontrol.py canva-promptlari.md` → her Mxx: kart kilidi birebir, sayfa + taban referansı (Leo'lu), bakış kamerada + aşağı bakış yasağı + kıyafet eki, stil kilidi + düz ek (plaka/nesne), yazı yasağı, aspectRatio, Kabul/Kullanım/Dalga, yer tutucu sırası, ekrana rakam yok, toplam ≤ tavan. Çıktı `araclar/prompt-kontrol-cikti.txt`.
- Üretim kaydı (lisans/kaynak: Canva AI, Niyazi hesabı, Canva Kullanım Koşulları): `canva-ham/uretim-kaydi.md` — Mxx | deneme | media ID | tarih UTC | dosya | karar.
- Değerlendirme (dalga dönünce): `tools/gorsel/tutarlilik.py` (Leo'lu, taban a), `araclar/rig-yama.py` (kafa bölgesi hizası) + 4× ağız yakın planı, `araclar/stil-olcum.py` (plaka/nesne), `araclar/kes-m4.py` (nesne başına kırp → M4; saçak + kapalı delik listesi), `araclar/ten-esle.py` (ten kayarsa önce bu, sonra hak), kontakt sayfası (karakter sayfası + a + yeni + Leo bindirme + 9:16 şerit).
""")
    pathlib.Path(sys.argv[1]).write_text("".join(o))
    print(len(C), "prompt yazıldı")
