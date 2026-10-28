import React from "react";
import { AbsoluteFill, interpolate } from "remotion";
import { fredoka, KAPI, KapiIsik, kapiMerkezX } from "./ortak";
import {
  anlar, Banknot, CizgiGrafik, CL, CubukGrafik, EIO, EOUT, Harita, HARITA_W, Illustration, Kamera, Kart, Kaynak, KAPI_RENK, Kilit, Leo, Plaka, POZLAR_T, RENK, SahneKok, Sayac, Takvim, useT, Yazi,
} from "./kit";
import { Klon } from "./Klon";
import { SigortaKutusu } from "./b2";
import { CPI22_IDX, CPI29_IDX, FDIC } from "./veri-grafik";

// Bölüm 5 sonu – 8 (S17–S24): March 1933, The Twist 2026, What the Game Really Tests

const ARKA_GRAFIK = "radial-gradient(ellipse at 50% 40%, #16223b 0%, #070b16 100%)";
const kapiY = (ad: keyof typeof KAPI) => KAPI[ad].panel[1] + KAPI[ad].panel[3] * 0.5;
const KLON = { klasor: "k1929t", pozlar: POZLAR_T };

const Studyo: React.FC<{ kareler: [number, number, number, number][]; filtre?: string; children?: React.ReactNode }> = ({ kareler, filtre, children }) => (
  <Kamera kareler={kareler}>
    <Plaka ad="C01" filtre={filtre} />
    <KapiIsik ad="mavi" an={-1} yaziHazir parlama={0} />
    <KapiIsik ad="yesil" an={-1} yaziHazir parlama={0} />
    <KapiIsik ad="kahve" an={-1} yaziHazir parlama={0} />
    {children}
  </Kamera>
);

// S17 · yeniden kanca: üç kapıya zincir + kilit, "MARCH 1933"
export const S17: React.FC = () => {
  const a = anlar("S17");
  return (
    <SahneKok>
      <Studyo kareler={[[0, 960, 560, 1.0], [6.8, 940, 560, 1.06]]}>
        <Kilit an={a("every") - 0.05} x={kapiMerkezX("mavi")} y={kapiY("mavi")} />
        <Kilit an={a("door") - 0.05} x={kapiMerkezX("yesil")} y={kapiY("yesil")} />
        <Kilit an={a("locked.") - 0.05} x={kapiMerkezX("kahve")} y={kapiY("kahve")} />
      </Studyo>
      <Yazi an={a("march")} x={760} y={70} boyut={110} renk={RENK.sari}>MARCH 1933</Yazi>
      <Leo id="S17" x={1700} y={420} s={0.86} pozlar={[[0, "a"], [a("locked.", 1, true) + 0.05, "d"]]} tohum={17} />
    </SahneKok>
  );
};

