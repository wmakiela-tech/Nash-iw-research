#!/usr/bin/env python3
"""M16 ROT002: source-parameter reproducibility of sharp 4-mode cross-gain radius.

Model: Geeky-S13 ROT009, N41 anisotropic Gaussian Fourier powers.
Theorems (endpoint least favourability, alias) are analytical; high precision
checks here DO NOT establish a new interval proof or a physical sensor.
"""
import mpmath as mp
mp.mp.dps = 90


def source_delta():
    c7 = mp.cos(2 * mp.pi * 7 / 41)
    c20 = mp.cos(2 * mp.pi * 20 / 41)
    vx = lambda c: mp.mpf(82)/75 + mp.mpf(31)*c/150
    vy = lambda c: mp.mpf(17)/15 + c/6
    return mp.log(vx(c7)/vy(c7)) - mp.log(vx(c20)/vy(c20))


def chernoff_lower_rate(d):
    """Provable lower bound on logistic+logistic Cramer-Chernoff exponent.

    E exp(t W)=(pi*t/sin pi*t)^2,
    log E exp(t W) <= pi^2*t^2/[3*(1-t^2)] for 0<t<1.
    Here d=(Delta/2)-eps>0 is the mean-threshold safety margin.
    """
    t = 3*d/(2*mp.pi**2)
    assert 0 < t < mp.mpf('0.01')
    logmgf = 2*mp.log(mp.pi*t/mp.sin(mp.pi*t))
    logmgf_up = mp.pi**2*t*t/(3*(1-t*t))
    assert logmgf < logmgf_up
    rate = t*d-logmgf_up
    assert rate > 0
    return t, rate


def report():
    D = source_delta()
    print('Delta exact-source expression; decimal:',mp.nstr(D,70))
    print('epsilon_star = Delta/2:',mp.nstr(D/2,60))
    print('Interpretation: all bounds conditional on iid latent W and a.s. |theta_j|<=eps.')
    for ratio in (mp.mpf('0'),mp.mpf(1)/8,mp.mpf(1)/4):
        eps = ratio*D
        d = D/2-eps
        t, rate = chernoff_lower_rate(d)
        print('eps_over_Delta =',mp.nstr(ratio,9),'margin=',mp.nstr(d,20),
              't=',mp.nstr(t,14),'I_lower=',mp.nstr(rate,20))
        for alpha in (mp.mpf('0.05'),mp.mpf('0.01')):
            nstar = mp.log(1/alpha)/rate
            n = int(mp.ceil(nstar))
            p_bound = mp.exp(-n*rate)
            assert p_bound < alpha
            assert mp.exp(-(n-1)*rate) > alpha
            print('  target error <',alpha,'n_sufficient=',n,
                  'real_bound=',mp.nstr(nstar,20),
                  'p_upper=',mp.nstr(p_bound,20),
                  'n_minus_1_reaches_this_bound=NO')
    eps_alias = D/2
    assert mp.almosteq(-eps_alias, -D+eps_alias)
    print('Exact alias at eps>=Delta/2: theta_A=-Delta/2, theta_B=+Delta/2.')


if __name__ == '__main__':
    report()
