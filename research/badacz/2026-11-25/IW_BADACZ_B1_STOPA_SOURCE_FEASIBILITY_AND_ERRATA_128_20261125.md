---
artifact_id: IW_BADACZ_B1_STOPA_SOURCE_FEASIBILITY_AND_ERRATA_128_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel B1
created_at: 2026-11-25
document_type: TRIAGE (odpowiedź na LT11_REQ_BADACZ_001_20261125) + ERRATA do DRAFT_127 / PREREG_125
responds_to: LT11 ROT004 (Nash-Priv, po ID); REC14 ROT015, REC14 ROT016 (Nash-Priv, po ID)
claim_ceiling: PROPOSAL / NO_RUN / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# B1 STOP A: czy da się uzyskać fizyczne źródło hadronów poniżej 1e9 g (+ errata)

**Rola:** Badacz. Pole §F, które ten dokument zmienia: „niepewność” STD_A i Q-B (STOP A). Nic nie uruchomiłem poza oszacowaniem pokrycia (`code/coverage_estimate_128.py`).

## 1. Odpowiedź: TAK, z istniejących zasobów; blokerem jest koszt i autoryzacja, nie brak źródła

**Trzy siatki, których nie wolno mylić:**
- (i) siatka mas PBH tablicy q_h w kodzie: 100 wierszy, pierwszy węzeł 1e9 g; poniżej kod ekstrapoluje z wierszy 0–1, nachylenie −1.20;
- (ii) siatka energii pierwotnych w BlackHawk: parametry `Emin`/`Emax`, u autorów 5–1e5 GeV (`tool_script-BlackHawk_extension.jl` l. 104–106);
- (iii) siatka hadronizacji E′: tablice BBN PYTHIA w BlackHawk mają 250 węzłów w zakresie 5–1e5 GeV.

Tożsame pliki (DAX-S10 ROT011: 11/11 SHA) nie dają nowego pokrycia: wszystkie trzy siatki kończą się na 1e5 GeV.

**Istniejące źródło generatora.** Autorzy mają w repozytorium własne skrypty PYTHIA8.jl (`fenyutanchan/primordial-black-hole` d395183, `arXiv-2509.05618/arXiv-2509.05618v1/PYTHIA8_table_scripts/table_up.jl`, `table_gluon.jl`):
- 1e5 zdarzeń na każdy z 100 węzłów E′, gatunki BBN zgrupowane (±211, ±321, ±2212, ±2112);
- jedynym ograniczeniem jest `Emax_initial = 1e5 # Above this energy, Pythia8 works too slowly.`, a więc koszt, nie fizyka ani brak kodu;
- trasa HDMSpectra (BlackHawk, `hadronization_choice` 4) odpada: autorzy opisują ją jako tablice „present epoch” (`tool_script-BlackHawk_extension.jl` l. 62), czyli stany końcowe po rozpadach, bez π±, K±, K0L i n.

**Wymagane pokrycie (szacunek w geometrycznej optyce, `data/coverage_estimate_128.json`):**
- Przy E′_max = 1e5 GeV nawet kotwica 1e9 g traci 1.6% strumienia energii pierwotnych q/g. Przy 5e8 g traci 32%.
- Przy E′_max = 2e6 GeV strata wynosi 9e−6 dla 1e8 g i 2e−4 dla 8e7 g.
- Poniżej 1e8 g kod emituje 1.3% hadronów j22 (kontrola: poniżej 1e9 g wychodzi 0.814, zgodnie z M16 ROT025 = 0.81400).

## 2. Najmniejszy rozstrzygający test (koszt rzędu godzin CPU na CI; wymaga zgody §E, bo to Julia)

**Generacja (wykonawca proponowany: Mech-S11, ma środowisko Julii na CI).** Skrypty autorów `table_up.jl` i `table_gluon.jl` bez zmian fizyki, z trzema zmianami:
- węzły E′ = {1e4, 3e4, 1e5, 3e5, 1e6, 2e6} GeV, po 2·10³ zdarzeń;
- liczniki rozdzielone na stany ładunkowe (π⁺/π⁻, K⁺/K⁻, p/p̄, n/n̄), tak by grupy dało się złożyć z powrotem;
- dwa ramiona: `TimeShower:weakShower` off/on.

**Bramki dopuszczalności:**
- G_OVL: przy 1e4–1e5 GeV krotności grup zgodne z tablicą BlackHawk dla kolumn u i g w granicach max(3σ_MC, 3%). Niezgodność jest systematyką proweniencji, nie blokerem, bo kształt bierzemy z jednego generatora.
- G_Q: ładunek zachowany w każdym zdarzeniu oraz |N(π⁺) − N(π⁻)|/N w granicach 3σ.
- G_E: suma energii stanów końcowych = 2E′ w granicach 1e−6; średnie energie gatunków zapisane (dla G_EC/G_DEP).
- G_COV: udział odpowiedzi j22 spod M_cov ≈ 1e8 g ≤ 7%, liczony instrumentem M16 ROT025 (sprzężony, zamrożone tło). Wtedy dwukrotny błąd ekstrapolacji poniżej M_cov przesuwa W o ≤ 0.03 dex.

