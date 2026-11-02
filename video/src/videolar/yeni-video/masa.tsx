import React from "react";
import { AbsoluteFill, Easing, Img, interpolate, random } from "remotion";
import { anton, fredoka } from "./ortak";
import { NESNE } from "./rig";
import { CL, EOUT, EPOP, f, Kamera, KameraKare, Leo, PozAdim, RENK, useT } from "./kit";

// S08 "Kitchen Table Budget" yapı taşları (animasyon-yonetmeni). Zamanlar sahne yerel saniyesi.
// Sabit set (metin H4): gece soğuk mavi mutfak, sıcak masa lambası. Zarf renkleri bütün videoda sabit (metin §2).
export const ZARF_RENK = {
  ss: "#3b8de0", // Social Security mavi
  medicare: "#2fae6a", // Medicare yeşil
  saglik: "#a8d672", // diğer sağlık açık yeşil (yeşille yan yana → her zaman doğrudan etiketli)
  savunma: "#8a93a6", // savunma gri
  faiz: "#e05a4f", // faiz kırmızı (logosuz düz kâğıt)
  borc: "#9b6bdf", // BORROWED / borç defteri mor
  diger: "", // her şey: kraft (boyasız)
} as const;
export type ZarfRenk = keyof typeof ZARF_RENK;

// G01 mutfak geometrisi (05-gorsel/rapor.md): masa üst kenarı y=810; lamba x780–1140 y30–245; buzdolabı notları sağ üstte
export const MASA_Y = 810;

// Kesme listesi: [başlangıç sn, öğe] — t'ye göre son başlamış öğe görünür (sert kesme = hızlı kurgu)
export const Kurgu: React.FC<{ kesmeler: [number, React.ReactNode][] }> = ({ kesmeler }) => {
  const t = useT();
  let i = 0;
  for (let k = 0; k < kesmeler.length; k++) if (t >= kesmeler[k][0]) i = k;
  return <>{kesmeler[i][1]}</>;
};

// Nesne (G03/G07 kesikleri): merkez (x, y), genişlik w; giriş: düşme (yukarıdan, sekme) veya pop
export const Nesne: React.FC<{
  ad: string;
  x: number;
  y: number;
  w: number;
  an?: number;
  giris?: "dus" | "pop" | "kay" | "yok";
  donme?: number;
  son?: number;
  renk?: string; // CSS color blend ile boya (kraft zarf → renkli)
  style?: React.CSSProperties;
  children?: React.ReactNode; // nesne üstü yazı (nesne kutusu koordinatı, 0..w)
}> = ({ ad, x, y, w, an = -1, giris = "pop", donme = 0, son, renk, style, children }) => {
  const t = useT();
  if (t < an - 0.02 || (son !== undefined && t > son + 0.2)) return null;
  const [nw, nh] = NESNE[ad];
  const h = (w * nh) / nw;
  const p = interpolate(t, [an, an + (giris === "dus" ? 0.42 : 0.24)], [0, 1], { ...CL, easing: giris === "dus" ? Easing.bounce : EPOP });
  const q = son !== undefined ? interpolate(t, [son, son + 0.2], [1, 0], CL) : 1;
  const dy = giris === "dus" ? -(1 - p) * 520 : 0;
  const dx = giris === "kay" ? (1 - p) * 700 : 0;
  const s = giris === "pop" ? 0.5 + 0.5 * p : 1;
  const op = (giris === "pop" ? Math.min(1, p * 2) : giris === "yok" ? 1 : Math.min(1, p * 4)) * q;
  const src = f(`${ad}.png`);
  return (
    <div style={{ position: "absolute", left: x - w / 2 + dx, top: y - h / 2 + dy, width: w, height: h, rotate: `${donme}deg`, scale: String(s), opacity: op, ...style }}>
      <Img src={src} style={{ position: "absolute", width: w, height: h, filter: "drop-shadow(0 10px 10px rgba(0,0,0,0.45))" }} />
      {renk ? (
        <div style={{ position: "absolute", width: w, height: h, background: renk, mixBlendMode: "color", WebkitMaskImage: `url(${src})`, WebkitMaskSize: "100% 100%", maskImage: `url(${src})`, maskSize: "100% 100%" }} />
      ) : null}
      {renk ? (
        <div style={{ position: "absolute", width: w, height: h, background: renk, mixBlendMode: "multiply", opacity: 0.35, WebkitMaskImage: `url(${src})`, WebkitMaskSize: "100% 100%", maskImage: `url(${src})`, maskSize: "100% 100%" }} />
      ) : null}
      {children}
    </div>
  );
};

