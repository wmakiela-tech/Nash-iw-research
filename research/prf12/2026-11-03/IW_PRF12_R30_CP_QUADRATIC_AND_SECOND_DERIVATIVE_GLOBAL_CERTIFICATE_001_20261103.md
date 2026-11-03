---
artifact_id: IW_PRF12_R30_CP_QUADRATIC_AND_SECOND_DERIVATIVE_GLOBAL_CERTIFICATE_001_20261103
created_at: 2026-11-03
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_SECOND_DERIVATIVE_GLOBAL_CERT / QUADRATIC_CP_NUISANCE_CORNER_THEOREM / SOURCE_RESET_FLOOR_EXACT_FORMULA / B_LINDBLAD_CP_CORNER_CERT / NONIID_N1682_EXACT_TAILS / FULL_ALPHABET_ANYTIME_UPLIFT / INDEPENDENT_2X2_4X4_PASS / REFEREE_PENDING
claim_ceiling: NOT_FULL_12_CATEGORY_MINIMAX / NOT_UNRESTRICTED_PHYSICAL_HARDWARE / CP_BETA_NUMERIC_SPECIAL_FUNCTION_LIMIT / NO_ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE / NO_NOVELTY / NO_CANON / NO_EXEC
---

# PRF12 R30 — tightening the complete source certificate via second derivatives and exact calibration geometry

**Date:** 2026-11-03. **Function:** PRF12. **Scientific status:** author-derived exact inequalities with independent numerical checks; **independent referee pending**. The result is an uplift of the R28/R29 **same physical two-shot source-control experiment**, not a new quantum measurement and not a resolution of the original three-qubit LOCC closure question.

## 0. Source and claim ceiling

First owner: PRF11 R35 source A (quasi-static symmetric Cauchy detuning) versus B (independent Cauchy–Lévy increments). Direct owners: PRF12 R23 fixed source-active rectangular physical control; R24/R25 conditional hidden-variable-aware source reset hazard; R26 fixed-reference Clopper–Pearson effective detector calibration; R28 signed-quartet Bernoulli test; R29 deterministic full-alphabet anytime e-process and precise negative knowledge that its Jensen improvement had not yielded a better fixed-N bound.

**Unchanged model:** one qubit freshly prepared and destructively measured TWICE per pair. The two shots share an identical hidden Xi if no reset. Xi may persist arbitrarily across many pairs or vary with arbitrary dependence between pairs. A reset INSIDE a pair is allowed, with no-reset survival at least `s=exp(-lambda*span)` **conditioned additionally on current hidden Xi, independently selected axis and any hazard-relevant latent variables**, or under an exogenous Poisson reset clock independent of such variables. Conditional independent measurement shots, stable detector, independent private axis and postmeasurement coins are essential. Under B, each shot has continuous source-active Lindblad dephasing also during preparation and analysis pulses. No iid Xi assumption is made.

Physical parameters remain gamma=1, max Rabi amplitude Omega=10, free exposure Delta=.5, Y preparation and X/Y source-on analysis pulse length `tp=pi/20`, ideal terminal Z projection; weights `(w_X,w_Y,w_Z)=(.18,.20,.62)`. Effective calibrated detector map is `E[R|m]=c*m+d`, including R25's declared terminal T1 and asymmetric assignment errors; no stochastic detector drift or correlated readout. Data for the calibration are **SYNTHETIC**: `n0=46000, k0=45540, n1=69000, k1=3705`.

Postmeasurement R28 score `f(j,++/--)`:

| Basis | `++` | `--` | `+-`,`-+` |
|---|---:|---:|---:|
| X | .94 | 1.00 | 0 |
| Y | .88 | .96 | 0 |
| Z | .36 | .02 | 0 |

A private coin generates genuine Bernoulli indicator Y with success probability equal to that score. THIS test, unlike an assumed full-likelihood ratio, has exact non-iid binomial stochastic domination when conditional means are bounded. R30 will **not** alter these coefficients, axes, physical operation or 115000 reference-shot cost.

## 1. Theorem R30.1 — quadratic nuisance-corner enclosure over the FULL CP rectangle

For any conditional, no-reset source A phase Xi, let `m_j(Xi)` be the pre-detector ideal mean of final Z readout for analysis choice j. It is real and |m_j|<=1. With `alpha_j,beta_j` from the table above, define

 `F_j(u)=[alpha_j(1+u)^2+beta_j(1-u)^2]/4`,
 `P_A(Xi;c,d)=sum_j w_j F_j(c*m_j(Xi)+d)`.

