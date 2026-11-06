#!/usr/bin/env python3
"""canva-promptlari.md üretici · S08 Kitchen Table Budget (gorsel-varlik-sanatcisi, 2026-11-02).
1929 videosunun prompt-uret.py'sinden türetildi: kilit blokları karakter kartından BİREBİR alınır (elle kopyalama kayması yok).
Değişen: id öneki G, plaka stil kilidine düz çizgi film eki (önceki videoda dönem plakaları boyamsı stile kaymıştı),
PROP (nesne sayfası) türü, mutfak plakası için 2 aday (C01 stil referanslı / referanssız).
Kullanım: python3 -I prompt-uret.py ../canva-promptlari.md"""
import re, sys, pathlib
KOK = pathlib.Path(__file__).resolve().parents[4]
kart = (KOK / "assets/karakter/karakter-karti.md").read_text()
bloklar = re.findall(r"```\n(.*?)```", kart, re.S)
TABAN = next(b for b in bloklar if b.startswith("CHARACTER LOCK"))
EDIT = next(b for b in bloklar if b.startswith("EDIT the first reference image"))
EDIT_KAL = EDIT.strip()
STYLE = "STYLE LOCK: clean 2D cartoon illustration, bold dark outlines, cel-shading with soft 2-tone shadows"
assert "<tek değişiklik>" in EDIT_KAL and STYLE in TABAN
SAYFA, TABAN_ID, C01 = "MAHZHpeQGdM", "MAHZHqW0_Uo", "MAHZMVzdpqQ"
DUZ = "flat colors, simplified shapes, minimal texture, NOT painterly, NOT photorealistic, consistent line weight, the look of a 2D animated TV-series background"
NOTXT = "No text, no letters, no numbers, no signage, no logos, no banknotes, no flags, no watermark."
NOPPL = "EMPTY SCENE: no people in the foreground, no main character, no man in a black shirt."
TASMA = "Keep all important elements inside the central 80% of the frame; extend the scenery naturally to the edges (room for camera pan and zoom)."
STIL_REF = ("Use only the drawing style of the reference image (line weight, flat cel shading, level of simplification); "
            "do not copy its colors, doors, stage, screen or audience.")
AYNI_MUTFAK = "the same kitchen as the reference image (same table, same lamp, same colors, same drawing style)"
BOS_ZEMIN = "plain flat slate-blue background (#3E5A7E), evenly lit, no shadows on the wall"

def edit(degisim):
    return EDIT_KAL.replace("<tek değişiklik>", degisim)

def plaka(sahne, isik, ekstra="", oran="16:9 landscape."):
    return (f"{STYLE}, {DUZ}.\nSCENE: {sahne}\nLIGHT AND PALETTE: {isik}\n{NOPPL}{(' ' + ekstra) if ekstra else ''}\n"
            f"{TASMA}\n{NOTXT} {oran}")

def prop(nesneler):
    return (f"{STYLE}, {DUZ}.\nPROP SHEET: {nesneler} Objects are evenly spaced in one row with clear empty background between them, "
            f"nothing overlapping, nothing touching the frame edges, front-on product-sheet layout, warm soft key light, only a faint contact shadow.\n"
            f"BACKGROUND: {BOS_ZEMIN}.\n{NOPPL}\n{NOTXT} 16:9 landscape.")

L169, P916 = "LANDSCAPE_16_9", "PORTRAIT_9_16 (bağlayıcıdaki dikey değer)"
K_DUZ = ("`tools/gorsel/tutarlilik.py` tabana (a) göre: kafa hist kor. **≥0.84**, ten ΔE ≤8, saç ΔE ≤10, gömlek ΔE ≤8, kafa merkez kayması ≤%4 "
         "(rig ağız yamaları bu pozda da aynı konuma oturmalı), ölçek farkı ≤%10; kontrol listesi 7/7 (saç hacmi yukarı-yana, kalın kaş, kısa sakal+bıyık, "
         "siyah gömlek yaka açık + kollar kıvrık, saat SOL bilekte, yüz oranı, çizgi stili); şapka/ceket/kravat yok; M4 kesme artığı ≤0.01, saçak ≤150 px")
