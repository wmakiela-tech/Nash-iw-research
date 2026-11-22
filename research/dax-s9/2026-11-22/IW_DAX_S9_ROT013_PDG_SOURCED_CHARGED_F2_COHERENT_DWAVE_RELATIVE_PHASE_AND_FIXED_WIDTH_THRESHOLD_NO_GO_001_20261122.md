---
artifact_id: IW_DAX_S9_ROT013_PDG_SOURCED_CHARGED_F2_COHERENT_DWAVE_RELATIVE_PHASE_AND_FIXED_WIDTH_THRESHOLD_NO_GO_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
document_type: ORIGINAL_BOUNDED_SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_TYPED_PDG_CHARGED_F2_PHOTOPRODUCTION_TWO_WAVE_REPLAY / COHERENT_BORN_F2_PHASE_IDENTIFIABILITY / FIXED_WIDTH_TENSOR_PION_THRESHOLD_NO_GO
claim_ceiling: NO_COMPLETE_PHYSICAL_PHOTOPRODUCTION / NO_AUTHOR_EXPERIMENTAL_FIT / NO_EXPERIMENTAL_CI / NO_IN_MEDIUM_PION_TRANSPORT_OR_NEUTRINOS / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT013 — conditional charged f2(1270) model, coherent Born interference, and fixed-width tensor threshold falsifier

**22 November 2026.** Source-first bounded scientific return after DAX9 ROT010 (original strong ππ/KK T), ROT011 (full-Born vs leading-two-wave fiducial truncation), ROT012 (original coherent γγ→π+π− leading s-wave Born+FSI, Watson negative control). Present turn reconstructs a **conditional** helicity-2 charged Born+f2 amplitude and explicitly tests its parametric and threshold limitations. Physics firstness belongs to the original authors, PDG, and mature centrifugal-barrier phenomenology. This is NOT Dai–Pennington fitted Solution I and NOT a full QCD pion/neutrino spectrum.

## Original source receipts

- S.P. Klevansky, R.H. Lemmer, A. Beygi, *EPJA* 61:49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , original publisher full article HTML **read**: Eqs (13),(17),(18),(21),(22),(66)–(70),(72)–(75), Table2, Sect3.2. Authors' resonance approximation expressly takes Γ(W)=constant for simplicity. The quoted example **P_neutral = Γγγ^(2) Br(π0π0) Γ = 0.16 MeV²**, is for NEUTRAL pions only, not a charged experimental measurement.
- PDG original 2025 f2(1270) listing https://pdgweb.lbl.gov/2025/listings/rpp2025-list-f2-1270.pdf : textual data read (web screenshot request CACHE_MISS; no visual PDF inspection or PDF-byte SHA claimed). Central Γγγ,total=2.6±0.5 keV (model-dependent), Br(ππ)=0.843 with asymmetric errors, Γtotal=186.6 MeV with asymmetric errors, helicity-0/helicity-2 ratio r=.037 with LARGE asymmetric errors. Public PDG Live crosschecks https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=sumtabM&node=M005 and https://pdgprod.lbl.gov/pdgprod/pdgLive/Fit.action?home=MXXX005&init=0&node=M005 ; live version drift not treated as original PDF identity.
- Mature original centrifugal barrier: Belle tensor resonance mass-dependent Γππ(W) ∝ q^5 times Blatt–Weisskopf factor, https://academic.oup.com/ptep/article/2013/12/123C01/1554656 and https://link.springer.com/article/10.1140/epjc/s10052-021-08875-6 . No novelty claimed for this known angular-momentum law.

## Source-typed *conditional* charge normalization, not measured charged interference

