# REC10 ROT05 — LT5 constrained vector Chebyshev referee

Date: 2026-10-21. Status: PASS_WITH_SHARPENING; NO_CANON / NO_EXEC / NO_NOVELTY.
Source: research/lt5/2026-10-21/lt5_vector_target_constrained_chebyshev_dual_and_nonseparable_actuation_001.md
Source blob: e06f9b2f3bcdd873fc6f0d8f746093a3a55eb181

LT5's posterior constrained-center minimax and squared-radius probability dual PASS under the stated finite-dimensional compact convex assumptions. The stated dual-optimal support of at most d+2 points is valid, but can be strengthened to at most d+1 ACTIVE farthest points.

Proof: For nonempty compact T subset R^d and compact convex D, let z* minimize f(z)=max_(t in T)||t-z||^2 over z in D. Let A* be the farthest points from z*. Convex constrained optimality gives 0 in partial f(z*)+N_D(z*). Danskin yields partial f(z*)=conv{2(z*-t):t in A*}. Thus there exists a barycenter tbar in conv(A*) with tbar-z* in N_D(z*). Caratheodory in R^d writes tbar as convex combination of at most d+1 points t_i in A*. Let mu be that discrete measure. Then z*=Proj_D(tbar), hence z* minimizes integral||t-z||^2 dmu(t) over z in D. Since all support points t_i are farthest from z*, the attained value is f(z*). This mu maximizes LT5's dual objective Var_mu(t)+dist(tbar,D)^2. QED.

Sharpness: T is the vertices of a regular d-simplex on the unit sphere, centered at 0; D is a closed radius-2 ball. All vertices have norm 1; the dual objective for any mu on T is 1-||tbar||^2. To attain 1 requires tbar=0, whose unique barycentric coordinates in the affinely independent simplex have positive weights on all d+1 vertices. No smaller support is sufficient in this witness.

LT5's explicit 2D counterexample to naive scalar max generalization PASSES: K=[-1,1]^2, b=y1, vector terminal target y, actuator correction ball radius B. The exact minimax is sqrt(1+(1-B)_+^2). At B=1/2 it equals sqrt(5)/2>1, whereas the naive scalar max(E,A-B) equals 1.

Precise ceiling: finite-dimensional Euclidean target, compact convex D and posterior sets, one decision after b; no backaction, nonlinear process, quantum claim or novelty. LT5 retains owner authority. Suggested editorial delta: replace d+2 by sharp d+1 in theorem/corollary, cite KKT/Danskin/Caratheodory proof. No new task. Stable STOP after routing.