// Zarf: kapalı/açık, renk + etiket (KOD yazı; plakada yazı yok)
export const Zarf: React.FC<{
  x: number;
  y: number;
  w: number;
  renk: ZarfRenk;
  etiket?: React.ReactNode;
  alt?: string;
  acik?: boolean;
  an?: number;
  giris?: "dus" | "pop" | "kay" | "yok";
  donme?: number;
  son?: number;
  yaziBoy?: number;
}> = ({ x, y, w, renk, etiket, alt, acik, an, giris, donme, son, yaziBoy }) => {
  const ad = acik ? "G03-zarf-acik" : "G03-zarf-kapali";
  const [nw, nh] = NESNE[ad];
  const h = (w * nh) / nw;
  const yb = yaziBoy ?? w * 0.14;
  // Kapalı zarfta yazı alanı kapak üçgeninin altında (alt %45); açık zarfta gövdenin ortası
  const yaziY = acik ? h * 0.62 : h * 0.6;
  return (
    <Nesne ad={ad} x={x} y={y} w={w} an={an} giris={giris} donme={donme} son={son} renk={ZARF_RENK[renk] || undefined}>
      {etiket ? (
        <div style={{ position: "absolute", left: 0, width: w, top: yaziY - yb * 0.6, textAlign: "center", fontFamily: anton, fontSize: yb, letterSpacing: 1, color: "#fbf7ee", WebkitTextStroke: `${Math.max(3, yb * 0.12)}px #141414`, paintOrder: "stroke fill", lineHeight: 1 }}>
          {etiket}
          {alt ? <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: yb * 0.62, marginTop: yb * 0.12 }}>{alt}</div> : null}
        </div>
      ) : null}
    </Nesne>
  );
};

// Masa sahnesi (G01): Leo masanın ARKASINDA (y<810 maskeli), masa önü nesneleri Leo'nun önünde
export const MasaSahne: React.FC<{
  kamera: KameraKare[];
  leo?: { id?: string; x?: number; s?: number; dy?: number; pozlar: PozAdim[]; tohum?: number; giris?: { an: number; dx?: number; dy?: number; sure?: number }; wink?: [number, number] } | null;
  arka?: React.ReactNode; // plaka üstü, Leo arkası (buzdolabı notları vb.)
  on?: React.ReactNode; // Leo önü (masadaki nesneler)
  isik?: number; // lamba ışığı yoğunluğu (S26 lambayı kısar)
}> = ({ kamera, leo, arka, on, isik = 1 }) => {
  const s = leo?.s ?? 0.58;
  // yüz y: Leo kesiği alt kenarı masa altında kalır (gövde masada kesilir)
  const yuzY = MASA_Y + 90 - (1057 - 307) * s + (leo?.dy ?? 0);
  return (
    <Kamera kareler={kamera}>
      <Img src={f("G01.jpg")} style={{ position: "absolute", width: 1920, height: 1080, filter: isik < 1 ? `brightness(${0.55 + 0.45 * isik})` : undefined }} />
      {arka}
      {leo ? (
        <div style={{ position: "absolute", left: 0, top: 0, width: 1920, height: MASA_Y + 6, overflow: "hidden" }}>
          <Leo id={leo.id} x={leo.x ?? 960} y={yuzY} s={s} pozlar={leo.pozlar} tohum={leo.tohum} giris={leo.giris} wink={leo.wink} />
        </div>
      ) : null}
      {/* masa kenarı gölgesi: Leo'nun gövdesi masaya oturur */}
      <div style={{ position: "absolute", left: 0, top: MASA_Y - 4, width: 1920, height: 26, background: "linear-gradient(rgba(0,0,0,0.28), rgba(0,0,0,0))" }} />
      {on}
    </Kamera>
  );
};

