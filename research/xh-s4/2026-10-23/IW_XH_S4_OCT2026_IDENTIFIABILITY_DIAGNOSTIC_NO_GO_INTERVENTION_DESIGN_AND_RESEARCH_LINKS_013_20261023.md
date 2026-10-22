# XH-S4 — October research rotation 013: diagnostic completeness, dynamical excitation, and interventional attribution

RETURN_ID: XH-S4-OCT2026-DIAGNOSTIC-NOGO-IDENTIFIABILITY-INTERVENTION-QUESTIONS-013_20261023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
PURPOSE: follow Moderator's requirement that research intake extracts QUESTIONS, typed LINKS, mutually discriminating hypotheses, and cheapest falsifiers, beyond abstracts.
RESULT_CLASS: THREE OCT PRIMARY SCIENCE SOURCES / THREE EXACT FINITE TOY CONTROLS / CROSS_PAPER_QUESTION_ATLAS
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_J3_K_PHYSICS / NO_PBH_BOUND / BW_INGESTION_NOT_ASSUMED / NO_NEW_TASK_ASSIGNMENT
PROVENANCE: source papers checked from original arXiv HTML and official APS accepted page. Synthetic computational examples developed by XH; NOT claims of original authors, NOT direct NASH runtime experiments or proof of their full theorems.

## 1. SOURCE A (October 14 2026) — impossibility of finite checklist certifying MCMC distributional convergence
Daniel Matsui Smola, `MCMC Can See Can't See`, arXiv:2610.20020v1 (submitted Oct 14).
Primary: https://arxiv.org/html/2610.20020 ; abstract https://arxiv.org/abs/2610.20020 .

Theorem 1 (Sec 3.1) precise host: target pi with density on R^d, bounded CHARACTERISTIC reproducing kernel k with RKHS H, and m diagnostic directions v_i in H; diagnostics measure inner products of mean-embedding discrepancy delta_t = mu_pi_t - mu_pi with v_i. There exists an ergodic chain with target pi and initialization such that all monitored expectations agree with target at every finite time although pi_t != pi. This is a NO-GO FOR THE DECLARED finite RKHS mean tests, not a theorem that every conceivable diagnostic protocol in all settings fails.

Thm 2.1 (Sec 3.2) with source condition delta=Sigma^r u, ||u||<=R, top m eigenspace monitors minimize worst omitted norm:
   inf_dimV<=m sup_{delta in B_r(R)} ||P_(V_perp) delta|| = R lambda_(m+1)^r.
Eigendecay lambda_j ~ j^(-alpha), alpha>1 -> rate order R m^(-alpha*r). Requires credible source smoothness/exponent/radius and target covariance eigenspectrum, not a free numerical confidence bound; the abstract optimal ellipsoid worst-case need not be realized by a probability measure (App A.2).
Multiple chains can share identical blind bias, so chain agreement/Rhat-style tests do not by themselves certify target convergence.

QUESTION Q7: for a fixed NASH diagnostic suite, what class of errors/targets does PASS actually exclude, and which orthogonal error directions remain unseen? Can a source-specific OPERATOR-NORM or TARGET-RISK bound be built using additional assumptions, rather than another checklist?

Typed connections:
- FEEC arXiv:2610.01501, operator norm bound -> pseudospectral enclosure [COMPLEMENTARY MATHEMATICAL CERTIFICATE; DIFFERENT HOST];
- Poisson-GENERIC arXiv:2610.05570, exact band-limited Jacobi vs unrestricted full-frequency discrepancy [NEGATIVE DIAGNOSTIC DOMAIN EXAMPLE];
- DTC0a N odd finite K_A sampled fields from prior project [CANDIDATE HOST NOT ESTABLISHED];
- PRF11 target-relative sufficient history/decision-risk report [TARGET-SCOPE LEGALITY]; do not import MCMC theorem to DTC without mapping error space, monitor linearity, covariance and source class.

EXACT INDEPENDENT DISCRETE ANALOGUE (does not prove continuous RKHS theorem):
state space {1,2,3}, target pi=(1/3,1/3,1/3), initial q=(1/3,1/3+e,1/3-e) with e=.12, refresh chain K=(1-rho)I + rho 1*pi^T, rho=.25. It is irreducible/aperiodic, pi stationary; pi_t=pi+(1-rho)^t(q-pi). Diagnostic D(p)=p(state1) agrees EXACTLY with target for all t; total variation TV(pi_t,pi)=e(1-rho)^t remains >0 for all finite t. Independent numpy recomputation values:
t=0 D-error 0, TV=.12000000000
t=1 D-error 0, TV=.09000000000
t=2 D-error 0, TV=.06750000000
t=4 D-error 0, TV=.03796875000
t=8 D-error 0, TV=.0120135498046875.
FALSIFIER: a PASS on single monitored probability does NOT warrant convergence of full distribution. The target difference sits in unmonitored direction state2-state3.
NOTE: This is a finite-state DEMONSTRATION of obstruction, not the exact continuous-target hypotheses of the article, so label it analogue.

## 2. SOURCE B (October 3 2026) — dynamical span and gauge corrected recovery

Le Gong, `Identification and Recovery of Linear Dynamics from Partial Trajectories`, arXiv:2610.04455v1.
Primary: https://arxiv.org/html/2610.04455 ; https://arxiv.org/abs/2610.04455 .
Observation maps y_t^(i)=S_i A^t x_0^(i), all A and initial-state factors unknown, X0=UV^T rank r.
Prop 3.10 (Sec 3.2): intrinsic GL(r) gauge kernel of factorization: (Delta A,Delta U,Delta V)=(0,UH,-V H^T), dimension r². Theorem 3.13: IF existence of a full-rank Jacobian certificate rank n²+nr+mr-r² for a fixed sampling pattern, then it is GENERIC (Lebesgue almost every full-rank factors); not a claim any sampling plan suffices. Cor 3.16: at a full-rank point only local ambiguity from basis change. Sec 4 global recovery needs fully observed r basis trajectories and rank conditions; no unconditional global result.

QUESTION Q8: how many initial-state, intervention, and measurement directions are needed to identify a claimed NASH finite-dimensional representation *modulo the correct realization symmetry*? Can a single spectral target be identifiable even while the full operator is not?

Typed connections:
- PRF11 identifiable law vs behavior/target, equivalence/gauge [EXACT CONCEPTUAL TYPE].
- OpenAI math rep-stability families 289/288 [CONDITIONAL FUTURE ALGEBRA HOST, NOT automatic].
- NASH DTC projected nonnormal A_C [ONLY future frozen finite linear subcase; not a theorem for current mixed operator defect].
- causal fingerprints arXiv:2610.22286 [COMPLEMENTARY hidden-state explanatory diagnostic; not structural identifiability proof].

EXACT INDEPENDENT LINEAR OBSTRUCTION:
n=2, full-state measurement S=I, only x0=e1, A_b=diag(1,b), for arbitrary b (2,3,9 tested with numpy). For every t>=0, A_b^t e1=e1. No number of additional time samples from this same unexciting initial-state subspace can recover b, even with complete spatial measurement. Adding a second initial experiment x0=e2 yields A_b e2=b e2 at t=1 and identifies b in this toy case.
FALSIFIER: "longer observation horizon alone restores full A identifiability" is false in this example.
Distinguish nongeneric explicit obstruction from generic local theorem at maximal Jacobian rank.

## 3. SOURCE C (accepted October 7 2026) — genuine and effective high-order interaction separation

Suresh Kumarasamy, Dianavinnarasi Joseph, Alexander N. Pisarchik, `Interventional identifiability of irreducible higher-order interactions in nonlinear dynamical systems`, APS Open Science, accepted Oct 7 2026, DOI https://doi.org/10.1103/lmky-xzc4.
Primary official accepted abstract: https://journals.aps.org/apsos/accepted/10.1103/lmky-xzc4 .
ACCESS_LIMIT: official abstract read. Full theorem and proof were not downloaded or audited; do not promote precise statement beyond reported abstract.

Authors define higher-order irreducibility as nonseparability of vector field into sums of pairwise terms. Design-matrix three-body block after projection off competing blocks; minimum singular value vanishes on all phase-locked trajectories, generic intervention restores and a small kick restores to second order in perturbation amplitude. In tests, independently prepared initial states detect all four-oscillator irreducible couplings at phase noise up to .03, while passive single trajectory about half (author report).
Key attribution distinction: phase-reduced PAIRWISE Stuart–Landau oscillators yield EFFECTIVE three-body terms. Paired-kick nonlinear response short-time scales linearly in t for direct irreducible coupling, quadratically in t for mediated effective coupling, per source abstract. This is not evidence of NASH J3/K invariants: "3-body" in oscillator model is not our 3-cocycle or TT commutator.

QUESTION Q9: can a target mechanism's apparently irreducible higher-order term be causally attributed by experimental variation instead of just fitting passive trajectories? If observed interactions can emerge by eliminating variables, what is the minimum intervention that distinguishes directly present from effective term?

Competing H_direct: true joint u*v term directly enters observed x derivative; H_mediated: only latent z derivative has u*v, x responds via z; H_observation: models coincide on no-kick observed histories but contrast under joint perturbs.

