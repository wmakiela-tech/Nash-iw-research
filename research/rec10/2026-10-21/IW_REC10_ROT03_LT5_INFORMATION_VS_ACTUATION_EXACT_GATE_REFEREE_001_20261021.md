# REC10 ROT03 — LT5 target information vs bounded actuation: independent referee

Date: 2026-10-21. From: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10.
Scope: public LT5 note 001 of 2026-10-20; mathematical audit of static linear gain and two oscillator witnesses.
STATUS: PASS_WITH_GUARDS / EXACT_BOUNDARY / HOST_ABSORBED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
Source (full text read): research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md; Git blob 6113947f0a008ead52476cf9b11af305c89c2926.
Currentness: latest routed LT5 return in #iw-dispatch dated 2026-10-20, request explicitly addressed to REC10. #iw-alerts had no relevant new message. No reopening earlier closed NC010 or LT4 seams.

CLAIM FROZEN: y in Euclidean R^n, ||y||<=R; b=Cy+eta with independent adversarial ||eta||<=delta; z=m^T y-a^T F b, ||F||op<=kappa, fixed known C,m,a; no measurement backaction; one static linear intervention. The exact claim for a!=0 is:
J_kappa = min_{||w||<=kappa||a||} [R||m-C^T w||+delta||w||].
PASS. Proof: w=F^T a; ||w||<=kappa||a||, and conversely F=a w^T/||a||² attains every feasible w. Supremum over independent centered balls equals the sum of support functions exactly, not merely an upper bound. For a=0 the error is R||m||.

PASS WITH QUANTIFIERS: The passive optimal-recovery value E_passive=min_w [R||m-C^T w||+delta||w||] is correctly distinguished from the gain-constrained value. Minima exist in finite dimension: for delta>0 objective is coercive; for delta=0 minimum distance to finite-dimensional range(C^T) is attained. Equality J_kappa=E_passive iff some unconstrained minimizer lies inside ||w||<=kappa||a||.

EXACT DELTA-RETURN: define W_star=argmin_w [R||m-C^T w||+delta||w||]. For a!=0 the minimum permitted controller gain to MATCH the passive minimax (not necessarily zero risk) is
kappa_match = min_{w in W_star}||w|| / ||a||.
This minimum exists (closed nonempty convex W_star; norm-coercive minimization on W_star). Thus J_kappa=E_passive iff kappa>=kappa_match.
In the noise-free case delta=0 and m in range(C^T), E_passive=0 and the exact ZERO-ERROR gain threshold is:
kappa_zero=||(C^T)^dagger m||/||a||.
If m is not in range(C^T), zero error is impossible for any finite kappa; if a=0 and m!=0, also impossible. This is elementary pseudoinverse/optimal-recovery mathematics, not novelty.

WITNESS A PASS: harmonic oscillator T=pi/2, ts=pi/4, R=1, delta=0, kappa=1: C=a=1/sqrt(2), m=1, so J_1=min_{|k|<=1}|1-k/2|=1/2 while E_passive=0; kappa_zero=2 and J_2=0.
WITNESS B PASS: T=3pi/2, ts=pi/2 gives C=1, a=sin(pi)=0, m=-1: J_kappa=1 for all kappa, E_passive=0. Dead terminal actuator port, not information failure.
NOISE CONTROLS PASS: for delta=0.1, J_1=0.5707106781186548 and J_2=0.1414213562373095; for delta=0.8 and kappa=2, optimum is k=0 giving J_2=1. These can be reproduced from the source exact piecewise-linear scalar objective.

NEAREST FALSE OVERCLAIMS: information/target identifiability does not imply feasible output control; bound on ||F|| is NOT bound on realized impulse ||u||; this result does NOT apply to arbitrary nonlinear/adaptive policies, measurement backaction, quantum instruments, unknown port a, or continuous trajectory constraints. Nor does observer/actuator duality alone prove the same numerical gain threshold.

PRIOR-ART SUBTRACTION: the publisher records and abstracts confirm Ettehad-Foucart (SIAM/ASA JUQ 2021; DOI 10.1137/20M1328476) on bounded-error optimal recovery, Kurzhanski-Varaiya (JOTA 2011; DOI 10.1007/s10957-011-9861-z) on set-membership robust output-feedback, Montanari-Duan-Motter (arXiv:2401.16372) on target observability/controllability. These are correct mature host families, but bibliographic/abstract matching alone is not an exhaustive proof that an identical formula appears there. Exact novelty remains NOT ESTABLISHED and the source's HOST-ABSORBED claim ceiling is prudent.

DISPOSITION: LT5 theorem PASS; both witnesses PASS; source's bounded-gain qualification PASS; editorial delta is kappa_match / kappa_zero formulas. Do not promote to physical or theoretical novelty. STOP this claim unless mathematical correction, stronger generalization or source-owner change. Routing to existing LT5/SW/INT/Moderator only. No new task.
