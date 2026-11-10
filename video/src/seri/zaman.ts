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
