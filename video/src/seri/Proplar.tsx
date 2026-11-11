import React from "react";
import { Easing, interpolate, spring } from "remotion";
import { Ikon } from "./Ikonlar";
import { ALTIN, anton, fredoka, GUVENLI, GUVENLI_W } from "./sabitler";
import type { Prop } from "./tipler";

// Kod-prop'lar (animasyon-yonetmeni 2026-11-11). Zaman = bölüm saniyesi `t`; giriş/çıkış kare-doğru (spring/interpolate).
// "ekran" uzayındakiler güvenli alan içinde (x 60–890, y 250–1440) ve altyazı bandının (1150–1420) üstünde durur.

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const FPS = 30;
const yay = (t: number, bas: number, cfg = { damping: 13, stiffness: 190, mass: 0.7 }) =>
  t < bas ? 0 : spring({ frame: Math.round((t - bas) * FPS), fps: FPS, config: cfg });
const cikis = (t: number, bitis: number, sure = 0.18) => interpolate(t, [bitis - sure, bitis], [1, 0], { ...CL, easing: Easing.in(Easing.cubic) });

/** Logosuz illüstrasyon banknot: yeşil, köşelerde 100, ortada yıldızlı mühür. */
export const Banknot: React.FC<{ w?: number }> = ({ w = 330 }) => (
  <svg viewBox="0 0 330 140" width={w} height={(w * 140) / 330}>
    <rect x="2" y="2" width="326" height="136" rx="10" fill="#a9c79a" stroke="#3d5a35" strokeWidth="4" />
    <rect x="14" y="14" width="302" height="112" rx="6" fill="none" stroke="#5f8452" strokeWidth="3" strokeDasharray="6 4" />
    <ellipse cx="165" cy="70" rx="44" ry="44" fill="#c9dfbd" stroke="#3d5a35" strokeWidth="3" />
    <path d="M165 40 l9 20 h21 l-17 13 l7 21 l-20-13 l-20 13 l7-21 l-17-13 h21z" fill="#5f8452" />
    <text x="40" y="52" fontFamily="Anton" fontSize="34" fill="#2f4a28" textAnchor="middle">100</text>
    <text x="290" y="118" fontFamily="Anton" fontSize="34" fill="#2f4a28" textAnchor="middle">100</text>
    <path d="M232 46 h70 M232 60 h56 M28 96 h70 M28 110 h50" stroke="#5f8452" strokeWidth="5" strokeLinecap="round" />
  </svg>
);

