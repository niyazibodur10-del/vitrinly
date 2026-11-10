#!/usr/bin/env python3
"""Flip By Vote — render öncesi grep + veri kapısı (yayın render'ı yer tutucu / hata ayıklama yazısı / eksik varlıkla başlamaz).

Kullanım:  python3 -I tools/seri/kapi.py <BolumId> [--taslak]
  Çıkış kodu: 0 GEÇTİ · 1 KALDI · 2 kullanım hatası (bölüm bulunamadı vb.)
Denetimler:
  1) Şablon kodu (video/src/seri/**/*.ts[x], bolumler/ hariç): yorumlar atıldıktan sonra console.*, debugger,
     TODO/FIXME/XXX/HACK, ekrana basılan JSON.stringify ve string/JSX metninde "placeholder/debug/lorem/test/yer tutucu" → KALDI.
  2) Bölüm veri dosyası (id'yi tanımlayan bolumler/*.ts + import ettiği .json'lar):
     yayında `yerTutucu` alanı, "TODO/TBD/lorem/placeholder/xxx" dizgileri → KALDI (taslakta yalnız bilgi).
  3) Veride geçen her public/ yolu (seri/...png|jpg|webp|wav|flac|mp3|m4a) video/public altında var mı → yoksa KALDI.
İkinci savunma hattı Remotion içinde: Bolum.tsx dogrula() yayın modunda ilk karede hata fırlatır (süre 60–90, kart
süreleri, yer tutucu, kılavuz). Bu betik o kapıyı render'a girmeden, saniyeler içinde ve kod düzeyinde tamamlar.
Seçim (2026-11-10, uretim-muhendisi): grep + Remotion içi veri kapısı (iki katman) > yalnız Remotion içi kapı (kod
düzeyindeki hata ayıklama yazısını göremez) > yalnız grep (TS yayılımı `...DEMO` ile gelen veriyi göremez).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SERI = ROOT / "video/src/seri"
PUBLIC = ROOT / "video/public"


def yorumsuz(s: str) -> str:
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    return re.sub(r"(^|[^:\"'`])//.*$", r"\1", s, flags=re.M)


KOD_YASAK = [
    (r"\bconsole\.(log|debug|info|warn)\b", "console çağrısı"),
    (r"\bdebugger\b", "debugger"),
    (r"\b(TODO|FIXME|XXX|HACK)\b", "iş notu"),
    (r"JSON\.stringify", "ekrana JSON basma"),
]
METIN_HARIC = {"dogrula.ts"}  # kapı hata iletileri; ekrana çizilmez (render'ı durdurur)
METIN_YASAK = re.compile(r"placeholder|\bdebug\b|lorem|\btest\b|yer ?tutucu|\bTBD\b", re.I)


def kod_denetimi():
    hatalar = []
    for p in sorted(SERI.rglob("*.ts*")):
        if "bolumler" in p.parts:
            continue
        kod = yorumsuz(p.read_text(encoding="utf-8"))
        for i, satir in enumerate(kod.splitlines(), 1):
            for desen, ad in KOD_YASAK:
                if re.search(desen, satir):
                    hatalar.append(f"{p.relative_to(ROOT)}:{i}: {ad}")
            # JSX metni (>...<) ve dizge sabitleri: ekranda görünebilecek yazı
            if p.name in METIN_HARIC:
                continue
            for m in re.findall(r">([^<>{}]+)<|\"([^\"]*)\"|'([^']*)'|`([^`]*)`", satir):
                metin = next((x for x in m if x), "")
                if METIN_YASAK.search(metin) and "yerTutucu" not in metin:
                    hatalar.append(f"{p.relative_to(ROOT)}:{i}: ekranda görünebilecek yazı «{metin.strip()[:40]}»")
    return hatalar


def bolum_dosyasi(bid: str):
    for p in sorted((SERI / "bolumler").glob("*.ts")):
        if re.search(r"\bid:\s*[\"']" + re.escape(bid) + r"[\"']", p.read_text(encoding="utf-8")):
            return p
    return None


def main():
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    taslak = "--taslak" in sys.argv
    if len(arg) != 1:
        print(__doc__.split("\n")[2], file=sys.stderr); sys.exit(2)
    bid = arg[0]
    p = bolum_dosyasi(bid)
    if not p:
        print(f"HATA: {bid} için video/src/seri/bolumler/*.ts içinde `id: \"{bid}\"` yok", file=sys.stderr); sys.exit(2)
    kaynaklar = [p] + [(p.parent / m).resolve() for m in re.findall(r"from\s+\"(\./[^\"]+\.json)\"", p.read_text(encoding="utf-8"))]
    veri = "\n".join(k.read_text(encoding="utf-8") for k in kaynaklar if k.exists())
    eksik_json = [str(k.relative_to(ROOT)) for k in kaynaklar if not k.exists()]

    kaldi, bilgi = [], []
    kaldi += kod_denetimi()
    kaldi += [f"eksik veri dosyası: {k}" for k in eksik_json]
    yt = len(re.findall(r"\byerTutucu\b", yorumsuz(p.read_text(encoding="utf-8"))))
    notlar = re.findall(r"[\"'`][^\"'`]*\b(TODO|TBD|lorem|placeholder|xxx)\b[^\"'`]*[\"'`]", yorumsuz(veri), re.I)
    (bilgi if taslak else kaldi).extend(
        ([f"{p.relative_to(ROOT)}: {yt} yer tutucu işareti (yerTutucu)"] if yt else [])
        + [f"{p.relative_to(ROOT)}: veri dizgisinde «{n}»" for n in notlar])
    yollar = sorted(set(re.findall(r"[\"'](seri/[^\"']+\.(?:png|jpe?g|webp|wav|flac|mp3|m4a))[\"']", veri)))
    for y in yollar:
        if not (PUBLIC / y).exists():
            kaldi.append(f"varlık yok: video/public/{y}")
    for j in kaynaklar[1:]:
        if j.exists():
            try:
                json.loads(j.read_text(encoding="utf-8"))
            except ValueError as e:
                kaldi.append(f"{j.relative_to(ROOT)}: geçersiz JSON ({e})")

    mod = "taslak" if taslak else "yayın"
    for b in bilgi:
        print(f"[kapı] bilgi: {b}")
    if kaldi:
        print(f"[kapı] {bid} ({mod}): KALDI — {len(kaldi)} sorun")
        for k in kaldi:
            print(f"  - {k}")
        sys.exit(1)
    print(f"[kapı] {bid} ({mod}): GEÇTİ — kod temiz, {len(yollar)} varlık mevcut, veri {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
