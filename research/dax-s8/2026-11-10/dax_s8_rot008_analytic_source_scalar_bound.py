#!/usr/bin/env python3
"""DAX-S8 ROT008: exact analytic high-COM source-scalar DPP fraction bounds.
NOT full QED differential; NOT a physical event or deposition estimate.
CRPropa3-data calc_electromagnetic.py blob 030af585f62357e4522f64f7a7daa81c635b20d3.
"""
from decimal import Decimal as D, localcontext
from math import comb, factorial
import json

def pi_chudnovsky(terms=7):
    total=D(0)
    for k in range(terms):
        total += D((-1)**k * factorial(6*k)*(13591409+545140134*k)) / (
            D(factorial(3*k)*factorial(k)**3*640320**(3*k)))
    return D(426880)*D(10005).sqrt()/total

def zeta3_apery(terms=100):
    return D(5)/2*sum(
        (D(1) if n%2 else D(-1))/(D(n)**3*D(comb(2*n,n)))
        for n in range(1,terms+1))

def main():
    with localcontext() as ctx:
        ctx.prec=58
        E=D('1436.554')*1000
        T=D('0.07818527068831995')
        me=D('0.51099895')
        Scut=D(4000)**2
        s0=16*me**2
        a=Scut/(4*E*T)
        chi=s0/(4*E*T)
        rho=s0/Scut
        z3=zeta3_apery()
        pi=pi_chudnovsky()
        assert abs(z3-D('1.20205690315959428539973816151144999076'))<D('1e-35')
        assert abs(pi-D('3.14159265358979323846264338327950288419716939937510'))<D('1e-43')
        m=12
        # Constant-sigma high COM collision weight with isotropic flux 2u:
        B=sum((-D(n)*a).exp()*(a/D(n)**2+D(1)/D(n)**3)
              for n in range(1,m+1))/z3
        remainder=(a+1)*(-D(m+1)*a).exp()/(1-(-a).exp())/z3
        assert remainder<D('1e-140')
        # Bernoulli (1-v)^6>=1-6v plus thresholded zero below s0.
        D_lower=1-chi*pi*pi/z3
        # For s>=Scut the source sigma ratio is in [(1-rho)^6,1].
        P_lower=B*(1-rho)**6
        P_upper=(B+remainder)/D_lower
        number_tail=sum((-D(n)*a).exp()*
            (a*a/D(n)+2*a/D(n)**2+2/D(n)**3)
            for n in range(1,m+1))/(2*z3)
        assert D_lower> D('0.9999')
        assert D('1.03e-14')<P_lower<P_upper<D('1.05e-14')
        assert P_upper<number_tail
        print(json.dumps({
            'status':'PASS_ANALYTIC_WEIGHTED_DPP_RATE_BOUND',
            'E_gamma_GeV':'1436.554','T_gamma_MeV':str(T),
            'a':str(a),'chi':str(chi),'rho':str(rho),
            'B_constant_sigma_angular_weight':str(B),
            'D_scalar_total_lower_bound':str(D_lower),
            'P_source_scalar_lower':str(P_lower),
            'P_source_scalar_upper':str(P_upper),
            'Planck_photon_number_tail':str(number_tail),
            'angular_weight_divided_by_number_tail':str(B/number_tail),
            'series_remainder_upper':str(remainder),
            'scope':'Only scalar CRPropa collision weight and necessary sqrt(s)>=4GeV COM cut; NOT full QED rate, 4-lepton differential or physical deposition.'
        },indent=2,sort_keys=True))

if __name__=='__main__':
    main()
