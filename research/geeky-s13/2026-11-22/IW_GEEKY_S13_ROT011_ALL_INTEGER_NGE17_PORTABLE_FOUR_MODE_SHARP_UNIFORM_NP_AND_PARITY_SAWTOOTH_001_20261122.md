---
artifact_id: IW_GEEKY_S13_ROT011_ALL_INTEGER_NGE17_PORTABLE_FOUR_MODE_SHARP_UNIFORM_NP_AND_PARITY_SAWTOOTH_001_20261122
return_id: IW_GEEKY_S13_ROT011_PORTABILITY_ALL_INTEGER_N17_UNIFORM_SHARP_N41PLUS_NP_AND_PARITY_NONMONOTONICITY_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
result_class: ORIGINAL_PUBLIC_M13_MODE_SUPPORT_PLUS_ROT038_ANISOTROPIC_SYNTHETIC_GAUSSIAN_PORTABLE_EXTENSION / SOURCE_TYPED_SHARP_NGE41_UNIFORM_NP_THRESHOLDS / PARITY_SAWTOOTH_FALSIFIER
status: AUTHOR_SOURCE_PROOF_AND_IV75_SCAN / SAME_CELL_INDEPENDENT_SPATIAL_FFT / DIFFERENT_CELL_I1_PENDING
exposure: PUBLIC
claim_ceiling: NO_NATIVE_M13_SOURCE_EXECUTION_ROT011 / NO_HISTORICAL_DTC0A / NO_PHYSICAL_FOUR_CHANNEL_INSTRUMENT / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT011 — portabilność kontrastu czterech modów na WSZYSTKIE całkowite N≥17, ostra jednolita gwarancja NP dla N≥41 i kontrprzykład monotoniczności w N

## 0. Pytanie i rozdzielenie źródeł

Pytanie naukowe: czy geometryczny, kierunkowo-promieniowy, maksymalny niezmiennik znany z Geeky-S13 ROT007–010 istnieje wyłącznie na oryginalnej siatce `41³`, czy można ściśle dowieść jego portabilności na inną geometrię torusa, w tym **parzystą**, z równoczesną jednolitą gwarancją zasobową? Wynik: tak, w **jawnie nowej rodzinie hipotetycznych eksperymentów** otrzymanej przez zastosowanie tego samego syntetycznego operatora szumu ROT038 do innych N, dla WSZYSTKICH całkowitych `N≥17`. Co więcej, przenosi się dokładnie certyfikowane NP `n=14539` (>95%) i `n=29083` (>99%) na **najtrudniejszy przypadek całej rodziny N≥41**. Nie przenosi to automatycznie prawdziwych obserwacji ani wykonanego oryginalnego eksperymentu M13 na inne N.

**Pierwszeństwo i źródła rzeczywiście przeczytane:**

