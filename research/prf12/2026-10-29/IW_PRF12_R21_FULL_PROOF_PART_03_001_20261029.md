## 2. Theorem R21.1 — source-GATED finite pulses retain R20 EXACT test; overhead shifts optimal Δ

S1 source OFF during perfect finite gates implies the ideal R20 output distribution exactly, since only free exposure induces A phase or B dephasing. Thus

 p_A=3/4 (every ξ), p_B=1/2+e^(−2q)/4.    (R21.3)

Each pair consumes two π/2 preparations and two π/2 analysis rotations. Let r=Ωmax/γ, d=γ(t_d+t_reset), and a=π/r+d. Dimensionless pair time γT_pair=2(q+a). For a fixed q, the exact likelihood ratio is a Bernoulli test. With p_A>p_B and equal priors, choose A iff K≥k, where

 k=ceil[N log((1−p_B)/(1−p_A))/{log(p_A/p_B)+log((1−p_B)/(1−p_A))}].

Errors are BinomCDF(k−1;N,p_A) and BinomSF(k−1;N,p_B). Define Bernoulli Chernoff information C(q)=−log min_{s∈[0,1]}[p_A^s p_B^(1−s)+(1−p_A)^s(1−p_B)^(1−s)]. The long-series information *per physical time* is C(q)/[2(q+a)]. At an interior optimum q* the stationary condition is C'(q*)(q*+a)=C(q*), not simply q*=.5895 from R20's zero-overhead model.

For **fixed** t_d=t_reset=.05/γ, accurate rectangular source-gated gates with Ω=Ωmax, exact finite-N classification and numeric scalar Chernoff/time minimization give:

| Ωmax/γ | a=γ prep+analysis+deadtime PER SHOT | q*_Chernoff/time | minimal N, BOTH conditional errors <5% at q* | γ total clock for that N |
|---:|---:|---:|---:|---:|
| 5 | .728319 | 1.021540 | 55 | 192.4844 |
| 10 | .414159 | .898253 | 56 | 146.9902 |
| 20 | .257080 | .814946 | 62 | 132.9312 |
| 50 | .162832 | .751874 | 66 | 120.7412 |
| 100 | .131416 | .727443 | 66 | 113.3694 |

Here q* optimizes CHERNOFF/time, not the discrete finite-sample total time globally. N is minimal at that chosen q*, not universally minimized over q. The source-switching power and source reset law are **unmodeled resources**; do not assert these numbers for an always-on source without further physical control.

