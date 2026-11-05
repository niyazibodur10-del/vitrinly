import React from "react";
import { AbsoluteFill, Img, interpolate, random, useVideoConfig } from "remotion";
import { CL, EIO, EOUT, EPOP, f, RENK, useT } from "./kit";
import { anton, fredoka } from "./ortak";
import { DURAK, G, KAYNAK } from "./veri-grafik";

// Kodla çizilen grafik ve nesneler (animasyon-yonetmeni, 2026-11-04 iskelet). Zamanlar sahne YEREL saniyesi.
// Kurallar (hafıza): tek eksen, doğrudan etiket, renkler #3b8de0/#2fae6a/#d9772e, yüzey #0f1626; zemin %0,35/sn sürekli itme;
// her grafik çekimi kesme anında (t0) çerçeve + başlıkla girer (≤1 sn boş an yok), değerler kelime çapasında dolar.
// Rakamlar yalnız veri-grafik.ts (G, R-kodlu; grafik-veri.py rakam-tablosu assert'i) — burada sayı literal'i yok.

export const KUTU_RENK = { ev: "#c4553a", emeklilik: "#2b4c8c", banka: "#2f9e62" } as const;
export type KutuTur = keyof typeof KUTU_RENK;
const KUTU_AD: Record<KutuTur, string> = { ev: "HOUSE", emeklilik: "RETIREMENT", banka: "BANK" };
// Okafor 10 kutusu [ÖRNEK]: 4 ev, 4 emeklilik, 2 banka. Kayıp sırası (kutu-hesap.py + 05-gorsel/sahne-listesi.md): LIVING −2 (lacivert 4,5) → CARE −1 (yeşil 8) → GIVING −1 (yeşil 9) → kalan 4 kiremit + 2 lacivert
export const OKAFOR: KutuTur[] = ["ev", "ev", "ev", "ev", "emeklilik", "emeklilik", "emeklilik", "emeklilik", "banka", "banka"];
export const KAYIP: { i: number; etiket: string }[] = [
  { i: 4, etiket: "SPENT ON LIVING" },
  { i: 5, etiket: "SPENT ON LIVING" },
  { i: 8, etiket: "CARE" },
  { i: 9, etiket: "GIVEN" },
];
export const ka = (k: Record<string, number>, ad: string, yedek: number) => (k[ad] !== undefined ? k[ad] : yedek);
export const useDikey = () => {
  const { width, height } = useVideoConfig();
  return height > width;
};
const yaz = (boyut: number, renk: string = RENK.murekkep, font: "anton" | "fredoka" = "anton"): React.CSSProperties => ({
  fontFamily: font === "anton" ? anton : fredoka,
  fontWeight: font === "anton" ? 400 : 700,
  fontSize: boyut,
  color: renk,
  lineHeight: 1.08,
  letterSpacing: font === "anton" ? 1.5 : 0,
  WebkitTextStroke: `${Math.max(4, Math.round(boyut * 0.09))}px #0b0b0b`,
  paintOrder: "stroke fill",
});
const gir = (t: number, an: number, d = 0.22) => interpolate(t, [an - 0.03, an + d], [0, 1], { ...CL, easing: EPOP });