**Kryterium (jedno).** Bierzemy źródło q_gen(M) na [M_cov, 1e9] g: krotności generatora po gatunkach splecione z widmami pierwotnymi BlackHawk przy E_max ≥ 15·T, zakotwiczone w wierszu 1e9 g kodu. Δ_src = log₁₀(W[q_gen]/W[q_code]) dla j22, w obu zegarach (GO, f_BH), z wkładami gatunków ze znakiem (p̄ < 0 wg M16 ROT025).
- PASS: |Δ_src| ≤ 0.03 i różnica ramion weakShower ≤ 0.03. Część STOP A dotycząca kształtu i normalizacji źródła j22 zostaje zamknięta w modelu liniowym. Przeniesienie na Y/β nadal wymaga natywnego przebiegu.
- FAIL: |Δ_src| > 0.03. Progi bezwzględne j22 (base i std) są zdominowane przez ekstrapolację i trzeba je zastąpić natywnym przebiegiem z q_gen.
- Rozrzut weakShower > 0.03: STOP A zostaje z udokumentowanym dnem systematyki generatora (wynik negatywny).

**Prior [▷], bez preregistracji.** α_PY = 0.305–0.317 przy 1e4–1e5 GeV (REVIEW_126) wobec 0.20 w kodzie oraz zwalnianie wzrostu krotności przy biegnącym α_s każą oczekiwać Δ_src ≈ +0.01…+0.07 dex, czyli wyniku w pobliżu progu. Przesunięcie STD_A jest na kształt mało czułe (REVIEW_126).

**Granice:**
- Poniżej 1e5 GeV PYTHIA jest strojona danymi. Powyżej działa model showeru i strun bez danych: twórcy BlackHawk sami traktują już zakres powyżej 10 TeV jako rozszerzenie walidacji.
- M < M_cov pozostaje ekstrapolacją z jawnym ograniczeniem z G_COV.
- Test nie rozstrzyga semantyki Q-B (T3); daje tylko dane per stan.

**Nie powielam §3 DRAFT_127.** Mech-S11 wykonuje część A (prereg 24c5fcb); części B nikt nie uruchamia.

## 3. Errata (przyjmuję korekty REC14)

1. **DRAFT_127 §1, pole eliminacji STD_A, oraz zwrot Slack z 23 XI 23:46.** „FAIL eliminuje STD_A” było błędem logicznym. Test relabelingu (B) testuje tylko H2, czyli prawo z §2. Natywnego przesunięcia STD_A (H1) nie testuje. Poprawnie (REC14 ROT016):
   - A PASS + B FAIL: H1 zostaje, H2 odrzucone;
   - A FAIL: H1 zagrożone, a B go nie ratuje;
   - oba PASS: oba wspierane przy sufiecie MODEL_CONDITIONAL.
2. **„Ślepy wobec wykonawcy”.** Przedziały B były jawne w dokumencie i w wiadomości oznaczonej Mech-S10, więc test jest precommitted, ale nie ślepy wobec wykonawcy.
3. **§2 DRAFT_127.** Nie istnieje jedno wspólne c. Dopasowanie PCHIP daje c = 0.905 przy j22 i 1.027 przy j62. Źródłowe c_eff wynosi 0.900–0.938 (REC14 ROT016). Reszta przy j62 dla c = 0.9 (−0.02998) leży na granicy tolerancji.
4. **DRAFT_127 §1, „ściana ok. 0.9e9 g, poniżej 10⁹ g”.** To prawda tylko dla mapy Y_code = 2X/(1−X). Przy mapie v3 (2X) pierwsza ściana std z przedziałem w danych natywnych wypada przy j20 = 1.059e9 g (REC14 ROT015). Zdanie zależy od STOP B i nie wchodzi do żadnego briefu bez rozstrzygnięcia mapy.
5. **PREREG_125, l. 50 („G_RUN: 18/18 pierwiastków”).** Poprawnie: 18/18 procesów, wszystkie ewaluacje Success, pierwiastki 15/18 (base j20 bez pierwiastka w [−21, −16]). REVIEW_126 podaje to poprawnie.

**origin_failure_mode:** `DECISION_RULE_SCOPE_OVERREACH`, czyli wniosek eliminacyjny z testu hipotezy pomocniczej. **Reguła:** każde kryterium eliminacji wskazuje hipotezę, którą testuje (H1/H2), i nie obejmuje innych.

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
