#!/usr/bin/env python3
"""MT15 ROT003. Exact mathematical gate + illustrative floating arithmetic.

Source model only: erfc(r/(2*ell)) versus nonnegative exponential mixtures.
No Eot-Wash apparatus source, physical inference, or novelty claim.
"""
import json, math


def solve3(A, b):
    A = [list(map(float, row)) + [float(y)] for row, y in zip(A, b)]
    for i in range(3):
        k = max(range(i, 3), key=lambda j: abs(A[j][i]))
        A[i], A[k] = A[k], A[i]
        piv = A[i][i]
        assert abs(piv) > 1e-14, "singular demonstration design"
        for q in range(i, 4):
            A[i][q] /= piv
        for j in range(3):
            if j != i:
                c = A[j][i]
                for q in range(i, 4):
                    A[j][q] -= c*A[i][q]
    return [A[i][3] for i in range(3)]


def certificate(ell_um, xyz_um):
    x,y,z = xyz_um
    assert ell_um > 0 and x >= 0 and x < y < z and abs(2*y-x-z) < 1e-10
    f = lambda r: math.erfc(r/(2*ell_um))
    fx,fy,fz = map(f, xyz_um)
    q = math.sqrt(fx*fz)/fy
    eps = (1-q)/(1+q)
    assert 0 < q < 1 and eps > 0

    # A single positive exponential attains the SHARP minimax relative error
    # at the three points, alternating (+eps,-eps,+eps).
    mass = math.log(fx/fz)/(z-x)
    amp = (1+eps)*fx*math.exp(mass*x)
    gg = [amp*math.exp(-mass*r) for r in xyz_um]
    rel = [a/b-1 for a,b in zip(gg,[fx,fy,fz])]
    assert max(abs(rel[i]-v) for i,v in enumerate([eps,-eps,eps])) < 1e-12

    # Positive mixtures satisfy g(y)^2 <= g(x)g(z), by Cauchy-Schwarz.
    # Test 101 explicit two-/three-component positive mixtures.
    for k in range(101):
        rates = [0.005+0.0001*k, 0.027+0.00007*k, 0.08]
        weights = [0.2+0.003*k, 0.1+0.004*k, 1.3]
        G = [sum(w*math.exp(-m*r) for w,m in zip(weights,rates)) for r in xyz_um]
        assert G[1]**2 <= G[0]*G[2]*(1+2e-14)
        assert max(abs(G[i]/(fx,fy,fz)[i]-1) for i in range(3)) >= eps-2e-13

    # Negative control: signed linear mixtures CAN interpolate all three
    # numbers, so this proof cannot obstruct unrestricted linear span.
    signed_rates = [0.0, 1/ell_um, 2/ell_um]
    A = [[math.exp(-m*r) for m in signed_rates] for r in xyz_um]
    signed = solve3(A,[fx,fy,fz])
    check = [sum(w*math.exp(-m*r) for w,m in zip(signed,signed_rates)) for r in xyz_um]
    assert max(abs(a-b) for a,b in zip(check,[fx,fy,fz])) < 1e-12
    assert min(signed) < -1e-9, "positive-cone contradiction failed"
    return dict(ell_um=ell_um, xyz_um=xyz_um, f_values=[fx,fy,fz],
                q=q, sharp_minimax_relative_error=eps,
                attained_by_single_exp_mass_per_um=mass,
                attained_by_single_exp_decay_length_um=1/mass,
                attained_by_single_exp_amplitude=amp,
                relative_residuals=rel,
                signed_negative_control_rates=signed_rates,
                signed_negative_control_weights=signed,
                positive_mixture_trials=101)

if __name__ == '__main__':
    out = [certificate(*data) for data in [
        (40.0,(52.0,80.0,108.0)),
        (40.0,(52.0,100.0,148.0)),
        (50.0,(52.0,80.0,108.0)),
        (30.0,(52.0,80.0,108.0))]]
    print(json.dumps({"status":"PASS", "host":"pointwise_positive_Yukawa_exponential_cone",
                      "not":"real_EotWash_transfer_or_bound", "cases":out},indent=2,ensure_ascii=False))
