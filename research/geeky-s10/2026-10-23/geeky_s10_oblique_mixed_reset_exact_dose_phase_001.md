---
artifact_id: GEEKY-S10-OBLIQUE-MIXED-RESET-EXACT-DOSE-PHASE-001
problem_id: P2-WEAK-RESET-RESOURCE-DOSING-002
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
document_type: PUBLIC_SCIENCE_RETURN
exposure: PUBLIC
claim_ceiling: EXACT_2X2_CONDITIONAL_ASYMPTOTIC_THEOREM / SHARP_PHASE_WITNESS / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
canonical_path: research/geeky-s10/2026-10-23/geeky_s10_oblique_mixed_reset_exact_dose_phase_001.md
source_revision: PENDING_COMMIT_AT_CREATION
supersedes: []
---

# Geeky-S10 — Exact oblique mixed-reset dose phase and sharpness of the exponential resource factor

## 0. One problem — one state

**Question.** In the no-common-storage dose theorem,
\[
\sum_j c_j^2
\le
\varepsilon B E^2
e^{2\mu_+T+2DEK}\|v\|^2,
\]
is the exponential dependence on conditional reset dose \(K\) merely a loose product/Grönwall artifact, or can oblique switching genuinely turn logarithmically growing dose into nonvanishing or divergent statistical information?

**Best prior positive result.**
- INT8 ROT006: deterministic oblique ideal-reset records have a total-dose guard and a sharp alternating instability threshold.
- Geeky-S10 dose theorem: mixed/raw conditional sensitivity obeys a general finite-dose upper bound without common \(V_*\).

**Best prior negative/control result.**
- Raw reset \(\kappa=0\): information survival at weak strength requires total dose \(B\asymp\varepsilon^{-1}\).
- Common-storage mixed reset: when global \(V_*\) exists, \(\varepsilon/\kappa\to0\) forces collapse independently of dose.

**Discriminator.**
Use the exact 2×2 oblique family that destroys common storage and calculate the mixed-reset conditional-sensitivity energy exactly.

**Answer.**
The exponential resource factor is real. For a symmetric oblique family \(q>1\), constant mixed-reset fraction \(\kappa=1-\alpha\), per-shot strength \(s\), and total actual dose \(B=2Ms\), a Perron-aligned preparation has
\[
\sum_{j=1}^{2M} c_j^2
\sim
\frac{s}{2(q-1)\kappa}
\left[
e^{(q-1)\kappa B}-1
\right].
\]
For fixed \(\kappa>0\) and \(B=c\log(1/s)\), the sharp threshold is
\[
c_*=\frac{1}{(q-1)\kappa}.
\]
Below \(c_*\) information collapses, at \(c_*\) it remains finite and nonzero, and above \(c_*\) it diverges in the bare mathematical model.

Thus the general dose theorem has the correct exponential **mechanism**, though its coefficient \(DE\) is only a universal norm envelope, not the sharp oblique Lyapunov exponent.

---

## 1. Typed mixed-reset sensitivity family

Take \(G=0\) and two self-attenuating oblique actions with readout directions
\[
e_1=(1,0)^\top,
\qquad
e_2=(0,1)^\top,
\]
and reset vectors
\[
d_1=(1,-q)^\top,
\qquad
d_2=(-q,1)^\top,
\qquad q>1.
\]

Each action satisfies
\[
e_i^\top d_i=1.
\]

Let the actual observation strength be \(s\in(0,1)\). Let a constant fraction
\[
\alpha\in[0,1],
\qquad
\kappa:=1-\alpha
\]
measure the fraction of the ideal signal retained in the conditional parameter-sensitivity reset.

As established in the mixed-reset theorem, after conditioning on the same observed current value, sensitivity evolves with effective reset strength
\[
r:=\kappa s.
\]

Thus
\[
Q_1(r)
=
I-rd_1e_1^\top
=
\begin{pmatrix}
1-r&0\\
qr&1
\end{pmatrix},
\]
\[
Q_2(r)
=
I-rd_2e_2^\top
=
\begin{pmatrix}
1&qr\\
0&1-r
\end{pmatrix}.
\]

One pair has sensitivity map
\[
B_r:=Q_2(r)Q_1(r)
=
\begin{pmatrix}
1-r+q^2r^2&qr\\
qr(1-r)&1-r
\end{pmatrix}.
\tag{1.1}
\]

