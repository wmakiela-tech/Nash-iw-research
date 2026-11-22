---
artifact_id: IW_DAX_S9_ROT011_KLEVANSKY_BORN_J00_J22_FIDUCIAL_TRUNCATION_SIGN_REVERSAL_AND_WARD_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: DIRECT_2025_PUBLISHED_PHOTOPRODUCTION_SOURCE_BORN_REEXECUTION / FIDUCIAL_PARTIAL_WAVE_TRUNCATION_SIGN_REVERSAL / WARD_AND_PHOTOLOOP_BRANCH
claim_ceiling: NO_FULL_BORN_FSI_F2_PHOTOAMPLITUDE / NO_DAI_PENNINGTON_SOLUTION / NO_PHYSICAL_NEUTRINO_OR_PBH_BBN / NO_EXPERIMENTAL_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT011 — charged pion photoproduction Born partial-wave truncation reverses error sign under Belle acceptance

**22 November 2026.** Original bounded mathematical-source audit, not new QED/hadronic physics, not new Mark II/Belle experimental result or full pion-photon amplitude. Follows DAX9 ROT010 reexecution of the *hadronic* (pi pi,K Kbar) coupled T, distinct from the photoproduction tensor. Source-first reference: S.P. Klevansky, R.H. Lemmer and A. Beygi, EPJA 61 49 (2025), https://doi.org/10.1140/epja/s10050-025-01524-6 ; original publisher full HTML equations (9),(13),(17),(18),(21),(22),(60)–(65),(72)–(75) and Table 2 were read. Original 17-page PDF text was read, screenshot Table2 failed cache; original PDF bytes NOT SHA checked. The 2025 authors already explicitly describe approximation by waves (J,λ)=(0,0),(2,2), about 90% of all-angle Born around s <=1GeV². Nothing here is a novel partial-wave formalism.

## Exact declared tested object

At W=sqrt(s), b=sqrt(1-4m_pi²/s), z=cos(theta), the source Eq21 gives
 dσ_B/dΩ=α² b/(2s){[(1-b²)/(1-b² z²)]²+[b²(1-z²)/(1-b² z²)]²}.
Its exact full-angle closed result is the source Eq22:
 σ_B=2πα²b/s [2-b²-(1-b⁴)/(2b) log((1+b)/(1-b))].
The source Eqs17/18 for only two partial waves yield
 σ_00=πα²b/(2s) [(1-b²)/b log((1+b)/(1-b))]²,
 σ_22=15πα²b/(4s) [(-3+5b²)/(3b²)+(1-b²)²/(2b³)log((1+b)/(1-b))]².

For the ACTUAL Belle angular support |z|<c=0.6, direct integration of the retained published Y00 and Y22 amplitudes yields
 σ_00,fid=c σ_00,
 σ_22,fid=F22(c) σ_22,
 F22(c)=15/8[c-(2/3)c³+c⁵/5], with F22(.6)=0.88416.
The EXACT full-Born fiducial result comes from independent angular integration of Eq21 over |z|<.6. These two expressions need not match due to omitted waves. In full 4π, partial wave orthogonality makes omitted integrated norm nonnegative; restricted |z|<.6, interference with omitted partial waves of the SAME helicity means the difference can reverse sign.

R68 kernel inherited with no changes: Eγ=1436554MeV, ideal bath T=0.07818527068831995MeV, H(W)=4W³/C²[-ln(1-exp(-W²/C))], C=4Eγ T, units consistent. Main model m_pi=140MeV from original 2025 paper, α=1/137.035999084. The previously used PDG m_pi=139.57039MeV is used separately for a historical-replay control only.

## Actual executed original-source result

| W GeV | R68-weighted (σ_two wave/σ_exact Born)-1, ALL 4π | SAME ratio error, BELLE |z|<0.6 |
|--|--:|--:|
| .35-.40 | -2.59197% | +21.25897% |
| .40-.54 | -5.57775% | +23.08823% |
| .54-.80 | -8.51333% | +20.30204% |
| .80-1.00 | **-10.23093%** | **+19.69034%** |
| 1.00-1.50 | -11.53358% | +20.21771% |

