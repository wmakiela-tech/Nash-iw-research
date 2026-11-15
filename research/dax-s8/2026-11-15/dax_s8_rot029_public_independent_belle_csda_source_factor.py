#!/usr/bin/env python3
"""DAX-S8 ROT029 independent source-typed HEADON source fold under restricted CSDA.
Requires source bundle files:
  BELLE_2007_I749358.yoda.gz (original SHA pinned Rivet-data source)
  inherited_rot027_kernel.py (original author executed finite hard-Q2 pion/e FD)
plus numpy/scipy. All in verified 20-member ROT029 ZIP.
This is NOT full in-medium pion stopping, source-wide discrete pion MC,
a final neutrino spectrum or a physical PBH/BBN constraint.
"""
from pathlib import Path
import sys,re,gzip,json,hashlib,math
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq
root=Path(__file__).resolve().parent
original=root/'BELLE_2007_I749358.yoda.gz'
sha='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(original.read_bytes()).hexdigest()==sha
sys.path.insert(0,str(root))
from inherited_rot027_kernel import Kernel,M,ctau_cm
raw=gzip.decompress(original.read_bytes()).decode()
tables={}
for match in re.finditer(r'(?ms)^BEGIN YODA_BINNEDESTIMATE<S>_V3 /REF/BELLE_2007_I749358/d(\d+)-x01-y01\n(.*?)^END YODA_BINNEDESTIMATE<S>_V3',raw):
    n=int(match.group(1)); values=[]
    for line in match.group(2).splitlines():
        x=line.split()
        if len(x)>=5 and re.match(r'^[-+]?\d+\.\d+e[-+]\d+$',x[0]):
            values.append(float(x[0]))
    tables[n]=np.asarray(values)
assert len(tables)==141 and all(len(tables[n+2])==12 for n in range(140))
Egrid=np.geomspace(1.2,1250,5501)
kernel=Kernel(nq=48,nmu=36)
loss=np.asarray([kernel.evaluate(float(E))[1] for E in Egrid])
g=M/(ctau_cm*np.sqrt(Egrid**2-M**2))/loss
H=cumulative_trapezoid(g,Egrid,initial=0.)
E_mean=718.2771443978552
Hmean=np.interp(E_mean,Egrid,H)
wn,ww=roots_legendre(8)
zn,wz=roots_legendre(8)
Egamma=1436554.0; T=0.07818527068831995; C=4*Egamma*T
mpi=139.57039
den=0.; num=0.
for i in range(140):
    vals=tables[i+2]
    assert abs(.05*vals.sum()/tables[1][i]-1)<6e-5
    for xw,fw in zip(wn,ww):
        W=800+5*i+2.5*(1+xw)
        y=W*W/C
        HW=4*W**3/C**2*(-math.log1p(-math.exp(-y)))
        bp=math.sqrt(1-4*mpi*mpi/W**2)
        for j,sig in enumerate(vals):
            z=(j+.5)*.05+.025*zn
            pairs=np.r_[Egamma/2000*(1+bp*z),Egamma/2000*(1-bp*z)]
            wzpair=np.r_[wz,wz]*(2.5*fw*HW*sig*.025/2)
            den+=float(wzpair.sum())
            num+=float(np.dot(wzpair,np.exp(-(np.interp(pairs,Egrid,H)-Hmean))))
Csource=num/den
def S(E,source=True):
    single=math.exp(-(Hmean-np.interp(E,Egrid,H)))
    return single*Csource if source else single
def median(source=True):
    return brentq(lambda E:S(E,source)-.5,1.2,20)
result={
    'status':'PASS_SECONDARY_BELLE_SOURCE_HEADON_CSDA_SEMIGROUP_FACTOR',
    'source_sha256':sha,
    'source_energy_entries':140,
    'source_angular_entries':140*12,
    'S_source_over_S_mean_constant_below_input_energy_support':Csource,
    'median_E_decay_source_GeV':median(True),
    'median_E_decay_single_mean_GeV':median(False),
    'delta_median_keV':(median(False)-median(True))*1e6,
    'survival_to_100GeV_source':S(100,True),
    'survival_to_100GeV_mean':S(100,False),
    'limits':'Headon source and bin average assumptions, hard Q2 vacuum Born pi-e only; not source-wide stochastic transport or physical neutrino production.'
}
print(json.dumps(result,sort_keys=True,indent=2))
