import sympy as S
from itertools import permutations,product
g=S.sqrt(3);r=S.Rational
vals=[(1,0),(-r(1,2),g/2),(-r(1,2),-g/2)]
words=list(product(range(3),repeat=3))
rays=[(r(2,3),[(a,b)]*3) for a,b in [(1,0),(0,1),(-1,0),(0,-1)]]
for p in permutations((0,1,2)):
 odd=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
 sgn=1 if odd else -1
 rays.append((r(8,9),[(sgn*vals[p[j]][0],sgn*vals[p[j]][1]) for j in range(3)]))
M=S.zeros(27,16)
for j,(weight,loc) in enumerate(rays):
 for i,w in enumerate(words):
  v=weight
  for k,t in enumerate(w):
   if t:v*=loc[k][t-1]
  M[i,j]=v
for k in range(3):
 for t in (1,2):
  w=tuple(t if j==k else 0 for j in range(3))
  M[words.index(w),10+2*k+t-1]=1
indices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,18,26]
d=S.simplify(M[indices,:].det(method='domain-ge'))
assert M.rank()==16 and d==-r(131072,59049)*g
print('exact rank',M.rank(),'exact minor',d)