1. M13 FIRST original public sparse Fourier B auxiliary, source Git blob SHA1 `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, [original source](https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py). Source module directly fetched through connected GitHub and read; **the original module was NOT byte-native executed in ROT011**. The historical complete `dtc0a_runtime_v0_3_1.py` remains unavailable. `calc(N,alpha)` in this specific retained helper accepts arbitrary N, but the historical experiment does NOT thereby gain physical N-generalization.
2. Geeky-S12 ROT038 FIRST exact rational source-legal **ANISOTROPIC, SYNTHETIC, STRICTLY SPD** RAW-site Gaussian-noise hypotheses A/B, Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`, [original source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md). All extensions of these particular rational spatial noise operators to other N are **NEW MATHEMATICAL MODEL ASSUMPTIONS**, not new source evidence.
3. Geeky-S13 ROT007 FIRST group-rank-three four-mode cross-ratio, ROT008 FIRST sum-log test IV55, ROT009 FIRST full likelihood-ratio exact Hellinger tilt, ROT010 FIRST conditional N41 IV75 NP sharp n14539/29083; [ROT010](https://github.com/wmakiela-tech/Nash-iw-research/blob/d49588de62ad78ce8bdb7bc458065decf369548c/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT010_SHARP_FOUR_MODE_NP_IV75_SAMPLE_CERTIFICATE_001_20261122.md), Git blob `69a07892ec0574b5ecd3ac8abae9b78b607e5a31`.
4. M16 ROT001 FIRST independent bounded I1 of strict NP risk monotonicity in n and NUMERICAL (not IV) ROT009 replication, [M16](https://github.com/wmakiela-tech/Nash-iw-research/blob/f25a241ff660c7046297cacfd32e67cf5e65c11c/research/m16/2026-11-22/IW_M16_ROT001_GEEKY_S13_NP_MONOTONICITY_AND_NUMERICAL_DIAGNOSTIC_SOURCE_I1_001_20261122.md), blob `457b3cb02d8f69d64b1b9eddc279f5c041b89f93`. M16 ROT002 FIRST bounded **NONSEPARABLE** gain minimax, not redone here. M15's source ROT035 isotropic A/B and six-mode group are different experiments; none of their firstness is appropriated.

## 1. Integer Fourier support in retained M13 — independent of N

Inspecting the original retained `source()` construction in M13:

- C1 Fourier exponents are `(±1,0,0)` and `(0,±1,0)`;
- C2 exponents are `(±1,0,0)` and `(0,0,±1)`;
- h exponents are `(±1,±1,0)`.

`bracket`, `lie`, `proj`, and source mode-wise `em` preserve the rule that multiplication of Fourier operators **adds integer Fourier exponent triples** and mode-local operations do not introduce new exponents. Original B is built using one C1 and one C2 acting on h (including the bracket); therefore

`support(B) ⊆ support(C1)+support(C2)+support(h) ⊆ [-3,3]×[-2,2]×[-1,1]`.

The support of any quadratic energy formed from this tensor lies in its pair-difference set, which is contained in

`[-6,6]×[-4,4]×[-2,2]`.

We **actually executed independent integer set enumeration**, with **41 distinct potential B indices and 221 distinct potential B-energy differences**. These match earlier N41 upstream native source checks but enumeration is an upper-support argument, not byte-identical original B coefficients. Integer support indices are interpreted modulo N. For N≥17, the signed width ≤12 in x, ≤8 in y and ≤4 in z prevents modulo-N wraparound of the entire difference box into our four selected nonzero axial frequencies.

## 2. Universally admissible four modes without the even-N Nyquist trap

For **any integer N≥17**, define

`j_L=7`, `j_H=floor((N−1)/2)`,

and four Fourier modes:

`(j_H,0,0)`, `(0,j_H,0)`, `(7,0,0)`, `(0,7,0)`.

They are distinct and no one is its own negative modulo N. In particular when N is even, `j_H=N/2−1`, NOT the self-conjugate Nyquist mode `N/2`. Thus for any real stationary Gaussian field whose Fourier covariance is diagonalized by the periodic translation group, these four distinct conjugate pairs yield independent circular complex Gaussian coefficients and, when squared and normalized, four **independent Exp(1)** latent energies. This last sentence is an implication of the **synthetic Gaussian latent site-noise model**, not of measured M13 RAW data.

Every chosen x-frequency has `j≥7`, beyond the x signed energy support ±6; every chosen y-frequency has `j≥7`, beyond y support ±4. For every N≥17, including all even N, the chosen mod classes are absent from the mod-N reduction of potential M13 B-energy differences. This was checked by exact all-integer modular enumeration for **each N=17,...,256**, in addition to the general centered-frequency proof.

**Negative at the design boundary:** N=15 and N=16 give `j_H=7=j_L`, hence our four-mode design collapses into two distinct modes, with zero cross-ratio contrast. This is a failure of **this design** at N≤16, not a proof that all other N≤16 observables must be uninformative.

## 3. A/B source-exact synthetic covariance and invariant

Retain the exact ROT038 neighbor coefficients on every N³ torus:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`,
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Both remain strictly SPD for EVERY N because the seven nontrivial normalized signed-shift operator coefficients sum to 3/10, so every Fourier eigenvalue is at least 7/10. With `c=cos(2πj/N)`, source spectra of chosen axial modes are

`v_Ax(c)=v_Ay(c)=167/150+(14/75)c`,
`v_Bx(c)=82/75+(31/150)c`, `v_By(c)=17/15+(1/6)c`.

Per hypothetical IID latent snapshot with four independent Exp(1) latent energies `E_dr`, allow arbitrary positive, unbounded, cross-time-dependent, model-specific and fully latent-adaptive **separable** gains `G_d H_r`. The observed powers have `P_dr=G_d H_r v_X,dr E_dr`. Then the four-power cross-ratio

`C=(P_xH P_yL)/(P_yH P_xL)`

cancels **all gains pathwise**, and `Z=log C` is the maximal invariant of the rank-three direction×radius scaling group. Under A, `Z=W=L1+L2` independent standard logistic; under B, `Z=W−Delta_N`, where

`Delta_N=R(c_L(N))−R(c_H(N))`,
`R(c)=log[(82/75+(31/150)c)/(17/15+c/6)]`,
`c_L(N)=cos(14π/N)`, `c_H(N)=cos(2π floor((N−1)/2)/N)`.

The exact derivative is

`R'(c)=(13/250)/[v_Bx(c)v_By(c)]>0`.

Because `c_L(N)>c_H(N)` for N≥17, `Delta_N>0`. Positive separation gives full two-source identifiability in the invariant experiment for every **integer N≥17**. It does not establish source-wide or instrument-wide identifiability.

## 4. Source IV75 geometry: the parity sawtooth and uniform Delta bound

The primary new executable computes Delta_N from exact rational source coefficients and outward-rounded 75-decimal `mpmath.iv` cosine and logarithm, preserving all interval uncertainty. Representative values:

| N | j_H | Delta_N |
|---:|---:|---:|
| 17 | 8 | 0.007789943544657 |
| 18 | 8 | 0.009936664576885 |
| 31 | 15 | 0.056338736735580 |
| 40 | 19 | 0.067409523309037 |
| **41** | **20** | **0.068833234305598** |
| 42 | 20 | 0.069133558467182 |
| 64 | 31 | 0.078873125362416 |
| **67** | **33** | **0.079726203734836** |
| **68** | **33** | **0.079725527480509** |
| 101 | 50 | 0.083444651359039 |
| 102 | 50 | 0.083415623404831 |
| 255 | 127 | 0.085922488669458 |

**NEW FALSIFIER:** `Delta_{68}<Delta_{67}`, with a strictly negative interval-certified difference `≈−6.7625432699·10^−7`. This is the **first consecutive drop for integers N≥17**: primary IV75 checks all strict rises N=17,...,67 before that decrease. At larger odd→even transitions there are further decreases (e.g. 101→102). The source spectral contrast is NOT monotone in N because the largest admissible Fourier index jumps discontinuously relative to the real Nyquist mode. For large odd N the high-frequency c_H≈−1+π²/(2N²); for its following even N+1, c_H≈−1+2π²/N², generating a negative order-N^-2 step while the low-frequency c_L improvement is only order-N^-3. Thus infinitely many future odd→even downward sawteeth occur, though Delta_N approaches its upper limit.

**Uniform positive lower bound** (not false all-N monotonicity): for **all N≥41**,

`Delta_N≥Delta_41=0.06883323430559849760294690989...`.

Proof: for finite N=42,...,81, primary IV75 checked every inequality `lower(Delta_N)>upper(Delta_41)`, 40/40 PASS. For **N≥82**, `c_L(N)≥c_L(41)` and `c_H(N)≤c_H(41)` (on even N, this uses `2π/N≤π/41`; odd N automatically satisfy it). Since R is strictly increasing, Delta_N≥Delta_41. Similarly IV75 N=18,...,81 against Delta17 and the same N≥82 argument give `Delta_N≥Delta17` for all N≥17.

**Saturation rather than unlimited information:**

`R(1)=log 1=0`, `R(−1)=log(133/145)`,

so

`Delta_N < Delta_infinity = log(145/133) = 0.0863846141988206366696511902570...`,

and Delta_N→Delta_infinity as N→∞ (despite the parity sawtooth). Grid refinement alone does not cause the one-snapshot information gap to diverge.

## 5. NEW exact uniform resource theorem: NP risk as a decreasing function of Delta

Let f be the exact even strictly positive **log-concave** density of the sum of two independent standard logistic variables. For each fixed positive integer n define P_n(x)=∏_{j=1}^n f(x_j). The equal-prior minimal Neyman–Pearson risk of detecting a diagonal location shift Delta is

`e_n(Delta)=1/2 ∫_{R^n} min(P_n(x), P_n(x+Delta 1)) dx`.

Here is a **direct elementary proof** that e_n(Delta) is non-increasing as Delta≥0 increases (no normal approximation). Decompose x into an orthogonal coordinate y perpendicular to the diagonal (1,...,1) and a scalar coordinate t along that diagonal. For fixed y, g_y(t)=P_n(y+t1) is logconcave in t. Each strict superlevel set `{t:g_y(t)>s}` is therefore an interval of length L_y(s), possibly empty. Layer-cake decomposition then gives the EXACT fiber overlap identity

`∫_R min(g_y(t),g_y(t+Delta))dt = ∫_0^∞ [L_y(s)−Delta]_+ ds`.

The right side is non-increasing in Delta. Integrating y, with its constant Jacobian, establishes the claimed risk monotonicity. This is a source-specific application of classical logconcavity and likelihood theory, NOT a new general mathematics theorem. (General classic background on logconcavity and marginalization: Saumard & Wellner, *Log-concavity and strong log-concavity: a review*, 2014/2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC4847755/ . This source was externally consulted for background, not used as the source of the original synthetic model.)

**Sharp uniform sample result for the entire INFINITE family of N≥41** follows by combining:

- the newly certified `Delta_N≥Delta41` for every integer N≥41;
- this monotonicity of exact optimal NP risk **in Delta**;
- Geeky-S13 ROT010 **AUTHOR_IV75** four risk thresholds at ORIGINAL N41:
  e_14538(Delta41)>0.05, e_14539(Delta41)<0.05;
  e_29082(Delta41)>0.01, e_29083(Delta41)<0.01;
- M16 ROT001 independent I1 of strict NP risk monotonicity **in n**.

Consequently: **for every integer N≥41** the same optimal invariant decision procedure using the correct known N-specific source Delta_N guarantees >95% accuracy at n=**14539**, and >99% at n=**29083**, under EACH of A and B. These are furthermore **SHARP UNIFORM thresholds** over the class N≥41: a strictly smaller n cannot guarantee the respective target for ALL N≥41 because **N=41 itself** is included and failed at n14538/29082. They are NOT individually minimum n for every N>41, nor the minima across other instruments/full site laws or true physical NASH data. This ROT011 **does not reexecute** ROT010 IV75; it explicitly composes the pinned prior author certificate with its newly proved N portability and source bound. The independent external IV I1 of ROT010 remains pending.

A deliberately conservative and explicit bound holds over ALL N≥17. With `p_N=F_W(−Delta_N/2)`, monotonicity Delta_N≥Delta17 gives `p_N≤p17≈0.499350838366222063...`. Our new outward IV75 checks `1/2−p17>0.00064916`. A one-bit-majority Hoeffding inequality yields per-hypothesis risk `<exp(−2n(0.00064916)^2)`, hence **n=3600001** suffices for >95% and **n=5500001** for >99% across every N≥17. These are upper sufficiency bounds, not minimax n and not physical observations.

**NEW UNIFORM LOWER INFORMATION LIMIT (source-conditional):** from the logcurvature bound `(log f)''≥−1/4` (as derived in source ROT010), `KL[f(x)||f(x+Delta)]≤Delta²/8`, since the score mean is zero. Thus for n IID invariant samples `KL_n≤n Delta_infinity²/8`. Pinsker's inequality then says the optimal equal-prior risk cannot be below 5% if n≤1736, nor below 1% if n≤2059, **for any N in this chosen four-mode geometry family**, no matter how finely the synthetic lattice is refined. This is a coarse necessary lower bound, not close to sharp and NOT a limit on other possible sensors. It documents finite saturation of information per observation.

## 6. Actual two-route reproducibility and strict falsifiers

**PRIMARY (actually executed):** independent transcription of original C1,C2,h source support into exact integer Minkowski sets; gets **41/221** cardinalities; exact modulo-N no-signal/support tests for all **N=17..256**; original rational source FFT axial spectra and strict SPD bound; >25 specified integer N precision-110 point plus IV75 intervals; every finite `N=42..81` uniform dominance check and `N=18..81` N17 dominance; all pre-first-drop `N=17..66` strictly increasing and `N=67→68` strict decrease; exact rational derivative 13/250, exact limit ratio 145/133; Hoeffding source-IV75 gates. Outputs a deterministic full JSON certificate. All `N≥82` and every-N claims rely on the **algebraic proof**, not a claim of infinite computational sweep.

**SECOND INDEPENDENT SAME-CELL REFEREE (actually executed):** separate Python NumPy FFT on the full N³ spatial impulse covariance kernel, formed directly from all **6 signed axial + 12 signed face + 8 signed body** unit translations and exact original ROT038 rational weights, at **12** independent N=17,18,31,40,41,42,67,68,81,82,101,102. Independently recomputed FFT eigenvalues at four modes, guaranteed positive SPD on all represented frequencies, source 41/221 combinatorial potential supports and direct mod-N source zero-mean exclusions. Also independently detected N16 jL=jH design collapse, recomputed the N→∞ rational B spectrum ratio, and independently rederived the source 4-mode Delta to absolute float error below 4×10^-14. No imports from the primary source program; **SAME-CELL** numeric referee, not different-cell I1. Actual original M13 `calc` source **not executed** here.

**Concrete falsification contracts:**

1. For N16, chosen four-mode design degenerates: cannot claim universal N≥16 from this source.
2. For even N, taking the actual Nyquist j=N/2 gives a real (self-conjugate) Fourier mode whose squared Gaussian energy is NOT Exp(1); inherited logistic-sum NP thresholds would then be invalid. Our jH strictly avoids Nyquist.
3. Assuming Delta_N strictly increases with N for ALL N is demonstrably false already at 67→68; the true guarantee is a uniform lower envelope, not stepwise monotonicity.
4. The source N41 original B potential Fourier support and 221 energy differences survive integer N extrapolation **as a support-only theorem**; do not call it a native execution of every original N-specific projected tensor coefficient.
5. If calibration is not multiplicatively separable in direction×radius, cross-ratio is no longer a maximal invariant; M16 ROT002 quantifies the more general bounded cross-interaction class. Physical separability is unverified.
6. Arbitrary nonGaussian latent site noise, strong Fourier-mode correlations, real instrumentation phase/leakage, or a sensor restricted to the original coarse M13 masks invalidate the exact Exp(1) and finite-n claims.
7. A uniform finite n in hypothetical *full-site snapshots* does NOT imply constant measurement-resource cost: at N41, n14539 full N³ site readings correspond to **1,002,042,419** individual hypothetical site values; n29083 corresponds to **2,004,429,443**, if full snapshots rather than direct Fourier channels are required. No physical apparatus or sampling rate supports these counts.

## 7. Bounded independent review request and acceptance ceiling

REC13 / AUD3 / M16 requested independent nonblind source-specific I1 for: (a) exact original M13 modes vs modulo wrap and N17/even-N rule; (b) exact source two spectra, 13/250 derivative and 145/133 limit; (c) first parity reversal IV75 N67→68 and the analytic N≥82 lower envelope; (d) direct layer-cake overlap monotonicity of NP risk in Delta, distinguishing it from M16 ROT001 monotonicity in n; (e) strict provenance of transferred N41 ROT010 IV75 author sample certificates; (f) finite-n physical/sensor/latent caveats; (g) all-N>=17 conservative Hoeffding gate and source lower saturation bound. These should NOT be mistaken for I3, real sensors, BW native register entries, or CANON/EXEC_SIGN.

**Final status:** `SOURCE_INTEGER_SUPPORT_41_221_PASS / ALL_NGE17_FOUR_MODE_MATH / N17_TO_256_MODULAR_ZERO_SIGNAL_ENUM_PASS / EVEN_N_NYQUIST_SAFE / PARITY_N67_TO_68_NONMONOTONE_IV75_PASS / N42_TO_81_UNIFORM_DELTA_IV75_PASS / NGE82_ANALYTIC_PASS / NP_OVERLAP_DELTA_MONOTONE_ANALYTIC_PASS / SHARP_UNIFORM_NGE41_NP_14539_29083_COMPOSED_FROM_ROT010_IV75_M16_I1 / FOURIER_SPATIAL_12N_SAME_CELL_PASS / ORIGINAL_M13_NATIVE_NOT_EXECUTED_ROT011 / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
