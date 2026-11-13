#!/usr/bin/env python3
"""DAX-S8 ROT019 compact reproducibility for SHA-pinned real Belle Rivet angular data.
Needs mpmath>=1.3 and original BELLE_2007_I749358.yoda.gz beside script.
Does NOT imply primary HEPData byte equality, experimentally proven 5MeV
bin-average semantics, full charged-pion QCD rate, decays, or PBH/BBN bound.
Full executed original and independent SciPy/4vector code live in ROT019 ZIP.
"""
from pathlib import Path
import gzip,hashlib,json,re
import mpmath as mp
mp.mp.dps=48
p=Path(__file__).parent/'BELLE_2007_I749358.yoda.gz'
source=p.read_bytes()
sha='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(source).hexdigest()==sha
body=gzip.decompress(source).decode('utf8')
tables={}
for typ,path,block in re.findall(r'(?ms)^BEGIN (YODA_[^ ]+) ([^\n]+)\n(.*?)^END YODA_[^\n]*',body):
    assert typ=='YODA_BINNEDESTIMATE<S>_V3'
    id=int(re.search(r'/d(\d+)-',path).group(1))
    coords=[mp.mpf(q) for q in json.loads(re.search(r'(?m)^Edges\(A1\): (\[.*\])$',block).group(1))]
    vals=[]
    for line in block.splitlines():
        if re.match(r'^\s*[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?\s',line):
            vals.append(mp.mpf(line.split()[0]))
    assert len(vals)==len(coords)
    tables[id]=(coords,vals)
assert len(tables)==141
E=mp.mpf('1436554');T=mp.mpf('0.07818527068831995')
mpi=mp.mpf('139.57039');C=4*E*T
zwidth=mp.mpf('.05')
nodes,weights=mp.gauss_quadrature(14,'legendre')
den=mid=uniform=low=high=iso=mp.mpf('0')
for i in range(140):
    z,ds= tables[i+2]
    assert len(z)==12
    assert all(abs(zk-(mp.mpf('.025')+j*zwidth))<mp.mpf('1e-43') for j,zk in enumerate(z))
    sig=zwidth*sum(ds)
    original=tables[1][1][i]
    assert abs(sig/original-1)<mp.mpf('6e-5')
    Z=lambda fn: sum(v*fn(zk) for v,zk in zip(ds,z))*zwidth/sig
    z2mid=Z(lambda zk:zk**2)
    z2uniform=z2mid+zwidth*zwidth/12
    z2lo=Z(lambda zk:(zk-zwidth/2)**2)
    z2hi=Z(lambda zk:(zk+zwidth/2)**2)
    w0=wb=ws=mp.mpf('0')
    for t,g in zip(nodes,weights):
        W=mp.mpf('802.5')+5*i+mp.mpf('2.5')*t
        y=W*W/C
        q=mp.exp(-y);I0=-mp.log1p(-q)
        Li2=mp.polylog(2,q);Li3=mp.polylog(3,q)
        mx=y+Li2/I0
        mx2=y*y+2*y*Li2/I0+2*Li3/I0
        A=1-2*(T/E)*mx+(T/E)**2*mx2
        B=2*(T/E)*(mx-y)
        beta2=1-4*mpi*mpi/W**2
        H=4*W**3/C**2*I0
        ww=mp.mpf('2.5')*g*H
        w0+=ww
        wb+=ww*beta2*B
        ws+=ww*beta2*(A-B)
    den+=w0*sig
    mid+=sig*(wb+ws*z2mid)
    uniform+=sig*(wb+ws*z2uniform)
    low+=sig*(wb+ws*z2lo)
    high+=sig*(wb+ws*z2hi)
    iso+=sig*(wb+ws*mp.mpf('.12'))
ratio=lambda x:mp.sqrt(x/den)
assert abs(ratio(uniform)-mp.mpf('0.32178080925857764'))<mp.mpf('1e-15')
print(json.dumps({
    'status':'PASS_REAL_RIVET_FIDUCIAL_PION_LAB_ENERGY_SPLIT',
    'YODA_sha256':sha,'angles':140*12,
    'M2_uniform':mp.nstr(uniform/den,29),
    'RMS_uniform':mp.nstr(ratio(uniform),29),
    'RMS_midpoint':mp.nstr(ratio(mid),29),
    'RMS_lower_angular_bin_support':mp.nstr(ratio(low),29),
    'RMS_upper_angular_bin_support':mp.nstr(ratio(high),29),
    'RMS_isotropic_z_comparator':mp.nstr(ratio(iso),29),
    'limits':'Only source-Rivet numerical angular data, fiducial 5MeV and 0.05 bin-average model; NOT a full QCD/pi/neutrino/cosmology result'
},indent=2,sort_keys=True))
