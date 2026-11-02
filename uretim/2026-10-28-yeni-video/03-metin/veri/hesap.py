"""S08 rakam türetme (finans-dogrulayici, 2026-11-02). Çalıştır: python3 -I hesap.py  (girdi: bu klasör; xls için PYTHONPATH'te xlrd)
Ölçek: federal milyar $/yıl  ==  hane $/ay  (5.403,3 milyar $/yıl -> 5.403 $/ay). Stok (borç) için: T$ * 12 / 1e9 * 1e12/1e12 -> hane $ = borç$ * 12 / 1e9."""
import json, csv, os, sys
H=os.path.dirname(os.path.abspath(__file__)); j=lambda f: json.load(open(os.path.join(H,f)))
def mts(f,desc,seq=None,col='current_fytd_rcpt_outly_amt'):
    for r in j(f)['data']:
        if r['classification_desc']==desc and (seq is None or r.get('sequence_number_cd')==seq): return float(r[col])
m9=j('mts9.json')['data']; tot=[r for r in m9 if r['classification_desc']=='Total']
rec=[float(r['current_fytd_rcpt_outly_amt']) for r in tot if float(r['current_fytd_rcpt_outly_amt'])<6e12][0]
out=[float(r['current_fytd_rcpt_outly_amt']) for r in tot if float(r['current_fytd_rcpt_outly_amt'])>6e12][0]
recp=[float(r['prior_fytd_rcpt_outly_amt']) for r in tot if float(r['prior_fytd_rcpt_outly_amt'])<6e12][0]
outp=[float(r['prior_fytd_rcpt_outly_amt']) for r in tot if float(r['prior_fytd_rcpt_outly_amt'])>6e12][0]
g=lambda d,c='current_fytd_rcpt_outly_amt': mts('mts9.json',d,col=c)/1e9
b=1e9; print(f"FY2026 gelir {rec/b:.1f} gider {out/b:.1f} açık {(out-rec)/b:.1f} milyar$ | FY2025 gelir {recp/b:.1f} gider {outp/b:.1f} açık {(outp-recp)/b:.1f}")
print(f"hane/ay: gelir ${rec/b:,.0f} gider ${out/b:,.0f} açık ${(out-rec)/b:,.0f} | gider/gelir {out/rec:.3f} -> 5$ başına {5*out/rec:.2f}$ | açık/gider {(out-rec)/out:.1%}")
kal=['Social Security','Medicare','Health','Net Interest','National Defense','Income Security','Veterans Benefits and Services','Individual Income Taxes','Employment and General Retirement','Corporation Income Taxes','Customs Duties']
for k in kal: print(f"  {k:36s} FY26 {g(k):8.1f}  FY25 {g(k,'prior_fytd_rcpt_outly_amt'):8.1f}  hane ${g(k):,.0f}/ay  gelirin {g(k)*b/rec:.1%}  gideri {g(k)*b/out:.1%}")
ni=g('Net Interest'); print(f"net faiz/gelir {ni*b/rec:.1%} (1/{rec/(ni*b):.2f}); net faiz-savunma {ni-g('National Defense'):.1f}; net faiz YoY {ni/g('Net Interest','prior_fytd_rcpt_outly_amt')-1:.1%}")
# tarih: MTS net faiz, savunma, gelir
hist={}
for f in ('mts9_net_interest_hist.jsonl','mts9_defense_total_hist.jsonl'):
    for l in open(os.path.join(H,f)):
        if l.strip():
            for r in json.loads(l)['data']:
                v=float(r['current_fytd_rcpt_outly_amt'])/b; y=r['record_date'][:4]; k=r['classification_desc']
                if k=='Total': k='Gelir' if r.get('sequence_number_cd')=='1.8' else 'Gider'
                hist.setdefault(y,{})[k]=v
