---
artifact_id: IW_DAX_S8_ROT028_REAL_BELLE_PION_ENERGY_ENSEMBLE_SOURCE_FOLD_AND_JENSEN_DECAY_HAZARD_AUDIT_001_20261115
date: 2026-11-15
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
class: ORIGINAL_REAL_SECONDARY_RIVET_BELLE_SOURCE_ENSEMBLE_JENSEN_AUDIT / ANALYTIC_ANGULAR_CONTROL
exposure: PUBLIC
bw: GITHUB_PENDING_BW_INGEST
ceiling: NO_PRIMARY_HEPDATA_BYTES / NO_VERIFIED_ORIGINAL_BIN_SEMANTICS / NO_FULL_PION_QCD / NO_COMPLETE_IN_MEDIUM_PION_STOPPING / NO_FULL_SOURCE_MC / NO_PHYSICAL_NEUTRINO_OR_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT028 — genuine Belle angular source folding versus mean-energy pion approximation in R68

15 November 2026. A source-conditioned scientific scope correction, not a novel result in classical field theory or QED.

FIRSTNESS: DAX-S7 R68 three restricted first gamma-gamma interaction channel rates remain conditional. DAX-S8 ROT017 FIRST retrieved real official **secondary Rivet-data** Belle 140 energy ×12 angular source values; ROT019 first pion LAB pair energy second moment, ROT020 conditional free pion decay neutrino moments, ROT024 ideal massive FD e± thermodynamics, ROT026 point-pion one-photon finite hard Q² pie electron local energy loss, ROT027 energy-updating selected hard pi-e scattering/decay model for **ONE** initial representative Epi=718.277GeV. ROT028 checks the failure mode of replacing the ACTUAL source-energy ensemble by its mean, without repeating a full 140×12 source-wide 500-track MC.

ORIGINAL NUMERIC SOURCE: Belle Mori et al JPSJ76 (2007) 074102 DOI https://doi.org/10.1143/JPSJ.76.074102 and validated Rivet https://www.heprivet.org/analyses/BELLE_2007_I749358/ . The **actual source bytes in full bundle** are official secondary Rivet-data 4.1.2 original YODA3 compressed file BELLE_2007_I749358.yoda.gz SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403, originally obtained with source-provenance ZIP in GitHub Actions ROT017 run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . No claimed byte-equality to PRIMARY HEPData; 140 genuine W values and 140×12 z source values. Source cells W 0.8..1.5GeV, |cosθ*|<=.6. Input W 5MeV and |z| .05 each modeled as **bin-average**: explicit extra assumption, not experimentally certified and not full pion production physics. Actual source 140/140 reconstructed angular-sum rates agree with energy data to <=6e-5 relative from original rounding.

FROZEN PRIOR STATES: ROT020 source conditional pion Emean JSON SHA256 7ebc9d3a08ba9e78e82017ff53a248ffb62d626de64db2addfb5534e77e09f08; ROT024 ideal FD e± JSON SHA256 fa7cf4cd416408a585eb4847fe9e1181e83fdedbcfd61a9dbe9491f31ce9bf2f. R68 E_gamma=1436554MeV, ideal isotropic Planck T=.07818527068831995MeV, pion m=139.57039MeV, cτ=780.45cm, e± number density 4.9953665820687041e26cm^-3. Selected point-scalar pi-e VACUUM one-photon elastic HARD Q² only [.001,.010]GeV² as in ROT026. Actual full finite-temperature dynamic-screened soft/hard matched pion stopping and real composite pion form factor NOT computed.

EXACT SOURCE MODEL TRANSFER: Incident photon ε=T x, u=(1−cosθ_in)/2, y=W²/(4ET)=xu, COM pion z=|cosθ*|, outgoing φ. Define beta_pi=sqrt(1−4mπ²/W²), Q=E_gamma+ε, D=beta_pi[(E_gamma−ε)z+sqrt(4E_gamma ε(1−u))sqrt(1−z²)cosφ]; pooled pion LAB energies (Q±D)/2. Planck x conditional density ∝1/(exp x−1) on x>=y; positive W kernel H(W)=4W³/(4ET)²*[-ln(1−exp(−y))] per linear dW. Directly weight each of 1680 genuine source-angle cross sections, both pion branches, conditional x and φ. Do NOT infer which charge corresponds to signed cosθ from an absolute-z source.

Pion vacuum decay intensity PER CM path κ(Eπ)=M/[cτ sqrt(Eπ²−M²)]. Unlike κ(meanE) take source mean of κ(E). For the selected one-photon pi-e model reexecute λ_hard(E) and b_hard(E) at 141 E-pion grid values spanning 200..1250GeV, cubic interpolate and independently validate 8 off-grid points (relative interpolation error <=9.63e-10 for local loss and <=5.18e-10 for collision rate).

FROZEN SOURCE-CONDITIONAL RESULTS (initial operators, NOT full real cosmic stopping):

