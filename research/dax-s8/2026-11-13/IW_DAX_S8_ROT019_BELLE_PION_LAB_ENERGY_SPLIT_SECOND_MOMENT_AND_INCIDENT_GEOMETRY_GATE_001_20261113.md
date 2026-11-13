---
artifact_id: IW_DAX_S8_ROT019_BELLE_PION_LAB_ENERGY_SPLIT_SECOND_MOMENT_AND_INCIDENT_GEOMETRY_GATE_001_20261113
created_at: 2026-11-13
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: REAL_SHA_PINNED_RIVET_BELLE_DIFFERENTIAL_ENERGY_MOMENT / EXACT_NONHEADON_THERMAL_BOOST / BIN_SUPPORT_ENVELOPE
claim_ceiling: NO_PRIMARY_HEPDATA_BYTE_EQUIVALENCE / NO_VERIFIED_PRIMARY_ENERGY_BIN_SEMANTICS / NO_FULL_PHYSICAL_QCD_RATE / NO_PION_DECAY_OR_DEPOSITION / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT019 — real Belle pion-pair LAB energy-sharing second moment for R68

13 Nov 2026. FIRST source-valued differential **energy-sharing** target gate in DAX R68 pion branch. Not first kinematic identity in physics, not a claim of novelty or a full hadron transport simulation.

## Provenance, firstness and source

DAX-S7 R68 FIRST scoped conditional three gamma-gamma first-event channels. DAX-S8 ROT012 first point-pion Born source proxy, ROT013–016 Belle collider fiducial and hadronic coherence source caution, ROT017 FIRST 141 original packaged Rivet YODA V3 numerical source tables with 140 W positions and 140x12 angular measurements, ROT018 first source asymmetrical errors and unidentifiable cross-energy covariance. ROT019 adds the previously missing physically relevant pion FINAL STATE energy second moment. Preserve all earlier limitations and attribution.

Original physics paper: Belle / Mori et al, J. Phys. Soc. Jpn. 76 074102 (2007), https://arxiv.org/abs/0704.3538 and review https://academic.oup.com/ptep/article/2012/1/04D001/1575434 ; W in [0.8,1.5]GeV, pion COM |cosθ*|<0.6. Original primary HEPData https://www.hepdata.net/record/ins749358 still not byte-opened (native 6/6 numeric endpoints HTTP403). ACTUAL DATA IN THIS CALCULATION are SECONDARY OFFICIALLY PACKAGED RIVET REFERENCE (not toy Born), Belle filename BELLE_2007_I749358.yoda.gz, compressed size 29215 bytes SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403. Official Rivet-data 4.1.2-2.1 source RPM SHA256 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b, native acquisition https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . All original data bytes, full local numerical scripts, JSON/CSV and SHA manifest are in originating ROT019 conversation ZIP.

## Exact relativistic and Planck derivation (not head-on approximation)

Primary gamma bath LAB E=1436554 MeV, ideal isotropic Planck T=0.07818527068831995 MeV, pion rest m=139.57039MeV. Incoming bath photon eps=Tx, collision u=(1-cos θinc)/2, W²=4ETxu, y=xu=W²/(4ET). The outgoing charged pion momenta in COM have modulus p*=sqrt(W²/4-m²). Define z=cosθ* relative to the incoming energetic-photon COM direction (NOT relative to LAB boost), and pion azimuth phi. LAB total energy Q=E+eps, boost momentum magnitude |P|=sqrt(Q²−W²). Exact angle between COM beam and boost: c=(E−eps)/|P|.

For pair LAB energy difference D=E_pi+−E_pi−, after azimuthal average (source unpolarized and phi symmetric), the EXACT geometric relation is:

< D²/E² >phi = βπ² [((E−Tx)²/E²) z² + (2ET(x−y)/E²)(1−z²)], with βπ²=1−4m²/W².

This is even in z, hence the Belle source differential dσ/d|z| is sufficient without reconstructing a signed pion forward/backward distribution. The result is a classical Lorentz-kinematic identity, not QED/QCD matrix element theory.

The positive incoming flux Planck measure is x²/(exp(x)−1) dx *2u du, transformed exactly to 2y dx dy/(exp(x)−1), x>=y. Define q=exp(−y),

I0=−ln(1−q), I1=y I0+Li2(q), I2=y² I0+2y Li2(q)+2 Li3(q).

The thermal kernel PER LINEAR dW is H(W)=4W³ I0/(4ET)². Exactly integrating x|y produces:

M2(W,z) = βπ² [A(y) z²+B(y)(1−z²)],
A=1−2(T/E)I1/I0+(T/E)² I2/I0,
B=2(T/E)(I1/I0−y).

