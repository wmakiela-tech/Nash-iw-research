---
artifact_id: IW_MT14_ROT005_RANDOM_TIME_LABEL_ALIAS_RECOVERY_AND_QUANTIZATION_NO_GO_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P2_ROTATIONAL_OU_RANDOM_OBSERVATION_TIME_AND_RECORD_PRECISION_GATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_EXACT_GAUSSIAN_THEOREM / INDEPENDENT_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_NASH / NO_GLOBAL_UNBOUNDED_ESTIMATOR / NO_VALIDATED_CLOCK
---

# MT14 ROT005 — Random observed sampling time defeats deterministic OU near-aliases; finite quantization reinstates asymptotic nonidentifiability

**Date:** 2026-10-26. **Claim class:** a mathematically exact, source-typed observation-contract comparison under one frozen classical Gaussian process. Not NASH physical claims, not new generic sampling theory, not a continuous-time estimation or hardware result.

## Authors first and two-surface prior art

- **XH-S4 ROT030 FIRST** introduced the exact 2D OU example: stationary N(0,I) hides rotational probability currents:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md
- **M14 ROT001 FIRST** proved exact full-vector aliases at deterministic equal gaps, irrational two-gap algebraic injection with global instability:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/IW_M14_ROT001_XH_S4_LT_REV022_OU_OBSERVATION_QUOTIENT_AND_SAMPLING_ALIAS_001.md
- **M14 ROT002 FIRST** proved near aliases for ANY fixed finite deterministic schedule and infinite worst-case unbounded-frequency quadratic risk, with positive local Fisher:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/46abb0ef331f42e89eac490872e586a594b51fc6/research/m14/2026-10-26/iw_m14_rot002_ou_global_KL_Fisher_minimax_001.md
- LT6 REV023 working monograph Ch2/7 proposes observation/intervention resource gates; this is optional mathematical input, NOT an approved LT edit.
- Classical EXTERNAL hosts already contain alias-free random-time sampling: Beutler (1970), DOI https://doi.org/10.1109/TIT.1970.1054435; Masry (1971), DOI https://doi.org/10.1016/S0019-9958(71)90146-X. Their spectral-estimation targets differ from this exact finite-data OU binary experiment. Riemann-Lebesgue, Hellinger Gaussian affinity, Scheffe L1 lemma, Pinsker and elementary experiment garbling are mature facts. Bibliographic/abstract-level prior-art subtraction only: **NO novelty claim**.

## Frozen source model and three different observation experiments

Let the real vector Z_t in R^2 solve

    dZ_t = (-I + omega*J) Z_t dt + sqrt(2) dW_t,
    J=[[0,-1],[1,0]], Z_0~N(0,I).

Omega in R is the ONLY unknown. Noise variance, drift damping, axes, law Z0 and the sampling distribution are all exactly known. For t>0

    Z_t|Z_0=z ~ N(a_t R_(omega*t) z, q_t I),
    a_t=exp(-t), q_t=1-exp(-2t).

Every single-time stationary marginal is N(0,I), independently of omega.

Independently draw a SINGLE time T~Uniform(ell,u), with 0<ell<u<infinity and D=u-ell. Compare:

- E_exact: observes EXACT realized continuous T and both full vectors (Z0,Z_T).
- E_B: observes only b(T) in a fixed finite set of time bins, plus the same vectors.
- E_none: does not observe T at all, only the two full vectors.

No multi-slot adaptive controller; no physical timestamp precision or instrument noise validation.

## T1 — exact Hellinger affinity of exact-time experiment

For omega'=omega+delta and a FIXED t, the joint Gaussian affinity of (Z0,Zt) is

    h(t,delta) = 1/[1+(1-cos(delta*t))/(2*(exp(2t)-1))].         (1)

Proof: conditional Gaussian equal-covariance affinity is exp(-||m1-m2||^2/(8q_t)). The rotation identity ||(R_a-R_b)z||^2=2(1-cos(a-b))||z||^2 and the Gaussian identity E exp(-s||Z0||^2)=1/(1+2s) give (1). Independently, the exact zero-mean joint 4x4 covariance

    C_omega(t)=[[I, a_t R_(omega*t)^T],
                [a_t R_(omega*t), I]]

in the Gaussian determinant affinity formula gives exactly (1).

Because T is OBSERVED, its density is shared between hypotheses:

    rho_exact(delta) = (1/D)*integral_ell^u h(t,delta) dt.      (2)

