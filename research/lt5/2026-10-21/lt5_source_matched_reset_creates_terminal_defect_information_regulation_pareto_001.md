# LT5 — Obrót 5: Source-matched reset, creation of terminal defect, and exact information–restoration frontier

Date: 2026-10-21.
Owner: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5.
Return ID: LT5-SOURCE-MATCHED-RESET-DEFECT-INFORMATION-RESTORATION-001.
Status: EXACT_CONDITIONAL_CLASSICAL_DERIVATION / SOURCE-TYPED COUNTEREXAMPLE / MATURE_HOST_SPECIALIZATION / INDEPENDENT_REFEREE_PENDING.
Exposition: PUBLIC_SAFE. No confidential initial states, datasets, physical interpretations or unpublished manuscript bytes.
Authority: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_CLAIM / NO_BW_AUTO_INGEST.
Relationship: follows LT5 turns 1–4; monograph NOT MUTATED.

## 0. The issue: information changes the future quantity being predicted

Earlier LT5 notes held the target mapping fixed during a measurement or treated only a translated scalar state. INT8 and Geeky-S10 established independently that a deterministic reset readout changes the source-matched terminal map, and the original pre-reset target cannot be inserted into the new measurement protocol without a type error.

Here we isolate an exact, testable phenomenon that is different from weak-sensor energy/conditioning: a deterministic readout reset can **create a nonzero terminal target from an initial-state family on which that very target was identically zero**. The record may identify the preparation better while the readout itself degrades the target. It is logically wrong to describe this as a physical observation or discovery; it is a consequence of explicitly typed linear operations.

The complete minimax treatment below shows a sharp information–restoration trade-off in this model. It belongs to classical set-membership estimation, 1-center recovery, and constrained output-feedback control. NO new mathematical priority is claimed.

## 1. Source model, roles and domain

Let X=R^n with Euclidean inner product, let F:X->X be a fixed known linear evolution map from just after an intermediate measurement to terminal time, and let ell in X be the scalar terminal readout.

Choose a unit measurement/reset direction e in X, ||e||=1. Fix a compact, convex, centrally symmetric set of admissible initial preparations K subset X, satisfying

    ell^T F x = 0     for ALL x in K.                        (1.1)

Thus the terminal target is **identically zero on K without the intermediate measurement reset**. This is a target-relative equality on K, not a full-operator identity on X.

The measurement instrument is declared as a CLASSICAL deterministic reset plus separately bounded numerical readout noise:

    b = s e^T x + eta,   |eta|<=delta,   delta>=0,
    x+ = Q_s x,          Q_s=I-s e e^T,                   (1.2)

where 0<s<1, and eta affects the numerical record ONLY. The reset is driven by the *ideal* pre-readout state, not by the observed noisy b. The instrument has no stochastic physical back-action. Its status as a quantum instrument is NOT asserted.

The physical terminal target after this actual reset, before control, is

    z_s(x) = ell^T F Q_s x.                               (1.3)

A separately declared terminal scalar actuator supplies a correction u(b) with

    |u(b)|<=B,   B>=0.

The final target residual is z_s(x)-u(b). We permit all measurable one-stage feedback rules; the source map F and the actuator port are known and fixed, and the actuator does not retroactively change the measurement. This is HARD terminal amplitude B, not a bound on feedback gain.

Write

    gamma := ell^T F e,
    H := max_{x in K} |e^T x|.

Because K is compact convex centrally symmetric, its image e^T K is exactly [-H,H]. If H=0 or gamma=0 the post-reset target remains zero for every admissible preparation and no interesting trade-off is present. Otherwise assume H>0 and gamma!=0.

## 2. Rank-one exact identity: an invariant is broken by the readout

**Proposition LT5-5.1 (source-matched rank-one defect).** Under (1.1)–(1.3), every x in K satisfies

    z_s(x) = -s gamma (e^T x).                             (2.1)

Consequently

    sup_{x in K} |z_s(x)| = s |gamma| H.                   (2.2)

The full-space difference between the terminal maps with and without reset is

    ell^T F Q_s - ell^T F
      = -s (ell^T F e) e^T,                               (2.3)

a rank-at-most-one functional, with Euclidean operator norm s|gamma|.

Proof. Substitute Q_s=I-s ee^T into (1.3) and use (1.1). Equation (2.3) is a rank-one product, and its operator norm follows from ||e||=1. Sharpness over K in (2.2) follows from the definition of H. QED.

**Type-safe interpretation:** The reset can change what the terminal observable IS; even if a numerical readout improves information about x, it may itself generate the measured terminal defect. It is forbidden to replace (2.1) by the pre-reset zero target in a control computation, or to call this effect an invariant of an unrelated physical theory.

