import React from "react";
import { AbsoluteFill, interpolate } from "remotion";
import { Banknot, CL, Damga, EOUT, EPOP, Kart, RENK, Sayac, Takvim, useT, Yazi } from "./kit";
import { anton, fredoka } from "./ortak";
import { Defter, Dolap, G10_NOT, GrafikZemin, Kurgu, MasaSahne, Nesne, NotYazi, OlcekSatiri, para, UstMasa, Yapraklar, YatayCubuklar, Zarf, ZARF_RENK } from "./masa";
import { Baslik, Hap, Ikon, LeoCekim, SayiKarti, Terazi } from "./parca";
import { BUTCE } from "./veri-grafik";
import { plan } from "./zaman";

// Bölüm 1–3 (S02–S11). Kesme zamanları zaman.ts'ten (K[i]); sahne kodu sabit saniye taşımaz.
const kesT = (id: string) => plan(id).kes!.map((c) => c[0]);

// Büyük yapışkan not (buzdolabı yakın planı G10 üstünde, tez/soru notları)
export const BuyukNot: React.FC<{ an: number; x?: number; y?: number; w?: number; h?: number; renk?: string; yazi?: string; children: React.ReactNode; boyut?: number; donme?: number }> = ({
  an,
  x = 790,
  y = 170,
  w = 780,
  h = 600,
  renk = "#e05a4f",
  yazi = "#fff",
  children,
  boyut = 70,
  donme = -2,
}) => {
  const t = useT();
  if (t < an - 0.02) return null;
  const p = interpolate(t, [an, an + 0.18], [0, 1], { ...CL, easing: EPOP });
  return (
    <div style={{ position: "absolute", left: x, top: y, width: w, height: h, background: renk, border: "6px solid #1a1a1a", borderRadius: 8, boxShadow: "0 22px 40px rgba(0,0,0,0.5)", rotate: `${donme}deg`, scale: String(1.6 - 0.6 * p), opacity: Math.min(1, p * 3), display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center", padding: 40, boxSizing: "border-box", fontFamily: anton, fontSize: boyut, lineHeight: 1.12, color: yazi, letterSpacing: 1 }}>
      {children}
    </div>
  );
};

// Hesap makinesi (G07) + ekranda KOD rakam (B planı: G08 RED)
const HesapMakinesi: React.FC<{ x: number; y: number; w: number; deger: React.ReactNode }> = ({ x, y, w, deger }) => (
  <Nesne ad="G07-hesap-makinesi" x={x} y={y} w={w} giris="yok">
    <div style={{ position: "absolute", left: w * 0.15, top: w * 0.09, width: w * 0.7, height: w * 0.2, background: "#b9d8a8", borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "flex-end", paddingRight: 10, boxSizing: "border-box", fontFamily: anton, fontSize: w * 0.13, color: "#1d2a1a" }}>{deger}</div>
  </Nesne>
);

export const S02: React.FC = () => {
  const { k } = plan("S02");
  const K = kesT("S02");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S02" tip="orta" t0={K[0]} t1={K[1]} pozlar={[[0, "C12"]]} tohum={2} />],
          [
            K[1],
            <MasaSahne
              key="b"
              kamera={[
                [K[1], 960, 520, 1.25],
                [K[1] + 1.2, 300, 270, 2.0],
                [K[2], 290, 265, 2.08],
              ]}
              arka={
                <>
                  <Ikon ad="araba" x={210} y={330} s={0.45} an={k.car} />
                  <Ikon ad="ev" x={395} y={315} s={0.45} an={k.mortgages} />
                  <div style={{ position: "absolute", left: 120, top: 150, width: 360, textAlign: "center", fontFamily: anton, fontSize: 30, color: "#fff", WebkitTextStroke: "5px #0b0b0b", paintOrder: "stroke fill", opacity: interpolate(t, [k.starting - 0.2, k.starting + 0.1], [0, 1], CL) }}>
                    TREASURY RATE →<br />
                    CAR LOANS · MORTGAGES
                  </div>
                </>
              }
            />,
          ],
          [
            K[2],
            <Dolap
              key="c"
              kamera={[
                [K[2], 1180, 470, 1.0],
                [K[2] + 6, 1180, 460, 1.08],
              ]}
            >
              <NotYazi kutu={G10_NOT[0]} an={k.fastest} boyut={36}>
                FASTEST BILL?
              </NotYazi>
              <NotYazi kutu={G10_NOT[1]} an={k.why} boyut={52}>
                WHY?
              </NotYazi>
              {[2, 3, 4].map((i, j) => (
                <NotYazi key={i} kutu={G10_NOT[i]} an={k.three + j * 0.18} boyut={96}>
                  {"ABC"[j]}
                </NotYazi>
              ))}
            </Dolap>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S03: React.FC = () => {
  const { k } = plan("S03");
  const K = kesT("S03");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S03" tip="yakin" t0={K[0]} t1={K[1]} pozlar={[[0, "C12"]]} tohum={4} />],
          [
            K[1],
            <GrafikZemin key="b">
              <div style={{ position: "absolute", left: 0, width: 1920, top: 190, textAlign: "center", fontFamily: anton, color: RENK.murekkep, WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill" }}>
                <div style={{ fontSize: 120, opacity: interpolate(t, [K[1], K[1] + 0.2], [0, 1], CL) }}>$1 A MONTH HERE</div>
                <div style={{ fontSize: 110, color: RENK.sari, opacity: interpolate(t, [k.equals, k.equals + 0.2], [0, 1], CL), scale: String(interpolate(t, [k.equals, k.equals + 0.25], [1.4, 1], { ...CL, easing: EOUT })) }}>= $1 BILLION A YEAR</div>
              </div>
              <div style={{ position: "absolute", left: 0, width: 1920, top: 560, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: RENK.ikincil, opacity: interpolate(t, [k.these, k.these + 0.3], [0, 1], CL) }}>
                Real Treasury numbers · FY2026 (Oct 2025–Sep 2026) · Monthly Treasury Statement
              </div>
            </GrafikZemin>,
          ],
          [K[2], <LeoCekim key="c" id="S03" tip="genis" t0={K[2]} t1={K[3]} tohum={4} />],
          [
            K[3],
            <Dolap
              key="d"
              kamera={[
                [K[3], 1180, 470, 1.0],
                [K[4], 1180, 470, 1.12],
              ]}
            >
              <BuyukNot an={k.country + 0.1} boyut={74}>
                A COUNTRY ISN&apos;T A FAMILY.
                <br />
                BUT THE INTEREST BILL WORKS THE SAME WAY.
              </BuyukNot>
            </Dolap>,
          ],
          [K[4], <LeoCekim key="e" id="S03" tip="yakin" t0={K[4]} t1={K[4] + 6} tohum={4} />],
        ]}
      />
      <Yazi an={0.3} son={K[1] - 0.2} x={300} y={110} boyut={64} renk={RENK.sari}>
        LEO
      </Yazi>
      <Yazi an={0.45} son={K[1] - 0.2} x={300} y={190} boyut={34} font="fredoka">
        cartoon roommate · not an advisor
      </Yazi>
      {t >= K[2] ? (
        <div style={{ position: "absolute", left: 34, top: 30, fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.sari, background: "rgba(0,0,0,0.45)", padding: "6px 14px", borderRadius: 8 }}>$1 a month here = $1 billion a year</div>
      ) : null}
    </AbsoluteFill>
  );
};

export const S04: React.FC = () => {
  const { k } = plan("S04");
  const K = kesT("S04");
  const serit = (an: number, metin: string, y: number, renk: string) => (
    <Nesne ad="G03-kagit" x={1120} y={y} w={150} an={an} giris="kay" donme={-88}>
      <div style={{ position: "absolute", left: -150, top: 60, width: 450, rotate: "88deg", textAlign: "center", fontFamily: anton, fontSize: 40, color: renk }}>{metin}</div>
    </Nesne>
  );
  const sira: [string, string][] = [
    ["ss", "SOC. SEC."],
    ["medicare", "MEDICARE"],
    ["saglik", "HEALTH"],
    ["savunma", "DEFENSE"],
    ["diger", "OTHER"],
    ["faiz", "?"],
  ];
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <UstMasa
              key="a"
              kamera={[
                [K[0], 960, 600, 1.0],
                [K[1], 1000, 600, 1.12],
              ]}
            >
              <Zarf x={760} y={640} w={420} renk="diger" etiket="$5,400" alt="IN" an={k.five} giris="dus" donme={-4} yaziBoy={80} />
              {serit(k.paychecks, "PAYCHECK TAXES", 470, "#1d4f8a")}
              {serit(k.company, "COMPANY TAXES", 640, "#2f6b3a")}
              {serit(k.payroll, "PAYROLL TAXES", 810, "#7a3b8a")}
            </UstMasa>,
          ],
          [
            K[1],
            <LeoCekim
              key="b"
              id="S04"
              tip="genis"
              t0={K[1]}
              t1={K[1] + 10}
              pozlar={[[0, "a"], [k.spending, "C12"]]}
              tohum={6}
              on={
                <>
                  {sira.map(([r, e], i) => {
                    const kenar = i === 5 && t >= k.last;
                    return (
                      <Zarf key={r} x={kenar ? 1620 : 300 + i * 190} y={kenar ? 860 : 865 + (i % 2) * 14} w={180} renk={r as never} etiket={e} an={k.envelope + i * 0.12} giris="pop" donme={(i - 2.5) * 4} yaziBoy={26} />
                    );
                  })}
                </>
              }
            />,
          ],
        ]}
      />
      <Baslik an={k.payday} son={k.five + 1.2} y={60}>
        PAYDAY
      </Baslik>
    </AbsoluteFill>
  );
};

