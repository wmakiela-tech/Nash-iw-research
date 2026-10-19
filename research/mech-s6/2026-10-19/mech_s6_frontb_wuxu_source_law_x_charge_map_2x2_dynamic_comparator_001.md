# MECH-S6 Front B — Wu–Xu source-law × charge-map 2×2 dynamic comparator

**RETURN_ID:** MECH-S6-FRONTB-WUXU-SOURCE-LAW-X-CHARGE-MAP-2X2-DYNAMIC-COMPARATOR-001  
**CELL:** IW_MECH_LINEAGE_001_SUCCESSOR_05 / Mech-S6  
**DATE:** 2026-10-19  
**EXPOSURE:** PUBLIC  
**CUSTODY:** GITHUB_PENDING_BW_INGEST  
**RESULT_CLASS:** two-factor dynamic executor comparator / interaction audit / no physical endpoint  
**CLAIM CEILING:** NO MODERN YP/DH ENDPOINT / NO PBH BOUND / NO CANON / NO EXEC_SIGN / NO NOVELTY CLAIM

## 1. Question

Two independent source-interface discrepancies are now established for the visible Wu–Xu v2 executor:

1. **source-law factor**
   - visible public helper below \(10^9\) g: species-specific edge log-log extrapolation, approximately \(M^{-1.20}\);
   - paper-declared method below \(10^9\) g: analytical rates calibrated at \(10^9\) g and scaling as \(M^{-1.3}\);

2. **charge-map factor**
   - literal public executor: aggregate \(\pi^\pm,K^\pm,p+\bar p,n+\bar n\) columns are injected into single tracked charge/antiparticle states;
   - conditional charge-symmetric candidate \(B_{\rm sym}\): affected single-species sources receive one half of the aggregate pair source, while \(K_L^0\) is unchanged.

M13 Rotation08 proved at source level that these factors interact and cannot be corrected additively.

This return executes the full dynamic \(2\times2\) contrast at one fixed diagnostic point.

## 2. Four cells

The factors are:

- source law \(L\in\{\text{public helper},\text{paper }M^{-1.3}\}\);
- reaction map \(B\in\{B_{\rm exec},B_{\rm sym}\}\).

The four executed cells are:

| source law | reaction map | shorthand |
|---|---|---|
| public helper | \(B_{\rm exec}\) | public_exec |
| public helper | \(B_{\rm sym}\) | public_sym |
| paper \(M^{-1.3}\) below \(10^9\) g | \(B_{\rm exec}\) | paper_exec |
| paper \(M^{-1.3}\) below \(10^9\) g | \(B_{\rm sym}\) | paper_sym |

The paper-law branch is species-wise continuous at the first table row:

\[
Q_h(M)=
Q_h(10^9{\rm g})
\left(\frac{M}{10^9{\rm g}}\right)^{-1.3},
\qquad
M<10^9{\rm g}.
\]

For \(M\ge10^9\) g the public table/interpolator is retained unchanged.

## 3. Numerical contract

Audited upstream:

- Wu–Xu repository commit: d395183674cace6c9906a8911bdeb7234ba4040d
- pinned NaturalUnits commit: 4a9f007ff1df416c9fef28c4d83d8fe8846099cf
- Julia: 1.12.3
- upstream BITS=100
- same package versions as the previous Mech-S6 dynamic comparator.

Diagnostic point:

\[
M_{\rm PBH}^{\rm initial}=6\times10^9\,{\rm g},
\qquad
\beta=10^{-16}.
\]

This is a deliberately strong reduced-executor diagnostic, not an exclusion-bound point.

The code evaluates its reduced endpoint proxy at:

\[
T_{\rm nuc}=0.07818527068831995\ {\rm MeV}.
\]

## 4. Implementation controls

Paper-law patch:

research/mech-s6/2026-10-19/apply_wuxu_paper_subedge_law.py

Charge-map patch:

research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py

Both are fail-closed against audited upstream contract drift.

Paper-law static CI:

- run 39262167139
- unit-tests: SUCCESS.

Dynamic runs:

- public-law pair: run 39074426824
- paper-law pair: run 39262167153.

All four ODE solves completed successfully.

The paper-law \(B_{\rm sym}\) cell was independently rerun in workflow 39262588261.

