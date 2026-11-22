---
artifact_id: IW_GEEKY_S13_ROT016_M13_EXACT_X_REFLECTION_FOUR_SENSOR_ALL_ALPHA_CAUCHY_AND_SIX_SITE_SHAPE_SPAN_IV80_001_20261122
return_id: IW_GEEKY_S13_ROT016_M13_ALL_ALPHA_X_MIRROR_FOUR_SITE_AFFINE_TEMPLATE_FREE_CAUCHY_TWO_DESIGN_IV80_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
source_scope: ORIGINAL_M13_PUBLIC_41_MODE_B_TENSOR_AUXILIARY_PLUS_GEEKY_S12_ROT038_SYNTHETIC_ANISOTROPIC_GAUSSIAN_SITE_NOISE
class: ORIGINAL_SOURCE_SYMMETRY_TYPED / FOUR_MIRRORED_RAW_SENSOR_ALL_ALPHA_ADAPTIVE_NUISANCE_INVARIANT / EXACT_CAUCHY_AND_IV80_RISK / SIX_SENSOR_PARAMETRIC_SHAPE_SUBSPACE_IV65 / SOURCE_MISSPECIFICATION_FALSIFIER
status: AUTHOR_ANALYTIC_AND_IV80_PASS / SAME_CELL_INDEPENDENT_FFT_PASS / DIFFERENT_CELL_ROT016_I1_PENDING
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_NATIVE_ORIGINAL_M13_EXECUTION_ROT016 / NO_HISTORICAL_FULL_DTC0A / NO_PHYSICAL_FOUR_CHANNEL_SENSOR / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT016 — dokładna symetria odbicia oryginalnego B usuwa cały nieznany profil α z czterech lokalnych pomiarów

## 0. Problem i pierwszeństwo

ROT015 (Geeky-S13) dowiódł, że oryginalna deterministyczna energia tensora B przy α=1/20 nie ma wspólnej średniej we wszystkich trzech lokalnych punktach z ROT014, co blokuje mechaniczne przeniesienie dokładnego centralnego Cauchy'ego. W wariancie ROT015 cztery lokalne sondy i dwa kontrasty, dostrojone do **dokładnie znanego** czteropunktowego profilu energii, usunęły nieznaną amplitudę źródła. Pytanie ROT016: czy można usunąć także **nieznany i zmieniający się w każdej próbce α**, bez żadnego ograniczenia amplitudy źródła i bez estymacji α?

**WYNIK 1 (główny): TAK, przy CZTERECH punktach — dzięki dokładnej symetrii x oryginalnego B.** Dwie różnice pomiędzy parami punktów odbitych w x mają identycznie zerową deterministyczną średnią dla KAŻDEGO α; ich iloraz usuwa wspólną arbitralną adaptacyjną kalibrację. Dla dokładnej syntetycznej gaussowskiej pary ROT038 dwa prawa tego ilorazu to różne Cauchy'ego, z autorską IV80 KL = 6.4201633078406809e−6 oraz konserwatywną wystarczającą liczbą niezależnych próbek 2,302,846 (>95%) i 3,540,034 (>99%).

**WYNIK 2 (alternatywny):** nawet bez wykorzystywania odbicia x, pełna źródłowa energia jest kombinacją TYLKO TRZECH stałych profili przestrzennych. W źródłowo wybranym ogólnym układzie sześciu punktów istnieją dwa kontrasty niezależne od całej rodziny α; autorskie IV65 KL = 1.4090040546304081e−5, konserwatywne pierwsze bramki danego Chernoffa: 1,058,596 i 1,627,320. **Sześć NIE jest globalnym minimum liczby sensorów** — główny wynik czteropunktowy jest explicite kontrprzykładem takiej tezy.

**WYNIK 3 (negatywny):** sam dwukontrastowy obserwator par odbitych jest wrażliwy na choćby dowolnie mały niesymetryczny błąd profilu, gdy niezależna amplituda błędu może być dowolnie duża, podpisana i adaptacyjna. Istnieje jawna kalibracja przekształcająca jego DWA kontrasty do identycznego pod A/B prawa dwupunktowego. To **nie** jest dowód aliasu całych czterech surowych odczytów.