// ---------- Zemin: soğuk koyu yüzey + sürekli itme (donma önleme) ----------
export const Zemin: React.FC<{ t0: number; children: React.ReactNode; renk?: string }> = ({ t0, children, renk = RENK.yuzey }) => {
  const t = useT();
  const s = 1 + 0.0035 * Math.max(0, t - t0) + 0.012 * interpolate(t, [t0, t0 + 0.5], [0, 1], { ...CL, easing: EOUT });
  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 38%, #1b2742 0%, ${renk} 62%, #070a12 100%)`, overflow: "hidden" }}>
      <AbsoluteFill style={{ scale: String(s) }}>{children}</AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------- Canva plakası: kaplama + yavaş itme/kayma (donma önleme); 9:16'da orta şerit ----------
export const PlakaArka: React.FC<{ t0: number; ad: string; odakX?: number; bulanik?: number; s0?: number; kay?: number }> = ({ t0, ad, odakX = 0.5, bulanik = 0, s0 = 1.04, kay = 5 }) => {
  const t = useT();
  const D = useDikey();
  const s = s0 + 0.0035 * Math.max(0, t - t0);
  const W = D ? 1920 * (1920 / 1080) : 1920, H = D ? 1920 : 1080;
  const sol = D ? 540 - W * odakX : 0;
  return (
    <AbsoluteFill style={{ overflow: "hidden", background: "#0c1424" }}>
      <Img src={f(`${ad}.jpg`)} style={{ position: "absolute", left: sol - (t - t0) * kay, top: 0, width: W + 60, height: H, objectFit: "cover", scale: String(s), filter: bulanik ? `blur(${bulanik}px) brightness(0.85)` : undefined }} />
    </AbsoluteFill>
  );
};
export const Kesik: React.FC<{ ad: string; x: number; alt: number; w: number; donme?: number; opak?: number; kirp?: string }> = ({ ad, x, alt, w, donme = 0, opak = 1, kirp }) => (
  <Img src={f(`${ad}.png`)} style={{ position: "absolute", left: x - w / 2, bottom: alt, width: w, rotate: `${donme}deg`, transformOrigin: "50% 100%", opacity: opak, clipPath: kirp }} />
);

// ---------- Yer tutucu plaka (Canva sahne illüstrasyonu gelene kadar) ----------
export const YerTutucu: React.FC<{ t0: number; ad: string; plaka?: string }> = ({ t0, ad, plaka }) => {
  const D = useDikey();
  const kasa = /kasa|kutuIci|varis/.test(plaka ?? "") || /kamyonun içi|kasa/.test(ad);
  return (
    <AbsoluteFill>
      <PlakaArka t0={t0} ad={kasa ? "M09" : "M08"} bulanik={2} />
      <div style={{ position: "absolute", left: 40, top: 36, right: 40, padding: "8px 16px", border: "3px dashed rgba(255,255,255,0.35)", borderRadius: 12, ...yaz(D ? 28 : 24, "rgba(255,255,255,0.85)", "fredoka"), WebkitTextStroke: "0px", background: "rgba(0,0,0,0.3)" }}>
        YER TUTUCU{plaka ? ` · ${plaka}` : ""} — {ad}
      </div>
    </AbsoluteFill>
  );
};

// ---------- Kaynak satırı (R-kodlu; ekranda insan okunur metin) ----------
export const KaynakSatiri: React.FC<{ kayit: [number, string][]; son: number }> = ({ kayit, son }) => {
  const t = useT();
  const D = useDikey();
  let aktif: [number, string] | null = null;
  for (const k of kayit) if (t >= k[0]) aktif = k;
  if (!aktif || t > son) return null;
  const p = interpolate(t, [aktif[0], aktif[0] + 0.3], [0, 1], CL);
  const metin = KAYNAK[aktif[1]];
  if (!metin) throw new Error(`KAYNAK yok: ${aktif[1]}`);
  return (
    <div style={{ position: "absolute", left: D ? 70 : 34, top: D ? 1560 : 1030, fontFamily: fredoka, fontWeight: 700, fontSize: D ? 26 : 22, color: "rgba(255,255,255,0.8)", background: "rgba(0,0,0,0.45)", padding: "5px 12px", borderRadius: 8, opacity: p, maxWidth: D ? 940 : 1100 }}>
      {aktif[1] === "ORNEK" ? "EXAMPLE FAMILY · ILLUSTRATION" : `Source: ${metin}`}
    </div>
  );
};

// Okafor karelerinde zorunlu köşe etiketi (P2)
export const OrnekEtiket: React.FC = () => {
  const D = useDikey();
  return (
    <div style={{ position: "absolute", left: D ? 70 : 34, top: D ? 200 : 110, padding: "6px 14px", borderRadius: 8, background: "rgba(0,0,0,0.5)", border: "2px solid rgba(255,255,255,0.4)", fontFamily: fredoka, fontWeight: 700, fontSize: D ? 28 : 24, color: "#fff" }}>
      EXAMPLE FAMILY · ILLUSTRATION
    </div>
  );
};

// ---------- Kutu (karton, renk = servet türü, "TO: THE KIDS") ----------
export const Kutu: React.FC<{ tur: KutuTur; x: number; y: number; w?: number; capraz?: number; etiket?: string; parla?: number; donme?: number; opak?: number; s?: number }> = ({ tur, x, y, w = 150, capraz, etiket, parla = 0, donme = 0, opak = 1, s = 1 }) => {
  const t = useT();
  const h = w * 0.78;
  const c = capraz !== undefined ? interpolate(t, [capraz, capraz + 0.25], [0, 1], { ...CL, easing: EOUT }) : 0;
  const renk = KUTU_RENK[tur];
  return (
    <div style={{ position: "absolute", left: x - w / 2, top: y - h, width: w, height: h, rotate: `${donme}deg`, opacity: opak * (1 - 0.45 * c), scale: String(s), transformOrigin: "50% 100%" }}>
      <div style={{ position: "absolute", inset: 0, background: renk, border: "5px solid #111", borderRadius: 8, boxShadow: parla ? `0 0 ${40 * parla}px rgba(255,200,90,${0.8 * parla})` : "0 8px 0 rgba(0,0,0,0.35)" }} />
      <div style={{ position: "absolute", left: w * 0.42, top: 0, width: w * 0.16, height: h, background: "rgba(240,220,170,0.55)", borderLeft: "2px solid rgba(0,0,0,0.25)", borderRight: "2px solid rgba(0,0,0,0.25)" }} />
      <div style={{ position: "absolute", left: 6, right: 6, top: h * 0.2, textAlign: "center", ...yaz(w * 0.13, "#fff", "fredoka"), WebkitTextStroke: `${Math.max(3, w * 0.02)}px #111` }}>{KUTU_AD[tur]}</div>
      <div style={{ position: "absolute", left: 6, right: 6, top: h * 0.56, textAlign: "center", ...yaz(w * 0.1, "#fff3d6", "fredoka"), WebkitTextStroke: `${Math.max(2, w * 0.016)}px #111` }}>TO: THE KIDS</div>
      {c > 0 ? (
        <>
          <svg width={w} height={h} style={{ position: "absolute", left: 0, top: 0 }}>
            <line x1={w * 0.08} y1={h * 0.12} x2={w * 0.08 + w * 0.84 * c} y2={h * 0.12 + h * 0.76 * c} stroke="#111" strokeWidth={w * 0.07} strokeLinecap="round" />
            <line x1={w * 0.08} y1={h * 0.12} x2={w * 0.08 + w * 0.84 * c} y2={h * 0.12 + h * 0.76 * c} stroke={RENK.kirmizi} strokeWidth={w * 0.04} strokeLinecap="round" />
          </svg>
          {etiket ? (
            <div style={{ position: "absolute", left: "50%", top: -w * 0.16, translate: "-50% 0", whiteSpace: "nowrap", padding: "2px 10px", background: "#f4f1ea", border: "3px solid #111", borderRadius: 6, rotate: "-6deg", ...yaz(w * 0.11, "#111", "fredoka"), WebkitTextStroke: "0px", scale: String(c) }}>{etiket}</div>
          ) : null}
        </>
      ) : null}
    </div>
  );
};

// Kutu dizisi: kayipOnce = önceki sahnelerde kaybolan kutu sayısı (KAYIP sırası); yeni kayıp(lar) capraz anında çizilir.
// gizle: kayıplar gösterilmez (kamyonda kalanlar). giris: kutuların sırayla yerine oturma anları (yükleme).
export const KutuDizisi: React.FC<{ t0: number; kayipOnce?: number; yeni?: { n: number; an: number }; gizle?: boolean; giris?: number[]; yalniz?: number; cx?: number; cy?: number; w?: number }> = ({
  t0,
  kayipOnce = 0,
  yeni,
  gizle,
  giris,
  yalniz,
  cx,
  cy,
  w,
}) => {
  const t = useT();
  const D = useDikey();
  const kw = w ?? (D ? 170 : 150);
  const kolonTam = D ? 4 : 5;
  const X = cx ?? (D ? 540 : 960);
  const Y = cy ?? (D ? 900 : 640);
  const kayipSet = new Map<number, { etiket: string; an: number }>();
  KAYIP.slice(0, kayipOnce).forEach((k) => kayipSet.set(k.i, { etiket: k.etiket, an: -10 }));
  if (yeni) KAYIP.slice(kayipOnce, kayipOnce + yeni.n).forEach((k, j) => kayipSet.set(k.i, { etiket: k.etiket, an: yeni.an + j * 0.35 }));
  const liste = OKAFOR.map((tur, i) => ({ tur, i })).filter((b) => !(gizle && kayipSet.has(b.i)));
  const kolon = liste.length <= 6 ? 3 : kolonTam;
  return (
    <>
      {liste.map((b, j) => {
        const sira = j % kolon, satir = Math.floor(j / kolon);
        const satirN = Math.min(kolon, liste.length - satir * kolon);
        const x = X + (sira - (satirN - 1) / 2) * (kw * 1.12);
        const y = Y + satir * kw * 0.92 - (Math.ceil(liste.length / kolon) - 1) * kw * 0.46;
        const g = giris ? giris[Math.min(giris.length - 1, j < 4 ? 0 : j < 8 ? 1 : 2)] + (j % 4) * 0.12 : t0;
        const p = interpolate(t, [g - 0.02, g + 0.25], [0, 1], { ...CL, easing: EPOP });
        const ky = kayipSet.get(b.i);
        const nefes = Math.sin((t + j) * 2.1) * 1.5; // idle: kutular hafif soluk alır
        return (
          <React.Fragment key={b.i}>
          {giris && p < 1 ? <div style={{ position: "absolute", left: x - kw / 2, top: y - kw * 0.78, width: kw, height: kw * 0.78, border: "4px dashed rgba(255,255,255,0.35)", borderRadius: 8 }} /> : null}
          <Kutu
            tur={b.tur}
            x={x}
            y={y - (1 - p) * 80 + nefes}
            w={kw}
            opak={p * (yalniz !== undefined && b.i !== yalniz ? 0.25 : 1)}
            capraz={ky?.an}
            etiket={ky?.etiket}
            parla={yalniz === b.i ? 0.6 + 0.4 * Math.sin(t * 3) : 0}
          />
          </React.Fragment>
        );
      })}
    </>
  );
};

// ---------- Pano (sızıntı çizelgesi / envanter listesi) ----------
export type PanoSatir = { deger?: string; an?: number; renk?: string; cizgi?: number; tik?: number };
export const Pano: React.FC<{ t0: number; satir: PanoSatir[]; alt?: { metin: string; an: number; renk?: string }; kumSaati?: number; isimAn?: number[] }> = ({ t0, satir, alt, kumSaati, isimAn }) => {
  const t = useT();
  const D = useDikey();
  const W = D ? 860 : 820, H = D ? 1040 : 860;
  const X = D ? 110 : 550, Y = D ? 330 : 170;
  const p = gir(t, t0, 0.3);
  return (
    <div style={{ position: "absolute", left: X, top: Y, width: W, height: H, opacity: p, transformOrigin: "50% 0%", scale: String((D ? 1 : 0.88) * (0.9 + 0.1 * p)), rotate: `${-1.5 + Math.sin(t * 0.8) * 0.4}deg` }}>
      <div style={{ position: "absolute", inset: 0, background: "#8a5a2f", border: "6px solid #111", borderRadius: 26 }} />
      <div style={{ position: "absolute", left: 34, right: 34, top: 70, bottom: 30, background: "#f4f1ea", border: "4px solid #111", borderRadius: 10 }} />
      <div style={{ position: "absolute", left: W / 2 - 110, top: 18, width: 220, height: 70, background: "#b9bec8", border: "5px solid #111", borderRadius: 14 }} />
      <div style={{ position: "absolute", left: 70, top: 108, ...yaz(46, "#111"), WebkitTextStroke: "0px" }}>OKAFOR MOVE · 10 BOXES</div>
      {DURAK.map(([ad], i) => {
        const s = satir[i] ?? {};
        const y = 196 + i * (D ? 118 : 96);
        const ip = isimAn ? interpolate(t, [isimAn[i], isimAn[i] + 0.2], [0, 1], CL) : 1;
        const dp = s.an !== undefined ? gir(t, s.an) : 0;
        const cz = s.cizgi !== undefined ? interpolate(t, [s.cizgi, s.cizgi + 0.3], [0, 1], { ...CL, easing: EOUT }) : 0;
        const tk = s.tik !== undefined ? gir(t, s.tik) : 0;
        return (
          <div key={ad} style={{ position: "absolute", left: 70, top: y, width: W - 140, height: 80, opacity: ip }}>
            <div style={{ position: "absolute", left: 0, top: 6, ...yaz(D ? 50 : 44, "#1a1a1a", "fredoka"), WebkitTextStroke: "0px" }}>
              {i + 1}. {ad}
            </div>
            {s.deger ? <div style={{ position: "absolute", right: 60, top: 0, ...yaz(D ? 58 : 52, s.renk ?? RENK.kirmizi), opacity: dp, scale: String(0.6 + 0.4 * dp) }}>{s.deger}</div> : null}
            {tk > 0 ? <div style={{ position: "absolute", right: 0, top: 2, ...yaz(50, RENK.yesil, "fredoka"), scale: String(tk) }}>✓</div> : null}
            <div style={{ position: "absolute", left: 0, top: 66, height: 7, width: `${cz * 62}%`, background: RENK.sari, borderRadius: 4, border: "2px solid #111" }} />
          </div>
        );
      })}
      {alt ? (
        <div style={{ position: "absolute", left: 70, right: 70, bottom: 56, textAlign: "center", ...yaz(D ? 56 : 50, alt.renk ?? "#111"), WebkitTextStroke: alt.renk ? "5px #111" : "0px", opacity: gir(t, alt.an) }}>{alt.metin}</div>
      ) : null}
      {kumSaati !== undefined ? <KumSaati an={kumSaati} x={W - 40} y={H - 120} /> : null}
    </div>
  );
};

export const KumSaati: React.FC<{ an: number; x: number; y: number }> = ({ an, x, y }) => {
  const t = useT();
  const p = gir(t, an);
  const don = interpolate(t, [an + 0.2, an + 0.8], [0, 180], { ...CL, easing: EIO });
  return (
    <div style={{ position: "absolute", left: x - 70, top: y - 90, width: 140, height: 180, opacity: p, scale: String(p), rotate: `${don}deg` }}>
      <svg width={140} height={180}>
        <path d="M20 10 H120 L75 90 L120 170 H20 L65 90 Z" fill={RENK.sari} stroke="#111" strokeWidth={8} strokeLinejoin="round" />
      </svg>
      <div style={{ position: "absolute", left: 150, top: 50, whiteSpace: "nowrap", rotate: `${-don}deg`, ...yaz(44, RENK.sari) }}>+YEARS</div>
    </div>
  );
};

// ---------- Durak tabelası (yeşil yol levhası) ----------
export const Tabela: React.FC<{ metin: string; x: number; y: number; an: number; s?: number; renk?: string; kesik?: boolean; kalp?: boolean }> = ({ metin, x, y, an, s = 1, renk = "#1f7a4a", kesik, kalp }) => {
  const t = useT();
  const p = gir(t, an, 0.3);
  const salla = Math.sin(t * 1.7 + x) * 0.8;
  return (
    <div style={{ position: "absolute", left: x, top: y, translate: "-50% -100%", scale: String(s * (0.7 + 0.3 * p)), opacity: p, transformOrigin: "50% 100%", rotate: `${salla}deg` }}>
      <div style={{ padding: "18px 44px", background: renk, border: kesik ? "6px dashed #f4f1ea" : "6px solid #f4f1ea", outline: "5px solid #111", borderRadius: 18, whiteSpace: "nowrap", ...yaz(78, "#f4f1ea"), WebkitTextStroke: "0px" }}>
        {kalp ? "♥ " : ""}
        {metin}
      </div>
      <div style={{ margin: "0 auto", width: 22, height: 220, background: "#9aa3b2", border: "4px solid #111", borderTop: "none" }} />
    </div>
  );
};

// Sarı durak tabelası (eş = durak, kayıp değil; R04/R05)
export const EsTabela: React.FC<{ t0: number; varyant: "s01" | "s13"; ikinci?: number }> = ({ t0, varyant, ikinci }) => {
  const t = useT();
  const D = useDikey();
  const p = gir(t, t0 + 0.05, 0.3);
  const sinyal = Math.floor((t - t0) * 2.4) % 2 === 0 ? 1 : 0.35;
  const ust = varyant === "s01" ? `$${G.es}T → SPOUSE FIRST` : `~$${G.es}T STOPS HERE FIRST`;
  const alt = varyant === "s01" ? "a stop, not a loss" : `~$${G.dul}T OF IT TO WIDOWED WOMEN`;
  const q = varyant === "s13" && ikinci !== undefined ? gir(t, ikinci) : 1;
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 540 : 960, top: D ? 760 : 470, translate: "-50% -50%", opacity: p, scale: String(0.8 + 0.2 * p) }}>
        <div style={{ width: D ? 920 : 1180, padding: "40px 30px", background: "#f2c230", border: "8px solid #111", borderRadius: 24, textAlign: "center", rotate: "-2deg" }}>
          <div style={{ ...yaz(D ? 92 : 110, "#111"), WebkitTextStroke: "0px" }}>{ust}</div>
          <div style={{ marginTop: 14, ...yaz(D ? 50 : 56, "#3a2a00", "fredoka"), WebkitTextStroke: "0px", opacity: q }}>{alt}</div>
        </div>
        <div style={{ margin: "0 auto", width: 30, height: D ? 500 : 300, background: "#9aa3b2", border: "5px solid #111" }} />
      </div>
      <div style={{ position: "absolute", left: D ? 860 : 1640, top: D ? 1180 : 760, width: 70, height: 70, borderRadius: 35, background: `rgba(255,170,40,${sinyal})`, border: "6px solid #111", boxShadow: `0 0 ${50 * sinyal}px rgba(255,170,40,0.9)` }} />
    </Zemin>
  );
};