Its trajectory SHA256 is identical in both runs:

ead81fc946ba5067447a93b9b6dea6174d8bb2eaea51fae577b0139fcf8e2769

Therefore:

**PAPER_SYM_INDEPENDENT_REPLICATION = BIT_IDENTICAL.**

## 5. Raw custody

Public-law artifact:

- run: 39074426824
- artifact: 12116193467
- ZIP SHA256: 75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5

Paper-law artifact:

- run: 39262167153
- artifact: 12192535869
- ZIP SHA256: 3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e

Paper trajectories:

- paper_exec SHA256: a30245ad7522da8849fc7c63464792e32e4407ff8e4c491ae6270b8755ce48b3
- paper_sym SHA256: ead81fc946ba5067447a93b9b6dea6174d8bb2eaea51fae577b0139fcf8e2769

Independent paper_sym replication:

- run: 39262588261
- artifact: 12192726250
- same trajectory SHA256 as above.

## 6. Four-cell reduced endpoint

The Wu–Xu reduced \(Y_P\) proxy is:

| cell | reduced \(Y_P\) proxy |
|---|---:|
| public_exec | 1.3230817938392783 |
| public_sym | 1.3177406564166434 |
| paper_exec | 1.3229769529861870 |
| paper_sym | 1.3178103739910758 |

At this diagnostic point all values are \(>1\).

Therefore these values are **not physical helium mass fractions**.

They are only a deterministic scalar diagnostic of the reduced executor.

The code defines

\[
Y_P=\frac{2X_n(T_{\rm nuc})}{1-X_n(T_{\rm nuc})}.
\]

The corresponding inferred \(X_n(T_{\rm nuc})\) values are:

| cell | inferred \(X_n(T_{\rm nuc})\) |
|---|---:|
| public_exec | 0.3981490303043891 |
| public_sym | 0.3971801273460239 |
| paper_exec | 0.3981300417378147 |
| paper_sym | 0.3971927944772350 |

## 7. Charge-map effect depends on source law

With the public helper held fixed:

\[
\Delta_B Y_P|_{\rm public}
=
Y_{\rm public,sym}-Y_{\rm public,exec}
=
-0.005341137422634867,
\]

or approximately:

\[
-0.403689\%.
\]

With the paper \(M^{-1.3}\) branch held fixed:

\[
\Delta_B Y_P|_{\rm paper}
=
Y_{\rm paper,sym}-Y_{\rm paper,exec}
=
-0.005166578995111193,
\]

or approximately:

\[
-0.390527\%.
\]

Thus the charge-map correction remains the dominant endpoint-level effect in this one-point reduced diagnostic, but its magnitude is source-law dependent.

## 8. Source-law effect changes sign with reaction map

Under the literal executor map:

\[
\Delta_L Y_P|_{B_{\rm exec}}
=
Y_{\rm paper,exec}-Y_{\rm public,exec}
=
-0.00010484085309125923,
\]

approximately:

\[
-0.007924\%.
\]

Under the charge-symmetric candidate:

\[
\Delta_L Y_P|_{B_{\rm sym}}
=
Y_{\rm paper,sym}-Y_{\rm public,sym}
=
+0.00006971757443241522,
\]

approximately:

\[
+0.005291\%.
\]

Therefore:

**THE SOURCE-LAW EFFECT REVERSES SIGN WHEN THE SOURCE-REACTION MAP IS CHANGED.**

This is a direct numerical demonstration that the two repairs cannot be applied as independent additive corrections.

## 9. Exact factorial interaction

Define the dynamic interaction:

\[
I_Y
=
Y_{\rm paper,sym}
-
Y_{\rm paper,exec}
-
Y_{\rm public,sym}
+
Y_{\rm public,exec}.
\]

Numerically:

\[
I_Y
=
+0.00017455842752367445.
\]

Relative to public_exec:

\[
I_Y/Y_{\rm public,exec}
\approx
+0.0131933\%.
\]

The interaction is:

- about 3.27% of the public-law charge-map effect magnitude;
- about 1.66 times the source-law effect magnitude under \(B_{\rm exec}\);
- about 2.50 times the source-law effect magnitude under \(B_{\rm sym}\);
- about 9.94 times the absolute factorial-average source-law main effect, because the two conditional source-law effects nearly cancel.