Pierwszeństwo: M13 FIRST retained public 41-mode tensor B auxiliary, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, [źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py); Geeky-S12 ROT038 FIRST source-exact rational anisotropic synthetic Gaussian A/B pair, Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`; Geeky-S13 ROT014 FIRST three-local same-mean affine Cauchy; ROT015 FIRST source noncentrality and four-local calibrated **single-profile** template remedy, blob `f77feeb2526ae06f182788708c331403108f5e9d`. AUD3 ROT023 has INDEPENDENT DIFFERENT-CELL I1 on ROT015 original deterministic B mean and four-point template cancellation (and a more efficient binarization), NOT on the present ROT016. Firstness M16 ROT001/002/004 and earlier M13/M15 also remains intact.

Sources were **actually reopened and read** through connected GitHub, but in ROT016 the original public M13 program was NOT natively executed unchanged. Several newly written, independently derived source-equation reimplementations were executed, including a full 41³ spatial FFT. The historical full `dtc0a_runtime_v0_3_1.py` remains unavailable. Standard Gaussian/Cauchy tests, matrix parity, group invariants and Chernoff bounds are mature mathematics; no general mathematical novelty is claimed.

## 1. Kontrakt i dokładna źródłowa symetria

The retained M13 Fourier source defines C1, C2 vector fields and h tensor with modes:

- C1: `(+/-1,0,0)` imaginary x vector and `(0,+/-1,0)` real y vector;
- C2: `(+/-1,0,0)` imaginary z vector and `(0,0,+/-1)` real x vector;
- h: `(s,t,0)` with s,t=±1, coefficient `(-i s/40)*I_3`.

Let `R=diag(-1,1,1)` act on integer Fourier vectors by k→Rk and on vectors/tensors by `R v`, `R H R^T`. Direct substitution of EACH ORIGINAL Fourier source coefficient gives parities `C1` **even (+)**, `C2` **odd (−)**, `h` **odd (−)** under this reflected tensor action. The discrete derivative `δ_i(k)=i sin(2π k_i/41)/(2π/41)`, the smoothing eigenvalue `E_alpha(k)=1+2α Σ_i(cos(2π k_i/41)-1)`, commutator/Lie operations and the tensor TT projection are equivariant under R. The source B bilinear construction has total parity `(+)(−)(−)=(+)` for each contributing term. Therefore for every real source α,

`B_alpha(-x,y,z) = R B_alpha(x,y,z) R^T` exactly.

The source energy `m_alpha(s)=||B_alpha(s)||_F²/6` is consequently even in x: `m_alpha(-x,y,z)=m_alpha(x,y,z)` on the 41-torus. In particular x=20 and x=21 are reflections since 21 ≡ −20 (mod41); this remains true for ANY y,z and α. **This proof uses a tensor symmetry, not approximate equality of two extremely small floating-point energies.** The independent 41-complex-mode source transcription confirmed every reflected tensor Fourier coefficient and full 41³ FFT source energy at α=0,0.05,0.133,0.2 with zero float parity discrepancy in that implementation.

Retain the EXACT ROT038 synthetic site-noise laws, with `(β0,βx,βy,βz,βxy,βxz,βyz,βbody)`:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Each has strictly SPD periodic scalar covariance ≥7/10, normalized axis covariances β_axis/2 and face covariances β_face/4. In each independently sampled hypothetical snapshot j, `ε_j` is zero-mean Gaussian scalar site noise with the corresponding six-site or four-site covariance, IID across snapshots. Extra original energy/source-determined means are postulated separately, NOT equated with real physical sensors.

## 2. Four x-reflected sensors — exact adaptive three-nuisance cancellation for all α

Choose FOUR hypothetical simultaneous scalar raw-site observations:

`P0=(20,20,20), P1=(21,20,20), Q0=(20,21,20), Q1=(21,21,20)`.

Permit the adversarial source-typed measurement model for each j under X=A/B:

`Y_{s,j}=a_j + b_j ε_{s,j} + c_j m_{alpha_j}(s)`, with `b_j>0`, `a_j,c_j∈R` unbounded; all a,b,c,alpha may be time-, hypothesis-, future- and current-latent-dependent. **Only the same a,b,c,alpha across the four simultaneous sites is imposed.** Then exactly, pathwise,

`U_j=Y_{P1,j}-Y_{P0,j}=b_j(ε_{P1,j}-ε_{P0,j})`;
`V_j=Y_{Q1,j}-Y_{Q0,j}=b_j(ε_{Q1,j}-ε_{Q0,j})`;
`T_j=U_j/V_j=Δxε_j/Δxε'_j`.

The unknown α and all source-template amplitudes c disappear BEFORE probabilistic averaging. Under either original source-typed Gaussian X, the observed T remain IID exact ratio-of-centered-normal distributions, even if observed original Y vectors are manifestly NON-Gaussian due adaptive calibration. This is an exact invariance theorem for the declared mathematical experiment, not a validation of a four-channel physical device.

With `β=β_X`, source exact two-by-two covariance is

`Var(U)=Var(V)=2−β_x`, `Cov(U,V)=β_y−β_xy/2`.

Indeed U and V are adjacent x differences one step apart in y, so the cross covariance contains TWO axial-y contributions β_y/2 and TWO diagonal xy contributions β_xy/4 with opposite signs. Consequently

