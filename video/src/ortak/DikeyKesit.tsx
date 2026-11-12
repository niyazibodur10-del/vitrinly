import React from "react";
import { AbsoluteFill, Sequence } from "remotion";

// 16:9 (1920x1080) bir sahne/kompozisyonu 9:16 (1080x1920) Shorts karesine yerleştirir.
// Altyapı bileşeni (uretim-muhendisi); Shorts'un kendi hook'u, altyazısı ve kurgusu kurgu-editoru'nundur.
// mod="kirp": 16:9 kare yüksekliğe ölçeklenir (x1.78), yatayda odakX (0 = sol, 0.5 = orta, 1 = sağ) etrafında kırpılır.
//   Not: 16:9 için yerleştirilmiş altyazı/yazı kırpılır → Shorts'ta altyazıyı dikey katman olarak ayrıca ekle.
// mod="dolgu": 16:9 kare genişliğe sığdırılır (x0.5625), üst/alt `arkaPlan` ile dolar (yazılar küçülür ama kaybolmaz).
// baslangicKare: kaynaktaki kesit başlangıcı (Shorts kesiti); kompozisyon süresi kesit süresidir.
// Kaynağı İKİ kez çizme (bulanık dolgu vb.): kaynaktaki <Audio> iki kez çalar.
export const DikeyKesit: React.FC<{
  children: React.ReactNode;
  mod?: "kirp" | "dolgu";
  odakX?: number;
  baslangicKare?: number;
  arkaPlan?: string;
}> = ({ children, mod = "kirp", odakX = 0.5, baslangicKare = 0, arkaPlan = "#0d1a33" }) => {
  const W = 1920, H = 1080, DW = 1080, DH = 1920;
  const olcek = mod === "kirp" ? DH / H : DW / W;
  const gw = W * olcek, gh = H * olcek;
  const x = mod === "kirp" ? -Math.min(Math.max(odakX * gw - DW / 2, 0), gw - DW) : 0;
  const y = (DH - gh) / 2;
  return (
    <AbsoluteFill style={{ background: arkaPlan, overflow: "hidden" }}>
      <div style={{ position: "absolute", left: x, top: y, width: W, height: H, transform: `scale(${olcek})`, transformOrigin: "0 0" }}>
        <Sequence from={-baslangicKare} layout="none">
          {children}
        </Sequence>
      </div>
    </AbsoluteFill>
  );
};
