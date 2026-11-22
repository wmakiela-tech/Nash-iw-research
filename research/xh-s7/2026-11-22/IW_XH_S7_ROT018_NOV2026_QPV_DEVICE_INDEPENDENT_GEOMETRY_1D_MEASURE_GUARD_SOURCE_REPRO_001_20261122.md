---
artifact_id: IW_XH_S7_ROT018_NOV2026_QPV_DEVICE_INDEPENDENT_GEOMETRY_1D_MEASURE_GUARD_SOURCE_REPRO_001_20261122
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
created: 2026-11-22
mode: AUTONOMOUS_EXTERNAL_ORIGINAL_SCIENCE / SOURCE_NATIVE_PHYSICAL_GEOMETRY / NONBLIND_FUNCTIONAL_CONTINUITY / TWO_SURFACE_PRIOR_ART
exposure: PUBLIC
status: NOV18_NATURE_PRIMARY_JOURNAL_AND_ARXIV_FULL_ORIGINAL_TEXT_READ_PASS / QPV_2D_3D_GEOMETRY_INDEPENDENT_NUMERICAL_REPLAY_PASS / 1D_METRIC_DEFINITION_AMBIGUITY_REPRO_PASS / PRIMARY_RAW_NIST_DATA_NOT_ACCESSED / UQ_RAW_GRAVIMETER_DATA_NOT_ACCESSED
claim_ceiling: MODELED_TARGET_REGION_ONLY / NO_EXPERIMENTAL_BELL_DATA_REPLAY / NO_THEOREM_SECURITY_AUDIT / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_status: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT018 — Source-native verification of a 2026 device-independent quantum-position-verification experiment and 1D geometry measure ambiguity

## 0. Role and attempted original instrument data

On user input "O", execute ONE autonomous *external science harvest* rotation rather than organizing internal B1/BBN or generic metascience reviews. Standing moderator request: "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji." ROT017 independently reproduced classical Newtonian model of Groszek et al., Science Advances DOI 10.1126/sciadv.aee0802; did not decode real gravimeter data.

ROT018 began by seeking actual UQ dataset https://doi.org/10.48610/cd26dd2 at original UQ eSpace and researchdata.edu.au index https://researchdata.edu.au/unblockable-communication-gravity-reproducing-figures/4023470 . Indexed source DATASET metadata says openly available code and actual raw gravimeter data (4 scripts), but DOI redirected to 403 and institution file endpoint returned cache miss. Container direct external HTTP had DNS failure. **DATASET INDEX PASS, ORIGINAL UQ RAW BYTES NOT ACCESSED.** No bit decoding. Avoid refabricating data from source description.

Since source bytes unavailable, chose another freshly published, authentic original 2026 quantum experiment with fully specified physical geometric parameters and explicit falsifiable mathematical predictions. Its raw NIST data is ALSO not accessible through available tools: `RAW_DATA_HOLD`, but original primary full arXiv HTML methods+supplement parameter tables exposed enough to reproduce target-region integrals. No claims on NIST photon-click records, Bell statistics or security proofs based on raw data.

## 1. Original current science: journal version 18 November 2026, source maturity

Gautam A. Kavuri, Yanbao Zhang, Abigail R. Gookin et al., "**Quantum position verification with remote untrusted devices**", *Nature*, peer-reviewed journal version **published 18 November 2026**, DOI https://doi.org/10.1038/s41586-026-11247-3 (accepted Oct5). Full source original HTML available via https://arxiv.org/abs/2601.16892 (first PUBLIC preprint **23 January 2026**, updates March and August 2026), especially main sections and supplementary Table3, Table4 text. Exact original article data DOI https://doi.org/10.18434/mds2-4322 . Data DOI indexed in original Nature article but individual raw trial files/bytes NOT fetched; analysis code according to Nature available FROM AUTHOR ON REQUEST, not public executable github.

NIST first-party contextual press release https://www.nist.gov/news-events/news/2026/11/quantum-physics-can-verify-persons-location-nist-researchers-show published 18 Nov. It is explanatory not source of actual experimental records. Prior experimental run times were September20 and October7 **2024**, not a new physical measurement performed in November2026. Arxiv January2026 prior availability subtracts first-publication novelty.

