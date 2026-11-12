import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { GorselKatman } from "./Gorsel";
import { AGIZ_YEDEK, GEN, YUK } from "./sabitler";
import type { AgizDosyasi, AgizSekli, AgizYolu, Gorsel, KarakterSahne, Konusmaci, Sahne, Satir, YerTutucu } from "./tipler";
import { agizSekli, konusuyor, sonSatir } from "./zaman";

// Sahne kartı: sabit 3D görünümlü sahne görseli + (opsiyonel) karakter katmanları + sinematik kamera.
// Kamera = yavaş zoom/pan (Ken Burns) × konuşmacıya punch-in. Sahneler arası geçiş sert kesmedir (Bolum.tsx Sequence sınırı).
// Ağız yolu (yama / ifade / kamera) sahne veya bölüm verisinden seçilir (tipler.ts AgizYolu).
// Kamera yolu: odak konuşan karakterin yüzüne ölçek 1,28 ile kayar; yama/ifade yolunda hafif punch-in (1,07).
// Kadraj daima görselin içinde kalır (odak sınırlanır), boş kenar görünmez.

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

const varsayilanPunch = (yol: AgizYolu) => (yol === "kamera" ? 1.28 : 1.07);

const yuz = (k: KarakterSahne) => k.odak ?? { x: k.x + k.w / 2, y: k.y + k.h * 0.22 };

type Durum = { s: number; fx: number; fy: number };

export const SahneKarti: React.FC<{
  sahne: Sahne;
  satirlar: Satir[];
  agiz?: AgizDosyasi;
  agizYolu: AgizYolu;
}> = ({ sahne, satirlar, agiz, agizYolu }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const yerel = frame / fps; // Sequence içi süre
  const t = sahne.bas + yerel; // bölüm zamanı
  const sure = sahne.bitis - sahne.bas;
  const yol = sahne.agizYolu ?? agizYolu;
  const kam = sahne.kamera ?? {};
  const karakterler = sahne.karakterler ?? [];

  // --- kamera ---
  const [z0, z1] = kam.zoom ?? [1, 1.06];
  const tabanZ = interpolate(yerel, [0, sure], [z0, z1], { ...CL, easing: Easing.inOut(Easing.quad) });
  const kx = kam.kay?.x ? interpolate(yerel, [0, sure], kam.kay.x, CL) : 0;
  const ky = kam.kay?.y ? interpolate(yerel, [0, sure], kam.kay.y, CL) : 0;
  const punch = kam.punch ?? varsayilanPunch(yol);
  const gecis = kam.gecis ?? (yol === "kamera" ? 0.35 : 0.25);
  const odakOran = yol === "kamera" ? 1 : 0.4; // kamera yolunda yüz merkeze gelir

  const sahneSatir = satirlar.filter((s) => s.bas < sahne.bitis && s.bitis > sahne.bas);
  const durum = (kim: Konusmaci | null): Durum => {
    const k = kim ? karakterler.find((c) => c.kim === kim) : undefined;
    if (!k || punch <= 1) return { s: 1, fx: GEN / 2, fy: YUK / 2 };
    const y = yuz(k);
    return { s: punch, fx: GEN / 2 + (y.x - GEN / 2) * odakOran, fy: YUK / 2 + (y.y - YUK / 2) * odakOran };
  };
  // aktif konuşmacı = sahnede t'den önce başlamış son satırın sahibi; değişim anından itibaren geçiş
  const son = sonSatir(sahneSatir, t);
  let degisim = sahne.bas;
  let onceki: Konusmaci | null = null;
  if (son) {
    const i = sahneSatir.indexOf(son);
    let j = i;
    while (j > 0 && sahneSatir[j - 1].konusmaci === son.konusmaci) j--;
    degisim = Math.max(sahne.bas, sahneSatir[j].bas);
    onceki = j > 0 ? sahneSatir[j - 1].konusmaci : null;
  }
  const a = durum(onceki);
  const b = durum(son?.konusmaci ?? null);
  const p = gecis > 0 ? interpolate(t - degisim, [0, gecis], [0, 1], { ...CL, easing: Easing.inOut(Easing.cubic) }) : 1;
  const s = (a.s + (b.s - a.s) * p) * tabanZ;
  const yarW = GEN / (2 * s), yarH = YUK / (2 * s);
  const fx = Math.min(GEN - yarW, Math.max(yarW, a.fx + (b.fx - a.fx) * p + kx));
  const fy = Math.min(YUK - yarH, Math.max(yarH, a.fy + (b.fy - a.fy) * p + ky));

  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: "#000" }}>
      <AbsoluteFill style={{ transformOrigin: "0 0", transform: `translate(${GEN / 2}px, ${YUK / 2}px) scale(${s}) translate(${-fx}px, ${-fy}px)` }}>
        <GorselKatman g={sahne.arka} />
        {karakterler.map((k) => (
          <KarakterKatman key={k.kim} k={k} yol={yol} t={t} sahne={sahne} satirlar={satirlar} agiz={agiz} />
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const ifadeSec = (k: KarakterSahne, sahne: Sahne, satirlar: Satir[], t: number): Gorsel | undefined => {
  if (!k.ifadeler) return k.gorsel;
  const atanan = sahne.ifadeler?.find((e) => e.kim === k.kim && t >= e.bas && t < e.bitis)?.ifade;
  const ad = atanan ?? (konusuyor(satirlar, k.kim, t) ? "konusur" : "notr");
  return k.ifadeler[ad] ?? k.ifadeler.notr ?? k.gorsel;
};

const yamaGorsel = (sekiller: Partial<Record<AgizSekli, Gorsel>> | YerTutucu, sekil: AgizSekli): Gorsel | undefined => {
  if ("yerTutucu" in sekiller) return sekiller as YerTutucu;
  const map = sekiller as Partial<Record<AgizSekli, Gorsel>>;
  for (const aday of AGIZ_YEDEK[sekil]) if (map[aday]) return map[aday];
  return undefined;
};

const KarakterKatman: React.FC<{
  k: KarakterSahne; yol: AgizYolu; t: number; sahne: Sahne; satirlar: Satir[]; agiz?: AgizDosyasi;
}> = ({ k, yol, t, sahne, satirlar, agiz }) => {
  const g = yol === "ifade" ? ifadeSec(k, sahne, satirlar, t) : k.gorsel;
  const sekil: AgizSekli = konusuyor(satirlar, k.kim, t) ? agizSekli(agiz?.[k.kim], t) : "X";
  const yama = yol === "yama" && k.agiz ? yamaGorsel(k.agiz.sekiller, sekil) : undefined;
  return (
    <>
      {g ? (
        <div style={{ position: "absolute", left: k.x, top: k.y, width: k.w, height: k.h }}>
          <GorselKatman g={g} style={typeof g === "string" ? { objectFit: "contain" } : undefined} />
        </div>
      ) : null}
      {yama && k.agiz ? (
        <div style={{ position: "absolute", left: k.agiz.x, top: k.agiz.y, width: k.agiz.w, height: k.agiz.h }}>
          <GorselKatman g={yama} sekil={sekil} style={typeof yama === "string" ? { objectFit: "contain" } : undefined} />
        </div>
      ) : null}
    </>
  );
};
