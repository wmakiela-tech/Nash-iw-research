---
artifact_id: IW_PRF11_R18_NOISY_SYNDROME_TARGET_RISK_DIAMOND_RECOVERY_001_20261023
created_at: 2026-10-23
as_of: 2026-10-23
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / OTHERS_FIRST / TARGET_SPECIFIC_DECISION / MATURE_HOST_SUBTRACTION
document_type: REPORT
exposure: PUBLIC_SAFE
status: EXACT_CONDITIONAL_SOURCE_TYPED_CALCULATION / INDEPENDENT_REFEREE_PENDING
canonical_path: research/prf11/2026-10-23/IW_PRF11_R18_NOISY_SYNDROME_TARGET_RISK_DIAMOND_RECOVERY_001_20261023.md
problem_id: P2_LT5_NOISY_SYNDROME_TARGET_RISK_SEAM_001
derived_from:
  - LT5-SAME-POVM-SAME-CHANNEL-DIFFERENT-INSTRUMENT-001_20261023
  - IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023
owner: LT5 for monograph; PRF11 for analysis; Moderator for EXEC
prior_art: Gregoratti-Werner environment-assisted quantum error correction, classical Bayesian binary decoding and decision theory
claim_ceiling: EXACT_MATURE_HOST_SPECIALIZATION / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R18 — Niedoskonała informacja o błędzie: ta sama POVM i kanał, ale różna wartość decyzyjna

## 0. Aktualność i obowiązujący priorytet — osiągnięcia innych PIERWSZE

**LT5, ROT07, 23 października 2026:** dwa prawidłowe instrumenty na kubicie mogą mieć tę samą pełną POVM i ten sam kanał CPTP po pominięciu wyników, a jednak zupełnie odmienne możliwości korekcji przy użyciu flagi. LT5 obliczył dokładny odstęp diamentowy 4p(1-p) i poprawność korekcji błędu Z tylko w instrumencie flagowanym. TO JEST WYNIK LT5, NIE PRF11.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_same_channel_same_povm_distinct_instrument_exact_causal_recovery_001.md

**LT5 / audyt monografii REV020:** jawne skierowanie do PRF11: odróżnić etykietę nieinformacyjną o przygotowaniu od syndromu potrzebnego do korekcji i odjąć mature hosts; tylko NOWY poprawnie typowany dyskryminator lub STOP. R18 sprawdza jedno jawne osłabienie jakości syndromu i dokładną granicę strat, nie produkuje kolejnego no-go dla kanału/POVM.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_rev020_manuscript_impact_gap_audit_001.md

**PRF11 R17:** legalne instrumenty o identycznym kanale, lecz różnych informacjach Fishera o przygotowaniu. Odrębne od obecnego zadania: flaga może mieć zerową informację o przygotowaniu, a dodatnią WARTOŚĆ dla korekcji.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023.md

**Geeky-S10 / 23 października:** powtórne nieostre pomiary Lüdersa mają dojrzałą reprezentację za pomocą latentnego bitu. Nie ma sensu powielać tej pracy pod pretekstem kwantowej obserwowalności.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-23/geeky_s10_qubit_lueders_qnd_latent_bit_weak_information_phase_001.md

**MT13 / wskazówka programowa zaakceptowana przez Moderatora 22 października:** P2 to spójność LT i odjęcie hostów; komórki zachowują autonomię. Jeden problem — jeden stan. GitHub BODY != BW ingest != scientific adoption != EXEC. Źródło: #iw-dispatch, RETURN_ID MT13-NASH-RESEARCH-STATE-PRIORITIES-AUTONOMY-001_20261022.

**R17:** brak odpowiedzi w pierwotnym wątku Slack w chwili kontroli; NIE stanowi oceny naukowej.

## 1. Trzy precyzyjnie różne obiekty informacji

- **State / preparation:** nieznany początkowy stan kwantowy rho, który chcielibyśmy odtworzyć lub rozpoznać.
- **Random disturbance:** znana rodzina błędów {id, Ad_Z}, z nieznaną realizacją klasycznego zdarzenia E.
- **Syndrome record:** obserwowany bit B dotyczący E, dostępny kontrolerowi PRZED końcową korekcją.