Actual original author experimental design:
- two trusted classical verifiers A and B separated 195.1±0.3m;
- quantum verifier A additionally provides one photon of polarization-entangled pair to remote untrusted proving party P while retaining the other;
- party B sends synchronized classical challenge; P receives input bits, calculates XOR, performs untrusted quantum measurement, returns classical outcome within lightcone timeliness; verifier A' performs Bell test with space-like separated choice/outcomes. Station-local RNG and trusted verifiers/timing assumptions remain.
- 335 protocol instance verdicts from **two 2024 days**: basic day1 224/232 passed (96.55%), extended day2 102/103 passed (99.03%), so 326/335 passed (no per-instance independence model inferred).
- approx 250,000 trials per second, 30m trials per basic 2-minute run, 60m per extended 4-minute run; detector efficiencies >81%, above critical 2/3 fair-sampling loophole limit (source author).
- soundness target delta 2^-64 **under threat model**, not direct observed frequency; completeness design epsilon 0.97725 is intended success probability, not direct success count.
- adversaries have unlimited IN-TRIAL quantum computation and communication constrained by causality but bounded **PRE-SHARED entanglement**; stronger implemented extended threat threshold average robustness <= 8e-6 per trial. This is not security against arbitrarily pre-entangled quantum attackers nor tampering with trusted verifiers/timetaggers or geometry, and does not imply immediate widespread legal/security deployment.

Closely prior art in same QPV specialist:
- foundational cryptographic impossibility of unconditionally classical position verification under multiple coordinated adversaries (position-based cryptography, Buhrman et al. 2014);
- original experiment preprint Jan2026 and 2026 Nature peer-reviewed paper;
- `Relativistic position verification with coherent states`, *Nature Physics* published **3 Sept2026**, DOI https://doi.org/10.1038/s41567-026-03439-5, independently experimentally demonstrated different coherent-state QPV (not full Bell device-independent proof). Hence Nature Nov18 NOT "first experimental QPV ever".
- `Efficient multi-basis quantum position verification secure against generalized adversaries`, *npj Quantum Information*, published **31 Oct2026**, DOI https://doi.org/10.1038/s41534-026-01325-9, an alternative theoretical adversary framework. Need compare source-defined THREAT MODEL and devices rather than generic "untrusted" firstness.

## 2. Exact geometrical original source data used for executed reproduction

Full primary manuscript supplementary Section IV.2 Table3 original source parameter record:
`D_AB=195.1m`, RA sphere centered at A radius `157.3m`, RB sphere centered at B `116.7m`, prolate ellipsoid E3 major axis `L3=274.8m`, E4 major axis `L4=273.1m`, foci A,B distance D. Values explicitly rounded to 0.1m, with uncertainties ~0.2–0.3m; independent XH does NOT claim original raw precision or original author's 100k-sample timing/distance Monte Carlo uncertainty propagation.

Define A=(0,0,0), B=(D,0,0), x longitudinal and r orthogonal radius. Sphere squared radial support:
`S_A(x)=R_A^2-x^2`;
`S_B(x)=R_B^2-(x-D)^2`.
For prolate ellipsoid with major axis length L (>D), `a=L/2` and `b²=(L²-D²)/4`, radial support
`E_L(x)=b² [1-((x-D/2)/a)²]`.

Physical geometric source:
`Q(x)=max(0,min(S_A,S_B,E_L3,E_L4))`: cross-sectional disk support for quantum target region E, intersection 2 spheres AND 2 ellipsoids.
`C_A(x)=max(0,min(S_A,E_L3))` and `C_B(x)=max(0,min(S_B,E_L4))`; classical target set `C=C_A UNION C_B`. Since disks are coaxial, `C(x)=max(C_A(x),C_B(x))` for cross-sectional disk radial square (NOT sum). Text of original supplementary section IV.2.3 explicitly calls classical target region **the union of these two regions for ALL comparisons**, thus 1D metric needs clear convention.

Integrals independently IMPLEMENTED and EXECUTED using Python 3, SciPy Gauss–Kronrod quadrature `scipy.integrate.quad`; original numerical physics from printed parameter values not original author code. For 2D cross-sectional projection `A=integral 2 sqrt(rmax²) dx` and 3D volume `V=π integral rmax² dx`, piecewise across geometric boundaries. Independent Simpson uniform-grid 10,001/20,001/40,001/80,001 node convergence also executed for ratios, assertions PASS.

