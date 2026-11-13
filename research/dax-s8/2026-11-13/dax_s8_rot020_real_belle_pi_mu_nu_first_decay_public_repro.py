#!/usr/bin/env python3
"""DAX-S8 ROT020 compact true-source Belle/Rivet 140x12 pion->mu nu first step.
Requires mpmath>=1.3.0; original SHA-pinned YODA gz beside script. Pure
2-body in-vacuum pion decays before scattering, 5MeV/0.05 bin mean assumed.
No primary HEPData byte equality, pion interaction survival, muon decay,
physical neutrino escape, complete hadronic QCD or PBH/BBN inference.
"""
from pathlib import Path
import hashlib,gzip,json,re
import mpmath as mp
mp.mp.dps=48
D=mp.mpf
path=Path(__file__).parent/'BELLE_2007_I749358.yoda.gz'
src=path.read_bytes()
SHA='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(src).hexdigest()==SHA
blocks={}
for typ,path,body in re.findall(r'(?ms)^BEGIN (YODA_[^ ]+) ([^\n]+)\n(.*?)^END YODA_[^\n]*',gzip.decompress(src).decode()):
    assert typ=='YODA_BINNEDESTIMATE<S>_V3'
    i=int(re.search(r'/d(\d+)-',path).group(1))
    z=[D(s) for s in json.loads(re.search(r'(?m)^Edges\(A1\): (\[.*\])$',body).group(1))]
    y=[D(s.split()[0]) for s in body.splitlines() if re.match(r'^\s*[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?\s',s)]
    assert len(z)==len(y)
    blocks[i]=(z,y)
assert set(blocks)==set(range(1,142))
E=D('1436554');T=D('0.07818527068831995')
mpi=D('139.57039');mmu=D('105.6583755');C=4*E*T
f=(mpi*mpi-mmu*mmu)/(2*mpi*mpi)
node,wt=mp.gauss_quadrature(12,'legendre')
den=qm=q2m=d2m=D('0')
for i in range(140):
    z,ds=blocks[i+2]
    assert len(z)==12
    sig=D('.05')*sum(ds)
    assert abs(sig/blocks[1][1][i]-1)<D('.00006')
    z2=(D('.05')*sum(ds[j]*z[j]**2 for j in range(12))/sig)+D('.05')**2/12
    for t,w in zip(node,wt):
        W=D(800+5*i)+D('2.5')*(1+t)
        y=W*W/C;q=mp.exp(-y);I0=-mp.log1p(-q)
        l2=mp.polylog(2,q);l3=mp.polylog(3,q)
        mx=y+l2/I0;mx2=y*y+2*y*l2/I0+2*l3/I0
        H=4*W**3/C**2*I0
        a=1-2*T/E*mx+(T/E)**2*mx2
        b=2*T/E*(mx-y)
        beta2=1-4*mpi*mpi/W**2
        wg=D('2.5')*w*H*sig
        den+=wg
        qm+=wg*(E+T*mx)
        q2m+=wg*(E*E+2*E*T*mx+T*T*mx2)
        d2m+=wg*E*E*beta2*(b+(a-b)*z2)
Q=qm/den;Q2=q2m/den;D2=d2m/den
mu=f*Q/2
nu2=f*f*(Q2+D2-mpi*mpi)/3
sd=mp.sqrt(nu2-mu*mu)
nu2_equal=f*f*(Q2-mpi*mpi)/3
assert abs(D2/E**2-D('0.103542889207105125579'))<D('1e-19')
assert abs(mu/1000-D('153.320585392397992'))<D('1e-12')
print(json.dumps({
 'status':'PASS_REAL_BELLE_RIVET_TO_PION_DECAY_FIRST_NEUTRINO_MOMENTS',
 'source_SHA256':SHA,'R68_fiducial_W_bins':140,'z_bins':12,
 'pion_to_mu_nu_f':mp.nstr(f,28),
 'one_first_neutrino_mean_GeV':mp.nstr(mu/1000,27),
 'one_first_neutrino_E2_GeV2':mp.nstr(nu2/1e6,27),
 'one_first_neutrino_sd_GeV':mp.nstr(sd/1000,27),
 'two_first_neutrinos_sum_mean_GeV':mp.nstr(f*Q/1000,27),
 'neutrino_E2_vs_equal_pion_energy_ratio':mp.nstr(nu2/nu2_equal,27),
 'limits':'Conditional free vacuum two-body pion decays, secondary Rivet source and bin semantics only; no physical pion survival, muon decay, neutrino transport or PBH bound.'
},indent=2,sort_keys=True))
