---
artifact_id: IW_DAX_S8_ROT030_REAL_BELLE_SOURCE_CONDITIONAL_FIRST_NEUTRINO_ENERGY_TAIL_AND_MOMENTS_001_20261116
date: 2026-11-16
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
type: PUBLIC_SCIENTIFIC_RETURN
source_class: REAL_SHA_PINNED_SECONDARY_RIVET_BELLE_140x12 + RESTRICTED_PION_PI_E_HARD_Q2_CSDA + TWO_BODY_PI_MU_NU
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_PRIMARY_HEPDATA_BYTES / NO_PROVEN_SOURCE_BIN_AVERAGES / NO_FULL_QCD_PION_SOURCE / NO_FULL_MEDIUM_PION_STOPPING / NO_SOURCE_WIDE_DISCRETE_MC / NO_SECONDARY_MUON_DECAY_OR_NEUTRINO_ESCAPE / NO_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT030 — Real Belle source conditional first pion-decay neutrino spectrum, heavy rare tail, moment falsifier

**16 Nov 2026.** A new source-conditioned combined calculation **within DAX-S8**, but classical pion decay and CSDA transport mathematics, NOT new particle physics or experimentally physical cosmic neutrino prediction.

## Prior results, original sources, actual limits

DAX-S7 R68 was originally restricted to three specific gamma-gamma first-muon channels. DAX-S8 ROT017 FIRST recovered actually measured and authenticated numerical Belle/Rivet SECONDARY official package reference (140 W values ×12 angular values), ROT019 LAB pion asymmetry, ROT020 conditional free pion->mu nu first daughter moments, ROT024 true massive FD residual e± density, ROT025 static Debye screen, ROT026 restricted point-pion vacuum one-photon hard Q² πe energy-transfer moment, ROT027 energy-dependent restricted hard πe scatter/decay (500+200 original fixed-E Monte Carlo plus CSDA), ROT028 source-folded initial decay +13%, and ROT029 actual source-folded **CONTINUOUS-SLOWING** pion decay-energy distribution/semigroup memory factor. ROT030 transports the ROT029 **full source conditional parent DECAY-energy distribution through two-body pion->mu neutrino kinematics**, testing the high-energy daughter tail and second moment. It does NOT rerun real pion physical transport.

Belle original paper T. Mori et al, JPSJ 76 074102 (2007) DOI https://doi.org/10.1143/JPSJ.76.074102 , validated Rivet https://www.heprivet.org/analyses/BELLE_2007_I749358/ . Authentic numerical SECONDARY official Rivet-data YODA gzip 29,215 bytes, SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**, acquired original verified native GitHub Actions https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . Original HEPData PRIMARY bytes have NOT been verified and source W 5MeV and |z| .05 bin-vs-point semantics/covariance NOT established. **ALL** following rates are conditional on positive source values interpreted as W/z uniform cell-average cross sections in Belle-only W=.8..1.5GeV, |cosθ*|<.6. They do not extrapolate real physical QCD pion sources outside this acceptance.

Physics charged pion original PDG 2025 https://pdg.lbl.gov/2025/tables/rpp2025-tab-mesons-light.pdf : m_pi=139.57039MeV, spin0, cτ=7.8045m. Muon m=105.6583755MeV. PDG original radiative-inclusive mu nu(γ) branch 99.98770%, https://pdg.lbl.gov/2025/reviews/rpp2025-rev-pseudoscalar-meson-decay-cons.pdf ; this is NOT equal to an exactly nonradiative exclusive branch probability. Condition explicitly on free two-body pion decay **IF and WHEN the modeled pion reaches its actual decay energy**, excluding all radiative modes, pion nuclear/photo competing channels, secondary muon polarization-decay and neutrino propagation.

Inherited exact ROT020 source machine JSON SHA256 7ebc9d3a08ba9e78e82017ff53a248ffb62d626de64db2addfb5534e77e09f08, ROT024 massive FD e± machine JSON SHA256 fa7cf4cd416408a585eb4847fe9e1181e83fdedbcfd61a9dbe9491f31ce9bf2f. Source R68 photon Eγ=1436554MeV, Planck T=.07818527068831995MeV, modeled e± number density 4.995366582068704e26cm^-3. Only **author-chosen, selective** invariant Q²=[.001,.010]GeV² in point-pion F_pi=1 **vacuum t-channel QED elastic πe±** on moving massive ideal FD targets is included, plus vacuum pion decay. Static ROT025 screening is not a physical stopping power; NO dynamic longitudinal/transverse finite-T photon propagator, all soft/hard matching, full pion structure or actual hadronic processes included.

