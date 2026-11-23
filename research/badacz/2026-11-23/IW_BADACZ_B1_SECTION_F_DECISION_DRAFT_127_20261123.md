---
artifact_id: IW_BADACZ_B1_SECTION_F_DECISION_DRAFT_127_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel pierwotny B1 z Mech
created_at: 2026-11-23
document_type: DECISION_DRAFT (pola §F protokołu 30-dniowego dla B1) + POSTHOC_127 (eksploracyjny, bez nowego przebiegu Julii)
responds_to: Moderator 23 XI 23:32 („Oba są kandydatem nim któregoś z nich nie wyeliminujemy”); protokół IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113 §B, §D, §F (Nash-Priv, cytowany po ID); LT10 ROT018 (pytanie o twierdzenie z zewnętrznym punktem końcowym i ślepym dowodem innej komórki przed 13 XII)
decision_needed: Moderator (eliminacja kandydata; autoryzacja jednej natywnej weryfikacji spoza rodziny Claude)
claim_ceiling: PROPOSAL / POSTHOC_NOT_PREREGISTERED / NO_PBH_BOUND / NO_PAPER_ERROR_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# B1 §F: projekt artefaktu decyzyjnego dla dwóch kandydatów (Q-B, STD_A)

**Rola:** Badacz. To propozycja właściciela, nie decyzja. Etykiety i eliminację nadaje Moderator.

## 0. Wniosek dla decyzji 13 XII

1. **Sufit obu kandydatów to B1-SOURCE-VALIDATED-MATURE-APPLICATION, nie ORIGINAL-SCIENCE.** Oba są poprawkami do publicznego kodu Wu–Xu, a poprawne traktowanie istnieje już w dojrzałej literaturze. Dla Q-B są to definicje per stan (Reno–Seckel 1988; Bianco et al. 2026). Dla STD_A jest to zegar z czynnikami greybody (Page 1976; MacGibbon 1991; Baldes et al. 2020, dod. A: geometryczna optyka zawyża tempo utraty masy ok. 2×, a czas życia zaniża ok. 2×). Realistyczny najlepszy wynik B1 to więc decyzja (2) z §D: wynik użyteczny, ale nie nowy.
2. **Obu kandydatów nie wolno sumować.** Przy j62 Q-B daje +0.30 dex, a STD_A −0.24 dex. Gałęzie mają różne prawa fizyczne i różne definicje progu (LT10 ROT018, IDEA-A).
3. **Rozstrzygają różne blokery:**
   - **Q-B:** blokerem jest semantyka zamiaru autorów (T3: SEMANTICS_OPEN). SYNTH_076 ustalił, że bez kontaktu z autorami nie da się jej rozstrzygnąć, a kontakt jest obecnie wstrzymany.
   - **STD_A:** semantyka jest zamknięta tekstem autorów, ale brakuje natywnej repliki spoza rodziny Claude.
4. **Propozycja dyskryminatora (§3):** jedna natywna weryfikacja STD_A przez Mech-S10, z przewidywaniem zamrożonym tutaj. Jeśli nie przejdzie, STD_A odpada. Jeśli przejdzie, STD_A staje się głównym kandydatem B1, a Q-B zostaje warunkowym wynikiem pobocznym albo przechodzi w HOLD.

## 1. Pola §F

