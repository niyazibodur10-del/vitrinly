#!/usr/bin/env python3
"""Flip By Vote bölüm paketi — TEK KAYNAK. Metinler burada; çıktılar betikle üretilir, elle düzenlenmez.
Çıktı: teslim/yayin-paketi.json (yukle.py şeması), teslim/platform-metinleri.md, uretim/kanal-kimligi/flipbyvote-kanal-paketi.json
Kapılar (çıkış 1 = hata): politika satırları birebir, yasak kalıplar, karakter sınırları, kanal.py dogrula.
Kullanım: python3 paket-uret.py   (repo kökünden veya herhangi bir yerden)"""
import json, os, re, sys, importlib.util
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
BOL = os.path.join(KOK, "uretim/seri/bolum-001")
TESLIM = os.path.join(BOL, "teslim")

POLITIKA = "Fiction. Not financial advice. Voices and visuals are AI-generated."
ANONIM = "We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment."
SORU = "Bike, dresser, or mystery box? Tell us in the comments."  # B01 + B02, videodaki soru birebir

# ---- YouTube Shorts ----
YT_BASLIK = "$100 to $1,000,000 — You Make Every Move · Ep. 1"
YT_ACIKLAMA = "\n".join([
    "Jake & Mike start with $100. The goal: $1,000,000. You decide every move.",
    "Episode 1: a $60 road bike with flat tires, a free dresser that has to go today, or a $40 mystery box of old games. " + SORU,
    "", ANONIM, "", POLITIKA, "", "#Shorts #flipbyvote #animatedseries"])
YT_ETIKET = ["Flip By Vote", "flipbyvote", "animated series", "interactive story", "you decide", "100 to 1 million",
             "flipping", "reselling", "side hustle", "garage sale", "furniture flip", "bike flip", "mystery box",
             "Jake and Mike", "animation", "cartoon"]
YT_KATEGORI = "24"  # Entertainment: kurgu dizi (eğitim değil)
PIN_YORUM = ("Mike wants the bike. Jake wants the dresser. Nobody trusts the box yet. Which one would you pick, and why? "
             "Got a better idea than all three? Tell us that too.\n\n" + ANONIM)

# ---- Instagram Reels ----
IG_ACIKLAMA = "\n".join([
    "Bike, dresser, or mystery box? You pick our first flip.",
    "Jake & Mike have $100 and one goal: $1,000,000. Every episode, the comments decide the next move.",
    SORU, "", ANONIM, "", POLITIKA, "", "#flipbyvote #animatedseries #sidehustle #flipping #youdecide"])
IG_KAPAK_SN = 81.0  # kare 2430 (koordinatör kapak kararı); yüklenen kapak bu kareden; uygulamada kare seçilirse 1:21
VIDEO_SHA12, VIDEO_SURE = "6d01844629ec", 83.2  # tur 3 render 2026-11-11
IG_SABIT_YORUM = PIN_YORUM

# ---- TikTok ----
TT_ACIKLAMA = "\n".join([
    "Bike, dresser, or mystery box? You pick our first flip. Ep. 1 of $100 → $1,000,000. Tell us in the comments.",
    "", ANONIM, "", POLITIKA, "", "#flipbyvote #animation #sidehustle #reselling #youdecide"])

# ---- Kanal (YouTube) ----
KANAL_ACIKLAMA = "\n".join([
    "An animated series where the comments make the moves: Jake and Mike start with $100, the goal is $1,000,000, and you decide what they do next.",
    "",
    "How it works:",
    "• Every episode ends on a real choice: what to buy, fix, sell or skip.",
    "• Suggest the next move in the comments. The best idea shapes the next episode.",
    "• " + ANONIM,
    "",
    "Flipping, haggling, garage-sale finds and bad ideas that sometimes work, told as a story you steer.",
    "",
    POLITIKA + " Jake and Mike are cartoon characters, not advisors.",
    "",
    "Start with Episode 1 and see where the comments take them."])
KANAL_KELIME = ('"Flip By Vote" flipbyvote "animated series" "interactive story" "you decide" "100 to 1 million" '
                'flipping reselling "side hustle" "garage sale" "furniture flip" "thrift flip" "animated comedy" '
                '"Jake and Mike" animation cartoon')
