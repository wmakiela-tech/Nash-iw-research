This is a classical weighted two-shot purity witness. Since p_A is NOT independent of xi, we need a globally quantified `p_A(xi)>=a0>b0>=p_B`. Then the sequence of bits under A stochastically dominates `Binomial(N,a0)` even if xi values are arbitrarily dependent between pairs; under B it is iid Bernoulli `p_B`. This is not a claim of identical Bernoulli probabilities under A.

## 2. Numerical axis-selection design, NOT a global optimum theorem

At fixed **rectangular** pulses (each theta=pi/2, duration pi/(2 Omega_max)), the three source-B squared magnetizations are:

`n_X^2=0.2724562757144595`, `n_Y^2=0.0000053516245520`, `n_Z^2=0.0023133578521287`.

A discretized semi-infinite robust linear program at 70,001 xi values in [-35,35] maximizes `min_xi (p_A(xi;w)-p_B(w))` over the probability simplex of axis weights. Numerical solution `w*≈(0.17911935,0.19744936,0.62343129)` has sampled worst-case gap ≈0.05953895, whereas equal weights have ≈0.03771741. THIS LP has neither off-grid nor infinite-detuning coverage and is **not** a proof that w* is globally optimal. Freeze a nearby rational triple `(18/100,20/100,62/100)` for certificates.

## 3. R23 theorem A — rigorous-style global rectangular-pulse certificate

Fix w=(.18,.20,.62). Source B 3×3 controlled Markovian matrices and independent 4×4 Lindblad density propagation yield

`p_B=0.5252387409109164`.

Compact interval: 3501 mpmath.iv nodes from xi=-35 to +35 at step .02, 40-digit interval precision, full source-on rotations, minimal lower node endpoint `p_A>=0.5846904500708817` at xi≈14.64. For each selected axis, Duhamel gives `|d p_A(xi)/d xi| <= Delta+t_prep+t_analysis_max = 0.5+pi/10 = 0.8141592653589793`; use the deliberately inflated `L=0.8151592653589793`. Every xi is within .01 of some sampled center, so the global **compact interval** lower bound is

`p_A(xi) >= 0.5765388574172919` for `|xi|<=35`.

Far tail: each transverse square-pulse segment has off-resonant flip amplitude no larger than `Omega/sqrt(xi^2+Omega^2)`. With `f=Omega^2/(35^2+Omega^2)=100/1325`, the two-pulse X/Y magnetizations obey `|m_X|,|m_Y|>=1-8 f` (positive at cutoff), and the one-pulse Z magnetization obeys `m_Z>=1-2 f`. Hence

`p_A(xi) >= 1/2 + 1/2[(.18+.20)(1-8f)^2 + .62(1-2f)^2] = 0.753307226771093`

for `|xi|>=35`. The combined global lower bound is the compact value 0.576538857417. Therefore

`inf_(xi in R) (p_A(xi)-p_B) >= 0.05130011650637556`.

