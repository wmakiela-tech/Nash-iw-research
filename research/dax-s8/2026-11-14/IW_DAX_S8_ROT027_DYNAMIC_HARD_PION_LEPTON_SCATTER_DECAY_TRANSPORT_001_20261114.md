---
artifact_id: IW_DAX_S8_ROT027_DYNAMIC_HARD_PION_LEPTON_SCATTER_DECAY_TRANSPORT_001_20261114
date: 2026-11-14
cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
type: ORIGINAL_AUTHOR_RESTRICTED_DYNAMIC_TRANSPORT_RETURN
exposure: PUBLIC
bw: GITHUB_PENDING_BW_INGEST
scope: POINT_SCALAR_ONE_PHOTON_Q2_HARD_ONLY / IDEAL_MASSIVE_FD_LEPTON_PLASMA / TWO_PROCESS_SCATTER_DECAY
claim_ceiling: NO_PHYSICAL_COMPLETE_PION_STOPPING / NO_SCREENED_DYNAMIC_FULL_SOFT_HARD_MATCH / NO_REAL_COMPOSITE_FPI / NO_HADRON_NUCLEAR_OR_PHOTON_COMPETITORS / NO_FULL_SOURCE_PION_ENERGY_DISTRIBUTION / NO_NEUTRINO_ESCAPED_FLUX_OR_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT027 — dynamic energy-changing hard π±e± elastic scattering vs pion decay at R68

**14 November 2026.** Author-scoped FIRST source-model dynamic test in this DAX-S8 line, not novel QED or a complete early-universe transport model. Previous DAX-S7 R68 was a 3-channel *restricted* gamma-gamma first-muon question. DAX-S8 ROT017 FIRST recovered secondary official SHA-verified Rivet/Belle original numeric 140×12 reference; ROT019/020 extracted conditional charged-pion LAB energy and FREE pion-decay daughter muon-neutrino moments, ROT024 established ideal massive equilibrium FD e± plasma; ROT025 static Debye mass and regime warning; ROT026 first fixed-energy, finite hard Q², moving massive FD pion–electron transfer moment. ROT027 takes ROT026's restricted source *energy-dependent* kernel and explicitly updates E and decay hazard AFTER EVERY simulated collision.

## Source custody, literature, explicit limited model

- Pion INITIAL energy E0=**718.2771443978551975GeV** is one reconstructed **fiducial Belle/Rivet ROT020 source-conditional average**, NOT a complete pion energy spectrum. Frozen actual ROT020 source JSON SHA256 **7ebc9d3a08ba9e78e82017ff53a248ffb62d626de64db2addfb5534e77e09f08**. The underlying secondary Rivet YODA was authenticated in ROT017, but ORIGINAL primary HEPData byte equality and source bin semantics remain OPEN.
- Stationary ideal e± **PLASMA temperature T=0.07818527068831995MeV**, combined lepton density n_e++n_e−=**4.9953665820687041e26/cm³**, m_e=0.51099895069MeV (ROT024 source state SHA256 **fa7cf4cd416408a585eb4847fe9e1181e83fdedbcfd61a9dbe9491f31ce9bf2f**). Neither primordial nuclear composition nor full finite-T photon self-energy was implemented.
- Vacuum pion M=139.57039MeV and cτ=7.8045 metres from original PDG charged pion listings https://pdgprod.lbl.gov/pdgprod/pdgLiveJson/DataBlock.action?node=S008M and https://pdg.lbl.gov/2020/download/db2020.pdf .
- Mature original one-photon pion–electron QED/radiative corrections: N. Kaiser, J.Phys.G38(2011)025003 DOI https://doi.org/10.1088/0954-3899/38/2/025003 ; standard CSDA and straggling are established in Gebäck/Asadzadeh (2012) DOI https://doi.org/10.1080/00411450.2012.671207 . No theoretical novelty claim.

ACTUAL modeled elastic collision is strictly **point pion** F_pi(-Q²)=1, single vacuum t-channel photon, spinor lepton of full mass, positive invariant transfer Q² in the **AUTHOR-CHOSEN [0.001,0.010]GeV²** only. No dynamic photon screening, soft/hard matching or true pion electromagnetic form factor; excluded photon/nucleon/nucleus collisions and radiation are not silently counted.

For s=M²+m²+2(E eps−p k μ), lambda=[s−(M+m)²][s−(M−m)²], p=sqrt(E²−M²), incident massive-FD lepton eps=sqrt(k²+m²), the exact one-photon Born differential is

dσ/dQ² = (4π α²/lambda)*[(s−M²−m²)²−Q²(s−m²)]/(Q²)²,

for 0<=Q²<=lambda/s; use upper=min(0.010,lambda/s), lower=0.001 GeV². Incident flux factor per pion LAB path is sqrt(lambda)/(2p eps). Pion electron LAB transfer after final COM azimuth phi is updated eventwise. The exact final-azimuth mean gain is

<G>_phi=Q²[(E+eps)(s+m²−M²)−2s eps]/lambda.

Draw incoming lepton k, μ weighted by thermally averaged elastic event rate, Q² by its actual differential kernel (rejection sampled from Q^-4 measure), outgoing phi uniform, then update E'=E−G with E'>=M checked. Draw competing path length from exponential intensity lambda_hard(E)+kappa_decay(E), where **kappa_decay(E)=M/[cτ sqrt(E²−M²)] per LAB length**. Recompute collision and decay intensities at each new E; elastic collision does NOT kill pion.

