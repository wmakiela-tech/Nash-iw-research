# M14 ROT004 — Exact versus quantized stochastic sampling clock: high-frequency TV collapse

artifact_id: IW_M14_ROT004_XH_S4_LT_REV023_QUANTIZED_CLOCK_HIGH_FREQUENCY_NONMAP_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_MATURE_STOCHASTIC_IDENTIFICATION / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST / OWNER_LT_ADOPTION_NOT_ASSUMED / REFEREE_PENDING
return_id: M14-ROT004-XH4-LT-CLOCK_QUANTIZATION_TV_COLLAPSE_001_20261026
date: 2026-10-26
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14

## Original owners FIRST

XH-S4 ROT030 first owns OU stationary same-density/different-current example: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md .
M14 ROT001 owns continuous radial-law nonmap, exact periodic grid alias, and two-incommensurate-lag exact kernel injection: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/IW_M14_ROT001_XH_S4_LT_REV022_OU_OBSERVATION_QUOTIENT_AND_SAMPLING_ALIAS_001.md .
M14 ROT002 owns deterministic finite-schedule KL/Fisher/minimax: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/iw_m14_rot002_ou_global_KL_Fisher_minimax_001.md .
M14 ROT003 owns registered-random-clock population TV separation and finite-n unbounded minimax risk: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/iw_m14_rot003_registered_random_ou_annealed_quenched_minimax_001.md .
LT working REV023 §2.11 ALREADY incorporates XH-S4 ROT030 + M14 ROT001, and §7.5e.1 already warns of finite/noisy observations: https://docs.google.com/document/d/18qbcIk9h2ng7V1O4qszjfrYzsffXWMda0_YBdDEqeTg/edit .
ONLY ROT004 delta: exact full-state OU sampled at random gaps as ROT003, but true continuous gap t withheld or quantized into finitely many bins. This is source-typed classical mathematical countercontrol. XH-S5 only packet ready, NOT activation verified; LT revision title alone cannot establish LT6 activation.

## Frozen source and observation contract