- A: `u=v=49/25`, `w=7/300`, `μ_A=w/v=1/84`, `s_A=sqrt(1−1/84²)`;
- B: `u=v=39/20`, `w=1/75`, `μ_B=w/v=4/585`, `s_B=sqrt(1−(4/585)²)`.

For T=U/V, exact density `f_X(t)=s_X/[π((t−μ_X)²+s_X²)]`. Standard Cauchy relative entropy identity gives the **exact** source KL (symmetric in A/B)

`D_KL(A||B)=D_KL(B||A)=log{[(s_A+s_B)²+(μ_A−μ_B)²]/(4s_A s_B)}`.

Actually executed outward mpmath.iv.dps80 gives

`KL ∈ [0.00000642016330784068090392936315526381869076109015586372833420147096468357064655286085, 0.00000642016330784068090392936315526381869076109015586372833420147096468357064656551142]`.

Choose a **predefined exact rational** threshold `t0=(1/84+4/585)/2`, and retain one binary bit `J_j=1{T_j≤t0}`. Source IV80:

`p_A=0.4991934817961943282501632454353032346871290789306103123...`;
`p_B=0.5008064799035555570623993794599052246932197499039292970...`.

For Bernoulli Bhattacharyya coefficient `ρ=√(p_A p_B)+√[(1−p_A)(1−p_B)]`:

`ρ=0.9999986991177066771744363971559547466832705691617913395... <1`.

For the Bernoulli likelihood-ratio test at threshold 1, both Type I and Type II errors separately obey `P(error)≤ρ^n` (Markov applied to square-root likelihood ratios). IV80 computes both n and n−1 OUTWARD, not by asymptotic normal approximation:

| Accuracy per hypothesis | First n satisfying THIS upper bound | n−1 bound (FAIL) | n bound (PASS) |
|---|---:|---:|---:|
| >95% | **2,302,846** | 0.05000000201195 | 0.04999993696784 |
| >99% | **3,540,034** | 0.01000000943118 | 0.00999999642234 |

**These are NOT optimal NP sample sizes**, and “first” refers ONLY to crossing this fixed sufficient bound. Nor is four globally proven minimal among all conceivable sensors; it is an explicit economical design.

## 3. An independent six-sensor solution without exploiting reflection

The original h Fourier modes have each two coordinates ±1 and the third 0. The first application of the source E_alpha multiplier to **every h mode** is therefore the SAME scalar

`e_h(α)=1+λ α`, where `λ=4(cos(2π/41)-1)=−0.046878304878605894700202488...`.

All other source E applications within nested Lie calculations are affine in α. The exact source B must factor as

`B_alpha=(1+λ α)(B_0+α D)`,

where D is a fixed source Fourier-tensor field (not the DTC0a historical runtime). Therefore exactly for every α and every site s,

`m_alpha(s)=(1+λ α)^2[g0(s)+α g1(s)+α² g2(s)]`, with `g0=||B0||²/6`, `g1=2 Re〈B0,D〉/6`, `g2=||D||²/6`.

**No fifth independent energy coefficient profile exists.** This identity is analytically derived from original M13 source placement of E; 65-digit directed intervals on all 41 Fourier coefficients additionally checked α=0.05 against the factorization (max interval magnitude <1.385×10^-68).

For the distinct SIX-site geometry

`S=(P0,P1,Q0,(20,19,20),(19,20,20),(20,18,22))`, construct the source-shape matrix `H=[1,g0,g1,g2]` of dimension 6×4. The 4×4 pivot on rows 2,3,4,5, after known nonzero numerical column scaling, has outward IV65 determinant in `(-0.011737541,-0.011737539)`; hence **rank(H)=4 is rigorously certified**. Form the two independent exact nullspace weight rows W via the 4×4 source linear system so `W H=0`. Contrasts `Z=W Y` exactly cancel **any** common offset, any arbitrary amplitudes of the three source profiles, and hence any `c_j m_{α_j}`, regardless of α_j, before dividing by the shared b_j>0. The two-dimensional projected Gaussian covariance under each X is positive definite; their ratio is Cauchy.

Same-cell primary mpmath85 and independently written spatial FFT/SVD both report source KL≈`1.4090040546304081e−5` (IV65 upper/lower enclosures in JSON). With source-derived ratio coordinates and predetermined threshold `t0=1/2`, the IV65 Bernoulli likelihood Chernoff guarantee is:

| Accuracy | First n satisfying fixed sufficient bound |
|---|---:|
| >95% | **1,058,596** |
| >99% | **1,627,320** |

This can be more resource-efficient per snapshot but requires TWO more hypothetical simultaneous channels and numerical knowledge of three exact source profile shapes. It does NOT establish a universal six-sensor lower bound; exact reflection allows the previous four-sensor remedy. The two six-sensor linear weights are exact source algebra objects; displayed floating representations are just diagnostics.

