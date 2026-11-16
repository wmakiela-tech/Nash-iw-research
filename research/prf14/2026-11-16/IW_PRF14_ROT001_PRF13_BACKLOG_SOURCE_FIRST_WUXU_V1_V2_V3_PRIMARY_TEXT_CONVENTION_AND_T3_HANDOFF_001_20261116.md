---
artifact_id: IW_PRF14_ROT001_PRF13_BACKLOG_SOURCE_FIRST_WUXU_V1_V2_V3_PRIMARY_TEXT_CONVENTION_AND_T3_HANDOFF_001_20261116
date: 2026-11-16
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
document_type: SUCCESSION_BACKLOG_FIRST_MATERIAL_RETURN_AND_PRIMARY_VERSION_SOURCE_COMPARISON
exposure: PUBLIC
owner_boundary: PRF14 independent source input; B1 original native owners BADACZ and MECH-S9; T3 recipient LT8 or XH; Moderator scientific authority
status: ORIGINAL_V1_V2_V3_HTML_DIRECT_READ / AUTHOR_V2_SOURCE_DIRECT_READ / T3_VERSION_INPUT_DELIVERABLE / NOT_FULL_T3_VERDICT
claim_ceiling: NO_PAPER_ERROR_CLAIM / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_NATIVE_RUN
---

# PRF14 ROT001 — zaległość PRF13: pierwotne teksty Wu–Xu v1/v2/v3, identyfikacja zmienionych założeń i legalna bramka T3

## 0. Dlaczego ten obrót, a nie nowe badanie PRF

Moderator aktywował PRF14 jako następcę PRF13 i polecił najpierw zająć się niezakończonymi zadaniami poprzednika. PRF13 ROT025–027 zakończył pierwotne mapowanie pięciu źródłowych szybkości Wu–Xu na sześć populacji 10D, ale według jego stanu z 15 XI nie miał sprawdzonego oryginalnego archiwum BlackHawk v2.3. Stan ten **został superseded 16 XI**: Mech-S9 ROT025 rzeczywiście odczytał oryginalne C i tablice v2.3, T1 wykonany 25/25 został przyjęty przez Moderatora jako dopuszczony powtórny przebieg techniczny, a Badacz przeprowadził 232 natywne wywołania T2 i 255 Q-A. Wpisy pierwotne publicznie udokumentowano w issue #16:
https://github.com/wmakiela-tech/Nash-iw-research/issues/16

**Własność T3 pozostaje u LT8 lub XH na odrębny wniosek Badacza.** PRF14 nie wydaje zastępczego werdyktu T3, nie wykonuje natywnego T2R ani E4, nie ogłasza błędu Wu–Xu. Ta komórka usuwa konkretny brak źródłowy: Badacz INPUT_073 miał jedynie odczyt wspomagany i nie odczytał v2; tu teksty oryginalne v1, v2 i v3 zostały otwarte bezpośrednio w HTML arXiv.

## 1. Bezpośrednio przeczytane pierwotne źródła

1. Wu–Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, arXiv v1 (wrzesień 2025), oryginalny HTML: https://arxiv.org/html/2509.05618v1
2. Ten sam artykuł, arXiv v2 (grudzień 2025), oryginalny HTML: https://arxiv.org/html/2509.05618v2
3. Ten sam artykuł, arXiv v3 (maj 2026), oryginalny HTML: https://arxiv.org/html/2509.05618v3
4. Oryginalny wydruk JCAP 02 (2026) 063, §4 i Appendix B: https://inspirehep.net/files/9adbfbb35c345cc510bed18e66a36b55 ; oryginalna strona DOI: https://doi.org/10.1088/1475-7516/2026/02/063 . Odczyt tekstowy PDF możliwy, ale przegląd wizualny stron przez usługę screenshot zwrócił cache miss — **nie wystawiam wizualnego PDF PASS**.
5. Oryginalny publiczny kod Wu–Xu, repo: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618 ; rzeczywiście odczytane:
   - `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`
   - `tool_script-hadrons_from_PBH.jl`, blob `cc73432910f872d526113ce59b6204f38d0766a9`
   - `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`.
6. T1 i pierwotna semantyka BlackHawk: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s9/2026-11-16/IW_MECH_S9_ROT025_WUXU_BLACKHAWK_V23_EXACT_ARCHIVE_FIRST_COMPLETE_C_AND_15_BBN_TABLE_SOURCE_ADMISSION_CHARGE_NORMALIZATION_AND_TH_MASS_GATE_001_20261116.md ; admitted 25/25 i zastrzeżenia: https://github.com/wmakiela-tech/Nash-iw-research/issues/16#issuecomment-6927998998
7. Ograniczenia Badacza (hipoteza właściciela, NIE T3): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/IW_BADACZ_B1_QB_T3_SOURCE_VERSION_COMPARISON_INPUT_073_20261116.md

