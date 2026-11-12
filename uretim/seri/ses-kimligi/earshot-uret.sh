#!/usr/bin/env bash
# earshot banka SFX'leri (kendi üretim: MIT kod, Leon Lin). Sabit seed = aynı bayt. Kullanım: earshot-uret.sh <cikis_klasoru>
set -euo pipefail
K="$(cd "$(dirname "$0")" && pwd)"; R="$K/../../.."; O="${1:-$K/aday}"; mkdir -p "$O"
while read -r ad id seed; do
  [ -z "$ad" ] && continue
  "$R/tools/earshot" sfx render "$id" --seed "$seed" --peak -1 -o "$O/es-$ad.wav" --threads 2 2>&1 | grep -o 'wrote.*' | sed "s|$O/||"
done <<'L'
carpma-desk knock/desk 7
carpma-punch cut_hit/punch 7
tik fit/tick/domino 7
swipe swipe/flick 7
ding pro_notify/ding_2045 7
pop-yumusak ui_pop/soft 7
whoosh-kart whoosh_fast/tight 7
gerilim-dusus pro_sub_drop/soft 7
L
