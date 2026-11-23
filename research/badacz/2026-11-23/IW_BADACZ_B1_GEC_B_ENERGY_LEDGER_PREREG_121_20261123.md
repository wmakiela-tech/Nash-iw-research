---
artifact_id: IW_BADACZ_B1_GEC_B_ENERGY_LEDGER_PREREG_121_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel G_EC+ i przebiegów natywnych B1
created_at: 2026-11-23
document_type: PREREGISTRATION (zamrożona przed obliczeniem)
authorization: Moderator 23 XI 09:22 („Najpierw A”: G_EC+(b) przed STD_A), rotacja „O” 10:42; stała autoryzacja 21 XI 16:05
answers: REC14 ROT002 (G_EC+), REC14 ROT009 (pokrycie mas), M16 ROT011/ROT014 (rejestr energii hadronów), EKS1 ROT027
claim_ceiling: NUMERYCZNY [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_121: G_EC+(b), rejestr energii tablic hadronizacji BlackHawk i tablicy hadronowej Wu–Xu

## 1. Cel

G_EC+(a) (REVIEW_120, I1: DAX ROT007, M16 ROT011) ustaliło dwie rzeczy. Kod traci masę 1.719× szybciej niż BlackHawk. Widma pierwotne 090 niosą moc BlackHawk do 1.2% w 2e9–1e11 g.

Otwarte jest, czy tablica hadronowa autorów (liczby hadronów na PBH i sekundę) jest energetycznie spójna z tą emisją (REC14 ROT002, M16 ROT014). Sprawdzam to na dwóch poziomach.

**T (tablice).** Dla każdej cząstki pierwotnej i i energii E′ liczę ułamek energii unoszonej przez 11 tabelowanych cząstek wtórnych:
ε_all,i(E′) = Σ_j Σ_k Ē_k N_jki(E′)/E′.
- N to liczba na jedną cząstkę pierwotną w przedziale [E_k, E_k+1], zgodnie z konwencją `secondary.c` l. 138.
- Ē_k = (E_k+1 − E_k)/ln(E_k+1/E_k). Nawiasy błędu to krawędzie przedziału.
- Liczę to dla tablic PYTHIA (wybór autorów, `hadronization_choice = 0`) i HERWIG (sprawdzian T1 przez energię).

**M (masy).** Splatam widma pierwotne 090 z tablicami PYTHIA. Otrzymuję:
- liczbę hadronów N_h(M), porównywaną z tablicą autorów (`hadrons_from_PBH.dat`, d395183);
- moc wtórną P_sec(M), porównywaną z pełną mocą pierwotną. Neutrina i grawiton przechodzą bez hadronizacji.

## 2. Ujawnienie wiedzy przed zamrożeniem

- Konwencję energii końcowej sprawdziłem na formacie: najniższy niezerowy przedział protonów zawiera m_p, a pionów m_π. Energie są więc całkowite, bez dodawania masy spoczynkowej.
- W tablicy HERWIG przy E′ = 1e5 GeV najwyższa niezerowa energia protonu to 46416 GeV, czyli < E′/2. W PYTHIA wynosi 90347 GeV. To jest zgodne z T1 (√s = E′, dżet E′/2) i czyni P_T2 częściowo przewidywalnym; P_T2 testuje sumę energii, a nie maksimum.
- Znane: BIN_PY = 1.0258 (T2, NOTE_114 r4) oraz P_spec/P_fM = 0.988 (REVIEW_120).
- Kod sprawdziłem na atrapie (`code/dummy_121.py`); przeszedł mechanicznie.

## 3. Bramki i predykcje (`code/gec_b_121.py`, progi w skrypcie)

**G_NUM (bramka interpretacyjna).** Tablica autorów × BIN_PY / moja liczba ze splotu ma być w ±3% dla 5 gatunków i mas 2e9–1e11 g. Masy muszą się zgadzać do 1e-4.
Uzasadnienie: autorzy całkują gęstość z dolnej krawędzi trapezem w ln E (T2), co daje wynik niższy o BIN. Moje N sumuje liczby w przedziałach.
Przy FAIL część M nie dotyczy tablicy autorów, tylko mojej rekonstrukcji.

**Predykcje:**

| id | wielkość | pasmo | podstawa |
|---|---|---|---|
| P_T1 | ε_all PYTHIA dla 14 pierwotnych; E′ ≥ 50 GeV (W, Z, H: ≥ 200; top: ≥ 400) | [0.90, 1.05] | zachowanie energii; brak podwójnego liczenia |
| P_T2 | ε_all HERWIG dla kwarków u, d, c, s, b i gluonów, E′ ≥ 100 GeV | [0.45, 0.55] | T1: zdarzenie przy √s = E′, liczby na pierwotną = liczby na zdarzenie / 2 |
| P_M1 | r_all(M) = P_sec/P_spec dla mas 2e9–1e11 g | [0.90, 1.05] | spójność rejestru na poziomie mas |

Raportowane bez progu:
- ε_had(E′), czyli udział 5 hadronów BBN w energii pierwotnej;
- r_had(M) = P_had/P_fM;
- liczba hadronów na GeV wyemitowanej energii n_E(M), moja i autorów;
- nachylenie d ln q_h/d ln M z wierszy 0–1 tablicy autorów, które wyznacza ekstrapolację poniżej 1e9 g.

## 4. Interpretacja (ustalona przed obliczeniem)

- **P_T1, G_NUM i P_M1 PASS.** Przy ustalonej masie tablica autorów jest energetycznie spójna ze standardową emisją BlackHawk, z dokładnością do T2 (−2.6%) i obcięcia siatki E′ przy 1e5 GeV.
  - Razem z G_EC+(a) oznacza to, że w obszarze tabelowanym kod daje na jedną PBH 0.582 liczby hadronów zgodnej z bilansem energii.
  - G_EC+(b) zamyka się wtedy dla 2e9–1e11 g.
  - Poniżej 1e9 g, gdzie przy j22 przypada 81% liczby hadronów (M16 ROT014), tablic brak. Spójności energii ekstrapolacji nie da się z nich sprawdzić; raportuję tylko n_E i nachylenie.
- **P_T1 FAIL.** Tablica PYTHIA nie zachowuje energii; raportuję, które kanały i energie.
- **P_T2 PASS.** Niezależne, energetyczne potwierdzenie T1 (DIR-009). **FAIL przy ε ≈ 1:** moje odczytanie normalizacji „na pierwotną” w HERWIG jest błędne i T1 wymaga rewizji.
- Nic tutaj nie daje granicy na β. G_DEP (M16 ROT011: ile wyemitowanej mocy osadza się w płynie ρ_SM) pozostaje osobną bramką.

## 5. Wejścia

- Tablice BlackHawk v2.3 `pythia_tables`, `herwig_tables` (SHA w wyniku).
- `primary_spectra_090.tsv.gz` (692bbeca…).
- `hadrons_from_PBH.dat` autorów (d395183).
- `fM.txt` (5baaac37…).
- `data/run119/fcode_119.csv` (przelicznik GeV/g).
