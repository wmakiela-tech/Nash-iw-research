---
artifact_id: IW_GEEKY_S12_ROT018_ACTIVE_SET_REENTRY_FALSIFIER_AND_UNIFORM_M13_QUADRATIC_CLOSURE_TUBE_001_20261113
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
status: AUTHOR_EXACT_FRACTION_GENERIC_ACTIVE_SET_REENTRY_FALSIFIER_PASS / AUTHOR_FULL_25D_SOURCE_M13_UNIFORM_TWO_ACTIVE_QUADRATIC_CLOSURE_PASS / ROT018_INDEPENDENT_REFEREE_PENDING
source_custody: ORIGINAL_M13_PUBLIC_N41_B_25_DIRECTED_QUARTIC_GIT_BLOB_A6F50F / M15_ROT008_INDEPENDENT_I1_ON_ROT016_NOT_ROT018
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_GENERAL_NOVELTY / NO_HISTORIC_DTC0A_RUNTIME_IDENTITY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT018 — aktywne powłoki mogą wracać; ścisłe, kwadratowe zanikanie straty M13 na całym przedziale kalibracji

## 0. Nowe recenzje, firstness i potrzeba zmiany pytania

M15 ROT008, wysłany 13 listopada 2026 o 17:40 CET, jest NOWYM niezależnym międzykomórkowym I1 NONBLIND audytem źródłowym Geeky ROT016: nowo napisany BigInt exact rational directed-interval program, nieimportujący Geeky Python, potwierdził w oryginalnej 25-wymiarowej rodzinie source M13 B przy alpha=.05 beta=.075 kappa=.066, że jedynie shell1 LOW oraz shell5 HIGH są aktywne, pozostałe trzy są STRICT INACTIVE, a ich ściśle dodatnie GLOBALNE minimalne kosztowe przedziały są prawidłowe. Pierwszeństwo wyniku ROT016 pozostaje Geeky; niezależnej kontroli M15. Jest to I1 source model review, NIE historyczny DTC0a i NIE formalne CANON.

Dokument pierwotny niezależnego M15 ROT008:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e0328f637a98d0184f9df2d5146f5d490758afb0/research/m15/2026-11-13/IW_M15_ROT008_INDEPENDENT_M13_B25_TWO_ACTIVE_CONVEX_KKT_NONZERO_RISK_REFEREE_001_20261113.md

M15 ROT007 niezależnie sprawdził ROT015 projektowy stosunek logarytmiczny 9+5 i ostry próg dokładnego dopasowania. AUD2 ROT005 i M15 ROT006 FIRST independently full ROT007/013 17+5 algebra, REC11 ROT029 FIRST independent delta=.02514 negative at eps1e-7. Nie odkrywamy na nowo tych wyników, nie przypisujemy sobie audytów innych komórek. ROT017 4 aktywne reżimy 5,4,3,2 to wciąż author PASS / independent referee PENDING.

Nowe pytanie ROT018: czy prawo obserwowane w czterech źródłowych przykładach ROT017, malejącej liczby aktywnych powłok po zwiększeniu kappa, można podnieść do uniwersalnej reguły; a jeśli nie, czy dla rzeczywistego M13 można przedłużyć wynik ROT016 z JEDNEGO kappa=.066 na cały ciągły przedział do progu zerowej straty, bez skanowania punktów przejścia?

## 1. Model i elementarna ogólna geometria

JEDEN wspólny dodatni gain c>0 plus pięć względnych gains eta_i w [-kappa,kappa], kappa∈[0,1). For positive r_i=s_i(alpha)/s_i(beta), A_i=w_i*s_i(beta)^2, the exact profiled squared residual is

Phi(c;kappa)=SUM_i A_i [max(r_i-(1+kappa)c,(1-kappa)c-r_i,0)]^2.

This is convex, continuous C1 in c. For kappa below the zero-fit threshold kappa_crit=(max r-min r)/(max r+min r) the global minimizer cstar>0 is unique and at least one residual is nonzero. The envelope derivative with respect to kappa is

d Dmin²/dkappa = -2*cstar*SUM_{active i} A_i*abs(the original active residual_i) <0,

so the GLOBAL OPTIMUM LOSS is strictly decreasing in kappa until exact-fit at kappa_crit. The active-set SUPPORT, however, does NOT have to shrink or be nested: this is the substantive generic negative knowledge.

## 2. Exact synthetic three-shell counterexample: HIGH -> INACTIVE -> LOW

Pure independent positive rational fixture (NOT M13 and NOT a physical source):

  ratios r=(1,2,100), weights A=(100,10,1).

The new actually executed Python stdlib fractions.Fraction global finite active-set solver returns:

