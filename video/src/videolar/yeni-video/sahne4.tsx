import React from "react";
import { AbsoluteFill, Img, interpolate } from "remotion";
import { Banknot, CL, EIO, EOUT, f, Kamera, RENK, useT, Yazi } from "./kit";
import { anton, fredoka } from "./ortak";
import { Dolap, G10_NOT, GrafikZemin, Kurgu, MasaSahne, NotYazi, UstMasa, Zarf, ZARF_RENK } from "./masa";
import { Baslik, Hap, Ikon, LeoCekim, SayiKarti, Tik, Yaris } from "./parca";
import { BuyukNot } from "./sahne2";
import { BorcGrafik } from "./sahne3";
import { ENF1946 } from "./veri-grafik";
import { plan } from "./zaman";

// Bölüm 6–7 (S21–S27)
const kesT = (id: string) => plan(id).kes!.map((c) => c[0]);

const ABC: [string, string][] = [
  ["A", "GROW"],
  ["B", "CHANGE THE ENVELOPES"],
  ["C", "LET PRICES RISE"],
];
const AbcNotlar: React.FC<{ anlar: number[]; luck?: number }> = ({ anlar, luck }) => (
  <>
    {ABC.map(([h, m], i) => (
      <NotYazi key={h} kutu={G10_NOT[[0, 2, 1][i]]} an={anlar[i]} boyut={30}>
        <div>
          <div style={{ fontFamily: anton, fontSize: 80, lineHeight: 0.9 }}>{h}</div>
          {m}
        </div>
      </NotYazi>
    ))}
    {luck !== undefined ? (
      <NotYazi kutu={G10_NOT[4]} an={luck} boyut={40} renk="#2f6b3a">
        + LUCK
      </NotYazi>
    ) : null}
  </>
);

export const S21: React.FC = () => {
  const { k } = plan("S21");
  const K = kesT("S21");
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S21" tip="orta" t0={K[0]} t1={K[1]} pozlar={[[0, "C12"]]} tohum={23} />],
          [
            K[1],
            <Dolap
              key="b"
              kamera={[
                [K[1], 1180, 470, 1.0],
                [K[1] + 4, 1180, 460, 1.08],
              ]}
            >
              <AbcNotlar anlar={[k.A, k.B, k.C]} />
            </Dolap>,
          ],
        ]}
      />
      <Baslik an={k.this2} y={60} boyut={58} renk={RENK.sari}>
        POSSIBILITIES, NOT A FORECAST
      </Baslik>
    </AbsoluteFill>
  );
};