// ---------- S01 hook: M08 yol + M01 kamyon (arka açık) içinde dev kutu $124T → damla → $18T dilimi → 10 kutu ----------
export const DevKutu: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const bol = ka(k, "one2", 99) + 0.15;
  const pb = interpolate(t, [bol, bol + 0.45], [0, 1], { ...CL, easing: EOUT });
  const charity = ka(k, "charity", 99);
  // kamyon kesiği 548x478; iç boşluk ≈ x %22–78, y %6–62
  const KW = D ? 960 : 1000, KH = (KW * 478) / 548;
  const kx = (D ? 540 : 960) - KW / 2, ky = (D ? 1500 : 1050) - KH;
  const ix0 = kx + KW * 0.22, ix1 = kx + KW * 0.78, iy0 = ky + KH * 0.06, iy1 = ky + KH * 0.62;
  const W = (ix1 - ix0) * 0.9, H = (iy1 - iy0) * 0.86;
  const cx = (ix0 + ix1) / 2;
  const itme = 1.06 + 0.012 * t + 0.05 * interpolate(t, [bol - 0.2, bol + 0.6], [0, 1], { ...CL, easing: EIO });
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <PlakaArka t0={t0} ad="M08" s0={1.02} kay={3} />
      <AbsoluteFill style={{ scale: String(itme), transformOrigin: `${cx}px ${iy1}px` }}>
        <Img src={f("ham-kamyon-arka.png")} style={{ position: "absolute", left: kx, top: ky, width: KW, height: KH }} />
        {pb < 1 ? (
          <div style={{ position: "absolute", left: cx - W / 2, top: iy1 - H, width: W, height: H, opacity: 1 - pb, scale: String(1 - pb * 0.2), transformOrigin: "50% 100%" }}>
            <div style={{ position: "absolute", inset: 0, background: "#b98a52", border: "7px solid #111", borderRadius: 10 }} />
            <div style={{ position: "absolute", left: "44%", top: 0, width: "12%", height: "100%", background: "rgba(240,220,170,0.6)" }} />
            <div style={{ position: "absolute", left: 0, right: 0, top: "18%", textAlign: "center", ...yaz(D ? 130 : 150, RENK.sari) }}>${G.toplam}T</div>
            <div style={{ position: "absolute", left: 0, right: 0, top: "62%", textAlign: "center", ...yaz(D ? 30 : 32, "#fff", "fredoka") }}>CERULLI EST. · THROUGH 2048</div>
            <div style={{ position: "absolute", right: -16, top: "8%", width: "16%", height: "84%", background: RENK.yesil, border: "6px solid #111", borderRadius: 8, translate: `${interpolate(t, [charity, charity + 0.5], [0, D ? 160 : 330], { ...CL, easing: EOUT })}px 0px`, opacity: t >= charity ? 1 : 0 }} />
          </div>
        ) : null}
        {t >= charity && pb < 1 ? <div style={{ position: "absolute", left: ix1 + (D ? -60 : 80), top: D ? iy0 - 120 : iy0 + 40, ...yaz(D ? 54 : 62, RENK.yesil), opacity: gir(t, charity + 0.2), whiteSpace: "nowrap" }}>${G.bagis}T → CHARITY</div> : null}
        {Array.from({ length: 12 }, (_, i) => {
          const bas = ka(k, "damla", 1.6) + i * 0.5;
          const q = (t - bas) / 0.9;
          if (q < 0 || q > 1 || pb >= 1) return null;
          return <div key={i} style={{ position: "absolute", left: cx - W * 0.42 + random(`d${i}`) * 50, top: iy1 - 10 + q * 260, width: 46, height: 24, background: "#7fc48a", border: "3px solid #111", borderRadius: 4, rotate: `${q * 140 + i * 30}deg`, opacity: 1 - q }} />;
        })}
        {pb > 0 ? <KutuDizisi t0={bol} giris={[bol, bol + 0.1, bol + 0.2]} cx={cx} cy={iy1 - (D ? 110 : 120)} w={D ? 92 : 96} /> : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// S12 bant gag'i (kutu yakın): M05 kesiğinin el + kutu kısmı (yüz kadraj dışı → anlatım sürerken ağız görünmez) + iki köşeden damla + 2. bant
export const BantEl: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "then", t0 + 1) + 0.4, b = ka(k, "so", t0 + 2.5) + 0.3;
  const w = D ? 1500 : 1700;
  const it = 1 + 0.01 * (t - t0);
  const bant = interpolate(t, [b, b + 0.4], [0, 1], { ...CL, easing: EOUT });
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <PlakaArka t0={t0} ad="M09" bulanik={3} />
      <AbsoluteFill style={{ scale: String(it) }}>
        <Kesik ad="ham-leo-bant" x={D ? 540 : 960} alt={D ? 300 : -360} w={w} kirp="inset(33% 0 0 0)" />
        {Array.from({ length: 7 }, (_, i) => {
          const q = (t - a - i * 0.45) / 0.9;
          if (q < 0 || q > 1) return null;
          return <div key={i} style={{ position: "absolute", left: (D ? 860 : 1330) + random(`b${i}`) * 30, top: (D ? 1500 : 980) + q * 200, width: 44, height: 22, background: "#7fc48a", border: "3px solid #111", borderRadius: 4, rotate: `${q * 160}deg`, opacity: 1 - q }} />;
        })}
        <div style={{ position: "absolute", left: D ? 560 : 1050, top: D ? 1420 : 860, height: 46, width: (D ? 420 : 520) * bant, background: "rgba(232,214,160,0.95)", border: "3px solid #8a7a4a", rotate: "-8deg" }} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------- G1: tek çubuk $124T = ~$105T heirs + ~$18T charity (R01–R03, R06); es: üstten geçen durak yolu (R04) ----------
export const G1: React.FC<{ t0: number; k: Record<string, number>; varyant?: "temel" | "es" | "bagis" }> = ({ t0, k, varyant = "temel" }) => {
  const t = useT();
  const D = useDikey();
  const L = D ? 90 : 210, W = D ? 900 : 1500, Y = D ? 820 : 560, H = D ? 150 : 150;
  const hazir = varyant !== "temel";
  const pm = hazir ? 1 : interpolate(t, [ka(k, "about1", t0 + 0.5), ka(k, "about1", t0 + 0.5) + 0.6], [0, 1], { ...CL, easing: EOUT });
  const pb = hazir ? 1 : interpolate(t, [ka(k, "about2", t0 + 1), ka(k, "about2", t0 + 1) + 0.5], [0, 1], { ...CL, easing: EOUT });
  const wm = (W * G.mirasci) / G.toplam, wb = (W * G.bagis) / G.toplam;
  const parla = varyant === "bagis" ? 0.5 + 0.5 * Math.sin((t - t0) * 4) : 0;
  const yol = varyant === "es" ? interpolate(t, [t0 + 0.2, t0 + 1.2], [0, 1], { ...CL, easing: EIO }) : 0;
  return (
    <Zemin t0={t0}>
      {varyant !== "es" ? (
        <>
          <div style={{ position: "absolute", left: L, top: Y - (D ? 420 : 330), ...yaz(D ? 64 : 76) }}>${G.toplam}T EXPECTED TO PASS DOWN</div>
          <div style={{ position: "absolute", left: L, top: Y - (D ? 330 : 230), ...yaz(D ? 32 : 34, RENK.ikincil, "fredoka") }}>Cerulli Associates forecast · Dec 2024 · through 2048 · figures rounded</div>
        </>
      ) : null}
      <div style={{ position: "absolute", left: L, top: Y, width: W, height: H, border: "5px solid rgba(255,255,255,0.5)", borderRadius: 14, opacity: gir(t, t0) }} />
      <div style={{ position: "absolute", left: L, top: Y, width: wm * pm, height: H, background: RENK.mavi, borderRadius: "14px 0 0 14px", border: "5px solid #111" }} />
      <div style={{ position: "absolute", left: L + wm, top: Y, width: wb * pb, height: H, background: RENK.yesil, borderRadius: "0 14px 14px 0", border: "5px solid #111", boxShadow: parla ? `0 0 ${60 * parla}px rgba(47,174,106,0.95)` : undefined }} />
      <div style={{ position: "absolute", left: L + 24, top: Y + 36, ...yaz(D ? 56 : 64), opacity: pm }}>~${G.mirasci}T HEIRS</div>
      <div style={{ position: "absolute", left: L + wm - (D ? 120 : 40), top: Y + H + 24, ...yaz(D ? 46 : 54, RENK.yesil), opacity: pb, whiteSpace: "nowrap" }}>~${G.bagis}T CHARITY</div>
      {varyant === "bagis" ? <div style={{ position: "absolute", left: L + wm - (D ? 360 : 380), top: Y + H + 100, ...yaz(D ? 46 : 54, RENK.sari), opacity: gir(t, t0 + 0.4) }}>THE ONE PART THAT SKIPS HEIRS</div> : null}
      {varyant === "temel" ? (
        <div style={{ position: "absolute", left: L, top: Y + H + (D ? 120 : 110), ...yaz(D ? 40 : 42, RENK.ikincil, "fredoka"), opacity: gir(t, ka(k, "nearly", t0) + 0.2) }}>
          ~${G.boomer}T from Baby Boomers and older ({G.boomerPay}%)
        </div>
      ) : null}
      {varyant === "es" ? (
        <>
          <svg width={D ? 1080 : 1920} height={D ? 1920 : 1080} style={{ position: "absolute", left: 0, top: 0 }}>
            <path d={`M ${L} ${Y - 40} C ${L + W * 0.3} ${Y - 260}, ${L + W * 0.7} ${Y - 260}, ${L + W} ${Y - 40}`} fill="none" stroke={RENK.sari} strokeWidth={14} strokeDasharray="30 18" pathLength={1} strokeDashoffset={0} opacity={yol} />
          </svg>
          <div style={{ position: "absolute", left: L + W / 2, top: Y - (D ? 300 : 290), translate: "-50% -100%", padding: "14px 26px", background: "#f2c230", border: "7px solid #111", borderRadius: 18, whiteSpace: "nowrap", ...yaz(D ? 46 : 54, "#111"), WebkitTextStroke: "0px", opacity: gir(t, ka(k, "fifty", t0) + 0.3) }}>
            SPOUSE FIRST · ~${G.es}T STOPS HERE ON THE WAY
          </div>
        </>
      ) : null}
    </Zemin>
  );
};

// ---------- Ömür şeridi: AGE 65 → ~20 MORE YEARS (R14) ----------
export const Omur: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const L = D ? 90 : 260, W = D ? 900 : 1400, Y = D ? 900 : 560;
  const p = interpolate(t, [ka(k, "about", t0 + 0.6) + 0.1, ka(k, "about", t0 + 0.6) + 1.2], [0, 1], { ...CL, easing: EOUT });
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L, top: Y - 260, ...yaz(D ? 70 : 84) }}>AGE 65 → ~{G.omur} MORE YEARS</div>
      <div style={{ position: "absolute", left: L, top: Y - 150, ...yaz(D ? 34 : 36, RENK.ikincil, "fredoka") }}>US average, at 65</div>
      <div style={{ position: "absolute", left: L, top: Y, width: W, height: 26, background: "rgba(255,255,255,0.18)", borderRadius: 13 }} />
      <div style={{ position: "absolute", left: L, top: Y, width: W * p, height: 26, background: RENK.mavi, borderRadius: 13, border: "4px solid #111" }} />
      {Array.from({ length: G.omur / 5 + 1 }, (_, i) => (
        <div key={i} style={{ position: "absolute", left: L + (W * i) / (G.omur / 5) - 30, top: Y + 50, width: 60, textAlign: "center", ...yaz(40, i * 5 <= p * G.omur ? RENK.murekkep : RENK.gri, "fredoka") }}>
          {65 + i * 5}
        </div>
      ))}
      <div style={{ position: "absolute", left: L + W * p - 28, top: Y - 34, width: 56, height: 56, borderRadius: 28, background: RENK.sari, border: "5px solid #111" }} />
    </Zemin>
  );
};

// ---------- İkon ızgarası (G2: 100 kişiden 56; 22'si >5 yıl — R16) ----------
const Insan: React.FC<{ x: number; y: number; s: number; renk: string }> = ({ x, y, s, renk }) => (
  <svg width={40 * s} height={60 * s} viewBox="0 0 40 60" style={{ position: "absolute", left: x, top: y }}>
    <circle cx={20} cy={12} r={10} fill={renk} stroke="#111" strokeWidth={3} />
    <path d="M4 58 C4 30, 36 30, 36 58 Z" fill={renk} stroke="#111" strokeWidth={3} />
  </svg>
);
export const G2: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const s = D ? 1.7 : 1.5;
  const L = D ? 60 : 140, T = D ? 520 : 200, ar = D ? 96 : 64;
  const a56 = ka(k, "more", t0 + 0.6), a22 = ka(k, "about", t0 + 2);
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L, top: D ? 260 : 70, ...yaz(D ? 54 : 60), width: D ? 960 : 1600 }}>OF AMERICANS TURNING 65 · SERIOUS LONG-TERM CARE</div>
      {Array.from({ length: 100 }, (_, i) => {
        const r = Math.floor(i / 10), c = i % 10;
        const renkli = i < G.bakimYuzde && t >= a56 + i * 0.012;
        const koyu = i < G.bakim5yil && t >= a22 + i * 0.02;
        return <Insan key={i} x={L + c * ar} y={T + r * (D ? 98 : 74)} s={s * 0.9} renk={koyu ? RENK.kahve : renkli ? RENK.mavi : "#3a4358"} />;
      })}
      <div style={{ position: "absolute", left: D ? 90 : 840, top: D ? 1530 : 330, ...yaz(D ? 120 : 150, RENK.mavi), opacity: gir(t, a56 + 0.4) }}>{G.bakimYuzde}%</div>
      <div style={{ position: "absolute", left: D ? 420 : 840, top: D ? 1560 : 520, ...yaz(D ? 50 : 60, RENK.kahve), opacity: gir(t, a22 + 0.3) }}>MORE THAN 5 YEARS: {G.bakim5yil}%</div>
      <div style={{ position: "absolute", left: D ? 90 : 840, top: D ? 1650 : 620, ...yaz(D ? 32 : 34, RENK.ikincil, "fredoka") }}>HHS/ASPE estimate</div>
    </Zemin>
  );
};

// Fatura kartı: NURSING HOME, PRIVATE ROOM $129,575 / YEAR (R13)
export const Fatura: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "median", t0 + 0.8);
  const v = interpolate(t, [a, a + 0.9], [0, G.huzurevi], { ...CL, easing: EOUT });
  const p = gir(t, t0);
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 90 : 460, top: D ? 520 : 200, width: D ? 900 : 1000, height: D ? 820 : 620, background: "#f4f1ea", border: "8px solid #111", borderRadius: 18, rotate: "-2deg", opacity: p, scale: String(0.85 + 0.15 * p) }}>
        <div style={{ margin: "50px 50px 0", ...yaz(D ? 52 : 56, "#111"), WebkitTextStroke: "0px" }}>NURSING HOME, PRIVATE ROOM</div>
        <div style={{ margin: "10px 50px", height: 6, background: "#111" }} />
        <div style={{ margin: "40px 50px 0", ...yaz(D ? 120 : 150, RENK.kirmizi) }}>{t < a ? "$ ?" : `$${Math.round(v).toLocaleString("en-US")}`}</div>
        <div style={{ margin: "0 50px", ...yaz(D ? 56 : 60, "#111"), WebkitTextStroke: "0px" }}>/ YEAR</div>
        <div style={{ margin: "40px 50px 0", ...yaz(D ? 32 : 34, "#555", "fredoka"), WebkitTextStroke: "0px" }}>US median · CareScout 2025</div>
      </div>
    </Zemin>
  );
};

// İki kapı: MEDICARE / MEDICAID (R25, mekanizma; eylem önerisi yok)
export const Kapilar: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const kapi = (x: number, y: number, ad: string, levha: string, an: number, renk: string) => (
    <div style={{ position: "absolute", left: x, top: y, width: D ? 800 : 620, opacity: gir(t, an), scale: String(0.85 + 0.15 * gir(t, an)) }}>
      <div style={{ height: D ? 360 : 440, background: renk, border: "8px solid #111", borderRadius: "16px 16px 0 0", display: "flex", alignItems: "flex-start", justifyContent: "center", paddingTop: 30 }}>
        <div style={{ ...yaz(D ? 76 : 70) }}>{ad}</div>
      </div>
      <div style={{ marginTop: 20, padding: "16px 20px", background: "#f4f1ea", border: "6px solid #111", borderRadius: 12, ...yaz(D ? 38 : 36, "#111", "fredoka"), WebkitTextStroke: "0px" }}>{levha}</div>
    </div>
  );
  return (
    <Zemin t0={t0}>
      {kapi(D ? 140 : 200, D ? 220 : 120, "MEDICARE", "LONG-TERM CUSTODIAL CARE: GENERALLY NOT COVERED", t0, "#35507e")}
      {kapi(D ? 140 : 1100, D ? 980 : 120, "MEDICAID", "STATES MUST TRY TO RECOVER COSTS FROM THE ESTATE", ka(k, "and", t0 + 1), "#5a3f7a")}
      <div style={{ position: "absolute", left: D ? 600 : 1500, top: D ? 1720 : 880, padding: "8px 18px", background: "#f2c230", border: "5px solid #111", rotate: "-8deg", ...yaz(40, "#111"), WebkitTextStroke: "0px", opacity: gir(t, ka(k, "states", t0 + 2)) }}>ESTATE RECOVERY</div>
    </Zemin>
  );
};

// 7 ikondan 1'i: ~1 IN 7 · $100K+ out of pocket (R17)
export const YedideBir: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "about", t0 + 0.5) + 0.2;
  const s = D ? 2.6 : 3;
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 70 : 200, top: D ? 360 : 120, ...yaz(D ? 60 : 70), width: D ? 940 : 1500 }}>PEOPLE TURNING 65: OUT-OF-POCKET CARE</div>
      {Array.from({ length: 7 }, (_, i) => (
        <Insan key={i} x={(D ? 40 : 230) + i * (D ? 140 : 210)} y={D ? 760 : 380} s={s * (D ? 0.95 : 1)} renk={i === 3 && t >= a ? RENK.kirmizi : "#3a4358"} />
      ))}
      <div style={{ position: "absolute", left: D ? 70 : 200, top: D ? 1100 : 640, ...yaz(D ? 66 : 80, RENK.kirmizi), opacity: gir(t, a + 0.2) }}>~1 IN 7: $100K+ OUT OF POCKET</div>
      <div style={{ position: "absolute", left: D ? 70 : 200, top: D ? 1200 : 760, ...yaz(D ? 32 : 36, RENK.ikincil, "fredoka") }}>estimate, 2020 dollars</div>
    </Zemin>
  );
};