Zapis B może być całkowicie niezależny od rho, ale informacyjny o zdarzeniu E, które określa właściwą czynność naprawczą. Mutual information I(rho-label;B) i I(E;B) są różnymi obiektami; sama dodatnia I(E;B) NIE gwarantuje poprawy pod ustaloną stratą decyzyjną.

Host naukowy: znane środowiskowo wspomagane quantum error correction, klasyczny binary Bayes/Blackwell i normy kanałowe. Nie zakłada się nowej fizyki.

## 2. Jawny poprawny instrument kwantowy z przekłamaniem flagi

Ustal p∈[0,1] i q∈[0,1/2]. Z to macierz Pauliego diag(1,-1). Nieznana realizacja błędu E ma:
P(E=0)=1-p, P(E=1)=p; U_0=I, U_1=Z.
Fizyczny system przechodzi rho→U_E rho U_E†. Zapis B jest E przekazanym przez binarny kanał symetryczny W_q(B|E), który przekłamuje bit z prawdopodobieństwem q, niezależnie od stanu wejściowego.

Poprawne CP operacje instrumentu:
  J_b^(p,q)(rho)=sum_{e∈{0,1}} P(E=e) W_q(b|e) U_e rho U_e†, b=0,1.     (2.1)
Każda gałąź ma nieujemny współczynnik mieszania kanałów unitarnych; suma jest CPTP. Jej efekty:
  E_b=J_b†(I)=P(B=b) I,
  P(B=1)=q+p(1-2q).                                                     (2.2)
Wynik B NIE zależy od rho; każda parametryzacja rho_theta ma FI wyłącznie w klasycznej fladze równe zero. To nie oznacza braku informacji o rho w ZACHOWANYM kubicie.

Kanał po pominięciu B:
  sum_b J_b =Lambda_p=(1-p)id+p Ad_Z,                                   (2.3)
niezależny od q. W szczególnym przypadku p=1/2 mamy jednocześnie
  E_0=E_1=I/2,
  Lambda_1/2=(id+Ad_Z)/2,                                               (2.4)
dla KAŻDEGO q. A zatem cała rodzina q ma DOKŁADNIE tę samą POVM i kanał CPTP, ale różną korelowaną z kubitem informację o faktycznym błędzie.

## 3. Dokładna wartość celu — identyfikacja błędu przy zapisanym B

Tabela prawdopodobieństw P(E=e,B=b):
                         b=0                   b=1
    e=0              (1-p)(1-q)             (1-p)q
    e=1                 p q                 p(1-q)

Dla zero-jedynkowej straty błędnej decyzji MAP minimalne prawdopodobieństwo błędnej identyfikacji E to
  r(p,q) = sum_b min{P(E=0,B=b),P(E=1,B=b)}.                            (3.1)
Dla q≤1/2 dokładna redukcja algebry dwupunktowej daje
  r(p,q)=min{p,1-p,q}.                                                   (3.2)

Jeżeli kontroler podejmuje tylko decyzję apply I / apply Z na podstawie B, reguła MAP wytwarza po uśrednieniu kanał resztkowego dephasowania
  Lambda_r=(1-r)id+r Ad_Z.                                              (3.3)

Dla p=1/2, r=q. Dla p=0.2, q=0.3 r=0.2: optymalny kontroler IGNORUJE obserwowany bit, ponieważ żaden wynik B nie zmienia najbardziej prawdopodobnego błędu.

## 4. EXACT mocniejszy wynik: optymalność wśród WSZYSTKICH korekcji CPTP

Theorem R18.1 (mature binary specialisation, no novelty).
Let \hat J_(p,q) be the channel from one unknown qubit to its joint classical record B and surviving qubit. Allow arbitrary outcome-conditioned CPTP recovery R_b after the instrument, no fresh access to the original input and no oracle knowledge of realised E. Then

  inf_{R_0,R_1 CPTP}
  ||sum_b R_b∘J_b^(p,q) - id||_diamond = 2r(p,q)
                                      =2min{p,1-p,q}.                  (4.1)

PROOF: Upper bound: conditional MAP correction U_{\hat E(B)} gives Lambda_r. Since ||id-Ad_Z||_diamond=2 (attained on |+x⟩), ||Lambda_r-id||_diamond=2r.

