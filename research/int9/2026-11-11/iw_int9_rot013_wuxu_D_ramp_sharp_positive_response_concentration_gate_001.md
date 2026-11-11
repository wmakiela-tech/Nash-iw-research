---
artifact_id: IW_INT9_ROT013_D_RAMP_SHARP_POSITIVE_RESPONSE_CONCENTRATION_GATE_001_20261111
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: CONDITIONAL_POSITIVE_LINEAR_RESPONSE_ONLY / NO_NATIVE_RAMP_RUN / NO_REAL_BBN_KERNEL / NO_BLACKHAWK_PYTHIA / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# INT9 ROT013 — sharp D-band response-weight envelope for a mass-dependent source ramp

## Sources, actual currentness, and priority

Wu–Xu authors FIRST, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02 (2026) 063, https://doi.org/10.1088/1475-7516/2026/02/063 . The pin for their PUBLIC v2 source table and code is `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`.

Mech-S8 ROT017 FIRST verified all 100 original table rows and contrasted original p2 first-edge slope with anchored 12-row p12, constructing an exact flat-edge nonunique continuation: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s8/2026-11-11/IW_MECH_S8_ROT017_WUXU_RATE_TABLE_LOO_FLAT_JET_E4_SOURCE_GATE_001_20261111.md .
Badacz PREREG060 FIRST designed and precommitted native p2-versus-p12 root tests j22,j28, predictions and their own conditional heuristic bracket:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-11/IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_PREREG_060_20261111.md .
Owner prediction data Git blob `179ab4712204b11d307171f0a186f775c62fb406`; prediction code Git blob `39ef45e35e0705c2fc6369e1c73f53b72886cfa0`.
Badacz REVIEW059 FIRST native tightened-tolerance replay maintained two-direction global A1 failure at j22 (G≈1.880), despite better root-fit precision. INT9 ROT006/008/011/012 are earlier conditional positive/count and moment sufficiency gates. This turn DOES NOT take priority for a Wu–Xu source experiment or physical result, and does not assert a native ramp answer exists.

**Distinct INT9 scientific delta:** Prove the exact *sharp* model-conditional positive target-weight envelope for a nonuniform source multiplier, and independently demonstrate why uniform-band rate tests plus monotonicity alone do not make owner PREREG060's number-weighted band-D multiplier an inevitable response bound. This is mature elementary rearrangement/bathtub mathematics, not mathematical novelty.

## Precisely typed source calculation

Use exactly the owner's below-first-grid hypothetical rate family:
- M1=1e9 g and band D `0<M<M_D=105726119.5158 g`, q=M_D/M1=0.1057261195158;
- original v2 mathematical rate `R_h(M)=R_{1,h}(M/M1)^(-p2_h)`; alternative p12 rate gives `k_h(M)=(M/M1)^(-d_h)` with `d_h=p12_h-p2_h>0`;
- on the original mass-only clock, `dt∝M²dM` and normalized *number-of-hadrons* measure `dμ_h(x)=(a_h/q^a_h) x^(a_h-1)dx`, x=M/M1 in (0,q), a_h=3-p2_h>d_h>0.

The **original owner count-weighted ratio** is exactly
 `K_count = ∫ k dμ = q^(-d)*a/(a-d)`.
This formula is already FIRST in Badacz PREREG060; it is correct for a HADRON-NUMBER target.

For a distinct hypothetical *linear* model response J, define nonnegative response density w(x)≥0 normalized by ∫w dμ=1 and the effective ramp factor `K_w=∫w k dμ`. Any such w gives exactly the SAME total response to EVERY uniform k (e.g. k=0,1,2), and is pointwise monotone in k, but gives potentially different output for nonuniform k(x). Because k(x)→∞ as x→0 in the formal author extrapolation and μ has finite ∫k, allowing unknown normalized nonnegative w without an upper bound makes `sup_w K_w=+∞`. It does NOT mean a real BBN response diverges; the true small-M source/energy/timing and endpoint may cut off.

## Sharp conditional POSITIVE theorem (new source-relative interface)

**Additional physical-source hypothesis to be independently justified:** a *single target-specific* normalized positive linear response w satisfies `0≤w(x)≤B` μ-a.e., with known B≥1. For a=3-p2, d=p12-p2, q as above:

`K_min(B)=q^(-d)*a/(a-d) * B*[1-(1-1/B)^((a-d)/a)]`

`K_max(B)=q^(-d)*a/(a-d) * B^(d/a)`.

These bounds are NECESSARY, SUFFICIENT AND ATTAINED in the stipulated class; no optimizer or distribution is guessed. Proof: set `u=(x/q)^a`, then `dμ=du`, `k=q^(-d)u^(-d/a)`, strictly decreasing in u. The elementary bathtub rearrangement principle puts w=B on u∈[0,1/B] for the maximum, w=B on u∈[1-1/B,1] for the minimum, and zero elsewhere. Both weights normalize. Integrate the power exactly to obtain the two formulas. At B=1 both collapse to the original count average. As B→∞, lower tends to q^-d while upper grows `B^(d/a)` unbounded. If the response weight is signed, depends on the perturbation, or the target nonlinear source cannot be linearized with error, none of these formulas automatically applies.

