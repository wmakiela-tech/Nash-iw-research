# IW_LT4_ROT01_CURRENTNESS_AND_J3_ENTIRE_FORM_FACTOR_NULL_SECTOR_COUNTEREXAMPLE_001_20261012

**FROM:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_02 / LT4 (functional rotation in response to Moderator's "o")  
**STATUS:** LT4 WORKING RESEARCH RETURN / EXACT SCALAR COUNTEREXAMPLE / UNREFEREED  
**CLAIM CEILING:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_INFERENCE / NO_REV021  
**DATE:** 2026-10-12 (CEST)

## 1. Currentness checkpoint

Source of controlling status: LT3->LT4 packet 003, Drive `1USB9w7_RlUZYv0KXiXvPfDfcAWjnQXdc_PxmhLMCM6Q`, and DRAFT018, Drive `1KorpE8IGJlPlDTkBcTs1WvMeepgff7Ga3qcpZP-wKuY`.

* Active LT head: DRAFT018; Drive searches yielded no DRAFT019.
* Last observed programme owner: MT13.
* P2=REV020_PLUS_COMPILER current; P3=HOST_ATLAS_ONLY fallback.
* TPE=HOLD, REV021 not created, T2 not run, compiler utility unmeasured, novelty none.
* H8R: NC A/B/D withdrawn/not established; H8R-C source-interface unresolved. INT7 Thread092 (Drive `1i6FnB7SAfPigmAr9zfGrXiSv6Ij2ctXFgZGKqQ8HJMA`) now supplies a linear/affine consistency -> CP extension -> higher-order normalization -> operational semantics gate. No change in canonical H8R disposition.
* Front B: (A,B) directional rates primary; DE predictive source admission, executor floor actuality, terminal extrapolation and target-weighted effect remain open; no numerical PBH/BBN release.
* J3: NC consolidation card 005, Drive `10qiBj80I7MRRcGlE4k12WljxOvFMwPed`, supersedes its earlier candidate returns where conflicting. Not referee-accepted.

This note does not claim formal succession activation independently of the Moderator's abbreviated rotation instruction.

## 2. The statement being checked

NC's candidate 002 and consolidation 005 give, for `T_C = L_C f(□)`,

```
J3[f] = ( L_C1 [f,L_C2] - L_C2 [f,L_C1] ) f h
       + L_[C1,C2] (f² - f) h.
```

The algebraic identity is correct on a common invariant domain with `[L_C1,L_C2]=L_[C1,C2]`. But the separate assertion that `J3=0` *requires both* `[f,L_C]=0` and `f²=f`, and the consequent unqualified statement that *no nontrivial entire f can close the algebra*, are stronger than this identity entails.

This return gives an exact counterexample in a declared **scalar** carrier. It does **not** provide a counterexample on the project's symmetric-tensor carrier and is not a physical result.

## 3. Exact counterexample

Let the carrier be smooth complex-valued scalar functions on the standard circle `S¹ = R/(2π Z)`. Let `Δ = d²/dx²` with Fourier eigenfunctions `e^{inx}` and eigenvalues `-n²`, `n∈Z`. Let `P_0` be the orthogonal projection onto constant functions. For a smooth vector field `C(x) ∂_x`, the scalar Lie derivative is `L_C u = C(x) u'(x)`.

Define the entire function

```
H(z) = Σ_{k=0}^∞ π^(2k) z^k / (2k+1)!
     = sinh(π √z)/(π √z),
f_a(z) = exp(a H(z)),   a∈R\{0}.
```

The power series proves `H` is entire (the square-root expression is shorthand with a removable point at zero); `f_a` is entire and zero-free. For `n≠0`,

```
H(-n²) = sin(π |n|)/(π |n|)=0,
H(0)=1.
```

Hence spectral calculus gives the exact bounded, nonlocal operator

```
f_a(Δ)= I + (e^a - 1) P_0.
```

Since every scalar Lie derivative kills constants, `L_C P_0=0` for all smooth `C`. Therefore

```
T_C = L_C f_a(Δ) = L_C
```

for **all** smooth vector fields and scalar inputs, and thus

```
[T_C1,T_C2] - T_[C1,C2]
  = [L_C1,L_C2] - L_[C1,C2]
  = 0.
```

Nevertheless,

```
f_a(Δ)² - f_a(Δ) = (e^(2a)-e^a) P_0 ≠ 0.
```

The commutator `[f_a(Δ),L_C]` is generally nonzero. Indeed, taking `C(x)=sin x` and `u(x)=cos x`,

```
L_C u = -sin² x,
P_0 L_C u = -1/2,
[f_a(Δ),L_C]u = -(e^a-1)/2 ≠ 0.
```

Thus all of the following hold **simultaneously**:

* `J3[f_a] = 0` for every pair of smooth vector fields and every scalar input;
* `f_a` is nonconstant, entire and zero-free;
* `f_a(Δ)≠I`, `f_a(Δ)²≠f_a(Δ)`;
* `[f_a(Δ),L_C]≠0` for some `C`.

This is an exact, full-circle spectral construction, not a finite-grid artifact.

## 4. Why this does not contradict NC's measured nonclosure

The modification `(f_a(Δ)-I)u` lies in `ker L_C` for every `C` because it is constant. Hence transport cannot see the nonlocal correction. The family of scalar Lie derivatives has a common invisible output sector, and `T_C` factors through the quotient by that sector.

NC instead studied specific tensor representations and several form factors including `exp(aΔ)`, for which it found nonclosure. The present example does **not** contradict their measured values or prove a full tensor-theory closure result. It only refutes the *unqualified*, carrier-independent necessity inference in NC 002 §1 and consolidation 005 §1.2.

The displayed identity should be retained, with the necessity/projection/no-entire assertions demoted unless accompanied by a theorem with declared carrier, domain, kernel/quotient, and richness assumptions.

## 5. Corrected claim-safe formulation

> For `T_C=L_C f(□)`, the commutator decomposition is an exact identity on a suitable common domain. Vanishing of `J3` does not, without additional carrier assumptions, imply separately `[f,L_C]=0` and `f²=f`. Nontrivial entire, even zero-free, functions can preserve closure when their deformation is invisible to the entire transport representation. Specific operator families and tensor carriers may still exhibit genuine nonclosure; this requires source-native analysis.

Possible next theorem (NOT CLAIMED): characterize closure modulo the common transport-annihilated subspace `N = ∩_C ker L_C`, rather than demand `f²=f` on the full carrier.

## 6. Negative knowledge and placement

* NOT A PHYSICAL COUNTEREXAMPLE; `S¹` scalar transport is not the symmetric-tensor nonlocal-gravity model.
* NO REV021, NO NOVELTY, NO CANON, NO EXEC_SIGN, NO PROGRAMME PROMOTION.
* DOES NOT RESURRECT withdrawn H8R obstructions.
* DOES NOT AFFECT Front B PBH/BBN or T2.
* Candidate for independent algebraic referee and NC wording correction, not a unilateral edit of NC source.

## 7. Direct source links

* LT3 -> LT4 packet 003: https://docs.google.com/document/d/1USB9w7_RlUZYv0KXiXvPfDfcAWjnQXdc_PxmhLMCM6Q/edit
* DRAFT018: https://docs.google.com/document/d/1KorpE8IGJlPlDTkBcTs1WvMeepgff7Ga3qcpZP-wKuY/edit
* NC 002: https://drive.google.com/file/d/137AAdDPepQ21UYKTejO9Xuspc3Ja0vAj/view
* NC consolidation 005: https://drive.google.com/file/d/10qiBj80I7MRRcGlE4k12WljxOvFMwPed/view
* NC H8R correction: https://drive.google.com/file/d/1zxWJdVe8OvI5p5W1g6pyW7vLllcHx8Kb/view
* INT7 Thread092: https://docs.google.com/document/d/1i6FnB7SAfPigmAr9zfGrXiSv6Ij2ctXFgZGKqQ8HJMA/edit

END RETURN.
