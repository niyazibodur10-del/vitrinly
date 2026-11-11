import React from "react";
import { AbsoluteFill, Easing, Img, interpolate, random, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { PropKatman } from "./Proplar";
import { PortreKatman, RigKatman } from "./Rig";
import { GEN, YUK } from "./sabitler";
import type { Konusmaci, MekanSeti, Sahne } from "./tipler";
import type { AgizDurum } from "./zaman";

// Çekim çatısı (animasyon-yonetmeni 2026-11-11): kesme listesindeki her sahne bir çekim anahtarıdır
// (genis / yakin:kim / portre:kim:ifade / ikiPortre / tahta). Aynı mekân seti + rig her bölümde tekrar kullanılır;
// bölüm verisi yalnız zaman, çekim, prop ve kamera parametresi taşır (kod yok).
// Kamera: yavaş zoom/pan (sahne.kamera.zoom/kay) × punch-in vuruşları (sahne.vurus) + sarsıntı (sahne.sarsinti);
// kadraj daima sahne kutusunun (1080x1920) içinde kalır → karakter tabanlarının kesik kenarları kadraj dışında.
// Sürekli itme: zoom aralığı en az %0,35/sn hareket verir (freezedetect, hafıza 2026-11-02).

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

export type AgizDurumlari = Partial<Record<Konusmaci, { bas: number; bitis: number; sekil: AgizDurum }[]>>;

const PlakaKatman: React.FC<{ src: string; olcek?: number; capa?: [number, number]; bulanik?: number; children?: React.ReactNode }> = ({ src, olcek = 1, capa = [0, 0], bulanik, children }) => (
  <div style={{ position: "absolute", left: 0, top: 0, width: GEN, height: YUK, transformOrigin: `${capa[0]}px ${capa[1]}px`, transform: `scale(${olcek})` }}>
    <Img src={staticFile(src)} style={{ position: "absolute", left: 0, top: 0, width: GEN, height: YUK, filter: bulanik ? `blur(${bulanik}px)` : undefined }} />
    {children}
  </div>
);

export const CekimKarti: React.FC<{ sahne: Sahne; mekan: MekanSeti; agiz: AgizDurumlari }> = ({ sahne, mekan, agiz }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = (frame + Math.round(sahne.bas * fps)) / fps; // bölüm zamanı (kare-doğru)
  const yerel = t - sahne.bas;
  const sure = sahne.bitis - sahne.bas;
  const c = sahne.cekim!;
  const kam = sahne.kamera ?? {};
  const proplar = sahne.proplar ?? [];

  // --- kamera ---
  const [z0, z1] = kam.zoom ?? [1.0, 1.04];
  let S = interpolate(yerel, [0, sure], [z0, z1], { ...CL, easing: Easing.inOut(Easing.quad) });
  for (const v of sahne.vurus ?? []) {
    S *= interpolate(t, [v.t, v.t + (v.sure ?? 0.1)], [1, v.olcek], { ...CL, easing: Easing.out(Easing.cubic) });
  }
  const varsayilanOdak = (): { x: number; y: number } => {
    if (c.tur === "yakin") {
      const y = mekan.karakterler[c.kim].yuz;
      return { x: (y.x + GEN / 2) / 2, y: y.y + 120 };
    }
    if (c.tur === "tahta") return { x: mekan.tahtaAlan.x + mekan.tahtaAlan.w / 2, y: mekan.tahtaAlan.y + mekan.tahtaAlan.h / 2 };
    if (c.tur === "genis") return { x: GEN / 2, y: 820 };
    return { x: GEN / 2, y: 760 };
  };
  const od = sahne.odak ?? varsayilanOdak();
  let fx = od.x + (kam.kay?.x ? interpolate(yerel, [0, sure], kam.kay.x, CL) : 0);
  let fy = od.y + (kam.kay?.y ? interpolate(yerel, [0, sure], kam.kay.y, CL) : 0);
  for (const sh of sahne.sarsinti ?? []) {
    const d = t - sh.t, ss = sh.sure ?? 0.12;
    if (d >= 0 && d < ss) {
      const g = (sh.guc ?? 14) * (1 - d / ss);
      fx += (random(`sx-${sahne.id}-${frame}`) - 0.5) * 2 * g;
      fy += (random(`sy-${sahne.id}-${frame}`) - 0.5) * 2 * g;
    }
  }
  const yarW = GEN / (2 * S), yarH = YUK / (2 * S);
  fx = Math.min(GEN - yarW, Math.max(yarW, fx));
  fy = Math.min(YUK - yarH, Math.max(yarH, fy));

  const rig = (kim: Konusmaci) => <RigKatman kim={kim} r={mekan.karakterler[kim]} t={t} agiz={agiz[kim]} />;

  let icerik: React.ReactNode = null;
  if (c.tur === "genis") {
    const sira: Konusmaci[] = mekan.onde === "jake" ? ["mike", "jake"] : ["jake", "mike"];
    icerik = (
      <>
        <PlakaKatman src={mekan.genis} />
        {sira.map((kim) => {
          const y = mekan.ikili[kim];
          return (
            <div key={kim} style={{ position: "absolute", left: y.xy[0], top: y.xy[1], transformOrigin: "0 0", transform: `scale(${y.olcek})` }}>
              {rig(kim)}
            </div>
          );
        })}
        {mekan.on ? <PlakaKatman src={mekan.on} /> : null}
        <div style={{ position: "absolute", left: 0, top: 0, width: GEN, height: YUK }}>
          <PropKatman proplar={proplar} t={t} uzay="sahne" />
        </div>
      </>
    );
  } else if (c.tur === "yakin") {
    const tk = mekan.tekli[c.kim];
    icerik = (
      <>
        <PlakaKatman src={mekan.genis} olcek={tk.plakaOlcek} capa={tk.capa} />
        {rig(c.kim)}
        {mekan.on ? <PlakaKatman src={mekan.on} olcek={tk.plakaOlcek} capa={tk.capa} /> : null}
        <div style={{ position: "absolute", left: 0, top: 0, width: GEN, height: YUK, transformOrigin: `${tk.capa[0]}px ${tk.capa[1]}px`, transform: `scale(${tk.plakaOlcek})` }}>
          <PropKatman proplar={proplar} t={t} uzay="sahne" />
        </div>
      </>
    );
  } else if (c.tur === "portre" || c.tur === "ikiPortre") {
    const pa = mekan.portreArka;
    if (c.tur === "portre") {
      const p = mekan.karakterler[c.kim].portreler[c.ifade];
      icerik = (
        <>
          <PlakaKatman src={mekan.genis} olcek={pa.olcek} capa={pa.capa} bulanik={pa.bulanik} />
          <PortreKatman kim={c.kim} p={p} t={t} />
        </>
      );
    } else {
      // ikili kameraya bakış: iki portre yan yana (0,8), yüzler üst yarıda; alt kenar maskeyle söner (kesik kenar görünmez)
      const yerles = (kim: Konusmaci, ifade: string, merkezX: number) => {
        const p = mekan.karakterler[kim].portreler[ifade];
        const o = 0.74;
        return { ...p, olcek: o, xy: [merkezX - (p.w / 2) * o, 10] as [number, number] };
      };
      const maske = "linear-gradient(to bottom, #000 0, #000 1300px, rgba(0,0,0,0) 1500px)";
      icerik = (
        <>
          <PlakaKatman src={mekan.genis} olcek={pa.olcek} capa={pa.capa} bulanik={pa.bulanik} />
          <PortreKatman kim={c.sol.kim} p={yerles(c.sol.kim, c.sol.ifade, 285)} t={t} maske={maske} />
          <PortreKatman kim={c.sag.kim} p={yerles(c.sag.kim, c.sag.ifade, 805)} t={t} maske={maske} />
          <div style={{ position: "absolute", left: 0, right: 0, top: 900, bottom: 0, background: "linear-gradient(to bottom, rgba(8,10,16,0) 0%, rgba(8,10,16,0.75) 45%, rgba(8,10,16,0.9) 100%)" }} />
        </>
      );
    }
  } else if (c.tur === "tahta") {
    icerik = (
      <PlakaKatman src={mekan.tahta}>
        <PropKatman proplar={proplar} t={t} uzay="sahne" />
      </PlakaKatman>
    );
  }

  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: "#000" }}>
      <AbsoluteFill style={{ transformOrigin: "0 0", transform: `translate(${GEN / 2}px, ${YUK / 2}px) scale(${S}) translate(${-fx}px, ${-fy}px)` }}>
        {icerik}
      </AbsoluteFill>
      <PropKatman proplar={proplar} t={t} uzay="ekran" />
    </AbsoluteFill>
  );
};
