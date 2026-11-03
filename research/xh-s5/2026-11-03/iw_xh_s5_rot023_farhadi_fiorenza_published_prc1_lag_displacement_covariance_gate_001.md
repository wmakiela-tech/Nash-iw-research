# XH-S5 ROT023 — primary published PRC1 displacement aggregates: independent drift-fit and lag-covariance gate

artifact_id: IW_XH_S5_ROT023_PRC1_SHEPHERDING_LAG_COVARIANCE_20261103
return_id: XH-S5-ROT023-FARHADI-PRC1-SHEPHERDING-PUBLISHED-AGGREGATES-AND-LAG-COVARIANCE-GATE-20261103
date: 2026-11-03
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_PUBLISHED_12_EXTENDED_DATA_AGGREGATES / ORIGINAL_AUTHOR_PINNED_CODE_READ / TWO_INDEPENDENT_EXECUTED_FIT_AND_COVARIANCE_CHECKS / NO_AUTHOR_RAW_TRAJECTORIES / NO_CYLAKS_EXECUTION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

## ORIGINAL SCIENCE FIRST; exact source and access level

Leila Farhadi, Shane A. Fiorenza, Sithara Wijeratne, Konstantinos Nakos, Yang Yue, Morgan Pimm, Jakia Jannat Keya, Kristen Verhey, Radhika Subramanian, Meredith Betterton, "Motors use biased diffusion to shepherd diffusible proteins on microtubules", Nature Physics, PUBLISHED 2026-10-30, DOI https://doi.org/10.1038/s41567-026-03489-9. The original authors describe and experimentally establish that active K401 motors can rectify Brownian diffusion of passive MAP PRC1 on microtubules into directed drift WITHOUT detected direct motor-to-MAP binding. They demonstrate roles of the number of motors, accessible protofilaments and lateral diffusion. ALL physical discovery priority belongs to the authors.

Primary source read: publisher Nature Physics original Extended Data Fig.7(A-C) caption, including six LAG DELAYS, 12 aggregate mean displacements with marginal SEM and displacement N, source reported slopes and confidence intervals. The original raw laboratory trajectories (136 control and 157 motor condition tracks) and Colorado Scholar underlying dataset https://scholar.colorado.edu/concern/datasets/r781wj02j were NOT downloaded or inspected. Our CSV is manually and independently authored TRANSCRIPTION of publisher's numbers, not author-supplied CSV or raw micrographs. No original physical model or authors' software calculations were executed. This bounded access is essential to avoid FM-DATA-ACCESS-OVERCLAIM.

## Original author program provenance
Author code: https://github.com/Betterton-Lab/CyLaKS, pinned commit 863a148358f2f646017d6ae5f29a00666f61885d dated 2026-06-15.
Actual source files READ through authenticated GitHub:
README.md Git blob 7b774edf3a08fc6ad44fd8fec91fe40ef0d9603c;
params/shepherding.yaml Git blob 9eea283dfc7321826b2f19e92ccf0f95eee3f3b4;
scripts_shepherding/launch_batch_Fig2d.sh Git blob 1b59d7b8bc09c3183da737e6bbbdc9fb02a460fe.
Original supplied shepherding config uses 8 modeled accessible subfilaments, 1000 sites about 8 micrometres, motor concentration 100 nM, MAP 0.1 nM; its dt field 5e-5s carries explicit comment 5e-6s used in publication simulations. Figure-2d launcher varies 3 motor concentrations x 5 processivity-time multipliers with only one ACTIVE seed index in the visible script; DOES NOT imply all published simulations or biological experiments had one repeat. Do not equate code DEFAULT configuration with full experiment, or the biological microtubule's 13 protofilaments. CyLaKS was NOT compiled/run and its source is NOT copied into our ZIP.

## Actual published source aggregates, 12 observations, no source fitting assumptions inserted
Delays t in seconds: 0.17,0.83,1.16,1.66,2.49,3.32.

PRC1 only: mean displacement in micrometres = [-0.00038,0.00185,-0.00038,-0.00127,0.00368,0.001816].
Marginal SEM = [0.00052,0.00157,0.00188,0.00229,0.00288,0.00342].
Displacement records N = [11943,11515,11301,10980,10445,9910], sourced from 136 TRACKS.
SOURCE authors report fit velocity 0.00063 micrometres/s, 95pct CI [-0.00031,0.00160].

PRC1 + 100 nM K401: means [0.006863,0.04876,0.06807,0.09648,0.14030,0.18690].
Marginal SEM [0.000435,0.001352,0.00161,0.001956,0.00236,0.00276].
Displacement N [20316,19728,19434,18993,18258,17523], sourced from 157 TRACKS.
SOURCE authors report fit velocity 0.05676 micrometres/s, 95pct CI [0.05598,0.05755].

Our full local CSV source transcription SHA256 583587ef067f89a36d38ad1eec874ae66da642a6d98c971fea62c687475fd90a.

## New independent math on source-published aggregates

Single-parameter linear kinematic fit THROUGH ORIGIN, v=sum(t_i*y_i)/sum(t_i^2). Route A computes EXACT FRACTION arithmetic, Route B separately NumPy least squares. Numerical results:
  PRC1 alone v=0.0006403475262572874 micrometres/s versus SOURCE 0.00063.
  PRC1+K401 v=0.05673890207109317 micrometres/s versus SOURCE 0.05676.
  Point-velocity difference 0.05609855454483589 micrometres/s.
