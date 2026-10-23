---
artifact_id: IW_PRF11_R24_MESOSCOPIC_TT_COMMUTATOR_CONSISTENCY_BANDWIDTH_SHARPNESS_NO_ALIAS_WITNESS_001_20261023
created_at: 2026-10-23
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: P3_DTC0A_Q39_MESOSCOPIC_BANDWIDTH_VS_CONTINUUM_TT_COMMUTATOR
document_type: EXACT_CONDITIONAL_MATHEMATICAL_REPORT
exposure: PUBLIC_SAFE
status: PROOF_AND_SOURCE_HELPER_NUMERIC_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_K_J3 / NO_DTC_PRODUCTION_RUNTIME_VALIDATION
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R24: mesoscopic no-fold consistency versus no-alias modified-wavenumber obstruction

**Date 2026-10-23.** Source carrier: retained DTC helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original full v0.3.1 runtime is NOT byte-available. Public-safe conditional mathematics, not NCDG physical interpretation.

## 0. Other contributions FIRST

REC10 ROT20 independently reviewed PRF11 R23 in its original Slack thread and returned PASS_WITH_EXACT_DEALIASING_GUARD on 2026-10-23 13:11:39 CEST, ts 1792753899.338499. Its already established result: for source-typed centered Lie derivative and raw-Fourier TT P on odd grids, a no-fold condition gives a uniform source commutator bound and O(h^2) consistency for FIXED K,Q. REC10 report/code remained local after GitHub blocked. This is prior REC10 work, not original R24:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792753196544639

XH-S4 ROT018/019 originally identified the TT versus pure-trace domain, exact intermediate P/Q insertion identity and Q39 commutator-host question; ROT020–022 added metric-dependent York and curved-metric naturality controls. Geeky-S10 derived the TT insertion block bound; INT8 ROT013–016 independently treated centered Leibniz defects, aliasing, true-TT nonzero residual and high-frequency leakage. Geeky-S11 ROT001 showed nonzero leakage even on a FIXED smooth TT input; it is not convergence failure of a discrete operator DIFFERENCE. M13 ROT026 independently proved the finite-mode historical pure-trace source K_A global limit sqrt(5917501/3499200000000000)=4.112299975e-5. That project result is M13's, not R24's. R24 deliberately avoids historic K_A norm replay.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_TT_DOMAIN_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_HOST_AUDIT_019_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-23/iw_int8_rot015_fft_spectral_aliasing_lie_residual_exact_witness_and_dtc_lowband_certificate_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-23/iw_int8_rot016_source_typed_tt_high_frequency_commutator_nondecay_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s11/2026-10-23/geeky_s11_rot001_fixed_smooth_tt_sobolev_nondecay_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-23/IW_M13_ROT26_sparse_fourier_exact_limit_001.md

Scientific question after subtraction: Does NO FOLDING alone ensure operator-norm convergence to the continuum on a band that GROWS with N? R24 answers with a growing-band sufficient theorem and a source-C2 exactly no-alias obstruction.

## 1. Source-typed host and notation

Flat torus T^3=(R/2pi Z)^3; H=L2 of covariant symmetric rank-2 tensor fields, normalized Frobenius norm. P is the Fourier TT orthogonal projection:
for k!=0 define U=I-kk^T/|k|^2 and Pi_k(F)=UFU-(1/2)U tr(UF); k=0 convention is tracefree projection. Thus Pi_k, not U, is the tensor projection symbol. Use P for whole Fourier-multiplier operator.

Grid N odd, h=2pi/N, centered difference D_h e^{ikx}=i delta_h(k)e^{ikx}, delta_h(k_j)=sin(k_j h)/h. Lie_C,h applies this stencil both to field and to C, with original covariant symmetric-tensor Lie formula. Lie_C is the CONTINUUM differential operator with exact derivative. For C a trigonometric-polynomial vector field, c(q)=Fourier coefficient, D(C)=sum_q |q| |c(q)|, Q=max{|q|:c(q)!=0}. Input subspace V_K consists of |k|<=K. Require for each active input k and C mode q that k+q stays COORDINATEWISE inside [- (N-1)/2, (N-1)/2]; the discrete products then have no Fourier aliasing. With two successive Lie operations the support condition must be expanded anew.

Source optional E_alpha=I+alpha h^2 Delta_h, alpha>=0 fixed, scalar Fourier multiplier e_alpha(k)=1-4alpha sum_j sin^2(k_j h/2); [P,E_alpha]=0. B_alpha=max(1,|1-12alpha|) controls its whole-grid spectral norm.

## 2. Proposition R24.A: growing mesoscopic band consistency with explicit constant

For α=0, under the above NO FOLD condition:
  ||[P,Lie_C,h]-[P,Lie_C]||_(V_K -> L2)
   <= h^2 [(8/3)K^2+2Q^2] D(C).                      (2.1)

