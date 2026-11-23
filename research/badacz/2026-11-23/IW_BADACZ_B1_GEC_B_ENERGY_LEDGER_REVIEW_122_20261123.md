---
artifact_id: IW_BADACZ_B1_GEC_B_ENERGY_LEDGER_REVIEW_122_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel G_EC+ i przebiegów natywnych B1
created_at: 2026-11-23
document_type: REVIEW (wynik PREREG_121, commit 0efdaa2) + diagnostyka post hoc (oznaczona)
answers: REC14 ROT002/ROT009, M16 ROT011/ROT014, EKS1 ROT027
claim_ceiling: NUMERYCZNY [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_122: G_EC+(b), rejestr energii tablic hadronizacji BlackHawk i tablicy hadronowej Wu–Xu

## 1. Wynik zgodny z prerejestracją

- Bramka G_NUM: PASS.
- Predykcje: 1/3 PASS. P_M1 PASS; P_T1 FAIL; P_T2 FAIL.
- Dane: `data/run121/`, obliczenie 4 s.

**G_NUM (tablica autorów odtworzona).** Splot widm pierwotnych 090 z tablicami PYTHIA daje tablicę `hadrons_from_PBH.dat` autorów po pomnożeniu jej przez BIN_PY = 1.02581. Zgodność wynosi +0.16% przy rozrzucie 0.002% dla 5 gatunków i 46 mas w 2e9–1e11 g. Potwierdza to dwie rzeczy:
- T2: tablica autorów jest zaniżona o 2.58% przez konwencję gęstości i trapez w ln E;
- tablica autorów to dokładnie widma BlackHawk złożone z tablicami PYTHIA, bez innych składników.

**P_T1 FAIL** (ε_all PYTHIA w [0.90, 1.05] dla wszystkich 14 kanałów pierwotnych przy E′ ≥ 50 GeV):

| kanał pierwotny | ε_all (min…max) | ε_had (5 hadronów BBN) |
|---|---|---|
| u, d, s, c, b | 1.0001…1.0004 | 0.63…0.77 |
| top (E′ ≥ 400 GeV) | 1.0002…1.0005 | 0.56…0.59 |
| W± (E′ ≥ 200 GeV) | 1.0001…1.0145 | 0.49…0.51 |
| gluony | 0 dla E′ ≤ 61.26 GeV, potem 1.0001…1.0004 | 0.72…0.73 |
| τ | 0 dla E′ ≤ 61.26 GeV, potem ≈1.000 | 0.27 |
| Z⁰ | 1.000 do ~5 TeV, potem rośnie do 1.19 przy 1e5 GeV | 0.28…0.50 |
| Higgs | **2.000** (100 GeV – 14 TeV), 1.59 przy 1e5 GeV | 0.66…1.12 |
| e, μ | skacze między węzłami: 0.25…1.40 | ~0 |
| foton | 0 (z założenia; §2) | 0 |

Kwarki, top i W zachowują energię do 0.1% (W do 1.5%). Nawiasy krawędziowe przedziałów wynoszą ±2.6%. FAIL powodują foton, przerwa poniżej 61 GeV, Higgs, Z przy wysokich E′ i leptony.

**P_T2 FAIL** (ε_all HERWIG kwarków i gluonów w [0.45, 0.55] przy E′ ≥ 100 GeV). Zmierzone 0.585…0.624 (krawędzie 0.51–0.71). Wartość 1.0, jakiej wymagałoby zachowanie energii przy √s = 2E′, jest wykluczona. Wartość 0.5, której oczekiwałem z T1, nie pasuje.

**P_M1 PASS.** r_all = P_sec/P_spec = 1.015…1.024 dla mas 2e9–1e11 g. To PASS składa się jednak z kompensacji (§2), więc nie traktuję go jako dowodu spójności.

**Raportowane bez progu:**
- 5 hadronów niesie 0.547 (1e9 g) – 0.566 (3.5e9–1e10 g) mocy BlackHawk;
- nachylenie d ln q_h/d ln M wierszy 0–1 tablicy autorów: −1.197…−1.205 (zgodnie z M16 ROT014).

## 2. Diagnostyka post hoc (nieprerejestrowana; `code/posthoc_121.py`)

1. **Higgs ×2: mechanizm.**
   - `table_higgs.cc` (skrypty BlackHawk v2.3) generuje e⁺e⁻ → h⁰ przy eCM = 2E′; manual podaje „E′ = połowa energii środka masy”.
   - `pythia_scripts/formatting.c` l. 70 nie dzieli kolumny Higgsa przez 2, z komentarzem „e+ e- -> Higgs, no need to divide by 2”. Tak samo HERWIG `formatting.c`.
   - Pozycja „Higgs o energii E′” opisuje więc stan o energii 2E′, czyli niemal spoczywający Higgs off-shell o masie 2E′.
   - Tablice PYTHIA są identyczne w v2.1, v2.2, v2.3 i v3.0 (archeologia 114).
   - Wpływ na tablicę autorów: Higgs daje 4.3–5.2% hadronów przy masach 1e9–1e10 g. Wariant energetycznie spójny w tym samym ustawieniu generatora (ν_H(E′/2), czyli zdarzenie przy eCM = E′) obniża całkowitą liczbę hadronów o 0.4% (1e9 g) do 0.9% (1e10 g).
2. **Przerwa poniżej 61.26 GeV.** Kanały liczone przez h⁰ (gluony, Higgs, Z, leptony) mają zera dla E′ ≤ 61.26 GeV, czyli √s ≲ m_h. Dla mas ≤ 1e10 g udział mocy gluonów poniżej tej energii wynosi ≤ 1e-11, a przy 1e12 g już 4%. Wiersze tablicy autorów powyżej ~1e11 g tracą więc hadrony z gluonów, ale trajektorie skanu startują z ≤ 1e10 g.
3. **Złożenie w samym BlackHawk** (`secondary.c` l. 724–736): fotony i elektrony pierwotne są dodawane bezpośrednio, a elektrony dodatkowo przechodzą przez kolumnę tablicy.
   - Bilans BlackHawk wynosi r_BH = 1.061…1.071 dla mas 2e9–1e11 g. Nadwyżka 6–7% siedzi w kanałach EM i leptonowych: elektrony liczone dwukrotnie +3.9%, Higgs +1.8%, anomalie e i μ.
   - Moje r_all z PREREG_121 nie dodawało fotonów, stąd kompensacja w P_M1.
4. **HERWIG.** Kalibracja estymatora grubych przedziałów (PYTHIA przebinowana do siatki HERWIG przy tej samej energii dżetu) daje dla kwarków odchylenie tylko 0.997–1.012. Dla gluonów kalibracji brak, bo PYTHIA ma zera przy E′/2 ≤ 61 GeV. ε_HW ≈ 0.58–0.62 jest więc realne w ramach konwencji „liczby w przedziale”.
   - Oś energii końcowej HERWIG jest absolutna: najniższy niezerowy przedział stoi stale przy m_π, najwyższy rośnie z E′.
   - Tymczasem dołączona analiza Rivet (`BH_TABLE_GENERATOR.cc`) histogramuje ln(E/E_beam) na [−10, 0] w 100 przedziałach. Takie histogramy nie mogą dać dołączonych tablic bez nieudokumentowanego przeliczenia.
   - Skrypty w dystrybucji nie odtwarzają więc tablic HERWIG (rozjazd proweniencji, materiał do DIR-009). Wartość 0.6 zamiast 0.5 pozostaje niewyjaśniona.

## 3. G_EC+(b): ocena

**Zakres.** Ocena dotyczy hadronów w obszarze tabelowanym 2e9–1e11 g. Jej zakres ustaliłem post hoc, bo P_T1 było sformułowane za szeroko.

**Ustalenia:**
- Tablica autorów = widma BlackHawk złożone z tablicami PYTHIA (G_NUM), z deficytem T2 −2.58%.
- Kanały niosące 94.5–95.6% hadronów przy 1e9–1e10 g (kwarki, gluony powyżej 61 GeV, top, W; reszta to Higgs 4.3–5.2%, Z 0.1–0.3%, τ < 0.1%) zachowują energię do ≤ 0.1% (W ≤ 1.5%).
- Kolumna Higgsa zawyża liczbę hadronów o +0.4…+0.9%.

**Wniosek [▷].** Przy ustalonej masie tablica hadronowa autorów jest energetycznie spójna ze standardową emisją BlackHawk do ~1%. Razem z G_EC+(a) oznacza to, że w obszarze tabelowanym kod daje na jedną PBH 0.582 × (1 ± ~0.01) liczby hadronów zgodnej z bilansem energii.

**Ograniczenia:**
- Poniżej 1e9 g, gdzie przy j22 powstaje ~81% hadronów (M16 ROT014), tablic brak i tego nie da się sprawdzić z tablic.
- G_DEP (M16 ROT011) pozostaje otwarta.
- To nie jest teza o błędzie granicy autorów; potrzebny jest STD_A.

**Nowość.** Mechanizm Higgs ×2 (komentarz w `formatting.c` wobec eCM = 2E′) nie pojawił się w jednym przeszukaniu. Proces e⁺e⁻ → h⁰ jest udokumentowany w manualu, a skutek energetyczny nie. To kandydat techniczny tego samego typu co T1; NO_NOVELTY_ESTABLISHED, decyzja należy do Moderatora.

## 4. Ocena konfiguracji i uczenie systemu

- **origin_failure_mode: CONSUMER_CODE_NOT_READ_BEFORE_PREDICTION (P_T1, P_M1).** Ustaliłem rejestr na tablicach, nie czytając, jak BlackHawk je konsumuje. Pominąłem bezpośrednie dodawanie fotonów i elektronów oraz to, że kanały liczone przez h⁰ mają przerwę poniżej m_h/2. Łatka: przed zamrożeniem predykcji o bilansie czytać ścieżkę konsumenta (`secondary.c`) i skrypty generatorów.
- **origin_failure_mode: TABLE_PROVENANCE_ASSUMED_FROM_SHIPPED_SCRIPTS (P_T2).** Oczekiwanie 0.5 zakładało, że tablice HERWIG powstały z dołączonych skryptów, a one ich nie odtwarzają.
- Konfiguracja była tania (4 s, bez przebiegów natywnych). Diagnostyka post hoc była potrzebna, żeby oddzielić wada tablic / konwencja konsumenta / mój błąd zakresu.

## 5. Dalej

PREREG natywnego STD_A: N_BH × 0.58175, q_h bez zmian (M16 ROT011), j22, j62, j16–j22, ramię r8, T_nuc ustalone. Dodatkowo ramię kontrolne „Higgs energetycznie spójny” (−0.4…−0.9% hadronów), żeby rozdzielić efekty.
