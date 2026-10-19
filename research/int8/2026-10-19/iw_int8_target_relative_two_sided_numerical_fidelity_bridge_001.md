---
artifact_id: IW_INT8_TARGET_RELATIVE_TWO_SIDED_NUMERICAL_FIDELITY_BRIDGE_001_20261019
origin: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-19
class: CROSS_FRONT_SCIENTIFIC_INTEGRATION / TARGET_RELATIVE_POSITIVE_BRIDGE_AND_FALSIFIER
exposure: PUBLIC
status: CONDITIONAL_MATHEMATICAL_RETURN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
source_basis:
  - research/lt4/2026-10-19/lt4_finite_profile_frame_to_operator_pseudospectral_gate_001.md
  - research/int7/2026-10-19/int7_xh_s4_feec_pseudospectral_dtc_gate_001.md
  - research/geeky-s10/2026-10-19/geeky_s10_fixed_sensor_available_storage_001.md
cross_surface_sync: GITHUB_BODY_WRITE / BW_INGESTION_NOT_ASSERTED
role_note: One bounded INT integration rotation; prior INT8 sensor-storage return is not superseded
---

# INT8 — Two-sided target-relative numerical fidelity

## 1. Research question and placement

LT4 established a sharp finite-profile frame gate for the norm of a **linear** error operator and INT7 prevented its illegal promotion to DTC/FEEC resolvent fidelity. The new integration question is narrower: when the downstream claim names only a specific family of input preparations and output readings, what is the *cheapest legal sufficient certificate*, and at which first map does it cease to support a global operator/pseudospectral claim?

The relation type here is a **target-relative compression** (an input/output sandwich), not a global operator isomorphism, continuum limit, DTC theorem, or physical bridge. This is elementary finite-dimensional Hilbert-space mathematics and does not establish independent novelty.

## 2. Exact positive bridge on typed finite carriers

Let H and Z be finite-dimensional Hilbert spaces and let E:H->Z be a bounded **linear** error map, with both compared operators already transported to the same typed source and target carriers and norms. Let U=span{v_1,...,v_m} subset H, with orthogonal projection P_U. Assume the frame operator S_U=sum_i |v_i><v_i| on U has lower frame bound alpha>0. Let W subset Z be the exact downstream output/tester subspace and Q=P_W. Define the *target-projected* RMS

r_W^2 = (1/m) sum_i ||Q E v_i||^2.

Then

||Q E P_U||_op <= sqrt(m/alpha) r_W.               (1)

Indeed sum_i ||QEv_i||^2 = tr_U[(E|_U)^* Q (E|_U) S_U] >= alpha ||Q E|_U||_HS^2 >= alpha ||Q E|_U||_op^2.

Consequently, for every normalized input u in U and readout w in W,

|<w, E u>| <= sqrt(m/alpha) r_W ||u|| ||w||.     (2)

The bound is sharp for a rank-one map E x=<x,a>w with a a unit lowest-eigenvalue vector of S_U and w a unit vector in W. For one explicitly fixed list of inputs/readouts the direct measured bilinear errors may be even cheaper than (1).

**Target-relative sufficiency claim:** If and only if the declared downstream *linear* target family factors through the tested sandwich Q E P_U, a certificate on that sandwich suffices for the corresponding linear error readings. It does **not** in general control nonlinear functionals of the underlying operator, trajectories, resolvents, full spectrum, full pseudospectrum, or any target using inputs outside U or outputs outside W.

When the observable is an already declared linear scalar of a response/solution error, (2) is a legitimate cheaper *positive* certificate. One does not need to prove ||E||->0 to control only those finite readings. Conversely, a scalar diagnostic that is not an identified linear E on common carriers is **not** automatically covered.

## 3. Exact obstruction to full operator or transient upgrade

Take H=Z=C^2, U=W=span(e_1), Q=P_U=diag(1,0), and

B=-I,  A_L=[[-1,L],[0,-1]],  E_L=A_L-B=[[0,L],[0,0]].

Then Q E_L P_U=0 for every L, hence the two-sided targeted certificate is exact. Yet ||E_L||=|L|. The full operators have the same spectrum {-1}, while

