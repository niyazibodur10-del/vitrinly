import React from "react";
import { AbsoluteFill, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ALTYAZI, Cue, SAHNELER, SHORTS_EK } from "./veri-sahne";
import { Doku, fredoka } from "./ortak";
import { f, Leo } from "./kit";
import { YER_TUTUCU_RIG } from "./rig";
import { Kes, plan, sure } from "./zaman";
import {
  AileKapi, Banknot, BantEl, BantKutu, Bayrak, BuyuyenKutu, DevKutu, Dilim, EkranYazilari, EsTabela, Etiket, Fatura, Faturalar, G1, G19, G2, G3, G4, G5, G7,
  Gise, GriSac, Hayalet, Ikonlar, Kapilar, KaynakSatiri, KutuDizisi, Omur, OrnekEtiket, Pano, PanoSatir, Saat, Selale, Siluet, Sold, Solma, Soz, SoruKutu,
  Kesik, PlakaArka, Tabela, Tabelalar, Tez, UkKart, useDikey, YedideBir, YerTutucu, YolHaritasi, YolIsareti, Zemin, ka,
} from "./grafik";

// Sahne çatısı (animasyon-yonetmeni, 2026-11-04 iskelet): her sahne = zaman.ts kesme listesi; her kesme bir çekim anahtarı
// (CEKIM) → kodla çizilen grafik ya da yer tutucu plaka (Canva illüstrasyonu gelince "yer:<ad>" → Plaka + kamera).
// Aynı çatı 16:9 ve 9:16'da çalışır (grafikler useDikey ile yerleşir).
export const FPS = 30;
export const kare = (s: number) => Math.round(s * FPS);
export const TAM_KARE = kare(SAHNELER[SAHNELER.length - 1].bitis);
// Ses kolu teslim edince true (public/kmiras/anlatim.wav + shorts-1-ek.wav / shorts-2-ek.wav)
export const ANLATIM_HAZIR = false;
const sh = (id: string) => SAHNELER.find((x) => x.id === id)!;
const SON = -10; // "önceki sahnede oldu" (statik durum)

// ---------- Pano durumları (sızıntı çizelgesi; kutu-hesap.py sırası) ----------
const panoDurum = (sid: string, t0: number, k: Record<string, number>) => {
  const d = (deger: string, an = SON, renk?: string): PanoSatir => ({ deger, an, renk });
  const L = d("−2"), C = d("−1"), Sp = d("−0"), Gv = d("−1");
  switch (sid) {
    case "S07":
      return <Pano t0={t0} satir={[]} isimAn={[0, 1, 2, 3, 4, 5].map((i) => ka(k, "six", t0) + 0.2 + i * 0.25)} />;
    case "S11":
      return <Pano t0={t0} satir={[L, d("−1", ka(k, "label", t0 + 0.8))]} />;
    case "S12":
      return <Pano t0={t0} satir={[L, C]} alt={{ metin: "TWO STOPS · −3 BOXES", an: t0 + 0.3, renk: "#e05a4f" }} />;
    case "S14":
      return <Pano t0={t0} satir={[L, C, d("−0", ka(k, "zero", t0 + 0.3), "#2fae6a")]} kumSaati={ka(k, "zero", t0 + 0.3) + 0.6} />;
    case "S16":
      return <Pano t0={t0} satir={[L, C, d("−0", SON, "#2fae6a"), d("−1", ka(k, "label", t0 + 0.8))]} />;
    case "S18":
      return (
        <Pano
          t0={t0}
          satir={[{ ...L, tik: ka(k, "living", t0) }, { ...C, tik: ka(k, "care", t0 + 0.6) }, { ...d("−0", SON, "#2fae6a"), tik: ka(k, "detour", t0 + 1.2) }, { ...Gv, tik: ka(k, "giving", t0 + 1.8) }]}
          alt={{ metin: "6 BOXES STILL ON BOARD", an: ka(k, "giving", t0 + 1.8) + 0.6, renk: "#ffd43b" }}
          kumSaati={SON}
        />
      );
    case "S22":
      return <Pano t0={t0} satir={[{ ...L, cizgi: ka(k, "living", t0 + 0.5) }, { ...C, cizgi: ka(k, "care", t0 + 1) }, Sp, Gv, {}, { ...d("−0", t0 + 0.2, "#2fae6a"), cizgi: ka(k, "time", t0 + 1.5) }]} alt={{ metin: "TAX: −0 (FOR THIS FAMILY)", an: t0 + 0.3 }} />;
    default:
      return <Pano t0={t0} satir={[L, C, Sp, Gv]} />;
  }
};