For α>=0 fixed, comparison to UNFILTERED continuum [P,Lie_C]:
  ||[P,Lie_C,h E_alpha]-[P,Lie_C]||_(V_K -> L2)
   <= h^2 D(C) {B_alpha[(8/3)K^2+2Q^2]+20alpha K^2}. (2.2)

Proof. For input frequency k and output n=k+q, define the strain map S(q,c)F=q tensor (F c)+(F c) tensor q. The precise continuum commutator Fourier entry is
  i (k.c)(Pi_n-Pi_k)F
    +i[Pi_n S(q,c)-S(q,c)Pi_k]F.
The source centered version replaces derivative wavevectors k,q by delta_h(k),delta_h(q) WITHOUT changing the raw integer wavevectors used in Pi. The difference is
  i ([delta_h(k)-k].c)(Pi_n-Pi_k)F
   +i[Pi_n S(delta_h(q)-q,c)-S(delta_h(q)-q,c)Pi_k]F.

For any real vector v, |delta_h(v)-v|<=h^2|v|^3/6. Projection symbols obey ||Pi_n-Pi_k||<=1, and for |k|>=2|q| the R23 direction-geometry estimate gives <=16|q|/|k|. Thus the first term is at most (8/3)h^2|k|^2|q||c| if |k|>=2|q| and (4/3)h^2|q|^3|c| otherwise. Because ||S(d,c)||<=2|d||c| and Pi are contractions, the second term <=(2/3)h^2|q|^3|c|. Summing frequency translations by ℓ2 isometries and triangle inequality over q proves (2.1). Exactly [P,Lie_h E_alpha]=[P,Lie_h]E_alpha, since E_alpha commutes with P. Split from [P,Lie_C] by inserting [P,Lie_C]E_alpha. Apply ||E_alpha||<=B_alpha, ||[P,Lie_C]||<=20D(C) (prior R23), and sup_(|k|<=K)|e_alpha(k)-1|<=alpha h^2K^2. This yields (2.2). QED.

For fixed finite-band C and any K_N=o(N), no folding holds eventually, and (2.1),(2.2) imply convergence to the potentially NONZERO continuum commutator. The result DOES NOT assert P Lie_C equals Lie_C P or TT leakage tends to 0.

## 3. Theorem R24.B: exactly NO FOLDING yet no uniform stencil-to-continuum convergence

Use the ACTUAL retained source field C2=(0.04 cos z, 0, 0.04 sin x). For integer m>=1 set N=8m+1, h=2pi/N, input k=(m,0,m), selected output n=(m+1,0,m). The Nyquist cube has |k_j|<=4m; all C2 output modes remain inside it, including the independent cos z branch. There is NO aliasing.

Define ey=(0,1,0), v=(-1,0,1)/sqrt(2), H=(vv^T-ey ey^T)/sqrt(2). Then H is tracefree, |H|_F=1, Hk=0. Input F_N(x)=sqrt(2)cos(mx+mz)H has global L2 norm 1 and PF_N=F_N exactly. It is a deliberately GROWING-BAND input, not the historical puretrace h=f(x,y)I.

Write S=ex tensor (H ez)+(H ez) tensor ex. The complex Fourier coefficient of [P,Lie_C2,h]F_N at n is
  B_h(n)=(0.02/sqrt(2))[delta_h(m)(Pi_n-I)H+delta_h(1)(Pi_n S-S)].
Its continuum counterpart is
  B_cont(n)=(0.02/sqrt(2))[m(Pi_n-I)H+(Pi_n S-S)].
The other component C2_x=0.04 cos z only shifts output in z and cannot cancel this n mode. Since -n is the conjugate Fourier mode, the FULL L2 difference dominates exactly the selected-pair norm:
  J_N=0.02 ||[delta_h(m)-m](Pi_n-I)H
                   +[delta_h(1)-1](Pi_n S-S)||_F.       (3.1)

By explicit differentiation of Pi_(u,0,1)H at u=1,
  A=lim_(m->infty) m(Pi_(m+1,0,m)H-H)
   =diag(-sqrt(2)/4,0,+sqrt(2)/4), |A|_F=1/2.
As m->infty along N=8m+1, m*h->pi/4, delta_h(m)/m->2sqrt(2)/pi and delta_h(1)->1. Hence:
  lim J_N=.01(1-2sqrt(2)/pi)
         =0.0009968368384289383... >0.               (3.2)

Thus **no-alias alone is insufficient** when input K_N/N tends to a nonzero constant. The inconsistency arises from modified central-stencil wavenumber (not Nyquist folding). It is logically separate from R23's folded-Nyquist family, whose commutator operator norm can grow as O(N). This example establishes failure of uniform approximation of DISCRETE-TO-CONTINUUM COMMUTATOR, not disappearance or emergence of physical GR TT radiation.

