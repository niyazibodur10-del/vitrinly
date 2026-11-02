import React from "react";
import { AbsoluteFill, Easing, Img, interpolate, random, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { anton, fredoka } from "./ortak";
import { KLASOR, SUNUCU_T, YAMA_T } from "./rig";
import { SahneVeri, SAHNELER } from "./veri-sahne";
import { Rig, Sunucu, SunucuPoz, yuzRig } from "./Sunucu";

// Kaynak: video/src/k1929/kit.tsx (1929'a özgü harita/kapı/kilit çıkarıldı; zarf, nesne, not, masa Leo eklendi).
// Tam video yapı taşları (animasyon-yonetmeni). Tüm zamanlar sahne YEREL saniyesidir (Sequence başı = 0).
export const RIG_T: Rig = { klasor: KLASOR, kutu: SUNUCU_T, yama: YAMA_T };
export const YUZ_T = yuzRig(RIG_T);
export const f = (ad: string) => staticFile(`${KLASOR}/${ad}`);
export const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
export const EIO = Easing.inOut(Easing.cubic);
export const EOUT = Easing.out(Easing.cubic);
export const EPOP = Easing.out(Easing.back(1.7));

// Grafik paleti (dataviz validator: dark, yüzey #0f1626 → tüm kontroller geçti; CVD taban bandı → her seri doğrudan etiketli)
export const RENK = { mavi: "#3b8de0", yesil: "#2fae6a", kahve: "#d9772e", sari: "#ffd43b", yuzey: "#0f1626", murekkep: "#f4f1ea", ikincil: "#a9b3c7", gri: "#6b7487", kirmizi: "#e05a4f" };
// Altyazı/ekran yazısı kapı renkleri (illüstrasyondaki kapılarla aynı his)
export const KAPI_RENK = { mavi: "#4da3ff", yesil: "#5fd35f", kahve: "#e0884a" } as const;

export const useT = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return frame / fps;
};

