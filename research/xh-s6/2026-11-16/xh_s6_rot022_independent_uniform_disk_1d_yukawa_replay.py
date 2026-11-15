#!/usr/bin/env python3
"""XH-S6 ROT022 independent 1D uniform thin-disk Yukawa SHAPE toy.

NOT An et al.'s actual wafers/rotating torsion balance or experimental limits.
Original experimental source: An et al., Nat. Commun. 2026,
DOI 10.1038/s41467-026-78187-4 (original abstract verified).
"""
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss

D1, D2 = 0.654, 1.554  # invented plane-to-plane gaps, mm
RADII = (0.02, 0.10, 0.50, 1.00, 2.00)  # invented disk radii, mm

def disk_q(radius_mm, d_mm, lam_mm, n=256):
    x, w = leggauss(n)
    x, w = (x+1)/2, w/2
    # Analytic PDF in x=s/(2a) for distance s between two uniform disk points.
    pdf = (16*x/math.pi)*(np.arccos(x)-x*np.sqrt(1-x*x))
    s = np.sqrt(d_mm**2 + (2*radius_mm*x)**2)
    kernel = d_mm/s**3
    z = s/lam_mm
    return float(np.sum(w*pdf*kernel*(1+z)*np.exp(-z)) / np.sum(w*pdf*kernel))

def shape(radius_mm, lam_mm):
    return disk_q(radius_mm,D1,lam_mm)-disk_q(radius_mm,D2,lam_mm)

def max_shape(radius_mm):
    a,b = math.log(0.02),math.log(20)
    t=(math.sqrt(5)-1)/2
    x,y=b-t*(b-a),a+t*(b-a)
    fx,fy=shape(radius_mm,math.exp(x)),shape(radius_mm,math.exp(y))
    for _ in range(120):
        if fx>fy:
            b=y; y=x; fy=fx
            x=b-t*(b-a); fx=shape(radius_mm,math.exp(x))
        else:
            a=x; x=y; fx=fy
            y=a+t*(b-a); fy=shape(radius_mm,math.exp(y))
    lam=math.exp((a+b)/2)
    return lam,shape(radius_mm,lam)

if __name__=='__main__':
    point=(D2-D1)/(2*math.log(D2/D1))
    qp=lambda d,l:(1+d/l)*math.exp(-d/l)
    ref=qp(D1,point)-qp(D2,point)
    print('Original source model data NOT used; synthetic finite disk shapes only')
    for a in RADII:
        l,c=max_shape(a)
        print(f'R={a:g} mm lambda_opt={l:.9f} mm peak={c:.9f} shift_lambda_pct={100*(l/point-1):.4f} contrast_change_pct={100*(c/ref-1):.4f}')