## Exact analytic source-to-decay-to-first-neutrino map

Original 140×12 source-weighted W/z values, exact Planck collision bath x|W and non-head-on COM-to-LAB conversion, and both π± outgoing energies give **3,870,720** positive source-weighted initial pion energies E0 (finite quadrature range [295.7402,1140.8171]GeV, NOT mathematical Planck support; mean 718.277144397869GeV, SD 231.127752GeV).

Define κ(E)=mπ/[cτ sqrt(E²−mπ²)] per pion LAB path, positive selective source-modeled energy-loss b(E) from ROT026/027 and CSDA S(E|E0)=exp[−∫_E^E0 κ(u)/b(u)du] for E≤E0. For weighted original source law w(E0), decay-parent CDF exactly in this CSDA:
Fπdec(E)=∫_{E0<E} w(dE0)+∫_{E0≥E}w(dE0)S(E|E0).
Its density p(E)=κ(E)/b(E)×∫_{E0≥E}S(E|E0)w(dE0). This preserves full source early-decay tail and avoids identifying the 13% INITIAL hazard correction with an entire final spectrum change.

Conditional NONRADIATIVE spin0 two-body pion decay (neutrino mass≈0), f=(mπ²−mμ²)/(2mπ²)=**0.21345602681111262** and pπ=sqrt(E²−mπ²):
Eν=f(E+pπ cosθ*), cosθ* uniform [-1,1].
Thus Eν|E uniform on [f(E−pπ),f(E+pπ)]; E[Eν|E]=fE; E[Eν²|E]=f²(4E²−mπ²)/3. For any a≥0 the exact source-CONDITIONAL daughter survival P(Eν>a) is the parent decay-energy density integral of clip{[f(E+pπ)−a]/(2f pπ),0,1}. Higher daughter-tail raw moments follow exact elementary integration over this uniform interval. This is textbook kinematics, not a new theorem.

## Executed complete source-conditioned numbers

Primary REAL source W/z and nonheadon Planck with selected pion CSDA source and grid n=12001 (36×28 massive FD pion hard loss quadrature):

| Conditional modeled observable | result |
|---|---:|
| Parent pion median energy AT DECAY (ROT029) | ~1.7824GeV |
| Parent pion MEAN energy at decay | **2.441979080 GeV** |
| Parent pion second moment E² at decay | **220.694156586 GeV²** |
| **One first daughter neutrino MEDIAN energy** | **0.391921810 GeV** |
| **One first daughter neutrino MEAN energy** | **0.521255152 GeV** |
| One neutrino raw second moment Eν² | **13.40716117 GeV²** |
| **One neutrino SD** | **3.624286721 GeV** |
| Neutrino 90th/95th/99th percentiles | **0.719993 / 0.811627 / 1.193398 GeV** |
| **Neutrino 99.9th percentile** | **32.526735 GeV** |
| P(Eν>1GeV) | **1.805226%** |
| P(Eν>10GeV) | **0.188702%** |
| P(Eν>100GeV) | **0.032780%** |
| P(parent π decays at energy>100GeV) | **0.146881%** |

MATERIAL RELATIVE RARE-TAIL SECOND MOMENT: only 0.1887% of first neutrinos have Eν>10GeV but this tail contributes **21.155% of first-neutrino unconditional MEAN energy** and **97.938% of unconditional Eν² second moment**. An even rarer 0.03278% with Eν>100GeV contributes **10.456% of mean energy** and **76.569% of raw Eν²**. High tail strongly controls variance, so sample medians and limited Monte Carlo do not certify the energy budget.

Source-vs-representative-average-E0 test: same entire pion stopping/decay model with initial E0 replaced by source mean 718.277144GeV gives Eνmean **0.521272927GeV** vs real-source **0.521255152GeV** (−0.003410%); but Eν² **12.18357012** vs source **13.40716117 GeV²** (**+10.04296% relative to simplified mean-initial-energy model**). Thus ROT029 near-equal decay parent medians DO NOT guarantee even an approximately equal daughter second energy moment. Source initial Jensen hazard +13% from ROT028 likewise must NOT be interpreted as +13% of cosmic daughter yield.