// ---------- G3: 55% (2024) → 47% (2026) — sol-orta yerleşim (S17 sonunda ABONE-2 sağ altta) ----------
export const G3: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const H = D ? 760 : 560, taban = D ? 1300 : 860, bw = D ? 280 : 230;
  const cubuk = (x: number, deger: number, yil: string, an: number, renk: string) => {
    const p = interpolate(t, [an, an + 0.6], [0, 1], { ...CL, easing: EOUT });
    const h = (H * deger) / 100;
    return (
      <>
        <div style={{ position: "absolute", left: x, top: taban - h * p, width: bw, height: h * p, background: renk, border: "5px solid #111", borderRadius: "10px 10px 0 0" }} />
        <div style={{ position: "absolute", left: x, width: bw, top: taban - h * p - 110, textAlign: "center", ...yaz(D ? 90 : 96, renk === RENK.mavi ? RENK.murekkep : RENK.ikincil), opacity: p }}>{deger}%</div>
        <div style={{ position: "absolute", left: x, width: bw, top: taban + 16, textAlign: "center", ...yaz(D ? 50 : 50, RENK.ikincil, "fredoka") }}>{yil}</div>
      </>
    );
  };
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 70 : 120, top: D ? 230 : 70, width: D ? 940 : 1000, ...yaz(D ? 54 : 58) }}>"THE NEXT GENERATION IS READY TO TAKE ON THE FAMILY'S GIVING"</div>
      <div style={{ position: "absolute", left: D ? 120 : 160, top: taban, width: D ? 840 : 760, height: 5, background: "rgba(255,255,255,0.5)" }} />
      {cubuk(D ? 170 : 220, G.hazir2024, "2024", ka(k, "fifty", t0 + 2), "#56607a")}
      {cubuk(D ? 600 : 580, G.hazir2026, "2026", ka(k, "forty", t0 + 1), RENK.mavi)}
      <div style={{ position: "absolute", left: D ? 70 : 120, top: D ? 1420 : 960, width: D ? 940 : 1040, ...yaz(D ? 30 : 28, RENK.ikincil, "fredoka") }}>
        BofA Private Bank survey · {G.orneklem.toLocaleString("en-US")} people with ${G.esikMilyon}M+ investable assets
      </div>
    </Zemin>
  );
};

// ---------- S19: BOOMERS ~41% OF US HOUSEHOLD REAL ESTATE (R23) ----------
export const G19: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const L = D ? 90 : 210, W = D ? 900 : 1500, Y = D ? 900 : 520;
  const a = ka(k, "fed", t0) + 0.3;
  const p = interpolate(t, [a, a + 0.8], [0, 1], { ...CL, easing: EOUT });
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L, top: Y - 260, ...yaz(D ? 60 : 72), width: W }}>ALL REAL ESTATE HELD BY US HOUSEHOLDS</div>
      <div style={{ position: "absolute", left: L, top: Y, width: W, height: 150, background: "#3a4358", border: "5px solid #111", borderRadius: 14 }} />
      <div style={{ position: "absolute", left: L, top: Y, width: ((W * G.boomerEmlak) / 100) * p, height: 150, background: KUTU_RENK.ev, border: "5px solid #111", borderRadius: "14px 0 0 14px" }} />
      <div style={{ position: "absolute", left: L + 24, top: Y + 30, ...yaz(D ? 64 : 76), opacity: p }}>BOOMERS ~{Math.round(G.boomerEmlak)}%</div>
      <div style={{ position: "absolute", left: L, top: Y + 190, ...yaz(D ? 34 : 36, RENK.ikincil, "fredoka") }}>about two-fifths · Fed DFA, Q2 2026</div>
    </Zemin>
  );
};

// ---------- G4: vergi eşiği $15M vs medyan ~$410K (R18, R19; aynı doğrusal ölçek) ----------
export const G4: React.FC<{ t0: number; k: Record<string, number>; eyalet?: boolean }> = ({ t0, k, eyalet }) => {
  const t = useT();
  const D = useDikey();
  const taban = D ? 1420 : 920, H = D ? 980 : 760, L = D ? 120 : 380;
  const aE = eyalet ? -10 : ka(k, "fifteen", t0 + 0.5), aM = eyalet ? -10 : ka(k, "median", t0 + 2), aB = eyalet ? -10 : ka(k, "the", t0 + 3);
  const pe = interpolate(t, [aE, aE + 0.4], [0, 1], { ...CL, easing: EOUT });
  const hm = (H * G.medyan) / G.esikVergi;
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L - 40, top: taban, width: D ? 900 : 1300, height: 5, background: "rgba(255,255,255,0.5)" }} />
      <div style={{ position: "absolute", left: L - 40, top: taban - H * pe, width: D ? 900 : 1300, height: 10, background: RENK.kirmizi, border: "3px solid #111", opacity: pe }} />
      <div style={{ position: "absolute", left: L - 40, top: taban - H - 130, ...yaz(D ? 52 : 60, RENK.kirmizi), opacity: eyalet ? 1 : gir(t, t0), width: D ? 900 : 1300 }}>
        US FEDERAL ESTATE TAX STARTS: ${G.esikVergi / 1e6}M PER PERSON (2026)
      </div>
      <div style={{ position: "absolute", left: L + (D ? 280 : 420), top: taban - Math.max(hm, 6), width: D ? 200 : 220, height: Math.max(hm, 6), background: RENK.mavi, border: "4px solid #111", opacity: gir(t, aM) }} />
      <div style={{ position: "absolute", left: L + (D ? 50 : 700), top: taban - (D ? 150 : 140), width: D ? 820 : 760, ...yaz(D ? 40 : 42, RENK.mavi, "fredoka"), opacity: gir(t, aM + 0.2) }}>
        MEDIAN NET WORTH, AGES 65–74: ~${Math.round(G.medyan / 1000)}K
      </div>
      {!eyalet ? (
        <div style={{ position: "absolute", left: L + (D ? 330 : 470), top: taban - H + 30, height: Math.max(0, H - hm - 60) * interpolate(t, [aB, aB + 0.6], [0, 1], CL), width: 8, background: RENK.sari }} />
      ) : null}
      <div style={{ position: "absolute", left: L + (D ? 380 : 520), top: taban - H / 2, ...yaz(D ? 54 : 64, RENK.sari), opacity: gir(t, aB + 0.4) }}>DOZENS OF TIMES HIGHER</div>
      {eyalet ? <div style={{ position: "absolute", left: L - 40, top: D ? 1500 : 250, ...yaz(D ? 44 : 48, RENK.sari, "fredoka"), opacity: gir(t, t0 + 0.1) }}>Some states have their own estate or inheritance taxes.</div> : null}
    </Zemin>
  );
};

export const UkKart: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "three", t0 + 1);
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 90 : 560, top: D ? 620 : 260, width: D ? 900 : 800, padding: 50, background: "#f4f1ea", border: "8px solid #111", borderRadius: 20, opacity: gir(t, t0), rotate: "1.5deg" }}>
        <div style={{ ...yaz(70, "#111"), WebkitTextStroke: "0px" }}>OTHER COUNTRIES: OTHER LINES</div>
        <div style={{ marginTop: 30, ...yaz(D ? 100 : 110, RENK.kirmizi), opacity: gir(t, a) }}>UK: £{G.ukEsik.toLocaleString("en-US")}</div>
        <div style={{ marginTop: 10, ...yaz(40, "#333", "fredoka"), WebkitTextStroke: "0px" }}>inheritance tax threshold (2026)</div>
      </div>
    </Zemin>
  );
};

// Gişe TAX (gölgeli) → bariyer kalkar
export const Gise: React.FC<{ t0: number; k: Record<string, number>; acik?: boolean }> = ({ t0, k, acik }) => {
  const t = useT();
  const D = useDikey();
  const a = acik ? ka(k, "the2", t0 + 0.5) + 0.3 : 99;
  const kalk = interpolate(t, [a, a + 0.6], [0, -78], { ...CL, easing: EOUT });
  const flas = !acik && t < ka(k, "so", 2) ? Math.max(0, Math.sin(t * 9) * interpolate(t, [0, 0.4, 0.8], [0, 1, 0], CL)) : 0;
  const cx = D ? 540 : 960, by = D ? 1300 : 800;
  return (
    <Zemin t0={t0} renk={acik ? RENK.yuzey : "#090c14"}>
      <div style={{ position: "absolute", left: cx - 260, top: by - 520, width: 520, height: 520, background: "#2b2f3d", border: "8px solid #111", borderRadius: "20px 20px 0 0" }}>
        <div style={{ margin: "30px auto", width: 380, padding: "10px 0", textAlign: "center", background: acik ? "#c8cfdb" : "#5b616f", border: "6px solid #111", borderRadius: 12, ...yaz(120, acik ? "#111" : RENK.kirmizi), WebkitTextStroke: "0px" }}>TAX</div>
      </div>
      <div style={{ position: "absolute", left: cx + 260, top: by - 160, width: D ? 260 : 620, height: 34, background: "repeating-linear-gradient(90deg, #e05a4f 0 60px, #f4f1ea 60px 120px)", border: "5px solid #111", transformOrigin: "0% 50%", rotate: `${kalk}deg` }} />
      <AbsoluteFill style={{ background: `rgba(200,220,255,${flas * 0.5})` }} />
    </Zemin>
  );
};

// ---------- G5: kuşak payları (R08) — iki ayrı pencere, iki ayrı kart (aynı eksende toplanmaz) ----------
export const G5: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const kart = (x: number, y: number, ust: string, deger: string, alt: string, an: number, renk: string) => (
    <div style={{ position: "absolute", left: x, top: y, width: D ? 900 : 760, padding: 40, background: "rgba(15,22,38,0.95)", border: `5px solid ${renk}`, borderRadius: 22, opacity: gir(t, an), scale: String(0.85 + 0.15 * gir(t, an)) }}>
      <div style={{ ...yaz(D ? 46 : 46, RENK.ikincil, "fredoka") }}>{ust}</div>
      <div style={{ ...yaz(D ? 130 : 140, renk) }}>{deger}</div>
      <div style={{ ...yaz(D ? 44 : 44, RENK.murekkep, "fredoka") }}>{alt}</div>
    </div>
  );
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 90 : 160, top: D ? 230 : 80, ...yaz(D ? 54 : 60) }}>WHO INHERITS THE MOST? (Cerulli est.)</div>
      {kart(D ? 90 : 160, D ? 420 : 260, "FIRST 10 YEARS", `GEN X ~$${G.genx10}T`, "the most, early on", ka(k, "in", t0 + 0.3), RENK.kahve)}
      {kart(D ? 90 : 1000, D ? 960 : 260, "THROUGH 2048", `MILLENNIALS ~$${G.millennial}T`, "the biggest share overall", ka(k, "but", t0 + 2), RENK.mavi)}
    </Zemin>
  );
};

