#!/usr/bin/env python3
"""MT15 ROT005: erfc versus positive Yukawa mixtures, EXACT interval minimax.

Computes four point-source radius examples and verifies analytic extremal.
No Lee/Eot-Wash apparatus, signed-span bound, novelty, or physical inference.
"""
import json
import math
from pathlib import Path


def errf(r, ell):
    return math.erfc(r / (2.0 * ell))


def logf(r, ell):
    f = errf(r, ell)
    if f <= 0:
        raise ValueError('erfc underflow in this double precision demonstration')
    return math.log(f)


def dlogf(r, ell):
    u = r / (2.0 * ell)
    return -math.exp(-u * u) / (ell * math.sqrt(math.pi) * errf(r, ell))


def solve(a, b, ell):
    assert 0 <= a < b and ell > 0
    la, lb = logf(a, ell), logf(b, ell)
    slope = (lb - la) / (b - a)
    assert dlogf(a, ell) > slope > dlogf(b, ell)
    left, right = a, b
    for _ in range(100):
        center = (left + right) / 2.0
        if dlogf(center, ell) > slope:
            left = center
        else:
            right = center
    rstar = (left + right) / 2
    logD = logf(rstar, ell) - la - slope * (rstar - a)
    D = math.exp(logD)
    eps = math.tanh(logD / 2.0)  # (D-1)/(D+1), numerically stable
    m = -slope
    amp = math.exp(la + math.log1p(eps) + m * a)
    assert 0 < eps < 1 and m > 0 and D > 1

    def witness(r):
        return amp * math.exp(-m * r)

    nodes = (a, rstar, b)
    residuals = [witness(r) / errf(r, ell) - 1.0 for r in nodes]
    assert abs(residuals[0] - eps) < 2e-13
    assert abs(residuals[1] + eps) < 2e-13
    assert abs(residuals[2] - eps) < 2e-13

    # Verify analytically attained sup numerically on dense independent grid.
    errors = [abs(witness(a + (b-a)*k/3000) / errf(a+(b-a)*k/3000, ell) - 1.0)
              for k in range(3001)]
    assert max(errors) <= eps + 1e-12
    assert abs(max(errors) - eps) < 2e-13

    # 3-radius ROT003 bound must be no larger than the entire interval value.
    mid = (a+b)/2
    logDmid = logf(mid,ell) - la - slope*(mid-a)
    eps_mid = math.tanh(logDmid/2)
    assert eps_mid <= eps + 2e-15

    # Synthetic random-free positive triple mixture checks of theorem.
    for k in range(61):
        rates = [0.001+0.0004*k, 0.01+0.0003*k, 0.12]
        weights = [0.02+0.004*k, 0.1+0.005*k, 0.2]
        def mix(r):
            return sum(w*math.exp(-rate*r) for w,rate in zip(weights,rates))
        actual = max(abs(mix(r)/errf(r,ell)-1.0) for r in nodes)
        assert actual + 1e-12 >= eps

    return dict(ell_um=ell,a_um=a,b_um=b,
                r_worst_um=rstar,point_source_f_endpoint_a=errf(a,ell),
                point_source_f_endpoint_b=errf(b,ell),
                D_max=D,three_radius_midpoint_lower_bound=eps_mid,
                sharp_continuous_interval_relative_error=eps,
                optimal_single_exp_mass_per_um=m,
                optimal_single_exp_decay_length_um=1/m,
                optimal_single_exp_prefactor=amp,
                equioscillation_relative_residuals=residuals,
                dense_grid_nodes_checked=len(errors),
                positive_mixture_tests=61)


def main():
    inputs = [(52.,108.,40.),(52.,148.,40.),(52.,108.,30.),
              (52.,108.,50.),(0.,200.,40.)]
    examples = [solve(*x) for x in inputs]
    data = dict(status='MATHEMATICAL_PROOF_ANALYTIC_NUMERIC_CHECK_PASS',
                type='ERFC_NORMALIZED_POINT_SOURCE_DEFICIENCY_ONLY',
                not_physical_bound=True,
                description='Positive Yukawa mixture (nonnegative coefficients, rates); signed mixtures excluded',
                model='f(r)=erfc(r/(2ell)); sup relative error on compact [a,b]',
                formula='inf_error=(D-1)/(D+1); D=max(f/h), h=geometric endpoint chord',
                examples=examples)
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    main()
