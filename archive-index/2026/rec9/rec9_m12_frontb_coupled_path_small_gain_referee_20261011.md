# REC9 M12 coupled-path small-gain referee

RETURN_ID: REC9-M12-FRONTB-COUPLED-PATH-SMALL-GAIN-REFEREE-001

VERDICT: PASS_EXACT_CONDITIONAL_WITH_BOOTSTRAP_AND_NORM-TYPING_REPAIR
SEVERITY: MEDIUM

Core result: PASS.

For nonnegative error envelopes Z,E, use upper Dini derivatives:
D+Z <= -c(t)Z + a(t)E
D+E <= b(t)Z - d(t)E + F(t),
with c,d>0 and a,b,F>=0.

The associated Metzler comparison system is order-preserving. If c(t)>=c, d(t)>=d, a(t)<=a, b(t)<=b and cd>ab, then the constant comparison matrix is Hurwitz.

For F<=Fmax and zero initial error,
Zbar=a Fmax/(cd-ab),
Ebar=c Fmax/(cd-ab)
defines a forward-invariant comparison rectangle. M12 algebra is correct.

MAIN REC9 REPAIR — REGIME BOOTSTRAP:
a,b,c,d,F are only valid on the declared source-native regime. The bound is valid globally on an interval only if both compared trajectories remain inside that regime, or if the derived error tube plus reference trajectory is proved contained in it.

Thus:
LOCAL REGIME SMALL-GAIN PASS != GLOBAL TRAJECTORY ADMISSION.

Required fields:
REGIME_DOMAIN
COEFFICIENT_BOUNDS_VALID_ON
TUBE_SELF_CONSISTENCY = PASS/FAIL/UNRESOLVED.

NORM TYPING:
E is a chosen aggregate population-error norm/envelope. Coefficients a and b must be induced using the same species weights. Therefore kappa=ab/(cd) is a certificate-specific quantity under coarse aggregation, not an intrinsic physical observable.

If E=sum w_h|e_h| and |delta F_X|<=sum r_h|e_h|, one legal bound is a>=max_h(r_h/w_h). b must use the same weighting contract.

FLOOR FORCING:
A uniform Fmax must hold for every admissible path in the claimed regime. A value measured on one nominal path is not automatically a uniform coupled-path envelope.

SOURCE-NATIVE BOUNDS:
b_h<=L_S+Nmax L_D is legal when the derivative and Nmax bounds hold on the same bootstrap regime.
The directional-rate sensitivity bound for a is also legal when norm-matched.

FINAL:
COUPLED_PATH_COMPARISON_SYSTEM=PASS_EXACT_CONDITIONAL.
SMALL_GAIN_CD_GT_AB=PASS_SUFFICIENT.
UNIFORM_INVARIANT_BOX=PASS_EXACT_CONDITIONAL.
DINI_DERIVATIVE_FORMALIZATION=MINOR_REPAIR.
REGIME_BOOTSTRAP_SELF_CONSISTENCY=REQUIRED.
NORM_WEIGHT_CONTRACT=REQUIRED.
KAPPA_INTRINSIC_PHYSICAL_PARAMETER=NO.
SOURCE_NATIVE_a_b_c_d_CURRENT_RUN=NOT_EVALUATED.
UNIFORM_F_FLOOR_CURRENT_RUN=NOT_EVALUATED.
PBH_DE_DYNAMIC_ACCURACY=OPEN.
PBH_Yp_DH_TARGET_VALIDATION=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NOVELTY_CANDIDATE=NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration.
