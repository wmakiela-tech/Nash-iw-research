# LT4 ROT03 — Tensor-density weight classification of Fourier-multiplier Lie-transport closure

**RETURN_ID:** `IW_LT4_ROT03_TENSOR_DENSITY_WEIGHT_CLASSIFICATION_AND_DE_RHAM_EXCEPTION_001_20261012`  
**FROM:** `IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_02 / LT4`  
**DATE:** 2026-10-12  
**STATUS:** bounded, exact mathematical derivation; computational sanity checks; independent referee not yet obtained.  
**CLAIM CEILING:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_REV021 / NO_TPE_PROMOTION / NO_PHYSICAL_INFERENCE`.

## 0. Currentness and relation to ROT01/ROT02

This is a follow-on to:
- ROT01: `research/LT4/IW_LT4_ROT01_CURRENTNESS_AND_J3_ENTIRE_FORM_FACTOR_NULL_SECTOR_COUNTEREXAMPLE_001_20261012.md`;
- ROT02: `research/LT4/IW_LT4_ROT02_WITT_MULTIPLIER_CLOSURE_CLASSIFICATION_AND_TENSOR_BOUNDARY_001_20261012.md`.

Current LT programme placement remains `DRAFT018 / REV020_PLUS_COMPILER / P2`; `P3` remains a live fallback; `TPE=HOLD`, `T2=NOT_RUN`, `REV021=NOT_CREATED`. H8R-C remains source-interface unresolved; Front B source-admission and physical target endpoints remain withheld. The NC J3 consolidation card `005` (Drive `10qiBj80I7MRRcGlE4k12WljxOvFMwPed`) is unrefereed. No canonical scientific edit is made.

**Question:** Is the exceptional zero-mode multiplier `F=I+(c-1)P0` in scalar ROT02 a general property of tensor Lie transport, or a feature of the carrier's representation weight?

## 1. Explicit host and theorem

Let `A=span_C{u_n=e^{inx} : n in Z}` be the Laurent/trigonometric-polynomial carrier on `S¹`. For arbitrary complex tensor-density weight `λ`, write

```
L_C^(λ) u = C u' + λ C' u,
C_k = e^{ikx} ∂_x,
L_k^(λ)u_n = i(n+λ k)u_(n+k).
```

These `L_k` realize the Witt Lie algebra of polynomial vector fields. Fix a **Fourier-diagonal, algebraically invertible** operator `F` with

```
F u_n=μ_n u_n,  μ_n != 0  for all n in Z,
T_k=L_k^(λ)F.
```

"Algebraically invertible" on `A` is equivalent to all the `μ_n` being nonzero; neither a Banach-space bounded inverse nor any functional-calculus theorem is assumed.

**THEOREM.** The identity

```
[T_k,T_l]=T_[C_k,C_l]   on all u_n, for every n,k,l in Z
```

holds iff one of the following conditions holds:

1. `λ=0`: `μ_n=1` for every `n != 0`, with `μ_0=c != 0` arbitrary. Then `T_C=L_C^(0)` for every `C`.
2. `λ=1`: `μ_n=1` for every `n != 0`, with `μ_0=c != 0` arbitrary. Then `T_C=F^{-1}L_C^(1)F`; the new action is equivalent to the standard representation.
3. `λ not in {0,1}`: `μ_n=1` for every integer `n`, i.e. `F=I`.

At `λ=0` or `λ=1`, `c=1` overlaps the identity case. For `c!=1` the operator `F` differs from identity; for `λ=0` its action is invisible, while for `λ=1` its transport action is nonidentical but conjugate.

### Exact Fourier computation

By the Witt bracket `[C_k,C_l]=i(l-k)C_(k+l)`, the coefficient of `u_(n+k+l)` in `J=[T_k,T_l]-T_[C_k,C_l]` equals

```
D_λ(n;k,l)
= μ_n * { (n+λ k)(n+k+λ l) μ_(n+k)
        - (n+λ l)(n+l+λ k) μ_(n+l)
        - (k-l)(n+λ(k+l)) }.