// Solan 1 $ banknotu: 2% × 20 yıl → ~$0.67 (R21 [H])
export const Banknot: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "even", t0) + 0.4;
  const p = interpolate(t, [a, a + 2.2], [0, 1], { ...CL, easing: EIO });
  const v = 1 - (1 - G.alimGucu) * p;
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 140 : 560, top: D ? 520 : 200, width: 800, height: 360, background: "#86c78f", border: "8px solid #111", borderRadius: 18, opacity: 1 - (1 - G.alimGucu) * p, scale: String(D ? 1 : 1), display: "flex", alignItems: "center", justifyContent: "center" }}>
        <div style={{ width: 220, height: 220, borderRadius: 110, border: "8px solid #2c5e35", display: "flex", alignItems: "center", justifyContent: "center", ...yaz(130, "#f4f1ea") }}>$1</div>
      </div>
      <div style={{ position: "absolute", left: D ? 140 : 560, top: D ? 960 : 600, ...yaz(D ? 120 : 130, RENK.sari) }}>BUYS ~${v.toFixed(2)}</div>
      <div style={{ position: "absolute", left: D ? 140 : 560, top: D ? 1120 : 760, ...yaz(D ? 46 : 50, RENK.murekkep, "fredoka"), opacity: gir(t, t0 + 0.1) }}>
        {G.enflasyon}% A YEAR × 20 YEARS (Fed target)
      </div>
    </Zemin>
  );
};

// ---------- G6: Okafor şelalesi (envanter; ailenin 10 kutusundan, D2) ----------
export const Selale: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const W = D ? 1000 : 1700, L = D ? 40 : 110, taban = D ? 1380 : 900, U = D ? 82 : 62; // U = 1 kutu yüksekliği
  const kolon = ["LOADED", ...DURAK.map((d) => d[0]), "DELIVERED"];
  const cw = W / kolon.length;
  const an = [ka(k, "loaded", t0), ...[1, 2, 3, 4, 5, 6].map((n) => ka(k, `s${n}`, t0 + n)), ka(k, "delivered", t0 + 7)];
  const dilim = 0.35; // görsel "slice" (rakamsız; kutu-hesap.py: HOUSE +0 → dilim)
  let kalan = 10;
  const cubuk: React.ReactNode[] = [];
  kolon.forEach((ad, i) => {
    const p = interpolate(t, [an[i], an[i] + 0.4], [0, 1], { ...CL, easing: EOUT });
    const x = L + i * cw + cw * 0.12, w = cw * 0.76;
    const etiket = (metin: string, y: number, renk: string) => (
      <div key={`e${i}`} style={{ position: "absolute", left: x - 10, width: w + 20, top: y, textAlign: "center", ...yaz(D ? 30 : 38, renk), opacity: p }}>{metin}</div>
    );
    if (i === 0 || i === kolon.length - 1) {
      const h = (i === 0 ? 10 : kalan - dilim) * U;
      cubuk.push(<div key={i} style={{ position: "absolute", left: x, width: w, top: taban - h * p, height: h * p, background: i === 0 ? "#b98a52" : RENK.mavi, border: "4px solid #111", borderRadius: "8px 8px 0 0" }} />);
      cubuk.push(etiket(i === 0 ? "10" : "6 − SLICE", taban - h - 54, RENK.murekkep));
      if (i > 0) cubuk.push(etiket("LATER", taban - h - 100, RENK.sari));
    } else {
      const d = DURAK[i - 1][1];
      const ust = kalan;
      const h = ad === "HOUSE" ? dilim : -d;
      kalan += d;
      if (h > 0) cubuk.push(<div key={i} style={{ position: "absolute", left: x, width: w, top: taban - ust * U, height: h * U * p, background: ad === "HOUSE" ? `repeating-linear-gradient(45deg, ${KUTU_RENK.ev} 0 8px, #7a2e20 8px 16px)` : RENK.kahve, border: "4px solid #111" }} />);
      else cubuk.push(<div key={i} style={{ position: "absolute", left: x, width: w, top: taban - ust * U - 4, height: 8, background: RENK.ikincil, opacity: p }} />);
      const metin = ad === "HOUSE" ? "− SLICE" : d === 0 ? "0" : `${d}`;
      cubuk.push(etiket(metin, taban - ust * U - 54, d === 0 && ad !== "HOUSE" ? RENK.ikincil : RENK.kahve));
      if (ad === "SPOUSE") cubuk.push(<KumSaati key="ks" an={an[i] + 0.2} x={x + w / 2 - (D ? 60 : 30)} y={taban - ust * U - 250} />);
    }
    cubuk.push(<div key={`a${i}`} style={{ position: "absolute", left: x - 16, width: w + 32, top: taban + 14, textAlign: "center", ...yaz(D ? 22 : 26, RENK.ikincil, "fredoka"), opacity: interpolate(t, [t0, t0 + 0.3], [0, 1], CL) }}>{ad}</div>);
  });
  const sp = gir(t, ka(k, "split", t0 + 9));
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L, top: D ? 260 : 178, ...yaz(D ? 56 : 60) }}>WHAT REACHES THE KIDS</div>
      <div style={{ position: "absolute", left: L, top: taban, width: W, height: 5, background: "rgba(255,255,255,0.5)" }} />
      {cubuk}
      <div style={{ position: "absolute", left: D ? 260 : 1240, top: D ? 1500 : 170, padding: "12px 26px", background: "#f2c230", border: "6px solid #111", borderRadius: 14, ...yaz(D ? 56 : 60, "#111"), WebkitTextStroke: "0px", opacity: sp, scale: String(0.7 + 0.3 * sp) }}>2 KIDS → ≈3 EACH</div>
      <OrnekEtiket />
    </Zemin>
  );
};

// ---------- G7: bölünmüş tablo kartı (R07 Cerulli ‖ R24 Fed DFA — ayrı paneller, toplanmaz) ----------
export const G7: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a2 = ka(k, "cerulli", t0) + 0.5, aD = ka(k, "and", t0 + 2) + 0.3, aB = ka(k, "bottom", t0 + 3);
  const hucre = D ? 62 : 46;
  const PL = D ? 230 : 120, PT = D ? 420 : 300;
  const bar = (y: number, etiket: string, deger: number, an: number, renk: string) => {
    const p = interpolate(t, [an, an + 0.6], [0, 1], { ...CL, easing: EOUT });
    const W = D ? 760 : 620;
    return (
      <div style={{ position: "absolute", left: D ? 160 : 1060, top: y }}>
        <div style={{ ...yaz(D ? 40 : 40, RENK.murekkep, "fredoka") }}>{etiket}</div>
        <div style={{ marginTop: 8, width: W, height: 70, background: "#2a3248", border: "4px solid #111", borderRadius: 10, position: "relative" }}>
          <div style={{ width: (W * deger * p) / 100, height: "100%", background: renk, borderRadius: 8 }} />
        </div>
        <div style={{ ...yaz(D ? 60 : 64, renk), opacity: p }}>≈{Math.round(deger)}%</div>
      </div>
    );
  };
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 60 : 120, top: D ? 200 : 60, width: D ? 960 : 1700, ...yaz(D ? 56 : 64) }}>THE HEADLINE IS REAL. IT'S JUST LUMPY.</div>
      {/* panel 1: Cerulli — 100 haneden 2 */}
      <div style={{ position: "absolute", left: PL - 20, top: PT - 90, ...yaz(D ? 36 : 36, RENK.kahve, "fredoka"), width: D ? 900 : 820 }}>${G.toplam}T: ~HALF (~${G.yari}T) FROM {G.haneYuzde}% OF HOUSEHOLDS</div>
      {Array.from({ length: 100 }, (_, i) => {
        const r = Math.floor(i / 10), c = i % 10;
        const turuncu = i < G.haneYuzde && t >= a2 + i * 0.2;
        return <div key={i} style={{ position: "absolute", left: PL + c * hucre, top: PT + r * hucre, width: hucre - 8, height: hucre - 8, borderRadius: 6, background: turuncu ? RENK.kahve : "#3a4358", border: "3px solid #111", opacity: interpolate(t, [t0 + i * 0.004, t0 + 0.2 + i * 0.004], [0, 1], CL), scale: turuncu ? String(1 + 0.12 * Math.sin(t * 4)) : "1" }} />;
      })}
      {/* ayırıcı: farklı kaynaklar */}
      <div style={{ position: "absolute", left: D ? 60 : 1000, top: D ? 1080 : 260, width: D ? 960 : 5, height: D ? 5 : 640, background: "rgba(255,255,255,0.35)" }} />
      <div style={{ position: "absolute", left: D ? 160 : 1060, top: D ? 1110 : 250, ...yaz(D ? 34 : 34, RENK.ikincil, "fredoka"), opacity: gir(t, aD) }}>US HOUSEHOLD WEALTH, Q2 2026 (Fed) — separate data</div>
      {bar(D ? 1180 : 330, "TOP 10%", G.ust10, aD, RENK.kahve)}
      {bar(D ? 1420 : 600, "BOTTOM 50%", G.alt50, aB, RENK.mavi)}
    </Zemin>
  );
};

// ---------- Kod nesneleri (Canva sahnesi gelince bazıları plaka + bu katman olur) ----------
export const Siluet: React.FC<{ x: number; y: number; h: number; renk?: string; opak?: number; sac?: string }> = ({ x, y, h, renk = "#11151f", opak = 1, sac }) => (
  <svg width={h * 0.5} height={h} viewBox="0 0 50 100" style={{ position: "absolute", left: x - h * 0.25, top: y - h, opacity: opak }}>
    <circle cx={25} cy={16} r={13} fill={renk} />
    {sac ? <path d="M12 14 A13 13 0 0 1 38 14 L38 10 A13 11 0 0 0 12 10 Z" fill={sac} /> : null}
    <path d="M6 100 C6 40, 44 40, 44 100 Z" fill={renk} />
  </svg>
);

export const AileKapi: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  const cx = D ? 540 : 620, y = D ? 1250 : 860;
  const isik = 0.85 + 0.15 * Math.sin(t * 1.3);
  return (
    <Zemin t0={t0} renk="#0d1a2e">
      <div style={{ position: "absolute", left: cx - 330, top: y - 640, width: 660, height: 640, background: `rgba(255,196,110,${0.75 * isik})`, border: "10px solid #3b2a1a", borderBottom: "none", boxShadow: `0 0 120px rgba(255,190,100,${0.5 * isik})` }} />
      {[[-210, 520], [-70, 560], [70, 400], [190, 380]].map(([dx, h], i) => (
        <Siluet key={i} x={cx + dx} y={y} h={h * 0.72 * interpolate(t, [t0 + i * 0.1, t0 + 0.3 + i * 0.1], [0.9, 1], { ...CL, easing: EPOP })} />
      ))}
      <OrnekEtiket />
    </Zemin>
  );
};

