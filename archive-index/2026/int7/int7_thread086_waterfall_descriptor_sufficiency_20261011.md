# INT7 Thread086 — waterfall descriptor sufficiency

RETURN_ID: INT7-THREAD086-FRONTB-WATERFALL-DESCRIPTOR-SUFFICIENCY-001
DATE: 2026-10-11

Let
a_h=Gamma_pn^had,
b_h=Gamma_np^had,
R_h=a_h+b_h,
X_qs=a_h/R_h.

Whenever R_h>0:
a_h=R_h X_qs,
b_h=R_h(1-X_qs).

If rho=R_h/R_weak and the weak total rate R_weak is independently known and positive on the same legal clock, then {X_qs,rho} reconstructs both hadronic directional rates exactly.

Therefore, for the reduced neutron-fraction equation
dX/dt=(a_w+a_h)(1-X)-(b_w+b_h)X,
a frozen descriptor history plus weak-rate history and initial condition is REPLAY-SUFFICIENT.

But:
REPLAY SUFFICIENCY != GENERATIVE CLOSURE.

A recorded descriptor curve gives only on-trajectory rates. If rates depend on state/source/background, two models can match the same benchmark descriptor while responding differently to a perturbed source.

Thus:
TRAJECTORY DESCRIPTOR != CONSTITUTIVE LAW.
BENCHMARK DESCRIPTOR MATCH != SOURCE-FAMILY CLOSURE.

For SOURCE_FAMILY sufficiency one needs a legal descriptor law
D=D(state,background,source)
or an equivalent theorem that all load-bearing dependence factors through D.

Target ceiling:
N/P DYNAMICS SUFFICIENCY != FULL BBN TARGET SUFFICIENCY.

A final Y_p or D/H claim additionally requires target descent through the reduced trajectory/background or a source-matched target-error certificate.

Ratio guard:
R_h/R_weak != R_h unless R_weak is known, positive, and clock/units are frozen.

Multi-hadron compression may be safe for the reduced p<->n equation and unsafe for targets sensitive to species/energy/other channels.

Cheap order:
descriptor -> rate reconstruction -> X_n replay -> source perturbation -> source-family closure -> final target.

VERDICT:
WATERFALL_DIRECTIONAL_RATE_RECONSTRUCTION_PASS /
REDUCED_NP_REPLAY_SUFFICIENCY_EXACT /
TRAJECTORY_DESCRIPTOR_VS_CLOSURE_LAW_SPLIT_PASS /
SOURCE_FAMILY_AND_FINAL_TARGET_VALIDATION_STILL_OPEN /
CHEAP_DESCRIPTOR_FIRST_ORDER_JUSTIFIED.

REV020 ACTIVE / TPE HOLD / NO NOVELTY / NO PBH BOUND / NO ENDPOINT.
