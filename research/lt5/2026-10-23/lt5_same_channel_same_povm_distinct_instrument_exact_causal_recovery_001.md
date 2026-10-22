# LT5 / obrót 7 — Same POVM and same CPTP marginal, different instruments and exact causal recoverability

- **Date:** 2026-10-23 (Europe/Warsaw)
- **Cell:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
- **Artifact ID:** LT5-SAME-POVM-SAME-CHANNEL-DIFFERENT-INSTRUMENT-001_20261023
- **Result type:** exact finite-dimensional quantum-instrument counterexample / diamond norm / causal correction
- **Source status:** PUBLIC_SAFE; independent matrix checks; host-absorbed mathematics, not novel
- **Claim ceiling:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_SIGNAL / NO_NEW_MODEL_EQUIVALENCE
- **Reviews:** independent referee for THIS theorem pending; REC10 prior comments apply only to their specified earlier LT5 notes
- **Living monograph:** no mutation pending theorem-specific referee/editorial adoption; §5.4–5.6 is candidate insertion site
- **BW:** separate ingestion NOT VERIFIED

## Scientific question and what earlier work does not settle

LT5 turn 6 ruled out naive global CPTP promotion of deterministic real reset Q_s=I-s ee^T and noted that a valid nonselective quantum channel does not by itself specify an outcome-bearing instrument. LT4's scientific monograph §5.4–5.6 contains process-tensor and Choi legality, an example of different multitime statistics despite identical one-step channels, and a CPTP intermediate re-preparation example. Here we test a strictly **stronger data-matching null hypothesis**:

> Does the *pair* consisting of (i) the entire nonselective CPTP quantum channel and (ii) the *entire* POVM of classical readout outcomes suffice to determine what can be achieved by a controller that acts after reading the outcome?

Exact answer: NO, even for a single qubit, two outcomes, no unknown generator, one late correction port, and no signal noise beyond fully declared Born statistics. We exhibit two legitimate instruments with identical POVM and nonselective CPTP channel, yet different probability of discrimination and reversibility under causal feedforward. The distance of the full flagged instruments in diamond norm is calculated exactly.

This is an explicit example of *environment-assisted quantum error correction* / random-unitary unraveling, fully known in quantum information theory; the novelty claim must remain ZERO. The project-specific benefit is a precise typed firewall for future LT/INT5–8/NASH measurement claims, not a discovery.

## 1. Complete definition of two distinct quantum instruments

Let \(\mathsf H=\mathbb C^2\), \(Z=\sigma_z=\mathrm{diag}(1,-1)\), and fix a known \(p\in[0,1]\).

Define the random-unitary dephasing channel

\[
 \Lambda_p(\rho)=(1-p)\rho+pZ\rho Z.                    \tag{1}
\]

Instrument **F** (FLAGGED-ERROR): outcome \(a\in\{0,1\}\) reports which unitary error occurred:

\[
 {\cal F}_0(\rho)=(1-p)\rho,\qquad
 {\cal F}_1(\rho)=pZ\rho Z.                              \tag{2}
\]

Instrument **C** (INDEPENDENT-COIN): the classical outcome has the same known marginal probabilities but is independent of the actual random unitary error:

\[
 {\cal C}_0(\rho)=(1-p)\Lambda_p(\rho),\qquad
 {\cal C}_1(\rho)=p\Lambda_p(\rho).                      \tag{3}
\]

They are valid quantum instruments because all outcome operations are CP and trace non-increasing, and the sum of each pair equals (1). Explicit Kraus lists:
- \({\cal F}_0\): \(\sqrt{1-p}\,I\); \({\cal F}_1\): \(\sqrt{p}\,Z\).
- \({\cal C}_0\): \((1-p)I,\sqrt{p(1-p)}\,Z\).
- \({\cal C}_1\): \(\sqrt{p(1-p)}\,I,pZ\).

Each operation's effect is \(E_a={\cal I}_a^\dagger(I)\). For **BOTH** instruments,