hist['2026']={'Net Interest':ni,'National Defense':g('National Defense'),'Gelir':rec/b,'Gider':out/b}
for y in sorted(hist): h=hist[y]; print(f"  FY{y} net faiz {h.get('Net Interest',0):7.1f} savunma {h.get('National Defense',0):6.1f} gelir {h.get('Gelir',0):7.1f} faiz/gelir {h.get('Net Interest',0)/h.get('Gelir',1):.1%}")
print(f"net faiz FY2021->FY2026 x{ni/hist['2021']['Net Interest']:.2f}")
# borç
d=j('debt_to_penny.json')['data']; e=[r for r in d if r['record_date']=='2026-09-30'][0]; L=d[0]
T=float(e['tot_pub_debt_out_amt']); P=float(e['debt_held_public_amt'])
print(f"borç 30 Eyl 2026: toplam {T/1e12:.2f} T$ halk {P/1e12:.2f} T$ | hane: toplam ${T*12/1e9:,.0f} halk ${P*12/1e9:,.0f} | borç/yıllık gelir toplam {T/rec:.2f} halk {P/rec:.2f} yıl")
print(f"son kayıt {L['record_date']}: toplam {float(L['tot_pub_debt_out_amt'])/1e12:.2f} halk {float(L['debt_held_public_amt'])/1e12:.2f}")
print(f"hane yıllık gelir ${rec*12/b:,.0f}")
# ortalama faiz
a=[(r['record_date'],float(r['avg_interest_rate_amt'])) for r in j('avg_interest_rates.json')['data'] if r['security_desc']=='Total Marketable']; a.sort()
mn=min(a,key=lambda x:x[1]); print(f"ort. faiz (Total Marketable): dip {mn} son {a[-1]} | 2019-12 {a[0]}")
def last(fn):
    rows=[r for r in csv.reader(open(os.path.join(H,fn)))][1:]; rows=[r for r in rows if r[1] not in ('','.')]; return rows[-1]
for s in ('DGS10','DTB3','DFEDTARU','GFDEGDQ188S','FYGFGDQ188S','A091RC1Q027SBEA','GDP'): print(' ',s,last(s+'.csv'))
gdp4=[float(r[1]) for r in list(csv.reader(open(os.path.join(H,'GDP.csv'))))[1:] if r[0] in ('2025-10-01','2026-01-01','2026-04-01','2026-07-01')]
print(f"FY2026 GSYH ~ (Q4'25–Q3'26 SAAR ort.) {sum(gdp4)/4/1000:.2f} T$ (n={len(gdp4)}) | açık/GSYH {(out-rec)/(sum(gdp4)/4*1e9):.1%}")
# OMB 7.1
try:
    import openpyxl, warnings; warnings.simplefilter('ignore')
    ws=openpyxl.load_workbook(os.path.join(H,'omb_t7_1_fy2025.xlsx'),data_only=True).active; R={}
    for r in ws.iter_rows(values_only=True):
        if r[0] and str(r[0]).strip()[:4].isdigit() and 'estimate' not in str(r[0]) and isinstance(r[3],(int,float)): R[int(str(r[0]).strip()[:4])]=r
    pk=max(R,key=lambda y:R[y][8]); lo=min((y for y in R if y>1946),key=lambda y:R[y][8])
    print(f"OMB 7.1 halk/GSYH zirve {pk} %{R[pk][8]} ; dip {lo} %{R[lo][8]} ; 1946 %{R[1946][8]} (${R[1946][3]/1e3:.1f} mlr) -> 1974 %{R[1974][8]} (${R[1974][3]/1e3:.1f} mlr); brüt 1946 %{R[1946][6]} 1974 %{R[1974][6]}; 2023 halk %{R[2023][8]} brüt %{R[2023][6]}")
except Exception as ex: print('OMB atlandı', ex)
try:
    import xlrd; s=xlrd.open_workbook(os.path.join(H,'shiller_ie_data.xls')).sheet_by_name('Data'); c={}
    for i in range(s.nrows):
        r=s.row_values(i)
        try: c[round(float(r[0]),2)]=float(r[4])
        except: pass
    print(f"CPI (Shiller) Ara45->Ara46 {c[1946.12]/c[1945.12]-1:.1%} ; Ara46->Ara47 {c[1947.12]/c[1946.12]-1:.1%} ; Haz46->Haz74 yıllık {(c[1974.06]/c[1946.06])**(1/28)-1:.2%}")
except Exception as ex: print('Shiller atlandı', ex)
