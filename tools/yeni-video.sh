#!/usr/bin/env bash
# Yeni video iskeleti: uretim klasörü + durum.md + yeniden üretim tarifi + Remotion kod klasörü (ortak kit kopyası).
# Kullanım: tools/yeni-video.sh <YYYY-MM-DD-slug> [--kisa K2026Fed] [--kit k1929|yok]
#   uretim/<klasör>/{00-ortam … 09-paket, teslim}/ + durum.md (bugunun-videosu.md §2 tablosu, tüm adımlar BEKLİYOR)
#   uretim/<klasör>/yeniden-uret.adimlar  (tools/yeniden-uret.sh tarifi; animasyon/kurgu doldurur)
#   video/src/videolar/<slug>/ : --kit ile verilen videonun kit dosyaları (kit/ortak/Sunucu/Klon/veri) kopyalanır,
#     public klasör adı <kisa-küçük> yapılır; <Kisa>Iskelet test kompozisyonu Root.tsx'e işaretten eklenir.
#     Kopya (paylaşılan import değil): kilitli eski videonun kodu yeni videonun değişikliğiyle bozulmaz (yeniden üretim
#     birebir kalır). Ortak hale gelmiş parçalar video/src/ortak/'a taşınır (sahibi uretim-muhendisi, içerik animasyon-yonetmeni).
# Elenen: (a) tek paylaşılan kit (eski videonun render'ı sessizce değişir — 2026-10-27 ho.norm dersi);
#         (b) boş klasör (1929'da kit ~600 satırı sıfırdan yazıldı; F5 en uzun faz).
# Seçim klasörü (F2 öncesi, slug yok): tools/yeni-video.sh 2026-10-30-secim → F2 sonunda `git mv`.
set -euo pipefail
[ $# -ge 1 ] || { sed -n 2,4p "$0"; exit 2; }
AD="$1"; shift; KISA=""; KIT="k1929"
while [ $# -gt 0 ]; do case "$1" in --kisa) KISA="$2"; shift 2;; --kit) KIT="$2"; shift 2;; *) echo "bilinmeyen: $1" >&2; exit 2;; esac; done
[[ "$AD" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+$ ]] || { echo "HATA: ad YYYY-MM-DD-slug olmalı (küçük harf, rakam, -): $AD" >&2; exit 2; }
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; U="$ROOT/uretim/$AD"; SLUG="${AD:11}"
[ -e "$U" ] && { echo "HATA: zaten var: $U" >&2; exit 1; }
mkdir -p "$U"/{00-ortam,01-arastirma,02-senaryo,03-metin,04-ses,05-gorsel,06-muzik,07-animasyon,08-kurgu,09-paket,teslim}
for d in "$U"/*/; do touch "$d/.gitkeep"; done
cat > "$U/durum.md" <<EOF
# Durum — $AD

- **Tetik:** (kim, ne zaman, UTC)
- **Kanal:** Toonomy (@toonomy), anlatıcı Leo.
- **Slot ve sütun:** (docs/yayin-takvimi.md)
- **Stok:** uzun ? / Shorts ?
- **Kod:** video/src/videolar/$SLUG/ · kompozisyon öneki ${KISA:-?}
- **Yeniden üretim:** \`tools/yeniden-uret.sh $AD\` (tarif: yeniden-uret.adimlar)

| Adım | Sahip | Durum | Teslim | Test kanıtı | Başlangıç–bitiş (UTC) |
|---|---|---|---|---|---|
| F0 açılış | koordinatör | BEKLİYOR | durum.md | | |
| F0 ortam | uretim-muhendisi | BEKLİYOR | 00-ortam/ortam-raporu.md | | |
| F1 konu havuzu | trend-avcisi | BEKLİYOR | 01-arastirma/konu-havuzu.md | | |
| F1 rakip özeti | kanal-analisti | BEKLİYOR | 01-arastirma/rakip-ozet.md | | |
| F2 senaryolar | senaryo-yazari | BEKLİYOR | 02-senaryo/senaryolar.md | | |
| F2 viralite / ön doğrulama / politika | viralite-analisti ‖ finans-dogrulayici ‖ monetizasyon-uyum-uzmani | BEKLİYOR | 02-senaryo/ | | |
| F2 karar | hakem | BEKLİYOR | 02-senaryo/senaryo-karari.md | | |
| F3 metin + doğrulama | senaryo-yazari → finans-dogrulayici ‖ monetizasyon-uyum-uzmani | BEKLİYOR | 03-metin/metin.md | | |
| F4 ses | ses-yonetmeni → ses-muhendisi | BEKLİYOR | 04-ses/ | | |
| F4 görsel | gorsel-varlik-sanatcisi | BEKLİYOR | 05-gorsel/ | | |
| F4 müzik + SFX adayları | muzik-ses-tasarimcisi | BEKLİYOR | 06-muzik/ | | |
| F4 paket taslağı | thumbnail-tasarimcisi ‖ youtube-paketleyici | BEKLİYOR | 09-paket/ | | |
| F5 kritik yol testi | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/senkron-rapor.md | | |
| F5 tüm sahneler + 9:16 | animasyon-yonetmeni | BEKLİYOR | 07-animasyon/ | | |
| F6 miks | muzik-ses-tasarimcisi | BEKLİYOR | 06-muzik/stems/ | | |
| F7 kurgu | kurgu-editoru | BEKLİYOR | 08-kurgu/ | | |
| F8 paket | thumbnail ‖ paketleyici ‖ viralite → monetizasyon | BEKLİYOR | 09-paket/ | | |
| F9 hakem | hakem | BEKLİYOR | hakem-raporu.md | | |
| F10 teslim | koordinatör | BEKLİYOR | teslim/ | | |

## Sonraki fazlara notlar
EOF
cat > "$U/yeniden-uret.adimlar" <<'EOF'
# tools/yeniden-uret.sh tarifi — konteyner gidince git dışı büyük dosyaları (wav, mp4) yeniden üretir.
# Biçim: her satır "<üretilen dosya (repo köküne göre)> | <komut>" — dosya varsa ve boş değilse adım atlanır.
# Komutlar repo kökünde çalışır; $PY = Whisper/görsel venv, $TTS_PY = Kokoro venv. Sıra önemlidir (bağımlılık sırası).
# Örnek (1929 tarifi: uretim/2026-10-26-1929-1000-dolar/yeniden-uret.adimlar):
# uretim/<klasör>/04-ses/anlatim.wav | ffmpeg -v error -y -i uretim/<klasör>/04-ses/anlatim.m4a -c:a pcm_f32le uretim/<klasör>/04-ses/anlatim.wav
# uretim/<klasör>/08-kurgu/final-16x9.mp4 | tools/render-parca.sh <Kisa>Final uretim/<klasör>/08-kurgu/final-16x9.mp4 --ses <miks.wav>
EOF
echo "[yeni-video] uretim/$AD hazır"
if [ "$KIT" != yok ]; then
  [ -n "$KISA" ] || { echo "HATA: --kit için --kisa <KompozisyonÖneki> gerekli (ör. K2026Fed)" >&2; exit 2; }
  [[ "$KISA" =~ ^[A-Za-z][A-Za-z0-9]*$ ]] || { echo "HATA: --kisa yalnız harf/rakam, harfle başlar" >&2; exit 2; }
  KAY="$ROOT/video/src/$KIT"; [ -d "$KAY" ] || KAY="$ROOT/video/src/videolar/$KIT"
  [ -d "$KAY" ] || { echo "HATA: kit kaynağı yok: $KIT" >&2; exit 1; }
  V="$ROOT/video/src/videolar/$SLUG"; [ -e "$V" ] && { echo "HATA: kod klasörü var: $V" >&2; exit 1; }
  mkdir -p "$V"; KUCUK="$(echo "$KISA" | tr 'A-Z' 'a-z')"; mkdir -p "$ROOT/video/public/$KUCUK"
  for f in kit.tsx ortak.tsx Sunucu.tsx Klon.tsx veri.ts veri-tam.ts; do
    [ -f "$KAY/$f" ] || continue
    sed -e "s#\`k1929/#\`$KUCUK/#g; s#\"k1929t\"#\"$KUCUK\"#g; s#klasor: \"k1929\"#klasor: \"$KUCUK\"#g; s#klasor = \"k1929\"#klasor = \"$KUCUK\"#g" "$KAY/$f" > "$V/$f"
  done
  sed -i "1i // Başlangıç kopyası: video/src/$KIT ($(date +%F), tools/yeni-video.sh). Veri dosyaları (veri*.ts) bu videonun\n// verisiyle yeniden üretilir: tools/animasyon/sahne-veri.py + videoya özel varlık betiği. Görseller video/public/$KUCUK/." "$V/kit.tsx"
  cat > "$V/Kompozisyonlar.tsx" <<EOF
import React from "react";
import { Composition } from "remotion";
import { SahneKok, Yazi } from "./kit";

// İskelet testi (tools/yeni-video.sh): kit derleniyor ve render ediliyor mu? Gerçek sahneler animasyon-yonetmeni'nin.
const Iskelet: React.FC = () => (
  <SahneKok>
    <Yazi an={0} x={960} y={480}>$KISA</Yazi>
  </SahneKok>
);

export const ${KISA}Kompozisyonlar: React.FC = () => (
  <>
    <Composition id="${KISA}Iskelet" component={Iskelet} durationInFrames={30} fps={30} width={1920} height={1080} />
  </>
);
EOF
  R="$ROOT/video/src/Root.tsx"
  grep -q "yeni-video.sh: import" "$R" || { echo "HATA: Root.tsx'te yeni-video işaretleri yok" >&2; exit 1; }
  sed -i "s#^// yeni-video.sh: import\$#import { ${KISA}Kompozisyonlar } from \"./videolar/$SLUG/Kompozisyonlar\";\n// yeni-video.sh: import#" "$R"
  sed -i "s#^\( *\){/\* yeni-video.sh: kompozisyon \*/}\$#\1<${KISA}Kompozisyonlar />\n\1{/* yeni-video.sh: kompozisyon */}#" "$R"
  echo "[yeni-video] video/src/videolar/$SLUG (kit: $KIT) + ${KISA}Iskelet → Root.tsx"
fi
