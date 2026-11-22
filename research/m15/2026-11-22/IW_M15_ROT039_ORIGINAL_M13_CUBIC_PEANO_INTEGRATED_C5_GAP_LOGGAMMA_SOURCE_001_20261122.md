---
artifact_id: IW_M15_ROT039_ORIGINAL_M13_CUBIC_PEANO_INTEGRATED_C5_GAP_LOGGAMMA_SOURCE_001_20261122
return_id: IW_M15_ROT039_ORIGINAL_M13_EXACT_CUBIC_PEANO_LIPSCHITZ_SATURATION_INTEGRAL_FINITESAMPLE_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-22
exposure: PUBLIC
result_class: NEW_ORIGINAL_M13_UNMODIFIED_NATIVE_IV110_ANALYTIC_CUBIC_PEANO_SATURATION_WITH_INDEPENDENT_41CUBED_SOURCE_FFT_SVD_QUADRATURE
sync: GITHUB_PENDING_BW_INGEST
ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_SITE_SENSOR / NO_FULL_HISTORIC_DTC0A_PRODUCER / NO_TASK_CASCADE
---

# M15 ROT039 — Exact original-M13 cubic Peano integration boosts the C5 calibration-safe Gaussian margin 31x

## Source-first result and priority

**NEW original-M13 source-specific mathematical certificate PASS.** Previous M15 ROT037 provided a strict C5 calibration-safe weighted Gaussian log-variance separation g_old>0.00002137477833689214 for two EXACT first-owner Geeky-S12 ROT035 source-legal Gaussian site covariance hypotheses A/B. Previous ROT038 established the direct weighted log-gamma Chernoff bound but inherited that conservative separation, requiring mathematically sufficient 80, 135, 175 and 270 BILLION hypothetical IID full-site observations for >75%, >90%, >95%, >99% two-known-hypothesis success.

**M15 ROT039 NEW:** exactly integrate the entire source Peano CUBIC over a rational interval around its unique sign-switch root rather than replacing the derivative by its minimum. SAME six original M13 energy-mean-free modes, SAME Gaussian covariance A/B shapes, SAME independently freely fitted cubic axial and FACE slope nuisances, SAME per-hypothesis C5 residual conditions |phi''''|<=16.5 and |phi'''''|<=50. Strict original-native-source mpmath.iv110 computes:

F > 0.00081493060926490795422370081571123432290639373513099932

g_new = Delta - 2*L*R + F > 0.00066924288760180009800437334620244830716001165452397092.

The **ratio of the two rigorously certified lower-bound expressions** g_new/g_old>31.30993346708580. Combined with ROT038 first-established mature log-gamma control, sufficient source-model IID full-site snapshots drop to **80 million, 135 million, 175 million, and 270 million** at the same success thresholds, respectively. Approximately **1000x decrease in mathematical sufficient counts** from ROT038, not an empirical precision improvement or a practical sample proposal. This is not claimed as an attained minimax gap, globally optimal statistical procedure, or novel general theorem of mathematics.

Firstness preserved: original M13 source; Geeky-S12 ROT035 FIRST two exact source-legal rational synthetic Gaussian stationary RAW-site noise laws; Geeky-S13 ROT001 FIRST separate unbounded C-infinity axial-only full-field alias; M15 ROT036 FIRST original six-mode FACE+C4 Peano sharp boundary, ROT037 FIRST C5 bounded restoration above C4 alias, ROT038 FIRST direct log-gamma concentration. No ownership reassignment.

## Original M13 actual native source and strict model

Unmodified original M13 public source 8,970 bytes verified *before actual import* by full SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c and original Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679. TWO distinct NEW scientific programs ACTUALLY execute original source tensor_polys(41)[B], calc(41,alpha=1/20)[B], and inner(B,B,41,k0); 41 original sparse tensor B Fourier modes and 221 original B-energy mode differences. Original:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Original fixed M13 source lacks the full historical dtc0a_runtime_v0_3_1.py code and does not document physical RAW spatial measurements or new Fourier sensing channels.

Six hypothetical added raw site energy Fourier wavevectors on source N41³=68921-site periodic grid:
 (20,20,20), (20,20,0), (20,0,0), (7,0,0), (12,12,13), (3,13,7).
All k and -k are OUTSIDE original 221 B-energy Fourier difference support. Therefore every one of their 12 normalized real cosine/sine deterministic source means is EXACT ZERO for every original alpha, not just floating-point approximately zero.