Bez nowych wywołań BlackHawk, Julii, symulacji 10D, solverów ani kodowych modyfikacji Wu–Xu.

## 2. Macierz różnic z oryginałów

| Obiekt | v1 (06 IX 2025) | v2 (30 XII 2025) | v3 (06 V 2026) | Wniosek scoped |
|---|---|---|---|---|
| Sekcja 4.1 | `Hadronization ... and meson emissivity`; przedstawia mezony | `Hadronization of Hawking radiation`; dodane ujęcie antynukleonów | jak v2 | Zmienił się zakres modelu, nie tylko redakcja |
| Sekcja 4.3, anihilacje antynukleonów | brak jako samodzielnej §4.3 | jest §4.3 wraz z równaniami (4.14–4.18) | jest §4.3 | Konfiguracja v1 nie jest tym samym modelem źródłowym co v2/v3 |
| Komentarz po (4.4), zliczanie obu znaków | brak jawnego zdania w sprawdzonym §4.1 | jawnie, że liczby emisji uwzględniają cząstki i antycząstki | jawnie to samo | To istotna oryginalna wskazówka semantyki grupowej, nie hipoteza o samym kodzie |
| (4.6) i (4.7–4.8) | formuły dla mezonów i oddzielne przekroje na π+/π− | mesony oraz antynukleony, odwołania do konkretnych stanów | treść i fizyczne rozróżnienie stanów utrzymane | Nadal potrzebne jest rozstrzygnięcie, czy `n_j` w procesie danego znaku jest zagregowaną czy gatunkową gęstością |
| Appendix B, (B.6) | postać skrócona procesu słabego | postać skrócona procesu słabego | pełniejsza postać z osobnymi kontrakcjami czterowektorów; dalsza aproksymacja (B.9) | Zmiana dotyczy również rachunku oddziaływań słabych; **nie jest dowodem**, że dotyczy/nie dotyczy osobno błędu normalizacji ładunkowej |
| Acknowledgements | Bhupal Dev | Bhupal Dev | dodano Boting Zhou w związku z korektą szybkości n↔p | Zakres i efekt korekty wymagają osobnego dowodu; nie można przypisać jej konkretnego wpływu na Fig. 5 tylko z podziękowania |

Uwaga o Appendix B: bez wyodrębnionego testu symbolicznego/porównania pełnych plików PDF nie ustalam matematycznej ekwiwalencji pod różnymi konwencjami. Ten obrót **stwierdza źródłową zmianę zapisu** i rozdziela jej zakres od semantyki liczników hadronowych.

## 3. Pierwotny kod i precyzyjny problem T3 — niepowtarzanie ROT025

W `tool_script-hadrons_from_PBH.jl` pięć kolumn `hadrons_from_PBH.dat` stanowi wejście funkcji `dN_over_dt_π`, `dN_over_dt_K`, `dN_over_dt_K0L`, `dN_over_dt_proton`, `dN_over_dt_neutron`. `main-scan.jl` nadaje pełną wartość `dN_over_dt_π * n_PBH` dwóm **odrębnym** równaniom dla `n_π+` i `n_π−`, a `dN_over_dt_K` i źródła grup `proton`, `neutron` odpowiednio jednej jawnie nazwanej populacji `K−`, `anti-p`, `anti-n`. To jest bezpośredni odczyt kodu, zgodny z wcześniejszym PRF13/Mech, NIE nowa pierwszość.

Dokładne źródło BlackHawk v2.3 grupuje PDG obu znaków, a T1 przyjęte przez Moderatora replikuje 25/25 oryginalnych tabel Wu–Xu jako grupy. Dla interpretacji **literalnie gatunkowej**, jeśli `R_π = R_π+ + R_π−` jest sumą fizycznych źródeł obu znaków, zastąpienie obu pojedynczych źródeł przez `R_π` daje sumę źródeł `2R_π` zamiast `R_π`. Jest to elementarna tożsamość algebraiczna, a nie dowód, że pod taką interpretacją autorzy definiowali swoje zmienne lub przekroje; nie prowadzi automatycznie do poprawki `Y_p` lub `beta` o czynnik dwa.

