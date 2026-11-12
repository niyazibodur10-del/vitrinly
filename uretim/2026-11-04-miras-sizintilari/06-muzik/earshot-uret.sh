#!/usr/bin/env bash
# F6b kendi üretim SFX (earshot bankası, sabit varsayılan seed → deterministik). Kullanım: bash 06-muzik/earshot-uret.sh
set -e
B=$(cd "$(dirname "$0")" && pwd); R=$(cd "$B/../../.." && pwd); T=${ES_GECICI:-/tmp/claude-0/-home-user/98cc376a-1af5-5176-856d-bb81c65c71b0/scratchpad/es}; mkdir -p "$T" "$B/kaynak/ozgun"
u() { ad=$1; shift; "$R/tools/earshot" sfx render "$@" --peak -3 -o "$T/$ad.wav" --out "$T/$ad.json" >/dev/null; ffmpeg -v error -y -i "$T/$ad.wav" -c:a flac -sample_fmt s32 "$B/kaynak/ozgun/es-$ad.flac"; }
u whoosh-whip      whoosh_fast/whip  --dur 0.6 --apex 0.20
u whoosh-tight     whoosh_fast/tight --dur 0.5 --apex 0.20
u whoosh-gecis     pro_whoosh_big/windy --dur 0.9 --apex 0.40
u whoosh-yukselen  whoosh_big/swell  --dur 1.4 --apex 1.00
u swish-soft       swish/soft        --dur 0.6 --apex 0.25
u swipe-paper      swipe/paper       --dur 0.7 --apex 0.20
u pop-0 pop/0
u pop-3 pop/3
u ui-pop-soft ui_pop/soft
u click-soft click/soft
u click-thock click/thock
u tap-table tap/table
u knock-wood knock/wood
u knock-desk knock/desk
u hover-tick hover_tick/mid
u zip-up pro_zip/up
u zip-down pro_zip/down_warm
u drip-drop drip/drop
u drip-plink drip/plink
u mallet-celesta mallet/celesta
u mallet-glock mallet/glock
u notify-wood notify/mid_wood
u riser-build riser/build
u impact-punch impact/punch --dur 1.2
u impact-deep impact/deep --dur 2.5
u shimmer pro_shimmer/m3
u toggle-latch toggle/latch
u typing-run pro_typing_run/tick
