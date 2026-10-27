import React from "react";
import { interpolate } from "remotion";
import { fredoka, KapiIsik, kapiMerkezX } from "./ortak";
import { anlar, CL, EOUT, Flas, Illustration, Kamera, Kart, Kaynak, KAPI_RENK, Leo, Plaka, POZLAR_T, RENK, SahneKok, Sayac, useT, Yazi } from "./kit";
import { Klon } from "./Klon";

// Bölüm 1 — The Game (S01–S04)

const KLON = { klasor: "k1929t", pozlar: POZLAR_T };

// S01 · HOOK: sepya sokak → stüdyo, $1,000, üç kapı, DISASTER? GAMBLE? SURPRISE?, "Let's play"
export const S01: React.FC = () => {
  const t = useT();
  const a = anlar("S01");
  const ST = 2.1;
  const sokak = t < ST;
  const uc = a("three");
  const lets = a("let's");
  return (
    <SahneKok>
      {sokak ? (
        <>
          <Kamera kareler={[[0, 1000, 520, 1.0], [ST, 1000, 520, 1.07]]}>
            <Plaka ad="C15" />
          </Kamera>
          <Yazi an={a("september")} x={960} y={330} boyut={190} renk="#fff3d6">
            SEPT 1929
          </Yazi>
          <Illustration />
        </>
      ) : (
        <>
          <Kamera kareler={[[ST, 1047, 582, 1.1], [7.9, 1047, 582, 1.14], [8.4, 1000, 560, 1.02], [13.9, 980, 560, 1.05], [14.5, 940, 520, 1.16], [15.6, 940, 520, 1.18]]}>
            <Plaka ad="C01" />
            <KapiIsik ad="mavi" an={a("stock") - 0} />
            <KapiIsik ad="yesil" an={a("bank")} />
            <KapiIsik ad="kahve" an={a("shoebox")} />
            <KapiIsik ad="mavi" an={lets} yaziHazir />
            <KapiIsik ad="yesil" an={lets + 0.08} yaziHazir />
            <KapiIsik ad="kahve" an={lets + 0.16} yaziHazir />
          </Kamera>
          <Leo id="S01" x={interpolate(t, [7.9, 8.4], [1640, 1700], { ...CL, easing: EOUT })} y={interpolate(t, [7.9, 8.4], [352, 420], { ...CL, easing: EOUT })} s={interpolate(t, [7.9, 8.4], [1.0, 0.86], { ...CL, easing: EOUT })} pozlar={[[0, "a"], [uc, "C12"], [8.2, "a"], [lets, "C12"]]} tohum={3} />
          <BinDolarHud an={a("one")} kose={uc - 0.2} />
          <Yazi an={a("disaster")} son={lets - 0.3} x={560} y={110} boyut={92} renk={RENK.kirmizi} donme={-4}>DISASTER?</Yazi>
          <Yazi an={a("gamble")} son={lets - 0.3} x={960} y={170} boyut={92} renk={RENK.sari} donme={3}>GAMBLE?</Yazi>
          <Yazi an={a("surprise")} son={lets - 0.3} x={1300} y={100} boyut={92} renk={KAPI_RENK.yesil} donme={-2}>SURPRISE?</Yazi>
          <Flas an={ST} />
        </>
      )}
    </SahneKok>
  );
};

// "$1,000": ortada sayaç gibi dolar, sonra köşe göstergesine küçülür (SEPT 1929 ile)
const BinDolarHud: React.FC<{ an: number; kose: number }> = ({ an, kose }) => {
  const t = useT();
  const k = interpolate(t, [kose, kose + 0.3], [0, 1], { ...CL, easing: EOUT });
  const p = interpolate(t, [an - 0.04, an + 0.14], [0, 1], CL);
  if (t < an - 0.05) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: interpolate(k, [0, 1], [700, 60]),
        top: interpolate(k, [0, 1], [330, 34]),
        translate: `${interpolate(k, [0, 1], [-50, 0])}% 0%`,
        fontFamily: "Anton",
        fontSize: interpolate(k, [0, 1], [250, 92]),
        color: RENK.sari,
        WebkitTextStroke: `${interpolate(k, [0, 1], [16, 8])}px #120c02`,
        paintOrder: "stroke fill",
        opacity: p,
        scale: String(0.6 + 0.4 * p),
        lineHeight: 1,
        whiteSpace: "nowrap",
        display: "flex",
        alignItems: "baseline",
        gap: 24,
      }}
    >
      <Sayac an={an} sure={0.5} bas={0} bit={1000} onEk="$" />
      <span style={{ fontSize: "0.42em", color: "#fff3d6", opacity: k }}>SEPT 1929</span>
    </div>
  );
};

