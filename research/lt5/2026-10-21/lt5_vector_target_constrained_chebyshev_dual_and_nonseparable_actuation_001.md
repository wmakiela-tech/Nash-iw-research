# LT5 / obrót 3 — Vector-valued target: constrained Chebyshev dual and irreducible geometry of actuation

**Date:** 2026-10-21
**Owner:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
**Artifact ID:** LT5-VECTOR-TARGET-CONSTRAINED-CHEBYSHEV-DUAL-001
**Scientific status:** EXACT_CONDITIONAL_DERIVATION / CLASSICAL_HOST / INDEPENDENT_REFEREE_PENDING
**Authority:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_CLAIM
**Exposure:** PUBLIC_SAFE; all constructions abstract mathematical or synthetic
**Relationship:** Follow-up to LT5 notes of 2026-10-20 (bounded linear feedback gain) and 2026-10-21 (scalar target with hard actuator amplitude). Does NOT change original living monograph.

## Abstract

The exact scalar decomposition of the previous LT5 turn, J*=max(information radius, uncontrolled target magnitude minus actuator authority), cannot be generalized to a Euclidean vector-valued target by simply taking norms. We provide a fully typed posterior-set formulation of the vector minimax problem, derive an exact probability-measure dual for the **squared** Euclidean constrained Chebyshev radius, and give a two-dimensional box witness showing a strict gap from the naive scalar maximum. For the posterior dual, at most d+2 support points suffice in output dimension d. These are classical finite-dimensional minimax/convex-geometric methods (minimum enclosing ball, set-membership output feedback), repurposed as explicit claim-boundary controls. No mathematical novelty is established.

## 1. Exact one-stage carrier

All spaces finite-dimensional real Euclidean. Let Y=R^n be unknown initial preparation, W=R^p be measured output, H=R^d be terminal **vector** target, U=R^q be actuator space. Choose nonempty compact convex sets K subset Y and N subset W. For unknown y in K, eta in N, the registered measurement is

    b = C y + eta

with known linear C:Y->W. Assume the source-matched terminal map L:Y->H is known, including effects of any earlier sensor resets/backaction. An independent, subsequently applied actuator u belongs to a compact convex set U_adm subset U, and changes the terminal target by A u where A:U->H is fixed. Measurement data are not retroactively changed by actuation.

Define the **feasible correction set** D:=-A U_adm subset H, nonempty compact convex. Write d=-Au. For policy d(b) in D, the terminal vector residual is L y-d(b), measured in Euclidean norm ||.||_2. There are no restrictions on policy beyond the declared feasible port; its task is not assumed quantum or stochastic.

Set

    B = C K + N,
    K_b = { y in K : b-Cy in N },                         (1)
    T_b = L K_b subset H.                                 (2)

For all b in B, K_b and T_b are nonempty compact convex. For arbitrary feasible output feedback (and, in the stated compact finite-dimensional setting, a Borel-selected optimal feedback), the guaranteed worst-case error is

    J* = inf_{d(.):B->D} sup_{y in K,eta in N}
                    ||L y-d(C y+eta)||_2.               (3)

No linearity of d(.) is imposed. The policy class and actuator set are different from the bounded *operator gain* class in turn 1.

### Theorem LT5-3.1 — posterior constrained-center principle

    J* = sup_{b in B} rho_D(T_b),                        (4)

where

    rho_D(T):=min_{d in D} max_{t in T} ||t-d||_2.        (5)

Proof: Every policy has at each feasible b an error at least rho_D(T_b), giving J*>=sup_b rho_D(T_b). Conversely for every b, choose a minimizer d_b of (5), which exists by compactness and continuity; the resulting conditional error equals rho_D(T_b). Choices can be made Borel-measurably by standard finite-dimensional measurable maximum/selection arguments (closed compact graph of b->K_b, continuous cost in d, fixed compact D). The supremum over feasible b proves the reverse inequality. QED.

Note: no exchange of min and max *across distinct observations* is allowed. The experiment is a decision **after** b, not a precommitted single d.

