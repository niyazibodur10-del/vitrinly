#!/usr/bin/env python3
"""finans-dogrulayici bağımsız yeniden hesap (F3). Kullanım: python3 -I dogrulama-hesap.py [fdic3.txt]
Yazarın veri/hesap.py'sinden bağımsız yazıldı; aynı CSV'leri (canlı FRED ile 165/165 aynı) ve FDIC PDF metnini kullanır."""
import csv, os, re, sys, datetime as dt
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "veri")
cpi = {}
for f in ("cpi-1928-1934-CPIAUCNS.csv", "cpi-2019-2026-CPIAUCNS.csv"):
    for r in csv.DictReader(open(os.path.join(B, f))):
        if r["CPIAUCNS"].strip(): cpi[r["observation_date"][:7]] = float(r["CPIAUCNS"])
ch = lambda a, b: (cpi[b] / cpi[a] - 1) * 100
print("1) Borsa: 41.22/381.17-1 = %.2f%% | $1000 -> $%.2f" % ((41.22/381.17-1)*100, 1000*41.22/381.17))
print("   13 Kas 1929 ara dip 198.60 (Wikipedia tablosu) -> $%.0f ; 3 Eyl->13 Kas = %.1f hafta" % (1000*198.60/381.17, (dt.date(1929,11,13)-dt.date(1929,9,3)).days/7))
print("   28 Eki öncesi kapanış 260.64+38.33 = %.2f -> zirveden %.1f%% (Kara Pazartesi'den ÖNCE)" % (260.64+38.33, ((260.64+38.33)/381.17-1)*100))
print("   381/63 = x%.2f ; Ağu 1921 -> Eyl 1929 = %.1f yıl" % (381/63, (dt.date(1929,9,1)-dt.date(1921,8,1)).days/365.25))
print("2) TÜFE Eyl29->Tem32 %.2f%% | alım gücü $%.0f | 108$ reel: $%.1f" % (ch("1929-09","1932-07"), 1000*cpi["1929-09"]/cpi["1932-07"], 1000*41.22/381.17*cpi["1929-09"]/cpi["1932-07"]))
print("   TÜFE Eyl29->Mar33 %.2f%% | alım gücü $%.0f | endeks 100 -> %.1f" % (ch("1929-09","1933-03"), 1000*cpi["1929-09"]/cpi["1933-03"], 100*cpi["1933-03"]/cpi["1929-09"]))
print("   TÜFE Eyl22->Eyl26 %.2f%% (48 ay) | alım gücü $%.0f" % (ch("2022-09","2026-09"), 1000*cpi["2022-09"]/cpi["2026-09"]))
print("   eşit 42 ay: Mar23->Eyl26 %.2f%%" % ch("2023-03","2026-09"))
print("   TÜFE Eyl25->Eyl26 %.2f%% | alım gücü $%.0f" % (ch("2025-09","2026-09"), 1000*cpi["2025-09"]/cpi["2026-09"]))
print("3) BEA 1929: 50,460 M$ ücret (BEA NipaDataA A034RC) / 35,286 bin FTE (T6.5A) = $%.0f ; 1000/1430*12 = %.1f ay" % (50460e6/35286e3, 1000/1430*12))
t = list(csv.DictReader(open(os.path.join(B, "fdic-tablo5-askiya-alma-1921-1933.csv"))))
if len(sys.argv) > 1:
    txt = open(sys.argv[1]).read()
    pdf = {m[0]: (m[1], m[2], m[3]) for m in re.findall(r"^\s+(19[23]\d)\s+([\d,]+)\s+\$?([\d,]+)\s+\$?([\d,]+)\s", txt, re.M)}
    bad = [r["yil"] for r in t if pdf.get(r["yil"]) != tuple(f"{int(r[k]):,}" for k in ("askiya_alinan_banka","mevduat_bin_usd","mudi_kaybi_bin_usd"))]
    print("4) FDIC Tablo 5 CSV vs PDF metni: %d/%d satır aynı, farklı: %s" % (len(t)-len(bad), len(t), bad or "yok"))
s = [r for r in t if int(r["yil"]) >= 1930]
n = sum(int(r["askiya_alinan_banka"]) for r in s); dep = sum(int(r["mevduat_bin_usd"]) for r in s); los = sum(int(r["mudi_kaybi_bin_usd"]) for r in s)
print("   1930-33: %d banka | kayıp/mevduat %.2f%% (dolar ağırlıklı) | $1000 -> kayıp $%.0f, kalan $%.0f" % (n, 100*los/dep, 1000*los/dep, 1000-1000*los/dep))
print("   yıllık oranlar: " + ", ".join("%s %.1f%%" % (r["yil"], 100*int(r["mudi_kaybi_bin_usd"])/int(r["mevduat_bin_usd"])) for r in s))
for den, lab in ((24000, "FRH-BP ~24.000"), (24026, "B&MS Haz 1929 24.026"), (24504, "B&MS Oca 1929 24.504")):
    print("   %d / %s = %.1f%%" % (n, lab, 100*n/den))
print("   B&MS net düşüş Haz1929 24.026 -> Haz1933 14.440 = %d (%.1f%%)" % (24026-14440, 100*(24026-14440)/24026))
print("   '1/3 eşiği' için gereken payda < %d" % (n*3))
liq_low = (1350+2293)*2/3 + 4000
print("   'most closed for good' alt sınır (1930-31 x 2/3 + 1933 4.000, 1932=0): %.0f / %d = %.0f%%" % (liq_low, n, 100*liq_low/n))
print("5) Eyl 1929 -> Kas 1936 = %.1f yıl ; Tem 1932 -> Kas 1936 = %.1f yıl" % ((dt.date(1936,11,1)-dt.date(1929,9,3)).days/365.25, (dt.date(1936,11,1)-dt.date(1932,7,8)).days/365.25))
print("6) 4 Mart -> 6 Mart 1933 = %d gün" % (dt.date(1933,3,6)-dt.date(1933,3,4)).days)
# 7) Banka kapısı mudi açısından: askıya alınan bankalardaki mevduatın tüm ticari banka mevduatına payı
#    tüm mevduat = kayıp / (sütun 4 / 100)  (FDIC Tablo 5 sütun 4, Friedman-Schwartz)
kalan = 1.0
for r in s:
    tum = int(r["mudi_kaybi_bin_usd"]) / (float(r["kayip_tum_mevduat_yuzde"]) / 100)
    pay = int(r["mevduat_bin_usd"]) / tum
    kalan *= (1 - pay)
    print("7) %s: tüm ticari mevduat ≈ %.1f milyar $ | askıya alınan bankalarda pay %.1f%%" % (r["yil"], tum / 1e6, 100 * pay))
print("   1930-33 bileşik: mevduat dolarının ≈%.0f%%'i askıya alınan bir bankadaydı, ≈%.0f%%'i değildi" % (100 * (1 - kalan), 100 * kalan))
print("   ortalama bir banka dolarının beklenen kaybı (sütun 4 toplamı) ≈ %.1f%%" % sum(float(r["kayip_tum_mevduat_yuzde"]) for r in s))
