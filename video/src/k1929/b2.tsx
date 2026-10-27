import React from "react";
import { interpolate } from "remotion";
import { fredoka, KAPI, KapiIsik } from "./ortak";
import {
  anlar, CizgiGrafik, CL, CubukGrafik, Damga, EIO, EOUT, Harita, Illustration, Kamera, Kart, Kaynak, KAPI_RENK, Leo, Plaka, RENK,
  SahneKok, Sayac, SeritYagmuru, Takvim, useT, Yazi,
} from "./kit";
import { FDIC } from "./veri-grafik";

// Bölüm 2–3 — Door One: The Stock Market (S05–S07) · Door Two: The Bank (S08–S10)

const ARKA_GRAFIK = "radial-gradient(ellipse at 50% 40%, #16223b 0%, #070b16 100%)";

// Dow çapaları (FRH-29). Çapalar arası çizgi kesikli: ara değer verisi değil, yalnız bağlantı.
const yil = (y: number, ay: number, gun = 1) => y + (ay - 1) / 12 + (gun - 1) / 365;

// S05 · mavi kapı açılır → C16; G1a 63 → 381.17 (×6); kısmi ödeme; 3 Eyl zirve
export const S05: React.FC = () => {
  const a = anlar("S05");
  const t = useT();
  const g1 = a("in", 1) - 0.2; // "In August 1921"
  const salon = a("ordinary") - 0.3;
  const zirve = a("stock") - 0.2; // "Stock Leo walks through the blue door"
  const [px, py, pw, ph] = KAPI.mavi.panel;
  const ac = interpolate(t, [0.5, 1.6], [0, 1], { ...CL, easing: EIO });
  if (t < g1) {
    // kapı açılışı: panel içinde C16, sonra tüm kareye büyür
    const s = interpolate(t, [0, 0.5, g1], [1.65, 1.7, 4.2], { ...CL, easing: EIO });
    return (
      <SahneKok>
        <Kamera kareler={[[0, px + pw / 2, py + ph / 2, s]]}>
          <Plaka ad="C01" />
          <KapiIsik ad="mavi" an={-1} yaziHazir parlama={0} />
          <div style={{ position: "absolute", left: px, top: py, width: pw, height: ph, overflow: "hidden", clipPath: `inset(0 ${(1 - ac) * 100}% 0 0)` }}>
            <Kamera kareler={[[0, 960, 540, ph / 1080]]} ekranW={pw} ekranH={ph}>
              <Plaka ad="C16" />
            </Kamera>
          </div>
        </Kamera>
      </SahneKok>
    );
  }
  const grafik = t < salon || (t >= a("it's") - 0.4);
  return (
    <SahneKok>
      <Kamera kareler={[[g1, 960, 540, 1.0], [salon, 990, 540, 1.04], [zirve, 1010, 560, 1.08], [35.9, 1100, 560, 1.12]]}>
        <Plaka ad="C16" filtre={grafik ? "blur(6px) brightness(0.45)" : undefined} />
      </Kamera>
      {!grafik ? (
        <>
          <SeritYagmuru an={salon} />
          <Leo x={470} y={360} s={0.9} pozlar={[[0, "f"]]} rozet={{ etiket: "STOCK", renk: KAPI_RENK.mavi }} giris={{ an: salon, dy: 300, sure: 0.4 }} tohum={7} />
          <Yazi an={a("put")} x={1260} y={160} boyut={70}>PART DOWN, REST BORROWED</Yazi>
          <Yazi an={a("ten")} x={1260} y={250} boyut={70} renk={RENK.sari}>SOMETIMES ONLY 10% DOWN</Yazi>
          <Yazi an={a("september", 2)} x={1260} y={420} boyut={84} renk={KAPI_RENK.mavi}>SEPT 3, 1929</Yazi>
          <Yazi an={a("three", 2)} x={1260} y={520} boyut={110} renk={RENK.sari}>381.17</Yazi>
          <Illustration />
        </>
      ) : (
        <>
          <Kart an={g1} x={300} y={110} w={1320} h={700}>
            <div style={{ position: "absolute", left: 36, top: 22, fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.ikincil }}>DOW JONES INDUSTRIAL AVERAGE · CLOSING ANCHORS</div>
            <div style={{ position: "absolute", left: 20, top: 70 }}>
              <CizgiGrafik
                an={a("by")}
                sure={a("eighty-one") - a("by") + 0.2}
                w={1280}
                h={600}
                xAralik={[1921.3, 1930.2]}
                yAralik={[0, 420]}
                renk={RENK.mavi}
                kesikli
                noktalar={[
                  { x: yil(1921, 8), y: 63, etiket: "AUG 1921: 63", etiketYon: "ust", an: a("sixty-three") },
                  { x: yil(1929, 9, 3), y: 381.17, etiket: t > a("it's") - 0.4 ? "SEPT 3, 1929: 381.17 — THE TOP" : "SEPT 1929: 381", etiketYon: "sol", an: a("eighty-one") },
                ]}
                eksenX={[1922, 1924, 1926, 1928, 1930].map((v) => ({ x: v, etiket: String(v) }))}
              />
            </div>
            <Yazi an={a("six")} x={760} y={250} boyut={140} renk={RENK.sari}>×6</Yazi>
          </Kart>
          <Kaynak metin="Source: Federal Reserve History · anchors only, dashed = not daily data" an={g1 + 0.3} />
        </>
      )}
    </SahneKok>
  );
};

