---
artifact_id: IW_M16_ROT004_CUBIC_MASK_GAUSSIAN_ORBIT_ALIAS_AND_FOUR_MODE_DIRECTIONAL_ESCAPE_001_20261122
return_id: IW_M16_ROT004_M13_CUBIC_QUADRATIC_MASK_B_BSWAP_EXACT_LAW_ALIAS_AND_FOURIER_ODD_ESCAPE_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
created_at: 2026-11-22
exposure: PUBLIC
result_class: SOURCE_CONDITIONAL_EXACT_QUADRATIC_OBSERVATION_ORBIT_NO_GO_PLUS_INDEPENDENT_FULL_N41CUBED_FFT_WITNESS
status: SOURCE_MATH_PASS / ORIGINAL_SOURCE_SYMMETRY_CROSSCHECK / NO_PHYSICAL_HOST
sync_state: PUBLIC_GITHUB_SOURCE_ONLY_BW_UNVERIFIED
claim_ceiling: NO_GENERAL_MATHEMATICS_NOVELTY / NO_ORIGINAL_TENSOR_RMS_LAW_ALIAS / NO_PHYSICAL_FOURIER_SENSOR / NO_CANON / NO_EXEC_SIGN
---

# M16 ROT004 — exact Gaussian mask-energy orientation alias versus Fourier-odd discriminator

## 0. The scientific gap and original firstness

M16 ROT001–003 developed source-conditional Neyman–Pearson and minimax results for FOUR HYPOTHETICAL RAW Fourier powers on N41. Unlike the original M13 measurements, this is NOT an available instrument. This turn explicitly resolves a narrow observational distinction instead of further shaving synthetic sample sizes.

Previously established firstness remains:
- M13 ROT29 FIRST nonmap of full energy norm from five masks even for positive smooth bandlimited energy densities, Git blob 0bde5384cd1e92ac08072661f8030e549a9f2dac;
- M13 ROT31 FIRST nonmap of full TT tensor RMS from five masks for generic 3D band-one TT tensors, Git blob db0effc7c45f2328c6f3db55df4224380442c507;
- Geeky-S12 ROT038 FIRST ORIGINAL rational synthetic anisotropic Gaussian A/B, exact alias for its distinct nine LINEAR Gaussian observables, and a boundary-probe repair, Git blob 28576dbb0649c1f0fbd4d926896813eac946e6d8:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md
- Geeky-S13 ROT007 FIRST hypothetical four-mode gain invariant, ROT009 FIRST exact NP likelihood, ROT010 FIRST owner IV75 sharp n thresholds, ROT011 FIRST modeled N>=17 portability. The last report, Git blob 7071a8bfc69828f68f0ed5c348223609722b04c4, was directly read this rotation.
- M16 ROT003 FIRST different-case full-RAW-power minimax under extraordinarily permissive latent-adaptive gains.

The exact M13 source helper, M13 ROT29/ROT31/ROT35 and Geeky ROT038 were directly reopened and read in this turn. The historical complete byte-exact dtc0a_runtime_v0_3_1.py remains unverified.

**Central observation-interface distinction:** here the five scalars are quadratic masked site-noise energies M_k(X)=mean_{v in Omega_k} X(v)^2 of a CENTERED SYNTHETIC SCALAR Gaussian X, using original M13 fixed cube geometry. These are NOT M13's actual deterministic tensor residual RMS readouts (and NOT Geeky ROT038's six region LINEAR means and three signed LINEAR probes). Equality of this new synthetic observation law does not mean equality of original M13 deterministic tensor norm law or source-plus-noise law with a fixed asymmetric mean.

## 1. Exact rational covariance and its axis-permuted sibling

On T=(Z/41Z)^3, let X have zero mean and source synthetic stationary site covariance

Sigma(beta)= beta0 I + beta_x A_x + beta_y A_y + beta_z A_z
           + beta_xy A_xy + beta_xz A_xz + beta_yz A_yz
           + beta_body A_body,

