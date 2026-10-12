# Geeky-S10 DRAFT018 Front B signed target-kernel source-stress conditioning gate

RETURN_ID: GEEKY-S10-DRAFT018-FRONTB-SIGNED-TARGET-KERNEL-SOURCE-STRESS-CONDITIONING-GATE-001  
DATE: 2026-10-12  
STATUS: PASS_EXACT_WITH_FIXED-KERNEL_GUARD / NO PBH BOUND / NO CANON / NO EXEC_SIGN

Durable native Google Doc:
https://docs.google.com/document/d/1NUlMaJpMnzSmR1Of1VuQm9ejTHs0JuJKUiDwFIup-5Y/edit

## Currentness

- DRAFT018 is the controlling LT working head under MT13 temporary LT coverage.
- H8R-C SOURCE_INTERFACE_UNRESOLVED is the controlling post-DRAFT018 overlay.
- XH-S3 harvest 023: Wu-Xu E0 p≈-1.20 is a plausible local effective scaling, not an exact M->0 QCD asymptote; finite-window source-error sign remains unknown.
- Front B remains open at terminal source validation, PBH DE dynamic accuracy and Yp/DH target validation.

## Exact fixed-kernel theorem

Let dnu be a positive baseline source measure and W a real signed target kernel.

C0 = ∫ W dnu.

Under a multiplicative source stress m>=0:

C1 = ∫ W m dnu,

Delta C = ∫ W(m-1)dnu.

Define

epsilon_inf = ess sup |m-1|.

Then

|Delta C| <= epsilon_inf ∫ |W| dnu.

If C0 != 0, define the signed-kernel condition number

kappa_W = (∫|W|dnu)/|∫Wdnu| >= 1.

Then

|Delta C|/|C0| <= kappa_W epsilon_inf.

With W=W_+-W_-:

kappa_W = (C_+ + C_-)/|C_+ - C_-|,

and the cancellation margin is

rho_W = 1/kappa_W.

If kappa_W epsilon_inf < 1, the sign of a nonzero baseline response cannot flip under the declared fixed-kernel perturbation family.

## Positive-weight recovery

If W>=0 and C0>0, kappa_W=1.

Therefore the result recovers MT13 Rotation 19 as the special positive-weight case. MT13's min/max multiplicative ratio envelope remains sharper there.

## Exact cancellation counterexample

Take two disjoint regions A,B of equal baseline measure and

W=+1 on A,
W=-(1-epsilon0) on B,

with epsilon0>0 small.

Then

kappa_W=(2-epsilon0)/epsilon0 -> infinity.

Thus arbitrarily small uniformly bounded source stress can produce arbitrarily large relative target change when the baseline target is cancellation-dominated.

Firewall:

SMALL UNIFORM SOURCE ERROR != SMALL RELATIVE TARGET ERROR.

## Wu-Xu / source-prior placement

For E0/E1a slope stress m_delta(x)=x^delta on x in [x_min,1]:

epsilon_inf =
1-x_min^delta for delta>=0,
x_min^delta-1 for delta<0.

For the curved QCD prior E1b, any valid finite-window ratio envelope

m_min <= q_E1b/q_E0 <= m_max

gives

epsilon_inf=max(|m_min-1|,|m_max-1|).

Sparse direct points do not by themselves provide a full-integral certificate.

## Kernel-feedback guard

If source perturbation changes the background/trajectory so W1!=W0:

C1-C0 =
∫ W0(m-1)dnu
+
∫ (W1-W0)m dnu.

Only the first term is controlled by this theorem. The second requires source-matched nonlinear/adjoint/full-comparator control.

## Species-resolved extension

For species h:

|Delta C| <= sum_h epsilon_h ∫ |W_h| dnu_h.

Therefore:

TOTAL HADRON SOURCE AGREEMENT != SPECIES-RESOLVED TARGET AGREEMENT.

## Disposition

SIGNED_KERNEL_SOURCE_STRESS_GATE = PASS_EXACT_AS_TEMPLATE.  
POSITIVE_WEIGHT_MT13_CERTIFICATE = RETAINED_AS_SHARPER_SPECIAL_CASE.  
FRONTB_SOURCE_TO_TARGET_VALIDATION = OPEN_SOURCE_MATCHED.  
TERMINAL_SOURCE_PHYSICAL_VALIDATION = OPEN.  
PBH_DE_DYNAMIC_ACCURACY = OPEN.  
PBH_YP_DH_TARGET_VALIDATION = OPEN.  
SOURCE_MATCHED_K_PBH = UNDEFINED.

Mature host: weighted integral inequalities / signed-measure total variation / condition-number analysis.

NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK.
