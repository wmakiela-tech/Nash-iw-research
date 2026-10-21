# LT5 / obrót 2 — Exact scalar target recovery–actuation decomposition with bounded terminal authority

**Data:** 2026-10-21
**Cell:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
**Class:** conditional mathematical derivation, host-absorbed candidate; no claim of novelty
**Authority:** NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM / NO_NOVELTY_PROMOTION
**Exposure:** PUBLIC_SAFE; standalone mathematics and synthetic oscillator only
**Custody:** full primary note in GitHub; BW ingestion and independent referee acceptance are separate states

## Abstract

We identify an exact, strictly scoped minimax decomposition that connects target-specific optimal recovery to a physically distinct control constraint: a hard bound on the terminal amplitude of a scalar actuator. This is not the operator-gain bound from the earlier LT5 note (2026-10-20). For centrally symmetric convex uncertainties, a scalar terminal target, a fixed non-invasive linear measurement and a single post-measurement actuation port, the worst-case terminal error attained by arbitrary measurable bounded-feedback policies equals the maximum of (i) the passive radius of information and (ii) the unrecoverable target amplitude after applying the actuator's entire terminal authority. A saturated Chebyshev-center rule attains the bound. The result fails without key type conditions; a vector-target counterexample is given.

The statement belongs to classical set-membership estimation/control and optimal recovery. We give an independent elementary proof for this specialized bridge and do **not** assert mathematical novelty.

## 1. Typed experiment

Let Y=R^n, W=R^p and U=R^q. Let K subset Y and N subset W be **nonempty compact, convex, centrally symmetric** sets: K=-K and N=-N. In particular 0 belongs to each. The unknown preparation y belongs to K; the adversarial observation disturbance eta belongs to N; they can be chosen independently. The measurement, made before the intervention and assumed not to change the source state, is

    b = C y + eta,            C in L(Y,W).

The unknown *scalar* terminal target without intervention is

    t(y) = m^T y,              m in Y.

After acquiring b, the controller selects u=pi(b) in the closed Euclidean ball ||u||_2<=Umax (Umax>=0). The scalar target responds according to a fixed, known linear terminal port a in U:

    z(y,eta,pi) = m^T y + a^T pi(Cy+eta).

There are no other paths from measurement or actuator to the terminal output, and no additional noise after intervention. Any known deterministic baseline is assumed to have been removed or canceled by an independently budgeted feedforward action; subtracting it is not free when it consumes the same bounded actuator.

Define the unlimited-algorithm / limited-actuator minimax error:

    J*(Umax)= inf_{policies pi: ||pi(b)||<=Umax}
              sup_{y in K, eta in N} |m^T y + a^T pi(Cy+eta)|.      (1)

Policies can be nonlinear (including saturation), unlike the norm-bounded *linear gain* F studied in LT5 turn 1. Define

    A := max_{y in K} |m^T y|,      B := Umax ||a||_2,               (2)

    E := max_{v in K, Cv in N} |m^T v|.                              (3)

E is the radius of information for the passive scalar target: the minimax worst-case error of estimating m^T y from b with no restriction on estimator magnitude.

## 2. Theorem: exact informational/actuation decomposition

**Theorem LT5-2.1 (conditional exact identity).** Under the assumptions in §1,

    J*(Umax) = max{ E, A-B }.                                         (4)

The number A-B can be negative; the maximum remains nonnegative because E>=0. Formula (4) holds for a=0 as well, in which case B=0 and J*=A.

**An explicit optimal policy.** For each feasible observation b in C K + N, define its posterior state set and the interval of compatible target values:

    K_b := { y in K : b-Cy in N },
    l(b):= min_{y in K_b} m^T y,
    h(b):= max_{y in K_b} m^T y,
    c(b):= [l(b)+h(b)]/2.                                          (5)

The allowed terminal corrections a^T u fill [-B,B]. Choose the desired *positive* corrective value

    v(b):=clip(c(b), -B, B).

For a!=0 choose

    pi*(b) = -a v(b)/||a||^2,                                     (6)

and pi*(b)=0 when a=0. Off the feasible observation set, define pi*(b)=0. On the feasible set, these maps can be chosen Borel measurable in this finite-dimensional compact-convex setting; measurable minimum/maximum value maps admit such a policy. In particular ||pi*||<=Umax.

**Proof, lower bounds.** The pair of feasible states (v,eta=-Cv) and (-v,eta=Cv), for any v in K with Cv in N, produce the *same observation b=0*. Hence any fixed correction selected at b=0 incurs worst-case absolute error at least |m^T v|. Maximizing gives J*>=E. Separately, a preparation y attaining |m^T y|=A and an admissible noise eta=0 shows |m^T y+a^T pi(b)| >= A-|a^T pi(b)|>=A-B. Thus J*>=max(E,A-B).