The fixed-size Clopper–Pearson reference intervals at joint coverage at least 99% give the effective detector nuisance rectangle, widened outward with additional explicit numerical buffers:

 `c in [0.93247792956...,0.93993781774...]`,
 `d in [0.03994180214...,0.04740169032...]`.

**Important:** CP beta quantiles are obtained by SciPy and enlarged outward by explicit rounding margins and independently checked through binomial tails. This is not a formal interval-arithmetic certification of the beta special function, though it is numerically robust to the displayed margins.

Fix Xi and let `(c,d)` be arbitrary in this rectangle. Write `(c,d)` as independent convex mixtures of the four corners. Direct quadratic expansion yields the **EXACT identity**

 `E_corner P_A(Xi;c_corner,d_corner)-P_A(Xi;c,d)`
 `=sum_j w_j (alpha_j+beta_j)/4 * [m_j(Xi)^2 Var(c_corner)+Var(d_corner)]`.

Here both variances are bounded by one quarter of their squared interval widths. Hence, *for every Xi and every calibrated (c,d)*,

 `P_A(Xi;c,d) >= min_{four corners} P_A(Xi;c_corner,d_corner) - H_CP`,

 `H_CP=(sum_j w_j(alpha_j+beta_j))[(c_hi-c_lo)^2+(d_hi-d_lo)^2]/16`.

Numerical, outward-enlarged `H_CP <= 0.0000066281`. This avoids repeatedly evaluating a wide interval `c*m+d` inside nonlinear squares, which is the primary avoidable overestimation in the earlier R28 certificate. No CP *point estimate* was substituted for the full nuisance rectangle.

## 2. Theorem R30.2 — rigorous O(h²) interpolation of unknown STATIC Xi

The conditional A propagator consists of source-active preparation, free sensing and source-active X/Y analysis; no statistical average over Xi is used. Let `T_j` be total time that the unknown source acts on the qubit in the chosen shot:

 `T_X=T_Y=Delta+2tp=.5+pi/10`, `T_Z=Delta+tp=.5+pi/20`.

The only Xi-dependent Hamiltonian term is Xi Z/2. Duhamel's formula gives

 `||dU_j/dXi||<=T_j/2`, `||d²U_j/dXi²||<=T_j²/4`.

Because `m_j=<Z>`, `|m'_j|<=T_j`, `|m''_j|<=T_j²`. Differentiate the exact quadratic `F_j(c*m_j+d)` twice. Using a physical detector output mean within [-1,1] and positive alpha,beta yields

 `|dF_j/dm_j|<=c_hi max(alpha_j,beta_j)`,
 `d²F_j/dm_j²=c²(alpha_j+beta_j)/2`.

Therefore a uniform, all-Xi, all-CP bound is

 `|d²P_A/dXi²|<=M_2`,
 `M_2=sum_j w_j [c_hi max(alpha_j,beta_j)+(alpha_j+beta_j)c_hi²/2]T_j²`.

`M_2<=0.57728962` after outward numerical buffer. For any interval between adjacent Xi nodes of spacing `h`, the Lagrange linear-interpolation remainder obeys

 `P_A(Xi;CP_corner) >= min(P_A(node_left),P_A(node_right)) - M_2 h²/8`.

This is a proof over **every point**, not merely a numerical scan. At h=.01 the interpolation loss is <=7.216121e-6, instead of the much larger R28 Lipschitz loss O(h). Combined with R30.1, the full compact score bound is

 `P_A(Xi;c,d)>=min_{nodes,CP corners}P_A - H_CP -M_2 h²/8`.

A standalone 7001-node mpmath.iv (45 dps) check over `Xi in [-35,35]` obtained the outward node lower 0.3196067 (node near Xi=.114). Thus

 `P_A(Xi;c,d)>=0.319592875232193` on the entire compact phase interval.

For `|Xi|>=35`, retain the source-typed analytically proved R23/R28 off-resonance bound: spin-flip leakage of each finite rectangular pulse is <=Omega/sqrt(Xi²+Omega²), yielding `m_AX,m_AY >=1-8v`, `m_AZ>=1-2v`, `v<=100/(35²+100)`. Each score F_j is a convex quadratic, so minimize explicitly on its possible output-mean interval. The tail lower is `0.39116545038768846`, which is STRICTLY ABOVE the compact bound. Hence the compact bound extends to **ALL Xi IN R**. The inherited tail lemma is an explicit source dependency, not reconstructed by the 7001 nodes.

