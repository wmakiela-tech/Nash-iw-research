import numpy as np
from itertools import product

# PREREG_COLL.md sha256 463f2da3695fea2b968611a4ac8329495003fac68da8face05123de0bc7dbfe4
# Naprawa NC-FAL-011: zamiast kappa_h(J) = sup norm blokow -> norma CALEJ czesci kolizyjnej.
# Widmo punktowe proste: P_i, Q_j rangi 1, wiec blok Q_j J P_i = wpis J[j,i].

rng = np.random.default_rng(20261024)

def rozklad(la, mu, J, h):
    """zwraca (J_hip, J_coll, J_match) — J_hip ma wyzerowane bloki niekolizyjne (hipoteza)"""
    HA, HB = h(la), h(mu)
    n, m_ = len(mu), len(la)
    Jh = np.array(J, dtype=J.dtype)
    coll = np.zeros_like(Jh); match = np.zeros_like(Jh)
    for j in range(n):
        for i in range(m_):
            if abs(HB[j]-HA[i]) > 1e-12:
                Jh[j, i] = 0.0                      # hipoteza J h(A) = h(B) J
            elif abs(mu[j]-la[i]) <= 1e-12:
                match[j, i] = Jh[j, i]              # para dopasowana: wspolczynnik m-m = 0
            else:
                coll[j, i] = Jh[j, i]               # kolizja
    return Jh, coll, match

def sup_defekt(la, mu, Jh, zesp=False, krokow=24):
    """sup po ||m||_inf <= 1 z ||J m(A) - m(B) J||. Defekt jest LINIOWY w m, norma wypukla,
       wiec sup po kostce siedzi w wierzcholku -> enumeracja +-1 jest DOKLADNA dla m rzeczywistych."""
    wart = sorted(set([round(float(x), 12) for x in list(la)+list(mu)]))
    idxA = [wart.index(round(float(x), 12)) for x in la]
    idxB = [wart.index(round(float(x), 12)) for x in mu]
    best, arg = 0.0, None
    if not zesp:
        for s in product([1.0, -1.0], repeat=len(wart)):
            mA = np.array([s[k] for k in idxA]); mB = np.array([s[k] for k in idxB])
            D = Jh*mA[None, :] - mB[:, None]*Jh
            v = np.linalg.norm(D, 2)
            if v > best: best, arg = v, s
    else:
        for _ in range(400):
            th = rng.uniform(0, 2*np.pi, len(wart))
            for _ in range(krokow):
                mA = np.exp(1j*th[idxA]); mB = np.exp(1j*th[idxB])
                base = np.linalg.norm(Jh*mA[None, :] - mB[:, None]*Jh, 2)
                g = np.zeros(len(wart))
                for k in range(len(wart)):
                    t2 = th.copy(); t2[k] += 1e-6
                    mA2 = np.exp(1j*t2[idxA]); mB2 = np.exp(1j*t2[idxB])
                    g[k] = (np.linalg.norm(Jh*mA2[None, :] - mB2[:, None]*Jh, 2)-base)/1e-6
                th = th + 0.5*g
            mA = np.exp(1j*th[idxA]); mB = np.exp(1j*th[idxB])
            v = np.linalg.norm(Jh*mA[None, :] - mB[:, None]*Jh, 2)
            if v > best: best, arg = v, th
    return best, arg