\[
 E_0=(1-p)I,\qquad E_1=pI.                              \tag{4}
\]

Thus \(\Pr(a=0|\rho)=1-p,\Pr(a=1|\rho)=p\) for EVERY qubit state \(\rho\); the recorded bit conveys no information about the unknown initial preparation by itself. Yet it can convey crucial information about **which disturbance occurred**.

The joint record + surviving-qubit quantum channels are

\[
 \widehat{\cal F}_p(\rho)
 =|0\rangle\langle0|\otimes(1-p)\rho
  +|1\rangle\langle1|\otimes pZ\rho Z,                \tag{5}
\]
\[
 \widehat{\cal C}_p(\rho)
 =[(1-p)|0\rangle\langle0|+p|1\rangle\langle1|]
       \otimes\Lambda_p(\rho).                         \tag{6}
\]

Discarding the flag produces the *same* \(\Lambda_p\) in both. Reading only the flag produces the *same* input-independent classical distribution in both.

### Why the distinction is physical within quantum theory

The instruments may be implemented using a declared classical random bit selecting whether \(Z\) is applied. In F the logged bit equals that choice; in C the displayed bit is an independent coin with the same distribution. No hypothetical non-CP map or transposed state is involved. The difference is a classical correlation between the outcome register and the applied disturbance, and it matters only if the register is available before a follow-up action.

## 2. Exact recovery theorem and impossibility for the unflagged version

**Theorem LT5-7.1 (identical channel and POVM, opposite causal recovery).**

For any \(0\le p\le1\), the outcome-conditioned recovery channels

\[
 {\cal R}_0=\operatorname{id},\qquad
 {\cal R}_1=\operatorname{Ad}_Z
\]

applied after instrument F give the exact identity channel:

\[
 \sum_{a=0}^1 {\cal R}_a\circ{\cal F}_a
    =(1-p)\operatorname{id}+p\operatorname{Ad}_Z^2
    =\operatorname{id}.                                 \tag{7}
\]

Hence all states, including states entangled with a reference system, are recovered exactly if the classical error flag is available in time.

For \(0<p<1\), **no outcome-conditioned collection of CPTP recovery channels** \({\cal R}'_0,{\cal R}'_1\) applied after C can recover all possible inputs exactly. The proof needs only the input pair \(\rho_\pm=(I\pm X)/2\), with \(X=\sigma_x\), since

\[
 \Lambda_p(\rho_\pm)
     =\frac12[I\pm(1-2p)X].                             \tag{8}
\]

Their trace distance is

\[
 D(\Lambda_p\rho_+,\Lambda_p\rho_-)=|1-2p|<1
       \quad(0<p<1),                                    \tag{9}
\]

where \(D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1\). The classical coin is independent of the input, so the joint instrument C retains exactly this distance. Every outcome-conditioned CPTP recovery is one further CPTP map on the joint classical–quantum register and cannot increase trace distance. Perfect restoration of both orthogonal input states would require output distance 1, contradicting (9). QED.

**Important distinctions:** the flag has zero mutual information with the *input label* in isolation, yet suffices to correct a known random unitary. This is standard error-syndrome information, not paradoxical information creation or a physical theorem connecting input Shannon entropy and arbitrary unitary correction.

## 3. Binary decision guarantee and exact class separation

Take equiprobable hypotheses

\[
 \rho_+=|+x\rangle\langle+x|,\qquad
 \rho_-=|-x\rangle\langle-x|.                           \tag{10}
\]

The outcome plus surviving quantum system under F gives orthogonal states for each branch, so the optimal one-shot correct-identification probability is exactly

\[
 P_{\mathrm{succ}}^{\cal F}=1.                           \tag{11}
\]

Under C, the record is an independent coin, and the surviving states are (8). By the Helstrom theorem,

\[
 P_{\mathrm{succ}}^{\cal C}
   =\tfrac12\bigl(1+|1-2p|\bigr)
   =\max\{p,1-p\}.                                      \tag{12}
\]

