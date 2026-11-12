#!/usr/bin/env python3
"""DAX-S8 ROT017: actual Rivet 4.1.2 BELLE_2007_I749358 YODA3 numeric
140x12 angular closure and conditional R68 5MeV constant-bin convolution.
Requires stdlib only; uses original sha-pinned downloaded YODA .gz in same folder.
NOT byte-equal to primary HEPData; NOT complete pi pi QCD or PBH physics.
"""
import gzip,hashlib,json,math,pathlib,re,sys
from decimal import Decimal as D
src=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path("BELLE_2007_I749358.yoda.gz")
raw=src.read_bytes()
wanted='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(raw).hexdigest()==wanted, 'Original YODA source SHA differs'
s=gzip.decompress(raw).decode('utf8')
blocks=re.findall(r'(?ms)^BEGIN (YODA_[^ ]+) ([^\n]+)\n(.*?)^END YODA_[^\n]*',s)
assert len(blocks)==141
data={}
for typ,path,body in blocks:
    assert typ=='YODA_BINNEDESTIMATE<S>_V3'
    n=int(re.search(r'/d(\d+)-',path).group(1))
    match=re.search(r'(?m)^Edges\(A1\): (\[.*\])$',body)
    centers=[D(v) for v in json.loads(match.group(1))]
    rows=[]
    for line in body.splitlines():
        if re.match(r'^\s*[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?\s',line):
            rows.append([D(v) for v in line.split()])
    assert len(rows)==len(centers)
    data[n]=(centers,rows)
assert set(data)==set(range(1,142))
centers,values=data[1]
assert centers==[D('0.8025')+D('.005')*i for i in range(140)]
maxrel=D(0)
for i in range(140):
    theta,rows=data[i+2]
    assert theta==[D('.025')+D('.05')*j for j in range(12)]
    reconstructed=D('.05')*sum((row[0] for row in rows),D(0))
    rel=abs(reconstructed-values[i][0])/values[i][0]
    maxrel=max(maxrel,rel)
assert maxrel<D('0.00006')
E=1436554.0;T=.07818527068831995;C=4*E*T
h=lambda w:4*w**3/(C*C)*(-math.log1p(-math.exp(-(w*w/C))))
nb_per_MeV2=float(D('197.3269804')**2*D(10000000))
# Simpson 3-point quadrature for each 5MeV bin; independently validated
# against 50-digit mpmath and scipy in full local research bundle.
K=0.0
for i in range(140):
    a=800.0+5*i;b=a+5.0;m=(a+b)/2
    K+=float(values[i][0])/nb_per_MeV2 * (b-a)/6*(h(a)+4*h(m)+h(b))
assert abs(K/3.886864669914784e-10-1)<1e-9
print(json.dumps({
 'status':'PASS_REAL_PACKAGED_BELLE_140x12_NUMERIC_CLOSURE_AND_SOURCE_MODEL',
 'original_YODA_sha256':wanted,'table_objects':len(data),
 'energies':140,'angular_bins_each':12,
 'max_relative_angular_closure':str(maxrel),
 'K_fiducial_R68_conditional_piecewise_constant':K,
 'scope':'Rivet secondary packaged reference source, not original HEPData byte identity; 5MeV bin-mean assumption, not full pion physical rate.'
},indent=2,sort_keys=True))
