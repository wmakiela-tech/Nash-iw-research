## 3. Theorem R21.2 — full source-ON finite basis pulses FALSIFY exact R20 X/Y phase invariance

Work in Bloch coordinates r∈R³; define [v]× r=v×r. Under static A:

 dr_A/dt=[ξ e_z+Ω(t) e_axis]× r_A.

Under independent Lévy B:

 dr_B/dt=[Ω(t)e_axis]×r_B − γ diag(1,1,0)r_B.

Use initial r=(0,0,1), finite prep with Y +Ω for t_g=π/(2Ω), source-active free Δ, and final X setting with Y −Ω or final Y setting with X +Ω, both lasting t_g. Let m_X(ξ),m_Y(ξ) be the final Z expectations of A on those axis branches (and similarly B without ξ). For two fresh shots of the same hidden ξ and same common randomly chosen axis,

 p_A(same|ξ)=1/2+[m_X(ξ)²+m_Y(ξ)²]/4,
 p_B(same)=1/2+[m_X(B)²+m_Y(B)²]/4.  (R21.4)

These are EXACT, using the full noncommuting expm during every driven segment, and are independently checked via qubit 2×2 density matrices and 4×4 driven Lindblad superoperators. Source-on preparation and basis switching do not preserve ideal cos²φ+sin²φ identity in general.

**Explicit counterexample, gamma=1, q=.5, Omega=10:** B full finite pulse result p_B=0.5681154068347529. A conditional at ξ=0 yields p_A=.75. By continuity and directly evaluated 3×3 matrix exponentials, at ξ*=23.496399049864984... one gets p_A(ξ*)=p_B (within <1e−12). At ξ≈24 the contrast is negative. The scalar equal/different statistic at this particular static ξ has EXACTLY the SAME Bernoulli law under A and B, for ANY number of independently prepared shot pairs. Thus no phase-uniform separating threshold exists for THIS scalar statistic with this rectangular always-on finite-pulse readout. Not a no-go for richer data, collective tests, different composite pulses or almost-sure consistency under a continuous Cauchy prior. The extremely rare ξ* is still a valid **uniform-in-ξ falsifier**. The narrow source-typed mechanism is noncommutation of drive and Z detuning, already known in external literature; no novelty claim.