BANNER = {"ana": "FLIP BY VOTE", "alt": "$100 → $1,000,000 · YOU DECIDE THE MOVES"}
LISTE = {"baslik": "Flip By Vote · Season 1: $100 to $1,000,000",
         "aciklama": "Jake and Mike start with $100 and one goal: $1,000,000. Every episode ends on a choice, and the comments decide "
                     "what happens next. Watch in order from Episode 1.\n\n" + POLITIKA, "gizlilik": "public"}

YASAK = re.compile(r"\b(tomorrow|daily|every ?day|drops?|comment (?:[a-c1-3])\b|like if|tag a friend|share|win|winner|giveaway|prize|"
                   r"subscribe|follow|you should|invest|guarantee|vote for)\b", re.I)


def kontrol():
    h = []
    metinler = {"YT açıklama": YT_ACIKLAMA, "IG açıklama": IG_ACIKLAMA, "TikTok açıklama": TT_ACIKLAMA, "Kanal açıklama": KANAL_ACIKLAMA}
    for ad, m in metinler.items():
        satirlar = m.split("\n")
        if not any(s == POLITIKA or s.startswith(POLITIKA + " ") for s in satirlar): h.append(f"{ad}: politika satırı birebir yok")
        if not any(s.endswith(ANONIM) for s in satirlar): h.append(f"{ad}: anonim satırı birebir yok")
    for ad, m in {**metinler, "pinli yorum": PIN_YORUM, "başlık": YT_BASLIK, "liste": LISTE["aciklama"], "banner": " ".join(BANNER.values())}.items():
        for y in YASAK.findall(m): h.append(f"{ad}: yasak kalıp '{y}'")
    if len(YT_BASLIK) > 60: h.append(f"YT başlık {len(YT_BASLIK)} > 60")
    if len(KANAL_ACIKLAMA) > 1000: h.append(f"kanal açıklama {len(KANAL_ACIKLAMA)} > 1000")
    if len(KANAL_KELIME) > 500: h.append("kanal anahtar kelime > 500")
    if len(IG_ACIKLAMA) > 2200: h.append("IG açıklama > 2200")
    if len(TT_ACIKLAMA) > 2200: h.append("TikTok açıklama > 2200 (güvenli sınır)")
    if IG_ACIKLAMA.count("#") > 5 or TT_ACIKLAMA.count("#") > 5: h.append("hashtag > 5")
    # dosya kontrolü: paket doğru videoya bağlı mı
    import hashlib, subprocess
    vy = os.path.join(TESLIM, "bolum-001.mp4")
    if not os.path.isfile(vy): h.append("video yok")
    else:
        sha = hashlib.sha256(open(vy, "rb").read()).hexdigest()[:12]
        if sha != VIDEO_SHA12: h.append(f"video sha {sha} ≠ {VIDEO_SHA12}")
        sure = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vy],
                                    capture_output=True, text=True).stdout)
        if abs(sure - VIDEO_SURE) > 0.05: h.append(f"video süresi {sure:.2f} ≠ {VIDEO_SURE}")
        if not 0 < IG_KAPAK_SN < sure: h.append("kapak karesi video dışında")
    # videodaki soru = paketteki soru (metin B01+B02)
    bt = open(os.path.join(BOL, "bolum.txt"), encoding="utf-8").read()
    for parca in ("Bike, dresser, or mystery box?", "Tell us in the comments."):
        if parca not in bt: h.append(f"soru videoda yok: {parca}")
    return h