**Proof, upper bound.** Fix a feasible b. The possible terminal target is precisely the compact interval [l(b),h(b)]. Put r(b)=[h-l]/2>=0 and c(b)=[h+l]/2. The correction v(b) minimizes the worst-case scalar error over [-B,B], giving

    min_{|v|<=B} max_{t in [l,h]} |t-v|
       = r(b) + (|c(b)|-B)_+.                                     (7)

We claim r(b)<=E: choose endpoint preparations y_high,y_low from K_b. By central symmetry and convexity,

    v=(y_high-y_low)/2 in K.

Their noises eta_high=b-Cy_high and eta_low=b-Cy_low belong to N; hence

    Cv=(eta_low-eta_high)/2 in N.

Consequently r(b)=|m^T v|<=E. Furthermore max(|l(b)|,|h(b)|)<=A.

If |c(b)|<=B, (7) is r(b)<=E.
If |c(b)|>B, (7) is r(b)+|c(b)|-B = max(|l(b)|,|h(b)|)-B<=A-B.
So the optimal conditional error is at most max(E,A-B) for *every* feasible observation b. Taking the worst case and combining with the lower bounds establishes (4). QED.

**Remark on measurability.** The proof of the exact minimax value does not require arbitrary pathological policies: the posterior endpoint maps are measurable for compact convex K,N and a continuous linear C. The stated clipped-center selection is an ordinary deterministic feedback.

## 3. Euclidean balls, connection to existing manuscript and turn 1

For K={||y||_2<=R}, N={||eta||_2<=delta}, R>0, delta>=0:

    A=R||m||_2,
    E=max_{||v||<=R,||Cv||<=delta}|m^T v|
     =min_{w in R^p} [R||m-C^T w||_2 + delta||w||_2].               (8)

The second equality is the known deterministic optimal-recovery duality already in the working LT monograph §7.5b, Theorem 7.9. It is NOT new here.

Then the exact *amplitude-limited* terminal regulation error is

    J*(Umax) =
       max( min_w [R||m-C^T w||+delta||w||],
            R||m||-Umax||a|| ).                                    (9)

Two quantitatively distinct thresholds:
- If B < A-E, actuator shortfall dominates and J*=A-B.
- If B >= A-E, the output error saturates at E: enlarging actuator amplitude alone does not improve the worst-case guarantee.
If E=0, exact cancellation requires B>=A. If a=0, no policy changes the terminal output, even if E=0 and the goal is known exactly.

This does **not** follow by imposing a constraint ||w||<=kappa||a|| on (8). That constraint is the **linear operator gain limit** from turn 1, not an actuator-output amplitude limit. In particular the feasible controller classes differ; one cannot compare the two errors as if kappa and Umax represented the same resource.

## 4. Explicit harmonic-oscillator realization and checked values

Before an intervention at time s, let x'=y, y'=-x, x(0)=0, y(0)=y0, |y0|<=R. Measure

    b=x(s^-)+eta = sin(s) y0 + eta,        |eta|<=delta,

and immediately apply a bounded velocity impulse

    y(s^+)=y(s^-)+u(b),   x(s^+)=x(s^-),    |u(b)|<=Umax.

The system evolves without further intervention to T, giving exactly

    x(T) = sin(T)y0 + sin(T-s)u(b).                                (10)

Thus the typed ports are C=sin(s), m=sin(T), a=sin(T-s). The control is a synthetic ideal impulse, not a physically calibrated instrument. It is different from bounds on impulse energy, intervention duration, sensor back-action or continuous-time rate constraints.

For T=pi/2, s=pi/4, R=1, delta=0.1, Umax=1:

    A=1,
    E=min(1, delta/|sin(s)|)=sqrt(2)/10=0.1414213562373095,
    B=Umax |sin(T-s)|=1/sqrt(2)=0.7071067811865475,
    J*=max(E, A-B)=1-1/sqrt(2)=0.2928932188134525.

The precise threshold Umax=(A-E)/|sin(T-s)| is sqrt(2)-0.2 = 1.2142135623730951. At and beyond it, J*=E until the sensor/noise model is changed. At delta=0, the threshold becomes sqrt(2).

**Comparison with turn 1, NOT the same resource:** with delta=0 and |k|<=1 in the proportional law u(b)=-k b, turn 1 yields an error of 1/2. With this turn's different admissible class |u(b)|<=1, the saturated nonlinear law yields 1-1/sqrt(2). The difference shows why hard actuator amplitude and fixed proportional gain must not be conflated, not an improvement against the same controller budget.

**Brute-force diagnostic validation.** Independent scalar feasibility-grid test (2001 b values; exact interval endpoints and clipped center) compared (4) to conditional worst case:
- (R=1,delta=0.1,C=1/sqrt2,m=1,B=1/sqrt2): exact 0.29289321881345254; grid same.
- (1,0.2,1,1,0.6): 0.4; grid same.
- (1,0,1,1,0): 1; grid same.
- (1,1.5,1,1,0.9): 1; grid same.
- (0.7,0.1,-1.7,-0.8,0.35): 0.21; grid same.
- (0.3,0.6,0,2,0.2): 0.6; grid same.
These synthetic checks validate examples and help catch sign mistakes; proof of (4) is analytic and independent of them.

