#!/bin/bash
# SessionStart kancası (uretim-muhendisi, 2026-10-28): bulut oturumunda üretim araçlarını hazır eder.
# - tools/kurulum.sh (idempotent): yeni konteynerde ~4–6 dk, kurulu konteynerde ~2 sn. Bulut ortamı konteyner durumunu
#   kanca bittikten sonra önbelleğe aldığı için sonraki oturumlar kurulu araçlarla açılır.
# - Model dosyalarını arka planda sayfa önbelleğine ısıtır (soğuk diskte ilk Whisper yüklemesi 44–136 sn → ~3 sn).
# - PY / TTS_PY / RHUBARB yollarını oturum ortamına yazar.
# Senkron (async değil): ajanlar araçlara kanca bitmeden dokunursa yarım kurulum görür. Çıktı kısa tutulur (bağlama girer).
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
R="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
A="${ARAC_DIZINI:-$HOME/.finansal-arac}"; mkdir -p "$A"
s=$(date +%s)
if "$R/tools/kurulum.sh" > "$A/oturum-kurulum.log" 2>&1; then
  echo "[oturum] üretim araçları hazır ($(( $(date +%s) - s )) sn; log $A/oturum-kurulum.log)"
else
  echo "[oturum] UYARI: tools/kurulum.sh başarısız — uretim-muhendisi'ne; son satırlar:"; tail -5 "$A/oturum-kurulum.log"
fi
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  { echo "export PY=$A/venv/bin/python"; echo "export TTS_PY=$A/kokoro-venv/bin/python"; echo "export RHUBARB=$A/rhubarb/build/rhubarb/rhubarb"; } >> "$CLAUDE_ENV_FILE"
fi
# Isıtma: Whisper small/medium, Kokoro, ESRGAN ağırlıkları + node_modules/remotion (düşük öncelik, arka planda)
( nice -n 19 find "$HOME/.cache/huggingface/hub" -type f \( -name '*.bin' -o -name '*.pth' -o -name '*.pt' -o -name '*.json' \) -size +100k \
    -exec cat {} + > /dev/null 2>&1; nice -n 19 cat "$A/RealESRGAN_x4.pth" > /dev/null 2>&1 ) </dev/null >/dev/null 2>&1 &
disown || true
exit 0
