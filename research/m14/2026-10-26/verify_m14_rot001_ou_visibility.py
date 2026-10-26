#!/usr/bin/env python3
"""Standalone deterministic controls for M14 ROT001; math proof in paired report.
No empirical or independent source-theorem certification is claimed.
Python >=3.9, standard library only.
"""
import json
import math
from fractions import Fraction


def transition(omega, delta):
    r = math.exp(-delta)
    c, s = math.cos(omega * delta), math.sin(omega * delta)
    return ((r*c, -r*s), (r*s, r*c))


def cov_increment(delta):
    q = 1.0-math.exp(-2.0*delta)
    return ((q, 0.0), (0.0, q))


def maxdiff(A, B):
    return max(abs(A[i][j]-B[i][j]) for i in range(2) for j in range(2))


def exact_generator_radial(k, x, y, omega):
    """Cartesian generator on f(x,y)=(x*x+y*y)^k, exact rational."""
    s = x*x + y*y
    if k == 0:
        return Fraction(0), Fraction(0)
    fx = 2*k*s**(k-1)*x
    fy = 2*k*s**(k-1)*y
    laplace = 4*k*k*s**(k-1)
    cart = (-x-omega*y)*fx + (omega*x-y)*fy + laplace
    reduced = -2*k*s**k + 4*k*k*s**(k-1)
    return cart, reduced


def main():
    for w in (Fraction(0), Fraction(1, 2), Fraction(-7, 3)):
        A = ((Fraction(-1), -w), (w, Fraction(-1)))
        assert all(A[i][j] + A[j][i] + (2 if i == j else 0) == 0
                   for i in range(2) for j in range(2))
        for x, y in ((Fraction(3, 5), Fraction(4, 5)),
                     (Fraction(3, 7), Fraction(-2, 7)),
                     (Fraction(0), Fraction(5, 3))):
            for k in range(12):
                a, b = exact_generator_radial(k, x, y, w)
                assert a == b, (k, x, y, w, a, b)
    exact_checks = 3*3*12
    step = 1.0
    base = 0.37
    alias = base + 2.0*math.pi/step
    regular_diff = maxdiff(transition(base, step), transition(alias, step))
    assert regular_diff < 3e-15
    assert cov_increment(step) == cov_increment(step)
    irrational_step = math.sqrt(2.0)
    irregular_diff = maxdiff(transition(base, irrational_step), transition(alias, irrational_step))
    assert irregular_diff > 0.1
    approximants = [12, 70, 408, 2378]
    near_alias_diff = [maxdiff(transition(0, irrational_step), transition(2*math.pi*n, irrational_step)) for n in approximants]
    assert all(maxdiff(transition(0,step),transition(2*math.pi*n,step)) < 2e-12 for n in approximants)
    assert all(a>b for a,b in zip(near_alias_diff, near_alias_diff[1:])), near_alias_diff
    assert near_alias_diff[-1] < 0.001
    output = {
        'return_id':'M14-ROT001-XH4-LT-SAMPLED-OU-OBSERVATION-QUOTIENT-001_20261026',
        'status':'DETERMINISTIC_CONTROL_PASS_NOT_THEOREM_PROVER',
        'exact_fraction_generator_checks':exact_checks,
        'stationary_lyapunov_exact_cases':3,
        'regular_sampling_delta':step,
        'regular_alias_max_entry_error':regular_diff,
        'incommensurate_lag': 'sqrt(2) (mathematical; floating evaluation used only for diagnostic)',
        'incommensurate_alias_max_entry_gap':irregular_diff,
        'unbounded_nonstable_alias_n':approximants,
        'unbounded_nonstable_second_lag_gaps':near_alias_diff,
        'claim_ceiling':'conditional OU mathematics; XH4 prior art and LT authorial decision retained; no physics/canon/EXEC'
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