// S02 · "I'm Leo": C03 orta plan, takvim 1929↔2026, soru ve üç madde ekranda
export const S02: React.FC = () => {
  const a = anlar("S02");
  const t = useT();
  const soru = a("where");
  return (
    <SahneKok>
      <Kamera kareler={[[0, 1000, 540, 1.04], [soru - 0.3, 1060, 520, 1.07], [soru + 0.3, 1290, 420, 1.13], [19.3, 1290, 420, 1.15]]}>
        <Plaka ad="C03" />
        {/* ekran içi (C03-ekran-kursu.json: 829,189 – 1760,633) */}
        <div style={{ position: "absolute", left: 829, top: 189, width: 931, height: 444, overflow: "hidden" }}>
          <div style={{ position: "absolute", left: 330, top: 26, opacity: interpolate(t, [soru - 0.3, soru], [1, 0], CL) }}>
            <TakvimEkran adimlar={[[0, "1929"], [a("real"), "2026"], [a("people"), "1929"]]} />
          </div>
          <EkranYazi an={soru} y={60} boyut={64}>WHERE WAS MONEY SAFE</EkranYazi>
          <EkranYazi an={a("nineteen", 2)} y={140} boyut={64} renk={RENK.sari}>IN 1929?</EkranYazi>
          <EkranYazi an={a("which")} y={252} boyut={40} font="fredoka">WHICH DOOR WON</EkranYazi>
          <EkranYazi an={a("why")} y={304} boyut={40} font="fredoka">WHY</EkranYazi>
          <EkranYazi an={a("why", 2)} y={356} boyut={40} font="fredoka">WHY IT FLIPS TODAY</EkranYazi>
        </div>
      </Kamera>
      <Leo id="S02" x={interpolate(t, [soru - 0.3, soru + 0.3], [450, 330], { ...CL, easing: EOUT })} y={330} s={0.95} pozlar={[[0, "a"], [a("cartoon") - 0.15, "balt"], [a("people") - 0.2, "a"], [a("by") - 0.1, "C12"], [17.0, "a"]]} tohum={4} />
    </SahneKok>
  );
};

const EkranYazi: React.FC<{ an: number; y: number; boyut: number; children: React.ReactNode; renk?: string; font?: "anton" | "fredoka" }> = ({ an, y, boyut, children, renk, font }) => (
  <Yazi an={an} x={465} y={y} boyut={boyut} renk={renk} font={font} kontur={font === "fredoka" ? 7 : undefined}>
    {children}
  </Yazi>
);

const TakvimEkran: React.FC<{ adimlar: [number, string][] }> = ({ adimlar }) => {
  const t = useT();
  let i = 0;
  for (let k = 0; k < adimlar.length; k++) if (t >= adimlar[k][0]) i = k;
  const p = interpolate(t, [adimlar[i][0], adimlar[i][0] + 0.18], [0, 1], CL);
  return (
    <div style={{ width: 270, height: 380, background: "#f6f0e2", borderRadius: 14, border: "5px solid #1b1b1b", overflow: "hidden", boxShadow: "0 12px 30px rgba(0,0,0,0.5)" }}>
      <div style={{ height: 70, background: RENK.kirmizi, borderBottom: "5px solid #1b1b1b" }} />
      <div style={{ textAlign: "center", fontFamily: "Anton", fontSize: 110, color: "#1b1b1b", marginTop: 70, scale: `1 ${0.2 + 0.8 * p}`, transformOrigin: "50% 0%" }}>{adimlar[i][1]}</div>
    </div>
  );
};

