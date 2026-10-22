"""PRF11 R17: exact qubit instrument/experiment checks; NumPy/SciPy only."""
import itertools
import math
import numpy as np
from scipy.special import gammaln
I2=np.eye(2, dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)

def rho(theta):
    assert abs(theta)<1/math.sqrt(2)
    return (I2+theta*X+theta*Y)/2

def matrix_sqrt_positive(a):
    w,v=np.linalg.eigh(a)
    return (v*np.sqrt(np.maximum(w,0)))@v.conj().T

def output_maps(s,theta):
    r=rho(theta)
    effects=[(I2+s*X)/2,(I2-s*X)/2]
    K=[matrix_sqrt_positive(e) for e in effects]
    out_l=sum((k@r@k for k in K),np.zeros((2,2),dtype=complex))
    k=math.sqrt(1-s*s); p=(1+k)/2
    out_u=p*r+(1-p)*(X@r@X)
    return np.max(np.abs(out_l-out_u)),K

def sequence_probs_kraus(s,theta,N):
    err,K=output_maps(s,theta)
    assert err<1e-12
    probs={}
    for seq in itertools.product((1,-1),repeat=N):
        cur=rho(theta)
        for val in seq:
            kk=K[0] if val==1 else K[1]
            cur=kk@cur@kk
        direct=float(np.trace(cur).real)
        Lp=math.prod((1+s*v)/2 for v in seq)
        Lm=math.prod((1-s*v)/2 for v in seq)
        model=(1+theta)/2*Lp+(1-theta)/2*Lm
        assert abs(direct-model)<1e-12,(seq,direct,model)
        probs[seq]=direct
    assert abs(sum(probs.values())-1)<1e-12
    return len(probs)

def fisher_luders_sequence(N,s,theta):
    """Exact binomial-sufficient log probabilities (no Monte Carlo)."""
    ks=np.arange(N+1,dtype=float)
    comb=gammaln(N+1)-gammaln(ks+1)-gammaln(N-ks+1)
    Lplus=comb+ks*np.log((1+s)/2)+(N-ks)*np.log((1-s)/2)
    Lminus=comb+ks*np.log((1-s)/2)+(N-ks)*np.log((1+s)/2)
    P=np.logaddexp(np.log((1+theta)/2)+Lplus,np.log((1-theta)/2)+Lminus)
    score=(np.exp(Lplus-P)-np.exp(Lminus-P))/2
    return float(np.sum(np.exp(P)*score*score))

def run():
    for s in [0.15,0.2,0.5,0.9]:
        for theta in [-0.3,0,0.25]:
            err,_=output_maps(s,theta)
            assert err<1e-12
            assert abs(fisher_luders_sequence(1,s,theta)-s*s/(1-s*s*theta*theta))<1e-12
            for n in [1,2,3,4]:sequence_probs_kraus(s,theta,n)
    print('CHANNEL_IDENTITY_AND_SEQUENCE_CARRIER: PASS')
    theta=.25;s=.2
    qfi=2/(1-2*theta*theta)
    sharp=1/(1-theta*theta)
    print('theta=0.25, QFI=',f'{qfi:.9f}','sigma_x sharp FI=',f'{sharp:.9f}')
    print('N       repeated Lueders FI       no-info unitary FI       QFI limit')
    for N in [1,2,5,25,100,500]:
        fi=fisher_luders_sequence(N,s,theta)
        assert 0<=fi<=sharp+1e-9
        print(f'{N:<5d}   {fi:<24.12f}  {0:<22d} {qfi:.12f}')
    R=.5
    assert R*R<.5
    J=R*R*(1-R*R)
    print('EXACT_SINGLE_COPY_SHARP_X_MINIMAX_MSE R=0.5:',J)
    print('NO_INFORMATION_MINIMAX_MSE:',R*R)
    print('LONG_SEQUENCE_CHERNOFF_DELTA_BOUND s=.2,N=500:',math.exp(-500*.2*.2/2))

if __name__=='__main__':run()
