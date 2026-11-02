# XH-S5 ROT021 — source-native Huntington CAG CTMC: ever crossing vs instantaneous occupancy

artifact_id: IW_XH_S5_ROT021_HD_CAG_FIRST_PASSAGE_VS_OCCUPANCY_20261103
return_id: XH-S5-ROT021-HD-CAG-FIRST-PASSAGE-VERSUS-INSTANTANEOUS-CLASSIFICATION-001-20261103
date: 2026-11-03
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_CODE_READ / EXACT_CLASSICAL_BIRTH_DEATH_FIRST_PASSAGE / SPARSE_MATRIX_ODE_AND_INDEPENDENT_GILLESPIE_REPLAY / NO_CLINICAL_INFERENCE / NO_SOURCE_R_EXECUTION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

## Original 2026 science FIRST
Simpson, Ranum, Leib et al, "Computational modeling and preclinical evaluation support targeting somatic instability for Huntington’s disease treatment", Nature Communications 17:11036, published 2026-10-28, DOI https://doi.org/10.1038/s41467-026-78769-2 . Full Nature text confirmed this turn: authors report preclinical animal experiments and hypothetical MODEL predictions of HD therapy with MSH3, NOT actual human therapeutic efficacy. Authored source software Github commit b9de42ac6f634d137f68e57b059caf08f9ef4d05; README blob 7172479e7ce11576b8f6145022c84373f00d3685, server.r blob 5e60890235717e67b629d061cf122e4c539bd0f6 verified again. Author code explicitly defines birth-death Q and expm(Q) in the RECOMMENDED Handsaker CTMC with p_exp=.676,T1=33.5,T2=72.2. Earlier event-sampling implementation T2=55 is DIFFERENT: ROT021 compares the SAME mathematical CTMC generator at both parameter variants, and never claims these are original authors' two identical algorithms.

Mature theoretical roots: Kolmogorov continuous-time Markov chains, birth-death hitting probabilities, absorbing generators and first-passage flux are all standard, not a new theorem. Original Handsaker et al Cell 2025 DOI https://doi.org/10.1016/j.cell.2024.11.038 supplies the CAG expansion framework. ROT019 already independently established source model strong sensitivity to T2. ROT021 is DIFFERENT endpoint classification audit. No original R/Shiny simulation executed, no model clinical outcome reproduced.

## Exactly specified observational variable
Q has birth intensity b(x)=mu(x)*p_exp/(2*p_exp-1), death d(x)=mu(x)*(1-p_exp)/(2*p_exp-1), with mu(x)=.035(x-33.5)_+ + .576(x-T2)_+. Two functions of SAME process:
A_t={X(t)>=150}, CURRENT marginal.
H_t={at least one s in [0,t] with X(s)>=150}, EVENT EVER hit threshold.
A_t subset H_t, so Pr(H_t)>=Pr(A_t) always. H_t is computed by ADDING ABSORPTION when 150 is first reached, in an independent copy of the generator; before first passage rates are identical. A_t uses ordinary full birth-death chain. These represent distinct scientific endpoints with distinct interpretations. They MUST NOT be conflated with human disease risk, irreversibility of gene expression changes, cell death or clinical diagnosis.

## Source-based independently computed numerical witness

Initial CAG | simulated time years | T2 | ordinary Pr[X_t>=150] | first-pass Pr[ever>=150] | difference | relative gap
55 | 8 | 55 | .5074640723245321 | .5096014891038013 | .002137416779 | .4212 percent
55 | 8 | 72.2 | .0000581312214197 | .0000601735075150 | .0000020422860953 | 3.5132 percent
55 | 12 | 55 | .8232068320096588 | .8238856726089582 | .0006788405993 | .08246 percent
55 | 12 | 72.2 | .0117716135561589 | .0119472772523512 | .0001756636962 | 1.4923 percent
125 | .5 | 55 | .525443563074711 | .562578008832189 | .037134445758 | 7.0673 percent
125 | .5 | 72.2 | .279908778226924 | .308628663788090 | .028719885561 | 10.2604 percent.

Initial state 125 is a HYPOTHETICAL already expanded somatic repeat state, NOT an inherited CAG. Do not interpret probability at .5y as any personal health prognosis. At source genotype55/t8 with T2=72.2 absolute difference is only ~2e-6; quoting relative gap alone would exaggerate practical importance.

## Strong independent exact Fraction proof
From initial x=149, earliest path that reached 150 then ended below is 149->150->149. Therefore
 Pr(H_t)-Pr(A_t) = (b(149)*d(150)/2)*t^2 + O(t^3).
Exactly by fractions.Fraction:
T2=55 => 37466472499443/12390400000 ≈3023.830747953496 yr^-2.
T2=72.2 => 3231137132875431/1548800000000 ≈2086.2197397181244 yr^-2.
This is provably strictly positive, a classical first-passage fact. Standalone standard-library uniformization at t=.0001,.0003,.001 verified short-time ratio ->1; at .0001 ratios .98533 and .98780 for T2 alternatives. Exact source-inspired generator math, NO theorem novelty.

## Independent EXECUTED checks and corrections
Route A independent Python stdlib rot021_exact.py builds rational rates and custom Poisson uniformization, asserts short-time expansion, writes deterministic JSON.
Route B independently coded scipy.sparse expm_multiply computes FULL Q and same Q with absorbing at 150, with upper state cap. Its first-passage CDF is checked AGAINST a separate solve_ivp(DOP853) numerical integral of entrance-flux b(149)*p_unhit_149(t), discrepancy <2.3e-10 in chosen scenarios. Changing high cap 200,220,260 yields negligible effect at tested x125,t.5 scenario.
Route C seeded independent Gillespie experiments THREE x5000 trajectories: x125,t.5,T2=55 observed 2666/5000 CURRENT vs 2852/5000 EVER, generator .52544 vs .56258; T2=72.2 observed 1397/5000 CURRENT vs1545/5000 EVER, generator .27991 vs .30863; x55,t8,T2=55 current 2559/5000, ever 2566/5000. All inside pre-specified conservative binomial fluctuation checks. No experiment with real patients.
Two replay scripts executed from fresh clean ZIP, TWO JSON byte identical, ZIP CRC PASS, all EIGHT content-member SHA256 PASS. SciPy round outputs to 9 significant digits only AFTER full precision computations, to remove adaptive trace estimator differences below scientifically material precision.

Moderator local complete ZIP IW_XH_S5_ROT021_HD_CAG_FIRST_PASSAGE_ENDPOINT_REPRO_20261103.zip
ZIP SHA256 04e37853bcd19dc27031572545b3653ca12006ea13729378d0b7362495b01da1
Full Markdown report SHA256 c3053ad035796e05f74b54aa888a9a348d2247a69aa8a28d3d87106e293c196c
Includes 2 original independent Python sources, 2 frozen JSON, manifest, verified README, replay verifier and complete Polish report, no redistribution of authors' R/Shiny code. Github report != whole ZIP.

## Correct scientific interpretation, hard limits
Question for source-model users, not a clinical recommendation: Does 150 repeat threshold operationally classify present transcriptional state or permanently altered cellular history? The source models currently healthy vs dysregulated repeat-length bands and does not supply evidence that a biological first hit has irreversible consequences. Depending on biology, one endpoint might be more suitable, but this math alone cannot choose. No claim author implementation defect or clinical efficacy. No assigned cross-cell tasks, BW/owner/referee/EXEC ingestion unverified.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_PHYSICAL_CLAIM / NO_CLINICAL_PREDICTION.