print("TABELA T1  KONTROLA F4 — czy ODTWARZAM naruszenie STAREJ nierownosci na macierzach REC9")
print("  A = diag(0,1), B = diag(2,3), h = cos(2 pi lambda), J = (1/2)[[1,1],[1,1]]")
la = np.array([0.0, 1.0]); mu = np.array([2.0, 3.0])
hcos = lambda x: np.cos(2*np.pi*np.asarray(x))
J0 = 0.5*np.ones((2, 2))
Jh, coll, match = rozklad(la, mu, J0, hcos)
print(f"  h(A) = {np.round(hcos(la),12).tolist()}   h(B) = {np.round(hcos(mu),12).tolist()}")
print(f"  hipoteza ||J h(A) - h(B) J|| = {np.linalg.norm(J0@np.diag(hcos(la))-np.diag(hcos(mu))@J0, 2):.3e}")
print(f"  liczba blokow kolizyjnych = {int(np.sum(np.abs(coll)>0))} z {la.size*mu.size}")
print(f"  ||J|| = {np.linalg.norm(J0,2):.12f}   kappa_h(J) = max|blok| = {np.max(np.abs(coll)):.12f}   "
      f"||J_coll|| = {np.linalg.norm(coll,2):.12f}")
d, s = sup_defekt(la, mu, Jh)
stara = 2*1.0*np.max(np.abs(coll)); nowa = 2*1.0*np.linalg.norm(coll, 2)
print(f"  sup defektu po ||m||_inf<=1 : {d:.12f}   (wierzcholek m = {s})")
print(f"  STARA granica 2||m||kappa_h = {stara:.12f}   naruszona: {'TAK' if d > stara+1e-9 else 'NIE'}")
print(f"  NOWA  granica 2||m|| ||J_coll|| = {nowa:.12f}   naruszona: {'TAK' if d > nowa+1e-9 else 'NIE'}")

print()
print("TABELA T2  H3 — czy stala 2 jest OSIAGANA; swiadek jawny na macierzach REC9")
print("  m = +1 na widmie A, -1 na widmie B  =>  m(A) = I, m(B) = -I,  J m(A) - m(B) J = 2J")
mA = np.array([1.0, 1.0]); mB = np.array([-1.0, -1.0])
D = Jh*mA[None, :] - mB[:, None]*Jh
print(f"  ||J m(A) - m(B) J|| = {np.linalg.norm(D,2):.15f}")
print(f"  2 ||m||_inf ||J_coll||  = {2*np.linalg.norm(coll,2):.15f}")
print(f"  iloraz = {np.linalg.norm(D,2)/(np.linalg.norm(coll,2)):.15f}   (ma byc 2)")