- kappa=0: shell1 LOW, shells2 and3 HIGH, none inactive; optimal loss 9703.963963963964 (human Float64 display only);
- kappa=1/101 approximately .9901%: shell1 LOW, shell3 HIGH, shell2 strictly INACTIVE; optimal loss 9696.161535385845;
- kappa=1/41 approximately 2.4390%: shells1 and2 LOW, shell3 HIGH, none inactive; optimal loss 9684.33968632569.

All point coordinates, optimum c, lower/upper cuts and strict active status are EXACT Fraction numbers in bundled rot018_exact_results.json. For each active set stationary c is solved by strict rational KKT, and global convexity certifies optimality, no numerical optimization needed. An independently authored SciPy scalar minimizer checked all three results and signs (diagnostic only).

Thus the claim "a once inactive shell cannot reactivate upon increasing calibration allowance" is STRICTLY FALSE even in simple, 3-shell, positive weighted scalar nuisance model. Active support sizes 3 -> 2 -> 3 while optimal loss strictly DECREASES. The user should NOT use monotone active-set elimination as a universal shortcut to ROT017. Classical parametric quadratic programming has long addressed active-set changes and multiple branching: U. Werner, Multiple branching in parametric quadratic programming, Optim Methods Softw 4 (1994), DOI 10.1080/10556789508805596; H.J. Ferreau et al, qpOASES: a parametric active-set algorithm for quadratic programming (2014). These are mature host references, not source of this particular exact three-ratio fixture, and we claim NO general mathematical priority.

## 3. Universal local lemma: two extremes only near zero-fit threshold

For ANY m positive r_i with unique MIN m=r_l and unique MAX R=r_h, strictly interior other ratios and positive A_i, put
  kcrit=(R-m)/(R+m),
  u=1-kappa, v=1+kappa.

For all kappa sufficiently close to kcrit FROM BELOW, the unique optimum has ONLY min-ratio shell l LOW active and max-ratio shell h HIGH active, with every intermediate shell exactly fitting. This follows from continuity of the explicit two-active stationary candidate, whose relative gain projection interval becomes [m,R] as kappa tends to kcrit, while every other ratio lies strictly inside (m,R).

On that entire sufficiently small left neighborhood, not merely asymptotic samples, the EXACT risk is
  Dmin²(kappa)= A_l A_h [u R-v m]^2 / [A_l u² + A_h v²]
               = A_l A_h (R+m)²(kcrit-kappa)² / [A_l(1-kappa)² + A_h(1+kappa)²].

Hence quadratic approach:
  Dmin²(kappa) = C (kcrit-kappa)² [1+O(kcrit-kappa)],
  C=A_l A_h(R+m)^4/[4(A_l m²+A_h R²)] >0.

The source-independent derivation is standard convex projection/implicit active KKT, NOT claimed novel math. It does not assert global monotone support when kappa is far below kcrit, as the synthetic counterexample proves.

## 4. NEW source-specific stronger result: ALL kappa from 6.6% to kcrit, ALL 25D M13 coefficient box

M13 FIRST source 25 directed quartics for N41 five nested B masks: 7501 original bytes, immutable Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Each of the 25 original directed coefficient intervals is separately enlarged by epsilon=1/10^7 as an EXACT rational source uncertainty box [lo-epsilon*abs(lo),hi+epsilon*abs(hi)]. Independent source coefficients need not be realizable from original Fourier fields. Five disjoint shell weights W=(7778,6938,6146,5402,24389); fixed alpha=1/20=.05, beta=3/40=.075; r1<r2<r3<r4<r5 is uniformly STRICT throughout the coefficient box.

NEW independent author Python3 stdlib Fraction code (does NOT import ROT016 or ROT017 codes) proves SIXTEEN strict full-box directed inequalities:
  four adjacent ratio ordering gates;
  r5<2*r1;
  t_upper*r1<2*r5 with t_upper=(1+.067)/(1-.067);
  kappa0=.066<kcrit=(r5-r1)/(r5+r1)<.067;
  r1<z0, t0*z0<r5 at kappa0;
  z0<r2,r3,r4<t0*z0 for all three middle ratios at kappa0.

Here t=(1+kappa)/(1-kappa) and z=(1-kappa)c. For the two-extreme stationary candidate,

  z(t)=(A1*r1+t*A5*r5)/(A1+t²*A5).

The DERIVATIVE SIGNS hold across the WHOLE continuous t interval [t0,tcrit=r5/r1]:
  z'(t) has sign A5[A1(r5-2t*r1)-t²*A5*r5] <0
     because r5<2*r1 and t>=1;
  (t z(t))' has sign A1[A1*r1+t*A5(2*r5-t*r1)]>0
     because the exact condition is t*r1<2*r5, verified uniformly with t_upper.

Thus the clipping interval (z(t),t*z(t)) EXPANDS continuously as kappa grows above .066 up to kcrit. Since all three middle ratios already lie strictly inside at .066, they remain STRICTLY INACTIVE throughout. The extrema remain strictly active for every kappa<kcrit by explicit positive identities
 z-m= t*A5*(R-t m)/(A1+t² A5)>0,
 R-t*z= A1*(R-t m)/(A1+t² A5)>0.
