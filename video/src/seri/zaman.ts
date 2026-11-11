import type {
  AgizCue,
  AgizSekli,
  Kelime,
  Konusmaci,
  Satir,
  SatirDosyasi,
  ZamanJson,
} from "./tipler";

/** Whisper kelime dosyası (ses-yonetmeni `kelimeler.json`: {"words":[{"w","s","e","p"}]}). */
export type WhisperKelimeler = { words: { w: string; s: number; e: number }[] };

/** ses-yonetmeni'nin <ad>.zaman.json'unu (tools/ses/diyalog.py) şablon biçimine çevirir.
 *  `kelime` verilirse her Whisper kelimesi en çok örtüştüğü satıra atanır (Whisper boşluğa taşan kelime başı verebilir;
 *  orta nokta kuralı bölüm 001'de 177 kelimeden 1'ini düşürdü, 2026-11-10) → altyazı kesin zamanlı olur. */
export const satirDosyasi = (
  j: ZamanJson,
  kelime?: WhisperKelimeler,
): SatirDosyasi => {
  const ortus = (
    w: { s: number; e: number },
    s: { bas: number; bitis: number },
  ) => Math.min(w.e, s.bitis) - Math.max(w.s, s.bas);
  const sahip = (kelime?.words ?? []).map((w) => {
    let en = -1,
      deger = -Infinity;
    j.satirlar.forEach((s, i) => {
      const o = ortus(w, s);
      if (o > deger) {
        deger = o;
        en = i;
      }
    });
    return en;
  });
  return {
    sure: j.sure,
    satirlar: j.satirlar.map((s, i) => {
      const k = s.konusmaci.toLowerCase();
      if (k !== "jake" && k !== "mike")
        throw new Error(
          `[seri] satır ${s.no ?? i + 1}: bilinmeyen konuşmacı ${s.konusmaci}`,
        );
      const ws = kelime?.words
        .filter((_, wi) => sahip[wi] === i)
        .map((w) => ({
          k: w.w.trim(),
          bas: Math.min(Math.max(w.s, s.bas), s.bitis),
          bitis: Math.max(Math.min(w.e, s.bitis), s.bas),
        }));
      return {
        konusmaci: k,
        bas: s.bas,
        bitis: s.bitis,
        metin: s.metin,
        kelimeler: ws?.length ? ws : s.kelimeler,
      };
    }),
  };
};

/** t anında konuşan satır (yoksa null). */
export const aktifSatir = (satirlar: Satir[], t: number): Satir | null =>
  satirlar.find((s) => t >= s.bas && t < s.bitis) ?? null;

/** t'den önce başlamış son satır (satır arası boşlukta kamera son konuşmacıda kalsın diye). */
export const sonSatir = (satirlar: Satir[], t: number): Satir | null => {
  let son: Satir | null = null;
  for (const s of satirlar) if (s.bas <= t) son = s;
  return son;
};

/** Satırın kelimeleri; ses-yonetmeni kelime zamanı vermediyse harf sayısına göre orantılı dağıtılır. */
export const kelimeler = (s: Satir): Kelime[] => {
  if (s.kelimeler && s.kelimeler.length) return s.kelimeler;
  const parca = s.metin.split(/\s+/).filter(Boolean);
  const top = parca.reduce((a, p) => a + p.length + 1, 0);
  let t = s.bas;
  return parca.map((p) => {
    const d = ((p.length + 1) / top) * (s.bitis - s.bas);
    const k = { k: p, bas: t, bitis: t + d };
    t += d;
    return k;
  });
};

/** Altyazı için kelimeyi satır metnindeki yazımla eşle (Kokoro/Whisper token'ı noktalamasız olabilir). */
export const ekranKelimeleri = (s: Satir): Kelime[] => {
  const ks = kelimeler(s);
  const metin = s.metin.split(/\s+/).filter(Boolean);
  if (metin.length === ks.length)
    return ks.map((k, i) => ({ ...k, k: metin[i] }));
  return ks;
};

