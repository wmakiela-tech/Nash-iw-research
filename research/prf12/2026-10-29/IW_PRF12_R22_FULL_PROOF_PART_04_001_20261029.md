for each unit-norm initial vector; a 10^-35 scalar interval inflation is enormously larger than cumulative two-gate truncation errors. The free interval multiplies transverse components by e^-0.5, computed with directed interval arithmetic. The resulting value is enclosed around p_B=0.54579583086519... and rigorously satisfies p_B<.5460. A second implementation using scipy.linalg.expm is a NONRIGOROUS independent cross-check, not the proof of the bound.

The combined difference is at least .5753−.5460=.0293 for all real xi. The claim uses the correctness of the interval arithmetic dependency; external referee is pending.

## 4. Theorem R22.2 — exact phase independence remains impossible for any FIXED finite bounded rectangular-composite control with direct Z readout

The uniform POSITIVE CONTRAST in R22.1 must not be misreported as restoration of R21's exact phase-independent p_A=2/3 identity. Indeed:

 - At ξ=0 the declared three-axis calibrated pulses give p_A(0)=2/3.
 - For |ξ|→∞ and any FIXED finite sequence of square transverse pulses with amplitudes bounded independently of ξ, each pulse has Z-flip transition amplitude O(Ω_max/|ξ|), hence an arbitrary fixed finite concatenation cannot significantly change the initial Z population. All free Z stages are diagonal. The prepared state approaches |0><0| in Z-population and EVERY Z-terminal analysis channel approaches the original Z readout in that same large-|ξ| limit.
 - Therefore the equal-sign event has p_A(ξ)→1 (while its value at ξ=0 is 2/3).

Thus no fixed finite bounded piecewise-constant sequence of transverse pulses meeting these assumptions can reproduce a CONSTANT 2/3 purity-parity response for every ξ∈R with only terminal computational Z measurement. **Scope:** the argument is not a general quantum-control no-go for infinitely many pulses, unbounded/amplitude-adaptive ξ-dependent controls, independently available orthogonal projective detectors, or additional quantum/measurement resources. It explains why robust *inequality* rather than exact phase invariance is the correct positive target under the declared drive restrictions.

## 5. Theorem R22.3 — finite sample control for arbitrary between-pair source persistence

For each pair j, the source-A frequency ξ_j may have ANY dependence on earlier values, no distribution assumption, including perfect persistence and adaptive drift based on past pairs, as long as it is exogenous to the fresh private J_j trit and persists within the two shots. Conditional on such a history, the new agreement bit has probability p_A(ξ_j)≥a=.5753. Under B independent Lévy increments give iid Bernoulli(p_B), with p_B≤b=.5460. Fresh independent measurement randomness yields stochastic domination:

