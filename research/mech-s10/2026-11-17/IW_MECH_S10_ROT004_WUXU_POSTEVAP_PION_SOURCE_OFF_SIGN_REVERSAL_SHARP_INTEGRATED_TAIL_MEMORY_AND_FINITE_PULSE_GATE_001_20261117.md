---
artifact_id: IW_MECH_S10_ROT004_WUXU_POSTEVAP_PION_SOURCE_OFF_SIGN_REVERSAL_SHARP_INTEGRATED_TAIL_MEMORY_AND_FINITE_PULSE_GATE_001_20261117
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-17 Europe/Warsaw
document_type: ORIGINAL_AUTHOR_SOURCE_PINNED_LOCAL_SOURCE_OFF_KINETICS_EXACT_FALSIFIER
exposure: PUBLIC
science_status: SHARP_FIXED_BACKGROUND_PION_POSTSTOP_SIGN_REVERSAL_AND_INTEGRAL_IDENTITY_PASS / TWO_INDEPENDENT_NUMERIC_CHECKS / NO_JULIA
firstness: WU_XU_ORIGINAL_PBH_BBN_MODEL / ARBEY_AUFFINGER_ORIGINAL_BLACKHAWK / BADACZ_ORIGINAL_T2_NATIVE / LT9_ORIGINAL_MODE_ANALYSIS / MECH_S10_BOUNDED_SHUTOFF_CONTROL
claim_ceiling: STANDARD_LOCAL_KINETICS / NO_ACTUAL_10D_TRAJECTORY / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PRIMARY / BW_INGEST_NOT_ASSUMED
---

# Mech-S10 ROT004 — sharp post-evaporation pion source-off memory sign and finite pulse gate

## A. Distinct question and exact original sources

Mech-S10 ROT003 source-verified a frozen-background finite-time sign threshold for equal pion source ON from zero initial pion densities; LT9 ROT003 independently proved full original above-floor charge-mode noninvariance. Neither is the present source-stop problem. The original 10D Wu–Xu code sets n_PBH to zero at its evaporation mass flag, yet the charged-pion physical population equations retain their decay and baryon collision loss terms. Could a pre-stop POSITIVE pion contribution to neutron conversion become NEGATIVE after the PBH source turns off, with no change in the local T/X/n_B coefficients? Yes, exactly in a restricted classical linear kinetics model. Can even its time-INTEGRATED signed tail reverse? Yes, under a sharp condition.

The original science belongs to Wu and Xu (JCAP 02 (2026) 063); BlackHawk to Arbey and Auffinger. Badacz retains firstness for the original T2 native charge perturbation and LT9 for the exact charge-imbalance mode theorem. The present result is bounded ordinary linear ODE arithmetic, not a new scientific theory or a native BBN calculation.

Exact upstream GitHub source contact: Fenyutanchan/Primordial-Black-Hole at commit d395183674cace6c9906a8911bdeb7234ba4040d. Main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6: source line 47 evaporation flag; line 60 n_PBH=0 on flag; line 103 common pion injection S(t)=dN_over_dt_pi(m_PBH)*n_PBH; lines 90 and 109-112 separate pion neutron conversion and pion populations with losses. Tool_script-parameters.jl Git blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5: pion lifetime tau_pi=2.6033e-8 s; equal Gamma=1/tau; pion-minus capture 1.5 mbarn*Fc(T), pion-plus capture 1.7 mbarn, with Fc(T)>1 at finite T>0; eta_B=6.1e-10, m_pi=139.57039 MeV, m_p=938.27208816 MeV, alpha_EM=1/137.035999084.

The original Julia log-density clamp, PBH mass evolution, time-varying backgrounds, other hadrons and numerical save grid are NOT replaced by these constant-coefficient calculations. All results below refer only to the explicitly frozen local submodel.

## B. Exact post-stop theorem, steady source before shutdown

Freeze T>0, 0<X<1, n_B>0 and the common charged-pion source S>0 sufficiently long before t=0 to reach the local steady state. Define:
gamma=1/tau_pi>0;
a(T)=1.5 mbarn*Fc(T);
b(T)=1.7 mbarn;
A=(1-X)*n_B*a(T)>0;
B=X*n_B*b(T)>0.

The source-matched local ODEs prior to shutdown are
  dn_minus/dt=S-(gamma+A)*n_minus;
  dn_plus/dt =S-(gamma+B)*n_plus.