export const S05: React.FC = () => {
  const { k } = plan("S05");
  const K = kesT("S05");
  const t = useT();
  const B = BUTCE;
  const toplam = B.ss + B.medicare + B.saglik;
  const dilim = (an: number, deger: number, sol: number, renk: string, etiket: string) => {
    const p = interpolate(t, [an, an + 0.5], [0, 1], { ...CL, easing: EOUT });
    const W = 1300 / B.gelir;
    return (
      <div style={{ position: "absolute", left: 60 + sol * W, top: 150, width: deger * W * p, height: 120, background: renk, borderRight: "4px solid #0f1626" }}>
        {p > 0.9 ? <div style={{ position: "absolute", left: 14, top: 128, whiteSpace: "nowrap", fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.murekkep }}>{etiket}</div> : null}
      </div>
    );
  };
  const grafik = (
    <GrafikZemin>
      <Kart an={-1} x={230} y={150} w={1460} h={560}>
        <div style={{ position: "absolute", left: 60, top: 40, fontFamily: anton, fontSize: 56, color: RENK.murekkep }}>WHERE THE $5,400 GOES</div>
        <div style={{ position: "absolute", left: 60, top: 150, width: 1300, height: 120, border: "4px dashed rgba(255,255,255,0.4)", borderRadius: 8, boxSizing: "border-box" }} />
        <div style={{ position: "absolute", left: 1210, top: 110, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>$5,400 IN</div>
        {dilim(-1, B.ss, 0, ZARF_RENK.ss, `SOCIAL SECURITY ${para(B.ss)}`)}
        {dilim(k.medicare, B.medicare, B.ss, ZARF_RENK.medicare, "")}
        {dilim(k.health, B.saglik, B.ss + B.medicare, ZARF_RENK.saglik, "")}
        <div style={{ position: "absolute", left: 60, top: 330, display: "flex", gap: 40, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.murekkep }}>
          {t >= k.medicare ? <span style={{ color: ZARF_RENK.medicare }}>MEDICARE {para(B.medicare)}</span> : null}
          {t >= k.health ? <span style={{ color: ZARF_RENK.saglik }}>OTHER HEALTH {para(B.saglik)}</span> : null}
        </div>
        {t >= k.three ? (
          <div style={{ position: "absolute", left: 60, top: 400, fontFamily: anton, fontSize: 110, color: RENK.murekkep }}>
            <Sayac an={k.three + 0.3} sure={0.9} bas={0} bit={toplam} onEk="$" /> SPENT
          </div>
        ) : null}
      </Kart>
      <OlcekSatiri y={735} />
    </GrafikZemin>
  );
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <LeoCekim
              key="a"
              id="S05"
              tip="orta"
              t0={K[0]}
              t1={K[1]}
              tohum={8}
              on={
                <>
                  <Zarf x={350} y={830} w={320} renk="ss" etiket="SOCIAL SECURITY" alt={t >= k.about1 ? "$1,667 / MO" : undefined} an={k.social} giris="dus" donme={-5} yaziBoy={40} />
                  <HesapMakinesi x={1530} y={850} w={200} deger={t >= k.about1 ? <Sayac an={k.about1} sure={0.6} bas={0} bit={B.ss} /> : "0"} />
                </>
              }
            />,
          ],
          [K[1], <React.Fragment key="b">{grafik}</React.Fragment>],
          [
            K[2],
            <UstMasa
              key="c"
              kamera={[
                [K[2], 960, 620, 1.05],
                [K[3], 960, 620, 1.18],
              ]}
            >
              <Zarf x={800} y={700} w={440} renk="ss" etiket="SOCIAL SECURITY" an={-1} giris="yok" donme={-6} yaziBoy={44} />
              <Zarf x={880} y={640} w={420} renk="medicare" etiket="MEDICARE" an={-1} giris="yok" donme={5} yaziBoy={48} />
              <Zarf x={960} y={580} w={400} renk="saglik" etiket="OTHER HEALTH" alt="$1,026 / MO" an={k.health} giris="dus" donme={-3} yaziBoy={44} />
            </UstMasa>,
          ],
          [K[3], <React.Fragment key="d">{grafik}</React.Fragment>],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S06: React.FC = () => {
  const { k } = plan("S06");
  const K = kesT("S06");
  const t = useT();
  const B = BUTCE;
  const sirali = [
    { etiket: "SOCIAL SECURITY", deger: B.ss },
    { etiket: "MEDICARE", deger: B.medicare },
    { etiket: "INTEREST", deger: B.faiz, vurgu: true },
    { etiket: "OTHER HEALTH", deger: B.saglik },
    { etiket: "DEFENSE", deger: B.savunma },
  ];
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <UstMasa
              key="a"
              kamera={[
                [K[0], 960, 640, 1.05],
                [K[1], 960, 640, 1.2],
              ]}
            >
              <Zarf x={960} y={660} w={480} renk="savunma" etiket="DEFENSE" alt={t >= k.nine ? "$965 / MO" : undefined} an={Math.min(k.defense, 0.25)} giris="dus" donme={-3} yaziBoy={64} />
              <Hap an={k.ships} x={700} y={430} boyut={38} donme={-6}>SHIPS</Hap>
              <Hap an={k.planes} x={1230} y={440} boyut={38} donme={5}>PLANES</Hap>
              <Hap an={k.salaries} x={690} y={900} boyut={38} donme={4}>SALARIES</Hap>
              <Hap an={k.bases} x={1240} y={890} boyut={38} donme={-4}>BASES</Hap>
            </UstMasa>,
          ],
          [
            K[1],
            <LeoCekim
              key="b"
              id="S06"
              tip="orta"
              t0={K[1]}
              t1={K[2]}
              tohum={9}
              on={<Zarf x={1560} y={830} w={300} renk="faiz" etiket={t >= k.interest ? "INTEREST" : ""} alt={t >= k.about ? "$1,050 / MO" : undefined} an={k.five - 0.1} giris="kay" donme={4} yaziBoy={52} />}
            />,
          ],
          [
            K[2],
            <GrafikZemin key="c">
              <Kart an={-1} x={230} y={110} w={1460} h={600}>
                <div style={{ position: "absolute", left: 60, top: 34, fontFamily: anton, fontSize: 56, color: RENK.murekkep }}>
                  INTEREST = <span style={{ color: ZARF_RENK.faiz }}>3RD-BIGGEST BILL</span>
                </div>
                <div style={{ position: "absolute", left: 40, top: 140 }}>
                  <YatayCubuklar an={k.that + 0.2} veri={sirali} w={1380} maks={B.ss} satir={84} />
                </div>
              </Kart>
              <OlcekSatiri y={730} />
            </GrafikZemin>,
          ],
          [
            K[3],
            <UstMasa
              key="d"
              kamera={[
                [K[3], 960, 600, 1.05],
                [K[4], 960, 600, 1.15],
              ]}
            >
              <Zarf x={720} y={640} w={440 * (B.faiz / B.faiz)} renk="faiz" etiket="INTEREST" alt="$1,050" an={-1} giris="yok" donme={-3} yaziBoy={56} />
              <Zarf x={1230} y={660} w={440 * (B.savunma / B.faiz)} renk="savunma" etiket="DEFENSE" alt="$965" an={-1} giris="yok" donme={3} yaziBoy={52} />
              <Yazi an={k.read + 0.4} x={960} y={330} boyut={110} renk={ZARF_RENK.faiz}>
                INTEREST &gt; DEFENSE
              </Yazi>
            </UstMasa>,
          ],
          [
            K[4],
            <GrafikZemin key="e">
              <div style={{ position: "absolute", left: 0, width: 1920, top: 130, textAlign: "center", fontFamily: anton, fontSize: 90, color: RENK.murekkep, WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill" }}>
                1 IN 5 DOLLARS OF INCOME
              </div>
              {Array.from({ length: 5 }).map((_, i) => (
                <div key={i} style={{ position: "absolute", left: 150 + i * 330, top: 300, width: 330, height: 260, filter: i === 4 && t >= k.one ? "hue-rotate(-110deg) saturate(2.2)" : undefined, scale: String(i === 4 && t >= k.one ? interpolate(t, [k.one, k.one + 0.2], [1.25, 1.1], CL) : 1) }}>
                  <Banknot x={150} y={130} adet={1} s={1.35} />
                </div>
              ))}
              {t >= k.one ? (
                <div style={{ position: "absolute", left: 1470, top: 560, width: 330, textAlign: "center", fontFamily: anton, fontSize: 60, color: ZARF_RENK.faiz, WebkitTextStroke: "6px #0b0b0b", paintOrder: "stroke fill" }}>INTEREST</div>
              ) : null}
              <OlcekSatiri y={730} />
            </GrafikZemin>,
          ],
          [
            K[5],
            <LeoCekim
              key="f"
              id="S06"
              tip="yakin"
              t0={K[5]}
              t1={K[5] + 8}
              tohum={9}
              arka={
                <>
                  <Hap an={k.road} x={520} y={380} boyut={40} renk="#f0d0cc">NO ROAD</Hap>
                  <Hap an={k.check} x={520} y={480} boyut={40} renk="#f0d0cc">NO CHECK</Hap>
                  <Hap an={k.ship} x={520} y={580} boyut={40} renk="#f0d0cc">NO SHIP</Hap>
                </>
              }
            />,
          ],
        ]}
      />
      {t >= K[5] ? <Damga an={k.nothing} x={1390} y={330} metin="BUYS NOTHING" boyut={84} /> : null}
    </AbsoluteFill>
  );
};