K_PLAKA = ("1680x944 (16:9); ön planda insan yok, siyah gömlekli adam yok; 1:1 + 2× kırpım incelemesinde harf/rakam/logo/tabela/banknot/bayrak yok; "
           "önemli öğe merkez %80'de; stil vekili `araclar/stil-olcum.py`: düzlük ≥%50 ve doku std ≤2,0 hedef (Leo 61–71 / 0,6–0,9; 1929 boyamsı plakalar 26–38 / 2,6–5,2)")
K_MUTFAK = (K_PLAKA + "; masa üst kenarı kadraj yüksekliğinin %62–75'inde ve masa alt kenardan taşar; masanın orta %40 genişliği (x 576–1344) masa üstü "
            "yüksekliğinde boş (Leo bel üstü kesiği oturur, gövdesi masa kenarında kesilir); sandalye/insan yok; buzdolabı notları boş; pencerede okunur tabela yok; "
            "Leo `a` kesiği bindirmesinde (kafa ≈ kadraj yüksekliğinin %20'si) ölçek ve ışık uyumlu (soğuk zemin + sıcak karakter); "
            "9:16 orta şerit (x 656–1264) masa ortası + lamba ışığını içerir")
K_PROP = ("düz slate-blue zemin (M4 renk anahtarı ile kesilebilir; köşe zemin ΔE yayılımı <6); nesneler birbirine ve kenara değmez; "
          "1:1 + 2× incelemede yazı/rakam/logo/pul/adres yok; her nesne M4 sonrası kenar artığı ≤0.01, saçak ≤150 px; stil düzlük ≥%50")

C = []
def ekle(i, ad, oncelik, tur, refs, kullanim, kabul, prompt, ar=L169, not_=""):
    C.append(dict(id=i, ad=ad, oncelik=oncelik, tur=tur, refs=refs, kullanim=kullanim, kabul=kabul, prompt=prompt, ar=ar, not_=not_))

MUTFAK_SAHNE = ("a small cozy apartment kitchen at night, medium shot from across the kitchen table at seated eye level, straight-on. "
    "The top of a plain light-wood kitchen table runs across the bottom 30% of the frame and continues past the bottom edge (the camera sits right at the table); "
    "the tabletop is mostly clear, only a ceramic mug and a small pile of blank white paper bills near the right edge. "
    "Behind the table the central 40% of the width is open and uncluttered at table height, with no chair visible (a seated character will be composited there later, "
    "his torso hidden by the table). Background: simple kitchen counters and cabinets in muted blue-grey, a window on the left showing a deep blue night sky "
    "with soft out-of-focus city lights and no readable signs, a tall plain fridge on the right third with five small square pale-yellow paper notes stuck on its door "
    "(the notes are completely blank on purpose). A warm pendant lamp hangs above the centre of the table.")
MUTFAK_ISIK = ("cool navy and blue-grey night palette in the room; one warm golden pool of light from the pendant lamp on the table centre and the open space behind it; "
               "cool background, warm centre; gentle contrast, cinematic.")

# ---------- Dalga 1 · P0 (F5 kritik yol: Leo masada + matruşka zarf) ----------
ekle("G01", "Mutfak masası orta plan — aday A (C01 stil referanslı)", "P0 (aday)", "CV-A karaktersiz plaka", f"[{C01}] (yalnız çizim dili)",
     "S08 ana sahnesi: Leo masada konuşur (rig), faturalar, matruşka anı, kapanış; 9:16 orta şerit Shorts yedeği", K_MUTFAK,
     plaka(MUTFAK_SAHNE, MUTFAK_ISIK, STIL_REF),
     not_="G01 ile G02 aynı sahnenin iki adayı; kazanan (kabul listesi + stil vekili + Leo bindirme) sonraki mutfak plakalarının referansı olur, kaybeden kullanılmaz.")
ekle("G02", "Mutfak masası orta plan — aday B (referanssız)", "P0 (aday)", "CV-A karaktersiz plaka", "yok",
     "G01 ile aynı", K_MUTFAK, plaka(MUTFAK_SAHNE, MUTFAK_ISIK),
     not_="Referanssız; stil yalnız metinle. 1929'da referanssız plakalar boyamsı çıktı → düz çizgi film eki bu farkı ölçer.")
