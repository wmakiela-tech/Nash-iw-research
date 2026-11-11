---
artifact_id: IW_MT15_ROT001_WUXU_SUBEDGE_TAIL_SHARP_PARTIAL_IDENTIFICATION_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
document_type: REPORT
exposure: PUBLIC
claim_ceiling: CONDITIONAL_SOURCE_TABLE_MASS_CLOCK_PARTIAL_IDENTIFICATION / NO_HADRON_PHYSICAL_VALIDATION / NO_BBN_Yp / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
status: RESEARCH_RETURN / INDEPENDENT_JS_CALCULATION / PYTHON_REPRODUCER_NOT_EXECUTED_IN_THIS_TURN
acceptance_owner: Mech-S8 (physics owner); Badacz (native data FIRST); Moderator (executive)
return_path: Moderator / MT15; scientific owner Mech-S8 on actual receipt
---

# MT15 ROT001 — What late hadron-number emission survives the Wu–Xu below-grid source hold?

## Decision class and source / author priority
Source Wu–Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, arXiv:2509.05618, published JCAP 02 (2026) 063, doi:10.1088/1475-7516/2026/02/063. Author repo @ d395183674cace6c9906a8911bdeb7234ba4040d; pinned original 100-row table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, Git blob `06d0883a27b108692720422294ba2baacd381a64`.

Badacz REVIEW057 FIRST native Julia heavy clock & post-Tnuc emitted hadron counts. Original 8-row clock at project public commit 5b5521ed1f057d341c1a410193e9a923c8ca1f8e, path `research/badacz/2026-11-11/data/heavy_end_clock.csv`, Git blob `357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e`. MT14 ROT029 FIRST own exact 5-channel log-log table quadratures and conditional endpoint non-map. Mech-S8 ROT015 FIRST primary/secondary energy-domain audit and ROT016 FIRST rate-only spectral nullspace. Rec11/INT9/AUD1 distinct current A1 crosschecks; not reassigned.

**New narrower question:** after discarding **all** unvalidated author-rate extrapolation below the first tabulated PBH mass 1e9 g, what fraction of emitted hadron NUMBER remains post-Tnuc in the same frozen Wu–Xu rate-table/clock model? Does arbitrary nonnegative continuation below the grid permit a LOWER late-number fraction?

## Source types, operator, target, held assumptions
SOURCE: original Wu–Xu five total hadron-number rate functions R_h(M) at 100 masses from 1e9 to 4e12 g; ORIGINAL_NATIVE_EVENT: Badacz four M(Tnuc) from j98/j99 and two beta points; CARRIER: classical mass trajectory dM/dt=-K/M^2, K>0 fixed, with unchanged event masses. OPERATOR: piecewise log-log interpolation between original table rows, exact integrals of M² R_h(M)dM (K cancels in fractions). INSTRUMENT: none; deterministic source-model quadrature. OBSERVABLE: fraction of mathematical hadron number emitted after the Tnuc event; NOT Yp, D/H, neutron conversion, or number density at BBN.

All four native M(Tnuc) exceed 1e9 g (2.489091e9, 2.523417e9, 4.580037e9, 4.613379e9 g); therefore every contribution below first table mass occurs after Tnuc in the frozen mass-order model. Hold all above-first-row rates and clock fixed. The unknown below-first-row tail U is assumed nonnegative but otherwise arbitrary and has no verified physical normalization.

## Mature host, theorem, proof and novelty subtraction
Classical **partial identification / monotone mixture bounds**, closely related to C.F. Manski (2003), *Partial Identification of Probability Distributions* (Springer, DOI 10.1007/b97478). No general theorem novelty.

Define T>0 total integrated hadron number above grid floor M*, 0<L<T its post-Tnuc subportion above the floor, and U>=0 arbitrary below-grid tail. The exact frozen-model late fraction is
F(U)=(L+U)/(T+U), with derivative F'(U)=(T-L)/(T+U)^2>0.
Thus the SHARP identified set with unconstrained nonnegative finite U is [L/T,1). U=0 attains lower bound; U -> infinity approaches 1. Adding an arbitrary below-grid nonnegative hadron-number source cannot reduce this CONDITIONAL numerator/denominator fraction. Without an independent U maximum, no finite sharp upper <1 exists. Without the fixed-above-grid and fixed-clock hypotheses, this bound does not transfer.