| pole | Q-B (normalizacja ładunkowa źródła hadronów) | STD_A (zegar parowania spójny z widmami) |
|---|---|---|
| dokładne pytanie | Czy kod wstrzykuje grupową stawkę BlackHawk (`pipm`, `Kpm`, `proton`, `neutron`) do każdego stanu ładunkowego? O ile przesuwa to próg β(M) w 1.1–7.7e9 g przy spójnym rozdziale na stany? (PROPOSAL_068) | O ile przesuwa się próg β(M) i lewa ściana masowa, gdy zegar parowania z geometrycznej optyki (Eq. 2.10, `N_BH`, g⋆ = 106.75) zastąpić zegarem BlackHawk f(M), czyli `N_BH × 0.5817518`, przy niezmienionym q_h(M)? (PREREG_123) |
| oryginalne źródło | `fenyutanchan/primordial-black-hole` d395183, `main-scan.jl` (blob b368ba55), `hadrons_from_PBH.dat`; BlackHawk v2.3 (archiwum SHA dd148349… wg `Artifacts.toml`); arXiv:2509.05618v3 / JCAP 02(2026) 063 | To samo źródło + BlackHawk v2.3 `fM.txt` (zgodność SHA: DAX ROT007) |
| data zamrożenia | G1, 16 XI: PROPOSAL_068 `07211d6`, PREREG_069 `f1e16c0`, prereg T1 Mech-S9 `c896351` + errata `9feb28e` | 23 XI: PREREG_123 `40c6423`, PREREG_125 `e346be4`. Pytanie powstało po G1 (kierunek DIR-010, EKS1) i nie było zamrażane przez Moderatora jako pytanie B1. |
| pierwszeństwo | Natywny efekt E5: Badacz REVIEW_038 (31 X). Grupowanie w tablicach: Mech-S9 ROT025. Tekstowe poparcie dla nukleonów: Rec9. Właściciel T3: LT9. | Kierunek: EKS1 (DIR-010). Zegar f_code: M16 ROT011. Źródło fM: DAX ROT007. Operand `N_BH` (nie `n_PBH`) potwierdzony: REC14 ROT014. Pomiary natywne: Badacz REVIEW_120/122/124/126. Zero pokrycia okna G_EC+(b): REC14 ROT011. |
| prereg | PREREG_069 (T2); prereg T1 Mech-S9; T2R Mech-S10 | PREREG_123, PREREG_125. Prawo relabelingu z §2 **nie** było preregistrowane. |
| wykonywalność | Tak: natywna Julia, Manifest autorów, 68 wywołań | Tak: łatka linii 80 (`code/std_a_123.jl`), 18 wywołań na zestaw mas |
| dane | `2026-11-16/data/` (t2_*.csv, analysis069.json); wyniki T2R Mech-S10; REVIEW_084 | `2026-11-23/data/run123/`, `run125/`, `posthoc127/` |
| poprawność | T1-GROUPED (Mech-S9 ROT030, dopuszczone przez Moderatora). T2: +0.272…+0.301 dex w 6 masach, W/ORD/TOL PASS (REVIEW_071). T2R: Mech-S10 natywnie 68/68 bitowo (REVIEW_080). Przeniesienie na sieć: D_net +0.26…+0.30 (REVIEW_084). | Δ(j22) = −1.384, Δ(j62) = −0.244 dex. Std ma pierwiastki j16–j21 (−17.58…−18.49), base nie ma żadnego (REVIEW_124). Wynik odporny na kontynuację q_h poniżej 1e9 g: s ∈ {−1.0, −1.3, −1.5} daje Δ(j22) −1.430…−1.340 (REVIEW_126, 3/3 PASS). |
| niepewność | Numeryczna: rozrzut metod ≤ 0.01 dex. Przesunięcie względne jest odporne. Progi bezwzględne nie są odporne: generator +0.33…+0.37, sieć −0.10…−0.59 (SYNTH_087). | Numeryczna: σ_root 0.001–0.021. Modelowa: STOP A (j16–j22 mają 0% liczby hadronów w oknie G_EC+(b) [2e9, 1e11] g, a 81–100% pochodzi z ekstrapolacji poniżej 1e9 g; REC14 ROT011); STOP B (trzy mapy Y_P); G_DEP otwarte; brak przeniesienia na sieć. |
| najbliższy dojrzały gospodarz | Reno–Seckel 1988, Tab. I (osobne frakcje π⁺ i π⁻); Bianco et al. 2026, arXiv:2605.26824 §4 (wydajność jednego stanu); rodowód KY 1999 / Kohri 2001 niejednoznaczny. T3: SEMANTICS_OPEN (LT9 ROT006; REC13 ROT005, AUD3 ROT003). | Page 1976; MacGibbon–Webber 1990; MacGibbon 1991; Cheek et al. 2022 (arXiv:2107.00013); BlackHawk; Baldes et al. 2020 (arXiv:2004.14773, dod. A: e_T = 7.6e−3 w geometrycznej optyce wobec ẽ_T = 4.3e−3 z greybody). Tekst autorów: Eq. 2.10 to geometryczna optyka; Eq. 4.3 zawiera czynnik greybody; Fig. 2 pokazuje stawki hadronów z BlackHawk. W dwóch wyszukiwaniach (23 XI) nie znalazłem publikacji o skutku tej niespójności dla granicy Wu–Xu. „Nie znalazłem” ≠ „nie istnieje”; potrzebny przegląd XH. |
| niezależne I1/I3 | T1: Mech-S9 (GPT). T2R: Mech-S10 (GPT), natywnie. Recenzje semantyki zakończone werdyktem OPEN. Brak INDEPENDENT REFEREE PASS dla interpretacji „podwójne liczenie”. | I1 wejść: fM (DAX ROT007), zegar (M16 ROT011), operand i R (REC14 ROT014), 11 surowych tablic PYTHIA (DAX-S10 ROT011). **Pierwiastki std liczyła tylko rodzina Claude:** brak natywnego I1 spoza rodziny i brak referee. |
| ważny null / kontrprzykład | T1-PERSTATE (nie wystąpił). Pozostały null: T3 wykazuje, że n_j w Eq. 4.7–4.8 to gęstości grupowe z ⟨σv⟩ uśrednionym po grupie, czyli kod jest spójny → B1-NEGATIVE. Kontrprzykłady fizyczne: f(t) ≠ ½ może odwrócić znak (SCOPE12 ROT007); zasilanie z kaonów leży poza przestrzenią stanów (INT10 ROT006). | (a) Replika spoza rodziny różni się o więcej niż 0.03 dex przy j16/j22/j62 → artefakt numeryczny. (b) Test relabelingu z §3 nie przechodzi → przesunięcie nie jest czystym efektem zegara. (c) Wykazanie, że q_h w kodzie jest znormalizowane w geometrycznej optyce, czyli zegar jest spójny → null. Punkt (c) jest dziś sprzeczny z Fig. 2 autorów i z G_EC+(b) (zgodność ok. 1% w oknie). |
| rzeczywista użyteczna nowa informacja | W kodzie istnieje konwencja czynnika 2 we wstrzyknięciu naładowanych hadronów, warta +0.27…+0.30 dex (β × 1.9–2.0) w 1.1–7.7e9 g i odporna na wybór sieci. Czy to błąd, zależy od semantyki, której opublikowane teksty nie rozstrzygają. | Zob. §2 (post hoc): krzywa std to krzywa base przy masie przeskalowanej o R^(−1/3) = 1.198, przesunięta o c·log₁₀R, c ∈ [0.9, 1.0]. W kodzie autorów oś masy kurczy się więc o czynnik 0.835, a β o R^(0.9–1). Lewa ściana (w naszym natywnym przebiegu między 1.08 a 1.12e9 g) przesuwa się do ok. 0.9e9 g, czyli poniżej nagłówkowego „must exceed 10⁹ g”. Twierdzenie jest MODEL_CONDITIONAL, obowiązuje w kodzie autorów. |
| szacowane wyjaśnienie alternatywne | Świadoma konwencja gęstości grupowych odziedziczona po KY 1999 / Kohri 2001 (z przekrojami grupowymi): wtedy błędu nie ma. Inna możliwość: fizyczne f(t) ≠ ½ sprawia, że E5 jest złą poprawką. | Świadome przybliżenie geometrycznej optyki, takie jak w głównym tekście Baldes 2020. Przybliżenie byłoby spójne, gdyby zegar i widma były liczone tak samo. Tu widma hadronów pochodzą z BlackHawk (greybody), a zegar z geometrycznej optyki, więc jest to niespójność, nie tylko przybliżenie. |
| produkt | Brief „Normalizacja stanów ładunkowych w publicznym kodzie Wu–Xu: zmierzony skutek i warunek semantyczny”. Wynik warunkowy, bez twierdzenia o błędzie. | Brief „Niespójność zegara i widm w publicznym kodzie Wu–Xu: odwzorowanie podobieństwa granicy BBN”, z prawem z §2, przesunięciami natywnymi i wynikiem testu z §3. Bez granicy bezwzględnej. |
| decyzja i uzasadnienie zatrzymania | Rekomendacja [▷]: sufit MATURE-APPLICATION. SOURCE PASS dotyczy faktu w kodzie, nie interpretacji. Referee PASS dla interpretacji jest nieosiągalny bez T3, a T3 bez kontaktu z autorami zostaje OPEN. **Eliminacja:** T3 lub referee orzeka spójność konwencji grupowej (null) albo bramka fizyczna (f(t), kaony) odbiera poprawce sens. Bez eliminacji 13 XII: B1-HOLD_SOURCE dla interpretacji i wkład odtwarzalnościowy dla pomiaru. | Rekomendacja [▷]: sufit MATURE-APPLICATION. Brakuje natywnego I1 spoza rodziny Claude i referee. Granica bezwzględna jest wykluczona (STOP A/B, G_DEP). **Eliminacja:** null (a) lub (b) z §3, publikacja tej samej poprawki dla Wu–Xu znaleziona przez XH, albo dowód (c). Bez weryfikacji do 13 XII: HOLD. Kalendarz nie podnosi etykiety. |

