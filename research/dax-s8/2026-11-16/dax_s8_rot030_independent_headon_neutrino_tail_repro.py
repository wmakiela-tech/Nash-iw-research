#!/usr/bin/env python3
"""Independent head-on real Belle/Rivet source & original ROT027 FD hard-Q2 kernel.
Draws only angular/W bins analytically headon; no ROT029 source geometry imports.
Pion -> mu nu two-body energy moments; restricted author model only, no full cosmic flux.
"""
import json,hashlib,gzip,math,re
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import cumulative_trapezoid,simpson
from scipy.optimize import brentq
from inherited_rot027_kernel import Kernel, M, ctau_cm
root=Path(__file__).resolve().parent
sha='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
src=root/'BELLE_2007_I749358.yoda.gz'
assert hashlib.sha256(src.read_bytes()).hexdigest()==sha
source=gzip.decompress(src.read_bytes()).decode('utf8')
tabs={}
for mat in re.finditer(r'(?ms)^BEGIN YODA_BINNEDESTIMATE<S>_V3 /REF/BELLE_2007_I749358/d(\d+)-x01-y01\n(.*?)^END YODA_BINNEDESTIMATE<S>_V3',source):
    i=int(mat.group(1));vals=[]
    for ln in mat.group(2).splitlines():
        a=ln.split()
        if len(a)>=5 and re.match(r'^[-+]?\d+\.\d+e[-+]\d+$',a[0]): vals.append(float(a[0]))
    tabs[i]=np.asarray(vals)
assert len(tabs)==141
nw,ww=roots_legendre(8);nz,wz=roots_legendre(8)
Eg=1436554.;T=.07818527068831995;mpi=139.57039;C=4*Eg*T
E0s=[];ws=[]
for i in range(140):
 vals=tabs[i+2]
 assert len(vals)==12 and abs(.05*vals.sum()/tabs[1][i]-1)<6e-5
 for n,wN in zip(nw,ww):
  W=800+5*i+2.5*(1+n);y=W*W/C
  H=4*W**3/C**2*(-math.log1p(-math.exp(-y)))
  beta=math.sqrt(1-4*mpi**2/W**2)
  for j,cs in enumerate(vals):
   zz=(j+.5)*.05+.025*nz
   pion_E=np.r_[(Eg/2000)*(1+beta*zz),(Eg/2000)*(1-beta*zz)]
   wbase=2.5*wN*H*.025*cs
   E0s.extend(pion_E.tolist())
   ws.extend(np.tile(wbase*wz/2,2).tolist())
sE=np.asarray(E0s);w=np.asarray(ws);w=w/w.sum()
assert abs(np.dot(sE,w)-718.277)<1e-9
order=np.argsort(sE);sE=sE[order];w=w[order]
model=Kernel(nq=48,nmu=36)
Es=np.geomspace(1.2,1250,7501)
bs=np.array([model.evaluate(float(e))[1] for e in Es]);assert np.all(bs>0)
g=(M/(ctau_cm*np.sqrt(Es**2-M*M)))/bs
H=cumulative_trapezoid(g,Es,initial=0.)
href=float(np.interp(718.277,Es,H))
Hw=np.interp(sE,Es,H)
tail=np.r_[np.cumsum((w*np.exp(-(Hw-href)))[::-1])[::-1],0]
pre=np.r_[0,np.cumsum(w)]
ind=np.searchsorted(sE,Es,side='left')
CDF=pre[ind]+np.exp(np.clip(H-href,-700,50))*tail[ind]
dens=g*np.exp(np.clip(H-href,-700,50))*tail[ind]
pi_mean=Es[0]+simpson(1-CDF,x=Es)
pi2=Es[0]**2+simpson(2*Es*(1-CDF),x=Es)
mmu=.1056583755;f=(M*M-mmu*mmu)/(2*M*M)
nu_m=f*pi_mean;nu2=f*f*(4*pi2-M*M)/3
p=np.sqrt(Es*Es-M*M)
def tail_neu(t):
    pr=np.clip((f*(Es+p)-t)/(2*f*p),0,1)
    return float(simpson(pr*dens,x=Es))
answer={'status':'PASS_INDEPENDENT_HEADON_SOURCE_AND_ORIGINAL_ROT027_KERNEL_NEUTRINO_TRANSFER',
 'source_sha256':sha,'W_bins':140,'z_bins':12,'source_kinematic_energy_nodes':len(sE),
 'headon_source_initial_E_GeV':float(np.dot(sE,w)),
 'pion_at_decay_mean_GeV':float(pi_mean), 'pion_at_decay_second_GeV2':float(pi2),
 'one_first_neutrino_mean_GeV':float(nu_m),'one_first_neutrino_second_GeV2':float(nu2),
 'one_first_neutrino_sd_GeV':float(np.sqrt(nu2-nu_m**2)),
 'P_nu_above_1GeV':tail_neu(1),'P_nu_above_10GeV':tail_neu(10),'P_nu_above_100GeV':tail_neu(100),
 'nu_median_GeV':brentq(lambda e:tail_neu(e)-.5,.001,3.),
 'claim_ceiling':'Real secondary Rivet source WITH 5MeV/0.05 source-bin-mean ASSUMPTION, exact headon idealization, artificial hard Q² .001–.010 pion/e vacuum Born CSDA. Not full early universe physical neutrino spectrum.'}
(root/'results_rot030_independent_headon.json').write_text(json.dumps(answer,sort_keys=True,indent=2)+'\n')
print(json.dumps(answer,sort_keys=True,indent=2))
