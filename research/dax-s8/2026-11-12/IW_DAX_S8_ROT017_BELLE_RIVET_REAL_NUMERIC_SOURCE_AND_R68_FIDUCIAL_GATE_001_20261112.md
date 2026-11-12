---
artifact_id: IW_DAX_S8_ROT017_BELLE_RIVET_REAL_NUMERIC_SOURCE_AND_R68_FIDUCIAL_GATE_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_PACKAGED_RIVET_BELLE_REFERENCE_BYTES / REAL_140x12_NUMERIC_ANGULAR_CLOSURE / CONDITIONAL_R68_FIDUCIAL_HADRON_RATE
claim_ceiling: NO_ORIGINAL_HEPDATA_BYTE_EQUALITY / NO_FULL_PI_PI_QCD_RATE / NO_ALL_SM_CHANNELS / NO_NEUTRINO_TRANSPORT / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT017: real Belle/Rivet numerical reference and conditional R68 pion-fiducial convolution

**12 November 2026.** First actual 140-energy x 12-angle **numerical source reference** verification in DAX-S8 lineage, not first discovery in physics. Scope inherited: DAX-S7 R68 FIRST 3 named gamma-gamma channels, DAX-S8 ROT012 pion point-Born conditional branch, ROT013-015 Belle fiducial/point-source identifiability, ROT016 fitted Belle f0 benchmark. Preserve old ceilings and precedence.

## Native source acquisition and access failures

Primary HEPData DOI 10.17182/hepdata.51842.v1 at https://www.hepdata.net/record/ins749358: source record and table inventory READ; actual bytes NOT READ. Native Ubuntu GitHub Actions run 43308798900 tested 3 individual CSV tables, submission CSV, submission YODA and record JSON: **6/6 HTTP 403**. This is an access blocker from that runner, NOT proven HEPData provider outage.

A separate independently released **Rivet-data 4.1.2-2.1** package was downloaded in native GitHub Actions run **43309487872**. Its publicly published openSUSE SHA256 is 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b, from https://tumbleweed.opensuse.org/download/slowroll/repo/oss/noarch/Rivet-data-4.1.2-2.1.noarch.rpm.mirrorlist . The runner downloaded the exact RPM through a second mirror (first URL 404), and confirmed the published whole-RPM digest via SHA256 check PASS.

The RPM contains **usr/share/Rivet/BELLE_2007_I749358.yoda.gz**, compressed 29,215 bytes, decompressed 255,574 bytes. Extracted original-package file SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**. GitHub Actions original artifact ID **13985880814**, archive SHA256 **666655df8b8534e45a4ca64bc91d4ad09b6f8a15336a4ca5b0c4200efeb8275c**. Verified download and unpack of the original artifact ZIP in the analysis runtime, CRC and YODA SHA PASS. All bytes preserved in full ROT017 local package. Run URL: https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 .

This is a source-pinned SECONDARY PACKAGED Rivet reference, NOT authenticated byte equality with the original HEPData tables. Native workflow first attempt run 43309081865 failed due author Python here-document indentation error; it was corrected and rerun successfully. Native run initial parser misleadingly returned zero objects because it only knew old YODA2 type syntax; original file is **YODA_BINNEDESTIMATE<S>_V3** and was parsed successfully using a separate local YODA3 parser. Failures are not suppressed.

## 141 numerical tables: exact real-data internal angular closure

The Rivet reference contains 141 YODA V3 objects. Table 1 has 140 source y-values with statistical and systematic error columns at W centers 0.8025, 0.8075,...,1.4975 GeV. Tables 2..141 each contain 12 differential-angle values at z=|cos(theta*)|=0.025,0.075,...,0.575 with three uncertainty labels. Source Rivet validated C++ https://heprivet.org/analyses/BELLE_2007_I749358/ verifies fiducial |cos(theta*)|<=0.6 and crossSection()/nanobarn/sumOfWeights normalisation, with differential angular histogram divided by its z-bin width. Thus reconstructed Table1 y units are nanobarn and each angular-table y is nanobarn per unit z, NOT unrestricted total pion cross section.

The packaged YODA blocks are stored in LEXICOGRAPHIC, not NUMERICAL, table-ID order. An initial wrong index alignment generated a false discrepancy up to nearly 9x; a negative control identified and corrected this by sorting numeric IDs d01..d141. FULL source-byte-specific rerun then verified:

For each i=1..140: sigma_fid,reco(W_i) = 0.05 * sum_(j=1)^12 [d sigma/dz](W_i,z_j).

**140/140 PASS at tolerance relative < 6e-5**, with maximum absolute relative discrepancy **5.863726984871584e-5** at W=0.9025 GeV. Exactly 17/140 are nonzero at original decimal precision, consistent with source rounding; median absolute discrepancy is zero. This is actual 140x12 source-number cross-validation, not an invented Born fixture.