export const sahne = (id: string): SahneVeri => SAHNELER.find((s) => s.id === id)!;
const norm = (w: string) => w.toLowerCase().replace(/[^a-z0-9$'-]/g, "");
// Kelime anı: n'inci geçiş (1'den), sahne yerel saniyesi
export const anlar = (id: string) => {
  const s = sahne(id);
  return (w: string, n = 1, son = false): number => {
    const hedef = norm(w);
    let say = 0;
    for (const k of s.kelimeler) {
      if (norm(k.w) === hedef && ++say === n) return son ? k.e : k.s;
    }
    throw new Error(`${id}: kelime yok: ${w} #${n}`);
  };
};

// ---------- Kamera ----------
export type KameraKare = [t: number, fx: number, fy: number, s: number];
export const kameraDurum = (t: number, kareler: KameraKare[]) => {
  if (t <= kareler[0][0]) return kareler[0];
  for (let i = 0; i < kareler.length - 1; i++) {
    const [t0, x0, y0, s0] = kareler[i];
    const [t1, x1, y1, s1] = kareler[i + 1];
    if (t < t1) {
      const p = EIO((t - t0) / (t1 - t0));
      return [t, x0 + (x1 - x0) * p, y0 + (y1 - y0) * p, s0 + (s1 - s0) * p] as KameraKare;
    }
  }
  return kareler[kareler.length - 1];
};
export const Kamera: React.FC<{ kareler: KameraKare[]; children: React.ReactNode; w?: number; h?: number; ekranW?: number; ekranH?: number; style?: React.CSSProperties }> = ({
  kareler,
  children,
  w = 1920,
  h = 1080,
  ekranW = 1920,
  ekranH = 1080,
  style,
}) => {
  const t = useT();
  const [, fx0, fy0, s0] = kameraDurum(t, kareler);
  // Sürekli çok hafif itme (%0,35/sn): son anahtar kareden sonra da kare donmaz (freezedetect −60 dB kapısı)
  const s = s0 * (1 + 0.0035 * Math.max(0, t - kareler[kareler.length - 1][0]));
  // Kenar koruması: plaka ekranı tamamen kaplamıyorsa odak kaydırılır (siyah kenar görünmez)
  const kis = (v: number, yarim: number, boy: number) => (boy * s >= yarim * 2 ? Math.min(Math.max(v, yarim / s), boy - yarim / s) : boy / 2);
  const fx = kis(fx0, ekranW / 2, w);
  const fy = kis(fy0, ekranH / 2, h);
  return (
    <div style={{ position: "absolute", width: w, height: h, transformOrigin: "0 0", translate: `${ekranW / 2 - fx * s}px ${ekranH / 2 - fy * s}px`, scale: String(s), ...style }}>
      {children}
    </div>
  );
};

// ---------- Plakalar ----------
export const Plaka: React.FC<{ ad: string; filtre?: string; w?: number; h?: number }> = ({ ad, filtre, w = 1920, h = 1080 }) => (
  <Img src={f(`${ad}.jpg`)} style={{ position: "absolute", width: w, height: h, filter: filtre }} />
);

// ---------- Leo ----------
export type PozAdim = [t: number, poz: SunucuPoz];
// Konuşan / duran bel üstü Leo: yüz merkezi (x, y) ekran koordinatı, ölçek s. Poz geçişinde 5 karelik oturma.
export const Leo: React.FC<{
  id?: string; // konuşuyorsa sahne kimliği (ağız çizelgesi); yoksa dış ses / sessiz
  x: number;
  y: number;
  s: number;
  pozlar: PozAdim[];
  tohum?: number;
  wink?: [number, number];
  rozet?: { etiket: string; renk: string };
  giris?: { an: number; dx?: number; dy?: number; sure?: number };
  cikis?: { an: number; dx?: number; dy?: number; sure?: number };
  konusmaz?: boolean;
  opak?: number;
}> = ({ id, x, y, s, pozlar, tohum = 1, wink, rozet, giris, cikis, konusmaz, opak = 1 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  let i = 0;
  for (let k = 0; k < pozlar.length; k++) if (t >= pozlar[k][0]) i = k;
  const poz = pozlar[i][1];
  const degisim = Math.round(pozlar[i][0] * fps);
  const otur = i > 0 ? interpolate(frame - degisim, [0, 2, 5], [0.965, 1.012, 1], CL) : 1;
  let dx = 0, dy = 0, op = opak;
  if (giris) {
    const p = interpolate(t, [giris.an, giris.an + (giris.sure ?? 0.35)], [0, 1], { ...CL, easing: EOUT });
    dx += (giris.dx ?? 0) * (1 - p); dy += (giris.dy ?? 0) * (1 - p);
    if (!giris.dx && !giris.dy) op *= p;
  }
  if (cikis) {
    const p = interpolate(t, [cikis.an, cikis.an + (cikis.sure ?? 0.35)], [0, 1], { ...CL, easing: Easing.in(Easing.cubic) });
    dx += (cikis.dx ?? 0) * p; dy += (cikis.dy ?? 0) * p;
    if (!cikis.dx && !cikis.dy) op *= 1 - p;
  }
  const veri = id ? sahne(id) : null;
  return (
    <div style={{ position: "absolute", left: x - YUZ_T.x * s + dx, top: y - YUZ_T.y * s + dy, scale: String(s), transformOrigin: "0 0", opacity: op }}>
      <div style={{ position: "relative", scale: String(otur), transformOrigin: `${YUZ_T.x}px ${RIG_T.kutu.h}px` }}>
        <Sunucu cues={veri ? veri.agiz : []} ofs={0} poz={poz} tohum={tohum} wink={wink} rig={RIG_T} konusmaz={konusmaz || !veri} />
        {rozet ? <Rozet {...rozet} x={YUZ_T.x + 125} y={YUZ_T.y + 330} boyut={1.7} /> : null}
      </div>
    </div>
  );
};

export const Rozet: React.FC<{ etiket: string; renk: string; x: number; y: number; boyut?: number }> = ({ etiket, renk, x, y, boyut = 1 }) => (
  <div
    style={{
      position: "absolute",
      left: x - 36 * boyut,
      top: y - 13 * boyut,
      width: 72 * boyut,
      height: 26 * boyut,
      borderRadius: 6 * boyut,
      background: renk,
      border: `${2.5 * boyut}px solid #101010`,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontFamily: fredoka,
      fontWeight: 700,
      fontSize: 16 * boyut,
      color: "#101010",
      boxShadow: "0 2px 0 rgba(0,0,0,0.35)",
    }}
  >
    {etiket}
  </div>
);

// ---------- Yazılar ----------
export const Yazi: React.FC<{
  an: number;
  son?: number;
  x: number;
  y: number;
  children: React.ReactNode;
  boyut?: number;
  renk?: string;
  font?: "anton" | "fredoka";
  hiza?: "sol" | "orta" | "sag";
  kontur?: number;
  genislik?: number;
  donme?: number;
  salla?: boolean;
}> = ({ an, son, x, y, children, boyut = 90, renk = RENK.murekkep, font = "anton", hiza = "orta", kontur, genislik, donme = 0, salla }) => {
  const t = useT();
  const p = interpolate(t, [an - 0.04, an + 0.16], [0, 1], { ...CL, easing: EPOP });
  const q = son !== undefined ? interpolate(t, [son, son + 0.2], [1, 0], CL) : 1;
  if (t < an - 0.05 || (son !== undefined && t > son + 0.25)) return null;
  const tx = hiza === "orta" ? "-50%" : hiza === "sag" ? "-100%" : "0%";
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        translate: `${tx} 0%`,
        width: genislik,
        textAlign: hiza === "orta" ? "center" : hiza === "sag" ? "right" : "left",
        fontFamily: font === "anton" ? anton : fredoka,
        fontWeight: font === "anton" ? 400 : 700,
        fontSize: boyut,
        lineHeight: 1.08,
        letterSpacing: font === "anton" ? 2 : 0,
        color: renk,
        WebkitTextStroke: `${kontur ?? Math.max(6, boyut * 0.11)}px #0b0b0b`,
        paintOrder: "stroke fill",
        opacity: p * q,
        scale: String(0.6 + 0.4 * p),
        rotate: `${donme + (salla ? Math.sin(t * 7) * 2.2 : 0)}deg`,
        whiteSpace: genislik ? "normal" : "nowrap",
      }}
    >
      {children}
    </div>
  );
};

