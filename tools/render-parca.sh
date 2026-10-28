#!/usr/bin/env bash
# Parça render: uzun videoyu N karelik görüntü parçalarına böler, yalnız DEĞİŞEN/EKSİK parçaları render eder,
# sesi ayrı alır, parçaları yeniden kodlamadan birleştirir, son stereo loudnorm uygular (render-son.sh ile aynı).
# Kullanım: tools/render-parca.sh <CompositionId> <cikis.mp4> [--parca 1800] [--yeniden 3,7] [--sifirla] [--ses miks.wav]
#             [--kaynak <BaskaId>] [--oto-yok] [--ornek 6] [--onizleme] [--is 2]
#   (varsayılan) OTOMATİK DEĞİŞİKLİK TESPİTİ: önce tüm kompozisyonun her 6. karesi 1/4 ölçekte render edilir ("iz",
#     12 dk ≈ 1–2 dk), son başarılı render'ın iziyle karşılaştırılır (tools/render-iz.py), yalnız farklı parçalar yeniden
#     render edilir. Kod/veri değişince elle --sifirla/--yeniden gerekmez. --oto-yok: eski davranış (yalnız eksik parça).
#   --kaynak <Id>: bu kompozisyonun önbelleği boşsa başka kompozisyonun parçaları + izi hardlink'le tohumlanır
#     (ör. K1929Final ← K1929Tam: kurgu katmanı yalnız birkaç parçayı değiştirir → yalnız onlar render edilir).
#   --ses: kompozisyonun tek ses kaynağı hazır miks ise (ör. video/public/<id>-ses.wav) Remotion ses render'ı atlanır
#     (ses render'ı ~50 kare/sn → 10,5 dk ≈ 30–70 sn). Kompozisyonda başka <Audio> varsa KULLANMA.
#   --onizleme: taslak (960x540, crf 30, x264 veryfast); ayrı önbellek. Yayın dosyası için KULLANMA.
#   --is N (varsayılan 2): aynı anda N parça (her biri --concurrency=nproc/N; bekleyen parça N'den azsa hepsine nproc).
#   Parçalar: $PARCA_DIZINI/<Id>[@onizleme]/ (varsayılan ~/.finansal-arac/parca; repo dışı). --sifirla tüm parçaları siler.
# Neden: tam render (4 vCPU) 1929 finali 18.949 kare 1716 sn (11 kare/sn) [Ö 2026-10-27]; her düzeltme turunda tekrar.
# Aday kıyası (2026-10-26/28, docs/uretim-hatti-testi.md, docs/uretim-kapasitesi.md):
#   A) tam render (render-son.sh)                  → basit, her değişiklikte baştan.
#   B) paralel parça (--is 2)                       → 2026-10-26'da "kazanç yok" diye elenmişti; 2026-10-28 ölçümü (K1929Final
#                                                     1800–2399, 600 kare, boşta): 1×c4 152,0 sn · 2×c2 141,5 sn (−%7) · 1×c3 162,4
#                                                     → D'nin içinde varsayılan --is 2 (tek Remotion süreci CPU'yu %82–96 dolduruyor).
#   C) sıralı parça + önbellek (2026-10-26)         → düzeltme turu yalnız değişen parça, ama geçersizleştirme ELLE (hata riski:
#                                                     unutulan --yeniden eski görüntüyü sessizce yayına sokar).
#   D) C + otomatik iz karşılaştırma (bu sürüm)     → SEÇİLDİ: iz maliyeti ~%5–8, elle geçersizleştirme yok.
#   Elenen iz yöntemi: MD5 (Chromium blur rasterleştirmesi deterministik değil, her şeyi "değişti" sayar → render-iz.py başlığı).
# Birleştirme: her parça kendi IDR karesiyle başlar, aynı kodlayıcı ayarı → concat demuxer -c copy (kare kaybı yok).
# Ses görüntüden ayrı (--codec=wav) render edilir: AAC parçaları uç uca eklemek sınırda tık/boşluk yapar.
# -shortest KULLANILMAZ (2026-10-27 F7: son 4 kareyi kesiyordu) → süre görüntüye sabitlenir (-t).
set -euo pipefail
ID="$1"; OUT="$2"; shift 2; PARCA=1800; YENIDEN=""; SIFIRLA=0; SES=""; KAYNAK=""; OTO=1; ORNEK=6; ONIZ=0; IS=2
while [ $# -gt 0 ]; do case "$1" in
  --parca) PARCA="$2"; shift 2;; --yeniden) YENIDEN="$2"; shift 2;; --sifirla) SIFIRLA=1; shift;;
  --ses) SES="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
  --kaynak) KAYNAK="$2"; shift 2;; --oto-yok) OTO=0; shift;; --ornek) ORNEK="$2"; shift 2;;
  --onizleme) ONIZ=1; shift;; --is) IS="$2"; shift 2;;
  *) echo "bilinmeyen bayrak: $1" >&2; exit 2;; esac; done
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)
[ -n "$B" ] || { echo "HATA: render tarayıcısı yok" >&2; exit 1; }
PY="$HOME/.finansal-arac/venv/bin/python"; [ -x "$PY" ] || PY=python3
EK=""; [ "$ONIZ" = 1 ] && EK="@onizleme"
KOK="${PARCA_DIZINI:-$HOME/.finansal-arac/parca}"; D="$KOK/$ID$EK"; [ "$SIFIRLA" = 1 ] && rm -rf "$D"
if [ -n "$KAYNAK" ] && [ ! -d "$D" ] && [ -d "$KOK/$KAYNAK$EK" ]; then
  mkdir -p "$D"; cp -al "$KOK/$KAYNAK$EK/." "$D/"; echo "[render-parca] önbellek $KAYNAK$EK'ten tohumlandı" >&2