Use explicitly stated approximations: isospin symmetry Br(π+π−)=(2/3)Br(ππ)=.562 (not independently published charged fit), Gammaγγ^(2)=Gammaγγ,total/(1+r)=.00250723240116MeV (r=.037). Then **P_charged,PDG = Gammaγγ^(2) × .562 × 186.6 MeV = 0.262931456123433 MeV²**. Independent and distinct author-neutral-channel-to-charged isospin-transfer scenario yields **P_charged,neutral-transfer = 2×.16 = .3200000 MeV²**, ratio to the preceding conditional value **1.21704723**, not a statistical disagreement between independent data. PDG marginal covariance, genuine charged BR and relative complex Born/f2 production phase are not provided. The author uses M=1.275GeV and Γ=.185GeV in Eq67, whereas PDG has Γ=186.6MeV; using PDG Γ only for P but the paper's pole/line shape elsewhere is an OPEN documented **mixed-input illustrative benchmark**, not an author fit.

## Original Eq13 and Eqs66-70 amplitudes, plus actual source execution

For W=sqrt(s), beta=sqrt(1-4mπ²/s), Q(W)=(-3+5β²)/(3β²)+(1-β²)²/(2β³)ln[(1+β)/(1-β)], source-published complex coefficients of Y_22:

**B22(W)=2i e² Q(W) sqrt(15π/2)** (Eq13), and **R22(W)=−16πi sqrt(20π/β) × [W sqrt(P)/(s−M²+iMΓ)]** (Eqs66-67). All P in GeV² (0.262931456 MeV² = 2.62931456e−7 GeV²). Set mπ=.140GeV, M=1.275GeV, Γ=.185GeV, α=1/137.035999084. For unpolarized photons, Eq75's **leading two-wave** source is σ^(00)_Born+FSI from existing source-tested ROT012, plus σ^(22)_{Born+f2} from **|B22+e^{iφ}R22|²**. No s-d interference (different incoming helicity components); d-Born versus d-f2 DOES interfere. Source Eq67 positive sqrt choice φ=0; **partial widths alone do not measure φ**, so φ=π is a counter-scenario, not an equally probable author fit.

Exact Belle acceptance **F22(.6)=15/8[.6−(2/3).6³+.6⁵/5]=.88416**. Independently performed direct |Y22|² angular integral, compared pure-Born d22 to original Eq18 and pure-f2 to Eq70: all PASS relative <2e−13. Independent direct 60-digit mpmath coefficients reproduce binary64 source implementation on 5 points to <2e−12. The sharp phase-unrestricted pointwise math floor/ceiling given fixed σ_B,σ_R is **(sqrt(σ_B)∓sqrt(σ_R))²**; not a confidence interval and individual energy extrema cannot all be achieved simultaneously by ONE global φ.

| W GeV | d-Born nb | d-f2 nb | d-coherent φ0 nb | d-coherent φπ nb | sum with s-wave Born+FSI φ0 / φπ nb |
|---:|---:|---:|---:|---:|---:|
| .80 | 98.535 | 11.075 | 173.865 | 45.356 | 184.339 / 55.829 |
| 1.00 | 73.433 | 25.445 | 179.772 | 17.984 | 195.695 / 33.906 |
| 1.20 | 55.337 | 126.259 | 284.981 | 78.211 | 293.674 / 86.904 |
| 1.275 | 50.066 | 204.452 | 254.518 | 254.518 | 261.966 / 261.966 |
| 1.40 | 42.703 | 67.934 | 22.613 | 198.661 | 28.493 / 204.541 |

No MarkII/Belle experimental fit, causal lepton background inference, or physical pion full-rate claim. At the model W=M, Breit–Wigner phase makes d-Born/d-f2 interference vanish, producing equal φ0/φπ values. Other energies differ dramatically; therefore resonance WIDTH input does not by itself specify a coherent production prediction.

## Stronger physical falsifier: constant-width f2 threshold NO-GO

**Exact original Eq70**: σ_f2(W)=40πP/[(W²−M²)²+(MΓ)²], with constant Γ and P. At W→2mπ+ this stays **NONZERO** because Eq66 R22 ∝ β^(−1/2) cancels the explicit beta phase-space factor. For above conditional charged P and Belle |z|<.6:

**lim σ_f2,fid (W→2mπ+) = 4.64377624355199 nb.**