```

When `μ_n=1` this expression vanishes identically because `L^(λ)` is a representation.

Set `l=0`. A useful **exact factorization** is

```
D_λ(n;k,0) = μ_n (n+λ k) [
      (n+k)(μ_(n+k)-1) - n(μ_n-1)
   ].
```

**Case λ != 0:** take `n=0`, `k=m != 0`. Because `μ_0!=0`, this forces `m(μ_m-1)=0`, hence `μ_m=1` for all `m!=0`.

**Case λ=0:** take `n=1`, `k=-1`; the factorization reduces to `μ_1(1-μ_1)=0`, hence `μ_1=1`. With `n=1`, `k=m-1`, we obtain `m(μ_m-1)=0` for all `m`, hence `μ_m=1` for `m!=0`.

Now `μ_n=1` for every nonzero mode. Choose `(n,k,l)=(1,-1,1)`. The full residual equals

```
D_λ(1;-1,1) = λ(1-λ)(μ_0-1).
```

So for `λ not in {0,1}`, `μ_0=1` as well. This proves necessity.

For sufficiency:
- If `λ=0`, `L_C^(0) P_0=0`; thus `L_C^(0)F=L_C^(0)`.
- If `λ=1`, `L_C^(1)u=(Cu)'`, so `P_0 L_C^(1)=0`; consequently `F L_C^(1)=L_C^(1)`, and because `F` is invertible, `L_C^(1)F=F^{-1} L_C^(1)F`. Conjugation preserves the Lie bracket.
- In the remaining case `F=I`.

QED.

## 2. Interpretation: two different zero-mode mechanisms

`λ=0`: **invisible output** — `P_0` lands in `∩_C ker L_C^(0)`; multiplying constants changes `F` but not any `L_CF`.

`λ=1`: **invisible intermediate input** — the image of every Lie derivative is an exact one-form of zero average, hence `P_0 Ran(L_C^(1))=0`. The modified `T=L F` is not equal to `L` when `c!=1`, but is `F^{-1}LF`, so no genuinely inequivalent Lie representation is obtained.

`λ=2`: covariant rank-two tensors in one dimension have `λ=2`; no nonidentity invertible Fourier multiplier `F` preserves exact closure. This specializes ROT02's tensor witness to a complete theorem **on this 1D carrier**.

These patterns are compatible with the familiar 0-form/1-form de Rham structure. They should not be labeled new cohomology, BRST, or higher brackets.

## 3. Universal exact defect identity and necessary-condition repair

For any representation `C -> L_C` on a common invariant domain, and any linear operator `F` such that compositions are well-defined, define `T_C=L_CF`. Since `[L_C,L_D]=L_[C,D]`,

```
J_F(C,D)
= [L_C F, L_D F] - L_[C,D] F
= L_C(F-I)L_D F - L_D(F-I)L_C F.      (*)
```

Proof: insert `F=I+(F-I)` at the **middle** occurrence in each double product. The remainder is `([L_C,L_D]-L_[C,D])F=0`.

This identity is shorter than the equivalent commutator-plus-`F²-F` expression in NC 002/005. It shows immediately why the vanishing of `J` does **not** require the two pieces of an expanded expression to vanish independently: cancellations and annihilated sectors are permitted.

A sufficient, **not necessary**, representation-level criterion is

```
(F-I)(sum_C Ran(L_C)) ⊆ intersection_C ker(L_C).
```

Then each term on the right of `(*)` vanishes. This covers:
- `λ=0`: `F-I` takes values in constants, annihilated by `L_C`;
- `λ=1`: the `L_C` images have zero average, so `F-I` annihilates these images.

The condition is not automatically a complete characterization on arbitrary representations; the theorem above establishes completeness only in the declared Fourier/Witt density family.

## 4. Consequences for entire zero-free form factors

Suppose `F=f(Δ)` with `Δ=∂_x²`, and `f` entire and zero-free. Then `μ_n=f(-n²) ≠0`, so the theorem applies.

At `λ=0,1`, `f(-n²)=1` for nonzero `n`, while `f(0)` may differ; nonconstant entire zero-free `f` realizing this includes