// S03 · tez + G0 maaş grafiği
export const S03: React.FC = () => {
  const a = anlar("S03");
  const t = useT();
  const g0 = a("now");
  const sekiz = a("eight");
  return (
    <SahneKok>
      <Kamera kareler={[[0, 960, 540, 1.04], [21.2, 960, 540, 1.1]]}>
        <Plaka ad="C03" filtre="blur(8px) brightness(0.55)" />
      </Kamera>
      {/* tez: tek satır, iki parça */}
      <div style={{ opacity: interpolate(t, [g0 - 0.3, g0], [1, 0], CL) }}>
        <Yazi an={a("safe")} x={1220} y={300} boyut={96}>SAFE ISN&apos;T A PLACE.</Yazi>
        <Yazi an={a("depends")} x={1220} y={420} boyut={96} renk={RENK.sari}>IT DEPENDS ON PRICES.</Yazi>
      </div>
      {/* G0: yıllık ortalama tam zamanlı ücret = 12 ay; 1.000 $ ≈ 8 ay */}
      <Kart an={g0} x={760} y={150} w={1040} h={620}>
        <div style={{ position: "absolute", left: 40, top: 26, fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.ikincil }}>HOW BIG IS $1,000 IN 1929?</div>
        <Yazi an={a("average")} x={40} y={86} boyut={52} hiza="sol" font="fredoka" kontur={6}>
          AVG. FULL-TIME PAY, 1929: <span style={{ color: RENK.sari }}>$1,430/yr</span>
        </Yazi>
        <AyKutulari an={a("year.")} dolu={sekiz} x={40} y={210} />
        <Yazi an={sekiz} x={520} y={440} boyut={86} renk={RENK.sari}>$1,000 ≈ 8 MONTHS</Yazi>
      </Kart>
      <Kaynak metin="Source: BEA, NIPA Table 6.6A" an={g0 + 0.3} />
      <Leo id="S03" x={430} y={340} s={0.92} pozlar={[[0, "a"], [g0, "C13"], [a("you", 1) - 0.1, "a"]]} tohum={6} giris={{ an: 0, dx: -60, sure: 0.4 }} />
    </SahneKok>
  );
};

const AyKutulari: React.FC<{ an: number; dolu: number; x: number; y: number }> = ({ an, dolu, x, y }) => {
  const t = useT();
  const aylar = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"];
  return (
    <div style={{ position: "absolute", left: x, top: y, display: "flex", gap: 10 }}>
      {aylar.map((m, i) => {
        const p = interpolate(t, [an + i * 0.05, an + i * 0.05 + 0.2], [0, 1], CL);
        const d = i < 8 ? interpolate(t, [dolu + i * 0.06, dolu + i * 0.06 + 0.15], [0, 1], CL) : 0;
        return (
          <div key={i} style={{ width: 70, height: 170, borderRadius: 10, border: "3px solid rgba(255,255,255,0.4)", position: "relative", opacity: p, overflow: "hidden" }}>
            <div style={{ position: "absolute", bottom: 0, width: "100%", height: `${d * 100}%`, background: RENK.yesil }} />
            <div style={{ position: "absolute", bottom: 8, width: "100%", textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 26, color: RENK.murekkep }}>{m}</div>
          </div>
        );
      })}
    </div>
  );
};

