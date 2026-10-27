import React from "react";
import { Easing, Img, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { POZ } from "./veri";
import { fredoka, k } from "./ortak";

// Klon Leo (Stock / Bank / Box): aynı Leo kesiğinin kopyası + renkli yaka kartı (KOD).
// Yürüme: tek yürüme pozu (C04 / C05) + adım ritminde dikey zıplama, adım eğimi ve ezilme-uzama (2 adım/sn);
// varınca duruş pozuna (C02) geçer ve oturur. Kesikler kadrajın SOLUNA yürür → klonlar sağdan girer. Aynalama YOK
// (saat sol bilekte kalmalı).
// Konum: x = ayak merkezi (sahne koordinatı), ayakY = taban çizgisi, boy = ekrandaki figür yüksekliği (px).
type PozAd = "C02" | "C04" | "C05";

// Yaka kartı konumu (poz kırpımına göre oran) — kareden ölçüldü
const ROZET: Record<PozAd, { x: number; y: number }> = {
  C04: { x: 0.6, y: 0.255 },
  C02: { x: 0.62, y: 0.25 },
  C05: { x: 0.5, y: 0.285 }, // kutunun ön yüzü
};
// Ayak merkezi (kırpım genişliğine oran): yürüyüş pozunda ağırlık önde
const AYAK_X: Record<PozAd, number> = { C04: 0.45, C02: 0.5, C05: 0.5 };

export const Klon: React.FC<{
  yurume: PozAd;
  durus: PozAd;
  xBas: number;
  xBit: number;
  bas: number; // yürüme başlangıcı (sn, Sequence yerel)
  bit: number; // varış (sn)
  ayakY: number;
  boy: number;
  rozet: { etiket: string; renk: string };
  isim?: { metin: string; an: number; son: number };
  ezil?: number; // varsa bu anda utangaç büzülme (kahkaha anı)
  tohum?: number;
}> = ({ yurume, durus, xBas, xBit, bas, bit, ayakY, boy, rozet, isim, ezil, tohum = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const yuruyor = t < bit;
  const poz: PozAd = yuruyor ? yurume : durus;
  const kutu = POZ[poz];
  const olcek = boy / kutu.h;
  const x = interpolate(t, [bas, bit], [xBas, xBit], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.25, 0.1, 0.35, 1),
  });
  // adım fazı: 2 adım/sn, varışa yaklaştıkça genlik azalır
  const faz = (t - bas) * 2 * Math.PI * 2;
  const genlik = yuruyor ? interpolate(t, [bas, bas + 0.15, bit - 0.35, bit], [0, 1, 1, 0.2], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 0;
  const zipla = -Math.abs(Math.sin(faz / 2)) * 9 * genlik;
  const egim = Math.sin(faz / 2) * 1.4 * genlik - 1.2 * genlik; // sola yürürken öne (sola) hafif eğilim
  const ezUz = 1 + Math.cos(faz) * 0.012 * genlik;
  // varış oturması + nefes
  const otur = yuruyor ? 1 : interpolate(t, [bit, bit + 0.07, bit + 0.2], [0.97, 1.015, 1], { extrapolateRight: "clamp" });
  const nefes = yuruyor ? 0 : Math.sin(((t + tohum) / 3.2) * Math.PI * 2) * 0.006;
  const buz = ezil !== undefined ? interpolate(t, [ezil, ezil + 0.12, ezil + 0.5, ezil + 1.4], [0, 1, 1, 0.3], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 0;
  const titre = ezil !== undefined && t > ezil && t < ezil + 0.6 ? Math.sin(t * 70) * 2.5 * (1 - (t - ezil) / 0.6) : 0;
  const w = kutu.w * olcek;
  const isimP = isim ? interpolate(t, [isim.an - 0.05, isim.an + 0.15, isim.son, isim.son + 0.25], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 0;
  if (t < bas - 0.01 && xBas > 1920) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: x - w * AYAK_X[poz] + titre,
        top: ayakY - boy + zipla,
        width: w,
        height: boy,
        transformOrigin: `${AYAK_X[poz] * 100}% 100%`,
        rotate: `${egim}deg`,
        scale: `${(1 + nefes) * otur * (1 + 0.03 * buz)} ${(1 - nefes * 0.3) * otur * ezUz * (1 - 0.05 * buz)}`,
      }}
    >
      <Img src={k(`leo-${poz}.png`)} style={{ width: w, height: boy }} />
      {/* yaka kartı */}
      <div
        style={{
          position: "absolute",
          left: ROZET[poz].x * w - 36,
          top: ROZET[poz].y * boy - 12,
          width: 72,
          height: 26,
          borderRadius: 6,
          background: rozet.renk,
          border: "2.5px solid #101010",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: fredoka,
          fontWeight: 700,
          fontSize: 16,
          color: "#101010",
          letterSpacing: 0.5,
          boxShadow: "0 2px 0 rgba(0,0,0,0.35)",
        }}
      >
        {rozet.etiket}
      </div>
      {/* isim balonu (adı söylendiğinde) */}
      {isim ? (
        <div
          style={{
            position: "absolute",
            left: w / 2 - 130,
            top: -78,
            width: 260,
            textAlign: "center",
            fontFamily: fredoka,
            fontWeight: 700,
            fontSize: 40,
            color: rozet.renk,
            WebkitTextStroke: "9px #0b0b0b",
            paintOrder: "stroke fill",
            opacity: isimP,
            scale: String(0.7 + 0.3 * isimP),
          }}
        >
          {isim.metin}
        </div>
      ) : null}
    </div>
  );
};
