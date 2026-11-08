# XH-S5 ROT024 — Original Nov 2026 resilience regression: known measurement-noise bias, exact magnitude and irregular-sampling real-domain failure

artifact_id: IW_XH_S5_ROT024_MEASUREMENT_NOISE_SAMPLING_GATE_20261108
return_id: XH-S5-ROT024-SMITH2026-LANGEVIN-OBSERVATION-NOISE-IRREGULAR-SAMPLING-DOMAIN-GATE_20261108
date: 2026-11-08
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_OPEN_FULL_PAPER_SOURCE_EQUATION_SPECIAL_CASE / PURE_STATIONARY_OU_ANALYTIC_MOMENTS / TWO_INDEPENDENT_EXECUTED_NUMERIC_ROUTES / NO_AUTHOR_ZENODO_NOTEBOOK_EXECUTION / NO_REAL_CLIMATE_DATA_REPLAY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

## ORIGINAL SCIENCE FIRST and authors' own limitation

Taylor Smith, Andreas Morr, Christof Schötz and Niklas Boers, "Estimating the resilience of non-stationary systems", Nature Communications 17:11286, published 2026-11-06, DOI https://doi.org/10.1038/s41467-026-78489-7 ; full original source text accessible via Nature search, key source equations (2), (3), (4), (10), (13), and Methods verified. Original authors introduce regression on state x_i and (x_(i+1)-x_i)/delta_i for inference of linear Langevin recovery rate lambda and harmonic modeling of nonstationary attractor. They test seasonality, irregular gaps, physical uncertainties and spatiotemporal data; those original scientific results and priority remain THEIRS.

CRITICAL AUTHORIZED SCOPE: Source authors EXPLICITLY ACKNOWLEDGE that observation measurement noise is shared between x_i and its increment with opposite signs and therefore biases fitted resilience lambda UPWARD; they specifically assume driving process-noise amplitude much larger than measurement noise. THIS IS NOT A NEWLY FOUND ERROR OR AN OMISSION IN THEIR ARTICLE. The executed ROT024 test independently quantifies that explicitly disclosed condition and demonstrates what happens when it fails. The author's robust IRLS/WLS implementation and actual satellite, paleoclimate and glacier data were NOT replayed or judged.

Original author Zenodo notebook/code https://doi.org/10.5281/zenodo.19731233 (v2 record https://zenodo.org/records/21440750), source data/secondary code https://doi.org/10.5281/zenodo.18031340. Zenodo source code NOT DOWNLOADED OR RUN; the v2 archive is indexed at ~663.8MB. The local ZIP contains only independent XH code and genuinely SYNTHETIC results, no copied paper code or author real data.

Prior scientific host: OU process, errors-in-variables, latent-state versus observed-state time series, Jensen convexity are mature. H. H. Strey, "Estimation of parameters from time traces originating from an Ornstein-Uhlenbeck process", Phys Rev E 100:062142 (2019) DOI https://doi.org/10.1103/PhysRevE.100.062142 addresses sampling interval/parameter inference and the confidence interval limitations. No new theoretical priority, no scientific novelty.

## Exact source-typed derivation from a stationary subclass of authors' Eq.(2),(3),(10),(13)

Take genuine latent stationary OU dz=-lambda z dt + sigma dW, lambda>0, stationary state variance V=sigma²/(2lambda). Independent additive measurement error e_i with mean0 variance tau²; OBSERVE y_i=z(t_i)+e_i. Measurements at predetermined times, gaps d_i>0 independent of latent state. For fixed d, the population regression of r_i=(y_(i+1)-y_i)/d on y_i WITH INTERCEPT satisfies:

Cov(y_i, y_(i+1)) = V exp(-lambda d);
Var(y_i)=V+tau²;
Cov(y_i,r_i)=[V(exp(-lambda d)-1)-tau²]/d.

Therefore positive fitted DISCRETE return rate b=-beta_y = [V(1-exp(-lambda d))+tau²]/[d(V+tau²)].
Applying source Eq.(13), lambda_est=-ln(1-b d)/d, yields EXACT large-sample identity

lambda_est = lambda + ln(1+tau²/V)/d.

Thus making the sampling denser at fixed sensor accuracy may spuriously increase the apparent resilience without changing the underlying physical dynamics. Uniform observation weights (homoskedastic tau) reduce WLS to OLS; this test alone does not audit all heteroskedastic IRLS weighting choices of the paper. For seasonal test below, independent *exact* Fourier basis for a KNOWN seasonal attractor does not eliminate the observed-state error-in-variables bias.

For irregular d_i, let E be the predetermined empirical limiting mixture of time steps. The population OLS coefficient is

b_* = [V E[(1-exp(-lambda D))/D] + tau² E(1/D)]/(V+tau²).

Mean-time source Eq.(13) conversion lambda_est = -ln(1-E[D]*b_*)/E[D] IS REAL ONLY IF 1-E[D]*b_*>0. Measurement error yields the singular amplifying term tau² E(1/D); short intervals can make the log argument nonpositive even with a perfectly stable true process. This is a well-defined special case outside the source's assumption dominating process noise; NOT a paper-level universal claim.

Also, Jensen gap for irregular d is mathematically classical: g(d)=(1-exp(-lambda*d))/d=integral_0^lambda exp(-s*d)ds, g''(d)=integral_0^lambda s²exp(-s*d)ds>0. The authors themselves discuss a related upper bound for mean-step conversion when d varies.