fi
mkdir -p "$D"
KALITE=(--codec=h264 --crf=18); [ "$ONIZ" = 1 ] && KALITE=(--codec=h264 --crf=30 --x264-preset=veryfast --scale=0.5)
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cd "$ROOT/video"
t0=$(date +%s)
npx remotion bundle --out-dir="$TMP/bundle" --log=error >/dev/null
N=$(npx remotion compositions "$TMP/bundle" --browser-executable="$B" 2>/dev/null | awk -v id="$ID" '$1==id{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/ && $(i+1) ~ /^\(/) print $i}')
[ -n "$N" ] || { echo "HATA: kompozisyon bulunamadı veya süre okunamadı: $ID" >&2; exit 1; }
DEGISEN=""
if [ "$OTO" = 1 ]; then
  npx remotion render "$TMP/bundle" "$ID" "$TMP/iz" --sequence --image-format=png --every-nth-frame="$ORNEK" --scale=0.25 \
    --browser-executable="$B" --concurrency="$(nproc)" --log=error >/dev/null
  if [ ! -d "$D/iz" ] && ls "$D"/p*.mp4 >/dev/null 2>&1; then
    # Geçiş: iz'siz eski önbellek (2026-10-28 öncesi) → mevcut parçalara güvenilir (eski davranış), iz bu turda kaydedilir.
    echo "[render-parca] UYARI: önbellekte iz yok → mevcut parçalar geçerli sayıldı; şüphe varsa --sifirla" >&2; : > "$TMP/iz.log"
  else
    DEGISEN=$("$PY" "$ROOT/tools/render-iz.py" "$TMP/iz" "$D/iz" "$ORNEK" "$PARCA" "$N" 2>"$TMP/iz.log") || { cat "$TMP/iz.log" >&2; exit 1; }
  fi
  echo "[render-parca] iz: $(grep -c 'DEĞİŞTİ\|eski iz yok' "$TMP/iz.log" || true) değişen parça ($( [ -n "$DEGISEN" ] && echo "$DEGISEN" || echo yok))" >&2
fi
ti=$(date +%s)
liste=(); bekleyen=()
for ((bas=0, i=0; bas<N; bas+=PARCA, i++)); do
  son=$(( bas+PARCA-1 < N-1 ? bas+PARCA-1 : N-1 )); f="$D/p$(printf %04d $i)-${bas}-${son}.mp4"
  if [[ ",$YENIDEN,$DEGISEN," == *",$i,"* ]]; then rm -f "$f"; fi
  [ -s "$f" ] || bekleyen+=("$bas $son $f")
  liste+=("$f")
