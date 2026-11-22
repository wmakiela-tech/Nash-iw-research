---
artifact_id: IW_DAX_S9_ROT016_BELLE_AUTHOR_POINT_SYSTEMATICS_AND_D0_SCOPE_AUDIT_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: PRIMARY_BELLE_2007_AUTHOR_BIAS_WARNING / SOURCE_TYPED_MARGINAL_ERROR_BOX / ORDINARY_D0_WAVE_SCOPE_COUNTERMODEL
claim_ceiling: NO_PRIMARY_HEPDATA_NATIVE_EXPORT / NO_EXPERIMENTAL_COVARIANCE_OR_STATISTICAL_SIGNIFICANCE / NO_PHYSICAL_D0_FIT / NO_PION_NEUTRINOS_OR_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT016 — Belle author error provenance, native asymmetric angular margins and omitted D₀ wave

**Date 2026-11-22.** This turn follows ROT015 and refrains from further arbitrary tensor phase/width searches. It independently reopens the original Belle experimental author article, verifies the actual angular error channels in SHA-pinned packaged source bytes, and supplies a constructive J=2 helicity-0 counterexample to overextending the prior two-wave no-go.

## 1. Original source contact and scientific firstness

**Original Belle primary author:** T. Mori et al, *High Statistics Measurement of the Cross Sections of γγ→π⁺π⁻ Production*, *J. Phys. Soc. Jpn.* 76 (2007) 074102, DOI https://doi.org/10.1143/JPSJ.76.074102; full article PDF TEXT read at https://hanyang.scholarworks.kr/api/assets/b219502c-147a-4ee3-91e5-6fc988cbc109/download ; specifically Secs 4,5,6.1, Table I, Fig 5, Eqs (3)–(5). The attempted PDF visual web screenshots for pages 4 and 5 failed cache; original PDF native bytes not held or SHA-checked, so no screenshot/byte claim.

**CRITICAL ORIGINAL AUTHOR NEGATIVE KNOWLEDGE ALREADY PUBLISHED IN 2007:** the Belle article explicitly notes apparent systematic angular structure in **0.45<|cosθ*|<0.6 below W=1.1GeV**; the origin of possible experimental bias had not been established. The issue involves angle-dependent μ/π statistical separation using ECL because KLM is ineffective for low-momentum µ; corrections and trigger efficiencies are source-modelled/smoothed and errors are point dependent. Table I gives total systematic 11.1–12.3%, including μ/π discrimination 5–7% and trigger 4–10%. The authors distinguish point-to-point systematics from *overall* errors. These sources were known to Belle in 2007 and discussed in mature Dai–Pennington PRD90(2014)036004; not a new DAX discovery, proof of muon contamination or evidence of an invalid experiment.

**Original source Eq(4)** includes **S, D₀ (J2 helicity0) and D₂ (J2 helicity2)** amplitudes:
dσ/dΩ=|S Y₀₀+D₀Y₂₀|²+|D₂Y₂₂|².
This is a broader leading-S/D class than DAX9 ROT014's Klevansky approximation retaining only (J,λ)=(0,0) and (2,2). Thus an anomalous high-angle source shape does NOT logically require J>=4; the ordinary D₀ wave can produce it. This source issue pre-exists DAX9.

## 2. Actual authentic but SECONDARY Belle numeric source errors

Original packaged official Rivet-data reference BELLE_2007_I749358.yoda.gz re-read from inherited ROT015 and SHA-256 verified exact **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**. MarkII original packed secondary reference SHA256 **ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d** also checked for custody, not used for Bellle uncertainty inference. Both are authentic PACKAGED SECONDARY reference bytes, not original HEPData native CSV/YODA or collider event records. Belle 140×12 angular density y values are nb/unit |cosθ| and must multiply by Δz=.05; source native labels are exactly `stat`, `sys_1`, `sys_2`, each with asymmetric up/down where reported. Recomputed 140 aggregate fiducial source sum guards PASS. Focus original 20×12=240 angular values in W=.85..95GeV.

Original source-positive R68 thermal Eγ=1,436,554MeV,T=.07818527068831995MeV, H(W)=4W³/C²[-ln(1−exp(−W²/C))], C=4EγT, each 5MeV W bin integrated. Original Belle conditional source-central high-angle share z∈[.4,.6] among z∈[0,.6] **Q0=.39519081247603166** reconfirmed exactly.

**Source-typed uncertainty caveat:** YODA `sys_1` behaves as source point-to-point error; YODA `sys_2` ~11.3–13.1% of local y resembles reported overall uncertainty but is not a recoverable correlated 240×240 nuisance model. Fully common multiplicative normalization cancels from Q; **it is improper to assume independent fluctuations of common normalization in all 240 angular bins**. No original full covariance, experimental 1σ joint distribution, detector error response or posterior has been obtained.

## 3. Sharp independent marginal BOX sensitivity — NOT experiment significance

