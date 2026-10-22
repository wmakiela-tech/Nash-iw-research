# LT5 — obrót 9: obserwabla zdarzenia, adjoint z ruchomą chwilą końcową i dokładny warunkowy certyfikat fixed-T

artifact_id: LT5-EVENT-ALIGNED-TARGET-ADJOINT-HOMOTOPY-FIXED-T-GATE-001_20261023
date: 2026-10-23
owner: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
document_class: EXACT_CONDITIONAL_CLASSICAL_THEOREM / MONOGRAPH_CH6_FOUNDATION_BRIDGE / TWO_COUNTEREXAMPLES / INDEPENDENT_NUMERIC_TEST
authority: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_PBH_UPGRADE
status: SELF_PROVED_AND_INDEPENDENT_NUMERICAL_CHECK / MATHEMATICAL_REFEREE_PENDING
bw_ingestion_event_id: UNKNOWN / NOT AUTOMATIC
manuscript_version: LT REV020 authoritative, candidate REV021 staged but NOT issued
manuscript_mutated: NO
sources: current local LT5 Ch6 and Ch7; MT13 and Mech-S7 source documents; mature event sensitivity / adjoints / saltation literature

## 0. Why this is not a ninth variant of noisy qubit feedback

The LT5 function is to evolve a coherent living theory monograph, not maximize turn count in one quantum error-syndrome toy model. Other cells have already closed the relevant unrestricted/noisy Pauli flag recovery and most simple quantum instrument bridges:
- PRF11 R18: full-CPTP unrestricted noisy binary-syndrome diamond recovery.
- LT5 ROT08: cost-defined randomized I/Z-only correction via exact Bayes fractional knapsack.
- INT8 ROT009, Geeky-S10 compatibility frontier: legal qubit source-target bridges on restricted families, NO full-classical reset identity.
- PRF11 R19: mature reachable-subspace model identifiability and noisy new-intervention target retrieval.
- MT13: exact source-restricted directional-rate nonidentifiability from one neutron trajectory, and conditional two-preparation identification.

These do NOT settle the practical analytic issue below, central to *Chapter 6*: a physical-source code may compare its observables at a *fixed temperature* T_nuc instead of fixed time t or fixed scale factor a. An existing fixed-time adjoint and Gronwall estimate can target the wrong functional if the event time moves with model assumptions or numerical error.

The question is NOT to reproduce Wu–Xu Julia or establish a PBH exclusion. It is a sharp, source-typed question about which terminal functional the current monograph actually estimates.

## 1. Current manuscript, source and prior art read before derivation

LT REV020 "Opisy efektywne w układach fizycznych — monografia robocza — rozdziały 1–7" §6.7–6.9 has the fixed-time adjoint formula (6.10), the exact secant identity (6.11), and finite-time Gronwall (6.12). §6.10–6.12 correctly withhold full BBN Y_p and D/H. §7.9's physical target gate remains open. The candidate LT5 editorial §6.10a already requests accepted-step active-source and fixed-T comparison, but not a *complete event-conditioned adjoint*.

MT13 2026-10-23 four-cell fixed-T comparison quantifies the **needed** global per-cell neutron endpoint error
    epsilon_J < 6.33356560556e-6
to preserve both signs of specified source-law contrasts. No code has CERTIFIED this accuracy. MT13 also gives a straightforward fixed-temperature Lipschitz error bound, but not a fully general exact event-endpoint source sensitivity identity across a homotopy of ODE models:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_frontb_2x2_state_readout_precision_gate_001.md

Mech-S7 ROT002 proves a fixed-a target is not interchangeable with the source-native fixed-T readout, and distinguishes frozen common background from separately computed numerical backgrounds:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-22/mech_s7_frontb_common_background_target_gate_002.md

MT13 on one-trajectory nonidentifiability of A,B concerns a different input/rate inference question:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_frontb_directional_rate_nonidentifiability_two_excitation_gate_001.md

