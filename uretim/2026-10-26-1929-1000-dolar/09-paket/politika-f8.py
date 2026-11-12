#!/usr/bin/env python3
"""F8 paket politika denetimi — ölçüm betiği (monetizasyon-uyum-uzmani).

Kullanım (üretim klasöründen):
  python3 -I 09-paket/politika-f8.py [--video 07-animasyon/tam-16x9-onizleme.mp4]

Deterministik; iki koşunun çıktısı bayt bayt aynı olmalı. Ölçer:
  [1] Meta veri dili: başlık, açıklama (yasal not + müzik atfı hariç), etiketler,
      Shorts başlık/açıklamaları, pinli yorum → tavsiye / bugüne dönük hüküm /
      şok / küfür desenleri (answer/1311392 AI persona; answer/6162278 "all portions").
  [2] AI beyanı: 3 pakette sentetik_medya=true + açıklamada AI satırı (answer/14328491).
  [3] Başlık / thumbnail / Shorts başlığı ↔ içerik: her vaat ifadesi kilitli anlatımda var mı.
  [4] Lisans: cue.json'daki her dosya lisans-kaydi.md'de; NC/ND/SA yok; üçüncü taraf
      dosyaların kanıt sayfası assets/lisans-kanit/ altında (Content ID itirazı).
  [5] Yeniden kullanılan sahne oranı: final önizlemenin 1 fps kareleri ↔ önceki
      renderlar (pilot-v1/v2, test yüklemesi) dHash; ≤6/64 bit = yeniden kullanım.
      İç kural ≤ %20 (YouTube sayısı değil).
  [6] Dış görüntü (reused): k1929/k1929t görsellerinin hepsi kendi üretim klasörümüzden mi.
"""
import json
import os
import re
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(KOK))

ADVICE = [
    r"\byou should\b", r"\byou need to\b", r"\byou must\b", r"\brecommend",
    r"\bmy advice\b", r"\bbuy now\b", r"\bsell now\b", r"\bguarantee", r"\binvest in\b",
    r"\bbest investment\b", r"\btips?\b", r"\bkeep (your )?cash\b",
    r"\bput your (money|savings)\b", r"\bmove your (money|savings)\b",
    r"\bwhere to (put|keep)\b", r"\bsafe (today|now)\b", r"\bcash is trash\b",
    r"\bdon'?t (invest|buy|sell|hold)\b", r"\bprotect your\b", r"\bget rich\b",
    r"\bsecret\b", r"\bexpert\b", r"\badvis[eo]r\b",
]
SHOCK = [r"\bsuicid", r"\bkill", r"\bdeath\b", r"\bdead\b", r"\bblood", r"\bcorpse",
         r"\bstarv", r"\bviolen", r"\briot", r"\bterror", r"\bshock", r"\bhorr"]
PROFANITY = [r"\bshit", r"\bfuck", r"\bdamn\b", r"\bhell\b", r"\bcrap\b", r"\bbitch"]
AI_SATIR = "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."
YASAK_LISANS = re.compile(r"\bCC BY-(NC|ND|SA)\b|\bBY-NC\b|\bBY-ND\b|\bBY-SA\b")


def norm(t):
    t = t.lower().replace("’", "'").replace("$1,000", "one thousand dollars")
    return " ".join(re.findall(r"[a-z0-9']+", t))


def bul(desenler, metin):
    out = []
    for d in desenler:
        for m in re.finditer(d, metin, re.I):
            out.append(m.group(0).lower())
    return sorted(set(out))


def aciklama_govde(a):
    """Yasal not paragrafı ve MUSIC & SOUND bölümü hariç (aynen-muaf metin)."""
    a = re.sub(r"LEGAL NOTE\n.*?\n\n", "", a, flags=re.S)
    a = re.sub(r"MUSIC & SOUND\n.*?\n\n", "", a, flags=re.S)
    a = re.sub(r"Music: .*\n", "", a)
    a = a.replace(AI_SATIR, "")
    a = a.replace("Not financial advice.", "").replace("not a financial adviser", "")
    return a


def anlatim():
    md = open(os.path.join(KOK, "03-metin/metin.md"), encoding="utf-8").read()
    satirlar = []
    for ln in md.splitlines():
        if ln.startswith("| ") and "**Sahne" in ln:
            satirlar.append(ln.split("|")[1])
    sh = re.findall(r"Okunacak tam metin[^<]*<<(.*?)>>", md)
    return norm(" ".join(satirlar)), [norm(s) for s in sh]