## 3. Theorem R30.3 — exact two-shot reset-floor minimization on the CP rectangle

If a reset occurs, each shot's pre-detector Z expectation can take an arbitrary value `m_1,m_2∈[-1,1]` under the declared exogenous trajectory. The new binary score probability for each axis is

 `G_j(u_1,u_2)=[alpha_j(1+u_1)(1+u_2)+beta_j(1-u_1)(1-u_2)]/4`,
 with `u_i=c*m_i+d`.

This expression is BILINEAR in `(m_1,m_2)`. Its minimum over the full square occurs at four corners with `m_i=±1`. For `m1=m2=±1`, minimize the convex scalar function `F_j(u)` over the attainable interval `u=±c+d` by clipping its stationary point `u*=(beta_j-alpha_j)/(alpha_j+beta_j)`. For the two opposite-sign cases,

 `G_j(c+d,-c+d)=[(alpha_j+beta_j)(1+d²-c²)+2(alpha_j-beta_j)d]/4`.

This is decreasing in positive `c`, so take `c=c_hi` and clip the same stationary point for `d`. Thus an **analytic entire-rectangle minimum** follows, without assuming that reset intervals permit only CP-corner detector values. Conservative separate axis floors:

 `r_X>=.0560861853135`, `r_Y>=.0527282081249`, `r_Z>=.0180107696670`.

Weighted overall lower floor `r>=.03180783217498`. It improves the earlier independent wide-interval floor while allowing arbitrary post-reset hidden phase trajectories. It is a *conditional-on-complete-source-histories* lower bound.

## 4. Theorem R30.4 — all-CP B upper and improved exact non-iid fixed-N certificate

Under B, the three pre-detector means have verified Lindblad values

 `(m_BX,m_BY,m_BZ)≈(0.5219734434954134,0.00231335785212866,0.04809737884883814)`.

With these means fixed, the score `P_B(c,d)=sum_j w_j F_j(c*m_Bj+d)` is a CONVEX function of `(c,d)`, since all score coefficients are nonnegative. Convexity and bilinear corner interpolation imply that its maximum on the entire CP rectangle is bounded by its largest of FOUR corner values. Numerical Taylor interval 120th order calculation of the source B 3×3 Bloch generator with explicit remainder, plus independent complex density-matrix `4×4` Lindbladian exponential, gives

 `P_B <= 0.2706612016991532` with stated numeric buffers.

Let `s=exp(-lambda*pair_span)=0.965058680566...`, lambda=.02, pair span `1.7783185307179588` in gamma-normalized units. The survival condition MUST hold also conditional on Xi, axis and latent hazard factors, or be implemented by an independent Poisson clock. Since `P_A^intact >= .319592875232193` and `P_A^reset>=.03180783217498029`, mixture yields

 `P_A(Y=1|complete past)>=0.30953728591436364`,
 `P_B(Y=1|complete past)<=0.2706612016991532`.

Use strictly interior, transparent safe constants `a=.3095`, `b=.2707`. Each realized Y is a TRUE Bernoulli bit produced by the private coin; the Xi histories may be arbitrarily dependent across pairs. Conditional Bernoulli stochastic domination yields, for N=1682 and decision **A iff K_N>=488**,

 `P_A(wrong B | calibration good)<= BinomCDF(487;1682,.3095)=0.03989654588613`,
 `P_B(wrong A | calibration good)<= BinomSF(487;1682,.2707)=0.03940977664157`.

Add at most `.01` simultaneous CP confidence failure and each false declaration probability is <.05. Nonconclusive calibration stays possible; original reference data are synthetic. This is **sufficient**, not the global minimum N for all conceivable tests. It improves the R28 **2251-pair** result to **1682**, saving **569 pairs =25.28%** with NO change of physics, detector, source assumptions, axis weights or score f.

Resource comparison (same declared R28 wall clock):

| | R28 | R30 |
|---|---:|---:|
| Synthetic reference reads | 115000 | 115000 |
| Scientific pairs | 2251 | **1682** |
| Total single-sensor readings | 119502 | **118364** |
| Modeled gamma-scaled wall time | 15615.5450 | **14575.2318** |

