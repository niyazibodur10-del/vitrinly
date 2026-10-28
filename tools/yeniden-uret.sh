#!/usr/bin/env bash
# Konteyner gidince kaybolan git dışı büyük dosyaları (wav stem'leri, final mp4, Shorts) tek komutla yeniden üretir.
# Kullanım: tools/yeniden-uret.sh <uretim-klasörü-adı> [--liste] [--zorla <dosya-deseni>] [--kontrol]
#   Tarif: uretim/<klasör>/yeniden-uret.adimlar — her satır "<üretilen dosya> | <komut>"; dosya varsa adım atlanır
#   (yarıda kalırsa yeniden çalıştırmak kaldığı yerden sürer). Komutlar repo kökünde, sırayla çalışır.
#   --liste: yalnız adımları ve durumlarını (VAR/YOK) göster. --zorla: deseni (bash glob) tutan dosyaları silip yeniden üretir.
#   --kontrol: bittikten sonra uretim/<klasör>/08-kurgu/sha256.txt'deki teslim dosyalarının görüntü akışlarını
#     ffprobe ile doğrular (kare sayısı/süre/çözünürlük) ve sha256 eşleşmesini raporlar (bilgi: ses m4a'dan geldiği için
#     sha256 farklı çıkar; görüntü kareleri aynı kod + aynı varlıktan gelir).
#   Ortam: $PY (Whisper/görsel venv), $TTS_PY (Kokoro venv) tarifte kullanılabilir. Önce tools/kurulum.sh.
# Neden (2026-10-28, uretim-muhendisi): 1929 finali için "konteyner giderse K1929Final/Shorts yeniden render ≈35 dk" notu
# vardı ama zincir (anlatım wav → müzik/SFX stem'leri → kurgu miksi → Shorts yatakları → render) 6 betik ve el bilgisi
# istiyordu. Tarif dosyası bu bilgiyi videonun klasöründe tutar; tools/yeni-video.sh her yeni videoya boş tarif koyar.
# Not: komutlar stdin=/dev/null ile çalışır (ffmpeg stdin okuyup tarifin sonraki satırlarını yutuyordu — 2026-10-28 testi).
# Elenen: Makefile (bağımlılık zaman damgası git checkout'ta anlamsız; tüm dosyalar "yeni" görünür), tek dev betik
# (her video farklı zincir).
set -euo pipefail
[ $# -ge 1 ] || { sed -n 2,4p "$0"; exit 2; }
AD="${1%/}"; AD="${AD#uretim/}"; shift; LISTE=0; ZORLA=""; KONTROL=0
while [ $# -gt 0 ]; do case "$1" in --liste) LISTE=1; shift;; --zorla) ZORLA="$2"; shift 2;; --kontrol) KONTROL=1; shift;;
  *) echo "bilinmeyen: $1" >&2; exit 2;; esac; done
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; T="$ROOT/uretim/$AD/yeniden-uret.adimlar"
[ -f "$T" ] || { echo "HATA: tarif yok: $T" >&2; exit 1; }
ARAC="${ARAC_DIZINI:-$HOME/.finansal-arac}"; export PY="$ARAC/venv/bin/python" TTS_PY="$ARAC/kokoro-venv/bin/python" ROOT
cd "$ROOT"; t0=$(date +%s); n=0; yapilan=0
while IFS= read -r satir || [ -n "$satir" ]; do
  [[ "$satir" =~ ^[[:space:]]*(#|$) ]] && continue
  hedef="$(echo "${satir%%|*}" | xargs)"; komut="${satir#*|}"; n=$((n+1))
  hedef="$(eval echo "$hedef")"  # ~ ve $HOME açılır
  if [ -n "$ZORLA" ] && [[ "$hedef" == $ZORLA ]]; then [ "$LISTE" = 1 ] || rm -f "$hedef"; fi
  if [ -s "$hedef" ]; then durum=VAR; else durum=YOK; fi
  if [ "$LISTE" = 1 ]; then printf '%2d %-4s %s\n' "$n" "$durum" "$hedef"; continue; fi
  [ "$durum" = VAR ] && { echo "[yeniden-uret] $n atla (var): $hedef"; continue; }
  echo "[yeniden-uret] $n üret: $hedef"; s=$(date +%s)
  mkdir -p -- "$(dirname -- "$hedef")"
  bash -euo pipefail -c "$komut" </dev/null || { echo "HATA: adım $n başarısız: $komut" >&2; exit 1; }
  [ -s "$hedef" ] || { echo "HATA: adım $n çalıştı ama hedef oluşmadı: $hedef" >&2; exit 1; }
  echo "[yeniden-uret] $n bitti ($(( $(date +%s) - s )) sn)"; yapilan=$((yapilan+1))
done < "$T"
[ "$LISTE" = 1 ] && exit 0
echo "[yeniden-uret] $AD: $yapilan/$n adım üretildi, toplam $(( $(date +%s) - t0 )) sn"
if [ "$KONTROL" = 1 ] && [ -f "uretim/$AD/08-kurgu/sha256.txt" ]; then
  while read -r h f; do
    p="uretim/$AD/08-kurgu/$f"; [ -s "$p" ] || { echo "KONTROL: $f YOK"; continue; }
    v=$(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=width,height,nb_read_packets -of csv=p=0 "$p")
    echo "KONTROL: $f görüntü=$v sha256=$( [ "$(sha256sum "$p" | cut -d' ' -f1)" = "$h" ] && echo aynı || echo farklı)"
  done < "uretim/$AD/08-kurgu/sha256.txt"
fi