// S18 · panik eyaletten eyalete; otel notu; 4 Mart tüm eyaletler; 6 Mart ulusal tatil; kilitli kasa; evde nakit; ~4.000 açılmadı; FDIC
export const S18: React.FC = () => {
  const a = anlar("S18");
  const t = useT();
  const kasa = a("bank", 3) - 0.2; // "Bank Leo stands at a locked door"
  const nakit = a("for", 2) - 0.2; // "For a few days, cash at home"
  const son = a("when") - 0.2;
  if (t >= kasa && t < nakit) {
    return (
      <SahneKok>
        <Kamera kareler={[[kasa, 1450, 520, 1.0], [nakit, 1500, 520, 1.05]]}>
          <Plaka ad="C17" filtre="brightness(0.7)" />
          <Kilit an={kasa + 0.15} x={1570} y={540} olcek={1.5} />
        </Kamera>
        <Leo x={560} y={390} s={0.85} pozlar={[[0, "e"]]} rozet={{ etiket: "BANK", renk: KAPI_RENK.yesil }} />
        <Yazi an={kasa + 0.2} x={1450} y={110} boyut={70}>LOCKED</Yazi>
        <Illustration />
      </SahneKok>
    );
  }
  if (t >= nakit && t < son) {
    return (
      <SahneKok>
        <Kamera kareler={[[nakit, 1100, 560, 1.04], [son, 1000, 560, 1.08]]}>
          <Plaka ad="C15" />
          <Klon {...KLON} yurume="C05" durus="C05" xBas={1500} xBit={700} bas={nakit} bit={son - 0.2} ayakY={900} boy={360} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} tohum={3} />
        </Kamera>
        <Yazi an={a("cash")} x={960} y={110} boyut={80} renk={RENK.sari}>CASH AT HOME: USEFUL</Yazi>
        <Yazi an={a("only")} x={960} y={210} boyut={46} font="fredoka">THE ONLY PLAYER HOLDING ANY</Yazi>
        <Illustration />
      </SahneKok>
    );
  }
  if (t >= son) {
    return (
      <SahneKok arka={ARKA_GRAFIK}>
        <Yazi an={a("four")} x={960} y={110} boyut={96} renk={RENK.kirmizi}>~4,000 BANKS NEVER REOPENED</Yazi>
        <Yazi an={a("june")} x={960} y={300} boyut={70}>JUNE 16, 1933: BANKING ACT</Yazi>
        <SigortaKutusu an={a("creates")} x={640} y={420} isaret isaretAn={a("insurance.")} />
        <Yazi an={a("january")} x={960} y={620} boyut={60} renk={RENK.yesil}>JAN 1, 1934: DEPOSITS INSURED</Yazi>
        <Yazi an={a("two", 2)} x={960} y={710} boyut={80} renk={RENK.sari}>UP TO $2,500 PER DEPOSITOR</Yazi>
        <Kaynak metin="Source: FDIC, A Brief History of Deposit Insurance" />
      </SahneKok>
    );
  }
  // harita: batıdan doğuya gri dalga (4 Mart'a kadar her eyalet tatil ilan etti); eyalet sınırları gösterilmez
  const bas = a("panic"), bitis = a("march") + 0.4;
  const hepsi = a("good");
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      <div style={{ position: "absolute", left: 60, top: 200, scale: "1.06", transformOrigin: "0 0" }}>
        <Harita
          noktaRengi={(n) => {
            const gri = bas + (n.x / HARITA_W) * (bitis - bas) + n.r * 0.5;
            if (t > hepsi + n.r * 0.6) return "rgba(255,255,255,0.05)";
            return t > gri ? "#56606f" : "#9fb3d1";
          }}
        />
      </div>
      <Yazi an={0} x={960} y={50} boyut={80}>WINTER 1933</Yazi>
      <Yazi an={bas} x={960} y={140} boyut={44} font="fredoka">PANIC JUMPS FROM STATE TO STATE</Yazi>
      {/* otel notu kartı */}
      <Kart an={a("notes")} son={a("by") - 0.2} x={1260} y={330} w={620} h={300} arka="#f6f0e2" cerceve="#1b1b1b" donme={-3}>
        <div style={{ padding: "26px 32px", fontFamily: fredoka, fontWeight: 700, color: "#1b1b1b" }}>
          <div style={{ fontSize: 32, letterSpacing: 2, color: "#7a5a2a" }}>NOTICE TO GUESTS</div>
          <div style={{ fontSize: 52, lineHeight: 1.1, marginTop: 14 }}>OUT-OF-TOWN CHECKS NOT ACCEPTED</div>
        </div>
      </Kart>
      <Yazi an={a("march")} son={a("two") - 0.2} x={1600} y={380} boyut={56} renk={RENK.sari}>BY MARCH 4:</Yazi>
      <Yazi an={a("every")} son={a("two") - 0.2} x={1600} y={450} boyut={56} renk={RENK.sari}>EVERY STATE</Yazi>
      <Yazi an={a("two")} x={1600} y={380} boyut={60} renk={RENK.kirmizi}>MARCH 6:</Yazi>
      <Yazi an={a("two") + 0.15} x={1600} y={455} boyut={48} renk={RENK.kirmizi}>NATIONWIDE BANK HOLIDAY</Yazi>
      <Radyo an={a("franklin")} />
      <Yazi an={hepsi} x={1600} y={720} boyut={38} font="fredoka">GOOD BANKS AND BAD BANKS: ALL SHUT</Yazi>
      <Kaynak metin="Source: FDIC · map shows the spread, not exact states" an={bas} />
    </SahneKok>
  );
};

