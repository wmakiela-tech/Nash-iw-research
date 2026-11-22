---
artifact_id: IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_PREREG_105_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); EKS1-DIR-009 krok 1, działaniem własnym (decyzja Moderatora 11:36: bez kontaktu z autorami)
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegami produkcyjnymi; budowa generatora w toku)
authorization: obrót „O” Moderatora 22 XI 17:09; stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY [▷] / NO_NOVELTY_ESTABLISHED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_105: czy Herwig 7.1.5 (domyślne strojenie) odtwarza tablice HERWIG z BlackHawk v2.3 przy √s = E′?

## 1. Kontekst

**Wynik REVIEW_098:** 7.2.0 i 7.3.0 przy √s = E′ odtwarzają piony, protony i neutrony z tablic. Brakuje kaonów, a deficyt rośnie z energią do −0.21 dex (7.3) i −0.27 dex (7.2). Stąd `NO_MATCH_PRE_72_CANDIDATE`.

**Rozumowanie:** tablice opisuje już manual v1.0 z V 2019. Herwig 7.1.5 wyszedł w IV 2019, a 7.2 dopiero w XII 2019, ze zmianami produkcji dziwności. Jeśli tablice wygenerowano domyślnym 7.1.x, to 7.1.5 powinien je odtworzyć łącznie z kaonami.

## 2. Generator (`build_herwig71_104.sh`)

**Źródła** (z `herwig.hepforge.org` i `thepeg.hepforge.org`):

| plik | SHA-256 |
|---|---|
| ThePEG-2.1.5.tar.bz2 | c61a00fb… |
| Herwig-7.1.5.tar.bz2 | 3965a6ac… |

**Zależności** (conda-forge, środowisko h71dep): GCC 9.5, boost-cpp 1.74, GSL 2.8, FastJet 3.5.3 (+ devel), LHAPDF 6.5.6, HepMC 2.06.11, zlib.

**Domyślne strojenie, bez modyfikacji źródeł.** Przebieg ruszy dopiero, gdy budowa i inicjalizacja repozytorium się powiodą. Jeśli budowa padnie, PREREG_105 zamykam jako `BUILD_FAIL`.

**Problemy budowy** (zgłaszam jawnie):
- brak `--with-zlib` w konfiguracji ThePEG;
- brak nagłówków FastJet w pakiecie fastjet-cxx (dodałem fastjet-cxx-devel);
- skrypt budowy przy pierwszej próbie wypisał STAGE_OK mimo błędu konfiguracji. Poprawione: każdy krok kończy się kodem ≠ 0.

## 3. Przebiegi (`run105.sh`)

- Herwig 7.1.5, kwark u, √s = E′.
- Te same 6 węzłów co w 097 (`spec_097.log`), po **10 000 zdarzeń** (w 097 było 2000).
- Skrypt zliczeń: `mult_herwig_097.py`, bez zmian.

## 4. Analiza (`analysis_105.py`, sprawdzona na atrapie z danych 7.3)

- **Miara:** L = log₁₀(N_BH/N_MC) dla π±, K±, K0L, p i n.
- **Bramki:**
  - G_MC: rc = 0, 10 000 zdarzeń, ⟨E_final/√s⟩ w 1e−3;
  - G_NODES;
  - G_SAME_NODES (węzły jak w 097).
- **Etykieta:** `MATCH_7.1`, jeśli wszystkie 30 komórek spełnia |L| ≤ max(0.04, 4·se_L). W przeciwnym razie `NO_MATCH`.
- **Dlaczego taka tolerancja:** nie może leżeć poniżej udokumentowanego szumu MC; to lekcja z REVIEW_100. Przy 2000 zdarzeniach (097) se sięgało 0.017 dex, więc stała 0.04 byłaby tylko ~2.4σ. Stąd 10 000 zdarzeń i tolerancja zależna od komórki.
- **Raportuję też:** spadek kaonów (L_K przy najniższym i najwyższym węźle) obok wartości dla 7.2 i 7.3 z 097.

## 5. Predykcja (moja, zamrożona)

- **Pr1:** `MATCH_7.1`.
- **Ostrzeżenie:** nawet przy MATCH ustalenie brzmi „zgodne z domyślnym 7.1.5”, a nie „wygenerowane 7.1.5”. Inne wersje 7.1.x i 7.0 mogą dawać to samo.

## 6. Granice

- Tylko kwark u. Wersje 7.0.x i pozostałe 7.1.x nie były testowane.
- Budowa z nowszym kompilatorem i bibliotekami niż w 2019. Domyślne strojenie zależy od plików wejściowych wersji, nie od kompilatora.
- Wynik nie mówi nic o progu PBH.