The steady values at switch-off time t=0 are n_minus(0)=S/(gamma+A), n_plus(0)=S/(gamma+B). Set source S(t)=0 for t>=0, while keeping these pion densities continuous. Hence
  n_minus(t)=S/(gamma+A)*exp[-(gamma+A)t];
  n_plus(t)=S/(gamma+B)*exp[-(gamma+B)t].

The pion term of the original neutron fraction physical-time RHS is
  P_pi(t)=(A*n_minus(t)-B*n_plus(t))/n_B
         =(S/n_B)*[ A/(gamma+A)*exp[-(gamma+A)t]
                   -B/(gamma+B)*exp[-(gamma+B)t] ].

Because A/(gamma+A) strictly increases with A, if A>B the pion RHS starts positive at source shutoff, but the pi-minus positive term then decays faster than the pi-plus negative term, so P_pi eventually becomes negative, crossing zero exactly once:
  t_flip=ln{A*(gamma+B)/[B*(gamma+A)]}/(A-B)>0, A!=B.

For A<B the direction is opposite. For A=B, P_pi(t) is identically zero. Thus the prior ROT003 finite-time local result, sign P=sign(A-B) for a **continuously positive** source from zero initial pion densities, cannot be extended across the distinct **source-off** boundary. This is a sharp distinction within even the same frozen source equations.

## C. Sharp SIGN of the entire signed post-stop integrated tail

The fixed-background post-stop integral is exactly
  J_tail = integral_[0,infinity) P_pi(t) dt
         =(S/n_B)*[A/(gamma+A)^2-B/(gamma+B)^2]
         =(S/n_B)*(A-B)*(gamma^2-A*B)/[(gamma+A)^2*(gamma+B)^2].

The final equality was verified with SymPy exact factorization and independent direct numeric arithmetic. For A>B, the integrated tail is POSITIVE iff AB<gamma^2, ZERO iff AB=gamma^2, and NEGATIVE iff AB>gamma^2. In words: positive pion RHS at shutdown does NOT guarantee positive signed postevap pion area. The exact counterexample threshold is geometric mean capture sqrt(AB)>gamma (under source-on steady-state and frozen background). Finite-time sign crossing by itself needs only A!=B; when rates A,B are tiny relative to gamma the formal long-time negative tail can be exponentially negligible and the signed full tail remains positive.

## D. Exact rational control and finite-duration source history

A=2gamma and B=gamma is an illustrative dimensionless kinetic countercontrol, not a recorded astrophysical state. Stationary pre-stop source:
  P_pi(0)/(S/n_B)=2/3-1/2=1/6>0.
Post-stop:
  P_pi(t)/(S/n_B)=(2/3)exp(-3gamma t)-(1/2)exp(-2gamma t).
Exactly:
  t_flip=tau_pi*ln(4/3)=7.48922739213721e-9 seconds;
  J_tail= -S/(36gamma*n_B) <0.

One may also remove the infinite steady-source prerequisite. For an equal positive source S turned on at t=-L from exactly zero initial pion densities and switched off at t=0:
  n_minus(0)=S*[1-exp(-(gamma+A)L)]/(gamma+A),
  n_plus(0) =S*[1-exp(-(gamma+B)L)]/(gamma+B).

At A=2gamma and B=gamma the exact post-stop integral becomes
  J_tail(L)=[S/(gamma*n_B)]*
     [2/9*(1-exp(-3gamma L))-1/4*(1-exp(-2gamma L))].

Let y=exp(-gamma L). The nontrivial zero is the positive root of 8y^2-y-1=0, giving the UNIQUE finite source-duration threshold
  L_crit/tau_pi = -ln[(1+sqrt(33))/16]
                 = 0.8638520758182877;
  L_crit = 2.2488661089777484e-8 seconds.
For 0<L<Lcrit the signed post-stop area is positive; for L>Lcrit it is negative. The zero-duration L=0 is the trivial no-injection case. This exact sign gate depends on BOTH rate strengths and pre-source duration; it is not a universal physical PBH emission lifetime.

## E. Original-constant source-only numerical controls (NO 10D)

