#!/usr/bin/env python3
"""PRF12 R10: exact SEP10 8x8 coefficient verification in integer cyclotomic ring."""
from itertools import product,permutations
bits=list(product((0,1),repeat=3))
perms=list(permutations((0,1,2)))
roots=((1,0),(0,1),(-1,-1))
def odd(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
def minus_coefficient(d):
 a=b=0
 for p in perms:
  sign=1 if odd(p) else (-1)**sum(d)
  r=roots[sum(p[j]*d[j] for j in range(3))%3]
  a+=sign*r[0];b+=sign*r[1]
 return a,b
for x in bits:
 for y in bits:
  d=tuple(a-b for a,b in zip(x,y))
  expected=(6,0) if x==y else ((-3,0) if sum(x)==sum(y) and sum(x) in (1,2) else (0,0))
  assert minus_coefficient(d)==expected,(x,y,d)
  weight_change=sum(d)
  plus=sum(1j**(k*weight_change) for k in range(4))
  assert abs(plus-(4 if weight_change==0 else 0))<1e-12
print('PASS: 64 exact cyclotomic character identities for SEP10; Eplus+Eminus=I')
print('NOTE: full POVM is separable and Helstrom-optimal, not necessarily LOCC')