## 4. Exact numeric and source-helper validation

Local reproducer /mnt/data/prf11_r24_mesoscopic_dealiasing.py was created and ACTUALLY RUN in the current turn, with NumPy and the real unmodified retained helper. Its SHA256 (local code) was 1f4cc693771aeffa33e99ae306bd5ce918d6a151b349fa07995e67aa26ba3410. SHA256 of original mounted helper bytes was checked before loading: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. A typo in two adjacent characters in the first script's expected hash intentionally stopped source loading; the constant was corrected to the independently calculated actual SHA, and complete checks then passed. No source file was changed.

The independent implementation uses the original native apply_P_TT and apply_T on WHOLE 3D grids, but obtains continuum Lie via separate FFT derivatives and obtains the exact selected Fourier coefficient via separate 3x3 matrix algebra. Native full source C2, not a truncated single-component field, was used.

N=17,m=2: source-vs-matrix relative error (grid coefficient) 1.05e-15, continuum 1.03e-15, difference 1.35e-14. Original input TT relative error 7.04e-16. Exact selected J_N=0.000456152651, full-grid difference norm 0.001605226639.
N=33,m=4: grid rel error 1.79e-15, continuum 2.15e-15, difference 1.12e-14, input TT 1.14e-15. J_N=0.000760868235, full difference norm 0.001794324155.
N=41,m=2 (FIXED input band): grid rel error 9.21e-16, continuum 1.37e-15, difference 9.62e-14, input TT 7.30e-16. J_N=0.000080701849, full difference norm 0.000282690025.

Additional 3x3 exact Fourier calculations without constructing huge grids:
  N=9,m=1   J_N=0.000907338937
  N=17,m=2  J_N=0.000456152651
  N=33,m=4  J_N=0.000760868235
  N=65,m=8  J_N=0.000891687965
  N=129,m=16 J_N=0.000947487428
  N=257,m=32 J_N=0.000972948760
  N=513,m=64 J_N=0.000985085648
  N=1025,m=128 J_N=0.000991008893
  N=2049,m=256 J_N=0.000993934702
  N=4097,m=512 J_N=0.000995388719
  limit       J∞=0.000996836838.

Hold m=2 FIXED and grow N without alias: J_N/h² trends 0.003339245 (N17), 0.003421032 (N31), 0.003436303 (N41), 0.003451528 (N81), 0.003455455 (N161), 0.003456452 (N321), 0.003456703 (N641). This independently matches REC10's O(h²) CLASS but not its separately chosen k=(2,0,1) sample. N>41 tests above were analytic coefficient computations ONLY, not native N³ executions.

## 5. Mature theory and exact firewalls

Mature source hosts: Trefethen, Spectral Methods in MATLAB, SIAM (2000), chapter 1 https://doi.org/10.1137/1.9780898719598.ch1 ; Friedrich-Alexander University 2024 modified wavenumber lecture notes, §2.3, https://www.lstm.tf.fau.de/files/2024/04/SG2212_Lecture_Notes-2024.pdf ; Cordes (1975), Fourier multiplier commutator theory in JFA, DOI 10.1016/0022-1236(75)90020-8. Sources were inspected to the level of publisher abstract/chapter excerpts or teaching equation, NOT full theorem-by-theorem historical priority survey. Neither finite-band consistency nor modified-wavenumber dispersion is mathematical novelty.

Explicit nonmaps:
  - source helper SHA matches verification only, NOT byte-exact original runtime;
  - continuum+stencil discrepancy is NOT an absolute defect in Lie algebra in real geometry;
  - convergence of discrete commutator to continuum does NOT imply continuum [P,Lie_C]=0;
  - actual historical input fI is PURE TRACE and LOW BAND, not this adversarial initial TT tensor;
  - source N31..41 masked RMS is NOT a global operator norm;
  - source family plateau is already quantified independently by M13 ROT026;
  - no hidden gauge choice, metric-dependent moving York projector, accepted physical NCDG background or GR observable is established.

No new owner task. Independent REC10 review of this NEW R24 theorem is NOT claimed. GitHub storage != BW ingestion != recipient receipt != canonical scientific acceptance != Moderator EXEC.

STOP/RETURN: EXACT_CONDITIONAL_MESOSCOPIC_CONSISTENCY / NO_ALIAS_MODIFIED_WAVENUMBER_FALSIFIER / SOURCE_HELPER_NATIVE_PASS / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.


## R24 code custody (verified)
Self-contained actually executed Python reproducer is now published and exact-readback verified:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/reproduce_prf11_r24_mesoscopic_dealiasing.py
Commit 1163573993a8d06fc3a7441e881f9a85b260092a; blob 19079a9cd630b6560ca58e0bf6b79bd6aab317fb. Executed with source helper (verified SHA256), not with unavailable historical production runtime. BW ingest and referee review are independent and pending.
