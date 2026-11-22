---
artifact_id: IW_DAX_S9_ROT020_WATSON_CONSTRAINED_CROSS_CHANNEL_MIN_NON_S_RELAXED_NORM_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NEW_PHYSICS / NO_EXPERIMENTAL_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT020 — sharp relaxed source-norm floor for arbitrary correction beyond Watson-constrained S wave

Original mathematical source-constrained audit, 22 Nov 2026. **NO_NEW_PHYSICS / NO_STATISTICAL_CI / NO_CANON / NO_EXEC_SIGN**. After the ROT018 original 2-channel source contact and ROT019 original Roy/GKPY phase reference, quantify how much central observed charged+neutral photoproduction amplitudes cannot be represented by a FLAT Watson-constrained S wave, WITHOUT assuming the measured total source is S only.

**Independent primary source** García-Martín et al PRD83 074004 (2011), arxiv 1102.2183 original Table XII page34 visually screenshot confirmed, δ00 and δ02 in elastic 0.84–0.94GeV. **Actual authenticated official packaged SECONDARY source bytes** charged Belle source SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403, neutral Belle source SHA256 65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd. Five neutral 20MeV W bins and twenty charged 5MeV W bins, all 12 common angular native 0.05 bin integrals z∈[0,.6], source-specific positive R68 H(W), small nominal betaC/betaN isospin phase-space adjustment from ROT018. Native primary HEPData exports inaccessible; no event-level/correlated experimental covariance.

**Actual bounded object:** represent measured two-channel unpolarized *SOURCE-CENTRAL norm* via original positive C_j,N_j cell integrals. Decompose amplitude A=S+R in a common energy-angle-helicity Hilbert space. S is **flat** in angle, with elastic Watson phases δ00 and δ02 and arbitrary real isospin production coefficients, allowed to vary across W. R is an **ARBITRARY** additive correction (NOT constrained to physical D0 or D2 partial waves). Minimize ||R||²/||A||². Any physical amplitude decomposition satisfying these assumptions has at least this correction norm; the sharp mathematical bound is attained in the *relaxed arbitrary-residual function class*, which need not be physically valid as a pure higher-J wave.

**Exact root-vector projection:** for n=12 equal-angle bins let c_j=√C_j, n_j=√N_j and T=Σ(C_j+N_j). Unconstrained flat-S projections x0=Σc_j/√n, y0=Σn_j/√n give Eshape=T−x0²−y0². Source phase difference Δ gives Watson S neutral/charged norm ratio r≥rmin(Δ)=(1−√(1+8cos²Δ)/3)/(1+√(1+8cos²Δ)/3), k=√rmin. If y0<k x0, the additional sharp residual Ephase=(k x0−y0)²/(1+k²); if already inside cone no penalty. Include symmetric upper phase-cone bound if relevant; no dataset rows need upper constraint. Source-data necessary correction minimum f_R,min=(Eshape+Ephase)/T. Derived from triangle/Cauchy–Schwarz and least-squares distance-to-cone geometry, NOT a new physical result.

| W MeV | shape-only necessary % | Roy central Watson-cone necessary % | deliberately broad ±published phase margins over W bin necessary % |
|---:|---:|---:|---:|
|850|1.4701|8.2130|6.4461|
|870|1.0684|5.2968|3.7585|
|890|0.7654|2.8118|1.4950|
|910|0.6560|1.3544|0.6560|
|930|0.4614|0.4614|0.4614|

**Five W source-intensity weighted total necessary relaxed R-norm floor:** angular-only 0.89469258%; Roy central **3.71152388%**; declared permissive marginal Roy band **2.63330674%**. Rounded source/phase central comparisons only. This is NOT a measured fraction of pions, events, physical D-wave energy, a photon-fusion cross section, a neutrino tail or a confidence interval. Do not combine with ROT018 10.1262% **I=2** norm floor: an I2 wave can belong to S and two definitions differ.

**Independent checks actually executed:** authentic both YODA SHA PASS, 5/5 Roy real-isospin coefficient direct 1D optimization of ratio vs closed eigenvalue rmin, 5/5 source 12-bin original unit layout and totals, 5/5 direct 24 root-vector least-squares residual vs Eshape+Ephase, 5/5 independent constrained 2D SLSQP phase-cone minimization. A separate **standard-library-only** second verifier recomputed ALL 5×3 values and the weighted totals from frozen 60-cell CSV without relying on the primary NumPy/SciPy solver. Two isolated fresh-directory runs regenerated JSON+CSV byte-identical.

**Full local original report + Python + true secondary sources and input data** DAX9_ROT020_Watson_Cross_Channel_Minimum_NonS_Residual_Norm_Repro.zip SHA256 **39085a7ab6204d680b4aa1a06a044d6ab38e8c605f03894f3be3024a697eda24**, ZIP CRC PASS and 14/14 payload SHA PASS, 2×2/2 regenerated files byte-identical PASS. GitHub contains only written report, not actual ZIP bytes.

**Important scientific ceiling:** test is conditional on source central cross sections, model-consistent angle/energy normalization and approximate pion isospin mass correction. Roy printed phase errors are correlated and the artificially broadened 1-margin interval is NOT a statistical phase posterior. Detector angular covariance/migration, neutral unfolding, charge ID, electromagnetic Born left-cut, realistic strong J2, true gamma-gamma helicity partial waves and coupled-channel energy continuation NOT recovered. A positive minimal residual does not identify what mechanism supplies it (ordinary D0/D2, higher waves, detector bias and data calibration all remain possible). NEXT source gate is actually fitted source S,D0,D2 across two channels with phase/dispersion data, not arbitrary free complex nuisance proliferation. NO_I3 / NO_BW_WRITE / NO_OWNER_OVERRIDE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.