---
artifact_id: GEEKY-S11-ROT001-FIXED-SMOOTH-TT-LEAKAGE-SOBOLEV-NONDECAY-COROLLARY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-23
problem_id: P3_DTC0A_TT_FIXED_SMOOTH_INPUT_LEAKAGE_AND_SOBOLEV_NORM_CEILING_001
class: EXACT_COROLLARY_OF_INT8_ROT016_WITH_NEW_FIXED_SMOOTH_QUANTIFIER_AND_SOURCE_HELPER_CHECK
exposure: PUBLIC
status: MATHEMATICAL_COROLLARY_VERIFIED / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_FIXED_PROJECTOR_FOURIER_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT001 — Fixed-smooth TT leakage persists as mesh spacing vanishes

## 0. Scientific question and currentness subtraction

**Question.** INT8 ROT016 proved a uniform L² full-band lower bound for the source-matched operator `Q Lie_C E_alpha P` using high-frequency TT inputs `H_{q_N}` whose frequency grows with N. Its interpretation carefully said that this *high-band witness* does not, by itself, refute convergence for a **single fixed smooth input** or under Sobolev restrictions. Can that possibility actually hold for the **same source-typed operator**, if we use a fixed low-frequency input instead?

**Answer:** No, in general. The *already published* INT8 ROT016 Theorem 016.1, eq. (2.3), was proved for every fixed resolved integer q, not just `q_N`. Setting **q=1 independently of N** yields an exact positive continuum limit of the TT leakage, even for a single smooth TT tensor and smooth fixed C. Consequently, generic decay to zero of `Q Lie_C E_alpha P` in `H^s -> L²` operator norm cannot follow from finite fixed Sobolev regularity of the source alone.

This is **not a novel independent theorem**: it is a decision-relevant **corollary and quantifier strengthening** of INT8's prior exact formula. INT8 retains priority for that formula, the source-stencil derivation, and high-frequency bound. XH-S4 retains first-order moving-York-projector naturality and ROT021 independently computed metric York projections. Geeky-S10 retains its P/Q block decomposition. INT8 ROT014 already gave a separate low-band finite-Fourier fixed-P two-generator projected-Lie nonclosure witness. The present note only fills the specified *one-generator, fixed-input, source-stencil, Sobolev-decay claim-map gap*.

Prior source: https://github.com/wmakiela-tech/Nash-iw-research/blob/d645a43ad0f2d5e4b34b40ef041786f57f9a8c3f/research/int8/2026-10-23/iw_int8_rot016_source_typed_tt_high_frequency_commutator_nondecay_001.md

Mature host: standard periodic Fourier TT/Leray-type projection and invariant-subspace geometry; the abstract observation that a generic variable vector-field transport does not preserve a fixed flat TT subspace is mature, not an NASH discovery. For vector Leray multipliers and Sobolev projections on periodic domains, cf. https://link.springer.com/article/10.1007/s10884-021-09944-w (not a tensor-TT theorem or an endorsement of a NASH physical model).

## 1. Source-typed domain

On the full periodic odd-N grid `T_N^3`, `N >= 7` odd, grid spacing `h=2π/N` and normalized full-grid Frobenius RMS norm, fix independently of N the smooth trigonometric fields

\[
 C(x,y,z)=(\sin x,0,0),\qquad
 H(x,y,z)=\operatorname{diag}(1,-1,0)\cos z.
\]

Let `P=P_TT` be the raw-wavevector Fourier TT orthogonal projector with the retained source's traceless-zero-mode convention, `Q=I-P`, and

\[
 D_{j,h}f(x)=\frac{f(x+h e_j)-f(x-h e_j)}{2h},\quad
 E_{\alpha,h}=I+\alpha h^2\Delta_h,
\]

where `Delta_h` is the componentwise sum of centered second differences. The retained covariant-tensor component formula for `Lie_C` is

\[
(\mathcal L_{C,h} F)_{ij}= C^mD_{m,h}F_{ij}+F_{mj}D_{i,h}C^m+F_{im}D_{j,h}C^m.
\]

For every such N, `P H=H` and `||H||_2=1`. The fields themselves do not vary with N; merely their samples do. `C` is source-admissible as an analytic test field but is **not** the archived historical C1/C2. `H` is **not** the historical pure-trace archived h=fI.

## 2. Exact fixed-input computation

Write `sigma_h=sin(h)/h` and `e_{alpha,h}=1-4alpha sin²(h/2)`. Since `H` depends only on z and `C` points along x, `C·D_h H=0`. The sole nonzero strain derivative is `D_{x,h}C^x=sigma_h cos x`. Therefore

\[
 E_{\alpha,h}H=e_{\alpha,h}H,
\qquad
 \mathcal L_{C,h}E_{\alpha,h}H
 =2\sigma_h e_{\alpha,h}\cos x\cos z\ e_xe_x^T.
\]

The outgoing Fourier modes are `(±1,0,±1)`. If `F=e_xe_x^T`, the projected part at any outgoing k satisfies

\[
\|\Pi_kF\|_F^2
=\tfrac12\Bigl(\frac{k_z^2}{k_x^2+k_z^2}\Bigr)^2=\tfrac18,
\quad \|Q_kF\|_F^2=\tfrac78.
\]

Parseval hence gives **an exact identity, for EVERY odd N >= 7**:

\[
\boxed{
\frac{\|Q\mathcal L_{C,h}E_{\alpha,h}PH\|_2}{\|H\|_2}
=\left|\frac{\sin h}{h}\right|
\left|1-4\alpha\sin^2\frac h2\right|
\sqrt{\frac78}.}
\tag{S11.1}
\]