Examples source Table1: W=0.8025GeV sigma=109.74nb, W=1.1475GeV sigma=185.23nb, W=1.1525GeV sigma=190.32nb, source maximum at W=1.2475GeV sigma=308.21nb, W=1.4975GeV sigma=25.07nb. The packaged Table1 has 140 numeric positions even though original HEPData abstract describes low-W total+differential and high-W differential; the representation difference remains an **OPEN PRIMARY_SOURCE_SEMANTICS_CHECK**, not evidence the primary HEPData Table1 has 140 source rows.

## Actual source-valued fiducial R68 convolution — reconstruction assumptions declared

Inherited fixed R68 E_gamma=1,436,554 MeV, Planck T=0.07818527068831995 MeV and incident isotropy. For unpolarized invariant-W cross section in a declared final-state angular acceptance,

K_fid = integral_800^1500 dW H(W) sigma_fid(W), 
H(W)=4W^3/C^2 *[-ln(1-exp(-W^2/C))], C=4E_gamma*T.

Source nbs converted using (hbar c)=197.3269804 MeV fm and 1 fm^2=10^7 nb, so 1 MeV^-2=389379371937.8198416 nb.

**Conditional numerical reconstruction:** treat each real Rivet Table1 source y(W_i) as a constant cross section over the W_i-centered 5MeV interval [W_i-2.5MeV,W_i+2.5MeV] across 800..1500MeV. Exact mpmath per-bin integral of H gives:

K_fid(constant) = **3.8868646699147836641883858195704408e-10**.

Independent arithmetic:
- reconstruct 140 y values from all 140x12 angular data first: K_fid(angular) = **3.8868446832698009699366581681852635e-10**, ~5.1421e-6 below Table1 K, source-number rounding scale;
- independently coded SciPy integration = **3.886864669914784e-10**, relative ~1e-15 agreement;
- piecewise LINEAR across W centers with constant edge extensions gives **3.886862791890122e-10**, -4.832e-7 relative to piecewise constant (NOT proven general interpolation uncertainty).

Under the **extra assumption** that source numbers are actual 5MeV BIN AVERAGES and nonnegative integrated bin areas, exact strictly decreasing H for W>=800MeV and ROT014 source-independent positivity yields the sharp bound

**3.86481057910705e-10 <= K_fid <= 3.90891706381247e-10**.

This is **conditional on bin-average semantics**, NOT an experimental 68/95% confidence interval. Original HEPData bin/point semantics and correlated statistical/systematic errors were not verified; a finite set of points alone does NOT imply a physical integrated bound (ROT015).

## Quantified model discrepancy, not a full physical pion hazard

ROT013 pion point-scalar Born model restricted to THE SAME Belle W and z support yielded K_Born,fid=1.77923637803288135e-10. Real Rivet-source-valued fiducial K divided by that is **2.18456901955438**. Thus the point-pion Born source substantially underestimates this restricted measured-reference numerical proxy in the explicitly chosen reconstruction. The full pion cross section beyond Belle W/z window is OPEN.

For a strictly conditional four-channel R68 first-event denominator test, hold three previously published scalar source rates K_e=5.983877841687106e-8, K_mu=9.433089008347292e-9, K_DPP=3.978875327380886e-8. Three-channel P_first_mu=0.0864939970805744. Add ONLY recovered fiducial charged-pion W+z source model K_fid: P=**0.0861868316264320**; relative decrease **0.3551292%**. This is NOT a fully physical muon probability or even a full charged-pion hazard, and not a PBH/BBN prediction. Unknown off-acceptance hadronic contribution and other channels can change total. Do not incoherently add f0 resonant amplitude on top of the already measured pi+pi- total (ROT016).

## Reproducibility, provenance and admission

Local full original research bundle includes SHA-pinned compressed original Rivet YODA bytes, GitHub original run artifact, native source access receipts, two **executed** original numerical programs, 140 energy reconstructed CSV, all 140 angular-closure CSV, frozen results JSON, full report, source audit, README and SHA manifest. ZIP CRC PASS, SHA256 14/14 payloads PASS, clean reexecution of two programs generated FOUR byte-identical frozen data files PASS. Local ZIP SHA256 **9e8129e46d5123a580b4f19a5017e343f36d8a6a8b8658ab45c2cf6d0c35359b**.

Original source YODA and the code are downloadable together from this conversation; GitHub Actions artifact separately provides exact raw source bytes. The original HEPData CSV/YODA remains HTTP403 in tested runners, and BW INGEST is NOT confirmed. Source owner XH-S6 has not accepted a new pion task. This rotation calls for a source-semantic reconciliation and independent review, not automatically another owner task or unbounded follow-up.

**DISPOSITION: REAL_RIVET_REFERENCE_BYTES_PASS / REAL_140x12_ANGULAR_CLOSURE_PASS / FIDUCIAL_R68_SOURCE_CONDITIONAL_QUADRATURE_PASS / HEPDATA_PRIMARY_BYTE_IDENTITY_OPEN / PHYSICAL_HADRONIC_QCD_RATE_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.**
