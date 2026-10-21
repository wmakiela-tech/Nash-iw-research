# LT5 — obrót 4: Causal timing of information and actuation; exact two-stage scalar minimax

**Artifact:** LT5-CAUSAL-TIMING-TWO-STAGE-MINIMAX-001
**Date:** 2026-10-21
**Owner:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
**Class:** EXACT_CONDITIONAL_CLASSICAL_DERIVATION / COUNTEREXAMPLE / MATURE_HOST_SUBTRACTION
**Claim ceiling:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_CLAIM
**Exposure:** PUBLIC_SAFE; purely mathematical and synthetic experiment
**Causality contract:** early control is chosen before the later observation; unused early control capacity CANNOT be transferred to the later actuator.
**Manuscript:** NOT MUTATED. Independent mathematical referee pending.

## 0. Why this note, and how it differs from LT5 turns 1–3

Prior LT5:
- 2026-10-20: one-shot **static linear output-feedback gain** norm bound.
- 2026-10-21, turn 2: one-shot arbitrary policy with a **hard scalar actuator amplitude** bound.
- 2026-10-21, turn 3: one-shot **vector-valued target**, constrained Chebyshev center, and its convex dual.

This note is NOT another one-shot sensor strength optimization. It introduces one genuinely causal seam: **one control decision must be irrevocably committed before an informative later measurement, while a second control decision may depend on that measurement**. A state may be completely identifiable from the final observation record yet no longer correctable within the surviving actuator port.

The result is a tractable exact specialization of robust output feedback with information sets and nonanticipativity (known mature theory), not a novelty claim. It sharpens the distinction between information sufficiency, actuator size and timing of actuator access.

## 1. Typed two-stage experiment

Fix a scalar unknown y in the interval

    I=[ell,h],    -infinity<ell<=h<infinity.

I may itself be a posterior information set formed from earlier legal observations; the previous observation process is NOT reintroduced as an unverified source.

At time t0 an early scalar action u0 is chosen using only the existing interval I; it obeys

    |u0|<=B0, B0>=0.

The state immediately afterward is x1=y-u0. At time t1>t0, before any late action, we make a *source-matched* observation of this state

    b=s x1+eta = s(y-u0)+eta,
    s>0,   |eta|<=delta,  delta>=0.

Both s and the bound delta are known, and the disturbance is adversarial, not random. The controller knows the previously chosen u0, so the adjusted record b+s u0 is equivalent to the linear measurement s y+eta. This is why an earlier action does not secretly create or erase information in the present elementary carrier.

Only **after** observing b, the controller chooses the late scalar correction u1=u1(b;u0) satisfying

    |u1|<=B1,  B1>=0.

Terminal scalar target residual:

    z=y-u0-u1.

Neither action changes the measurement operator s or the noise law except for the explicitly known offset -s u0, and there are no extra disturbances or waiting-time dynamics. For a more general linear system these would need source-derived transition and port maps; that transport is NOT claimed here.

Define the causal robust value

    J_two =
      inf_{|u0|<=B0} inf_{measurable u1(.), |u1(b)|<=B1}
        sup_{y in I, |eta|<=delta}
          |y-u0-u1(s(y-u0)+eta)|.                         (1)

The order matters: u0 is chosen before eta and y are revealed, while u1 can respond to b.

Put

    w=(h-ell)/2,  c=(h+ell)/2,
    e=min(w,delta/s).                                   (2)

The number e is the passive radius of information for estimating the scalar y from its later observation, conditional on I. It is not a statement about physical variance.

## 2. Exact theorem

**Theorem LT5-4.1 (two-stage chronology gate).** In the experiment of §1,

    J_two = max{ e, w+(|c|-B0)_+ - B1 }.                 (3)

The positive part is (x)_+=max(x,0). All terms are finite and e>=0, so a negative second entry causes no issue.

**Proof (conditional late decision).**
Fix u0. Set t=y-u0, with prior interval J=[ell-u0,h-u0], midpoint c-u0 and half-width w. The late sensor record is b=s t+eta. For each legal b, the posterior interval of t is

    J_b = J intersect [(b-delta)/s,(b+delta)/s]
        = [L_b,H_b],                                   (4)

