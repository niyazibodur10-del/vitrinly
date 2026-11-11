import React from "react";
import { Img, random, staticFile } from "remotion";
import type { GozElips, Konusmaci, RigKarakter } from "./tipler";
import { agizDurumu, type AgizDurum } from "./zaman";

// Rig katmanı (animasyon-yonetmeni 2026-11-11): taban görseli + 3 durumlu ağız yaması (2 karelik alfa karışımı)
// + kodla göz kırpma (ten rengi kapak, 3–5 sn'de bir, 4 kare) + nefes (alt kenara yaslı, ölçek ≥1 → kesik kenar içeri girmez).
// Hepsi görselin piksel uzayında tek kutuda: kamera/yerleşim dönüşümü tabanla birebir aynı uygulanır (dikiş yok).

export const AGIZ_GECIS_SN = 2 / 30;

/** Göz kırpma takvimi: kişi başına deterministik 3–5 sn aralık; her kırpma 4 kare. */
const KIRPMA_KARE = [0.55, 1, 0.9, 0.45];
const takvimler: Partial<Record<Konusmaci, number[]>> = {};
export const kirpmaTakvimi = (kim: Konusmaci, sure = 120): number[] => {
  if (takvimler[kim]) return takvimler[kim]!;
  const out: number[] = [];
  let t = 0.9 + random(`kirp-${kim}-0`) * 1.6;
  for (let i = 1; t < sure; i++) {
    out.push(t);
    t += 3 + random(`kirp-${kim}-${i}`) * 2;
  }
  takvimler[kim] = out;
  return out;
};
export const kapakOrani = (kim: Konusmaci, t: number, fps = 30): number => {
  for (const b of kirpmaTakvimi(kim)) {
    const k = Math.floor((t - b) * fps + 1e-6);
    if (k >= 0 && k < KIRPMA_KARE.length) return KIRPMA_KARE[k];
    if (b > t) break;
  }
  return 0;
};

/** Göz kapağı (tur 2, hakem Z2): düz renk yerine GERÇEK DERİ — göz altındaki yanak derisi göz çizgisine göre
 *  aynalanıp kapak bölgesine (badem ∩ kapak kenarı üstü) kırpılır; üstte yumuşak gölge kıvrımı, kenarda göz konturunu
 *  izleyen kirpik kavisi (köşelere doğru incelir). Hepsi aynı görselden, eşzamanlı (Img + CSS clip-path) → render'da gecikme yok. */
type Nokta = [number, number];
const dondur = (g: GozElips, [x, y]: Nokta): Nokta => {
  const r = (g.aci * Math.PI) / 180, dx = x - g.cx, dy = y - g.cy;
  return [g.cx + dx * Math.cos(r) - dy * Math.sin(r), g.cy + dx * Math.sin(r) + dy * Math.cos(r)];
};
const gozGeometri = (g: GozElips, oran: number) => {
  const R = g.ry + 6, X = g.rx + 7, cy = g.cy;
  const P = (x: number, y: number) => dondur(g, [x, y]).map((v) => v.toFixed(1)).join(" ");
  const sol: Nokta = [g.cx - X, cy], sag: Nokta = [g.cx + X, cy];
  // kenarın orta noktası: açık → üst kavis (cy−R), kapalı → alt kapak çizgisi (cy+0,75R)
  const tepe = cy - R + 1.85 * R * oran;
  const kc = 2 * tepe - cy;
  const kapali = oran >= 0.85;
  // kapak bölgesi = badem üst kavsi + kenar kavsi (kapalıda badem alt kavsi)
  const ust = `M ${P(...sol)} Q ${P(g.cx, cy - 2.2 * R)} ${P(...sag)}`;
  const bolge = kapali
    ? `${ust} Q ${P(g.cx, cy + 2.0 * R)} ${P(...sol)} Z`
    : `${ust} Q ${P(g.cx, Math.min(kc, cy + 2.0 * R))} ${P(...sol)} Z`;
  const kenar = `M ${P(sol[0] + 6, cy)} Q ${P(g.cx, kc)} ${P(sag[0] - 6, cy)}`;
  const kivrim = `M ${P(sol[0] + 6, cy - 0.2 * R)} Q ${P(g.cx, cy - 2.2 * R)} ${P(sag[0] - 6, cy - 0.2 * R)}`;
  return { R, bolge, kenar, kivrim, ayna: cy + R };
};

