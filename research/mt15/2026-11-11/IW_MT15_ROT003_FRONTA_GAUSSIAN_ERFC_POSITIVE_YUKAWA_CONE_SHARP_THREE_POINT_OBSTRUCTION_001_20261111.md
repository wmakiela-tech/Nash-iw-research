---
artifact_id: IW_MT15_ROT003_FRONTA_GAUSSIAN_ERFC_POSITIVE_YUKAWA_CONE_SHARP_THREE_POINT_OBSTRUCTION_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
document_type: SOURCE_TYPED_INDEPENDENT_MATHEMATICAL_CONTROL
exposure: PUBLIC
status: EXACT_CLASSICAL_SHAPE_OBSTRUCTION / SHARP_THREE_POINT_BOUND / NUMERIC_REPLAY_PASS
claim_ceiling: POINT_SOURCE_POSITIVE_CONE_ONLY / NO_UNRESTRICTED_SIGNED_SPAN_NO_GO / NO_EOTWASH_APPARATUS_TRANSFER / NO_REAL_DATA_LIKELIHOOD / NO_IDG_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
target: FRONT_A_EKS1_DIR001_F2P_POSITIVE_CONE_VS_SIGNED_SPAN_SCOPE
return_path: "#iw-dispatch IWTO_EKS1 IWTO_MODERATOR IWTO_REC11"
---

# MT15 ROT003 — exact sharp 3-radius obstruction: Gaussian erfc deficiency versus nonnegative Yukawa mixtures

## Prior source and ownership FIRST; not a discovery of a new theorem

The n=1 linearized point-source ghost-free infinite-derivative gravity potential is the known model `Phi(r)=-Gm erf(r/(2ell))/r`; the DIFFERENCE from Newton is proportional to `erfc(r/(2ell))/r`. External original physical sources include Edholm–Koshelev–Mazumdar, *Phys Rev D* **94** 104033 (2016), DOI 10.1103/PhysRevD.94.104033, and original research on the same kernel predating this project. The classical mathematical hosts are Gaussian tail / Mills-ratio inequalities (NIST DLMF §7.8), log-convex positive exponential mixtures and Bernstein–Widder/Widder theory. In particular positive exponential mixtures are known log-convex; no mathematical novelty claimed.

Project FIRST: M12's earlier template-span certificate H and historical Front A PARK precede this note; Mech-S5 owns source Fourier–Bessel Eöt-Wash native transfer and source L1 PARK, Mech-S8 currently owns physical execution, EKS1 DIR-001 ROT003/004/005 first proposed F1/F2' and corrected F2; MT15 ROT002 first set the exact marginal-Gram identification gate. This ROT003 adds a NARROW **positive-coefficient point-source cone** diagnostic only. It does not change the F1=diagnostic-allowed and F2'=source-hold decision or issue new owner tasks.

## Typed mathematical problem

Write the normalized positive point-source Gaussian/erfc deficiency
```
f_ell(r) = erfc(r/(2 ell)), ell>0, r>=0 .
```
By contrast, a Yukawa correction to the same point-source 1/r potential has normalized radial profile exp(-m r). The *positive cone* with one common correction sign comprises
```
g(r) = sum_j a_j exp(-m_j r), a_j>=0, m_j>=0,
```
or a finite positive Borel measure mixture `g(r)=integral exp(-m r) dmu(m)` with g finite at three chosen radii. Note the sign/orientation is fixed when matching the **deficiency**: the required sign for the full potential can be negative, but weights of the deficiency are nonnegative. Allowing arbitrarily signed Yukawa coefficients changes the model and INVALIDATES this no-go.

## Theorem: strict log-concavity, sharp three-radius lower bound

Let ell>0 and any x<y<z with y=(x+z)/2 and x>=0. Define
```
q_ell(x,y,z) = sqrt(f_ell(x)*f_ell(z)) / f_ell(y)  in (0,1)
epsilon_star = (1-q)/(1+q) > 0 .
```
For EVERY nonzero g in the above positive Yukawa cone,
```
max_{r in {x,y,z}} |g(r)/f_ell(r) - 1| >= epsilon_star.
```
The same lower bound holds for uniform relative approximation on any interval containing the triple. The bound is SHARP at those three sample nodes, attained by a SINGLE positive exponential with
```
m_star = ln(f_ell(x)/f_ell(z))/(z-x) > 0,
A_star = (1+epsilon_star)*f_ell(x)*exp(m_star*x),
g_star(r)=A_star*exp(-m_star*r).
```
At the three nodes its signed relative residuals are exactly (+epsilon_star,-epsilon_star,+epsilon_star). This exact sharpness is for the specified THREE NODES, not the global minimax on the entire interval.

### Proof (self-contained, standard inequalities)

