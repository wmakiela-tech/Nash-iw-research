import sympy as s,itertools
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],[1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,s.Rational(9,100),s.Rational(11,100)],[s.Rational(7,100),0,s.Rational(1,10)],[s.Rational(8,100),s.Rational(12,100),0]])
T=lambda rr: (rr,rr*P,rr*P**2,L*rr)
G=[s.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
Ggp=list(itertools.product((0,1),repeat=2));chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
def pp(M):return [s.factor((1+sum(M[i,j]*chi(j,v)*chi(i,w) for i in range(3) for j in range(3) if i!=j))/16) for v in Ggp for w in Ggp]
u=s.symbols('u',real=True)
for i in range(3):
 for j in range(3):
  if i==j:continue
  print('\nBEACON',i,j)
  allc=[]
  for sign in (+1,-1):
   d=[1,1,1]
   if sign==-1:d[i]=-1;d[(i+1)%3]=-1
   base=s.diag(*d)*R
   H=s.eye(3)+2*u/(1+u*u)*G[i]+2*u*u/(1+u*u)*G[i]**2
   e=s.factor(sign*(L*H*base)[i,j]-(L*R)[i,j])
   num=s.fraction(e)[0]
   roots=s.solve(num,u)
   # infinity root if phi=pi
   Hinf=s.eye(3)+2*G[i]**2
   if s.simplify(sign*(L*Hinf*base)[i,j]-(L*R)[i,j])==0:roots.append('inf')
   print(' sign',sign,'eq num',s.factor(num),'roots',roots)
   for root in roots:
    RR=(Hinf if root=='inf' else H.subs(u,root))*base
    RR=RR.applyfunc(s.factor)
    allM=[]
    okay=True
    mins=[]
    for q in range(4):
     Ap=T(R)[q];Bp=T(RR)[q]
     if any(s.simplify(Bp[a,b])==0 for a in range(3) for b in range(3) if a!=b):
      okay=False;break
     M=s.Matrix(3,3,lambda a,b:s.factor(C[a,b]*Ap[a,b]/Bp[a,b]) if a!=b else 0)
     allM.append(M)
     mins.append(min(pp(M)))
    phys=okay and all(z>0 for z in mins)
    allc.append((sign,root,phys,RR,allM,mins))
    print('   root',root,'phys',phys,'mins',list(map(str,mins)))
  print('TOTAL',len(allc),'LEGAL',sum(x[2] for x in allc))
