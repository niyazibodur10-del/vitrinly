#!/usr/bin/env bash
# TTS ham çıktısını yayın seviyesine getirir: 48 kHz mono, highpass 70 Hz, hafif de-ess, 2 geçişli loudnorm.
# Kullanım: tools/ses/tts-son.sh <ham.wav> <cikis.wav> [m4a-kopyasi.m4a]
# Not: TTS çıktısı temiz olduğu için gürültü giderme/kompresör yok (gereksiz işlem artefakt üretir).
# Not 2: Bu mono anlatım seviyesidir; videonun SON stereo miksinde tekrar normalize edilir (ortak ders: mono→stereo ~+3 LU).
set -euo pipefail
IN="$1"; OUT="$2"
PRE="aresample=48000:resampler=soxr,highpass=f=70,deesser=i=0.3"
J=$(ffmpeg -hide_banner -nostats -i "$IN" -af "$PRE,loudnorm=I=-14:TP=-1:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -hide_banner -v error -y -i "$IN" -af "$PRE,loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" -ar 48000 -ac 1 -c:a pcm_s24le "$OUT"
if [ "${3:-}" != "" ]; then ffmpeg -hide_banner -v error -y -i "$OUT" -c:a aac -b:a 192k "$3"; fi