export const S22: React.FC = () => {
  const { k } = plan("S22");
  const K = kesT("S22");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Baslik an={0.15} y={70} boyut={80} renk={RENK.sari}>
                A · GROW THE PAYCHECK
              </Baslik>
              <Yaris an={k.faster - 1.2} maas={[0.05, 0.85]} borc={[0.05, 0.45]} sure={2.6} />
            </GrafikZemin>,
          ],
          [
            K[1],
            <GrafikZemin key="b">
              <BorcGrafik an={K[1]} sure={1.6} araliK={[1940, 1980]} etiketler={[{ y: 1946, an: K[1], metin: ">100%", yon: "ust" }, { y: 1974, an: K[1] + 1.5, metin: "~23%", yon: "ust" }]} />
            </GrafikZemin>,
          ],
          [K[2], <LeoCekim key="c" id="S22" tip="yakin" t0={K[2]} t1={K[3]} tohum={24} arka={<Yazi an={k.catch} x={1470} y={190} boyut={70} renk={RENK.sari}>GROWTH vs RATE</Yazi>} />],
          [
            K[3],
            <GrafikZemin key="d">
              <Baslik an={K[3]} y={70} boyut={70}>
                IF THE RATE BEATS GROWTH…
              </Baslik>
              <Yaris an={K[3] + 0.2} maas={[0.05, 0.5]} borc={[0.05, 0.9]} sure={k.wins - K[3]} />
              {t >= k.fatter ? (
                <div style={{ position: "absolute", left: 1500, top: 120, scale: String(interpolate(t, [k.fatter, k.fatter + 0.6], [0.8, 1.25], { ...CL, easing: EOUT })) }}>
                  <Zarf x={150} y={120} w={300} renk="faiz" etiket="5" an={k.fatter} giris="pop" yaziBoy={80} />
                </div>
              ) : null}
            </GrafikZemin>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S23: React.FC = () => {
  const { k } = plan("S23");
  const K = kesT("S23");
  const zarflar: [string, string, keyof typeof k, string][] = [
    ["ss", "emekli", "retirees", "RETIREES"],
    ["saglik", "hasta", "patients", "PATIENTS"],
    ["savunma", "asker", "soldiers", "SOLDIERS"],
    ["diger", "ogrenci", "students", "STUDENTS"],
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
                [K[0], 960, 620, 1.0],
                [K[1], 960, 620, 1.1],
              ]}
            >
              {zarflar.map(([r], i) => (
                <Zarf key={r} x={690 + i * 180} y={650 + (i % 2) * 30} w={250} renk={r as never} an={0.2 + i * 0.1} giris="pop" donme={(i - 1.5) * 5} />
              ))}
              <Hap an={k.raise} x={720} y={420} boyut={40}>RAISE TAXES</Hap>
              <Hap an={k.cut} x={1220} y={420} boyut={40}>CUT SPENDING</Hap>
            </UstMasa>,
          ],
          [
            K[1],
            <UstMasa
              key="b"
              kamera={[
                [K[1], 960, 600, 1.05],
                [K[2], 960, 600, 1.12],
              ]}
            >
              {zarflar.map(([r, ikon, w, e], i) => (
                <React.Fragment key={r}>
                  <Zarf x={600 + i * 240} y={780} w={220} renk={r as never} acik an={-1} giris="yok" />
                  <Ikon ad={ikon} x={600 + i * 240} y={560} s={0.95} an={k[w]} etiket={e} />
                </React.Fragment>
              ))}
              <Yazi an={K[1] + 0.2} x={960} y={250} boyut={56}>
                EVERY ENVELOPE BELONGS TO SOMEBODY
              </Yazi>
            </UstMasa>,
          ],
          [K[2], <LeoCekim key="c" id="S23" tip="orta" t0={K[2]} t1={K[2] + 6} tohum={25} arka={<Yazi an={k.slow} x={1480} y={200} boyut={72} renk={ZARF_RENK.faiz}>SLOW AND LOUD</Yazi>} />],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S24: React.FC = () => {
  const { k } = plan("S24");
  const K = kesT("S24");
  const t = useT();
  const kucul = interpolate(t, [k.smaller, k.smaller + 1.6], [1.25, 0.6], { ...CL, easing: EIO });
  const fis = interpolate(t, [k.grocery, k.grocery + 1.4], [120, 520], { ...CL, easing: EOUT });
  const sis = interpolate(t, [k.fatter - 0.5, k.fatter + 0.5], [1, 1.45], { ...CL, easing: EOUT });
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <GrafikZemin key="a">
              <Baslik an={0.15} y={70} boyut={80} renk={RENK.sari}>
                C · LET PRICES RISE
              </Baslik>
              <div style={{ position: "absolute", left: 960 - 160 * kucul, top: 470 - 110 * kucul, scale: String(kucul), transformOrigin: "0 0" }}>
                <Banknot x={130} y={90} adet={5} s={1.9} />
              </div>
              <Yazi an={k.smaller} x={960} y={720} boyut={52} font="fredoka">
                old dollars paid back buy less
              </Yazi>
            </GrafikZemin>,
          ],
          [
            K[1],
            <GrafikZemin key="b">
              <SayiKarti an={K[1] + 0.1} x={460} y={200} w={1000} ust="1946 ALONE: CONSUMER PRICES" deger={t >= k.eighteen ? `+${Math.round(ENF1946)}%` : "…"} renk={ZARF_RENK.faiz} alt="Dec 1945 → Dec 1946 · Source: Shiller CPI (from BLS CPI-U)" />
            </GrafikZemin>,
          ],
          [
            K[2],
            <LeoCekim
              key="c"
              id="S24"
              tip="orta"
              t0={K[2]}
              t1={K[3]}
              tohum={26}
              on={
                <div style={{ position: "absolute", left: 1440, top: 840 - fis, width: 170, height: fis, background: "#f6f2ea", border: "5px solid #1b1b1b", borderRadius: 4, overflow: "hidden" }}>
                  {Array.from({ length: Math.floor(fis / 34) }).map((_, i) => (
                    <div key={i} style={{ height: 6, margin: "14px 16px", background: "rgba(0,0,0,0.25)" }} />
                  ))}
                </div>
              }
              arka={<Yazi an={k.grocery} x={1480} y={200} boyut={56}>GROCERY BILL ▲</Yazi>}
            />,
          ],
          [
            K[3],
            <LeoCekim
              key="d"
              id="S24"
              tip="orta"
              t0={K[3]}
              t1={K[3] + 9}
              tohum={26}
              on={
                <div style={{ position: "absolute", left: 1500 - 165 * sis, top: 860 - 140 * sis, width: 330 * sis }}>
                  <Zarf x={165 * sis} y={140 * sis} w={330 * sis} renk="faiz" etiket="INTEREST" an={-1} giris="yok" donme={4} yaziBoy={50 * sis} />
                </div>
              }
              arka={<Yazi an={k.fatter} x={600} y={160} boyut={52} renk={RENK.sari}>OLD DEBT SHRINKS · NEW RATES RISE</Yazi>}
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S25: React.FC = () => {
  const { k } = plan("S25");
  const K = kesT("S25");
  const t = useT();
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <Dolap
              key="a"
              kamera={[
                [K[0], 1180, 470, 1.0],
                [K[1], 1180, 470, 1.1],
              ]}
            >
              <AbcNotlar anlar={[-1, -1, -1]} luck={k.luck} />
            </Dolap>,
          ],
          [K[1], <LeoCekim key="b" id="S25" tip="yakin" t0={K[1]} t1={K[2]} pozlar={[[0, "C12"]]} tohum={27} />],
          [
            K[2],
            <GrafikZemin key="c">
              {["A", "B", "C"].map((h, i) => (
                <div key={h} style={{ position: "absolute", left: 420 + i * 400, top: 220, width: 280, height: 280, background: "#ffd43b", border: "7px solid #1b1b1b", borderRadius: 10, rotate: `${(i - 1) * 4}deg`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: anton, fontSize: 200, color: "#1b1b1b", opacity: interpolate(t, [k.A + 0.1 + i * 0.25, k.A + 0.3 + i * 0.25], [0, 1], CL) }}>
                  {h}
                </div>
              ))}
              <Yazi an={k.comments - 0.6} x={960} y={600} boyut={78} renk={RENK.sari}>
                ONE LETTER IN THE COMMENTS
              </Yazi>
            </GrafikZemin>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S26: React.FC = () => {
  const { k } = plan("S26");
  const K = kesT("S26");
  const t = useT();
  const isik = interpolate(t, [k.paper, k.abone + 1.2], [1, 0.35], CL);
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            K[0],
            <Dolap
              key="a"
              kamera={[
                [K[0], 1180, 470, 1.0],
                [K[1], 1180, 470, 1.1],
              ]}
            >
              <BuyukNot an={0.2} boyut={64} h={520}>
                A COUNTRY ISN&apos;T A FAMILY.
                <br />
                BUT THE INTEREST BILL WORKS THE SAME WAY.
              </BuyukNot>
              <div style={{ position: "absolute", left: 830, top: 720, display: "flex", gap: 22 }}>
                {([["money", "OWN MONEY"], ["retires", "NEVER RETIRES"], ["raise", "GIVES ITSELF A RAISE"]] as const).map(([w, e]) => (
                  <div key={w} style={{ position: "relative", padding: "10px 16px 10px 64px", background: "#f6f2ea", border: "5px solid #1b1b1b", borderRadius: 8, fontFamily: fredoka, fontWeight: 700, fontSize: 28, opacity: t >= k[w] ? 1 : 0 }}>
                    <Tik an={k[w]} x={34} y={28} s={0.45} />
                    {e}
                  </div>
                ))}
              </div>
            </Dolap>,
          ],
          [K[1], <LeoCekim key="b" id="S26" tip="yakin" t0={K[1]} t1={K[2]} tohum={28} arka={<Yazi an={K[1] + 0.6} x={1480} y={200} boyut={64} renk={RENK.sari}>RATE × BALANCE</Yazi>} />],
          [
            K[2],
            <MasaSahne
              key="c"
              kamera={[
                [K[2], 900, 560, 1.12],
                [k.abone + 2, 860, 560, 1.22],
              ]}
              isik={isik}
              leo={{ id: "S26", pozlar: [[0, "a"]], tohum: 28 }}
              on={
                <>
                  <div style={{ position: "absolute", left: 200, top: 700 }}>
                    <Zarf x={150} y={60} w={240} renk="borc" an={-1} giris="yok" donme={-12} />
                  </div>
                  <Zarf x={400} y={800} w={330} renk="faiz" etiket="INTEREST" alt="$1,050 / MO" an={-1} giris="yok" donme={-4} yaziBoy={50} />
                </>
              }
              arka={<Yazi an={k.military} x={600} y={250} boyut={50}>$1,050 / MO &gt; DEFENSE $965</Yazi>}
            />,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

export const S27: React.FC = () => {
  const { k } = plan("S27");
  const K = kesT("S27");
  const t = useT();
  const uc = interpolate(t, [k.where + 0.3, k.where + 3.2], [0, 1], { ...CL, easing: EIO });
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [K[0], <LeoCekim key="a" id="S27" tip="orta" t0={K[0]} t1={K[1]} tohum={29} />],
          [
            K[1],
            <Dolap
              key="b"
              kamera={[
                [K[1], 1180, 470, 1.0],
                [k.five, 1180, 470, 1.04],
                [k.five + 0.6, 1170, 430, 1.5],
              ]}
            >
              <NotYazi kutu={G10_NOT[2]} an={K[1]} boyut={70} renk="#b3261e">
                ~5%
              </NotYazi>
            </Dolap>,
          ],
          [
            K[2],
            <Kamera
              key="c"
              kareler={[
                [K[2], 700, 420, 1.15],
                [K[2] + 4, 330, 290, 1.75],
              ]}
            >
              <Img src={f("G01.jpg")} style={{ position: "absolute", width: 1920, height: 1080 }} />
              <div style={{ position: "absolute", left: 1560 - 1250 * uc, top: 330 - 60 * uc - Math.sin(uc * Math.PI) * 160, width: 130, height: 130, background: "#ffd43b", border: "5px solid #1b1b1b", borderRadius: 6, rotate: `${uc * 380}deg`, scale: String(1 - 0.45 * uc), display: "flex", alignItems: "center", justifyContent: "center", fontFamily: anton, fontSize: 56, color: "#b3261e" }}>~5%</div>
            </Kamera>,
          ],
        ]}
      />
    </AbsoluteFill>
  );
};

