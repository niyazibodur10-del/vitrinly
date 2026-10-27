import React from "react";
import { AbsoluteFill, interpolate, random } from "remotion";
import { fredoka, KapiIsik, kapiMerkezX } from "./ortak";
import {
  anlar, Banknot, CizgiGrafik, CL, CubukGrafik, Damga, EIO, EOUT, Harita, Illustration, Kamera, Kart, Kaynak, KAPI_RENK, Leo, Plaka, RENK, SahneKok, Sayac, useT, Yazi,
} from "./kit";
import { CPI29 } from "./veri-grafik";

// Bölüm 3 sonu – 5 (S11–S16): abone, Door Three: The Shoebox, The Bottom: July 1932

const ARKA_GRAFIK = "radial-gradient(ellipse at 50% 40%, #16223b 0%, #070b16 100%)";
const KAHVE_X = kapiMerkezX("kahve");

// Spot ışığı: ekranı karartır, (x, y) çevresi açık kalır
const Spot: React.FC<{ x: number; y: number; r: number; koyu?: number }> = ({ x, y, r, koyu = 0.62 }) => (
  <AbsoluteFill style={{ background: `radial-gradient(circle at ${x}px ${y}px, rgba(0,0,0,0) ${r * 0.55}px, rgba(0,0,0,${koyu}) ${r}px)`, pointerEvents: "none" }} />
);

// Abone düğmesi (3 sn, sessiz, logo animasyonu yok)
const Abone: React.FC<{ an: number }> = ({ an }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.3, an + 2.7, an + 3.0], [0, 1, 1, 0], CL);
  const tik = interpolate(t, [an + 1.0, an + 1.15, an + 1.3], [1, 0.9, 1], CL);
  const abone = t > an + 1.15;
  if (p <= 0) return null;
  return (
    <div style={{ position: "absolute", left: 60, bottom: 190, opacity: p, translate: `${(1 - p) * -60}px 0px`, display: "flex", alignItems: "center", gap: 16 }}>
      <div style={{ scale: String(tik), background: abone ? "#3a3a3a" : "#cc1f1f", color: "#fff", fontFamily: fredoka, fontWeight: 700, fontSize: 36, padding: "14px 30px", borderRadius: 40 }}>{abone ? "SUBSCRIBED" : "SUBSCRIBE"}</div>
      <svg width={50} height={70} style={{ opacity: interpolate(t, [an + 0.5, an + 0.8], [0, 1], CL) }}>
        <path d="M10,60 L10,20 L40,40 L28,42 L35,58 L28,61 L21,45 L10,60 Z" fill="#fff" stroke="#000" strokeWidth={3} />
      </svg>
    </div>
  );
};

