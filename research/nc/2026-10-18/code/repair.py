import numpy as np, itertools
rng=np.random.default_rng(20261018)

# WERSJA LT4 (Tw. 7.12, wzory 7.16-7.18):
#   J_col = suma_{lam_i != mu_j, h(lam_i)=h(mu_j)} Q_j J P_i
#   || J m(A) - m(B) J || <= 2 ||m||_inf || J_col ||
# MOJA WYCOFANA WERSJA (pakiet 002 §B.2):
#   kappa_h = max_{pary kolizyjne} || Q_j J P_i ||   <-- FALSZ
# Ten skrypt: (a) probuje OBALIC wersje LT4 losowo i w konfiguracjach wielokolizyjnych,
# (b) mierzy, ile par kolizyjnych trzeba, zeby rozdzielic obie wersje,
# (c) sprawdza, czy stala 2 jest osiagana.

def spec(diag):
    vals=sorted(set(diag))
    return np.array(vals),[np.diag([1.0 if d==v else 0.0 for d in diag]) for v in vals]

def fc(H,m):
    w,V=np.linalg.eigh(H); return V@np.diag(m(w))@V.conj().T

def defect(J,A,B,m):
    return np.linalg.norm(J@fc(A,m)-fc(B,m)@J,2)

def pieces(J,lam,Ps,mu,Qs,h):
    Jcol=np.zeros_like(J); mx=0.0; npair=0
    for i,li in enumerate(lam):
        for j,mj in enumerate(mu):
            if abs(li-mj)>1e-12 and abs(h(li)-h(mj))<1e-12:
                blk=Qs[j]@J@Ps[i]; Jcol=Jcol+blk
                mx=max(mx,np.linalg.norm(blk,2)); npair+=1
    return Jcol,mx,npair

def worst_mult(J,A,B,lam,mu):
    # dla widma czystopunktowego najgorszy ograniczony m to znaki +-1 na wartosciach wlasnych
    vals=sorted(set(list(lam)+list(mu))); best=0.0
    for s in itertools.product([-1.0,1.0],repeat=len(vals)):
        d={v:si for v,si in zip(vals,s)}
        m=lambda w,d=d: np.array([d[min(d,key=lambda k:abs(k-wi))] for wi in np.atleast_1d(w)])
        best=max(best,defect(J,A,B,m))
    return best

print("TABELA R1  kontrprzyklad 7.4 LT4 — rekonstrukcja")
A=np.diag([0.,1.]); B=np.diag([2.,3.]); h=lambda l: np.cos(2*np.pi*l)
lam,Ps=spec([0.,1.]); mu,Qs=spec([2.,3.]); J=0.5*np.ones((2,2))
Jcol,mx,npair=pieces(J,lam,Ps,mu,Qs,h)
w=worst_mult(J,A,B,lam,mu)
print(f"  par kolizyjnych      {npair}")
print(f"  max blok (moja)      {mx:.6f}   -> moja granica 2*{mx:.3f} = {2*mx:.6f}")
print(f"  ||J_col|| (LT4)      {np.linalg.norm(Jcol,2):.6f}   -> granica LT4 = {2*np.linalg.norm(Jcol,2):.6f}")
print(f"  faktyczny defekt     {w:.6f}")
print(f"  moja granica zachodzi?  {w<=2*mx+1e-9}")
print(f"  granica LT4 zachodzi?   {w<=2*np.linalg.norm(Jcol,2)+1e-9}")
print(f"  granica LT4 osiagana?   {abs(w-2*np.linalg.norm(Jcol,2))<1e-9}")

print()
print("TABELA R2  proba OBALENIA wersji LT4: 4000 losowych ukladow, widma z wymuszonymi kolizjami")
print("  n   prob   maxiloraz defekt/granicaLT4   maxiloraz defekt/mojagranica   naruszen LT4   naruszen moich")
for n in [2,3,4]:
    viol_lt4=0; viol_nc=0; r_lt4=0.0; r_nc=0.0; trials=0
    for _ in range(4000//1):
        # widma tak, by h=cos(2 pi lam) dawalo kolizje: wartosci calkowite
        dA=list(rng.integers(0,4,size=n).astype(float))
        dB=list(rng.integers(0,4,size=n).astype(float)+0.0)
        if len(set(dA))<1 or len(set(dB))<1: continue
        lam,Ps=spec(dA); mu,Qs=spec(dB)
        A=np.diag(dA); B=np.diag(dB)
        J=rng.normal(size=(n,n))
        # wymus hipoteze J h(A) = h(B) J : zeruj bloki o roznych wartosciach h
        for i,li in enumerate(lam):
            for j,mj in enumerate(mu):
                if abs(h(li)-h(mj))>1e-12: J=J-Qs[j]@J@Ps[i]
        if np.linalg.norm(J,2)<1e-12: continue
        if defect(J,A,B,h)>1e-9: continue
        Jcol,mx,npair=pieces(J,lam,Ps,mu,Qs,h)
        if npair==0: continue
        w=worst_mult(J,A,B,lam,mu); trials+=1
        b_lt4=2*np.linalg.norm(Jcol,2); b_nc=2*mx
        if b_lt4>1e-14: r_lt4=max(r_lt4,w/b_lt4)
        if b_nc>1e-14: r_nc=max(r_nc,w/b_nc)
        if w>b_lt4+1e-9: viol_lt4+=1
        if w>b_nc+1e-9: viol_nc+=1
    print(f"  {n}   {trials:<6} {r_lt4:<28.6f} {r_nc:<30.6f} {viol_lt4:<14} {viol_nc}")

print()
print("TABELA R3  ile par kolizyjnych rozdziela obie wersje (ile potrzeba, by moja padla)")
print("  par kolizyjnych   czy znaleziono naruszenie mojej granicy")
for npair_target in [1,2,3,4]:
    found=False
    for _ in range(20000):
        n=2 if npair_target<=4 else 3
        dA=list(rng.integers(0,4,size=n).astype(float)); dB=list(rng.integers(0,4,size=n).astype(float))
        lam,Ps=spec(dA); mu,Qs=spec(dB); A=np.diag(dA); B=np.diag(dB)
        J=rng.normal(size=(n,n))
        for i,li in enumerate(lam):
            for j,mj in enumerate(mu):
                if abs(h(li)-h(mj))>1e-12: J=J-Qs[j]@J@Ps[i]
        if defect(J,A,B,h)>1e-9: continue
        Jcol,mx,npair=pieces(J,lam,Ps,mu,Qs,h)
        if npair!=npair_target or mx<1e-12: continue
        w=worst_mult(J,A,B,lam,mu)
        if w>2*mx+1e-9: found=True; break
    print(f"  {npair_target:<17} {found}")