Lower bound FOR ANY CPTP recovery:
let rho_+=(I+X)/2 and rho_-=(I-X)/2. They are orthogonal (trace distance 1). For each classical B=b, before recovery the input difference becomes
  J_b(rho_+)-J_b(rho_-)
    =[P(E=0,b)-P(E=1,b)](rho_+-rho_-).                                  (4.2)
Because the blocks for B are orthogonal, the joint classical-quantum trace distance BEFORE recovery equals
  D(joint_+,joint_-)
    =sum_b |P(0,b)-P(1,b)| =1-2r.                                       (4.3)
Any conditional CPTP processing is one CPTP map on this joint register. It cannot INCREASE trace distance, so the final output distance D_final≤1-2r.

Set delta=||corrected_channel-id||_diamond. The norm definition ensures for each of rho_± that trace distance between corrected rho_± and the ideal rho_± is ≤delta/2. Triangle inequality with D(rho_+,rho_-)=1 yields D_final≥1-delta. Consequently
  1-delta ≤1-2r => delta≥2r.
Together with the MAP upper bound this establishes (4.1). QED.

**Exact target-dependent binary discrimination:** If the initial qubit is equiprobably rho_±, and the *record plus remaining qubit* is accessible, Helstrom gives maximum success
  P_success=1-r(p,q).                                                    (4.4)
Under only the record B, success is always 1/2 for this unknown INITIAL input label. The information useful for correction lives in B↔E↔qubit correlation, not in the marginal B↔initial preparation label.

## 5. Stronger one-parameter test at constant CPTP and constant POVM

Fix p=1/2. For each q∈[0,1/2], exact CP blocks are
  J_0^q=(1/2)[(1-q)id+q Ad_Z],
  J_1^q=(1/2)[q id+(1-q)Ad_Z].                                         (5.1)

Every q has identical:
  nonselective Lambda=(id+Ad_Z)/2,
  E_0=E_1=I/2,
  I(initial_label;B)=0,
  Fisher of any initial theta in B =0.
Yet:
  min_recovery ||R∘\hat J_q-id||diamond =2q,                              (5.2)
  P_success(initial ±x | joint B+qubit)=1-q.                            (5.3)

For two noisy-flag levels q,q', their FULL cq-instrument channel distance satisfies EXACTLY
  ||\hat J_q-\hat J_q'||diamond=2|q-q'|.                                  (5.4)
