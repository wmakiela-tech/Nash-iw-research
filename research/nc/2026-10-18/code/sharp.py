import numpy as np, itertools
rng=np.random.default_rng(20261018)

# A = sum lam_i P_i , B = sum mu_j Q_j  (self-adjoint, spectral projections)
# CLAIM (NC sharp form):
#   given J h(A) = h(B) J,
#   J m(A) = m(B) J for ALL bounded Borel m
#   IFF  Q_j J P_i = 0 for every (i,j) with lam_i != mu_j AND h(lam_i) == h(mu_j)
# Derivation: Q_j(J f(A) - f(B) J)P_i = (f(lam_i) - f(mu_j)) Q_j J P_i.

def spectral(diag):
    n=len(diag); vals=sorted(set(diag))
    Ps=[np.diag([1.0 if d==v else 0.0 for d in diag]) for v in vals]
    return np.array(vals), Ps

def blocks(J,Ps,Qs):
    return [[Qs[j]@J@Ps[i] for i in range(len(Ps))] for j in range(len(Qs))]

def intertw_defect(J,A,B,m):
    def fc(H):
        w,V=np.linalg.eigh(H); return V@np.diag(m(w))@V.conj().T
    return np.linalg.norm(J@fc(A)-fc(B)@J)

MS=[('1/(1+w)',lambda w:1/(1+w)), ('exp(-.7w)',lambda w:np.exp(-.7*w)),
    ('1_{w>1.5}',lambda w:(w>1.5).astype(float)), ('w^2',lambda w:w**2),
    ('sin(2w)',lambda w:np.sin(2*w)), ('sqrt(w)',lambda w:np.sqrt(np.abs(w)))]

print("TABLE S1  THE SHARP CRITERION, forward and backward, h NON-SEPARATING throughout")
print("  h(lambda)=cos(pi*lambda);  sigma(A)={0,1}, sigma(B)={0,3};  collision: h(1)=h(3)=-1")
print("  so the ONLY offending pair is (lam=1, mu=3). Criterion: Q_{mu=3} J P_{lam=1} = 0 ?")
print()
dA=[0.0,1.0,1.0]; dB=[0.0,3.0,3.0]
lamA,Ps=spectral(dA); muB,Qs=spectral(dB)
h=lambda w: np.cos(np.pi*w)
A=np.diag(dA); B=np.diag(dB)
i1=list(lamA).index(1.0); j3=list(muB).index(3.0)

cases={}
# case 1: J that DOES couple the colliding pair
J1=np.zeros((3,3)); J1[0,0]=1.0; J1[1,1]=1.0           # Q_{3} J P_{1} != 0
# case 2: J that does NOT couple it (only the matched block lam=0 <-> mu=0)
J2=np.zeros((3,3)); J2[0,0]=1.0
# case 3: random J restricted to the matched block only
J3=np.zeros((3,3)); J3[0,0]=rng.normal()
cases['couples colliding pair']=J1
cases['does NOT couple (matched block only)']=J2
cases['random, matched block only']=J3

print(f"{'J':<38} {'||Q3 J P1||':>12} {'hyp ||Jh(A)-h(B)J||':>21} {'max_m ||Jm(A)-m(B)J||':>23} {'criterion predicts':>20}")
for name,J in cases.items():
    blk=np.linalg.norm(Qs[j3]@J@Ps[i1])
    hyp=intertw_defect(J,A,B,h)
    worst=max(intertw_defect(J,A,B,m) for _,m in MS)
    pred = 'FULL TRANSPORT' if blk<1e-12 else 'FAILS'
    print(f"{name:<38} {blk:>12.3e} {hyp:>21.3e} {worst:>23.3e} {pred:>20}")

print()
print("TABLE S2  randomized test of the IFF over many (A,B,J,h) with forced collisions")
print("  for each trial: build A,B with a known collision under h, pick J randomly,")
print("  ZERO OUT only the offending blocks with prob p, then check prediction vs reality.")
print(f"{'trial':>5} {'offending blocks':>17} {'all zero?':>10} {'hyp defect':>12} {'max_m defect':>13} {'IFF holds':>10}")
ok=0; tot=0
for tr in range(14):
    dA=[0.0,1.0]; dB=[0.0,3.0]
    lamA,Ps=spectral(dA); muB,Qs=spectral(dB)
    A=np.diag(dA); B=np.diag(dB)
    J=rng.normal(size=(2,2))
    # enforce the hypothesis: zero every block with h(lam_i)!=h(mu_j)
    for i,li in enumerate(lamA):
        for j,mj in enumerate(muB):
            if not np.isclose(h(np.array([li]))[0],h(np.array([mj]))[0]):
                J=J-Qs[j]@J@Ps[i]
    if tr%2==0:   # also kill the offending (collision, lam!=mu) blocks
        for i,li in enumerate(lamA):
            for j,mj in enumerate(muB):
                if (not np.isclose(li,mj)) and np.isclose(h(np.array([li]))[0],h(np.array([mj]))[0]):
                    J=J-Qs[j]@J@Ps[i]
    offend=[np.linalg.norm(Qs[j]@J@Ps[i]) for i,li in enumerate(lamA) for j,mj in enumerate(muB)
            if (not np.isclose(li,mj)) and np.isclose(h(np.array([li]))[0],h(np.array([mj]))[0])]
    allzero=all(o<1e-12 for o in offend)
    hyp=intertw_defect(J,A,B,h)
    worst=max(intertw_defect(J,A,B,m) for _,m in MS)
    iff = (allzero and worst<1e-10) or ((not allzero) and worst>1e-10)
    ok+=iff; tot+=1
    print(f"{tr:>5} {len(offend):>17} {str(allzero):>10} {hyp:>12.3e} {worst:>13.3e} {str(iff):>10}")
print(f"  IFF held in {ok}/{tot} trials")
