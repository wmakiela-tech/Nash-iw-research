#!/usr/bin/env python3
"""Independent mpmath 48dps source/YODA parser, analytic z-bin integral
for charge-symmetrized inverse daughter pion energy in HEAD-ON limit.
No code imports from full source fold. Source W/z average assumptions explicit.
"""
from pathlib import Path
import gzip,re,json,hashlib
import mpmath as mp
D=mp.mpf;mp.mp.dps=48
root=Path(__file__).resolve().parent
src=root/'BELLE_2007_I749358.yoda.gz'
hash='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(src.read_bytes()).hexdigest()==hash
# INDEPENDENT extraction numerical rows by anchored columns and actual ID.
t={}
for match in re.finditer(r'(?ms)^BEGIN YODA_BINNEDESTIMATE<S>_V3 /REF/BELLE_2007_I749358/d(\d+)-x01-y01\n(.*?)^END YODA_BINNEDESTIMATE<S>_V3',gzip.decompress(src.read_bytes()).decode()):
    index=int(match.group(1)); lines=match.group(2).splitlines()
    v=[D(line.split()[0]) for line in lines if re.match(r'^\s*[+\-]?\d+\.\d+e[+\-]\d+\s',line) and len(line.split())>=5]
    t[index]=v
assert len(t)==141 and all(len(t[i+2])==12 for i in range(140))
E=D('1436554');T=D('0.07818527068831995');mpi=D('139.57039');C=4*E*T
mGeV=D('.13957039');ctau=D('780.45')
N0=N2=Nfull=Nlo=Nhi=D(0)
wn,ww=mp.gauss_quadrature(8,'legendre')
for i in range(140):
  v=t[i+2]
  assert abs((D('.05')*sum(v))/t[1][i]-1)<D('.00006')
  for node,weight in zip(wn,ww):
    W=D(800)+D(5)*i+D('2.5')*(1+node)
    y=W*W/C; L=-mp.log1p(-mp.exp(-y))
    H=4*W**3*L/C**2
    beta=mp.sqrt(1-4*mpi*mpi/W**2)
    wb=D('2.5')*weight*H
    for j,sig in enumerate(v):
       a=D(j)*D('.05');b=a+D('.05')
       wbin=wb*sig*D('.05')
       inv=(mp.atanh(beta*b)-mp.atanh(beta*a))/(beta*(b-a))
       square=beta**2*(a*a+a*b+b*b)/3
       N0+=wbin
       N2+=wbin*square
       Nfull+=wbin*inv
       Nlo+=wbin/(1-beta**2*a*a)
       Nhi+=wbin/(1-beta**2*b*b)
ratio=Nfull/N0
out={'status':'PASS_SECONDARY_RIVET_WZ_SOURCE_HEADON_ANALYTIC_INV_ENERGY',
'source_sha256':hash,'angular_source_values':1680,
'inverse_energy_Jensen_ratio_headon':mp.nstr(ratio,34),
'leading_variance_only_ratio_1_plus_beta2z2':mp.nstr(1+N2/N0,34),
'nonlinear_tail_beyond_beta2z2':mp.nstr(ratio-1-N2/N0,34),
'angular_support_min_ratio':mp.nstr(Nlo/N0,34),
'angular_support_max_ratio':mp.nstr(Nhi/N0,34),
'bound_pion_mass_shell_correction_max_rel':mp.nstr((mGeV/(E/2000*(1-D('.6'))))**2,10),
'claim_ceiling':'HEADON inverse energy analytical angular integration; mass-shell corrections small separately; source W/z bin averages assumed, not physical QCD full pion transport.'}
(root/'results_rot028_independent.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps(out,sort_keys=True,indent=2))
