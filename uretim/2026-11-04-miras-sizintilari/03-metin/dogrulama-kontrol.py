"""F3 S03 metin doğrulama: ANLATIM + Shorts okunacak metinden sayı ifadelerini, tavsiye ve mutlak dil kalıplarını çıkarır."""
import re, sys
t = open(sys.argv[1]).read().split("## 3. Retention")[0]
anl = []
for line in t.splitlines():
    if line.startswith("| ") and not line.startswith("| ANLATIM") and not line.startswith("|---") and "**Sahne" in line or "**Grafik" in line:
        anl.append(line.split(" | ")[0].lstrip("| ").strip())
sh = re.findall(r"<<(.*?)(?:>>|$)", open(sys.argv[1]).read(), flags=re.M)
metin = anl + sh
N = r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fourteen|fifteen|eighteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion|half|third|quarter|fifths?|percent|zero|dozens?)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine|ten|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion|percent|tenths?|fifths?|dollars|pounds|years?|boxes))*\b|\d[\d,.]*"
TAV = r"\b(you should|should you|buy|sell|invest in|guarantee\w*|set up a trust|gift it|estate plan|spend down|avoid tax|must|need to)\b"
MUT = r"\b(every|always|never|nobody|everyone|everybody|only|all|most people|truly|nothing)\b"
for i, s in enumerate(metin):
    nums = [m.group(0) for m in re.finditer(N, s, flags=re.I)]
    tv = re.findall(TAV, s, flags=re.I); mt = re.findall(MUT, s, flags=re.I)
    print(f"[{i:02d}] SAYI {nums}\n     TAVSIYE {tv} MUTLAK {mt}")
print("ANLATIM satırı:", len(anl), "Shorts:", len(sh))