def main():
    h = kontrol()
    yp = {"sema": "yayin-paketi/1", "tur": "shorts",
          "dosyalar": {"video": "bolum-001.mp4", "altyazilar": []},
          "metadata": {"baslik": YT_BASLIK, "aciklama": YT_ACIKLAMA, "etiketler": YT_ETIKET, "bolumler": [],
                       "kategori_id": YT_KATEGORI, "varsayilan_dil": "en", "ses_dili": "en"},
          "durum": {"gizlilik": "private", "yayin_zamani": None, "cocuklara_ozel": False, "sentetik_medya": True,
                    "lisans": "youtube", "gomulebilir": True},
          "oynatma_listesi_id": None, "onay": {"niyazi_onayi": False, "tarih": None},
          "_not": ("yayin_zamani YER TUTUCU: Niyazi onayında belirlenir. Öneri 12:00 ET = 17:00Z = 20:00 TSİ (EST −05:00, 2026-11-01 sonrası). "
                   "sentetik_medya=true: politika-format.md §3 kararı (altered/synthetic = Yes). cocuklara_ozel=false zorunlu (§0 koşul 2). "
                   f"Video {VIDEO_SURE} sn, sha256 {VIDEO_SHA12}. Kaynak: paket/paket-uret.py; elle düzenleme yok.")}
    json.dump(yp, open(os.path.join(TESLIM, "yayin-paketi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    kp = {"aciklama": KANAL_ACIKLAMA, "anahtar_kelimeler": KANAL_KELIME, "varsayilan_dil": "en", "ulke": "TR",
          "oynatma_listeleri": [LISTE], "fragman_video_id": None, "banner_metni": BANNER,
          "_not": ("TASLAK — uygulama yalnız Niyazi onayıyla (kanal.py --uygula --onayli). Ülke TR değişmez (YPP ikamet). "
                   "Liste Bölüm 1 yüklendikten sonra açılır (boş liste yok). banner_metni kanal.py'ye girmez; görsel üretimi "
                   "gorsel/thumbnail ajanında. Gün/ritim sözü yok. Kaynak: uretim/seri/bolum-001/paket/paket-uret.py")}
    json.dump(kp, open(os.path.join(KOK, "uretim/kanal-kimligi/flipbyvote-kanal-paketi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    # kanal.py çevrimdışı doğrulama (ağ yok)
    sp = importlib.util.spec_from_file_location("kanal", os.path.join(KOK, "tools/yayin/kanal.py"))
    sys.path.insert(0, os.path.join(KOK, "tools/yayin")); km = importlib.util.module_from_spec(sp); sp.loader.exec_module(km)
    h += [f"kanal.py: {x}" for x in km.dogrula(kp, None)]
    md = ["# Bölüm 001 · platform metinleri (betik çıktısı: paket/paket-uret.py — elle düzenleme yok)", "",
          f"Video: `bolum-001.mp4` · {VIDEO_SURE} sn · 1080x1920 · sha256 {VIDEO_SHA12}", "",
          f"## YouTube Shorts\nBaşlık ({len(YT_BASLIK)} krk):\n```\n{YT_BASLIK}\n```\nAçıklama ({len(YT_ACIKLAMA)} krk):\n```\n{YT_ACIKLAMA}\n```",
          f"Etiketler: `{', '.join(YT_ETIKET)}` · Kategori 24 Entertainment · made for kids: No · altered/synthetic: Yes · dil en",
          f"\nSabit yorum (yayından sonra; Studio/uygulamada sabitlenir):\n```\n{PIN_YORUM}\n```",
          f"\n## Instagram Reels\nAçıklama ({len(IG_ACIKLAMA)}/2200 krk):\n```\n{IG_ACIKLAMA}\n```",
          f"Kapak: `kapak-1080x1920.jpg` yükle (kaynak kare {IG_KAPAK_SN:.2f} sn = kare {round(IG_KAPAK_SN*30)} = 1:21; uygulamada kare seçilirse 1:21); profil ızgarası kırpımı: `kapak-1080x1350.jpg`.",
          "AI etiketi (\"AI info\"): AÇIK (politika §3).",
          f"\nSabit yorum (ilk yorum olarak yazılır ve sabitlenir):\n```\n{IG_SABIT_YORUM}\n```",
          f"\n## TikTok\nAçıklama ({len(TT_ACIKLAMA)} krk):\n```\n{TT_ACIKLAMA}\n```",
          "Kapak: `kapak-1080x1920.jpg` (veya kare 1:21). AI-generated etiketi: AÇIK. Otomatik yorum yanıtı YOK (politika §5).", ""]
    open(os.path.join(TESLIM, "platform-metinleri.md"), "w", encoding="utf-8").write("\n".join(md))
    for x in h: print("HATA:", x)
    print(f"kapı: {len(h)} hata · YT başlık {len(YT_BASLIK)} · kanal açıklama {len(KANAL_ACIKLAMA)} · ilk 150: {KANAL_ACIKLAMA[:150]!r}")
    return 1 if h else 0


if __name__ == "__main__":
    sys.exit(main())