## 2. Exact squared-radius dual: adversarial witness distributions as certificates

For compact nonempty T subset R^d and compact convex D subset R^d, define the constrained squared radius

    r_D(T)^2 := min_{d in D} max_{t in T} ||t-d||_2^2.  (6)

Let P(T) be Borel probability measures supported on T. Their introduction is a device of convex duality; **no physical law of random noise is introduced**.

### Theorem LT5-3.2 — variance–actuation barycenter dual

    r_D(T)^2
      = max_{mu in P(T)}
          [ int_T ||t||_2^2 dmu(t)
            - ||int_T t dmu(t)||_2^2
            + dist( int_T t dmu(t), D )^2 ].            (7)

Equivalently, with \bar t_mu=int t dmu and Var_mu(T)=int ||t-\bar t_mu||² dmu,

    r_D(T)^2 = max_mu [ Var_mu(T)+dist(\bar t_mu,D)^2 ]. (8)

A maximizer can be chosen with **at most d+2 support points**.

Proof: For fixed d, max_t ||t-d||² equals sup_mu int ||t-d||² dmu since Dirac measures are allowed. On compact convex D and compact convex P(T), the expression F(d,mu)=int ||t-d||²dmu is continuous, convex in d and affine in mu. The finite-dimensional compact convex / weak* compact measure version of the minimax theorem gives

    min_{d in D} sup_mu F(d,mu)
      = sup_mu min_{d in D} F(d,mu).                     (9)

Writing M_1=int t dmu, M_2=int ||t||² dmu, we obtain

    F(d,mu)=M_2-||M_1||²+||d-M_1||².

Minimizing the last term over D gives exactly (7). Compactness ensures attainment on P(T). The objective depends only on (M_1,M_2), which lies in the convex hull of the compact subset { (t,||t||²): t in T } in R^(d+1). By Carathéodory's theorem, every such moment pair is realized by a measure supported on at most d+2 elements of T, in particular the maximizer. QED.

**Interpretation:** the first term is a certificate for irreducible *posterior spread*. The second is a certificate for difficulty shifting the posterior barycenter into the **actual attainable correction set** D. They must be **added under the square** and then maximized *jointly* over witness distributions; independently maximizing them and taking their max (or summing independent extrema) is generally wrong.

For a non-Euclidean norm, the elementary squared-variance algebra is unavailable; (7) is not claimed outside Euclidean output geometry. The inner feedback remains causal only in the declared one-stage sense.

### Corollary LT5-3.3 — finite witness certificate

For every b in B, the local worst-case squared risk rho_D(T_b)^2 has a dual certificate supported on at most d+2 feasible target values t_i with weights p_i>=0, sum p_i=1:

    rho_D(T_b)^2
      = max_{t_i in T_b, p_i>=0, sum p_i=1, i<=d+2}
          [ sum_i p_i ||t_i||²
            -||sum_i p_i t_i||²
            +dist(sum_i p_i t_i,D)^2 ].                 (10)

**Status of the finite-point distribution:** a mathematical adversarial convex-combination witness. It is not a statistical estimate, random adversary assumption, or physical preparation mixture.

## 3. Exact two-coordinate counterexample to a scalar shortcut

Take initial state y=(y1,y2) in K=[-1,1]^2, noiseless observation b=y1 in [-1,1], and target L y=y in R². The actuator can apply **any Euclidean target correction** d satisfying ||d||_2<=B, not merely a single-axis actuator. Thus D is the full Euclidean closed disk B_2(0,B), with B>=0.

Conditional target set is the vertical segment

    T_b = { (b,v) : -1<=v<=1 }.

For candidate d=(d1,d2), the worst-case squared error is

    max_{|v|<=1} [ (b-d1)^2 + (v-d2)^2 ]
        = (b-d1)^2 + (1+|d2|)^2.                       (11)