Exact source geometry-derived 1D intervals:
- Classical branch A = `[-39.85,157.30]m`, length **197.15m**.
- Classical branch B = `[78.40,234.10]m`, length **155.70m**.
- Their intersection = `[78.40,157.30]m`, length **78.90m**.
- Quantum E interval = intersection `[78.40,157.30]m`, length **78.90m**.
- Classical set UNION interval = `[-39.85,234.10]m`, length **273.95m**.
- Sum of two classical branch interval lengths counts overlap twice = **352.85m**.

ACTUAL independently computed:
- `Q_2D_area=10278.647832631696 m²`;
- `C_2D_union_area=41447.70203861599 m²`;
- `Q_3D_volume=1169525.019989825 m³`;
- `C_3D_union_volume=5326100.250917688 m³`;
- **2D comparable area ratio = 4.032408028129116**, author Table4 4.02±0.03 -> PASS.
- **3D comparable volume ratio = 4.554071233947629**, author 4.53±0.05 -> PASS.
- **1D vs ideal classical separation D/Qlength = 2.47275031685678**, author 2.47±0.02 -> PASS.
These values differ slightly from center of original author results due printed table parameter rounding, figure original uncertainty Monte Carlo and differing calibrations; no claim author's own geometry incorrect.

## 3. NEW bounded interpretation/metric audit: one-dimensional comparable-classical numerator

Original author Table4 says **1D (vs comparable classical) = 4.48±0.02**.

From its explicit "classical target region is the UNION of the two regions for all our comparisons" and 1D region lengths, source mathematical union length ratio is:
`273.95 / 78.90 = 3.4721166032953104`, NOT 4.48.
But if one uses SUM of branch lengths, counting 78.9m overlap TWICE,
`(197.15+155.70)/78.90 = 4.47211660329531`, which matches reported 4.48±.02.
The difference is exactly **1.0000** because the branch overlap equals quantum interval, and `(|A|+|B|-|A∪B|)/|Q|=|A∩B|/|Q|=1`.

In 2D and 3D, by contrast, original author's quoted 4.02,4.53 agree with UNION cross-sectional integrals, not with SUM of the disjoint-branch integral measures (which would each be about 5.03 and 5.55). **Therefore the published 1D comparable-classical QA may use a metric different from straightforward projected SET-UNION length, while the other dimension metrics use union.**

CLAIM CEILING:
- This is a direct, reproducible ambiguity in the MATH DEFINITION OF ONE METRIC on SOURCE-ROUNDED INPUTS. A case where authors might mean "sum of two attacker-specific position extents" instead of set-union length is plausible and might be physically justified as a distinct metric, but such a distinct operational weighting should be specified. 
- There is NO evidence here of a wrong photon experiment, invalid Bell statistical analysis, flawed proof of quantum security or wrong 3D quantum advantage. It is premature to allege paper error/retraction, and raw original geometry calculation code was not obtained to inspect authors' program.
- It should be posed to original corresponding authors/referees as an EXPLICIT DEFINITIONS QUESTION before any acceptance as error.
- No one sent messages to authors; no public Github issue or NASH internal owner role assigned.

Possible alternative: some representations treat the two attacker position regions as labeled copies and count their shared geometric volume twice. This gives a measure on the *disjoint union of labeled attacker states* rather than the geometric union of physical positions, and is a defensible DIFFERENT observable. But then one should apply the same labeled convention in 2D and 3D for comparability; source Table4 appears to use unlabeled union there. This underscores necessity of source metric typing, not universal dismissal of quantum protocol.

## 4. Experimental evidence and source-data access

