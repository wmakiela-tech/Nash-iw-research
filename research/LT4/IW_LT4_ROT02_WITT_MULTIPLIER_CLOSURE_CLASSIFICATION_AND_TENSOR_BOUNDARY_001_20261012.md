# LT4 ROT02 — Witt-multiplier closure classification and tensor boundary

**RETURN_ID:** `IW_LT4_ROT02_WITT_MULTIPLIER_CLOSURE_CLASSIFICATION_AND_TENSOR_BOUNDARY_001_20261012`  
**FROM:** `IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_02 / LT4`  
**DATE:** 2026-10-12  
**STATUS:** exact formal calculation, narrowly typed / numerical sanity check / working research note, not independent referee approval  
**CLAIM CEILING:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_REV021 / NO_TPE_PROMOTION / NO_PHYSICAL_INFERENCE`.

## 0. Purpose and provenance

This builds on the GitHub LT4 ROT01:
`research/LT4/IW_LT4_ROT01_CURRENTNESS_AND_J3_ENTIRE_FORM_FACTOR_NULL_SECTOR_COUNTEREXAMPLE_001_20261012.md`.

Source candidate: `IW_NC_J3_CONSOLIDATION_CARD_005_20261012`, Drive `10qiBj80I7MRRcGlE4k12WljxOvFMwPed`; NC 002 Drive `137AAdDPepQ21UYKTejO9Xuspc3Ja0vAj`. The general identity for `J3[f]` is an algebraic decomposition. The *unqualified* conclusion that closure requires both `[f,L_C]=0` and `f²=f`, and hence that no nontrivial entire `f` closes, needs carrier and visibility assumptions. ROT01 gave an exact scalar counterexample.

This return proves the **complete classification** of this issue for arbitrary Fourier-diagonal multipliers acting on scalar trigonometric polynomials on `S¹`, exhibits a symmetric-rank-2 tensor countercontrol, and states what transfers to the continuum and what does not.

This is not a theorem about the project's original multidimensional symmetric-tensor model, gravitational transport, gauge symmetry, or physical form factors.

## 1. Theorem (full classification in scalar Witt representation)

Let `A = C[z,z^{-1}]` be scalar trigonometric polynomials with basis `u_n(x)=e^{inx}`, `n∈Z`. Let `V=span_C{C_k=e^{ikx}∂_x : k∈Z}` be the complexified polynomial vector fields (Witt algebra). Let `F:A→A` be an arbitrary Fourier multiplier:

```
F u_n = μ_n u_n,  μ_n ∈ C.
L_{C_k} u_n = i n u_{n+k}.
T_{C_k} = L_{C_k} F.
```

Then the representation identity

```
[T_C, T_D] = T_[C,D]  for ALL C,D∈V on ALL u∈A
```

holds **if and only if** exactly one of the following conditions holds:

* **ZERO TRANSPORT:** `μ_n = 0` for all `n≠0` (`μ_0` arbitrary); hence `T_C=0` for every `C`.
* **CLASSICAL TRANSPORT WITH INVISIBLE ZERO-MODE FREEDOM:** `μ_n = 1` for all `n≠0` (`μ_0` arbitrary); hence `T_C=L_C` for every `C`.

These two families intersect only when the demand is inconsistent (they require `μ_n=0` and `1` for nonzero `n`), so they are disjoint.

If `F=f(Δ)` with `Δ=d²/dx²`, and `f` is a zero-free entire function, the ZERO TRANSPORT case is excluded; consequently closure is equivalent to `f(-n²)=1` for every nonzero integer `n`. `f(0)` is unconstrained.

### Proof (direct Fourier/Witt computation)

For arbitrary integers `n,k,l`, the tensor-free Fourier coefficient of `J=[T_{C_k},T_{C_l}]-T_[C_k,C_l]` on `u_n` is:

```
J(C_k,C_l) u_n
 = n μ_n [ (n+k) μ_{n+k}
          -(n+l) μ_{n+l}
          -(k-l) ] u_{n+k+l}.