The .40-.54GeV band is an exclusively hypothetical **Born-model** calculation; original Mark II did NOT obtain reliable pion identification there. No MarkII cross sections were added or extrapolated. W-point controls: at W=.8GeV, two wave/full-Born all angle=0.90324595; W=1GeV=0.89170270; W=1.5GeV=0.87307404.

**Independent numerical controls:** analytic Eq22 vs adaptive direct Eq21 angular integration, maximal relative error <1e-11; two-wave Eq17+18 fiducial fractions vs separately coded complex-spherical-harmonic Y00 and Y22 direct amplitude quadrature in six W points and both zmax=.6,1.0, maximal relative error **4.4409e-16**. Source R68 full-angle exact Born total integrated with predecessor PDG pion mass [2mπ,5GeV] reproduces DAX8 ROT012 historical value **9.097617621183627e-10** as **9.097617621183693e-10 MeV^-2** (relative 7.33e-15). These are source-author mathematical checks, not independent detector/scattering measurements.

**Gauge/threshold controls** (not full physical FSI): directly compute Ward contractions for the published Eq60 projector P^{μν}=g^{μν}(q1·q2)-q2^μ q1^ν, maximum residual **1.71e-17** in original CM momenta. Photon-loop function J_photo of original Eq62 independently checked below/above 2m branch with 65-dps mpmath, max abs difference <2e-13. At threshold J_photo=1-π²/4=-1.46740110027234. IMPORTANT: J_photo is NOT the hadronic loop J_hadronic of predecessor ROT010. Neither actual source Eq65's charge/isospin projected coherent FSI cross section nor f2(1270) resonance has been numerically added to the photon amplitude here.

## Scope, scientific stop, and next discriminator

**Falsified transfer premise:** the source-paper statement of ~90% full-angle Born partial-wave capture cannot be re-used as a 10% or less truncation error estimate for Belle's restricted angular acceptance. The SAME Born two-wave model overestimates its exact Born target around 20% for fiducial bands, even while underestimating its exact 4π target. This is a controlled model-approximation issue, NOT evidence that the original 2025 authors made an error, nor that the resulting full Born+FSI+f2 photo amplitude overshoots measured Belle data by 20%. DAX8 ROT012/017 full exact-Born comparisons remain valid.

Prior 2014 Dai–Pennington fitted photoproduction coefficients, 2025 charged-channel coherent FSI+f2 source model and model/data covariance, original HEPData bytes, actual in-medium pion scatter/decay and first daughter neutrino transport remain NOT RECOVERED here. Next legal scientific turn must source and verify Table2 charge/isospin normalization and coherent interference, recheck no-interaction full Born control under *actual acceptance* before identifying a hadronic production result. No automatic BW write, source owner reassignment or I3 approval.

**LOCAL REPRO SOURCE:** full report plus executed Python, JSON, two CSV, original-source receipt, README, log, 8-member SHA256 manifest and ZIP, fully clean-directory replay 3/3 byte-identical; ZIP CRC PASS, 8/8 member SHA PASS; ZIP SHA256 **00e2612b9da970cb6685cc79c71c1e2ef1694a58901e72f0ceb8b118afac388f**. Local artifact in original DAX9 conversation, not misleadingly represented as a GitHub upload of code or experimental source.

**RETURN: FULL_SCALAR_BORN_EQUATIONS_REPRO_PASS / TWO_PARTIAL_WAVE_TRUNCATION_FULL_VS_FIDUCIAL_SIGN_REVERSAL_PASS / EXACT_PREDECESSOR_R68_BORN_REPLAY_PASS / WARD_AND_PHOTOLOOP_BRANCH_PASS / COHERENT_FSI_F2_PHOTOPRODUCTION_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