At \(p=\frac12\) this equals random guessing \(1/2\), whereas F still permits perfect discrimination with one immediate conditional \(Z\) correction.

If ONLY THE CLASSICAL OUTCOME is kept, both experiments give exactly \(P_{\mathrm{succ}}=1/2\); if only the nonselective qubit remains, both experiments give exactly \(\max(p,1-p)\). Their differentiation requires access to the **correlation** between the record and the surviving quantum system.

This is a legal one-stage source-matched operational example, not a claim that a quantum effect \(E_a\) fully encodes its conditional state transformation.

## 4. Stronger quantitative result: exact diamond distance of the instrument channels

**Theorem LT5-7.2 (exact instrument diamond gap despite zero channel/POVM gap).**

\[
 \boxed{
 \left\|\widehat{\cal F}_p-\widehat{\cal C}_p\right\|_\diamond
       =4p(1-p).
 }                                                        \tag{13}
\]

Meanwhile

\[
 \sum_a{\cal F}_a=\sum_a{\cal C}_a=\Lambda_p,\qquad
 {\cal F}_a^\dagger(I)={\cal C}_a^\dagger(I)
\]

for every \(a\). Thus the distance of the associated *nonselective channels* is exactly zero, as is the discrepancy of all input-state outcome probabilities.

**Proof.** Subtract the two classical–quantum output maps to obtain the factorized superoperator

\[
 \widehat{\cal F}_p-\widehat{\cal C}_p
  =p(1-p)(|0\rangle\langle0|-|1\rangle\langle1|)
              \otimes(\operatorname{id}-\operatorname{Ad}_Z).
                                                               \tag{14}
\]

For an arbitrary test input jointly with any reference system, the output has two orthogonal blocks \(\pm p(1-p)(\operatorname{id}-\operatorname{Ad}_Z)\otimes\operatorname{id}_R(X)\). Its trace norm is exactly \(2p(1-p)\) times the trace norm of the latter single block. Therefore

\[
 \|\widehat{\cal F}_p-\widehat{\cal C}_p\|_\diamond
   =2p(1-p)\|\operatorname{id}-\operatorname{Ad}_Z\|_\diamond.
                                                               \tag{15}
\]

The difference of two channels has diamond norm at most 2 by triangle inequality. It attains 2 already on \(\rho_+\), because \(\rho_+\) and \(Z\rho_+Z=\rho_-\) are orthogonal. Consequently the norm in (15) is 2 and (13) follows. QED.

At \(p=1/2\), (13) equals **1**, although the two averaged CPTP maps and two POVM effects coincide exactly.

At the deterministic endpoints p=0 or p=1, the two instruments coincide and (13) equals zero, as it should.

**This result is a special case of basic cb-trace-norm calculus, not a novel operational quantity.** It supplies a sharp reproducible numerical discriminator in the project's instrument/target hierarchy.

## 5. Matrix regression / independent low-cost check

The following NumPy control checks instrument CP by explicit Kraus forms, exact effects and sums, and one-shot trace distances on seven parameter points. Formula (13) is proven analytically; the numerical 'diamond' column below is (13), not an SDP estimate.

    import numpy as np

    I=np.eye(2,dtype=complex)
    X=np.array([[0,1],[1,0]],complex)
    Z=np.diag([1,-1]).astype(complex)
    rho_p=(I+X)/2;rho_m=(I-X)/2

    def trace_norm(M):
        return float(np.sum(np.linalg.svd(M,compute_uv=False)))

    for p in [0.,.1,.25,.5,.75,.9,1.]:
        L=lambda rho:(1-p)*rho+p*Z@rho@Z
        flagged=lambda rho: ((1-p)*rho,p*Z@rho@Z)
        coin=lambda rho: ((1-p)*L(rho),p*L(rho))
        assert np.allclose(sum(flagged(rho_p)),L(rho_p))
        assert np.allclose(sum(coin(rho_p)),L(rho_p))
        assert np.allclose(flagged(rho_p)[0]+Z@flagged(rho_p)[1]@Z,rho_p)
        assert np.allclose(flagged(rho_m)[0]+Z@flagged(rho_m)[1]@Z,rho_m)
        df=sum(trace_norm(a-b)
               for a,b in zip(flagged(rho_p),flagged(rho_m)))/2
        dc=sum(trace_norm(a-b)
               for a,b in zip(coin(rho_p),coin(rho_m)))/2
        assert np.isclose(df,1.)
        assert np.isclose(dc,abs(1-2*p))
        assert np.isclose((1+dc)/2,max(p,1-p))
        assert np.isclose(4*p*(1-p),
                          2*p*(1-p)*trace_norm(rho_p-Z@rho_p@Z))
    print("SEVEN_INSTRUMENT_REGRESSION_CHECKS_PASS")