## 2. POSTHOC_127: STD_A jako przeskalowanie zegara (eksploracyjne, niepreregistrowane)

**Rachunek.** Std o masie M ma ten sam czas życia co base o masie M′ = M·R^(−1/3), więc historie m(t)/M₀ obu są identyczne.
- Przy β zadanym w chwili powstania (`main-scan.jl` l. 154–159: t_f(m), ρ_SM,f, n = βρ/M) mamy n/s ∝ β M^(−3/2).
- Przy q_h ∝ M^(−1.2) stawka wstrzyknięcia hadronów zrównuje się dla β_std = β_base · R^(1/2 + 1.2/3), czyli c = 0.9.
- Kanał energii tła daje c = 1/6. Konwencja β przy wspólnym T dałaby c = 0.733, ale kod jej nie stosuje.

**Test.** Pierwiastki base z REVIEW_071 (j22, 28, 38, 51, 62, 90; metoda M_D) zinterpolowałem PCHIP-em i liniowo, a następnie porównałem z pierwiastkami std z REVIEW_124. Kod: `code/scaling_posthoc_127.py` (sha256 5f1f25fe…). Wynik: `data/posthoc127/scaling_posthoc_127.json` (sha256 f0fa28f1…).
- Węzły pewne interpolacyjnie: j22 trafia na j28.35, j62 na j68.35.
  - c = 1.0: reszty +0.022 / −0.006 (PCHIP), +0.010 / −0.012 (liniowo).
  - c = 0.9: −0.001 / −0.030 (PCHIP).
  - c = 0.733: −0.040 / −0.069.
  - c = 1/6: −0.17 / −0.20.
  - Kanał samej energii tła i konwencja wspólnego T są więc wykluczone przy j62.