// Panel kart (koyu yüzey, ince çerçeve): grafik ve bilgi kartları için
export const Kart: React.FC<{ an: number; son?: number; x: number; y: number; w: number; h: number; children?: React.ReactNode; cerceve?: string; arka?: string; donme?: number }> = ({
  an,
  son,
  x,
  y,
  w,
  h,
  children,
  cerceve = "rgba(255,255,255,0.18)",
  arka = "rgba(15,22,38,0.92)",
  donme = 0,
}) => {
  const t = useT();
  const p = interpolate(t, [an - 0.04, an + 0.22], [0, 1], { ...CL, easing: EPOP });
  const q = son !== undefined ? interpolate(t, [son, son + 0.22], [1, 0], CL) : 1;
  if (t < an - 0.05 || (son !== undefined && t > son + 0.25)) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        width: w,
        height: h,
        background: arka,
        border: `3px solid ${cerceve}`,
        borderRadius: 22,
        boxShadow: "0 18px 50px rgba(0,0,0,0.45)",
        opacity: p * q,
        scale: String(0.85 + 0.15 * p),
        rotate: `${donme}deg`,
        overflow: "hidden",
      }}
    >
      {children}
    </div>
  );
};

export const Kaynak: React.FC<{ metin: string; an?: number; son?: number }> = ({ metin, an = 0, son }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.3], [0, 1], CL) * (son !== undefined ? interpolate(t, [son, son + 0.3], [1, 0], CL) : 1);
  return (
    <div style={{ position: "absolute", right: 34, bottom: 30, fontFamily: fredoka, fontWeight: 700, fontSize: 22, color: "rgba(255,255,255,0.78)", background: "rgba(0,0,0,0.42)", padding: "5px 12px", borderRadius: 8, opacity: p }}>
      {metin}
    </div>
  );
};

export const Illustration: React.FC<{ an?: number; son?: number }> = ({ an = 0, son }) => {
  const t = useT();
  if (t < an || (son !== undefined && t > son)) return null;
  return (
    <div style={{ position: "absolute", left: 34, bottom: 30, padding: "5px 13px", borderRadius: 8, background: "rgba(0,0,0,0.45)", color: "rgba(255,255,255,0.85)", fontFamily: fredoka, fontWeight: 700, fontSize: 23 }}>
      Illustration
    </div>
  );
};

// Sayaç: an → an+sure arasında bas → bit (yuvarlanmış), biçim: önEk + binlik ayraç
export const Sayac: React.FC<{ an: number; sure?: number; bas: number; bit: number; onEk?: string; sonEk?: string; ondalik?: number }> = ({ an, sure = 0.8, bas, bit, onEk = "", sonEk = "", ondalik = 0 }) => {
  const t = useT();
  const v = interpolate(t, [an, an + sure], [bas, bit], { ...CL, easing: EOUT });
  return (
    <>
      {onEk}
      {v.toLocaleString("en-US", { minimumFractionDigits: ondalik, maximumFractionDigits: ondalik })}
      {sonEk}
    </>
  );
};

