#!/usr/bin/env python3
"""ROT006 exact rational finite-vertex verification; source-native 3Q A/B.

Quantitative bound for protocols in which Alice measures ONCE, then B and C
may jointly measure, with arbitrary rank-one/rank-two initial Alice POVM.
This is NOT a bound for unrestricted LOCC, for protocols where Alice measures again,
or for protocols with pre-shared entanglement.
"""
import sympy as sp
from itertools import product

I=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]])

def tensor(A,B): return sp.kronecker_product(A,B)
XI=tensor(X,I); IX=tensor(I,X); YI=tensor(Y,I); IY=tensor(I,Y)
XX=tensor(X,X); YY=tensor(Y,Y); XY=tensor(X,Y); YX=tensor(Y,X)

def normalized_BC(x,nx,ny):
    # C(n)/b = Tr_A[(|n><n| tensor I_4) (D/b)]
    return (XX+YY+nx*(XI+IX)+ny*(YI+IY))/16 + x*(nx*(3*XX+YY)+ny*(XY+YX))/32


def exact_trace_norm_upper(A,eps=sp.Rational(1,10000000)):
    z=sp.Symbol('z')
    cp=sp.Poly(A.charpoly(z).as_expr(),z,domain=sp.QQ)
    intervals=sp.polys.polytools.intervals(cp,eps=eps)
    assert sum(mult for (_,mult) in intervals)==4, 'missing charpoly roots'
    upper=sum(max(abs(a),abs(b))*mult for ((a,b),mult) in intervals)
    return upper, [(tuple(map(str,rg)),m) for rg,m in intervals],cp


def main():
    endpoint_x=[sp.Rational(7,10),sp.Rational(3,4)]
    V=sp.Rational(11,100); M=sp.Rational(12,25)
    # Circle r_x^2+r_y^2 <=1 is in octagon, since sqrt(2) <= 17/12.
    assert sp.Rational(17,12)**2>=2
    vertices=[(sx*sp.Rational(1),sy*sp.Rational(5,12)) for sx,sy in product((1,-1),repeat=2)]
    vertices += [(sx*sp.Rational(5,12),sy*sp.Rational(1)) for sx,sy in product((1,-1),repeat=2)]
    record=[]
    for x in endpoint_x:
        for (nx,ny) in vertices:
            A=normalized_BC(x,nx,ny)
            assert A==A.conjugate().T, 'not Hermitian'
            ub,ints,cp=exact_trace_norm_upper(A)
            left=ub-V*nx
            assert left<M, (x,nx,ny,ub,left,M)
            record.append((x,nx,ny,ub,left))
            print('vertex', 'x=',x,'nx=',nx,'ny=',ny,'normU=',float(ub),'affineU=',float(left),'margin=',float(M-left))
    max_upper=max(t[-1] for t in record)
    print('EXACT_RATIONAL_ALL_16_CERTIFIED: PASS')
    print('maximum_certificate=',max_upper, 'float=',float(max_upper))
    for x in endpoint_x:
        b=1-x*x
        print('x=',x,'global_helstrom=',sp.Rational(1,2)*b,'one_round_bound=',M*b,
              'restricted_LOCC_lower_gap=',(sp.Rational(1,2)-M)*b)

    # Independent scalar matrix fixture: D_{u,v}(q)=1/8(x^|sumΔ| - x^sum|Δ|)
    x=sp.Rational(3,4)
    words=list(product((0,1),repeat=3))
    D=sp.Matrix(8,8,lambda i,j:(x**abs(sum(words[i][k]-words[j][k] for k in range(3)))
                                   -x**sum(abs(words[i][k]-words[j][k]) for k in range(3)))/8)
    def paul(word):
        R=sp.eye(1)
        for ch in word:
            R=tensor(R, {'I':I,'X':X,'Y':Y}[ch])
        return R
    b=1-x*x;a=x*b
    D2=b*sum((paul(ch) for ch in ('XXI','XIX','IXX','YYI','YIY','IYY')),sp.zeros(8))/16
    D2+=a*(3*paul('XXX')+paul('XYY')+paul('YXY')+paul('YYX'))/32
    assert D==D2
    assert D.trace()==0
    assert sum(abs(z)*m for z,m in D.eigenvals().items())==b # Helstrom TV=b/2
    print('INDEPENDENT_8X8_SOURCE_D_AND_PAULI_EXPANSION: PASS')

if __name__=='__main__':main()
