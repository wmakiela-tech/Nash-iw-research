---
artifact_id: IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_REVIEW_098_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); EKS1-DIR-009, krok 1, działaniem własnym
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_097)
follows: PREREG_097 (Nash-iw-research@24dbfaf)
claim_ceiling: DEFINICYJNY (kod) / NUMERYCZNY [▷] / NO_NOVELTY_ESTABLISHED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_098: tablice HERWIG z BlackHawk v2.3 powstały przy √s = E′, czyli pierwotne mają energię E′/2, a nie E′; kaony wskazują na Herwig sprzed 7.2

## 1. Przebieg

- **Ramiona:** Herwig 7.2.0 i 7.3.0 (conda-forge, domyślne strojenia), kwark u, przepis `LEP.in` BlackHawk.
- **Statystyka:** 6 węzłów tablicy (25–1e5 GeV) × 2000 zdarzeń × 3 ramiona; 11:50:26–11:56:14.
- **Bramki:** G_MC i G_NODES PASS. ⟨E_final/√s⟩ = 1.000000, a domknięcie energii działa także zdarzeniowo.
- **Błąd statystyczny MC:** ≤ 0.017 dex na krotność.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA 48dae1ed…).

## 2. Wynik według preregistracji: Pr1 i Pr2 PASS

**L_SQRTS = `SQRTS_EQ_E`.**

- Herwig 7.3 przy √s = E′ odtwarza piony z tablicy BlackHawk do |L| ≤ 0.027 dex we wszystkich 6 węzłach.
- Przy √s = 2E′, czyli w konwencji z manualu, odchylenie sięga 0.10 dex.
- Punkty końcowe widm π leżą przy E′/2: na przykład 1e4 przy E′ = 20356 i 12.9 przy E′ = 25.

**L_VER = `NO_MATCH_PRE_72_CANDIDATE`.** Wartości L dla K± przy √s = E′:

| E′ [GeV] | 25 | 134 | 713 | 3811 | 20356 | 1e5 |
|---|---|---|---|---|---|---|
| względem 7.2.0 | +0.04 | −0.07 | −0.15 | −0.20 | −0.25 | −0.27 |
| względem 7.3.0 | +0.02 | −0.07 | −0.12 | −0.17 | −0.19 | −0.21 |

- K0L zachowuje się tak samo.
- Piony, protony i neutrony zgadzają się z 7.3 do ≲ 0.07 dex.
- Tablica ma więc mniej kaonów niż obie współczesne wersje, a deficyt rośnie z energią. Przy 7.2 jest większy niż przy 7.3.

## 3. Odczyt [▷]

**(a) Etykieta energii: wada kodu i tablic, a nie rocznika.**

- `main.cpp` zapisuje `LuminosityFunction:Energy = E′`, a `formatting.c` dzieli przez 2 i podpisuje wiersz energią E′. Manual podaje E′ = √s/2.
- Dane tablic zgadzają się ze skryptem, nie z manualem.
- Skutek dla użytkownika `hadronization_choice = 1`:
  - przy danej energii pierwotnego krotności odpowiadają energii o połowę niższej. Wszystkie gatunki są przez to zaniżone o ~0.09–0.15 dex (zmierzone jako L(√s = 2E′) − L(√s = E′) dla 7.3; π 0.09–0.13, K± 0.10–0.15, p 0.10–0.13);
  - widma wtórne są ściśnięte do E′/2.
- Tablice PYTHIA w tym samym archiwum mają punkt końcowy przy E′, czyli są zgodne z manualem.

**(b) Kaony: rocznik generatora, wciąż kandydat.**

- Po korekcie √s zostaje deficyt K rosnący z energią do −0.21…−0.27 dex.
- Zgadza się to z tablicami sprzed Herwig 7.2, czyli sprzed zmian produkcji dziwności z XII 2019; tablice istnieją od V 2019.
- Nie jest to dowód: 7.0 i 7.1 nie były testowane, a wpływ ustawień niedomyślnych nie jest wykluczony.

**(c) Rozkład dawnego kontrastu tablic.** Różnica H73 do BH-HER (REC13 ROT012, REVIEW_091 §3) składa się z trzech składników:

- binowanie: 0.046 dex;
- etykieta √s: ~0.09–0.15 dex dla wszystkich gatunków, słabo malejąco z energią;
- deficyt kaonów: do ~0.2 dex.

Ile każdy z nich daje na progu β, wymaga przebiegu natywnego z tablicą BH-HER o poprawionej osi energii. Na poziomie tablic odpowiada to jednak na zastrzeżenie REC13 ROT012 („potrzebne trzecie źródło”): trzecim źródłem jest etykieta √s.

**(d) Nowość:** nie ustalona.

- Dwa wyszukiwania nie znalazły doniesienia o √s = E′ w tablicach HERWIG BlackHawk. To nie znaczy, że go nie ma.
- Systematyczny przegląd: XH-S7 (kroki 2 i 4).
- Według reguły z 21 XI 15:48 o tym, czy to wynik „niosący nowość”, decyduje Moderator.

## 4. Granice

- Odcisk tylko dla kwarku u i 6 węzłów.
- Pre-7.2 to wniosek przez wykluczenie dwóch wersji, a nie dopasowanie.
- Archiwum jest niespójne: `formatting.c` i analiza Rivet nie odtwarzają osi energii tablic (PREREG_097 §1). Wniosek o √s opiera się na danych, a kod go tylko wspiera.
- Wpływ na próg β nie został zmierzony.

## 5. Trzy warstwy

- **Wynik:**
  - tablice HERWIG z BlackHawk v2.3 powstały przy √s = E′ (pierwotny E′/2), wbrew konwencji manualu;
  - kaony wskazują na Herwig sprzed 7.2 [▷].
- **Konfiguracja:** po decyzji Moderatora (bez pytania autorów) samodzielne działanie zajęło około 30 minut: czytanie kodu archiwum, test punktu końcowego i odcisk dwóch wersji. Dało więcej niż poszlaki z NOTE_096.
- **Uczenie systemu:**
  - Przed użyciem tablic narzędzia trzeba sprawdzić punkt końcowy widm wtórnych względem deklarowanej energii pierwotnej. To test na minutę.
  - W 090 przyjąłem konwencję √s = 2E dla obu generatorów na podstawie skryptów PYTHIA, nie sprawdzając skryptu HERWIG. origin_failure_mode: CONVENTION_ASSUMED_FROM_SIBLING_SCRIPT.
  - Nie zmienia to wyników 090/091 (P83 i H73 liczone jednolicie przy √s = 2E), ale zmienia interpretację dhold.

## 6. Dane

- `data/mc097/{H72_f1,H73_f1,H73_f2}.json`, `analysis097.json`.
- Logi: `timeline_097.log`, `inputs_sha_097.log` (SHA tablic BlackHawk i kodu), `versions_097.log`, `spec_097.log`, `mc_logs_097.log`.
- SHA w `MANIFEST_SHA256_092.md` (sekcja 097).
- I1 zewnętrzne: przeliczenie L z tablic BlackHawk v2.3 i `mc097/*.json`, a najlepiej niezależny przebieg Herwig 7.3 przy √s = E′ i √s = 2E′.
