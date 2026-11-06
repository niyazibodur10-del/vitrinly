#!/usr/bin/env python3
"""S08 ölçek hesabı (D1). Girdi: on-dogrulama.md §4 S08 satırları (MTS FY2026, Debt to the Penny 30 Eyl 2026).
Ölçek: hane $/ay = federal milyar $/yıl  (5.403,3 milyar $/yıl -> 5.403 $/ay).
Stok (borç) için: borç / yıllık gelir oranı korunur -> hane borcu = borç/gelir x (hane aylık gelir x 12).
[RAKAM?] satırları finans-dogrulayici teyidi bekler (Treasury avg_interest_rates, FRED FYPUGDA188S)."""
G, H = 5403.3, 7395.8          # milyar $ gelir / gider (MTS Table 1, FY2026)
K = dict(sosyal_guvenlik=1667.1, medicare=1072.6, saglik=1025.6, net_faiz=1051.8, savunma=965.2)  # MTS Table 9
BORC_HALK, BORC_TOPLAM = 32.43e3, 40.17e3   # milyar $ (Debt to the Penny)
print(f"olcek: 1 $/ay = 1 milyar $/yil | gelir {G:.1f} $/ay | gider {H:.1f} $/ay | acik {H-G:.1f} $/ay")
for k, v in K.items(): print(f"{k}: {v:.1f} $/ay")
ilk3 = K['sosyal_guvenlik'] + K['medicare'] + K['saglik']
diger = H - sum(K.values())
print(f"ilk 3 zarf toplami: {ilk3:.1f} $/ay")
print(f"diger her sey: {diger:.1f} $/ay")
print(f"faiz/gelir: {K['net_faiz']/G*100:.1f} % | faiz/acik: {K['net_faiz']/(H-G)*100:.1f} % | faiz-savunma: {K['net_faiz']-K['savunma']:.1f} $/ay")
yillik = G * 12   # hane yillik geliri ($)
for ad, b in (("halk", BORC_HALK), ("toplam", BORC_TOPLAM)):
    print(f"hane borcu ({ad}): {b/G*yillik:,.0f} $ = {b/G:.2f} yillik gelir")
r21, r26 = 1.470, 3.518   # [RAKAM?] Treasury avg_interest_rates Total Marketable 2021-09-30 / 2026-09-30
print(f"[RAKAM?] ort. faiz 2021->2026: {r21} -> {r26} % = x{r26/r21:.2f}")