Thus:

**SMALL AVERAGED SOURCE MAIN EFFECT != NEGLIGIBLE SOURCE-LAW × MAP INTERACTION.**

For inferred \(X_n(T_{\rm nuc})\):

\[
I_{X_n}
=
+3.1655697785459846\times10^{-5}.
\]

## 10. Supported-domain charge-map materiality is robust to the source-law ambiguity

The paper and public source laws are identical for \(M\ge10^9\) g.

Numerically, on every saved source-active point with \(M_{\rm PBH}\ge10^9\) g:

\[
\Delta_B X_n|_{\rm paper}
=
\Delta_B X_n|_{\rm public}
\]

exactly in the saved data.

Likewise the saved \(A,B,F_{\rm had}\) charge contrasts are identical between the two source-law branches in that supported region.

The already established charge-map maximum therefore survives the \(2\times2\) test unchanged:

\[
\max|\Delta_B X_n|
=
0.0728514990160335
\]

at approximately:

- \(T=0.393875\) MeV,
- \(M_{\rm PBH}=5.79601\times10^9\) g.

And:

\[
\max|\Delta_B F_{\rm had}|
=
1.0728507210500483\times10^{-25}\ {\rm GeV}
\]

at approximately:

- \(T=3.07730\) MeV,
- \(M_{\rm PBH}=5.99696\times10^9\) g.

Therefore:

**SUPPORTED-DOMAIN CHARGE-MAP MATERIALITY DOES NOT DEPEND ON WHICH SUBEDGE SOURCE LAW IS CHOSEN.**

This is stronger than the previous one-factor result.

## 11. Where the source-law interaction enters

At all saved supported source-active points:

\[
\Delta_L X_n=0,
\qquad
I_{X_n}=0.
\]

The first saved nonzero source-law contrast occurs at output index 1470, after the PBH source has been zeroed in the saved trajectory.

At the public_exec coordinate of that saved point:

- \(T\approx0.142434\) MeV;
- saved \(M_{\rm PBH}\approx8.45\) g;
- saved hadronic \(A=B=F_{\rm had}=0\).

Nevertheless the four \(X_n\) trajectories already differ because the adaptive solver internally traversed the terminal \(M<10^9\) g interval between saved samples.

At that first post-evaporation saved point:

\[
\Delta_L X_n|_{B_{\rm exec}}
\approx
-2.05243\times10^{-5},
\]

\[
\Delta_L X_n|_{B_{\rm sym}}
\approx
+1.35590\times10^{-5},
\]

and

\[
I_{X_n}
\approx
+3.40833\times10^{-5}.
\]

Thus the sign-changing interaction is already deposited during the unresolved internal terminal integration, before the reduced nucleosynthesis endpoint is sampled.

## 12. Saved-point limitation

The largest saved post-terminal source-law contrasts in \(X_n\) are:

\[
\max|\Delta_L X_n|_{B_{\rm exec}}
=
2.372756\times10^{-4},
\]

\[
\max|\Delta_L X_n|_{B_{\rm sym}}
=
3.026261\times10^{-5},
\]

and:

\[
\max|I_{X_n}|
=
2.282656\times10^{-4}.
\]

However, at saved points the source-law contrasts of \(A,B,F_{\rm had}\) are zero because the output grid skips from the last active above-edge sample to post-evaporation points where hadron sources have been zeroed.

Therefore:

**SAVED A/B/F SOURCE-LAW CONTRAST = 0**

does **not** imply:

**INTERNAL TERMINAL A/B/F SOURCE-LAW CONTRAST = 0.**

A terminally densified or internal-step instrumented run is required to resolve that mechanism directly.

## 13. Floor audit

Across all four runs, every saved source-active floor flag is zero for:

- \(\pi^-\),
- \(\pi^+\),
- \(K^-\),
- \(K_L^0\),
- \(\bar p\),
- \(\bar n\).

Therefore the saved-point \(2\times2\) contrasts are not contaminated by an observed active log-floor interval.

Guard retained:

**SAVED FLOOR INACTIVITY != INTERNAL-STEP FLOOR INACTIVITY PROOF.**

## 14. Interpretation

The \(2\times2\) gives three distinct conclusions.

### A. Charge-map problem is independently material

