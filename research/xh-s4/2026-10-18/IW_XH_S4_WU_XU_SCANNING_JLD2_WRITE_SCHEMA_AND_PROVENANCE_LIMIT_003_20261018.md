# XH-S4 — Wu–Xu scanning.jld2 write schema and provenance limit (003 / 2026-10-18)

STATUS: SOURCE_CODE_WRITE_SCHEMA_VERIFIED / BINARY_PAYLOAD_NOT_PARSED / FIGURE_BINDING_OPEN / NO_EXEC / NO_CANON

## Primary code inspection
V1 main-scan.jl https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/arXiv-2509.05618v1/main-scan.jl lines 282–289:
- Yₚ_mat = pmap(params -> (last ∘ magic)(params...), Iterators.product(m_PBH_f_list, β_PBH_list))
- χ²_mat = ((Yₚ_mat .- .245) ./ .003).^2
- jldopen(output_data_directory/scanning.jld2, w+, compress=true) writes:
  - m_PBH_list [gram]
  - β_PBH_list
  - Y_P_mat
  - chi2_mat

V2 main-scan.jl https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl lines 243–250 has the identical four output key names and chi2 formula.

These specific write blocks do NOT record code commit SHA, hadron helper version, or subedge extrapolation rule. This absence is scoped to the inspected write blocks, not a claim about all possible embedded binary metadata or other files.

## Tracked artifact identities (earlier report 002, GitHub tree)
V1 scanning.jld2 blob ff08072449c4ef46144cb800778224acd9669a8f 149272 bytes.
V2 scanning.jld2 blob 10cc9b3f078fcadb91b5e520e75845859ca00b74 151089 bytes.
Files differ; binary contents have not been parsed. No proof ties either file to journal-endpoint values or final figure source.

## Claim guard
Do NOT infer that equal field schema equals equal numerical result; do NOT infer numerical differences solely from different blob SHA; do NOT equate a published figure with a particular commit absent figure-level derivation; do NOT claim PBH bound adjustment. Source-only finding.

## Narrow next source steps
Compare main.ipynb figure reader with four-key schema and determine if figure path reads tracked v1 or v2 scanning.jld2. If available, inspect JLD2 values independently in read-only mode and check dimensions and difference but mark any inference conditional on source provenance.