No head-on or m=0 substitute used; conditional model is ideal isotropic bath, unpolarized COM angular distribution and fixed R68 parameters. The head-on substitution βπ² z² differs from exact source-integrated M2 by only +4.570070211116e−7 RELATIVE (full exact minus head-on), explicitly quantified.

## Source-data conditions and numerical results

The ACTUAL 140x12 YODA source numbers d02..d141 have 12 z-center positions 0.025..0.575 (step .05), and per-energy Table1 records W-centers 0.8025..1.4975GeV (step .005). **Source reconstruction assumption:** every W source y is treated as the invariant-W BIN AVERAGE over 5MeV and each differential angular source y as the z-BIN AVERAGE over width 0.05. Original HEPData exact point-vs-bin semantics not independently verified. The final rate/moment is strictly conditional on W=[800,1500]MeV and |z|<=0.6. No extrapolation.

Exact incoming x integration using Li2/Li3, 58-digit mpmath, 14pt GL quadrature in each W source bin and real 140x12 YODA numbers gives (source-normalized second moment of Delta=(E_pi+−E_pi−)/E):

- M2 if source differential is UNIFORM within each 0.05 z-bin: **0.10354288920710512558**.
- RMS Delta: **0.32178080925857764021**.
- RMS LAB single pion energy deviation from HALF THE TOTAL PAIR ENERGY: **231.12775433182337 GeV**. RMS pair energy difference **462.25550866364674 GeV**.
- z-CENTER midpoint approximation instead of true z-bin uniform: RMS **0.32147963203646693403**. This preliminary value was initially mislabeled uniform and subsequently explicitly corrected. z-bin uniform has center² + (0.05)²/12 exactly. Source-support bounds unchanged.
- SHARP positive angular-bin support-limited RMS: **[0.30114856696739369, 0.34230141775766463]**, i.e M2 [0.09069045938651478,0.11717026059890719], provided W-bin-average and angular-bin integrals are valid. Achievable as inf/sup with sources concentrated near z-bin edges; NOT a confidence interval or full statistical/systematic error band.
- Synthetic ISOTROPIC-in-fiducial-angle comparator, with identical measured real W source weighting, z² mean 0.6²/3=0.12: RMS **0.33405341662432274**. Actual source angular moment2 is **7.212720141159684% smaller** than this synthetic isotropic comparator, while RMS is 3.6738458% smaller. No source claim of physical isotropy.
- Real 140x12 angular source reconstructed fiducial K=3.88684468326980097e−10; independent source Table1 K=3.88686466991478366e−10, source rounding maximum angular closure 5.863726984871584e−5. Same benchmark as ROT017/018.
- A flat equal-pion-energy surrogate predicts M2=0 and therefore CANNOT preserve this defined source-based 2nd LAB energy moment; this is not an alleged mistake in a named codebase.

## Independent execution and exact four-vector controls

Primary: original source-hash-pinned Python 3.13 script with 58-digit mpmath, Li2/Li3 and full 140x12 YODA sample, storing a full 140-row W-dependent downstream CSV and frozen JSON.

INDEPENDENT: separately authored source YODA parser, scipy.integrate.quad directly integrating x over incoming Planck conditional support WITHOUT Li2/Li3 and independent GL W quadrature. Numerical RMS=0.32178080925857766, min=0.3011485669673937, max=0.342301417757665. Additionally constructs explicit pion LAB 4-momenta from COM for three NONHEADON incoming x,u,z tuples and 4 azimuthal points. Eventwise E+ + E−=E+eps and azimuth average D²/E² matches exact invariant analytical expression with maximum ABS difference about 1.2e−15. These are kinematic numerical source controls, not a native pion transport Monte Carlo or external referee.

Original complete 12-entry local ZIP contains primary original YODA, both original scripts, 2 frozen JSONs, W-resolved 140-row CSV, full science body, SOURCE_AUDIT, README_RUN, environment, SHA manifest and clean-room verifier. Local CRC PASS; 11/11 SHA256 content PASS; YODA SHA PASS; clean isolated replay of BOTH scripts generates 3 frozen results byte-identically PASS. ZIP SHA256=1caf164c5e6560c4f081a02780c4221e4a198fc1bc617c1450362f1a4349db11.

## Claim ceiling and next gate

ONLY source-fiducial pion pair 2body LAB second moment with explicit reconstruction assumptions. Not original-primary HEPData byte equality, physical full pion angular/energy QCD rate, missing angular shape/stat/sys covariance, charged-pion lifetime/decay spectrum, eventual muons/neutrinos, EM/neutrino energy deposition or PBH/BBN. No new external source-owner task/acceptance assumed. Source study is closed as a bounded positive moment until physically complete angular data and/or downstream pion decay process target are assigned with owner and original source; avoid repetitive source-only proxy saturation.

BW GITHUB_PENDING_BW_INGEST; NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