Its strongest dynamic effect occurs entirely inside the directly tabulated source domain and is exactly unchanged by the subedge source-law choice.

### B. Paper-vs-helper source-law mismatch is smaller at this one reduced endpoint but not additively separable

Its conditional endpoint effect is small in absolute terms here, but it changes sign between \(B_{\rm exec}\) and \(B_{\rm sym}\).

### C. Interaction matters for attribution

Because the source-law main effect reverses sign, one cannot infer a source-exponent correction and then separately apply a factor-two charge correction.

The reaction map must be fixed before the source-law effect can be assigned a sign at this endpoint.

## 15. What this does not establish

The paper-declared \(M^{-1.3}\) branch is implemented here exactly as described by XH026:

- BlackHawk/public table at and above \(10^9\) g;
- analytical \(M^{-1.3}\) branch below;
- species-wise normalization at the \(10^9\) g edge.

But XH-S4 has not yet established exact file-level genealogy between this branch and the numerical payload used for the final published JCAP scan figures.

Therefore:

**PAPER-DECLARED METHOD != PROVEN PUBLISHED NUMERICAL RUN LINEAGE.**

This return does not establish:

- a correction to the published PBH bound;
- a physical modern \(Y_P\) or D/H result;
- source-valid high-energy hadronization below \(10^9\) g;
- a full mass–\(\beta\) result;
- internal-step floor inactivity;
- CANON / EXEC / novelty.

## 16. Status

PAPER_SUBEDGE_PATCH_STATIC_CONTRACT = PASS_CI

FOUR_DYNAMIC_CELLS = PASS

PAPER_SYM_INDEPENDENT_REPLICATION = PASS_BIT_IDENTICAL

SUPPORTED_DOMAIN_CHARGE_MAP_EFFECT = MATERIAL_AND_SOURCE_LAW_ROBUST

REDUCED_YP_CHARGE_EFFECT_PUBLIC = -0.403689_PERCENT_DIAGNOSTIC

REDUCED_YP_CHARGE_EFFECT_PAPER = -0.390527_PERCENT_DIAGNOSTIC

REDUCED_YP_SOURCE_EFFECT_BEXEC = -0.007924_PERCENT_DIAGNOSTIC

REDUCED_YP_SOURCE_EFFECT_BSYM = +0.005291_PERCENT_DIAGNOSTIC

REDUCED_YP_FACTOR_INTERACTION = +0.013193_PERCENT_OF_PUBLIC_BASELINE

SOURCE_LAW_EFFECT_SIGN_FLIP_ACROSS_MAP = PASS_NUMERICAL

SAVED_SUPPORTED_SOURCE_LAW_EFFECT = ZERO_BY_CONSTRUCTION_AND_RUN

INTERNAL_TERMINAL_SOURCE_LAW_MECHANISM = NOT_RESOLVED

PUBLISHED_PAPER_BOUND_CORRECTION = NOT_ESTABLISHED

MODERN_YP_DH_ENDPOINT = NOT_RUN

SOURCE_VALID_E2B = OPEN

SOURCE_MATCHED_K_PBH = UNDEFINED

NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY

## 17. Cheapest next control

The next high-value control is no longer another endpoint rerun.

It is **terminal-window instrumentation** of the same \(2\times2\) design:

- save or instrument internal states while \(M_{\rm PBH}\) traverses \(10^9\) g down to evaporation;
- resolve \(Q_h\), populations, \(A,B,F_{\rm had}\), floor status and \(X_n\);
- identify where and why the source-law effect changes sign between \(B_{\rm exec}\) and \(B_{\rm sym}\).

That directly localizes the interaction mechanism before any full mass–\(\beta\) scan or modern BBN endpoint is attempted.

## 18. Reproducibility assets

Paper-law patch:

research/mech-s6/2026-10-19/apply_wuxu_paper_subedge_law.py

Paper-law patch CI:

run 39262167139

Charge-map patch:

research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py

Dynamic harness:

research/mech-s6/2026-10-18/wuxu_dynamic_comparator/

Durable machine-readable \(2\times2\) summary:

research/mech-s6/2026-10-19/wuxu_source_law_x_charge_map_2x2_summary_001.json

Raw public-law artifact:

12116193467

Raw paper-law artifact:

12192535869

Independent paper_sym replication artifact:

12192726250
