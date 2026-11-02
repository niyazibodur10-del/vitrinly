import React from "react";
import { AbsoluteFill, interpolate } from "remotion";
import { CL, EIO, Kart, RENK, Sayac, useT, Yazi } from "./kit";
import { anton, fredoka } from "./ortak";
import { Capitol, Dolap, EvMaketi, G10_NOT, GrafikZemin, Kurgu, leoPx, MasaSahne, NotYazi, OlcekSatiri, UstMasa, Zarf, ZARF_RENK } from "./masa";
import { plan } from "./zaman";

// ---------- S01 HOOK (kritik yol H4: Leo masada konuşur) ----------
export const S01: React.FC = () => {
  const { k } = plan("S01");
  const t = useT();
  // Capitol: tam ekrandan masadaki ev konumuna küçülür (0 → ev)
  const p = interpolate(t, [0.15, k.ev], [0, 1], { ...CL, easing: EIO });
  const masaUstu = (
    <>
      <Zarf x={360} y={880} w={340} renk="diger" etiket={<Sayac an={k.five} bas={0} bit={5400} onEk="$" />} alt="IN" an={k.brings + 0.1} giris="dus" donme={-6} yaziBoy={62} />
      {t >= k.ev ? <EvMaketi x={1160} y={880} s={0.72} /> : null}
    </>
  );
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            0,
            <MasaSahne
              key="a"
              kamera={[
                [0, 960, 540, 1],
                [k.spends, 975, 555, 1.08],
              ]}
              leo={t >= k.ev ? { id: "S01", pozlar: [[0, "a"]], giris: { an: k.ev, dy: -150, sure: 0.38 }, tohum: 3 } : null}
              on={masaUstu}
            />,
          ],
          [
            k.spends - 0.1,
            <Dolap
              key="b"
              kamera={[
                [k.spends - 0.1, 1080, 470, 1.02],
                [k.lets, 1090, 480, 1.1],
              ]}
            >
              <NotYazi kutu={G10_NOT[0]} an={k.spends - 0.1} renk="#1f7a45" boyut={48}>
                $5,400 IN
              </NotYazi>
              <NotYazi kutu={G10_NOT[1]} an={k.seven} renk="#b3261e" boyut={46}>
                ~$7,400 OUT
              </NotYazi>
              <NotYazi kutu={G10_NOT[2]} an={k.eksi} renk="#fff" zemin={Math.floor((t - k.eksi) * 4) % 2 === 0 ? "#d9443a" : "#a8261e"} boyut={50}>
                −$2,000 /MO
              </NotYazi>
            </Dolap>,
          ],
          [
            k.lets - 0.1,
            <MasaSahne
              key="c"
              kamera={[
                [k.lets - 0.1, 960, 560, 1.0],
                [k.son, 960, 500, 1.3],
              ]}
              leo={{ id: "S01", pozlar: [[0, "a"], [k.gap - 0.6, "C12"]], tohum: 3 }}
              on={masaUstu}
            />,
          ],
        ]}
      />
      {/* Capitol katmanı (ekran uzayı): küçülürken plaka aydınlanır */}
      {t < k.ev + 0.05 ? (
        <>
          <AbsoluteFill style={{ background: "#0a1226", opacity: 0.82 * (1 - p) }} />
          <div style={{ position: "absolute", left: 960 + (1160 - 960) * p - 500 * (1.15 - 1.0 * p), top: 470 + (850 - 470) * p - 280 * (1.15 - 1.0 * p), scale: String(1.15 - 1.0 * p), transformOrigin: "0 0" }}>
            <Capitol />
          </div>
        </>
      ) : null}
    </AbsoluteFill>
  );
};

// ---------- S12 DORUK: matruşka zarf (kritik yol H4) ----------
const MATRUSKA = (k: Record<string, number>) => {
  const anlar = [k.so2 - 0.05, k.i2, k.i3, k.i4, k.i5, k.i5 + 0.75];
  let x = 820, y = 640, w = 600;
  return anlar.map((an, n) => {
    const o = { an, n, x, y, w, renk: (n % 2 === 0 ? "borc" : "faiz") as "borc" | "faiz" };
    x += 46; y -= 34; w *= 0.74;
    return o;
  });
};