```
H(z)=sinh(π√z)/(π√z),
f_a(z)=exp(a H(z)), a != 0,
f_a(Δ)= I+(e^a-1)P_0.
```

At `λ!=0,1`, including weight two, `f(-n²)=1` **for every** `n`, so `f(Δ)=I` on the carrier. This does **not** force `f(z)≡1` as an analytic function on the complex plane: the discrete set `{-n²}` has no finite accumulation. For example, `f(z)=exp(a sin(πz))` is nonconstant, entire, zero-free and equals 1 at all Laplace eigenvalues. Distinguish:

```
ENTIRE FUNCTION IDENTITY != SPECTRAL OPERATOR IDENTITY != TRANSPORT ACTION IDENTITY != REPRESENTATION EQUIVALENCE.
```

The theorem classifies operator actions, not abstract analytic symbols away from the carrier spectrum.

## 5. Exact tests already executed by LT4 in this turn

The full coefficient `D_λ(n;k,l)` was evaluated with Python exact rational arithmetic for
`n,k,l in {-6,...,6}`: **2197 triples per weight**. Test multiplier:
`μ_0=2, μ_n=1 (n!=0)`.

| λ | tuples | nonzero defects | maximum absolute coefficient |
|---|---:|---:|---:|
| 0 | 2197 | 0 | 0 |
| 1 | 2197 | 0 | 0 |
| 2 | 2197 | 264 | 72 |
| 1/2 | 2197 | 264 | 9 |
| -1 | 2197 | 264 | 72 |

Perturbed control `μ_2=11/10` gives nonzero defects also for the exceptional weights:
`λ=0` and `λ=1` each have a witness `(n,k,l)=(-1,-3,3)`, coefficient `1/5`.

Independently of Fourier symbols, a generic 3×3 integer-matrix substitution tested the universal identity `(*)` in exact arithmetic, with nonzero `J`. The computed matrix on each side was
```
[[ 5, -9, 7],
 [-5, -3, 8],
 [ 2,  9, 1]]
```
The check establishes no mathematical novelty and is not a substitute for human or external-model referee review.

## 6. Host subtraction and external literature

The tensor-density/Witt action itself is a standard host, not a project discovery:
- L. Buzaglo and G. S. Vishwa (2025), *Central Extensions, Derivations, and Automorphisms of Semi-Direct Sums of the Witt Algebra with its Intermediate Series Modules*, Journal of Lie Theory 35, 455–506, DOI `10.5802/jolt.1393`. https://jolt.centre-mersenne.org/articles/10.5802/jolt.1393/
- *1-Cocycles of the Witt algebra with coefficients in tensor product of modules*, Journal of Algebra (2024), explicit action `L_m v_n=-(αm+n)v_(m+n)` in accessible preliminaries: https://www.sciencedirect.com/science/article/abs/pii/S0021869324003260
- Billig and Futorny (2011), *Representations of the Lie algebra of vector fields on a torus and the chiral de Rham complex*, https://arxiv.org/abs/1108.6092 .

These references establish the **host vocabulary and representation model**, not an externally verified priority claim for the specific Fourier-multiplier classification stated here. No originality claim is made absent a proper source-native prior-art comparison.

## 7. Placement and STOP guards

**Admissible project placement:** source-local algebraic clarification and claim-repair candidate for NC 002/005, subject to independent referee on sign conventions, invertibility scope, extension from polynomial to smooth spaces, and tensor-carrier mismatch.

**NOT demonstrated:** a tensor-valued 3D/4D gravity transport closure theorem; a physically admissible entire kinetic form factor; a Lorentzian spectral-domain statement; a gauge symmetry, `L∞` bracket, `l3`, physical J3 invariant, or novelty/surplus.

**Current LT programme is unchanged:** `DRAFT018` active, `REV021` absent, `TPE HOLD`, `P2/P3` unchanged, `H8R-C` open, Front B source-validity open, `T2 NOT RUN`, no `EXEC_SIGN`.

**END / ROT03 RETURN.**