// Yapışkan not yazısı (G10 buzdolabı not kutuları, 05-gorsel/rapor.md)
export const G10_NOT: [number, number, number, number][] = [
  [823, 203, 201, 204],
  [1333, 210, 196, 197],
  [1079, 337, 193, 194],
  [938, 583, 197, 199],
  [1261, 583, 189, 193],
];
export const NotYazi: React.FC<{ kutu: [number, number, number, number]; an: number; children: React.ReactNode; renk?: string; boyut?: number; zemin?: string; donme?: number }> = ({
  kutu,
  an,
  children,
  renk = "#1d1d1d",
  boyut = 34,
  zemin,
  donme = 0,
}) => {
  const t = useT();
  if (t < an - 0.02) return null;
  const p = interpolate(t, [an, an + 0.22], [0, 1], { ...CL, easing: EPOP });
  const [x, y, w, h] = kutu;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        width: w,
        height: h,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        padding: 12,
        boxSizing: "border-box",
        background: zemin,
        borderRadius: 4,
        fontFamily: fredoka,
        fontWeight: 700,
        fontSize: boyut,
        lineHeight: 1.05,
        color: renk,
        opacity: Math.min(1, p * 1.5),
        scale: String(0.7 + 0.3 * p),
        rotate: `${donme + (1 - p) * -8}deg`,
      }}
    >
      {children}
    </div>
  );
};

// Buzdolabı yakın plan (G10)
export const Dolap: React.FC<{ kamera: KameraKare[]; children?: React.ReactNode }> = ({ kamera, children }) => (
  <Kamera kareler={kamera}>
    <Img src={f("G10.jpg")} style={{ position: "absolute", width: 1920, height: 1080 }} />
    {children}
  </Kamera>
);

// Kuşbakışı masa (G06): nesneler y 320–1000, x 560–1400
export const UstMasa: React.FC<{ kamera: KameraKare[]; children?: React.ReactNode }> = ({ kamera, children }) => (
  <Kamera kareler={kamera}>
    <Img src={f("G06.jpg")} style={{ position: "absolute", width: 1920, height: 1080 }} />
    {children}
  </Kamera>
);

// Grafik zemini: mutfak plakası bulanık + koyu (sahne bağlamı korunur, grafik okunur)
export const GrafikZemin: React.FC<{ plaka?: string; children?: React.ReactNode; kamera?: KameraKare[] }> = ({ plaka = "G01", children, kamera }) => {
  const t = useT();
  const s = 1.06 + t * 0.004;
  return (
    <AbsoluteFill>
      <Img src={f(`${plaka}.jpg`)} style={{ position: "absolute", width: 1920, height: 1080, filter: "blur(16px) brightness(0.38) saturate(0.8)", scale: String(s) }} />
      {kamera ? <Kamera kareler={kamera}>{children}</Kamera> : <AbsoluteFill style={{ scale: String(1 + 0.0035 * t), translate: `0px ${Math.sin(t * 0.9) * 2}px` }}>{children}</AbsoluteFill>}
    </AbsoluteFill>
  );
};

// D1: her bütçe grafiğinin altında sabit iki satır
export const OlcekSatiri: React.FC<{ x?: number; y?: number; w?: number; an?: number; kaynak?: string }> = ({ x = 960, y = 760, w = 1500, an = 0, kaynak = "FY2026 (Oct 2025–Sep 2026), Monthly Treasury Statement" }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.3], [0, 1], CL);
  return (
    <div style={{ position: "absolute", left: x - w / 2, top: y, width: w, textAlign: "center", opacity: p, fontFamily: fredoka, fontWeight: 700, color: RENK.ikincil, fontSize: 25, lineHeight: 1.3 }}>
      <span style={{ color: RENK.sari }}>$1 a month here = $1 billion a year</span>
      <br />
      {kaynak}
    </div>
  );
};