The two original owner-created EXACT source-legal Gaussian spatial site-noise hypotheses are centered stationary RAW source energy noise with eigenvariance
 v_X(k)=beta0_X*[1+theta_ax_X*a(k)+theta_face_X*f(k)+theta_body_X*b(k)],
 a=(cx+cy+cz)/3; f=(cxcy+cxcz+cycz)/3; b=cxcycz; c_i=cos(2pi*k_i/41).
A: beta0=1, theta axial=3/25, face=1/10, body=2/25.
B: beta0=99779719687217/10^14, theta axial=316869474178226/2494492992180425, face=93110637627687/997797196872170, body=205860943554709/2494492992180425.

These mathematical source site covariance laws are strictly SPD but **NOT empirically calibrated**. Each candidate X permits separately fitted UNRESTRICTED cubic p_X(a), UNRESTRICTED face slope tau_X*f, plus arbitrary residual phi_X(a)∈C5(J) with BOTH |phi_X''''|<=L=33/2 and |phi_X'''''|<=M=50 on the source axial node interval J. Completely unrestricted lower derivatives and different candidate-specific calibration parameters remain allowed. Full source covariance after positive spectral multiplication remains SPD but generally NONLOCAL. NO measured calibration derivative bound or real source sensor.

Prior original science full bytes SHA-LOCKED and INCLUDED in user-local reproducer, not silently claimed newly re-derived:
 ROT029 exact rational original site covariance certificate SHA256 00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90;
 ROT036 original six-mode IV Peano SHA256 d5744a9e6b74174c0aa1c240160414b6fccb796e3711079b586e3d0d40c33ec6;
 ROT037 source C5 SHA256 a059696b29e21dd230170b3d6065551e5e2a88eca330b9b711f898fc09efdef2;
 ROT038 source log-gamma SHA256 b5f92d2c3e614f36ba6cd7bd25e99b3b44bbe5e9e0cdee3cdae4b95ad5fc547b.

## New Peano cubic integration: precise theorem and proof

Let w be the unique six-component original-source nuisance-null log-variance contrast with last w_5=1, obtained by NEW actual IV110 LU from original native M13 Fourier geometry. Exactly:
 sum_i w_i*(1,a_i,a_i²,a_i³,f_i)=0.
Let Delta=sum_i w_i log(v_B(k_i)/v_A(k_i))>0.

Sorted original source axial node ordering is indices [0,1,4,5,2,3]. Let K(t)=sum_{a_i>t}w_i(a_i-t)^3/6, the signed Peano kernel, and R=integral_J |K(t)|dt. Previous locked source IV110 gives R≈0.000111970857506390929 and a **UNIQUE simple sign-switch root**
 t_star∈[0.03081114391431705277793181424633070026588259539317446,
          0.03081114391431705277993181424633070026588259539317785].
The old source root isolation and global one-sign-change theorem are explicitly inherited from the verified ROT036–037 parents; this rotation rechecks the original native-source computed weights, Delta, and root consistency.

**New strict geometry:** choose h=7/25=0.28. Both t_star−h and t_star+h lie strictly between the SAME two original axial nodes a_sorted,2≈−0.31301054718822 and a_sorted,3≈0.32160557943399. Therefore K is ONE exact polynomial CUBIC throughout the WHOLE paired integration window, with source coefficients:
 K(t_star+u)=p1*u+p2*u²+p3*u³;
 -K(t_star−u)=p1*u−p2*u²+p3*u³
 for every 0<=u<=h.
The constant is exactly zero by definition of t_star as a kernel root (not numerically rounded to zero). Actual NEW 110-digit outward source intervals STRICTLY certify p1=K'(t_star)>0, p2=K''(t_star)/2<0 and p3=K'''/6<0.

Hence the PRECISE source curvature identity
 |K(t_star−u)| − K(t_star+u) = −2*p2*u² >=0
 is exact for every u in the window. Source parent global sign isolation proves K right nonnegative and K left nonpositive. This comparison permits using the actual right cubic to lower bound BOTH left and right contributions to loss of the best unbounded-C4 sign-switch optimizer.

Let g=phi_B''''−phi_A''''. Under admitted C5 model |g|<=2L, |g'|<=2M. The two lost saturation deviations d_left(u)=2L+g(t_star−u)>=0 and d_right(u)=2L−g(t_star+u)>=0 obey
 d_left+d_right>=4L−4M*u.
This RHS is positive on entire window because h=0.28<L/M=0.33.

