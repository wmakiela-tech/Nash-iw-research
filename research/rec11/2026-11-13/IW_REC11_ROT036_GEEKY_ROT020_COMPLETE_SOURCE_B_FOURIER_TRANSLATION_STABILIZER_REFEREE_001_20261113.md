---
artifact_id: IW_REC11_ROT036_GEEKY_ROT020_COMPLETE_SOURCE_B_FOURIER_TRANSLATION_STABILIZER_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
review_type: I1_NONBLIND_INDEPENDENT_ORIGINAL_M13_FOURIER_TT_INTERVAL_AND_EXACT_INTEGER_LATTICE_REFEREE
status: PASS_GEEKY_ROT020_SCOPED / PASS_COMPLETE_GLOBAL_TWO_POINT_FULL_B_TRANSLATION_STABILIZER_AT_ALPHA_1_OVER_20
ceiling: ORIGINAL_PUBLIC_M13_AUXILIARY_OPERATOR_ONLY / NOT_GLOBAL_SHELL_ENERGY_INJECTIVITY / NOT_PHYSICAL_TRANSLATIONS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
owner_ack: UNVERIFIED
bw_science_receipt: UNVERIFIED
---

# REC11 ROT036 — exact full-Fourier-field translation stabilizer from original M13, N41, alpha=1/20

## Original source and priority

