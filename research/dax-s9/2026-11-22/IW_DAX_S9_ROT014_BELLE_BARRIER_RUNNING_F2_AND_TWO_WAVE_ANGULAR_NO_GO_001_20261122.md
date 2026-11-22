---
artifact_id: IW_DAX_S9_ROT014_BELLE_BARRIER_RUNNING_F2_AND_TWO_WAVE_ANGULAR_NO_GO_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_TYPED_F2_RUNNING_Q5_BLATT_WIDTH / SHARP_TWO_WAVE_ANGULAR_SOURCE_CENTRAL_NO_GO
claim_ceiling: NO_PRIMARY_HEPDATA_BYTES / NO_EXPERIMENTAL_COVARIANCE_OR_CI / NO_FULL_PHYSICAL_PHOTOPRODUCTION / NO_NEUTRINOS / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT014 — Running f2 width repairs threshold; two-wave angular shape is incompatible with Belle central source bins

Date **2026-11-22**. Science-first bounded DAX9 return following ROT010–ROT013. The original full 11,212-byte scientific report, source-verified executable, primary-author transcriptions, two SHA-pinned official SECONDARY Rivet references, 140-bin and angular source outputs, frozen JSON, replay log and manifest are contained in the originating conversation's local ZIP `DAX9_ROT014_Running_f2_Barrier_TwoWave_Angular_Source_NoGo_Repro.zip`, SHA256 `321307e8afbce7c650a1063cd30ac452fc6a2097f02822c01b85bcc3007ecdef`. This GitHub Markdown is the publishable evidence summary, not a claim that complete executable source was uploaded into the repository.

## 1. Original scientific and experimental source receipts

- Original 2025 charged photon-pion source: S.P. Klevansky, R.H. Lemmer, A. Beygi, EPJA 61:49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 ; publisher original full HTML equations (9),(13),(17),(18),(21),(22),(65)–(70),(74)–(75) actually read. Eq(67) can accommodate Gamma(W); authors **explicitly take Gamma(W)=constant for simplicity** in original numerical illustration. Their charged-pion cross-section keeps leading J00 Born+FSI and J22 Born+f2; neither is the exact full-angular Born.
- Belle Collaboration, *High-statistics study of K0S pair production in two-photon collisions*, PTEP 2013 123C01, DOI https://doi.org/10.1093/ptep/ptt097, **original Eq(13)** supplies standard tensor centrifugal decay barrier Gamma_X(W)=Gamma_R Br_X (q(W)/q(M))^5 D2(q(W)r_R)/D2(q(M)r_R), D2(x)=1/(9+3x^2+x^4); source Belle Table2 f2 radius r_R=**3.62±.03 (GeV/c)^-1**. This source concerns a different final state, so reuse in charged pion production is a **DECLARED illustrative cross-source combination**, not an original common author-fitted amplitude.
- PDG 2025 original f2(1270) listing https://pdg.lbl.gov/2025/listings/rpp2025-list-f2-1270.pdf ; Gamma_gamma_gamma,total=2.6keV, helicity0/helicity2 ratio=.037 (large error), Br(pi pi)=.843. Br(pi+pi-)=(2/3)*.843=.562 is **isospin assumption**, not independent charged phase measurement. This turn consistently uses source-paper pole mass M=1.275GeV and width Gamma_R=.185GeV in BOTH numerator and denominator, resulting product P_pole=Gamma_gg(hel2)*Br_ch*Gamma_R=**0.2606769527483125 MeV²**. This is modestly different from ROT013's 0.262931456123433 MeV², whose numerator employed PDG total 186.6MeV and denominator original paper 185MeV. Both are conditional, not new measured parameters.
- **Actual verified bytes re-read**: MarkII official packaged SECONDARY Rivet `MARKII_1990_I304882.yoda.gz` compressed SHA256 `ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d`, and Belle packaged SECONDARY `BELLE_2007_I749358.yoda.gz` compressed SHA256 `28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403`. 140/140 Belle author-original Appendix B central W σ entries equal YODA d01 at published precision. Original primary HEPData exports, collider-event data and correlated experimental errors remain NOT READ. MarkII angular values are bin-integrated nb; Belle angular values density nb/unit |cosθ| and require multiplication by .05.

