"""PRF13 ROT001: exact copula/readout calibration diagnostic (Python stdlib only).
Public, synthetic algebraic counterexample. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.
"""
from fractions import Fraction as F
from itertools import product

P0 = F(99, 100)
P1 = F(247, 4600)  # R34 reference comparator 3705/69000
Z_ALPHA, Z_BETA = F(347, 1000), F(18, 1000)
OMEGA_Z = F(62, 100)


def joint_law(u, v, t):
    """P(++),P(+-),P(-+),P(--) with registered-plus marginals u,v."""
    lo, hi = max(F(0), u + v - 1), min(u, v)
    assert lo <= t <= hi
    q = (t, u - t, v - t, 1 - u - v + t)
    assert sum(q) == 1 and all(x >= 0 for x in q)
    assert q[0] + q[1] == u and q[0] + q[2] == v
    return q


def signed_score(q, alpha=Z_ALPHA, beta=Z_BETA):
    return alpha * q[0] + beta * q[3]


def pair_couplings(u, v):
    return {
        'frechet_min': joint_law(u, v, max(F(0), u + v - 1)),
        'independent': joint_law(u, v, u * v),
        'shared_uniform': joint_law(u, v, min(u, v)),
    }


def main():
    # Every input pair is calibrated to the SAME one-shot conditional p0/p1.
    for z in product((0, 1), repeat=2):
        u, v = (P0 if bit == 0 else P1 for bit in z)
        laws = pair_couplings(u, v)
        expected_width = (Z_ALPHA + Z_BETA) * (min(u, v) - max(F(0), u + v - 1))
        observed_width = signed_score(laws['shared_uniform']) - signed_score(laws['frechet_min'])
        assert observed_width == expected_width
        assert all(joint_law(u, v, law[0]) == law for law in laws.values())

    # Identical reference marginals for the ideal (--)-pair, different joint-score law.
    cases = pair_couplings(P1, P1)
    independent = signed_score(cases['independent'])
    shared = signed_score(cases['shared_uniform'])
    difference = shared - independent
    assert difference == (Z_ALPHA + Z_BETA) * P1 * (1 - P1)
    assert independent == F(72449017, 4232000000)
    assert shared == F(164063, 4600000)
    assert difference == F(78488943, 4232000000)

    # This input-conditional deviation in the Z arm (alone) exceeds the
    # numerical score-response budget for the inherited R33 a,b decision.
    # It does NOT establish that this input distribution occurs in R31's source.
    budget = min(F('0.3106993896688963') - F('0.2995'),
                 F('0.2828') - F('0.27161358975207756'))
    weighted_deviation = OMEGA_Z * difference
    assert weighted_deviation > budget

    # For arbitrary ideal-pair mixture mu, a score-only calibration bound
    # |g(z)-g_nom(z)| <= eps entails |sum mu(z)(g-g_nom)| <= eps.
    nominal, correlated = [], []
    for z in product((0, 1), repeat=2):
        u, v = (P0 if bit == 0 else P1 for bit in z)
        laws = pair_couplings(u, v)
        nominal.append(signed_score(laws['independent']))
        correlated.append(signed_score(laws['shared_uniform']))
    eps = max(abs(x - y) for x, y in zip(nominal, correlated))
    for weights in product((F(0), F(1, 4), F(1, 2), F(1)), repeat=4):
        if sum(weights) == 1:
            dev = abs(sum(m * (x - y) for m, x, y in zip(weights, nominal, correlated)))
            assert dev <= eps

    print('P1=', P1, 'decimal=', float(P1))
    print('Z |-- > independent score=', independent, 'decimal=', float(independent))
    print('Z |-- > shared score=', shared, 'decimal=', float(shared))
    print('exact score difference=', difference, 'decimal=', float(difference))
    print('max Frechet score width at (--)=', (Z_ALPHA+Z_BETA)*P1)
    print('R33/R34 inherited score-response budget=', float(budget))
    print('Z-weighted countermodel shift=', float(weighted_deviation))
    print('exact tests: PASS (not a physical demonstration)')


if __name__ == '__main__':
    main()