External mature scientific hosts, intentionally subtracted in advance:
- Corner, Sandu & Sandu, *Adjoint Sensitivity Analysis of Hybrid Multibody Dynamical Systems* (arXiv 1802.07188, 2018). Event-time sensitivity and adjoint jumps, https://arxiv.org/abs/1802.07188 .
- *Modeling and sensitivity analysis methodology for hybrid dynamical system*, Nonlinear Analysis: Hybrid Systems 31 (2019), pp 19–40, DOI https://doi.org/10.1016/j.nahs.2018.07.003 .
- Kong et al., *The Salted Kalman Filter*, Automatica 131 (2021), 109782, arXiv https://arxiv.org/abs/2007.12233 . Event/hybrid sensitivity as classical host.
- Standard ODE sensitivity, implicit function theorem, adjoint calculus, Gronwall. The case of a terminal guard **without a jump/reset** is simpler than full hybrid saltation; we do NOT import a jump formula without its reset-map hypotheses.

Nothing here has a novelty or physics-discovery priority claim.

## 2. Exact FINITE-difference identity for two event-aligned scalar readouts

Consider two C¹ trajectories z_i(t)=(X_i(t),T_i(t)) defined on a common time interval containing both event times. Let T_* be a fixed threshold, crossed exactly once with T_i strictly monotone:

    T_0(tau_0) = T_1(tau_1) = T_*.

Define e_X(t)=X_1(t)-X_0(t), e_T(t)=T_1(t)-T_0(t).

For tau_1≠tau_0 set

    bar_Xdot_1 = (tau_1-tau_0)^(-1)
                 integral_(tau_0)^(tau_1) dot X_1(s) ds,
    bar_Tdot_1 = (tau_1-tau_0)^(-1)
                 integral_(tau_0)^(tau_1) dot T_1(s) ds.

These definitions also have continuous limits at tau_1=tau_0; in the coincident case e_T(tau_0)=0 and the identity below is direct. If T_1 monotone, bar_Tdot_1 !=0.

**THEOREM LT5-9.1 — exact event-secant identity:**

    Delta J_event := X_1(tau_1)-X_0(tau_0)
       = e_X(tau_0)
        - (bar_Xdot_1/bar_Tdot_1) e_T(tau_0).          (2.1)

Proof. T_1(tau_1)-T_1(tau_0)
= T_* - [T_0(tau_0)+e_T(tau_0)]
= -e_T(tau_0)
=bar_Tdot_1 (tau_1-tau_0).
Similarly X_1(tau_1)-X_1(tau_0)
=bar_Xdot_1(tau_1-tau_0).
Add the latter to e_X(tau_0) and substitute the first identity. QED.

If |dot X_1|<=L_X and |dot T_1|>=m_T>0 throughout the segment, with temperature monotonic, then

    |Delta J_event|
      <= |e_X(tau_0)|+(L_X/m_T)|e_T(tau_0)|.         (2.2)

This is the MT13-style sufficient norm guard; (2.1) is stronger because it retains the sign and possible cancellation between direct state and clock terms. The entire formula is deterministic; its use with random temperature requires a specified stochastic event experiment and cannot be transferred by relabeling variables.

**No event crossings or no transversality:** if T_1 is non-monotone or the crossing is not unique, there may be multiple legal tau or a grazing event. Neither (2.1) in this simple quotient nor derivative formulas below can be applied without further branch conventions and event hypotheses.

## 3. Two falsifiers of treating fixed time and fixed temperature as the same target

On t>=0 set X(0)=0,T(0)=2,T_*=1 and constant positive Xdot and negative Tdot.

**Falsifier A — identical WHOLE X(t) histories, different fixed-temperature goal:**
- Model 0: Xdot=1,Tdot=-1, event tau_0=1, J_0=1.
- Model 1: Xdot=1,Tdot=-2, event tau_1=1/2, J_1=1/2.

They have X_0(t)=X_1(t)=t for ALL t. Hence at every common time the X error e_X(t)=0. Nevertheless the event-aligned endpoint error is J_1-J_0=-1/2. Equation (2.1) gives:
  e_T(tau_0)=-1, bar_Xdot_1=1,bar_Tdot_1=-2,
  Delta J=0-(1/-2)*(-1)=-1/2.
Thus even exact equality of the full time history X(t) does not identify X at a *different clock* unless T(t) is also source-matched.

**Falsifier B — large fixed-time difference, IDENTICAL fixed-temperature goal:**
- Model 0: Xdot=1,Tdot=-1, tau_0=1,J_0=1.
- Model 1: Xdot=2,Tdot=-2, tau_1=1/2,J_1=1.

At common t=tau_0, e_X=1 and e_T=-1; (2.1) yields Delta J=1-(2/-2)*(-1)=0. A report of |e_X|=1 at fixed time would falsely suggest a change in the actual event target. This example is a **pure clock reparameterization** of the parametric trajectory X(T).

