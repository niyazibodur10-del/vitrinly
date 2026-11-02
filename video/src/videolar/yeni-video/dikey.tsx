import React from "react";
import { AbsoluteFill, Img, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { Banknot, CL, Damga, EOUT, f, Kamera, KameraKare, Kart, Leo, PozAdim, RENK, RIG_T, Sayac, Takvim, useT, Yazi, YUZ_T } from "./kit";
import { Sunucu } from "./Sunucu";
import { Doku, anton, fredoka } from "./ortak";
import { Kurgu, Nesne, YatayCubuklar, Zarf, ZARF_RENK } from "./masa";
import { Hap, Ikon, Tik } from "./parca";
import { BorcGrafik } from "./sahne3";
import { BUTCE } from "./veri-grafik";
import { SAHNELER, SHORTS_EK } from "./veri-sahne";
import { AltyaziParca, kare } from "./Tam";
import { plan } from "./zaman";

// 9:16 (1080x1920) Shorts sahneleri (animasyon-yonetmeni) — kurgu-editoru keser, ek kayıtları (hook/kapanış) ekler.
// Güvenli alan: üst 192, alt 1536, sağ 918 px → yazı, yüz ve grafik bu kutuda. Altyazı alt=430 (≈1340–1490).
// Kural (1929 dersi): her kesmede grafik/nesne ≤1 sn'de girer; hiçbir an yalnız arka plan + altyazı değildir.
// G09 dikey mutfak: masa üstü y=1151, lamba alt kenarı ≈560 → Leo s=0.64 (kafa lambanın altında).
const W = 1080, H = 1920, MASA_D = 1151, LS = 0.64;
const kesT = (id: string) => plan(id).kes!.map((c) => c[0]);
const leoD = (cx: number, cy: number, s = LS, dy = 0) => {
  const yuzY = MASA_D + 90 - 750 * s + dy;
  return { x: 540 - 740 * s + cx * s, y: yuzY - 307 * s + cy * s };
};

const DMasa: React.FC<{ kamera: KameraKare[]; id?: string; pozlar?: PozAdim[]; on?: React.ReactNode; ust?: React.ReactNode; dy?: number; tohum?: number }> = ({ kamera, id, pozlar = [[0, "a"]], on, ust, dy = 0, tohum = 1 }) => (
  <AbsoluteFill>
    <Kamera kareler={kamera} w={W} h={H} ekranW={W} ekranH={H}>
      <Img src={f("G09.jpg")} style={{ position: "absolute", width: W, height: H }} />
      <div style={{ position: "absolute", left: 0, top: 0, width: W, height: MASA_D + 6, overflow: "hidden" }}>
        <Leo id={id} x={540} y={MASA_D + 90 - 750 * LS + dy} s={LS} pozlar={pozlar} tohum={tohum} />
      </div>
      <div style={{ position: "absolute", left: 0, top: MASA_D - 4, width: W, height: 26, background: "linear-gradient(rgba(0,0,0,0.28), rgba(0,0,0,0))" }} />
      {on}
    </Kamera>
    {ust}
  </AbsoluteFill>
);
// kamera kalıpları (dikey): orta / yakın Leo yüzüne
const kam = (tip: "orta" | "yakin", t0: number, t1: number): KameraKare[] =>
  tip === "orta"
    ? [
        [t0, 540, 960, 1.0],
        [t1, 540, 950, 1.06],
      ]
    : [
        [t0, 540, 860, 1.32],
        [t1, 540, 850, 1.42],
      ];

const DZemin: React.FC<{ children?: React.ReactNode }> = ({ children }) => {
  const t = useT();
  return (
    <AbsoluteFill>
      <Img src={f("G09.jpg")} style={{ position: "absolute", width: W, height: H, filter: "blur(18px) brightness(0.36) saturate(0.8)", scale: String(1.08 + t * 0.004) }} />
      {children}
    </AbsoluteFill>
  );
};
const DBaslik: React.FC<{ an: number; children: React.ReactNode; y?: number; boyut?: number; renk?: string }> = ({ an, children, y = 230, boyut = 76, renk = RENK.murekkep }) => (
  <Yazi an={an} x={490} y={y} boyut={boyut} renk={renk} genislik={800}>
    {children}
  </Yazi>
);
const D1: React.FC = () => (
  <div style={{ position: "absolute", left: 60, top: 200, width: 840, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, lineHeight: 1.25, color: RENK.ikincil, background: "rgba(0,0,0,0.45)", borderRadius: 10, padding: "6px 0" }}>
    <span style={{ color: RENK.sari }}>$1 a month here = $1 billion a year</span>
    <br />
    FY2026 (Oct 2025–Sep 2026), Monthly Treasury Statement
  </div>
);

// ---------- D-S06 ----------
const DS06: React.FC = () => {
  const { k } = plan("S06");
  const K = kesT("S06");
  const t = useT();
  const B = BUTCE;
  return (
    <Kurgu
      kesmeler={[
        [
          K[0],
          <DZemin key="a">
            <Zarf x={490} y={820} w={720} renk="savunma" etiket="DEFENSE" alt={t >= k.nine ? "$965 / MO" : undefined} an={Math.min(k.defense, 0.25)} giris="dus" donme={-3} yaziBoy={96} />
            <Hap an={k.ships} x={260} y={480} boyut={46} donme={-6}>SHIPS</Hap>
            <Hap an={k.planes} x={720} y={480} boyut={46} donme={5}>PLANES</Hap>
            <Hap an={k.salaries} x={260} y={1160} boyut={46} donme={4}>SALARIES</Hap>
            <Hap an={k.bases} x={720} y={1160} boyut={46} donme={-4}>BASES</Hap>
          </DZemin>,
        ],
        [
          K[1],
          <DMasa key="b" id="S06" tohum={9} kamera={kam("orta", K[1], K[2])} on={<Zarf x={300} y={1235} w={380} renk="faiz" etiket={t >= k.interest ? "INTEREST" : ""} alt={t >= k.about ? "$1,050 / MO" : undefined} an={k.five - 0.1} giris="kay" donme={-4} yaziBoy={60} />} />,
        ],
        [
          K[2],
          <DZemin key="c">
            <D1 />
            <DBaslik an={K[2]} y={330} boyut={70}>
              INTEREST = <span style={{ color: ZARF_RENK.faiz }}>3RD-BIGGEST BILL</span>
            </DBaslik>
            <div style={{ position: "absolute", left: 30, top: 600, scale: "1", transformOrigin: "0 0" }}>
              <YatayCubuklar an={K[2] + 0.05} arasi={0.08} veri={[{ etiket: "SOC. SECURITY", deger: B.ss }, { etiket: "MEDICARE", deger: B.medicare }, { etiket: "INTEREST", deger: B.faiz, vurgu: true }, { etiket: "OTHER HEALTH", deger: B.saglik }, { etiket: "DEFENSE", deger: B.savunma }]} w={880} maks={B.ss} satir={110} />
            </div>
          </DZemin>,
        ],
        [
          K[3],
          <DZemin key="d">
            <Zarf x={490} y={640} w={600} renk="faiz" etiket="INTEREST" alt="$1,050" an={K[3] + 0.05} giris="pop" donme={-3} yaziBoy={80} />
            <Zarf x={490} y={1080} w={600 * (B.savunma / B.faiz)} renk="savunma" etiket="DEFENSE" alt="$965" an={K[3] + 0.2} giris="pop" donme={3} yaziBoy={72} />
            <DBaslik an={k.read + 0.4} y={300} boyut={84} renk={ZARF_RENK.faiz}>
              INTEREST &gt; DEFENSE
            </DBaslik>
          </DZemin>,
        ],
        [
          K[4],
          <DZemin key="e">
            <DBaslik an={K[4]} y={330} boyut={84}>
              1 IN 5 DOLLARS OF INCOME
            </DBaslik>
            {Array.from({ length: 5 }).map((_, i) => (
              <div key={i} style={{ position: "absolute", left: 180, top: 560 + i * 150, width: 400, height: 140, filter: i === 4 && t >= k.one ? "hue-rotate(-110deg) saturate(2.2)" : undefined }}>
                <Banknot x={150} y={70} adet={1} s={1.35} />
              </div>
            ))}
            {t >= k.one ? <div style={{ position: "absolute", left: 560, top: 1180, fontFamily: anton, fontSize: 64, color: ZARF_RENK.faiz, WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill" }}>INTEREST</div> : null}
          </DZemin>,
        ],
        [
          K[5],
          <DMasa
            key="f"
            id="S06"
            tohum={9}
            kamera={kam("yakin", K[5], K[5] + 8)}
            ust={
              <>
                <Hap an={k.road} x={250} y={420} boyut={44} renk="#f0d0cc">NO ROAD</Hap>
                <Hap an={k.check} x={480} y={330} boyut={44} renk="#f0d0cc">NO CHECK</Hap>
                <Hap an={k.ship} x={720} y={420} boyut={44} renk="#f0d0cc">NO SHIP</Hap>
                <Damga an={k.nothing} x={490} y={1250} metin="BUYS NOTHING" boyut={96} />
              </>
            }
          />,
        ],
      ]}
    />
  );
};

// ---------- D-S12 (matruşka: kule dikeyde yükselir) ----------
const DS12: React.FC = () => {
  const { k } = plan("S12");
  const K = kesT("S12");
  const t = useT();
  const L = { dy: -40 };
  const ic = leoD(724, 590, LS, L.dy), dis = leoD(760, 850, LS, L.dy);
  const anlar = [K[4], k.i2, k.i3, k.i4, k.i5, k.i5 + 0.75];
  let y = 1180, w = 640;
  const kule = anlar.map((an, n) => {
    const o = { an, y, w, renk: (n % 2 === 0 ? "borc" : "faiz") as "borc" | "faiz" };
    y -= w * 0.5; w *= 0.8;
    return o;
  });
  const kameraKule: KameraKare[] = kule.map((m, i) => [m.an + (i ? 0.05 : 0), 540, Math.min(960, m.y + 120), 1 + 0.08 * i]);
  return (
    <Kurgu
      kesmeler={[
        [K[0], <DMasa key="a" id="S12" tohum={5} kamera={kam("orta", K[0], K[1])} on={<Zarf x={300} y={1235} w={380} renk="faiz" etiket="INTEREST" alt="$1,050 / MO" an={0.25} giris="kay" donme={-5} yaziBoy={60} />} />],
        [
          K[1],
          <DMasa
            key="b"
            id="S12"
            tohum={5}
            dy={L.dy}
            pozlar={[[0, "a"], [k.open, "G05k"]]}
            kamera={[
              [K[1], 540, 900, 1.3],
              [K[2], 540, 920, 1.4],
            ]}
            on={
              <>
                {t >= k.open ? <Yazi an={k.open + 0.1} x={dis.x} y={dis.y - 30} boyut={40} renk="#ffd9d4">INTEREST</Yazi> : null}
                <Yazi an={k.borrowed} x={ic.x} y={ic.y - 25} boyut={40} renk="#efe4ff">BORROWED</Yazi>
              </>
            }
          />,
        ],
        [
          K[2],
          <DZemin key="c">
            <D1 />
            <Kart an={K[2]} x={60} y={420} w={860} h={760}>
              <div style={{ position: "absolute", left: 40, top: 36, fontFamily: anton, fontSize: 66, color: RENK.murekkep }}>THE MONTHLY GAP ≈ $2,000</div>
              <div style={{ position: "absolute", left: 40, top: 190, width: 780, height: 140, borderRadius: 14, background: "#4b5875", overflow: "hidden" }}>
                <div style={{ width: `${(1051.8 / 1992.5) * 100 * interpolate(t, [k.half, k.half + 0.7], [0, 1], CL)}%`, height: "100%", background: ZARF_RENK.faiz }} />
              </div>
              {t >= k.half + 0.35 ? (
                <>
                  <div style={{ position: "absolute", left: 40, top: 380, fontFamily: anton, fontSize: 76, color: ZARF_RENK.faiz }}>INTEREST ≈ $1,050</div>
                  <div style={{ position: "absolute", left: 40, top: 490, fontFamily: anton, fontSize: 104, color: RENK.murekkep, lineHeight: 1.05 }}>
                    = <Sayac an={k.half + 0.35} sure={0.6} bas={0} bit={53} sonEk="%" />
                    <br />
                    OF THE GAP
                  </div>
                </>
              ) : null}
            </Kart>
          </DZemin>,
        ],
        [
          K[3],
          <DMasa
            key="d"
            id="S12"
            tohum={7}
            dy={L.dy}
            pozlar={[[0, "G05m"]]}
            kamera={[
              [K[3], 540, 900, 1.25],
              [K[4], 540, 910, 1.32],
            ]}
            on={
              <>
                <Yazi an={k.so1} x={dis.x} y={dis.y - 30} boyut={40} renk="#efe4ff">BORROWED</Yazi>
                <Yazi an={k.newm - 0.3} x={ic.x} y={ic.y - 25} boyut={40} renk="#ffd9d4">INTEREST</Yazi>
              </>
            }
          />,
        ],
        [
          K[4],
          <AbsoluteFill key="e">
            <DZemin />
            <Kamera kareler={kameraKule} w={W} h={H} ekranW={W} ekranH={H}>
              {kule.map((m, i) => {
                const cik = interpolate(t, [m.an, m.an + 0.3], [0, 1], { ...CL, easing: EOUT });
                const ust = i ? kule[i - 1] : m;
                return t >= m.an ? (
                  <Zarf key={i} x={490} y={ust.y + (m.y - ust.y) * cik} w={m.w} renk={m.renk} acik={!!kule[i + 1] && t >= kule[i + 1].an} etiket={m.renk === "faiz" ? "INTEREST" : "BORROWED"} an={m.an} giris={i ? "yok" : "pop"} donme={i % 2 ? 4 : -3} yaziBoy={m.w * 0.13} />
                ) : null;
              })}
            </Kamera>
          </AbsoluteFill>,
        ],
      ]}
    />
  );
};

// ---------- D-S19 (G5 dikey: çizgi ≤1 sn'de görünür) ----------
const DS19: React.FC = () => {
  const { k } = plan("S19");
  const K = kesT("S19");
  const t = useT();
  const buyu = interpolate(t, [k.paycheck - 0.2, k.paycheck + 0.8], [1, 1.5], { ...CL, easing: EOUT });
  const cub = (an: number, x: number, deger: number, etiket: string) => {
    const p = interpolate(t, [an, an + 0.6], [0, 1], { ...CL, easing: EOUT });
    const h = (deger / 343.7) * 560 * p;
    return (
      <>
        <div style={{ position: "absolute", left: x, top: 1180 - h, width: 260, height: h, background: ZARF_RENK.borc, borderRadius: 8 }} />
        <div style={{ position: "absolute", left: x - 40, width: 340, top: 1110 - h, textAlign: "center", fontFamily: anton, fontSize: 64, color: RENK.murekkep, opacity: p }}>${Math.round(deger)}B</div>
        <div style={{ position: "absolute", left: x - 40, width: 340, top: 1195, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: RENK.ikincil }}>{etiket}</div>
      </>
    );
  };
  return (
    <Kurgu
      kesmeler={[
        [K[0], <DMasa key="a" id="S19" tohum={21} pozlar={[[0, "C12"]]} kamera={kam("orta", K[0], K[1])} />],
        [
          K[1],
          <DZemin key="b">
            <DBaslik an={K[1]} y={250} boyut={64}>
              DEBT vs THE WHOLE ECONOMY
            </DBaslik>
            <BorcGrafik an={K[1] + 0.1} sure={k.quarter - K[1] + 0.1} x={40} y={430} w={880} h={820} araliK={[1940, 1980]} etiketler={[{ y: 1946, an: K[1] + 0.3, metin: ">100% (1946)", yon: "sag" }, { y: 1974, an: k.quarter, metin: "~23% (1974)", yon: "ust" }]} />
          </DZemin>,
        ],
        [
          K[2],
          <DZemin key="c">
            <DBaslik an={K[2]} y={300} boyut={80}>
              THE DEBT ITSELF GREW
            </DBaslik>
            {cub(K[2] + 0.1, 150, 241.9, "1946")}
            {cub(k.grew, 560, 343.7, "1974")}
            <div style={{ position: "absolute", left: 60, width: 860, top: 1270, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.ikincil }}>Debt held by the public · OMB Historical Table 7.1</div>
          </DZemin>,
        ],
        [
          K[3],
          <DZemin key="d">
            <div style={{ position: "absolute", left: 490 - 260 * buyu, top: 560 - 220 * buyu, width: 520 * buyu }}>
              <Zarf x={260 * buyu} y={220 * buyu} w={520 * buyu} renk="diger" etiket="PAYCHECK" an={K[3]} giris="pop" yaziBoy={74 * buyu} />
            </div>
            <DBaslik an={k.paycheck} y={260} boyut={64} renk={RENK.sari}>THE PAYCHECK GREW</DBaslik>
            <div style={{ position: "absolute", left: 300, top: 1000, width: 380, height: 270, background: "#5b3b9a", border: "7px solid #1b1b1b", borderRadius: 16, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: anton, fontSize: 58, color: "#f4ecff" }}>LOAN BOOK</div>
            <DBaslik an={k.loan} y={1300} boyut={52} renk={RENK.ikincil}>THE LOAN STAYED</DBaslik>
          </DZemin>,
        ],
        [K[4], <DMasa key="e" id="S19" tohum={21} kamera={kam("yakin", K[4], K[4] + 5)} />],
      ]}
    />
  );
};

// ---------- D-S16 ----------
const DS16: React.FC = () => {
  const { k } = plan("S16");
  const K = kesT("S16");
  const t = useT();
  const adet = Math.floor(interpolate(t, [k.if + 0.4, k.inflation + 0.6], [1, 9], CL));
  const sepet = interpolate(t, [k.if + 0.4, k.inflation + 0.6], [1, 0.45], CL);
  const kartStil = (renk: string): React.CSSProperties => ({ position: "absolute", left: 60, width: 860, padding: 36, boxSizing: "border-box", background: "rgba(15,22,38,0.94)", border: `3px solid ${renk}`, borderRadius: 22 });
  return (
    <Kurgu
      kesmeler={[
        [
          K[0],
          <DZemin key="a">
            <DBaslik an={0.1} y={260} boyut={80} renk={RENK.sari}>
              1 · IT BORROWS IN ITS OWN MONEY
            </DBaslik>
            <div style={{ ...kartStil("rgba(255,255,255,0.2)"), top: 640, opacity: interpolate(t, [0.4, 0.6], [0, 1], CL) }}>
              <div style={{ fontFamily: anton, fontSize: 66, color: RENK.ikincil }}>A FAMILY</div>
              <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 52, color: RENK.murekkep }}>borrows dollars it can&apos;t make</div>
            </div>
            <div style={{ ...kartStil(RENK.yesil), top: 960, opacity: interpolate(t, [1.2, 1.4], [0, 1], CL) }}>
              <div style={{ fontFamily: anton, fontSize: 66, color: RENK.yesil }}>THIS HOUSEHOLD</div>
              <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 52, color: RENK.murekkep }}>borrows in its own currency</div>
            </div>
          </DZemin>,
        ],
        [
          K[1],
          <DZemin key="b">
            <div style={{ position: "absolute", left: 110, top: 470, width: 760, height: 700, background: "#ffd43b", border: "7px solid #1a1a1a", borderRadius: 8, rotate: "3deg", display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center", padding: 40, boxSizing: "border-box", fontFamily: anton, fontSize: 92, lineHeight: 1.1, color: "#1b1b1b" }}>WHY DO LENDERS KEEP SAYING YES?</div>
            <Tik an={k.answered} x={760} y={1080} s={2.6} />
          </DZemin>,
        ],
        [K[2], <DMasa key="c" id="S16" tohum={18} pozlar={[[0, "C12"]]} kamera={kam("orta", K[2], K[3])} />],
        [
          K[3],
          <DZemin key="d">
            <Ikon ad="fotokopi" x={490} y={560} s={1.4} an={-1} />
            {Array.from({ length: adet }).map((_, i) => (
              <div key={i} style={{ position: "absolute", left: 160 + (i % 3) * 210, top: 760 + Math.floor(i / 3) * 60 }}>
                <Banknot x={90} y={60} adet={1} s={0.85} donme={(i % 3) * 6 - 6} />
              </div>
            ))}
            <div style={{ position: "absolute", left: 240, top: 980, width: 500, height: 280, display: "flex", alignItems: "flex-end", justifyContent: "center" }}>
              <div style={{ display: "flex", gap: 14, alignItems: "flex-end", scale: String(sepet), transformOrigin: "50% 100%" }}>
                {["#e05a4f", "#ffd43b", "#2fae6a", "#c8955a"].map((r, i) => (
                  <div key={r} style={{ width: 90, height: 120 + i * 22, background: r, border: "5px solid #111", borderRadius: 10 }} />
                ))}
              </div>
            </div>
            <div style={{ position: "absolute", left: 220, top: 1260, width: 540, height: 60, background: "#8a6a2a", border: "6px solid #111", borderRadius: 12 }} />
            <DBaslik an={k.inflation} y={260} boyut={100} renk={ZARF_RENK.faiz}>INFLATION</DBaslik>
          </DZemin>,
        ],
        [K[4], <DMasa key="e" id="S16" tohum={18} kamera={kam("yakin", K[4], K[4] + 5)} />],
      ]}
    />
  );
};

// ---------- D-S17 ----------
const DS17: React.FC = () => {
  const { k } = plan("S17");
  const K = kesT("S17");
  const t = useT();
  const yillar: [number, string][] = Array.from({ length: 12 }).map((_, i) => [k.payday + i * 0.22, String(2026 + i * 7)]);
  return (
    <Kurgu
      kesmeler={[
        [
          K[0],
          <DZemin key="a">
            <DBaslik an={0.1} y={260} boyut={84} renk={RENK.sari}>
              2 · IT NEVER RETIRES
            </DBaslik>
            <Takvim x={250} y={560} w={480} adimlar={[[0, "∞"], ...yillar, [k.payday + 12 * 0.22, "∞"]]} altYazi="NO LAST PAYDAY" />
          </DZemin>,
        ],
        [
          K[1],
          <DMasa
            key="b"
            id="S17"
            tohum={19}
            kamera={kam("orta", K[1], K[2])}
            on={
              <>
                {[0, 1, 2].map((i) => {
                  const d = Math.max(0, t - k.rolling - i * 0.35);
                  return (
                    <Nesne key={i} ad="G03-kagit" x={220 + i * 230} y={1230 - Math.sin(Math.min(d, 1) * Math.PI) * 200} w={150} an={k.rolling + i * 0.35 - 0.3} giris="pop" donme={d * 360}>
                      <div style={{ position: "absolute", top: 80, width: 150, textAlign: "center", fontFamily: anton, fontSize: 46, color: "#1d4f8a" }}>IOU</div>
                    </Nesne>
                  );
                })}
              </>
            }
          />,
        ],
        [
          K[2],
          <DZemin key="c">
            <div style={{ position: "absolute", left: 60, width: 860, top: 560, textAlign: "center", fontFamily: anton, fontSize: 104, color: RENK.ikincil, WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill" }}>
              PAY IT ALL BACK?
              <div style={{ position: "absolute", left: 40, top: 70, height: 14, background: ZARF_RENK.faiz, width: 780 * interpolate(t, [Math.min(k.back, K[2] + 0.6), Math.min(k.back, K[2] + 0.6) + 0.35], [0, 1], CL) }} />
            </div>
            <Yazi an={k.keep2} x={490} y={820} boyut={100} renk={RENK.sari} genislik={820}>
              KEEP PAYING THE INTEREST?
            </Yazi>
          </DZemin>,
        ],
      ]}
    />
  );
};

export const DIKEY_SAHNE: Record<string, React.FC> = { S06: DS06, S12: DS12, S16: DS16, S17: DS17, S19: DS19 };

export const DikeySahneComp: React.FC<{ id: string; altyazi?: boolean }> = ({ id, altyazi = true }) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  const B = DIKEY_SAHNE[id];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas)} />
      <B />
      <Doku />
      {altyazi ? <AltyaziParca ofs={s.bas} alt={430} boyut={62} genislik={760} /> : null}
    </AbsoluteFill>
  );
};

