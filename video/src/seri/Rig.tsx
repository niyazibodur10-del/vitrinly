import React from "react";
import { Img, random, staticFile } from "remotion";
import type { GozElips, Konusmaci, RigKarakter } from "./tipler";
import { agizDurumu, type AgizDurum } from "./zaman";

// Rig katmanı (animasyon-yonetmeni 2026-11-11): taban görseli + 3 durumlu ağız yaması (2 karelik alfa karışımı)
// + kodla göz kırpma (ten rengi kapak, 3–5 sn'de bir, 4 kare) + nefes (alt kenara yaslı, ölçek ≥1 → kesik kenar içeri girmez).
// Hepsi görselin piksel uzayında tek kutuda: kamera/yerleşim dönüşümü tabanla birebir aynı uygulanır (dikiş yok).

export const AGIZ_GECIS_SN = 2 / 30;

/** Göz kırpma takvimi: kişi başına deterministik 3–5 sn aralık; her kırpma 4 kare. */
const KIRPMA_KARE = [0.55, 1, 0.9, 0.45];
const takvimler: Partial<Record<Konusmaci, number[]>> = {};
export const kirpmaTakvimi = (kim: Konusmaci, sure = 120): number[] => {
  if (takvimler[kim]) return takvimler[kim]!;
  const out: number[] = [];
  let t = 0.9 + random(`kirp-${kim}-0`) * 1.6;
  for (let i = 1; t < sure; i++) {
    out.push(t);
    t += 3 + random(`kirp-${kim}-${i}`) * 2;
  }
  takvimler[kim] = out;
  return out;
};
export const kapakOrani = (kim: Konusmaci, t: number, fps = 30): number => {
  for (const b of kirpmaTakvimi(kim)) {
    const k = Math.floor((t - b) * fps + 1e-6);
    if (k >= 0 && k < KIRPMA_KARE.length) return KIRPMA_KARE[k];
    if (b > t) break;
  }
  return 0;
};

const koyult = (hex: string, f: number) => {
  const n = parseInt(hex.slice(1), 16);
  const c = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map((v) => Math.round(v * f));
  return `rgb(${c.join(",")})`;
};

/** Göz kapakları: görsel boyutunda SVG. Her göz badem (iki köşe + üst/alt kavis) ile kırpılır; kapak ten renginde
 *  (yumuşak kenar), kapak kenarında koyu kirpik kavisi. oran 1 = kapalı (kenar alt kapakta, aşağı kavisli). */
export const GozKapaklari: React.FC<{ gozler: GozElips[]; w: number; h: number; oran: number; id: string }> = ({ gozler, w, h, oran, id }) => {
  if (oran <= 0) return null;
  return (
    <svg viewBox={`0 0 ${w} ${h}`} width={w} height={h} style={{ position: "absolute", left: 0, top: 0 }}>
      <defs>
        <filter id={`${id}-yum`} x="-20%" y="-40%" width="140%" height="180%">
          <feGaussianBlur stdDeviation="1.6" />
        </filter>
      </defs>
      {gozler.map((g, i) => {
        const R = g.ry + 3, X = g.rx + 4;
        const x0 = g.cx - X, x1 = g.cx + X, cy = g.cy;
        const badem = `M ${x0} ${cy} Q ${g.cx} ${cy - 2.1 * R} ${x1} ${cy} Q ${g.cx} ${cy + 2.0 * R} ${x0} ${cy} Z`;
        // kenarın orta noktası: açık → üst kavis (cy−R), kapalı → alt kapak çizgisi (cy+0,8R); kapalıda badem tamamen dolar
        const tepe = cy - R + 1.8 * R * oran;
        const kc = 2 * tepe - cy; // kuadratik kontrol
        const kenar = `M ${x0 - 2} ${cy} Q ${g.cx} ${kc} ${x1 + 2} ${cy}`;
        const kapak = oran >= 0.85
          ? `M ${x0 - 4} ${cy - 2.5 * R} L ${x1 + 4} ${cy - 2.5 * R} L ${x1 + 4} ${cy + 2.5 * R} L ${x0 - 4} ${cy + 2.5 * R} Z`
          : `M ${x0 - 4} ${cy - 2.5 * R} L ${x1 + 4} ${cy - 2.5 * R} L ${x1 + 4} ${cy} Q ${g.cx} ${kc} ${x0 - 4} ${cy} Z`;
        return (
          <g key={i} transform={`rotate(${g.aci} ${g.cx} ${g.cy})`}>
            <clipPath id={`${id}-k${i}`}><path d={badem} /></clipPath>
            <linearGradient id={`${id}-g${i}`} x1="0" y1={cy - R} x2="0" y2={cy + R} gradientUnits="userSpaceOnUse">
              <stop offset="0" stopColor={koyult(g.ten, 0.93)} />
              <stop offset="1" stopColor={koyult(g.ten, 1.0)} />
            </linearGradient>
            <g clipPath={`url(#${id}-k${i})`}>
              <path d={kapak} fill={`url(#${id}-g${i})`} filter={`url(#${id}-yum)`} />
            </g>
            <path d={kenar} fill="none" stroke="#2a1812" strokeWidth={Math.max(3.5, R * 0.17)} strokeLinecap="round" opacity={0.92} />
          </g>
        );
      })}
    </svg>
  );
};