The close quantitative match shows source-published mean displacement lag pairs are numerically compatible with the reported drift. It does NOT prove that source actually used through-origin fitting or reproduce source uncertainty method.

Alternative fit and model sensitivity:
free-intercept unweighted OLS velocities control 0.00084764515 and K401 0.05650069 micrometres/s;
zero-intercept WLS with weights 1/SEM^2 yields 0.0004954101973 and 0.0565494990708 micrometres/s;
leave-one-lag-out through-origin slopes control [0.0003125367707,0.0008411544185] and K401 [0.0565414997485,0.0571827563050] micrometres/s.
For every one-point omission source +K401 fit drift remains strongly positive. The control's very small fitted positive point slope alone does not establish experimental significance.

## Fundamental statistical IDENTIFIABILITY gate, not accusation of author error

The data caption reports N=9910–11943 displacement RECORDS at each lag from 136 PRC1 trajectories; with motors, 17523–20316 records per lag from 157 tracks. Their across-lag record sums are 66094 and 114242 respectively. Those sums are NOT independent biological track or experimental replication counts. Six lag-derived mean displacement statistics may be correlated because they are derived from overlapping time intervals on the SAME tracks. The supplied six marginal SEM values determine only covariance matrix diagonal, not off-diagonal covariance.

Mathematically exact for a through-origin slope: set weights a_i=t_i/sum_j(t_j^2). The variance is a^T Sigma a, with Sigma the SIX-BY-SIX lag-mean covariance matrix. To demonstrate nonidentifiability, construct two HYPOTHETICAL positive-semidefinite covariance matrices with IDENTICAL SOURCE marginal SEMs but different between-lag correlations:
 Sigma_ij=SEM_i*SEM_j*rho^abs(i-j) for rho=0 versus rho=0.8.

For PRC1 without K401, implied conditional slope SE under rho0 0.0006436334169, under rho0.8 0.0010381199535 micrometres/s, ratio ~1.61.
For PRC1+K401, implied conditional slope SE under rho0 0.0005247753690, under rho0.8 0.0008540709791 micrometres/s, ratio ~1.63.
These are illustrative model SEs, NOT real measured covariance or an alternative scientifically validated CI, NOR evidence the author's stated CIs are wrong. The real source authors may have used track-level/hierarchical inference that is inaccessible from reported aggregates.

Independent B route seeded with 20261103 sampled 120000 hypothetical six-dimensional Gaussian vectors for rho0 and rho0.8 PER condition; verified empirical slope SE vs exact quadratic form within 1.2pct. This simulation concerns the SIX source mean estimates under chosen artificial covariance, NOT synthetic molecules, raw trajectories or real biology. Route A pure stdlib exact Fractions; Route B independent NumPy implementation; no cross-script scientific imports.

A concrete source-native future reviewer falsifier if actual original trajectories become accessible: compute lag-mean cross-covariance and re-evaluate slopes and 95pct CIs with track-cluster and independent-experiment-cluster bootstraps compared with a naive displacement-row bootstrap. Observe whether very strong drift signal and uncertainty survive. NOT EXECUTED, no automatic cross-cell task, no accusation of original pseudoreplication.

## Mature host subtraction and claim ceiling
Standard Brownian ratchet/active matter literature: Bechinger et al, RMP 88:045006 (2016) DOI10.1103/RevModPhys.88.045006; Cates and Tailleur, Annual Review of Condensed Matter Physics 6,219 (2015) DOI10.1146/annurev-conmatphys-031214-014710. Ordinary OLS/WLS, regression sensitivity, covariance and clustered trajectories are MATURE statistical tools, no theorem or new biophysics. NASH public code search shepherding, CyLaKS, Farhadi, microtubule found zero indexed hits, NOT proof of no private BW prior art.

## Reproduction and custody
LOCAL complete original XH reproducibility ZIP:
IW_XH_S5_ROT023_PRC1_SHEPHERDING_PUBLISHED_AGGREGATES_COVARIANCE_REPRO_20261103.zip
ZIP SHA256 925c5d08fe8ae7983dad68df2d61a6f0d0bc6c5fa0b8cb7e9bf6ec141fd467f2
FULL local Polish report SHA256 6f01953a53d85f24c2c581f5751ee7121417aaaf47c5c2205af99e9f4674cc8f.
10 ZIP members: full independent report, manual source text aggregate CSV, two XH original runnable Python scripts, two frozen deterministic JSON, source_locator.json, README, replay verifier and SHA256 manifest.
ZIP CRC PASS, all NINE scientific content-member SHA256 checks PASS, clean temp EXTRACTION and standalone rerun both programs yielded TWO JSON BYTE_IDENTICAL PASS. Runtime Python3.13, NumPy2.3.5. The present GitHub text is standalone substantial science; it is NOT remote storage of the original local ZIP, raw experimental source tracks, or author CyLaKS source.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_SOURCE_RAW_TRACK_REPLAY / NO_AUTHOR_CYLAKS_EXECUTION / NO_PHYSICAL_UPGRADE / BW_INGEST_UNVERIFIED / NO_TASK_CASCADE.