## 3. Two exact minimax quantities: identification and restoration

The readout depends on x only through theta=e^T x in [-H,H]. Its scalar observation law is

    b=s theta + eta,  |eta|<=delta,                       (3.1)

and the source-matched target is z_s=-s gamma theta.

Define the passive estimation radius for theta:

    E_theta(s)
       := inf_{estimators f} sup_{|theta|<=H,|eta|<=delta}
                     |theta-f(s theta+eta)|.              (3.2)

Define the best controllable terminal residual:

    J(s,B)
       := inf_{|u(b)|<=B} sup_{x in K, |eta|<=delta}
                    |ell^T F Q_s x-u(s e^T x+eta)|.       (3.3)

**Theorem LT5-5.2 (exact simultaneous information and post-reset control).** For every 0<s<1,

    E_theta(s) = min(H, delta/s),                         (3.4)

    J(s,B) = max{ |gamma| min(sH,delta),
                  |gamma| sH-B }.                        (3.5)

This includes delta=0 and B=0. The right side is nonnegative because the first term is nonnegative.

**Proof of (3.4).** For v=min(H,delta/s), states theta=+v and theta=-v with errors eta=-sv,+sv generate the same b=0; no estimator can give worst-case error below v. Conversely every feasible b defines a posterior interval

    I_b = [-H,H] intersect [(b-delta)/s,(b+delta)/s].

Its half-width is <=v. The midpoint estimator attains a uniform error <=v. QED.

**Proof of (3.5).** The uncorrected terminal target is a scalar a theta with a=-s gamma; its magnitude reaches A=|gamma|sH. For the same indistinguishable preparations +/-v at b=0, the terminal target takes values +/-av. Any common correction suffers error >=|a|v=|gamma|min(sH,delta). For a state attaining the endpoint |a theta|=A, bounded actuator amplitude forces error >=A-B. These are the two lower bounds.

For upper bound, given b let I_b=[L_b,U_b], center c_b=(L_b+U_b)/2, half-width r_b=(U_b-L_b)/2. Choose the terminal correction

    u*(b)=clip(a c_b, -B, B).

Then its conditional worst-case residual is exactly

    |a| r_b + (|a c_b|-B)_+.

If |a c_b|<=B this is <=|a|v. If |a c_b|>B, this is |a| max(|L_b|,|U_b|)-B<=A-B. Hence every b has risk <=max(|a|v,A-B), matching the lower bounds. QED.

**Distinction from LT5 turn 2:** (3.5) is the old scalar Chebyshev recovery structure applied only **after** deriving the actual target map a=-s gamma from the reset. The source-derived dependence of a on s is essential. We do not present the scalar minimax algebra as a newly discovered mathematical method.

## 4. Joint information requirement: exact feasible frontier

Suppose the task contract additionally REQUIRES a guaranteed reconstruction accuracy epsilon for the original preparation coordinate theta,

    E_theta(s) <= epsilon,
    0<epsilon<H.                                           (4.1)

Assume delta>0 and 0<s<1. By (3.4), (4.1) is feasible precisely when

    delta/epsilon < 1,                                    (4.2)

and the allowed strengths are s in [delta/epsilon,1), with s_min=delta/epsilon.

For fixed gamma,H,delta,B, both terms inside max in (3.5) are nondecreasing in s. Therefore the smallest guaranteed terminal residual among instruments meeting (4.1) occurs at s_min:

**Corollary LT5-5.3 (joint information–restoration frontier).**

    inf_{0<s<1 : E_theta(s)<=epsilon} J(s,B)
      = max{ |gamma| delta,
              |gamma| H delta/epsilon - B }              (4.3)

when delta>0 and delta/epsilon<1.

In particular, even with an arbitrarily large but finite terminal actuator B capable of canceling any **known** target value, the irreducible worst-case error under the declared independent bounded readout disturbance is |gamma|delta. A stronger readout strength does not reduce this floor, because the quantity created by the reset scales with the signal in the same proportion.

**Proof.** Since epsilon<H and s>=delta/epsilon, we have sH>delta; hence |gamma|min(sH,delta)=|gamma|delta. The other term |gamma|sH-B increases with s. Its minimum over feasible s is attained at s_min. QED.

No promise is made about an actual detector's noise law. If delta scales with s, or if the reset is driven by noisy observations, the constraint and frontier change.

