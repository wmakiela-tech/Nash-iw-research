#!/usr/bin/env python3
"""Source-free exact-integer Fourier support census for ROT017; no NumPy required."""
from fractions import Fraction

for N in (4,6,8,10,12,16,20,24,32,40):
    signed=range(-N//2,N//2)
    bad=0
    max_c=Fraction(0)
    argmax=None
    for x in signed:
        for y in signed:
            for z in signed:
                p=(x,y,z)
                ny=sum(t==-N//2 for t in p)
                b=sum(t*t for t in p if t!=-N//2)
                if not ny or not b: continue
                bad+=1
                a=ny*(N//2)**2
                c=Fraction(abs(a-b),a+b)
                if c>max_c:
                    max_c,argmax=c,p
    assert bad==3*N*N-3*N-6
    assert max_c==Fraction(N*N-2,N*N+2)
    cost=(3+max_c**2)/4
    assert cost==1-Fraction(2*N*N,(N*N+2)**2)
    dim_B=2*N**3-6*N*N+6*N+15
    dim_A=2*N**3+6*N*N-6*N-9
    assert dim_A-dim_B==4*bad
    print(f'N={N:2} bad={bad:5} rank_B={dim_B:6} rank_A={dim_A:6} '
          f'cost={float(cost):.12f} witness={argmax}')
print('ROT017 exact rational frequency count and cost: PASS')
