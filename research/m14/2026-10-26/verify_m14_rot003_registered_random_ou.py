#!/usr/bin/env python3
"""M14 ROT003: random registered OU sampling versus deterministic near-alias.
Standard-library independent quadrature/control, no NASH private data.
This script is an arithmetic falsifier, not a theorem prover.
"""
import json
import math

A, B = 0.75, 1.25
L = B - A
Z = (math.exp(2 * B) - math.exp(2 * A)) / 2 - L
M = 1.0 / math.expm1(2 * A)

def density(t):
    return math.expm1(2 * t) / Z

def exact_random_K(delta):
    if delta == 0:
        return 0.0
    return (2.0 / Z) * (L - (math.sin(delta * B) - math.sin(delta * A)) / delta)

def numerical_K(delta):
    return simpson(lambda t: density(t) * 2 * (1 - math.cos(delta * t)) /
                   math.expm1(2 * t), 24000)

def conditional_affinity(delta):
    def integrand(t):
        x = (1 - math.cos(delta * t)) / (2 * math.expm1(2 * t))
        return density(t) / (1 + x)
    return simpson(integrand, 24000)

def simpson(f, n):
    assert n % 2 == 0
    h = L / n
    s = f(A) + f(B)
    for j in range(1, n):
        s += (4 if j % 2 else 2) * f(A + j * h)
    return s * h / 3

def deterministic_K(delta, gaps):
    return sum(2 * (1 - math.cos(math.remainder(delta * t, 2 * math.pi))) /
               math.expm1(2 * t) for t in gaps)

def run():
    assert abs(simpson(density, 2000) - 1) < 5e-13
    fisher = 2 * (B**3 - A**3) / (3 * Z)
    fisher_fdiff = 2 * exact_random_K(0.001) / 0.001**2
    assert abs(fisher - fisher_fdiff) < 2e-7, (fisher, fisher_fdiff)
    scenarios = []
    for delta in [0.05, 0.7, 2., 10., 2 * math.pi * 12,
                  2 * math.pi * 70, 2 * math.pi * 408]:
        k = exact_random_K(delta)
        kn = numerical_K(delta)
        affinity = conditional_affinity(delta)
        tv_floor = 1 - affinity
        floor1 = 2 * L / (7 * Z) * min((delta * L / 2)**2, 1)
        floor2 = k / (4 * (1 + M))
        assert abs(k - kn) < 3e-8, (delta,k,kn)
        assert k >= floor1 - 1e-11, (delta,k,floor1)
        assert tv_floor >= floor2 - 1e-11, (delta,tv_floor,floor2)
        assert 0 < tv_floor < 1
        assert k <= 4 * L / Z + 1e-12
        scenarios.append(dict(delta=delta,KL_exact=k,KL_simpson=kn,
                              affinity=affinity,TV_lower=tv_floor,
                              KL_global_lower=floor1,TV_cert_lower=floor2))
    distant = []
    for q in (12,70,408,2378):
        d = 2 * math.pi * q
        known = deterministic_K(d,[1,math.sqrt(2)])
        random = exact_random_K(d)
        assert abs(random - 2 * L / Z) < 1e-10
        distant.append(dict(q=q, delta=d, KL_deterministic=known,
                            KL_randomized_joint=random))
    assert all(distant[i]["KL_deterministic"] >
               distant[i+1]["KL_deterministic"] for i in range(3))
    assert distant[-1]["KL_deterministic"] < 1e-6
    result = dict(
        id="M14_ROT003_RANDOM_TIMES_OU_ANNEALED_QUENCHED_001_20261026",
        status="DETERMINISTIC_NUMERIC_CONTROLS_PASS_NOT_A_PROOF",
        distribution="observed IID gap on [0.75,1.25], p(t)=(e^(2t)-1)/Z",
        Z=Z, high_frequency_KL_limit=2*L/Z,
        global_KL_ceiling_one_gap=4*L/Z,
        single_gap_fisher=fisher, fisher_small_delta=fisher_fdiff,
        scenarios=scenarios,
        deterministic_versus_randomized=distant,
        scope="stationary isotropic OU, known clock, observed full state",
        novelty="none", physics="none", canonical="no",
        BW_ingest="unknown")
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__ == "__main__":
    run()