**Noiseless singular limit.** When delta=0, every s>0 gives E_theta(s)=0 (the record b=s theta can be divided by s). At s=0 the record is constant and the minimax estimation error is H. For B=0 and gamma!=0, J(s,0)=s|gamma|H>0 for every s>0 but inf_{s>0}J(s,0)=0 as s->0; the infimum is not attained within the positive-strength instrument class. This is algebraic identifiability without a uniform conditioning guarantee, consistent with the INT8/Geeky-S10 warnings. It is NOT physically free exact information under finite noise.

## 5. Explicit two-coordinate source-valid witness

Set X=R^2 with state x=(q,p), no free evolution F=I, unit e=(1,0), terminal row ell=(-1,1), and admissible initial preparations

    K={(theta,theta): -R<=theta<=R}.

The original terminal target is p-q=0 for every preparation. A strength-s readout measures q and resets ONLY q:

    b=s q+eta=s theta+eta,
    (q+,p+) = ((1-s)theta,theta).

The source-matched terminal target is

    p+-q+ = s theta.                                     (5.1)

Here gamma=ell^T e=-1 and H=R, and therefore

    J(s,B)=max{min(sR,delta),sR-B}.                       (5.2)

The measurement has **created a terminal mismatch** from a perfect-cancellation manifold K. If a separate terminal actuator changes p by -u after the readout, (5.2) is the exact best post-actuation residual.

For R=1, delta=0.08, B=0.15:
- s=0 (no measurement/reset): target identically 0; J=0 but no information about theta;
- s=0.05: E_theta=1 and J=0.05;
- s=0.10: E_theta=0.8 and J=0.08;
- s=0.30: E_theta=0.266666... and J=0.15;
- s=0.80: E_theta=0.1 and J=0.65.

Require E_theta<=0.25. Then s_min=0.32 and exact optimal J=min_s J(s,0.15)=max(0.08,0.32-0.15)=0.17. If B increases to 0.30, the best risk is max(0.08,0.32-0.30)=0.08. Even this larger terminal actuator cannot remove the 0.08 information-noise floor when nontrivial original-state identification is required.

**Early-versus-late port (optional typed extension):** If the same initial (q,p) is additionally subject to an early scalar p-shift u0 chosen before the q readout, |u0|<=B0, while the late p-shift u1(b) has |u1|<=B1, the terminal residual is s theta-u0-u1(b). For centered theta∈[-R,R] the exact minmax is STILL (5.2) with B=B1, independent of B0. Any fixed u0 merely shifts the target center; choosing u0=0 is optimal. Early nominal actuation budget is not interchangeable with late action in response to the future record.

The early p shift has no effect on the q readout or the q reset, so this is a correctly typed two-stage source experiment. This is an application of LT5 turn 4, not an independent discovery.

## 6. Numeric falsification checks

For fixed parameters s,R,delta,gamma,B, enumerate a fine grid of all feasible b in [-sR-delta,sR+delta]. At each b compute I_b exactly; calculate

    risk(b)=|s gamma|(U_b-L_b)/2
            + max(|s gamma (U_b+L_b)/2|-B,0).

Compare max_b risk(b) with (3.5). A Python/NumPy control with 20,001 grid nodes produced:

    (R,delta,gamma,B,s)     exact J      gridded J
    (1,.08,2,.15,.05)       .1000000     .1000000
    (1,.08,2,.15,.10)       .1600000     .1600000
    (1,.08,2,.15,.30)       .4500000     .4500000
    (1,.08,2,.15,.80)      1.4500000    1.4500000
    (.7,.04,-1.1,.2,.35)    .0695000     .0695000
    (1,.08,2,.6,.32)        .1600000     .1600000
    (2,.3,.75,.4,.4)        .2250000     .2250000

All seven absolute displayed gaps were zero. These are sanity checks for arithmetic/sign/parameter choice, not proofs or physical runtime tests. The executable reference implementation:

    import numpy as np

    def exact(R, delta, gamma, B, s):
        return max(abs(gamma)*min(s*R,delta),
                   abs(gamma)*s*R-B)

    def grid_check(R,delta,gamma,B,s,n=20001):
        b=np.linspace(-s*R-delta,s*R+delta,n)
        lo=np.maximum(-R,(b-delta)/s)
        hi=np.minimum(R,(b+delta)/s)
        feasible=(lo<=hi+1e-10)
        center=(lo[feasible]+hi[feasible])/2
        rad=(hi[feasible]-lo[feasible])/2
        a=-s*gamma
        loss=abs(a)*rad+np.maximum(abs(a*center)-B,0)
        return np.max(loss)

    cases=[
        (1,.08,2,.15,.05),(1,.08,2,.15,.1),
        (1,.08,2,.15,.3),(1,.08,2,.15,.8),
        (.7,.04,-1.1,.2,.35),(1,.08,2,.6,.32),
        (2,.3,.75,.4,.4)]
    for row in cases:
        assert abs(exact(*row)-grid_check(*row))<1e-8
    print("SEVEN_SYNTHETIC_CHECKS_PASS")

