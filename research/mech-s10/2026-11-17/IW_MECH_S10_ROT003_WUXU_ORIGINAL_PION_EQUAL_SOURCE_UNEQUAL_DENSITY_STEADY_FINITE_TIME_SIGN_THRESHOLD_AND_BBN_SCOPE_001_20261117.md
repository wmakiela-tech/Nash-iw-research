---
artifact_id: IW_MECH_S10_ROT003_WUXU_ORIGINAL_PION_EQUAL_SOURCE_UNEQUAL_DENSITY_STEADY_FINITE_TIME_SIGN_THRESHOLD_AND_BBN_SCOPE_001_20261117
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
created_at: 2026-11-17 Europe/Warsaw
document_type: ORIGINAL_AUTHOR_SOURCE_PINNED_LOCAL_KINETICS_EXACT_FALSIFIER
exposure: PUBLIC
science_status: LOCAL_FIXED_BACKGROUND_FINITE_TIME_AND_STATIONARY_EXACT_ALGEBRA_PASS / ORIGINAL_SOURCE_READ / NO_10D_RUN
claim_ceiling: CLASSICAL_LINEAR_KINETICS_ONLY / NOT_FULL_WUXU_10D / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PRIMARY / BW_INGEST_NOT_ASSUMED
---

# Mech-S10 ROT003 — equal pion injection is not equal charge densities: exact local kinetic threshold, steady-state bias and conditional weak-equilibrium transition

## 0. Distinct problem and original firstness

This is NOT another BlackHawk T1, Badacz T2/T2R, LT9 T3/lumpability or INT10 source-lift theorem. Their firstness is preserved: Wu–Xu original PBH/BBN code and model, Arbey–Auffinger original BlackHawk, Mech-S9 official source T1 25/25, Badacz native charge normalization T2, LT9 exact quotient theorem, INT10 five-group lift obstruction. This work derives one narrow classical kinetic response directly from original Wu–Xu pion population loss laws.

Question: if a hypothetical charge allocation convention gives exactly equal SOURCE injection to pi-minus and pi-plus, does that force their DENSITIES to be equal? And what does charge-blind equal-density replacement do to the pion-driven neutron-fraction rate? Answer: generally NO, even with equal pion decay lifetimes, due to unequal collision loss coefficients.

## 1. Exact author original sources directly reopened

Frozen author repository Fenyutanchan/Primordial-Black-Hole at commit d395183674cace6c9906a8911bdeb7234ba4040d.

Original main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, physical-time ODE lines 87–112:
- dX_n/dt pion = (1-X)n_pi_minus sigma_minus(T) - X n_pi_plus sigma_plus(T);
- source injected into BOTH distinct pion states is dN_over_dt_pi(m_PBH)*n_PBH;
- dn_pi_minus/dt = S - gamma_pi_minus*n_minus - sigma_minus(T)*(1-X)*n_B*n_minus;
- dn_pi_plus/dt = S - gamma_pi_plus*n_plus - sigma_plus(T)*X*n_B*n_plus.
The code evolves log densities with time-dependent background and a tiny nonzero initial hadron density. It is mathematically defined; source charge-pair interpretation remains bounded T3 AUTHOR_INTENT_UNRESOLVED.

Original tool_script-parameters.jl Git blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5:
gamma_pi_minus=gamma_pi_plus=1/(2.6033e-8 s); sigma_minus=1.5 mbarn*Fc(T); sigma_plus=1.7 mbarn; eta_B=6.1e-10; m_pi=139.57039 MeV; m_p=938.27208816 MeV; m_n=939.5654205 MeV; alpha_EM=1/137.035999084; T_nuc=0.078185270688319950 MeV. Fc(T)=x/[1-exp(-x)], x=2pi alpha_EM/[sqrt(T/m_pi)+sqrt(T/m_p)]>0, so Fc(T)>1 at finite positive T. Baryon density n_B=eta_B*(2 zeta3/pi^2)*T^3 in source natural units.