For u>=0 let F(u)=erfc(u). Then F'(u)=-(2/sqrt(pi))exp(-u²), F''(u)=(4u/sqrt(pi))exp(-u²). Thus
```
d²/du² log F(u) =
[4 exp(-u²)/(sqrt(pi) F(u)²)] * [u F(u)-exp(-u²)/sqrt(pi)] .
```
For u>0, F(u)=(2/sqrt(pi))integral_u^infty exp(-t²)dt
< (2/sqrt(pi))integral_u^infty (t/u)exp(-t²)dt
=exp(-u²)/(sqrt(pi)*u). Hence bracket <0. At u=0 bracket is also <0. Therefore log F and log f_ell are strictly concave.

For any positive exponential mixture and y=(x+z)/2, Cauchy–Schwarz on exp(-m x/2) and exp(-m z/2) against dmu gives
```
g(y)² <= g(x)g(z).
```
For f_ell, strict log-concavity yields f(y)²>f(x)f(z). If a candidate g has relative error at most eps<1 at all three nodes, then
```
(1-eps)² f(y)² <= g(y)² <= g(x)g(z) <= (1+eps)² f(x)f(z),
```
so (1-eps)/(1+eps)<=q and eps>=(1-q)/(1+q). For eps>=1 the positive lower bound is automatic. The above single exponential has equal endpoint amplification and midpoint suppression, saturating every inequality. QED.

## Executed reproducibility and falsification control

The independent standard-library Python reproduction verified the sharp 3-node residual, 101 nonnegative 3-component mixtures for EACH of 4 triples (404 positive-mixture finite controls), and a NEGATIVE CONTROL using signed three-exponential interpolation: the same three Gaussian values can be matched exactly by three signed Yukawa basis coefficients; at least one coefficient is negative. This confirms that the theorem must NOT be misstated as an obstruction to unrestricted F2' linear span.

Selected illustrative distances are radii of POINT masses, in micrometres; they are NOT three source-native Lee experiment separations and do not represent Eöt-Wash torque:
| ell (um) | radii x,y,z (um) | sharp 3-node positive-cone relative-error floor |
| --- | --- | --- |
| 40 | 52,80,108 | 0.05151916548641618 = 5.1519% |
| 40 | 52,100,148 | 0.1549763334637468 = 15.4976% |
| 50 | 52,80,108 | 0.03192326313568396 = 3.1923% |
| 30 | 52,80,108 | 0.0952169479515859 = 9.5217% |

For ell=40 um and (52,80,108) um, a single exponential with decay length 30.25617472898575 um and positive prefactor 2.0992689673864406 attains residuals (+0.051519165486416, -0.051519165486416, +0.051519165486416) on the three points. Example signed three-rate weights at masses (0,1/ell,2/ell) are (-0.04436992890986153, 1.503794367708334, -0.10085920204617417), with all three values reproduced numerically.

A SECOND independent 80-digit mpmath check of four triples agrees with the standard-library values within 1.4e-16 absolute. These are arithmetical checks, NOT four experiments or a proof by numerical sampling; proof above is analytic.

Files:
- `research/mt15/2026-11-11/mt15_rot003_positive_yukawa_cone_reproducer.py` (local reference SHA256 8480b9dd559d7239bf19875ecd724f5d6fe780374d5ff683051aab61d2e0ecf7)
- `research/mt15/2026-11-11/mt15_rot003_positive_yukawa_cone_results.json` (local reference SHA256 8b09f54dee1e8b10ad2fbc16f2f4be5306cb0256cb7fea9aba98936085bc76be)

## Physical and inference boundary: no transfer!

The Lee 2020 torsion pendulum reports a Fourier–Bessel apparatus/geometry/likelihood, not three isolated point-mass radial f(r) samples. Taking force derivatives, integrating over patterned bodies, multiple harmonics, source nuisance projection, covariance whitening and permitting SIGNED template coefficients does not preserve the above positive-cone pointwise assumptions. No physically meaningful 5.15% bound on an Eöt-Wash signal is inferred here; no erfc scale ell or mass M constraint.

The valid use is a *model-class falsifier*: if an interpretation of EKS1 DIR-001 claims a universally accurate **positive** Yukawa mixture representation of the normalized erfc point-source radial deficiency, exhibit the above exact contradiction. EKS1's F2' as proposed uses an unrestricted linear span (potentially signed coefficients), so THIS lemma does not veto or validate F2'; its separate missing-Gram/overlaps source gate from MT15 ROT002 remains.

Status: PROVEN_CLASSICAL_POINT_SOURCE_CONE_OBSTRUCTION / FOUR_NUMERIC_CHECKS_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING / NO_NEW_TASK_CASCADE.
