#!/usr/bin/env python3
"""konu-havuzu.md kaynak kapısı (trend-avcisi).

Her konu (`### <ID> ...` başlığı) için kaynak satırlarını okur:
  - K: [başlık](url) · yayıncı · tarih: YYYY-MM-DD · anahtar: <kelime>
Kontroller:
  1. Bağımsız kaynak sayısı = farklı kayıtlı alan adı (ör. en.wikipedia.org ve
     wikipedia.org aynı sayılır). Kapı: >= 2.
  2. Link açılıyor mu: HTTP 200 + sayfa metninde `anahtar` kelimesi geçiyor
     (soft-404 / bot sayfasını eler). Kapı: konu başına açılan >= 2 bağımsız kaynak.
  3. Güncel (B) konularda: en az 1 kaynak tarihi son 30 gün içinde (bugün - 30).
Kullanım: python3 kaynak-kontrol.py konu-havuzu.md [--bugun 2026-10-27] [--cevrimdisi]
Çıktı: markdown kontrol tablosu (stdout). Çıkış kodu 0 = tüm konular geçti.
"""
import datetime as dt
import html
import re
import subprocess
import sys

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
KAYNAK = re.compile(r"^\s*- K\d*: \[(?P<baslik>[^\]]+)\]\((?P<url>[^)]+)\)(?P<rest>.*)$")
BASLIK = re.compile(r"^### (?P<id>[ABC]\d+)\b(?P<ad>.*)$")


def alan(url):
    h = re.sub(r"^https?://", "", url).split("/")[0].lower()
    parca = h.split(".")
    if len(parca) >= 3 and parca[-2] in ("co", "com", "org", "gov") and len(parca[-1]) == 2:
        return ".".join(parca[-3:])
    return ".".join(parca[-2:])


def ac(url, anahtar):
    r = subprocess.run(["curl", "-s", "-L", "--compressed", "-A", UA, "--max-time", "30",
                        "-w", "\n__KOD__%{http_code}", url], capture_output=True)
    t = r.stdout.decode("utf-8", "ignore")
    kod = t.rsplit("__KOD__", 1)[-1].strip() if "__KOD__" in t else "000"
    x = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    x = html.unescape(re.sub(r"<[^>]+>", " ", x))
    ok = kod == "200" and (not anahtar or anahtar.lower() in x.lower())
    return kod, ok


def main():
    yol = sys.argv[1]
    bugun = dt.date.fromisoformat(sys.argv[sys.argv.index("--bugun") + 1]) if "--bugun" in sys.argv else dt.date.today()
    cevrimdisi = "--cevrimdisi" in sys.argv
    sinir = bugun - dt.timedelta(days=30)
    konular, cur = [], None
    for satir in open(yol, encoding="utf-8"):
        if satir.startswith("## Kontrol listesi"):
            break
        m = BASLIK.match(satir)
        if m:
            cur = {"id": m["id"], "ad": m["ad"].strip(" —-"), "k": []}
            konular.append(cur)
            continue
        m = KAYNAK.match(satir)
        if m and cur:
            rest = m["rest"]
            tarih = re.search(r"tarih: (\d{4}-\d{2}-\d{2})", rest)
            anahtar = re.search(r"anahtar: ([^·]+)", rest)
            cur["k"].append({"url": m["url"], "tarih": tarih.group(1) if tarih else None,
                             "anahtar": anahtar.group(1).strip() if anahtar else ""})
    print(f"Kontrol tarihi: {bugun} · konu: {len(konular)} · mod: {'çevrimdışı (link testi yok)' if cevrimdisi else 'canlı (curl + anahtar kelime)'}\n")
    print("| ID | Konu | Kaynak | Bağımsız alan | Açılan (200+anahtar) | Açılan bağımsız | Son 30 gün (B) | Sonuç |")
    print("|---|---|---|---|---|---|---|---|")
    hepsi = True
    sayac = {"A": 0, "B": 0, "C": 0}
    for k in konular:
        alanlar = {alan(x["url"]) for x in k["k"]}
        acilan = []
        notlar = []
        for x in k["k"]:
            if cevrimdisi:
                continue
            kod, ok = ac(x["url"], x["anahtar"])
            if ok:
                acilan.append(x)
            else:
                notlar.append(f"{alan(x['url'])}:{kod}")
        acilan_alan = {alan(x["url"]) for x in acilan}
        guncel = "—"
        guncel_ok = True
        if k["id"].startswith("B"):
            n = sum(1 for x in k["k"] if x["tarih"] and dt.date.fromisoformat(x["tarih"]) >= sinir)
            guncel = str(n)
            guncel_ok = n >= 1
        gecti = len(alanlar) >= 2 and (cevrimdisi or len(acilan_alan) >= 2) and guncel_ok
        hepsi &= gecti
        sayac[k["id"][0]] += 1
        print(f"| {k['id']} | {k['ad'][:48]} | {len(k['k'])} | {len(alanlar)} | "
              f"{'—' if cevrimdisi else len(acilan)} | {'—' if cevrimdisi else len(acilan_alan)} | {guncel} | "
              f"{'GEÇTİ' if gecti else 'KALDI'}{' (açılmayan: ' + ', '.join(notlar) + ')' if notlar else ''} |")
    print(f"\nSütun sayımı: A={sayac['A']} · B={sayac['B']} · C={sayac['C']} · toplam={len(konular)}")
    print(f"Kapı: {'GEÇTİ' if hepsi and len(konular) >= 15 else 'KALDI'} (her konuda >=2 bağımsız açılan kaynak; B'de >=1 kaynak son 30 gün; toplam >=15)")
    sys.exit(0 if hepsi and len(konular) >= 15 else 1)


if __name__ == "__main__":
    main()