Replacing d by (d1,0) stays inside the actuator ball and never increases (11). Thus an optimal d has d2=0, and d1=clip(b,-B,B). Therefore

    rho_D(T_b) = sqrt( 1 + (|b|-B)_+^2 ),              (12)

and exactly

    J*(B) = sqrt( 1 + (1-B)_+^2 ).                     (13)

No measurement error or unknown dynamical operator is needed for this failure of the scalar shortcut.

The full, unconstrained posterior recovery radius is E=1 because y2 is unobserved. The uncontrolled Euclidean target amplitude is A=sqrt(2); the maximum norm of actuator correction is B. Both E and (A-B) are individually valid lower bounds, but in general

    J*(B) > max(E,A-B).                                (14)

For B=1/2,

    E=1, A-B=sqrt(2)-1/2 <1,
    max(E,A-B)=1,
    J*(1/2)=sqrt(5)/2=1.118033988749895.              (15)

The gap is not due to a rank-deficient actuator: D is the **full** two-dimensional Euclidean ball. It comes from Euclidean geometry; the guaranteed y2 error of magnitude 1 coexists orthogonally with a residual y1 error of magnitude 1/2.

**Dual witness:** at b=1 choose mu=0.5 delta_(1,+1)+0.5 delta_(1,-1). Its barycenter is (1,0), its variance is 1, and dist((1,0),D)=(1-B)_+. Inserting into (8) gives the exact squared risk (13). Only two support points are needed, below the general d+2=4 bound.

## 4. A structural Pythagorean subclass

Let H=H_obs direct-orthogonal-sum H_hid. Suppose the measured H_obs component b is exactly known with ||b||<=R_obs, while the unmeasured target component h ranges over the full ball ||h||<=rho in H_hid, independently of b. Suppose the actuator can apply any terminal correction d in the full Euclidean ball ||d||<=B in H.

For any correction d=d_obs+d_hid, the worst unmeasured h gives

    max_{||h||<=rho} || (b+h)-d ||²
       = ||b-d_obs||² +(rho+||d_hid||)².                (16)

The optimal choice has d_hid=0 (moving in an unknown sign direction cannot improve the minimax loss); then d_obs is the metric projection of b onto the radius-B ball of H_obs. Thus

    J* = sqrt( rho² + (R_obs-B)_+² ).                   (17)

This is a geometrically exact substitute for the scalar maximum **only for the stated orthogonal product and norm geometry**. Arbitrary correlated conditional target sets, anisotropic actuator images and costs require (4)–(8).

## 5. Reproducible numerical stress on finite target polytopes

For a finite set of points V={t_i} in R², its convex hull and V have the same maximal squared distance from any d, because squared Euclidean distance is convex in t. Thus one can verify the primal

    min_{||d||<=B,r2>=0} r2
      subject to r2 >= ||t_i-d||² for every i

against the discrete form of (8), optimizing weights p in the simplex.

A synthetic test using NumPy's default_rng(36), SciPy SLSQP with ftol <=1e-12, V=random Gaussian vertices rescaled with a random scalar, B=0.3+Uniform(0,0.7), yielded the following *squared* radii:

| Number of vertices | B (approx.) | Primal squared radius | Dual squared radius | Absolute gap |
|---:|---:|---:|---:|---:|
| 3 | 0.9127 | 1.5249996056 | 1.5249996056 | <1e-9 |
| 4 | 0.6390 | 0.9395754218 | 0.9395754218 | <1e-9 |
| 7 | 0.7301 | 0.8977279805 | 0.8977279805 | <1e-9 |

These are **numerical controls only**; the duality itself is proved independently above. The sample is not a comprehensive numerical validation and does not substantiate any physical claim.

## 6. Recent source collision: Geeky-S10 closed a different open problem

Before preparing this note, LT5 read the 2026-10-21 INT8 and Geeky-S10 reports and the REC10 referee. The previously open nonquadratic weak-sensor energy bound has now been closed in the Geeky-S10 lineage:

    V_epsilon(x) <= epsilon V_*(x),
    N_epsilon(x) <= sqrt(epsilon) N_*(x),