For 240 positive source y_ij, model an expressly ARTIFICIAL independent simultaneous source box: y_ij∈[max(0,y_ij−t d_ij), y_ij+t u_ij]. Its exact MIN high share is attained by setting all high-z cells to their lower bounds and all low-z cells to their upper bounds; MAX vice versa. This follows by elementary monotonicity of H/(H+L); R68 W kernel weights are positive, so no statistical assumptions are made. `t` is the scale of independent per-cell PUBLISHED MARGINAL ERRORS, **not a Gaussian sigma, simultaneous confidence region or a valid experimental nuisance parameter**.

| Artificial declared source margin choice | Q_min at t=1 | Q_max at t=1 | Minimal t allowing Q≤1/3 |
|---|---:|---:|---:|
| Stat ONLY | 37.1931% | 41.8507% | 2.664701 |
| Point sys_1 ONLY | 37.0599% | 42.3081% | 2.505843 |
| sqrt(stat²+point_sys_1²) per cell | **36.0870%** | 43.1946% | **1.800293** |
| stat + point_sys_1, linear per cell | 34.7310% | 44.6183% | 1.291416 |
| sqrt(stat²+point_sys_1²+overall_sys_2²) per cell **UNPHYSICAL INDEPENDENCE** | 32.8579% | 46.6383% | 0.927032 |

The last line is a deliberately over-permissive negative control showing that destroying the overall error correlation can erase apparent 1/3 protection. The opposite ideal common multiplier cancels EXACTLY. The published source DOES NOT supply intermediate real experimental covariance. Independently in each of twenty 5MeV native W rows, source central 20/20 >1/3, but under independent per-cell t=1 combined stat+sys_1 marginal bounds **19/20 still have Q_min>1/3**, one W=.9475GeV can reach ≤1/3. These 20 are correlated W measurements, NOT twenty independent statistical rejections.

For the fixed parameter and exact Born higher-wave ROT015 phase-max benchmarks, minimal t of combined stat+sys_1 per cell to reach model caps: `fixed Γ` high max .3925684974 requires t=.076506; `q⁵` max .3425016128 requires t=1.534040; `q⁵+Blatt` max .3558409490 requires t=1.146296. The almost-zero fixed-Γ gap is plainly not robust even within this artificial model; no experimental p-value or credible interval is asserted.

## 4. Explicit D₀ J=2 helicity-0 existence witness (author Eq4)

Choose D₂=0 and real reduced amplitude A(z)=1+c(3z²−1), with 0≤z≤.6. The root **c=.19867441331723026** gives exactly
∫_.4^.6 |A(z)|²dz /∫_0^.6 |A(z)|²dz = **.39519081247603166**, matching original Belle central high share to arithmetic precision, despite having ONLY J=0 and J=2. With standard Belle source spherical harmonics, real D₀/S=2c/√5=**.177699797427**. This is a mathematical existence result, NOT a source-determined fit, physical phase, test of gauge-invariant full production or unique explanation. Original twelve-cell source shape remains different: TV12=**.060821071756**. The primary experimental authors themselves supply the S+D0+D2 class and acknowledge potential bias.

**Scope correction:** ROT014 1/3 was rigorously true for narrow class (S,D₂). ROT015 correctly showed exact Born higher-J can evade the bound. The present stronger scientific guard is that even WITH ALL J>2 set to zero, the ordinary **D₀** term permitted by published Belle Eq4 can evade the same bound. No high-angle anomaly logically establishes higher-J pion dynamics or new physics.

## 5. Executed verification, reproducibility, next original-source gate

Original independent executable `verify_rot016_belle_uncertainty_and_D0.py` re-parses actual source YODA, validates two SHA-256 source bytes, recreates R68 bin weights, computes exact partial-bin uncertainty box extrema and t roots, and emits frozen JSON+three CSV. Second independently coded `independent_check_rot016.py` checks Eq4 witness against adaptive SciPy integration and exact common nuisance cancellation. Two separate clean directories independently reexecuted BOTH scripts, yielding **2×4/4 byte-identical files PASS**, ZIP CRC PASS and **12/12 member SHA256 PASS**, manifest included (13 members). Archive in originating conversation `DAX9_ROT016_Belle_Author_Systematics_And_D0_Countermodel_Repro.zip`, SHA256 **5c73821ffc98df78ff0faa548c8a8259cfbec2e3db808016e7327151f3cbe138**. This public GitHub Markdown report is TEXT ONLY, not uploaded executable source or native data.

**Next scientifically justified gate:** retrieve original Belle angular-correction systematic covariance or source-validated helicity-0 D₀ strong amplitude and its correlation/phase from mature coupled-channel solution; not another arbitrary independent error-vector model or free tensor-resonance parameter scan. No original HEPData native bytes, experimental significance, complete source support, real pion stopping / daughter neutrinos, PBH/BBN inference, scientific novelty, independent referee/I3 or BW ingestion claimed.

**RETURN: ORIGINAL_BELLE_AUTHOR_POINT_BIAS_DISCLOSURE_PASS / AUTHENTIC_SECONDARY_240_NATIVE_ERROR_FIELDS_PASS / SHARP_SOURCE_MARGINAL_BOX_AUDIT_PASS / ORDINARY_J2_D0_CONSTRUCTIVE_SCOPE_COUNTEREXAMPLE_PASS / NO_EXPERIMENTAL_COVARIANCE_OR_PHYSICAL_FIT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**