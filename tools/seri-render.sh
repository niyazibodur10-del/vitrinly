#!/usr/bin/env bash
# Flip By Vote bölüm render'ı: kapı → render (render-son.sh: son stereo loudnorm -14 LUFS / -1 dBTP) → çıktı kapısı.
# Kullanım: tools/seri-render.sh <BolumId> <cikis.mp4> [--taslak] [--kilavuz] [--onizleme] [ek remotion bayrakları]
#   (varsayılan) YAYIN: tools/seri/kapi.py (grep + veri + varlık) GEÇMEZSE render başlamaz; Remotion içinde ikinci kapı
#     (video/src/seri/dogrula.ts) yer tutucu / süre 60–90 / kart süreleri / kılavuz ihlalinde ilk karede durur.
#   --taslak: yer tutucu serbest (demo, kanıt); --kilavuz: güvenli alan çizgileri (yalnız taslakla).
#   RENDER_ESZAMANLI (varsayılan 4): Remotion --concurrency. Ölçüm ve seçim aşağıda.
# Çıktı kapısı: ffprobe 1080x1920 / 30 fps / süre = bölüm süresi ±1 kare, h264 + aac 48 kHz; ebur128 I ve TP satırı.
# Süre/bellek ölçümü stderr'e: render süresi, gerçek-zaman oranı, tepe bellek (MemAvailable düşüşü, 0,5 sn örnekleme).
# Ölçüm (2026-11-10, 4 vCPU, yer tutucu demo; ayrıntı: .claude/agents/hafiza/uretim-muhendisi.md):
#   adaylar: tam render c4 (SEÇİLDİ) · tam render c2 · parça render (render-parca.sh, 2×c2). Sonuçlar video/src/seri/README.md.
set -euo pipefail
[ $# -ge 2 ] || { sed -n 2,4p "$0" >&2; exit 2; }
ID="$1"; OUT="$2"; shift 2
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TASLAK=false; KILAVUZ=false; EK=()
for a in "$@"; do
  case "$a" in --taslak) TASLAK=true;; --kilavuz) KILAVUZ=true;; *) EK+=("$a");; esac
done
case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
if $KILAVUZ && ! $TASLAK; then echo "HATA: --kilavuz yalnız --taslak ile" >&2; exit 2; fi

KAPI=(python3 -I "$ROOT/tools/seri/kapi.py" "$ID"); $TASLAK && KAPI+=(--taslak)
"${KAPI[@]}" || { echo "[seri-render] kapı geçmedi → render yok" >&2; exit 1; }

PROPS="{\"bolumId\":\"$ID\",\"taslak\":$TASLAK,\"kilavuz\":$KILAVUZ}"
# bellek örnekleyici: MemAvailable'ın başlangıca göre en büyük düşüşü (render + tarayıcı + ffmpeg)
MEMLOG="$(mktemp)"; ( b=$(awk '/MemAvailable/{print $2}' /proc/meminfo); m=0
  while :; do a=$(awk '/MemAvailable/{print $2}' /proc/meminfo); d=$((b-a)); [ $d -gt $m ] && m=$d && echo $m >"$MEMLOG"; sleep 0.5; done ) &
OP=$!; trap 'kill $OP 2>/dev/null; rm -f "$MEMLOG"' EXIT
t0=$(date +%s.%N)
RENDER_ESZAMANLI="${RENDER_ESZAMANLI:-4}" "$ROOT/tools/render-son.sh" "$ID" "$OUT" --props="$PROPS" "${EK[@]+"${EK[@]}"}"
t1=$(date +%s.%N)
kill $OP 2>/dev/null || true; TEPE=$(cat "$MEMLOG" 2>/dev/null || echo 0)

# çıktı kapısı
# süre = video kare sayısı / fps (format süresi AAC ön dolgusuyla ~0,1 sn uzun çıkar, 2026-11-10)
read -r W H R D VC < <(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=width,height,r_frame_rate,codec_name,nb_read_packets \
  -of default=nw=1 "$OUT" | awk -F= '{v[$1]=$2} END{split(v["r_frame_rate"],f,"/"); print v["width"], v["height"], v["r_frame_rate"], v["nb_read_packets"]*f[2]/f[1], v["codec_name"]}')
AC=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate -of csv=p=0 "$OUT")
BEKLENEN=$(cd "$ROOT/video" && grep -h -A3 "id: \"$ID\"" src/seri/bolumler/*.ts | grep -oE 'sure: [0-9.]+' | head -1 | grep -oE '[0-9.]+' || true)
EB=$(ffmpeg -hide_banner -nostats -i "$OUT" -filter_complex ebur128=peak=true -f null - 2>&1 | awk '/Integrated loudness/{f=1} f&&/ I:/{i=$2} f&&/Peak:/{p=$2} END{print i, p}')
python3 - "$W" "$H" "$R" "$D" "$VC" "$AC" "${BEKLENEN:-0}" "$t0" "$t1" "$TEPE" "$EB" <<'PY'
import sys
w, h, r, d, vc, ac, bek, t0, t1, tepe, eb = sys.argv[1:12]
n, m = map(int, r.split("/")); fps = n / m; d = float(d); bek = float(bek)
sure = float(t1) - float(t0)
sorun = []
if (w, h) != ("1080", "1920"): sorun.append(f"boyut {w}x{h}")
if abs(fps - 30) > 1e-6: sorun.append(f"fps {fps}")
if vc != "h264": sorun.append(f"video kodek {vc}")
if not ac.startswith("aac,48000"): sorun.append(f"ses {ac}")
if bek and abs(d - bek) > 1.5 / 30: sorun.append(f"süre {d:.3f} ≠ {bek}")
print(f"[seri-render] {w}x{h} {fps:g} fps {d:.2f} sn {vc}+{ac} | ebur128 I/TP: {eb} | render {sure:.1f} sn "
      f"({sure / max(d, 1e-9):.2f}x gerçek zaman; 90 sn ≈ {sure / max(d, 1e-9) * 90 / 60:.1f} dk) | tepe bellek ≈ {int(tepe) / 1024 / 1024:.2f} GB",
      file=sys.stderr)
if sorun:
    print("[seri-render] ÇIKTI KAPISI KALDI: " + "; ".join(sorun), file=sys.stderr); sys.exit(1)
print("[seri-render] çıktı kapısı GEÇTİ", file=sys.stderr)
PY