const IlanKarti: React.FC<{ p: Extract<Prop, { tur: "ilan" }>; t: number }> = ({ p, t }) => {
  const g = yay(t, p.bas, { damping: 14, stiffness: 170, mass: 0.8 });
  const c = cikis(t, p.bitis);
  const titre = p.titre !== undefined && t >= p.titre && t < p.titre + 0.6 ? Math.sin((t - p.titre) * 70) * 5 * (1 - (t - p.titre) / 0.6) : 0;
  if (p.yer === "alt") {
    // alçak yatay kart (tur 2, hakem Ö3): y 800–1120 → konuşanın yüzü ve ağzı açık kalır; altyazı bandının (1150) üstünde
    const karart = interpolate(t, [p.bas, p.bas + 0.15], [0, 1], CL) * c;
    return (
      <>
        <div style={{ position: "absolute", left: 0, right: 0, top: 760, height: 420, background: `linear-gradient(to bottom, rgba(6,10,18,0) 0%, rgba(6,10,18,${0.5 * karart}) 40%)` }} />
        <div style={{ position: "absolute", left: GUVENLI.sol + 20, width: GUVENLI_W - 40, top: 805, transform: `translateY(${(1 - g) * 700}px) rotate(${(1 - g) * 6 - 1.5}deg)`, opacity: c }}>
          <div style={{ display: "flex", borderRadius: 30, background: "#ffffff", overflow: "hidden", boxShadow: "0 18px 40px rgba(0,0,0,0.55)", height: 300 }}>
            <div style={{ width: 290, flex: "none", background: "linear-gradient(160deg,#eef3f9,#d6e1ee)", display: "flex", alignItems: "center", justifyContent: "center", position: "relative" }}>
              <div style={{ transform: `rotate(${titre}deg) translateY(${Math.abs(titre) * -2}px)` }}>
                <Ikon ad={p.ikon} boyut={230} hale={false} />
              </div>
              <div style={{ position: "absolute", left: 14, top: 12, padding: "4px 12px", borderRadius: 12, background: "#1d1b22", color: "#fff", fontFamily: fredoka, fontWeight: 700, fontSize: 22, letterSpacing: 2 }}>
                LISTING
              </div>
            </div>
            <div style={{ padding: "22px 24px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 6 }}>
              <div style={{ fontFamily: anton, fontSize: 52, lineHeight: 1.02, color: "#1d1b22", letterSpacing: 1 }}>{p.baslik}</div>
              <div style={{ fontFamily: anton, fontSize: 78, lineHeight: 1, color: "#2fae6a" }}>{p.fiyat}</div>
              <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 36, color: "#e2564a" }}>{p.not}</div>
            </div>
          </div>
        </div>
      </>
    );
  }
  const karart = interpolate(t, [p.bas, p.bas + 0.15], [0, 0.55], CL) * c;
  return (
    <>
      <div style={{ position: "absolute", inset: 0, background: `rgba(6,10,18,${karart})` }} />
      <div
        style={{
          position: "absolute", left: GUVENLI.sol + 45, width: GUVENLI_W - 90, top: 400,
          transform: `translateY(${(1 - g) * 900}px) rotate(${(1 - g) * 8 - 2}deg) scale(${0.9 + 0.1 * c})`, opacity: c,
        }}
      >
        <div style={{ borderRadius: 34, background: "#ffffff", overflow: "hidden", boxShadow: "0 22px 50px rgba(0,0,0,0.55)" }}>
          <div style={{ height: 360, background: "linear-gradient(160deg,#eef3f9,#d6e1ee)", display: "flex", alignItems: "center", justifyContent: "center", position: "relative" }}>
            <div style={{ transform: `rotate(${titre}deg) translateY(${Math.abs(titre) * -2}px)` }}>
              <Ikon ad={p.ikon} boyut={270} hale={false} />
            </div>
            <div style={{ position: "absolute", left: 22, top: 20, padding: "6px 16px", borderRadius: 14, background: "#1d1b22", color: "#fff", fontFamily: fredoka, fontWeight: 700, fontSize: 26, letterSpacing: 2 }}>
              LISTING
            </div>
          </div>
          <div style={{ padding: "22px 30px 28px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", gap: 12 }}>
              <div style={{ fontFamily: anton, fontSize: 64, lineHeight: 1.05, color: "#1d1b22", letterSpacing: 1 }}>{p.baslik}</div>
              <div style={{ fontFamily: anton, fontSize: 76, lineHeight: 1, color: "#2fae6a" }}>{p.fiyat}</div>
            </div>
            <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: "#e2564a", marginTop: 8 }}>{p.not}</div>
          </div>
        </div>
      </div>
    </>
  );
};