This is precisely INT8 ROT016 (2.3) specialized to **fixed q=1**, not a new independent operator identity. The same test also gives the exact full-input commutator relation

\[
 [P,\mathcal L_{C,h}E_{\alpha,h}]P H
 =-Q\mathcal L_{C,h}E_{\alpha,h}P H.
\]

For any fixed alpha, since `sigma_h -> 1` and `e_{alpha,h} -> 1`, it follows that

\[
\boxed{
\lim_{N\to\infty\atop N\ \mathrm{odd}}
\frac{\|Q\mathcal L_{C,h}E_{\alpha,h}PH\|_2}{\|H\|_2}
=\sqrt{7/8}=0.9354143466934853\ldots >0.}
\tag{S11.2}
\]

For alpha=0.05 and all odd N>=7, monotonicity of `sin h/h` and `1-0.2 sin²(h/2)` as h decreases on this interval gives the explicit **uniform fixed-input** lower bound equal to its N=7 value:

\[
\|Q\mathcal L_{C,h}E_{0.05,h}P\|_{L^2\to L^2}
\ \ge\ 0.7840936613773702\ldots .\tag{S11.3}
\]

The point is not sharpness of the full operator norm: (S11.3) is attained only on the test H at N=7, and lower bounds the full operator norm.

## 3. The Sobolev inference (finite regularity alone is not enough)

Use standard periodic inhomogeneous Fourier Sobolev norms with weights `(1+|k|²)^{s/2}` on the grid, so the fixed H supported at `k=(0,0,±1)` has

\[
\|H\|_{H^s}=2^{s/2}\|H\|_{L^2}\quad(s\ge0).
\]

For **every fixed finite s >= 0**, the same fixed test therefore proves

\[
\boxed{
\liminf_{N\to\infty\atop N\ \mathrm{odd}}
\|Q\mathcal L_{C,h}E_{\alpha,h}P\|_{H^s\to L^2}
\ge 2^{-s/2}\sqrt{7/8}>0.}
\tag{S11.4}
\]

No assumption of a uniform upper norm bound is needed to obtain this lower bound. Therefore **generic vanishing-to-zero of this fixed-flat-P commutator cannot be justified by a positive finite Sobolev regularity exponent alone**. The result does not preclude a non-vanishing bounded upper commutator estimate `O(||∇C||)`, convergence of the discrete commutator to a **nonzero** continuum commutator, special Killing/TT-preserving transport classes, moving metric-dependent `P_g`, or an estimate of the *difference* between discrete and continuum commutators. Such objects are different targets and must be typed independently.

Crucially, even with alpha=0 this fixed-P leakage persists. Thus (S11.2) is a **mature geometric fixed-projector non-invariance**, not evidence for the physical action of a nonlocal E operator and not a continuum gravity/J3/K anomaly.

## 4. Independent numerical verification / retained source check

A standalone NumPy reproducer independently Fourier-projects the exact output on odd N=7,9,17,31 with alpha in {0,0.05,0.2} (12 rows). An additional optional direct import of the **retained helper** runs its actual `apply_E`, `lie_derivative_tensor`, `apply_P_TT` functions at N=9,17,31 and alpha=0.05. Input source SHA256:

`23b0ec865263c5688682425af9d4c1f9d582a0f2f33d99c642c176f801`

This helper is `deepseek_python_20260627_a87249.py`; it is **not** byte-identical to the unavailable historical declared `dtc0a_runtime_v0_3_1.py` SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`.

| N | exact alpha=.05 ratio | independent Fourier | direct retained helper |
|---:|---:|---:|---:|
| 7 | 0.7840936613773702 | 0.7840936613773702 | not run |
| 9 | 0.8411101245710378 | 0.8411101245710378 | 0.8411101245710381 |
| 17 | 0.9080887089344173 | 0.9080887089344173 | 0.9080887089344173 |
| 31 | 0.9271212161329490 | 0.9271212161329491 | 0.9271212161329492 |

Maximum gap across all 12 independent Fourier comparisons: `1.11e-16`; maximum retained helper ratio gap: `2.22e-16`. TT-input projector discrepancy ≤`3.42e-16`. No historical byte-exact production executor confirmation claimed.

Reproducer (standalone by default, optional source import):
`research/geeky-s11/2026-10-23/geeky_s11_rot001_fixed_smooth_tt_leakage_reproduce.py`

Output JSON obtained from execution:
`research/geeky-s11/2026-10-23/geeky_s11_rot001_fixed_smooth_tt_leakage_results.json`

## 5. Decision-changing claim-map patch / stop

- **Earlier high-mode caveat:** the *high-mode q_N witness itself* does not test a fixed smooth H. **CORRECT**, preserve it.
- **But a broader reading that generic fixed-smooth TT leakage might vanish as N→∞ in the same declared source operator:** **FAIL_EXACT** by specializing the prior q-general formula to q=1.
- **Generic `H^s -> L²` vanishing solely from any fixed finite Sobolev exponent s:** **FAIL_EXACT** in this host.
- **Non-vanishing upper estimate, symbol-specific remainder, discrete-to-continuum commutator convergence:** still valid DIFFERENT questions. Owner need required before doing them.
- **Moving York projector physical/geometric compensation:** separate XH-S4 owner programme, not contradicted here.

`NO_NEW_TASK`. `NO_OWNER_ADOPTION_INFERRED`. `NO_BW_INGESTION_INFERRED`.
`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_J3K_INVARIANT`.