// S06 · takvim Eyl→Eki; dalgalı iniş; Black Monday/Tuesday çubukları; marjin sarmalı; ~yarı; $1,000 → ~$500
export const S06: React.FC = () => {
  const a = anlar("S06");
  const t = useT();
  const cubuk = a("on", 1) - 0.2; // "On Monday"
  const sarmal = a("borrowed") - 0.2;
  const kasim = a("by") - 0.2;
  const leo = a("stock") - 0.2;
  // Gün: 0 = 3 Eyl 1929. Etiketsiz ara noktalar biçim içindir (metin: "dalgalı, aşağı eğimli"; 28 Eki öncesi ≈299 [FRH-29]).
  const yol = [
    { x: 0, y: 381.17, etiket: "381", etiketYon: "ust" as const },
    { x: 8, y: 360 }, { x: 14, y: 372 }, { x: 22, y: 345 }, { x: 28, y: 358 }, { x: 36, y: 330 }, { x: 42, y: 340 }, { x: 50, y: 305 }, { x: 54, y: 299 },
    { x: 55, y: 260 }, { x: 56, y: 230 }, { x: 62, y: 245 }, { x: 68, y: 205 }, { x: 73, y: 191, etiket: "MID-NOV: ALMOST HALF", etiketYon: "sol" as const, an: a("half") },
  ];
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <Kamera kareler={[[0, 960, 540, 1.0], [34.2, 960, 540, 1.05]]}>
        <Plaka ad="C16" filtre="blur(9px) brightness(0.3) saturate(0.4)" />
      </Kamera>
      {t < cubuk ? <Takvim x={160} y={190} w={340} adimlar={[[0, "SEP"], [a("october") - 0.1, "OCT"]]} altYazi="1929" /> : null}
      <Kart an={0} son={cubuk - 0.2} x={620} y={150} w={1140} h={620}>
        <div style={{ position: "absolute", left: 30, top: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>DOW, FALL 1929 (shape illustrative)</div>
        <div style={{ position: "absolute", left: 10, top: 60 }}>
          <CizgiGrafik an={0.3} sure={a("arrives.") - 0.3} w={1110} h={540} xAralik={[0, 75]} yAralik={[150, 400]} renk="#8fa6c9" noktalar={yol.slice(0, 9)} eksenX={[{ x: 0, etiket: "SEPT 3" }, { x: 28, etiket: "OCT 1" }, { x: 55, etiket: "OCT 28" }]} />
        </div>
      </Kart>
      {t >= cubuk && t < sarmal ? (
        <>
          <Kart an={cubuk} x={360} y={130} w={1200} h={640}>
            <div style={{ position: "absolute", left: 36, top: 22, fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.ikincil }}>ONE-DAY DROP IN THE DOW</div>
            <div style={{ position: "absolute", left: 200, top: 80 }}>
              <CubukGrafik an={a("thirteen") - 0.3} arasi={a("twelve") - a("thirteen")} w={800} h={520} maks={14} renk="#8fa6c9" veri={[{ etiket: "MON OCT 28", deger: 13, ustYazi: "−13%" }, { etiket: "TUE OCT 29", deger: 12, ustYazi: "−12%" }]} />
            </div>
          </Kart>
          <Yazi an={a("black")} x={700} y={880 - 120} boyut={64} renk={RENK.murekkep}>BLACK MONDAY</Yazi>
          <Yazi an={a("black", 2)} x={1220} y={880 - 120} boyut={64} renk={RENK.murekkep}>BLACK TUESDAY</Yazi>
        </>
      ) : null}
      {t >= sarmal && t < kasim ? <Sarmal a={a} /> : null}
      {t >= kasim ? (
        <>
          <Kart an={kasim} x={620} y={150} w={1140} h={620}>
            <div style={{ position: "absolute", left: 30, top: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>DOW, FALL 1929 (shape illustrative)</div>
            <div style={{ position: "absolute", left: 10, top: 60 }}>
              <CizgiGrafik an={kasim} sure={a("half") - kasim + 0.3} w={1110} h={540} xAralik={[0, 75]} yAralik={[150, 400]} renk="#8fa6c9" noktalar={yol} eksenX={[{ x: 0, etiket: "SEPT 3" }, { x: 28, etiket: "OCT 1" }, { x: 55, etiket: "OCT 28" }, { x: 73, etiket: "MID-NOV" }]} yatayCizgi={[{ y: 190.6, etiket: "½ OF 381" }]} />
            </div>
          </Kart>
          <Leo x={330} y={420} s={0.75} pozlar={[[0, "d"]]} rozet={{ etiket: "STOCK", renk: KAPI_RENK.mavi }} giris={{ an: leo, dx: -500, sure: 0.35 }} />
          <Yazi an={leo + 0.2} x={330} y={100} boyut={96} renk={RENK.sari}>
            <Sayac an={a("now")} sure={a("hundred.") - a("now") + 0.3} bas={1000} bit={500} onEk="$" />
          </Yazi>
          <Yazi an={a("hundred.") + 0.1} x={330} y={210} boyut={44} font="fredoka">$1,000 → ~$500</Yazi>
        </>
      ) : null}
      <Kaynak metin="Source: Federal Reserve History" an={cubuk} />
    </SahneKok>
  );
};

const Sarmal: React.FC<{ a: (w: string, n?: number) => number }> = ({ a }) => {
  const t = useT();
  const adim: [string, number][] = [["PRICES DROP", a("drop,")], ["LENDERS CALL LOANS", a("lenders")], ["PEOPLE SELL", a("sell,")], ["PRICES DROP AGAIN", a("again.")]];
  const merkez = [960, 470], r = 270;
  return (
    <>
      <Yazi an={a("borrowed")} x={960} y={90} boyut={70} renk={RENK.sari}>BORROWED MONEY MAKES IT WORSE</Yazi>
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        {adim.map((_, i) => {
          const a0 = (-90 + i * 90 + 18) * (Math.PI / 180), a1 = (-90 + (i + 1) * 90 - 18) * (Math.PI / 180);
          const p = interpolate(t, [adim[i][1], adim[i][1] + 0.4], [0, 1], CL);
          const x0 = merkez[0] + r * Math.cos(a0), y0 = merkez[1] + r * Math.sin(a0), x1 = merkez[0] + r * Math.cos(a1), y1 = merkez[1] + r * Math.sin(a1);
          return <path key={i} d={`M${x0},${y0} A${r},${r} 0 0 1 ${x1},${y1}`} stroke={RENK.kirmizi} strokeWidth={10} fill="none" strokeLinecap="round" strokeDasharray={600} strokeDashoffset={600 * (1 - p)} />;
        })}
      </svg>
      {adim.map(([m, an], i) => {
        const ang = (-90 + i * 90) * (Math.PI / 180);
        return (
          <Yazi key={i} an={an} x={merkez[0] + r * Math.cos(ang)} y={merkez[1] + r * Math.sin(ang) - 34} boyut={50} font="fredoka">
            {m}
          </Yazi>
        );
      })}
    </>
  );
};

// S07 · "−50% IN ~10 WEEKS"; Stock Leo sakin; bölünmüş ekran → banka içi, Bank Leo kollar kavuşturmuş; "Right?"
export const S07: React.FC = () => {
  const a = anlar("S07");
  const t = useT();
  const bol = a("over") - 0.2;
  const k = interpolate(t, [bol, bol + 0.5], [0, 1], { ...CL, easing: EOUT });
  const solW = 1920 - 960 * k;
  return (
    <SahneKok>
      <div style={{ position: "absolute", left: 0, top: 0, width: solW, height: 1080, overflow: "hidden" }}>
        <Kamera kareler={[[0, 960, 540, 1.0], [bol, 900, 540, 1.04]]}>
          <Plaka ad="C16" filtre="brightness(0.55) saturate(0.6)" />
        </Kamera>
        <Leo x={solW / 2 - (1 - k) * 380} y={380} s={0.86} pozlar={[[0, "d"], [a("stays") - 0.1, "e"]]} rozet={{ etiket: "STOCK", renk: KAPI_RENK.mavi }} />
        <Yazi an={0.05} son={bol} x={1380} y={220} boyut={110} renk={RENK.sari}>−50%</Yazi>
        <Yazi an={0.3} son={bol} x={1380} y={350} boyut={64}>IN ~10 WEEKS</Yazi>
        <Yazi an={a("dip,")} son={bol} x={1380} y={480} boyut={54} font="fredoka">&quot;IT&apos;S JUST A DIP&quot;</Yazi>
      </div>
      {k > 0 ? (
        <div style={{ position: "absolute", left: solW, top: 0, width: 1920 - solW, height: 1080, overflow: "hidden", borderLeft: "8px solid #0b0b0b" }}>
          <Kamera kareler={[[bol, 1450, 540, 1.0], [16.9, 1500, 540, 1.06]]} ekranW={960}>
            <Plaka ad="C17" />
          </Kamera>
          <Leo x={430} y={380} s={0.86} pozlar={[[0, "C13"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} konusmaz giris={{ an: a("bank"), dx: 600, sure: 0.4 }} />
          <Yazi an={a("vault")} x={700} y={120} boyut={54} font="fredoka">VAULT ✓</Yazi>
          <Yazi an={a("marble")} x={700} y={190} boyut={54} font="fredoka">MARBLE FLOOR ✓</Yazi>
          <Yazi an={a("right?")} x={480} y={720} boyut={120} renk={RENK.sari} salla>RIGHT?</Yazi>
        </div>
      ) : null}
      <Illustration />
    </SahneKok>
  );
};

// S08 · sigorta yok; ~24.000 banka (1 nokta = 10 banka); 1930 sonu dalga dalga kapanışlar
export const S08: React.FC = () => {
  const a = anlar("S08");
  const t = useT();
  const harita = a("and", 1) - 0.2; // "And there were a lot of banks"
  if (t < harita) {
    return (
      <SahneKok>
        <Kamera kareler={[[0, 1000, 540, 1.04], [harita, 1150, 470, 1.1]]}>
          <Plaka ad="C03" />
          <div style={{ position: "absolute", left: 829, top: 189, width: 931, height: 444 }}>
            <Yazi an={a("twenty-nine,")} x={465} y={40} boyut={58}>1929</Yazi>
            <SigortaKutusu an={a("insurance.") - 0.4} x={300} y={130} isaret={false} />
            <Yazi an={a("insurance.")} x={465} y={320} boyut={46} font="fredoka" renk={RENK.sari}>NO FEDERAL DEPOSIT INSURANCE</Yazi>
          </div>
        </Kamera>
        <Leo id="S08" x={450} y={330} s={0.95} pozlar={[[0, "a"], [a("had") - 0.1, "C12"], [a("if") - 0.1, "a"]]} tohum={8} />
        <Kaynak metin="Source: FDIC" an={a("insurance.")} />
      </SahneKok>
    );
  }
  const yan = a("banks.") ;
  const fed = a("eight");
  const disi = a("sixteen");
  const dalga = a("fail");
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <div style={{ position: "absolute", left: 120, top: 150, scale: "1.18", transformOrigin: "0 0" }}>
        <Harita
          noktaRengi={(n, i) => {
            const gir = yan + (i / 2400) * 1.2;
            if (t < gir) return null;
            const kapandi = dalga + 0.2 + n.r * 2.6;
            if (n.r < 0.03 && t > kapandi) return t < kapandi + 0.25 ? RENK.kirmizi : "rgba(255,255,255,0.06)";
            if (t >= fed && t < disi + 3 && n.fed) return KAPI_RENK.mavi;
            if (t >= disi && t < disi + 3 && !n.fed) return "#e8e2d0";
            return "#9fb3d1";
          }}
        />
      </div>
      <div style={{ position: "absolute", left: 1460, top: 180, width: 400 }}>
        <Yazi an={yan} x={0} y={0} boyut={42} hiza="sol" font="fredoka" kontur={6}>~24,000 BANKS</Yazi>
        <Yazi an={yan + 0.2} x={0} y={56} boyut={28} hiza="sol" font="fredoka" kontur={5} renk={RENK.ikincil}>1 DOT = 10 BANKS</Yazi>
        <Yazi an={fed} x={0} y={150} boyut={46} hiza="sol" renk={KAPI_RENK.mavi}>8,000+ IN THE FED SYSTEM</Yazi>
        <Yazi an={disi} x={0} y={230} boyut={46} hiza="sol" renk="#e8e2d0">~16,000 OUTSIDE</Yazi>
        <Yazi an={a("small")} x={0} y={310} boyut={36} hiza="sol" font="fredoka" kontur={5}>MANY SMALL & LOCAL</Yazi>
        <Yazi an={a("late")} x={0} y={430} boyut={64} hiza="sol" renk={RENK.kirmizi}>LATE 1930</Yazi>
        <Yazi an={a("hundreds")} x={0} y={520} boyut={40} hiza="sol" font="fredoka" kontur={6}>HUNDREDS CLOSE IN WEEKS</Yazi>
      </div>
      <Leo x={1640} y={820} s={0.42} pozlar={[[0, "C13"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} giris={{ an: a("for") - 0.1, dy: 500, sure: 0.4 }} cikis={{ an: a("then,") , dy: 500, sure: 0.4 }} />
      <Kaynak metin="Source: Federal Reserve History · dot positions illustrative" an={yan} />
    </SahneKok>
  );
};

const SigortaKutusu: React.FC<{ an: number; x: number; y: number; isaret: boolean; isaretAn?: number }> = ({ an, x, y, isaret, isaretAn = 0 }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.25], [0, 1], { ...CL, easing: EOUT });
  const c = isaret ? interpolate(t, [isaretAn, isaretAn + 0.3], [0, 1], CL) : 0;
  return (
    <div style={{ position: "absolute", left: x, top: y, opacity: p, scale: String(0.7 + 0.3 * p), display: "flex", alignItems: "center", gap: 24 }}>
      <svg width={130} height={130}>
        <rect x={8} y={8} width={114} height={114} rx={16} fill="#0f1626" stroke="#f4f1ea" strokeWidth={8} />
        {c > 0 ? <path d="M30,68 l24,26 l48,-60" stroke={RENK.yesil} strokeWidth={14} fill="none" strokeLinecap="round" strokeDasharray={160} strokeDashoffset={160 * (1 - c)} /> : null}
      </svg>
      <div style={{ fontFamily: "Anton", fontSize: 72, color: "#f4f1ea", letterSpacing: 3 }}>INSURANCE</div>
    </div>
  );
};
export { SigortaKutusu };

// S09 · 11 Ara 1930 Bank of United States; kuyruk; mekanizma (10 para, 9 LOANS); kuyruk yan bankaya
export const S09: React.FC = () => {
  const a = anlar("S09");
  const t = useT();
  const mek = a("here's") - 0.2;
  if (t < mek) {
    return (
      <SahneKok>
        <Kamera kareler={[[0, 1100, 520, 1.06], [a("picture") - 0.2, 1100, 520, 1.08], [mek, 760, 560, 1.12]]}>
          <Plaka ad="C18" />
        </Kamera>
        <Yazi an={a("december")} son={a("picture") - 0.2} x={960} y={110} boyut={78} renk={RENK.sari}>DEC 11, 1930</Yazi>
        <Yazi an={a("bank", 2)} son={a("picture") - 0.2} x={960} y={210} boyut={60}>BANK OF UNITED STATES CLOSES</Yazi>
        <Yazi an={a("fourth-largest")} son={a("picture") - 0.2} x={960} y={290} boyut={38} font="fredoka">NEW YORK CITY&apos;S 4TH-LARGEST BANK</Yazi>
        <Leo x={1560} y={470} s={0.72} pozlar={[[0, "C20"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} giris={{ an: a("long") - 0.2, dx: 700, sure: 0.45 }} />
        <Illustration />
      </SahneKok>
    );
  }
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <Mekanizma a={a} />
      <Kaynak metin="Source: Federal Reserve History" />
    </SahneKok>
  );
};

const Mekanizma: React.FC<{ a: (w: string, n?: number) => number }> = ({ a }) => {
  const t = useT();
  const gir = a("a", 2) - 0.1; // "A bank doesn't keep"
  const borc = a("lends");
  const herkes = a("everyone");
  const bos = a("run");
  const yan = a("next");
  const kasa = { x: 760, y: 300, w: 400, h: 400 };
  const kuyrukX = interpolate(t, [yan, yan + 1.2], [0, 1], { ...CL, easing: EIO });
  return (
    <>
      <Yazi an={a("problem.")} x={960} y={70} boyut={70} renk={RENK.sari}>HERE&apos;S THE PROBLEM</Yazi>
      {/* kasa (banka 1) */}
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        <rect x={kasa.x} y={kasa.y} width={kasa.w} height={kasa.h} rx={24} fill="#1d2a45" stroke="#c9ccd2" strokeWidth={8} />
        <text x={kasa.x + kasa.w / 2} y={kasa.y - 20} textAnchor="middle" fill="#f4f1ea" style={{ fontFamily: "Anton", fontSize: 44 }}>BANK</text>
        {Array.from({ length: 10 }).map((_, i) => {
          const giris = interpolate(t, [gir + i * 0.12, gir + i * 0.12 + 0.35], [0, 1], { ...CL, easing: EOUT });
          const disari = i < 9 ? interpolate(t, [borc + i * 0.08, borc + i * 0.08 + 0.6], [0, 1], { ...CL, easing: EIO }) : 0;
          const cekildi = i === 9 ? interpolate(t, [bos, bos + 0.4], [0, 1], CL) : 0;
          const cx0 = kasa.x + 70 + (i % 5) * 65, cy0 = kasa.y + 150 + Math.floor(i / 5) * 90;
          const cx = cx0 + disari * (1400 - cx0) + cekildi * -500;
          const cy = cy0 - (1 - giris) * 400 + disari * (520 - cy0 + i * 22);
          return (
            <g key={i} opacity={giris * (1 - cekildi)}>
              <circle cx={cx} cy={cy} r={28} fill="#e9c35a" stroke="#6b4d0e" strokeWidth={5} />
              <text x={cx} y={cy + 11} textAnchor="middle" style={{ fontFamily: "Anton", fontSize: 30 }} fill="#6b4d0e">$</text>
            </g>
          );
        })}
        <path d={`M${kasa.x + kasa.w + 20},500 L1330,500`} stroke={RENK.sari} strokeWidth={8} markerEnd="url(#ok)" opacity={interpolate(t, [borc, borc + 0.3], [0, 1], CL)} />
        <defs>
          <marker id="ok" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M0,0 L10,5 L0,10 z" fill={RENK.sari} />
          </marker>
        </defs>
        {/* kuyruk: 10 kişi ikonu, sonra yan bankaya kayar */}
        {Array.from({ length: 10 }).map((_, i) => {
          const p = interpolate(t, [herkes + i * 0.07, herkes + i * 0.07 + 0.3], [0, 1], CL);
          const x = 120 + i * 58 + kuyrukX * 1100;
          return (
            <g key={`k${i}`} opacity={p} transform={`translate(${x} ${820})`}>
              <circle cx={0} cy={-70} r={20} fill="#c9ccd2" />
              <rect x={-22} y={-48} width={44} height={60} rx={14} fill="#c9ccd2" />
            </g>
          );
        })}
        {kuyrukX > 0 ? (
          <g opacity={kuyrukX}>
            <rect x={1460} y={660} width={300} height={200} rx={20} fill="#1d2a45" stroke="#c9ccd2" strokeWidth={6} />
            <text x={1610} y={640} textAnchor="middle" fill="#f4f1ea" style={{ fontFamily: "Anton", fontSize: 36 }}>NEXT BANK</text>
          </g>
        ) : null}
      </svg>
      <Yazi an={borc} x={1500} y={420} boyut={52} renk={RENK.sari}>LOANS</Yazi>
      <Yazi an={borc + 0.4} x={960} y={160} boyut={46} font="fredoka">BANKS LEND MOST DEPOSITS OUT</Yazi>
      <Damga an={a("cash.")} x={960} y={500} metin="EMPTY" />
    </>
  );
};

// S10 · G2 askıya almalar 1921–33; ~20¢/1$; iki sonuç; GAMBLE damgası
export const S10: React.FC = () => {
  const a = anlar("S10");
  const t = useT();
  const g2 = a("from") - 0.4;
  const kayip = a("if", 1) - 0.2;
  const kasa = a("for", 2) - 0.2;
  const veri = FDIC.map((r) => ({ etiket: `’${String(r.yil).slice(2)}`, deger: r.banka, vurgu: r.yil >= 1930, ustYazi: r.yil >= 1930 ? r.banka.toLocaleString("en-US") : undefined }));
  const top = FDIC.filter((r) => r.yil >= 1930).reduce((s, r) => s + r.banka, 0);
  const mev = FDIC.filter((r) => r.yil >= 1930).reduce((s, r) => s + r.mevduat, 0);
  const kay = FDIC.filter((r) => r.yil >= 1930).reduce((s, r) => s + r.kayip, 0);
  const sent = Math.round((kay / mev) * 100); // ≈20¢ (19.6) [H]
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      {t < kasa ? (
        <>
          <Yazi an={0} x={960} y={60} boyut={64}>THE SCORE FOR DOOR 2</Yazi>
          <Yazi an={a("two.", 2)} x={960} y={150} boyut={52} renk={RENK.sari} font="fredoka">NOT ONE NUMBER. TWO.</Yazi>
          <Kart an={g2} son={kayip} x={220} y={240} w={1480} h={600}>
            <div style={{ position: "absolute", left: 36, top: 20, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>COMMERCIAL BANK SUSPENSIONS PER YEAR, 1921–1933</div>
            <div style={{ position: "absolute", left: 20, top: 60 }}>
              <CubukGrafik an={g2 + 0.2} veri={veri} w={1440} h={530} maks={4200} renk={RENK.yesil} vurguAn={a("about")} />
            </div>
            <Yazi an={a("nine")} x={1030} y={110} boyut={62} renk={RENK.sari}>1930–33: ~9,000</Yazi>
            <Yazi an={a("more")} x={1030} y={190} boyut={44} font="fredoka">MORE THAN 1 BANK IN 3</Yazi>
            <Yazi an={a("some")} x={1030} y={250} boyut={30} font="fredoka" renk={RENK.ikincil}>SOME REOPENED · THOUSANDS NEVER DID</Yazi>
          </Kart>
          <Kart an={kayip} x={360} y={260} w={1200} h={500}>
            <div style={{ position: "absolute", left: 40, top: 30, fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.ikincil, width: 1120 }}>LOST BY DEPOSITORS IN SUSPENDED BANKS, 1930–33</div>
            <Yazi an={a("twenty")} x={600} y={120} boyut={200} renk={RENK.sari}>~{sent}¢</Yazi>
            <Yazi an={a("every")} x={600} y={360} boyut={60}>PER $1, ON AVERAGE</Yazi>
          </Kart>
        </>
      ) : (
        <>
          <Kamera kareler={[[kasa, 1570, 517, 1.0], [39.3, 1450, 540, 1.08]]}>
            <Plaka ad="C17" filtre="brightness(0.6)" />
          </Kamera>
          <Leo x={480} y={400} s={0.85} pozlar={[[0, "d"], [a("if", 2) - 0.1, "e"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} />
          <Kart an={a("hundred")} x={980} y={170} w={760} h={190} cerceve={RENK.kirmizi}>
            <div style={{ padding: "22px 30px", fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>BANK SUSPENDED</div>
            <div style={{ position: "absolute", left: 30, top: 95, fontFamily: "Anton", fontSize: 60, color: RENK.sari }}>~$800 + WAIT</div>
          </Kart>
          <Kart an={a("survived,")} x={980} y={400} w={760} h={190} cerceve={RENK.yesil}>
            <div style={{ padding: "22px 30px", fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>BANK SURVIVED</div>
            <div style={{ position: "absolute", left: 30, top: 95, fontFamily: "Anton", fontSize: 60, color: RENK.yesil }}>$1,000</div>
          </Kart>
          <Damga an={a("gamble.")} x={1360} y={760} metin="GAMBLE" />
          <Illustration />
        </>
      )}
      <Kaynak metin={`Source: FDIC, A Brief History of Deposit Insurance, Table 5 · 1930–33 total ${top.toLocaleString("en-US")}`} an={g2} son={kasa} />
    </SahneKok>
  );
};
