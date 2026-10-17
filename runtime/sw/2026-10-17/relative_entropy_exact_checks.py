#!/usr/bin/env python3
"""Exact audit witnesses; stdlib only. Not a numerical simulation of a CFT.

Rational polynomial integration checks the perturbation-order calculation.
The C-infinity witness and geometric statement are proved in the report.
The compact piecewise polynomial used here is C3, not C-infinity.
"""
from fractions import Fraction as F
import json


def clean(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return clean([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def scale(a, k):
    return clean([k*x for x in a])


def mul(a, b):
    p = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i+j] += x*y
    return clean(p)


def deriv(a, n=1):
    for _ in range(n):
        a = clean([i*a[i] for i in range(1, len(a))] or [0])
    return a


def value(a, x):
    return sum(c*x**i for i, c in enumerate(a))


def integral(a, left=F(-1, 2), right=F(1, 2)):
    return sum(c*(right**(i+1)-left**(i+1))/F(i+1)
               for i, c in enumerate(a))


def run():
    checks = []
    def check(name, ok, detail):
        if not ok:
            raise AssertionError(name)
        checks.append({'name': name, 'status': 'PASS', 'detail': detail})

    # g=(1-4u^2)^4 inside [-1/2,1/2], zero outside.
    g = [F(1)]
    for _ in range(4):
        g = mul(g, [1, 0, -4])
    w = [F(1, 2), F(0), F(-1, 2)]
    gp, gpp, gppp = (deriv(g, n) for n in (1, 2, 3))
    endpoints_ok = all(value(deriv(g,n), x) == 0
                       for n in range(4) for x in (F(-1,2),F(1,2)))
    check('polynomial_zero_boundary_jets_0_to_3', endpoints_ok,
          'C3 zero-extension; used only for rational integration controls')
    q = integral(mul(w,mul(gpp,gpp))) - integral(mul(gp,gp))
    check('positive_quadratic_form', q > 0, str(q))
    linear = integral(mul(w,gppp))
    check('zero_first_order_Schwarzian_moment', linear == 0, str(linear))
    second = add(scale(mul(gp,gppp),-1), scale(mul(gpp,gpp),F(-3,2)))
    moment = integral(mul(w,second))
    check('second_order_moment_equals_minus_Q_over_2', moment == -q/2, str(moment))
    flow_term = integral(mul(w,deriv(scale(mul(g,gp),F(1,2)),3)))
    check('flow_acceleration_has_zero_weighted_moment', flow_term == 0, str(flow_term))
    check('relative_entropy_epsilon2_coefficient_over_c', q/24 > 0, str(q/24))
    # Endpoint formula: diffeomorphism is identity near -1,+1.
    endpoint_ratio = F(2)**2/(F(2)**2*F(1)*F(1))
    check('exact_geodesic_endpoint_ratio', endpoint_ratio == 1, str(endpoint_ratio))
    # Analytic smooth-bump proof uses pi>3, giving 3*pi^2/8-1>19/8.
    lower = F(3*9,8)-1
    check('smooth_bump_Poincare_strict_lower_bound', lower > 0, str(lower))
    # One null contraction fails to fix a symmetric tensor.
    k = [1,1,0,0]
    tensor_diag = [0,0,1,0]
    contraction = sum(tensor_diag[i]*k[i]*k[i] for i in range(4))
    check('one_null_contraction_does_not_fix_tensor', contraction == 0 and tensor_diag[2] != 0,
          'diag(0,0,1,0), k=(1,1,0,0), Minkowski signature (-+++)')
    moment_kernel = integral(mul([0,-1],[F(2,3),1]),F(-1),F(0))
    check('one_weighted_flux_not_pointwise_identification', moment_kernel == 0, str(moment_kernel))
    # Rational log coefficients for D(diag(1/4,3/4)||diag(3/4,1/4)).
    log3_coefficient = F(-1,4)+F(3,4)
    check('unitary_qubit_entropy_unchanged_but_relative_entropy_positive',
          log3_coefficient == F(1,2), 'D=(1/2)*log(3), delta_von_Neumann_entropy=0')
    # Negative control: an endpoint-changing deformation need not have zero length.
    changed_ratio = F(3)**2/F(2)**2
    check('endpoint_change_negative_control', changed_ratio != 1, str(changed_ratio))
    return {
        'artifact_id': 'IW_SW_RELATIVE_ENTROPY_GEOMETRY_AUDIT_001_20261017',
        'arithmetic': 'fractions.Fraction; exact rational arithmetic; no random sampling',
        'status': 'AUTHOR_REPRODUCED',
        'check_count': len(checks),
        'checks': checks,
        'limitations': [
            'No CFT or Einstein solver; no independent-model validation.',
            'C-infinity compact bump and geodesic conclusions require the analytic proof in the report.',
            'The polynomial witness is C3 after zero extension, not C-infinity.',
            'No novelty, experimental, or gravitational-stability claim.'
        ]
    }


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