// S11 · abone (kısa) + yeniden kanca: spot kahve kapıya, Box Leo kutuyu sallar
export const S11: React.FC = () => {
  const a = anlar("S11");
  const t = useT();
  const kapi = a("one", 2) - 0.2; // "One door is still closed"
  const spotP = interpolate(t, [a("now,"), kapi], [0, 1], { ...CL, easing: EIO });
  if (t < kapi) {
    return (
      <SahneKok>
        <Kamera kareler={[[0, 1047, 582, 1.1], [kapi, 1047, 582, 1.13]]}>
          <Plaka ad="C01" />
          <KapiIsik ad="mavi" an={-1} yaziHazir parlama={0} />
          <KapiIsik ad="yesil" an={-1} yaziHazir parlama={0} />
          <KapiIsik ad="kahve" an={-1} yaziHazir parlama={0} />
        </Kamera>
        <Leo id="S11" x={1640} y={352} s={1.0} pozlar={[[0, "a"]]} tohum={11} />
        {spotP > 0 ? <Spot x={interpolate(spotP, [0, 1], [1640, 960 + (KAHVE_X - 1047) * 1.1])} y={480} r={interpolate(spotP, [0, 1], [900, 380])} koyu={0.65 * spotP} /> : null}
        <Abone an={a("if") - 0.2} />
      </SahneKok>
    );
  }
  const salla = t > a("something") ? Math.sin((t - a("something")) * 14) * 5 * interpolate(t, [a("something"), a("something") + 0.3], [0, 1], CL) : 0;
  return (
    <SahneKok>
      <Kamera kareler={[[kapi, KAHVE_X, 500, 1.7], [17.2, KAHVE_X, 490, 1.8]]}>
        <Plaka ad="C01" />
        <KapiIsik ad="kahve" an={kapi} yaziHazir />
      </Kamera>
      <Spot x={960} y={520} r={760} koyu={0.55} />
      <div style={{ position: "absolute", left: 0, top: 0, width: 1920, height: 1080, rotate: `${salla}deg`, transformOrigin: "960px 1080px" }}>
        <Leo x={960} y={400} s={0.85} pozlar={[[0, "C14"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} giris={{ an: a("box") - 0.2, dy: 600, sure: 0.4 }} />
      </div>
      <Yazi an={kapi + 0.1} x={1560} y={330} boyut={100} renk={KAPI_RENK.kahve}>DOOR 3</Yazi>
      <Yazi an={a("laughed")} son={a("he") - 0.1} x={1520} y={470} boyut={44} font="fredoka">THE ONE EVERYBODY LAUGHED AT</Yazi>
      <Yazi an={a("something")} x={960} y={600} boyut={150} renk={RENK.sari} salla>?</Yazi>
    </SahneKok>
  );
};

// S12 · aynı deste her sabah; vitrinde etiketler küçülür; G3 TÜFE; $1,000 ≈ $1,272; Box Leo güçlenir
export const S12: React.FC = () => {
  const a = anlar("S12");
  const t = useT();
  const vitrin = a("but") - 0.2;
  const g3 = a("the", 4) - 0.2; // "The official price index"
  const tile = a("so") - 0.2;
  const son = a("box", 3) - 0.2; // "Box Leo did nothing"
  const veri = CPI29.filter((p) => p.ay <= "1932-07").map((p) => ({ x: p.x, y: p.y }));
  const ilk = veri[0], tem = veri[veri.length - 1];
  const yuzde = Math.round(((tem.y - ilk.y) / ilk.y) * 1000) / 10; // −21.4 [H]
  const alim = Math.round((1000 * ilk.y) / tem.y); // 1,272 [H]
  if (t < vitrin) {
    return (
      <SahneKok>
        <Kamera kareler={[[0, KAHVE_X, 560, 1.75], [vitrin, KAHVE_X, 540, 1.8]]}>
          <Plaka ad="C01" />
        </Kamera>
        <Leo x={760} y={400} s={0.85} pozlar={[[0, "C14"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} />
        <Banknot x={1420} y={560} adet={8} s={1.3} />
        <Yazi an={a("thousand")} x={1420} y={300} boyut={96} renk={RENK.sari}>$1,000</Yazi>
        <Yazi an={a("same")} x={1420} y={760} boyut={46} font="fredoka">SAME STACK. EVERY MORNING.</Yazi>
      </SahneKok>
    );
  }
  if (t < g3 || t >= son) {
    // vitrin C19: genel fiyat etiketleri (ürün fiyatı iddiası yok) tek tek küçülür
    const kucul = a("falling.");
    const etiket: [number, number][] = [[620, 330], [900, 320], [1180, 330], [1460, 320], [700, 470], [1000, 480], [1300, 470], [1600, 480], [820, 610], [1120, 620], [1420, 610]];
    return (
      <SahneKok>
        <Kamera kareler={t < g3 ? [[vitrin, 1300, 520, 1.02], [g3, 1450, 470, 1.1]] : [[son, 1200, 520, 1.04], [33.5, 1150, 520, 1.08]]}>
          <Plaka ad="C19" />
          {t < g3
            ? etiket.map(([x, y], i) => {
                const k = interpolate(t, [kucul + i * 0.18, kucul + i * 0.18 + 0.5], [1, 0.55], { ...CL, easing: EOUT });
                return (
                  <div key={i} style={{ position: "absolute", left: x, top: y, width: 84, height: 54, scale: String(k), background: "#f6f0e2", border: "3px solid #3a2a12", borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 30, color: "#3a2a12", rotate: `${(i % 3) * 4 - 4}deg` }}>
                    $
                  </div>
                );
              })
            : null}
        </Kamera>
        {t < g3 ? (
          <>
            <Yazi an={a("prices")} x={560} y={150} boyut={96} renk={RENK.sari}>PRICES ARE FALLING</Yazi>
            <Yazi an={a("average")} x={560} y={270} boyut={44} font="fredoka">THE AVERAGE PRICE OF WHAT FAMILIES BUY</Yazi>
          </>
        ) : (
          <>
            <Leo x={560} y={400} s={0.85} pozlar={[[0, "f"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} giris={{ an: son, dy: 500, sure: 0.35 }} />
            <Banknot x={1000} y={760} adet={8} s={1.0} parilti={interpolate(t, [a("stronger."), a("stronger.") + 0.4], [0, 1], CL)} />
            <Yazi an={a("stronger.")} x={1380} y={180} boyut={86} renk={RENK.sari}>STRONGER MONEY</Yazi>
          </>
        )}
        <Illustration />
      </SahneKok>
    );
  }
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      {t < tile ? (
        <Kart an={g3} x={260} y={120} w={1400} h={680}>
          <div style={{ position: "absolute", left: 36, top: 20, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>U.S. CONSUMER PRICE INDEX, MONTHLY (1982–84 = 100)</div>
          <div style={{ position: "absolute", left: 20, top: 70 }}>
            <CizgiGrafik
              an={a("from")}
              sure={a("thirty-two,") - a("from") + 0.4}
              w={1360}
              h={590}
              xAralik={[1929.6, 1932.65]}
              yAralik={[12, 18]}
              renk={RENK.kahve}
              alan
              noktalar={veri.map((p, i) => (i === 0 ? { ...p, etiket: "SEPT 1929: 17.3", etiketYon: "sag" as const } : i === veri.length - 1 ? { ...p, etiket: "JULY 1932: 13.6", etiketYon: "sol" as const } : p))}
              eksenX={[1930, 1931, 1932].map((v) => ({ x: v, etiket: String(v) }))}
            />
          </div>
          <Yazi an={a("twenty-one")} x={760} y={150} boyut={120} renk={RENK.sari}>{`PRICES ${Math.round(yuzde)}%`}</Yazi>
          <Yazi an={a("twenty-one") + 0.2} x={760} y={290} boyut={40} font="fredoka">SEPT 1929 → JULY 1932</Yazi>
        </Kart>
      ) : (
        <Kart an={tile} x={460} y={200} w={1000} h={520}>
          <div style={{ position: "absolute", width: "100%", top: 50, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 44, color: RENK.ikincil }}>SAME $1,000 NOW BUYS LIKE</div>
          <div style={{ position: "absolute", width: "100%", top: 130, textAlign: "center", fontFamily: "Anton", fontSize: 230, color: RENK.sari, lineHeight: 1 }}>
            <Sayac an={a("one")} sure={a("dollars", 3) - a("one") + 0.2} bas={1000} bit={alim} onEk="$" />
          </div>
          <div style={{ position: "absolute", width: "100%", top: 400, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: RENK.murekkep }}>IN 1929 PRICES</div>
        </Kart>
      )}
      <Kaynak metin="Source: BLS CPI via FRED (CPIAUCNS)" an={g3} />
    </SahneKok>
  );
};

// S13 · neden? iş kaybı + para arzı −~30% (G3b); "Here's the strange part"; bir ülke dolusu kutu
export const S13: React.FC = () => {
  const a = anlar("S13");
  const t = useT();
  const g3b = a("federal") - 0.2;
  const garip = a("here's") - 0.15;
  const harita = a("while") - 0.2;
  if (t < harita) {
    return (
      <SahneKok>
        <Kamera kareler={[[0, 1000, 540, 1.04], [garip, 1060, 540, 1.06], [garip + 0.35, 700, 400, 1.14], [harita, 700, 400, 1.15]]}>
          <Plaka ad="C03" filtre={t >= g3b && t < garip ? "blur(6px) brightness(0.5)" : undefined} />
          {t < g3b ? (
            <div style={{ position: "absolute", left: 829, top: 189, width: 931, height: 444 }}>
              <Yazi an={a("why")} x={465} y={30} boyut={70} renk={RENK.sari}>WHY WERE PRICES FALLING?</Yazi>
              <Yazi an={a("fewer")} x={465} y={150} boyut={50} font="fredoka">FEWER JOBS → LESS SPENDING</Yazi>
              <Yazi an={a("money")} x={465} y={240} boyut={50} font="fredoka">MONEY ITSELF WAS SHRINKING</Yazi>
            </div>
          ) : null}
        </Kamera>
        {t >= g3b && t < garip ? (
          <Kart an={g3b} x={760} y={140} w={1000} h={640}>
            <div style={{ position: "absolute", left: 36, top: 20, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>U.S. MONEY SUPPLY (fall 1930 = 100)</div>
            <div style={{ position: "absolute", left: 120, top: 70 }}>
              <CubukGrafik an={a("supply")} arasi={a("winter") - a("supply")} w={760} h={480} maks={110} renk={RENK.yesil} veri={[{ etiket: "FALL 1930", deger: 100, ustYazi: "100" }, { etiket: "WINTER 1933", deger: 70, ustYazi: "~70" }]} />
            </div>
            <Yazi an={a("thirty")} x={720} y={150} boyut={100} renk={RENK.sari}>−~30%</Yazi>
            <Yazi an={a("less")} x={500} y={560} boyut={40} font="fredoka">LESS MONEY, SAME GOODS → LOWER PRICES</Yazi>
          </Kart>
        ) : null}
        <Leo id="S13" x={interpolate(t, [garip, garip + 0.35], [450, 560], { ...CL, easing: EOUT })} y={330} s={0.95} pozlar={[[0, "C13"], [garip, "a"]]} tohum={13} />
        <Kaynak metin="Source: Federal Reserve History" an={g3b} son={garip} />
      </SahneKok>
    );
  }
  const kutu = interpolate(t, [a("pulled"), a("home.") + 0.4], [0, 1], CL);
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <div style={{ position: "absolute", left: 70, top: 170, scale: "1.06", transformOrigin: "0 0" }}>
        <Harita kutular={kutu} noktaRengi={(n) => (n.r < kutu * 0.5 ? "rgba(255,255,255,0.06)" : "#9fb3d1")} />
      </div>
      <div style={{ position: "absolute", left: 1320, top: 200, width: 560 }}>
        <Yazi an={a("people")} x={0} y={0} boyut={40} hiza="sol" font="fredoka" kontur={6}>CASH PULLED OUT,</Yazi>
        <Yazi an={a("kept")} x={0} y={56} boyut={40} hiza="sol" font="fredoka" kontur={6}>KEPT AT HOME</Yazi>
        <Yazi an={a("one")} x={0} y={200} boyut={58} hiza="sol" renk={RENK.yesil}>ONE BOX ✓</Yazi>
        <Yazi an={a("whole")} x={0} y={290} boyut={58} hiza="sol" renk={RENK.kirmizi}>A COUNTRY OF</Yazi>
        <Yazi an={a("whole") + 0.15} x={0} y={360} boyut={58} hiza="sol" renk={RENK.kirmizi}>BOXES ✗</Yazi>
      </div>
      <Kaynak metin="Source: Federal Reserve History; FDIC · positions illustrative" an={0} />
    </SahneKok>
  );
};

// S14 · tuzak kartları: 0% INTEREST · FIRE · THEFT · JOB LOSS; "NOT SO FAST"; dibe atlama
export const S14: React.FC = () => {
  const a = anlar("S14");
  const t = useT();
  const atla = a("let's");
  const dus = interpolate(t, [atla + 0.3, atla + 0.9], [0, 1], { ...CL, easing: Easing2 });
  const kartlar: [string, number, string][] = [["0% INTEREST", a("earns"), "%"], ["FIRE", a("burn."), "🔥"], ["THEFT", a("stolen."), "✋"], ["JOB LOSS", a("lose"), "$"]];
  const uc = interpolate(t, [a("spend"), a("empty.") + 0.2], [0, 1], CL);
  return (
    <SahneKok>
      <div style={{ position: "absolute", inset: 0, translate: `0px ${-dus * 1100}px` }}>
        <Kamera kareler={[[0, 1000, 560, 1.06], [20.4, 1000, 560, 1.1]]}>
          <Plaka ad="C01" filtre="blur(8px) brightness(0.45)" />
        </Kamera>
        <Leo x={470} y={380} s={0.88} pozlar={[[0, "C14"], [a("box", 3) - 0.1, "e"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} />
        <Yazi an={0} son={a("not") - 0.1} x={1300} y={300} boyut={90} renk={RENK.sari}>CHAMPION?</Yazi>
        <Damga an={a("not")} x={1300} y={260} metin="NOT SO FAST" boyut={96} />
        {kartlar.map(([m, an, ik], i) => {
          const p = interpolate(t, [an - 0.05, an + 0.3], [0, 1], { ...CL, easing: EOUT });
          if (p <= 0) return null;
          return (
            <div key={i} style={{ position: "absolute", left: 900 + (i % 2) * 480, top: 420 + Math.floor(i / 2) * 230, width: 450, height: 200, perspective: 800 }}>
              <div style={{ width: "100%", height: "100%", rotate: `y ${(1 - p) * 90}deg`, background: "#f6f0e2", border: "6px solid #1b1b1b", borderRadius: 18, display: "flex", alignItems: "center", gap: 18, padding: "0 26px", boxShadow: "0 10px 30px rgba(0,0,0,0.5)" }}>
                <TuzakIkon tur={ik} />
                <div style={{ fontFamily: "Anton", fontSize: 46, color: "#1b1b1b", whiteSpace: "nowrap" }}>{m}</div>
              </div>
            </div>
          );
        })}
        {/* JOB LOSS: banknotlar tek tek uçar, kutu boşalır */}
        {uc > 0
          ? Array.from({ length: 10 }).map((_, i) => {
              const b = interpolate(uc, [i / 10, i / 10 + 0.25], [0, 1], CL);
              if (b <= 0 || b >= 1) return null;
              return <Banknot key={i} x={500 + b * (300 + random(`u${i}`) * 900)} y={700 - b * (500 + random(`v${i}`) * 300)} adet={1} s={0.55} donme={b * 200 * (random(`w${i}`) - 0.5)} />;
            })
          : null}
        <Yazi an={a("hardest")} x={960} y={110} boyut={64}>THE HARDEST MOMENT</Yazi>
      </div>
    </SahneKok>
  );
};
const Easing2 = (x: number) => x * x * x;

const TuzakIkon: React.FC<{ tur: string }> = ({ tur }) => (
  <svg width={110} height={110} viewBox="0 0 110 110">
    {tur === "%" ? <g><circle cx={55} cy={55} r={42} fill="#e9c35a" stroke="#6b4d0e" strokeWidth={6} /><text x={55} y={74} textAnchor="middle" style={{ fontFamily: "Anton", fontSize: 50 }} fill="#6b4d0e">%</text></g> : null}
    {tur === "🔥" ? <path d="M55,10 C70,35 90,45 82,75 C76,98 34,100 28,75 C24,58 36,48 40,36 C46,50 52,52 54,46 C58,34 50,24 55,10 Z" fill="#e8742a" stroke="#1b1b1b" strokeWidth={5} /> : null}
    {tur === "✋" ? <path d="M30,100 L30,50 C30,44 38,44 38,50 L38,30 C38,24 46,24 46,30 L46,22 C46,16 54,16 54,22 L54,28 C54,22 62,22 62,28 L62,40 C62,34 70,34 70,40 L70,78 C70,92 60,100 48,100 Z" fill="#333" stroke="#1b1b1b" strokeWidth={4} /> : null}
    {tur === "$" ? <g><rect x={15} y={35} width={80} height={44} rx={6} fill="#9cc58f" stroke="#2c4a26" strokeWidth={5} /><text x={55} y={68} textAnchor="middle" style={{ fontFamily: "Anton", fontSize: 30 }} fill="#2c4a26">$</text></g> : null}
  </svg>
);

// S15 · dip: 8 Tem 1932 41.22; −89%; $108 (yalnız fiyat); 1929 fiyatlarıyla ~$138; iki cevap: 1954 / ~1936 sonu
export const S15: React.FC = () => {
  const a = anlar("S15");
  const t = useT();
  const nokta = [
    { x: yil(1921, 8), y: 63, etiket: "1921: 63", etiketYon: "ust" as const },
    { x: yil(1929, 9, 3), y: 381.17, etiket: "SEPT 3, 1929: 381.17", etiketYon: "sag" as const },
    { x: yil(1929, 11, 15), y: 190.6 },
    { x: yil(1932, 7, 8), y: 41.22, etiket: "JULY 8, 1932: 41.22", etiketYon: "sag" as const, an: a("forty-one") },
  ];
  const cevap1 = a("november");
  const tam = [...nokta, { x: yil(1954, 11, 23), y: 381.17, etiket: "NOV 1954", etiketYon: "sol" as const, an: cevap1 }];
  const ciz2 = t >= cevap1 - 0.3;
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <Kart an={0} x={160} y={60} w={1600} h={560}>
        <div style={{ position: "absolute", left: 36, top: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>DOW JONES INDUSTRIAL AVERAGE · CLOSING ANCHORS (PRICE INDEX)</div>
        <div style={{ position: "absolute", left: 10, top: 56 }}>
          <CizgiGrafik
            an={ciz2 ? cevap1 - 0.3 : 0.2}
            sure={ciz2 ? 1.2 : a("two.") - 0.2}
            w={1580}
            h={490}
            xAralik={[1920.5, 1956]}
            yAralik={[0, 430]}
            renk={RENK.mavi}
            kesikli
            noktalar={ciz2 ? tam : nokta}
            eksenX={[1925, 1930, 1935, 1940, 1945, 1950, 1955].map((v) => ({ x: v, etiket: String(v) }))}
          />
        </div>
        {t >= a("late") ? <Dikey x={yil(1936, 11)} an={a("late")} metin="~LATE 1936" /> : null}
        <Yazi an={a("eighty-nine")} x={980} y={120} boyut={110} renk={RENK.kirmizi}>−89%</Yazi>
      </Kart>
      {/* alt satır: istatistik kutuları (çift eksen yok) */}
      {t < a("so") - 0.2 ? (
        <>
          <Kart an={a("one") - 0.1} x={160} y={650} w={760} h={190}>
            <div style={{ padding: "20px 28px", fontFamily: "Anton", fontSize: 64, color: RENK.sari }}>
              $1,000 → <Sayac an={a("one")} sure={0.8} bas={1000} bit={108} onEk="$" />
            </div>
            <div style={{ position: "absolute", left: 28, top: 116, fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.murekkep }}>Price only, before dividends.</div>
          </Kart>
          <Kart an={a("thirty-eight")} x={1000} y={650} w={760} h={190}>
            <div style={{ padding: "20px 28px", fontFamily: "Anton", fontSize: 64, color: RENK.ikincil }}>IN 1929 PRICES: ~$138</div>
            <div style={{ position: "absolute", left: 28, top: 116, fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.murekkep }}>{t > a("dividends", 2) ? "Dividends helped — look at the gap" : "Even with falling prices"}</div>
          </Kart>
        </>
      ) : (
        <>
          <Yazi an={a("so")} x={960} y={640} boyut={64} renk={RENK.murekkep}>BACK TO $1,000?</Yazi>
          <Kart an={a("dow's") - 0.1} x={160} y={730} w={780} h={150} cerceve={RENK.mavi}>
            <div style={{ padding: "14px 24px", fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>ANSWER 1: <span style={{ color: RENK.mavi }}>1954</span> (PRICE)</div>
          </Kart>
          <Kart an={a("counting")} x={980} y={730} w={780} h={150} cerceve={RENK.sari}>
            <div style={{ padding: "14px 24px", fontFamily: "Anton", fontSize: 44, color: RENK.murekkep }}>ANSWER 2: <span style={{ color: RENK.sari }}>~LATE 1936</span></div>
            <div style={{ position: "absolute", left: 24, top: 86, fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.ikincil }}>dividends + falling prices (Hulbert, NYT 2009)</div>
          </Kart>
          <Yazi an={a("seven")} x={980} y={250} boyut={64} renk={RENK.sari}>STILL 7 YEARS</Yazi>
          <div style={{ position: "absolute", left: 160, top: 640, fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.murekkep }}>Price only, before dividends.</div>
        </>
      )}
      <Kaynak metin="Source: Federal Reserve History; BLS CPI via FRED; Hulbert (NYT, 2009)" an={0} />
    </SahneKok>
  );
};
const yil = (y: number, ay: number, gun = 1) => y + (ay - 1) / 12 + (gun - 1) / 365;

// Grafik kartı içine dikey işaret (S15 düzeni: x 1920.5–1956, kart iç genişlik 1580, sol pay 30+10)
const Dikey: React.FC<{ x: number; an: number; metin: string }> = ({ x, an, metin }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.3], [0, 1], CL);
  const px = 10 + 30 + ((x - 1920.5) / (1956 - 1920.5)) * (1580 - 60);
  return (
    <div style={{ position: "absolute", left: px, top: 96, height: 394, borderLeft: `4px dashed ${RENK.sari}`, opacity: p }}>
      <div style={{ position: "absolute", left: 10, top: 0, fontFamily: "Anton", fontSize: 36, color: RENK.sari, whiteSpace: "nowrap" }}>{metin}</div>
    </div>
  );
};

// S16 · G4 skor tablosu (koşullu banka satırları; "IN A DECADE OF FALLING PRICES" şeridi)
export const S16: React.FC = () => {
  const a = anlar("S16");
  const t = useT();
  const kol = (x: number, renk: string, baslik: string, an: number, icerik: React.ReactNode) => (
    <Kart an={an} x={x} y={150} w={380} h={600} cerceve={renk}>
      <div style={{ height: 90, background: renk, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 54, color: "#101010" }}>{baslik}</div>
      <div style={{ padding: "26px 24px" }}>{icerik}</div>
    </Kart>
  );
  const satir = (an: number, m: React.ReactNode, boyut = 32) => (
    <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: boyut, color: RENK.murekkep, opacity: interpolate(t, [an, an + 0.25], [0, 1], CL), marginBottom: 18, lineHeight: 1.2 }}>{m}</div>
  );
  return (
    <SahneKok>
      <Kamera kareler={[[0, 960, 540, 1.04], [27.5, 960, 540, 1.08]]}>
        <Plaka ad="C03" filtre="blur(8px) brightness(0.5)" />
      </Kamera>
      <Yazi an={0.1} x={1270} y={50} boyut={64}>SCOREBOARD · JULY 1932</Yazi>
      {kol(690, KAPI_RENK.mavi, "STOCK", a("stock") - 0.1, (
        <>
          {satir(a("about"), <span style={{ fontFamily: "Anton", fontSize: 96, color: RENK.sari }}>$108</span>)}
          {satir(a("price"), "price only")}
        </>
      ))}
      {kol(1090, KAPI_RENK.yesil, "BANK", a("bank") - 0.1, (
        <>
          {satir(a("question"), <span style={{ fontFamily: "Anton", fontSize: 110, color: RENK.sari }}>?</span>)}
          {satir(a("maybe"), "If your bank survived: same as the box", 28)}
          {satir(a("maybe", 2), "If your bank suspended: avg. ~$800 left", 28)}
        </>
      ))}
      {kol(1490, KAPI_RENK.kahve, "BOX", a("box", 2) - 0.1, (
        <>
          {satir(a("one"), <span style={{ fontFamily: "Anton", fontSize: 96, color: RENK.sari }}>$1,000</span>)}
          {satir(a("twelve"), "= $1,272 of 1929 goods")}
        </>
      ))}
      <Kart an={a("decade.")} x={690} y={780} w={1180} h={90} arka={RENK.sari} cerceve="#101010">
        <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 50, color: "#101010", letterSpacing: 3 }}>IN A DECADE OF FALLING PRICES</div>
      </Kart>
      <Leo id="S16" x={330} y={340} s={0.85} pozlar={[[0, "C12"], [2.5, "a"]]} tohum={16} />
      <Kaynak metin="Sources: FRH; FDIC Table 5; BLS CPI via FRED" an={2.5} />
    </SahneKok>
  );
};