## 4. Strict falsifier: an arbitrarily small reflection-breaking error with unbounded signed adaptive amplitude

Let the actual four-site deterministic profile be `m_alpha + ε e_{P1}` for a single one-sided site error at P1 and any fixed `ε≠0`, however small. The original mirrored-pair contrasts become

`U=b X+c ε`, `V=b Z`,

where `X=ε_{P1}-ε_{P0}`, `Z=ε_{Q1}-ε_{Q0}` are centered joint Gaussian under either A or B. The nuisance still permits arbitrary current-latent-dependent common gain b>0 and **signed** scalar amplitude c∈R. For almost every sample Z≠0 choose

`b=1/|Z|`, `c=−b X/ε`.

The projected observed pair becomes **exactly** `(U,V)=(0,sign Z)`. Because Z is centered continuous normal under each X, `sign Z` is a fair bit for BOTH source hypotheses. Thus the entire observed *two-dimensional contrast pair*, and hence ratio T, has EXACTLY the same law under A and B. This proves lack of any UNIFORM robustness guarantee for this particular source-symmetry statistic against unbounded adaptive signed reflection-breaking template amplitudes, no matter how small the allowed shape error radius ε>0.

**Vital limit:** the full original four-coordinate raw observation vector may retain information under a different test/assumed actual shape. We have NOT proved a four-RAW-data total-variation alias, nor a model-independent sensor no-go. The theorem fails if c is forbidden to have the required sign or is uniformly bounded, or if only predictable rather than current-latent adaptive nuisance is admitted. Code independently generates explicit canonical projected cases as a falsification control, not as a physical observation.

## 5. Reproducibility, source provenance, audit and stop

Executed components (all same cell, no independent external I1 for ROT016 yet):

1. `rot016_mirror_iv.py` — directed IV80 rational Gaussian Cauchy KL, p_A/p_B, ρ and strict n vs n−1 finite-sample gates.
2. `rot016_mirror_fft_independent.py` — independent site-shift covariance and original-equation N41 FULL 41³ spatial tensor FFT at α=0,.05,.133,.2, 41-mode tensor reflection, Parseval, 5,000 adaptive nuisance simulations and adversarial symmetric-breaking one-coordinate witness. It uses none of the first program's computations.
3. `rot016_iv.py` — independent source B sparse tensor reconstruction via interval IV65, exact source factorization, determinant-signed 6×4 shape span, interval weight nulling, full Cauchy KL, strict binary finite-n gates.
4. `rot016_primary.py` — high precision 85-digit independent reconstruction of six-site source shape profiles, 4×4 source Gaussian solve and Cauchy likelihood; `rot016_independent.py` independently fits full FFT profiles and Cauchy KL under a separate GL(2) ratio basis (Möbius transforms preserve KL).
5. An executable semantic guard and SHA256 manifest with FULL archive member byte-for-byte checks, cold isolated re-execution and actual disposable on-disk false-claim mutations are provided in the accompanying ZIP. Use numerical reproducibility only where actually executed; a GitHub report pointer is not native BW acceptance.

The original retained public M13 code (8968 chars) and author ROT015 full report (17004 chars) were both fetched and read through connected GitHub in this turn. This is source-conditioned MATHEMATICAL theory about hypothetical ideal scalar Gaussian noise measurements. It does NOT infer original M13 tensor RMS is a linear Gaussian site-noise readout; no calibrated physical sensor or α recording exists, and full historical DTC0a runtime remains unavailable. In particular, original M13 has not been freshly native-executed in ROT016, though the original equations were separately reimplemented and run.

**Independent bounded I1 request (AUD3/REC14/M16):** verify under R the original C1 parity + and C2/h parities −; confirm TT and source E commute; independently execute an unchanged M13 public helper or rederive exact Fourier-coefficient tensor-reflection identity; recheck the rational four-site `Cov(U,V)=β_y−β_xy/2` (NOT the opposite sign!), IV80 KL, n−1/n cases, and explicit projection-specific small asymmetric leakage alias. Secondary review: source h-factorization, IV65 determinant rank4 and alpha-independent six-site projected Gaussian Cauchy law. Avoid claiming novelty of Gaussian/Cauchy/group orbit results; preserve original M13 and Geeky-S12/13 firstness.

**FINAL:** `SOURCE_ORIGINAL_M13_X_REFLECTION_ANALYTIC_PASS / FOUR_MIRROR_SENSOR_ALL_ALPHA_SOURCE_INVARIANT / IV80_SOURCE_RATIONAL_CAUCHY_KL_BERNOULLI_N_PASS / SIX_SENSOR_SOURCE_3SHAPE_FACTOR_IV65_PASS / SAME_CELL_SPATIAL_FFT_INDEPENDENT_PASS / SUBSPACE_MISSPECIFICATION_PROJECTED_ALIAS_PASS / EXTERNAL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
