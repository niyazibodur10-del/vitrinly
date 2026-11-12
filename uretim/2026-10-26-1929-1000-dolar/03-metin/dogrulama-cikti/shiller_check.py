import sys
sys.path.insert(0, sys.argv[1])
import xlrd
wb = xlrd.open_workbook(sys.argv[2]); sh = wb.sheet_by_name('Data')
rows = {}
for r in range(sh.nrows):
    v = sh.row_values(r)
    if isinstance(v[0], float) and 1920 < v[0] < 1960:
        d = f"{v[0]:.2f}"; rows[d] = (v[1], v[2], v[4])  # P, D (annualized), CPI
ks = sorted(rows)
start = '1929.09'
P0, D0, C0 = rows[start]
# nominal total return index (monthly reinvest D/12), real = /CPI
tr = 1.0; prevP = P0; out = []
for k in ks[ks.index(start)+1:]:
    P, D, C = rows[k]
    if not P or not C: continue
    tr *= (P + D/12) / prevP; prevP = P
    out.append((k, P/P0, tr, tr * C0 / C))
first_nom_tr = next((k for k, p, t, r in out if t >= 1), None)
first_real_tr = next((k for k, p, t, r in out if r >= 1), None)
first_price = next((k for k, p, t, r in out if p >= 1), None)
low = min(out, key=lambda x: x[3])
print("Shiller S&P Composite, start", start, "P0", P0)
print("price back >= start:", first_price)
print("nominal total return back:", first_nom_tr)
print("real total return back:", first_real_tr)
print("real TR low:", low[0], round(low[3], 3))