// Roosevelt: gerçekçi yüz yok — yalnız radyo silueti + ekran yazısı (K5)
const Radyo: React.FC<{ an: number }> = ({ an }) => {
  const t = useT();
  const p = interpolate(t, [an, an + 0.3], [0, 1], { ...CL, easing: EOUT });
  if (p <= 0) return null;
  return (
    <div style={{ position: "absolute", left: 1330, top: 560, opacity: p, display: "flex", alignItems: "center", gap: 20 }}>
      <svg width={120} height={110}>
        <path d="M20,30 Q60,0 100,30" stroke="#c9ccd2" strokeWidth={6} fill="none" />
        <rect x={10} y={30} width={100} height={72} rx={14} fill="#5a3d20" stroke="#1b1b1b" strokeWidth={5} />
        <circle cx={40} cy={66} r={18} fill="#2a1d10" />
        {[0, 1, 2].map((i) => <rect key={i} x={68} y={50 + i * 12} width={30} height={5} rx={2} fill="#2a1d10" />)}
      </svg>
      <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.murekkep, lineHeight: 1.15 }}>NEW PRESIDENT<br />FRANKLIN ROOSEVELT</div>
    </div>
  );
};

// S19 · 1934: 61 askıya alma, 9 sigortalı; çalışan kilit; Box Leo kazanır; kapı 2026'ya kayar
export const S19: React.FC = () => {
  const a = anlar("S19");
  const t = useT();
  const kilit = a("the") - 0.1;
  const kazan = a("so") - 0.2;
  const haksiz = a("now") - 0.2;
  const kapi = a("let's", 2) - 0.2;
  if (t < kilit) {
    const v = FDIC.filter((r) => r.yil >= 1930).map((r) => ({ etiket: String(r.yil), deger: r.banka, ustYazi: r.banka.toLocaleString("en-US") }));
    return (
      <SahneKok arka={ARKA_GRAFIK}>
        <Kart an={0} x={260} y={110} w={1400} h={650}>
          <div style={{ position: "absolute", left: 36, top: 20, fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>BANK SUSPENSIONS PER YEAR</div>
          <div style={{ position: "absolute", left: 60, top: 70 }}>
            <CubukGrafik an={0} arasi={0.02} w={1280} h={560} maks={4200} renk={RENK.yesil} veri={[...v, { etiket: "1934", deger: 61, ustYazi: "61", vurgu: true, renk: RENK.sari }]} />
          </div>
          <Yazi an={a("nine")} x={560} y={160} boyut={58} renk={RENK.sari}>1934: 9 INSURED BANKS</Yazi>
          <Yazi an={a("suspended.")} x={560} y={240} boyut={40} font="fredoka">SUSPENDED (OF 61 IN ALL)</Yazi>
        </Kart>
        <Kaynak metin="Source: FDIC, A Brief History of Deposit Insurance (Table 5; p. 31)" />
      </SahneKok>
    );
  }
  if (t < kazan) {
    return (
      <SahneKok>
        <Studyo kareler={[[kilit, kapiMerkezX("yesil"), 540, 1.7], [kazan, kapiMerkezX("yesil"), 540, 1.78]]}>
          <Kilit an={kilit + 0.1} x={kapiMerkezX("yesil")} y={kapiY("yesil")} modern={interpolate(t, [a("lock"), a("lock") + 0.5], [0, 1], CL)} />
        </Studyo>
        <Yazi an={a("works.")} x={430} y={460} boyut={80} renk={KAPI_RENK.yesil}>A LOCK THAT WORKS</Yazi>
      </SahneKok>
    );
  }
  if (t < haksiz) {
    return (
      <SahneKok>
        <Studyo kareler={[[kazan, kapiMerkezX("kahve"), 560, 1.75], [haksiz, kapiMerkezX("kahve"), 540, 1.82]]} />
        <Leo x={760} y={400} s={0.85} pozlar={[[0, "f"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} giris={{ an: kazan, dy: 500, sure: 0.35 }} />
        <Yazi an={a("wins")} x={1420} y={200} boyut={80} renk={RENK.sari}>BOX WINS 1929</Yazi>
        <Yazi an={a("same")} x={1420} y={310} boyut={48} font="fredoka">SAME GAIN IN BUYING POWER</Yazi>
        <Yazi an={a("without")} x={1420} y={380} boyut={48} font="fredoka">WITHOUT THE GAMBLE</Yazi>
      </SahneKok>
    );
  }
  if (t < kapi) {
    return (
      <SahneKok>
        <Kamera kareler={[[haksiz, 1000, 540, 1.04], [kapi, 900, 480, 1.1]]}>
          <Plaka ad="C03" />
        </Kamera>
        <Leo id="S19" x={450} y={330} s={0.95} pozlar={[[0, "balt"]]} tohum={19} />
        <Yazi an={a("unfair.")} x={1290} y={300} boyut={90} renk={RENK.sari}>SOMETHING UNFAIR</Yazi>
      </SahneKok>
    );
  }
  // kahve kapı raylarda kayar, takvim 1933 → 2026
  const [x0, y0, x1, y1] = KAPI.kahve.kasa;
  const kay = interpolate(t, [a("move") - 0.2, a("today.") + 0.3], [0, 1], { ...CL, easing: EIO });
  return (
    <SahneKok>
      <Studyo kareler={[[kapi, 1050, 540, 1.05], [17.7, 1100, 540, 1.08]]}>
        <div style={{ position: "absolute", left: x0, top: y0, width: x1 - x0, height: y1 - y0, background: "#05070f" }} />
        <div style={{ position: "absolute", left: x0 + kay * 700, top: y0, width: x1 - x0, height: y1 - y0, overflow: "hidden", boxShadow: "0 20px 40px rgba(0,0,0,0.6)" }}>
          <div style={{ position: "absolute", left: -x0, top: -y0 }}>
            <Plaka ad="C01" />
          </div>
        </div>
        <div style={{ position: "absolute", left: 700, top: 760, width: 1200, height: 10, background: "#9aa3b3", opacity: interpolate(t, [kapi, kapi + 0.3], [0, 1], CL) }} />
      </Studyo>
      <Takvim x={90} y={560} w={260} adimlar={[[0, "1933"], [a("today."), "2026"]]} />
    </SahneKok>
  );
};

// S20 · aynı kutu, 2026: TÜFE +3.7% (12 ay, Eyl 2026, NSA); $1,000 ≈ $964; banknotlar küçülür, sayı aynı
export const S20: React.FC = () => {
  const a = anlar("S20");
  const t = useT();
  const kucul = interpolate(t, [a("buys"), a("earlier.") + 0.4], [1.25, 1.0], { ...CL, easing: EIO });
  const SOGUK = "hue-rotate(-12deg) saturate(0.65) brightness(0.72) contrast(1.05)";
  return (
    <SahneKok>
      <Kamera kareler={[[0, 960, 540, 1.04], [25.9, 1000, 540, 1.1]]}>
        <Plaka ad="C03" filtre={SOGUK} />
      </Kamera>
      <AbsoluteFill style={{ background: "rgba(40,90,170,0.18)", mixBlendMode: "multiply" }} />
      <Leo x={1660} y={410} s={0.8} pozlar={[[0, "e"]]} rozet={{ etiket: "BOX", renk: KAPI_RENK.kahve }} />
      <Banknot x={520} y={660} adet={8} s={kucul} />
      <Yazi an={a("thousand")} x={520} y={410} boyut={96} renk={RENK.sari}>$1,000</Yazi>
      <Takvim x={110} y={110} w={220} adimlar={[[0, "2025"], [a("twelve"), "2026"]]} altYazi="SEPT" />
      <Kart an={a("twelve")} x={380} y={110} w={740} h={110}>
        <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 52, color: RENK.murekkep }}>12 MONTHS TO SEPT 2026</div>
      </Kart>
      <Yazi an={a("three")} son={a("so") - 0.2} x={1050} y={250} boyut={170} renk={RENK.kirmizi}>+3.7%</Yazi>
      <Yazi an={a("percent")} son={a("so") - 0.2} x={1050} y={450} boyut={34} font="fredoka" genislik={560}>CPI, 12 MONTHS TO SEPT 2026 (not seasonally adjusted)</Yazi>
      <Kart an={a("nine")} x={780} y={250} w={560} h={250}>
        <div style={{ position: "absolute", width: "100%", top: 24, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: RENK.ikincil }}>$1,000 NOW BUYS LIKE</div>
        <div style={{ position: "absolute", width: "100%", top: 80, textAlign: "center", fontFamily: "Anton", fontSize: 130, color: RENK.sari, lineHeight: 1 }}>
          <Sayac an={a("nine")} sure={0.9} bas={1000} bit={964} onEk="$" />
        </div>
      </Kart>
      <Yazi an={a("nothing")} x={520} y={800} boyut={40} font="fredoka">NOTHING STOLEN · SAME BILLS</Yazi>
      <Yazi an={a("they")} x={1060} y={600} boyut={64} renk={RENK.sari}>THEY JUST BUY LESS</Yazi>
      <Kaynak metin="Source: BLS CPI (Sept 2026 release); FRED CPIAUCNS" an={a("three")} />
    </SahneKok>
  );
};

// S21 · G5 ayna: 1929–33 (42 ay) ve 2022–26 (48 ay), başlangıç = 100, aynı ölçek
export const S21: React.FC = () => {
  const a = anlar("S21");
  const t = useT();
  const panel = (x: number, an: number, sure: number, veri: { x: number; y: number }[], renk: string, baslik: string, ay: string, sonEtiket: string, alim: string, alimAn: number, xa: [number, number], eksen: { x: number; etiket: string }[]) => (
    <Kart an={an - 0.3} x={x} y={130} w={760} h={540}>
      <div style={{ position: "absolute", left: 28, top: 16, fontFamily: "Anton", fontSize: 44, color: renk }}>{baslik}</div>
      <div style={{ position: "absolute", right: 28, top: 26, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>{ay}</div>
      <div style={{ position: "absolute", left: 6, top: 64 }}>
        <CizgiGrafik
          an={an}
          sure={sure}
          w={740}
          h={420}
          xAralik={xa}
          yAralik={[65, 120]}
          renk={renk}
          noktalar={veri.map((p, i) => (i === veri.length - 1 ? { ...p, etiket: sonEtiket, etiketYon: "sol" as const } : p))}
          yatayCizgi={[{ y: 100, etiket: "START = 100" }]}
          eksenX={eksen}
        />
      </div>
      <div style={{ position: "absolute", left: 28, bottom: 18, fontFamily: fredoka, fontWeight: 700, fontSize: 32, color: RENK.murekkep, opacity: interpolate(t, [alimAn, alimAn + 0.3], [0, 1], CL) }}>{alim}</div>
    </Kart>
  );
  const sol = CPI29_IDX.map((p) => ({ x: p.x, y: p.y }));
  const sag = CPI22_IDX.map((p) => ({ x: p.x, y: p.y }));
  const solSon = sol[sol.length - 1].y, sagSon = sag[sag.length - 1].y;
  return (
    <SahneKok arka={ARKA_GRAFIK}>
      {panel(120, a("from"), a("percent.") - a("from"), sol, RENK.kahve, "SEPT 1929 → MAR 1933", "42 MONTHS", `${solSon.toFixed(1)} (${(solSon - 100).toFixed(1)}%)`, `$1,000 buys like $${Math.round(100000 / solSon).toLocaleString("en-US")}`, a("cash"), [1929.6, 1933.25], [{ x: 1930, etiket: "1930" }, { x: 1932, etiket: "1932" }])}
      {panel(1040, a("from", 2), a("percent.", 2) - a("from", 2), sag, RENK.mavi, "SEPT 2022 → SEPT 2026", "48 MONTHS", `${sagSon.toFixed(1)} (+${(sagSon - 100).toFixed(1)}%)`, `$1,000 buys like $${Math.round(100000 / sagSon).toLocaleString("en-US")}`, a("rising,"), [2022.6, 2026.75], [{ x: 2023, etiket: "2023" }, { x: 2025, etiket: "2025" }])}
      <Yazi an={0} son={a("same") - 0.2} x={960} y={20} boyut={80}>SIDE BY SIDE</Yazi>
      <Yazi an={a("same")} son={a("that's") - 0.2} x={960} y={20} boyut={80} renk={RENK.sari}>SAME BOX. OPPOSITE RESULT.</Yazi>
      <Yazi an={a("that's")} x={960} y={20} boyut={80}>ARITHMETIC, NOT A PLAN</Yazi>
      <Leo id="S21" x={960} y={interpolate(t, [0, 0.4], [1300, 690], { ...CL, easing: EOUT })} s={0.72} pozlar={[[0, "C12"]]} tohum={21} />
      <Kaynak metin="Source: BLS CPI via FRED (CPIAUCNS), index start = 100" an={a("from")} />
    </SahneKok>
  );
};

// S22 · yeşil kapı: 1934 kilidi modern kilide; $2,500 (1934) → en az $250,000 (bugün)
export const S22: React.FC = () => {
  const a = anlar("S22");
  const t = useT();
  return (
    <SahneKok>
      <Studyo kareler={[[0, kapiMerkezX("yesil"), 560, 1.55], [12.8, kapiMerkezX("yesil"), 540, 1.75]]}>
        <Kilit an={0} x={kapiMerkezX("yesil")} y={kapiY("yesil")} modern={interpolate(t, [a("today,"), a("today,") + 0.6], [0, 1], CL)} />
      </Studyo>
      <Kart an={a("nineteen")} x={120} y={330} w={520} h={170} cerceve="#b8a27a">
        <div style={{ padding: "18px 26px", fontFamily: "Anton", fontSize: 76, color: RENK.murekkep }}>$2,500</div>
        <div style={{ position: "absolute", left: 26, top: 112, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>per depositor (1934)</div>
      </Kart>
      <Kart an={a("two")} x={1220} y={330} w={620} h={200} cerceve={KAPI_RENK.yesil}>
        <div style={{ padding: "12px 26px", fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: RENK.ikincil }}>today: at least</div>
        <div style={{ position: "absolute", left: 26, top: 50, fontFamily: "Anton", fontSize: 84, color: KAPI_RENK.yesil }}>$250,000</div>
        <div style={{ position: "absolute", left: 26, top: 150, fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: RENK.ikincil }}>per depositor, per insured bank</div>
      </Kart>
      <Kaynak metin="Source: FDIC" an={a("fdic")} />
    </SahneKok>
  );
};

// S23 · final etiketleri DISASTER / GAMBLE / SURPRISE; fiyat termometresi; tez
export const S23: React.FC = () => {
  const a = anlar("S23");
  const t = useT();
  const tez = a("that's") - 0.2;
  const etiket = (ad: keyof typeof KAPI, metin: string, renk: string, an: number) => (
    <Yazi an={an} x={kapiMerkezX(ad)} y={150} boyut={60} renk={renk}>{metin}</Yazi>
  );
  return (
    <SahneKok>
      <Studyo kareler={[[0, 960, 540, 1.0], [tez, 940, 540, 1.04], [25.6, 900, 540, 1.08]]}>
        {etiket("mavi", "DISASTER", RENK.kirmizi, a("hurt"))}
        {etiket("yesil", "GAMBLE", RENK.sari, a("came") - 0.1)}
        {etiket("kahve", "SURPRISE", KAPI_RENK.yesil, a("top."))}
      </Studyo>
      {t < tez ? (
        <Kart an={a("what")} x={300} y={790} w={1000} h={96}>
          <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", gap: 40, fontFamily: "Anton", fontSize: 50, color: RENK.murekkep }}>
            <span style={{ color: RENK.mavi }}>PRICES ↓ (1930s)</span>
            <span>↔</span>
            <span style={{ color: RENK.kirmizi }}>PRICES ↑ (2026)</span>
          </div>
        </Kart>
      ) : (
        <>
          <AbsoluteFill style={{ background: "rgba(5,7,15,0.55)", opacity: interpolate(t, [tez, tez + 0.4], [0, 1], CL) }} />
          <Yazi an={a("safe", 2)} x={760} y={250} boyut={100}>SAFE ISN&apos;T A PLACE.</Yazi>
          <Yazi an={a("depends")} x={760} y={380} boyut={100} renk={RENK.sari}>IT DEPENDS ON PRICES</Yazi>
          <Yazi an={a("rules")} x={760} y={510} boyut={56} font="fredoka">AND ON THE RULES AROUND EACH DOOR</Yazi>
        </>
      )}
      <Leo id="S23" x={1700} y={420} s={0.86} pozlar={[[0, "a"], [a("not") - 0.1, "C13"], [tez, "a"]]} tohum={23} />
    </SahneKok>
  );
};

// S24 · uç ekran köprüsü: ışıklar kısılır, dördüncü kapı silueti, el sallama; sağ yarı uç ekran öğelerine boş
export const S24: React.FC = () => {
  const a = anlar("S24");
  const t = useT();
  const kis = interpolate(t, [0, 3], [1, 0.45], CL);
  const dort = interpolate(t, [a("history"), a("history") + 1.0], [0, 1], { ...CL, easing: EOUT });
  return (
    <SahneKok>
      <Studyo kareler={[[0, 960, 540, 1.0], [13.3, 980, 540, 1.03]]} filtre={`brightness(${kis})`}>
        <div style={{ position: "absolute", left: 120, top: 300, width: 250, height: 450, background: "#020306", border: `4px solid rgba(160,180,220,${0.35 * dort})`, borderRadius: 6, opacity: dort, boxShadow: `0 0 40px rgba(120,150,220,${0.3 * dort})` }} />
      </Studyo>
      <Leo id="S24" x={620} y={380} s={0.88} pozlar={[[0, "a"], [a("thanks") - 0.15, "C21"]]} tohum={24} />
      <Yazi an={a("thanks")} x={620} y={60} boyut={86} renk={RENK.sari}>THANKS FOR PLAYING</Yazi>
    </SahneKok>
  );
};