/** Altyazı öbekleri: satır içinde en fazla `max` kelime veya noktalama sonunda bölünür. */
export const obekler = (s: Satir, max = 4): Kelime[][] => {
  const out: Kelime[][] = [];
  let cur: Kelime[] = [];
  for (const k of ekranKelimeleri(s)) {
    cur.push(k);
    if (cur.length >= max || /[.!?,;:]$/.test(k.k)) {
      out.push(cur);
      cur = [];
    }
  }
  if (cur.length) out.push(cur);
  return out;
};

export const agizSekli = (
  cues: AgizCue[] | undefined,
  t: number,
): AgizSekli => {
  if (!cues) return "X";
  const c = cues.find((x) => t >= x.bas && t < x.bitis);
  return ((c?.sekil as AgizSekli) ?? "X") as AgizSekli;
};

export const konusuyor = (satirlar: Satir[], kim: Konusmaci, t: number) =>
  satirlar.some((s) => s.konusmaci === kim && t >= s.bas && t < s.bitis);

export const kare = (sn: number, fps: number) => Math.round(sn * fps);

/** Rhubarb A–H/X → 3 durum (kapali/yari/acik) — görsel-varlık eşlemesi (VARLIKLAR.md):
 *  X,A → kapali · B,F,G,H → yari · C,D,E → acik. Aynı durumlar birleşir; `minSn`'den kısa cue bir öncekine katılır
 *  (2 kareden kısa ağız titremesi okunmaz, göz yorar). Çıktı sekil alanı durum adıdır. */
export type AgizDurum = "kapali" | "yari" | "acik";
export const DURUM_ESLEME: Record<string, AgizDurum> = {
  X: "kapali", A: "kapali", B: "yari", F: "yari", G: "yari", H: "yari", C: "acik", D: "acik", E: "acik",
};
export const ucDurumAgiz = (cues: AgizCue[], minSn: number): { bas: number; bitis: number; sekil: AgizDurum }[] => {
  const birlestir = (l: { bas: number; bitis: number; sekil: AgizDurum }[]) => {
    const o: typeof l = [];
    for (const c of l) {
      const son = o[o.length - 1];
      if (son && son.sekil === c.sekil) son.bitis = c.bitis;
      else o.push({ ...c });
    }
    return o;
  };
  const ham = birlestir(cues.map((c) => ({ bas: c.bas, bitis: c.bitis, sekil: DURUM_ESLEME[c.sekil] ?? "kapali" })));
  const out: typeof ham = [];
  for (const c of ham) {
    const son = out[out.length - 1];
    if (son && c.bitis - c.bas < minSn - 1e-6) son.bitis = c.bitis; // kısa cue öncekine katılır
    else out.push({ ...c });
  }
  return birlestir(out);
};

/** t anındaki ağız: iki durum ve karışım oranı. Geçiş cue sınırına ORTALI `gecisSn` (2 kare: sınırdan 1 kare önce
 *  %0 → sınırda %50 → 1 kare sonra %100) — gecikme yok, ses ile ağız aynı karede döner. Sonuç: `alt` tam, `ust` p ile üstte. */
export const agizDurumu = (
  cues: { bas: number; bitis: number; sekil: AgizDurum }[] | undefined, t: number, gecisSn: number,
): { alt: AgizDurum; ust: AgizDurum; p: number } => {
  const bul = (x: number): AgizDurum => {
    if (!cues) return "kapali";
    let lo = 0, hi = cues.length - 1, i = -1;
    while (lo <= hi) { const m = (lo + hi) >> 1; if (cues[m].bas <= x) { i = m; lo = m + 1; } else hi = m - 1; }
    return i >= 0 && x < cues[i].bitis ? cues[i].sekil : "kapali";
  };
  const h = gecisSn / 2;
  const once = bul(t - h), sonra = bul(t + h);
  if (once === sonra || gecisSn <= 0) return { alt: bul(t), ust: bul(t), p: 1 };
  // sınır anı: (t-h, t+h] içinde durum değişimi; oran sınıra göre
  let lo = t - h, hi = t + h;
  for (let k = 0; k < 20; k++) { const m = (lo + hi) / 2; if (bul(m) === once) lo = m; else hi = m; }
  const p = Math.min(1, Math.max(0, (t - (hi - h)) / gecisSn));
  return { alt: once, ust: sonra, p };
};
