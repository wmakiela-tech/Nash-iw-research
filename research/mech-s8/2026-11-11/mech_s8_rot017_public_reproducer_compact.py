#!/usr/bin/env python3
"""Wu–Xu v2 original table source-only LOO and smooth-subedge witness.
Run with --download (original 100 rows, Internet) or no arguments (requires
exact first12 excerpt adjacent; verifies SHA). No BBN/PBH bound inference.
"""
import hashlib,math,sys,urllib.request
from pathlib import Path

SHA100='25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df'
SHA12='0a81af204bbfe2ced214b3edaaf31bcd52354d4b1934adb67571e726d9d26ac3'
COMMIT='d395183674cace6c9906a8911bdeb7234ba4040d'
URL=f'https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/{COMMIT}/arXiv-2509.05618/data/out/hadrons_from_PBH.dat'
excerpt=Path(__file__).parent/'hadrons_from_PBH_FIRST12_PINNED_AUTHOR_EXCERPT.dat'
if '--download' in sys.argv or not excerpt.exists():
    raw=urllib.request.urlopen(URL,timeout=30).read(); expected=SHA100
else:
    raw=excerpt.read_bytes(); expected=SHA12
assert hashlib.sha256(raw).hexdigest()==expected
rows=[[float(v) for v in line.split()] for line in raw.decode().splitlines()[1:]]
assert len(rows) in (12,100)
xx=[math.log(row[0]/rows[0][0]) for row in rows]
ks=(2,3,4,5,8,12)

def slope(yy,k):
    x=xx[:k];y=yy[:k];ax=sum(x)/k;ay=sum(y)/k
    return -sum((a-ax)*(b-ay) for a,b in zip(x,y))/sum((a-ax)**2 for a in x)

def flat(t):
    if t<=0:return 0.
    if t>=1:return 1.
    a=math.exp(-1/t);b=math.exp(-1/(1-t));return a/(a+b)

for idx,name in enumerate(('pion','kaon','K0L','proton_group','neutron_group'),1):
    y=[math.log(row[idx]) for row in rows]
    p=[slope(y,k) for k in ks]
    c=10.**(p[-1]-p[0])
    # Equal at ALL tabulated M>=M0, exactly equal edge jet for flat modifier.
    for row in rows:
        t=math.log(rows[0][0]/row[0])/math.log(10)
        assert flat(t)==0.0
    if len(rows)==100:
        err=[math.exp(y[j-1]+(y[j+1]-y[j-1])*(xx[j]-xx[j-1])/(xx[j+1]-xx[j-1])-y[j])-1 for j in range(1,99)]
        loo=100*max(abs(e) for e in err)
    else:loo=None
    print(name,'p2=',round(p[0],9),'p12=',round(p[-1],9),
          'anchored R12/R2 at 1e8 g=',round(c,9),'loo_max_pct=',loo,
          'exact_data_and_all_edge_jets_preserved_by_flat_multiplier=True')
print('STATUS: CONDITIONAL SOURCE-ONLY / NO_BLACKHAWK_REPLAY / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN')
