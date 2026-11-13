---
artifact_id: IW_DAX_S8_ROT022_SOFT_PION_COMPTON_ENERGY_TRANSFER_DRIFT_DIFFUSION_VS_DECAY_001_20261113
created_at: 2026-11-13
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXACT_SCALAR_QED_SOFT_PION_COMPTON_PHOTON_LAB_ENERGY_GAIN_FIRST_AND_SECOND_JUMP_MOMENTS / INDEPENDENT_X_T_Z_QUADRATURE / ENERGY_LOSS_LOCAL_GATE
claim_ceiling: NO_PHYSICAL_COMPOSITE_PION_QCD_CROSS_SECTION / NO_FULL_BELLE_PION_ENERGY_DISTRIBUTION_FOLD / NO_STOCHASTIC_MULTISCATTER_CASCADE / NO_ESCAPED_NEUTRINO_FLUX / NO_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT022 — quantitative pion soft Compton LAB energy-transfer moments, local energy-loss length and cutoff falsifier

**13 November 2026.** This is a result new ONLY within the DAX-S8 R68 sequence, not novel particle physics. DAX-S7 R68 was strictly a conditional three-channel gamma-gamma first-event calculation. DAX ROT017 obtained actual officially packaged secondary Rivet/Belle 140x12 numerical source; ROT019 extracted a pion LAB energy split moment; ROT020 extracted first-step pion->mu nu energy moments **IF** free pion decay precedes collisions; ROT021 first established the **point-scalar model soft-Compton first event** versus vacuum pion decay at one fixed pion energy. ROT022 is its next scientifically discriminating question: how much energy does that scattering transfer, on average and in squared fluctuations?

## Source-native scope

The initial pion energy is ONLY the **ROT020 fiducial Belle/Rivet source-conditional mean** E_pi=718277.1443978551974897MeV (718.277GeV), NOT the full parent pion energy ensemble. R68 ideal isotropic stationary photon bath T=0.07818527068831995MeV, pion mass m_pi=139.57039MeV, vacuum c tau=7.8045m. Restricted ONLY to incoming photons with pion-rest energy omega <= m_pi/20=6.9785195MeV.

First-original physical sources:
- Abreu et al, *Compton scattering in scalar electrodynamics*, CERN-2008-004.293, DOI https://doi.org/10.5170/CERN-2008-004.293, exact point-scalar QED/Born unpolarized recoil: d sigma/dOmega=alpha²/(2m²)*(omega_prime/omega)²*(1+z²).
- COMPASS Collaboration, *Measurement of the Charged-Pion Polarizability*, PRL114 062002 (2015), DOI https://doi.org/10.1103/PhysRevLett.114.062002: real composite pion polarizability correction is physically needed and not assessed in this report.
- PDG charged pion 2025 summary https://pdg.lbl.gov/2025/tables/rpp2025-sum-mesons.pdf, m_pi/c tau.
- Actual Belle reference originally acquired in ROT017 native https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 , official Rivet-data-4.1.2-2.1 RPM SHA256 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b, packaged original BELLE_2007_I749358.yoda.gz SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403. This is secondary packaged numerical source; primary HEPData byte identity and exact energy-bin semantics still OPEN. Only frozen E_pi mean is passed to this ROT022 physics test.

## Exact kinematics, incoming geometry and outgoing azimuth

Set gamma=E_pi/m_pi, beta=sqrt(1-gamma^-2). An incident bath photon has epsilon=Tx and lab cosine mu relative to pion LAB velocity; let t=1-beta*mu, omega=gamma*T*x*t (incoming photon energy in pion REST). Incident photon direction in pion REST forms angle chi with the boost axis, satisfying beta cos(chi)=T*x/(gamma*omega)-1. Outgoing pion-rest photon scattering cosine z=cos(theta), azimuth phi, and Compton energy recoil r=omega_prime/omega=[1+(omega/m_pi)(1-z)]^-1. Scalar Born normalized angular kernel:

(1/sigma_Th) d sigma_B/dz = (3/8)(1+z²)r², sigma_Th=8*pi*alpha²/(3m_pi²)=8.9173460480236483e-30 cm².

Photon LAB gain G=epsilon_prime_lab-epsilon_lab=-Delta E_pi (may have either sign eventwise) has exact azimuth mean
**G_phi = gamma*omega*r*(1-z) - T*x*(1-r*z)**,
and azimuth contribution to its raw second moment
**Var_phi(G)=r²*(1-z²)/2 *[-omega² + 2gamma*omega*T*x -(T*x)²]**.

Both identities were checked against explicit NONHEADON Lorentz-boosted on-shell incoming and outgoing photon+pion four-vectors at 3 distinct x,t,z,phi; largest 42dps rest-frame squared mass-shell residual 5.8774717541e-39MeV², total four-vector conservation and individual photon shells PASS. This is kinematics, not a pion-QCD cross section.

## Exact Planck reduction, first two event-jump moments

For fixed omega, incident x lies in [omega/(gamma*T*(1+beta)),omega/(gamma*T*(1-beta))]. Define J_n(omega)=integral_{xlo}^{xhi} x^n/(exp(x)-1) dx, n=0,1,2. All are elementary-log/polylog: J0=[ln(1-e^-x)] from xlo to xhi; upper-tail S1(x)=-x ln(1-e^-x)+Li2(e^-x), S2(x)=-x² ln(1-e^-x)+2x Li2(e^-x)+2 Li3(e^-x), with Jn=S_n(xlo)-S_n(xhi) for n=1,2.