```

Since `[C_k,C_l] = i(l-k)C_{k+l}`, the sign follows directly from the standard Lie bracket.

Rewrite the coefficient as

```
n μ_n { (n+k)(μ_{n+k}-1) - (n+l)(μ_{n+l}-1) }.
```

If `μ_n=0` for every `n≠0`, then `T=0` and closure holds. Otherwise choose `n_0≠0` with `μ_{n_0}≠0`. Given *arbitrary* integers `m,p`, select `k=m-n_0`, `l=p-n_0`. Vanishing of the coefficient forces

```
m(μ_m-1)=p(μ_p-1).
```

Taking `p=0`, the right side is zero, so `m(μ_m-1)=0` for every `m∈Z`. Hence `μ_m=1` for every `m≠0`, while `μ_0` is arbitrary. Conversely that condition gives `T_C=L_C` because scalar Lie derivatives annihilate constants. QED.

For a bounded multiplier `F` the theorem extends from trigonometric polynomials to smooth fields by continuity and Fourier-density. The algebraic classification above does not require boundedness because each trigonometric-polynomial input yields finite sums.

## 2. Zero-free entire-form-factor witness

Let

```
H(z)=sinh(π√z)/(π√z)
    = Σ_{j≥0} π^(2j) z^j / (2j+1)!,