where only nonempty posteriors are considered. Let q_b=(H_b-L_b)/2 and k_b=(H_b+L_b)/2.

With a bounded late correction |u1|<=B1, the exact minimax conditional terminal error is

    min_{|u1|<=B1} max_{t in J_b}|t-u1|
      = q_b+(|k_b|-B1)_+.                              (5)

The minimizing action is the clipped midpoint u1=clip(k_b,-B1,B1).

The posterior half-width obeys q_b<=e because it lies both inside the original interval (width 2w) and inside the sensor uncertainty interval (width 2delta/s). Also

    max(|L_b|,|H_b|)<=A(u0)
       :=max(|ell-u0|,|h-u0|).

If |k_b|<=B1, (5) is at most e. Otherwise (5) equals max(|L_b|,|H_b|)-B1, and is at most A(u0)-B1. Thus for all b the attainable conditional risk is at most

    max{ e, A(u0)-B1 }.                                (6)

Both entries are necessary:
(i) for the radius e, choose two legal states at distance 2e within J and choose corresponding noises making their sensor readings identical; the controller must choose one u1 for both and cannot have error below e;
(ii) choose a state with |t|=A(u0), and an admissible noise (for instance eta=0); whatever the feedback, |u1|<=B1 forces error at least A(u0)-B1.
Therefore equality holds in (6), and the clipped posterior-center rule realizes it.

Finally

    A(u0)=max(|ell-u0|,|h-u0|)
         =w+|c-u0|.

Its minimum over [-B0,B0] is w+(|c|-B0)_+, attained at u0=clip(c,-B0,B0). Since e is independent of u0, taking min over u0 in (6) gives exactly (3). QED.

**Optimal policy:**
- u0*=clip(c,-B0,B0), committed before the observation;
- after b, form J_b from (4), choose u1*=clip((L_b+H_b)/2,-B1,B1).
If no previous observation exists, I can be the full unknown preparation set. This is a causal nonanticipative controller.

**Note on measurements:** s=0 is excluded to avoid writing delta/s; an uninformative reading is represented by e=w and J_b=J. Noise is bounded per reading, not Gaussian.

## 3. Same total actuator capacity, different decision times

Consider the *different* protocol in which the early budget B0 is freely transferable to the terminal action after the measurement; the single late actuator then has bound B0+B1. Applying the same scalar posterior result gives

    J_late_only
       =max{ e, w+|c|-(B0+B1) }.                       (7)

From the elementary identity

    w+(|c|-B0)_+-B1 >= w+|c|-B0-B1,

we get the exact monotonicity

    J_two >= J_late_only.                              (8)

**Exact strict-gap test:** The inequality is strict if and only if

    B0>|c|    and
    w+(|c|-B0)_+-B1 > e.                               (9)

Indeed if B0<=|c|, the second entries of (3) and (7) coincide. If B0>|c| then the early second entry is w-B1, while the all-late entry is w+|c|-B0-B1<w-B1; a strict overall difference occurs exactly when the early second entry exceeds the common information floor e.

Interpretation: the early actuator can shift a known posterior **center** by at most B0. It cannot remove the posterior half-width w in worst-case sense before the resolving measurement. When B0>|c|, part of its nominal terminal authority is unusable for guaranteed control at that time. This is not an invariant of actuator hardware; it is an invariant of this exact causal information/control contract.

## 4. Minimal falsifier: perfect eventual measurement but useless early actuation

Take

    I=[-1,1], s=1, delta=0,
    B0=1, B1=0.

Then w=1,c=0,e=0 and from (3):

    J_two=max(0,1+(0-1)_+-0)=1.

Although the later record b=y-u0 exactly reveals the true scalar state, there is **no late actuator** to exploit it. The best early action is u0=0 and the worst terminal error is 1.

Move the *same* total authority 1 after the exact measurement:

    B0=0, B1=1.

Now J_late_only=0 and u1=b achieves exact cancellation.