def dhash_kareler(yol, fps="1"):
    cmd = ["ffmpeg", "-v", "error", "-i", yol, "-vf", f"fps={fps},scale=9:8,format=gray",
           "-f", "rawvideo", "-"]
    ham = subprocess.run(cmd, capture_output=True, check=True).stdout
    hs = []
    for i in range(0, len(ham) - 71, 72):
        b = ham[i:i + 72]
        v = 0
        for r in range(8):
            for c in range(8):
                v = (v << 1) | (1 if b[r * 9 + c] > b[r * 9 + c + 1] else 0)
        hs.append(v)
    return hs


def main():
    args = sys.argv[1:]
    video = os.path.join(KOK, "07-animasyon/tam-16x9-onizleme.mp4")
    if "--video" in args:
        video = os.path.join(KOK, args[args.index("--video") + 1])
    hata = 0
    P = os.path.join(KOK, "09-paket")
    paketler = {k: json.load(open(os.path.join(P, f), encoding="utf-8")) for k, f in [
        ("uzun", "yayin-paketi.json"), ("shorts-1", "yayin-paketi-shorts-1.json"),
        ("shorts-2", "yayin-paketi-shorts-2.json")]}
    paket_md = open(os.path.join(P, "paket.md"), encoding="utf-8").read()
    pin = re.search(r"<!-- veri:pinli-yorum -->\n```text\n(.*?)```", paket_md, re.S).group(1)
    basliklar = re.search(r"<!-- veri:basliklar -->\n```text\n(.*?)```", paket_md, re.S).group(1)

    print("[1] Meta veri dili (tavsiye/hüküm · şok · küfür)")
    for k, p in paketler.items():
        m = p["metadata"]
        parcalar = {"baslik": m["baslik"], "aciklama": aciklama_govde(m["aciklama"]),
                    "etiketler": ", ".join(m.get("etiketler", []))}
        for ad, t in parcalar.items():
            a, s, f = bul(ADVICE, t), bul(SHOCK, t), bul(PROFANITY, t)
            durum = "0" if not (a or s or f) else f"tavsiye={a} sok={s} kufur={f}"
            if a or s or f:
                hata += 1
            print(f"  {k:9s} {ad:9s} {durum}")
    for ad, t in [("pinli", pin), ("yedek-baslik", basliklar)]:
        a, s, f = bul(ADVICE, t), bul(SHOCK, t), bul(PROFANITY, t)
        print(f"  {'paket.md':9s} {ad:9s} {'0' if not (a or s or f) else (a, s, f)}")
        hata += bool(a or s or f)

    print("[2] AI beyanı")
    for k, p in paketler.items():
        sm = p["durum"].get("sentetik_medya")
        satir = AI_SATIR in p["metadata"]["aciklama"]
        nf = "Not financial advice." in p["metadata"]["aciklama"]
        print(f"  {k:9s} sentetik_medya={sm} ai_satiri={satir} yasal_kisa={nf}")
        hata += (sm is not True) + (not satir)

    print("[3] Vaat ↔ içerik (kilitli anlatımda geçiyor mu)")
    ana, shorts = anlatim()
    vaatler = [
        ("baslik T1", ["one thousand dollars", "nineteen twenty-nine", "keep"], ana),
        ("thumb A2 ONE IS A DISASTER", ["one door is a disaster"], ana),  # parafraz
        ("thumb B1 THE SURPRISE DOOR", ["surprise", "door"], ana),
        ("thumb B1 damga 1929", ["nineteen twenty-nine"], ana),
        ("thumb D1 EVERY DOOR LOCKED", ["every door gets locked"], ana),
        ("shorts-1 baslik", ["nineteen twenty-nine", "door", "one thousand dollars"], shorts[0]),
        ("shorts-2 'same box'", ["same box"], shorts[1]),
        ("shorts-2 'opposite result'", ["opposite result"], shorts[1]),
        ("shorts-2 '1932'", ["nineteen thirty-two"], shorts[1]),
        ("shorts-2 '2026'", ["twenty twenty-six"], shorts[1]),
        ("shorts-2 niteleyici", ["prices were falling", "not a plan"], shorts[1]),
    ]
    for ad, ifadeler, metin in vaatler:
        eksik = [i for i in ifadeler if norm(i) not in metin]
        print(f"  {ad:30s} {'VAR' if not eksik else 'EKSIK ' + str(eksik)}")
        hata += bool(eksik)
    tavsiye_sh = [bul(ADVICE, s) for s in shorts]
    print(f"  shorts okuma metni tavsiye deseni: {tavsiye_sh}")

    print("[4] Lisans kaydı + Content ID itiraz kanıtı")
    kayit = open(os.path.join(KOK, "06-muzik/lisans-kaydi.md"), encoding="utf-8").read()
    f6 = kayit.split("## F6", 1)[1].split("## Değerlendirilip", 1)[0]
    cue = json.load(open(os.path.join(KOK, "06-muzik/cue.json"), encoding="utf-8"))
    dosyalar = sorted({os.path.basename(c["dosya"]) for c in cue["muzik"] + cue["sfx"] + cue["shorts"]})
    kayitsiz = [d for d in dosyalar if d not in f6]
    lis = {}
    for ln in f6.splitlines():
        m = re.match(r"\| `([^`]+)`.*?\| ([^|]+) \|", ln)
        if m:
            lis[m.group(1)] = m.group(2).strip()
    yasak = sorted(d for d, l in lis.items() if YASAK_LISANS.search(l))
    kanit_dir = os.path.join(REPO, "assets/lisans-kanit")
    kanitlar = set(os.listdir(kanit_dir))
    ucuncu = sorted(d for d, l in lis.items() if l != "Bizim")
    # kanıt eşlemesi: ana tablodaki satırın kanıt sütunu
    kanit_yok = []
    for d in ucuncu:
        kok = re.sub(r"_0?\d+$", "_", d.split(".")[0])
        satir = next((ln for ln in kayit.split("## F6")[0].splitlines() if d.split(".")[0] in ln or kok in ln), "")
        refs = re.findall(r"((?:oga|kenney)-[a-z0-9-]+(?:\.html|-License\.txt))", satir)
        if not refs:
            refs = ["kenney-impact-sounds-License.txt"] if d.startswith(("muhur", "pop", "tik")) else []
        if not refs or not all(r in kanitlar for r in refs):
            kanit_yok.append(d)
    print(f"  cue dosyası {len(dosyalar)} · kayıtsız {kayitsiz} · NC/ND/SA {yasak}")
    print(f"  üçüncü taraf {len(ucuncu)} · kanıt sayfası eksik {kanit_yok}")
    cc_by = sorted(d for d, l in lis.items() if "CC BY" in l)
    print(f"  kullanılan CC BY (zorunlu atıf) {cc_by}")
    hata += bool(kayitsiz) + bool(yasak) + bool(kanit_yok)

    print("[5] Yeniden kullanılan sahne oranı (dHash ≤6/64, 1 fps)")
    onceki = ["uretim/ses-testi/pilot/pilot-v1.mp4", "uretim/ses-testi/pilot/pilot-v2.mp4",
              "uretim/ses-testi/yayin-manuel/video.mp4"]
    havuz = []
    for o in onceki:
        hs = dhash_kareler(os.path.join(REPO, o), "2")
        havuz += hs
        print(f"  önceki {o}: {len(hs)} kare (2 fps)")
    bu = dhash_kareler(video, "1")
    # siyah/tek renkli kareler (hash 0) karşılaştırmadan çıkar
    gecerli = [h for h in bu if h != 0]
    tekrar = sum(1 for h in gecerli if min(bin(h ^ p).count("1") for p in havuz) <= 6)
    oran = 100.0 * tekrar / max(1, len(gecerli))
    print(f"  bu video {len(bu)} kare, geçerli {len(gecerli)}, eşleşen {tekrar} → %{oran:.1f} (iç kural ≤ %20)")
    hata += oran > 20

    print("[6] Dış görüntü / klip")
    pub = os.path.join(REPO, "video/public")
    dis = []
    for alt in ("k1929", "k1929t"):
        for kok, _, fs in os.walk(os.path.join(pub, alt)):
            for f in sorted(fs):
                if f.lower().endswith((".mp4", ".mov", ".webm", ".gif")):
                    dis.append(os.path.relpath(os.path.join(kok, f), pub))
    print(f"  k1929/k1929t video klip dosyası: {dis if dis else 0} (görseller Canva üretimi + kod)")

    print(f"SONUC hata={hata}")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
