#!/usr/bin/env bash
# Remotion render + son ses normalizasyonu (stereo ölçümde -14 LUFS, tepe -1 dBTP).
# Mono anlatım stereoya kopyalanınca ~+3 LU ölçülür; bu yüzden normalizasyon son dosyada yapılır.
# Kullanım: tools/render-son.sh <CompositionId> <cikis.mp4>
set -euo pipefail
ID="$1"; OUT="$2"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell | head -1)
TMP="$(mktemp -d)"
(cd "$ROOT/video" && npx remotion render "$ID" "$TMP/ham.mp4" --browser-executable="$B" --codec=h264 --crf=18 --log=error)
J=$(ffmpeg -hide_banner -nostats -i "$TMP/ham.mp4" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i "$TMP/ham.mp4" -c:v copy -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$OUT"
rm -rf "$TMP"
