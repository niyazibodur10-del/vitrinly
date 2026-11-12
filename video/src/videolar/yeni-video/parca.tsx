import React from "react";
import { AbsoluteFill, interpolate, random } from "remotion";
import { CL, EIO, EOUT, EPOP, PozAdim, RENK, useT } from "./kit";
import { anton, fredoka } from "./ortak";
import { MasaSahne, ZARF_RENK } from "./masa";
import type { SunucuPoz } from "./Sunucu";

// Çekim kalıpları ve ikonlar (animasyon-yonetmeni). Zamanlar sahne yerel saniyesi.

// Leo masada: genis / orta / yakin kamera kalıbı (t0→t1 yavaş itme; hiç durmayan kamera = canlılık)
export const LeoCekim: React.FC<{
  id: string;
  tip: "genis" | "orta" | "yakin";
  t0: number;
  t1: number;
  pozlar?: PozAdim[];
  on?: React.ReactNode;
  arka?: React.ReactNode;
  tohum?: number;
  isik?: number;
  odakX?: number;
}> = ({ id, tip, t0, t1, pozlar = [[0, "a"]], on, arka, tohum = 1, isik, odakX = 960 }) => {
  const K = { genis: [540, 1.0, 1.07], orta: [560, 1.2, 1.28], yakin: [515, 1.48, 1.58] }[tip];
  // arka: ekran uzayında üst katman (yakın planda kadraj dışına taşmaz)
  return (
    <AbsoluteFill>
      <MasaSahne
        kamera={[
          [t0, odakX, K[0], K[1]],
          [t1, odakX, K[0] - 10, K[2]],
        ]}
        leo={{ id, pozlar, tohum }}
        on={on}
        isik={isik}
      />
      {arka}
    </AbsoluteFill>
  );
};

// Büyük başlık (ekran uzayı, üst bant; altyazı bandı y>830 serbest)
export const Baslik: React.FC<{ an: number; children: React.ReactNode; y?: number; boyut?: number; renk?: string; son?: number }> = ({ an, children, y = 70, boyut = 92, renk = RENK.murekkep, son }) => {
  const t = useT();
  if (t < an - 0.03 || (son !== undefined && t > son + 0.2)) return null;
  const p = interpolate(t, [an, an + 0.22], [0, 1], { ...CL, easing: EPOP });
  const q = son !== undefined ? interpolate(t, [son, son + 0.2], [1, 0], CL) : 1;
  return (
    <div style={{ position: "absolute", left: 0, width: 1920, top: y, textAlign: "center", fontFamily: anton, fontSize: boyut, letterSpacing: 2, color: renk, WebkitTextStroke: `${Math.round(boyut * 0.11)}px #0b0b0b`, paintOrder: "stroke fill", opacity: p * q, scale: String(0.7 + 0.3 * p) }}>
      {children}
    </div>
  );
};

// Hap etiket (SHIPS, VETERANS …): renkli zemin üstünde kısa söz
export const Hap: React.FC<{ an: number; x: number; y: number; children: React.ReactNode; renk?: string; boyut?: number; donme?: number; son?: number }> = ({ an, x, y, children, renk = "#f4f1ea", boyut = 40, donme = 0, son }) => {
  const t = useT();
  if (t < an - 0.03 || (son !== undefined && t > son + 0.2)) return null;
  const p = interpolate(t, [an, an + 0.2], [0, 1], { ...CL, easing: EPOP });
  return (
    <div style={{ position: "absolute", left: x, top: y, translate: "-50% -50%", padding: `${boyut * 0.18}px ${boyut * 0.5}px`, borderRadius: boyut * 0.4, background: renk, border: "4px solid #111", fontFamily: fredoka, fontWeight: 700, fontSize: boyut, color: "#111", whiteSpace: "nowrap", scale: String(0.4 + 0.6 * p), opacity: Math.min(1, p * 2), rotate: `${donme}deg`, boxShadow: "0 8px 0 rgba(0,0,0,0.35)" }}>
      {children}
    </div>
  );
};

