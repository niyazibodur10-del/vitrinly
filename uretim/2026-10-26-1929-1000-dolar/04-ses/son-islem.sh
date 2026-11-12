#!/usr/bin/env bash
# ses-muhendisi son işlem adayı: <giris.wav> <cikis.wav> "<filtre zinciri veya 'yok'>" -> zincir + 2 geçişli doğrusal loudnorm (I=-14, TP=-1.5), 48 kHz mono 24-bit.
set -euo pipefail
IN="$1"; OUT="$2"; F="$3"; TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
if [ "$F" = "yok" ]; then cp "$IN" "$TMP/a.wav"; else ffmpeg -hide_banner -v error -y -i "$IN" -af "$F" -c:a pcm_f32le "$TMP/a.wav"; fi
J=$(ffmpeg -hide_banner -nostats -i "$TMP/a.wav" -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -hide_banner -v error -y -i "$TMP/a.wav" -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" -ar 48000 -ac 1 -c:a pcm_s24le "$OUT"