ekle("G03", "Zarf nesne sayfası (matruşka)", "P0", "PROP nesne sayfası", "yok",
     "Matruşka zarf anı (KOD: zarf açılır, içinden küçültülmüş kopya çıkar, kule büyür; 'INTEREST' vb. etiketler KOD yazı), fatura bölümü",
     K_PROP + "; zarf rengi G04/G05'teki elde tutulan zarfla aynı kraft kahve (Lab ΔE ≤10)",
     prop("four separate objects: (1) a closed plain kraft-brown paper envelope seen straight from the front; (2) the same envelope seen from the back with its "
          "triangular flap fully open upward and the empty inside visible; (3) a neat tall stack of about twelve identical closed kraft-brown envelopes seen from a slight "
          "three-quarter angle; (4) a plain folded sheet of white paper. All envelopes and paper are completely blank: no writing, no stamps, no address, no lines, no logos."))
ekle("G04", "Leo zarfı açıp içine bakar (matruşka 1)", "P0 (kilit poz, aday)", "CV-L düzenleme (kol değişimi)", f"[{TABAN_ID}, {SAYFA}]",
     "Matruşka anı: Leo zarfı açar (masada, gövdesi masa kenarında kesilir); fatura açma", K_DUZ + "; zarf düz kraft kahve, yazısız; ağız kapalı nötr (rig ağızları bindirilebilir)",
     edit("he holds an open plain kraft-brown paper envelope with both hands at chest height, flap up, and his eyes glance down into it with eyebrows slightly raised in curiosity; "
          "his head stays in exactly the same place and angle facing the camera, mouth closed and neutral; torso stays in the same place; the envelope is completely blank with "
          "no writing; the black wristwatch on his left wrist stays visible"),
     not_="G04 ve G05 kilit anın iki adayı; ikisi de geçerse ikisi de kullanılır (açar → çıkarır). Kafa yerinde kalmalı ki ağız yamaları konuşmaya devam etsin.")
ekle("G05", "Leo büyük zarftan küçük zarf çıkarır (matruşka 2)", "P0 (kilit poz, aday)", "CV-L düzenleme (kol değişimi)", f"[{TABAN_ID}, {SAYFA}]",
     "Matruşka doruğu: zarfın içinden zarf çıkar (KOD ile tekrarlanır, kule G03 yığınıyla büyür)",
     K_DUZ + "; büyük zarf sol elde (saat görünür), küçük zarf sağ elde yarı dışarıda; ikisi de yazısız",
     edit("his left hand holds a large open plain kraft-brown envelope at chest height and his right hand pulls a smaller identical kraft-brown envelope halfway up out of it; "
          "eyebrows raised in mild surprise, eyes looking at the camera, mouth closed; his head stays in exactly the same place and angle; torso stays in the same place; "
          "both envelopes are completely blank with no writing; the black wristwatch on his left wrist stays visible"))
# ---------- Dalga 2 · P1 ----------
ekle("G06", "Masa üstü — kuşbakışı fatura masası", "P1", "CV-A karaktersiz plaka", "[<G01|G02 kazanan media id>]",
     "Faturalar bölümü (KOD zarflar masaya düşer, kategori etiketleri), kredi kartı bölümü (G07 nesneleri yerleşir), matruşka kulesi üstten",
     K_PLAKA + "; masa orta %50'si boş (KOD nesne alanı); kazanan mutfak plakasıyla aynı ahşap tonu ve lamba ışığı (kontaktta yan yana)",
     plaka("a top-down overhead view looking straight down at " + AYNI_MUTFAK.replace("the same kitchen", "the same kitchen table") +
           ", under the same warm pendant light. The wooden tabletop fills the whole frame; its centre half is clear and empty (objects will be composited there later). "
           "Near the edges only: a few blank white paper bills, one closed plain kraft-brown envelope, a ceramic mug seen from above and a pencil. All paper is completely blank.",
           "warm golden lamp light pooled on the table centre, falling off to cooler blue-grey shadows at the frame edges."))