The exact signed loss relative to ideal unrestricted fourth-derivative saturation therefore obeys
 2L*R − integral_J K*g
 >= integral_0^h (4L−4M*u)*K(t_star+u)du
 = F.

No sampled interpolation, floating fit or discrete approximation enters this inequality. Integrating the actual cubic polynomial gives

 F = 4L*(p1*h²/2+p2*h³/3+p3*h⁴/4)
   − 4M*(p1*h³/3+p2*h⁴/4+p3*h⁵/5).

NEW truly outward source IV110:
 F∈[0.0008149306092649079542237008157112343229063937351309993241,
     0.0008149306092649079605745748260657750887955286130861781998].
Then for ALL admissible separate A/B calibrations,
 Delta_eff=Delta+integral_J K*g>=Delta−2L*R+F,
 and the NEW strict IV110 source lower-bound expression is
 g_new∈[0.0006692428876018000980043733462024483071600116545239709283,
           0.0006692428876018001055540947367335240114969166170132282963].

This narrow interval encloses **the calculated universal lower-bound expression**, not actual possible Delta_eff values (which can be larger). It is not an exact attainable infimum; **no sharp new C5 threshold** is claimed. The source-bound ratio to the prior ROT037 conservative lower bound exceeds 31.3099334670858.

**Essential fixed-decision-threshold guard:** The C5 nuisance set is centrally symmetric. Applying the same loss argument with g=+2phi'''' and g=−2phi'''' yields each candidate's individual nuisance score displacement bounded by LR−F/2. Thus a common classifier threshold Delta/2 separates both entire nuisance-law sets. Pairwise positive separation alone would not have justified that classifier.

## Combined rigorous old log-gamma result: source sample counts

No change to full-site observation model, six modes, two fixed A/B noise shapes, or bounded C5 nuisance class. For n iid hypothetical complete RAW spatial site recordings, six independent normalized cosine/sine pair energy sums give Xi~Gamma(n,1), independent. Weighted log statistic Z=sum_i w_i log(Xi/n), sum w_i=0 EXACT. The centered log-MGF originally derived by M15 ROT038 is F_Z(t)=sum_i [log Gamma(n+twi)−log Gamma(n)] and F_Z''(t)=sum_i wi² trigamma(n+twi). Classical bound trigamma(x)<=1/(x−1/2) and the source original weight square sum V≈2.8147662920276676 give the previously certified Chernoff inequality, now with MUCH larger g_new:

 P(error | each X) <= exp[−n*g_new²/(9V)], n>=80,000,000.

The original-source IV110 source also certifies the MGF domain requirement eta<0.1 at n80million.

Strict certified finite-sample mathematical SUFFICIENT counts:
- >75% each candidate at n=80,000,000: error <0.243072;
- >90% at n=135,000,000: error <0.091924;
- >95% at n=175,000,000: error <0.045321;
- >99% at n=270,000,000: error <0.008450.

All are pure source-model mathematical sufficient statements for TWO known fixed hypotheses with arbitrary separately fitted nuisance functions satisfying the stated bounds. Not necessary n, not a verified physical experiment, and not a general unknown-covariance estimator.

## Independent original 41³ spatial FFT, source site rolls, Peano quadrature and loggamma controls

A NEW SEPARATELY authored program actually imports and runs unchanged original M13, builds nine original complex B tensor component fields over EVERY source 41³ site via inverse 3D FFT, and directly computes all six cosine/sine source energy projections. Native source full B energy and direct full-site spatial energy agree to relative <3e−13; original high-frequency deterministic energy means numerically vanish as predicted by the EXACT Fourier-support argument. It computes each A/B normalized cosine/sine variance through ALL 6 AXIAL, 12 FACE and 8 BODY ORIGINAL signed spatial site array rolls — not by importing the main IV source spectral rows.

Independently, a new numerical 5x6 SVD yields the nuisance-null source weights. Separate root finding via scipy.optimize.brentq and integration of the original site/SVD-derived whole piecewise Peano kernel via scipy.integrate.quad, NOT via copying the primary IV110 cubic formula, gives:
 F≈0.0008149306092649172,
 g_new≈0.0006692428876037001,
 old g≈0.000021374778336892146,
 ratio≈31.3099334671747.

Independent MP70 **both signed** exact-loggamma saddlepoint diagnostics at n80million give numeric tails ≈0.2036809143 and 0.2036805639, strictly below the IV110 conservative <0.243072. Comparable checks PASS for all four target sample counts. These FLOAT/MP route results are subordinate diagnostics and DO NOT replace primary IV110 source proof. One preliminary separate numerical route failed from a reused Python variable name, corrected before final clean source replay; not counted successful.