export const Solma: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "when", t0) + 1.2;
  const cx = D ? 540 : 960, y = D ? 1250 : 880;
  return (
    <Zemin t0={t0} renk="#0d1a2e">
      <div style={{ position: "absolute", left: cx - 300, top: y - 620, width: 600, height: 620, background: "rgba(255,196,110,0.75)", border: "10px solid #3b2a1a", borderBottom: "none", boxShadow: "0 0 140px rgba(255,190,100,0.55)" }} />
      <Siluet x={cx - 120} y={y} h={400} opak={interpolate(t, [a, a + 1.4], [1, 0], { ...CL, easing: EIO })} />
      <Siluet x={cx + 120} y={y} h={385} />
    </Zemin>
  );
};

export const Bayrak: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const aB = ka(k, "baton", t0 + 1.5), aK = ka(k, "kids", t0 + 3);
  const L = D ? 80 : 160, W = D ? 920 : 1600, y = D ? 1150 : 760;
  const devir = interpolate(t, [aB, aB + 0.8], [0, 1], { ...CL, easing: EIO });
  const kos = (x: number, renk: string, lbl: string, an: number) => (
    <>
      <Siluet x={x} y={y} h={D ? 300 : 260} renk={renk} opak={gir(t, an)} />
      <div style={{ position: "absolute", left: x - 140, width: 280, top: y + 20, textAlign: "center", ...yaz(D ? 34 : 34, RENK.murekkep, "fredoka"), opacity: gir(t, an) }}>{lbl}</div>
    </>
  );
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: L, top: y - 30, width: W, height: 60, background: "#a8442f", borderTop: "6px solid #f4f1ea", borderBottom: "6px solid #f4f1ea" }} />
      <div style={{ position: "absolute", left: L, top: D ? 250 : 100, ...yaz(D ? 60 : 70) }}>A RELAY, NOT A LEAK</div>
      {kos(L + W * 0.12, "#2b3550", "PARENT 1", t0)}
      {kos(L + W * 0.38, "#2b3550", "PARTNER", t0 + 0.2)}
      {kos(L + W * 0.82, "#3b4a6e", "KIDS (WAITING)", aK)}
      {kos(L + W * 0.92, "#3b4a6e", "", aK + 0.1)}
      <div style={{ position: "absolute", left: L + W * (0.12 + 0.26 * devir) - 40, top: y - (D ? 220 : 190), width: 80, height: 22, background: RENK.sari, border: "4px solid #111", borderRadius: 8, rotate: "-20deg" }} />
    </Zemin>
  );
};

export const BuyuyenKutu: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  const b = interpolate(t, [t0 + 0.2, t0 + 1.2, t0 + 2.4, t0 + 3.6], [1, 1.18, 1.18, 0.82], { ...CL, easing: EIO });
  return (
    <Zemin t0={t0}>
      <Kutu tur="emeklilik" x={D ? 540 : 960} y={D ? 1250 : 800} w={D ? 520 : 460} s={b} />
      <div style={{ position: "absolute", left: D ? 90 : 300, top: D ? 300 : 110, ...yaz(D ? 54 : 60), opacity: gir(t, t0 + 0.2) }}>INVESTED: CAN GROW</div>
      <div style={{ position: "absolute", left: D ? 90 : 1220, top: D ? 420 : 110, ...yaz(D ? 54 : 60, RENK.kahve), opacity: gir(t, t0 + 2.4) }}>BEING SPENT: SHRINKS</div>
    </Zemin>
  );
};

export const BantKutu: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "then", t0) + 0.4, b = ka(k, "so", t0 + 1.5) + 0.3;
  const bant = (an: number, y: number) => <div style={{ position: "absolute", left: D ? 260 : 700, top: y, height: 40, width: (D ? 560 : 520) * interpolate(t, [an, an + 0.35], [0, 1], { ...CL, easing: EOUT }), background: "rgba(232,214,160,0.92)", border: "3px solid #8a7a4a", rotate: "-4deg" }} />;
  return (
    <Zemin t0={t0}>
      <Kutu tur="banka" x={D ? 540 : 960} y={D ? 1200 : 820} w={D ? 600 : 560} />
      {bant(-1, D ? 1130 : 760)}
      {bant(b, D ? 760 : 470)}
      {Array.from({ length: 6 }, (_, i) => {
        const q = (t - a - i * 0.5) / 0.9;
        if (q < 0 || q > 1) return null;
        return <div key={i} style={{ position: "absolute", left: D ? 790 : 1200, top: (D ? 900 : 560) + q * 260, width: 40, height: 22, background: "#7fc48a", border: "3px solid #111", rotate: `${q * 160}deg`, opacity: 1 - q }} />;
      })}
    </Zemin>
  );
};

export const Hayalet: React.FC<{ t0: number; uc?: boolean }> = ({ t0, uc }) => {
  const t = useT();
  const D = useDikey();
  const kamyon = (x: number, y: number, kutu: number, lbl: string, an: number, konvoy?: boolean) => (
    <div style={{ position: "absolute", left: x, top: y, opacity: gir(t, an) * 0.85, translate: `${Math.sin((t + x) * 1.2) * 4}px 0` }}>
      {(konvoy ? [0, 1, 2] : [0]).map((j) => (
        <div key={j} style={{ position: "absolute", left: j * 120, top: -j * 26, width: 420, height: 200, background: "rgba(216,116,44,0.55)", border: "6px dashed rgba(255,255,255,0.7)", borderRadius: 16 }}>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 6, padding: 14, width: 300 }}>
            {Array.from({ length: kutu }, (_, i) => <div key={i} style={{ width: 40, height: 32, background: "#b98a52", border: "3px solid #111", borderRadius: 4 }} />)}
          </div>
        </div>
      ))}
      <div style={{ position: "absolute", left: 0, top: 220, width: 440, ...yaz(40, RENK.murekkep, "fredoka") }}>{lbl}</div>
    </div>
  );
  return (
    <Zemin t0={t0}>
      {uc ? (
        <>
          {kamyon(D ? 300 : 100, D ? 300 : 300, 0, "SMALLER SAVINGS: EMPTY", t0)}
          {kamyon(D ? 300 : 700, D ? 820 : 300, 6, "THE OKAFORS: 6 − SLICE", t0 + 0.4)}
          {kamyon(D ? 200 : 1200, D ? 1340 : 300, 10, "VERY WEALTHY: CONVOY", t0 + 0.8, true)}
        </>
      ) : (
        <>
          {kamyon(D ? 300 : 260, D ? 500 : 300, 10, "ANOTHER FAMILY: 0 BOXES TO CARE", t0)}
          {kamyon(D ? 300 : 1100, D ? 1050 : 300, 6, "ANOTHER FAMILY: 4 BOXES TO CARE", t0 + 0.4)}
          <div style={{ position: "absolute", left: D ? 90 : 640, top: D ? 1500 : 760, ...yaz(D ? 80 : 90, RENK.sari), opacity: gir(t, t0 + 1) }}>IT VARIES A LOT</div>
        </>
      )}
    </Zemin>
  );
};

export const Ikonlar: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const ads: [string, string][] = [["schools", "SCHOOLS"], ["hospitals", "HOSPITALS"], ["churches", "PLACES OF WORSHIP"], ["research", "RESEARCH"]];
  return (
    <Zemin t0={t0}>
      {ads.map(([w, lbl], i) => {
        const an = ka(k, w, t0 + i * 0.5);
        const x = D ? 90 + (i % 2) * 470 : 120 + i * 430, y = D ? 500 + Math.floor(i / 2) * 560 : 330;
        return (
          <div key={w} style={{ position: "absolute", left: x, top: y, width: 400, height: 420, background: "rgba(15,22,38,0.95)", border: `5px solid ${RENK.yesil}`, borderRadius: 22, opacity: gir(t, an), scale: String(0.8 + 0.2 * gir(t, an)), display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 30 }}>
            <div style={{ width: 160, height: 160, borderRadius: 30, background: RENK.yesil, border: "6px solid #111" }} />
            <div style={{ ...yaz(42, RENK.murekkep, "fredoka"), textAlign: "center", width: 360 }}>{lbl}</div>
          </div>
        );
      })}
    </Zemin>
  );
};

export const Sold: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "if", t0) + 0.6;
  const p = interpolate(t, [a, a + 0.14], [0, 1], CL);
  return (
    <Zemin t0={t0}>
      <Kutu tur="ev" x={D ? 540 : 960} y={D ? 1300 : 900} w={D ? 700 : 640} />
      <div style={{ position: "absolute", left: D ? 540 : 960, top: D ? 760 : 400, translate: "-50% -50%", rotate: "-10deg", scale: String(2 - p), opacity: p, padding: "10px 50px", border: `12px solid ${RENK.kirmizi}`, borderRadius: 20, background: "rgba(10,10,10,0.35)", ...yaz(160, RENK.kirmizi), WebkitTextStroke: "0px" }}>SOLD</div>
    </Zemin>
  );
};

export const Faturalar: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const ads: [string, string][] = [["agent", "AGENT FEES"], ["repairs", "REPAIRS"], ["property", "PROPERTY TAX & BILLS"]];
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: 0, right: 0, top: D ? 240 : 90, textAlign: "center", ...yaz(D ? 66 : 72), opacity: gir(t, t0) }}>SELLING HAS ITS OWN COSTS</div>
      {ads.map(([w, lbl], i) => {
        const an = ka(k, w, t0 + 0.3 + i * 0.6);
        const p = interpolate(t, [an, an + 0.4], [0, 1], { ...CL, easing: EOUT });
        return (
          <div key={w} style={{ position: "absolute", left: D ? 140 + i * 40 : 260 + i * 470, top: (D ? 420 + i * 420 : 300 + (i % 2) * 120) + (1 - p) * 300, width: D ? 760 : 460, padding: "40px 30px", background: "#f4f1ea", border: "6px solid #111", borderRadius: 14, rotate: `${(i - 1) * 6 + Math.sin(t * 2 + i) * 1.5}deg`, opacity: p, ...yaz(D ? 60 : 54, "#111"), WebkitTextStroke: "0px", textAlign: "center" }}>
            {lbl}
          </div>
        );
      })}
    </Zemin>
  );
};

export const Dilim: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const a = ka(k, "it", t0) + 0.1;
  const p = interpolate(t, [a, a + 0.5], [0, 1], { ...CL, easing: EOUT });
  const x = D ? 540 : 960, y = D ? 1250 : 860, w = D ? 640 : 600;
  return (
    <Zemin t0={t0}>
      <Kutu tur="ev" x={x - p * 30} y={y} w={w} />
      <div style={{ position: "absolute", left: x + w / 2 - 50 + p * 90, top: y - w * 0.78, width: 50, height: w * 0.78, background: `repeating-linear-gradient(45deg, ${KUTU_RENK.ev} 0 8px, #7a2e20 8px 16px)`, border: "5px solid #111", rotate: `${p * 8}deg` }} />
      <div style={{ position: "absolute", left: x + w / 2 + 80, top: y - w * 0.95, ...yaz(D ? 80 : 90, RENK.kahve), opacity: p }}>−A SLICE</div>
    </Zemin>
  );
};

