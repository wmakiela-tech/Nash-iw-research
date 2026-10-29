 \[\Pr_A(K<k)\le\Pr\{\operatorname{Bin}(N,a)<k\},\quad
   \Pr_B(K\ge k)\le\Pr\{\operatorname{Bin}(N,b)\ge k\}.\tag{R22.6}\]

Choose **N=3300 pairs**, k=1851. Declare A if K≥1851; else declare B. Exact numerical evaluation of the two *ordinary binomial tail upper bounds* gives

 \[ \boxed{\Pr_A(\text{false B})\le.045655862283,
 \qquad\Pr_B(\text{false A})\le.044205382212.}\tag{R22.7}\]

These tail values were evaluated with scipy.stats.binom and can be checked independently in any binomial implementation. Their separation from .05 is sufficient to tolerate machine-precision evaluation error. The inequalities (R22.6) are algebraic couplings, not assumptions of iid ξ_j. The number 3300 is a simple robust **achievable** witness, not proof that a smaller N is impossible with better experimental settings or more informative labels.

Resource ledger: 3300 PAIRS = **6600 fresh preparations and Z readouts**; each shot consumes Δ+t plus an extra t for X/Y analysis. Max measured free-plus-drive physical time per pair is 2(Δ+2t)≈1.6283185307/γ and max total across 3300 pairs is ≈5373.45115137/γ. Mean free-plus-drive time given fair trits is 2[Δ+t+(2/3)t]≈1.5235987756/γ per pair, i.e. ≈5027.87595947/γ in expectation. **Unknown positive terminal readout/reset durations must be added** to any physical hardware claim, and the source must remain static across those two shots of each A pair. Hardware cost remains far larger than the idealized true XYZ projector fixture in R21 (185 pairs), so the advance is proof of robustness/implementability of the finite analysis pulses, not resource efficiency.

## 6. Reproducibility, falsifiers, external audits and status

The full single-file Python reproducer uses mpmath.iv with 40 digits to enclose **3,501 grid points**, analytic interpolation .815*.01, analytic high-detuning bound, a 65th-order three-dimensional Bloch Lindbladian series with explicit remainder and 10^-35 interval inflation, and independent noninterval NumPy/SciPy Bloch values. A second independent script separately computes a 2×2 source-A density-matrix evolution and a 4×4 source-B Lindblad superoperator: for twelve hidden frequencies and the exact B fixture, both routes agree to <1e-12. Exact binomial tails are included. No Monte Carlo or parameter fitting is used.

