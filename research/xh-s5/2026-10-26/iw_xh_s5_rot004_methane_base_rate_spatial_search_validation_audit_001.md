# XH-S5 ROT004 — Methane satellite alert validity under rare-event deployment and unknown source locations

artifact_id: IW_XH_S5_ROT004_METHANE_BASE_RATE_AND_SPATIAL_SEARCH_AUDIT_001_20261026
return_id: XH-S5-ROT004-METHANE-BASE_RATE-AND-SPATIAL-SEARCH-AUDIT_20261026
source_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
date: 2026-10-26
exposure: PUBLIC
claim_ceiling: PRIMARY_SOURCE_REVIEW / EXACT_CONDITIONAL_BAYES_AND_BINOMIAL_AUDIT / NO_AUTHOR_DATA_REANALYSIS / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Source first / external science
Reuland, Adams, Sherwin, El Abbadi, Kort, Brandt, "Evaluating space-based methane detection through a one-year blind test", Nature 658, 673–681 (14 Oct 2026), DOI https://doi.org/10.1038/s41586-026-11115-0 . **AUTHOR SOURCE FACT:** 746 controlled events, 481 metered releases (9.5–1183.7 kg/h), 265 blank events, 12 satellites, 15 analyst teams, >2250 estimates. Dedicated methane instruments reported TPR 92–100% and FPR 0–11% across reported systems/protocols. **These endpoints are not a measured joint (TPR,FPR) pair of a particular device.** 79% of total false positives were attributed to AI-based analysis: this is the fraction of the FP numerator, not necessarily the AI systems' conditional FPR. Cloud cover >20% degraded performance. The authors explicitly qualify their applicability with **source location approximately known**.

External prior: Sherwin et al., "Single-blind test of nine methane-sensing satellite systems from three continents", Atmospheric Measurement Techniques 17, 765–782 (2024), DOI https://doi.org/10.5194/amt-17-765-2024 . Earlier blind test 82 releases / 134 estimates, 34 correct true negative responses and 0 false positive answers, with authors noting possible background artifacts and the advantage of known location. These 34 responses do **not** establish 34 independent trials of one frozen satellite system.

Access limitation: source release/meteorology and manuscript figure reproduction data live at Stanford DOI https://doi.org/10.25740/QH001QT3946; the repository request returned 403 in this investigation. **Author-level data and source code were NOT downloaded or executed.** This return is a source-specific experimental transfer audit plus exact standalone math, never a reproduction of paper figures or measurements.

## Two transport gaps (mature classical mathematics; not a new theorem)
The source's test establishes results conditional on a high frequency of artificially staged emissions, known approximate location, a range of fluxes, atmospheric conditions and instruments. Transferring TPR to another **base rate** does not identify *positive predictive value* PPV, and transferring an alert algorithm from one known location to blind **spatial search** changes the number of possible false alerts. Both are established diagnostics: Bayes 1763 / classic rare-event detection, exact binomial zero-failure upper confidence (Clopper–Pearson 1934), multiple-comparisons union bound / Bonferroni.

Let pi=P(real event), s=TPR, f=FPR, where one trial/opportunity is precisely defined. Then:
PPV=pi*s/(pi*s+(1-pi)*f). For ANY s>0 and f>0, PPV→0 as pi→0; TPR does not establish alert accuracy without base rate.

**XH EXECUTED CONDITIONAL SYNTHETIC EXPERIMENT (not source observation):** set pi=.001 and s=.92. All values below are math on these explicit assumptions, not a claimed satellite's performance.
  f=.11    => PPV=.008302499774388593 (0.83%), expected FP/10k=1098.9 vs TP/10k=9.2
  f=.01    => PPV=.08432630614115490  (8.43%), FP/10k=99.9 vs TP/10k=9.2
  f=.001   => PPV=.4794163626889005   (47.94%), FP/10k=9.99 vs TP/10k=9.2
  f=.0001  => PPV=.9020492205118149   (90.20%), FP/10k=.999 vs TP/10k=9.2

To demand target precision PPV>=q=.9 at pi=.001, s=.92, require EXACTLY
 f <= pi*s*(1-q)/((1-pi)*q) = .0001023245467689912 (0.01023245%).