export const S12: React.FC = () => {
  const { k } = plan("S12");
  const t = useT();
  const zarfMasa = <Zarf x={400} y={870} w={330} renk="faiz" etiket="INTEREST" alt="$1,050 / MO" an={0.25} giris="kay" donme={-5} yaziBoy={52} />;
  const L = { s: 0.58, dy: -70 };
  const ic = leoPx(724, 590, L);
  const dis = leoPx(760, 850, L);
  const etiket = (metin: string, x: number, y: number, an: number, renk: string) => (
    <Yazi an={an} x={x} y={y} boyut={44} renk={renk}>
      {metin}
    </Yazi>
  );
  const mat = MATRUSKA(k);
  // kamera: her açılışta punch-in (kademe başına ×1.24, en çok 2.3)
  const kam = mat.map((m, i) => [m.an + (i ? 0.05 : 0), m.x + m.w * 0.1, m.y, Math.min(1 + 0.27 * i, 2.3)] as [number, number, number, number]);
  return (
    <AbsoluteFill style={{ background: "#05070f" }}>
      <Kurgu
        kesmeler={[
          [
            0,
            <MasaSahne
              key="a"
              kamera={[
                [0, 1020, 600, 1.18],
                [k.watch, 1000, 590, 1.24],
              ]}
              leo={{ id: "S12", pozlar: [[0, "a"]], tohum: 5 }}
              on={zarfMasa}
            />,
          ],
          [
            k.watch - 0.05,
            <MasaSahne
              key="b"
              kamera={[
                [k.watch - 0.05, 960, 560, 1.5],
                [k.heres, 960, 600, 1.62],
              ]}
              leo={{ id: "S12", ...L, pozlar: [[0, "a"], [k.open, "G05k"]], tohum: 5 }}
              on={
                <>
                  {t >= k.open ? etiket("INTEREST", dis.x, dis.y - 40, k.open + 0.1, "#ffd9d4") : null}
                  {etiket("BORROWED", ic.x, ic.y - 30, k.borrowed, "#efe4ff")}
                </>
              }
            />,
          ],
          [
            k.heres - 0.05,
            <GrafikZemin key="c">
              <Kart an={k.heres - 0.05} x={240} y={150} w={1440} h={600}>
                <div style={{ position: "absolute", left: 60, top: 40, fontFamily: anton, fontSize: 64, color: RENK.murekkep, letterSpacing: 2 }}>THE MONTHLY GAP</div>
                <div style={{ position: "absolute", right: 60, top: 52, fontFamily: anton, fontSize: 56, color: RENK.murekkep }}>≈ $2,000</div>
                <div style={{ position: "absolute", left: 60, top: 190, width: 1320, height: 120, borderRadius: 14, background: "#4b5875", overflow: "hidden" }}>
                  <div style={{ width: `${(1051.8 / 1992.5) * 100 * interpolate(t, [k.half, k.half + 0.7], [0, 1], CL)}%`, height: "100%", background: ZARF_RENK.faiz }} />
                </div>
                {t >= k.half + 0.35 ? (
                  <>
                    <div style={{ position: "absolute", left: 60, top: 340, fontFamily: anton, fontSize: 70, color: ZARF_RENK.faiz }}>INTEREST ≈ $1,050</div>
                    <div style={{ position: "absolute", left: 60, top: 440, fontFamily: anton, fontSize: 92, color: RENK.murekkep }}>
                      = <Sayac an={k.half + 0.35} sure={0.6} bas={0} bit={53} sonEk="% OF THE GAP" />
                    </div>
                  </>
                ) : null}
              </Kart>
              <OlcekSatiri y={768} an={k.heres} />
            </GrafikZemin>,
          ],
          [
            k.so1 - 0.05,
            <MasaSahne
              key="d"
              kamera={[
                [k.so1 - 0.05, 960, 600, 1.35],
                [k.so2, 960, 580, 1.42],
              ]}
              leo={{ id: "S12", ...L, pozlar: [[0, "G05m"]], tohum: 7 }}
              on={
                <>
                  {etiket("BORROWED", dis.x, dis.y - 40, k.so1, "#efe4ff")}
                  {etiket("INTEREST", ic.x, ic.y - 30, k.newm - 0.3, "#ffd9d4")}
                </>
              }
            />,
          ],
          [
            k.so2 - 0.05,
            <UstMasa key="e" kamera={kam}>
              {mat.map((m, i) => {
                const sonraki = mat[i + 1];
                const acik = sonraki ? t >= sonraki.an : false;
                const cik = interpolate(t, [m.an, m.an + 0.35], [0, 1], { ...CL, easing: EIO });
                const ust = i ? mat[i - 1] : m;
                const x = ust.x + (m.x - ust.x) * cik;
                const y = ust.y + 40 + (m.y - ust.y - 40) * cik;
                return t >= m.an ? (
                  <Zarf key={i} x={x} y={y} w={m.w} renk={m.renk} acik={acik} etiket={m.renk === "faiz" ? "INTEREST" : "BORROWED"} an={m.an} giris={i ? "yok" : "pop"} donme={i % 2 ? 4 : -3} yaziBoy={m.w * 0.13} />
                ) : null;
              })}
            </UstMasa>,
          ],
        ]}
      />
      {t >= k.i5 + 0.9 ? (
        <div style={{ position: "absolute", left: 120, top: 90, fontFamily: fredoka, fontWeight: 700, fontSize: 46, color: "#fff", WebkitTextStroke: "8px #0b0b0b", paintOrder: "stroke fill", opacity: interpolate(t, [k.i5 + 0.9, k.i5 + 1.2], [0, 1], CL) }}>
          INTEREST › BORROWED › INTEREST › …
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
