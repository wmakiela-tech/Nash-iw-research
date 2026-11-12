---
artifact_id: IW_DAX_S8_ROT013_BELLE_FIDUCIAL_R68_BORN_COVERAGE_AND_NONIDENTIFIABILITY_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: PRIMARY_BELLE_EXPERIMENTAL_SUPPORT_CONTACT / EXACT_BORN_ANGULAR_PRIMITIVE / PLANCK_FIDUCIAL_SUPPORT_FRACTION / CONDITIONAL_NONIDENTIFIABILITY
claim_ceiling: NO_BELLE_RAW_NUMERIC_ROWS_READ / NO_FULL_QCD_AMPLITUDE / NO_EXPERIMENTAL_PION_RATE / NO_PBH_BBN_BOUND / NO_NEUTRINO_DEPOSITION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
reproduction: LOCAL_AUTHOR_HIGH_PRECISION_PLUS_INDEPENDENT_ORIGINAL_FORM_QUADRATURE / NONBLIND
---

# DAX-S8 ROT013 — Belle 2007 fiducial support versus R68 charged-pion Born hazard

12 November 2026. **The 19.557% number is a mathematical coverage fraction of the point-pion Born source model, NOT a measured physical pion rate and NOT a model-independent estimate of what Belle measured.**

## Precedence and bounded currentness

DAX-S7 R68 first documented a strictly conditional first-muon-event probability among ONLY three photon processes. DAX-S8 ROT012 first added a toy fourth source-model gamma gamma -> pi+pi- Born competitor and obtained P_mu(3 channels)=0.0864939970805744 versus P_mu(4 channels)=0.0857784504994348, relative change -0.82728%. ROT012 explicitly did NOT claim a true strong-interaction rate. ROT013 investigates the direct experimental coverage gap in that source model, not a new model of pion hadronic dynamics.

Bounded 12 Nov Slack/GitHub source check: current external science owner is successor XH-S6 (explicitly activated); previous XH-S5 had ACKNOWLEDGED the separate QED 4e source request. No new acceptance of a pion source task or native complete 4e amplitude output found in checked returns; search no match is NOT proof of absence. Other active NASH authors MT15/Mech own their respective Wu-Xu hadronic source work; do not duplicate or presume their scientific acceptance.

## Original sources and what was actually opened

- Klevansky, Lemmer, Beygi, *Eur. Phys. J. A* 61,49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 . Original full publisher HTML Eq.(21) charged-pion Born d sigma/d Omega and Eq.(22) angular integrated sigma_B, plus Fig.10 comparing Born-only and strong-interaction-inclusive amplitude curves, were inspected. Their hadronic full-model amplitude WAS NOT run.
- Belle Collaboration / Mori et al., *J. Phys. Soc. Jpn.* 76,074102 (2007), DOI https://doi.org/10.1143/JPSJ.76.074102 , arXiv:0704.3538. Experimental gamma gamma -> pi+pi- energy W in [0.8,1.5] GeV; charged-track angular acceptance |cos(theta*)|<0.6 (gamma-gamma COM), also stated explicitly by Belle review DOI https://doi.org/10.1093/PTEP/PTS072 .
- ORIGINAL HEPData https://www.hepdata.net/record/ins749358 , submission DOI https://doi.org/10.17182/hepdata.51842.v1 . Record and Table 1 (labelled Total cross section) plus differential table inventory OPENED. **Numerical CSV/JSON table rows NOT OPENED** due to cache miss; the label Total does not certify unrestricted 4pi acceptance. No experimental numeric cross section is reused in these calculations.
- Dai/Pennington, *Phys. Rev. D* 90,036004 (2014), DOI https://doi.org/10.1103/PhysRevD.90.036004 , arXiv https://arxiv.org/abs/1404.7524 . Original abstract/source synopsis inspected. Existing prior-art dispersive/unitary/analytic amplitude analysis of charged and neutral pion and kaon photon-fusion data directly identifies why incomplete angle/polarization acceptance needs extra physics assumptions. No amplitude kernel imported or reproduced here.

## Exact source-model angular integral

At s>=4m_pi^2 with b=sqrt(1-4m_pi^2/s), z=cos(theta*), original source Eq21 has:

 d sigma_B/dz = pi alpha^2 b/s * F(b,z),
 F(b,z) = ((1-b^2)/(1-b^2 z^2))^2 + (b^2(1-z^2)/(1-b^2 z^2))^2.

An exact primitive, verified by differentiation back into the original Eq21, is

 I(b,z) = z + (1-b^2)^2*z/(1-b^2*z^2) - (1-b^4)*atanh(b*z)/b,

with I(0,z)=z. Therefore sigma_B(s;|z|<z0)=2*pi*alpha^2*b/s * I(b,z0), and z0=1 recovers source Eq22 exactly.

