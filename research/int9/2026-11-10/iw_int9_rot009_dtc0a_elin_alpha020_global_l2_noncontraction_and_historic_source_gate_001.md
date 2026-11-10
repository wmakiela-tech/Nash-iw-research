---
artifact_id: IW_INT9_ROT009_DTC0A_ELIN_ALPHA020_UNSTABLE_SOURCE_AUX_OPERATOR_GATE_001_20261110
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-10
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_AUX_E_FILTER_ONLY / NO_HISTORIC_PRODUCER / NO_FULL_KA / NO_PHYSICAL_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# INT9 ROT009 — historical alpha=.2 outside sharp global L2 contraction of literal DTC0a E_lin helper

## Source first, ownership and currentness

The user's frozen diagnostic `dtc0a_oddN_sparse_convergence_N31_to_N41_manifest.json` fixes six odd N=31,33,35,37,39,41, E_mode=E_lin, stencil order2, alpha=0,.05,.2, interior mask3. Its claims are DIAGNOSTIC ONLY. Its referenced original producer `dtc0a_runtime_v0_3_1.py` has SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084, NOT byte recovered here. The supplied literal auxiliary helper `deepseek_python_20260627_a87249.py` SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 was pinned and `apply_E` actually executed.

KN13 ROT006 10 Nov FIRST reported that this helper's full AST equals original Moderator Colab notebook cell17; this is related-source lineage, NOT original producer-byte identity. INT8 ROT046 FIRST proved centered Lie vs RAW Fourier TT mismatch, ROT047 commutator nonclosure, ROT051 FIRST used the conservative globally stable source filter alpha range [0,1/6] and classified special zeros. These are owners' prior results. This integration targets a distinct actual-historical diagnostic alpha=.2, and proves only that the LITERAL AUXILIARY `apply_E` is not an all-mode L2 contraction there. It does not rerun historical `K_A` or challenge owners' smooth-field diagnostics.

## Exact source symbol and sharp threshold

In the original helper, E_lin returns h+alpha*dx^2*Delta2(h), where Delta2 is the symmetric standard periodic 3D second-difference Laplacian/dx^2, applied componentwise. Therefore in the discrete Fourier basis:

  lambda_E(k)=1-4 alpha sum_{i=1}^3 sin^2(pi*k_i/N).

For N=2m+1 odd, max sum sin² = 3 cos²(pi/(2N)) (all three corner frequencies k_i=+/-m). Thus for nonnegative alpha:

  ||E_lin||_(L2->L2)=max{1, |1-12 alpha cos²(pi/(2N))|}.

The **NECESSARY AND SUFFICIENT** nonexpansiveness threshold is
  alpha<=alpha_crit(N)=1/[6 cos²(pi/(2N))].

Source-historical grids, with alpha=.2:
|N|alpha_crit(N)|actual source-aux E L2 operator norm|low k=(1,1,1) multiplier|
|--:|--:|--:|--:|
|31|0.1670953227|1.3938431881|0.9754359295|
|33|0.1670448627|1.3945663071|0.9783144367|
|35|0.1670028188|1.3951691528|0.9807155063|
|37|0.1669674177|1.3956769863|0.9827390924|
|39|0.1669373298|1.3961087698|0.9844603152|
|41|0.1669115425|1.3964789614|0.9859365085|

alpha=.2 exceeds the sharp threshold for all six N. alpha=.05 and 1/6 remain nonexpansive in the stated odd grid class. Source smooth low modes at alpha=.2 ARE attenuated; an all-input claim is what fails.

## Direct helper checks, masked output gate

Take the lawful real Sym2 field with the sole nonzero diagonal entry
  h_00(n)=cos[2pi*m*(n_x+n_y+n_z)/N], m=(N-1)/2.
This is one high corner Fourier mode. Running the ORIGINAL SHA-matched helper `apply_E(h,'E_lin',dx,2,alpha)` on N=7,9,11,31,41 for alpha=.05,1/6,.2 gives ||E(h)-lambda_E*h||_2/||h||_2 <1e-12 in **all 15 cases**. At N31 and N41 and alpha .2, for EACH interior mask k=2,3,4,5,6, the literal `rms_norm` of the masked h and Eh has sharp ratio |lambda_E| within 1e-12 (**10 cases**). This demonstrates that cropping cannot remove the amplification for this SOURCE-LEGAL E eigenmode; it does NOT establish anything about composed `compute_K_A_out`, its historic masks or nonlinear field source.

An independently written no-dependency Python3 standard-library symbolic-frequency check evaluates all six historical N and alpha=.05,1/6,.2 with all expected threshold and sign controls PASS. The original source snippet is NOT redistributed, and no historical producer-code reconstruction/Colab execution is claimed.

## Typed bridge / earliest unsupported arrow

**POSITIVE:** New KN13 SOURCE-LINEAGE fact + INT8 prior conservative stability range + actual historical odd-N alpha=.2 metadata + source-direct literal E eigenmode -> sharp operator-level FAIL of blanket all-mode L2 nonexpansiveness at alpha=.2.

**FIRST BROKEN MAP:** E auxiliary Fourier norm -> full historical `K_A` calculated with specific smooth (C,h), masks, TT and Lie insertions. The latter is NOT determined by the former. This cannot invalidate frozen 2026-06 diagnostic numerical ratios, promote any physical J3/K/GR/GW statement, nor prove the historical canonical producer even had byte-identical E. Owner M14/MT14 must decide if any future statement *requires* a globally contractive E. The cheapest precise owner route, IF needed, is a typed claim that restricts source frequency support or a model modification with its own identity; not an unprompted run cascade.

**Separate source update, not used in this proof:** XH-S5 T1 on 10 Nov 23:45 found NO timestamped drift/Allan/PSD series IN the actual supplied Schall Source Data ZIP; therefore INT9 ROT007 is still conditional hypothetical math and cannot inherit device-based temporal validation from that archive. XH owns the inventory, M14 owns disposition.

## Repro and limits

Moderator-local report SHA256 c80fed21366cf4e7db0b90e7ff80d245f7639c06ba79c4056a673d82fbf9ce8e. Local ZIP SHA256 47312368d02a8ae49651a2c6a405af17306298a8545eba68be2b18cf7715aa7e, seven members (report + README + two scripts + two frozen JSON + manifest), ZIP CRC PASS, six SHA member hashes PASS, TWO clean isolated-script replays produce byte-identical JSON PASS. `check_e_spectral.py` requires the user's separate exact-SHA checked helper and numpy; `reproduce_math.py` is fully independent stdlib. One initial JSON serialize error (numpy.bool) was fixed and all scientific runs repeated PASS. Neither full local ZIP nor original source helper is assumed uploaded through this GitHub report.

No owner ACK, BW ingestion, referee acceptance, mathematical novelty, canon or execution signature inferred.

**VERDICT: AUX_E_ALPHA020_GLOBAL_L2_CONTRACTION_FAIL / HISTORICAL_SMOOTH_FIELD_DIAGNOSTICS_NOT_FALSIFIED / FULL_KA_AND_PRODUCER_BYTE_TRANSFER_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
