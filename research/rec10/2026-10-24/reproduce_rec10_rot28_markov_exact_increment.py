#!/usr/bin/env python3
"""REC10 ROT28: exact rational TV increments and first-passage sample thresholds."""
from math import comb
from fractions import Fraction
def threshold(n):
    if not n: return 1
    return next(k for k in range(n+1) if 3**n*2**k > 4**n)
def TV(n):
    if n==0: return Fraction(0)
    return Fraction(sum(comb(n,k)*(3**n-2**(2*n-k))
             for k in range(threshold(n),n+1)),6**n)
prev=Fraction(0)
for n in range(1,1001):
    t0=threshold(n-1);t1=threshold(n)
    assert t1 in (t0,t0+1)
    if t1==t0:
        delta=comb(n-1,t0-1)*(Fraction(1,2**n)
                       -Fraction(2**(n-t0),3**n))
    else:
        delta=comb(n-1,t0)*(Fraction(2**(n-t0),3**n)
                       -Fraction(1,2**n))
    v=TV(n)
    assert delta>0 and v-prev==delta,(n,v,prev,delta)
    prev=v
targets=[(1,2),(3,4),(9,10),(19,20),(99,100),
         (999,1000),(9999,10000)]
expected=[16,46,93,133,230,374,522]
for (p,q),want in zip(targets,expected):
    m=next(n for n in range(1,1001) if TV(n)>=Fraction(p,q))
    assert m==want and TV(m-1)<Fraction(p,q)<=TV(m)
    print(f"TV>={p}/{q}, min n={m}, TV={float(TV(m)):.15f}")
print("PASS ROT28 integer-exact 1000 recurrence, strict monotonicity, all 7 thresholds")