ROT020 hypothetical instantaneous FREE pion decay neutrino average **153.320585GeV** vs this strongly cooled restricted hard πe CSDA **0.521255GeV** is a factor **294.14** conditional MODEL COMPARISON, NOT an actual early-universe neutrino suppression ratio, not a statement of cosmic transport efficiency, and not a measured source.

## Independent numerical controls and strict negative records

PRIMARY: actual original secondary source SHA, 3.87M positive nonheadon W,z,x,φ,± initial pion lab-energy samples; original inherited source-verified ROT029 CSDA kernel reexecuted. Grid n3501/7501/12001 yields neutrino mean (GeV) **.521256700/.521255377/.521255152**, SD (GeV) **3.624286717/3.624286730/3.624286721**, P(Eν>100GeV) **.000327793864/.000327795384/.000327796507**, 99.9th quantile **32.52656/32.52666/32.52673GeV**. Pion mean and second moment independently computed by survival-CDF integration by parts and direct decay-density quadrature; agree to numerical sensitivity ~1e−5 for mean and ~2.6e−5GeV² for E². Finite-grid decay-density integral = **0.99999629** vs mathematical one: residual ~3.7e−6 at n12001, explicitly NOT represented as an exact normalized PDF. Daughter moment identity uses CDF integration for most stable moment calculation.

INDEPENDENT: separately written original YODA parser, **215,040 W/z head-on source kinematics** with 8pt W ×8pt z and independent inherited original ROT027 mass-FD pi-e hard kernel 48×36 plus n7501 CSDA: parent mean **2.441979993GeV**, parent E² **220.694070105GeV²**, one neutrino mean **0.521255347GeV**, Eν² **13.407155916GeV²**, SD **3.624285968GeV**, median **0.391919863GeV**, P(Eν>10)=.0018870180, P(Eν>100)=.0003277982. Head-on differs in original source initial mean (718.2770000 vs nonheadon 718.2771444GeV) by omission of thermal bath photon energy; not a code failure.

Original ROT027 500 fixed-initial-E discrete tracks had pion decay-energy sample mean2.748GeV vs source-CSDA expectation2.442GeV, not a controlled source-ensemble MC comparison. Rare early event and 500 samples have large uncertainty: CSDA model parent variance about 215GeV², rough 500-sample SE ~.66GeV. Moreover CSDA misses individual ~18%-E jumps near the 1.8GeV pion-decay regime. NO claim of source-wide discrete MC/rare-tail validation from 500 tracks.

## Full reproducing artifact and exact ceiling

Original complete conversation archive **DAX_S8_ROT030_Belle_CSDA_First_Neutrino_Rare_Tail_20261116.zip**, 20 members ZIP CRC PASS, **19/19 SHA256 content hashes PASS**, 3 independently implemented author programs replay and generate **five byte-identical results** in clean directory from SHA-pinned original YODA source; ZIP SHA256 **6c15c0545522cfb7163a90f4818357cec663aa4ae7f3d7fd88cf58cc92ff63db**. Includes original source YODA, original ROT020/024 input JSON, inherited actual ROT029 full nonheadon and separate original ROT027 kernel, primary and independent code, results JSON, daughter-tail CSV, extended original 13k report, source audit, README, SHA manifest, verifier; no opaque 35MB NPZ used. AUTHOR reproduction, NOT external scientific referee. All source claims confined to already stated limits.

**STOP:** no PRIMARY original HEPData byte identity, verified original W/z bin semantics/covariance, complete pion production amplitudes outside Belle W/z; no correct full dynamic-screened scalar pion finite-T QED soft+hard rate, no πγ/πN/πA or actual BBN network; no full source-WIDE discrete energy-changing pion trajectories, polarized muon daughter distribution and neutrino escape/deposition. No actual physical cosmological neutrino spectrum or PBH/BBN claim, no task cascade or native KN13 BW ingestion read receipt.

**RETURN:** ROT030_SOURCE_TYPED_FIRST_NEUTRINO_CSDA_MOMENTS_PASS / RARE_HIGH_ENERGY_TAIL_DOMINATES_SECOND_RAW_MOMENT / SOURCE_MEAN_INITIAL_ENERGY_SECOND_MOMENT_BIAS_PLUS_10P043PCT / INDEPENDENT_HEADON_REPLAY_PASS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