**Prior art**: Dai/Pennington PRD90 036004 (2014) had already noticed Belle W≈.8–.9 GeV high-angle rise, possibly but not proven from gamma gamma -> mu+mu- background. DAX9 ROT008/009 established source-central angular histogram anomalies; ROT011 showed ~+20% fiducial Born two-wave truncation versus exact scalar Born; ROT012/013 established source-specified coherent s/d amplitudes and the constant-width tensor threshold problem. This turn reports exact **model-class source falsification**, NOT a new strong-interaction effect or published experiment discovery.

## 2. Physics model scope and exact source-width comparison

Use m_pi=.140GeV, q(W)=sqrt(W²−4m_pi²)/2, q0=q(M); R_q5=(q/q0)^5, R_BW=R_q5 D2(qr_R)/D2(q0r_R). Three **matched pole-normalized** models:
1. `fixed`: Gamma_pi+pi-(W)=Br_ch Gamma_R; Gamma_tot(W)=Gamma_R.
2. `q5`: Gamma_pi+pi-=Br_ch Gamma_R R_q5(W); Gamma_tot(W)=Gamma_R[(1−Br_pi pi)+Br_pi pi R_q5(W)].
3. `bw`: replace R_q5 by R_BW in both expressions.

All use the original 2025 Eqs (66),(67),(70) for resonance amplitude, and coherent J22 Born+f2 with inherited ROT012 J00 Born+FSI, in Belle fiducial |z|<.6. The other **15.7% total width remains constant** (29.045MeV) in q5/bw. This does NOT properly handle all additional thresholds, charged/neutral mass differences, coupled-channel analytic dispersive effects, nor fit the actual amplitude. Relative complex d-wave resonance/Born phase is not determined by the width product; phi0 uses original chosen amplitude convention, phiPi is a deliberately reversed alternative.

At W=M all three pure-f2 rate and interference values coincide by construction. Numeric pure-f2 threshold beta_pi powers from beta=.025→.0125:
- `fixed`: **0.000067** (nonzero f2-only threshold);
- `q5`: **5.001760**;
- `bw`: **5.001702**.

This is an actual source-typed repair of the unphysical extrapolation of constant-width f2 **for the pion channel only**; it does not establish the physical full photoproduction amplitude. Independent direct exact Eq70 pure-f2 control at 5 W points, matched pole and 21 Gauss-12 versus SciPy adaptive bin integral comparisons PASS (<3e−9 relative).

**Thermal R68 conditional** E_gamma=1436554MeV, Planck T=.07818527068831995MeV and H(W)=4W³/C²[-log(1−exp(−W²/C))], C=4E_gamma T. Two-wave K comparisons:
| W GeV | K_fixed phi0 | K_bw phi0 | BW/fixed−1 at phi0 | BW/fixed−1 at phiPi |
|---|---:|---:|---:|---:|
| .35–.54 | 1.825540308e−10 | 1.412443468e−10 | −22.63% | +31.73% |
| .54–.80 | 3.450233219e−10 | 2.620861781e−10 | −24.04% | +43.37% |
| .80–1.00 | 2.380771549e−10 | 1.907011523e−10 | **−19.90%** | **+41.75%** |
| 1.00–1.15 | 1.604622391e−10 | 1.440588502e−10 | −10.22% | −4.22% |
| 1.15–1.35 | 1.568795275e−10 | 1.588565475e−10 | +1.26% | −3.53% |
| 1.35–1.50 | 7.196012006e−12 | 8.803544945e−12 | +22.34% | +2.06% |

The direction itself changes with an unknown relative phase; NOT an empirical source correction or PBH/neutrino rate. MarkII W=.40–.54 lacks reliable pion identification and is NOT converted into measured source here. All 140 Belle author-printed W central cross sections fall within the independently constructed **pointwise arbitrary-phase envelope** of each of three models (0/140 outside). That is a WEAK necessary possibility test, not a single phase globally fitting all bins and not detector-statistical agreement.

## 3. Stronger and parameter-independent model-class angular no-go