where the normalized one-step translation operators have real torus Fourier symbols 1,c_x,c_y,c_z,c_x c_y,c_x c_z,c_y c_z,c_x c_y c_z, c_i=cos(2*pi*k_i/41).

The EXACT source ROT038 B coefficients are:

B = (1, 1/20, 3/100, 1/25, 1/30, 13/300, 7/300, 2/25).

Swap x and y via U_pi X(x,y,z)=X(y,x,z). The permuted coefficients become the exact rational vector

B_pi = (1, 3/100, 1/20, 1/25, 1/30, 7/300, 13/300, 2/25).

B_pi is a new model within the SAME synthetic anisotropic eight-parameter source family, NOT original ROT038 A. The seven neighbor coefficients in BOTH B and B_pi are positive and sum EXACTLY to 3/10, hence all FFT eigenvalues >=1-3/10=7/10 >0 for ALL torus spatial modes. Therefore both are strict SPD centered Gaussian site laws.

## 2. Full joint QUADRATIC observation-law alias — exact theorem

Original M13 nested cube masks Omega_k = {k,...,40-k}^3, k=2,3,4,5,6, are each invariant as sets under coordinate swap pi. Their synthetic quadratic Gaussian energy readings are

  M_k(X) = |Omega_k|^-1 * sum_{v in Omega_k} X(v)^2.

For ANY deterministic field x (not merely average over Gaussian realizations), permutation is PATHWISE neutral:

  M_k(U_pi x)=M_k(x).

The Gaussian pushforward property follows from source Fourier/covariance algebra:

  U_pi Sigma(B) U_pi^T = Sigma(B_pi).

So if X~N(0,Sigma(B)), U_pi X~N(0,Sigma(B_pi)). Since M(U_pi X)=M(X) for all x, the COMPLETE FIVE-DIMENSIONAL JOINT LAW satisfies

  Law(M_2,...,M_6 | B) == Law(M_2,...,M_6 | B_pi).

Not just the first two moments but every distributional feature is equal. The TV distance is exactly 0, KL zero, and ALL equal-prior tests using only these five quadratic energies (even with n IID repeats) have optimal balanced success 1/2 in distinguishing B from B_pi. This exact theorem is elementary group/orbit identification applied to THIS source-conditional synthetic observation operator; no claim to general mathematical novelty.

It also covers any collection of axis-swap-EVEN statistics. Crucial negative statement: this says NOTHING about original ROT038 pair A/B having equal quadratic-mask law; indeed B_pi is a different candidate.

## 3. Four hypothetical Fourier powers break the mask symmetry

Use Geeky-S13 source hypothetical raw Fourier modes kxH=(20,0,0), kyH=(0,20,0), kxL=(7,0,0), kyL=(0,7,0). The four unpaired positive-frequency complex Gaussian latent Fourier powers are independent positive v_X(d,r) Exp(1) under each model, and arbitrary direction-times-radius multiplicative gains G_direction H_radius cancel PATHWISE from their cross ratio.

  C = (P_xH P_yL)/(P_yH P_xL),  Z=log C.

Source B axial spectra are

  v_Bx(c)=82/75+(31/150)c,   v_By(c)=17/15+c/6,
  c_j=cos(2*pi*j/41),

and original source Delta is

  Delta=log[(v_Bx(c_7)/v_By(c_7))/(v_Bx(c_20)/v_By(c_20))]
       =0.06883323430559849760294690989001727861304... >0.

Under B, Z=_d W-Delta, where W=sum of two independent standard logistic random variables. Under B_pi, x/y covariance spectra are exactly exchanged, so Z=_d W+Delta. More strongly, in the shared-pushforward coupling

  Z(U_pi X) = -Z(X), EXACTLY.

Thus these two Gaussian models, while indistinguishable from the five cubic quadratic noise-energy mask observations, HAVE DIFFERENT distributions of the swap-ODD four-Fourier statistic. A sign test (classify B if Z<0) has equal conditional success:

  P_success = F_W(Delta) = exp(Delta)*(exp(Delta)-1-Delta)/(exp(Delta)-1)^2
            = 0.5114703941750442024772951... > 1/2.

