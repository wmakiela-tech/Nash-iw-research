---
artifact_id: IW_M15_ROT014_FIVE_SHELL_OBSERVATION_COMPLETE_COMMON_PERIOD_SUBGROUP_001_20261113
return_id: IW_M15_ROT014_ORIGINAL_M13_FIVE_OBSERVABLE_SHELL_UNIFORM_TRANSLATION_PERIOD_LATTICE_IV55_CERT_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: DIFFERENT_CELL_I1_INTERNAL_NONBLIND_INDEPENDENT_ORIGINAL_SOURCE_FORMULAE_FOURIER_OBSERVATION_PERIOD_SUBGROUP_EXACT_LATTICE_AND_DIRECTED_55_DPS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_M13_N41_FOURIER_FORMULAE_REIMPLEMENTED / HYPOTHETICAL_COMMON_FIELD_TRANSLATION_FIXED_MASK_OBSERVER / EXACT_COMMON_PERIOD_GROUP_NOT_GLOBAL_INJECTIVITY / NOT_ORIGINAL_MODULE_BYTE_EXECUTION / NOT_HISTORICAL_DTC0A_PRODUCER / NO_EXTERNAL_I3 / NO_PHYSICAL_FIELD_TRANSLATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# M15 ROT014 — exact global common period subgroup of all FIVE observed M13 B shell energies

## 0. Scientific result and key non-implication

**New source-specific, independently interval-certified mathematical closure of a narrower gap than full global identifiability.** At N=41 and alpha=1/20, for the original public M13 auxiliary sparse Fourier B operator, mathematically EXTEND its frozen original input fields C1,C2,h by a common translation t in a continuous 3-torus, but hold all five source spatial observation masks FIXED. Let
    S(t)=(s1(t),s2(t),s3(t),s4(t),s5(t))
be the five source disjoint-shell energy averages, with s5(t)=g6(t) the innermost mask energy. The **COMMON PERIOD SUBGROUP** is
    Per(S)={h in R3/(2pi Z3) : S(t+h)=S(t) for EVERY t in R3/(2pi Z3)}.

M15's new independent 55-digit directed interval calculation on the original M13 SOURCE-EQUATION reconstruction proves
    Per(S) = { (0,0,0), (pi,pi,pi) } mod 2pi.     (M14.1)

More strongly, the SINGLE scalar fifth shell energy g6(t) already has exactly this same complete global PERIOD subgroup. This is a genuinely different mathematical object from ROT013's complete period subgroup of the FULL Fourier B TENSOR, since it checks nonzero Fourier coefficients AFTER the fixed spatial mask and quadratic energy aggregation; an aggregation could have erased the full tensor information. In this exact source it DOES NOT enlarge the group of globally uniform translation periods.

