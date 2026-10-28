import re,sys
L=open(sys.argv[1]).read().splitlines()
LAB=re.compile(r'\[(API|H|ALT|GÖZ|T|ÖB)[\],: ]')
head='';fails=[];n=0
assert '2026-10-28' in '\n'.join(L[:5]), 'üst bilgide ölçüm tarihi yok'
for i,l in enumerate(L,1):
    if l.startswith('## 7. Test'): break  # test bölümünün kendisi ölçüm değil
    if l.startswith('#'): head=l; continue
    if not re.search(r'\d',l) or re.match(r'\|[-| ]+\|$',l): continue
    if l.startswith('| ') and i>1 and re.match(r'\|[-| ]+\|$',L[i]) : continue  # tablo başlık satırı
    n+=1
    if LAB.search(l) or LAB.search(head) or '`' in l and 'uretim/' in l: continue
    fails.append((i,head[:40],l[:90]))
print('rakamlı satır',n,'etiketsiz',len(fails))
for f in fails: print(f)