A physical J=2 decay to TWO spinless π requires partial-width factor **q^5** (centrifugal barrier), hence resonance contribution should vanish at threshold. The original paper itself says it fixes Γ(W) constant FOR SIMPLICITY; this **does not falsify** its possible local fit around 1.275 GeV, but does falsify its automatic physical extrapolation into low-W pion source for R68. Independently verified original scalar Born J=2 threshold numerical beta-exponent **4.9995167**, not a constant. At beta=.1 (just above threshold), Eq70 constant-width resonance gives **4.6484254 nb**, whereas a deliberately MINIMAL **illustrative, not physical amplitude completion** multiplying its rate by (q/q_R)^5 gives **2.7550×10^−8 nb**. Physical running-width treatment also requires proper denominator, barrier form factors, other channels, resonance phase, model fitting; no such model newly asserted as completed.

## Conditional R68 source fold, benchmark only

Inherited Eγ=1436.554 GeV and Planck T=.00007818527068831995GeV, same H(W), charged |z|<.6. Two-wave source model K in six W bands for global φ0 / φπ:

- .35-.54 GeV: 1.827727586e−10 / 1.002452046e−10;
- .54-.80: 3.456071193e−10 / 1.323176860e−10;
- .80-1.00: 2.386654400e−10 / 5.110891911e−11;
- 1.00-1.15: 1.610396587e−10 / 2.157549701e−11;
- 1.15-1.35: 1.577942727e−10 / 1.059342897e−10;
- 1.35-1.50: 7.243637945e−12 / 4.719400964e−11.

Separate 128-point Gauss–Legendre (with threshold split W=.992 for inherited chiral FSI) and SciPy adaptive fold agree to **max relative 5.801e−7**. These synthetic models do NOT demonstrate real pion production, MarkII/Belle experimental agreement, neutrino spectra or BBN/PBH bounds. The low-W mass dependence of original constant-width f2 is specifically UNPHYSICAL at threshold.

**Born fiducial fallback guard:** exact scalar-QED Eq21 source re-integrated independently (including both ±z halves), and original J00+J22 truncated pure Born fiducial output differs by **+19.628% at W=.80GeV**, **+19.857% at W=1.0**, **+20.467% at W=1.275**. Thus the presently coherent leading TWO-wave amplitude must NOT be called full physically untruncated photo production. A preliminary supplementary Born reference check detected an angular symmetry factor 2 omission, explicitly FIXED before frozen results, and asserts these ~+20% deviations to protect ROT011 precedence.

## Original reproducibility, provenance and decision

Complete local original report and SOURCE-VERIFIED REPLAY package, **ZIP SHA256 266645a7f3828ffbccfec85df21bcd7e8febaa70e8acb4fd8ccc7c546999ad2c**, ZIP CRC PASS, **9/9 member SHA256 PASS**, clean directory (local relative source import) **3/3 generated JSON+CSV BYTE-IDENTICAL PASS**. Files: report, original executing code, immutable/source-named copied predecessor s-wave checker, 2 CSV, JSON, execution log, primary source citation/receipt JSON, README, 9-file SHA manifest. The package is attached in originating conversation and NOT represented as uploaded to GitHub. No original author fit coefficients or HEPData raw bytes. Present GitHub Markdown is report-only, not custody of code. No independent external referee/I3 or BW ingestion is inferred from GitHub or Slack write.

**Next high-value discriminator:** physical energy-dependent **charged f2→π+π−** q^5 + barrier line shape with original-source-defined *relative photon d-wave phase* and actual MarkII/Belle differential uncertainty structure, then control full exact Born fiducial baseline. No more arbitrary source-only weighting, no owner override.

**RETURN: PUBLISHED_EQ13_EQ66_70_CHARGED_DWAVE_REEXEC_PASS / PDG_CHARGED_PRODUCT_CONDITIONAL / COHERENT_TWO_WAVE_SOURCE_MODEL_PASS / RELATIVE_PHASE_NOT_DETERMINED_FROM_WIDTHS / SOURCE_FIXED_WIDTH_TENSOR_THRESHOLD_PHYSICAL_NO_GO / INDEPENDENT_ANGLE_MPMATH_R68_PASS / FULL_PHYSICS_AND_EXPERIMENTAL_CI_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