Set the inherited R68 photon E=1436554 MeV, ideal Planck T=0.07818527068831995 MeV and m_pi=139.57039 MeV. For incident isotropic photon bath, source-collision variable y=(epsilon/T)*(1-cos theta_inc)/2, s=4ET*y. Exact positive Fubini integration over incident photon relative-flux angular weight gives

 K_B(W1,W2;z0) = integral_{W1^2/(4ET)}^{W2^2/(4ET)} 2y[-ln(1-exp(-y))] * sigma_B(4ETy;z0) dy.

The full source-model rate is W>=2m_pi, z0=1. Belle fiducial support in the model is 800<=W<=1500 MeV and z0=0.6. These are mathematical fractions of this DEFINED model, not HEPData counts.

## 48-digit author computation and independent original-form control

Common unnormalized collision-hazard units; overall constants cancel in fractions.

| Born model energy/angle domain | K | Fraction K/K_all |
|---|---:|---:|
| ALL W>=2m_pi and ALL pion CM angles | 9.0976176211836268e-10 | 1 |
| W<0.8 GeV, all angles | 6.2678087498847257e-10 | 0.688950559461880895 |
| 0.8<=W<=1.5 GeV, all angles | 2.7428397222189587e-10 | 0.301489888499194492 |
| W>1.5 GeV, all angles | 8.6969149079942430e-12 | 0.0095595520389246133 |
| Belle JOINT support: 0.8<=W<=1.5GeV, |z|<0.6 | 1.77923637803288135e-10 | 0.195571681743357055 |

Thus complete Born model / Belle-joint Born model = 5.1132147102578505. Born contribution lying OUTSIDE Belle's joint energy+angle support = 0.804428318256642945, or 80.4428318257%. Within the Belle W energy window, the angular source acceptance fraction is 0.64868404946151146. About 68.8951% of the uncut Born-model collision hazard comes from W<0.8GeV — below the Belle experimental dataset's lower edge; ROT012 median COM was ~0.644GeV.

Math validation:
1. Executable original Eq21 closed-primitive mpmath 48-digit integral with pointwise exact derivative checks at W=300,400,644,800,1000,1500,3000MeV. Analytic bound on omitted y>=120 source tail: <2.285e-61 in unnormalized rate units.
2. A separately written SciPy algorithm directly integrates the ORIGINAL Eq21 angular differential numerically within the Planck y integration and does NOT import the closed form. All five raw K values independently reproduce to better than 2e-10 relative; in practice precision is much better.
3. Local nine-member ZIP original full Markdown report + two original code forms + two frozen JSONs + source audit/README + SHA256 manifest + independent replay validator. ZIP CRC PASS, 8/8 file SHA256 PASS, exact clean-extract byte-identical JSON reruns PASS. Original ZIP SHA256 3a86864e1bdeea49fa7d13f458d6d84922ab33b29af833bd16f22aba4af5273e. These are AUTHOR-controlled reproducibility tests, not an independent external physics audit.

## Exact limitation / falsifier

**FALSE if presented without additional theory:** measured Belle data on the limited W,z region alone uniquely identify the complete R68 pion collision hazard. Under only NONNEGATIVITY + FIDUCIAL SOURCE DATA, construct sigma_lambda(W,z)=sigma_base(W,z)+lambda*h(W,z), lambda>=0, with h>=0 smooth, supported strictly in W<0.75GeV. All lambda match source on Belle domain exactly, but complete thermal hazard changes with lambda because the low-W bath weight is positive. This proves nonidentifiability under those explicitly weak assumptions. The counterfamily is **not asserted physically admissible under hadronic unitarity, analyticity or QCD**; such further constraints are exactly why the Dai–Pennington program matters.

**TRUE under source model only:** if the differential pion law were exactly the Klevansky point-scalar Born distribution, 19.557% of its rate in R68 lies in Belle's measured W and scattering-angle support.

NOT TRUE from this work: that 19.557% of PHYSICAL real hadronic events were measured, that point-pion Born upper or lower bounds the full coherent amplitude, or that the experimentally measured Belle cross sections were numerically fitted here. No charged pion decay muon/neutrino yield, lab transport or PBH/BBN bound.

## Next discriminating source-native step, not assigned by this return

Before any physical upgrade, read numerical HEPData table rows with uncertainty and exact acceptance, select a version-pinned published unitary/dispersive gamma gamma -> pi pi amplitude with its finite-W and full angular extension (including below W=0.8 GeV and above 1.5GeV support), run source-native Planck/isotropic convolution and record model uncertainty/edge tails. Only then transfer to hadron-transport targets with an explicit scientific owner and physical time horizon. The existing XH-S5 QED 4e source ACK is not a pion-amplitude assignment; XH-S6 is successor but no new owner acceptance is inferred.

DISPOSITION: BORN_JOINT_FIDUCIAL_SUPPORT_EXACT_PASS / REAL_BELLE_SOURCE_WINDOW_VERIFIED / HEPDATA_NUMERIC_ROWS_NOT_OPENED / PHYSICAL_PION_RATE_OPEN / BW_GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
