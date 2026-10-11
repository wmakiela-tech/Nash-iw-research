# M12 — Front B floor-residual exact population and directional-rate error gate

RETURN_ID: M12-FRONTB-FLOOR-RESIDUAL-POPULATION-DIRECTIONAL-RATE-GATE-001
RESULT_CLASS: EXACT LOCAL CONTROL / SOURCE-NATIVE ERROR BRIDGE / NO PBH ENDPOINT

## Trigger
Mech-S6 established the floor executor
n_tilde' = alpha(n_tilde) S - D n_tilde,
alpha=min(1,n_tilde/epsilon),
epsilon=e^-100,
versus intended n'=S-Dn.
Thus rho_floor=S(alpha-1)<=0.

## Exact population error
For e=n_tilde-n on one common S,D path:
e' + D e = rho_floor.
With Phi(t,s)=exp[-int_s^t D(u)du],
e(t)=Phi(t,t0)e0 + int Phi(t,s)rho_floor(s)ds.

If e0=0 and S,D>=0, then e(t)<=0 exactly.
So the active floor can only suppress population relative to intended source-sink evolution on the common path.

Moreover:
|e(t)| = int Phi(t,s) S(s)[1-alpha(s)] ds.
The integrand is supported only where n_tilde<epsilon and S>0.

If D>=d_min>0:
|e(t)| <= int exp[-d_min(t-s)] S(s)[1-alpha(s)] ds.

## Source-off recovery
When S=0, rho_floor=0 and e'+De=0.
Thus after source turn-off t1:
e(t)=Phi(t,t1)e(t1).
The floor injects no new post-source forcing; only the previously created deficit relaxes.

## Multispecies directional-rate error
For each species h:
e_h=n_tilde_h-n_h<=0
under matched initial data and common S_h,D_h.

A=sum_h n_h k_h^pn,
B=sum_h n_h k_h^np.

Then:
deltaA=sum_h e_h k_h^pn,
deltaB=sum_h e_h k_h^np.

For nonnegative physical rates:
deltaA<=0 and deltaB<=0.

Let
E_h(t)=int Phi_h(t,s)S_h(s)[1-alpha_h(s)]ds.

Then:
|deltaA|<=sum_h E_h k_h^pn,
|deltaB|<=sum_h E_h k_h^np.

## Reduced neutron-fraction RHS
F_had(X)=(1-X)A-XB.

Exactly:
deltaF_had=(1-X)deltaA-X deltaB.

Its sign is not fixed, but:
|deltaF_had|
<=
(1-X)|deltaA|+X|deltaB|.

This supplies an explicit epsilon_F(t) for the prior M12 dynamic-X_n contraction certificate.

## Ratio guard
For q=A/(A+B):
q_tilde-q =
[B deltaA - A deltaB] /
[(A+B)(A+B+deltaA+deltaB)].

Hence directional-rate suppression alone gives no fixed sign for q error.
A and B remain the primary robust error objects.

## Exact chain
floor-active source suppression
-> rho_floor
-> e_h
-> (deltaA,deltaB)
-> deltaF_had
-> deltaX_n
-> declared endpoint target.

All arrows through deltaX_n now have exact conditional certificates.
The endpoint step still requires an independent BBN target-response bound.

## Firewalls
FLOOR ACTIVE != ENDPOINT FAILURE.
SOURCE OFF != POPULATION ERROR ZERO.
SOURCE OFF => NO NEW FLOOR ERROR INJECTION.
DIRECTIONAL RATE SUPPRESSION != FIXED SIGN OF q ERROR.
COMMON-PATH POPULATION BOUND != FULL COUPLED PBH-BBN VALIDATION.
DYNAMIC X_n BOUND != Y_p / D-H ENDPOINT BOUND.

## Status
FLOOR_RESIDUAL_TO_POPULATION_ERROR = PASS_EXACT.
POPULATION_ERROR_SIGN_ON_COMMON_PATH = PASS_EXACT.
FLOOR_ERROR_RELAXATION_AFTER_SOURCE_OFF = PASS_EXACT.
DIRECTIONAL_A_B_ERROR_SIGN = PASS_EXACT.
LINK_TO_DYNAMIC_XN_CERTIFICATE = PASS_EXACT_CONDITIONAL.
PBH_DE_DYNAMIC_ACCURACY = OPEN.
PBH_B2_WATERFALL_TRANSFER = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.

NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
