---
artifact_id: IW_DAX_S8_ROT020_REAL_BELLE_PION_TO_MUON_NEUTRINO_FIRST_DECAY_MOMENT_TRANSFER_001_20261113
date: 2026-11-13
cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
class: REAL_BELLE_140x12_TO_TWO_BODY_FIRST_NEUTRINO_MOMENTS / EXACT_NONHEADON_LORENTZ_PLANCK / TWO_INDEPENDENT_NUMERIC_REPLAYS
source_type: SECONDARY_SHA_PINNED_RIVET_BELLE
bw: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_PRIMARY_HEPDATA_BYTE_IDENTITY / NO_FULL_QCD / NO_PION_SCATTERING_SURVIVAL / NO_MUON_DECAY / NO_NEUTRINO_ESCAPE_OR_DEPOSITION / NO_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT020 — exact first-generation pi-to-mu-neutrino energy moments from real Belle/Rivet differential source

**13 November 2026.** First in this DAX-S8 R68 branch to pass from real Belle charged-pion energy **SECOND MOMENT** to the **FIRST-generation two-body pion decay neutrino energy moments**, while retaining exact incoming incidence. This is a classical positive kinematic gate, not new theoretical particle physics and not a physical cosmic neutrino yield.

## Source receipts, precedence and domain

DAX-S7 R68 FIRST restricted original gamma-gamma first-muon event probability to exactly 3 modeled channels. DAX-S8 ROT012 first a strictly point-scalar Born charged-pion fourth-branch model, ROT013–016 collider acceptance and resonance coherence guards; ROT017 first acquired real 140-energy x 12-angle packaged Belle/Rivet numerical source; ROT018 tested original errors and covariance non-identifiability; ROT019 first computed source conditional exact pion LAB energy-split second moment.

Actual original-source data used: Belle/Mori et al JPSJ 76 074102 (2007) arxiv 0704.3538, with measured COM W=0.8..1.5GeV, |cos theta_star|<=0.6, referential numerical source packaged in official Rivet-data 4.1.2-2.1 RPM, original package SHA256 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b, original reference BELLE_2007_I749358.yoda.gz SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**. Bytes acquired by successful NATIVE GitHub Actions https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . Primary HEPData https://www.hepdata.net/record/ins749358 CSV/YODA byte equality NOT established (all 6 exact runner URLs gave HTTP403). Source W positions and z angular values are TREATED AS 5MeV and 0.05 BIN AVERAGES: additional primary-source semantics gate still OPEN. Within angular bins central case uses UNIFORM distribution, with a separate exact positivity-based range.

Particle Data Group original 2026 pages: charged pion https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=MXXX005&init=0&node=S008 , mass m_pi=139.57039MeV, spin0, lifetime 2.6033e-8s, dominant pi+->mu+ nu_mu (99.98770%); pi- modes charge conjugate. 2025 PDG table https://pdg.lbl.gov/2025/tables/rpp2025-tab-mesons-light.pdf gives ctau_pi=7.8045m. Muon mass m_mu=105.6583755MeV from 2026 original PDG https://pdglive.lbl.gov/DataBlock.action?node=S004M . **The source branching ratio does NOT imply the exact 2-body energy map describes radiative modes or all charged pion histories.** This is conditional on TWO FREE in-vacuum, nonradiative, spin-zero isotropic pi->mu nu decays BEFORE any pion scattering, zero neutrino mass.

## Exact one-step transport kernel

In charged pion rest frame, E_star(nu)=p_star(nu)=(m_pi²-m_mu²)/(2m_pi)=29.79214090987744517MeV. Define f=E_star/m_pi=(m_pi²-m_mu²)/(2m_pi²)=**0.21345602681111262333655107689**. For LAB parent pion energy P>=m_pi and momentum magnitude p=sqrt(P²-m_pi²), neutrino from the exact two-body decay has energy

E_nu=f [P+p cos(theta_decay)], cos(theta_decay) uniform in [-1,1] (scalar parent).

Thus conditional E_nu|P is UNIFORM on [f(P-p), f(P+p)], has mean fP and second moment f²(4P²-m_pi²)/3. Explicit boosted on-shell neutrino+muon 4-vector shell, sum energy and sum momentum PASS at 57-digit accuracy for 5 parent energies and 4 angular directions each.

For a source pair Q=E_pi+ + E_pi- = E_gamma+epsilon, D=E_pi+ - E_pi-, select ONE of the two first-generation neutrinos uniformly. **EXACT** moments

mean E_nu = f <Q>/2;
mean E_nu² = (f²/3)[<Q²>+<D²>-m_pi²];
variance = mean E_nu² - (mean E_nu)².

The equation is for the POOLED two-neutrino distribution and does not depend on knowing the sign of the pion charge/COM z label. The average summed energy of BOTH first-generation neutrinos is f<Q>; the two outgoing muons retain (1-f)<Q> in this idealized branch.

## Exact incoming isotropic Planck bath: NO head-on approximation