| quantity | one prior representative Emean | full REAL Belle/Rivet fiducial source ensemble | relative source correction |
| --- | ---: | ---: | ---: |
| reconstructed Eπ mean, GeV | 718.277144397855 | 718.277144397869 | matching source |
| pion vacuum decay κ, cm^-1 | 2.48975244712632e-7 | **2.81376576604784e-7** | **+13.0138769%** |
| selected hard πe first-event collision λ, cm^-1 | .116806741390608 | **.116760039814053** | **−.0399819%** |
| selected hard πe first local loss b, GeV/cm | .235819456140242 | **.235651083109683** | **−.0713991%** |
| decay before FIRST selected hard pi-e encounter κ/(κ+λ) | 2.13150980033655e-6 | **2.41105004845268e-6** | **+13.1146593%** |

Material deduction: source **mean-energy collapse biases first decay hazard ~13%** despite source mean local selected hard pi-e loss robust to ~.07%. The initial decay first-event P is not eventual charged pion disappearance or muon/neutrino yield; first elastic pi-e event leaves pion alive. The input Eπ source SD is ~231.127752GeV, so a nonlinear decay hazard is not interchangeable with evaluating at its mean.

Source-averaged ONLY-CSDA survival from each starting Eπ to a fixed lower 100GeV energy, evolving κ(E)/b(E) along the restricted model trajectory: S_100(Emean)=**.9984876447259401**, source-average S_100(Einitial)=**.9985317446088173**, absolute +.0000440998828772 (=+.004410 percentage points). ROT027 separately had .99848708146 at Emean with its earlier quadrature; difference ~5.6e−7 numeric, not physical. This is NOT a source-wide DISCRETE source-ensemble pion energy-updating Monte Carlo and NOT a neutrino outcome. Note the initial hazard and survival to fixed lower energy need not change in the same direction because starting energies and travel distances vary.

INDEPENDENT ORIGINAL 48-DIGIT METHOD: In headon high-boost limit, pooled initial inverse-energy hazard relative to κ(Egamma/2) is exactly 1/(1−βπ² z²). Angular integration over a source assumed uniform z bin [a,b] has EXACT primitive [atanh(βπ b)−atanh(βπ a)]/βπ. An independently coded 48digit **different YODA parser** and 8pt W quadrature, requiring no hard πe interpolation and no x/φ averaging, yields:
- headon source inverse-energy ratio **1.13013870716677536717**;
- first βπ² z² moment **0.1035428418872993972**, so keeping only SECOND MOMENT predicts **1.1035428418873**;
- source-conditional higher even z moments add strictly positive **0.026595865279476** (2.6595865 additional percentage points), i.e. second moment alone does not preserve nonlinear inverse-energy decay rate;
- with only each original angular bin's nonnegative integral but arbitrary intra-bin distribution, sharp headon angular bounds **[1.1114002493686674,1.1505345484112936]**. These are source-model angular support envelopes, NOT Belle experimental statistical/systematic CI, primary-source verified bin semantics or physical all-angle hadronic rate bounds.

Primary full nonheadon massive-pion model ratio **1.1301387691356604**, agreeing with headon analytic to the ~5.5e−8 relative scale. The primary full source+lepton spline program executes 4pt W,4pt z,12pt photon Laguerre x, 6pt outgoing azimuth. Negative parser control: an early independent parser assumed all tables have five numerical columns and rejected actual seven-column angular data; corrected to first numeric source value with variable number of error columns. An ambitious simultaneous 6W×5z×16x×8phi extended test hit a runtime cap with NO result. **Do not claim full higher-order convergence PASS**. These corrections and unresolved controls preserved in local SOURCE_AUDIT.

ORIGINAL REPRO PACKAGE: complete original **15-file ZIP** includes original secondary Belle source YODA (SHA pinned), inherited ROT020/024 frozen input and ROT026 original code, complete extended report, two actually executed independent source codes, three frozen result JSON/CSV, README, audit, environment, SHA manifest and self-contained verifier. ZIP CRC PASS; **SHA256 14/14 members PASS**; two clean extracted program replays generate THREE frozen derived files byte-identical PASS. ZIP SHA256 **ecab5ba2cbbea5ef901587ccf619e80a09652b129f6e07e65bc596988dd4f226**. External scientific referee absent, native KN13 BW ingest not checked: GITHUB_PENDING_BW_INGEST.

CLAIM CEILING: no primary HEPData original source bytes, verified joint source covariance or full pion dynamics outside Belle fiducial support; no genuine fully dynamically screened finite-T scalar pion QED or full QCD pion source, hadronic/nuclear competitors, source-wide eventwise pion transport, full muon neutrino source, escaped neutrino spectrum or PBH/BBN bound. No novelty or canon/exec sign or new task cascade.

DISPOSITION: ROT028_REAL_SOURCE_ENSEMBLE_JENSEN_DECAY_13P014_PERCENT_PASS / HARD_LOCAL_STOPPING_MEAN_APPROX_0P071_PERCENT / INDEPENDENT_SOURCE_ANALYTIC_Z_CHECK_PASS / PHYSICAL_COMPLETE_TRANSPORT_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