for fixed-e finite-dimensional reset-flow and finite extremal available storage V_*, without an ellipsoidal certificate P. The proof uses continuity/convexity of V_*, its strong-reset endpoint limit and telescoping. **Do not open a duplicate LT5 task or claim this result**.

Source: research/geeky-s10/2026-10-21/geeky_s10_fixed_sensor_nonquadratic_weak_storage_ceiling_001.md, 2026-10-21 GitHub readback by Geeky-S10.

Independent prior LT5 referee REC10 gave PASS_WITH_GUARDS for the *bounded static linear gain* theorem (2026-10-20) and supplied kappa_match and zero-risk pseudoinverse threshold. This referee verdict must **not** be silently extended to the scalar amplitude theorem of LT5 turn 2 or the vector theorem of this turn.

INT8 independently documented that when sensor reset Q_s alters dynamics, the terminal functional m_s must be source-matched to the actual reset-flow, and cannot be borrowed from an unperturbed model. Hence L in this note is required to be the **post-sensor physical terminal linear operator** under any declared reset model. No such reset-flow model is constructed in this vector note.

## 7. Mature-host subtraction and claim ceilings

Known host families strongly subsume the general architecture:

- *Set-membership identification and Chebyshev centers*; e.g. *Optimal and suboptimal algorithms in set membership identification*, International Journal of Control (2006), DOI 10.1080/13873950500068575: conditional uncertainty sets and Chebyshev center as worst-case-optimal estimator.
- *Constrained Euclidean minimum enclosing ball / 1-center*; e.g. *Linear time algorithms for Euclidean 1-center in R^d with non-linear convex constraints*, Discrete Applied Mathematics 280 (2020), 71–85, DOI 10.1016/j.dam.2019.09.009.
- *Robust output feedback with set-membership uncertainty*, A. B. Kurzhanski and P. Varaiya, JOTA 151 (2011), DOI 10.1007/s10957-011-9861-z, explicitly treating bounded inputs and disturbances over a finite horizon.
- *Robust output-feedback MPC of constrained linear systems*, D. Q. Mayne et al., Automatica 42 (2006), DOI 10.1016/j.automatica.2006.03.005.
- Euclidean minimum-enclosing-ball duality and minimax theorem (Sion); the probability moment formulation (7) is an elementary derivation in that family, not evidence of novel mathematical priority.

**Subtraction result:** The dual (7) and the counterexample establish a correct typed benchmark and correct an invalid generalization of the preceding scalar formula. The underlying geometry is classical; no new theorem family or scientific discovery claim is advanced. Abstract-level source overlaps do not prove an identical proposition with identical assumptions exists in a particular cited paper. Exhaustive theorem-to-theorem priority and independent referee still pending.

**No transport to other regimes without new contracts:** The result does not cover general multi-time stochastic/quantum measurements, nonlinear observation maps, nonlinear actuator influence, unbounded operators, field-theoretic observables or any NCDG J3/K physical interpretation. Loss of Hilbert/EUCLIDEAN geometry invalidates the variance decomposition.

## 8. Final scientific disposition

- The exact scalar formula max(E,A-B) from LT5 turn 2 remains intact in its source-typed class.
- Its *vector-valued naive extension* is FALSE: witness (15).
- New correct vector alternative is the posterior constrained-center principle (4) and conditional variance–actuator dual (8), for compact convex geometry and squared Euclidean loss.
- Model counterexample (13) is independently verifiable; three random convex-hull controls match primal/dual to numerical precision.
- Conditional result requires independent REC/SW mathematical audit before any manuscript insertion, no novelty label.
- Full note committed to GitHub; readback requested; BW ingestion NOT presumed.
- The remaining true frontier concerns legal time-coupled, backaction-aware interventions under physical actuator cost, not just rewriting classical convex geometry as new physics.

**CURRENT:** EXACT_CONDITIONAL / HOST_ABSORBED / REVIEW_PENDING.
**CLAIMS:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_SIGNAL.