// Büyük sayı kartı (stat tile): başlık + değer + kaynak satırı
export const SayiKarti: React.FC<{ an: number; x: number; y: number; w: number; ust: string; deger: React.ReactNode; alt?: string; renk?: string }> = ({ an, x, y, w, ust, deger, alt, renk = RENK.murekkep }) => {
  const t = useT();
  if (t < an - 0.03) return null;
  const p = interpolate(t, [an, an + 0.25], [0, 1], { ...CL, easing: EPOP });
  return (
    <div style={{ position: "absolute", left: x, top: y, width: w, padding: "26px 34px", boxSizing: "border-box", background: "rgba(15,22,38,0.94)", border: "3px solid rgba(255,255,255,0.2)", borderRadius: 22, opacity: Math.min(1, p * 2), scale: String(0.85 + 0.15 * p), boxShadow: "0 18px 50px rgba(0,0,0,0.45)" }}>
      <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.ikincil }}>{ust}</div>
      <div style={{ fontFamily: anton, fontSize: 150, lineHeight: 1.1, color: renk }}>{deger}</div>
      {alt ? <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 24, color: RENK.ikincil }}>{alt}</div> : null}
    </div>
  );
};

// ---------- İkonlar (düz, kalın konturlu, yüzsüz; P1: parti/bayrak/kişi yok) ----------
const ST = { stroke: "#111", strokeWidth: 6, strokeLinejoin: "round" as const, strokeLinecap: "round" as const };
const IKON: Record<string, React.ReactNode> = {
  araba: (
    <g {...ST}>
      <path d="M20,120 L30,80 Q40,55 70,55 L130,55 Q160,55 172,80 L182,120 Z" fill="#4da3ff" />
      <rect x={12} y={110} width={176} height={36} rx={10} fill="#4da3ff" />
      <circle cx={55} cy={148} r={18} fill="#333" />
      <circle cx={148} cy={148} r={18} fill="#333" />
      <path d="M52,82 L66,62 L100,62 L100,90 L48,90 Z" fill="#cfe6ff" />
    </g>
  ),
  ev: (
    <g {...ST}>
      <rect x={40} y={80} width={120} height={90} fill="#f1e7d2" />
      <path d="M22,88 L100,22 L178,88 Z" fill="#c4553f" />
      <rect x={86} y={118} width={30} height={52} fill="#7a4b2a" />
    </g>
  ),
  banka: (
    <g {...ST}>
      <path d="M20,70 L100,24 L180,70 Z" fill="#d9c79a" />
      {[40, 75, 110, 145].map((x) => (
        <rect key={x} x={x} y={76} width={18} height={70} fill="#efe6cf" />
      ))}
      <rect x={18} y={146} width={164} height={22} fill="#d9c79a" />
    </g>
  ),
  kure: (
    <g {...ST}>
      <circle cx={100} cy={96} r={70} fill="#3b8de0" />
      <path d="M55,60 Q80,70 72,100 Q60,120 76,140 M120,40 Q140,70 128,90 Q150,110 140,150" fill="none" stroke="#2fae6a" strokeWidth={14} />
      <ellipse cx={100} cy={96} rx={30} ry={70} fill="none" />
    </g>
  ),
  fed: (
    <g {...ST}>
      <rect x={30} y={56} width={140} height={20} fill="#c9ccd6" />
      {[40, 70, 100, 130, 156].map((x) => (
        <rect key={x} x={x - 6} y={76} width={14} height={72} fill="#e6e8ee" />
      ))}
      <rect x={22} y={148} width={156} height={20} fill="#c9ccd6" />
      <path d="M60,56 Q100,10 140,56 Z" fill="#c9ccd6" />
    </g>
  ),
  bono: (
    <g {...ST}>
      <rect x={30} y={40} width={140} height={110} rx={6} fill="#efe6cf" />
      <circle cx={100} cy={92} r={26} fill="none" />
      <path d="M50,62 L80,62 M120,130 L150,130" />
    </g>
  ),
  emekli: (
    <g {...ST}>
      <circle cx={92} cy={44} r={22} fill="#8a93a6" />
      <path d="M70,70 L114,70 L120,150 L64,150 Z" fill="#8a93a6" />
      <path d="M134,86 L140,166" stroke="#7a4b2a" strokeWidth={9} />
    </g>
  ),
  hasta: (
    <g {...ST}>
      <circle cx={100} cy={44} r={22} fill="#8a93a6" />
      <path d="M72,70 L128,70 L134,160 L66,160 Z" fill="#8a93a6" />
      <path d="M100,92 L100,130 M81,111 L119,111" stroke="#e05a4f" strokeWidth={12} />
    </g>
  ),
  asker: (
    <g {...ST}>
      <circle cx={100} cy={50} r={22} fill="#8a93a6" />
      <path d="M74,44 Q100,10 126,44 Z" fill="#5d6b4a" />
      <path d="M72,76 L128,76 L134,160 L66,160 Z" fill="#5d6b4a" />
    </g>
  ),
  ogrenci: (
    <g {...ST}>
      <circle cx={100} cy={52} r={22} fill="#8a93a6" />
      <path d="M60,30 L100,14 L140,30 L100,46 Z" fill="#222" />
      <path d="M72,78 L128,78 L134,160 L66,160 Z" fill="#3b8de0" />
    </g>
  ),
  makas: (
    <g {...ST}>
      <circle cx={60} cy={140} r={24} fill="none" strokeWidth={10} />
      <circle cx={140} cy={140} r={24} fill="none" strokeWidth={10} />
      <path d="M74,120 L150,24 M126,120 L50,24" strokeWidth={12} stroke="#c9ccd6" />
      <path d="M74,120 L150,24 M126,120 L50,24" strokeWidth={3} />
    </g>
  ),
  fren: (
    <g {...ST}>
      <circle cx={100} cy={96} r={68} fill="#9aa3b5" />
      <circle cx={100} cy={96} r={22} fill="#5b6475" />
      {Array.from({ length: 6 }).map((_, i) => (
        <circle key={i} cx={100 + 44 * Math.cos((i * Math.PI) / 3)} cy={96 + 44 * Math.sin((i * Math.PI) / 3)} r={7} fill="#5b6475" />
      ))}
      <path d="M150,40 Q186,96 150,152 L132,140 Q158,96 132,52 Z" fill="#e05a4f" />
    </g>
  ),
  fotokopi: (
    <g {...ST}>
      <rect x={24} y={60} width={152} height={90} rx={10} fill="#c9ccd6" />
      <rect x={40} y={40} width={120} height={26} rx={4} fill="#9aa3b5" />
      <rect x={60} y={150} width={80} height={14} fill="#5b6475" />
      <circle cx={150} cy={86} r={8} fill="#2fae6a" />
    </g>
  ),
};
export const Ikon: React.FC<{ ad: string; x: number; y: number; s?: number; an?: number; etiket?: string; son?: number }> = ({ ad, x, y, s = 1, an = -1, etiket, son }) => {
  const t = useT();
  if (t < an - 0.03 || (son !== undefined && t > son + 0.2)) return null;
  const p = interpolate(t, [an, an + 0.25], [0, 1], { ...CL, easing: EPOP });
  return (
    <div style={{ position: "absolute", left: x - 140 * s, top: y - 140 * s, width: 280 * s, scale: String(0.4 + 0.6 * p), opacity: Math.min(1, p * 2) }}>
      <svg width={280 * s} height={266 * s} viewBox="0 0 200 190">
        {IKON[ad]}
      </svg>
      {etiket ? <div style={{ textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 38 * Math.max(1, s * 0.7), color: RENK.murekkep, WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill", marginTop: 4 }}>{etiket}</div> : null}
    </div>
  );
};

// Terazi: sol kefe (giderler) / sağ kefe (gelir); an'da sol (gider) tarafına yatar (sönümlü salınım)
export const Terazi: React.FC<{ an: number; x: number; y: number; sol: string; sag: string }> = ({ an, x, y, sol, sag }) => {
  const t = useT();
  const d = Math.max(0, t - an);
  const aci = t < an ? 0 : 13 * (1 - Math.cos(Math.min(d, 2) * 7) * Math.exp(-d * 3.2));
  const rad = (aci * Math.PI) / 180;
  const L = 430, by = y + 150;
  const kefe = (taraf: -1 | 1, etiket: string, renkler: string[]) => {
    const ux = x + taraf * L * Math.cos(rad), uy = by - taraf * L * Math.sin(rad);
    return (
      <div style={{ position: "absolute", left: ux - 190, top: uy }}>
        <svg width={380} height={200} style={{ position: "absolute", left: 0, top: 0, overflow: "visible" }}>
          <path d="M190,0 L40,150 M190,0 L340,150" stroke="#111" strokeWidth={5} />
          <path d="M20,150 Q190,230 360,150 Z" fill="#c9a24a" stroke="#111" strokeWidth={6} />
        </svg>
        {renkler.map((r, i) => (
          <div key={i} style={{ position: "absolute", left: 60 + (i % 3) * 88, top: 104 - Math.floor(i / 3) * 42, width: 84, height: 44, background: r || "#c8955a", border: "4px solid #111", borderRadius: 5 }} />
        ))}
        <div style={{ position: "absolute", left: -60, width: 500, top: 210, textAlign: "center", fontFamily: anton, fontSize: 70, color: RENK.murekkep, WebkitTextStroke: "8px #0b0b0b", paintOrder: "stroke fill" }}>{etiket}</div>
      </div>
    );
  };
  return (
    <>
      <div style={{ position: "absolute", left: x - 16, top: by, width: 32, height: 430, background: "#8a6a2a", border: "5px solid #111" }} />
      <div style={{ position: "absolute", left: x - 140, top: by + 420, width: 280, height: 38, background: "#8a6a2a", border: "5px solid #111", borderRadius: 8 }} />
      <div style={{ position: "absolute", left: x - L - 10, top: by - 13, width: 2 * L + 20, height: 26, background: "#c9a24a", border: "5px solid #111", borderRadius: 8, rotate: `${-aci}deg` }} />
      <div style={{ position: "absolute", left: x - 26, top: by - 26, width: 52, height: 52, borderRadius: 26, background: "#c9a24a", border: "5px solid #111" }} />
      {kefe(-1, sol, [ZARF_RENK.ss, ZARF_RENK.medicare, ZARF_RENK.saglik, ZARF_RENK.savunma, ZARF_RENK.faiz, ""])}
      {kefe(1, sag, [""])}
    </>
  );
};

// Konveyör: kredi şeritleri soldan sağa; uçta "CHEAP 1%" etiketi düşer, yerine "NEW 5%" gelir (S14)
export const Konveyor: React.FC<{ an: number; x: number; y: number; w: number; degisim: number }> = ({ an, x, y, w, degisim }) => {
  const t = useT();
  const hiz = 150;
  const seritler = Array.from({ length: 8 });
  return (
    <div style={{ position: "absolute", left: x, top: y, width: w, height: 300 }}>
      <div style={{ position: "absolute", left: 0, top: 200, width: w, height: 40, background: "#3a4152", border: "5px solid #111", borderRadius: 20 }} />
      {Array.from({ length: Math.ceil(w / 70) }).map((_, i) => (
        <div key={i} style={{ position: "absolute", left: ((i * 70 + (t - an) * hiz) % w + w) % w, top: 212, width: 16, height: 16, borderRadius: 8, background: "#7b8496" }} />
      ))}
      {seritler.map((_, i) => {
        const uz = 120 + random(`ks${i}`) * 260;
        const px = ((i * (w / 8) + (t - an) * hiz) % (w + 300)) - 300;
        const yeni = t >= degisim && px > w * 0.62;
        return (
          <div key={i} style={{ position: "absolute", left: px, top: 116, width: uz + 60, height: 80, background: "#f3ecdc", border: "5px solid #111", borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: anton, fontSize: 44, color: yeni ? ZARF_RENK.faiz : "#2f7a4f" }}>
            {yeni ? "NEW 5%" : "CHEAP 1%"}
          </div>
        );
      })}
    </div>
  );
};

// Gösterge (ibre): oran yükselir — rakamsız mekanizma (S15)
export const Gosterge: React.FC<{ an: number; x: number; y: number; etiket: string }> = ({ an, x, y, etiket }) => {
  const t = useT();
  const a = interpolate(t, [an, an + 3.5], [-70, 40], { ...CL, easing: EIO }) + Math.sin(t * 9) * 1.2;
  return (
    <div style={{ position: "absolute", left: x - 300, top: y - 300 }}>
      <svg width={600} height={360} viewBox="0 0 600 360">
        <path d="M60,320 A240,240 0 0 1 540,320" fill="none" stroke="#3a4152" strokeWidth={56} />
        <path d="M60,320 A240,240 0 0 1 300,80" fill="none" stroke={RENK.yesil} strokeWidth={56} opacity={0.8} />
        <path d="M300,80 A240,240 0 0 1 540,320" fill="none" stroke={ZARF_RENK.faiz} strokeWidth={56} opacity={0.8} />
        <g transform={`rotate(${a} 300 320)`}>
          <path d="M292,320 L300,110 L308,320 Z" fill="#f4f1ea" stroke="#111" strokeWidth={5} />
        </g>
        <circle cx={300} cy={320} r={24} fill="#f4f1ea" stroke="#111" strokeWidth={6} />
      </svg>
      <div style={{ textAlign: "center", fontFamily: anton, fontSize: 64, color: RENK.murekkep, WebkitTextStroke: "8px #0b0b0b", paintOrder: "stroke fill" }}>{etiket}</div>
    </div>
  );
};

// Sarmal: INTEREST → BORROWING döngüsü dönen oklar (S20)
export const Sarmal: React.FC<{ an: number; x: number; y: number }> = ({ an, x, y }) => {
  const t = useT();
  const d = Math.max(0, t - an) * 70;
  return (
    <div style={{ position: "absolute", left: x - 260, top: y - 260, width: 520, height: 520 }}>
      <svg width={520} height={520} style={{ rotate: `${d}deg` }}>
        <path d="M260,40 A220,220 0 0 1 480,260" fill="none" stroke={ZARF_RENK.faiz} strokeWidth={34} strokeLinecap="round" />
        <path d="M480,260 l-30,-46 l58,6 Z" fill={ZARF_RENK.faiz} transform="rotate(10 480 260)" />
        <path d="M260,480 A220,220 0 0 1 40,260" fill="none" stroke={ZARF_RENK.borc} strokeWidth={34} strokeLinecap="round" />
        <path d="M40,260 l30,46 l-58,-6 Z" fill={ZARF_RENK.borc} transform="rotate(10 40 260)" />
      </svg>
      <div style={{ position: "absolute", top: 150, width: 520, textAlign: "center", fontFamily: anton, fontSize: 58, color: ZARF_RENK.faiz, WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill" }}>INTEREST</div>
      <div style={{ position: "absolute", top: 300, width: 520, textAlign: "center", fontFamily: anton, fontSize: 58, color: "#c9b0f2", WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill" }}>BORROWING</div>
    </div>
  );
};

// Yarış pisti: iki koşucu (maaş zarfı / borç defteri), ilerleme oranları (S22)
export const Yaris: React.FC<{ an: number; maas: [number, number]; borc: [number, number]; sure?: number }> = ({ an, maas, borc, sure = 3 }) => {
  const t = useT();
  const p = interpolate(t, [an, an + sure], [0, 1], { ...CL, easing: EOUT });
  const koşu = (y: number, [a, b]: [number, number], icerik: React.ReactNode, etiket: string) => {
    const x = 220 + (a + (b - a) * p) * 1300;
    return (
      <>
        <div style={{ position: "absolute", left: 160, top: y + 70, width: 1600, height: 8, background: "rgba(255,255,255,0.25)" }} />
        <div style={{ position: "absolute", left: x - 110, top: y - 40 + Math.abs(Math.sin(t * 10)) * -10, width: 220, height: 130 }}>{icerik}</div>
        <div style={{ position: "absolute", left: x - 150, width: 300, top: y + 90, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.murekkep }}>{etiket}</div>
      </>
    );
  };
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 1720, top: 250, width: 16, height: 420, background: "repeating-linear-gradient(#fff 0 20px, #111 20px 40px)" }} />
      {koşu(300, maas, <div style={{ width: 300, height: 170, background: "#c8955a", border: "6px solid #111", borderRadius: 8, fontFamily: anton, fontSize: 58, display: "flex", alignItems: "center", justifyContent: "center" }}>PAYCHECK</div>, "THE ECONOMY")}
      {koşu(560, borc, <div style={{ width: 300, height: 170, background: "#5b3b9a", border: "6px solid #111", borderRadius: 10, fontFamily: anton, fontSize: 54, color: "#f4ecff", display: "flex", alignItems: "center", justifyContent: "center" }}>LOAN BOOK</div>, "THE DEBT")}
    </AbsoluteFill>
  );
};

export const Tik: React.FC<{ an: number; x: number; y: number; s?: number; renk?: string }> = ({ an, x, y, s = 1, renk = "#2fae6a" }) => {
  const t = useT();
  if (t < an) return null;
  const p = interpolate(t, [an, an + 0.25], [0, 1], CL);
  return (
    <svg style={{ position: "absolute", left: x - 50 * s, top: y - 50 * s, overflow: "visible" }} width={100 * s} height={100 * s} viewBox="0 0 100 100">
      <path d="M12,52 L40,80 L90,16" fill="none" stroke="#0b0b0b" strokeWidth={22} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray="1" strokeDashoffset={1 - p} />
      <path d="M12,52 L40,80 L90,16" fill="none" stroke={renk} strokeWidth={12} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray="1" strokeDashoffset={1 - p} />
    </svg>
  );
};

export type { SunucuPoz };