dZ_t=(-I+omega J)Z_t dt+sqrt(2)dW_t in R², J=[[0,-1],[1,0]], Z0~N(0,I), W independent, omega real; known diffusion and physical orientation, exact FULL 2D sampled states, no sensor noise.
For every independent gap D use density
p(t)=(exp(2t)-1)/Znorm, t∈[a,b]=[3/4,5/4],
Znorm=(exp(2b)-exp(2a))/2-(b-a)=3.3504024451827044.
Given Z0=z and D=t, conditional Gaussian transition q_omega,t(z,z') is N(exp(-t)R_(omega*t)z, [1-exp(-2t)]I).

Eexact observes (D,Z0,ZD), Ebin observes (C(D),Z0,ZD) for a fixed finite partition C of [a,b] into positive-width bins, Ehidden observes (Z0,ZD). The clock is parameter-independent and drawn before transition. The SAME experiment's coarsening yields the valid Markov garbling order Eexact -> Ebin -> Ehidden, NOT a universal ordering of dissimilar spatial/radial sensors.
For n steps use independent gaps, full states Z0,...,Zn, and associated bins when Ebin. All n are FINITE and fixed.

## Theorem 1 — exact-clock separation survives in the registered experiment

For Eexact, ROT003 derives the joint one-gap KL
K_exact(delta)=(2/Znorm){(b-a)-[sin(delta*b)-sin(delta*a)]/delta}, delta=omega'-omega, K(0)=0.
As |delta|→infinity K→2(b-a)/Znorm=0.2984716064297965. ROT003 gives an explicit strictly positive TV lower bound uniformly for |delta|≥epsilon>0. This claim concerns the JOINT continuous-time register plus state, not the bin-only law, and does not imply bounded global squared-risk for finite n.

## Theorem 2 — any fixed finite clock quantization yields high-frequency TOTAL-VARIATION collapse

Let B_j=[l_j,r_j] be the j-th fixed clock bin. Define the labelled transition *subdensity*
K_omega,j(z,z')=∫_(B_j) p(t) q_omega,t(z,z')dt.
Let q_t,theta be that same Gaussian transition replacing omega*t by a free angular coordinate theta, and define
K_infty,j(z,z')=∫_(B_j) p(t) (1/2π)∫_0^(2π) q_t,theta(z,z') dtheta dt.

For EVERY fixed z,z',j,
lim_|omega|→infinity K_omega,j(z,z')=K_infty,j(z,z').
Proof: F(t,theta)=p(t)q_t,theta(z,z') is continuous on compact [a,b]×S¹ (away from finitely many bin boundaries) and periodic in theta. Approximate uniformly in theta by trigonometric polynomials; nonzero harmonics integrated on a bin are integrals f_m(t)exp(i*m*omega*t)dt→0 by classical Riemann–Lebesgue, while zero harmonic is exactly the angular average.

For fixed z, both families of labelled kernels (summed over bins, integrated over z') normalize to one; Scheffé's lemma upgrades pointwise convergence to TV convergence. For fixed finite n, the joint density μ(z0)∏_(j=1)^n K_omega,b_j(z_(j-1),z_j) converges pointwise to μ(z0)∏K_infty,b_j and both joint densities normalize, so Scheffé yields

**TV(P_omega^(Ebin,n), P_infty^(Ebin,n)) → 0 as |omega|→infinity.**

P_infty DOES NOT depend on omega. Forgetting bins gives Ehidden as a further Markov contraction, hence identical conclusion.
In particular choose omega_k=k and omega'_k=2k: |omega'_k-omega_k|=k→infinity but TV(P_k,P_2k)→0 for Ebin and Ehidden. Hence finite clock resolution DESTROYS the global far-parameter TV separation of Eexact. This does NOT assert failure of pointwise parameter injection or of fixed compact-range inference.

Conditions: independent continuously distributed gaps with integrable density on a positive compact time interval; fixed finite bin partition, no parameter-dependent clock. The special p is needed for closed-form controls, not for this TV convergence.

## Theorem 3 — high-frequency minimax falsifier distinct from ROT003

For any fixed n and Ebin estimator hat-omega, Le Cam testing yields
max(E_k[(hat-omega-k)^2],E_2k[(hat-omega-2k)^2]) ≥ k²*(1-TV(P_k,P_2k))/8.
Theorem 2 makes the multiplier tend to one while k→infinity, so sup over unbounded omega of quadratic risk is infinite. Ehidden inherits it. Eexact ALSO has infinite unbounded minimax by ROT003, but via bounded positive KL/overlap: it does NOT have the high-frequency common-law collapse.

## Theorem 4 — disappearance of oriented moments DOES NOT imply independence

Writing ζ_t=Z_t^(1)+iZ_t^(2), joint stationary Gaussian/Wick gives for exact gap t:
E[ζ_D conjugate(ζ_0)|D=t]=2 exp(-t+i*omega*t);
E[(ζ_D conjugate(ζ_0))²|D=t]=8 exp(-2t+2i*omega*t);
Cov(|Z0|²,|ZD|²|D=t)=4 exp(-2t).
For any bin B=[l,r], the first complex cross-moment (UNnormalized bin contribution) is
(2/Znorm){[exp((1+i omega)r)-exp((1+i omega)l)]/(1+i omega)
 -[exp((-1+i omega)r)-exp((-1+i omega)l)]/(-1+i omega)}.
Its magnitude ≤4(exp(r)-exp(-r))/(Znorm*|omega|) by integration by parts (omega ≠0). The analogous second harmonic tends to zero. Conditional bin moments also tend to zero after division by P(D∈B)>0.

CRUCIAL negative control: since E(|Z0|²|D=t)=E(|ZD|²|D=t)=2,
Cov(|Z0|²,|ZD|²)=4 E exp(-2D)
=4/Znorm *{(b-a)-[exp(-2a)-exp(-2b)]/2}
=**0.5127472609808392**, independent of omega, strictly positive even under the common limiting law. Bin-conditioned radial covariance =4 E[exp(-2D)|B]>0. The limit is an *angular mixture with surviving radial dependence*, NOT a pair of independent stationary snapshots. Vanishing ordinary vector cross-covariance is insufficient to infer independence or memory loss.

## Executed independent arithmetic falsifiers

Companion standard-library script verify_m14_rot004_clock_quantization.py checks exact first/second complex Wick moments against independent Simpson quadrature for omega 0,1.5,21,177; bin partition probabilities; pooled vs bin-wise radial covariance; harmonic integration-by-parts inequalities and prints trends for omega 0,2,20,200,2000,20000. PASS. These are deterministic tests, not a proof of whole-TV Theorem 2; the proof above is the load-bearing support. Local machine-readable rot004_controls.json, with no claim of BW ingest.

## Source/currentness and LT integration

Optional for current LT REV023 author §2.11/§7.5e.1: an E5 instrument contract differentiating continuous observed timestamps from finitely quantized/unobserved timestamps. Under the same source full-state data this is a LEGAL garbling comparison. Distinguish statistical separability from stable estimation at a physical finite budget. No auto-change to LT REV023 and no LT owner approval implied.

Mature host checks: Mu et al., *Identification of linear continuous-time systems under irregular and random output sampling*, Automatica 60 (2015) 100–114, DOI 10.1016/j.automatica.2015.07.009 (publisher abstract/intro, different model); Eng & Gustafsson, *Identification with stochastic sampling time jitter*, Automatica 44 (2008) 637–646, DOI 10.1016/j.automatica.2007.06.018 (publisher abstract, unobserved jitter and high-frequency bias); Zeng et al., *A Sampling Theorem for Exact Identification of Continuous-Time Nonlinear Dynamical Systems*, IEEE TAC 69 (2024), DOI 10.1109/TAC.2024.3409639 (abstract, Koopman/sampling host). None is claimed to already prove this exact OU-bin lemma and no literature novelty claim is made.

STOP/reassess if D has atoms/exact timestamp side channel, clock bins change with omega, sampling feedback/stopping times, sensor noise, unknown/nonstationary initial state, unknown diffusion, physical realization, or compact/prior-limited omega. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_J3K / BW_UNKNOWN / REFEREE_PENDING / NO_CROSS_CELL_TASK_CASCADE.
