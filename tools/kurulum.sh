#!/usr/bin/env bash
# Yeni konteynerde üretim araçlarını kurar (her oturum başında bir kez).
# - Rhubarb Lip Sync: GitHub sürüm indirmesi ağda kapalı → kaynak koddan derlenir (git clone çalışıyor).
# - Python ortamı: faster-whisper (yazıya dökme), torch CPU + spandrel + opencv (karakter görseli büyütme/kesme).
# - Real-ESRGAN x4 ağırlıkları Hugging Face'ten (ai-forever/Real-ESRGAN).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; ARAC="${ARAC_DIZINI:-$HOME/.finansal-arac}"; mkdir -p "$ARAC"
if [ ! -x "$ARAC/rhubarb/build/rhubarb/rhubarb" ]; then
  command -v cmake >/dev/null && dpkg -s libboost-dev >/dev/null 2>&1 || { apt-get update -q >/dev/null; apt-get install -y -q libboost-dev cmake g++; }
  git clone -q --depth 1 https://github.com/DanielSWolf/rhubarb-lip-sync.git "$ARAC/rhubarb"
  # CMake 3.28'de CMP0167 politikası yok → koşullu yap
  sed -i 's/^cmake_policy(SET CMP0167 OLD).*/if(POLICY CMP0167)\n  cmake_policy(SET CMP0167 OLD)\nendif()/' "$ARAC/rhubarb/rhubarb/CMakeLists.txt"
  mkdir -p "$ARAC/rhubarb/build" && (cd "$ARAC/rhubarb/build" && cmake .. -DCMAKE_BUILD_TYPE=Release >/dev/null && make -j"$(nproc)" rhubarb >/dev/null)
fi
if [ ! -x "$ARAC/venv/bin/python" ]; then
  python3 -m venv "$ARAC/venv"
  "$ARAC/venv/bin/pip" -q install faster-whisper soundfile opencv-python-headless
  "$ARAC/venv/bin/pip" -q install torch torchvision --index-url https://download.pytorch.org/whl/cpu
  "$ARAC/venv/bin/pip" -q install spandrel
fi
[ -f "$ARAC/RealESRGAN_x4.pth" ] || curl -sSL -o "$ARAC/RealESRGAN_x4.pth" https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth
(cd "$ROOT/video" && npm ci --silent)
echo "Hazır: RHUBARB=$ARAC/rhubarb/build/rhubarb/rhubarb  PY=$ARAC/venv/bin/python  ESRGAN=$ARAC/RealESRGAN_x4.pth"
