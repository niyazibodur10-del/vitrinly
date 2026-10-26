#!/usr/bin/env bash
# Ses temizleme zinciri v1: giriş (ham) -> çıkış (48 kHz mono WAV, -14 LUFS)
# Kullanım: tools/ses-temizle.sh <ham-dosya> <cikis.wav>
# Zincir: highpass -> RNNoise (konuşma/kayıt modeli) -> hafif FFT gürültü -> de-ess -> EQ -> kompresör -> 2 geçişli loudnorm
set -euo pipefail
IN="$1"; OUT="$2"; DIR="$(cd "$(dirname "$0")" && pwd)"
PRE="highpass=f=80,arnndn=m=$DIR/rnnoise-sh.rnnn:mix=0.85,afftdn=nf=-45:nr=8,deesser=i=0.4,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3500:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=3:attack=10:release=150:makeup=2"
# 1. geçiş: ölçüm
J=$(ffmpeg -hide_banner -nostats -i "$IN" -af "$PRE,loudnorm=I=-14:TP=-1:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
# 2. geçiş: doğrusal normalizasyon + baş/son sessizlik kırpma (0.3 sn pay)
ffmpeg -hide_banner -v error -y -i "$IN" -af "$PRE,loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.3,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.3,areverse" -ar 48000 -ac 1 -c:a pcm_s24le "$OUT"