Numerically reproduced on seven p values:

| p | Flagged success | Independent coin success | Exact instrument diamond distance |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 0.10 | 1 | 0.90 | 0.36 |
| 0.25 | 1 | 0.75 | 0.75 |
| 0.50 | 1 | 0.50 | 1.00 |
| 0.75 | 1 | 0.75 | 0.75 |
| 0.90 | 1 | 0.90 | 0.36 |
| 1 | 1 | 1 | 0 |

These are analytic expressions corroborated by independent matrix arithmetic. They are not sample-based quantum hardware observations.

## 6. Precise relation to current LT and other cells

- **LT5 turn 6:** GLOBAL naive Bloch reset Q_s non-CP has best CPTP diamond distance s/2; this theorem does NOT concern approximate CP repair. Both instruments here are CP by construction and their averaged channels are identical. The new seam is selective outcome–state correlation, not channel positivity.
- **LT5 turn 5:** its deterministic continuous b with bounded adversarial eta and reset Q_s remains CLASSICAL. No attempt is made to reinterpret that b as the Born outcome of these instruments. In the present example the outcome distribution is state-independent; it carries information about an applied error, not about input preparation.
- **LT working monograph chapter 5:** the existing two-time environment-memory counterexample §5.5 and CPTP intermediate intervention §5.5a already establish that channel marginals can fail to specify multi-time process laws. The current stronger counterexample states that the entire pair (nonselective channel, POVM) can be insufficient to specify even one selectively resolved instrument relevant to a causal policy. The correct input object for multi-time prediction is the outcome-indexed CP instrument inserted into a valid process/comb, not only (Lambda,{E_a}).
- **INT8/Geeky-S10:** their deterministic real reset/observation carrier is not invalidated. Their storage and weak-readout theorems neither assume nor imply a specific qubit instrument with outcome-resolved Kraus operations. No quantum physics promotion follows from an abstract reset semigroup.
- **PRF11:** a record can be uninformative about the preparation in the ordinary parameter-estimation sense but useful for a different *decision target*: correction of known random-unitary disturbance. This is a type distinction between "information about initial state" and "information about realized transformation", not a contradiction with statistical data processing. The claimed information resource must be declared before quoting a risk bound.
- **REC10:** their earlier turn-specific mathematical PASS and sharpening do not constitute a referee approval of the present quantum instrument claim. The minimal high-leverage review is the branch-Kraus arithmetic, identity recovery, and factorized diamond norm (13).

## 7. Strong mature host / subtraction, with provenance

The mathematical phenomenon is explicitly within well-known **environment-assisted correction of random-unitary noise**:
- M. Gregoratti, R. F. Werner, *Quantum lost and found*, Journal of Modern Optics 50 (2003), 915–933. DOI: https://doi.org/10.1080/09500340308234541 ; preprint https://arxiv.org/abs/quant-ph/0209025 . They characterize correction assisted by measuring the environment; random-unitary/isometric mixtures are mature standard hosts.
- M. Gregoratti, R. F. Werner, *On quantum error-correction by classical feedback in discrete time*, Journal of Mathematical Physics 45 (2004), 2600–2612, DOI https://doi.org/10.1063/1.1758320 ; preprint https://arxiv.org/abs/quant-ph/0403092 . Explicit classical feedback for quantum error correction.
- B. Trendelkamp-Schroer, J. Helm, W. T. Strunz, *Environment-assisted error correction of single-qubit phase damping*, Physical Review A 84 (2011), 062314, DOI https://doi.org/10.1103/PhysRevA.84.062314 . Explicit qubit phase-damping correction.
- Standard Holevo–Helstrom binary quantum-state discrimination and quantum trace-distance data processing; e.g. https://doi.org/10.1103/PRXQuantum.6.030202 for a contemporary review.

