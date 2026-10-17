# IW_XH_S4_WU_XU_HISTORICAL_SCAN_FIGURE_SOURCE_CONTINUITY_004_20261018

CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
STATUS: SOURCE_NATIVE_COMPARISON_VERIFIED / NOTEBOOK_BINARY_LINEAGE_UNRESOLVED
CLAIM_CEILING: SOURCE_PROVENANCE / NO_EXEC_SIGN / NO_CANON / NO_NOVELTY / NO_PBH_BOUND / NO_ENDPOINT
DATE: 2026-10-18

## 1. Exact matched scanning-parameter file

Both public v1 and v2 use identical tracked file content under `main-scan-parameters.jl`, Git blob `53faee65beda383348580c28d0424188da69b660`.
Declared ranges: m_PBH initial 6e8..1e10 g (100 grid points); beta_PBH 1e-20..1e-17 (100 grid points); Cartesian 10,000-parameter scan specification. A shared input parameter file does NOT prove actual binary scan executions used the same runtime/config or were completed.

- v1: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/arXiv-2509.05618v1/main-scan-parameters.jl
- v2: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan-parameters.jl

## 2. Exact full-table comparison

v1 `data/out/mesons_from_PBH.dat`: Git blob `1cfc5eac427bd71aa984e630ac939188848b3952`, 100 numeric rows and four columns (mass, charged pion, charged kaon, neutral-long kaon).
v2 `data/out/hadrons_from_PBH.dat`: Git blob `06d0883a27b108692720422294ba2baacd381a64`, 100 numeric rows and six columns (same first four, then proton and neutron).

Direct read-only comparison of all parsed numeric rows by raw string shows 100/100 exact matching across each of the first four columns including masses and three meson source rates. V2 appends separate proton and neutron columns without changes to those four tabulated strings.

Table header uses `charged_pion_dN_over_dt`, `charged_kaon_dN_over_dt` and `kaon_zero_long_dN_over_dt` rather than independently charge-resolved pi+ and pi- columns. Column identity does NOT settle charge-resolution or reaction-source normalization. Independent Rec9 referee reviewed on 2026-10-18: symmetry half-split for p/n is source-supported; for pi/K is conditional under charge-conjugation equality; no PBH endpoint inference.

- v1 table: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/arXiv-2509.05618v1/data/out/mesons_from_PBH.dat
- v2 table: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/data/out/hadrons_from_PBH.dat
- Rec9 guard: https://github.com/wmakiela-tech/Nash-iw-research/blob/c2c4619f0739c9c086c3c6b3f13778341d8393f9/archive-index/2026/rec9/rec9_wuxu_charge_pair_source_map_paper_code_contract_referee_20261018.md

## 3. Author-tracked binary history pointer

The v2 path `arXiv-2509.05618/data/out/scanning_old.jld2` is a 47-byte Git blob with SHA `5dd0a2032c4612a25c0e1a72ab58d0ad8f8ab084`. Native Git blob content is the relative link text:
`../../arXiv-2509.05618v1/data/out/scanning.jld2`
This is a Git symlink target to archived v1 scanning data, not a third independently computed scan.
Separate tracked binary scans:
- v1 scanning.jld2: blob ff08072449c4ef46144cb800778224acd9669a8f, 149272 bytes
- v2 scanning.jld2: blob 10cc9b3f078fcadb91b5e520e75845859ca00b74, 151089 bytes

Both main-scan.jl source write blocks define keys `m_PBH_list [gram]`, `β_PBH_list`, `Y_P_mat`, `chi2_mat` (chi2=((Yp-.245)/.003)^2). Binary payloads were NOT decoded; differing blob SHAs do not prove specific numerical changes or journal-figure genealogy.

## 4. Archived vs current figure objects

v1 `plots/Y_P.png`: Git blob `313e40639567084abcfa00d8cae700194d804e0a`, 185594 bytes; `Y_P.pdf`: `ca810f10815551cbef41743f10d906d5d1339a13`, 142346 bytes.
v2 `plots/Y_P.png`: Git blob `3b8bb8438660da9c1fb84a383b22dd1a6878a7b0`, 167078 bytes; `Y_P.pdf`: `302bad83d5581597e9c0e68d2d49f9ac5a31f5dd`, 111995 bytes.
v2 `plots/Y_P_with_v1.pdf`: blob `b071d12285da75a01d387b70537e29f67274952a`, 113232 bytes; name suggests explicit v1 comparison, but binary figure content was not read and no graphical comparison claim is made.

Notebook refs:
- v1 `main.ipynb` blob `89a69d1ac23f3024893db51da29c9f573ecf0c5f`, 1,834,659 bytes.
- v2 `main.ipynb` blob `171c4a29e414860d724c817641896628f35982b0`, 2,526,919 bytes.
The connected GitHub text-file reader returns empty content on those oversized notebook blobs; attempted parsing fails due to empty output. Notebook derivation/plot reader could NOT be inspected. This is a tool access limitation, not negative evidence that notebook lacks such code.

## 5. Reaction population architecture and guard

In v1 main-scan.jl (approx lines 162-169), a single aggregate pion source is assigned unchanged to both pi- and pi+ ODE source terms; the analogous direct injection remains in v2 main-scan.jl (lines 103-112). Thus that code-level issue predates the v2 introduction of proton/antiproton and neutron/antineutron channels. V2 also expands kaon depletion terms. Shared meson rate tables plus shared scan grid do NOT imply any calculated Yp or chi2 change arises only from new nucleon channels: the kinetic equations also changed.

Per current Rec9/KN10 source ceiling, the aggregate-column-vs-reaction-species mismatch remains high but the physically justified half-split for pi/K is conditional on an explicit symmetry contract, while paper-vs-code subedge extrapolation discrepancy does not establish executed journal-run provenance. No direct Yp/DH/PBH limit correction is established.

## 6. What is and is not closed

CLOSED AT SOURCE LEVEL: identical v1/v2 scan parameter blobs; exact 100-row meson table preservation; authors' old-scan link target; distinct scan and plot blobs; v2 appended nucleon columns; both code versions assign one pion input function to two charge-labeled state ODEs.

OPEN: reading binary scanning.jld2 numerical data and embedded metadata; actual notebook read/plot chain; exact journal Fig. 5 ancestry; charge-resolution source generator meaning; physical sensitivity after legal normalization and floor controls; published endpoint provenance.

DURABLE SOURCE ONLY. Repository GitHub write/readback does NOT imply Slack delivery, BW ingestion, scientific acceptance, or closure.