exp(t A_L)=exp(-t)[[1,Lt],[0,1]],  exp(tB)=exp(-t)I,

so transient behavior for untested preparations differs arbitrarily with L>0 at any fixed t>0. Moreover at z=0, ||(zI-A_L)^(-1)|| grows with L whereas ||(zI-B)^(-1)||=1. Thus neither global resolvent nor pseudospectral fidelity follows from zero target-projected error. This is a standard nonnormal Jordan-block mechanism, not a new mathematical result.

A **target-bounded conclusion** and a **full-carrier pseudospectral conclusion** are different claim classes. Even a correct target-specific experimental certificate may be blind to severe operator error in the discarded input/output sector.

## 4. Claim-to-certificate map

| Downstream claim | Minimal legal object in this finite linear host | Not implied |
|---|---|---|
| Selected linear input/output readings | Individual <w_j,E u_i>, if exact legal readouts | Other preparations, dynamics |
| Uniform linear readings across U x W | ||Q E P_U||; (1) is sufficient under a lower frame bound | ||E|| on H |
| Full operator fidelity | ||E|| on the whole source carrier (or a validated independent complement bound) | Continuum comparison without transfer maps |
| Full pseudospectral perturbation | Same-carrier operator-norm perturbation bound or appropriate resolvent control | Physical validation |
| DTC scalar K_A or K_C over profile set | Direct declared scalar diagnostic with its own normalization/provenance | An operator E, Q, U or W without proof |
| Continuum DTC operator response | Typed continuum/discrete carriers, comparison maps, domains, and appropriate operator-norm/resolvent certificate | Automatically inherited from FEEC or projected TT RMS |

For LT4's full E bound, an independently verified bound b=||E(I-P_U)|| combined with a=||EP_U|| yields the sharper inequality ||E|| <= sqrt(a^2+b^2) by Cauchy-Schwarz on the orthogonal domain splitting; the a+b triangle bound is valid but weaker. This is a standard Hilbert-space tightening, and does not alter the target-only result.

## 5. DTC application gate, first legal break

No current DTC evidence read for this return identifies the measured K_A/K_C residual as Q E P_U for one bounded **linear** difference of transported continuum/discrete solution operators on a shared normed Hilbert carrier. In particular, scalar RMS of a diagnostic under changes of TT test profiles is not the same as RMS of ||Q E v_i|| for a fixed linear E. This is the first unclosed bridge.

Hence:
- POSITIVE_TARGET_RELATIVE_FINITE_LINEAR_THEOREM: PASS under exactly the stated assumptions.
- INTERFACE_TO_LT4_FINITE_PROFILE_FRAME_HOST: PASS as source-native specialization.
- CURRENT_DTC_INSTRUMENT_IDENTIFICATION_AS_LINEAR_E: NOT_ESTABLISHED.
- DTC_FULL_OPERATOR_NORM_CERTIFICATE: ABSENT in the inspected source chain.
- DTC_PSEUDOSPECTRAL_OR_PHYSICAL_FIDELITY: NOT_ESTABLISHED.
- FEEC_DIRECT_TRANSFER: REJECT.

**Cheapest future discriminator** if DTC owners decide this target matters: freeze one actual downstream linear observable, its input/readout spaces, operator realization and norms; test whether its finite-N residual equals one fixed transported linear E_N. If not, stop the frame argument and instead certify the original scalar functional on its declared test class. No new task is assigned by this research note.

## 6. Negative knowledge, currentness and provenance

Target-relative zero is not full-map zero. Testing a spanning *input* profile set is insufficient when output-readout geometry or linearity is ill-typed; a target-sufficient observable need not be globally sufficient for a different claim. Equality of spectra is insufficient for nonnormal transient fidelity. Do not export a finite-dimensional same-carrier theorem to an infinite-dimensional/discrete-continuum limit without comparison-map, stability, domain and relevant convergence contracts.

This note adds a **positive sufficiency branch and sharp no-upgrade witness** to the LT4/INT7 numerical hierarchy; it does not supersede the independently recorded INT8 sensor-storage result or the current LT4 monograph. No source-owner acceptance, BW ingestion, CANON, EXEC_SIGN, originality, or physical outcome is implied.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
