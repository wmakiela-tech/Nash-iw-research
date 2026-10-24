"""LT5-NASH Stage1: arithmetic-only reference check, NOT a blinded trial."""
from math import isfinite
state=0x4D595DF4

def rand():
    global state
    state^=(state << 13)&0xFFFFFFFF
    state^=state >> 17
    state^=(state << 5)&0xFFFFFFFF
    state&=0xFFFFFFFF
    return state/2**32

def values(ell,h,B0,B1,s,delta):
    assert h>=ell and B0>=0 and B1>=0 and s>0 and delta>=0
    w=(h-ell)/2
    c=(h+ell)/2
    e=min(w,delta/s)
    two=max(e,w+max(abs(c)-B0,0)-B1)
    late=max(e,w+abs(c)-B0-B1)
    premium=min(max(B0-abs(c),0),max(w-B1-e,0))
    return two,late,premium

max_error=0.
positive=0
for k in range(100_000):
    ell=-5+10*rand()
    h=ell+10*rand()
    B0=8*rand()
    B1=8*rand()
    s=.05+5*rand()
    delta=4*rand()
    two,late,premium=values(ell,h,B0,B1,s,delta)
    err=abs((two-late)-premium)
    assert isfinite(err) and err < 4e-15
    max_error=max(err,max_error)
    positive+=premium>1e-9

for case in ((-1,1,1,0,1,0),(-.8,1.2,.7,.4,1,.05),(0,0,0,0,1,0),
             (0,0,2,0,1,4),(-1,1,10,0,.1,100),(-1,1,1,1,1,0)):
    two,late,premium=values(*case)
    assert abs(two-late-premium)<1e-12
assert positive==10333,positive
print(f'PASS n=100000 positive_premium={positive} max_abs_err={max_error:.3e}; six boundary cases PASS')