// Konuşan Leo (rig) — Canva plakası üstünde; ağız çizelgesi sahnenin (veya ek kaydın) Rhubarb'ı.
// tip: kapi (M08 yol + kamyon yan kesiği, Leo sol-orta) · yakin (M08 bulanık) · kasa (M09 kasa içi) · kasaYakin
const LeoCekim: React.FC<{ id?: string; cues?: Cue[]; t0: number; tip: string; ad: string }> = ({ id, cues, t0, tip }) => {
  const D = useDikey();
  const yakin = tip === "yakin" || tip === "kasaYakin";
  const kasa = tip.startsWith("kasa");
  const p = D ? (yakin ? { x: 540, y: 760, s: 0.98 } : { x: 540, y: 860, s: 0.74 }) : yakin ? { x: 960, y: 420, s: 0.95 } : { x: 640, y: 470, s: 0.62 };
  return (
    <AbsoluteFill>
      <PlakaArka t0={t0} ad={kasa ? "M09" : "M08"} bulanik={yakin ? 5 : kasa ? 2 : 0} odakX={0.5} />
      {tip === "kapi" ? <Kesik ad="ham-kamyon-yan" x={D ? 760 : 1420} alt={D ? 560 : 70} w={D ? 760 : 900} /> : null}
      <Leo id={id} cues={cues} x={p.x} y={p.y} s={p.s} pozlar={[[0, "a"]]} tohum={Math.round(t0 * 7) + 3} />
      {YER_TUTUCU_RIG ? (
        <div style={{ position: "absolute", left: D ? 70 : 34, top: D ? 300 : 30, padding: "4px 10px", background: "rgba(224,90,79,0.85)", color: "#fff", fontFamily: fredoka, fontWeight: 700, fontSize: 20, borderRadius: 6 }}>
          RIG: S08 Leo kesiği (aynı karakter; bu videonun pano/bant rig pozları gelince değişir)
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

// Çekim anahtarı → bileşen. k = sahne planı çapaları (Shorts ek kaydında cümle zamanından kurulur)
export const Cekim: React.FC<{ sid: string; leoId?: string; leoCues?: Cue[]; kes: Kes; k: Record<string, number> }> = ({ sid, leoId, leoCues, kes, k }) => {
  const [t0, ad, , cekim = "yer"] = kes;
  const [anahtar, param] = cekim.split(":");
  switch (anahtar) {
    case "leo":
      return <LeoCekim id={leoId} cues={leoCues} t0={t0} tip={param ?? "kapi"} ad={ad} />;
    case "devKutu":
      return <DevKutu t0={t0} k={k} />;
    case "esTabela":
      return <EsTabela t0={t0} varyant={param === "s13" ? "s13" : "s01"} ikinci={k.nearly} />;
    case "g1":
      return <G1 t0={t0} k={k} varyant={(param as "es" | "bagis") ?? "temel"} />;
    case "etiket":
      return <Etiket t0={t0} />;
    case "soruKutu":
      return <SoruKutu t0={t0} />;
    case "aileKapi":
      return <AileKapi t0={t0} />;
    case "kutular": {
      // param: önceki kayıp sayısı (0, 4) ya da "yalniz" (S31: kiremit kutu tek başına parlar)
      const yeniS08 = sid === "S08" ? { n: 2, an: ka(k, "label", t0 + 0.6) } : undefined;
      const yukleme = sid === "S06" && ad.startsWith("10 kutu") ? [ka(k, "four1", t0 + 0.3), ka(k, "four2", t0 + 1), ka(k, "two3", t0 + 1.6)] : undefined;
      return (
        <Zemin t0={t0}>
          <KutuDizisi t0={t0} kayipOnce={param === "yalniz" ? 4 : Number(param) || 0} yeni={yeniS08} gizle={param === "4" || param === "yalniz"} giris={yukleme} yalniz={param === "yalniz" ? 0 : undefined} />
          {sid === "S19" ? <div style={{ position: "absolute", left: 0, right: 0, top: 120, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 64, color: "#f4f1ea", WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill" }}>4 OF 10 BOXES: THE HOUSE</div> : null}
          <OrnekEtiket />
        </Zemin>
      );
    }
    case "pano":
      return (
        <Zemin t0={t0}>
          {panoDurum(param ?? sid, t0, k)}
          <OrnekEtiket />
        </Zemin>
      );
    case "tabela":
      return (
        <AbsoluteFill>
          <YerTutucu t0={t0} ad={ad} plaka="yol + tabela" />
          <TabelaOrta metin={param ?? ad} t0={t0} kalp={param === "GIVING"} />
        </AbsoluteFill>
      );
    case "tabelalar":
      return <Tabelalar t0={t0} />;
    case "omur":
      return <Omur t0={t0} k={k} />;
    case "g2":
      return <G2 t0={t0} k={k} />;
    case "fatura":
      return <Fatura t0={t0} k={k} />;
    case "kapilar":
      return <Kapilar t0={t0} k={k} />;
    case "yedide1":
      return <YedideBir t0={t0} k={k} />;
    case "hayalet":
      return <Hayalet t0={t0} uc={param === "uc"} />;
    case "bantKutu":
      return <BantKutu t0={t0} k={k} />;
    case "bantEl":
      return <BantEl t0={t0} k={k} />;
    case "solma":
      return <Solma t0={t0} k={k} />;
    case "buyuyenKutu":
      return <BuyuyenKutu t0={t0} />;
    case "bayrak":
      return <Bayrak t0={t0} k={k} />;
    case "ikonlar":
      return <Ikonlar t0={t0} k={k} />;
    case "g3":
      return <G3 t0={t0} k={k} />;
    case "kararsiz":
      return <Kararsiz t0={t0} />;
    case "g19":
      return <G19 t0={t0} k={k} />;
    case "sold":
      return <Sold t0={t0} k={k} />;
    case "faturalar":
      return <Faturalar t0={t0} k={k} />;
    case "dilim":
      return <Dilim t0={t0} k={k} />;
    case "gise":
      return <Gise t0={t0} k={k} acik={param === "acik"} />;
    case "g4":
      return <G4 t0={t0} k={k} eyalet={param === "eyalet"} />;
    case "uk":
      return <UkKart t0={t0} k={k} />;
    case "saat":
      return <Saat t0={t0} k={k} yakin={param === "yakin"} />;
    case "griSac":
      return <GriSac t0={t0} />;
    case "g5":
      return <G5 t0={t0} k={k} />;
    case "banknot":
      return <Banknot t0={t0} k={k} />;
    case "yolIsareti":
      return <YolIsareti t0={t0} k={k} />;
    case "selale":
      return <Selale t0={t0} k={k} />;
    case "g7":
      return <G7 t0={t0} k={k} />;
    case "yolHaritasi":
      return <YolHaritasi t0={t0} k={k} />;
    case "soz":
      return <Soz t0={t0} metin="A FORECAST COUNTS MONEY BEFORE IT'S LIVED ON." />;
    case "tez":
      return <Tez t0={t0} />;
    default:
      return <YerTutucu t0={t0} ad={ad} plaka={param} />;
  }
};

const TabelaOrta: React.FC<{ metin: string; t0: number; kalp?: boolean }> = ({ metin, t0, kalp }) => {
  const D = useDikey();
  return <Tabela metin={metin} x={D ? 540 : 960} y={D ? 1150 : 760} an={t0 + 0.05} s={D ? 0.9 : 1} kalp={kalp} />;
};

// S17 sonu: kutu iki siluet arasında (sol-orta; ABONE-2 sağ altta)
const Kararsiz: React.FC<{ t0: number }> = ({ t0 }) => {
  const D = useDikey();
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const x = (D ? 540 : 700) + Math.sin((t - t0) * 2.2) * (D ? 160 : 140);
  return (
    <Zemin t0={t0}>
      <Siluet x={D ? 260 : 380} y={D ? 1200 : 900} h={D ? 520 : 460} renk="#26324d" />
      <Siluet x={D ? 820 : 1020} y={D ? 1200 : 900} h={D ? 500 : 440} renk="#26324d" />
      <div style={{ position: "absolute", left: x - 90, top: (D ? 820 : 520) + Math.abs(Math.sin((t - t0) * 2.2)) * -20, width: 180, height: 140, background: "#2f9e62", border: "6px solid #111", borderRadius: 8 }} />
      <div style={{ position: "absolute", left: D ? 60 : 120, top: D ? 300 : 90, fontFamily: fredoka, fontWeight: 700, fontSize: D ? 64 : 64, color: "#ffd43b", WebkitTextStroke: "7px #0b0b0b", paintOrder: "stroke fill", opacity: interpolate(t, [t0 + 0.2, t0 + 0.5], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
        WHO CARRIES THIS BOX NEXT?
      </div>
    </Zemin>
  );
};

// ---------- Sahne: aktif kesmenin çekimi + ekran yazıları + R-kodlu kaynak satırı ----------
export const Sahne: React.FC<{ id: string }> = ({ id }) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const p = plan(id);
  let i = 0;
  for (let j = 0; j < p.kes.length; j++) if (t >= p.kes[j][0]) i = j;
  return (
    <AbsoluteFill style={{ background: "#05070f", overflow: "hidden" }}>
      <Cekim key={i} sid={id} leoId={p.kes[i][2] ? id : undefined} kes={p.kes[i]} k={p.k} />
      <EkranYazilari liste={p.ekran} />
      <KaynakSatiri kayit={p.kaynak} son={sure(id)} />
    </AbsoluteFill>
  );
};

// Altyazı: ses-muhendisi parçaları (veri-sahne ALTYAZI, global zaman); ofs = sahnenin global başlangıcı. Kaynak: yeni-video/Tam.tsx
export const AltyaziParca: React.FC<{ ofs: number; alt?: number; boyut?: number; genislik?: number }> = ({ ofs, alt = 70, boyut = 74, genislik = 1500 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + ofs;
  const i = ALTYAZI.findIndex((c, k) => {
    const bas = c[0].s - 0.08;
    const son = k + 1 < ALTYAZI.length ? Math.min(ALTYAZI[k + 1][0].s - 0.08, c[c.length - 1].e + 0.9) : c[c.length - 1].e + 0.6;
    return t >= bas && t < son;
  });
  if (i < 0) return null;
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: alt, pointerEvents: "none" }}>
      <div style={{ display: "flex", gap: 18, flexWrap: "wrap", justifyContent: "center", maxWidth: genislik }}>
        {ALTYAZI[i].map((w, k) => {
          const p = interpolate(t, [w.s - 0.06, w.s + 0.05], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          return (
            <span key={k} style={{ fontFamily: fredoka, fontWeight: 700, fontSize: boyut, color: w.renk ?? "#ffffff", WebkitTextStroke: `${Math.round(boyut * 0.17)}px #0b0b0b`, paintOrder: "stroke fill", opacity: p, scale: String(0.85 + 0.15 * p), translate: `0px ${(1 - p) * 12}px`, display: "inline-block", textTransform: "uppercase" }}>
              {w.t.replace(/[,;:]$/, "")}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

export const SahneComp: React.FC<{ id: string; altyazi?: boolean }> = ({ id, altyazi = true }) => {
  const s = sh(id);
  const D = useDikey();
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {ANLATIM_HAZIR ? <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas)} trimAfter={kare(s.bitis)} /> : null}
      <Sahne id={id} />
      <Doku />
      {altyazi ? (D ? <AltyaziParca ofs={s.bas} alt={430} boyut={62} genislik={760} /> : <AltyaziParca ofs={s.bas} />) : null}
    </AbsoluteFill>
  );
};

export const Tam: React.FC<{ altyazi?: boolean }> = ({ altyazi = true }) => (
  <AbsoluteFill style={{ background: "#000" }}>
    {ANLATIM_HAZIR ? <Audio src={f("anlatim.wav")} /> : null}
    {SAHNELER.map((s) => (
      <Sequence key={s.id} from={kare(s.bas)} durationInFrames={kare(s.bitis) - kare(s.bas)} name={s.id} premountFor={30}>
        <Sahne id={s.id} />
      </Sequence>
    ))}
    <Doku />
    {altyazi ? <AltyaziParca ofs={0} /> : null}
  </AbsoluteFill>
);

// ---------- Kritik yol testi (H4): S01 tamamı (damla + bölünme + konuşan Leo) + S12 bant gag'i başı ----------
export const kritikParcalar = () => {
  const k12 = plan("S12").k;
  return [
    { id: "S01", bas: 0, sure: sh("S01").sure },
    { id: "S12", bas: 0, sure: Math.min(sh("S12").sure, k12.okay + 1.6) },
  ];
};
export const KRITIK_KARE = kritikParcalar().reduce((a, p) => a + kare(p.sure), 0);
export const KritikTest: React.FC = () => {
  let from = 0;
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {kritikParcalar().map((p) => {
        const s = sh(p.id);
        const el = (
          <Sequence key={p.id} from={from} durationInFrames={kare(p.sure)} name={p.id}>
            {ANLATIM_HAZIR ? <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas + p.bas)} trimAfter={kare(s.bas + p.bas + p.sure)} /> : null}
            <Sahne id={p.id} />
            <Doku />
            <AltyaziParca ofs={s.bas} />
          </Sequence>
        );
        from += kare(p.sure);
        return el;
      })}
    </AbsoluteFill>
  );
};

// ---------- 9:16 Shorts ----------
// (a) uzun anlatımdan dikey sahneler (Shorts 1: S01·S13·S14; Shorts 2: S21·S22) — kurgu-editoru keser
export const DIKEY_SAHNE = ["S01", "S13", "S14", "S21", "S22"] as const;
// (b) Shorts tam okuma (metin §5 "Okunacak tam metin", ayrı kayıt): cümle → çekim; aynı çekim art arda gelirse birleşir.
// Veri grafiği cümlesinin başında (≤1 sn) girer; son 3,5 sn alt orta boş (Shorts ABONE, kurgu-editoru).
const EK_CEKIM: Record<"sh1" | "sh2", string[]> = {
  sh1: ["devKutu", "etiket", "leo:yakin", "esTabela:s01", "solma", "esTabela:s13", "leo:yakin", "pano:S14", "pano:S14", "yer:karsiKaldirim", "leo:yakin", "buyuyenKutu", "soruKutu"],
  sh2: ["gise", "gise", "leo:yakin", "g4", "g4", "g4", "g4", "gise:acik", "soruKutu"],
};
export const ekPlan = (ek: "sh1" | "sh2") => {
  const c = SHORTS_EK[ek].cumleler;
  const anahtar = EK_CEKIM[ek];
  if (anahtar.length !== c.length) throw new Error(`${ek}: cümle ${c.length} ≠ çekim ${anahtar.length} (metin değişti → EK_CEKIM güncelle)`);
  const bas = (i: number) => Math.max(0, c[i].bas - 0.15);
  const kes: Kes[] = [];
  anahtar.forEach((a, i) => {
    if (i && anahtar[i - 1] === a) return;
    kes.push([bas(i), c[i].metin.slice(0, 40), a.startsWith("leo"), a]);
  });
  const k: Record<string, number> =
    ek === "sh1"
      ? { damla: 1.6, nearly: c[5].bas + 0.8, zero: c[7].bas, when: c[4].bas - 0.6 }
      : { so: c[2].bas, fifteen: c[3].bas + 4.3, median: c[5].bas + 4.5, the: c[6].bas, the2: c[7].bas + 0.4 };
  return { kes, k };
};
export const DEk: React.FC<{ ek: "sh1" | "sh2"; altyazi?: boolean }> = ({ ek, altyazi = true }) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const { kes, k } = ekPlan(ek);
  let i = 0;
  for (let j = 0; j < kes.length; j++) if (t >= kes[j][0]) i = j;
  const c = SHORTS_EK[ek].cumleler;
  const ci = c.findIndex((x, j) => t >= x.bas - 0.1 && (j + 1 >= c.length || t < c[j + 1].bas - 0.1));
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {ANLATIM_HAZIR ? <Audio src={f(ek === "sh1" ? "shorts-1-ek.wav" : "shorts-2-ek.wav")} /> : null}
      <Cekim key={i} sid={ek} leoCues={SHORTS_EK[ek].agiz} kes={kes[i]} k={k} />
      <KaynakSatiri kayit={ek === "sh1" ? [[0, "R01"], [c[3].bas, "R04"], [c[5].bas, "R05"]] : [[c[3].bas, "R18"], [c[5].bas, "R19"]]} son={SHORTS_EK[ek].sure} />
      <Doku />
      {altyazi && ci >= 0 ? <EkAltyazi metin={c[ci].metin} bas={c[ci].bas} son={c[ci].son} t={t} /> : null}
    </AbsoluteFill>
  );
};

// Ek kayıt altyazısı: cümle ≤6 kelimelik öbeklere, süre harf sayısıyla orantılı (kaynak: yeni-video/dikey.tsx). Ses gelince Whisper öbekleri.
const EkAltyazi: React.FC<{ metin: string; bas: number; son: number; t: number }> = ({ metin, bas, son, t }) => {
  const ws = metin.split(" ");
  const obek: string[][] = [];
  for (let i = 0; i < ws.length; i += 6) obek.push(ws.slice(i, i + 6));
  const top = ws.reduce((a, w) => a + w.length + 1, 0);
  let acc = bas, secili = obek[0];
  for (const o of obek) {
    if (t >= acc - 0.05) secili = o;
    acc += ((son - bas) * o.reduce((a, w) => a + w.length + 1, 0)) / top;
  }
  return (
    <div style={{ position: "absolute", left: 120, width: 840, bottom: 430, textAlign: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 62, color: "#fff", WebkitTextStroke: "10px #0b0b0b", paintOrder: "stroke fill", textTransform: "uppercase" }}>
      {secili.join(" ")}
    </div>
  );
};
