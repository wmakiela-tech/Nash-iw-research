---
artifact_id: IW_DAX_S9_ROT012_COHERENT_BORN_FSI_CHARGE_PROJECTION_WATSON_PHASE_AND_R68_KERNEL_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: COHERENT_SOURCE_PUBLISHED_PHOTOPRODUCTION_S_WAVE_EXECUTION / ORDERED_ISOSPIN_PROJECTION / WATSON_ELASTIC_NEGATIVE_CONTROL / R68_SOURCE_REWEIGHT
claim_ceiling: NO_COMPLETE_GAMMAGAMMA_PIPI_PHOTOPRODUCTION / NO_VALIDATED_F2_CHARGED_PRODUCT / NO_EXPERIMENTAL_CI / NO_PHYSICAL_NEUTRINO_OR_IN_MEDIUM_TRANSPORT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT012 — coherent Born+FSI gamma-gamma -> charged-pion s-wave and elastic Watson normalization falsifier

Date **2026-11-22**. This is a SOURCE-RESTRICTED ORIGINAL REEXECUTION of previously published mature physics, not a new charged-pion prediction, not a reproducing Dai–Pennington 2014 Solution I, nor a complete Klevansky et al 2025 Born+FSI+f2 photon production spectrum. Scientific firstness of ROT010 original strong hadronic T and ROT011 original scalar Born partial wave tests is retained.

## 1. Original primary published source directly re-read

S.P. Klevansky, R.H. Lemmer, A. Beygi, EPJA **61**, 49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , full publisher HTML equations (9), (28)–(37), (55)–(56), (60), (62), (65)–(70), (72)–(75), Table 2. Secondary original-paper PDF *text* at https://wiredspace.wits.ac.za/server/api/core/bitstreams/4c69ff7b-4d5f-485c-9a69-e65971f49e28/content confirms Table 2 and a separate Eq83 neutral-pion prefactor. The attempted web screenshot of the PDF yielded a cache miss. No original PDF native SHA or visual image inspection claimed. The paper itself states no associated deposited code/data. The central new DAX9 work is a **separate executing model implementation** checked against original equations.

## 2. Ordered particle charge projectors from source Eq28

Author states:

- |ππ;I0> = −(|π+π−>+|π−π+>+|π0π0>)/sqrt(3)
- |ππ;I2> = −(|π+π−>+|π−π+>−2|π0π0>)/sqrt(6)
- |KbarK;I0> = −(|K+K−>+|K0 Kbar0>)/sqrt(2)

Taking **ordered physical particle state** overlaps rather than conflating them with a normalized charged symmetrized two-pion isospin state gives:

T_{π+π−;π+π−} = (1/3)T0_{22} + (1/6)T2_{22};
T_{π+π−;K+K−} = T0_{21}/sqrt(6).

They are SOURCE-DERIVED projection coefficients, not a fit. In particular using (2/3)T0+(1/3)T2 for a fixed ordered charged-pair T in Eq65 (while retaining its Born normalization) doubles the hadron term erroneously. That error is directly falsified by Watson phase below.

## 3. Coherent published s-wave Eq9 + Eq65

Use Klevansky author mπ=0.140 GeV, mK=0.496 GeV, fπ=.093 GeV, Λ=1.351 GeV, original published hadron T0/T2 on-shell loops and **distinct** photo loop J from Eq62. Define β²=1−4mπ²/W², B(W)=(1−β²)log[(1+β)/(1−β)]/β. Normalize the photoproduction amplitude by its common −i e² factor:

F(W) = B(W) − [Jπ(W)(T0_{22}/3 + T2_{22}/6) + JK(W)T0_{21}/sqrt(6)]/(8π²).

The exact **leading s-wave** fiducial |z|<.6 source equation then yields σ_s(W) = .6 πα²β/(2W²) |F(W)|². Setting hadron T=0 returns original Eq17 Born s-wave. This is *not* exact full scalar-QED Born, which includes higher J, and *not* the author's full Eq75 (needs Born+f2 d-wave).

Executed source conditional point ratios σ_{s,B+FSI}/σ_{s,B}: W=.4 GeV **.752170**; W=.5 **.158228**; W=.6 **.399539**; W=.8 **1.828876**; W=.9 **1.460895**; W=.95 **.0355174**; W=.98 **7.819363**; W=1.0 **8.401711**. These are sharply dependent on model resonance/threshold interference and *not* an experimentally observed factor or a full production enhancement.

## 4. Independent phase/normalization veto (NOT novelty)

Separate I=0 and I=2 reduced photo amplitudes:

F0=(2/3)B−[Jπ T0/3+JK T0_{21}/sqrt(6)]/(8π²);
F2=(1/3)B−Jπ T2/(6·8π²).

