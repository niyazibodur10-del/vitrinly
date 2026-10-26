#!/usr/bin/env bash
# Yeni konteynerde üretim araçlarını kurar (her oturum başında bir kez; tekrar çalıştırmak güvenli ve hızlı).
# Kullanım: tools/kurulum.sh            (ARAC_DIZINI ile hedef değiştirilebilir; varsayılan ~/.finansal-arac)
# - Rhubarb Lip Sync: GitHub sürüm indirmesi ağda kapalı → kaynak koddan derlenir (git clone çalışıyor).
# - venv (python3, 3.13): faster-whisper (yazıya dökme), torch CPU + spandrel + opencv (görsel büyütme/kesme).
# - kokoro-venv (python3.12): Kokoro-82M TTS. Kokoro/misaki Python 3.13'te kurulamıyor (2026-10-26) → ayrı ortam.
#   Elenen: tek ortamı 3.12'ye taşımak (Whisper/görsel betikleri 3.13 venv'de test edildi, gereksiz risk);
#   kokoro-onnx (ses kör testi PyTorch Kokoro ile yapıldı, çıktı birebir aynı olmayabilir).
#   misaki'nin çalışma anında indirdiği spaCy en_core_web_sm burada önceden kurulur (önce PyPI-dışı GitHub wheel,
#   olmazsa Hugging Face spacy/en_core_web_sm) → TTS ilk çalıştırmada ağa çıkmaz.
# - Ağırlıklar (Hugging Face, trust_remote_code yok): Real-ESRGAN x4 (ai-forever/Real-ESRGAN),
#   Kokoro-82M (hexgrad/Kokoro-82M: model + am_fenrir/am_michael sesleri), faster-whisper medium.en + small.en.
# - Remotion: `npm ci` yalnız package-lock.json değiştiyse (damga: node_modules/.kurulum-kilit) → ikinci çalıştırma saniyeler.
# Ölçüm (2026-10-26, 4 vCPU): ikinci çalıştırma ~2 sn; sıfırdan kurulum için docs/uretim-hatti-testi.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; ARAC="${ARAC_DIZINI:-$HOME/.finansal-arac}"; mkdir -p "$ARAC"
adim(){ echo "[kurulum $(date +%T)] $*"; }
if [ ! -x "$ARAC/rhubarb/build/rhubarb/rhubarb" ]; then
  adim "Rhubarb derleniyor"
  command -v cmake >/dev/null && dpkg -s libboost-dev >/dev/null 2>&1 || { apt-get update -q >/dev/null; apt-get install -y -q libboost-dev cmake g++; }
  rm -rf "$ARAC/rhubarb"; git clone -q --depth 1 https://github.com/DanielSWolf/rhubarb-lip-sync.git "$ARAC/rhubarb"
  # CMake 3.28'de CMP0167 politikası yok → koşullu yap
  sed -i 's/^cmake_policy(SET CMP0167 OLD).*/if(POLICY CMP0167)\n  cmake_policy(SET CMP0167 OLD)\nendif()/' "$ARAC/rhubarb/rhubarb/CMakeLists.txt"
  mkdir -p "$ARAC/rhubarb/build" && (cd "$ARAC/rhubarb/build" && cmake .. -DCMAKE_BUILD_TYPE=Release >/dev/null && make -j"$(nproc)" rhubarb >/dev/null)
fi
if [ ! -x "$ARAC/venv/bin/python" ] || ! "$ARAC/venv/bin/python" -c "import faster_whisper, spandrel, cv2, soundfile" 2>/dev/null; then
  adim "Python venv (Whisper, torch CPU, spandrel, opencv)"
  python3 -m venv "$ARAC/venv"
  "$ARAC/venv/bin/pip" -q install faster-whisper soundfile opencv-python-headless
  "$ARAC/venv/bin/pip" -q install torch torchvision --index-url https://download.pytorch.org/whl/cpu
  "$ARAC/venv/bin/pip" -q install spandrel
fi
if [ ! -x "$ARAC/kokoro-venv/bin/python" ] || ! "$ARAC/kokoro-venv/bin/python" -c "import kokoro, soundfile, en_core_web_sm" 2>/dev/null; then
  adim "Kokoro TTS ortamı (python3.12)"
  command -v python3.12 >/dev/null && python3.12 -c "import ensurepip" 2>/dev/null || { apt-get update -q >/dev/null; apt-get install -y -q python3.12 python3.12-venv; }
  python3.12 -m venv "$ARAC/kokoro-venv"
  "$ARAC/kokoro-venv/bin/pip" -q install torch --index-url https://download.pytorch.org/whl/cpu
  "$ARAC/kokoro-venv/bin/pip" -q install "kokoro==0.9.4" "misaki[en]==0.9.4" soundfile
  "$ARAC/kokoro-venv/bin/pip" -q install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl \
    || "$ARAC/kokoro-venv/bin/pip" -q install https://huggingface.co/spacy/en_core_web_sm/resolve/main/en_core_web_sm-any-py3-none-any.whl
fi
[ -s "$ARAC/RealESRGAN_x4.pth" ] || { adim "Real-ESRGAN ağırlığı"; curl -fsSL -o "$ARAC/RealESRGAN_x4.pth.tmp" https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth && mv "$ARAC/RealESRGAN_x4.pth.tmp" "$ARAC/RealESRGAN_x4.pth"; }
# Model önbelleği (HF_HOME varsayılanı ~/.cache/huggingface). Önbellekteyse ağa çıkmaz (HF_HUB_OFFLINE denemesi).
HF_HUB_OFFLINE=1 "$ARAC/kokoro-venv/bin/python" -c "
from huggingface_hub import hf_hub_download as d
for f in ['config.json','kokoro-v1_0.pth','voices/am_fenrir.pt','voices/am_michael.pt']: d('hexgrad/Kokoro-82M', f)" 2>/dev/null || {
  adim "Kokoro-82M ağırlıkları"
  "$ARAC/kokoro-venv/bin/python" -c "
from huggingface_hub import hf_hub_download as d
for f in ['config.json','kokoro-v1_0.pth','voices/am_fenrir.pt','voices/am_michael.pt']: d('hexgrad/Kokoro-82M', f)"; }
for M in medium.en small.en; do
  HF_HUB_OFFLINE=1 "$ARAC/venv/bin/python" -c "from faster_whisper.utils import download_model as d; d('$M')" >/dev/null 2>&1 || {
    adim "Whisper $M"; "$ARAC/venv/bin/python" -c "from faster_whisper.utils import download_model as d; d('$M')" >/dev/null; }
done
KILIT="$(sha256sum "$ROOT/video/package-lock.json" | cut -d' ' -f1)"
if [ "$(cat "$ROOT/video/node_modules/.kurulum-kilit" 2>/dev/null)" != "$KILIT" ]; then
  adim "Remotion npm ci"
  (cd "$ROOT/video" && npm ci --silent) && echo "$KILIT" > "$ROOT/video/node_modules/.kurulum-kilit"
fi
ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell >/dev/null 2>&1 \
  || echo "UYARI: render tarayıcısı (/opt/pw-browsers/chromium_headless_shell-*) yok → tools/render-son.sh çalışmaz" >&2
echo "Hazır: RHUBARB=$ARAC/rhubarb/build/rhubarb/rhubarb  PY=$ARAC/venv/bin/python  TTS_PY=$ARAC/kokoro-venv/bin/python  ESRGAN=$ARAC/RealESRGAN_x4.pth"