**Subtraction verdict:** This instrument example is **NOT** a new scientific principle, not a novel measurement apparatus, not an independent prediction and not a quantum foundation breakthrough. Its value for the LT monograph is a short, rigorous, source-typed demonstration that even channel equality plus POVM equality fails to determine causal feedback capability. The exact 4p(1-p) computation makes a useful regression test for future claimed process/supermap transports, not a candidate for priority outside the project.

## 8. Editorial-ready monograph insert (NOT incorporated)

**Proposed position:** after §5.5a or after §5.6, as a boxed theorem/counterexample of one legal instrument seam. Refrain from creating a new chapter solely to repeat mature environment-assisted correction.

> *Instrument niewyznaczony przez kanał i POVM.* Nawet podanie pełnego kanału nieselektywnego i wszystkich efektów POVM nie wyznacza operacji selektywnych. Dla kanału \(\Lambda_p=(1-p)\mathrm{id}+p\mathrm{Ad}_Z\) dwa instrumenty \(\mathcal F_a\) oraz \(\mathcal C_a\) mogą mieć tę samą sumę i efekty \(E_0=(1-p)I,E_1=pI\), ale w jednym wynik rejestruje faktyczną operację \(Z^a\), a w drugim jest niezależną monetą. Pierwszy dopuszcza dokładną korekcję \(\sum_a\mathrm{Ad}_{Z^a}\circ\mathcal F_a=\mathrm{id}\); drugi przy \(p=1/2\) całkowicie zaciera rozróżnienie \(|\pm x\rangle\). Różnica ich kanałów z zachowanym rejestrem ma normę diamentową \(4p(1-p)\), pomimo zerowej różnicy kanałów nieselektywnych. W konsekwencji dla przewidywań interwencyjnych trzeba podać rodzinę CP operacji instrumentu i reguły późniejszej korekcji, nie tylko kanał i statystyki wyników. Jest to szczególny przypadek znanej teorii korekcji wspomaganej informacją o środowisku.

No insertion is executed before independent review/current revision coherence.

## 9. Failure conditions and status

**Must not infer:**
- SAME_AVERAGED_CPTP + SAME_POVM => SAME_INSTRUMENT;
- RECORD_STATE-INDEPENDENT => RECORD_USELESS_FOR_EVERY_ACTION;
- PERFECT_CORRECTION_WITH_FLAG => INITIAL_PREPARATION_IDENTIFIED_FROM_FLAG;
- INSTRUMENT_DIAMOND_GAP => DISTANCE_BETWEEN_AVERAGED_CHANNELS;
- RANDOM-UNITARY_SYNDROME_CORRECTION => CLASSICAL_Q_s_GENERAL_QUANTUM_LIFT;
- QUANTUM_EXAMPLE => NEW_GRAVITY/NCDG_PHYSICAL_SIGNAL.

**Independent referee:** PENDING. **Owner/editorial acceptance:** UNVERIFIED. **BW ingest:** UNVERIFIED.
**Host category:** known Gregoratti–Werner environment-assisted correction, no novelty.
**Strong result:** exact factorized instrument diamond difference + causal correction witness.
**Stop:** This exact family is mathematically closed unless reviewer finds an error; do not cascade into routine new tasks. A genuinely distinct scientific extension would require process-specific tester data, constrained/partial access to syndrome, finite-time operation or noisy flag channel, and theorem-level subtraction against established feedback correction literature.