// Para/oran sayacı biçimleyici
export const para = (v: number) => "$" + Math.round(v).toLocaleString("en-US");

// Basit yatay çubuk (sıralı karşılaştırma; yalnız vurgu renkli, diğerleri nötr — dataviz)
export type YatayCubuk = { etiket: string; deger: number; renk?: string; vurgu?: boolean };
export const YatayCubuklar: React.FC<{ an: number; veri: YatayCubuk[]; w: number; satir?: number; maks: number; arasi?: number; degerYaz?: (v: number) => string }> = ({
  an,
  veri,
  w,
  satir = 78,
  maks,
  arasi = 0.12,
  degerYaz = para,
}) => {
  const t = useT();
  const etW = 330;
  return (
    <div style={{ position: "relative", width: w, height: veri.length * satir }}>
      {veri.map((c, i) => {
        const p = interpolate(t, [an + i * arasi, an + i * arasi + 0.5], [0, 1], { ...CL, easing: EOUT });
        const bw = ((w - etW - 150) * c.deger) / maks;
        return (
          <div key={i} style={{ position: "absolute", top: i * satir, left: 0, height: satir - 16, width: w, opacity: Math.min(1, p * 3) }}>
            <div style={{ position: "absolute", left: 0, width: etW - 20, textAlign: "right", top: 8, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: c.vurgu ? RENK.murekkep : RENK.ikincil }}>{c.etiket}</div>
            <div style={{ position: "absolute", left: etW, top: 4, height: satir - 24, width: bw * p, borderRadius: 6, background: c.renk ?? (c.vurgu ? ZARF_RENK.faiz : "#4b5875") }} />
            <div style={{ position: "absolute", left: etW + bw * p + 14, top: 6, fontFamily: anton, fontSize: 36, color: c.vurgu ? RENK.murekkep : RENK.ikincil }}>{p > 0.6 ? degerYaz(c.deger) : ""}</div>
          </div>
        );
      })}
    </div>
  );
};

// Kâğıt yaprakları (borç defteri sayfaları akar; gag)
export const Yapraklar: React.FC<{ an: number; adet?: number; x: number; y: number; renk?: string }> = ({ an, adet = 26, x, y, renk = "#f3ecdc" }) => {
  const t = useT();
  if (t < an) return null;
  return (
    <>
      {Array.from({ length: adet }).map((_, i) => {
        const d = t - an - i * 0.07;
        if (d < 0) return null;
        const yy = y + d * (380 + random(`yv${i}`) * 260) + d * d * 120;
        const xx = x + (random(`yx${i}`) - 0.5) * 120 + Math.sin(d * 3 + i) * 50;
        if (yy > 1180) return null;
        return <div key={i} style={{ position: "absolute", left: xx, top: yy, width: 110, height: 140, background: renk, border: "3px solid #2a2a2a", borderRadius: 4, rotate: `${(random(`yr${i}`) - 0.5) * 80 + d * 90}deg`, boxShadow: "0 6px 10px rgba(0,0,0,0.35)" }} />;
      })}
    </>
  );
};

