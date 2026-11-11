#!/usr/bin/env bash
# Bölüm sesi tek komut (ses-yonetmeni 2026-11-11): diyalog → transkript + WER → LUFS → Rhubarb (konuşmacı başına) → kilit.
# Kullanım: tools/ses/bolum-ses.sh <bolum-dizini> [girdi.txt] [--ses JAKE=pocket:michael --ses MIKE=pocket:marius ...]
#   girdi varsayılanı: <dizin>/ses/bolum-tts.txt varsa o, yoksa <dizin>/bolum.txt
# Çıktı (<dizin>/ses/): <ad>.wav (+ .m4a), <ad>.zaman.json, <ad>-JAKE/MIKE.wav/.txt, referans.txt, kelimeler.json,
#   rhubarb/JAKE.json, rhubarb/MIKE.json, kilit.json (sha256, süre, WER, LUFS, TP, sesler). <ad> = dizin adı (bolum-001).
# Kapılar (ekrana): süre 60–90 sn, WER ≤ %5, LUFS −14 ±0,5. Kapıdan kalırsa çıkış kodu 2 (dosyalar yine yazılır).
set -euo pipefail
DIZIN="$(cd "$1" && pwd)"; shift
GIRDI=""; if [ $# -gt 0 ] && [ "${1:0:2}" != "--" ]; then GIRDI="$(realpath "$1")"; shift; fi
[ -z "$GIRDI" ] && { [ -f "$DIZIN/ses/bolum-tts.txt" ] && GIRDI="$DIZIN/ses/bolum-tts.txt" || GIRDI="$DIZIN/bolum.txt"; }
ARAC="$(cd "$(dirname "$0")" && pwd)"; A=~/.finansal-arac
GV="$A/gercekci-venv/bin/python"; [ -x "$GV" ] || GV="$A/kokoro-venv/bin/python"
V="$A/venv/bin/python"; R="$(find "$A/rhubarb" -name rhubarb -type f -perm -u+x | head -1)"
AD="$(basename "$DIZIN")"; S="$DIZIN/ses"; mkdir -p "$S/rhubarb"; TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
t0=$(date +%s)
"$GV" "$ARAC/diyalog.py" "$GIRDI" "$S/$AD.wav" "$@" 2>&1 | grep -v -i -E 'warn|^\s*$|super\(\)|WeightNorm' || true
[ -f "$S/$AD.zaman.json" ] || { echo "diyalog üretilemedi"; exit 1; }
t1=$(date +%s)
"$V" -c "import json,sys;print('\n'.join(s['metin'] for s in json.load(open(sys.argv[1]))['satirlar']))" "$S/$AD.zaman.json" > "$S/referans.txt"
"$V" "$ARAC/yaziya-dok.py" "$S/$AD.wav" "$S/kelimeler.json" small.en >/dev/null 2>&1
WER=$(python3 "$ARAC/hata-orani.py" "$S/referans.txt" "$S/kelimeler.json" | tee "$TMP/wer.txt" | sed -n 's/.*WER=%\([0-9.]*\).*/\1/p')
OL=$(ffmpeg -hide_banner -nostats -i "$S/$AD.wav" -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p')
LUFS=$(echo "$OL" | awk '/ I:/{print $2; exit}'); TP=$(echo "$OL" | awk '/Peak:/{print $2; exit}')
for k in $(ls "$S" | sed -n "s/^$AD-\([A-Z]*\)\.wav$/\1/p"); do
  ffmpeg -v error -y -i "$S/$AD-$k.wav" -ar 16000 -ac 1 -c:a pcm_s16le "$TMP/$k.wav"
  "$R" -q --dialogFile "$S/$AD-$k.txt" -f json "$TMP/$k.wav" -o "$S/rhubarb/$k.json" &
done; wait
ffmpeg -v error -y -i "$S/$AD.wav" -c:a aac -b:a 160k "$S/$AD.m4a"
"$V" - "$S" "$AD" "$GIRDI" "$WER" "$LUFS" "$TP" "$((t1 - t0))" "$(date +%s)" "$t0" <<'EOF'
import json, sys, hashlib, os, datetime
S, AD, GIRDI, WER, LUFS, TP, TU, TN, T0 = sys.argv[1:]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
z = json.load(open(f"{S}/{AD}.zaman.json"))
dosya = {os.path.basename(p): sha(p) for p in [GIRDI, f"{S}/{AD}.wav"] + [f"{S}/{x}" for x in sorted(os.listdir(S)) if x.startswith(AD + "-") and x.endswith(".wav")]}
rh = {}
for f in sorted(os.listdir(f"{S}/rhubarb")):
    c = json.load(open(f"{S}/rhubarb/{f}"))["mouthCues"]; k = f[:-5]
    kendi = [s for s in z["satirlar"] if s["konusmaci"] == k]
    rh[k] = {"cue": len(c), "satir_hareketli": sum(1 for s in kendi if any(x["value"] != "X" and x["start"] < s["bitis"] and x["end"] > s["bas"] for x in c)), "satir": len(kendi)}
k = {"tarih": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%MZ"), "sesler": z["sesler"], "sure_sn": z["sure"], "wer_yuzde": float(WER),
     "lufs": float(LUFS), "tp_dbfs": float(TP), "uretim_sn": int(TU), "toplam_sn": int(TN) - int(T0), "sha256_12": dosya, "rhubarb": rh}
json.dump(k, open(f"{S}/kilit.json", "w"), indent=1, ensure_ascii=False)
kapi = {"süre 60–90": 60 <= z["sure"] <= 90, "WER ≤5": float(WER) <= 5, "LUFS −14±0,5": abs(float(LUFS) + 14) <= 0.5,
        "Rhubarb tüm satırlar": all(v["satir_hareketli"] == v["satir"] for v in rh.values())}
print(f"{AD}: {z['sure']:.1f} sn · WER %{WER} · {LUFS} LUFS TP {TP} · üretim {TU} sn, toplam {k['toplam_sn']} sn · {z['sesler']}")
print("Rhubarb:", rh); print("kapılar:", {a: ("GEÇTİ" if b else "KALDI") for a, b in kapi.items()})
sys.exit(0 if all(kapi.values()) else 2)
EOF
