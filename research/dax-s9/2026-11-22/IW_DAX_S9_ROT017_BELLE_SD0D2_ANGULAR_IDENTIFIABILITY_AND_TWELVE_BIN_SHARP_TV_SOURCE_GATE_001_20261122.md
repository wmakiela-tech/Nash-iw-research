---
artifact_id: IW_DAX_S9_ROT017_BELLE_SD0D2_ANGULAR_IDENTIFIABILITY_AND_TWELVE_BIN_SHARP_TV_SOURCE_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_NATIVE_BELLE_12_ANGLE_SD0D2_SHARP_TV / PRIMAL_DUAL_CERTIFIED_GLOBAL_MODEL_MINIMUM / FULL_ANGULAR_HELICITY_AMBIGUITY / ARTIFICIAL_MARGINAL_ERROR_BOX
claim_ceiling: NO_PRIMARY_HEPDATA_BYTES / NO_ORIGINAL_DETECTOR_COVARIANCE / NO_EXP_STATISTICAL_REJECTION / NO_HADRONIC_PHYSICAL_FIT / NO_PION_NEUTRINOS_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT017 — Belle S+D0+D2 12-bin sharp TV bound, dual certificate and exact helicity decomposition non-identifiability

**22 Nov 2026.** Bounded original mathematical-source diagnostic of a mature published partial-wave ambiguity. A FULLER report and independently executing 12-member reproducibility ZIP with authenticated SECONDARY source bytes are available in originating user conversation. THIS GitHub text is a public report only, NOT an upload of executable/data files; no BW writes or scientific novelty asserted.

## 1. Actual original and packaged SECONDARY sources

- Original Belle authors, T. Mori et al, *High statistics measurement of the cross sections of gamma gamma -> pi+ pi- production*, JPSJ 76 (2007) 074102, DOI https://doi.org/10.1143/JPSJ.76.074102 ; original arXiv https://arxiv.org/abs/0704.3538 . Original author PDF TEXT actually read in predecessor ROT016 and source-derived report/code re-opened now (no new native author-PDF SHA or visual PDF screenshot). Author Eq(4): `dσ/dΩ=|S Y00+D0 Y20|²+|D2 Y22|²`. Authors already noted potential angular point-specific systematic structure in 0.45<|cosθ*|<0.6, W<1.1GeV; possible muon/pion separation and trigger nuisance not causally established.
- Belle official packed SECONDARY Rivet `BELLE_2007_I749358.yoda.gz` actual compressed bytes SHA256 `28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403` reopened and checked, along with independent authentic MarkII packaged SECONDARY `MARKII_1990_I304882.yoda.gz` SHA256 `ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d` custody only. Belle 140×12 original angular **density** records (multiply .05 for bin-integrals), original 20×12 native source data in W=.85–.95GeV. Source reported asymmetric labels `stat`, `sys_1`, `sys_2`; original author 12×20 covariance, primary HEPData numeric export and detector-level event records NOT READ.
- Mature prior art explicitly discusses non-identifiability without polarization/additional constraints: Belle review *Physics achievements from the Belle experiment*, PTEP (2012), article 04D001, DOI https://doi.org/10.1093/ptep/pts072 , Sec10.6 Eq10.1–10.2, full original review HTML read this rotation. Dai/Pennington, PRD90 036004 (2014), DOI https://doi.org/10.1103/PhysRevD.90.036004, applies hadronic coupled-channel unitarity/analyticity/crossing to reduce solution space. None of this fundamental nonidentifiability is novel DAX science.

## 2. Angular polynomial class / scope of mathematical theorem

From author Eq(4), with z=|cosθ*|, Y00 constant, Y20∝(3z²−1), Y22∝(1−z²), the **unpolarized** differential rate at a given W has the form
 `I(z)=|S+D0(3z²−1)|²+|D2|²(1−z²)²=a+b z²+c z⁴`.
Here S,D0,D2 are reduced complex coefficients after known spherical normalization; physical admissibility requires a nonnegative Gram decomposition. ANY positive energy-band mixture with W-varying amplitudes remains a quartic polynomial in z. The previous ROT016's single-bin 39.5191% high-angle existence witness is NOT claimed to fit the full twelve-bin angular distribution.

Original **unchanged** R68 kernel integrated over source W=[.85,.95]GeV: Eγ=1,436,554MeV, T=.07818527068831995MeV, `H(W)=4W³/C²[-ln(1−exp(−W²/C))]`, C=4EγT. Native 20 W bins ×12 angular bins, source y densities in nb/unit z; 0.05 finite bin width. Reproduces original Belle high-z [.4,.6] share 0.39519081247603166.

## 3. NEW original exact sharp 12-bin geometry result

Let `p_j` be the 12 source-central normalized Belle native angle-bin masses, and `G_jk=∫_{.05j}^{.05(j+1)} z^(2k)dz`, k=0,1,2. Minimize `TV12=.5 Σ_j|p_j−(Gθ)_j|` subject to `Σ_j(Gθ)_j=1, (Gθ)_j≥0`. This is a genuine FINITE LINEAR PROGRAM (3 free real polynomial coefficients + 12 absolute-residual auxiliaries). Actually executed SciPy HiGHS yields **SHARP PRIMAL min TV12=0.04480614538458212**, i.e. **4.4806145%** of normalized published 12-bin source-central masses.