// Borç defteri (LOAN BOOK, kalın mor cilt; kredi kartı DEĞİL — R31): kapalı/açık
export const Defter: React.FC<{ x: number; y: number; w?: number; an?: number; acik?: number; satir?: string; donme?: number; giris?: "kay" | "pop" }> = ({ x, y, w = 360, an = -1, acik = 0, satir, donme = -4, giris = "kay" }) => {
  const t = useT();
  if (t < an) return null;
  const p = interpolate(t, [an, an + 0.35], [0, 1], { ...CL, easing: EOUT });
  const h = w * 0.72;
  const dx = giris === "kay" ? (1 - p) * -600 : 0;
  const s = giris === "pop" ? 0.6 + 0.4 * p : 1;
  return (
    <div style={{ position: "absolute", left: x - w / 2 + dx, top: y - h / 2, width: w, height: h, rotate: `${donme}deg`, scale: String(s), opacity: Math.min(1, p * 3) }}>
      {acik > 0 ? (
        <div style={{ position: "absolute", left: -w * 0.5 * acik, top: 0, width: w * (1 + 0.5 * acik), height: h, background: "#f3ecdc", border: "5px solid #1b1b1b", borderRadius: 10, overflow: "hidden" }}>
          {Array.from({ length: 7 }).map((_, i) => (
            <div key={i} style={{ position: "absolute", left: 24, right: 24, top: 30 + i * (h / 8), height: 3, background: "rgba(80,80,120,0.35)" }} />
          ))}
          {satir ? <div style={{ position: "absolute", right: 30, bottom: 22, fontFamily: anton, fontSize: w * 0.13, color: ZARF_RENK.faiz }}>{satir}</div> : null}
        </div>
      ) : (
        <div style={{ position: "absolute", inset: 0, background: "#5b3b9a", border: "6px solid #1b1b1b", borderRadius: 14, boxShadow: "0 16px 30px rgba(0,0,0,0.5), inset -14px 0 0 #43297a" }}>
          <div style={{ position: "absolute", left: 0, right: 0, top: h * 0.32, textAlign: "center", fontFamily: anton, fontSize: w * 0.13, letterSpacing: 3, color: "#f4ecff" }}>LOAN BOOK</div>
        </div>
      )}
    </div>
  );
};

// Capitol silüeti (düz, yüzsüz, bayraksız) — S01 açılış küçülmesi
export const Capitol: React.FC<{ renk?: string }> = ({ renk = "#e8eef8" }) => (
  <svg width={1000} height={560} viewBox="0 0 1000 560" style={{ overflow: "visible" }}>
    <g fill={renk} stroke="#141a2a" strokeWidth={8} strokeLinejoin="round">
      <rect x={60} y={380} width={880} height={150} rx={6} />
      <rect x={110} y={330} width={260} height={60} />
      <rect x={630} y={330} width={260} height={60} />
      <rect x={390} y={300} width={220} height={90} />
      <path d="M400,300 Q500,120 600,300 Z" />
      <rect x={470} y={120} width={60} height={70} />
      <path d="M460,125 Q500,60 540,125 Z" />
      <rect x={494} y={30} width={12} height={40} />
    </g>
    <g fill="#141a2a" opacity={0.55}>
      {Array.from({ length: 16 }).map((_, i) => (
        <rect key={i} x={90 + i * 52} y={410} width={18} height={100} rx={3} />
      ))}
    </g>
  </svg>
);

// Ev maketi (S01: Capitol → masadaki ev)
export const EvMaketi: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <svg style={{ position: "absolute", left: x - 110 * s, top: y - 150 * s, overflow: "visible" }} width={220 * s} height={180 * s} viewBox="0 0 220 180">
    <g stroke="#1b1b1b" strokeWidth={6} strokeLinejoin="round">
      <rect x={30} y={78} width={160} height={96} fill="#f1e7d2" />
      <path d="M14,86 L110,14 L206,86 Z" fill="#c4553f" />
      <rect x={92} y={116} width={36} height={58} fill="#7a4b2a" />
      <rect x={46} y={104} width={32} height={30} fill="#ffd27a" />
      <rect x={142} y={104} width={32} height={30} fill="#ffd27a" />
    </g>
  </svg>
);

export const Sicak = { lamba: "rgba(255,196,110,0.18)" };

// Leo kırpım koordinatı (cx, cy) → G01 plaka koordinatı (MasaSahne yerleşimiyle aynı formül)
export const leoPx = (cx: number, cy: number, o: { x?: number; s?: number; dy?: number } = {}) => {
  const s = o.s ?? 0.58;
  const yuzY = MASA_Y + 90 - (1057 - 307) * s + (o.dy ?? 0);
  return { x: (o.x ?? 960) - 740 * s + cx * s, y: yuzY - 307 * s + cy * s };
};