The actual conditional observation coefficients still use strength \(s\), not \(r\).

---

## 2. Exact Perron multiplier

The trace and determinant are
\[
\operatorname{tr}B_r
=
2(1-r)+q^2r^2,
\]
\[
\det B_r=(1-r)^2.
\]

Hence the two exact eigenvalues are
\[
\lambda_\pm(r)
=
1-r+\frac{q^2r^2}{2}
\pm
\frac{qr}{2}
\sqrt{4-4r+q^2r^2}.
\tag{2.1}
\]

For \(q>1\) and \(r\downarrow0\),
\[
\lambda_+(r)
=
1+(q-1)r
+\frac{q(q-1)}{2}r^2
+O(r^3),
\tag{2.2}
\]
and
\[
\log\lambda_+(r)
=
(q-1)r
+\frac{q-1}{2}r^2
+O(r^3).
\tag{2.3}
\]

Thus the exact first-order oblique growth exponent per conditional-reset dose is
\[
q-1.
\]

This is the sharp local exponent that replaces the generic norm coefficient \(DE\) for this family.

---

## 3. Exact pair-output energy on the Perron mode

Let \(x_m\) be the sensitivity state before action 1 of pair \(m\).

The two observation coefficients in that pair are
\[
c_{2m+1}
=
s\,e_1^\top x_m,
\]
\[
c_{2m+2}
=
s\,e_2^\top Q_1(r)x_m.
\]

Hence pair energy is
\[
c_{2m+1}^2+c_{2m+2}^2
=
s^2 x_m^\top W_r x_m,
\]
where
\[
W_r
=
e_1e_1^\top
+
Q_1(r)^\top e_2e_2^\top Q_1(r)
=
\begin{pmatrix}
1+q^2r^2&qr\\
qr&1
\end{pmatrix}.
\tag{3.1}
\]

Let \(v_r\) be a unit right Perron eigenvector of \(B_r\):
\[
B_rv_r=\lambda_+(r)v_r.
\]

Set
\[
A_r:=v_r^\top W_rv_r.
\]
Since \(v_r\to(1,1)^\top/\sqrt2\) and \(W_r\to I\),
\[
A_r\to1.
\tag{3.2}
\]

Starting from \(x_0=v_r\), after \(M\) pairs the total conditional sensitivity energy is **exactly**
\[
\boxed{
\mathcal E_M(s,\kappa,q)
=
s^2A_r
\frac{\lambda_+(r)^{2M}-1}
{\lambda_+(r)^2-1},
\qquad
r=\kappa s.
}
\tag{3.3}
\]

This is an exact finite-\(s\), finite-\(M\) formula.

---

## 4. Continuous-dose asymptotic

Let total actual strength dose be
\[
B_s:=2Ms.
\tag{4.1}
\]

Allow \(\kappa=\kappa_s>0\) to depend on \(s\), with
\[
r_s=\kappa_s s\to0.
\]

Assume
\[
B_s/s\to\infty
\]
and
\[
B_s\kappa_s^2s\to0.
\tag{4.2}
\]

The second condition ensures that the accumulated \(O(r^2)\) error in \(\log\lambda_+\) is negligible.

Using (2.3),
\[
2M\log\lambda_+(r_s)
=
(q-1)\kappa_sB_s+o(1).
\tag{4.3}
\]

Also
\[
\lambda_+(r_s)^2-1
=
2(q-1)\kappa_ss+o(\kappa_ss).
\tag{4.4}
\]

Therefore
\[
\boxed{
\mathcal E_M
\sim
\frac{s}{2(q-1)\kappa_s}
\left[
\exp\!\big((q-1)\kappa_sB_s\big)-1
\right].
}
\tag{4.5}
\]

This is the sharp dose-growth interpolation for this oblique family.

---

## 5. Three asymptotic regimes

Define
\[
L_s:=(q-1)\kappa_sB_s.
\]

### 5.1 Raw-like regime: \(L_s\to0\)

Then
\[
e^{L_s}-1\sim L_s
\]
and (4.5) becomes
\[
\boxed{
\mathcal E_M
\sim
\frac{sB_s}{2}.
}
\tag{5.1}
\]

This is exactly the raw-reset scaling.