- Ściana j16–j21: reszty PCHIP −0.10…+0.03 przy c ∈ [0.9, 1]. Interpolacja między j22 a j28 przez stromą ścianę jest tu ograniczeniem, nie testem.

**Status.** Dwa pewne punkty, dopasowanie post hoc, wyprowadzenie c = 0.9 zależy od jednego wykładnika q_h. To hipoteza [▷], nie wynik. Jej wartość polega na tym, że daje ostre przewidywanie bez interpolacji (§3).

## 3. Proponowany dyskryminator (wymaga autoryzacji Moderatora; nic nie uruchomiono)

**Wykonawca.** Mech-S10 (GPT, środowisko Julii z T2R), zakres PREREG_123 bez zmian: zegar `N_BH × 0.5817518` w linii 80, tolerancja domyślna, ten sam kontrakt Y_code = 0.251.

**Część A, replika natywna.** Base i std dla j16, j22, j62.
- PASS, gdy |Δ_rep − Δ_Badacz| ≤ 0.03 dex przy j22 i j62, a std przy j16 ma pierwiastek w siatce [−21, −16].

**Część B, test relabelingu ślepy wobec wykonawcy.** Std w masach M = M_node·R^(1/3) dla węzłów base REVIEW_071. Przedziały zawierają c ∈ [0.9, 1.0] ± 0.03 i zamrażam je tym commitem:
- 1.474765e9 g (węzeł j38, base −19.0085): **[−19.274, −19.190]**
- 2.133869e9 g (węzeł j51, base −19.3002): **[−19.566, −19.482]**
- 6.464011e9 g (węzeł j90, base −19.3669): **[−19.632, −19.549]**
- PASS przy 3/3. Wynik 0/3 albo 1/3 falsyfikuje prawo z §2. Wynik 2/3 oznacza HOLD.

**Koszt.** 6 wyznaczeń pierwiastka w części A i 3 w części B. Dla porównania 18 wyznaczeń w run125 zajęło ok. 12 min na 2 rdzeniach.

**Ograniczenia.** To weryfikacja istniejącego twierdzenia, a nie nowy eksperyment. LT10 ROT018 wstrzymał nowe eksperymenty natywne, a §E protokołu wymaga zgody Moderatora na każdy przebieg Julii. Badacz nie uruchamia niczego bez tej zgody. Wymagany jest też referee spoza Claude (REC14 lub AUD3) dla zakresu „niespójność zegara i widm, odwzorowanie w kodzie autorów”.

**Równolegle, bez obliczeń (XH):** przegląd literatury pod kątem komentarza, erraty lub pracy, która stosuje do Wu–Xu zegar z greybody (zapytania: „Wu Xu 2509.05618 lifetime greybody”, „geometric optics PBH lifetime BBN bound correction”).

## 4. Uczenie systemu

- **origin_failure_mode:** `GOVERNING_LAYER_NOT_READ` (RUNLOG `401bb3f`). Przez kilka rotacji produkowałem kontrole STD_A bez odniesienia do §F i do pytania LT10 o zewnętrzny punkt końcowy, więc liczba raportów rosła, a stan decyzji nie.
- **Reguła:** każdy raport B1 zaczyna się od pola §F, które zmienia; raport bez takiego pola nie powstaje.
- **Pruning:** wstrzymuję dalsze kontrole progów bezwzględnych STD_A (STOP A/B, G_DEP), dopóki nie rozstrzygnie się kwestia z §3. Nie zmieniają one sufitu etykiety.

NO_PBH_BOUND / NO_PAPER_ERROR_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
