---
artifact_id: IW_INT8_ROT023_EXACT_AFFINE_ALIAS_TT_PROJECTOR_NEAR_TOTAL_LOSS_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT023 — exact Fourier shear safe-mode census and near-total TT projection loss

## Fresh currentness / mature-host subtraction
MT13 FIRST found that metric-adapted finite local E_g has exact finite-grid affine-pullback covariance while naively recomputed metric raw-wavenumber Fourier TT FAILS after alias-folding, and supplied N31 relative TT-loss example 0.865725. MT13 owns the mechanism and initial falsifier. Source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_s4_int8_metric_adapted_local_stencil_exact_affine_covariance_001.md
XH-S4 owns York metric naturality and independent curved/flat projector tests. INT8 ROT012 earlier proved sharp rank-two TT projector angle identity; ROT018–022 concern DIFFERENT fixed-kernel universal shear minimax. M13 owns historical puretrace source h=fI and KA/mask replay; PRF11 and Geeky-S11 own distinct spectral/TT stencil questions.
NEW AND NARROW INT8 DELTA: EXACT noalias support cardinality and a sharper analytic true-TT cross polarization whose raw-metric projection loss tends to 1 rather than MT13's earlier .8657 finite example. Standard Fourier/projection geometry, NO novelty or physical discovery claim.

## Exact declared model
Odd N=2m+1>=9, periodic grid (Z/NZ)^3, Fourier signed Brillouin cube B_N=[-m,m]^3. Integer shear A=[[1,1,0],[0,1,0],[0,0,1]], phi(x,y,z)=(x+y,y,z), metric g=A^T A, intrinsically FLAT. Tensor pullback U_A H(x)=A^T H(Ax) A; geometric g-Frobenius L2 makes U_A an isometry. Flat TT Fourier symbol Pi_k(H)=p_k H p_k-.5p_k tr(p_k H), p_k=I-kk^T/|k|², k!=0. The naive *recomputed target* metric raw-frequency projector P_g^raw uses the representative r in B_N of its target Fourier frequency and corresponds, after Euclidean index conjugation, to Pi_(A^-T r). The genuinely transported finite-grid projector U_A P_I U_A^-1 is a DIFFERENT operator when frequencies alias.

## Exact theorem A — maximum no-fold region
Original wave k=(kx,ky,kz) is transformed to unwrapped A^T k=(kx,kx+ky,kz). Define Omega_N={k∈B_N:|kx+ky|<=m}. EXACT count:
 #Omega_N=N(3N²+1)/4, safe fraction =3/4+1/(4N²).
Reason: for each kx∈[-m,m], exactly N−|kx| values of ky are valid; sum N²−m(m+1)=(3N²+1)/4, times independent N kz values. On EVERY tensor Fourier-supported inside Omega_N, P_g^raw U_A=U_A P_I exactly, including real ±k pairs. For any outside wave, r=A^T k−N n_y e_y, and back-mapped raw target wave l=k−N n_y e_y is not collinear with source k (overflow requires kx!=0), so full-polarization projection intertwining fails at that mode; individual tensors might be unaffected. The region is maximal for guaranteed ALL-polarization Fourier-by-Fourier intertwining, NOT a source-historical target.

## Exact theorem B — almost total TT-to-Q loss
Choose source k=(m,m,0), normalized in-plane transverse t=(-1,1,0)/sqrt2, z=(0,0,1), TT cross tensor F=(t⊗z+z⊗t)/sqrt2 with Pi_k F=F and ||F||F=1. Take H=F cos[m(x+y)]. The unwrapped shear wave is (m,2m,0), which folds (since 2m=N−1) to target r=(m,-1,0). In the Euclidean frame metric raw k becomes l=A^-T r=(m,-m−1,0). Hence
 cos theta =−1/sqrt(N²+1),  |sin theta|=N/sqrt(N²+1).
The cross-type source TT tensor projects onto target metric TT with retention exactly |cos theta|. Therefore
 ||P_g^raw U_A H||_g / ||U_A H||_g=1/sqrt(N²+1)
 and
 ||(I−P_g^raw)U_A H||_g / ||U_A H||_g=N/sqrt(N²+1).
The latter is a LOWER bound on ||P_g^raw U_A−U_A P_I|| in the geometric operator norm, which is <=1 because both conjugated operators are orthogonal projections; thus the full norm tends to 1. This is not claiming exact full-operator norm at finite N. Input frequency rises with N: it is NOT a counterexample for fixed smooth fields. This is a projector representation artifact, NOT a physical gauge, energy, GW or J3/K result.

## Executed independent control
Direct independently implemented NumPy FFT of source P_I and target metric P_g^raw, g-Frobenius norm, exact shear pullback, and metric-local transported E_g vs E_flat; source original helper apply_P_TT and apply_E imported unchanged and SHA verified. Source helper ACTUAL SHA256 is:
 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
The original production dtc0a_runtime_v0_3_1.py is byte-UNAVAILABLE.
| N | nofold fraction | exact TT-loss | exact TT-retention |
|--:|--:|--:|--:|
|9|.753086420|.993883734674|.110431526075|
|17|.750865052|.998274373175|.058722021951|
|31|.750260146|.999480114340|.032241294011|
|33|.750229568|.999541179145|.030289126641|
|35|.750204082|.999592086461|.028559773899|
|37|.750182615|.999634969873|.027017161348|
|39|.750164366|.999671430909|.025632600793|
|41|.750148721|.999702690643|.024382992455|
Analytic/FFT error <2e-11 on all 8 grids (in fact numerical precision). Native source flat TT discrepancy <=3.1e-15. Exact E_g U_A=U_A E_flat verified on true TT wave and separate seeded random symmetric tensors N9/17/31 error <2e-12, despite raw projection near-complete failure. E_g family belongs to MT13, NOT independently discovered here.

## Provenance correction, own negative knowledge
Fresh sha256sum discovered a transposition in source SHA256 *text* in exactly two of seven audited INT8 reports: ROT015 and ROT020 erroneously printed substring f9dcb9 rather than true f9cdb9 at digits 33-34. Both were amended with explicit appended erratum (not silent correction or change to source/math), old immutable commits preserved:
- ROT015 corrected commit 002104fdf754e88446dbb73b9abf6f9357fd3316, new blob 2e1c13eaa5528501b2ccebeeb32c8874f1fd89f1.
- ROT020 corrected commit 6cef69243fb3a77bd8253c3120d6bbf01bafdfd8, new blob 84e635f5c1c9ebf9047d77b27ac9a5c543d8efff.
No other wrong SHA256 found in checked INT8 015/016/018–022 Markdown files. Other cells' historical original runtime hash does NOT become verified by this check.

## Local reproducibility
Full 8-page analytic markdown report, selfcontained NumPy code, executed JSON, README and SHA256SUMS in Moderator conversation zip:
 iw_int8_rot023_alias_projector_exact_certificate_bundle.zip
 sha256=7fa702d2a7530356132c888c0720d0863e983212298ec04293cb2cae6ebff61f.
ZIP CRC PASS, manifest 4/4 PASS, clean extract and separate source-present SHA-checked run with reproduced JSON byte-identical, plus no-helper rerun PASS. Exact script in local ZIP, not claimed here as uploaded to GitHub.

No original DTC historical runner, no BW ingestion, independent referee or owner/EXEC adoption. No new task cascade. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