**Negative control sample budget:** If and ONLY if a fixed classifier has k=0 false alarms in n IID independent negative control opportunities, the exact ONE-SIDED 95%-level binomial upper bound is f_U(n)=1-.05**(1/n). Thus
 n=34 => f_U=.0843396433506254, lower PPV conditional on pi/s=.010801252944888805
 n=265 => f_U=.0112409926329601, lower PPV=.07572171244606869
 n=1000 => f_U=.00299124954509530, lower PPV=.23539897581679245
 n=10000 => f_U=.000299528359776612, lower PPV=.7545753317946812
 n=29276 => f_U=.0001023220045865014 <= precision threshold, lower PPV=.900002235993216
 n=30000 => f_U=.000099852756833388, lower PPV=.9021793380751518.
N=29276 is the exact minimal ideal independent negative-control number with zero observed FP for certification of the conditional PPV target at 95% one-sided confidence, assuming pi/s precisely known and stable. n=265 is total blank events in the study, NOT a demonstrated independent negative sample for any single device or method. One cannot claim operational FPR from this example.

**Unknown location (separate transfer):** Take a hypothetical M=1000 candidate locations and target probability of at least one false alarm <=.05 in an all-blank scene. If window alarms are independent, FWER=1-(1-f)**1000, so f<=.00005129197890901785 and an ideal zero-FP independent per-window calibration would require 58404 negative trials. WITHOUT spatial independence, Bonferroni union bound gives sufficient per-window f_i<=.05/1000=.00005, needing >=59914 independent negative calibration trials for the identical threshold under k=0 with one-sided 95% confidence. Bonferroni FWER control does not require within-scene window independence, but a binomial interval fitted to training negatives still requires appropriate independent validation trials. These are experimental-design ceilings, not field-satellite figures. Spatially adjacent pixels are typically correlated; a deployable model must define the opportunity/window and correlation.

**Source denominator audit:** "79% of false positives came from AI methods" = FP_AI / (FP_AI+FP_other), NOT FP_AI / negatives_AI. Ranking conditional FPR requires matched denominators for each analysis cohort plus weather/flux/location/abstention stratification. Two different hypothetical exposure tables can preserve that 79% share and reverse method FPR ordering.

## Validation and negative knowledge
Original executable stdlib Python (not authors' code) and independent SciPy binomial test + brentq root: all PASS. Source facts and toy assumptions kept in different schema objects. Prove sample size minimal via n vs n-1; validate odds-form of Bayes, survival (1-f_U)**n=.05, exact FWER under independent hypothesis, and safe Bonferroni upper bound. Clean extracted ZIP replay, manifest SHA-256 and deterministic JSON byte-identical PASS.

FULL local Moderator archive (NOT claimed committed with this locator): IW_XH_S5_ROT004_METHANE_BASE_RATE_SPATIAL_SEARCH_REPRO_20261026.zip, SHA256 c51f1115c142cb4bee7aef8c238a4db2c778c3a0a2df7316fb2e1f0daf7700e0.
Report SHA256 1579380bc6fa00acc1bbf2d3ed6c7e025044aa4b89a1bcc9f09f0ee7ccc89b77.
Stdlib source SHA256 17136c734aa59c34223b9e350936df8a75562d617e6756b29c7353a8b54033cd.
Independent test SHA256 1203c9f3274430138c2a72085a335017a259fcba801d10f12763ba07dc1dd355.
JSON SHA256 224e1ff59160e34bab388fcf0146fdd10af1001ace1f87f1340d9336dac08563.

**MATURE HOST PRIORITY:** No new Bayes, no new Clopper-Pearson, no new multiple testing theory, no claim of refuting the paper. Other NASH work is methodologically related (XH-S4 028 diagnostic denominators, XH-S5 ROT003 competing models) but distinct; repo keyword searches do not prove absence of private prior art. No satellite source imagery read, no atmosphere simulation, no deployment prevalence measured, no per-device observational confusion matrix reconstructed, no NASH physical upgrade.
**PROPOSED DISCRIMINATING EXPERIMENT ONLY:** freeze algorithm and detection window definitions; preregister held-out negative locations/dates/weather, compare known-location detection with unknown-location scanning on same held-out scenes, measure TP/FP/TN/FN/abstain, effective n and spatial FWER, account for actual emission prevalence, and require independent ground truth. No tasks assigned to another cell.
NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED / NO_NEW_TASK_CASCADE.
