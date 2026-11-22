#!/usr/bin/env python3
"""M16 ROT001: independent DOUBLE-PRECISION numerical diagnostic, NOT interval proof.
The strict monotonicity result in the accompanying note is analytical.
Primary source: Geeky-S13 ROT009, Git blob 14fbe78c6371bbed80bf5b4febc0de69f4120e4c.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp


def density_logistic_sum(x):
    """Stable density of sum of two independent Logistic(0,1) variables."""
    x = np.asarray(x, dtype=float)
    y = np.abs(x)
    out = np.empty_like(y)
    small = y < 0.6
    z2 = y[small]**2
    out[small] = (1/6 - z2/60 + z2**2/1008 - z2**3/21600
                  + z2**4/532224 - 691*z2**5/9906624000
                  + z2**6/410572800 - 3617*z2**7/44460928512000)
    v = y[~small]
    q = np.exp(-v)
    out[~small] = q * ((v - 2) + (v + 2)*q) / (-np.expm1(-v))**3
    return out


def source_delta():
    mp.mp.dps = 65
    c7 = mp.cos(2*mp.pi*7/41)
    c20 = mp.cos(2*mp.pi*20/41)
    vx = lambda c: mp.mpf(82)/75 + mp.mpf(31)*c/150
    vy = lambda c: mp.mpf(17)/15 + c/6
    return float(mp.log(vx(c7)/vy(c7)) - mp.log(vx(c20)/vy(c20)))


def risk(n, nx, nt, delta):
    # Gauss-Legendre inner integral [-45,45], outer [0,8].
    # No rigorous truncation or quadrature remainder; compare two meshes.
    xg, xw = leggauss(nx)
    x, wx = 45*xg, 45*xw
    p, q = density_logistic_sum(x), density_logistic_sum(x+delta)
    hraw = np.sqrt(p*q)
    rho = np.dot(wx, hraw)
    ell = np.log(q/p)
    measure = wx*hraw/rho
    tg, tw = leggauss(nt)
    t, wt = 4*(tg+1), 4*tw
    psi = np.cos(t[:, None]*ell[None, :]) @ measure
    if min(psi) <= 0:
        raise ArithmeticError('This diagnostic expected positive psi on [0,8]')
    integral = np.dot(wt, np.power(psi, n)/(t*t+0.25))
    return np.exp(n*np.log(rho)) * integral/(2*np.pi), rho


if __name__ == '__main__':
    delta = source_delta()
    print('Delta:', format(delta, '.16f'))
    print('NOTE: double-precision diagnostic only; no IV certification')
    for n in (14538, 14539, 29082, 29083):
        a, ra = risk(n, 500, 600, delta)
        b, rb = risk(n, 800, 600, delta)
        print(f'n={n} mesh500={a:.12f} mesh800={b:.12f} diff={b-a:+.3e} '
              f'rho500={ra:.15f} rho800={rb:.15f}')
