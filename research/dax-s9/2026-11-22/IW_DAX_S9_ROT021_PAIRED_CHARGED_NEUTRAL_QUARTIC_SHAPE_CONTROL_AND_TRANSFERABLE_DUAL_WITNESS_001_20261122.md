---
artifact_id: IW_DAX_S9_ROT021_PAIRED_CHARGED_NEUTRAL_QUARTIC_SHAPE_CONTROL_AND_TRANSFERABLE_DUAL_WITNESS_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: INDEPENDENT_BELLE_NEUTRAL_CHANNEL_SOURCE_CONTROL / PRIMAL_DUAL_CERTIFIED_QUARTIC_ANGULAR_GEOMETRY / SINGLE_DUAL_WITNESS_CROSS_CHANNEL
claim_ceiling: NO_PRIMARY_HEPDATA_NATIVE_EXPORT / NO_EXPERIMENTAL_STATISTICAL_CI_OR_PID_CAUSAL_CLAIM / NO_NEW_HADRONIC_AMPLITUDE_FIT / NO_PION_NEUTRINO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT021 — independent original neutral-channel angular control of charged Belle source-central shape

**22 November 2026; source-typed original numerical diagnostic of mature experimental data.** After ROT017 showed a nonzero source-central quartic angular residual in Belle charged data and ROT018 obtained the independent neutral Belle measurement, re-execute the SAME sharp model-class angular-shape test in BOTH channels at precisely common measured W/angle support. No scientific new physics firstness, experimental hypothesis p-value, or primary native event-level data inferred.

## Original source evidence and identity

Original charged author: T. Mori et al, JPSJ76 (2007) 074102 DOI 10.1143/JPSJ.76.074102, author Eq4 ordinary S+D0+D2 unpolarized angular class; original paper already discusses anomalous |cos theta|≈.45-.6 below 1.1GeV and possible charged pion-muon PID/trigger correction problems without identifying a cause. Original neutral author: S. Uehara et al, PRD79 (2009) 052009 DOI 10.1103/PhysRevD.79.052009, original HEPData record https://www.hepdata.net/record/ins815978 source Tables5/6 and separately independent Table31. Original neutral published |cos theta|<.8; restrict to 12 native cells |z|<.6 for matched charged acceptance; DO NOT combine full neutral .8 range with charged .6 range.

Actual authoritative PACKAGED SECONDARY compressed Rivet-data references directly re-opened and SHA256 verified: charged BELLE_2007_I749358.yoda.gz **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**, neutral BELLE_2009_I815978.yoda.gz **65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd**. Original neutral acquisition via separately pinned original official whole RPM SHA in source-only GitHub Actions run 45025075860. Original primary HEPData download bytes HTTP403, thus NOT obtained; experimental covariance and detector event-level posterior not obtained.

Exactly five 20-MeV native neutral W cells with centres W=.85,.87,.89,.91,.93GeV covering source W=[.84,.94]GeV and twenty 5-MeV native charged cells (four per neutral), all 12 native angular densities width delta z=.05. Original inherited R68 *conditional source weighting* H(W)=4W^3/C^2 [-ln(1-exp(-W^2/C))], C=4E_gamma T, E_gamma=1436554MeV, T=.07818527068831995MeV, positive and identically applied to both channels over their exact W intervals. Neutral optional nominal beta_charged/beta_neutral pion mass correction per W cell is angle-constant, so does not change each neutral row normalized shape; verified 5/5. Source YODA nb PER UNIT cos, multiply by .05 ONCE. Direct original authentic raw YODA independently parsed to reconstruct 60×three source cells and reproduced independently frozen original ROT018 CSV to 5e-13 relative PASS; independent neutral original Table31 source total from angular sums 5/5 PASS within maximum .0045nb original printed rounding.

## Exact same source-published wave class and sharp source-central primal/dual

From original unpolarized author ordinary J<=2 S+D0+D2 Eq4: I(z)=|S Y00 +D0Y20|² +|D2Y22|² =a+b z²+c z⁴, z=|cos theta|. Any positive W mixture is STILL a quartic polynomial, though independent parameters/channels may differ. Native exact bin integration G_jk=integral_(.05j)^(.05(j+1)) z^(2k) dz, k0,1,2. For each channel independently minimize TV=.5 sum_j|p_j-(Gtheta)_j| for published positive central bin probabilities p_j, with sum(Gtheta)=1, (Gtheta)_j>=0. LP is a superset of physical waves => lower bound. In both channels actual optimum a>0,c>0,b²<4ac, so construct complex u=sqrt(a), v=b/(2u)+i sqrt(c−b²/(4a)) and I(z)=|u+v z²|² using genuine ordinary S+D0 alone. Thus **sharp bound physically attainable within THIS angular class** but not a genuine QCD or photon amplitude fit.

Independent LP dual: find |lambda_j|<=1 and G^T lambda=mu G^T 1. For ANY normalized model quartic density, functional .5(lambda·p−mu) is a valid lower bound on TV. Both primal and dual match to 1e−12; original exact coefficients and dual lambda,mu frozen JSON; separate Python-STANDARD-LIBRARY ONLY checker independently verifies angle moments and physical representations without calling SciPy optimizer.