Inherited R68 E_gamma=1436554MeV, T_gamma=0.07818527068831995MeV. Incident bath x=epsilon/T, u=(1-cos(theta_in))/2 and y=xu=W²/(4ET). With q=exp(-y), define I0=-ln(1-q), I1=y I0+Li_2(q), I2=y² I0+2y Li_2(q)+2 Li_3(q). Conditional moments x|y are I1/I0, I2/I0; thermal rate per linear dW is H(W)=4W³ I0/(4ET)². Thus at each W, <Q>=E+T I1/I0; <Q²>=E²+2ET I1/I0+T² I2/I0. Full <D²> from ROT019 exact non-head-on pion LAB Lorentz map, with source dσ/d|cosθ_star| 140x12 REAL numeric values. Source K_fid from 140 angular table reconstruction =3.88684468326980097e-10 in shared R68 kernel units, not full physical pion cross section.

## Real-source high-precision numeric outputs

A 57-digit mpmath 14pt Gaussian-Legendre W quadrature over 140 actual W source bins and 12 z bins, positive source cross section, uniform within each z bin central, yields:

- <Q>=**1436554.2887957103949794MeV**, <Q²>=**2063688224657.3592593MeV²**.
- <D²>/E_gamma²=**0.1035428892071051255793**, reproducing ROT019 exact independent first-owner result.
- E_star(nu)=29.79214090987744517MeV; f=0.21345602681111262.
- Average single first-generation neutrino E_nu = **153.3205853923979923GeV**.
- Average sum TWO first-generation neutrinos = **306.6411707847959845GeV**; the two muons together carry **1129.9131180109143GeV** before muon decay.
- Single neutrino second moment = **34588.2724092896688GeV²**; standard deviation **105.26666378403974GeV**.
- Artificial equal-parent-energy surrogate D=0, SAME <Q> and <Q²>: second neutrino moment **31342.9355775664040GeV²**. Real source moment **+10.3542848553%** relative to equal-parent output; variance **+41.4171405942%** relative; SD ratio **1.18918939027460**. First moment is EXACTLY the same, so checking the mean alone FAILS as a sufficient physics-source validity gate.
- Sharp conditional angular-BIN INTEGRAL/support envelope, at same W and positive actual bin values: single neutrino second moment in **[34185.43968757112,35015.39406521457]GeV²**, standard deviation **[103.3355591386794,107.2762422913245]GeV**. These are NOT statistical or systematic Belle confidence intervals; source errors/covariances (ROT018) not propagated.
- Decay-in-vacuum pion lab flight characteristic scale at average E_pi≈718.277GeV is approximately **40.16km**. Universal mass-shell inequality E_pi-m_pi<=|p_pi|<=E_pi yields a source-ensemble strict bound on the mean free-flight scale **[40.15683194941496,40.16463644941496]km** using ctau_pi=7.8045m. No ambient pion scattering hazard, survival or branching exposure was evaluated.

## Independent numerical execution

Original 57-digit method uses source SHA-pinned raw YODA full 141 objects, polylog exact incident x power moments and 14pt W Gauss. Independently written source split-parser + SciPy 3 separate DIRECT incident x Planck quadratures at each W, NO polylogs, 8pt W Gauss and 12pt Gauss daughter two-body decay angle check for four parent energies, obtains:
single mean=153.32058539239807GeV;
single second moment=34588.27240928971GeV²;
single SD=105.26666378403984GeV;
<D²>/E_gamma²=0.10354288920710515;
independent four parent-energy decay angular quadratures PASS.
These are two author-controlled independent algorithms, not external referee validation.

Full LOCAL 12-file original bundle includes source YODA original bytes, two executed scripts, two frozen JSON, 140-energy per-W output CSV, full extended report, source audit, README, environment, SHA256 manifest and clean replay verifier. ZIP CRC PASS, 11/11 payload SHA256 PASS, both executed program fresh temp reruns produce THREE frozen files byte-for-byte identical PASS. Local ZIP SHA256 **eb946cd3300772d1e277a34100252aae083e371bee13755cff0a880a6c79d285**. Public report is a self-standing compressed account; full method/data are in the local full original package in the originating conversation.

## Strict scope / falsifier / closure

FALSE: 'Equal LAB pion energies are enough to preserve first-generation pion-decay neutrino energy variance in Belle fiducial R68.' The original source real angular moment makes the variance +41.4% larger in this declared two-body-in-vacuum model. TRUE UNDER X: The exact two-body map is valid IF both charged pions survive to decay before interactions and the input fiducial source bin approximation is allowed.

It is **NOT** established that pions in the hot R68 bath decay before additional collisions. The ~40km vacuum flight characteristic is precisely the OPEN competition-scale gate; branching fraction alone never certifies the time/hazard. Also OPEN: primary HEPData byte equality, original W/z bin semantics, off-fiducial W/angles and full QCD hadronic amplitude, radiative pion modes, muon polarization-dependent 3-body decays, subsequent neutrino interactions or escape, EM deposition, cosmological PBH/BBN. No new external task cascade or unassigned source owner acceptance; current XH-S6 source role pertains to distinct work, KN13 controls BW ingestion.

RETURN: REAL_BELLE_FIRST_NEUTRINO_MOMENT_KERNEL_PASS / DECAY_VS_SCATTERING_HAZARD_OPEN / PRIMARY_SOURCE_SEMANTICS_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
