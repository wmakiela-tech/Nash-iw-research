#!/usr/bin/env python3
"""Source-typed rate-cap visibility checks for NASH, 2026-10-26.
Reproduces finite-n singleton-overlap E1 and count-only E3, not quantum 2^4096 POVM.
Requires numpy and scipy; no external data or network.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import gammaln

def grid(n,c,kind):
    if kind=="uniform": return np.full(n,1./n)
    m=math.ceil(math.sqrt(n)); d=np.full(n,c/n)
    if kind=="early_boost": d[:m]+=(1-c)/m
    elif kind=="late_boost": d[-m:]+=(1-c)/m
    else: raise ValueError(kind)
    assert abs(d.sum()-1)<1e-12 and np.min(d)>=c/n-1e-14
    return d

def fixture(n,c,kind,a=1.,beta=2.):
    d=grid(n,c,kind)
    u=np.maximum(0.,1.-np.cumsum(d))
    b=-np.expm1(-beta*u/n)/2
    s=-np.expm1(-a*d)/2
    q=b+s-2*b*s
    p0=float(np.prod(1-s)); B0=float(np.prod(1-b))
    delta=float(B0*np.minimum((1-p0)*b/(1-b),p0*s/(1-s)).sum())
    return dict(n=n,c=c,kind=kind,E=float((d*d).sum()),m=float(u.mean()),
                p0=p0,B0=B0,delta=delta,b=b,s=s,q=q)

def full_tv(f):
    n=f["n"]; b=f["b"]; q=f["q"]
    assert n<=18
    words=np.arange(1<<n,dtype=np.uint64)
    lp=np.zeros(len(words)); lq=np.zeros(len(words))
    for j in range(n):
        bit=((words>>np.uint64(j))&1).astype(bool)
        lp+=np.where(bit,np.log(np.maximum(b[j],1e-300)),np.log1p(-b[j]))
        lq+=np.where(bit,np.log(np.maximum(q[j],1e-300)),np.log1p(-q[j]))
    return float(np.abs(np.exp(lp)-np.exp(lq)).sum()/2)

def click_pmf(probs,kmax=35):
    v=np.zeros(kmax+1);v[0]=1.
    for p in probs:
        v[1:]=v[1:]*(1-p)+v[:-1]*p
        v[0]*=(1-p)
    assert v.sum()>1-5e-10
    return v

def count_tv(f):
    p=click_pmf(f["b"]);q=click_pmf(f["q"])
    return float((np.abs(p-q).sum()+abs(p.sum()-q.sum()))/2)

def poisson_tv(lam1,lam2):
    k=np.arange(101,dtype=float)
    def law(x):
        if x==0:
            y=np.zeros_like(k);y[0]=1;return y
        return np.exp(-x+k*np.log(x)-gammaln(k+1))
    return float(np.abs(law(lam1)-law(lam2)).sum()/2)

def main():
    rows=[]
    for n in (8,12,16,64,256,1024,4096):
      for c in (.25,.5,.8,1.):
       for kind in ("uniform","early_boost","late_boost"):
        f=fixture(n,c,kind)
        tv=full_tv(f) if n<=16 else None
        if tv is not None:
            assert tv<=1-f["p0"]-f["delta"]+2e-13, (n,c,kind)
        if kind=="early_boost": assert f["m"]>=c*(n-1)/(2*n)-1e-11
        rows.append(dict(n=n,c=c,kind=kind,mesh_energy=f["E"],mean_age=f["m"],
             E1_overlap_delta=f["delta"], full_label_reference_tv=tv,
             count_tv=count_tv(f) if n>=64 else None,
             Poisson_at_mean_age_tv=poisson_tv(f["m"],f["m"]+.5)))
    assert len(rows)==84
    envelope=[]
    a,beta=1.,2.;p=math.exp(-a/2)
    for c in (.25,.5,.8,1.):
        envelope.append(dict(c=c,count_only_sharp=poisson_tv(beta*c/4,beta*c/4+a/2),
          quantum_strict_gap_lower=math.exp(-beta/2)*(beta*c/4)*min(1-p,p*a*c/beta)))
    out=dict(metadata="NO_NOVELTY / NO_CANON / NO_EXEC / REFEREE_PENDING",
             source="PRF11 R35; local previous G1/G2; new E1-E3",
             tests="PASS: 84 grids; 36 finite full-labelled reference TV comparisons",
             envelope=envelope,rows=rows)
    target=Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out,indent=2)+"\n")
    print(out["tests"]);print("saved",target)
    for e in envelope:print(e)

if __name__=="__main__":main()