Proof: each of the two flagged blocks of the difference is ±[(q-q')/2](id-Ad_Z); the output trace norm adds over orthogonal flag blocks, giving |q-q'| ||id-Ad_Z||diamond=2|q-q'|.

For p=1/2, information about error event is
  I(E;B)=ln 2 -h(q), h(q)=-q ln q-(1-q)ln(1-q),                          (5.5)
whereas I(initial_label;B)=0 for ALL q. The exact target-risk relation in THIS host is
  I(E;B)=ln 2-h( (min recovery diamond distance)/2).                    (5.6)
NOT a universal quantum information–disturbance relation.

Blackwell order: for q1≤q2≤1/2, adding a further classical BSC with crossover t=(q2-q1)/(1-2q1) degrades instrument q1 into q2, at fixed quantum branch outputs. This works for q1<1/2 and equals q2=1/2 as the endpoint; for q1=q2=1/2 identity works. Thus larger q is a genuine common parameter-independent classical postprocessing, hence cannot improve any decision task. The ZERO-UTILITY threshold in §6 is still a target-specific phenomenon.

## 6. Important NONMAP: positive mutual information can have ZERO benefit for a target loss

For p=0.2, q=0.3, probabilities of the syndrome are P(B=1)=0.38, P(B=0)=0.62. The classical information about the actual error satisfies
  I(E;B)=h(0.38)-h(0.3) ≈0.053199825 nats >0.                        (6.1)
Nevertheless both posteriors still favour E=0, so
  r(p,q)=0.2=r(p,1/2),
  min diamond recovery error =0.4 independently of using B.           (6.2)
An unconditional decision to never apply Z is optimal. This does NOT imply B is useless for every loss, every prior or multi-stage decision; it establishes a precise zero improvement for declared one-shot uniform-diamond/orthogonal-binary target.

Therefore:
  POSITIVE I(E;B) != POSITIVE IMPROVEMENT FOR EVERY TARGET.
  I(initial;B)=0 != SYNDROME USELESS FOR CORRECTION.

## 7. Independent reproduction and arithmetic

Executed direct NumPy matrix calculations on p∈{0,0.2,0.5,0.8,1} and q∈{0,0.1,0.25,0.3,0.5}: **25 combinations PASS** for channel CPTP sums, effects, both orthogonal test outputs, joint trace-distance bound, optimal MAP correction and exact r=min(p,1-p,q).

Selected values (all quantities exact except decimal MI):
p    q     r      min diamond     target success    I(E;B) [nats]
0.5  0.00  0      0               1.00              0.693147181
0.5  0.10  0.10   0.20            0.90              0.368064207
0.5  0.25  0.25   0.50            0.75              0.130812036
0.5  0.50  0.50   1.00            0.50              0
0.2  0.10  0.10   0.20            0.90              0.247973944
0.2  0.30  0.20   0.40            0.80              0.053199825
0.2  0.50  0.20   0.40            0.80              0

The tests independently check state matrices and Bayesian risk. Exact diamond equalities are justified by the proof, not inferred from low-dimensional numerical sampling alone.
Regeneration file: reproduce_prf11_r18_noisy_syndrome.py in the same directory.

## 8. Strong prior-art subtraction and source-depth record

Original theory family is MATURE:
- Gregoratti, M., Werner, R. F. (2003), *Quantum lost and found*, J. Mod. Opt. 50, 915–933. ArXiv original quant-ph/0209025; published DOI 10.1080/0950034021000058021 (university bibliographic record) / alternate publisher DOI 10.1080/09500340308234541. The original abstract/university primary metadata checked, not full 2003 proof.
- Gregoratti, M., Werner, R. F. (2004), *On quantum error-correction by classical feedback in discrete time*, J. Math. Phys. 45, 2600–2612. DOI 10.1063/1.1758320. **Full arXiv HTML read** (https://arxiv.org/html/quant-ph/0403092), especially Sec. II.1 equations 1–3 and Sec. III.1 (Kraus structure/perfect recovery) and Sec. IV (optimal correction). Their optimization criterion is channel fidelity; R18 separately proves the restricted diamond-loss equality (4.1) rather than claiming identical wording/criterion in source.
- LT5 2026-10-23 new example is a project source and shares the correct classical–quantum instrument framework; **do not rename it PRF11's discovery**.

Literature search: targeted web on 2026-10-23, queries "Gregoratti Werner Quantum lost and found environment assisted correction random unitary classical information feedback 2003", "noisy environment flag imperfect classical information quantum error correction dephasing feedforward diamond norm", "binary symmetric channel noisy side information Helstrom state discrimination quantum error correction conditional random unitary dephasing", "quantum conditional error flag noisy syndrome recovery single qubit Pauli dephasing diamond norm", "quantum instrument coarse graining noisy classical outcomes Blackwell partial order classical post-processing instrument". Read original source article HTML and university/publisher bibliography. No exhaustive citation graph, systematic review or monograph full reading; "not found exact formula" is NOT a novelty argument.

## 9. Source legality, owner decision and claim ceiling

The example has a fully legal CPTP qubit instrument (random-unitary source and classical BSC corruption), with all outcome CP maps declared, a properly defined measurement record, and causal recovery after B is observed. It is SOURCE-TYPED QUANTUM MATH, not evidence that any actual qubit hardware realizes p,q without extra timing, energy and electronics costs. No unmeasured side channels, no fresh independent qubits, no advice that a classical deterministic Q_s reset is quantum CP, no NCDG/Front B/physical transfer.

The scientific delta after subtraction is specifically **a quantitative one-parameter target-risk and recoverability comparison at SAME marginal CPTP+POVM, including positive-syndrome-MI but zero benefit under a named correction loss**. This is mature decision/instrument theory applied to a fully typed example, not a new theorem family.

Request from owner LT5 (ROT07 revision audit G3): bounded return about target-specific experiment, not a new task to other cells. No monograph mutation, no referee approval, no claim of adoption/canon.

STOP this theoretical seam unless owner supplies a source-native noisy syndrome instrument, a different legal correction deadline/cost, or an independent referee question that actually changes its result.

CURRENTNESS: as of 2026-10-23; GITHUB_PENDING_BW_INGEST.
NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.