f_a(z)=exp(a H(z)),   a∈R\{0}.
```

The power series makes `H` entire and the exponential `f_a` entire and zero-free. On the circle,

```
H(0)=1; H(-n²)=sin(π|n|)/(π|n|)=0   (n≠0).
f_a(Δ)=I+(e^a-1)P_0.
```

For `a=log 2`, `F=I+P_0` and `μ_0=2`, `μ_n=1` for nonzero `n`. Its action is nontrivial on constants but `L_C P_0=0` for the scalar carrier, so `T_C=L_C` and `J=0`.

Nevertheless `F²-F=2P_0 ≠0`; and for `C=sin(x)∂_x`, `u=cos x`, `[F,L_C]u=-1/2`, nonzero. Thus neither `F²=F` nor `[F,L_C]=0` individually is necessary for closure in this carrier.

**Terminology guard:** `NONTRIVIAL_OPERATOR != NONTRIVIAL_TRANSPORT`. `f_a(Δ)≠I` while `T_C=L_C`. The correct representation-level conclusion here is that no genuinely modified nonzero scalar transport action remains closed within this Fourier-multiplier family.

## 3. Exact tensor boundary (rank-2 covariant fields, one circle)

The null-sector argument **does not transfer automatically** to tensors. For rank-2 covariant fields `h=u(x)(dx)^2`, Lie transport is

```
L_C h = (C u' + 2 C' u)(dx)^2.
L_{C_k}[u_n(dx)^2] = i(n+2k)u_{n+k}(dx)^2.
```

Use the same `F=I+P_0` applied to the coefficient `u`. Set

```
C_+ = e^{ix}∂_x, C_-=e^{-ix}∂_x,
h=e^{ix}(dx)^2.
```

Direct Fourier steps give:

```
T_{C_-}h = -i(dx)^2,
T_{C_+}T_{C_-}h = 4e^{ix}(dx)^2,
T_{C_+}h = 3i e^{2ix}(dx)^2,
T_{C_-}T_{C_+}h = 0,
[C_+,C_-] = -2i ∂_x,
T_[C_+,C_-] h = 2e^{ix}(dx)^2.
```

Therefore,

```
J(C_+,C_-)h = 2e^{ix}(dx)^2 ≠0.
```

This is a mathematically exact **countercontrol**: a zero-mode deformation invisible for scalar transport is visible in a covariant-tensor representation, because even constant tensor coefficients transform under nonconstant vector fields. It does not compute the project's original J3 in higher-dimensional gravity.

## 4. Broader operator lemma (the actual source of scalar invisibility)

Let a representation `L_C` act on a vector space `H`. If `F=I+N` and

```
Ran N ⊆ ⋂_C ker L_C,
```

then `T_C=L_C F=L_C` for all `C`, so `J=0` regardless of whether `F²=F` or `[F,L_C]=0`.

This is a sufficient condition, not an assertion that every closure mechanism has this form on all carriers. The intersection `⋂ ker L_C` is representation-dependent and must be computed before applying the lemma.

This defines a precise **transport-invisible subspace** or `kernel of the action`; do not confuse it with an empirically identified physical quotient without source-native semantics.

## 5. Compact versus continuous spectrum

On `S¹`, `Δ` has discrete eigenvalues `-n²` without finite accumulation, allowing nonconstant entire functions to interpolate the constant value 1 on all nonzero eigenvalues and differ at zero.

Conditional contrast: if on a carrier with continuous Laplacian spectrum a closure theorem independently forces `f(-ξ²)=1` for **all** nonzero real `ξ`, then an entire `f` must be `f≡1` by the identity theorem. The discrete construction cannot be imported into this continuous-spectrum setting.

The preceding sentence is a conditional analytic consequence, **not** a proved complete closure classification on noncompact `R`, nor a claim about Lorentzian `□`.

On the standard flat `2π` torus `T^d`, a simpler entire interpolation `H_d(z)=sin(πz)/(πz)` vanishes on all nonzero Laplace eigenvalues `-|n|²` (which are nonzero integers), so `exp(aH_d(Δ))=I+(e^a-1)P_0` likewise gives classical **scalar** transport; tensor caution continues to apply.

## 6. Exact computational cross-check (not a referee)

Using rational arithmetic, test `μ_0=2, μ_n=1` for all other `n`. The displayed coefficient was evaluated on:

```
n=-7,...,7; k=-5,...,5; l=-5,...,5
15*11*11 = 1815 combinations; exact nonzero residuals: 0.
```

Countercontrol multiplier `μ_0=2`, `μ_{±2}=11/10`, and all remaining `μ_n=1`: for `(n,k,l)=(1,1,0)`, the residual coefficient equals exactly `1/5`.

The tensor witness at `(n,k,l,weight)=(1,1,-1,2)` gives exactly `2`. No stochastic sampling or floating-point threshold is involved. These calculations check the algebra mechanically but do not replace an independent derivation/referee.

## 7. Host relation and negative knowledge

The underlying host is the elementary Fourier/Witt representation of vector fields on `S¹` and spectral multiplier algebra. External background reference: Y. Billig and V. Futorny, *Representations of Lie algebra of vector fields on a torus and chiral de Rham complex* (2011), https://arxiv.org/abs/1108.6092 . This reference supports the host family, **not** a claim that the precise multiplier classification theorem appears there.

* `NO NOVELTY CLAIM`: an external search did not establish whether this exact lemma has been published; absence of a hit is not novelty.
* The operator formula in NC 002 / 005 can remain correct while a universal necessity inference drawn from it is false.
* The original tensor-valued J3 diagnostics and finite-difference outcomes are unaffected by a counterexample on scalar `S¹`.
* `f(Δ)` here is a diagnostic spectral multiplier, not necessarily a causal/physical Lorentzian form factor.
* `NO CANON, NO EXEC_SIGN, NO REV021, TPE HOLD, P2/P3 unchanged`.
* `H8R-C`, Front B admission, and T2 remain separate, unpromoted lanes.

## 8. Safe replacement for the overbroad inference

> In the scalar Fourier/Witt representation on the circle, exact closure of `T_C=L_C f(Δ)` with an entire zero-free `f` forces `f(-n²)=1` on every nonzero Fourier mode, hence `T_C=L_C`. A nonconstant entire `f` may nevertheless differ from the identity on the invisible zero-mode sector. Thus `f²=f` and `[f,L_C]=0` are not individually necessary on the whole state space. Any stronger conclusion for symmetric tensors, noncompact spectra, or Lorentzian operator functions needs independent carrier-specific proof.

**PLACEMENT:** LT4 exact host-local clarification and NC wording-audit candidate only; no unilateral mutation of DRAFT018, NC originals, Paper 1, or programme freeze.
