# XH-S5 ROT008 — polarimetry: source-motivated valley Chern and gauge metric gate

Artifact: IW_XH_S5_ROT008_SUBLATTICE_POLARIMETRY_VALLEY_CHERN_GAUGE_METRIC_AUDIT_20261110
Date: 2026-11-10
Cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
Return ID: XH-S5-ROT008-SUBLATTICE_POLARIMETRY_VALLEY_PARTITION_AND_GAUGE_METRIC_GATE_20261110
Exposure: PUBLIC
CLAIM_CEILING: PUBLISHED_2026_ABSTRACT + FULL_2025_AUTHOR_PREPRINT / NO_AUTHOR_DATA_REPLAY / NO_NOVELTY / NO_FINAL_2026_METRIC_ERROR_CLAIM / NO_NASH_PHYSICAL / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED

## Primary host — two version boundaries
M. Guillot, C. Blanchard, N. Pernet et al., A sublattice polarimeter to probe the quantum geometry of synthetic photonic lattices, Nature Communications, published 2026-11-04, https://doi.org/10.1038/s41467-026-78322-1 . The source's sublattice Stokes polarimeter reconstructs Bloch eigenvector amplitudes/phases and quantum geometry in photonic honeycomb lattices. Publisher's citable early Nov2026 version FULL Methods unavailable via current source fetch.

Full mathematical source USED is authors' 2025 preprint, DIFFERENT version: M. Guillot et al., A sublattice Stokes polarimeter for bipartite photonic lattices, 2025-07-22, https://arxiv.org/abs/2507.16446 . Eq1: H=[[epsilon0/2,-t gamma],[-t gamma*,-epsilon0/2]], gamma=sum exp(ik.d_i). Source |epsilon0/t|=1.26, ideal theoretical valley Chern approx -0.28, measured valley Chern -0.25 +/- .01 and other valley opposite sign; total C zero. These numeric claims belong to PREPRINT 2025, not necessarily identical 2026 paper. No raw CCD data, code or real instrument used. Related data is catalogued at Zenodo DOI 10.5281/zenodo.20698532; NOT fetched.

## Mature prior art / no novelty
Fukui-Hatsugai-Suzuki, JPSJ 74 1674 (2005), DOI 10.1143/jpsj.74.1674 already gives gauge-invariant discrete holonomy; source itself cites it. Conventional Pauli/Bloch projector quantum metric; none are new. Existing EXTERNAL Pith review https://pith.science/paper/2507.16446 already flags gauge-dependent raw-overlap metric equations in 2025 preprint; our derivation is independent numerical evidence, NOT priority or publication-first criticism. Public IW/NASH GitHub search on polarimetry and quantum-metric gauge returned no match (cannot rule out private work).

## Independent ideal model numerical execution (NOT author data)
Honeycomb m=|epsilon0|/(2t)=.63, reciprocal torus p,q in [0,2pi)^2. Physical embedding gamma=exp(-i(p+q)/3)*(1+exp(ip)+exp(iq)), Bloch vector d=(-Re gamma,Im gamma,m), occupied-band Berry curvature F=-d.(d_p x d_q)/(2|d|^3). Define valley K=(4pi/3,2pi/3), Kprime=(2pi/3,4pi/3) and physically metric nearest-copy Voronoi split. Integrate F/(2pi).

ANALYTIC differentiated d + midpoint quadrature N=401:
C_K=-0.27889745423974494; C_Kprime=+0.278897454239745; C_total abs<1e-15.
This independently reproduces preprint IDEAL theory -0.28, NOT measured -0.25 +/-0.01. No fitted data or measurement uncertainty is recreated.

INDEPENDENT NumPy.linalg.eigh 2x2 spinors plus FHS overlap plaquette algorithm (no code import from first), periodic representation gamma=1+exp(ip)+exp(iq), N=241:
C_K=-0.27889139209115843; C_Kprime=+0.27889139209115843; C_total abs<1e-15. Difference from analytic C_K 6.06215e-6. Sitewise random U(1) spinor phases change discrete FHS flux sums by less than 1e-12. Orbital embedding physical vs periodic is NOT an overall state U(1) gauge and may alter local geometric densities; no universal embedding equivalence is claimed (example K integrals -0.278897454 and -0.278895360 at N=241).

BOUNDARY SENSITIVITY: vary only the integration region by criterion D_K^2-D_Kprime^2 < b, physical reciprocal metric with periodic images; Hamiltonian and curvature FIXED. For b=-10, -5, -2, 0, +2, +5, +10, corresponding area percentages 9.22,25.62,39.24,49.81,60.76,74.38,90.78; corresponding K flux -0.200582,-0.262647,-0.276404,-0.278897,-0.276404,-0.262647,-0.200582. TOTAL C stays zero. Regional (valley) Berry flux is generally NONINTEGER and depends on the defined region; TOTAL C is the topological invariant. This does not show an error by authors using an explicit fixed valley partition.

## Exact independent gauge witness: earlier 2025 preprint, NOT final Nov2026
The 2025 preprint writes diagonal metric as raw gxx=(1-<u(k)|u(k+dk)>)/dk^2. This is complex and gauge-dependent; Pith already criticized this PREPRINT formula. A constant ray u(k)=exp(i3k)*(1,0) has true Fubini-Study gxx=0; dk=.05 gives raw complex gxx=4.49157 -59.77525i. Correct leading order projector-overlap metric gxx=(1-|<u(k)|u(k+dk)>|^2)/dk^2. On independent honeycomb spinor at (p,q)=(.31,-.67): direct analytic Pauli derivative metric gpp=.026257332739213914, separate eigenspinor overlap finite-difference dp=.001 gives .026253621498995017, error 3.71124e-6. Six independently drawn gauge phases change raw metric real part from about 522 to 1,999,987 while corrected metric remains .0262536215. Raw overlap violation is independent of Berry FHS success. Does NOT prove the November 2026 final version or its executed source processing uses the same formula. Need source-final full Methods+code for that.

## Execution receipts
Repro local ZIP name IW_XH_S5_ROT008_SUBLATTICE_CHERN_GAUGE_METRIC_REPRO_20261110.zip
ZIP SHA256 eabf416a4adaf752b13dde41925969286d621e835ccf7c73736346111d70cd89
Full Polish report SHA256 b5475dbd21a4f39f480e90f555f8c6f9e158fbe184f6a66d858867e9844cf226
Two INDEPENDENT scripts, crosscheck 11 criteria, frozen JSON (3 files), README, per-member SHA256 manifest and report; all scripts re-executed in CLEAN ZIP EXTRACTION with BYTE-IDENTICAL JSON. ZIP CRC PASS, all member SHA256 PASS. This GitHub report is detailed but NOT an upload of the ZIP.

Suggested source-native falsifiers only: compare *final 2026* full code/metric formulas against random spinor U(1) rephasing, verify raw Stokes, Gaussian smoothing 2px, and publish explicitly measured valley mask boundaries. No task cascade or physics admission.

STATUS: SOURCE_MOTIVATED_THEORY_BOUNDARY / NO_MATH_NOVELTY / NO_AUTHOR_DATA_REPRO / NO_FINAL_PAPER_ERROR_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_VERIFIED.