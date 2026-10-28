import math
import numpy as np
from scipy.stats import binom
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
def k3(a): return np.kron(np.kron(a,a),a)
def agree(a): return k3((I+a)/2)+k3((I-a)/2)
E=(agree(X)+agree(Y))/2
for phi in np.linspace(-31,43,307):
 u=np.array([1,np.exp(1j*phi)])/math.sqrt(2)
 v=np.kron(np.kron(u,u),u)
 assert abs(np.vdot(v,E@v).real-5/8)<1e-13
q=1/3
x=math.exp(-q);pA=5/8;pB=(2+3*x*x)/8
assert abs(np.trace(E@k3((I+x*X)/2)).real-pB)<1e-13
def error(n):
 a=math.log(pA/pB);d=math.log((1-pB)/(1-pA))
 k=math.ceil(n*d/(a+d)-1e-12)
 return (binom.cdf(k-1,n,pA)+binom.sf(k-1,n,pB))/2,k
assert error(80)[0]<.05
assert all(error(n)[0]>.05 for n in range(1,80))
print('PASS 307 phase checks, B matrix, exact finite N')
print('pA',pA,'pB',pB,'minimal N for <5 percent Bayes error',80,'value',error(80))