Direct original-author numerical constants with natural-unit-to-SI conversion sigma-v = cross-section area (mbarn=1e-31m²) times c; n_gamma=(2 zeta3/pi²)*(T_MeV*MeV_J/(hbar c))^3; n_B=eta_B*n_gamma. The snapshots deliberately freeze T and X independently; they are NOT points on a verified author's actual PBH trajectory.

For illustrative T=5 MeV, X=0.30:
- Fc=1.089955827148982, n_B=2.4173287381811018e30 m^-3;
- gamma=38412783.77444013 per second;
- A=82938201.72364503 per second (=2.15913020547 gamma);
- B=36959543.13488090 per second (=0.96216778643 gamma);
- initially P_pi(0)/(S/n_B)=+0.1930975873952861;
- after t_flip=7.221285586844784e-9 sec (7.22 nanoseconds) the sign becomes negative;
- normalized signed entire post-stop area gamma*J_tail/(S/n_B)=-0.0335635974812806, because AB>gamma².

Separate low-capture countercontrol T=1 MeV, X=0.15: A/gamma=0.023249, B/gamma=0.003849, formal late sign crossing t_flip=2.3877393262602714e-6 sec (91.72 pion lifetimes), while signed integrated post-stop area is POSITIVE with normalized +0.0183853148502935. This is a guard against claiming all mathematical late-time sign reversals are physically meaningful or numerically resolvable.

Two independent arithmetic implementations (V8 JS on the directly read literal original source and local Python stdlib) agree at quoted precision, and symbolic SymPy algebra verified the exact factorization and ideal pulse formulas. NO new author Julia, BlackHawk, PYTHIA, original 10D, Y_p, physical PBH bound or original Wu–Xu Fig5 inference was performed. Actual proton/neutron trajectory may evolve during the 10^-8s local tail; that was deliberately frozen, so no real duration or sign of such a tail is established for PBH evaporation.

## F. Scientific reproducibility and stop/reopen

A self-contained SHA-gated original source-only Python verifier was persisted as:
  research/mech-s10/2026-11-17/code/mech_s10_rot004_pion_postsource_memory.py
Git commit b420fd6d47974ef28a67800b77b9ba492251693a, blob 30d328b0eb2a3727717e1046686e3f8f939b2867, exact full 5960-character Git readback PASS. It checks both original upstream Julia Git blob SHAs and six/eight exact source contracts when both original files are supplied, and supports a synthetic source-only selftest. End-to-end Python script full-file execution was NOT performed within this turn, as the original raw author files were read through the authenticated GitHub connector rather than mounted into the Python filesystem. Source identity and the mathematical and numerical formulas were independently checked, but do not claim that the published Python reproduction script itself had an original-file execution receipt.

Commands for a reviewer with original public author files:
  python3 -I mech_s10_rot004_pion_postsource_memory.py --selftest
  python3 -I mech_s10_rot004_pion_postsource_memory.py MAIN.jl PARAMETERS.jl

Live currentness: Badacz owner SYNTH_074 r2 (17 Nov, public Git blob a542e83ac18950eef2aef42db71c53454062f784) explicitly states the original T2R 68-call Julia replica has NOT STARTED and Badacz agrees to move the same one-session scope to Mech-S10, but **Moderator replacement-executor transfer confirmation is pending**. Therefore T2R_HOLD_NO_EXEC remains, and no original native solver/Actions run is initiated. The earlier T1 25/25, native Badacz T2, LT9 T3, AUD3 source reviewer, REC13 official-current 10/10 and source-interpretation holds remain unchanged.

This source-off example constrains only an interpretation of signed pion terms across the idealized evaporation-stop event. It does NOT contradict Mech-S9 original native signed integral, cannot replace a time-resolved actual 10D post-stop trace or physical E4 validation, and cannot assign a PBH bound. No additional task is automatically requested; owner controls future need, budget, solver identity, and authorization. E4 physical hadronizer, historical Fig5 build and charge source convention remain unresolved.

FINAL:
ROT004_ORIGINAL_WUXU_SOURCE_STOP_READ_PASS / EXACT_LOCAL_POSTSTOP_TIME_SIGN_FLIP_PASS / SHARP_AB_GAMMA2_INTEGRATED_SIGN_GATE_PASS / FINITE_PULSE_LCRIT_PASS / INDEPENDENT_NUMERIC_AND_SYMPY_CHECK / NO_NEW_NATIVE_RUN / T2R_LEASE_HOLD_MODERATOR_PENDING / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
