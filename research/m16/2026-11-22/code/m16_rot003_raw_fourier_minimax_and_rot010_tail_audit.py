#!/usr/bin/env python3
"""M16 ROT003: source-conditioned independent mathematical/interval checks.

Not a reproduction of Geeky-S13 ROT010's 32-node Gauss-Legendre / 4000-panel
IV75 computation. Only source Delta, score-minorization preconditions and the
entire Fourier integral tail are independently checked here.
"""
import json
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 75
mp.iv.dps = 80
iv = mp.iv


def spectra(c, model):
    if model == 'A':
        v = mp.mpf(167)/150 + mp.mpf(14)*c/75
        return v, v
    return mp.mpf(82)/75+mp.mpf(31)*c/150, mp.mpf(17)/15+c/6


def f_pos(t, scalar=mp):
    q=scalar.exp(-t)
    return q*((t-2)+(t+2)*q)/(1-q)**3


def interval_check():
    c7 = iv.cos(2*iv.pi*7/41)
    c20 = iv.cos(2*iv.pi*20/41)
    vx=lambda c: iv.mpf(82)/75+iv.mpf(31)*c/150
    vy=lambda c: iv.mpf(17)/15+c/6
    delta = iv.log(vx(c7)/vy(c7))-iv.log(vx(c20)/vy(c20))
    fpoint = f_pos(2+delta/2,iv)
    ellpoint = iv.log(f_pos(2+delta/2,iv)/f_pos(2-delta/2,iv))
    tail = iv.mpf('0.998272')**14538 / (16*iv.pi)
    assert delta > iv.mpf('0.068')
    assert delta < iv.mpf('0.069')
    assert fpoint > iv.mpf('0.11')
    assert ellpoint < iv.mpf('-0.024')
    assert tail < iv.mpf('2.4e-13')
    return dict(Delta=str(delta), f_2_Delta_over_2=str(fpoint), ell_2=str(ellpoint),
                full_tail_14538_bound=str(tail), pass_tail_conditions=True)


def canonical_gauge_test(eps_frac, seed=314159, N=600):
    # RAW power vector order [x20, y20, x7, y7]
    c7=mp.cos(2*mp.pi*7/41)
    c20=mp.cos(2*mp.pi*20/41)
    ax20,ay20=spectra(c20,'A')
    ax7,ay7=spectra(c7,'A')
    bx20,by20=spectra(c20,'B')
    bx7,by7=spectra(c7,'B')
    a=np.log(np.array([float(v) for v in (ax20,ay20,ax7,ay7)]))
    b=np.log(np.array([float(v) for v in (bx20,by20,bx7,by7)]))
    w=np.array([1.,-1.,-1.,1.])
    delta=-(w@b)
    assert abs(w@a)<1e-14
    assert delta>0
    eps=eps_frac*delta
    # Each E_ij generated independently Exp(1); shared E coupling under A/B
    # for checking equality of the *entire* RAW observation path.
    e=np.log(np.random.default_rng(seed).exponential(size=(N,4)))
    def make(base,eta):
        latent=e+base
        z0=latent@w
        z=z0+eta
        y=np.outer(z,w)/4.0
        loggain=y-latent
        assert np.max(np.abs((loggain@w)-eta))<2e-14
        assert np.all(np.exp(loggain)>0)
        assert np.max(np.abs((y@w)-z))<1e-14
        return y,loggain,z
    ya,ka,za=make(a,-eps)
    yb,kb,zb=make(b,+eps)
    shift=delta-2*eps
    assert np.max(np.abs((za-zb)-shift))<2e-14
    assert np.max(np.abs((ya-yb)-np.outer(np.full(N,shift),w)/4))<1e-14
    if abs(eps_frac-0.5)<1e-12:
        assert np.max(np.abs(ya-yb))<5e-14  # logarithmic relative-power criterion
    return dict(eps_divided_by_Delta=eps_frac, delta=delta,
                crossgain_A=-eps, crossgain_B=eps,
                max_abs_raw_log_matched_diff=float(np.max(np.abs(ya-yb))),
                alias_all_four_raw_energies=abs(eps_frac-0.5)<1e-12,
                checks_pass=True)


def main():
    output={"scope":"four RAW powers, adaptive model-specific latent-dependent gains only",
            "status":"independent deterministic algebra check and bounded interval tail subaudit, not full IV75 replay",
            "interval":interval_check(),
            "gauge_checks":[canonical_gauge_test(x) for x in (0.,0.25,0.5)]}
    print(json.dumps(output,indent=2,ensure_ascii=False))


if __name__=='__main__':
    main()