export const Saat: React.FC<{ t0: number; k: Record<string, number>; yakin?: boolean }> = ({ t0, k, yakin }) => {
  const t = useT();
  const D = useDikey();
  const tik = Math.floor((t - ka(k, "clock", t0 + 1)) * 2);
  const aci = (Math.max(0, tik) * 6) % 360;
  const r = (yakin ? 1.5 : 1) * (D ? 300 : 280);
  return (
    <Zemin t0={t0} renk="#0a0f1c">
      <div style={{ position: "absolute", left: (D ? 540 : 960) - r, top: (D ? 900 : 540) - r, width: r * 2, height: r * 2, borderRadius: r, background: "#f4f1ea", border: "14px solid #111", boxShadow: "0 0 80px rgba(255,214,120,0.35)" }}>
        {Array.from({ length: 12 }, (_, i) => <div key={i} style={{ position: "absolute", left: r - 6, top: 14, width: 12, height: 36, background: "#111", transformOrigin: `6px ${r - 14}px`, rotate: `${i * 30}deg` }} />)}
        <div style={{ position: "absolute", left: r - 8, top: r * 0.25, width: 16, height: r * 0.75, background: RENK.kirmizi, transformOrigin: `8px ${r * 0.75}px`, rotate: `${aci}deg`, borderRadius: 8 }} />
        <div style={{ position: "absolute", left: r - 10, top: r * 0.45, width: 20, height: r * 0.55, background: "#111", transformOrigin: `10px ${r * 0.55}px`, rotate: `${aci / 12 + 120}deg`, borderRadius: 10 }} />
      </div>
    </Zemin>
  );
};

export const GriSac: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  const p = interpolate(t, [t0 + 0.6, t0 + 2.4], [0, 1], { ...CL, easing: EIO });
  const sac = `rgb(${Math.round(40 + 150 * p)},${Math.round(30 + 160 * p)},${Math.round(25 + 170 * p)})`;
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 140 : 560, top: D ? 360 : 140, padding: "16px 40px", background: "#f4f1ea", border: "6px solid #111", borderRadius: 12, ...yaz(D ? 80 : 84, "#111"), WebkitTextStroke: "0px", rotate: "-3deg" }}>TO: THE KIDS</div>
      <Siluet x={D ? 380 : 820} y={D ? 1400 : 960} h={D ? 640 : 560} renk="#26324d" sac={sac} />
      <Siluet x={D ? 700 : 1100} y={D ? 1400 : 960} h={D ? 600 : 520} renk="#26324d" sac={sac} />
      <div style={{ position: "absolute", left: D ? 140 : 1300, top: D ? 1480 : 500, ...yaz(D ? 60 : 64, RENK.sari), opacity: p }}>+ YEARS</div>
    </Zemin>
  );
};

export const YolIsareti: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const D = useDikey();
  return (
    <Zemin t0={t0}>
      <Tabela metin="STARTING OUT → FIRST HOME / BUSINESS" x={D ? 540 : 620} y={D ? 900 : 640} an={t0} s={D ? 0.55 : 0.6} />
      <Tabela metin="LATER → OWN RETIREMENT / OWN KIDS" x={D ? 540 : 1340} y={D ? 1500 : 900} an={ka(k, "money2", t0 + 2)} s={D ? 0.55 : 0.6} renk="#5a4a2a" />
    </Zemin>
  );
};

export const Tabelalar: React.FC<{ t0: number }> = ({ t0 }) => {
  const D = useDikey();
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: 0, right: 0, top: D ? 1250 : 820, height: D ? 300 : 200, background: "#2a2d36" }} />
      {DURAK.map(([ad], i) => (
        <Tabela key={ad} metin={`${i + 1} · ${ad}`} x={D ? 300 + (i % 2) * 480 : 170 + i * 316} y={D ? 560 + Math.floor(i / 2) * 340 : 800} an={t0 + i * 0.18} s={D ? 0.5 : 0.34} />
      ))}
    </Zemin>
  );
};

export const YolHaritasi: React.FC<{ t0: number; k: Record<string, number> }> = ({ t0, k }) => {
  const t = useT();
  const D = useDikey();
  const aC = ka(k, "if1", t0 + 1) + 0.4, aT = ka(k, "if2", t0 + 3) + 0.4;
  const pc = interpolate(t, [aC, aC + 0.6], [0, 1], { ...CL, easing: EOUT });
  const pt = interpolate(t, [aT, aT + 0.6], [0, 1], { ...CL, easing: EIO });
  return (
    <Zemin t0={t0}>
      <svg width={D ? 1080 : 1920} height={D ? 1920 : 1080} style={{ position: "absolute", left: 0, top: 0 }}>
        <path d={D ? "M 540 1800 C 200 1500, 900 1100, 540 700 S 540 300, 540 150" : "M 80 900 C 500 600, 900 1000, 1300 650 S 1800 500, 1880 300"} fill="none" stroke="#3a3f52" strokeWidth={70} strokeLinecap="round" />
        <path d={D ? "M 540 1800 C 200 1500, 900 1100, 540 700 S 540 300, 540 150" : "M 80 900 C 500 600, 900 1000, 1300 650 S 1800 500, 1880 300"} fill="none" stroke="rgba(255,214,120,0.7)" strokeWidth={8} strokeDasharray="40 30" />
      </svg>
      <Tabela metin="CARE" x={D ? 300 : 520} y={D ? 1420 : 700} an={t0} s={(D ? 0.5 : 0.45) * (1 + 0.35 * pc)} kesik={pc > 0.02} />
      <Tabela metin="TAX" x={(D ? 760 : 1400) + pt * 120} y={(D ? 820 : 560) - pt * 60} an={t0 + 0.2} s={D ? 0.5 : 0.45} kesik={pt > 0.02} />
    </Zemin>
  );
};

export const Etiket: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 540 : 960, top: D ? 900 : 520, translate: "-50% -50%", rotate: `${-4 + Math.sin(t * 1.5) * 1.2}deg`, padding: "40px 60px", background: "#f4f1ea", border: "8px solid #111", borderRadius: 18, textAlign: "center", opacity: gir(t, t0), scale: String(0.8 + 0.2 * gir(t, t0)) }}>
        <div style={{ ...yaz(D ? 110 : 130, "#111"), WebkitTextStroke: "0px" }}>FORECAST</div>
        <div style={{ ...yaz(D ? 52 : 60, "#444", "fredoka"), WebkitTextStroke: "0px" }}>CERULLI · DEC 2024</div>
      </div>
    </Zemin>
  );
};

export const SoruKutu: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  const salla = Math.sin((t - t0) * 9) * 4 * interpolate(t, [t0 + 0.2, t0 + 0.5, t0 + 1.4], [0, 1, 0.2], CL);
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: (D ? 540 : 960) - 260, top: (D ? 1000 : 600) - 400, width: 520, height: 400, background: "#b98a52", border: "8px solid #111", borderRadius: 12, rotate: `${salla}deg`, display: "flex", alignItems: "center", justifyContent: "center", ...yaz(260, RENK.sari), opacity: gir(t, t0) }}>?</div>
      <div style={{ position: "absolute", left: 0, right: 0, top: D ? 1100 : 660, textAlign: "center", ...yaz(D ? 80 : 90), opacity: gir(t, t0 + 0.2) }}>BIGGEST LEAK = ?</div>
    </Zemin>
  );
};

export const Soz: React.FC<{ t0: number; metin: string }> = ({ t0, metin }) => {
  const t = useT();
  const D = useDikey();
  return (
    <Zemin t0={t0}>
      <div style={{ position: "absolute", left: D ? 70 : 200, right: D ? 70 : 200, top: D ? 700 : 340, textAlign: "center", ...yaz(D ? 96 : 110), opacity: gir(t, t0), scale: String(0.9 + 0.1 * gir(t, t0)) }}>{metin}</div>
    </Zemin>
  );
};

// Tez: kamyonun yan yüzüne boyanır (S03 / S30)
export const Tez: React.FC<{ t0: number }> = ({ t0 }) => {
  const t = useT();
  const D = useDikey();
  const satir = ["AN INHERITANCE ISN'T A NUMBER.", "IT'S WHATEVER IS LEFT", "AT THE END OF A LONG ROAD."];
  return (
    <Zemin t0={t0} renk="#0d1a2e">
      <div style={{ position: "absolute", left: D ? 30 : 120, top: D ? 520 : 170, width: D ? 1020 : 1680, height: D ? 900 : 700, background: "#d8742c", border: "10px solid #111", borderRadius: 24 }} />
      {satir.map((s, i) => {
        const p = interpolate(t, [t0 + 0.15 + i * 0.7, t0 + 0.75 + i * 0.7], [0, 1], { ...CL, easing: EOUT });
        return (
          <div key={i} style={{ position: "absolute", left: D ? 70 : 200, top: (D ? 640 : 280) + i * (D ? 230 : 160), ...yaz(D ? 70 : 100, i === 0 ? "#f4f1ea" : RENK.sari), clipPath: `inset(0 ${100 - p * 100}% 0 0)`, whiteSpace: D ? "normal" : "nowrap", width: D ? 940 : undefined }}>{s}</div>
        );
      })}
    </Zemin>
  );
};

// Ekran yazısı katmanı (zaman.ts Ekran listesi; üst bant, ekran uzayı)
export const EkranYazilari: React.FC<{ liste: [number, string, number?, string?][] }> = ({ liste }) => {
  const t = useT();
  const D = useDikey();
  return (
    <>
      {liste.map(([an, metin, son, renk], i) => {
        if (t < an - 0.05 || (son !== undefined && t > son + 0.25)) return null;
        const p = gir(t, an);
        const q = son !== undefined ? interpolate(t, [son, son + 0.2], [1, 0], CL) : 1;
        return (
          <div key={i} style={{ position: "absolute", left: D ? 60 : 120, right: D ? 60 : 120, top: D ? 260 : 60, textAlign: "center", ...yaz(D ? 70 : 76, renk ?? RENK.murekkep), opacity: p * q, scale: String(0.7 + 0.3 * p) }}>
            {metin}
          </div>
        );
      })}
    </>
  );
};