export const GozKapaklari: React.FC<{ gozler: GozElips[]; w: number; h: number; oran: number; id: string; src: string }> = ({ gozler, w, h, oran, id, src }) => {
  if (oran <= 0) return null;
  return (
    <>
      {gozler.map((g, i) => {
        const geo = gozGeometri(g, oran);
        return (
          <div key={i} style={{ position: "absolute", left: 0, top: 0, width: w, height: h, clipPath: `path("${geo.bolge}")` }}>
            {/* göz altı derisi, göz alt çizgisine göre aynalı */}
            <Img src={staticFile(src)} style={{ position: "absolute", left: 0, top: 0, width: w, height: h, transformOrigin: `0px ${geo.ayna}px`, transform: "scaleY(-1)" }} />
            {/* kapak hacmi: üstten koyulaşan ten gölgesi (aynalı deri göz altından açık gelir) */}
            <div style={{ position: "absolute", left: 0, width: w, top: g.cy - geo.R * 1.2, height: geo.R * 2.4, background: "linear-gradient(to bottom, rgba(110,55,30,0.28) 0%, rgba(110,55,30,0.12) 55%, rgba(110,55,30,0.04) 100%)" }} />
          </div>
        );
      })}
      <svg viewBox={`0 0 ${w} ${h}`} width={w} height={h} style={{ position: "absolute", left: 0, top: 0 }}>
        <defs>
          <filter id={`${id}-yum`} x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="2.4" /></filter>
        </defs>
        {gozler.map((g, i) => {
          const geo = gozGeometri(g, oran);
          return (
            <g key={i}>
              {/* kapak gölgesi: kıvrım çizgisi boyunca yumuşak koyuluk (düz disk görünmesin) */}
              <path d={geo.kivrim} fill="none" stroke="rgba(90,45,25,0.22)" strokeWidth={geo.R * 0.6} filter={`url(#${id}-yum)`} style={{ clipPath: `path("${geo.bolge}")` }} />
              {/* kirpik kavisi: kontur boyunca, yumuşak + keskin iki geçiş */}
              <path d={geo.kenar} fill="none" stroke="rgba(30,16,10,0.35)" strokeWidth={Math.max(3, geo.R * 0.18)} strokeLinecap="round" filter={`url(#${id}-yum)`} />
              <path d={geo.kenar} fill="none" stroke="#2a1812" strokeWidth={Math.max(2, geo.R * 0.08)} strokeLinecap="round" />
            </g>
          );
        })}
      </svg>
    </>
  );
};

/** Konuşma tabanı + ağız + göz + nefes. Kutu: görsel pikseli (w×h); dış yerleşimi çağıran verir. */
export const RigKatman: React.FC<{
  kim: Konusmaci; r: RigKarakter; t: number;
  agiz?: { bas: number; bitis: number; sekil: AgizDurum }[];
  /** göz kırpma açık mı (Cekim: kanca 0–3 sn ve ekranda yüz ölçeği ≥1,15 olan çekimlerde kapalı) */
  kirp?: boolean;
}> = ({ kim, r, t, agiz, kirp = true }) => {
  const a = agizDurumu(agiz, t, AGIZ_GECIS_SN);
  const dosya = (d: AgizDurum) => r.agiz[d];
  // nefes: 0,25 Hz, ölçek 1 → 1,006 (alt merkez); hafif omuz kalkışı
  const ev = kim === "jake" ? 0 : 1.7;
  const nef = 1 + 0.003 * (1 + Math.sin(2 * Math.PI * 0.25 * t + ev));
  const oran = kapakOrani(kim, t);
  return (
    <div style={{ position: "absolute", left: 0, top: 0, width: r.w, height: r.h, transformOrigin: `${r.w / 2}px ${r.h}px`, transform: `scale(${nef})` }}>
      <Img src={staticFile(r.taban)} style={{ position: "absolute", left: 0, top: 0, width: r.w, height: r.h }} />
      {a.alt !== "kapali" || a.ust !== "kapali" ? (
        <div style={{ position: "absolute", left: r.agiz.x, top: r.agiz.y, width: r.agiz.w, height: r.agiz.h }}>
          <Img src={staticFile(dosya(a.alt))} style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }} />
          {a.p > 0 && a.ust !== a.alt ? (
            <Img src={staticFile(dosya(a.ust))} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: a.p }} />
          ) : null}
        </div>
      ) : null}
      {kirp ? <GozKapaklari gozler={r.gozler} w={r.w} h={r.h} oran={oran} id={`gk-${kim}`} src={r.taban} /> : null}
    </div>
  );
};

/** İfade portresi (ağız oynamaz) + istenirse göz kırpma + nefes. */
export const PortreKatman: React.FC<{ kim: Konusmaci; p: RigKarakter["portreler"][string]; t: number; maske?: string; kirp?: boolean }> = ({ kim, p, t, maske, kirp = true }) => {
  const nef = 1 + 0.003 * (1 + Math.sin(2 * Math.PI * 0.25 * t + (kim === "jake" ? 0 : 1.7)));
  const oran = p.gozler ? kapakOrani(kim, t) : 0;
  return (
    <div style={{ position: "absolute", left: p.xy[0], top: p.xy[1], width: p.w, height: p.h, transformOrigin: "0 0", transform: `scale(${p.olcek})`, WebkitMaskImage: maske, maskImage: maske }}>
      <div style={{ position: "absolute", inset: 0, transformOrigin: `${p.w / 2}px ${p.h}px`, transform: `scale(${nef})` }}>
        <Img src={staticFile(p.dosya)} style={{ position: "absolute", left: 0, top: 0, width: p.w, height: p.h }} />
        {p.gozler && kirp ? <GozKapaklari gozler={p.gozler} w={p.w} h={p.h} oran={oran} id={`gp-${kim}`} src={p.dosya} /> : null}
      </div>
    </div>
  );
};
