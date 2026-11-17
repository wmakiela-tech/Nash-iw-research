#!/usr/bin/env python3
"""PRF14 ROT005: exact rational indistinguishability of Pauli memory and unknown gate.
This is a model-specific finite certificate, NOT hardware or novel GST theory.
"""
from fractions import Fraction as Q
from itertools import product

G = list(product([0,1], repeat=2))
A = ('X','Y','Z')
def chi(a,v):
    x,z=v
    return {'X':(-1)**z, 'Y':(-1)**(x+z), 'Z':(-1)**x}[a]
Rstar=[[Q(-1,3),Q(2,3),Q(2,3)],
       [Q(2,3),Q(-1,3),Q(2,3)],
       [Q(2,3),Q(2,3),Q(-1,3)]]
Rold=[[Q(-3,7),Q(-2,7),Q(6,7)],
      [Q(6,7),Q(-3,7),Q(2,7)],
      [Q(2,7),Q(6,7),Q(3,7)]]
def dot(v,w):return sum(x*y for x,y in zip(v,w))
def transpose(M):return list(map(list, zip(*M)))
def determinant(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
for R in (Rstar,Rold):
    assert determinant(R)==1
    assert all(dot(R[i],R[j])==(i==j) for i in range(3) for j in range(3))

def coeff(R):
    return {(j,i):(Q(0) if i==j else Q(1,30)/R[i][j])
            for j in range(3) for i in range(3)}
cstar,cold=coeff(Rstar),coeff(Rold)
assert set(cstar.values()) == {Q(0),Q(1,20)}
assert {v for v in cold.values() if v} == {Q(-7,60),Q(7,60),Q(7,180)}

def law(c):
    return {(v,w):Q(1,16)*(1+sum(c[j,i]*chi(A[j],v)*chi(A[i],w)
               for j in range(3) for i in range(3) if j!=i))
            for v in G for w in G}
ps,po=law(cstar),law(cold)
assert sum(ps.values())==sum(po.values())==1
assert min(ps.values())>0 and min(po.values())>0
assert ps != po
assert all(sum(p[v,w] for w in G)==Q(1,4)
           for p in (ps,po) for v in G)
assert all(sum(p[v,w] for v in G)==Q(1,4)
           for p in (ps,po) for w in G)
# C_ab: all first-stage, second-stage and idle endpoint Pauli coefficients
# are independent uniform for both models; only 6 off-diagonals survive.
def fourier(p,j,i):
    return sum(p[v,w] * chi(A[j],v)*chi(A[i],w) for v in G for w in G)
for i in range(3):
    assert fourier(ps,i,i)==fourier(po,i,i)==0
for j in range(3):
    for i in range(3):
        assert fourier(ps,j,i)==cstar[j,i]
        assert fourier(po,j,i)==cold[j,i]
        # Equality of full single-slot interposed effective qubit channel
        target=Q(0) if i==j else Q(1,30)
        assert Rstar[i][j]*fourier(ps,j,i)==Rold[i][j]*fourier(po,j,i)==target
TV=sum(abs(ps[z]-po[z]) for z in ps)/2
assert TV>0
# A second, independently KNOWN common gate W=V_star breaks the alias.
# Source-vs-source Bloch coordinate (input Y, output X): delta T = 1/9.
second_gate_delta = Rstar[0][1]*(cstar[1,0]-cold[1,0])
assert second_gate_delta==Q(1,9)
second_gate_binary_tv=abs(second_gate_delta)/2
assert second_gate_binary_tv==Q(1,18)
print('Independently known second gate, (input Y, output X) binary TV:',second_gate_binary_tv)
print('Exact rational source law positivity:',min(ps.values()),min(po.values()))
print('All 10 ordinary Fourier coordinates identical: YES')
print('All 9 interposed qubit Bloch transfer entries equal: diag 0, offdiag 1/30')
print('Different Pauli source laws, TV(p_star,p_old)=',TV, float(TV))
print('Different real physical unitary rotations Rstar != Rold:',Rstar!=Rold)
print('PASS: nonzero six-coordinate legal source vs unknown gate alias')