At the endpoint \(\kappa=0\), sensitivity does not reset at all. For the fixed preparation
\[
u_+=(1,1)^\top/\sqrt2,
\]
each pair contributes exactly \(s^2\), so
\[
\mathcal E_M
=
Ms^2
=
\frac{sB_s}{2}.
\tag{5.2}
\]

Thus the \(\kappa\downarrow0\) limit is continuous.

### 5.2 Finite amplification regime: \(L_s\to L\in(0,\infty)\)

Then
\[
\mathcal E_M
\sim
\frac{sB_s}{2}
\frac{e^L-1}{L}.
\tag{5.3}
\]

The raw dose law \(sB/2\) is multiplied by a finite oblique amplification factor.

### 5.3 Exponential amplification regime: \(L_s\to\infty\)

Then
\[
\boxed{
\log\mathcal E_M
=
\log\frac{s}{\kappa_s}
+
(q-1)\kappa_sB_s
-
\log[2(q-1)]
+
o(1).
}
\tag{5.4}
\]

Hence the sharp balance variable is
\[
\boxed{
\Psi_s
:=
(q-1)\kappa_sB_s
-
\log(\kappa_s/s).
}
\tag{5.5}
\]

In this regime:
- \(\Psi_s\to-\infty\): collapse;
- \(\Psi_s\to\psi\in\mathbb R\): finite nonzero energy;
- \(\Psi_s\to+\infty\): divergence.

This is substantially sharper than the universal sufficient condition
\[
sB_se^{2DEK_s}\to0.
\]

---

## 6. Fixed-\(\kappa\) logarithmic-dose phase transition

Let
\[
\kappa\in(0,1]
\]
be fixed and
\[
B_s
=
c\log(1/s)+o(\log(1/s)),
\qquad c>0.
\]

Then (4.5) gives
\[
\mathcal E_M
\sim
\frac{1}{2(q-1)\kappa}
s^{1-c(q-1)\kappa}.
\tag{6.1}
\]

Therefore the exact critical dose coefficient is
\[
\boxed{
c_*
=
\frac{1}{(q-1)\kappa}.
}
\tag{6.2}
\]

So:
- \(c<c_*\): \(\mathcal E_M\to0\);
- \(c=c_*\): \(\mathcal E_M\to[2(q-1)\kappa]^{-1}\);
- \(c>c_*\): \(\mathcal E_M\to\infty\).

For \(\kappa=1\), this reduces exactly to the INT8 ideal-reset threshold
\[
c_*=\frac1{q-1}.
\]

For \(\kappa<1\), injecting more current readout noise weakens conditional-sensitivity damping and moves the instability threshold to larger actual dose by the factor \(1/\kappa\).

---

## 7. Fixed preparation, not only moving Perron vectors

Equation (3.3) uses the exact Perron eigenvector \(v_r\), which depends on \(r\).

The phase boundary does **not** rely on this moving choice.

Let
\[
u_+=(1,1)^\top/\sqrt2
\]
be fixed independently of \(s\).

As \(r\to0\), the right and left Perron eigendirections converge to \(u_+\), while the subdominant eigendirection converges to
\[
u_-=(1,-1)^\top/\sqrt2.
\]

Thus the Perron projection of fixed \(u_+\) tends to one. In the logarithmic-dose regime of section 6,
\[
\left|\frac{\lambda_-(r)}{\lambda_+(r)}\right|^M
\to0.
\]

Therefore fixed \(u_+\) has the same exponent, same critical \(c_*\), and the same leading asymptotic constant as the Perron-aligned family.

So the sharp phase transition is a property of one fixed preparation direction, not an artifact of allowing the target state to vary with \(s\).

---

## 8. Gaussian statistical interpretation

With iid innovation noise
\[
\eta_j\sim N(0,\sigma^2),
\]
the conditional Fisher information for scalar \(\theta\) is
\[
I_M
=
\frac{\mathcal E_M}{\sigma^2}.
\tag{8.1}
\]

Hence for fixed \(\kappa>0\) and
\[
B_s=c\log(1/s),
\]
\[
I_M
\sim
\frac{1}{2(q-1)\kappa\sigma^2}
s^{1-c(q-1)\kappa}.
\tag{8.2}
\]