done
# Kompozisyon kısaldıysa / parça boyu değiştiyse artık listede olmayan eski parçaları sil
for f in "$D"/p*.mp4; do [ -e "$f" ] || continue; [[ " ${liste[*]} " == *" $f "* ]] || rm -f "$f"; done
calistir(){ local bas=$1 son=$2 f=$3
  npx remotion render "$TMP/bundle" "$ID" "$f.tmp.mp4" --browser-executable="$B" "${KALITE[@]}" --muted \
    --frames="$bas-$son" --concurrency="$ESZ" --log=error >/dev/null && mv "$f.tmp.mp4" "$f"; }
# Eşzamanlılık: bekleyen parça sayısı IS'ten azsa tek parçaya tüm çekirdekler (düzeltme turunda 1 parça → --concurrency=nproc)
ISE=$(( ${#bekleyen[@]} < IS ? ${#bekleyen[@]} : IS )); [ "$ISE" -ge 1 ] || ISE=1
ESZ="${RENDER_ESZAMANLI:-$(( $(nproc) / ISE > 0 ? $(nproc) / ISE : 1 ))}"
hata=0; aktif=0
for is_ in "${bekleyen[@]}"; do
  calistir $is_ & aktif=$((aktif+1))
  if [ "$aktif" -ge "$ISE" ]; then wait -n || hata=1; aktif=$((aktif-1)); fi
done
while [ "$aktif" -gt 0 ]; do wait -n || hata=1; aktif=$((aktif-1)); done
[ "$hata" = 0 ] || { echo "HATA: parça render'ı başarısız" >&2; exit 1; }
# İz yalnız tüm parçalar başarıyla bittikten sonra güncellenir (yarım kalan turda eski iz geçerli kalır)
if [ "$OTO" = 1 ]; then rm -rf "$D/iz.yeni"; mv "$TMP/iz" "$D/iz.yeni"; rm -rf "$D/iz"; mv "$D/iz.yeni" "$D/iz"; fi
t1=$(date +%s)
printf "file '%s'\n" "${liste[@]}" > "$TMP/liste.txt"
if [ -n "$SES" ]; then ffmpeg -v error -y -i "$SES" -c:a pcm_f32le "$TMP/ses.wav"
else npx remotion render "$TMP/bundle" "$ID" "$TMP/ses.wav" --browser-executable="$B" --codec=wav --log=error >/dev/null; fi
ffmpeg -v error -y -f concat -safe 0 -i "$TMP/liste.txt" -c copy "$TMP/goruntu.mp4"
VSURE=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=nw=1:nk=1 "$TMP/goruntu.mp4")
J=$(ffmpeg -hide_banner -nostats -i "$TMP/ses.wav" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
if [ -z "$J" ] || ! python3 -c "import math,sys;v=float(sys.argv[1]);sys.exit(0 if math.isfinite(v) and v>-70 else 1)" "$(g input_i 2>/dev/null)" 2>/dev/null; then
  echo "[render-parca] UYARI: ses ölçülemedi (sessiz/çok kısa) → normalizasyon atlandı; yayın dosyası için kullanmayın" >&2
  ffmpeg -v error -y -i "$TMP/goruntu.mp4" -i "$TMP/ses.wav" -map 0:v -map 1:a -c:v copy -ar 48000 -c:a aac -b:a 192k -t "$VSURE" -movflags +faststart "$OUT"
else
ffmpeg -v error -y -i "$TMP/goruntu.mp4" -i "$TMP/ses.wav" -map 0:v -map 1:a -c:v copy \
  -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true" \
  -ar 48000 -c:a aac -b:a 192k -t "$VSURE" -movflags +faststart "$OUT"
fi
# Kare sayısı kapısı (2026-10-27 -shortest dersi): çıktı kompozisyonla aynı kare sayısında olmalı
KS=$(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of default=nw=1:nk=1 "$OUT")
[ "$KS" = "$N" ] || { echo "HATA: çıktı $KS kare, kompozisyon $N kare" >&2; exit 1; }
t2=$(date +%s)
echo "[render-parca] kare=$N parca=$PARCA yeni_render=${#bekleyen[@]}/${#liste[@]} iz=$((ti-t0))s goruntu=$((t1-ti))s ses+birlestirme=$((t2-t1))s toplam=$((t2-t0))s$( [ "$ONIZ" = 1 ] && echo ' (ONIZLEME)')" >&2
