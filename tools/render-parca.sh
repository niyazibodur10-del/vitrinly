#!/usr/bin/env bash
# Parça render: uzun videoyu N karelik görüntü parçalarına böler, yalnız EKSİK (veya --yeniden ile istenen) parçaları render eder,
# sesi bir kez ayrı render eder, parçaları yeniden kodlamadan birleştirir, son stereo loudnorm uygular (render-son.sh ile aynı).
# Kullanım: tools/render-parca.sh <CompositionId> <cikis.mp4> [--parca 1800] [--yeniden 3,7] [--sifirla] [--ses miks.wav]
#   --ses: kompozisyonun tek ses kaynağı hazır miks ise (ör. video/public/<id>-ses.wav) Remotion ses render'ı atlanır
#   (Pilot ölçümü: ses render'ı ~50 kare/sn → 12 dk ≈ 7 dk [H]). Kompozisyonda başka <Audio> varsa KULLANMA.
#   Parçalar: $PARCA_DIZINI/<Id>/ (varsayılan ~/.finansal-arac/parca; repo dışı). --sifirla tüm parçaları siler.
#   RED sonrası yalnız değişen sahnenin parçası silinir/--yeniden ile verilir → 12 dk videoda tam render yerine ~1/12.
# Neden: tam render (4 vCPU) ~8 kare/sn → 12 dk ≈ 45 dk [H]; her düzeltme turunda tekrar. Parçalı yolda yalnız değişen 60 sn.
# Aday kıyası (2026-10-26, docs/uretim-hatti-testi.md):
#   A) tam render (render-son.sh)                  → basit, her değişiklikte baştan.
#   B) paralel parça (aynı anda 2+ Remotion süreci) → ELENDİ: Remotion zaten --concurrency=nproc ile CPU'yu dolduruyor, kazanç yok.
#   C) sıralı parça + önbellek (bu betik)            → SEÇİLDİ: ilk render ≈ tam render, düzeltme turu yalnız değişen parça.
# Birleştirme: her parça kendi IDR karesiyle başlar, aynı kodlayıcı ayarı → concat demuxer -c copy (kare kaybı yok).
# Ses görüntüden ayrı (--codec=wav) render edilir: AAC parçaları uç uca eklemek sınırda tık/boşluk yapar.
# DİKKAT: Ses/zamanlama (data.ts, wav) değişirse tüm parçalar geçersizdir → --sifirla.
set -euo pipefail
ID="$1"; OUT="$2"; shift 2; PARCA=1800; YENIDEN=""; SIFIRLA=0; SES=""
while [ $# -gt 0 ]; do case "$1" in
  --parca) PARCA="$2"; shift 2;; --yeniden) YENIDEN="$2"; shift 2;; --sifirla) SIFIRLA=1; shift;; --ses) SES="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
  *) echo "bilinmeyen bayrak: $1" >&2; exit 2;; esac; done
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)
[ -n "$B" ] || { echo "HATA: render tarayıcısı yok" >&2; exit 1; }
D="${PARCA_DIZINI:-$HOME/.finansal-arac/parca}/$ID"; [ "$SIFIRLA" = 1 ] && rm -rf "$D"; mkdir -p "$D"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cd "$ROOT/video"
t0=$(date +%s)
npx remotion bundle --out-dir="$TMP/bundle" --log=error >/dev/null
N=$(npx remotion compositions "$TMP/bundle" --browser-executable="$B" 2>/dev/null | awk -v id="$ID" '$1==id{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/ && $(i+1) ~ /^\(/) print $i}')
[ -n "$N" ] || { echo "HATA: kompozisyon bulunamadı veya süre okunamadı: $ID" >&2; exit 1; }
yapilan=0; : > "$TMP/liste.txt"
for ((bas=0, i=0; bas<N; bas+=PARCA, i++)); do
  son=$(( bas+PARCA-1 < N-1 ? bas+PARCA-1 : N-1 )); f="$D/p$(printf %04d $i)-${bas}-${son}.mp4"
  if [[ ",$YENIDEN," == *",$i,"* ]]; then rm -f "$f"; fi
  if [ ! -s "$f" ]; then
    npx remotion render "$TMP/bundle" "$ID" "$f.tmp.mp4" --browser-executable="$B" --codec=h264 --crf=18 --muted \
      --frames="$bas-$son" --concurrency="${RENDER_ESZAMANLI:-$(nproc)}" --log=error && mv "$f.tmp.mp4" "$f"
    yapilan=$((yapilan+1))
  fi
  echo "file '$f'" >> "$TMP/liste.txt"
done
t1=$(date +%s)
if [ -n "$SES" ]; then ffmpeg -v error -y -i "$SES" -c:a pcm_f32le "$TMP/ses.wav"
else npx remotion render "$TMP/bundle" "$ID" "$TMP/ses.wav" --browser-executable="$B" --codec=wav --log=error; fi
ffmpeg -v error -y -f concat -safe 0 -i "$TMP/liste.txt" -c copy "$TMP/goruntu.mp4"
# -shortest KULLANILMAZ: ffmpeg mux tamponu yüzünden görüntünün son 4 karesini kesiyordu (2026-10-27 F7: parçalar 18.949 kare,
# birleşik görüntü 18.949, -shortest'li çıktı 18.945). Süre görüntüye sabitlenir; ses görüntüden uzunsa kırpılır.
VSURE=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=nw=1:nk=1 "$TMP/goruntu.mp4")
J=$(ffmpeg -hide_banner -nostats -i "$TMP/ses.wav" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i "$TMP/goruntu.mp4" -i "$TMP/ses.wav" -map 0:v -map 1:a -c:v copy \
  -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true" \
  -ar 48000 -c:a aac -b:a 192k -t "$VSURE" -movflags +faststart "$OUT"
t2=$(date +%s)
echo "[render-parca] kare=$N parca=$PARCA yeni_render=$yapilan/$(wc -l < "$TMP/liste.txt") goruntu=$((t1-t0))s ses+birlestirme=$((t2-t1))s toplam=$((t2-t0))s" >&2