**CRITICAL NON-IMPLICATION:** No claim that the observation vector S(t) is globally injective modulo these periods, or that S(t)=S(t') at ONE t,t' forces t'-t to be a period. Non-period accidental POINTWISE aliases may exist and are UNCLASSIFIED. No global inversion of alpha and translation, physical translation parameter or calibration is asserted. The weak assertion that the COMMON PERIOD subgroup is precisely two elements must never be mislabeled "complete global inverse" or "no other aliases".

## 1. Source priority and original surfaces

M13 FIRST original public N41 B sparse Fourier bracket/Lie/TT operator source and five-mask source coefficient table.
- ORIGINAL author module: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
  immutable original Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, directly fetched and verified again this rotation.
- ORIGINAL B source 25 directed quartic coefficients:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json
  immutable original Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, independently fetched and verified again.

Geeky-S12 ROT020 FIRST introduced the source-equation hypothetical common spatial torus translation against FIVE FIXED masks, demonstrated rank4 projective alpha+3-shifts and found original even-parity nonzero (pi,pi,pi) tensor symmetry. Its original public scientific report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/91be7247e878a15f3c60949010f9915f3cd7abcb/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT020_SOURCE_FOURIER_TRANSLATION_FIXED_MASK_PROJECTIVE_RANK_LOCAL_ID_AND_PARITY_STABILIZER_001_20261113.md

M15 ROT013 FIRST gave a separate 50-dps independent formula-IV confirmation of Geeky ROT020 full LOCAL rank and a complete EXACT two-element translation stabilizer of the UNOBSERVED FULL Fourier B tensor, using three original nonzero tensor modes with integer determinant 2:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2613b178cfac6c1ede7f551bcbe6c3707bfbf17a/research/m15/2026-11-13/IW_M15_ROT013_INDEPENDENT_SOURCE_FOURIER_TRANSLATION_RANK_AND_EXACT_TENSOR_STABILIZER_001_20261113.md

Geeky ROT021 subsequent FIRST computed a separate hypothetical local Fisher information/noise projection and leave-one-shell-out result; M15 ROT014 does NOT claim to audit ROT021 or establish source noise accuracy or robust statistical information.

The new M15 ROT014 checks a DIFFERENT, globally defined observation period question with independent Fourier coefficients gamma AFTER the fixed mask. M13 source priority and Geeky ROT020 original translation priority are preserved. All underlying Fourier/annihilator lattice mathematics is classical, so **NO NOVELTY**.

## 2. Fourier coefficient formula for the observed fixed-mask energy

The original public M13 source Fourier tensor at N=41, alpha=1/20 has 41 nonzero-support mode keys m in Z3 (some individual coefficients may be zero). The source bracket and Lie operations are translation-equivariant. For a hypothetical COMMON shift t of all three source fields, one has EXACTLY
    B_m(t)=exp(i m dot t) B_m(0),
while FIXED source windows are not shifted.

The innermost observed energy is s5(t)=g6(t). From the original fixed-mask quadratic Fourier norm with the original 1/6 factor:
    g6(t) = sum_(q in Z3) gamma_q exp(i q dot t),
    gamma_q = [prod_(j=1..3) W6(q_j)] / 6
             * sum_(m-n=q) <B_m,B_n>,
where <B_m,B_n>=sum_(a,b) B_m,ab conjugate(B_n,ab), and W6(q_j) is the ORIGINAL M13 fixed-mask one-axis Fourier window coefficient at k=6. This is NOT a first-principles physical claim. It is exact finite Fourier algebra derived by expanding the original observed squared norm.

The independent M15 checker does NOT call the Geeky ROT020/021 code, reported Jacobian or numerical gamma. It takes the M15 ROT012 separately authored source-equation reconstruction, verifies its SHA256 BEFORE importing it, changes only its mpmath arithmetic backend to outward-directed iv.dps=55, and independently enumerates ALL 41x41=1681 source mode pairs into EXACTLY 221 possible Fourier differences q=m-n. It then reconstructs three individual observed gamma_q, not whole tensor amplitudes or local Jacobians. All 221 possible q have even total coordinate parity because all 41 B mode indices have even parity.

Source code provenance: original M15 standalone source-equation reconstruction SHA256
    4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e.
This is NOT original M13 source module byte-execution; the original M13 source is used as the publicly verified mathematical host. Earlier independent M15 ROT012 regression matched all original B 25 quartic source midpoint coefficients to approximately 9.3e-17 relative in high precision numerical display. The present IV55 gamma proof remains SOURCE-CONDITIONAL to that independently implemented equation host.

## 3. NEW three nonzero observed gamma and exact integer determinant

At original alpha=1/20 and source fifth observed shell s5=g6, select observed Fourier difference wavevectors
    q1=(-2,0,0),
    q2=(0,1,1),
    q3=(3,0,-1).
The independent program includes respectively 26,20,14 matching original tensor mode pairs for these q. Its iv.dps=55 directed enclosures for gamma are strictly nonzero by checking the LOWER endpoint of |gamma|²=Re(gamma)²+Im(gamma)² is STRICT >0. The complex amplitudes below are DISPLAY approximations ONLY; the machine JSON contains all complete outward lower/upper IV bounds for both Re and Im and squared magnitude.

| observed q | approximate Re gamma | approximate Im gamma | strict exact-IV lower squared-norm sign |
| --- | ---: | ---: | --- |
| (-2,0,0) | +4.24616095364321e-15 | +6.55859829513156e-16 | >0 PASS |
| (0,1,1) | -4.70553572491007e-16 | +7.26814619605893e-17 | >0 PASS |
| (3,0,-1) | +2.67605390773862e-17 | +1.73252806492490e-16 | >0 PASS |

Their EXACT INTEGER determinant, independently computed, is
    det[q1;q2;q3] = +2.
These three NONZERO Fourier OBSERVABLE coefficients therefore force the lattice Lg6 generated by all nonzero gamma_q to contain a full-rank sublattice with index 2 in Z3.

Independently, every possible q=m-n from source B support belongs to even-parity sublattice
    E={q in Z3: qx+qy+qz even},   [Z3:E]=2.
Therefore q1,q2,q3 belong to Lg6, and all of Lg6 belongs to E; since the three witness q already span an index-2 sublattice,
    span_Z(q1,q2,q3) = Lg6 = E, EXACTLY.
Neither a 3D numerical mode fit nor a sampled t-grid is used in this lattice argument.

## 4. Exact proof of COMPLETE observable period subgroup

For a finite Fourier polynomial g6(t)=sum_q gamma_q exp(i q.t), a vector h is a PERIOD FOR ALL t iff
    g6(t+h)=g6(t) for EVERY t.
Uniqueness/linear independence of Fourier characters exp(i q.t) gives the exact necessary and sufficient condition
    gamma_q [exp(i q.h)-1]=0 for EVERY q.
Since Lg6=E, this is equivalent to exp(i q.h)=1 for EVERY even-parity q. The annihilator E-perp in the 3-torus consists EXACTLY of
    h in {(0,0,0),(pi,pi,pi)} modulo2pi.

To extend from just g6 to the full five-shell observation vector, use two inclusions:
- A COMMON period of S must in particular preserve its fifth coordinate g6, so Per(S) is a subset of the proven two-element group.
- EVERY original source B output Fourier mode has even total parity. Thus the common shift (pi,pi,pi) multiplies EVERY B_m by exp(i*pi*even)=1 and preserves ALL original fixed-mask energies and five shells. The zero shift trivially preserves them.
Hence Per(S) contains both points and is contained in those two; this proves formula (M14.1).

**Important:** Per(S) is the common translation PERIOD subgroup. It is NOT a description of all pointwise coincidences of S, NOT a proof that S(t)=S(t') implies t'−t in Per(S), and NOT a unique inverse for (alpha,t). A single scalar g6 obviously cannot globally identify a full continuous 3D shift, despite having a finite period subgroup; the same logical distinction must be retained for five shells. The previous Geeky/M15 rank4 local IV result concerns local invertibility at t=0, not all global aliases.

One may also permit an UNKNOWN POSITIVE CONSTANT common energy gain c under the stronger condition S(t+h)=c S(t) FOR ALL t and the SAME c. Integrating any positive-energy shell over the torus yields c=1 because its mean is positive, reducing to the same period subgroup. This observation does NOT cover gains c=c(t) allowed to change with t or merely at pairs of points; no statement about the global period group in full projective observation space under point-dependent scaling is made.

## 5. Independent controls and reproducibility

The original M15 ROT014 Python3 source mathematical reviewer is newly written, not imported from Geeky, and ACTUALLY executed on the locked independent source-formula host:
    verify_m15_rot014_observed_shell_period_lattice.py
    SHA256 6a5becf5a7caa24878e794673b9baba0cb5b929d39c86fdee485d6c2a8af69fc.
The actual original computed complete directed result JSON including all three gamma complex component enclosures:
    m15_rot014_observed_five_shell_period_exact_results.json
    SHA256 fd77d275c9a2eeae044355f76ac0102b61821c4f7d216baf052aa1e76a0fb206.

Executed verification PASS:
- original source-formula dependency SHA lock pre-import PASS;
- 41 even-parity source tensor Fourier mode indices PASS;
- 221 possible source energy Fourier difference q, each even parity PASS;
- all THREE selected observed gamma_q have strictly positive 55-digit directed |gamma|² lower bound PASS;
- independently evaluated negative-q Hermitian conjugate coefficients gamma_-q=conj(gamma_q) enclose ZERO difference for all three PASS;
- summing 221 observed gamma_q at t=0 encloses the independently computed direct original fixed-mask source energy inner(B,N,6) and both have strictly positive energy PASS;
- exact 3x3 integer det +2 PASS;
- analytic lattice/torus character argument for Per(S) EXACTLY two elements PASS.

The new original source verifier plus original locked formula file, original full directed result JSON, README, original stdout, isolated rerun stdout, fail-closed tamper fixture and SHA256 manifest were bundled in a user-conversation-local reproducibility archive:
    IW_M15_ROT014_FIVE_SHELL_OBSERVATION_FULL_PERIOD_STABILIZER_EXACT_IV_REPRO_001_20261113.zip
Size 13,200 bytes; SHA256
    59ca49769fcc698c7c41919e4f552d083facb58656bfac44dc9336df8c195530.
Archive CRC PASS, all 7/7 payload SHA256 manifest checks PASS, clean reexecution in isolated temporary folder produces byte-identical full original JSON PASS. One-byte adversarial corruption of the locked source formula dependency is rejected with PRE_SCIENCE_SOURCE_FORMULAE_HASH_MISMATCH BEFORE mathematical computation, FAIL-CLOSED PASS. These controls are nontrivial reproducibility tests but not a formal all-code security/fuzz proof. The exact local archive includes source formula reconstruction, NOT original byte-identical M13 module or historical DTC0a runtime.

The original M13 public source and B25 table were both independently re-fetched from pinned GitHub SHA this rotation and their Git blobs verified. The newly executed mathematical script and full interval data remain in the local conversation ZIP; THIS public science report and a separate curated JSON constitute public visibility, not a false claim of GitHub binary mirror. The native M13 original Python or missing historical dtc0a_runtime_v0_3_1.py were NOT byte-executed.

## 6. Strict scope and stop

This result strengthens ROT013's exact FULL-TENSOR stabilizer conclusion by checking the effect of the ACTUAL fixed observation mask. For the mathematically enlarged source fields, no additional UNIFORM periods of five observed energies exist beyond (pi,pi,pi); the global pointwise inverse and additional accidental aliases remain OPEN.

This does not make hypothetical common translations a source-native tunable parameter; original source() has fixed Fourier field coefficients and no t argument. No physically realized translation, physical Fourier-field uncertainty, experimental instrument mask shift, NASH K/J3/TPE, Schall optical sensor time covariance, Wu-Xu PBH/BBN or RNN animal data are involved. The observed scalar fifth-shell period algebra is mathematical only, not a new law or new physics. Geeky ROT020/021 author results and M13 original firstness preserved; no claim of external blind I3 or recipient signoff.

BW GITHUB_PENDING_BW_INGEST, KN14 source-event custodian, not actual BW ingest receipt. No CANON, EXEC_SIGN, owner override, extra new tasks or automatic continuation demanded.

FINAL:
M15_ROT014_FIVE_SHELL_OBSERVABLE_COMMON_PERIOD_EXACT_TWO_ELEMENT_GROUP_PASS /
ORIGINAL_M13_FORMULA_41_MODES_221_DIFFERENCE_Q /
THREE_OBSERVED_G6_FOURIER_COEFFICIENTS_DIRECTED_IV55_NONZERO_PASS /
EXACT_INTEGER_DET2_LATTICE_INDEX2_PASS /
HERMITIAN_AND_DIRECT_MASK_ENERGY_CROSSCHECK_PASS /
GLOBAL_POINTWISE_INVERSE_NOT_PROVEN /
SOURCE_FORMULA_NOT_ORIGINAL_AUTHOR_BYTE_EXECUTION /
ORIGINAL_CODE_RERUN_BYTE_IDENTICAL_AND_TAMPER_FAIL_CLOSED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
