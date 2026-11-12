#!/usr/bin/env python3
"""M15 ROT002: exact stdlib Fraction checks for four-axis correlation minimax.

Proof (global minimax via proper Gaussian priors) is in the accompanying MD;
this program is a deterministic finite algebra/negative-control verifier, NOT
an empirical sensor simulation and NOT an independent referee.
"""
from fractions import Fraction as F
import hashlib
import json

A = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
I = tuple(tuple(F(i == j) for j in range(4)) for i in range(4))
J = tuple(tuple(F(1) for _ in range(4)) for _ in range(4))
P = tuple(tuple(I[i][j] - J[i][j] / 4 for j in range(4)) for i in range(4))
Cworst = tuple(tuple(F(4, 3) * P[i][j] for j in range(4)) for i in range(4))
Ccommon = J

def transpose(a):
    return tuple(zip(*a))

def mm(a, b):
    bt = transpose(b)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt) for row in a)

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

def gram_error_cov(C, sigma2=F(1)):
    # Estimator L=A^T/4; Cov(L epsilon)=sigma2 * A^T C A / 16.
    atca = mm(mm(transpose(A), C), A)
    return tuple(tuple(sigma2 * q / 16 for q in row) for row in atca)

def risk(C, sigma2=F(1)):
    return trace(gram_error_cov(C, sigma2))

def scalar_summ(C):
    return sum(q for row in C for q in row)

def eqcorr(rho):
    return tuple(tuple(F(1) if i == j else rho for j in range(4)) for i in range(4))

def fmt(q):
    q = F(q)
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)

# Geometric identity of tetrahedral axes.
assert mm(transpose(A), A) == tuple(tuple(4 * F(i == j) for j in range(3)) for i in range(3))
assert mm(A, transpose(A)) == tuple(tuple(4 * I[i][j] - J[i][j] for j in range(4)) for i in range(4))
assert all(sum(A[i][j] for i in range(4)) == 0 for j in range(3))
assert mm(P, P) == P
assert mm(P, A) == A
assert all(Cworst[i][i] == 1 for i in range(4))
assert all(sum(Cworst[i][j] for j in range(4)) == 0 for i in range(4))
assert all(sum(Ccommon[i][j] for j in range(4)) == 4 for i in range(4))

cases = {
    "independent": I,
    "max_contrast_anticorrelation_rho_minus_one_third": Cworst,
    "perfect_common_mode": Ccommon,
    "equicorrelated_rho_plus_one_half": eqcorr(F(1, 2)),
    "equicorrelated_rho_minus_one_sixth": eqcorr(F(-1, 6)),
}
expected = {
    "independent": F(3, 4),
    "max_contrast_anticorrelation_rho_minus_one_third": F(1),
    "perfect_common_mode": F(0),
    "equicorrelated_rho_plus_one_half": F(3, 8),
    "equicorrelated_rho_minus_one_sixth": F(7, 8),
}
checks = 0
for name, C in cases.items():
    assert risk(C) == expected[name]
    checks += 1
    assert risk(C) == 1 - scalar_summ(C) / 16
    checks += 1
    assert all(C[i][i] == 1 for i in range(4))
    checks += 1
    rho = C[0][1]
    assert all(C[i][j] == (1 if i == j else rho) for i in range(4) for j in range(4))
    assert 1 + 3*rho >= 0 and 1-rho >= 0
    checks += 1

assert risk(I) == F(3, 4)
assert risk(Cworst) == F(1)
assert gram_error_cov(Cworst) == tuple(tuple(F(i == j, 3) for j in range(3)) for i in range(3))
assert gram_error_cov(I) == tuple(tuple(F(i == j, 4) for j in range(3)) for i in range(3))
assert risk(Cworst) / risk(I) == F(4, 3)
m, N, sigma2 = 100, 400, F(1)
assert risk(I, sigma2)/m == F(3, N)
assert risk(Cworst, sigma2)/m == F(4, N)
checks += 10

summary = {
    "artifact_id": "IW_M15_ROT002_TETRAHEDRAL_UNKNOWN_WITHIN_GROUP_CORRELATION_MINIMAX_001_20261112",
    "checked_cases": {name: {
        "rho": fmt(C[0][1]),
        "one_group_total_risk_per_sigma2": fmt(risk(C)),
        "oneT_C_one": fmt(scalar_summ(C)),
    } for name, C in cases.items()},
    "m": m,
    "N": N,
    "independent_risk_example": fmt(risk(I, sigma2)/m),
    "robust_worst_risk_example": fmt(risk(Cworst, sigma2)/m),
    "risk_inflation": fmt(risk(Cworst)/risk(I)),
    "checks_passed": checks,
    "status": "EXACT_FRACTION_ALGEBRA_PASS_NOT_PROOF_OF_MINIMAX_NOT_PHYSICS",
}
serialized = json.dumps(summary, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
print(serialized, end="")