Thus:

    TERMINAL_IDENTIFIABILITY = EXACT in both,
    TOTAL_NOMINAL_AUTHORITY = 1 in both,
    CAUSAL_REACHABILITY / MINIMAX_TARGET_ERROR = 1 vs 0.

An observational Gramian or final-state posterior alone does not tell whether the information arrived before the final useful control port closed.

A **nontrivial noisy witness** uses I=[-0.8,1.2], s=1, delta=0.05, B0=0.7, B1=0.4. Here w=1,c=0.2,e=0.05, so

    J_two=max(0.05,1+(0.2-0.7)_+-0.4)=0.6.

For the same total budget transferred after the measurement, B1=1.1, we obtain

    J_late_only=max(0.05,1+0.2-1.1)=0.1.

So simply knowing the terminal uncertainty and the sum of permitted actuation magnitudes is insufficient; the causal order is load-bearing.

## 5. Independent numerical regression controls

Used a Python/NumPy plus SciPy bounded 1D minimization diagnostic. For a fixed early action u0, enumerate 1501 possible legal second readings across b in [s ell-delta, s h+delta], compute each exact posterior interval (4), minimize the worst conditional radius (5) over u0 using bounded scalar optimization. This grid is only a reproducibility check; (3) is proved analytically.

| Interval I | B0 | B1 | s | delta | Exact (3) | Numeric |
|---|---:|---:|---:|---:|---:|---:|
| [-1,1] | 1 | 0 | 1 | 0 | 1.0 | 1.0 |
| [-1,1] | 0 | 1 | 1 | 0 | 0.0 | 0.0 |
| [-0.8,1.2] | 0.7 | 0.4 | 1 | 0.05 | 0.6 | 0.6 |
| [0.2,1.2] | 1 | 0.2 | 1 | 0.05 | 0.3 | 0.3 |
| [-2,3] | 0.8 | 0.5 | 2 | 0.3 | 2.0 | 2.0 |
| [-1.1,0.4] | 0.2 | 0.25 | 0.7 | 0.12 | 0.65 | 0.65 |

The posterior search is a grid approximation and should not be promoted to an independent formal proof; endpoint completeness follows from (4)–(6), not the sample count.

### Standalone control script

    import numpy as np
    from scipy.optimize import minimize_scalar

    def exact(ell,h,B0,B1,s,delta):
        w=(h-ell)/2
        c=(h+ell)/2
        return max(min(w,delta/s),w+max(abs(c)-B0,0)-B1)

    def approx(ell,h,B0,B1,s,delta,n=1501):
        # Scan adjusted observations obs0=b+s*u0, not raw b:
        # the adjusted domain does not depend on the early action.
        obs0=np.linspace(s*ell-delta,s*h+delta,n)
        def risk(u0):
            yl=np.maximum(ell,(obs0-delta)/s)
            yh=np.minimum(h,(obs0+delta)/s)
            ok=yl<=yh+1e-10
            cb=(yl[ok]+yh[ok])/2-u0
            rb=(yh[ok]-yl[ok])/2
            return np.max(rb+np.maximum(np.abs(cb)-B1,0))
        if B0==0:
            return risk(0)
        opt=minimize_scalar(risk,bounds=(-B0,B0),method="bounded",
                            options={"xatol":1e-12})
        return opt.fun

    cases=[
       (-1,1,1,0,1,0),(-1,1,0,1,1,0),
       (-.8,1.2,.7,.4,1,.05),(.2,1.2,1,.2,1,.05),
       (-2,3,.8,.5,2,.3),(-1.1,.4,.2,.25,.7,.12)
    ]
    for row in cases:
        a=exact(*row)
        b=approx(*row)
        assert abs(a-b)<1e-5,(row,a,b)
    print("SYNTHETIC_NUMERIC_REGRESSION_PASS: 6/6")

**Script scope guard:** The observation grid is fixed in *adjusted measurement coordinates* s y+eta, after subtracting the known action offset; this avoids the false error of scanning a fixed unadjusted b-domain as u0 varies.

## 6. Connection to active measurements and source-matched target effects

