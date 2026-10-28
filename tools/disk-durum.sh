#!/usr/bin/env bash
# Disk/bellek durumu + güvenli temizlik. Varsayılan yalnız RAPOR verir; --temizle ile yalnız yeniden üretilebilir
# geçici dosyaları siler (üretim klasörlerine, modellere, venv'lere DOKUNMAZ).
# Kullanım: tools/disk-durum.sh [--temizle]
# Silinenler (--temizle): 60 dk'dan eski /tmp/tmp* (miks.py/render-son.sh eski sürüm artıkları: ham.wav, m.wav, v.wav, ham.mp4),
#   pip önbelleği (~0,8 GB; kurulum bittiyse gereksiz).
# Neden: 10–14 dk video başına ara dosya ≈ 2 GB [H] (render ham ~0,45 GB + final ~0,45 GB + miks ara WAV ~0,8 GB + görseller);
#   konteyner ~20 GB boş (2026-10-26) → tek oturumda ~8 video sonra dolabilir. Eşik: boş < 5 GB → UYARI.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; ARAC="${ARAC_DIZINI:-$HOME/.finansal-arac}"
BOS_GB=$(df -BG --output=avail / | tail -1 | tr -dc 0-9)
echo "Disk boş: ${BOS_GB} GB | RAM kullanılabilir: $(free -m | awk '/Mem:/{print $7}') MB | çekirdek: $(nproc)"
du -sh "$ARAC" "$HOME/.cache/huggingface" "$HOME/.cache/pip" "$ROOT/video/node_modules" "$ROOT/uretim" 2>/dev/null || true
echo "Üretim klasörleri (büyükten küçüğe):"; du -sh "$ROOT"/uretim/*/ 2>/dev/null | sort -rh | head -10 || true
ESKI=$(find /tmp -maxdepth 1 -name 'tmp*' -type d -mmin +60 2>/dev/null || true)
[ -n "$ESKI" ] && echo "60 dk'dan eski geçici klasör: $(echo "$ESKI" | wc -l) adet, $(du -sch $ESKI 2>/dev/null | tail -1 | cut -f1)"
[ "$BOS_GB" -ge 5 ] || echo "UYARI: disk boşluğu < 5 GB — teslim edilmiş üretimlerin büyük ara dosyalarını (WAV, ham PNG) kaldırın" >&2
if [ "${1:-}" = "--temizle" ]; then
  [ -n "$ESKI" ] && rm -rf $ESKI
  rm -rf "$HOME/.cache/pip"
  echo "Temizlendi. Disk boş: $(df -BG --output=avail / | tail -1 | tr -dc 0-9) GB"
fi