/** Konuşma tabanı + ağız + göz + nefes. Kutu: görsel pikseli (w×h); dış yerleşimi çağıran verir. */
export const RigKatman: React.FC<{
  kim: Konusmaci; r: RigKarakter; t: number;
  agiz?: { bas: number; bitis: number; sekil: AgizDurum }[];
}> = ({ kim, r, t, agiz }) => {
  const a = agizDurumu(agiz, t, AGIZ_GECIS_SN);
  const dosya = (d: AgizDurum) => r.agiz[d];
  // nefes: 0,25 Hz, ölçek 1 → 1,006 (alt merkez); hafif omuz kalkışı
  const ev = kim === "jake" ? 0 : 1.7;
  const nef = 1 + 0.003 * (1 + Math.sin(2 * Math.PI * 0.25 * t + ev));
  const oran = kapakOrani(kim, t);
  return (
    <div style={{ position: "absolute", left: 0, top: 0, width: r.w, height: r.h, transformOrigin: `${r.w / 2}px ${r.h}px`, transform: `scale(${nef})` }}>
      <Img src={staticFile(r.taban)} style={{ position: "absolute", left: 0, top: 0, width: r.w, height: r.h }} />
      {a.alt !== "kapali" || a.ust !== "kapali" ? (
        <div style={{ position: "absolute", left: r.agiz.x, top: r.agiz.y, width: r.agiz.w, height: r.agiz.h }}>
          <Img src={staticFile(dosya(a.alt))} style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }} />
          {a.p > 0 && a.ust !== a.alt ? (
            <Img src={staticFile(dosya(a.ust))} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: a.p }} />
          ) : null}
        </div>
      ) : null}
      <GozKapaklari gozler={r.gozler} w={r.w} h={r.h} oran={oran} id={`gk-${kim}`} />
    </div>
  );
};

/** İfade portresi (ağız oynamaz) + istenirse göz kırpma + nefes. */
export const PortreKatman: React.FC<{ kim: Konusmaci; p: RigKarakter["portreler"][string]; t: number; maske?: string }> = ({ kim, p, t, maske }) => {
  const nef = 1 + 0.003 * (1 + Math.sin(2 * Math.PI * 0.25 * t + (kim === "jake" ? 0 : 1.7)));
  const oran = p.gozler ? kapakOrani(kim, t) : 0;
  return (
    <div style={{ position: "absolute", left: p.xy[0], top: p.xy[1], width: p.w, height: p.h, transformOrigin: "0 0", transform: `scale(${p.olcek})`, WebkitMaskImage: maske, maskImage: maske }}>
      <div style={{ position: "absolute", inset: 0, transformOrigin: `${p.w / 2}px ${p.h}px`, transform: `scale(${nef})` }}>
        <Img src={staticFile(p.dosya)} style={{ position: "absolute", left: 0, top: 0, width: p.w, height: p.h }} />
        {p.gozler ? <GozKapaklari gozler={p.gozler} w={p.w} h={p.h} oran={oran} id={`gp-${kim}`} /> : null}
      </div>
    </div>
  );
};