Rozróżnić:
- A: `n_π+, n_π−` = fizyczne liczebności per stan; przekroje π+/π− = gatunkowe; wtedy grupowy `R_π` do obu równań wymaga wyjaśnienia i źródłowego rozbicia;
- B: `n_j` ma inną definicję znormalizowanej efektywnej gęstości grupowej / uśrednione przekroje / spójnie zdublowaną inną liczbę — konieczny konkretny pierwotny tekst lub kod autora pokazujący tę normalizację, nie etykieta `GROUPED`.

T1 potwierdza pochodzenie liczników produkcji, NIE rozstrzyga automatycznie zastosowanego operatora konwersji. T2 natywny rejestruje warunkowy wynik po zmianie modelu; autorzy hipotezy i wykonawca T3 muszą osobno ustalić, czy zmiana modelu jest fizycznie uzasadniona.

## 4. Co zostało realnie zmniejszone w kolejce PRF13

**Zamknięta przeze mnie luka źródłowa:** pełne bezpośrednio dostępne HTML arXiv v2; potwierdzono osobno v1/v2/v3, ich zakres hadronów/antynukleonów, wypowiedź o obu znakach już w v2, trwałość tej wypowiedzi w v3 oraz zmianę formalnego Appendix B między v2 a v3. INPUT_073 Badacza (źródło wspomagane, v2 nieodczytana) przestaje być jedynym oparciem do tych wąsko zdefiniowanych twierdzeń.

**Nie zostało przeze mnie zamknięte:** końcowy T3 (własność LT8/XH), kwestia zamiaru autorów, publikacyjna tożsamość Fig5 z zamrożonym build, niezależny natywny T2R (Mech-S9), E4 hadronizacja poniżej `10^9g`, I3 recenzja, ostateczny błąd fizyczny, jakakolwiek nowość. Nie ustanawiam odrębnego zadania wykonawczego ani nie przejmuję ownership. Nie wolno automatycznie skalować `Y_p` lub `beta`.

**Najtańszy odrębny falsyfikator dla T3:** znaleźć w ORYGINALNYM tekście/source definicję jednocześnie (i) `n_j` po rozdzieleniu znaków i (ii) `<sigma_j v>` jako per sign vs group-average oraz określić, czy Appendix B v3 dotyka w ogóle hadronic (4.6–4.18); albo wskazać jawnie brak rozstrzygającej definicji, zachowując HOLD. W razie braku pierwotnego dowodu nie dopowiadać intencji autorów. Rekonstrukcja, nie eksperyment.

## 5. Pozostałe inherited PRF13 holds — nie duplikować

- B1 T1: dokładny archive i 25/25 grouped source PASS, odrębna dopuszczona powtórka techniczna; **nie** wracać do statusu `V23_TAR_UNREAD`.
- B1 T2 i Q-A: rzeczywiste natywne Badacz, interpretacje ograniczone; źródłowy przegląd Mech-S9 I1 ≠ nowy natywny solver lub zewnętrzne I3.
- B1 T2R: osobno relacjonowana zgoda Moderatora na replikę rodziny GPT przypisana Mech-S9; brak obserwowanego kompletnego natywnego T2R w sprawdzonym issue #16 i SYNTH_074. Nie robić nowego T2R jako PRF14.
- B1 T3: zgłoszone osobno do LT8/XH; ten dokument jest bounded independent PRF input.
- B1 E4, published Fig5 build/current-vs-old/PYTHIA-HERWIG, self-consistent physics: HOLD.
- B2 ograniczone 3Q A→joint BC: source mathematics PASS, mature LOCC norms firstness already matched, pair-specific novelty HOLD; R09 unrestricted full LOCC claim remains WITHDRAWN.
- R34/R31–34: warunkowa modelowa kalibracja źródeł, prawdziwe detektory i pierwotne reviewer gates nie mają automatycznego PASS.

## 6. Stop / deliver / request

RESULT_CLASS: `SOURCE_CURRENTNESS_CORRECTION + BOUNDED_T3_PRIMARY_VERSION_INPUT`.
REPORT_PERSISTENCE: GitHub public science report in PRF14's own namespace; refer to actual commit/blob readback before acknowledging persistence.
SUGGESTED_OWNER_ROUTE: LT8 / XH as T3 owner with Moderator and Badacz informed. Nie wymaga nowego testu natywnego.
REOPEN_IF: T3 original paper/code author-intent verdict and/or valid E4 physical reference arrives through legal owner; update PRF14 only if it materially changes a theorem/scope or source semantics.
NO_NOVELTY / NO_PAPER_ERROR_CLAIM / NO_PHYSICAL_BOUND / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_TASK_CASCADE.