## Reproduction and 10 real negative controls

Actual 2/2 new scientific programs were COLD independently executed with python -I in a NEW isolated directory and regenerated their complete JSON outputs BYTE IDENTICAL. Ten REAL disposable named negative fixtures were run, each exited nonzero with expected source/science guard:
1–2 native original M13 tamper checked against BOTH programs;
3–5 three independent frozen original proof/data JSONs ROT037, ROT038, ROT029 tampered;
6 current main IV110 result tampered before spatial checker;
7 FALSE enlarged cubic shared-segment halfwidth h=2/5;
8 FALSE curvature sign (p2>0);
9 FALSE strict guaranteed g_new>0.0008;
10 FALSE >99% at only n=10,000,000.
**10/10 FAIL CLOSED** and original sources unchanged.

Final user-accessible original-source executable ZIP includes 15 files: original native M13, FOUR SHA-locked prior full machine certificates, TWO new actual standalone executed science Python scripts, TWO complete new result JSONs, actual isolated replay+10-negative script and receipt, detailed full ~source report, README, deterministic builder and SHA manifest. ZIP CRC PASS; payload SHA256 14/14 PASS; 15/15 archived member exact full byte readback PASS. Exact final ZIP was ALSO extracted to another clean directory and BOTH scientific scripts ACTUALLY independently reexecuted from the ZIP with their COMPLETE JSON byte-identical: 2/2 PASS.

User-local ZIP 59,167 bytes, SHA256 b44eed8ace1b52c46146f3bfe8c064e98d8ef3d209f7b06c87b0521cffdb7596.
Original primary executable SHA256 d08bc7e34c1d8b3dcc1ee6f4d2618742f3ee9c209a5a4b5d3b236fc336b8f2e2.
Complete IV110 JSON SHA256 8091c09bf3d2b1a032bfe7d94a965cf13d2b8a5beb5a43e0eeb9c7a9a041326e.
Independent original M13 full spatial/SVD/quad source Python SHA256 06a72bbae98bc2bfcc81e1709593459c2ce8942d8c73ce7e1ac94687a14e6a5b.
Complete independent spatial JSON SHA256 9e7aabd35f193e257fe9e06cf6cb63fce036c4fbc57d774561ef71418fd5e6ba.
Ten negative test receipt JSON SHA256 4255941ab163c4fb94f1879223d804083f34a034a57117621ba171218a5baf1d.

## HARD SCIENCE STOP and requested audit

Original public M13 AUXILIARY mathematical source, not missing complete historical DTC0a producer; Gaussian RAW spatial noise and FACE/C5 calibration derivative magnitudes hypothetical, no actual 68921-site RAW measurement, six extra Fourier sensors or 80–270 million IID source samples. No source physical NASH K/J3/TPE/GR/GW claims, no general mathematics novelty, no new alpha-global inverse or globally optimal experiment. M13, Geeky-S12, Geeky-S13 original firstness and prior M15 derivations preserved. This is M15 INTERNAL nonblind source-IV proof with separately written computational crosscheck, NOT REC13/AUD3 different-cell acceptance nor external blind I3. KN15 BW native ingestion receipt NOT verified. GitHub publishing and Slack dispatch are transports, not owner ACK, CANON or EXEC_SIGN. NO_TASK_CASCADE.

FINAL: M15_ROT039_ACTUAL_ORIGINAL_M13_NATIVE_IV110_PASS / EXACT_SHARED_CUBIC_PEANO_WINDOW_AND_NEGATIVE_SECOND_DERIVATIVE_PASS / ANALYTIC_PAIRED_LOSS_F_IV110_PASS / STRICT_NEW_LOGGAP_GT_0P0006692428876_PASS / 80_TO_270M_IID_SAMPLE_SUFFICIENCY_PASS / INDEPENDENT_ORIGINAL_41CUBED_SITE_FFT_SOURCE_SVD_QUADRATURE_PASS / TWO_FULL_JSON_BYTE_IDENTICAL_COLD_REPLAYS_PASS / TEN_REAL_NAMED_SOURCE_NEGATIVE_FIXTURES_REJECTED / FINAL_ZIP_EXTRACT_2OF2_BYTE_IDENTICAL_PASS / ZIP_CRC_SHA14_OF14_PASS / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