Both are mathematically exact toy ODEs and say NOTHING about whether the physical Wu–Xu backgrounds actually differ this way.

## 4. Local terminal event functional and its geometric meaning

Let z(t;theta)∈R^n solve a smooth initial-value problem

    z_dot=f_theta(z,t),    z(t0;theta)=z0(theta),

with f_theta C¹ in z,theta (and sufficiently regular in t). Define a scalar guard h(z) and terminal readout g(z), both C¹ with NO explicit theta/time dependence for the present theorem. Suppose for ALL theta∈[0,1] there is a unique smooth event tau_theta in (t0,Tmax), h(z(tau_theta;theta))=0, and the *transversality* denominator satisfies

    |n_theta^T f_theta(z(tau_theta;theta),tau_theta)|
        >= m >0,
    n_theta := nabla h(z(tau_theta;theta)).            (4.1)

The true target is

    J(theta) = g(z(tau_theta;theta)).                   (4.2)

Write xi(t;theta)=partial_theta z(t;theta) at FIXED t. The variational equation is

    xi_dot = A_theta xi + b_theta,
    A_theta = D_z f_theta(z(t;theta),t),
    b_theta = partial_theta f_theta(z(t;theta),t),
    xi(t0)=z0'(theta).                                 (4.3)

Differentiate the guard identity:
    0 = n_theta^T [xi(tau_theta)+f_theta(tau_theta) tau_theta'],
hence
    tau_theta' = -(n_theta^T xi)/(n_theta^T f_theta).  (4.4)

Therefore

**THEOREM LT5-9.2 — exact differential event-terminal projection:**

    J'(theta)= q_theta^T xi(tau_theta),                (4.5)
    q_theta := nabla g
               - [(nabla g)^T f_theta/(nabla h)^T f_theta]
                    nabla h                              (4.6)

evaluated at z(tau_theta;theta),t=tau_theta.

Proof. Chain rule J'=(nabla g)^T(xi+f tau'), substitute (4.4). QED.

**Geometric identity:** q_theta^T f_theta=0. It removes *pure shifts along the physical flow*: an infinitesimal time shift xi=f_theta c produces zero target change after readjusting the event time. The denominator in (4.6) is a source-required event transversality measure; if it vanishes near grazing, the derivative may become ill-conditioned.

For g(z)=X and h(z)=T-T_* in an enlarged state z=(X,T,...), q has X coordinate +1 and T coordinate -dotX/dotT; other coordinates enter through the flow and variational propagation rather than directly in the guard gradient. This is the precise target derivative missing from blindly applying a fixed-time g-gradient.

If g or h depends explicitly on time or theta, an extended-state or explicit derivative version is needed; (4.6) cannot be copied without additional terms.

## 5. Source-typed event adjoint and exact homotopy identity

For each theta solve the **backward** adjoint

    -p_theta_dot=A_theta(t)^T p_theta(t),
    p_theta(tau_theta)=q_theta.                         (5.1)

Differentiate p_theta^T xi using (4.3):

    d/dt (p_theta^T xi) = p_theta^T b_theta.

Integrating gives
    J'(theta)=p_theta(t0)^T z0'(theta)
       + integral_t0^tau_theta p_theta(t)^T
             partial_theta f_theta(z_theta(t),t) dt.  (5.2)

This is an exact sensitivity formula in parameter theta, not a first-order *finite-model-difference* approximation.

Now suppose the two declared vector fields f_0,f_1 and initial states z00,z01 admit a continuously regular and physically LEGAL homotopy
    f_theta=(1-theta) f_0+theta f_1,
    z0(theta)=(1-theta) z00+theta z01,                 (5.3)
with the above unique transversal event for all theta. Then partial_theta f_theta=f_1-f_0 at fixed z,t and z0'=z01-z00. By the fundamental theorem of calculus,

**THEOREM LT5-9.3 — exact finite-difference homotopy event-adjoint:**

  J(1)-J(0)
   = integral_0^1 [p_theta(t0)^T(z01-z00)
       + integral_t0^tau_theta p_theta(t)^T
               (f_1-f_0)(z_theta(t),t) dt] dtheta.    (5.4)

No smallness assumption on f1−f0 is required in (5.4). It follows from the exact derivative (5.2), integrated over the full model path. q_theta must use the EVENT projection (4.6), not the fixed-time gradient nabla g.