These two actual original Git blob source texts were fetched and checked: 7 specific physical-source fragments and 13 exact constants/formula fragments each appeared exactly once. No replacement code or claimed earlier historical generator source is involved.

## 2. Exact local finite-time theorem

FREEZE the background at one positive temperature T, neutron fraction 0<X<1, fixed positive baryon density n_B, and a constant equal nonzero source S in each charge-state ODE, for a finite interval t. Assume zero initial pion densities in THIS idealized local subsystem (not the author's literal tiny nonzero initial pion density). Define:

gamma=1/tau_pi >0;
a(T)=1.5 mbarn*Fc(T)>0;
b(T)=1.7 mbarn>0;
A=(1-X)*n_B*a(T), B=X*n_B*b(T).

In the frozen local model (using natural units) the two scalar ODEs solve exactly as:

n_minus(t)=S*[1-exp(-(gamma+A)t)]/(gamma+A);
n_plus(t)=S*[1-exp(-(gamma+B)t)]/(gamma+B).

The pion contribution to the neutron fraction is P(t)=[A*n_minus(t)-B*n_plus(t)]/n_B.

For t>0, h_t(z)=z*[1-exp(-(gamma+z)t)]/(gamma+z). Its derivative

h_t'(z) = gamma*[1-exp(-(gamma+z)t)]/(gamma+z)^2
         + z*t*exp(-(gamma+z)t)/(gamma+z) > 0.

Therefore sign P(t)=sign(A-B) for every t>0 in this exact constant-coefficient, equal-S, ZERO-initial-pion system. The source-typed local separating threshold is:

X_star(T)=a/(a+b) = 1.5*Fc(T)/[1.5*Fc(T)+1.7].

Thus for X<X_star pion conversion increases neutron fraction; for X>X_star it decreases neutron fraction, and at equality this local pion contribution vanishes. Fc(T)>1 implies X_star(T)>0.46875 at finite T>0, with formal limits X_star ->1 as T->0 and ->0.46875 as T->infinity.

No conclusion about full time-varying 10D trajectories is implied: actual T,X,n_B and S vary, initial pion densities are small but nonzero, after PBH evaporation S vanishes, other species and PBH backreaction matter.

## 3. Exact local steady-state and charge-blind bias

Under same constant coefficients and source S:

n_minus_inf=S/(gamma+A), n_plus_inf=S/(gamma+B),
n_minus_inf/n_plus_inf=(gamma+B)/(gamma+A).

Equal production into pi-minus/pi-plus therefore generally creates UNEQUAL steady-state densities if A != B. For A>B, pi-minus has higher effective removal and n_minus<n_plus. This clarifies the exact conceptual difference between splitting a GROUPED PRODUCTION RATE in half and assuming the resulting charge DENSITIES are each half of a grouped density.

P_inf= S*gamma*(A-B)/[n_B*(gamma+A)*(gamma+B)].

Compare with an explicit charge-blind approximation keeping the TRUE grouped steady-state density g=n_minus_inf+n_plus_inf and assigning n_minus=n_plus=g/2 INSIDE the pion neutron reaction (a separate approximation, not E5). For A!=B, the exact attenuation ratio is

P_inf/P_blind = 2*gamma/[2*gamma+A+B] in (0,1).

So the equal-DENSITY approximation overstates the absolute steady pion rate by factor (2gamma+A+B)/(2gamma) under THIS idealization. At fixed background and zero initial pion densities, common-S to S/2 (the E5 pion injection comparator only) halves this local component at all times; it does not halve the full nonlinear physical 10D outcome or beta contour.

## 4. Numerical source-constant controls (conditional, not a 10D experiment)

Using the exact author constants and SI unit conversion for a source-only frozen-temperature illustration: 1 mbarn=1e-31 m^2, sigma*v=(sigma as area)*c, n_gamma=(2zeta3/pi^2)*(T_MeV*MeV_J/(hbar*c))^3, n_B=eta_B*n_gamma.

The following intentionally FIXES X=0.15 at all T; it is NOT an actual author's X_n(T) PBH trajectory:

| T MeV | X_star(T) | n_minus_inf/n_plus_inf | P_inf/P_blind, same grouped density |
|---:|---:|---:|---:|
| 0.0781852706883 (author T_nuc) | 0.620978 | 0.999985 | 0.999991 |
| 1 | 0.515978 | 0.981040 | 0.986632 |
| 5 | 0.490245 | 0.408936 | 0.391935 |
| 10 | 0.484008 | 0.225969 | 0.076028 |

The local response at high illustrative T can be strongly charge-asymmetric even with equal source. These are neither observed PBH dynamics nor uncertainty bars for Wu–Xu.

Optional separate WEAK-EQUILIBRIUM track assumption X_eq(T)=1/[1+exp(Q/T)] with Q=m_n-m_p=1.29333234 MeV. Equality X_eq(T)=X_star(T) becomes:

1.5*Fc(T)*exp(Q/T)=1.7.

Fc(T) and exp(Q/T) strictly decrease with T>0, their product decreases continuously from infinity to 1, and 1.7/1.5 lies strictly between: unique positive crossing. Bisection gives T_cross=16.6553673421359 MeV with X_eq=X_star=0.480596602678145. It is a mathematically exact CONDITIONAL frozen-local/weak-equilibrium sign crossover only, NOT a transition established along the real cosmic PBH trajectory or a validated BBN observation.

Independent numerical arithmetic checks on source constants in V8 and a separate Python numerical environment agree at stated precision; finite-time signs were checked at 10 tau_pi for positive and negative cases. No original Julia run or physical Hawking injection model executed.

## 5. Reproducible controls and scientific gates

Reproducer: research/mech-s10/2026-11-17/code/mech_s10_rot003_pion_local_kinetics_source_auditor.py, Git commit bb93f1fe18b7feca8ee4a30ca0b796a36ef0f799; Git blob 82c1faecb9462714db75fb2f8d7e39ddacddde1d, exact 5733 characters.

It accepts the two original author Julia source files, requires both original Git blob SHA1 identities and the 7+13 exact source contracts before any output, and computes frozen coefficient examples and the conditional weak-equilibrium crossover with standard-library Python only. Usage:
python3 -I mech_s10_rot003_pion_local_kinetics_source_auditor.py /path/main-scan.jl /path/tool_script-parameters.jl

Script was written to GitHub and fetched back byte-identically; the direct V8 original-source contract and independent numeric calculations were executed. Full end-to-end local Python execution of script with TWO original raw source files was not performed because those files were available via connector, not local Python mounting. DO NOT CALL a full binary source-script replay PASS. This limited reproduction gap does not alter the independent exact hand derivation and read-only checked constants.

The already-approved separate T2R scope is 68 original native Julia calls by one authorized GPT-family executor (j22,j62 orig/E5). Transfer/one-run lease to Mech-S10 remains unconfirmed; no existing permission authorizes this additional local result as a new native experiment. T3 bounded source review LT9 delivered; AUD3 source-only reviewer PASS_WITH_GUARDS; REC13 source table 10/10 identity (official CURRENT only); E4 physical hadronizer, Wu–Xu Fig5 historical compiled selector and physical Yp remain HOLD.

No new Julia, BlackHawk, PYTHIA, GitHub Actions original runtime, source paper error adjudication, contact to authors, independent external I3, physical beta shift or novelty claims.

FINAL: ORIGINAL_SOURCE_PION_LOCAL_KINETICS_EXACT_PASS / EQUAL_SOURCE_NOT_EQUAL_STEADY_DENSITY / LOCAL_FINITE_TIME_XSTAR_SIGN_THRESHOLD / QUASI_STEADY_EQUAL_DENSITY_BIAS_IDENTITY / WEAK_EQ_LOCAL_CROSS_16P655367_MEV_ONLY / FULL_10D_E4_HOLD / T2R_LEASE_HOLD / NO_NEW_NATIVE_EXEC / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