For every source coefficient choice and every REAL kappa in [.066, kcrit), the two-active stationary formula remains GLOBAL by convexity. This is a continuous-parameter, uniform-source-box theorem, not a kappa pointwise grid or threshold root search.

The resulting EXACT risk throughout this whole tube is the above two-extreme formula with l=1,h=5. The full 25D source-box critical threshold has conservative exterior decimal enclosure:
  .06626784 < kcrit < .06627136.
The quadratic coefficient, after multiplying by 10^24, has STRICT conservative exterior rational bounds:
  59.9771354 < 10^24*C < 59.9785346.
Source midpoint 10^24*C approximately 59.97783497216416.

At kappa=.066 existing ROT016 source-box risk interval has the previous sharper exact Fraction endpoints: 4.304990867358497e-6 to 4.417277646937626e-6 in 10^24 D² display, retained as FIRST and already independently reviewed by M15 ROT008. ROT018 does not weaken or change it. A SINGLE source midpoint rational fixture at kappa=kcrit-1/100000 gives exact five-shell Fraction active-set loss identical to the two-shell expression; normalized loss /[C*(kcrit-kappa)^2] approximately 1.000013658, independent SciPy diagnostic corroborates.

Notice logical scope: source-uniform theorem on the interval starts at .066, NOT all kappa from 0. Generic active sets CAN re-enter. We proved continuous two-extreme stability in this bounded final segment using strict ratio inequalities and monotone clipping interval, and NO claim about arbitrary parameter pairs alpha,beta or arbitrary calibration technologies.

## 5. Actual execution, controls and bundle

User conversation ZIP:
  Geeky_S12_ROT018_reentry_and_uniform_quadratic_closure.zip,
  26273 bytes, SHA256 b4b69a1a3544d33298af34c4e431f53c7bd6194b3f1b4c09f23decbedb1a0831,
  eight members, ZIP CRC PASS and 8/8 exact SHA256 plus byte readback PASS.

Contents:
- actually executed independent stdlib Python Fraction prover, SHA256 4b12ae2d637b6ec03aa6aa9cf58a1512d69f20631f8d120adbff7fe971725c43;
- original immutable M13 source direct_B, SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f;
- FULL 33101B exact results JSON with 16 strict source-box margins, actual Fraction numerator/denominator for each boundary, source critical interval and quadratic coefficient, SHA256 0d0ea689a4222c559127df585b6fb7e2f5c079804fd726e7d75143952bb369e1;
- independent SciPy numerical scalar minimizer and actual 5-fixture results JSON (3 synthetic +2 M13), not part of proof;
- clean isolated Python rerun producing BYTE-IDENTICAL full result; one-byte deliberate change in a TEMP copied source rejected with SOURCE_GIT_BLOB_MISMATCH and exit 1 BEFORE math;
- README and SHA256 member manifest.

No original author M13 files modified. The actual full 12KB executed Python and exact 33KB result JSON reside in the user ZIP; only condensed science report and machine summary are mirrored to public GitHub, NOT original executed Python as a public source code file. Do NOT overclaim public code byte identity.

## 6. Custody, prior art and final gate

M13 first source, Geeky ROT016 first fixed-kappa two-active risk, M15 ROT008 first independent reviewer of that original prior theorem. ROT018 new model-specific **uniform continuous kappa interval** plus exact synthetic NO-MONOTONE-SUPPORT falsifier, all author same-cell. REC11/AUD2/M15 has NOT yet independently reviewed ROT018 whole continuous tube or generic reentry numbers. Source original 25D coefficient box is a mathematical overapproximation, not source field-realizable or physically measured noise. Historic dtc0a_runtime_v0_3_1.py remains missing byte-exact. Nothing extends to physical NASH K/J3/TPE, optical sensors, Wu-Xu cosmology, or mathematical novelty. BW ingestion unverified, M15 canon/owner decision unverified. No automatic task cascade and no micro-threshold scanning.

FINAL:
M15_ROT008_INDEPENDENT_I1_REFEREE_ROT016_PASS /
GENERIC_ACTIVE_SET_REENTRY_NEGATIVE_EXACT_FRACTION_PASS /
M13_25D_EPS1E7_SOURCE_16_STRICT_GATES_UNIFORM_KAPPA_0P066_TO_KCRIT_PASS /
EXACT_QUADRATIC_CLOSURE_COEFFICIENT_SOURCE_BOX_PASS /
INDEPENDENT_SCIPY_NUMERIC_CHECK_PASS /
CLEAN_BYTE_REPLAY_AND_SOURCE_TAMPER_PASS /
ROT018_REFEREE_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
