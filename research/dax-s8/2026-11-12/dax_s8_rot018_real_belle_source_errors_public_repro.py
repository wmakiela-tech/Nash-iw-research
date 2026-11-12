#!/usr/bin/env python3
"""DAX-S8 ROT018: public pure-stdlib source-typed Belle marginal error gate.
Run from directory containing BELLE_2007_I749358.yoda.gz, SHA-pinned from
native official Rivet-data 4.1.2 packaged source, NOT primary HEPData byte match.
No experimental covariance or true hadronic/PBH rate is asserted.
"""
from pathlib import Path
import gzip,hashlib,json,math,re

source=Path("BELLE_2007_I749358.yoda.gz").read_bytes()
sha="28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403"
assert hashlib.sha256(source).hexdigest()==sha
body=gzip.decompress(source).decode("utf8")
name="BEGIN YODA_BINNEDESTIMATE<S>_V3 /REF/BELLE_2007_I749358/d01-x01-y01"
assert body.count(name)==1
table=body.split(name,1)[1].split("END YODA_BINNEDESTIMATE<S>_V3",1)[0]
assert 'ErrorLabels: ["stat", "sys"]' in table
centers=json.loads(table.split("Edges(A1): ",1)[1].splitlines()[0])
rows=[]
for line in table.splitlines():
    if re.match(r"^\s*[-+]?\d+\.\d+e[+-]\d+\s",line):
        x=[float(v) for v in line.split()]
        assert len(x)==5 and x[0]>0
        rows.append(x)
assert len(rows)==140 and len(centers)==140
assert abs(float(centers[0])-.8025)<1e-10
assert abs(float(centers[-1])-1.4975)<1e-10

E=1436554.0
T=.07818527068831995
C=4*E*T
unit=(197.3269804**2)*1e7
def h(w):
    return 4*w**3/C**2*(-math.log1p(-math.exp(-w*w/C)))
w=[]
for i in range(140):
    a=800.+5*i;b=a+5.;mid=(a+b)/2.
    w.append((b-a)*(h(a)+4*h(mid)+h(b))/(6*unit))
central=math.fsum(wi*row[0] for wi,row in zip(w,rows))
errors={
 "stat_down":[abs(row[1]) for row in rows],
 "stat_up":[row[2] for row in rows],
 "sys_down":[abs(row[3]) for row in rows],
 "sys_up":[row[4] for row in rows]
}
info={}
for key,sigma in errors.items():
    a=[wi*si for wi,si in zip(w,sigma)]
    coherent=math.fsum(a)
    independent=math.sqrt(math.fsum(v*v for v in a))
    info[key]={
     "relative_if_independent":independent/central,
     "relative_if_fully_correlated":coherent/central,
     "sharp_min_variance_if_only_PSD_correlation_known":
       max(0.,2*max(a)-coherent)**2,
     "sharp_max_variance_if_only_PSD_correlation_known":coherent**2
    }
low=central-math.fsum(wi*(ds+dt) for wi,ds,dt in
     zip(w,errors["stat_down"],errors["sys_down"]))
high=central+math.fsum(wi*(us+ut) for wi,us,ut in
     zip(w,errors["stat_up"],errors["sys_up"]))
assert 0<low<central<high
assert abs(central/3.8868646699147837e-10-1)<2e-9
assert abs(low/3.3943177950208697e-10-1)<2e-9
assert abs(high/4.3907152771902659e-10-1)<2e-9
print(json.dumps({
 "status":"PASS_RIVET_REAL_TABLE1_STAT_SYS_COVARIANCE_GUARD",
 "source_sha256":sha,"n_source_energies":140,
 "K_fid_central":central,
 "K_box_down":low,"K_box_up":high,
 "component_sensitivity":info,
 "limitations":"5MeV bin mean assumed; asymmetric errors not joint CI; unknown covariance; secondary Rivet reference, not primary HEPData; no full physical pi/QCD or PBH/BBN"
},indent=2,sort_keys=True))
