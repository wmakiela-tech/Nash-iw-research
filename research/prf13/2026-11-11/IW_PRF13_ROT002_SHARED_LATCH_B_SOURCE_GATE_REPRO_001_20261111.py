#!/usr/bin/env python3
"""PRF13 ROT002: source-native shared-latch falsifier in R31 source B.
Standalone Python3 + mpmath >=1.3; no physical data, no original 3Q LOCC claim.
Source R34 independent 2x2/4x4 B audit was used for an independent check.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / REFEREE_PENDING.
"""
import mpmath as mp
mp.mp.dps=70
f=mp.mpf
I=mp.eye(2)
X=mp.matrix([[0,1],[1,0]])
Y=mp.matrix([[0,-1j],[1j,0]])
Z=mp.matrix([[1,0],[0,-1]])
rho0=mp.matrix([[1,0],[0,0]])
T=mp.pi/20

def vecf(R):
    return mp.matrix([R[0,0],R[1,0],R[0,1],R[1,1]])

def matf(v):
    return mp.matrix([[v[0],v[2]],[v[1],v[3]]])

def kron(A,B):
    M=mp.zeros(A.rows*B.rows,A.cols*B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l in range(B.cols):
                    M[i*B.rows+k,j*B.cols+l]=A[i,j]*B[k,l]
    return M

def lb(H):
    return -1j*(kron(I,H)-kron(H.T,I)) + f('0.5')*(kron(Z,Z)-mp.eye(4))

def evolve(state,H,dt):
    return mp.expm(dt*lb(H))*state

def zmean(state):
    R=matf(state)
    return mp.re(R[0,0]-R[1,1])

def B_means():
    # The same continuous Lindblad physical source B as R31/R34:
    # source ON during pi/2 preparation, free evolution, and analysis.
    state=evolve(vecf(rho0),5*Y,T)
    state=evolve(state,mp.zeros(2),f('0.5'))
    return [zmean(evolve(state,-5*Y,T)),
            zmean(evolve(state, 5*X,T)),
            zmean(state)]

def main():
    mb=B_means()
    W=[f('.18'),f('.20'),f('.62')]
    A=[f('.943'),f('.907'),f('.347')]
    B=[f('1'),f('1'),f('.018')]
    p0=f('.99')
    p1=f(3705)/f(69000)
    d=p0-p1
    independent=f(0);latched=f(0)
    detail=[]
    for j in range(3):
        p=(1+mb[j])/2 # ideal +-probability for each fresh shot
        q=p1+d*p # same recorded-plus marginal in BOTH models
        t_ind=q*q
        # A fresh U~Uniform[0,1] is used for both recorded shots.
        # Conditional on ideal Z bits z1,z2, thresholds are p0 or p1.
        # Since p0 >= p1, averaging min(threshold1,threshold2)
        # over two independent ideal B shot bits yields:
        t_latch=p1+d*p*p
        assert t_latch>=t_ind
        g_ind=A[j]*t_ind+B[j]*(1-2*q+t_ind)
        g_latch=A[j]*t_latch+B[j]*(1-2*q+t_latch)
        independent+=W[j]*g_ind
        latched+=W[j]*g_latch
        detail.append((mp.nstr(mb[j],30),mp.nstr(g_latch-g_ind,30)))
    assert abs(mb[0]-f('.5219734434954134')) < f('1e-14')
    assert abs(mb[1]-f('.00231335785212866')) < f('1e-14')
    assert abs(mb[2]-f('.04809737884883814')) < f('1e-14')
    assert independent < f('.2828') < latched
    shift=latched-independent
    theta_critical=(f('.2828')-independent)/shift
    assert 0 < theta_critical < 1
    N=9500;K=2765
    tail_old=mp.betainc(K,N-K+1,0,f('.2828'),regularized=True)
    tail_latched=mp.betainc(K,N-K+1,0,latched,regularized=True)
    assert tail_old < tail_latched
    assert tail_old+f('.01')<f('.05')<tail_latched+f('.01')
    print('B source axis m=',detail)
    for name,val in [('B_independent',independent),('B_latched',latched),
        ('B_latch_minus_independent',shift),
        ('B_latched_minus_b02828',latched-f('.2828')),
        ('theta_critical',theta_critical),('B_binom_tail_old',tail_old),
        ('B_binom_tail_latched',tail_latched),
        ('tail_plus_calibration_alpha001',tail_latched+f('.01'))]:
        print(name+'='+mp.nstr(val,60))
    print('PASS: source-B conditional-score bound fails outside independent-readout contract')
    print('IMPORTANT: alpha+tail is a failed UNION-BOUND CERTIFICATE, not proven actual >5% error')

if __name__=='__main__':
    main()