For exactly unpolarized source Eqs(74),(75) **only** J00 and J22 (different photon helicities, incoherent), with z=|cosθ*| in [0,.6], the differential angular source has the form
`dσ/dz = A(W) + B(W)(1−z²)^2` with **A,B≥0**. Thus its accepted angular density is nonincreasing. For **any positive** thermal W mixture, any f2 width, any complex d-wave Born/f2 phase, and any s-wave FSI normalization,
`P(0.4≤z≤0.6) ≤ (0.6−0.4)/0.6 = 1/3`.
Pure s-wave saturates 33.3333%; pure J22 gives **23.7875497647%**, hence full allowed mixture [23.78755%,33.33333%]. This is exact *model geometry*, independent of assumptions about how the unknown physical angles are distributed **within original data bins**, since the tested endpoint z=.4 and z=.6 exactly align native bins.

**ACTUALLY READ original secondary numeric source** with original R68 positive H(W) over precisely matched W=.85–.95GeV:
- Belle original 20×12 angular cells: **39.5190812476%** of source central cross section in .4≤z≤.6.
- MarkII original broad W angular cells: **29.2397660819%**, within the theoretical mixture range.
- Exact Belle central-source necessary violation: **≥6.1857479143 percentage points** above the 33.33333% model supremum. MarkII's being inside the range does NOT validate a full angular fit.

**Independent non-thermal strengthening:** all **20/20** native *individual* Belle 5-MeV W-bin angular distributions, with W centers .8525..9475GeV, have central high-angle shares **strictly above 1/3**: min **35.2046656129%**, max **42.9697906122%**. No Planck weighting, bin-average artifact, or MarkII source is required for that result. Every original source set of 12 angular densities is multiplied by .05; no phantom units. This is a **central histogram vs model-class algebraic NO-GO**, NOT 20 independent significance rejections. Belle covariance, systematics, background subtraction and detector migration are not independently validated here. Mature Dai/Pennington had already described related Belle angular anomaly without proving muon contamination. Actual pion theory can include higher Born J, D0 helicity0, higher tensor helicities and other terms, so the NO-GO **DOES NOT** apply to full Standard Model, exact scalar Born, Belle experimental validity, or any realistic fitted inclusive source.

## 4. Reproduction and research disposition

Actual executable original Python `verify_running_width_and_shape.py` (NumPy/SciPy) plus source-verified predecessor ROT012 chiral s-wave, verified official-secondary Rivet inputs and Belle 140 author-paper triples, frozen original JSON (140 individual W model values and fit-free phase envelopes), FOUR CSV output tables, full original Markdown report, README, source receipt, run log and SHA manifest. **Clean replay FIVE generated files BYTE IDENTICAL PASS; ZIP CRC PASS; all 15 payload SHA256 PASS**. Local complete ZIP SHA256 `321307e8afbce7c650a1063cd30ac452fc6a2097f02822c01b85bcc3007ecdef`; not represented as hosted in GitHub. The original 2025 model used one effective kaon mass in s-wave FSI, the source 2013 barrier radius is borrowed across final states and the photon f2 phase has no source-native independent charged fit. No primary HEPData bytes, full experimental covariance, full physical production/stopping, daughter neutrino spectrum, PBH/BBN inference, external referee approval or BW ingestion.

**Next material falsifier**: add exact charged scalar-QED Born *higher partial waves* coherently in original source's helicity basis, then confront 12 native Belle angle cells (while retaining strict source unit and detector covariance controls); alternatively obtain genuine independent angular measurement covariance and background audit. Further arbitrary Gamma/phi box scans are low-value without new physical evidence. No source ownership override.

**RETURN: PUBLISHED_RUNNING_F2_Q5_BARRIER_SOURCE_TYPED_PASS / PURE_RESONANCE_THRESHOLD_EXPONENT_5_PASS / R68_PHASE_DIRECTION_UNIDENTIFIED / SHARP_TWO_WAVE_HIGH_ANGLE_ONE_THIRD_BOUND_PASS / NATIVE_BELLE_20OF20_INDIVIDUAL_ANGULAR_CENTRAL_NO_GO / NO_EXPERIMENTAL_CI_OR_FULL_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
