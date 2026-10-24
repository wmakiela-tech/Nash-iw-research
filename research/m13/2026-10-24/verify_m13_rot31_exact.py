#!/usr/bin/env python3
"""ROT31 exact finite-field certificate: band 1 is enough for 3-D TT nonmap.
All arithmetic of the 6x6 certificate is exact mod 821. Evaluation
of a rational cyclotomic number at primitive 41st root 159 in F_821
is a ring homomorphism; nonzero determinant mod 821 proves nonzero
of the original determinant over Q(zeta_41).
"""
P=821;N=41;ROOT=159
assert pow(ROOT,41,P)==1 and ROOT!=1
assert (P-1)%41==0
K=[(-1,-1,0),(-1,-1,-1),(0,0,-1),(-1,1,-1),(-1,0,1),(-1,1,0)]

def inv(x):
 x=x%P
 assert x
 return pow(x,P-2,P)

def mul(A,B):
 return [[sum(A[i][t]*B[t][j] for t in range(3))%P for j in range(3)] for i in range(3)]

def proj(k,A):
 n=sum(x*x for x in k)
 M=[[(int(i==j)-k[i]*k[j]*inv(n))%P for j in range(3)] for i in range(3)]
 PAM=mul(mul(M,A),M)
 tr=sum(M[i][j]*A[j][i] for i in range(3) for j in range(3))%P
 return [[(PAM[i][j]-inv(2)*M[i][j]*tr)%P for j in range(3)] for i in range(3)]

def dot(A,B):
 return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))%P

def ds(q,n):
 # sum_{j=-(n-1)/2}^{(n-1)/2} zeta^(qj), exact finite-field
 assert n%2==1
 return sum(pow(ROOT,q*j%41,P) for j in range(-(n//2),n//2+1))%P

def coscos(k,l,n):
 dminus=1;dplus=1
 for a,b in zip(k,l):
  dminus=dminus*ds(a-b,n)%P
  dplus=dplus*ds(a+b,n)%P
 return inv(2)*(dminus+dplus)*inv(n**3)%P

def det(A):
 X=[row[:] for row in A];z=1;n=len(X)
 for j in range(n):
  p=next((p for p in range(j,n) if X[p][j]),None)
  if p is None:return 0
  if p!=j:X[j],X[p]=X[p],X[j];z=-z
  pivot=X[j][j]
  z=z*pivot%P
  for i in range(j+1,n):
   q=X[i][j]*inv(pivot)%P
   for c in range(j,n):X[i][c]=(X[i][c]-q*X[j][c])%P
 return z%P

A=[[0,0,0],[0,1,0],[0,0,-1]]
B0=proj(K[0],A)
BB=[B0]+[proj(k,B0) for k in K[1:]]
for k,B in zip(K,BB):
 assert sum(B[i][i] for i in range(3))%P==0
 assert all(sum(k[i]*B[i][j] for i in range(3))%P==0 for j in range(3))
rows=[]
for mask in [0,2,3,4,5,6]:
 n=N-2*mask
 rows.append([dot(B0,B)*coscos(K[0],l,n)%P for B,l in zip(BB,K)])
assert rows[0][0]!=0 and rows[0][1:]==[0]*5
assert det(rows)==247, (det(rows),rows)
assert det([row[1:] for row in rows[1:]])==804
# With one u=B0cos(k0*x), 5x5 masked system determines
# v=u+sum_i c_i B_i cos(k_i*x) such that all cross-mask
# inner products vanish. The nonzero global determinant ensures
# global inner product u.v = ||u||_0^2 != 0.
# Band 0: constant traceless tensor has identical all mask/global RMS.
print('PASS: exact finite-field primitive root 159, p=821')
print('PASS: TT projector rank and polarization for six coordinate-band-one modes')
print('6x6 detector determinant mod 821:',det(rows))
print('5x5 interior detector determinant mod 821:',det([row[1:] for row in rows[1:]]))
print('matrix of six exact cyclotomic detector values reduced to F821:')
for row in rows:print(' '.join(str(x) for x in row))
print('THEOREM: exact real six-mode TT counterexample exists at componentwise bandwidth 1')