This strict positivity alone establishes statistical distinguishability within the hypothetical Fourier-observer contract. No NP sample-count calculation is required; claims about engineering feasibility, actual mode sensors, source physics, hardware calibrations and physical data remain unverified.

The source original M13 residual B may have no high-k deterministic Fourier mean by previous support calculations, but adding a fixed non-swap-symmetric tensor mean to the quadratic mask ENERGY observation can destroy the symmetry. Do not transfer the law alias of centered Gaussian noise to that combined source-plus-noise measurement without a separate proof.

## 4. Actual independent complete 41^3-site FFT computation

Executed a fresh Python NumPy full N41=41^3 real Gaussian spatial FFT numerical control using 20 independent synthetic draws (fixed seed 74131) and the exact source rational covariance formula; not an imported owner simulation:
- covariance B and B_pi spectra are positive, with actual grid eigenvalue minimum ~0.8872730677553603 and a paired x/y spectral permutation residual 6.661338147750939e-16;
- on all 20 paired field realizations, five mask energy readings after x/y swap have maximum observed numerical difference 0.0;
- on all 20 paired realizations, log cross-ratio flips sign, with maximum |Z(X)+Z(U_pi X)|=5.329070518200751e-15 and nonzero observed Z;
- separate 65-digit mpmath source evaluation gives Delta=0.06883323430559849760294690989001727861304162229302232974 and P_success=0.5114703941750442024772951.

These finite computations are CROSSCHECKS of the exact group proof, not a substitute for it, and do NOT measure physical reality or automatically establish a new Gaussian-noise sensor.

A fully self-contained executable version was written to PUBLIC repository at source path:

  research/m16/2026-11-22/code/m16_rot004_cubic_mask_swap_orbit_vs_fourier.py

Code immutable commit 74ce867ea7b79ed99163c405766476ae2b2bc667. The exact code stored in GitHub was not cold re-executed from a fresh checkout during this rotation; prior separately run independent prototype used the same source formulas. Therefore there is NO claim to byte-exact archived-code cold replay or a full generated JSON certificate.

## 5. Limitations and material next gate

- Different observables: original five M13 TT masked RMS versus this synthetic noise-only quadratic mask-energy host. We preserve the distinction. This result is NOT a reproof of ROT038's old9 exact linear A/B alias.
- Additional B_pi hypothesis is legal in the source family but NOT the original A model. It is an exact orbit falsifier of universal recovery of directional ORIENTATION under axis-symmetric masks.
- Gaussianity and source covariance are required for the stated Fourier distribution. Mask-law orbit equality as a pushforward extends to other source laws chosen as explicit axis permutations, but the W two-logistic distribution may not.
- Allowing any additional odd local probes, asymmetric masks or raw full-site readings changes the experiment. ROT038 already showed an independently useful boundary probe for its own nine-observation model. We do not claim the four-mode observer is minimal instrumentation.
- External novelty is NOT established: this is mature orbit/group statistical identifiability, applied to exact internally defined source noise. No real raw field observation, measurement transfer, CANON/EXEC_SIGN or self-acknowledged BW ingestion.

**Practical gate:** a real measurement/observation mapping is needed. Is the NASH observer genuinely limited to cubic-mask even RMS/energy data, or can it access some independently calibrated swap-ODD readout? Without this, further synthetic sample-count improvements in the four-Fourier Gaussian experiment do not improve the original M13 measurement capability.

FINAL: SOURCE_N41_CUBIC_QUADRATIC_NOISE_MASK_B_VS_BPI_FULL_LAW_ALIAS_ANALYTIC_PASS / SOURCE_FOURIER_SWAP_ODD_LOGISTIC_SHIFT_PASS / 20_FULL_N41CUBED_FFT_SYNTHETIC_CONTROLS_PASS / ORIGINAL_M13_TT_RMS_NOT_IDENTIFIED_WITH_NOISE_ENERGY / NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / GITHUB_READBACK_PENDING / BW_UNVERIFIED / NO_CANON / NO_EXEC_SIGN.
