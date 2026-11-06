import React from "react";
import { AbsoluteFill, Img, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { Doku, fredoka } from "./ortak";
import {
  anlar, Banknot, CizgiGrafik, CL, CubukGrafik, Damga, EIO, EOUT, f, Illustration, Kamera, Kart, Kaynak, KAPI_RENK, Leo, RENK, Sayac, Takvim, useT, Yazi,
} from "./kit";
import { CPI22_IDX, CPI29, CPI29_IDX, FDIC } from "./veri-grafik";
import { SAHNELER, SHORTS_EK } from "./veri-tam";
import { AltyaziParca, kare } from "./Tam";
import { Sunucu } from "./Sunucu";
import { RIG_T, YUZ_T } from "./kit";

// 9:16 (1080x1920) Shorts sahneleri — kurgu-editoru keser ve kendi hook'unu ekler.
// Güvenli alan (YouTube Shorts arayüzü): üst ~%10 (192 px), alt ~%20 (1536 px altı), sağ ~%15 (918 px sağı) → yazı ve yüz dışarıda.
// Kapılar: C22 dikey stüdyo (kapılar yan yana okunur; 16:9 kırpım gerekmez). Vitrin: C19 x 1200–1807 kırpımı.

const W = 1080, H = 1920;
const ARKA = "radial-gradient(ellipse at 50% 35%, #16223b 0%, #070b16 100%)";
// C22 levha iç alanları (1080x1920 ölçümü, gözle; levhalar boş)
const LEVHA_D = { mavi: [232, 515, 368, 590], yesil: [444, 470, 588, 552], kahve: [672, 405, 838, 500] } as const;

const DKok: React.FC<{ children: React.ReactNode; arka?: string }> = ({ children, arka = "#05070f" }) => <AbsoluteFill style={{ background: arka, overflow: "hidden" }}>{children}</AbsoluteFill>;

// 16:9 plakayı dikey kareyi kaplayacak biçimde (yükseklik 1920) yerleştirir; kx = kaynak plakada kırpım merkezi x
const YatayPlaka: React.FC<{ ad: string; kx: number; filtre?: string; s?: number }> = ({ ad, kx, filtre, s = 1 }) => {
  const olcek = (H / 1080) * s;
  return <Img src={f(`${ad}.jpg`)} style={{ position: "absolute", width: 1920 * olcek, height: 1080 * olcek, left: W / 2 - kx * olcek, top: H / 2 - 540 * olcek, filter: filtre }} />;
};

const DikeyStudyo: React.FC<{ kareler: [number, number, number, number][]; filtre?: string; children?: React.ReactNode; isik?: { mavi?: number; yesil?: number; kahve?: number } }> = ({ kareler, filtre, children, isik = {} }) => (
  <Kamera kareler={kareler} w={W} h={H} ekranW={W} ekranH={H}>
    <Img src={f("C22.jpg")} style={{ position: "absolute", width: W, height: H, filter: filtre }} />
    {(["mavi", "yesil", "kahve"] as const).map((k) => (
      <LevhaD key={k} ad={k} an={isik[k] ?? -1} />
    ))}
    {children}
  </Kamera>
);

const LevhaD: React.FC<{ ad: keyof typeof LEVHA_D; an: number }> = ({ ad, an }) => {
  const t = useT();
  const [x0, y0, x1, y1] = LEVHA_D[ad];
  const p = interpolate(t, [an - 0.05, an + 0.12], [0, 1], CL);
  const etiket = { mavi: "STOCKS", yesil: "BANK", kahve: "SHOEBOX" }[ad];
  return (
    <div style={{ position: "absolute", left: x0, top: y0, width: x1 - x0, height: y1 - y0, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 30, color: "#fff6dc", textShadow: `0 0 12px ${KAPI_RENK[ad]}, 0 2px 0 #000`, opacity: p, scale: String(0.6 + 0.4 * p) }}>
      {etiket}
    </div>
  );
};

// D-S01 · kapı tanıtımı (Shorts 1)
export const DS01: React.FC = () => {
  const a = anlar("S01");
  const t = useT();
  if (t < 2.1) {
    return (
      <DKok>
        <YatayPlaka ad="C15" kx={820} s={interpolate(t, [0, 2.1], [1, 1.06])} />
        <Yazi an={a("september")} x={460} y={420} boyut={150} renk="#fff3d6">SEPT 1929</Yazi>
        <Illustration />
      </DKok>
    );
  }
  return (
    <DKok>
      <DikeyStudyo kareler={[[2.1, 540, 900, 1.08], [15.6, 540, 880, 1.14]]} isik={{ mavi: a("stock"), yesil: a("bank"), kahve: a("shoebox") }} />
      <Yazi an={a("one")} x={460} y={210} boyut={130} renk={RENK.sari}>
        <Sayac an={a("one")} sure={0.5} bas={0} bit={1000} onEk="$" />
      </Yazi>
      <Yazi an={a("disaster")} x={290} y={1130} boyut={70} renk={RENK.kirmizi} donme={-4}>DISASTER?</Yazi>
      <Yazi an={a("gamble")} x={290} y={1220} boyut={70} renk={RENK.sari} donme={3}>GAMBLE?</Yazi>
      <Yazi an={a("surprise")} x={290} y={1310} boyut={70} renk={KAPI_RENK.yesil} donme={-2}>SURPRISE?</Yazi>
      <Leo id="S01" x={720} y={1450} s={0.62} pozlar={[[0, "a"], [a("three"), "C12"], [8.2, "a"], [a("let's"), "C12"]]} giris={{ an: 2.1, dy: 500, sure: 0.4 }} tohum={3} />
    </DKok>
  );
};

// D-S06 · Kasım 1929: ~yarı; $1,000 → ~$500 (Shorts 1; "NOV 1929" etiketi korunur)
export const DS06: React.FC = () => {
  const a = anlar("S06");
  const t = useT();
  const cubuk = a("on") - 0.2, kasim = a("by") - 0.2, leo = a("stock") - 0.2;
  return (
    <DKok arka={ARKA}>
      <YatayPlaka ad="C16" kx={760} filtre="blur(9px) brightness(0.3) saturate(0.4)" />
      {t < cubuk ? <Takvim x={330} y={300} w={360} adimlar={[[0, "SEP"], [a("october") - 0.1, "OCT"]]} altYazi="1929" /> : null}
      {t >= cubuk && t < kasim ? (
        <Kart an={cubuk} x={60} y={260} w={860} h={900}>
          <div style={{ position: "absolute", left: 30, top: 20, fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.ikincil }}>ONE-DAY DROP IN THE DOW</div>
          <div style={{ position: "absolute", left: 30, top: 80 }}>
            <CubukGrafik an={a("thirteen") - 0.3} arasi={a("twelve") - a("thirteen")} w={800} h={780} maks={14} renk="#8fa6c9" veri={[{ etiket: "OCT 28", deger: 13, ustYazi: "−13%" }, { etiket: "OCT 29", deger: 12, ustYazi: "−12%" }]} />
          </div>
        </Kart>
      ) : null}
      {t >= kasim ? (
        <>
          <Yazi an={kasim} x={460} y={230} boyut={90}>NOV 1929</Yazi>
          <Yazi an={a("half")} x={460} y={340} boyut={64} renk={RENK.ikincil}>DOW: ALMOST HALF GONE</Yazi>
          <Yazi an={leo + 0.2} x={460} y={480} boyut={170} renk={RENK.sari}>
            <Sayac an={a("now")} sure={a("hundred.") - a("now") + 0.3} bas={1000} bit={500} onEk="$" />
          </Yazi>
          <Yazi an={a("hundred.") + 0.1} x={460} y={690} boyut={56} font="fredoka">$1,000 → ~$500</Yazi>
          <Leo x={470} y={1200} s={0.75} pozlar={[[0, "d"]]} rozet={{ etiket: "STOCK", renk: KAPI_RENK.mavi }} giris={{ an: leo, dy: 700, sure: 0.35 }} />
        </>
      ) : null}
      <Kaynak metin="Source: Federal Reserve History" an={cubuk} />
    </DKok>
  );
};

// D-S10 · G2 + iki sonuç (Shorts 1: "≈9,000 SUSPENDED")
export const DS10: React.FC = () => {
  const a = anlar("S10");
  const t = useT();
  const g2 = a("from") - 0.4, kasa = a("for", 2) - 0.2;
  const veri = FDIC.map((r) => ({ etiket: `’${String(r.yil).slice(2)}`, deger: r.banka, vurgu: r.yil >= 1930, ustYazi: r.yil >= 1930 ? r.banka.toLocaleString("en-US") : undefined }));
  return (
    <DKok arka={ARKA}>
      {t < kasa ? (
        <>
          <Yazi an={0} x={460} y={220} boyut={80}>DOOR 2: THE SCORE</Yazi>
          <Kart an={g2} x={40} y={330} w={1000} h={740}>
            <div style={{ position: "absolute", left: 28, top: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil, width: 840 }}>COMMERCIAL BANK SUSPENSIONS PER YEAR, 1921–1933</div>
            <div style={{ position: "absolute", left: 10, top: 100 }}>
              <CubukGrafik an={g2 + 0.2} veri={veri} w={980} h={620} maks={4200} renk={RENK.yesil} vurguAn={a("about")} />
            </div>
          </Kart>
          <Yazi an={a("nine")} x={460} y={1095} boyut={84} renk={RENK.sari}>≈9,000 SUSPENDED</Yazi>
          <Yazi an={a("more")} x={460} y={1200} boyut={48} font="fredoka">1930–33 · MORE THAN 1 IN 3</Yazi>
        </>
      ) : (
        <>
          <YatayPlaka ad="C17" kx={1450} filtre="brightness(0.6)" />
          <Leo x={470} y={1180} s={0.8} pozlar={[[0, "d"], [a("if", 2) - 0.1, "e"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} />
          <Kart an={a("hundred")} x={60} y={240} w={860} h={190} cerceve={RENK.kirmizi}>
            <div style={{ padding: "18px 28px", fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>BANK SUSPENDED: <span style={{ color: RENK.sari }}>~$800 + WAIT</span></div>
          </Kart>
          <Kart an={a("survived,")} x={60} y={460} w={860} h={150} cerceve={RENK.yesil}>
            <div style={{ padding: "18px 28px", fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>BANK SURVIVED: <span style={{ color: RENK.yesil }}>$1,000</span></div>
          </Kart>
          <Damga an={a("gamble.")} x={460} y={780} metin="GAMBLE" />
          <Illustration />
        </>
      )}
      <Kaynak metin="Source: FDIC, Table 5" an={g2} />
    </DKok>
  );
};

// D-S16 · dikey skor kartı + şerit (Shorts 1)
export const DS16: React.FC = () => {
  const a = anlar("S16");
  const t = useT();
  const satir = (y: number, renk: string, baslik: string, an: number, ana: string, alt: React.ReactNode, altAn: number) => (
    <Kart an={an} x={60} y={y} w={860} h={270} cerceve={renk}>
      <div style={{ position: "absolute", left: 0, top: 0, width: 200, height: "100%", background: renk, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 50, color: "#101010" }}>{baslik}</div>
      <div style={{ position: "absolute", left: 230, top: 24, fontFamily: "Anton", fontSize: 96, color: RENK.sari }}>{ana}</div>
      <div style={{ position: "absolute", left: 230, top: 150, width: 610, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.murekkep, lineHeight: 1.2, opacity: interpolate(t, [altAn, altAn + 0.25], [0, 1], CL) }}>{alt}</div>
    </Kart>
  );
  return (
    <DKok arka={ARKA}>
      <Yazi an={0} x={460} y={210} boyut={72}>SCOREBOARD · JULY 1932</Yazi>
      {satir(330, KAPI_RENK.mavi, "STOCK", a("stock") - 0.1, "$108", "price only", a("price"))}
      {satir(620, KAPI_RENK.yesil, "BANK", a("bank") - 0.1, "?", <>If your bank survived: same as the box<br />If your bank suspended: avg. ~$800 left</>, a("maybe"))}
      {satir(910, KAPI_RENK.kahve, "BOX", a("box", 2) - 0.1, "$1,000", "= $1,272 of 1929 goods", a("twelve"))}
      <Kart an={a("decade.")} x={60} y={1210} w={860} h={100} arka={RENK.sari} cerceve="#101010">
        <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 46, color: "#101010", letterSpacing: 2 }}>IN A DECADE OF FALLING PRICES</div>
      </Kart>
      <Kaynak metin="Sources: FRH; FDIC; BLS via FRED" an={2} />
    </DKok>
  );
};

// D-S12 · vitrin (C19 x 1200–1807) + G3 + $1,272 (Shorts 2)
export const DS12: React.FC = () => {
  const a = anlar("S12");
  const t = useT();
  const g3 = a("the", 4) - 0.2, tile = a("so") - 0.2, son = a("box", 3) - 0.2;
  const veri = CPI29.filter((p) => p.ay <= "1932-07").map((p) => ({ x: p.x, y: p.y }));
  const alim = Math.round((1000 * veri[0].y) / veri[veri.length - 1].y);
  if (t < g3 || t >= son) {
    return (
      <DKok>
        <YatayPlaka ad="C19" kx={1503} />
        {t < g3 ? (
          <>
            <Yazi an={a("prices")} x={460} y={240} boyut={96} renk={RENK.sari}>PRICES ARE FALLING</Yazi>
            {[[300, 640], [560, 660], [380, 860], [640, 880], [320, 1080], [600, 1100]].map(([x, y], i) => {
              const k = interpolate(t, [a("falling.") + i * 0.2, a("falling.") + i * 0.2 + 0.5], [1, 0.55], { ...CL, easing: EOUT });
              return <div key={i} style={{ position: "absolute", left: x, top: y, width: 110, height: 70, scale: String(k), background: "#f6f0e2", border: "4px solid #3a2a12", borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 40, color: "#3a2a12" }}>$</div>;
            })}
          </>
        ) : (
          <>
            <Leo x={460} y={1150} s={0.8} pozlar={[[0, "f"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} giris={{ an: son, dy: 600, sure: 0.35 }} />
            <Yazi an={a("stronger.")} x={460} y={300} boyut={96} renk={RENK.sari}>STRONGER MONEY</Yazi>
          </>
        )}
        <Illustration />
      </DKok>
    );
  }
  return (
    <DKok arka={ARKA}>
      {t < tile ? (
        <>
          <Kart an={g3} x={40} y={300} w={1000} h={820}>
            <div style={{ position: "absolute", left: 28, top: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil, width: 860 }}>U.S. CONSUMER PRICES (CPI), MONTHLY</div>
            <div style={{ position: "absolute", left: 10, top: 70 }}>
              <CizgiGrafik an={a("from")} sure={a("thirty-two,") - a("from") + 0.4} w={980} h={730} xAralik={[1929.6, 1932.65]} yAralik={[12, 18]} renk={RENK.kahve} alan noktalar={veri.map((p, i) => (i === 0 ? { ...p, etiket: "SEPT 1929: 17.3", etiketYon: "sag" as const } : i === veri.length - 1 ? { ...p, etiket: "JULY 1932: 13.6", etiketYon: "sol" as const } : p))} eksenX={[1930, 1931, 1932].map((v) => ({ x: v, etiket: String(v) }))} />
            </div>
          </Kart>
          <Yazi an={a("twenty-one")} x={460} y={1170} boyut={110} renk={RENK.sari}>PRICES −21%</Yazi>
          <Yazi an={a("twenty-one") + 0.2} x={460} y={1300} boyut={44} font="fredoka">SEPT 1929 → JULY 1932</Yazi>
        </>
      ) : (
        <Kart an={tile} x={60} y={500} w={860} h={560}>
          <div style={{ position: "absolute", width: "100%", top: 50, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 44, color: RENK.ikincil }}>$1,000 NOW BUYS LIKE</div>
          <div style={{ position: "absolute", width: "100%", top: 140, textAlign: "center", fontFamily: "Anton", fontSize: 220, color: RENK.sari, lineHeight: 1 }}>
            <Sayac an={a("one")} sure={a("dollars", 3) - a("one") + 0.2} bas={1000} bit={alim} onEk="$" />
          </div>
          <div style={{ position: "absolute", width: "100%", top: 420, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: RENK.murekkep }}>IN 1929 PRICES</div>
        </Kart>
      )}
      <Kaynak metin="Source: BLS CPI via FRED" an={g3} />
    </DKok>
  );
};

// D-S20 · 2026: "12 MONTHS TO SEPT 2026" kartı cümle başında; +3.7%; $964 (Shorts 2)
export const DS20: React.FC = () => {
  const a = anlar("S20");
  const t = useT();
  const kucul = interpolate(t, [a("buys"), a("earlier.") + 0.4], [1.4, 1.1], { ...CL, easing: EIO });
  return (
    <DKok>
      <DikeyStudyo kareler={[[0, 540, 960, 1.04], [25.9, 540, 960, 1.1]]} filtre="hue-rotate(-12deg) saturate(0.65) brightness(0.62)" />
      <AbsoluteFill style={{ background: "rgba(40,90,170,0.18)", mixBlendMode: "multiply" }} />
      <Kart an={a("twelve") - 0.1} x={60} y={220} w={860} h={180}>
        <div style={{ position: "absolute", width: "100%", top: 16, textAlign: "center", fontFamily: "Anton", fontSize: 60, color: RENK.murekkep }}>12 MONTHS TO SEPT 2026</div>
        <div style={{ position: "absolute", width: "100%", top: 100, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 44, color: RENK.ikincil }}>2025 → 2026</div>
      </Kart>
      <Yazi an={a("three")} son={a("so") - 0.2} x={460} y={460} boyut={190} renk={RENK.kirmizi}>+3.7%</Yazi>
      <Yazi an={a("percent")} son={a("so") - 0.2} x={460} y={690} boyut={34} font="fredoka" genislik={780}>U.S. CPI, not seasonally adjusted</Yazi>
      <Kart an={a("nine")} x={160} y={470} w={660} h={280}>
        <div style={{ position: "absolute", width: "100%", top: 24, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 38, color: RENK.ikincil }}>$1,000 NOW BUYS LIKE</div>
        <div style={{ position: "absolute", width: "100%", top: 84, textAlign: "center", fontFamily: "Anton", fontSize: 150, color: RENK.sari, lineHeight: 1 }}>
          <Sayac an={a("nine")} sure={0.9} bas={1000} bit={964} onEk="$" />
        </div>
      </Kart>
      <Banknot x={300} y={1000} adet={8} s={kucul} />
      <Leo x={690} y={1200} s={0.62} pozlar={[[0, "e"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} />
      <Yazi an={a("they")} x={460} y={800} boyut={70} renk={RENK.sari}>THEY JUST BUY LESS</Yazi>
      <Kaynak metin="Source: BLS CPI (Sept 2026)" an={a("three")} />
    </DKok>
  );
};

// D-S21 · ayna grafik: üst-alt panel (Shorts 2)
export const DS21: React.FC = () => {
  const a = anlar("S21");
  const t = useT();
  const panel = (y: number, an: number, sure: number, veri: { x: number; y: number }[], renk: string, baslik: string, ay: string, son: string, xa: [number, number], alim: string, alimAn: number) => (
    <Kart an={an - 0.3} x={60} y={y} w={860} h={500}>
      <div style={{ position: "absolute", left: 26, top: 14, fontFamily: "Anton", fontSize: 44, color: renk }}>{baslik}</div>
      <div style={{ position: "absolute", right: 26, top: 24, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>{ay}</div>
      <div style={{ position: "absolute", left: 6, top: 66 }}>
        <CizgiGrafik an={an} sure={sure} w={840} h={360} xAralik={xa} yAralik={[65, 120]} renk={renk} noktalar={veri.map((p, i) => (i === veri.length - 1 ? { ...p, etiket: son, etiketYon: "sol" as const } : p))} yatayCizgi={[{ y: 100, etiket: "START = 100" }]} />
      </div>
      <div style={{ position: "absolute", left: 26, bottom: 14, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.murekkep, opacity: interpolate(t, [alimAn, alimAn + 0.3], [0, 1], CL) }}>{alim}</div>
    </Kart>
  );
  const sol = CPI29_IDX.map((p) => ({ x: p.x, y: p.y })), sag = CPI22_IDX.map((p) => ({ x: p.x, y: p.y }));
  const s1 = sol[sol.length - 1].y, s2 = sag[sag.length - 1].y;
  return (
    <DKok arka={ARKA}>
      <Yazi an={0} son={a("same") - 0.2} x={460} y={200} boyut={70}>SIDE BY SIDE</Yazi>
      <Yazi an={a("same")} son={a("that's") - 0.2} x={460} y={200} boyut={64} renk={RENK.sari}>SAME BOX. OPPOSITE RESULT.</Yazi>
      <Yazi an={a("that's")} x={460} y={200} boyut={64}>ARITHMETIC, NOT A PLAN</Yazi>
      {panel(300, a("from"), a("percent.") - a("from"), sol, RENK.kahve, "SEPT 1929 → MAR 1933", "42 MONTHS", `${s1.toFixed(1)} (${(s1 - 100).toFixed(1)}%)`, [1929.6, 1933.25], `$1,000 buys like $${Math.round(100000 / s1).toLocaleString("en-US")}`, a("cash"))}
      {panel(830, a("from", 2), a("percent.", 2) - a("from", 2), sag, RENK.mavi, "SEPT 2022 → SEPT 2026", "48 MONTHS", `${s2.toFixed(1)} (+${(s2 - 100).toFixed(1)}%)`, [2022.6, 2026.75], `$1,000 buys like $${Math.round(100000 / s2).toLocaleString("en-US")}`, a("rising,"))}
      <Kaynak metin="Source: BLS CPI via FRED, start = 100" an={a("from")} />
    </DKok>
  );
};

// Shorts ek kayıtları (yeni hook / kapanış): konuşan Leo C22 önünde, cümle altyazısı
export const DEk: React.FC<{ ek: "sh1" | "sh2" }> = ({ ek }) => {
  const v = SHORTS_EK[ek];
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const c = v.cumleler.find((x) => t >= x.bas - 0.05 && t < x.son + 0.25);
  return (
    <DKok>
      <Audio src={f(`shorts-${ek === "sh1" ? 1 : 2}-ek.wav`)} />
      <DikeyStudyo kareler={[[0, 540, 900, 1.06], [v.sure, 540, 880, 1.12]]} isik={{ mavi: 0, yesil: 0, kahve: 0 }} />
      <div style={{ position: "absolute", left: 470 - YUZ_T.x * 0.8, top: 1000 - YUZ_T.y * 0.8, scale: "0.8", transformOrigin: "0 0" }}>
        <Sunucu cues={v.agiz} ofs={0} poz="a" tohum={9} rig={RIG_T} />
      </div>
      {c ? (
        <AbsoluteFill style={{ justifyContent: "flex-start", alignItems: "center", paddingTop: 260 }}>
          <div style={{ width: 840, marginRight: 160, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 66, color: "#fff", WebkitTextStroke: "11px #0b0b0b", paintOrder: "stroke fill", textTransform: "uppercase", lineHeight: 1.15 }}>{c.metin}</div>
        </AbsoluteFill>
      ) : null}
      <Doku />
    </DKok>
  );
};

export const DIKEY_SAHNE: Record<string, React.FC> = { S01: DS01, S06: DS06, S10: DS10, S16: DS16, S12: DS12, S20: DS20, S21: DS21 };

// Dikey sahne kompozisyonu: sahnenin anlatım parçası + dikey sahne + altyazı (güvenli alanda)
export const DikeySahneComp: React.FC<{ id: string; altyazi?: boolean }> = ({ id, altyazi = true }) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  const B = DIKEY_SAHNE[id];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas)} />
      <B />
      <Doku />
      {altyazi ? <AltyaziParca ofs={s.bas} alt={420} boyut={64} genislik={760} /> : null}
    </AbsoluteFill>
  );
};
