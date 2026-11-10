// Flip By Vote — dizi şablonu veri tipleri. Bir bölüm = tek bir `Bolum` nesnesi (bolumler/bolum-XXX.ts).
// Zamanlar SANİYE (bölüm başına göre); konumlar 1080x1920 kare pikseli (kamera dönüşümünden ÖNCEKİ sahne uzayı).

export type Konusmaci = "jake" | "mike";
export type AgizSekli = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "X";

/** Yer tutucu görsel: yalnız taslak render'da kabul edilir (yayın render'ı `dogrula` kapısında durur). */
export type YerTutucu = { yerTutucu: "blok" | "figur" | "agiz"; renk: string; renk2?: string };
/** `public/` altındaki dosya yolu (ör. "seri/bolum-001/s1-arka.png") veya yer tutucu. */
export type Gorsel = string | YerTutucu;

/** Ağız yolu (görsel-varlik-sanatcisi önerir, bölüm/sahne verisinde seçilir):
 *  yama   = konuşmacının ağız bölgesine Rhubarb A–H/X yama karesi (agiz.json gerekir)
 *  ifade  = yalnız ifade görseli değişir (konuşurken "konusur", dinlerken "notr" veya satırın ifadesi)
 *  kamera = ağız hareketi yok; kamera konuşan karaktere kayar/yaklaşır */
export type AgizYolu = "yama" | "ifade" | "kamera";

export type Kelime = { k: string; bas: number; bitis: number };
/** Şablonun iç satır biçimi (konuşmacı küçük harf). kelimeler opsiyonel; yoksa harf sayısına göre dağıtılır. */
export type Satir = { konusmaci: Konusmaci; bas: number; bitis: number; metin: string; kelimeler?: Kelime[] };
export type SatirDosyasi = { ses?: string; sure?: number; satirlar: Satir[] };
/** ses-yonetmeni çıktısı olduğu gibi: tools/ses/diyalog.py → <ad>.zaman.json
 *  {"sesler":{JAKE:"am_onyx:0.95",...}, "sure", "satirlar":[{"no","konusmaci":"JAKE","bas","bitis","metin", "kelimeler"?}]}
 *  zaman.ts satirDosyasi() ile şablon biçimine çevrilir (konuşmacı küçük harfe, bilinmeyen konuşmacı → hata). */
export type ZamanJson = {
  sesler?: Record<string, string>; sure?: number;
  satirlar: { no?: number; konusmaci: string; bas: number; bitis: number; metin: string; kelimeler?: Kelime[] }[];
};
export type AgizCue = { bas: number; bitis: number; sekil: AgizSekli | string };
export type AgizDosyasi = Partial<Record<Konusmaci, AgizCue[]>> & { kaynak?: unknown };

export type AgizYamasi = {
  /** yamanın sahne uzayındaki kutusu (px) */
  x: number; y: number; w: number; h: number;
  /** şekil → görsel; eksik şekil Rhubarb eşlemesiyle en yakın şekle düşer (G→F, H→C, X→A) */
  sekiller: Partial<Record<AgizSekli, Gorsel>> | YerTutucu;
};

export type KarakterSahne = {
  kim: Konusmaci;
  /** karakter katmanı; yoksa karakter arka plan görseline gömülüdür (yalnız odak/ağız konumu kullanılır) */
  gorsel?: Gorsel;
  /** katman kutusu (px): x,y sol üst; w,h boyut. Gömülü karakterde odak hesabı için yine verilir. */
  x: number; y: number; w: number; h: number;
  /** "ifade" yolu: ifade adı → görsel ("notr" ve "konusur" önerilir) */
  ifadeler?: Record<string, Gorsel>;
  /** "yama" yolu */
  agiz?: AgizYamasi;
  /** kamera odak noktası (yüz merkezi); varsayılan kutunun üst %22'si */
  odak?: { x: number; y: number };
};

export type Kamera = {
  /** yavaş hareket: başlangıç/bitiş ölçeği ve kayma (px). Varsayılan 1 → 1.06, kayma yok. */
  zoom?: [number, number];
  kay?: { x?: [number, number]; y?: [number, number] };
  /** konuşmacıya punch-in ölçeği (yama/ifade yolunda hafif, kamera yolunda güçlü). 1 = kapalı. */
  punch?: number;
  /** konuşmacı değişiminde geçiş süresi (sn); 0 = kesme (sert punch-in) */
  gecis?: number;
};

export type Sahne = {
  id: string;
  bas: number; bitis: number;
  arka: Gorsel;
  karakterler?: KarakterSahne[];
  agizYolu?: AgizYolu; // sahne düzeyinde; yoksa bölümün varsayılanı
  kamera?: Kamera;
  /** satır aralığına ifade ataması ("ifade" yolu): bu aralıkta kim hangi ifadede */
  ifadeler?: { bas: number; bitis: number; kim: Konusmaci; ifade: string }[];
};

export type BankOlayi = { t: number; deger: number; /** public/ yolu; false = sessiz; yoksa varsayılan */ ses?: string | false };

export type KazananYorum = { kullanici: string; metin: string; begeni?: number; bas?: number; sure?: number };

export type KararKarti = {
  soru: string;
  secenekler: string[]; // 2–3 seçenek; harfler A/B/C otomatik
  sure?: number; // 5–8 sn, bölüm sonuna yaslanır
};

export type SesKatmanlari = {
  diyalog: string; // public/ yolu (wav)
  muzik?: { dosya: string; ses?: number };
  sfx?: { dosya: string; ses?: number };
  /** şablonun kendi efektleri (BANK, abone klik, kart girişleri). Stem'de varsa false. */
  sablonSfx?: boolean;
};

export type Bolum = {
  /** kompozisyon kimliği, ör. "FBV-B001" */
  id: string;
  no: number;
  /** toplam süre (sn). Yayın kapısı: 60–90. */
  sure: number;
  satirlar: SatirDosyasi;
  agiz?: AgizDosyasi;
  agizYolu: AgizYolu;
  sahneler: Sahne[];
  bank: { baslangic: number; olaylar?: BankOlayi[] };
  ses: SesKatmanlari;
  kazananYorum?: KazananYorum;
  karar: KararKarti;
  /** abone/takip kartı; varsayılan karar kartından 0,4 sn önce biter. false = yok */
  abone?: { bas?: number } | false;
  /** logo dosyası (public/); yoksa şablonun geçici logosu */
  logo?: string;
};

export type BolumProps = { bolumId: string; taslak: boolean; kilavuz: boolean };