## Executed exact case table

Set source-INDEPENDENT illustrative lambda_true=.35, sigma=.9, V=.81/.7=1.157142857. Time units arbitrary, not observed climate recovery rates.

sampling steps d | tau | exact population converted lambda_est
.10 | 0 | .3500000
.05 | .30 | 1.8480262
.10 | .30 | 1.0990131
.50 | .30 | .4998026
alternating [.05,.15] | .30 | 1.3711959
alternating [.02,.18] | .60 | 11.5635878
alternating [.01,.19] | .60 | UNDEFINED_REAL: b_*=12.7512238187; E[D]=.10; log argument -0.2751223819
known seasonal attractor, d=.10 | .30 | population formula 1.0990131 (Fourier basis included)

The true latent OU lambda is .35 in EVERY test. For the extreme alternating case, an unmodified regular conversion to continuous time has no real output, rather than a meaningful resilience estimate. This is an exact population-domain witness, not stochastic finite-sample speculation.

## Independent actually executed numerical validation

ROUTE A independent Python3.13 standard-library script rot024_exact.py implements analytic covariance, regular identity, finite-difference conversion, irregular bound, Jensen convexity proof and all 8 cases. All strict assertions PASS.

ROUTE B independent Python NumPy2.3.5/SciPy1.17 rot024_independent.py generates exact OU transitions without Euler discretization, each from its stationary distribution with time steps exactly specified, adds independent normal sensor error. 8 distinct cases x180000 steps EACH = 1,440,000 exact OU transitions with seeded RNG20261108. Fits ordinary Eq.(3) regression, computes continuous-time source Eq.(13) conversion, and fits an independent lag-covariance moment correction with EXTERNALLY KNOWN tau². Independent seasonal control adds mu(t)=1.8*sin(2pi*t/3.7)+.5*cos(4pi*t/3.7) and uses a correct two-harmonic Fourier basis in the regression, plus an independent Huber IRLS control (NOT original paper's software).

Representative observed simulated outcomes, alongside EXACT population expectations:
regular no noise d.1: lambda_OLS .348592 vs .350000;
regular noisy d.05 tau.3: 1.844141 vs 1.848026;
regular noisy d.1 tau.3: 1.087925 vs 1.099013;
regular noisy d.5 tau.3: .499438 vs .499803;
irregular d[.05,.15] tau.3: 1.314976 vs 1.371196;
irregular d[.02,.18] tau.6: 11.394801 vs 11.563588;
irregular d[.01,.19] tau.6: source conversion UNDEFINED_REAL in both population and simulation (sample b=12.5753);
seasonal Fourier case: OLS 1.142500, independent Huber-IRLS 1.144705, both strongly above .35 despite *correct* seasonal basis.

Independent deattenuated-lag-covariance moment correction, ASSUMING tau² is known from external sensor calibration, recovers lambda close to .35 in all cases. For irregular d[.02,.18] tau.6 gives .350027; irregular d[.01,.19] tau.6 gives .353754. This is an ORACLE correction not a solution when measurement error is unobserved, correlated, non-Gaussian or state dependent. No original field data or statistical uncertainty estimates, no claimed climate tipping forecast.

## Custody of reproduced work, exact clean ZIP result

FULL MODERATOR LOCAL ZIP: IW_XH_S5_ROT024_NONSTATIONARY_RESILIENCE_OBSERVATION_NOISE_GATE_REPRO_20261108.zip
ZIP SHA256: 95d29ffaff2eee560bf9ed7df6520a34f6cad0537fd457fd545570806c383baf
FULL REPORT SHA256: 18fa27ffb54a8808bb283015cfeebca16b8ec55ccc286c630de0e958c1cdbb24
9 ZIP members: self-contained Polish scientific report, two independent runnable Python scripts, two frozen results JSON, source_locator.json (source access/negative knowledge), README, clean replay verifier, manifest_sha256.json.
ZIP CRC PASS, all 8 SHA256 content member checks PASS; clean external ZIP extraction and both scientific scripts reexecuted under Python3.13. Both JSON result files BYTE-IDENTICAL to frozen originals PASS. The GitHub text IS NOT the complete independent-code ZIP; file custody limits explicit.

## Bounded scientific interpretation / conditional falsifier

Positive finding: exact strength and regular/irregular sampling dependence of an ALREADY-ACKNOWLEDGED source noise limitation, plus explicit real-domain failure of mean-step conversion when short-step sensor error dominates. Test holds for OU stationary subclass and source-style ordinary regression, and has a supportive independent seasonal Fourier/Huber numerical control. It does NOT invalidate the author’s real-world climate analyses, Huber weighting, published conclusions, or source method in its stated regime. It does NOT claim a mathematical novelty or priority over measurement error theory.

Referee-only question: before interpreting lambda trends as changes in physical resilience, report instrumentation tau²/V, distributions E[D] and E[1/D], check 1-b*E[D]>0, and if needed benchmark source robust regression against latent-state likelihood with independently calibrated sensor noise and out-of-sample validation. No task cascade, no NASH K/J3/GR/GW physical upgrade, BW/REFEREE/OWNER/EXEC acceptance unverified.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_AUTHOR_NOTEBOOK_REPLAY / NO_REAL_WORLD_DATA_REPLAY / BW_INGEST_UNVERIFIED.