Therefore:
- below \(c_*\), the full Gaussian experiment collapses to no-information;
- at \(c_*\), a nonzero finite Fisher-information scale survives;
- above \(c_*\), Fisher information diverges in the bare model.

This is a mathematical information phase transition. It is not a physical sensor claim.

---

## 9. Relation to the general dose theorem

The general theorem gave
\[
\sum c_j^2
\le
sB E^2e^{2DEK}\|v\|^2,
\]
with
\[
K=\kappa B
\]
for constant \(\kappa\).

For the present family,
\[
E=1,
\qquad
D=\sqrt{1+q^2}.
\]

The universal upper bound therefore grows with exponent proportional to
\[
2DE\kappa B
=
2\sqrt{1+q^2}\,\kappa B.
\]

The exact Perron exponent in the squared sensitivity energy is instead
\[
(q-1)\kappa B.
\]

Thus:

**PASS mechanism:** exponential dependence on conditional-reset dose is genuinely necessary without common storage.

**REPAIR constant:** the generic norm envelope is not sharp; the correct coefficient is the top Lyapunov/Perron growth rate of the realized switching geometry.

This is the correct placement relative to mature switched-system theory.

---

## 10. Relation to common storage

For this \(q>1\) alternating oblique family, the ideal deterministic action family does not possess a finite all-protocol common storage on the growing Perron direction.

The present theorem shows exactly what replaces the missing storage:
- a finite dose can still enforce collapse;
- logarithmically growing dose can reach a critical information phase;
- larger dose can amplify information.

Therefore:

\[
\text{NO COMMON }V_*
\neq
\text{IMMEDIATE NONCOLLAPSE}.
\]

The relevant question is the joint scaling of:
\[
s,\quad
B,\quad
\kappa,\quad
\text{and switching growth rate}.
\]

---

## 11. Prior-art subtraction / host

The mathematical ingredients are mature:
- Perron–Frobenius theory for positive matrices;
- exact 2×2 eigenvalue analysis;
- products of near-identity matrices;
- continuous-time / impulsive switching asymptotics;
- Lyapunov exponent / joint spectral growth;
- Gaussian Fisher information.

No novelty claim is made for these hosts.

The project-local contribution is the typed placement across the already separated carriers:
- actual measurement strength \(s\);
- current-noise mixing fraction \(\alpha\);
- conditional reset strength \(r=\kappa s\);
- total actual dose \(B\);
- conditional dose \(K=\kappa B\);
- statistical information versus deterministic reset energy.

---

## 12. Firewalls

GENERIC GRÖNWALL EXPONENT
!=
SHARP SWITCHING EXPONENT.

EXPONENTIAL DOSE DEPENDENCE
!=
PROOF OF PHYSICAL INSTABILITY.

NO COMMON STORAGE
!=
AUTOMATIC INFORMATION SURVIVAL.

FINITE PHYSICAL TIME
!=
FINITE TOTAL DOSE.

FIXED SELF-ATTENUATING ACTIONS
!=
COMMON DISSIPATIVITY.

RAW LIMIT \(\kappa=0\)
!=
DISCONTINUOUS SPECIAL CASE;
it is the \(L_s\to0\) limit of the mixed phase law.

FISHER DIVERGENCE IN BARE MODEL
!=
SOURCE-LEGAL UNLIMITED INFORMATION.

CLASSICAL MIXED RESET
!=
QUANTUM INSTRUMENT.

---

## 13. Disposition / STOP criterion

**EXACT finite-pair formula:** PASS.

**Sharp asymptotic law:**
\[
\mathcal E_M
\sim
\frac{s}{2(q-1)\kappa}
\left[e^{(q-1)\kappa B}-1\right].
\]

**Fixed-\(\kappa\) critical logarithmic dose:**
\[
B_*(s)
\sim
\frac{\log(1/s)}{(q-1)\kappa}.
\]

**Interpretation:**
the exponential factor in the general no-storage dose theorem is structurally real, while its universal norm coefficient is conservative.

**STOP this abstract seam** unless a future result supplies at least one of:
1. a source-admitted physical relation among \(s,B,\kappa,T\);
2. a genuinely different switching geometry with a new sharp phase;
3. a quantum/CPTP instrument whose legal information-disturbance law changes the carrier;
4. an independent referee correction to the exact algebra above.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