// S04 · kurallar + 3 klon kapılara (H4) + "Remember that laugh" wink + mavi kapıya punch-in
export const S04: React.FC = () => {
  const a = anlar("S04");
  const t = useT();
  const kahkaha = a("laughs");
  const yakin = a("remember") - 0.1;
  const kapi1 = a("door", 4) - 0.1; // "Door one goes first"
  const AYAK = 792, BOY = 410, GIRIS = 2060;
  const pb = kahkaha - 0.25;
  if (t >= yakin && t < kapi1) {
    return (
      <SahneKok>
        <Kamera kareler={[[yakin, 1290, 420, 1.1], [kapi1, 1290, 420, 1.13]]}>
          <Plaka ad="C03" filtre="blur(7px) brightness(0.78)" />
        </Kamera>
        <Leo id="S04" x={1010} y={420} s={interpolate(t, [yakin, kapi1], [1.06, 1.1])} pozlar={[[0, "a"]]} tohum={2} wink={[a("laugh.") + 0.2, a("laugh.") + 0.58]} />
      </SahneKok>
    );
  }
  const kam: [number, number, number, number][] =
    t < yakin
      ? [[0, 960, 560, 1.0], [pb, 960, 560, 1.035], [pb + 0.4, kapiMerkezX("kahve"), 600, 1.42]]
      : [[kapi1, 960, 560, 1.05], [kapi1 + 0.6, kapiMerkezX("mavi"), 540, 1.55], [23.8, kapiMerkezX("mavi"), 520, 1.65]];
  return (
    <SahneKok>
      <Kamera kareler={kam}>
        <Plaka ad="C01" />
        <KapiIsik ad="mavi" an={t < yakin ? a("blue") + 0.1 : kapi1} yaziHazir parlama={t < yakin ? 1 : 1.4} />
        <KapiIsik ad="yesil" an={a("green") + 0.1} yaziHazir />
        <KapiIsik ad="kahve" an={a("brown") + 0.1} yaziHazir />
        <Klon {...KLON} yurume="C04" durus="C02" xBas={GIRIS} xBit={kapiMerkezX("mavi")} bas={a("stock") - 0.15} bit={a("stock") + 3.0} ayakY={AYAK} boy={BOY} rozet={{ etiket: "STOCK", renk: KAPI_RENK.mavi }} isim={{ metin: "STOCK LEO", an: a("stock"), son: a("stock") + 3.3 }} tohum={0.4} />
        <Klon {...KLON} yurume="C04" durus="C02" xBas={GIRIS} xBit={kapiMerkezX("yesil")} bas={a("bank") - 0.15} bit={a("bank") + 2.45} ayakY={AYAK} boy={BOY} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} isim={{ metin: "BANK LEO", an: a("bank"), son: a("bank") + 2.8 }} tohum={1.3} />
        <Klon {...KLON} yurume="C05" durus="C05" xBas={GIRIS} xBit={kapiMerkezX("kahve")} bas={a("box") - 0.25} bit={a("box") + 2.4} ayakY={AYAK} boy={BOY} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} isim={{ metin: "BOX LEO", an: a("box"), son: a("box") + 3.2 }} ezil={kahkaha} tohum={2.1} />
      </Kamera>
      {/* kural kartları (pop) */}
      <Kart an={a("switch")} son={a("each") - 0.2} x={260} y={180} w={640} h={150} donme={-2}>
        <KuralYazi no="1" metin="NO SWITCHING" />
      </Kart>
      <Kart an={a("future.")} son={a("each") - 0.2} x={1020} y={360} w={680} h={150} donme={2}>
        <KuralYazi no="2" metin="NO CRYSTAL BALL" />
      </Kart>
      <HaHa an={kahkaha + 0.05} son={yakin - 0.2} />
      {t >= kapi1 ? (
        <Yazi an={a("smartest")} x={960} y={110} boyut={84} renk={RENK.sari}>
          THE SMARTEST CHOICE?
        </Yazi>
      ) : null}
    </SahneKok>
  );
};

const KuralYazi: React.FC<{ no: string; metin: string }> = ({ no, metin }) => (
  <div style={{ display: "flex", alignItems: "center", height: "100%", padding: "0 30px", gap: 22, fontFamily: "Anton", fontSize: 62, color: RENK.murekkep }}>
    <span style={{ color: RENK.sari }}>RULE {no}:</span> {metin}
  </div>
);

const HaHa: React.FC<{ an: number; son: number }> = ({ an, son }) => {
  const t = useT();
  const yer: [number, number, number][] = [[470, 250, -9], [1420, 210, 7], [560, 640, 6], [1480, 620, -6]];
  return (
    <>
      {yer.map(([x, y, r], i) => (
        <Yazi key={i} an={an + i * 0.32} son={son} x={x} y={y} boyut={78} font="fredoka" donme={r + Math.sin(t * 9 + i) * 3}>
          HA!
        </Yazi>
      ))}
    </>
  );
};