**Important legality limitation:** The mathematical interpolation (5.3) may be an UNPHYSICAL mixture of microscopic source laws, couplings or constraints. Formula (5.4) is a source-valid **physical** comparison only if the entire interpolating family remains in the admitted physical model class. Otherwise it is a mathematical decomposition, NOT evidence of a legitimate intermediate PBH dynamics or unique mechanism attribution. Its adjoint weights depend on the entire homotopy trajectory; it is not a per-channel attribution without source-matched f1−f0 and further certificates.

For one fixed theta, a norm estimate follows from ||p_theta(t)|| and ||partial_theta f_theta|| over its own interval, but converting it to *certified* numerical/global model error requires a validated norm and state interpolation with acceptable sources.

### Relationship to REV020 ODE results
LT REV020 equation (6.10) (fixed-endpoint adjoint) is recovered when the terminal time does not depend on theta, in which case the correct terminal condition is nabla g, not (4.6). Equations (6.11)–(6.12) remain valid as fixed-time statements. The current (4.6)/(5.4) is a **typed extension** to the event-aligned target and should be presented as classical ODE/adjoint calculus in an optional compact §6.9a, not as evidence of new physics.

## 6. Independent numerical falsification and reproducibility

Synthetic smooth ODE with state z=(X,T), initial z0=(0.23,2), event T=1, and parameter theta∈[0,1]:
    Xdot = (0.35+0.17theta) X(1-X)+(0.07+0.07theta),
    Tdot = -(1+0.4theta)(1+0.1X).
The field interpolates exactly between endpoint sources and is smooth/transversal throughout the selected path. Time horizon 1.2. All model states are pure synthetic scalars, not source plasma/cosmology.

For five theta values direct solve_ivp(DOP853) event integration, variational equation (4.3), backward adjoint (5.1), and finite differences give:

| theta | event time tau | J=X(tau) | exact variational J' | numerical adjoint J' |
|--:|--:|--:|--:|--:|
| 0.00 | 0.97109447397 | 0.36848721700 | 0.04944501678 | 0.04944501678 |
| 0.20 | 0.8987702528 | 0.37763888894 | 0.04234590734 | 0.04234590734 |
| 0.50 | 0.8084536989 | 0.38906403883 | 0.03424988271 | 0.03424988271 |
| 0.80 | 0.7346315153 | 0.39839887517 | 0.02826862199 | 0.02826862199 |
| 1.00 | 0.69247692663 | 0.40372743118 | 0.02511031168 | 0.02511031168 |

Adjoint and forward sensitivity agree below 5e−11. Two-sided parameter differences agree at central theta values to <2e−8 and near endpoints to <1e−6 for step 1e−5.

Exact endpoint change:
   J(1)-J(0) = 0.03524021417371348.
Gauss-Legendre 16-node integration in theta of the **independently calculated variational sensitivity**:
   0.03524021417366954.
Absolute difference:
   4.394e−14.

The exact finite event-secant identity (2.1) supplies independent decomposition at the first model's event time:
   e_X(tau_0)=+0.10989439686602381,
   e_T(tau_0)=−0.4072643896283009,
   clock/event-time correction=−0.07465418269229893,
   resulting Delta J=+0.03524021417371348,
   secant identity residual <1.2e−14.

Thus approximately 68% of the raw fixed-time X difference in this example cancels when correctly aligning the event. This percentage describes this *synthetic* ODE alone, NOT the actual Wu–Xu data.

**Reproduction code** (direct write/readback PASS; exact same equations and regression asserts):
https://github.com/wmakiela-tech/Nash-iw-research/blob/063e084ecc87145623ac02dccf5bde9c4d206153/research/lt5/2026-10-23/reproduce_lt5_event_conditioned_adjoints_001.py
Script SHA (blob readback): 99c34b8b65e16fbd8a23ffb9c459bb9c39fe4c30.
Requirements: NumPy, SciPy. No Monte Carlo, no OCR, no outside data. The numerical test is not a proof of mathematical generality and does not execute original Julia source.

## 7. Specific implication for Front B acceptance, not a claim of physical validation

The current four-cell Wu–Xu diagnostic source-reported conditional endpoint signs are to be compared at the **same T_nuc**, with distinct event times along separately integrated numerical backgrounds. Let Xhat_i be an approximation of the exact model's X_i at its own approximate T crossing. Suppose its total ENDPOINT error is rigorously bounded
    |Xhat_i(hat tau_i)-X_i(tau_i)| ≤ epsilon_J