## Distinct mathematical transport algorithms and positive results

(A) **CSDA** on exactly the same numerically reevaluated one-photon kernel b(E)=expected LAB energy loss per unit path:
dE/dell=−b(E); S(E)=exp[−∫_E^E0 kappa_decay(E')/b(E') dE'].
This APPROXIMATES stochastic collision jumps as continuous. CSDA source-moment checkpoints:
- b(718.277GeV)=**0.235819456140115GeV/cm** and lambda_hard(E0)=**0.116806741390573/cm**, matching ROT026.
- b(100GeV)=**0.226859287GeV/cm**; b(20GeV)=**0.157227023**; b(5GeV)=**0.015542535**; b(2GeV)=**0.0000875178** GeV/cm. Initial stopping is NOT constant.
- Path to 100GeV **26.41315344m**; S(no decay to 100GeV)=**0.99848708146**. To 20GeV path **30.21836497m**, survival **0.99706331731**; to 5GeV path **32.38793012m**, survival **0.99239611750**.
- CSDA median decay energy **1.78254516893GeV**. Here 36×28 thermal/incident quadrature and 1100 log-energy nodes.
- **Dynamic first-hard-collision/decay instantaneous equality** lambda_hard(E*)=kappa_decay(E*) at **E*=1.795145972GeV**, each selected first-event mean free path ~100metres. Independent 20×16 and 48×36 quadratures give E* 1.79561053 and 1.79535924GeV, respectively. At this energy the single-event average loss is ~18% of parent E, so small-jump CSDA becomes invalid for *individual* trajectories.
- Quadrature sensitivity: S(100GeV) with 20×16,36×28,48×36: 0.99848701316,0.99848708146,0.99848703369. These are MODEL numerical controls, not physical uncertainties.

(B) **Exact restricted discrete scattering + decay event sampling**: seed **20261114**, 500 histories with eventwise recomputation of rates and outgoing COM azimuth. Frozen results:
- median pion energy at vacuum decay **1.72365139869GeV**, 10–90% quantiles [1.37962356,2.19779779]GeV;
- median path to decay **107.85041159m**; median selected hard event count **366**, mean 364.944.
- Bootstrap 95% interval for the FINITE-SAMPLE estimator of the median with 3000 fixed-seed resamples **[1.6866687603,1.7557379785]GeV**, NOT experimental, model or cosmic uncertainty.
- ONE of 500 histories decays above 100GeV; observed p=0.002 but exact Clopper-Pearson 95% interval for this narrow model event **[0.0000506343,0.011092477]**; strongly under-resolved rare tail. Sample mean energy at decay 2.748GeV is dominated by a rare early event and is not promoted as physical energy or neutrino yield.
- Additional separate seed **20261116**, 200 histories with independent finer 48×36 thermal quadrature, median energy at decay **1.78820940244GeV**, 10–90% [1.38764403,2.43377086]GeV. This checks sensitivity to MC seed/grid using the SAME physical kernel; not an external refereed second model.
- Source eventwise k/μ/Q²/phi sampler 4000 draws at E0 gives mean event LAB loss **1.9664814GeV**, MC standard error **0.02729166GeV**, vs analytic first moment **2.01888567GeV** (within 2 standard errors). The initial numerical model rate/moment was also independently validated in ROT026 by direct triple quadrature with full massive leptons.

## Negative knowledge, reproducibility, STOP

- CSDA is not a substitute for discrete energy jumps near E=1.8GeV: single restricted hard event means ~18% of E.
- Mere encounter does not destroy the charged pion; neither initial tiny decay-before-FIRST-hard-event probability from ROT026 nor these source-model final energies determine a real physical surviving-neutrino flux.
- Larger N900/1000/1200 test executions hit the local runtime cap; DO NOT report as completed. Fully executed 500+200 histories only.
- Initial CSV parser accidentally used both names=True and skip_header=1, dropping one history; detected with exact 501 CSV lines (header+500), corrected. Nondeterministic runtime field removed from frozen JSON; two full methods now write deterministic outputs.
- Real physics still requires all longitudinal/transverse finite-T QED hard/soft matching, realistic Fπ and radiation, all pion interactions with photons/nucleons/nuclei, BBN nuclear composition and dynamical bath, the full real source pion energy distribution, pion/muon decays, and neutrino escape/deposition. These are OPEN and no PBH/BBN bound or novelty claim follows.
- Author original full **16-file ZIP** includes three original SHA-pinned prior machine JSONs, original published ROT026 compact baseline code, full dynamic and statistical programs, all **four frozen CSV/JSON outputs**, report, audit, README, SHA manifest and verifier. ZIP CRC PASS, **14/14 per-member SHA256 PASS**, new clean unpacked replay scripts generated FOUR byte-identical data results (verified against independent temp extraction). Full package ZIP SHA256 **f92995b8c66381a556885137666bac0e271fe3d37c8eab47d7fc6398578ea175**. This is author reproduction, NOT independent referee or native BW ingestion.

**Disposition:** ROT027_DEFINED_DYNAMIC_SCATTER_DECAY_PASS / SOURCE_CROSSOVER_ESTAR_1P795GEV / DISCRETE_MC_500_PLUS_200_REPRODUCED / CSDA_SMALL_JUMP_BREAKDOWN_NEAR_DECAY / FULL_PHYSICAL_PION_STOPPING_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
