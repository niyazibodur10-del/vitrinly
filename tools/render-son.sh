#!/usr/bin/env bash
# Remotion render + son ses normalizasyonu (stereo ölçümde -14 LUFS, tepe -1 dBTP).
# Mono anlatım stereoya kopyalanınca ~+3 LU ölçülür; bu yüzden normalizasyon son dosyada yapılır.
# Kullanım: tools/render-son.sh <CompositionId> <cikis.mp4> [ek remotion render bayrakları, ör. --frames=0-299 --concurrency=4]
#   RENDER_ESZAMANLI (varsayılan nproc; Remotion çekirdek sayısından fazlasını reddeder) = Remotion --concurrency. Ölçüm 2026-10-26, 4 vCPU, Pilot 14,1 sn:
#   varsayılan (2) vs 4 vs 6 → docs/uretim-hatti-testi.md. Ara dosyalar $TMPDIR'da, çıkışta silinir (trap).
#   Süre dökümü stderr'e: render / loudnorm ölçüm / son kodlama.
# Elenen: Remotion'ın kendi ses normalizasyonu (yok); render içinde loudnorm (mono kaynak, +3 LU sapma).
set -euo pipefail
ID="$1"; OUT="$2"; shift 2; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)
[ -n "$B" ] || { echo "HATA: render tarayıcısı yok (/opt/pw-browsers/chromium_headless_shell-*)" >&2; exit 1; }
case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
t0=$(date +%s.%N)
(cd "$ROOT/video" && npx remotion render "$ID" "$TMP/ham.mp4" --browser-executable="$B" --codec=h264 --crf=18 \
  --concurrency="${RENDER_ESZAMANLI:-$(nproc)}" --log=error "$@")
t1=$(date +%s.%N)
J=$(ffmpeg -hide_banner -nostats -i "$TMP/ham.mp4" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
t2=$(date +%s.%N)
# Kısa (<0,4 sn ebur128 penceresi) veya sessiz render'da ölçüm -inf/boş çıkar ve ikinci geçiş loudnorm'u
# "measured_I out of range" ile düşer (2026-10-27, 2 karelik test render'ı). O durumda normalizasyon atlanır,
# ses olduğu gibi AAC'ye kodlanır ve uyarı verilir. Elenen: tek geçiş dinamik loudnorm (sessizde anlamsız, sessizce
# yanlış seviye üretir); hata verip durmak (test/önizleme render'larını gereksiz kırar).
IIN=$( [ -n "$J" ] && g input_i 2>/dev/null || echo yok )
if [ -z "$J" ]; then
  echo "[render-son] UYARI: ses akışı yok/ölçülemedi → ses normalizasyonu atlandı" >&2
  ffmpeg -v error -y -i "$TMP/ham.mp4" -c copy -movflags +faststart "$OUT"
elif ! python3 -c "import math,sys;v=float(sys.argv[1]);sys.exit(0 if math.isfinite(v) and v>-70 else 1)" "$IIN" 2>/dev/null; then
  echo "[render-son] UYARI: ölçülen ses seviyesi $IIN LUFS (çok kısa/sessiz render) → normalizasyon atlandı; yayın dosyası için kullanmayın" >&2
  ffmpeg -v error -y -i "$TMP/ham.mp4" -c:v copy -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$OUT"
else
  ffmpeg -v error -y -i "$TMP/ham.mp4" -c:v copy -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$OUT"
fi
t3=$(date +%s.%N)
python3 -c "print(f'[render-son] render={$t1-$t0:.1f}s loudnorm_olcum={$t2-$t1:.1f}s son_kodlama={$t3-$t2:.1f}s toplam={$t3-$t0:.1f}s')" >&2