print()
print("TABELA T3  F1/F2 — zamiatanie losowe; iloraz = sup defektu / (2 ||J_coll||)")
print("  n   prob   przyp. z J_coll != 0   max iloraz   min iloraz   naruszen F1   max ||J_coll||/||J||")
for n in [2, 3, 4, 5, 6]:
    tot = 0; mx = 0.0; mn = 9.9; viol = 0; rq = 0.0
    for _ in range(300):
        # widma calkowite -> cos(2 pi .) skleja wszystko; dla rozmaitosci mieszam skale
        tryb = rng.integers(0, 3)
        if tryb == 0:
            la = rng.choice(np.arange(0, 12), size=n, replace=False).astype(float)
            mu = rng.choice(np.arange(0, 12), size=n, replace=False).astype(float)
            h = hcos
        elif tryb == 1:
            la = rng.choice(np.arange(0, 10), size=n, replace=False).astype(float)
            mu = la + rng.choice([2.0, 4.0, 6.0], size=n)
            h = lambda x: np.cos(np.pi*np.asarray(x))
        else:
            la = rng.normal(0, 2, n); mu = np.concatenate([la[:max(1, n//2)], rng.normal(0, 2, n-max(1, n//2))])
            h = lambda x: np.round(np.asarray(x), 0)       # skleja po zaokragleniu
        if len(set(np.round(la, 9))) < n or len(set(np.round(mu, 9))) < n: continue
        J = rng.normal(0, 1, (n, n))
        Jh, coll, match = rozklad(la, mu, J, h)
        if np.linalg.norm(coll, 2) < 1e-13: continue
        tot += 1
        d, _ = sup_defekt(la, mu, Jh)
        r = d/(2*np.linalg.norm(coll, 2))
        mx = max(mx, r); mn = min(mn, r)
        if r > 1+1e-9: viol += 1
        if np.linalg.norm(Jh, 2) > 1e-13:
            rq = max(rq, np.linalg.norm(coll, 2)/np.linalg.norm(Jh, 2))
    print(f"  {n}   300    {tot:<21} {mx:<12.9f} {mn:<12.9f} {viol:<13} {rq:.9f}")

print()
print("TABELA T4  F3 — przypadki z ||J_coll|| = 0: defekt MUSI byc zerowy (kryterium jakosciowe)")
print("  n   przyp. z J_coll = 0   max sup defektu   max |J_match|   naruszen F3")
for n in [2, 3, 4, 5]:
    tot = 0; mxd = 0.0; mxm = 0.0; viol = 0
    for _ in range(400):
        la = rng.choice(np.arange(0, 10), size=n, replace=False).astype(float)
        mu = rng.choice(np.arange(0, 10), size=n, replace=False).astype(float)
        J = rng.normal(0, 1, (n, n))
        Jh, coll, match = rozklad(la, mu, J, hcos)
        Jh = Jh - coll                                   # wymus J_coll = 0
        _, c2, m2 = rozklad(la, mu, Jh, hcos)
        if np.linalg.norm(c2, 2) > 1e-13: continue
        if np.linalg.norm(Jh, 2) < 1e-13: continue
        tot += 1
        d, _ = sup_defekt(la, mu, Jh)
        mxd = max(mxd, d); mxm = max(mxm, np.max(np.abs(m2)))
        if d > 1e-9: viol += 1
    print(f"  {n}   {tot:<21} {mxd:<17.3e} {mxm:<15.9f} {viol}")

print()
print("TABELA T5  F5/H4 — czy ||J_coll|| <= 2||J||, i jak duzy jest iloraz")
print("  n   przyp.   max ||J_coll||/||J||   naruszen (>2)")
for n in [2, 3, 4, 6, 8]:
    tot = 0; mx = 0.0; viol = 0
    for _ in range(400):
        la = rng.choice(np.arange(0, 14), size=n, replace=False).astype(float)
        mu = rng.choice(np.arange(0, 14), size=n, replace=False).astype(float)
        J = rng.normal(0, 1, (n, n))
        Jh, coll, match = rozklad(la, mu, J, hcos)
        nj = np.linalg.norm(Jh, 2)
        if nj < 1e-13: continue
        tot += 1
        r = np.linalg.norm(coll, 2)/nj
        mx = max(mx, r)
        if r > 2+1e-9: viol += 1
    print(f"  {n}   {tot:<8} {mx:<22.9f} {viol}")

print()
print("TABELA T6  m ZESPOLONE, |m| <= 1 — czy granica 2||m|| ||J_coll|| nadal trzyma")
print("  n   przyp.   max iloraz (rzecz.)   max iloraz (zesp.)   naruszen F1 zesp.")
for n in [2, 3, 4]:
    tot = 0; mr = 0.0; mc = 0.0; viol = 0
    for _ in range(40):
        la = rng.choice(np.arange(0, 10), size=n, replace=False).astype(float)
        mu = rng.choice(np.arange(0, 10), size=n, replace=False).astype(float)
        J = rng.normal(0, 1, (n, n)) + 1j*rng.normal(0, 1, (n, n))
        Jh, coll, match = rozklad(la, mu, J, hcos)
        nc = np.linalg.norm(coll, 2)
        if nc < 1e-13: continue
        tot += 1
        dr, _ = sup_defekt(la, mu, Jh, zesp=False)
        dc, _ = sup_defekt(la, mu, Jh, zesp=True)
        mr = max(mr, dr/(2*nc)); mc = max(mc, dc/(2*nc))
        if dc > 2*nc+1e-7: viol += 1
    print(f"  {n}   {tot:<8} {mr:<21.9f} {mc:<20.9f} {viol}")
