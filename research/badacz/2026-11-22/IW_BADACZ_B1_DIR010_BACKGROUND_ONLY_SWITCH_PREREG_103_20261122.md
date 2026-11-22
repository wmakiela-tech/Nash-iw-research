---
artifact_id: IW_BADACZ_B1_DIR010_BACKGROUND_ONLY_SWITCH_PREREG_103_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel natywny B1; odpowiedź na XH-S8 ROT001 (DIR-010: „decyzja o jednym przełączeniu natywnym należy do Badacza i Moderatora”)
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegiem natywnym)
authorization: obrót „O” Moderatora 22 XI 17:09 (praca z funkcji właściciela natywnego B1); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelu Wu–Xu [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_103: jedno przełączenie natywne dla DIR-010: tło bez hadronów w modelu Wu–Xu

## 1. Dyspozycja wobec XH-S8 ROT001 (DIR-010)

**Pytanie EKS1** (ROT016): skąd biorą się różnice 0.5–2.2 dex między krzywymi Wu–Xu a Kohri i Keith przy M ≈ 1.1–3.5e9 g?

**Ustalenia XH-S8:**
- Kohri, Keith, Wu–Xu i Wang używają różnych estymatorów.
- Podmiana operatora źródła na zamiennik Kohri lub Keith bez autentycznego adaptera źródłowego to TYPE_TRANSFER_HOLD.

**Decyzja Badacza:**
- Takiego adaptera nie buduję, bo nie byłby replikacją natywną.
- Wykonuję jedno przełączenie, które jest natywne i rozdziela pierwszą oś: tło i parowanie PBH (gęstość energii, entropia, rozszerzanie) wobec hadronowego n↔p.
- Wang i in. 2025/2026 pomijają hadrony i dostają efekty Y_p wyłącznie z tła. Jeśli tło w Wu–Xu działa dopiero przy β o rzędy wielkości większym niż progi hadronowe, to różnice 0.5–2.2 dex między pracami muszą pochodzić z sektora hadronowego (wydajności, przekroje n↔p, profil czasowy) albo z progów obserwacyjnych, a nie z tła.

## 2. Przebiegi (`run103.sh`, kod natywny bez zmian)

| ramię | tablica | zakres |
|---|---|---|
| z | tablica hadronów autorów × 1e−12 (`table_scale_085.py`); wstrzykiwanie hadronowe praktycznie wyłączone, tło PBH bez zmian | j22 i j62, log β od −20 do −13 co 0.25, plus baza; 60 przebiegów |
| k | tablica autorów bez zmian, węzeł 22 −17.20 | kontrola: musi być bitowo równa 083 o22_1720 |

Tylko model kodu Wu–Xu. Ramię sieciowe przenosi wyłącznie szybkości hadronowe, więc tu nic nie mówi. Czas: ~15 min.

## 3. Analiza (`analysis_103.py`, sprawdzona na atrapie)

**Bramki:**

| bramka | warunek |
|---|---|
| G_COMPLETE | komplet identyfikatorów |
| G_RUN | n_points ≥ 20000, i_last_alive > 200 |
| G_DRIVER | k bitowo równe 083 |
| G_BASE | ≤ 5e−4 |

v2 tylko raportuję, bo przy hadronach ≈ 0 test względny jest źle uwarunkowany.

**Estymaty dla każdej masy:**
- ΔX_z(lb) względem bazy;
- przecięcia Y* ∈ {0.251, 0.2484} na siatce;
- ułamek tła na progach hadronowych: f(Y*) = ΔX_z(lb_PYBH,code(Y*)) / (X(Y*) − X_S);
- znak ΔX_z przy −16 i −15, czyli tam, gdzie krzywa hadronowa nasyca się i lekko spada (REVIEW_072).

## 4. Predykcje (moje, zamrożone)

- **Pr1:** Y_z < 0.2484 dla każdego lb ≤ −15 przy obu masach. Progi Wu–Xu w tym zakresie mas są hadronowe.
- **Pr2:** |f| < 0.1 dla obu progów Y* przy obu masach (4 wartości).

## 5. Granice

- Przełączenie dotyczy jednej osi rozkładu: tło wobec hadronów. Nie rozkłada różnicy względem Kohri i Keith; reszta to TYPE_TRANSFER_HOLD według XH-S8.
- Tablica × 1e−12, a nie dokładne zero, żeby nie liczyć logarytmu z zera.
- Wynik dotyczy modelu Wu–Xu, nie fizycznej granicy PBH.