Positive Fubini gives common normalized photon-bath flux factor 1/[4 beta zeta(3)(gamma*T)²] times integral_0^cap d omega *omega* integral_{-1}^1 dz (3/8)(1+z²)r² times J0, first moment J0*A−J1*B, and second moment from (A−Bx)²+Var_phi, where A=gamma*omega*r*(1-z), B=T*(1-r*z). This avoids treating a photon NUMBER fraction as a scattering-weighted fraction, and avoids treating bath geometry as head-on.

## Frozen results, E_pi=718.277GeV, cap=m_pi/20

- Photon density n_gamma=1.5152025724753423e28 cm^-3.
- Exact soft-collision relative flux F_B=0.0001543929805264445926284 (not number fraction).
- Soft Born collision mean-free path **479.36477888369652 metres** (ROT021 independently replayed).
- Initial free pion vacuum-decay length **40164.635691158115 metres**.
- **MEAN photon LAB energy gain per scattering = 21.267977425758640811GeV**.
- **STANDARD DEVIATION of photon LAB energy gain = 16.397213044002213GeV**.
- Raw second jump moment **721.1954593929754GeV²**; variance **268.8685956103963GeV²**.
- Mean INITIAL pion energy fraction transferred per scatter **0.0296097092767555 = 2.961%**.
- Event-jump coefficient of variation **0.7709813**, so a deterministic one-energy-per-event treatment misses a large spread.
- INITIAL local pion LAB energy-loss drift **−44.36700058624599GeV/km**.
- INITIAL raw second Kramers–Moyal jump per distance **1504.48153715514GeV²/km**. The diffusion term would use one HALF this second coefficient under a separate justified Fokker–Planck approximation, which has NOT been validated for these ~3% individual jumps.
- INITIAL local energy-loss length L_loss=E_pi/|dE_pi/dx| = **16189.445644439734metres = 16.189km**.
- At this initial energy L_decay/L_loss **2.48091482397068**. This is a LOCAL RATIO, not integrated survival/cooling or pion decay energy.

SAME_SOURCE_MODEL sensitivity, recomputing exact direct 3D integral with independent SciPy from x,t,z (not importing the 1D/polylog method), at E_pi=718.277GeV:
| photon rest cap | mean photon gain per hit | initial L_loss | L_decay/L_loss |
|---|---:|---:|---:|
| m_pi/20 | 21.268 GeV | 16.189km | 2.481 |
| m_pi/40 | 11.133 GeV | 106.065km | 0.379 |
| m_pi/100 | 4.589 GeV | 1367.570km | 0.0294 |

Nine original model checks also include E_pi=300GeV and 1200GeV at the three caps, frozen in local original CSV. **The sign of the local comparison “cooling faster than vacuum decay” flips by changing the arbitrary soft-sector cutoff alone**, even without changing the point-scalar model. Consequently no full physical pion energy-loss bound, cutoff-independent cooling claim, or cosmic neutrino yield follows from this partial-sector test.

## Independent execution and negative knowledge

A completely separate SciPy program directly integrates the ORIGINAL 3D Planck x, incident t, scattered z variables with a separately derived outgoing-azimuth squared moment, no Li2/Li3; reproduces F_B=0.00015439298052644448, mean G=21.26797742575867GeV, SD G=16.397213044002196GeV, MFP=479.3647788836972m and L_loss=16189.445644439733m. The first code is mpmath42 1D exact reduction and explicit on-shell four-vector checks. This agreement validates the defined calculation, not real composite pion QCD.

The earlier ROT021 first-encounter fixed-energy ratio Gamma_scatter/Gamma_decay≈83.787 cannot be iterated as 83.787 events * 2.961%=248% fractional energy loss; such a result is **physically impossible** and falsifies a naive frozen-energy repeated-collision shortcut. All relevant rates change with parent E_pi, event jumps fluctuate, scattering is ELASTIC not pion destruction, and later pion decay may still create neutrinos. Genuine pion polarizability corrections (and inelastic bath processes), full real Belle pion energy distribution, dynamic eventwise transport, muon decay, neutrino interaction and cosmological evolution remain OPEN. STOP on repeated source-only Born proxy improvement without new physical source or explicitly owned differential transport target.

## Original reproducibility bundle

Locally executed ORIGINAL 13-member ZIP in originating ROT022 conversation, source original Rivet YODA bytes, frozen prior ROT020 source JSON, complete report, 2 independently written actual executed scripts, 2 JSON outputs, 9-case original CSV, README, SOURCE_AUDIT, environment, SHA256SUMS and clean-room replay verifier. CRC PASS; **12/12 SHA256** content files PASS; clean-room reruns of BOTH scripts produce THREE BYTE-IDENTICAL frozen JSON/CSV outputs PASS; ZIP SHA256 **17411259eba94bf316e35de21c94d2e448271f8565fd62998f6c16de4204197c**. Local source-bearing full bundle not assumed uploaded to GitHub by publishing this Markdown. Public compact reproduction code can be published separately and must be labeled as such.

**CUSTODY / DISPOSITION: ROT022_POINT_SCALAR_SOFT_PHOTON_ENERGY_DRIFT_AND_DIFFUSION_PASS / CUTOFF_DEPENDENCE_MATERIAL / MULTISCATTER_HADRON_DECAY_TRANSPORT_OPEN / BW_GITHUB_PENDING_BW_INGEST / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN.**