In the source elastic region 2mπ < W < 2mK, the source hadron loop satisfies Im(1/T_I)=−ρπ, ρπ=β/(32π), and the photo loop satisfies Im[Jπ/(8π²)]=−2ρπ B. Below 2mK, JK and T0_{21}/T0 are real. Therefore Im(F0/T0)=Im(F2/T2)=0 (Watson/elastic phase; established mature prior art). **ACTUALLY NUMERIC:** maximum relative I0 residual **2.488310301e−18**, I2 residual **1.772268457e−18** over 11 W controls below the model kaon threshold.

**NEGATIVE CONTROL:** double the T0 pion loop coefficient without changing Born — the resulting **nonzero Watson-phase violation** has minimum normalized magnitude **0.00205638677** across all 11 controls. Thus a genuine erroneous isospin/charge factor can be detected. Elastic phase test internal to model does not prove physics/model accuracy; above 2mK it must not be applied as a one-channel identity.

**SECOND algebraic prefactor control:** four neutral-pion FSI-only points from Eq65 with identical π0π0 symmetry factor ε=1/2 exactly reproduce original primary article Eq83. The calculation is a normalization check, NOT a prediction checked against neutral pion measurements.

**Independent numerics:** separately implemented 68-digit mpmath exact complex hadron/photon amplitude agrees with NumPy binary64 to max relative **4.05e−15** on six points. Original R68 conditional thermal integration with Eγ=1436554 MeV, T=.07818527068831995 MeV, unchanged H(W), fiducial z<.6: independent adaptive SciPy and Gauss-Legendre-192 at seven W ranges and two Born/FSI scenarios agree max relative **4.943e−7** (threshold 0.992 GeV split correctly).

## 5. Same-source R68 conditional s-wave fold (not physical pion or neutrino rate)

| W in GeV | K_s(B) | K_s(B+FSI) | relative |
|---|---:|---:|---:|
|.35–.40|2.940891498e−11|2.621614571e−11|−10.856%|
|.40–.54|4.893718123e−11|1.918638885e−11|−60.794%|
|.54–.80|2.759747165e−11|1.901560327e−11|−31.097%|
|.80–.95|3.933856131e−12|6.284491950e−12|+59.754%|
|.95–.992|5.639877329e−13|2.515721838e−12|+346.060%|
|.992–1.05|5.581478068e−13|4.577925040e−12|+720.199%|
|1.05–1.25|8.473178319e−13|8.374359803e−12|+888.337%|

ALL rows: theoretical **leading s-wave** chiral amplitude *only*. Mark II had no reliable pion identification in W=.40–.54 GeV (original DAX ROT005). Near kaon threshold original author uses a single effective mK=.496GeV; physically charged/neutral kaon thresholds differ (DAX ROT010) and this model does not resolve them. The true full charged-pion photo cross section also requires f2 d-wave interference plus higher Born waves, and original ROT011 demonstrated up to ~+20% difference between Born J00+J22 and **exact Born in Belle fiducial support**.

## 6. Repro artifact and explicit HOLD

The originating chat's complete local source package is `DAX9_ROT012_Coherent_Born_FSI_Watson_R68_Repro.zip`: author's independent executed Python `verify_coherent_born_fsi.py` + `verify_quadrature_independent.py`, full scientific report, frozen JSON+CSV, original published-source URLs/receipts, README, execution log, SHA256 manifest. **ZIP SHA256 1155ececfa3c17b08f0d71bf1b7a4cfa7f8fbf34c9f08a4667ed8bf9a5aba4b2**; ZIP CRC PASS, 10/10 member SHA256 PASS, complete clean reexecution byte-identical PASS. This GitHub Markdown report does NOT constitute GitHub upload of code or scientific data.

Full charged f2 photoproduction amplitude and experimental comparison **HOLD**: source paper's explicit product Γγγ^(2) Br Γ=.16 MeV² was for **neutral** π0π0, not validated charged π+π− input; do not silently transplant. Original coherent FSI Eq65 calculation and source model's elastic Watson identity cannot be promoted to full physical pion generation, plasma transport, daughter neutrino spectrum, BBN/PBH, or new physics. No native HEPData, original code, complete covariance, I3/referee acceptance or BW ingestion claimed. No duplicate KN15 BW request, no owner override.

**RETURN: PUBLISHED_COHERENT_CHARGED_S_WAVE_REEXEC_PASS / CHARGE_PROJECTOR_FROM_EQ28_PASS / WATSON_I0_I2_PASS / WRONG_FACTOR_NEGATIVE_CONTROL_FAIL_AS_DESIGNED / NEUTRAL_EQ83_SOURCE_NORMALIZATION_PASS / R68_SAME_SCOPE_QUADRATURE_PASS / F2_CHARGED_AND_FULL_PHOTOPRODUCTION_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
