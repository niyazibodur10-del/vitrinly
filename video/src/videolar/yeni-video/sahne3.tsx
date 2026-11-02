import React from "react";
import { AbsoluteFill, interpolate } from "remotion";
import { Banknot, CizgiGrafik, CL, Damga, EOUT, Kart, RENK, Takvim, useT, Yazi } from "./kit";
import { anton, fredoka } from "./ortak";
import { Defter, Dolap, GrafikZemin, Kurgu, Nesne, OlcekSatiri, UstMasa, Zarf, ZARF_RENK } from "./masa";
import { Baslik, Gosterge, Hap, Ikon, Konveyor, LeoCekim, Sarmal, SayiKarti, Tik } from "./parca";
import { BuyukNot } from "./sahne2";
import { BORC_GSYH, BORC_GSYH_2026, DGS10, DTB3, NET_FAIZ, ORT_FAIZ } from "./veri-grafik";
import { plan } from "./zaman";

// Bölüm 4–5 (S13–S20). Rakamlar veri-grafik.ts'ten (rakam-tablosu.md + OMB T7.1).
const kesT = (id: string) => plan(id).kes!.map((c) => c[0]);
const yuzde = (v: number, d = 1) => `${v.toFixed(d)}%`;

// G5: halkın elindeki borç / GSYH (OMB T7.1, gerçekleşen FY1940–FY2023); 2026 noktası ayrı kaynak (FRED), çizgiye bağlanmaz
export const BorcGrafik: React.FC<{ an: number; sure: number; x?: number; y?: number; w?: number; h?: number; araliK?: [number, number]; nokta2026?: number; etiketler?: { y: number; an: number; metin: string; yon?: "ust" | "alt" | "sag" | "sol" }[] }> = ({
  an,
  sure,
  x = 210,
  y = 150,
  w = 1500,
  h = 560,
  araliK = [1940, 2027],
  nokta2026,
  etiketler = [],
}) => {
  const t = useT();
  const veri = BORC_GSYH.filter((d) => d.y >= araliK[0] && d.y <= Math.min(araliK[1], 2023));
  const noktalar = veri.map((d) => {
    const e = etiketler.find((q) => q.y === d.y);
    return { x: d.y, y: d.pct, etiket: e?.metin, etiketYon: e?.yon, an: e?.an };
  });
  const iw = w - 60, ih = h - 96 - 90;
  const X = (v: number) => 30 + ((v - araliK[0]) / (araliK[1] - araliK[0])) * iw;
  const Y = (v: number) => 40 + ih - (v / 130) * ih;
  const yil = araliK[1] - araliK[0] > 40 ? [1946, 1974, 2000, 2023] : [1946, 1960, 1974];
  return (
    <Kart an={-1} x={x} y={y} w={w} h={h}>
      <div style={{ position: "absolute", left: 40, top: 24, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.murekkep }}>Federal debt held by the public, % of GDP</div>
      <div style={{ position: "absolute", left: 0, top: 70 }}>
        <CizgiGrafik
          an={an}
          sure={sure}
          noktalar={noktalar}
          w={w}
          h={h - 96}
          xAralik={araliK}
          yAralik={[0, 130]}
          renk={RENK.mavi}
          kalin={6}
          alan
          eksenX={yil.map((v) => ({ x: v, etiket: String(v) }))}
          yatayCizgi={[{ y: 100, etiket: "100% = the whole economy" }]}
        />
        {nokta2026 !== undefined && t >= nokta2026 ? (
          <>
            <div style={{ position: "absolute", left: X(2026) - 13, top: Y(BORC_GSYH_2026) - 13, width: 26, height: 26, borderRadius: 13, background: RENK.kahve, border: `4px solid ${RENK.yuzey}`, scale: String(interpolate(t, [nokta2026, nokta2026 + 0.25], [2, 1], CL)) }} />
            <div style={{ position: "absolute", left: X(2026) - 330, top: Y(BORC_GSYH_2026) - 70, width: 310, textAlign: "right", fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.kahve }}>~{Math.round(BORC_GSYH_2026)}% (Q2 2026)</div>
          </>
        ) : null}
      </div>
      <div style={{ position: "absolute", left: 40, bottom: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 22, color: RENK.ikincil }}>
        <span style={{ color: RENK.mavi }}>━</span> OMB Historical Table 7.1 (actuals to FY2023){nokta2026 !== undefined ? <><span style={{ color: RENK.kahve, marginLeft: 26 }}>●</span> FRED FYGFGDQ188S (Q2 2026)</> : null}
      </div>
    </Kart>
  );
};