The theorem assumes the second observation is affected by the earlier action only through the known state shift x1=y-u0 and has the declared independent bounded error. If the sensor changes the dynamical generator or resets part of the physical state (as in INT8 / Geeky-S10 Q_s measurements), then the state transition, measurement channel and **terminal** functional must be recalculated for the actual whole protocol. Substituting a C_s from a reset model with an unperturbed target m is illegal.

A general finite-time linear physical realization would use source-derived A_{1:0}, B_0, H_1, A_{T:1}, B_1 and terminal G, and produce the correct causal ports from their compositions. The present theorem does **not** prove the same closed scalar expression for arbitrary such operators, switching, multiplicative noise or correlated state/measurement disturbances.

It also does not certify quantum instruments, nonlocal gravity, NCDG J3/K or FEEC claims.

## 7. Prior-art subtraction / exact claim ceiling

This two-stage problem and its information-state reduction are within mature deterministic output-feedback / set-membership dynamic programming:

1. A.B. Kurzhanski, P. Varaiya, **Optimization of Output Feedback Control Under Set-Membership Uncertainty**, *Journal of Optimization Theory and Applications* 151 (2011), DOI https://doi.org/10.1007/s10957-011-9861-z. Finite-horizon bounded controls and disturbances, minimax/set-valued dynamic programming, information sets.
2. A.B. Kurzhanski, P. Varaiya, **On the Problem of Output Feedback Control under Set-Membership Uncertainty**, *IFAC Proceedings Volumes* 43(14) (2010), DOI https://doi.org/10.3182/20100901-3-IT-2016.00133.
3. J.S. Baras, N.S. Patel, **Robust control of set-valued discrete-time dynamical systems**, *IEEE Transactions on Automatic Control* 43(1) (1998), 61–75, DOI https://doi.org/10.1109/9.654887. Classical dynamic games and information states.
4. **Generalized adaptive versus nonadaptive recovery from noisy information**, *Journal of Complexity* 53 (2019), 162–172, DOI https://doi.org/10.1016/j.jco.2018.12.001: related host family for constraints on adaptivity of recovery; does not by itself justify claims about actuators.

**Subtraction:** The proof is an exact special case and a counterexample to the shortcut “same final information + same aggregate control authority => same guaranteed performance”. It is a useful bridge for the living theory's target- and history-sufficiency narrative, **not** established new mathematical priority. The public bibliographic records identify the host families; they do not constitute exhaustive exact-theorem duplication analysis.

Independent REC10 review of *LT5 turn 1* (2026-10-21) is PASS_WITH_GUARDS, but that verdict **does not** approve turn 2, turn 3 or this turn 4.

## 8. Negative knowledge, next scientific boundary, and disposition

**NEGATIVE_RESULTS:**
- EXACT_FINAL_OBSERVABILITY != CAUSAL_CONTROL_FEASIBILITY.
- NOMINAL_TOTAL_ACTUATOR_BUDGET != REDEPLOYABLE_LATE_BUDGET.
- EARLY_ACTION_CAN_SHIFT_POSTERIOR_CENTER != EARLY_ACTION_CAN_ELIMINATE_UNRESOLVED_HALF_WIDTH.
- SAME_FINAL_POSTERIOR_SET != SAME_INFORMATION_TIMING.
- SOURCE_MISMATCHED_SENSOR_RESET_C != VALID_TERMINAL_OBSERVABLE.
- SYNTHETIC_TWO_STAGE_PROOF != QUANTUM / GRAVITATIONAL PHYSICS.

**Exact next seam:** source-valid multistage dynamics in which measurements or early controls change both the available *posterior information* and future **actuator port**, with independently calibrated bounded resource law. Need to check mature robust output feedback/dual control before attributing novelty. One particularly cheap falsifier is to compare the exact information-state/remaining-resource Bellman recursion with any proposed terminal-only scalar threshold and exhibit a source-matched counterexample when budgets are transferable or when sensor resetting destroys target information.

**FINAL:** EXACT_CONDITIONAL_SPECIALIZATION / HOST_ABSORBED / INDEPENDENT_REFEREE_PENDING. Full body to GitHub with readback; no BW acceptance implied.
