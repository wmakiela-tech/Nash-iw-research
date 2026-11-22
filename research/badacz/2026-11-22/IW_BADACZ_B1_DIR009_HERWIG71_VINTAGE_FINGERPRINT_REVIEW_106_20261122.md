---
artifact_id: IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_REVIEW_106_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); EKS1-DIR-009 krok 1, działaniem własnym
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_105)
follows: PREREG_105 (Nash-iw-research@d8577f9; środowisko aca10a8)
claim_ceiling: NUMERYCZNY [▷] / NO_NOVELTY_ESTABLISHED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_106: Herwig 7.1.5 z domyślnym strojeniem przy √s = E′ odtwarza tablice HERWIG z BlackHawk v2.3 do 0.01 dex we wszystkich 30 komórkach. Rocznik ustalony jako „zgodny z 7.1.5”; Pr1 PASS

## 1. Przebieg

- **Budowa** (`build_herwig71_104.sh`): ThePEG 2.1.5 i Herwig 7.1.5 ze źródeł hepforge, z GCC 9.5 (conda-forge). Inicjalizacja repozytorium z MMHT2014lo68cl i nlo68cl. Pilot PASS.
- **Przebieg:** kwark u, √s = E′, 6 węzłów × 10 000 zdarzeń, 18:09:01–18:13:43.
- **Bramki 3/3 PASS:**
  - G_MC: domknięcie energii zdarzeniowo ≤ 6.5e−7;
  - G_NODES;
  - G_SAME_NODES.
- Błąd statystyczny ≤ 0.007 dex, więc tolerancja wynosi wszędzie 0.04.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA 01eb9618…).

## 2. Wynik według preregistracji: `MATCH_7.1`, Pr1 PASS

L = log₁₀(N_BH/N_7.1.5) przy √s = E′:

| E′ [GeV] | π± | K± | K0L | p | n |
|---|---|---|---|---|---|
| 25 | +0.001 | +0.000 | −0.005 | +0.010 | −0.006 |
| 134 | +0.000 | −0.007 | −0.003 | −0.001 | +0.000 |
| 713 | −0.000 | −0.002 | −0.001 | +0.001 | −0.001 |
| 3811 | −0.003 | +0.001 | −0.003 | +0.001 | −0.001 |
| 20356 | +0.005 | +0.005 | −0.001 | +0.003 | +0.000 |
| 1e5 | −0.002 | −0.001 | −0.004 | −0.004 | −0.003 |

- max |L| = 0.0097. Spadek kaonów między skrajnymi węzłami: 0.001 dex, wobec 0.23 dla 7.3 i 0.31 dla 7.2.

## 3. Odczyt [▷]

**DIR-009, krok 1 (rocznik).**

- Tablice HERWIG z BlackHawk v2.3 dla epoki BBN są zgodne do ≤ 1% z Herwig 7.1.5 z domyślnym strojeniem, uruchomionym przy √s = E′. Zgadzają się wszystkie gatunki we wszystkich 6 węzłach, od 25 GeV do 100 TeV.
- Deficyt kaonów wobec 7.2 i 7.3 (REVIEW_098) to więc rocznik generatora: zmiany produkcji dziwności i strojenia w 7.2. Nie jest to wada tablic.
- Sformułowanie ostrożne: „zgodne z domyślnym 7.1.5”. Inne wydania 7.1.x z tym samym strojeniem dałyby prawdopodobnie to samo; 7.0 nie testowałem.

**Etykieta √s jeszcze mocniej potwierdzona.** Z właściwą wersją generatora zgodność przy √s = E′ sięga ~0.01 dex dla wszystkich gatunków. Przy √s = 2E′ różnice dla pionów wynoszą ~0.1 dex (097, wersja 7.3). Tablice opisują więc pierwotne o energii E′/2, wbrew konwencji manualu.

**Pełny obraz historycznych tablic HERWIG** (REVIEW_098, 100, 102 i 106):
- rocznik: 7.1.5;
- etykieta: √s = E′, czyli podwójna energia pierwotnego w podpisie;
- binowanie: konwencja BlackHawk na rzadkiej siatce (100 węzłów), 0.046 dex w konwencji całkowania autorów.

Żaden składnik nie jest nieznany.

**Konsekwencja dla j22.** REVIEW_100 i 102 zostawiły etykietę przy j22 nieoznaczoną z dokładnością do ekstrapolacji ponad 5e4 GeV (−0.01…−0.08 dex). Z działającym Herwig 7.1.5 można teraz wygenerować brakujące krotności tego samego rocznika dla pierwotnych 5e4–1e5 GeV przy √s = 2E. To zamyka tę niejednoznaczność pomiarem, a nie wariantami Sa i Sb. Proponuję to jako następny krok; wymaga osobnej preregistracji.

**Nowość:** nie ustalona. XH-S8: brak zweryfikowanego opublikowanego użycia choice = 1 (NOT_VERIFIED). Prior art dla klasy wad konwencji BlackHawk: arXiv:2506.13861, dodatek A. O ewentualnym statusie „niosącym nowość” decyduje Moderator.

## 4. Granice

- Tylko kwark u, 6 węzłów.
- Budowa współczesnym kompilatorem. Domyślne strojenie pochodzi z plików wersji.
- Wynik dotyczy tablic, nie progu PBH.

## 5. Trzy warstwy

- **Wynik:** tablice HERWIG z BlackHawk v2.3 są zgodne z Herwig 7.1.5 (strojenie domyślne) przy √s = E′, do ≤ 0.01 dex. DIR-009 krok 1 zamknięty co do rocznika.
- **Konfiguracja:** po decyzji Moderatora (samodzielnie, bez autorów) budowa ze źródeł zajęła ~55 minut, a odcisk 5 minut. Trzy problemy środowiskowe (zlib, nagłówki FastJet, zbiory PDF) rozwiązałem jawnie.
- **Uczenie systemu:**
  - Skrypt budowy wypisał sukces mimo błędu konfiguracji. Łatka: każdy krok kończy się kodem ≠ 0, a STAGE_OK pada tylko po sukcesie wszystkich kroków.
  - Tolerancja z błędu MC (10 000 zdarzeń zamiast 2000) zadziałała zgodnie z łatką z REVIEW_100.

## 6. Dane

- `data/mc105/H71_f1.json`, `analysis105.json`.
- Logi: `timeline_105.log`, `inputs_sha_105.log`, `versions_105.log`, `spec_105.log`, `mc_logs_105.log`, `build_conf_tail_105.log`, `build_sha256_105.log` (SHA źródeł, binarium, repozytorium i zbiorów PDF).
- SHA w `MANIFEST_SHA256_092.md` (sekcja 105).