For interpolation segment R(M)=R_i(M/M_i)^p and mass clock dM/dt=-K/M², the quadrature is
I(a,b)=R_i M_i^3 / K * ((b/M_i)^(p+3)-(a/M_i)^(p+3))/(p+3).
For p=-3 replace ratio by log(b/a). The first-pair log-log extrapolation has five slopes p roughly -1.19665 to -1.20476, so its integral to zero is finite within THAT hypothesis, but unverified physically.

## Exact source-row calculation (JS on fetched pinned original 100 rows, 2026-11-11)
| native case | sharp lower f=L/T, no subedge | MT14 / original first-pair tail f | extrapolated U / total | extrapolated U / post-Tnuc |
| --- | ---: | ---: | ---: | ---: |
| j98 beta 1e-30 | 0.07986575027149 | 0.09787569531776 | 0.01957317103628 | 0.19997989258452 |
| j98 beta 10^-19.2 | 0.08225696033744 | 0.10022010182011 | 0.01957317103628 | 0.19530184744189 |
| j99 beta 1e-30 | 0.25163833316559 | 0.26559907297183 | 0.01865507070304 | 0.07023771014825 |
| j99 beta 10^-19.2 | 0.25500814557970 | 0.26890602129710 | 0.01865507070304 | 0.06937394191865 |

Cross-check: all four model-with-tail fractions agree with independent MT14 ROT029 to displayed ~1e-14; ROT029 reports agreement with original Badacz late fractions to <1.4e-11. A separate JS computation fetched and operated on all 100 original source rows plus the original eight native clock rows, NOT a synthetic dataset, NOT re-running Julia, NOT any physical BlackHawk. Reproducer code in this same directory is a non-executed Python port to enable independent replay (claim its status precisely).

## Interpretation and actual falsifier
The claim that the 10%-27% MODEL_NUMBER post-Tnuc fraction is entirely an artifact of post-1e9g source extrapolation is FALSIFIED in the frozen rate-table model: ~8% for j98 and ~25% for j99 already arises from the tabulated mass domain (with current clock). Conversely, any claim of a 10%-27% *physical helium response* is still invalid: missing E-dependent spectra/charge separation, time/temperature collision/thermalization response, full BBN target and original BlackHawk producer provenance. Above-grid tabulated number rates do not certify real physics.

The above sharp lower bounds are **not confidence intervals**, not physically conservative emission bounds and not bounds on Yp. A physically changed below-grid source can alter evaporation timing, thermodynamics or emission above-grid; those cases violate frozen-carrier assumptions. Nonnegative *number* need not imply signed/positive helium response kernel. Wu–Xu §4.1 itself integrates secondary spectra and applies rapid-thermalization assumptions; Kohri & Yokoyama, Phys Rev D 61 023501 (1999), and Kawasaki/Kohri/Moroi, Phys Rev D 71 083502 (2005), distinguish hadronic n-p conversion and later hadrodissociation.

### Source-native next decisive test (owner: Mech-S8 + Badacz source)
Do NOT recompute this number integral. To decide whether this conditional survivor matters for physical Yp, run the original/source-legitimate after-Tnuc nuclear/collision response with checked charged hadron/antihadron, energy-dependence, exact BlackHawk tables, and network targets. If the physical response is zero or source energy production excluded at those times, the number-only survivor does not support a late Yp correction. If a source-validated response is demonstrably nonzero and reaches held-out calibrations, reopen physical inference for owner review. THIS file makes neither outcome.

## Reproduction from clean source checkout
Download exact original table and eight-row clock using the pinned public GitHub source links above (compare Git blob SHA if available). Save as `hadrons_from_PBH.dat`, `heavy_end_clock.csv`, and run:

`python3 -I iw_mt15_rot001_tail_partial_identification_reproducer.py --table hadrons_from_PBH.dat --clock heavy_end_clock.csv`

Expected 4 rows and f_with_tail matching the four published ROT029 values within 3e-10. Python implementation not executed in this turn; this is a documented reproducibility gap, not a replay PASS. The ACTUAL independent source-row JS quadrature was executed and crosschecked.

## Custody and decisions
Source-first, no duplicate claims from Badacz/MT14/Mech. PUBLIC research; GitHub storage/readback separate from BW. `GITHUB_PENDING_BW_INGEST`; NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