// Damga (GAMBLE vb.): büyükten küçüğe çakılır
export const Damga: React.FC<{ an: number; x: number; y: number; metin: string; renk?: string; donme?: number; boyut?: number }> = ({ an, x, y, metin, renk = RENK.kirmizi, donme = -12, boyut = 120 }) => {
  const t = useT();
  if (t < an) return null;
  const p = interpolate(t, [an, an + 0.12], [0, 1], { ...CL, easing: Easing.in(Easing.quad) });
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        translate: "-50% -50%",
        rotate: `${donme}deg`,
        scale: String(2.2 - 1.2 * p),
        opacity: p,
        border: `10px solid ${renk}`,
        borderRadius: 18,
        padding: "4px 30px",
        fontFamily: anton,
        fontSize: boyut,
        letterSpacing: 6,
        color: renk,
        background: "rgba(10,10,10,0.25)",
      }}
    >
      {metin}
    </div>
  );
};

// ---------- Grafikler (SVG; tek eksen; doğrudan etiket; ince işaretler) ----------
export type Cubuk = { etiket: string; deger: number; vurgu?: boolean; renk?: string; ustYazi?: string };
export const CubukGrafik: React.FC<{
  an: number;
  veri: Cubuk[];
  w: number;
  h: number;
  maks: number;
  renk: string;
  arasi?: number; // çubuklar arası gecikme (sn)
  degerYaz?: (c: Cubuk) => string;
  soluk?: number; // vurgusuzların opaklığı
  vurguAn?: number;
}> = ({ an, veri, w, h, maks, renk, arasi = 0.06, degerYaz, soluk = 0.45, vurguAn }) => {
  const t = useT();
  const pad = { l: 20, r: 20, t: 46, b: 52 };
  const iw = w - pad.l - pad.r, ih = h - pad.t - pad.b;
  const bw = iw / veri.length;
  const vurguP = vurguAn !== undefined ? interpolate(t, [vurguAn, vurguAn + 0.3], [0, 1], CL) : 0;
  return (
    <svg width={w} height={h}>
      <line x1={pad.l} x2={w - pad.r} y1={pad.t + ih} y2={pad.t + ih} stroke="rgba(255,255,255,0.35)" strokeWidth={2} />
      {veri.map((c, i) => {
        const p = interpolate(t, [an + i * arasi, an + i * arasi + 0.45], [0, 1], { ...CL, easing: EOUT });
        const bh = (c.deger / maks) * ih * p;
        const x = pad.l + i * bw + bw * 0.14;
        const op = c.vurgu ? 1 : 1 - (1 - soluk) * vurguP;
        return (
          <g key={i} opacity={op}>
            <rect x={x} y={pad.t + ih - bh} width={bw * 0.72} height={Math.max(0, bh)} rx={4} fill={c.renk ?? renk} />
            <text x={x + bw * 0.36} y={pad.t + ih + 36} textAnchor="middle" fill={RENK.ikincil} style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 24 }}>
              {c.etiket}
            </text>
            {(degerYaz || c.ustYazi) && p > 0.95 ? (
              <text x={x + bw * 0.36} y={pad.t + ih - bh - 12} textAnchor="middle" fill={RENK.murekkep} style={{ fontFamily: fredoka, fontWeight: 700, fontSize: c.vurgu ? 28 : 22 }}>
                {c.ustYazi ?? degerYaz!(c)}
              </text>
            ) : null}
          </g>
        );
      })}
    </svg>
  );
};

