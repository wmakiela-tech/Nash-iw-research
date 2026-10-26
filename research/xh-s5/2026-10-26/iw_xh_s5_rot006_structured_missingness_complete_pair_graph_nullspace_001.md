# XH-S5 ROT006 — Pairwise-complete site network does not identify three-way dependence

artifact_id: IW_XH_S5_ROT006_STRUCTURED_MISSINGNESS_PAIRWISE_TRIPLE_NULLSPACE_001_20261026
return_id: XH-S5-ROT006-STRUCTURED_MISSINGNESS_COMPLETE_PAIRWISE_THREE_WAY_NULLSPACE_001_20261026
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
date: 2026-10-26
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_FINITE_DISTRIBUTION_WITNESS / PRIOR_ART_MATURE / NO_AUTHOR_REPLICATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## 2026 source, exact evidence boundary
B. Rehák Bučková, C. Fraza, C. K. Lemvigh et al., "Structured missingness in biomedical research", Communications AI & Computing 1, 19, published 9 Oct 2026, DOI https://doi.org/10.1038/s44488-026-00025-9 . Source studies site-design deterministic missing blocks, 40-variable Gaussian synthetic datasets, and real cognitive test batteries, compares Extra Trees, AutoComplete, MICE and site-hierarchical MICE with accuracy, Jensen-Shannon and multivariate-correlation metrics. Authors THEMSELVES stress missing empirical bridges and irrecoverable relations without assumptions. Their code/figure data: https://github.com/bbuckova/The-Art-of-Not-Knowing-Accommodating-Structured-Missingness-in-Biomedical-Research ; NOT CLONED, NO AUTHOR DATA OR EXPERIMENT REPRODUCED.

Mature PRIOR ART: pairwise independence does not imply mutual independence, XOR construction (Kevin Murphy *Probabilistic Machine Learning* public solutions https://probml.github.io/pml-book/solns-public.pdf); classical missing-data theory Rubin 1976 DOI 10.1093/biomet/63.3.581; finite loglinear three-way interactions and marginalization rank. No novel math.

## Exact new-to-cell SOURCE-MOTIVATED countercontrol
Three independent same-population site cohorts, site A only sees XY, B only YZ, C only XZ. Complete pairwise overlap graph but no subject has XYZ jointly measured. On {0,1}^3 define P_theta(x,y,z)=[1+theta*(-1)^(x+y+z)]/8, |theta|<1. All cells strictly positive. Each of the 3*4=12 observable pair margins is EXACTLY 1/4 regardless of theta, even for unlimited subjects. Hence pair-only likelihood constant in theta and Fisher info exactly 0.

Models theta+=3/5 and theta-=-3/5 reproduce ALL observations equally. Yet conditional P(Z=X XOR Y | X,Y)=(1+theta)/2 equals 4/5 versus 1/5 for EVERY (X,Y). Under matching world the best prediction is 80% accurate and under wrong-sign world 20%; paired observables cannot select. Any distribution-matching criterion restricted to observed pair margins is equally perfect, even if the missing conditional is wrong. This is classical EXACT structural nonidentification, NOT an empirical finding that the source's hierarchical MICE fails.

Independent Fraction linear operator: 12x8 pair-marginal matrix rank=7, one-dimensional kernel spanned by parity vector (-1)^(x+y+z). Adding one actual JOINT triple cell constraint P(000) gives rank8. A complete overlap graph is insufficient for a 3-way target; target-relevant hyperedge information is required unless stronger distributional assumptions bridge it. Gaussianity or known conditional independence can exclude this non-Gaussian family and is NOT refuted by this witness.

## Falsifying experiment and exact cost for TWO preregistered worlds
Collect K genuinely independent, target-population joint XYZ triples (same measurement definitions/selection). For theta=+3/5 vs -3/5, with equal prior and 0-1 model-identification loss, each parity-even measurement has odds multiplier4, parity-odd multiplier1/4; optimal sign decision = majority parity with randomized tie. Exact binomial error: K=0: .5; K=1:.2; K=3:.104; K=5:.05792; K=9:.01958144; K=11:.01165420544; K=13:.0070035611648; K=20:.001579120549167. In THIS synthetic two-hypothesis experiment K=13 is first with expected wrong-sign error <=1%; NOT a clinical sample size bound. One joint sample MI about model sign = ln2-h(.8)=.1927447570217574 nats, KL(+||-) =.6 ln4=.8317766166719344 nats. Fisher for unknown theta per joint triple=1/(1-theta²)=1.5625 at theta=.6; pair-only=0.

## Controls / provenance
Executed independently as a stdlib Fraction 8-state probability table, exact binomial tails, and a SECOND independent Fraction Gaussian rank elimination, with two separately generated deterministic JSON results. Full clean extracted ZIP rerun both programs yields BYTE-IDENTICAL original JSON; manifest member SHA256 and ZIP CRC PASS.
MODERATOR LOCAL COMPLETE ZIP: IW_XH_S5_ROT006_STRUCTURED_MISSINGNESS_TRIPLE_NULLSPACE_REPRO_20261026.zip SHA256 ba23b8eabedb45483ca791925c05b198e8e1ced7b1be34b9e308f7722008de24.
Local full report SHA256 dec73443c3e435a3d2c96c46845ffd5bd832b5a20674bedf4fd083d7cf2ae4cc.
This GitHub report is substantive science and provenance, not the complete ZIP unless the ZIP is independently uploaded and read back.

No novel math, original clinical source data not run, source's 40-var Gaussian experiment not refuted, target-population exchangeability and fair triad auditing stipulated, no biomedical predictive validation. NASH parallel is ONLY general observation-operator claim governance and scientific experiment design, never a physical K/J3 or PBH inference.
NO_CANON / NO_EXEC_SIGN / NO_OWNER_ACCEPTANCE_ASSUMED / NO_BW_INGESTION_ASSUMED / NO_NEW_TASK_CASCADE.