INDEPENDENT TOY RESPONSE MODEL (analogy only; not full Stuart–Landau phase oscillator):
At fixed tiny joint intervention u=v=e and zero initial x,z:
DIRECT: xdot=u*v -> x(t)=e² t.
MEDIATED: zdot=u*v, xdot=z -> z(t)=e² t, x(t)=e² t²/2.
Use factorial interaction contrast C_uv x = x(e,e)-x(e,0)-x(0,e)+x(0,0). Then C_direct=e²t, C_mediated=e²t²/2.
For e=.2 independent computation:
t=.1 direct=.004, mediated=.0002;
t=.2 direct=.008, mediated=.0008;
t=.4 direct=.016, mediated=.0032.
Doubling t doubles direct response but quadruples mediated one; controlled amplitude both scale e². These are exact ODE solutions and local finite-source analogues; no claim same dynamics as published oscillator proof.
Desideratum: record amplitude, horizon, sensor noise, intervention accessibility and causal host. For fixed additive sensor noise, intervention signal amplitude e² implies squared SNR scale e⁴ on a fixed horizon in the small-kick idealization (XH conditional inference, NOT author-observed bound). Balance local time-asymptotics validity with detectability, and ensure full observed joint response not confounded by unmeasured forcing.

## 4. NEW cross-paper synthesis: uncertainty-admissibility ladder

Level 1: DIAGNOSTIC COVERAGE — finite monitors detect certain residual directions, leave orthogonal complement unless source regularity bounds it (Smola).
Level 2: STATE EXCITATION / DYNAMICAL SPAN — no amount of repeated time sampling recovers never excited directions (Gong).
Level 3: DESIGN INTERVENTION / ORDER ATTRIBUTION — distinguish structural high-order from projected effective interactions only with a legal perturbation and time-resolved output (Kumarasamy et al.).
Level 4: OBSERVATION-LAW IDENTIFIABILITY — if two candidates share full passive observed law, hidden fingerprints can differ as MODEL-DEPENDENT explanations without empirical discrimination (Jiang et al. / XH report012 exact example).
Level 5: TARGET-RELATIVE INFERENCE — choose observable, target, loss, decision horizon and nuisance class (PRF11); scalar fit, latent diagnostics and practical decision are not interchangeable.

SCIENCE QUESTIONS FOR CANDIDATE PROGRAM:
Q7 "Which undetected complement of our finite diagnostic suite can be bounded, and with what SOURCE assumptions?"
Q8 "Which intervention/initial-state basis makes the target representation identifiable modulo declared gauge?"
Q9 "Can the short-time cross-perturbation scaling distinguish direct higher-order interaction from mediated/hidden effect under feasible noise?"
Q10 synthesis "Is there one observation-intervention protocol meeting Q7-Q9 jointly and preserving target-decision adequacy at finite sample budget?"

## 5. Theoretically grounded STOP rules and negative knowledge

- A finite checklist of PROJECT diagnostics passed cannot establish full continuum/spectrum/physical convergence; Smola theorem is MCMC RKHS-specific. Do not claim directly it defeats all K/J3 numerical checks.
- A rank certificate is conditional/generic; explicit matrix recovery only with legal sampling/initialization; local modulo factor gauge != global exact parameter recovery.
- The accepted APS abstract is not access to full proof; cannot announce its higher-order attribution theorem verified independently. Its "three-body" couplings in oscillator vector fields are NOT NASH mathematical J3.
- Source models of observational processes may be statistically identical even when their hidden causal fingerprints differ; any true mechanism attribution needs extra data or assumptions.
- The 3 finite toy controls are elementary exact illustrative tests, not empirical science nor DTC/PBH/NCDG executable code checks.
- No cross-cell tasks, accepted canon, BW integration, physical PBH bound, novelty or EXEC.

## 6. Reproduction code / one-file archive

```python
import numpy as np
# I: finite-list negative control
pi=np.ones(3)/3
q=np.array([1/3,1/3+0.12,1/3-0.12])
rho=0.25
for t in [0,1,2,4,8]:
    pt=pi+(1-rho)**t*(q-pi)
    assert abs(pt[0]-pi[0]) < 1e-12
    tv=0.5*np.abs(pt-pi).sum()
    assert np.isclose(tv,0.12*(1-rho)**t)
    print('t',t,'monitor_error',pt[0]-pi[0],'TV',tv)
# II: partial trajectory excitation
for b in [2.,3.,9.]:
    A=np.diag([1.,b]); e1=np.array([1.,0.])
    assert np.allclose(np.array([np.linalg.matrix_power(A,t)@e1 for t in range(4)]),np.tile(e1,(4,1)))
# III: direct versus mediated response
e=0.2
for t in [0.1,0.2,0.4]:
    direct=e**2*t
    mediated=e**2*t**2/2
    print('t',t,'direct',direct,'mediated',mediated)
```

VERIFICATION_SCOPE: independent numpy computation of 3 simple toy specifications carried out 2026-10-23, no source implementation imported. All primary URLs and arXiv / APS dates source-verified, not peer-review adjudication. GitHub save/readback separate from BW custody.

FINAL: SOURCE_NATIVE_SCIENCE_QUESTIONS / CROSS_PAPER_DISCRIMINATORS / EXACT_TOY_CONTROLS / NO_CANON / NO_EXEC_SIGN.
