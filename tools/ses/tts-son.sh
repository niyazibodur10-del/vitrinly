#!/usr/bin/env bash
# TTS ham çıktısını yayın seviyesine getirir: 48 kHz mono, -14 LUFS, true peak <= -1 dBTP (hedef -1.5: AAC kodlaması tepeyi ~0.1-0.3 dB yükseltiyor).
# Kullanım: tools/ses/tts-son.sh <ham.wav> <cikis.wav> [m4a-kopyasi.m4a]
# Zincir: highpass 70 Hz -> hafif de-ess -> hafif kompresör (2.5:1, -24 dB) -> kazanç -> tepe sınırlayıcı (-2 dBFS)
#         -> 2 geçişli doğrusal loudnorm (son düzeltme + true peak garantisi).
# Neden kompresör + sınırlayıcı: Kokoro çıktısının tepe/ortalama oranı ~23 dB; doğrusal loudnorm TP -1'i korumak için
#   kazancı kısıp -14.9 LUFS'ta kalıyordu (2026-10-26 ölçümü). Gürültü giderme YOK (TTS temiz; gereksiz işlem artefakt yapar).
# Not: mono anlatım seviyesidir; videonun SON stereo miksinde tekrar normalize edilir (ortak ders: mono→stereo ~+3 LU).
set -euo pipefail
IN="$1"; OUT="$2"; TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
PRE="aresample=48000:resampler=soxr,highpass=f=70,deesser=i=0.3,acompressor=threshold=-24dB:ratio=2.5:attack=5:release=120:makeup=1"
I=$(ffmpeg -hide_banner -nostats -i "$IN" -af "$PRE,ebur128" -f null - 2>&1 | sed -n '/Summary/,$p' | awk '/ I:/{print $2; exit}')
G=$(python3 -c "print(round(-14.2-($I),2))")
ffmpeg -hide_banner -v error -y -i "$IN" -af "$PRE,volume=${G}dB,alimiter=limit=-2dB:attack=1:release=60:level=false" -c:a pcm_f32le "$TMP/a.wav"
J=$(ffmpeg -hide_banner -nostats -i "$TMP/a.wav" -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -hide_banner -v error -y -i "$TMP/a.wav" -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" -ar 48000 -ac 1 -c:a pcm_s24le "$OUT"
if [ "${3:-}" != "" ]; then ffmpeg -hide_banner -v error -y -i "$OUT" -c:a aac -b:a 192k "$3"; fi