Mature host prior: E. H. Lieb & M. Loss, *Analysis*, Theorem 1.14, Bathtub Principle. No priority claim for the underlying optimization.

**Source-printed five channels:** frozen owner p2,p12 and q. Values below are target-hypothesis examples, NOT confidence/error bands or true BBN limits.

| channel | d=p12-p2 | k at M_D | K_count | sharp K at hypothetical B=10 | sharp K at B=100 |
|---|---:|---:|---:|---:|---:|
| π± | 0.084291488 | 1.208518 | 1.267908 | [1.211453,1.412307] | [1.208802,1.573151] |
| K± | 0.083085940 | 1.205249 | 1.263460 | [1.208127,1.404866] | [1.205527,1.562097] |
| K0L | 0.083307392 | 1.205849 | 1.264257 | [1.208737,1.406162] | [1.206128,1.563994] |
| p/pbar | 0.085531565 | 1.211890 | 1.272501 | [1.214883,1.420002] | [1.212180,1.584602] |
| n/nbar | 0.085639158 | 1.212183 | 1.272905 | [1.215181,1.420691] | [1.212473,1.585635] |

For this artificial mathematical continuation, k>2 only at M<~(2.38–3.05)×10^5 g, which contributes only about 1.68e−5 to 2.76e−5 of source-native *D-band number*; no bound on actual TARGET impact follows without w. Real small-mass BlackHawk/PYTHIA and hadron thermalization remain source-unverified.

## Exact purely rational monotone/uniform-response counterexample

Choose a SEPARATE toy q=1, p2=6/5, d=1/10, so a=9/5 and K_count=a/(a-d)=18/17. Let response w_A=1. Let w_B=2^18 on x∈(0,2^-10), zero otherwise. The latter support has EXACT μ mass (2^-10)^(9/5)=2^-18, hence ∫w_B dμ=1. Its effective ramp response is
 `∫w_B x^(-1/10)dμ = 36/17`.
Both positive response functionals are linear, monotone and have IDENTICAL values under all spatially uniform source multipliers (including all Badacz uniform band x2/x0 diagnostic types), but they differ by factor exactly 2 on the within-band ramp. This exact `Fraction` witness is not a possible simulated BBN or Pythia spectrum and does not prove the actual prereg interval will fail.

## Scientific disposition and currentness

Badacz PREREG060 uses additional *explicit* assumptions: root monotonicity, source band secants under A1, species averaging, numerical fit-SE and 0.010-dex allowance, and takes the D-band per-hadron response nearly constant during last ~3e−4 s. Those assumptions are SCIENTIFIC HYPOTHESES, not mathematical consequences of uniform perturbation tests. Hence the preregistered j22 forecast window [-0.0751339368,-0.0097364840] dex and j28 [-0.0623158337,+0.0022229059] dex are VALID FALSIFICATION WINDOWS, but NOT universally certified all-possible-output envelopes.

Native ramp run to be owned by Badacz: a future PASS would support this particular predictive approximation, not validate the full time-energy kernel or E4 physical PBH bound; a FAIL would refute the declared transfer at the tested j, not invalidate measured native uniform C/D secants. At source check on 11 Nov no confirmed native ramp review was located; therefore NO PASS/FAIL is declared. One cannot infer new real PBH limits. Mech-S8 retains E4 owner; MT15 scope; REC11/AUD1 external referee; KN13 custody; no new task cascade.

## Local reproducibility and custody

Executed a separate Python3 stdlib `fractions.Fraction` rational witness and source-printed five-species arithmetic. 1250 groups PASS: 1200 randomized nonnegative normalized 64-cell response weights with B=2,10,100 checked against closed sharp bounds using an independently coded interval primitive; 20 base cases and 30 alternative integration checks. Exact rational `18/17→36/17` PASS. Original author Julia, native Badacz ramp and BlackHawk/PYTHIA NOT RUN. Full Polish local report SHA256 `9d45eb0a1c558c3adf2525176dfd9c0704c4d02272d513759935e17e2ffc633e`; Moderator-local five-file ZIP SHA256 `168065b9109a327ce1fccffd7543db64031d3b3613b2274710eede808891a4ee`; ZIP CRC PASS, 4 member SHA256 PASS, clean extracted script JSON BYTE IDENTICAL PASS. Local ZIP files NOT hosted by this public text. BW ingest, owner adoption, independent referee unverified.

**STATUS:** `CONDITIONAL_B_BOUNDED_SHARP_ENVELOPE_PASS / UNIFORM_BAND_SECCANT_TO_NONUNIFORM_RESPONSE_NO_MAP / PREREG060_NATIVE_PENDING / PHYSICAL_E4_SOURCE_BLOCK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
