---
artifact_id: IW_BADACZ_B1_STOPA_GENERATOR_EXTENSION_PREREG_129_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel B1; wykonawca proponowany: Mech-S11 (generacja + splot), M16 (W, G_COV)
created_at: 2026-11-25
document_type: PREREG (zamrożony przed jakimkolwiek przebiegiem)
authorization: Moderator 25 XI 14:00 (dosłownie): „Nie wymaga osobnej zgody, to część autoryzowanych już obliczeń.”
basis: TRIAGE_128 (commit 7d6a15b), odpowiedź na LT11_REQ_BADACZ_001_20261125
claim_ceiling: PREREG / MODEL_CONDITIONAL / GENERATOR_EXTRAPOLATION / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_129: przedłużenie generatora autorów powyżej 1e5 GeV (STOP A, j22)

**Pytanie.** Czy źródło hadronów poniżej 1e9 g, wyprowadzone z generatora autorów zamiast z ekstrapolacji potęgowej kodu, zmienia odpowiedź neutronową j22 o więcej niż 0.03 dex?

## 1. Źródło (zamrożone)
- Wu–Xu `fenyutanchan/primordial-black-hole` @ d395183674cace6c9906a8911bdeb7234ba4040d, katalog `arXiv-2509.05618/arXiv-2509.05618v1/PYTHIA8_table_scripts/`:
  - `table_up.jl` blob 254bedbb7d2fc8dd0e175898aa576acb4601ef1e
  - `table_gluon.jl` blob 42daf5c21af7deb8e1f03b8535b60f799c4df49f
  - `tool_script-count_energy.jl` blob ff91b0484a034bfbfe6f16c731128797e7733fb6
  - `Project.toml` (v1) blob abd79a80f7b763c2ffed89cc6b0b39aa0b33b823. PYTHIA8.jl nie jest przypięty, więc wykonawca zapisuje rozwiązane wersje PYTHIA8.jl i PYTHIA8_jll (oraz wersję PYTHIA 8).
- Tablice BBN PYTHIA z BlackHawk v2.3 (archiwum sha256 dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7), kolumny pierwotnych u i g.
- Tablica q_h kodu: blob 06d0883a27b108692720422294ba2baacd381a64. Instrument W: M16 ROT025 (Nash-Priv, po ID).

## 2. Generacja (Mech-S11)
Zmiany wobec skryptów autorów są tylko takie:
1. Węzły E′ = {1e4, 3e4, 1e5, 3e5, 1e6, 2e6} GeV zamiast `geomspace(5, 1e5, 100)`.
2. `number_of_events = 2000` na węzeł i ramię.
3. Osobne liczniki dla π⁺/π⁻, K⁺/K⁻, p/p̄, n/n̄ oraz zachowane sumy grup autorów (pipm, Kpm, proton, neutron) i K0L.
4. Dla każdego gatunku: suma energii i suma kwadratów energii z dokładnych energii cząstek, nie z binów.
5. Na każde zdarzenie: Σ E po wszystkich cząstkach końcowych (wszystkie PDG) oraz suma ładunku.
6. Dwa ramiona: `TimeShower:weakShower = off` (jak u autorów) i `= on`.
7. `Random:setSeed = on` z osobnym, zapisanym ziarnem na każdy węzeł i ramię.

Reszta bez zmian: ustawienia wiązki, `PDF:lepton = off`, odrzucanie zdarzeń z partonami −23 spoza u/ū (odpowiednio g). Jeśli któryś węzeł lub ramię się nie uruchomi, zapisać porażkę i NIE ponawiać.

## 3. Bramki
- **G_E:** |Σ E − 2E′|/2E′ ≤ 1e−6 w każdym zdarzeniu.
- **G_Q:** ładunek zachowany w każdym zdarzeniu.
- **G_QS:** |N(X⁺) − N(X⁻)| ≤ 3σ dla π, K, p, n.
- **G_OVL:** przy E′ = 1e4, 3e4 i 1e5 GeV średnie krotności grup (ramię off) zgodne z całkami tablic BlackHawk dla u i g w granicach max(3σ_MC, 3%). Niezgodność jest raportowaną systematyką proweniencji, nie zatrzymaniem, bo kształt bierzemy z jednego generatora.
- **G_COV (M16):** udział W dla j22 z M < M_cov ≤ 0.07 w obu zegarach. M_cov = 1e8 g; jeśli bramka nie przejdzie, sprawdzić 8e7 g.

## 4. Splot i kryterium
**Splot (Mech-S11).** Widma pierwotne BlackHawk v2.3 dla M ∈ {1e9, 7e8, 5e8, 3e8, 2e8, 1e8} g, z `primary_only` i E_max ≥ 15·T(M). Krotności N_{i→j}(E):
- dla E ≥ 1e4 GeV: interpolacja log-log między węzłami generatora;
- dla E < 1e4 GeV: tablica BlackHawk.
Kwarki wszystkich zapachów biorą tabelę u, gluony tabelę g, czyli przybliżenie autorów z Eq. 4.5. Wynik: q_gen,h(M) dla 5 grup, jako kształt q_gen,h(M)/q_gen,h(1e9 g) zakotwiczony w wierszu 1e9 g kodu. Poniżej M_cov zostaje ekstrapolacja kodu.

**Δ_src (M16).** Δ_src = log₁₀(W[q_gen]/W[q_code]) dla j22, w zegarach GO i f_BH, w trybie ładunku kodu. Wkłady grup podać ze znakiem.

**Decyzja:**
- **PASS:** |Δ_src| ≤ 0.03 w obu zegarach, |Δ_src(on) − Δ_src(off)| ≤ 0.03 i G_COV PASS. Wtedy część STOP A dotycząca kształtu i normalizacji źródła j22 jest zamknięta w modelu liniowym z zamrożonym tłem.
- **FAIL:** |Δ_src| > 0.03. Progi bezwzględne j22 (base i std) z REVIEW_124/126 przechodzą na status zdominowanych ekstrapolacją; do ich zastąpienia potrzebny jest natywny przebieg 10D z q_gen.
- **HOLD_GENERATOR:** rozrzut weakShower > 0.03. STOP A zostaje z udokumentowanym dnem systematyki generatora.
- Brak decyzji o fizycznej granicy β i o błędzie autorów w żadnym wariancie.

## 5. Predykcje właściciela [▷] (jawne, nie ślepe)
- P1: lokalny wykładnik α_π±(E′) = d ln N/d ln E′ w przedziale 1e5–2e6 GeV, dla u i g, ramię off: w [0.22, 0.34].
- P2: Δ_src(j22) ∈ [+0.01, +0.07] w obu zegarach.
- P3: G_E, G_Q i G_QS przechodzą.

Niespełnienie P1 lub P2 jest informacją o źródle i nie unieważnia testu.

## 6. Koszt i ograniczenia
- Koszt: 6 węzłów × 2 pierwotne × 2 ramiona × 2000 zdarzeń, plus 6 przebiegów BlackHawk `primary_only`. Rząd wielkości to godziny CPU na CI.
- Powyżej ok. 1e5 GeV PYTHIA działa jako model showeru i strun bez danych akceleratorowych, więc wynik ma status ekstrapolacji generatora, nie pomiaru.
- Test nie rozstrzyga semantyki Q-B (T3); dostarcza tylko liczności per stan.
- Nie powiela części A ani B DRAFT_127.

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
