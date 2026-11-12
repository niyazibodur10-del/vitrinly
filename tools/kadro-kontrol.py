# Kadro kontrolü: her ajanın frontmatter (name/description/tools), protokol satırı, hafıza dosyası, skill ve çalışma şekli bölümleri.
# Kullanım: python3 tools/kadro-kontrol.py
import glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, ".claude/agents")
ok_all = True
rows = []
for f in sorted(glob.glob(f"{R}/*.md")):
    ad = os.path.basename(f)[:-3]
    t = open(f, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); fm[k.strip()] = v.strip()
        body = m.group(2)
    else:
        body = ""
    first = next((l for l in body.splitlines() if l.strip()), "")
    proto = first == f"Her işte önce `docs/ajan-protokolu.md` ve `.claude/agents/hafiza/{ad}.md` oku; iş sonunda hafızana ders ekle."
    hf = f"{R}/hafiza/{ad}.md"
    hok = os.path.exists(hf) and all(s in open(hf, encoding="utf-8").read() for s in (f"# {ad}", "## Kurallar", "## Dersler"))
    tools = [x.strip() for x in fm.get("tools", "").split(",") if x.strip()]
    checks = {
        "frontmatter": bool(m),
        "name=dosya": fm.get("name") == ad,
        "description": len(fm.get("description", "")) > 20,
        "tools": len(tools) > 0,
        "protokol": proto,
        "hafiza": hok,
        "skill-bolumu": "## Kullandığın skill'ler" in body,
        "calisma-sekli": "## Çalışma şekli: 2–3 aday" in body,
        "Skill-araci": "Skill" in tools,
    }
    good = all(checks.values()); ok_all &= good
    rows.append((ad, good, [k for k, v in checks.items() if not v]))
for ad, good, bad in rows:
    print(f"{'OK  ' if good else 'HATA'} {ad:26s} {'' if good else bad}")
yetim = [os.path.basename(h)[:-3] for h in glob.glob(f"{R}/hafiza/*.md") if not os.path.exists(f"{R}/{os.path.basename(h)}")]
print(f"ajan sayısı: {len(rows)} | hafıza dosyası: {len(glob.glob(R+'/hafiza/*.md'))} | sahipsiz hafıza: {yetim or 'yok'}")
cl = open(os.path.join(ROOT, "CLAUDE.md"), encoding="utf-8").read()
eksik = [ad for ad, _, _ in rows if f"`{ad}`" not in cl and ad not in cl]
print("CLAUDE.md'de geçmeyen ajan:", eksik or "yok")
print("SONUÇ:", "GEÇTİ" if ok_all and not yetim and not eksik else "KALDI")
sys.exit(0 if ok_all else 1)