ekle("G07", "Ev nesneleri sayfası — kumbara, kasa, kart, hesap makinesi", "P1", "PROP nesne sayfası", "yok",
     "Gelir/birikim (kumbara), borç (kasa boş/dolu KOD), kredi kartı bölümü, hesaplama anları; thumbnail yardımcı nesneleri",
     K_PROP + "; kart ve hesap makinesi ekranı tamamen boş (rakam/logo yok); paralar işaretsiz",
     prop("five separate objects: (1) a glossy pink ceramic piggy bank in side view with a coin slot on top; (2) a small dark-steel home safe, door closed, with a round dial "
          "and a handle; (3) a plain blank credit card in deep blue with only a small gold chip, no numbers, no name, no logo; (4) a chunky pocket calculator with a blank "
          "empty grey display and plain unmarked buttons; (5) a small stack of three plain unmarked gold coins with no faces or symbols."))
ekle("G08", "Leo hesap makinesine tuşlar (bütçe tutan)", "P1", "CV-L düzenleme (kol değişimi)", f"[{TABAN_ID}, {SAYFA}]",
     "Leo'nun rolü (ev arkadaşı / bütçe tutan): ölçek hesabı 'Let's do the math', fatura toplama", K_DUZ + "; hesap makinesi ekranı ve tuşları boş (rakam KOD)",
     edit("he holds a chunky pocket calculator in his left hand at chest height and taps it with his right index finger, eyes glancing down at it with a focused look; "
          "his head stays in exactly the same place and angle facing the camera, mouth closed and neutral; torso stays in the same place; the calculator display is blank "
          "and the buttons have no markings; the black wristwatch on his left wrist stays visible"))
# ---------- Seçmeli · P2 ----------
ekle("G09", "Dikey mutfak masası (Shorts)", "P2 seçmeli", "CV-A karaktersiz plaka (9:16)", "[<G01|G02 kazanan media id>]",
     "Shorts matruşka kesiti (~50 sn) zemini (yoksa B: kazanan plakanın x 656–1264 orta şeridi, ×1,78 büyütme, yumuşak)",
     "1080x1920'ye uygun dikey oran; ön planda insan yok; yazı yok; masa üst kenarı yükseklik %58–66; üst %15 ve alt %35 sade (Shorts arayüzü); kazanan plakayla aynı mutfak",
     plaka(AYNI_MUTFAK + " in a tall vertical frame: the light-wood table top across the lower part of the frame with its top edge at about 62% of the frame height and "
           "running past the bottom edge, the warm pendant lamp above the centre, the fridge with blank notes partly visible at one side; the centre above the table is open "
           "(a seated character will be composited there).", "same palette as the reference: cool navy and blue-grey night room, warm golden pool of lamp light on the table centre.",
           oran="9:16 portrait.").replace(TASMA, "Keep the top 15% and bottom 35% of the frame calm and simple (vertical video interface)."), ar=P916)
ekle("G10", "Buzdolabı kapısı yakın plan — boş notlar", "P2 seçmeli", "CV-A karaktersiz plaka", "[<G01|G02 kazanan media id>]",
     "Aylık bütçe notları (KOD: '$5,400 IN / $7,400 OUT' vb.), thumbnail zemini adayı",
     K_PLAKA + "; notlar boş ve düz yüzlü (KOD yazı için ≥ 220x220 px), magnetler işaretsiz",
     plaka("a close-up of the fridge door from " + AYNI_MUTFAK + ": a plain fridge door filling most of the frame with five large square pale-yellow paper notes "
           "arranged in a loose grid and two round plain magnets; the notes are completely blank on purpose, flat and facing the camera.",
           "cool blue-grey fridge surface, warm lamp light spilling in from the left side."))