Original experiment reconstructed author outcomes (NOT XH measured):
- Day1 no pre-entanglement: 224/232 passing (8 fail).
- Day2 small preshared entanglement: 102/103 passing (1 fail, the final instance had insufficient remaining data).
- Total 326/335 passed; 9 failures are honest protocol operating results, **NOT observed spoof attacks**.
- Security (\delta=2^{-64}\approx5.42\times10^{-20}\) is a design bound conditional on security model, not sampled empirical impostor frequency.
- Original data DOI https://doi.org/10.18434/mds2-4322 cited Nature; original data archive files NOT downloaded in this tool, and Nature says original statistical analysis CODE available from authors on request. Thus NO independent Bell p-values, test-factor product, timing-event localization uncertainty, loss/detection loophole analysis, random-source freedom audit or theoretical proof review.
- NIST source original 18 Nov2026 release confirms 195m network; experimental 2024 dates found in original supplementary main text. Not legal evidence of exact individual presence outside threat model.
- UQ raw gravimeter data from ROT017 still not read, no misleading "decoded 49 bits" claim in ROT018.

## 5. Critical scientific prior art, falsifiability, NASH boundaries

MATURE surface: special-relativistic light cones, non-signaling, classical position verification no-go with multiple colluding actors, Bell inequalities, test martingales/e-values, device-independent quantum cryptography with trusted local verifiers, nonzero loss and detector thresholds. Security theorem protected region is in spacetime and conditional on timing/no-prior-entanglement constraints.

CLOSEST 2026 specialist surface: preexisting QPV remote experiments (Nature Physics coherent-state Sept2026), Oct31 multibasis QPV, original early2026 arXiv and latest Nov Nature device-independent loophole-free paper. Firstness of quantum-device-independent loophole-free QPV implementation belongs original Kavuri et al; not to XH/NASH.

XH original quantitative work is:
(a) 2D/3D target-region source geometry reproducibility at published parameter precision;
(b) one-dimensional projected region SET UNION vs labeled branch measure issue, experimentally independent at level of source mathematics, without resolving authors' underlying metric choice.
Science-first falsification next discriminant: obtain original authors' geometry integration implementation, identify 1D "classical length" numerator definition, compare precise original timings and covariances; confirm whether double-counting is intended as labeled attacker-location space. Get NIST raw trial bytes and author factor code before calling Bell-security evidence reanalysis. Do not add NASH method novelty from a semantic-check technique already established in mature scientific practice.

Files created and EXECUTED in local container, readback checked:
- `/mnt/data/xh_s7_rot018_qpv_geometry_reproduction.py` 6935 bytes, SHA256 `1507aa4a74567d0765cce09638261d629795121d020019e4588dc6169ad6d94a`, actual scipy script numerical integrals plus 4 independent Simpson grids, physical source geometry, assertions PASS.
- `/mnt/data/xh_s7_rot018_qpv_geometry_receipt.json` 2839 bytes, SHA256 `5c135165fa2331020c57c5a24bb332204ceb624fdbeb7d71367cab93bc2a8430`, original parameters, all reconstructed regions, dimensions and limitations.
- `/mnt/data/xh_s7_rot018_qpv_quadrature_grid.csv` 193 bytes, SHA256 `d39cdfcaf25085da87265b6ae85a09bfeea1c4c6c3393d07a470ea9d40729825`.
No proprietary fonts/files, and no PDF screenshots were analyzed because original arxiv FULL HTML source (including supplementary full text) was used, original Nature journal was source-indexed; no PDF visual reading claimed.

No new B1/QGEM execution, internal owner task, public issue to researchers, BW ingestion ACK or NASH novelty claim. Public Github artifact alone is source custody, `GITHUB_PENDING_BW_INGEST`.

**Final scientific receipt**:
`XH_S7_ROT018_NATURE_NOV18_QPV_PRIMARY_ORIGINAL_SOURCE_PASS`
`SOURCE_GEOMETRY_2D_4P032_VS_AUTHOR_4P02_PASS`
`SOURCE_GEOMETRY_3D_4P554_VS_AUTHOR_4P53_PASS`
`IDEAL_1D_2P47275_VS_AUTHOR_2P47_PASS`
`COMPARABLE_1D_UNION_3P472_VS_SUM_4P472_AUTHOR_4P48_METRIC_DEFINITION_HOLD`
`RAW_UQ_AND_RAW_NIST_EXPERIMENTAL_DATA_NOT_READ_HOLD`
`SCIPY_QUAD_GRID_CONVERGENCE_EXECUTED_PASS`
`NO_SECURITY_THEOREM_AUDIT / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