export type Nokta = { x: number; y: number; etiket?: string; etiketYon?: "ust" | "alt" | "sag" | "sol"; an?: number };
// Çizgi grafik: noktalar veri koordinatında; xAralik/yAralik ile ölçeklenir; an→an+sure çizilir
export const CizgiGrafik: React.FC<{
  an: number;
  sure: number;
  noktalar: Nokta[];
  w: number;
  h: number;
  xAralik: [number, number];
  yAralik: [number, number];
  renk: string;
  kalin?: number;
  eksenX?: { x: number; etiket: string }[];
  yatayCizgi?: { y: number; etiket: string; renk?: string }[];
  alan?: boolean;
  kesikli?: boolean;
}> = ({ an, sure, noktalar, w, h, xAralik, yAralik, renk, kalin = 5, eksenX = [], yatayCizgi = [], alan, kesikli }) => {
  const t = useT();
  const pad = { l: 30, r: 30, t: 40, b: 56 };
  const iw = w - pad.l - pad.r, ih = h - pad.t - pad.b;
  const X = (v: number) => pad.l + ((v - xAralik[0]) / (xAralik[1] - xAralik[0])) * iw;
  const Y = (v: number) => pad.t + ih - ((v - yAralik[0]) / (yAralik[1] - yAralik[0])) * ih;
  const p = interpolate(t, [an, an + sure], [0, 1], { ...CL, easing: Easing.inOut(Easing.quad) });
  // ilerleme x ekseninde: çizilen kısım xAralik içinde p oranı
  const xSon = noktalar[0].x + (noktalar[noktalar.length - 1].x - noktalar[0].x) * p;
  const gor: Nokta[] = [];
  for (let i = 0; i < noktalar.length; i++) {
    const n = noktalar[i];
    if (n.x <= xSon) gor.push(n);
    else {
      const o = noktalar[i - 1];
      if (o) gor.push({ x: xSon, y: o.y + ((n.y - o.y) * (xSon - o.x)) / (n.x - o.x) });
      break;
    }
  }
  const d = gor.map((n, i) => `${i ? "L" : "M"}${X(n.x).toFixed(1)},${Y(n.y).toFixed(1)}`).join(" ");
  return (
    <svg width={w} height={h} style={{ overflow: "visible" }}>
      <line x1={pad.l} x2={w - pad.r} y1={pad.t + ih} y2={pad.t + ih} stroke="rgba(255,255,255,0.35)" strokeWidth={2} />
      {eksenX.map((e, i) => (
        <text key={i} x={X(e.x)} y={pad.t + ih + 38} textAnchor="middle" fill={RENK.ikincil} style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 24 }}>
          {e.etiket}
        </text>
      ))}
      {yatayCizgi.map((c, i) => (
        <g key={i}>
          <line x1={pad.l} x2={w - pad.r} y1={Y(c.y)} y2={Y(c.y)} stroke={c.renk ?? "rgba(255,255,255,0.4)"} strokeWidth={2} strokeDasharray="8 8" />
          <text x={pad.l + 8} y={Y(c.y) - 10} textAnchor="start" fill={RENK.ikincil} style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 22 }}>
            {c.etiket}
          </text>
        </g>
      ))}
      {alan && gor.length > 1 ? <path d={`${d} L${X(gor[gor.length - 1].x)},${pad.t + ih} L${X(gor[0].x)},${pad.t + ih} Z`} fill={renk} opacity={0.14} /> : null}
      <path d={d} fill="none" stroke={renk} strokeWidth={kalin} strokeLinejoin="round" strokeLinecap="round" strokeDasharray={kesikli ? "10 9" : undefined} />
      {noktalar.map((n, i) =>
        n.etiket && n.x <= xSon + 1e-9 && t >= (n.an ?? -1) ? (
          <g key={i}>
            <circle cx={X(n.x)} cy={Y(n.y)} r={8} fill={renk} stroke={RENK.yuzey} strokeWidth={3} />
            <text
              x={X(n.x) + (n.etiketYon === "sag" ? 16 : n.etiketYon === "sol" ? -16 : 0)}
              y={Y(n.y) + (n.etiketYon === "alt" ? 40 : n.etiketYon === "sag" || n.etiketYon === "sol" ? 9 : -18)}
              textAnchor={n.etiketYon === "sag" ? "start" : n.etiketYon === "sol" ? "end" : "middle"}
              fill={RENK.murekkep}
              style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 28 }}
            >
              {n.etiket}
            </text>
          </g>
        ) : null,
      )}
    </svg>
  );
};

// Kâğıt şerit (ticker tape) yağmuru
export const SeritYagmuru: React.FC<{ an: number; adet?: number; w?: number; h?: number; renk?: string }> = ({ an, adet = 70, w = 1920, h = 1080, renk = "#efe6cf" }) => {
  const t = useT();
  if (t < an) return null;
  return (
    <svg width={w} height={h} style={{ position: "absolute", left: 0, top: 0 }}>
      {Array.from({ length: adet }).map((_, i) => {
        const hiz = 180 + random(`sh${i}`) * 220;
        const x0 = random(`sx${i}`) * w;
        const y = ((t - an) * hiz + random(`sy${i}`) * h * 1.2) % (h * 1.2) - h * 0.1;
        const x = x0 + Math.sin((t - an) * 2 + i) * 40;
        const r = ((t - an) * 120 * (random(`sr${i}`) - 0.5) + i * 37) % 360;
        return <rect key={i} x={x} y={y} width={10} height={64 + random(`sl${i}`) * 50} rx={3} fill={renk} opacity={0.85} transform={`rotate(${r} ${x} ${y})`} />;
      })}
    </svg>
  );
};