An INDEPENDENT dual program with `|λ_j|≤1`, `G^T λ=μ G^T 1` yields for every normalized model in this class `TV(p,p_model)≥(λ·p−μ)/2=0.04480614538458227`. Primal–dual gap **1.46×10^-16**; full 12 dual λ and μ frozen in original JSON. **Physical sharpness separately verified:** primal polynomial has positive a,c and b²<4ac. Therefore a real-positive u and complex v exist with `I(z)=|u+v z²|²` and D2=0, which reproduces all 12 optimum masses. This proves 4.4806% is EXACT minimum over the physically allowed author `S+D0+D2` wave-set as well, even with positive W mixtures and fully freely chosen helicity phases. It does NOT reject a full model containing J≥4, experimental measurement uncertainty or detector migration.

The 20 individual native Belle 5MeV W-bin quartic class TV minima range **3.3948%–6.1495%**, median **4.8094%**; these are descriptive correlated source W rows, NOT 20 independent statistical tests.

**Source-localization negative control:** omit the final Belle angle cell z=.55–.60, renormalize the 11 remaining central probabilities onto z∈[0,.55], and resolve the same primal LP. Exact TV drops to **0.012661894568505624 (1.26619%)** from 4.48061%. This localizes much of the central-shape mismatch to source endpoint and is compatible with, but does NOT prove, the original author-recognized detector correction/bias warning.

## 4. Stronger source-class non-identifiability even with perfect FULL angular acceptance

For ONE best source-central quartic fit `I(z)=a+bz²+cz⁴` (a≈1.59419056,b≈−3.37430708,c≈18.41793831), introduce arbitrary **D2 intensity coefficient** `w≥0`. Exact identity for **all** 0≤z≤1:
`I(z)=|u(w)+v(w)z²|²+w(1−z²)²`, with
`u(w)=sqrt(a−w)` real, `Re v(w)=(b+2w)/(2u(w))`,
`Im v(w)=sqrt(c−w−(Re v(w))²)`.
This is valid for `0≤w≤w_max=min(a,c,(4ac−b²)/(4(a+b+c)))=1.5936711293814578`; source exemplar satisfies a+b+c>0. Set `S(w)=u+v/3, D0(w)=v/3, |D2(w)|=sqrt(w)`. Numerically checked `w=0,.5,.99 w_max` at 1001 grid z points from 0 to 1 and by adaptive integration over all 12 native angle bins. The different PHYSICAL complex amplitude tuples give the SAME exact entire continuous unpolarized angular function, not just the restricted Belle bins. In THIS one fitted example, the D2 component share of integrated |z|<.6 intensity can range **0%–75.14988084%** while observable intensity is unchanged. **NOT** an experimental confidence range for genuine Belle D2; it is an exact constructed non-identifiability witness. Additional polarization, coupled-channel dispersive/hadronic phase and independent channel data are required for separation.

## 5. SOURCE-MARGINAL errors, no Gaussian inference

Read all native 240 Belle W×angle central values and original SECONDARY asymmetric `stat` and `sys_1` error bands. Under an EXPRESSLY ARTIFICIAL independent simultaneous marginal box `y_ij±t sqrt(stat_ij²+sys1_ij²)` with correct up/down asymmetries, positive R68 W weights and free total amplitude normalization, an independently solved LP over (a,b,c,t) yields the SHARP minimum **t=1.9108838410850555** before all 12 model bin-integrated predictions may simultaneously fall in their hypothetical marginal intervals. At t=1 NO feasible quartic angular model. The optimum is physically reachable by complex S+D0 alone, not an unphysical unconstrained polynomial. A truly common source `sys_2` normalization is not given 240 independent fluctuations (source-covariance destruction), and the actual Belle joint uncertainty structure was not retrieved.

**Critical language restriction:** t=1.9109 is NOT '1.91 sigma', nor a confidence interval, p-value, experimental incompatibility, exact detector likelihood or demonstration of real experimental error. It is a precise robust-arithmetic test of stated independently movable marginal boxes.

## 6. Reproducibility, integrity and next gate

Full *local* ORIGINAL implementation `verify_rot017_SD0D2_identifiability.py` + `independent_check_rot017.py`, actual source SHA-pinned compressed YODA files, frozen `results_rot017.json`, original 12-angle and twenty-5MeV-row CSV, full original ~12kb scientific Markdown report, original source receipt, README, execution log and SHA manifest. ZIP in originating conversation: `DAX9_ROT017_Belle_SD0D2_Identifiability_Sharp_TV_Repro.zip`; **ZIP SHA256 028591e08f2b4542d4692015a6f789a0f5c2cad591d7bc6a56a90a90dbae4655**, ZIP CRC PASS, **11/11 SHA256 member digests PASS**, 12 archive members including manifest. Replayed in TWO fresh isolated directories: both independent numerical verifier and independent quadrature checker PASS, frozen **2×3/3 files BYTE-IDENTICAL PASS**. No raw detector data, native HEPData or author-native numerical fitted amplitudes in ZIP.

Decision: do NOT infer true helicity amplitude fractions or the cause of Belle angular anomaly from unpolarized 12-bin source data alone. To advance physics, obtain independent **helicity0 D0 hadronic coupled-channel phase/amplitude** constraints, detector covariance and/or polarized measurements, with real measured angular/source support. Do not invent them from source residuals or saturate arbitrary nuisance boxes. No BW write, no I3 independent signoff, no physics novelty/canon or exec sign, no neutrino/PBH/BBN claims.

**RETURN: ORIGINAL_BELLE_AUTHOR_SD0D2_SOURCE_PASS / NATIVE_SHARP_TV_PRIMAL_DUAL_PASS / EXACT_PHYSICAL_ATTAINABILITY_PASS / CONTINUOUS_IDENTICAL_INTENSITY_MULTIPLE_D2_FRAC_PASS / MARGINAL_SOURCE_BOX_SHARP_TMIN_PASS / NO_EXPERIMENTAL_LIKELIHOOD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