const Telefon: React.FC<{ p: Extract<Prop, { tur: "telefon" }>; t: number }> = ({ p, t }) => {
  const g = yay(t, p.bas, { damping: 15, stiffness: 150, mass: 0.9 });
  const c = cikis(t, p.bitis, 0.12);
  const W = 430, H = 760;
  return (
    <div style={{ position: "absolute", left: 540 - W / 2 - 60, top: 470, width: W, height: H, transform: `translateY(${(1 - g) * 1100}px) rotate(${-4 + (1 - g) * 10}deg)`, opacity: c }}>
      <div style={{ position: "absolute", inset: 0, borderRadius: 56, background: "#16171d", boxShadow: "0 24px 50px rgba(0,0,0,0.55), inset 0 0 0 4px #3a3d47" }} />
      <div style={{ position: "absolute", left: 16, top: 16, right: 16, bottom: 16, borderRadius: 42, background: "#f3f5f9", overflow: "hidden", padding: "50px 18px 18px" }}>
        <div style={{ position: "absolute", left: "50%", top: 14, width: 110, height: 24, marginLeft: -55, borderRadius: 12, background: "#16171d" }} />
        <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 30, color: "#1d1b22", marginBottom: 12, marginLeft: 6 }}>Near you</div>
        {p.ogeler.map((o, i) => {
          const q = yay(t, p.bas + 0.25 + i * 0.12);
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 16, padding: 12, marginBottom: 12, borderRadius: 22, background: "#fff", boxShadow: "0 3px 10px rgba(0,0,0,0.1)", opacity: q, transform: `translateX(${(1 - q) * 60}px)` }}>
              <div style={{ width: 120, height: 120, borderRadius: 16, background: "#e4ebf4", display: "flex", alignItems: "center", justifyContent: "center" }}>
                <Ikon ad={o.ikon} boyut={96} hale={false} />
              </div>
              <div style={{ fontFamily: anton, fontSize: 52, color: o.fiyat === "FREE" ? "#2fae6a" : "#1d1b22" }}>{o.fiyat}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

/** Elle yazılıyor efekti: harfler soldan sağa kırpma maskesiyle açılır (kalem ucu izi). */
const ElYazisi: React.FC<{ metin: string; ilerleme: number; boyut: number; renk: string }> = ({ metin, ilerleme, boyut, renk }) => (
  <div style={{ position: "relative", display: "inline-block", fontFamily: fredoka, fontWeight: 700, fontSize: boyut, lineHeight: 1, color: renk, whiteSpace: "nowrap", clipPath: `inset(-20% ${100 - ilerleme * 100}% -20% -5%)` }}>
    {metin}
  </div>
);

export const PropKatman: React.FC<{ proplar: Prop[]; t: number; uzay: "ekran" | "sahne" }> = ({ proplar, t, uzay }) => (
  <>
    {proplar.map((p, i) => {
      const pu = p.tur === "banknot" || p.tur === "tahtaYazi" ? "sahne" : p.tur === "ikon" ? p.uzay ?? "ekran" : "ekran";
      if (pu !== uzay) return null;
      if (t < p.bas - 1e-6) return null;
      if ("bitis" in p && p.bitis !== undefined && t >= p.bitis) return null;
      switch (p.tur) {
        case "banknot": {
          // düşüş: 3 kare (üstten), çarpma anında hafif sekme
          const d = p.dus ? interpolate(t, [p.bas, p.bas + 0.1], [-(p.yukseklik ?? 700), 0], { ...CL, easing: Easing.in(Easing.quad) }) : 0;
          const sek = p.dus ? interpolate(t, [p.bas + 0.1, p.bas + 0.16, p.bas + 0.24], [0, -14, 0], CL) : 0;
          return (
            <div key={i} style={{ position: "absolute", left: p.x, top: p.y, transform: `translate(-50%,-50%) translateY(${d + sek}px) rotate(${p.aci ?? 0}deg) scale(${p.olcek ?? 1})`, filter: "drop-shadow(0 10px 8px rgba(0,0,0,0.35))" }}>
              <Banknot />
            </div>
          );
        }
        case "ikon": {
          const g = yay(t, p.bas);
          const c = cikis(t, p.bitis);
          const parla = p.parla ? 0.6 + 0.4 * Math.sin((t - p.bas) * 8) : 0;
          return (
            <div key={i} style={{ position: "absolute", left: p.x, top: p.y, transform: `translate(-50%,-50%) scale(${g * c}) rotate(${(1 - g) * -25}deg)` }}>
              <Ikon ad={p.ad} boyut={p.boyut ?? 160} parla={parla} />
            </div>
          );
        }
        case "ikonSira": {
          const c = cikis(t, p.bitis);
          const b = p.boyut ?? 170;
          return (
            <div key={i} style={{ position: "absolute", left: GUVENLI.sol, width: GUVENLI_W, top: p.y, display: "flex", justifyContent: "center", alignItems: "center", gap: 26, opacity: c }}>
              {p.ogeler.map((o, j) => {
                const g = yay(t, o.t);
                return (
                  <React.Fragment key={j}>
                    {j > 0 && p.ayrac ? (
                      <div style={{ fontFamily: anton, fontSize: 70, color: "#fff", WebkitTextStroke: "8px #0b0d12", paintOrder: "stroke fill", opacity: g }}>{p.ayrac}</div>
                    ) : null}
                    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", transform: `scale(${g}) translateY(${(1 - g) * 40}px)` }}>
                      <Ikon ad={o.ad} boyut={b} />
                      {o.etiket ? (
                        <div style={{ marginTop: 6, fontFamily: fredoka, fontWeight: 700, fontSize: 38, color: "#fff", WebkitTextStroke: "7px #0b0d12", paintOrder: "stroke fill" }}>{o.etiket}</div>
                      ) : null}
                    </div>
                  </React.Fragment>
                );
              })}
            </div>
          );
        }
        case "ilan":
          return <IlanKarti key={i} p={p} t={t} />;
        case "telefon":
          return <Telefon key={i} p={p} t={t} />;
        case "tahtaYazi":
          return (
            <React.Fragment key={i}>
              {p.satirlar.map((s, j) => {
                if (t < s.t) return null;
                const tiklar = s.tik ?? [];
                // tik listesi: kök ("$1") süre içinde yazılır, sonra her tikte bir sıfır eklenir (virgüller kendiliğinden)
                let metin = s.metin;
                const ilerleme = interpolate(t, [s.t, s.t + (s.sure ?? 0.6)], [0, 1], { ...CL, easing: Easing.inOut(Easing.quad) });
                if (tiklar.length) {
                  const kok = s.metin.replace(/[0,]+$/, "");
                  const n = tiklar.filter((x) => t >= x).length;
                  const sayi = Number(kok.replace(/[^0-9]/g, "") + "0".repeat(n));
                  metin = kok.replace(/[0-9]+$/, "") + sayi.toLocaleString("en-US");
                }
                return (
                  <div key={j} style={{ position: "absolute", left: s.x, top: s.y, transform: "rotate(-2deg)" }}>
                    <ElYazisi metin={metin} ilerleme={ilerleme} boyut={s.boyut} renk={s.renk ?? "#1f3f8f"} />
                  </div>
                );
              })}
            </React.Fragment>
          );
        case "tahtaKose": {
          const g = yay(t, p.bas);
          const c = cikis(t, p.bitis);
          const ilerleme = interpolate(t, [p.yaz, p.yaz + 0.9], [0, 1], { ...CL, easing: Easing.inOut(Easing.quad) });
          return (
            <div key={i} style={{ position: "absolute", left: p.x, top: p.y, transform: `scale(${g * c}) rotate(-3deg)`, transformOrigin: "0 0" }}>
              <div style={{ padding: "22px 30px", borderRadius: 16, background: "#f7f8fa", border: "10px solid #b9bec7", boxShadow: "0 14px 30px rgba(0,0,0,0.5)" }}>
                <ElYazisi metin={p.metin} ilerleme={ilerleme} boyut={64} renk="#1f3f8f" />
              </div>
            </div>
          );
        }
        case "yazi": {
          const g = yay(t, p.bas, { damping: 10, stiffness: 220, mass: 0.6 });
          const c = cikis(t, p.bitis);
          return (
            <div key={i} style={{ position: "absolute", left: GUVENLI.sol, width: GUVENLI_W, top: p.y, textAlign: "center", transform: `scale(${(0.4 + 0.6 * g) * (0.9 + 0.1 * c)})`, opacity: Math.min(1, g * 2) * c }}>
              <span style={{ fontFamily: anton, fontSize: p.boyut ?? 120, letterSpacing: 4, color: p.renk ?? ALTIN, WebkitTextStroke: "14px #0b0d12", paintOrder: "stroke fill", textShadow: "0 8px 0 rgba(0,0,0,0.35)" }}>
                {p.metin}
              </span>
            </div>
          );
        }
      }
      return null;
    })}
  </>
);
