#!/usr/bin/env python3
"""Rakamlı her satırda etiket veya repo yolu var mı; üst bilgide ölçüm tarihi var mı.
Kullanım: etiket_test.py <dosya.md> <tarih> [--bolum '## v2' '---']  (bölüm verilirse yalnız o aralık)"""
import re,sys
f,tarih=sys.argv[1],sys.argv[2]; L=open(f).read().splitlines()
if '--bolum' in sys.argv:
    a,b=sys.argv[sys.argv.index('--bolum')+1:sys.argv.index('--bolum')+3]
    i0=next(i for i,l in enumerate(L) if l.startswith(a)); i1=next(i for i,l in enumerate(L) if i>i0 and l.startswith(b)); L=L[i0:i1]
assert tarih in '\n'.join(L[:5]), 'üst bilgide ölçüm tarihi yok'
LAB=re.compile(r'\[(API|H|ALT|GÖZ|T|ÖB|AÇK|AÖ)[\],: ]'); head='';fails=[];n=0
for i,l in enumerate(L):
    if l.startswith('## Test'): break
    if l.startswith('#'): head=l; continue
    if not re.search(r'\d',l) or re.match(r'\|[-| ]+\|$',l): continue
    if l.startswith('| ') and i+1<len(L) and re.match(r'\|[-| ]+\|$',L[i+1]): continue
    n+=1
    if LAB.search(l) or LAB.search(head) or ('`' in l and ('uretim/' in l or 'olcum/' in l)): continue
    fails.append((i+1,l[:90]))
print(f,'rakamlı satır',n,'etiketsiz',len(fails))
for x in fails: print('  ',x)