export const S07: React.FC = () => {
  const { k } = plan("S07");
  const K = kesT("S07");
  const t = useT();
  const yerler: [keyof typeof k, string, number, number][] = [
    ["veterans", "VETERANS", 640, 420],
    ["roads", "ROADS", 1280, 420],
    ["food", "FOOD AID", 600, 640],
    ["science", "SCIENCE", 1330, 640],
    ["parks", "NATIONAL PARKS", 700, 880],
    ["courts", "COURTS", 1250, 880],
  ];
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <UstMasa
              key="a"
              kamera={[
                [K[0], 960, 640, 1.0],
                [K[1], 960, 640, 1.12],
              ]}
            >
              <Zarf x={960} y={650} w={520} renk="diger" etiket="EVERYTHING ELSE" alt={t >= k.about1 ? "~$1,600 / MO" : undefined} an={0.15} giris="dus" donme={2} yaziBoy={52} />
              {yerler.map(([w, e, x, y], i) => (
                <Hap key={e} an={k[w]} x={x} y={y} boyut={34} donme={(i % 2 ? 1 : -1) * 5}>
                  {e}
                </Hap>
              ))}
            </UstMasa>,
          ],
          [
            K[1],
            <GrafikZemin key="b">
              <Terazi an={k.out} x={960} y={60} sol={t >= k.out ? "~$7,400 OUT" : ""} sag={t >= k.in ? "$5,400 IN" : ""} />
              {t >= k.short ? (
                <Yazi an={k.short} x={960} y={60} boyut={96} renk={ZARF_RENK.faiz}>
                  −$2,000 / MO
                </Yazi>
              ) : null}
            </GrafikZemin>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S07"
              tip="orta"
              t0={K[2]}
              t1={K[2] + 7}
              tohum={10}
              odakX={900}
              on={<Defter x={470} y={850} w={330} an={k.loan - 0.15} acik={t >= k.loan + 0.4 ? 1 : 0} satir="+$2,000" />}
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S08: React.FC = () => {
  const { k } = plan("S08");
  const K = kesT("S08");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <LeoCekim
              key="a"
              id="S08"
              tip="orta"
              t0={K[0]}
              t1={K[1]}
              tohum={11}
              on={
                <>
                  <Defter x={480} y={850} w={340} an={-1} acik={interpolate(t, [k.open, k.open + 0.4], [0, 1], CL)} giris="pop" />
                  <Yapraklar an={k.decades} x={420} y={820} />
                </>
              }
            />,
          ],
          [
            K[1],
            <GrafikZemin key="b">
              <SayiKarti an={K[1] + 0.05} x={260} y={170} w={1400} ust="THE LOAN BALANCE (household scale)" deger={<Sayac an={k.balance + 0.4} sure={1.0} bas={0} bit={389000} onEk="~$" />} />
              {t >= k.real ? (
                <div style={{ position: "absolute", left: 260, top: 470, width: 1400, padding: "22px 34px", boxSizing: "border-box", background: "rgba(15,22,38,0.94)", border: "3px solid rgba(255,255,255,0.2)", borderRadius: 22, fontFamily: fredoka, fontWeight: 700, color: RENK.murekkep, fontSize: 40, opacity: interpolate(t, [k.real, k.real + 0.3], [0, 1], CL) }}>
                  Real scale: debt held by the public <span style={{ fontFamily: anton, fontSize: 64, color: RENK.sari }}>$32.43 TRILLION</span>
                  <div style={{ fontSize: 24, color: RENK.ikincil }}>Sep 30, 2026 · Source: U.S. Treasury, Debt to the Penny</div>
                </div>
              ) : null}
            </GrafikZemin>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S08"
              tip="yakin"
              t0={K[2]}
              t1={K[3]}
              pozlar={[[0, "C12"]]}
              tohum={11}
              arka={
                <Hap an={k.average} x={1450} y={300} boyut={38} renk="#d8f0d8">
                  ≈ 3–3.5% a year · not card rates
                </Hap>
              }
            />,
          ],
          [
            K[3],
            <UstMasa
              key="d"
              kamera={[
                [K[3], 960, 620, 1.05],
                [K[3] + 8, 960, 620, 1.15],
              ]}
            >
              <Nesne ad="G07-kumbara" x={720} y={640} w={330} an={K[3] + 0.1} giris="pop" />
              <Nesne ad="G07-kasa" x={1230} y={630} w={280} an={k.trust} giris="pop" />
              <Hap an={K[3] + 0.2} x={720} y={860} boyut={34}>GOVERNMENT</Hap>
              <Hap an={k.trust} x={1230} y={860} boyut={34}>TRUST FUNDS</Hap>
              {t >= k.pocket ? (
                <svg style={{ position: "absolute", left: 860, top: 470 }} width={240} height={120}>
                  <path d={`M10,80 Q120,${10} ${10 + 210 * interpolate(t, [k.pocket, k.pocket + 0.5], [0, 1], CL)},70`} fill="none" stroke="#ffd43b" strokeWidth={12} strokeLinecap="round" />
                </svg>
              ) : null}
              <Yazi an={k.trust + 0.4} x={960} y={330} boyut={60} renk={RENK.ikincil}>
                LEFT OUT: ONE POCKET → ANOTHER
              </Yazi>
            </UstMasa>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S09: React.FC = () => {
  const { k } = plan("S09");
  const K = kesT("S09");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S09" tip="yakin" t0={K[0]} t1={K[1]} tohum={12} arka={<Yazi an={0.1} x={1480} y={200} boyut={96} renk={RENK.sari}>~$389,000</Yazi>} />],
          [
            K[1],
            <GrafikZemin key="b">
              <div style={{ position: "absolute", left: 0, width: 1920, top: 80, textAlign: "center", fontFamily: anton, fontSize: 92, color: RENK.murekkep, WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill" }}>≈ 6 YEARS OF INCOME</div>
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} style={{ opacity: interpolate(t, [k.six + i * 0.28, k.six + i * 0.28 + 0.15], [0, 1], CL) }}>
                  <Takvim x={190 + i * 260} y={260} w={230} adimlar={[[0, `Y${i + 1}`]]} altYazi="$64,800" />
                </div>
              ))}
              {t >= k.nothing ? (
                <Yazi an={k.nothing} x={960} y={600} boyut={64} renk={ZARF_RENK.faiz}>
                  NO FOOD · NO RENT · NOTHING ELSE
                </Yazi>
              ) : null}
              <OlcekSatiri y={735} kaynak="Debt held by the public ÷ FY2026 revenue (Treasury) ≈ 6.0" />
            </GrafikZemin>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S09"
              tip="orta"
              t0={K[2]}
              t1={K[2] + 5}
              tohum={12}
              on={<Defter x={470} y={850} w={330} an={-1} acik={1} satir={t >= k.adding ? "+$2,000" : ""} giris="pop" />}
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S10: React.FC = () => {
  const { k } = plan("S10");
  const K = kesT("S10");
  const ikonlar: [keyof typeof k, string, string][] = [
    ["americans", "bono", "SAVINGS BONDS"],
    ["pension", "emekli", "PENSION FUNDS"],
    ["banks", "banka", "BANKS · INSURERS"],
    ["foreign", "kure", "FOREIGN GOV'TS"],
    ["federal", "fed", "THE FED"],
  ];
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S10" tip="orta" t0={K[0]} t1={K[1]} tohum={13} arka={<Yazi an={0.2} x={960} y={110} boyut={80}>WHO HOLDS THE LOAN?</Yazi>} />],
          [
            K[1],
            <GrafikZemin key="b">
              <Baslik an={K[1]} y={90} boyut={76}>
                NOT ONE BANK
              </Baslik>
              {ikonlar.map(([w, ad, e], i) => (
                <Ikon key={ad} ad={ad} x={260 + i * 350} y={440} s={1.05} an={k[w]} etiket={e} />
              ))}
            </GrafikZemin>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S10"
              tip="orta"
              t0={K[2]}
              t1={K[2] + 7}
              pozlar={[[0, "C12"]]}
              tohum={13}
              on={
                <Nesne ad="G03-kagit" x={1480} y={820} w={180} an={k.promise} giris="pop" donme={8}>
                  <div style={{ position: "absolute", top: 90, width: 180, textAlign: "center", fontFamily: anton, fontSize: 54, color: "#1d4f8a" }}>IOU</div>
                </Nesne>
              }
              arka={<Yazi an={k.treasury} x={960} y={110} boyut={70} renk={RENK.sari}>TREASURY BOND = A PROMISE</Yazi>}
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S11: React.FC = () => {
  const { k } = plan("S11");
  const K = kesT("S11");
  const t = useT();
  const form = (x: number, baslik: string) => (
    <div style={{ position: "absolute", left: x, top: 170, width: 560, height: 560, background: "#f3ecdc", border: "6px solid #1b1b1b", borderRadius: 12, boxShadow: "0 18px 30px rgba(0,0,0,0.5)" }}>
      <div style={{ padding: 30, fontFamily: anton, fontSize: 52, color: "#1b1b1b" }}>LOAN APPLICATION</div>
      <div style={{ paddingLeft: 30, fontFamily: fredoka, fontWeight: 700, fontSize: 36, color: "#444" }}>{baslik}</div>
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i} style={{ position: "absolute", left: 30, right: 30, top: 230 + i * 56, height: 4, background: "rgba(0,0,0,0.2)" }} />
      ))}
    </div>
  );
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              {form(300, "A REAL FAMILY")}
              {form(1060, "THIS HOUSEHOLD")}
              <Damga an={k.stop} x={580} y={500} metin="DENIED" boyut={110} />
              <Damga an={k.yes} x={1340} y={500} metin="APPROVED" renk="#2fae6a" boyut={100} donme={-8} />
            </GrafikZemin>,
          ],
          [
            K[1],
            <Dolap
              key="b"
              kamera={[
                [K[1], 1180, 470, 1.0],
                [K[2], 1180, 470, 1.1],
              ]}
            >
              <BuyukNot an={k.hold + 0.1} renk="#ffd43b" yazi="#1b1b1b" boyut={84} donme={3}>
                WHY DO LENDERS KEEP SAYING YES?
              </BuyukNot>
            </Dolap>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S11"
              tip="orta"
              t0={K[2]}
              t1={K[2] + 6}
              tohum={14}
              on={
                <>
                  <AbsoluteFill style={{ background: `radial-gradient(circle at 1560px 830px, rgba(0,0,0,0) 170px, rgba(0,0,0,${0.55 * interpolate(t, [k.strange, k.strange + 0.4], [0, 1], CL)}) 300px)` }} />
                  <Zarf x={1560} y={830} w={300} renk="faiz" etiket="5" an={-1} giris="yok" donme={4} yaziBoy={90} />
                </>
              }
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