export const S13: React.FC = () => {
  const { k } = plan("S13");
  const K = kesT("S13");
  const t = useT();
  const maks = NET_FAIZ[NET_FAIZ.length - 1].v;
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S13" tip="orta" t0={K[0]} t1={K[1]} tohum={15} arka={<><Hap an={k.part} x={420} y={260} boyut={42}>SIZE OF THE LOAN</Hap><Hap an={k.rate0} x={1500} y={260} boyut={56} renk="#ffd43b">THE RATE ▲</Hap></>} on={<Zarf x={1560} y={830} w={320} renk="faiz" etiket="INTEREST" alt="$1,050 / MO" an={-1} giris="yok" donme={4} yaziBoy={56} />} />],
          [
            K[1],
            <GrafikZemin key="b">
              <Baslik an={K[1]} y={70} boyut={72}>
                AVERAGE RATE ON THE DEBT
              </Baslik>
              <SayiKarti an={k.early + 0.3} x={250} y={230} w={620} ust="EARLY 2022" deger={`~${yuzde(ORT_FAIZ.oca2022)}`} renk={RENK.yesil} />
              <div style={{ position: "absolute", left: 900, top: 330, fontFamily: anton, fontSize: 120, color: RENK.murekkep, opacity: interpolate(t, [k.sep, k.sep + 0.2], [0, 1], CL) }}>→</div>
              <SayiKarti an={k.sep + 0.3} x={1050} y={230} w={620} ust="SEP 2026" deger={`~${yuzde(ORT_FAIZ.eyl2026)}`} renk={ZARF_RENK.faiz} />
              <div style={{ position: "absolute", left: 0, width: 1920, top: 640, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.ikincil }}>Average interest rate, total marketable Treasury debt · Source: U.S. Treasury</div>
            </GrafikZemin>,
          ],
          [
            K[2],
            <GrafikZemin key="c">
              <Kart an={-1} x={210} y={110} w={1500} h={610}>
                <div style={{ position: "absolute", left: 50, top: 28, fontFamily: anton, fontSize: 54, color: RENK.murekkep }}>
                  THE INTEREST BILL: <span style={{ color: ZARF_RENK.faiz }}>~3× IN 5 YEARS</span>
                </div>
                {NET_FAIZ.map((d, i) => {
                  const p = interpolate(t, [k.just + 0.2 + i * 0.09, k.just + 0.6 + i * 0.09], [0, 1], { ...CL, easing: EOUT });
                  const bh = (d.v / maks) * 360 * p;
                  const son = i === NET_FAIZ.length - 1;
                  const vurgu = d.fy === 2021 || son;
                  const yan = son && t >= k.growing && Math.floor((t - k.growing) * 4) % 2 === 0;
                  return (
                    <div key={d.fy}>
                      <div style={{ position: "absolute", left: 70 + i * 128, top: 520 - bh, width: 92, height: bh, borderRadius: 6, background: vurgu ? ZARF_RENK.faiz : "#4b5875", opacity: yan ? 0.55 : 1 }} />
                      <div style={{ position: "absolute", left: 50 + i * 128, width: 132, top: 530, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 22, color: RENK.ikincil }}>FY{String(d.fy).slice(2)}</div>
                      {vurgu && t >= k.kitchen ? <div style={{ position: "absolute", left: 30 + i * 128, width: 172, top: 470 - bh, textAlign: "center", fontFamily: anton, fontSize: 40, color: RENK.murekkep }}>${Math.round(d.v).toLocaleString("en-US")}</div> : null}
                    </div>
                  );
                })}
                {t >= k.kitchen ? <div style={{ position: "absolute", left: 50, top: 90, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>per month in our kitchen ($1 a month = $1 billion a year)</div> : null}
              </Kart>
              <OlcekSatiri y={735} kaynak="US net interest, fiscal years 2016–2026 (Monthly Treasury Statement)" />
            </GrafikZemin>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S14: React.FC = () => {
  const { k } = plan("S14");
  const K = kesT("S14");
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S14" tip="yakin" t0={K[0]} t1={K[1]} pozlar={[[0, "C12"]]} tohum={16} />],
          [
            K[1],
            <GrafikZemin key="b">
              <Baslik an={K[1]} y={80} boyut={74}>
                MANY LOANS, ROLLING OVER
              </Baslik>
              <Konveyor an={K[1]} x={110} y={330} w={1700} degisim={k.replaced} />
              <Hap an={k.weeks} x={520} y={300} boyut={36}>SOME LAST WEEKS</Hap>
              <Hap an={k.decades} x={1400} y={300} boyut={36}>SOME LAST DECADES</Hap>
              <Yazi an={k.roll} x={420} y={640} boyut={54} renk={RENK.sari}>
                ROLL OVER, A FEW AT A TIME
              </Yazi>
              <Hap an={k.every} x={1500} y={560} boyut={34} renk="#f0d0cc">OLD CHEAP LOAN DUE</Hap>
              <Yazi an={k.replaced} x={1500} y={640} boyut={54} renk={ZARF_RENK.faiz}>
                CHEAP OUT → EXPENSIVE IN
              </Yazi>
            </GrafikZemin>,
          ],
          [
            K[2],
            <GrafikZemin key="c">
              <SayiKarti an={k.late + 0.2} x={250} y={180} w={680} ust="NEW 10-YEAR LOANS (late Oct 2026)" deger={`~${Math.round(DGS10)}%`} renk={ZARF_RENK.faiz} />
              <SayiKarti an={k.short} x={990} y={180} w={680} ust="SHORT-TERM BORROWING" deger={`~${Math.round(DTB3)}%`} renk={RENK.kahve} />
              <div style={{ position: "absolute", left: 0, width: 1920, top: 560, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.ikincil }}>Source: FRED DGS10 (10-year Treasury), DTB3 (3-month bill), Oct 29, 2026</div>
            </GrafikZemin>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S15: React.FC = () => {
  const { k } = plan("S15");
  const K = kesT("S15");
  const t = useT();
  const sira: [string, string][] = [["faiz", "INTEREST"], ["ss", "SOC. SEC."], ["medicare", "MEDICARE"], ["saglik", "HEALTH"], ["savunma", "DEFENSE"]];
  const one = interpolate(t, [k.and1 + 0.3, k.and1 + 0.9], [0, 1], { ...CL, easing: EOUT });
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Gosterge an={k.climbing - 0.4} x={960} y={420} etiket="AVERAGE RATE" />
              <Yazi an={k.climbing + 1.5} x={960} y={110} boyut={58} font="fredoka">
                …even with no new borrowing
              </Yazi>
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
              <BuyukNot an={K[1] + 0.15} renk="#ffd43b" yazi="#1b1b1b" boyut={86}>
                RATE × BALANCE
                <br />= INTEREST BILL
              </BuyukNot>
            </Dolap>,
          ],
          [
            K[2],
            <UstMasa
              key="c"
              kamera={[
                [K[2], 960, 620, 1.05],
                [K[3], 960, 620, 1.15],
              ]}
            >
              {sira.map(([r, e], i) => {
                const hedef = i === 0 ? 600 : 600 + i * 0;
                const x = i === 0 ? 1400 - one * 820 : 700 + i * 190;
                return <Zarf key={r} x={i === 0 ? x : x + one * 120} y={i === 0 ? hedef - one * 60 : 700} w={i === 0 ? 300 : 230} renk={r as never} etiket={e} an={-1} giris="yok" donme={(i - 2) * 3} yaziBoy={i === 0 ? 46 : 32} />;
              })}
              {t >= k.skip ? <Damga an={k.skip} x={580} y={380} metin="CAN'T SKIP" boyut={86} /> : null}
            </UstMasa>,
          ],
          [
            K[3],
            <LeoCekim
              key="d"
              id="S15"
              tip="orta"
              t0={K[3]}
              t1={K[3] + 7}
              tohum={17}
              arka={
                <div style={{ position: "absolute", left: 1450, top: 250, width: 420 }}>
                  <div style={{ fontFamily: anton, fontSize: 96, color: "#fff", WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill", textAlign: "center" }}>FAMILY?</div>
                  {t >= k.break ? (
                    <svg style={{ position: "absolute", left: 60, top: 0 }} width={300} height={130}>
                      <path d="M150,0 L135,40 L165,62 L140,96 L158,130" fill="none" stroke="#111" strokeWidth={9} strokeDasharray="200" strokeDashoffset={200 - 200 * interpolate(t, [k.break, k.break + 0.3], [0, 1], CL)} />
                    </svg>
                  ) : null}
                </div>
              }
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S16: React.FC = () => {
  const { k } = plan("S16");
  const K = kesT("S16");
  const t = useT();
  const adet = Math.floor(interpolate(t, [k.if + 0.4, k.inflation + 0.6], [1, 9], CL));
  const sepet = interpolate(t, [k.if + 0.4, k.inflation + 0.6], [1, 0.45], CL);
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Baslik an={0.15} y={90} boyut={88} renk={RENK.sari}>
                1 · IT BORROWS IN ITS OWN MONEY
              </Baslik>
              <Kart an={0.6} x={250} y={300} w={660} h={330}>
                <div style={{ padding: 34, fontFamily: anton, fontSize: 64, color: RENK.ikincil }}>A FAMILY</div>
                <div style={{ paddingLeft: 34, fontFamily: fredoka, fontWeight: 700, fontSize: 52, color: RENK.murekkep }}>borrows dollars it can&apos;t make</div>
              </Kart>
              <Damga an={k.currency} x={1340} y={720} metin="OWN CURRENCY ✓" renk={RENK.yesil} boyut={64} donme={-6} />
              <Yazi an={k.run} x={580} y={700} boyut={48} font="fredoka" renk={RENK.sari}>can&apos;t run out of dollars</Yazi>
              <Kart an={1.6} x={1010} y={300} w={660} h={330} cerceve={RENK.yesil}>
                <div style={{ padding: 34, fontFamily: anton, fontSize: 64, color: RENK.yesil }}>THIS HOUSEHOLD</div>
                <div style={{ paddingLeft: 34, fontFamily: fredoka, fontWeight: 700, fontSize: 52, color: RENK.murekkep }}>borrows in its own currency</div>
              </Kart>
            </GrafikZemin>,
          ],
          [
            K[1],
            <Dolap
              key="b"
              kamera={[
                [K[1], 1180, 470, 1.0],
                [K[2], 1180, 470, 1.08],
              ]}
            >
              <BuyukNot an={-1} renk="#ffd43b" yazi="#1b1b1b" boyut={84} donme={3}>
                WHY DO LENDERS KEEP SAYING YES?
              </BuyukNot>
              <Tik an={k.answered} x={1420} y={640} s={2.6} />
            </Dolap>,
          ],
          [K[2], <LeoCekim key="c" id="S16" tip="orta" t0={K[2]} t1={K[3]} pozlar={[[0, "C12"]]} tohum={18} />],
          [
            K[3],
            <GrafikZemin key="d">
              <Ikon ad="fotokopi" x={480} y={330} s={1.5} an={-1} />
              {Array.from({ length: adet }).map((_, i) => (
                <div key={i} style={{ position: "absolute", left: 230 + (i % 3) * 170, top: 560 + Math.floor(i / 3) * 50 }}>
                  <Banknot x={90} y={60} adet={1} s={0.85} donme={(i % 3) * 6 - 6} />
                </div>
              ))}
              <div style={{ position: "absolute", left: 1150, top: 300, width: 460, height: 360, display: "flex", alignItems: "flex-end", justifyContent: "center" }}>
                <div style={{ display: "flex", gap: 14, alignItems: "flex-end", scale: String(sepet), transformOrigin: "50% 100%" }}>
                  {["#e05a4f", "#ffd43b", "#2fae6a", "#c8955a"].map((r, i) => (
                    <div key={r} style={{ width: 80, height: 110 + i * 20, background: r, border: "5px solid #111", borderRadius: 10 }} />
                  ))}
                </div>
              </div>
              <div style={{ position: "absolute", left: 1120, top: 660, width: 520, height: 70, background: "#8a6a2a", border: "6px solid #111", borderRadius: 12 }} />
              <div style={{ position: "absolute", left: 1150, top: 750, width: 460, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.murekkep }}>what $1 buys</div>
              <Yazi an={k.inflation} x={960} y={110} boyut={100} renk={ZARF_RENK.faiz}>
                INFLATION
              </Yazi>
            </GrafikZemin>,
          ],
          [K[4], <LeoCekim key="e" id="S16" tip="yakin" t0={K[4]} t1={K[4] + 5} tohum={18} />],
        ]}
      />
      {/* Etkileşim anı (metin S16): sessiz alt köşe yazısı, 3 sn; ABONE ile çakışmaz */}
      {t >= k.answered + 0.8 && t < k.answered + 3.8 ? (
        <div style={{ position: "absolute", left: 40, top: 720, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: "#fff", background: "rgba(0,0,0,0.6)", padding: "8px 18px", borderRadius: 10, opacity: interpolate(t, [k.answered + 0.8, k.answered + 1.1, k.answered + 3.5, k.answered + 3.8], [0, 1, 1, 0], CL) }}>
          LIKE IF THE ENVELOPE TOWER SURPRISED YOU
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

export const S17: React.FC = () => {
  const { k } = plan("S17");
  const K = kesT("S17");
  const t = useT();
  const yillar: [number, string][] = Array.from({ length: 12 }).map((_, i) => [k.payday + i * 0.22, String(2026 + i * 7)]);
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Baslik an={0.15} y={90} boyut={88} renk={RENK.sari}>
                2 · IT NEVER RETIRES
              </Baslik>
              <Takvim x={750} y={250} w={420} adimlar={[[0, "∞"], ...yillar, [k.payday + 12 * 0.22, "∞"]]} altYazi="NO LAST PAYDAY" />
            </GrafikZemin>,
          ],
          [
            K[1],
            <LeoCekim
              key="b"
              id="S17"
              tip="orta"
              t0={K[1]}
              t1={K[2]}
              tohum={19}
              on={
                <>
                  {[0, 1, 2].map((i) => {
                    const d = Math.max(0, t - k.rolling - i * 0.35);
                    return (
                      <Nesne key={i} ad="G03-kagit" x={1380 + i * 140} y={820 - Math.sin(Math.min(d, 1) * Math.PI) * 180} w={130} an={k.rolling + i * 0.35 - 0.3} giris="pop" donme={d * 360}>
                        <div style={{ position: "absolute", top: 70, width: 130, textAlign: "center", fontFamily: anton, fontSize: 40, color: "#1d4f8a" }}>IOU</div>
                      </Nesne>
                    );
                  })}
                </>
              }
            />,
          ],
          [
            K[2],
            <GrafikZemin key="c">
              <div style={{ position: "absolute", left: 0, width: 1920, top: 260, textAlign: "center", fontFamily: anton, fontSize: 104, color: RENK.ikincil, WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill" }}>
                PAY IT ALL BACK?
                <div style={{ position: "absolute", left: 470, top: 70, height: 14, background: ZARF_RENK.faiz, width: 980 * interpolate(t, [k.back, k.back + 0.35], [0, 1], CL) }} />
              </div>
              <Yazi an={k.keep2} x={960} y={470} boyut={104} renk={RENK.sari}>
                KEEP PAYING THE INTEREST?
              </Yazi>
            </GrafikZemin>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S18: React.FC = () => {
  const { k } = plan("S18");
  const K = kesT("S18");
  const t = useT();
  const kadran = Math.sin(Math.max(0, t - k.tax) * 3) * 60 * (t >= k.tax ? 1 : 0);
  const kes = interpolate(t, [k.cut, k.cut + 0.5], [0, 1], CL);
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Baslik an={0.15} y={90} boyut={88} renk={RENK.sari}>
                3 · IT CAN GIVE ITSELF A RAISE
              </Baslik>
              <Zarf x={640} y={540} w={460} renk="diger" etiket="PAYCHECK" an={0.4} giris="pop" yaziBoy={60} />
              <div style={{ position: "absolute", left: 790, top: 360, width: 150, height: 150, borderRadius: 75, background: "#c9ccd6", border: "7px solid #111", rotate: `${kadran}deg`, opacity: t >= k.tax - 0.2 ? 1 : 0 }}>
                <div style={{ position: "absolute", left: 66, top: 8, width: 10, height: 56, background: ZARF_RENK.faiz, borderRadius: 5 }} />
              </div>
              {t >= k.tax ? <Hap an={k.tax} x={865} y={560} boyut={30}>TAX RATE ▲▼</Hap> : null}
              <Zarf x={1260} y={560} w={300} renk="ss" etiket="BILLS" an={0.6} giris="pop" yaziBoy={50} />
              <div style={{ position: "absolute", left: 1150 + kes * 140, top: 360 + kes * 120, rotate: `${-30 + kes * 40}deg`, opacity: t >= k.cut - 0.2 ? 1 : 0 }}>
                <Ikon ad="makas" x={100} y={100} s={1.1} />
              </div>
              {t >= k.cut ? <Hap an={k.cut} x={1260} y={760} boyut={30}>CUT ITS OWN BILLS</Hap> : null}
            </GrafikZemin>,
          ],
          [K[1], <LeoCekim key="b" id="S18" tip="yakin" t0={K[1]} t1={K[1] + 6} pozlar={[[0, "C12"], [k.roommate - 0.4, "balt"]]} tohum={20} arka={<Yazi an={K[1] + 0.3} x={1480} y={180} boyut={56} renk={RENK.ikincil}>VOTERS DECIDE</Yazi>} />],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S19: React.FC = () => {
  const { k } = plan("S19");
  const K = kesT("S19");
  const t = useT();
  const cub = (an: number, x: number, deger: number, etiket: string) => {
    const p = interpolate(t, [an, an + 0.6], [0, 1], { ...CL, easing: EOUT });
    const h = (deger / 343.7) * 330 * p;
    return (
      <>
        <div style={{ position: "absolute", left: x, top: 600 - h, width: 200, height: h, background: ZARF_RENK.borc, borderRadius: 8 }} />
        <div style={{ position: "absolute", left: x - 60, width: 320, top: 545 - h, textAlign: "center", fontFamily: anton, fontSize: 52, color: RENK.murekkep, opacity: p }}>${Math.round(deger)}B</div>
        <div style={{ position: "absolute", left: x - 60, width: 320, top: 615, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.ikincil }}>{etiket}</div>
      </>
    );
  };
  const buyu = interpolate(t, [k.paycheck - 0.2, k.paycheck + 0.8], [1, 1.7], { ...CL, easing: EOUT });
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S19" tip="orta" t0={K[0]} t1={K[1]} pozlar={[[0, "C12"]]} tohum={21} arka={<Yazi an={0.3} x={960} y={110} boyut={64}>THE DIFFERENCE IN THE DATA</Yazi>} />],
          [
            K[1],
            <GrafikZemin key="b">
              <Hap an={k.bigger} x={1300} y={90} boyut={40} renk="#ffd43b">BIGGER THAN THE WHOLE ECONOMY</Hap>
              <BorcGrafik
                an={k.n46 - 0.1}
                sure={k.quarter - k.n46 + 0.2}
                araliK={[1940, 1980]}
                etiketler={[
                  { y: 1946, an: k.n46, metin: ">100% (1946)", yon: "ust" },
                  { y: 1974, an: k.quarter, metin: "~23% (1974)", yon: "ust" },
                ]}
              />
            </GrafikZemin>,
          ],
          [
            K[2],
            <GrafikZemin key="c">
              <Baslik an={K[2]} y={70} boyut={70}>
                THE DEBT ITSELF GREW
              </Baslik>
              {cub(K[2] + 0.2, 560, 241.9, "1946")}
              {cub(k.grew, 1160, 343.7, "1974")}
              <div style={{ position: "absolute", left: 0, width: 1920, top: 700, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.ikincil }}>Debt held by the public, billions of dollars · Source: OMB Historical Table 7.1</div>
            </GrafikZemin>,
          ],
          [
            K[3],
            <UstMasa
              key="d"
              kamera={[
                [K[3], 960, 620, 1.05],
                [K[4], 960, 620, 1.12],
              ]}
            >
              <div style={{ position: "absolute", left: 0, top: 0, width: 1920, height: 1080 }}>
                <div style={{ position: "absolute", left: 700 - 210 * buyu, top: 640 - 180 * buyu, width: 420 * buyu }}>
                  <Zarf x={210 * buyu} y={180 * buyu} w={420 * buyu} renk="diger" etiket="PAYCHECK" an={-1} giris="yok" yaziBoy={60 * buyu} />
                </div>
              </div>
              <Defter x={1280} y={640} w={360} an={-1} giris="pop" donme={6} />
              <Yazi an={k.loan} x={1280} y={420} boyut={52} renk={RENK.ikincil}>
                THE LOAN STAYED
              </Yazi>
              <Yazi an={k.paycheck} x={700} y={300} boyut={52} renk={RENK.sari}>
                THE PAYCHECK GREW
              </Yazi>
            </UstMasa>,
          ],
          [K[4], <LeoCekim key="e" id="S19" tip="yakin" t0={K[4]} t1={K[4] + 5} tohum={21} />],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S20: React.FC = () => {
  const { k } = plan("S20");
  const K = kesT("S20");
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <BorcGrafik an={-1} sure={0.01} nokta2026={k.ninety} etiketler={[{ y: 1946, an: -1, metin: ">100%", yon: "ust" }, { y: 1974, an: -1, metin: "~23%", yon: "alt" }, { y: 2023, an: -1, metin: "97% (FY2023)", yon: "sol" }]} />
            </GrafikZemin>,
          ],
          [
            K[1],
            <GrafikZemin key="b">
              <Sarmal an={K[1] + 0.3} x={960} y={430} />
              <Yazi an={k.possibility} x={960} y={740} boyut={60} renk={RENK.sari}>
                SPIRAL? A POSSIBILITY, NOT A VERDICT
              </Yazi>
            </GrafikZemin>,
          ],
          [K[2], <LeoCekim key="c" id="S20" tip="orta" t0={K[2]} t1={K[3]} pozlar={[[0, "C12"]]} tohum={22} />],
          [
            K[3],
            <GrafikZemin key="d">
              <Baslik an={K[3]} y={80} boyut={80}>
                THREE REAL BRAKES
              </Baslik>
              <Ikon ad="fren" x={430} y={430} s={1.25} an={k.currency} etiket="OWN CURRENCY" />
              <Ikon ad="fren" x={960} y={430} s={1.25} an={k.years} etiket="LONG LOANS" />
              <Ikon ad="fren" x={1490} y={430} s={1.25} an={k.safest} etiket="LENDERS' TRUST" />
            </GrafikZemin>,
          ],
          [K[4], <LeoCekim key="e" id="S20" tip="yakin" t0={K[4]} t1={K[4] + 8} tohum={22} />],
        ]}
      />
    </AbsoluteFill>
  );
};