# ---------- yazdır ----------
o = [f"""# F4 görsel kol — Canva prompt paketi · S08 Kitchen Table Budget (dalga 1–2, metinden bağımsız temel varlıklar)

**Ajan:** gorsel-varlik-sanatcisi · **Tarih:** 2026-11-02 · **Üreten:** koordinatör (`mcp__Canva__generate-image`; bu ajanın aracı yok)
**Kaynak kilit:** `assets/karakter/karakter-karti.md` (taban + düzenleme blokları). Bu dosya `araclar/prompt-uret.py` ile kartın kod bloklarından **birebir** üretildi; elle düzenleme yapma, betiği değiştirip yeniden üret. Denetim §6.
**Bütçe:** çekirdek 8 (G01–G08; G01/G02 aynı plakanın 2 adayı) + seçmeli 2 (G09, G10) + tekrar payı 2 → **tavan 12**. Ek ücret yok (Niyazi'nin Canva AI hakkı).

## 1. Koordinatör için çalışma sırası
1. Her üretim: `generate-image` → prompt = ```prompt bloğu **aynen**; referanslar = "Referanslar" satırı (sıra önemli: 1. taban/çapa, 2. karakter sayfası); aspectRatio = belirtilen.
2. `<G01|G02 kazanan media id>` = G01/G02'den benim **kabul** ettiğim mutfak plakası (karar `05-gorsel/rapor.md` erken karar satırında).
3. Tam çözünürlük: `tools/gorsel/canva-indir.md` (tuval `DAHZHv3mU9w`, sayfa başlığı = Gxx) → `05-gorsel/canva-ham/Gxx.png` (G09: 1080x1920 sayfa). Media id + tarih `canva-ham/uretim-kaydi.md`'ye.

| Dalga | İşler (paralel ≤5) | Bağımlılık | Amaç |
|---|---|---|---|
| 1 | **G01, G02, G03, G04, G05** | yok (hazır id'ler) | F5 kritik yol (H4): Leo masada konuşur + matruşka zarf |
| 2 | G06, G07, G08 (+ seçmeli G09, G10) | G06/G09/G10 ← mutfak kazananı | fatura masası, kumbara/kasa, hesap makinesi pozu, Shorts zemini |
| 3 | metin kilidinden sonra (yalnız GÖRSEL sütunundaki karşılanmayan sahneler; tavanın kalanı ≤2) | metin | — |

**F5 kritik yol için en az:** mutfak kazananı (G01|G02) + G03 + G04 (ya da G05). Konuşan Leo = mevcut rig (paket-v1 `a` + 1929 `rig/` ağız/göz yamaları), yeni üretim gerekmez. B planı (H4): G04/G05 kalırsa zarflar yalnız G03 nesneleriyle KOD katmanı olarak açılır, Leo `d-saskin` ile tepki verir.

## 2. Yeniden kullanılan karakter varlıkları (yeni üretim YOK; kanal karakter varlığı = özgünlük muaf sınıfı)
- Konuşma + rig: `assets/karakter/paket-v1/a` (MAHZHqW0_Uo) + `uretim/2026-10-26-1929-1000-dolar/05-gorsel/rig/` (B, C/H, E, F, G=B, göz kırpma; `rig-yamalar.json`). D = paket-v1 b.
- Jestler (`…/1929-1000-dolar/05-gorsel/leo/`, M4 kesikler): c-isaret (buzdolabı notuna/grafiğe işaret), d-saskin (faiz faturası tepkisi), e-dusunen ("aile değil" bölümü), f-sevincli, C12-sunum (üç olasılık), C13-kollar-kavusmus, C20-saate-bakar (vade/zaman), C21-el-sallar (kapanış), C02/C04 tam boy (mutfağa giriş).
- Rakip ayrışması (Fred - Money Historian: silindir şapka + takım elbise): Leo'da şapka/ceket/kravat yok; kilit "Outfit never changes" kartta zaten; kabul listesine "şapka/ceket/kravat yok" eklendi. Mekân dili de farklı: ev mutfağı, stüdyo/müze değil.

## 3. Tasarım kararları (aday → eleme)
| Konu | Adaylar | Seçilen | Gerekçe |
|---|---|---|---|
| Leo masada | (A) mevcut bel üstü rig + masa plakası alt kenardan taşar (gövde masa kenarında kesilir) · (B) yeni oturan Leo tabanı · (C) Leo'lu sahne illüstrasyonu | A | B yeni taban = tüm rig yamaları geçersiz + 7 ek üretim; C'de yüz kayar ve dudak senkronu olmaz (hafıza 2026-10-27). A sıfır üretim, rig aynen çalışır |
| Mutfak stili | (A) C01 stil referansı + düz çizgi film eki · (B) referanssız + aynı ek | **ikisi de üretilir, ölçümle elenir** | 1929'da referanslı C15 de boyamsı çıktı; yeni ek "NOT painterly" ilk kez deneniyor → yeni sahne tipi + kilit sahne = 2 aday kuralı |
| Matruşka | (A) Canva'da zarf-içinde-zarf illüstrasyonu · (B) zarf nesne sayfası + KOD tekrar/ölçek + Leo tutma pozu | B | Tekrar sayısı ve 'INTEREST' etiketi metne göre değişir; KOD esnek, metin RED'inde görsel değişmez; Leo pozu kafa sabit → konuşma sürer |
| Rakam/etiket | (A) modele yazdır · (B) boş yüzey + KOD | B | AI harfleri bozuk; bütçe rakamları doğrulanmış olmalı ([D] D1–D5) |
| Nesneler | (A) her nesne ayrı üretim · (B) tek sayfada 4–5 nesne + M4 kesme | B | 2 üretimde 9 nesne; düz zemin M4 ile artık ≤0.001 (1929 ölçümü) |

## 4. Ortak kilitler (her prompt'ta birebir)
- Leo **düzenleme** (G04, G05, G08): kartın `EDIT the first reference image. Keep EVERYTHING identical … ONLY CHANGE: …` kalıbı birebir; referans [paket-v1 a, karakter sayfası]; "head stays in exactly the same place and angle" (rig ağızları bindirilebilsin).
- **Plakalar** (G01, G02, G06, G09, G10): `STYLE LOCK` cümlesi birebir + düz çizgi film eki (`{DUZ}`) + `EMPTY SCENE … no man in a black shirt` + yazı/banknot/bayrak yasağı (P1: parti/bayrak/yüz yok) + taşma kuralı.
- **Nesne sayfaları** (G03, G07): aynı stil kilidi + düz slate-blue zemin (M4) + yazı yasağı.

"""]
o.append("## 5. Prompt'lar\n\n")
for c in C:
    o.append(f"### {c['id']} · {c['ad']} · {c['oncelik']}\n")
    o.append(f"- **Tür:** {c['tur']}\n- **Referanslar:** {c['refs']}\n- **aspectRatio:** {c['ar']}\n- **Kullanım:** {c['kullanim']}\n- **Kabul:** {c['kabul']}\n")
    if c["not_"]: o.append(f"- **Not:** {c['not_']}\n")
    o.append("\n```prompt\n" + c["prompt"].strip() + "\n```\n\n")
o.append("""## 6. Denetim ve kayıt
- `python3 -I araclar/prompt-kontrol.py canva-promptlari.md` → her Gxx: kart kilidi birebir, sayfa referansı (Leo'lu), stil kilidi + düz ek (plaka/nesne), yazı yasağı, aspectRatio, Kabul/Kullanım, yer tutucu sırası, toplam ≤12. Çıktı `araclar/prompt-kontrol-cikti.txt`.
- Üretim kaydı (lisans/kaynak: Canva AI, Niyazi hesabı, Canva Kullanım Koşulları): `canva-ham/uretim-kaydi.md` — Gxx | deneme | media ID | tarih UTC | dosya | karar.
- Değerlendirme yöntemi (dalga dönünce): `tools/gorsel/tutarlilik.py` (Leo'lu, taban a), `araclar/stil-olcum.py` (plaka/nesne), `araclar/kes-m4.py` (M4 v2, saçak + kapalı delik listesi), `araclar/rig-yama.py` (G04/G05/G08 kafa bölgesi a'ya hizalı mı), kontakt sayfası (karakter sayfası + a + yeni varlıklar + Leo bindirme).
""")
pathlib.Path(sys.argv[1]).write_text("".join(o))
print(len(C), "prompt yazıldı")