- M13 retains original source and generator priority: [original public Fourier / TT / stencil operator, pinned](https://github.com/wmakiela-tech/Nash-iw-research/blob/91be7247e878a15f3c60949010f9915f3cd7abcb/research/m13/2026-10-24/verify_m13_rot33_interval.py); Git blob **`c6377cfbc9a0070abc34ffedc5871e719f6a4679`**, 8968 characters; directly re-fetched and read by REC11. Relevant original functions: `source()` lines31–41; `delta()`43–45; `em()`47–49; `bracket()`59–68; `lie()`70–79; `proj()`81–94; `calc()`96–106. The original B tensor is exactly `proj(L(C1,L(C2,h))−L(C2,L(C1,h))−L([C1,C2],h))`; its original `inner()` divides Fourier tensor energy by 6, verified at original line142.
- Original source [M13 25 directed B quartic coefficient intervals](https://github.com/wmakiela-tech/Nash-iw-research/blob/91be7247e878a15f3c60949010f9915f3cd7abcb/research/m13/2026-10-26/direct_B.json), Git blob **`a6f50fbe5904e580e84c87ee87c5ad043cdec5d0`**, also checked. This NEW result uses the **Fourier operator**, not the 25 coefficient box.
- **Geeky-S12 ROT020 FIRST** proved covariance under common torus translations of all three source fields, demonstrated the nontrivial exact symmetry `t=(pi,pi,pi)`, ran the original unmodified M13 N41 Fourier source, and proved a strict local 4×4 projective Jacobian rank for translations plus alpha with five FIXED observational mask-energy profiles. [Geeky original ROT020 pinned](https://github.com/wmakiela-tech/Nash-iw-research/blob/91be7247e878a15f3c60949010f9915f3cd7abcb/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT020_SOURCE_FOURIER_TRANSLATION_FIXED_MASK_PROJECTIVE_RANK_LOCAL_ID_AND_PARITY_STABILIZER_001_20261113.md), original source report; firstness not reassigned.
- **REC11 NEW:** full classification of *all* translations leaving the entire B Fourier tensor unchanged at N41, alpha=1/20 (not merely a exhibited subgroup). Original code is **not** imported/executed unchanged by REC in this rotation: the source algebra is independently reimplemented using two distinct mpmath numeric modes plus an independent stdlib exact integer-lattice auditor.

## Theorem — exact two-element global stabilizer of the FULL tensor B

Fix the **same** M13 source fields, N=41, alpha=1/20 and centered stencil/TT, but hypothetically translate **all three input fields** C1,C2,h by the same `t∈(R/2piZ)^3` before applying the original operator, keeping five observational masks FIXED. Source convolutions and diagonal Fourier multipliers imply (Geeky FIRST)

`B_(alpha,t)(m)=exp(i m·t) B_(alpha,0)(m)`.

**REC complete-stabilizer theorem:**

```
{t in (R/2piZ)^3 : B_(alpha,t)(m)=B_(alpha,0)(m) for EVERY m}
    = {(0,0,0), (pi,pi,pi)} mod 2pi.                 (R36.1)
```

**Exact support lemma.** Reading original `source()` directly gives
```
support(C1)={(±1,0,0),(0,±1,0)};
support(C2)={(±1,0,0),(0,0,±1)};
support(h) ={(±1,±1,0)}.
```
Every term contains precisely one C1, one C2, one h; B's Fourier mode can only come from a triple Minkowski sum. Exhaustive *integer-only* independent enumeration finds **41 candidate dictionary modes**, all with **even** coordinate sum; it does **NOT** assert all 41 tensors are nonzero after TT projection. Therefore `(pi,pi,pi)` stabilizes *every* actual B coefficient for all alpha in source.

**Three rigorously nonzero Fourier tensors.** Independent source-formula reimplementation with directed interval `mpmath.iv` at 65 decimal digits yields these strict squared tensor Frobenius lower bounds at alpha=1/20:
```
m=(-3,-1, 0): sum_a,b |B_m,ab|² > 4.0e-15;
m=(-2,-1,-1): sum_a,b |B_m,ab|² > 2.0e-14;
m=(-2,-1,+1): sum_a,b |B_m,ab|² > 2.0e-14.
```
All three *complete directed enclosure intervals* including all 9 complex components and exact sign witnesses are supplied in the local `interval_certificate.json`, and all lower endpoints were checked strictly positive in interval arithmetic. No float64 sign decision or assertion of all-41 nonzero.

**Integer lattice and maximality.** The integer matrix with those three ordered rows has **determinant +2**. These rows therefore generate a sublattice of index 2 in Z³. It lies inside the even-coordinate-sum lattice, itself of index 2; the two lattices are equal. The independent exact stdlib integer program also computes gcd of ALL 3×3 candidate-support minors =2. The annihilator of the even-sum lattice on the translation torus contains precisely the two elements `0` and `(pi,pi,pi)`. Any translation fixing the **entire** Fourier B must fix those three strictly nonzero coefficients, so it lies in that annihilator; both candidate translations fix all coefficients by source parity. This proves (R36.1), with no hidden extra operator-level translation symmetry.

## Independent computational crosschecks and limitations

- Own independent `mpmath` **85-digit** implementation reconstructs Fourier B via source C1,C2,h, centered stencil, E_lin, original Lie/tensor terms and TT projection. Its unmasked Parseval norm **with original factor 1/6** equals approximately `5.678293109054793759445...×10^-14`, matching owner's original unmodified-source output `0.05678293109054794×10^-12` to owner's 17-digit display precision; this is a *sanity check*, not a claim of byte-identical code.
- A separate `mpmath.iv` **65-digit directed-outward interval** script proves the three chosen tensors' norms cannot be zero. The higher-precision 85-digit computed center norms fall strictly inside the interval bounds (checked separately with independent `Decimal` program).
- An unrelated **standard-library integer-only** auditor builds the 41 candidate modes, computes all 3×3 minors' gcd, verifies the 3×3 basis determinant exactly and enumerates the possible stabilizer subgroup without any Fourier floating arithmetic. All integer and interval tests PASS.
- A small `SOURCE_MODE_SUPPORT_EXTRACT.json` preserves the **exact relevant mode supports** manually extracted from original M13 source and its original Git blob reference. It is **not the full original M13 module**. Its SHA256 is `a8b8bd47a36183b606e3cdb106c32066aa9b18210732dbbf9845dd9d5de77aa2`. Three independently executed source-reading verifiers refuse any SHA-mismatched input before science; **3 mutation types × 3 independent scripts = 9/9 correct fail-closed rejections**.
- All full-input mathematical scripts and exact data, full Polish proof, status limits, JSON, stdout and SHA manifest are in user-conversation local standalone archive **`IW_REC11_ROT036_M13_FOURIER_STABILIZER_COMPLETE_INDEX2_REPRO_001_20261113.zip`** (16 files, 19,452 bytes, SHA256 **`4de82d2ec4c457449a8d1fefe3607730085f51b262d676a23c763e555aff4df9`**). CRC PASS, 15/15 payload SHA256 PASS, full isolated ZIP extraction and **4/4 scripts reproduce corresponding JSON and stdout byte-identically**. ZIP is LOCAL only, not claimed hosted on GitHub.

### Important distinction between tensor symmetry and observational identifiability

The result is EXACT for translation vectors which preserve **the entire Fourier tensor B** at **this fixed alpha**. There may be **additional collisions** between translations or alpha values when only the FIVE original shell/mask energies are observed: those are quadratic summaries of B and discard phases. Neither the two-element tensor stabilizer nor Geeky's locally invertible four-observable Jacobian proves full global identifiability from mask energies even *modulo* this Z2. Conversely the locally certified projective rank of Geeky ROT020 is not invalidated by a remote discrete translation symmetry.

The translation is a **precisely posed hypothetical source-field deformation**, *not* a parameter exposed in original `calc(N,alpha)`; no physically moveable mask, hardware gain, source-native 5-shell gains, whole-field realization, historical `dtc0a_runtime_v0_3_1.py` byte identity or physics of NASH K/J3/TPE/GR/GW is proven. Original M13, Geeky priority retained. No BW verified science ingest, no owner adoption/ACK, no external blind I3, no globally novel mathematical result, no CANON, no EXEC_SIGN, no automatic task cascade.

**RETURN_ID:** `IW_REC11_ROT036_GEEKY_ROT020_COMPLETE_SOURCE_B_FOURIER_TRANSLATION_STABILIZER_REFEREE_001_20261113`.

**FINAL:** `PASS_GEEKY_SOURCE_EQUIVARIANCE / PASS_NEW_COMPLETE_TWO_ELEMENT_FULL_B_STABILIZER_AT_ALPHA_0P05 / PASS_3_DIRECTED_NONZERO_TENSORS / PASS_INTEGER_LATTICE_DET2 / HOLD_GLOBAL_SHELL_OBSERVABLE_INJECTIVITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
