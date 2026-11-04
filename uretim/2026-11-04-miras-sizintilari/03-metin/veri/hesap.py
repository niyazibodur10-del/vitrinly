"""S03 rakam tablosu hesapları + çift sayım assert'leri. Çalıştır: python3 -I hesap.py (veri/ içinden)."""
import csv, json, os
D = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(D, "kaynaklar.json")))
c = K["cerulli_2024_12_05"]
out = []
def p(*a): out.append(" ".join(str(x) for x in a))

# --- D2 çift sayım kapıları ---
son = c["mirascilara_T"] + c["bagis_T"]
assert abs(son - c["toplam_T"]) <= 1, "105+18 toplamı 124'ü yuvarlama içinde vermeli"
p(f"[D2] 105 + 18 = {son} ≈ 124 (fark {c['toplam_T']-son} T$, %{(c['toplam_T']-son)/c['toplam_T']*100:.1f}) → son varış noktaları toplamı")
assert son + c["ese_T"] > c["toplam_T"] + 1, "eş payı eklenirse toplam aşılır → 54 ayrı/ek kalem değil"
p(f"[D2] 105+18+54 = {son+c['ese_T']} > 124 → 54 ek kalem DEĞİL (aynı paranın durağı)")
yasak = c["toplam_T"] - c["ese_T"] - c["bagis_T"]
assert yasak == 52
p(f"[D2] YASAK çıkarma: 124-54-18 = {yasak} → metin/grafik/Shorts'ta geçerse RED")
assert c["dul_kadin_T"] < c["ese_T"]
p(f"[R05] 40 / 54 = %{c['dul_kadin_T']/c['ese_T']*100:.0f} eş transferi dul kadınlara")
assert c["boomer_ve_yasli_T"] / c["toplam_T"] * 100 > c["boomer_pay_yuzde"] - 1
p(f"[R06] 100/124 = %{c['boomer_ve_yasli_T']/c['toplam_T']*100:.1f} (bülten: %81, 'nearly 100')")
assert abs(c["hnw_T"] / c["toplam_T"] - 0.5) < 0.01  # bülten ">50%" diyor ama 62/124 = tam %50 → "about half"
p(f"[R07] 62/124 = %{c['hnw_T']/c['toplam_T']*100:.1f} → bültenin '>50%' ifadesi yuvarlama sınırında; metin 'about half' der")
p(f"[R03] bağış payı 18/124 = %{c['bagis_T']/c['toplam_T']*100:.1f} (~1/7)")
p(f"[R08] 85 - 46 = {c['genx_mill_T']-c['millennial_T']} T$ Gen X (25 yıl)")

b = K["bofa_2026_09_30"]
p(f"[R09] {b['hazir_2024']}% → {b['hazir_2026']}% = {b['hazir_2026']-b['hazir_2024']} puan")

# --- bakım ---
cs = K["carescout_2026_03_02"]
assert cs["nh_ozel_gun"] * 365 == cs["nh_ozel_yil"]; assert cs["nh_ortak_gun"] * 365 == cs["nh_ortak_yil"]
assert cs["assisted_ay"] * 12 == cs["assisted_yil"]
p(f"[R13] huzurevi özel oda {cs['nh_ozel_gun']}$/gün ×365 = {cs['nh_ozel_yil']:,}$/yıl; ortak {cs['nh_ortak_yil']:,}; assisted {cs['assisted_yil']:,}")
p(f"[R13] ayda ≈ {cs['nh_ozel_yil']/12:,.0f}$ (özel oda)")

# --- vergi eşiği vs tipik aile ---
irs = K["irs_2026"]; s = K["scf_2022"]
p(f"[R18] 15 M$ / 65–74 medyan {s['medyan_65_74_k']}k$ = {irs['muafiyet_usd']/(s['medyan_65_74_k']*1e3):.0f}x (birim farkı: 2026 nominal vs 2022 $ → yalnız 'dozens of times' yazılır)")
p(f"[R19] ortalama/medyan 65–74: {s['ort_65_74_k']/s['medyan_65_74_k']:.1f}x; 75+: {s['ort_75p_k']/s['medyan_75p_k']:.1f}x")
p(f"[R18] çift muafiyet (evli) 2×15 = {2*irs['muafiyet_usd']/1e6:.0f} M$ [AÖ: portability; metne girmez]")

# --- enflasyon örneği [H] ---
r = K["fed_hedef_enflasyon_yuzde"] / 100
for y in (10, 20, 24):
    p(f"[R21] %2 enflasyonda {y} yıl: 1$ alım gücü {1/(1+r)**y:.3f}")
assert 0.66 < 1/(1+r)**20 < 0.68

# --- Fed DFA (2026:Q2 son) ---
def son_satir(f):
    rows = list(csv.DictReader(open(os.path.join(D, f))))
    q = rows[-1]["Date"]
    return q, {x["Category"]: x for x in rows if x["Date"] == q}
q, g = son_satir("dfa-generation-shares.csv")
p(f"[R22] DFA {q} net servet payı: " + ", ".join(f"{k} {v['Net worth']}%" for k, v in g.items()))
p(f"[R23] DFA {q} gayrimenkul payı: " + ", ".join(f"{k} {v['Real estate']}%" for k, v in g.items()))
q2, lv = son_satir("dfa-generation-levels.csv")
bb = float(lv["BabyBoom"]["Net worth"]) / 1e6; tot = sum(float(v["Net worth"]) for v in lv.values()) / 1e6
p(f"[R22] DFA {q2} boomer net servet {bb:.1f} T$ / toplam {tot:.1f} T$ = %{bb/tot*100:.1f}; boomer gayrimenkul {float(lv['BabyBoom']['Real estate'])/1e6:.1f} T$")
q3, w = son_satir("dfa-networth-shares.csv")
top10 = sum(float(w[k]["Net worth"]) for k in ("TopPt1", "RemainingTop1", "Next9"))
p(f"[R24] DFA {q3} en üst %10 = {top10:.1f}% · en üst %1 = {float(w['TopPt1']['Net worth'])+float(w['RemainingTop1']['Net worth']):.1f}% · alt %50 = {w['Bottom50']['Net worth']}%")
assert top10 > 60 and float(w["Bottom50"]["Net worth"]) < 5
print("\n".join(out)); print("ASSERT: hepsi geçti")
