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
# v2 (2026-10-28): bağımsız işler PARALEL (rhubarb derleme ‖ venv+Whisper modelleri ‖ kokoro-venv+ağırlıklar ‖ ESRGAN ‖ npm ci),
#   paketler uv ile (temel imajda; yoksa pip) ve tam sabit sürümle (tools/gereksinim/*.txt, torch TORCH_SURUM). Loglar $ARAC/kurulum-log/.
#   Aday kıyası (temiz ARAC_DIZINI + boş önbellek, ölçüm docs/uretim-kapasitesi.md §1): A) v1 sıralı pip; B) sıralı uv;
#   C) paralel uv (SEÇİLDİ). Elenen: önceden derlenmiş Rhubarb'ı repoya koymak (ikili dosya, lisans/güven denetimi zor;
#   derleme paralel yolda kritik değil), Docker imajı (bulut oturumu imaj seçtirmiyor). Asıl kazanç: SessionStart kancası
#   (.claude/hooks/oturum-baslat.sh) kurulumu oturum başında yapar, bulut konteyner durumu kancadan sonra önbelleğe alınır.
#   Sürüm güncelleme: venv'de yükselt + test et → `pip freeze` ile tools/gereksinim/*.txt yenile (torch satırları hariç).
# Ölçüm (2026-10-26, 4 vCPU): ikinci çalıştırma ~2 sn; sıfırdan kurulum için docs/uretim-hatti-testi.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; ARAC="${ARAC_DIZINI:-$HOME/.finansal-arac}"; mkdir -p "$ARAC"; ARAC="$(cd "$ARAC" && pwd -P)"
adim(){ echo "[kurulum $(date +%T)] $*"; }
# espeak-ng veri yolu ~160 karakterde kesiliyor → uzun ARAC_DIZINI'nde Kokoro "phontab: No such file" verir (2026-10-26 ölçümü:
# 174 karakterlik yol kırıldı, /root/... çalıştı). Veri yolu = $ARAC + 70 karakter.
[ $(( ${#ARAC} + 70 )) -lt 150 ] || { echo "HATA: ARAC_DIZINI çok uzun (${#ARAC} karakter; en çok 79): $ARAC" >&2; exit 1; }
LOG="$ARAC/kurulum-log"; mkdir -p "$LOG"; ISLER=(); PIDLER=(); T0=$(date +%s)
is_(){ local ad="$1"; shift; adim "başladı: $ad (log: $LOG/$ad.log)"; ( set -euo pipefail; s=$(date +%s); "$@"; echo "[$ad] $(( $(date +%s) - s )) sn" ) >"$LOG/$ad.log" 2>&1 & ISLER+=("$ad"); PIDLER+=($!); }
# Paket kurucu: uv (temel imajda var; pip'ten ~5–10x hızlı, önbellek venv'ler arası hardlink) → yoksa pip.
UV="$(command -v uv || true)"
pk(){ local py="$1"; shift; if [ -n "$UV" ]; then "$UV" pip install -q --python "$py" "$@"; else "$py" -m pip install -q "$@"; fi; }
mkvenv(){ local pyv="$1" hedef="$2"; if [ -n "$UV" ]; then "$UV" venv -q --seed --allow-existing --python "$pyv" "$hedef"; else "$pyv" -m venv "$hedef"; fi; }
TORCH_SURUM="2.14.1+cpu"; TORCHVISION_SURUM="0.29.1+cpu"; TORCH_IDX="https://download.pytorch.org/whl/cpu"
GER="$ROOT/tools/gereksinim"
# apt (yalnız eksikse; temel imajda cmake/g++/boost/python3.12 var). Paralel işlerden ÖNCE: apt kilidi çakışmasın.
EKSIK=(); command -v cmake >/dev/null || EKSIK+=(cmake); command -v g++ >/dev/null || EKSIK+=(g++); dpkg -s libboost-dev >/dev/null 2>&1 || EKSIK+=(libboost-dev)
{ command -v python3.12 >/dev/null && python3.12 -c "import ensurepip" 2>/dev/null; } || EKSIK+=(python3.12 python3.12-venv)
[ ${#EKSIK[@]} -eq 0 ] || { adim "apt: ${EKSIK[*]}"; apt-get update -q >/dev/null; apt-get install -y -q "${EKSIK[@]}" >/dev/null; }

rhubarb_kur(){
  rm -rf "$ARAC/rhubarb"; git clone -q --depth 1 https://github.com/DanielSWolf/rhubarb-lip-sync.git "$ARAC/rhubarb"
  # CMake 3.28'de CMP0167 politikası yok → koşullu yap
  sed -i 's/^cmake_policy(SET CMP0167 OLD).*/if(POLICY CMP0167)\n  cmake_policy(SET CMP0167 OLD)\nendif()/' "$ARAC/rhubarb/rhubarb/CMakeLists.txt"
  mkdir -p "$ARAC/rhubarb/build" && cd "$ARAC/rhubarb/build" && cmake .. -DCMAKE_BUILD_TYPE=Release >/dev/null && make -j"$(nproc)" rhubarb
}
venv_kur(){
  if ! "$ARAC/venv/bin/python" -c "import importlib.util as u,sys; sys.exit(not all(u.find_spec(m) for m in ['faster_whisper','spandrel','cv2','soundfile','torch']))" 2>/dev/null; then
    mkvenv python3 "$ARAC/venv"
    pk "$ARAC/venv/bin/python" --index-url "$TORCH_IDX" "torch==$TORCH_SURUM" "torchvision==$TORCHVISION_SURUM"
    pk "$ARAC/venv/bin/python" -r "$GER/venv.txt"
  fi
  for M in medium.en small.en; do
    HF_HUB_OFFLINE=1 "$ARAC/venv/bin/python" -c "from faster_whisper.utils import download_model as d; d('$M')" >/dev/null 2>&1 \
      || "$ARAC/venv/bin/python" -c "from faster_whisper.utils import download_model as d; d('$M')" >/dev/null
  done
}
kokoro_kur(){
  if ! "$ARAC/kokoro-venv/bin/python" -c "import importlib.util as u,sys; sys.exit(not all(u.find_spec(m) for m in ['kokoro','misaki','soundfile','en_core_web_sm','torch']))" 2>/dev/null; then
    mkvenv python3.12 "$ARAC/kokoro-venv"
    pk "$ARAC/kokoro-venv/bin/python" --index-url "$TORCH_IDX" "torch==$TORCH_SURUM"
    pk "$ARAC/kokoro-venv/bin/python" -r "$GER/kokoro.txt"
    pk "$ARAC/kokoro-venv/bin/python" https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl \
      || pk "$ARAC/kokoro-venv/bin/python" https://huggingface.co/spacy/en_core_web_sm/resolve/main/en_core_web_sm-any-py3-none-any.whl
  fi
  local K="from huggingface_hub import hf_hub_download as d
for f in ['config.json','kokoro-v1_0.pth','voices/am_fenrir.pt','voices/am_michael.pt']: d('hexgrad/Kokoro-82M', f)"
  HF_HUB_OFFLINE=1 "$ARAC/kokoro-venv/bin/python" -c "$K" 2>/dev/null || "$ARAC/kokoro-venv/bin/python" -c "$K"
}
esrgan_kur(){ curl -fsSL -o "$ARAC/RealESRGAN_x4.pth.tmp" https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth && mv "$ARAC/RealESRGAN_x4.pth.tmp" "$ARAC/RealESRGAN_x4.pth"; }
KILIT="$(sha256sum "$ROOT/video/package-lock.json" | cut -d' ' -f1)"
npm_kur(){ cd "$ROOT/video" && npm ci --silent --no-audit --no-fund --prefer-offline && echo "$KILIT" > "$ROOT/video/node_modules/.kurulum-kilit"; }

# Hızlı yol kontrolleri (ikinci çalıştırma ≈2 sn): yalnız eksik olan iş başlatılır; işler birbirinden bağımsız → paralel.
[ -x "$ARAC/rhubarb/build/rhubarb/rhubarb" ] || is_ rhubarb rhubarb_kur
VENV_TAMAM=0; [ -x "$ARAC/venv/bin/python" ] && "$ARAC/venv/bin/python" -c "import importlib.util as u,sys; sys.exit(not all(u.find_spec(m) for m in ['faster_whisper','spandrel','cv2','soundfile','torch']))" 2>/dev/null \
  && HF_HUB_OFFLINE=1 "$ARAC/venv/bin/python" -c "from faster_whisper.utils import download_model as d; d('medium.en'); d('small.en')" >/dev/null 2>&1 && VENV_TAMAM=1
[ "$VENV_TAMAM" = 1 ] || is_ venv venv_kur
KOK_TAMAM=0; [ -x "$ARAC/kokoro-venv/bin/python" ] && "$ARAC/kokoro-venv/bin/python" -c "import importlib.util as u,sys; sys.exit(not all(u.find_spec(m) for m in ['kokoro','misaki','soundfile','en_core_web_sm','torch']))" 2>/dev/null \
  && HF_HUB_OFFLINE=1 "$ARAC/kokoro-venv/bin/python" -c "
from huggingface_hub import hf_hub_download as d
for f in ['config.json','kokoro-v1_0.pth','voices/am_fenrir.pt','voices/am_michael.pt']: d('hexgrad/Kokoro-82M', f)" 2>/dev/null && KOK_TAMAM=1
[ "$KOK_TAMAM" = 1 ] || is_ kokoro kokoro_kur
[ -s "$ARAC/RealESRGAN_x4.pth" ] || is_ esrgan esrgan_kur
[ "$(cat "$ROOT/video/node_modules/.kurulum-kilit" 2>/dev/null)" = "$KILIT" ] || is_ npm npm_kur
HATA=0
for i in "${!PIDLER[@]}"; do
  if wait "${PIDLER[$i]}"; then adim "bitti: ${ISLER[$i]} ($(tail -1 "$LOG/${ISLER[$i]}.log"))"
  else HATA=1; echo "HATA: ${ISLER[$i]} başarısız — son satırlar ($LOG/${ISLER[$i]}.log):" >&2; tail -25 "$LOG/${ISLER[$i]}.log" >&2; fi
done
[ "$HATA" = 0 ] || exit 1
[ ${#ISLER[@]} -eq 0 ] || adim "kurulan: ${ISLER[*]} — toplam $(( $(date +%s) - T0 )) sn"
ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell >/dev/null 2>&1 \
  || echo "UYARI: render tarayıcısı (/opt/pw-browsers/chromium_headless_shell-*) yok → tools/render-son.sh çalışmaz" >&2
echo "Hazır: RHUBARB=$ARAC/rhubarb/build/rhubarb/rhubarb  PY=$ARAC/venv/bin/python  TTS_PY=$ARAC/kokoro-venv/bin/python  ESRGAN=$ARAC/RealESRGAN_x4.pth"