## 5. Failure modes, exact scope and counterexamples

**(i) Vector target: the scalar identity cannot be lifted by treating ||a||Umax as a universal correction radius.**
Let y range over the unit disk in R^2, b=y noiselessly (C=I), and let the vector terminal target be z=y+(u,0), |u|<=1. There is no information loss (E=0) and the uncorrected target radius A=1; a naive scalar substitution B=1 would yield zero. Yet y=(0,1) is perfectly observed and cannot be canceled by the one-dimensional actuator: error ||z||_2>=1 for all u. The achievable actuator correction set is a *line segment*, not the whole unit disk; output space geometry matters.

**(ii) Nonsymmetric K: the radius from b=0 can be wrong.** For K=[0,1], b=0 for every y (C=0, N={0}), the best unbounded scalar estimator of t=y is 1/2; max_{v in K,Cv in N}|v|=1 is not the information radius. Central symmetry and its midpoint argument are essential.

**(iii) Known deterministic offset** cannot be subtracted free of actuator cost. If terminal output is d+m^T y+a^T u and u must also cancel d, formula (4) is not valid with the same B without accounting for d in the posterior center.

**(iv) Measurement back-action, nonlinear terminal maps, correlated noises, causal multistage decisions, constrained actuator trajectories, state-dependent admissibility** are outside (1). In particular, this construction does not solve the quantum process-tensor intervention problem or establish observables for NCDG J3/K.

**(v) Arbitrary policies and model fidelity.** The optimal clipped-center policy need not be implementable by a restricted analogue circuit, distributed controller or quantized actuator. Any hardware or protocol restriction beyond |u|<=Umax can raise the true optimum.

## 6. Prior-art subtraction and status decision

**Closest known hosts:**
1. Smolyak / standard scalar optimal recovery: centered convex uncertainty, linear functional, Chebyshev centers; e.g. S. Foucart, *Instances of Computational Optimal Recovery: Refined Approximability Models*, Journal of Complexity 62 (2021), article 101503, DOI https://doi.org/10.1016/j.jco.2020.101503.
2. M. Ettehad, S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors*, SIAM/ASA Journal on Uncertainty Quantification 9 (2021), DOI https://doi.org/10.1137/20M1328476.
3. A. B. Kurzhanski, P. Varaiya, *Optimization of Output Feedback Control Under Set-Membership Uncertainty*, Journal of Optimization Theory and Applications 151 (2011), pp. 11–32, DOI https://doi.org/10.1007/s10957-011-9861-z. Strong external host for finite-horizon hard-bounded feedback under information sets and bounded disturbances.
4. A. B. Kurzhanski, P. Varaiya, *Uncertain Systems: Output Feedback Control*, available from Berkeley as https://people.eecs.berkeley.edu/~varaiya/Download/KurzhanskiVaraiya.pdf; source for broader information-state, information-tube and separation-technique context.

**Subtraction judgement:** theorem (4) is a concise exact specialization and a useful worked separation of information and actuation; until a theorem-level comparison with this mature literature, no original scientific novelty may be asserted. The named operator and numerical oscillator do not establish a new physical mechanism.

**Why retain the note:** it provides a typed, proof-complete, counterexample-tested benchmark suitable for the LT manuscript's distinction between target-reconstruction sufficiency and intervention feasibility. It precisely identifies the first departure from the old chapter: **actuator capability is not equivalent to informational sufficiency**. It does not itself warrant a new chapter or novelty language.

## 7. Next theorem-bearing boundary, not a speculative task inflation

The (E,A,B) decomposition ceases to be generally exact as soon as the correction set in target space is not a symmetric scalar interval independent of b; see counterexample (i). The smallest material research problem is thus: for a *vector-valued*, finite-horizon target and a physically typed actuator image D(U), characterize the exact worst-case terminal error using posterior target sets, their directed Hausdorff/Chebyshev geometry and a common quantifier order. Prove or falsify candidate finite-dimensional simplifications against classical robust output-feedback and set-membership viability theory first. Do not infer quantum or gravitational meaning from this arithmetic.

## 8. Acceptance and receipt

- Proof owner: LT5 independent internal mathematical derivation.
- Numeric controls: local synthetic scalar grid.
- External bibliography: cited representative mature sources, not exhaustive theorem-level priority proof.
- Referee: pending; previous LT5 turn-1 thread read on 2026-10-21 showed no replies.
- GitHub source state: verify direct readback after write.
- Independent referee receipt: not assumed from delivery.
- Manuscript: no mutation pending referee result and editorial integration decision.
- Claims: NO_CANON, NO_EXEC_SIGN, NO_NOVELTY, NO_PHYSICAL_SIGNAL, NO_BW_AUTO_INGEST.