The 6.66% modeled wall-clock reduction is modest because the calibration dominates. No real physical speedup has been measured.

## 5. Theorem R30.5 — stronger FULL TWELVE-CATEGORY anytime factors inherited from R29

Without the extra R28 Bernoulli coin, retain the signed outcome category `z=(axis,r1,r2)` and its deterministic score `f(z)` from the table. The sharper safe mean constraints define

 `G_A(z)=r_0+(r_1-r_0) f(z)`, `r_1=a/b=1.143332101957887`, `r_0=(1-a)/(1-b)=.9467982997394762`;
 `G_B(z)=s_0+(s_1-s_0) f(z)`, `s_1=b/a=.8746365105008077`, `s_0=(1-b)/(1-a)=1.0561911658218683`.

Under B, `E(G_A|past)<=1` and under A, `E(G_B|past)<=1`, including composite calibration nuisance and arbitrary Xi dependence, conditional on CP calibration success. Thus the separate products are nonnegative test supermartingales. Threshold 25 and Ville's inequality bound each wrong crossing by <=.04 plus <=.01 calibration failure. The correct factors are NOT reciprocals because f is fractional.

The R29 Rao–Blackwell/Jensen calculation applies verbatim. The Z++ fractional category and analytic `m_A,Z(Xi)>=0` yield conservative positive uniform lower bounds on `E[f(1-f)|past]`. The certified lower **per-pair expected log evidence** improves to

 `under A >= .00425814626798062`,
 `under B >= .004231699158336381`,

versus R29's `.003188829529778685 / .003179830816085791`: +33.53% and +33.08% improvement in these LOWER BOUNDS. This is NOT a proof of lower stopping time in every trajectory or a new globally optimized 12-category factor. R30 has improved the old complete-category factors through a stronger source certificate, without optimizing arbitrary category weights.

## 6. Reproducibility and falsification

Full independent, runnable Python3 + NumPy + SciPy + mpmath.iv includes (i) CP p0,p1 tail inversion with outward buffering, (ii) 7001 directed-interval phase nodes and all four CP corners, (iii) the exact calibration quadratic penalty, (iv) a Duhamel analytic second-derivative bound, (v) old off-resonance analytic tail, (vi) exact full CP reset floor, (vii) independent Taylor-interval B source channel, (viii) exact binomial sample thresholds and (ix) sharpened opposite-null deterministic e-factors.

Separate physically independent test (NOT importing main source) computes source A with complex 2×2 matrix exponentials, source B with 4×4 Liouvillian exponentials, checks the corner-mixture inequality on many interior detector points, finite-difference numerical second derivatives, explicit reset-floor search and exact binomial tails. Main and independent runs PASS. A 3501-node coarser control is available but 7001 nodes are the controlling certificate.

**Unresolved/negative knowledge:** Full global optimization of the 12-category composite-null factors is still OPEN. The new fixed-N test uses precisely R28's private Bernoulli coin; the stronger full-alphabet factors belong to the separate anytime procedure. R30 is primarily a new **proof-efficiency / nuisance-set geometry uplift**, not a new physical source observable. The full original single-copy three-party LOCC-closure problem retracted in R09 remains OPEN. Not an experimental implementation, not a source novelty claim, no review approval, no CANON or EXEC. The special-function inversion of CP endpoints uses non-directed SciPy beta quantiles and outward buffers with independent tail checks, NOT a formal proof assistant or fully directed interval certificate for all special functions. Science conditional error claims require the Xi-conditional hazard and stationary detector assumptions exactly as stated. BW ingestion and independent scientific referee pending.

**Next R31:** Either pursue fully composite-optimal 12-category e-factor design with independent all-Xi interval verification, or replace synthetic fixed calibration with a real drift-aware and optionally stopped calibration confidence sequence; NEVER assume free quantum resources or iid Xi to claim improvement.

RETURN: PRF12_R30 / CP_QUADRATIC_CORNER_AND_DUHAMEL_SECOND_DERIVATIVE_GLOBAL / 1682_PAIR_NONIID_CERTIFICATE / SAME_R28_HARDWARE / R29_DETERMINISTIC_E_PROCESS_SHARPENED / INDEPENDENT_2X2_4X4_REPRO_PASS / FULL_ALPHABET_MINIMAX_UNSOLVED / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