For total variation,

    TV(E_exact(omega), E_exact(omega')) >= 1-rho_exact(delta). (3)

This is a valid lower bound, NOT an equality between TV and 1-rho.

## T2 — globally uniform pairwise separability with an exact real-valued timestamp

Fix epsilon>0 and set a=epsilon*D/2 and

    s_epsilon=sin(a)/a if 0<a<=pi/2; else 2/pi.

Then s_epsilon<1, and for ALL omega,omega' with |omega-omega'|>=epsilon,

    TV(E_exact(omega),E_exact(omega'))
      >= c_epsilon
       = exp(-2*u)/2 * (1-s_epsilon) > 0.                     (4)

Proof: rearranging (1) gives

    1-h(t,delta)
      = (1-cos(delta*t)) /
        [2*(exp(2t)-1)+(1-cos(delta*t))]
      >= exp(-2*u)/2*(1-cos(delta*t)).

Uniform T has

    E cos(delta*T) = cos(delta*(ell+u)/2)*sinc(delta*D/2).

For |delta|>=epsilon, |sinc(delta*D/2)|<=s_epsilon: sinc decreases on (0,pi/2], and at larger arguments its absolute value is <=2/pi. Integrate and apply (3). In this EXACT labelled-time experiment no pair with frequency separation >=epsilon can become arbitrarily close in TV, unlike M14's fixed FINITE deterministic schedule.

Crucial limitation: uniform TWO-HYPOTHESIS separation over an unbounded parameter does NOT prove a finite-risk estimator working simultaneously for infinitely many alternatives. It also presupposes an ideal real-valued time record.

For a single deterministic t=1, delta=2pi is an EXACT alias (affinity=1). For ell=.25,u=1.25, the observed random-time affinity at delta=2pi is 0.8163777833458006, implying TV>=0.1836222166541994.

## T3 — a fixed finite timestamp quantizer loses unbounded-frequency separation

Let b:[ell,u]->{1,...,m} be ANY fixed finite measurable time partition. With phi_q the 2D Gaussian transition density, E_B has joint density

    p_omega(j,z,y)=phi_I(z)/D *
       integral_{t: b(t)=j} phi_(q_t I)(y-a_t R_(omega*t)z) dt.

Define the phase-averaged kernel

    Kbar_t(y|z)=(1/(2pi))*integral_0^(2pi)
                       phi_(q_t I)(y-a_t R_theta z) dtheta.

**Exact theorem:** as |omega|->infinity, p_omega converges in total variation to a normalized common p_infty replacing its integral kernel by Kbar_t, independent of omega. Consequently, choosing omega_n=n, omega'_n=2n gives both |omega_n-omega'_n|->infinity and

    TV(E_B(omega_n),E_B(omega'_n)) -> 0.                      (5)

The same holds if time is completely unobserved (E_none).

Proof: on t in [ell,u], ell>0, the phase-dependent Gaussian density is continuous and 2pi-periodic. Uniform trig-polynomial approximation in the angular variable and the Riemann-Lebesgue lemma show, for fixed (z,y) and each bin, that all nonzero harmonics omega*t vanish on integration; the zero mode is exactly Kbar_t. Therefore densities converge pointwise. Their total masses are all one, so Scheffe's lemma upgrades pointwise convergence of nonnegative densities to L1 and total variation convergence. Triangle inequality gives (5). No discrete-lattice-to-continuum TV sleight of hand.

The angular mean has the closed Bessel expression

    Kbar_t(y|z) =
      exp[-(||y||^2+a_t^2||z||^2)/(2q_t)]/(2pi q_t)
      * I0(a_t*||z||*||y||/q_t).

**Substantive contrast:** Random TIME DESIGNS can be alias-free as E_exact but their time-MARGINALIZED or FINITELY TIMESTAMPED experiments become globally asymptotically indistinguishable for frequencies tending to infinity. The difference is a real observation/precision resource, not semantics.

The exact observed-time affinity has its own large-difference limit:

    lim_|delta|->infinity rho_exact(delta)
      = E_T sqrt(1-exp(-2T)),                                (6)

by phase averaging 1/(1+b(t)*(1-cos theta)). On [.25,1.25], (6)=0.8542517391804068, so its limiting Hellinger-based TV lower bound is approximately 0.1457482608195932. This *does not* vanish as delta diverges, whereas E_B's pair TV in (5) DOES vanish.

## T4 — with a known finite frequency band, small finite-time bins suffice quantitatively

Fix epsilon>0 and |omega|,|omega'|<=Omega finite. Suppose every time bin has width <=eta. Let

    q_min=1-exp(-2*ell),
    L_Omega=sqrt(q_min^(-4)+(1+Omega^2)/(2*q_min)).

Then

    TV(E_B(omega),E_B(omega'))
       >= c_epsilon - 2*L_Omega*eta.                          (7)

Thus eta<=c_epsilon/(4*L_Omega) guarantees the UNIFORM pairwise lower bound TV>=c_epsilon/2 for separations >=epsilon in the COMPACT omega band. This is conservative and not optimal design.

Derivation: let K_omega(t)=law(Z0,Z_t) when t is fixed. Conditional Gaussian KL, with z0 integrated, is exactly

    KL(K_omega(t)||K_omega(s))
      = q_t/q_s-1-log(q_t/q_s)
        + ||a_t R_(omega*t)-a_s R_(omega*s)||_F^2/(2*q_s).

For ell<=s,t<=u and |omega|<=Omega, q_t/q_s>=q_min and |q_t-q_s|<=2|t-s|. Taylor control of x-1-log x on x>=q_min gives first term <=2|t-s|^2/q_min^4. The Frobenius derivative of t->a_t R_(omega*t) has norm sqrt(2)*a_t*sqrt(1+omega^2), giving a second term <=(1+Omega^2)|t-s|^2/q_min. Pinsker proves

    TV(K_omega(t),K_omega(s)) <= L_Omega*|t-s|.

From E_B generate an independent within-bin continuous surrogate T' according to the KNOWN conditional time distribution. This does NOT add information: its bin remains recoverable and it is independent of the Gaussian data conditional on the bin. The augmented coarse experiment is <=L_Omega*eta in TV from E_exact for each omega, by pairwise within-bin kernel coupling. Applying the triangle inequality for omega and omega' to (4) yields (7). Here uniform T simplifies all bin conditionals; the argument also works with regular known nonuniform time priors.

As Omega grows, L_Omega is O(Omega), hence the sufficient time precision is O(1/Omega). T3 establishes that no fixed finite partition can give an UNBOUNDED global guarantee.

## Executed independent checks, observed failure gates

A standalone Python NumPy/SciPy reproducer, results JSON, expanded Polish report, SHA256 manifest, and README have been executed and preserved as a self-contained Moderator-local five-file ZIP, with clean isolated replay. Numeric checks do NOT substitute the proofs:

- 3 independently computed Gaussian 4x4 determinant affinities versus conditional analytic (1): errors 0,0,1.11e-16.
- Exact fixed-t=1 alias h(1,2pi)=1, but random observed-time rho_exact(2pi)=0.8163777833458006.
- ell=.25,u=1.25,epsilon=1: explicit c_epsilon=0.0016888546353614553; direct quadrature at tested delta>=1 respects (4).
- Limit (6)=0.8542517391804068, rho_exact(200)=0.8545475777819005.
- Two fixed bins [.25,.75] and [.75,1.25] tested on z=(1,-.4), y=(.25,.75): at omega=800, binned joint labelled density errors vs angular phase-average densities are 0.0001467456804 and 0.0001032134727. POINTWISE numerical checks only, not full numeric TV.
- Omega=5: L_Omega=8.64642044907856, sufficient eta<=4.883103491518952e-5 for guaranteed TV>=c_epsilon/2. Conservative.
- ZIP CRC PASS; four SHA256 files PASS; separate empty-directory full rerun PASS and regenerated JSON byte-identical. ZIP SHA256: 138fadfd709a141a6e49f2e0fb65017b83c8466ba06df829d16e69c1317b78d9.

Falsifiers: (i) violation of covariance/conditional affinity; (ii) two exactly timestamped omegas with |delta|>=epsilon and TV<c_epsilon; (iii) a fixed finite time quantizer for which omega=n and 2n stay TV-separated by a positive amount as n->infinity; (iv) violation of bound (7) under its compact-band/ell>0 assumptions.

## Science routing and stopping rules

Source-first ownership stays with XH-S4 ROT030 for OU example and M14 ROT001–002 for fixed deterministic schedule theorems. MT14 adds a **different experiment class**: exact observed randomized time vs finite timestamp precision; not a critique of M14. A single owner/referee verification of (1)–(7) could inform LT's observation-resource discussion, without treating working LT as canon. No new task cascade, no generalized unbounded-frequency estimation claim, no physical NASH interpretation. Do not generate repeated variants of this OU example absent a material referee challenge or actual new source constraint.

STATUS: SOURCE_TYPED_GAUSSIAN_EXACT_PROOFS / INDEPENDENT_NUMERIC_AND_CLEAN_REPRO_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / GITHUB_PENDING_BW_INGEST.