// Banknot destesi (S12, S14, S20): adet ve ölçek animasyonlu
export const Banknot: React.FC<{ x: number; y: number; adet?: number; s?: number; parilti?: number; donme?: number }> = ({ x, y, adet = 6, s = 1, parilti = 0, donme = 0 }) => (
  <svg style={{ position: "absolute", left: x - 130 * s, top: y - 90 * s, overflow: "visible", rotate: `${donme}deg` }} width={260 * s} height={180 * s}>
    <g transform={`scale(${s})`}>
      {Array.from({ length: adet }).map((_, i) => (
        <g key={i} transform={`translate(${10 + i * 2}, ${110 - i * 9})`}>
          <rect width={220} height={60} rx={6} fill="#9cc58f" stroke="#2c4a26" strokeWidth={4} />
          <rect x={14} y={10} width={192} height={40} rx={4} fill="none" stroke="#2c4a26" strokeWidth={2} opacity={0.6} />
          <circle cx={110} cy={30} r={16} fill="#cfe5c6" stroke="#2c4a26" strokeWidth={3} />
          <text x={110} y={38} textAnchor="middle" style={{ fontFamily: anton, fontSize: 22 }} fill="#2c4a26">
            $
          </text>
        </g>
      ))}
      {parilti > 0 ? <ellipse cx={120} cy={90} rx={150} ry={100} fill="url(#parilti)" opacity={parilti} /> : null}
      <defs>
        <radialGradient id="parilti">
          <stop offset="0" stopColor="#fff6c8" stopOpacity={0.9} />
          <stop offset="1" stopColor="#fff6c8" stopOpacity={0} />
        </radialGradient>
      </defs>
    </g>
  </svg>
);

// Takvim yaprağı (dev): metinler arasında çevrilir
export const Takvim: React.FC<{ x: number; y: number; w?: number; adimlar: [number, string][]; altYazi?: string }> = ({ x, y, w = 300, adimlar, altYazi }) => {
  const t = useT();
  let i = 0;
  for (let k = 0; k < adimlar.length; k++) if (t >= adimlar[k][0]) i = k;
  const p = interpolate(t, [adimlar[i][0], adimlar[i][0] + 0.18], [0, 1], CL);
  return (
    <div style={{ position: "absolute", left: x, top: y, width: w, height: w * 1.05, background: "#f6f0e2", borderRadius: 16, border: "5px solid #1b1b1b", boxShadow: "0 14px 40px rgba(0,0,0,0.5)", overflow: "hidden" }}>
      <div style={{ height: w * 0.24, background: RENK.kirmizi, borderBottom: "5px solid #1b1b1b" }} />
      <div style={{ position: "absolute", top: w * 0.28, width: "100%", textAlign: "center", fontFamily: anton, fontSize: w * 0.36, color: "#1b1b1b", scale: `1 ${0.2 + 0.8 * p}`, transformOrigin: "50% 0%" }}>
        {adimlar[i][1]}
      </div>
      {altYazi ? <div style={{ position: "absolute", bottom: w * 0.08, width: "100%", textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: w * 0.09, color: "#555" }}>{altYazi}</div> : null}
    </div>
  );
};

// Sahne kök kutusu: arka plan rengi + gren/vinyet + altyazı sahne katmanında değil (tam kompozisyonda ortak)
export const SahneKok: React.FC<{ children: React.ReactNode; arka?: string }> = ({ children, arka = "#05070f" }) => (
  <AbsoluteFill style={{ background: arka, overflow: "hidden" }}>{children}</AbsoluteFill>
);

export const Karartma: React.FC<{ an: number; sure?: number; ters?: boolean; renk?: string; maks?: number }> = ({ an, sure = 0.4, ters, renk = "#000", maks = 1 }) => {
  const t = useT();
  const p = interpolate(t, [an, an + sure], ters ? [maks, 0] : [0, maks], CL);
  return <AbsoluteFill style={{ background: renk, opacity: p, pointerEvents: "none" }} />;
};

// Flaş geçiş (whoosh kesmesi)
export const Flas: React.FC<{ an: number }> = ({ an }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.13], [0.85, 0], CL);
  if (t < an || t > an + 0.15) return null;
  return <AbsoluteFill style={{ background: "#fff", opacity: p }} />;
};