for each of the four cells. Then the error in each pairwise difference is ≤2epsilon_J. MT13's source-reported smaller absolute contrast magnitude ≈1.26671312111e−5 requires
    epsilon_J < 6.33356560556e−6
to certify that both signs are preserved.

This demands a bound on the *event-aligned target*, not merely the state error at one arbitrary fixed numerical time. When a numerical trajectory and exact one have bound |e_X(tau)|≤epsilon_X and |e_T(tau)|≤epsilon_T around the true event and transversality / state speed give L_X,m_T>0, (2.2) gives the sufficient component
    epsilon_J ≤ epsilon_X + (L_X/m_T) epsilon_T + epsilon_interp,   (7.1)
with epsilon_interp a separately declared discrete root/interpolation contribution that must not be counted twice. If the approximate continuous interpolant already defines hat tau and the uniform state/temp bounds refer to it, epsilon_interp may be zero; if the endpoint uses a distinct linear interpolation in Q/T, its error is not zero by declaration.

Therefore a *conditional sufficient numerical test* is
    epsilon_X+(L_X/m_T)epsilon_T+epsilon_interp
      < 6.33356560556e−6.                            (7.2)

None of epsilon_X,epsilon_T,m_T,L_X,epsilon_interp for the ORIGINAL source-active interval below M=1e9g has been certified by this note, and no guarantee for physical Y_p/D/H has been obtained. There may be source populations continuing to react after fresh emission stops (REC10 ROT08); setting post-emission hadron forcing to zero would require its own source proof.

The conditional sensitivity formula (5.4) also does NOT turn a four-case factorial interaction into an identified microscopic cause. MT13's directional-rate one-trajectory nonidentifiability and PRF11's restricted-subspace intervention nonmap remain in force.

## 8. Prior-art subtraction and editorial decision

**Classical host:** implicit function theorem for event time, event-time sensitivity, sensitivity adjoints, moving-boundary derivatives, and the established saltation/hybrid ODE family. The no-reset event-readout theorem is an elementary specialization. Its exact homotopy finite difference simply integrates an existing exact derivative; the phrase "exact" is not proof of mathematical originality. There is no novel gravity/quantum mechanism or PBH exclusion.

**Recommended manuscript treatment:** Include a compact, fully typed §6.9a between the existing fixed-time adjoint and the real hadron source case. Present (2.1), (4.6), (5.4) and the simple counterexample of equal X(t) but unequal X(T_*); refer to the GitHub note and reproducibility code. Leave the four-cell numeric sign threshold only in the time-stamped §6.10a status note. Do not insert a separate free-standing theory chapter or change Ch.6 theorem numbers before the global editorial normalization.

**Independent mathematical review requested only if material:** REC10/SW may test signs in q_event, regularity/guard assumptions, the legality of the homotopy, and exact versus fixed-time distinction. MT13/Mech-S7 may use (7.2) as a type-safe acceptance condition if an accepted-step fixed-T source trace and rigorous solver bounds become available; NOT a new forced task.

### Explicit negative knowledge:
- SAME X(t) AT EVERY COMMON t does NOT imply SAME X AT EACH MODEL'S T=T_*.
- LARGE FIXED-TIME TARGET ERROR does NOT imply LARGE EVENT-ALIGNED ERROR.
- FIXED-TIME ADJOINT TERMINAL nabla g IS NOT GENERALLY THE CORRECT EVENT-TARGET TERMINAL GRADIENT.
- PHYSICAL EVENT TRANVERSALITY and UNIQUE CROSSING are load-bearing.
- f_theta CONVEX HOMOTOPY AS ALGEBRA != LEGAL INTERMEDIATE PHYSICAL MODEL.
- NEED epsilon_J CERTIFICATION != ALREADY CERTIFIED GLOBAL SOLVER ERROR.
- NO FRESH PBH EMISSION != NO RESIDUAL HADRON CONVERSION.
- NUMERIC SOURCE-PROXY != Y_p / D/H or a physical PBH bound.

**Outcome:** mathematically complete conditional event/adjoint analysis, synthetic regression PASS, external mature host identified, standalone reproducibility committed; scientific acceptance PENDING and REV020 untouched.