**EXACT source-central comparison on COMMON W=.84−.94GeV:**
- Charged sharp TV12 **0.04688212712744671 = 4.688213%**.
- Neutral sharp TV12 **0.004739543697665348 = 0.473954%**.
- Ratio of sharp SOURCE-CENTRAL geometric residual magnitudes **9.89169635687511** — **NOT statistical significance ratio**.
- Leave out only last native angular cell z=.55–.6 and renormalize first 11: charged min TV11 **0.013260590220964465 (1.326059%)**; neutral min TV11 **0.005023003269087167 (.502300%)**. Charged mismatch drops by ~71.7%; neutral does NOT materially decrease.
- Last angular original source central probability charged **0.08907910056730255** (8.907910%) against charged optimal quartic prediction **0.12748581580186996** (12.748582%), deficit **3.8406715pp**. Neutral last source fraction **0.06855912507053367** (6.855913%) equals neutral source-optimal quartic endpoint to numerical accuracy. A fitted polynomial may match an endpoint by optimizer choice; do NOT promote it to a causal detector result.
- Original native source high angle z=.4-.6 central share charged **40.306087%**, neutral **28.692075%**; direct cross-channel TV12 of two normalized measured central source shapes **11.6140117%** (not a physics amplitude distance).
- **SINGLE dual witness applied unchanged to INDEPENDENT source:** original lambda and mu determined solely from charged data, with G^T lambda=mu G^T 1, yield exact contrast W_charged=**0.04688212712744673 (4.688213%)**, W_neutral=**0.0001901112417959025 (0.019011%)**. This annihilates all normalized quartic-model predictions and localizes an independent source-central difference. Chosen on charged data so NOT preregistered experimental test. No significance ratio inference.
- Primal-dual gaps charged **2.08e−17**, neutral **8.40e−16**, both optimal polynomials explicitly realisable as S+D0 amplitude squares.

**Individual original source W bins:** matched center W=.85,.87,.89,.91,.93GeV: sharp TV12 charged=(5.7269,4.8756,4.2401,4.3251,4.4944)% vs neutral=(1.8308,1.1692,1.4548,2.3990,1.7654)% respectively. Charge-endpoint negative residual all 5 original energy regions, ranging −4.6811pp to −3.0137pp; neutral source-optimal quartic fits each endpoint within numerical tolerance. This supports source central *across-W persistence*, but neighboring neutral W after unfolding correlated and not independent hypothesis rejections.

**IMPORTANT scope transfer:** ROT017's charged source TV12 4.4806% used W=.85−.95GeV, NOT same W support; current correctly matched charged W=.84−.94 yields 4.6882%. ROT020's earlier 3.7115% relaxed Watson-S additive residual is a DIFFERENT functional and retains its original declared necessary-condition ceiling. No conclusion here that ROT020 R equals a measured physical D0 or D2 intensity. No source-backed new strong partial wave fit.

## Limitations and decision

The neutral Belle low-W angular per-bin marginal statistical/systematic errors are large compared with many charged relative errors. Different neutral photon reconstruction, energy-unfolding and charged trigger/PID corrections, and the lack of actual joint experimental angular covariance mean **THE NUMERICAL TENFOLD SOURCE-CENTRAL DIFFERENCE IS NOT TENFOLD EVIDENCE OR A STATISTICAL REJECTION**. Could reflect real charged vs neutral hadronic dynamics, source point biases, smooth W averaging of independent experimental noise or a mixture. Charged–neutral true photoproduction fit needs helicity phases and partial waves as well as experimental correlated nuisances. No transfer to pion plasma, neutrinos, PBH/BBN.

**Local full original executable reproduction ZIP:** DAX9_ROT021_Paired_Belle_Neutral_Control_Sharp_Quartic_Dual_Repro.zip exact **SHA256 d4ca1fa6d0697c7c19bc6ab8fc190041be5c9862975abe77a71013653386d31a**, ZIP CRC PASS, **13/13 payload member SHA256 PASS**, two separate clean-directory reexecutions each original Python reparser/LP + independent standard-library checker PASS and **3/3 newly generated JSON+2 CSV bytes identical per run**. Bundle contains the two genuine source compressed YODA assets, original ROT018 frozen CSV, primary executing code, separate independent source/certificate checker, original full 13k science report, JSON+CSV, receipt, README, run and replay logs, SHA manifest. GitHub report is TEXT ONLY not code/data ZIP upload.

**RETURN: SOURCE_AUTHENTICATED_PAIRED_BELLE_PASS / SHARP_CROSS_CHANNEL_PRIMAL_DUAL_PASS / NEUTRAL_NEGATIVE_CONTROL_SOURCE_CENTRAL_PASS / FIXED_CHARGED_DUAL_WITNESS_TRANSFER_PASS / NO_STATISTICAL_SIGNIFICANCE_OR_PID_CAUSE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**