**Important grid qualification:** maximization of the posterior error over gridded b is an approximate validation; the exact result is established by the independent algebraic proof in §3.

## 7. Host subtraction, cross-cell awareness, failure boundaries

**Source-native project record checked before derivation:**
- LT5 turns 1–4 in public GitHub: static gain, hard scalar amplitude, vector constrained Chebyshev dual, causal early-vs-late control.
- REC10 ROT03: independent PASS_WITH_GUARDS applies ONLY to LT5 turn 1, not automatically to later claims.
- INT8 2026-10-21 weak protocol cross-front note: correct terminal map must include reset Q_s; no combination of reset C_s and unperturbed m.
- Geeky-S10 2026-10-21: finite common extremal storage implies arbitrary-finite-shot weak record energy <=epsilon V_*, including heterogeneous readout/reset under a finite common-storage condition; no re-opening that theorem.
- PRF11 R14: vanishing unwhitened l2 record energy does not force vanishing *statistical* Gaussian Fisher information without a noise covariance floor. The present deterministic per-shot bounded-error model is distinct; do not transfer it to correlated Gaussian experiments.
- MT13 2026-10-21: vector terminal correction dual/source host; the present scalar target rank-one result does not claim novelty in that front.

**External mature hosts:**
- B. Houska, *Intrinsic separation principles*, Automatica 183 (January 2026), article 112661, DOI 10.1016/j.automatica.2025.112661. Constrained control, information measures and dual-control/separation structure.
- J.S. Baras, N.S. Patel, *Robust Control of Set-Valued Discrete Time Dynamical Systems*, IEEE Trans. Automatic Control 43 (1998) 61–75, DOI 10.1109/9.654887; information-state dynamic programming.
- D.Q. Mayne, S.V. Rakovic, R. Findeisen, F. Allgower, *Robust output feedback model predictive control of constrained linear systems*, Automatica 42 (2006) 1217–1222, DOI 10.1016/j.automatica.2006.03.005.
- Classical deterministic set-membership optimal recovery/Chebyshev center duality, as in LT5 monograph §7.5b and Ettehad-Foucart (2021), DOI 10.1137/20M1328476.

**Subtraction verdict:** identities (2.1)–(2.3) are elementary linear operator algebra. The minimax formula (3.5) and frontier (4.3) use standard scalar optimal recovery and constrained actuation. The worked example is a clear warning against conflating altered target dynamics with sensor-generated information, not an established new theorem family or empirical fact. Literature verification has located primary external hosts but is not exhaustive theorem-to-theorem uniqueness analysis.

**Critical firewalls:**
- ORIGINAL TARGET VANISHES ON K != SOURCE-MATCHED TARGET VANISHES AFTER RESET.
- GOOD IDENTIFICATION OF theta != TARGET PRESERVATION.
- VANISHING TERMINAL RISK AT s=0 != SUCCESS OF RECONSTRUCTION.
- ESTIMATION WITH NOISE FLOOR != PHYSICAL QUANTUM DISTURBANCE THEOREM.
- LOW RESET STRENGTH != UNIFORM ROBUST INFORMATION.
- HARD TERMINAL AMPLITUDE B != STATIC GAIN NORM kappa.
- FIXED BOUNDED READOUT ERROR != GENERAL CORRELATED GAUSSIAN LAW.
- OPERATOR MAP F OF DECLARED CLASSICAL MODEL != GRAVITATIONAL FIELD EQUATION OR NCDG OBSERVABLE.
- REC10 TURN-1 PASS != AUTOMATIC PASS OF LT5 TURN 5.

## 8. Final status / possible monograph value

The exact mathematical claim is bounded, self-contained and reproducible. Its only recommended role in the living monograph is a compact counterexample in the section on time-dependent, operationally defined observations and measurement intervention legality, after separate mathematical referee and author/editorial decision. It cannot prove a physical obstruction and does not warrant a new claim of priority.

The future genuinely difficult seam is the source-validated multi-time case in which the apparatus simultaneously alters the target, the future *availability of actuator ports*, and the observation noise law. A useful mathematical attempt must explicitly construct the causal transition and noise/resource contract before any theorem claim. A slogan about “measurement backaction” is not a substitute.

CUSTODY: GitHub public-safe full body; direct readback required postwrite.
INDEPENDENT REVIEW: PENDING. OWNER ACCEPTANCE: UNKNOWN. BW INGESTION: UNKNOWN.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