// ---------- Shorts ek kayıtları (hook / köprü / kapanış): konuşan Leo G09 + cümleye bağlı grafik ----------
export const DEk: React.FC<{ ek: "sh1" | "sh2"; altyazi?: boolean }> = ({ ek, altyazi = true }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const E = SHORTS_EK[ek];
  const c = E.cumleler;
  const ci = Math.max(0, c.findIndex((x, i) => t >= x.bas - 0.15 && (i + 1 >= c.length || t < c[i + 1].bas - 0.15)));
  const bas = (i: number) => Math.max(0, (c[i]?.bas ?? 0) - 0.15);
  // Leo ağız çizelgesi ek kaydın kendi Rhubarb'ı (SHORTS_EK[ek].agiz)
  const LeoEk: React.FC<{ kamera: KameraKare[]; on?: React.ReactNode; ust?: React.ReactNode }> = ({ kamera, on, ust }) => (
    <AbsoluteFill>
      <Kamera kareler={kamera} w={W} h={H} ekranW={W} ekranH={H}>
        <Img src={f("G09.jpg")} style={{ position: "absolute", width: W, height: H }} />
        <div style={{ position: "absolute", left: 0, top: 0, width: W, height: MASA_D + 6, overflow: "hidden" }}>
          <EkSunucu ek={ek} />
        </div>
        {on}
      </Kamera>
      {ust}
    </AbsoluteFill>
  );
  const sh1: [number, React.ReactNode][] = [
    [bas(0), <LeoEk key="a" kamera={kam("orta", 0, 6)} on={<Zarf x={300} y={1235} w={380} renk="faiz" etiket="INTEREST" alt="$1,050 / MO" an={1.2} giris="kay" donme={-5} yaziBoy={60} />} ust={<><Yazi an={0.1} x={490} y={260} boyut={66} genislik={820}>IF THE U.S. WERE A FAMILY…</Yazi><Yazi an={1.0} x={490} y={360} boyut={92} renk={RENK.sari}>$5,400 / MO IN</Yazi></>} />],
    [bas(1), <LeoEk key="b" kamera={kam("yakin", bas(1), bas(1) + 3)} ust={<Damga an={bas(1) + 0.9} x={490} y={330} metin="BUYS NOTHING" boyut={96} />} />],
    [bas(2), <LeoEk key="c" kamera={kam("orta", bas(2), bas(2) + 3)} ust={<Yazi an={bas(2) + 0.2} x={490} y={300} boyut={70} genislik={820} renk={RENK.sari}>FULL KITCHEN TABLE → LONG VIDEO</Yazi>} />],
  ];
  const sh2: [number, React.ReactNode][] = [
    [
      bas(0),
      <DZemin key="a">
        <DBaslik an={0.05} y={250} boyut={64}>DEBT vs THE WHOLE ECONOMY</DBaslik>
        <BorcGrafik an={0.1} sure={Math.max(0.5, (c[0]?.son ?? 4) - 0.4)} x={40} y={430} w={880} h={820} araliK={[1940, 1980]} etiketler={[{ y: 1946, an: 0.3, metin: ">100% (1946)", yon: "sag" }, { y: 1974, an: (c[0]?.son ?? 4) - 0.6, metin: "~23% (1974)", yon: "ust" }]} />
      </DZemin>,
    ],
    [bas(1), <LeoEk key="b" kamera={kam("orta", bas(1), bas(1) + 4)} ust={<Yazi an={bas(1) + 0.2} x={490} y={300} boyut={70} genislik={820}>THE ECONOMY GREW AROUND IT</Yazi>} />],
    [bas(2), <LeoEk key="c" kamera={kam("yakin", bas(2), bas(2) + 3)} ust={<Yazi an={bas(2) + 0.1} x={490} y={300} boyut={76} renk={RENK.sari} genislik={820}>1 · OWN MONEY</Yazi>} />],
    [bas(3), <LeoEk key="d" kamera={kam("orta", bas(3), bas(3) + 3)} ust={<Yazi an={bas(3) + 0.1} x={490} y={300} boyut={76} renk={RENK.sari} genislik={820}>2 · NEVER RETIRES</Yazi>} />],
    [bas(4), <LeoEk key="e" kamera={kam("yakin", bas(4), bas(4) + 3)} ust={<Yazi an={bas(4) + 0.1} x={490} y={300} boyut={70} genislik={820}>HISTORY, NOT A FORECAST</Yazi>} />],
  ];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f(ek === "sh1" ? "shorts-1-ek.wav" : "shorts-2-ek.wav")} />
      <Kurgu kesmeler={(ek === "sh1" ? sh1 : sh2).slice(0, Math.max(1, c.length))} />
      <Doku />
      {altyazi && c[ci] ? (
        <div style={{ position: "absolute", left: 160, width: 760, bottom: 430, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 58, color: "#fff", WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill", textTransform: "uppercase" }}>
          {c[ci].metin.replace(/\[(.+?)\]\(.+?\)/g, "$1")}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

// Ek kayıt için konuşan Leo (sahne kimliği yerine ek çizelgesi)
const EkSunucu: React.FC<{ ek: "sh1" | "sh2" }> = ({ ek }) => {
  const s = LS;
  const yuzY = MASA_D + 90 - 750 * s;
  return (
    <div style={{ position: "absolute", left: 540 - YUZ_T.x * s, top: yuzY - YUZ_T.y * s, scale: String(s), transformOrigin: "0 0" }}>
      <Sunucu cues={SHORTS_EK[ek].agiz} ofs={0} poz="a" tohum={ek === "sh1" ? 31 : 33} rig={RIG_T} />
    </div>
  );
};

