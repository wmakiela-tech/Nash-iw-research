---
artifact_id: IW_EKS1_FRONTB_WUXU_REPLICATION_PACKAGE_INDEX_001_20261112
exposure: PUBLIC
claim_ceiling: REPLICATION_PACKAGE_AND_TASK_SPEC_ONLY / NO_RESULT / MODEL_INTERNAL_TARGETS / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_PAPER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-12
origin_cell: EKSPLORATOR / EKS1 (wątek Claude; solver DECLARED_ONLY)
document_type: PACKET
task_id: decyzja Moderatora 2026-11-12 — replika spoza rodziny Claude, kolejność GPT → Grok
---

# Front B (Wu–Xu): paczka repliki spoza rodziny Claude — indeks i wspólny protokół

**Po co.** Wszystkie natywne liczby projektu dla kodu Wu–Xu z ostatnich tygodni zmierzył Badacz (rodzina Claude). Zanim cokolwiek z nich wejdzie do dalszej pracy, mają być odtworzone poza tą rodziną. Decyzja Moderatora z 12.11.2026: najpierw uczestnik z rodziny GPT, dopiero potem Grok.

**Co to jest, a czym nie jest.** To specyfikacja zadania i spis materiałów. Nie zawiera wyniku. Wszystkie wielkości są wewnętrzne dla modelu autorów (MODEL_INTERNAL): nie są granicą na PBH ani oceną opublikowanej pracy.

Pliki w tym folderze:

| plik | dla kogo |
|---|---|
| ten indeks | wszyscy; definicje, materiały, okna porównania |
| `KOMUNIKAT_GPT_REPLIKA_NATYWNA_001.md` | uczestnik z rodziny GPT (pierwszy) |
| `KOMUNIKAT_GROK_REPLIKA_NIEZALEZNA_001.md` | Grok (drugi, po zwrocie GPT) |

## 1. Co replikujemy

Cel: tabela z Badacz REVIEW_053 (8.11) — przesunięcie konturu przy poprawionym wzorze na ułamek helu — oraz kalibracja SBBN, od której zależy wariant C1 właściciela frontu B.

Definicje (za Badacz PREREG_051, zapisanym przed przebiegami):

- `X` — ułamek neutronów `n/(n+p)`, czwarta zmienna stanu w `magic()` autorów.
- `T0 = T_nuc = 0.078185270688319950 MeV` (literał z `tool_script-parameters.jl`).
- `X(T)` — interpolacja liniowa `X` po zmiennej `Q/T` na 10 000 punktach `a` (geomspace), dokładnie jak w `magic()`.
- **SBBN:** przebieg z `β = 1e-30` (PBH bez znaczenia). `X0s = X_SBBN(T0)`.
- `Y_code = 2X/(1−X)` — wzór z kodu autorów. `2X` — wzór z tekstu arXiv v3.
- `T1` — temperatura, przy której `2·X_SBBN(T1) = 0.245`.
- **V0:** kontur `Y_code(T0) = 0.251`. **V1:** kontur `2X(T1) = 0.251`. **V2:** kontur `2X(T0) − 2X_SBBN(T0) = 0.006`.
- **Korzeń:** `log10 β`, przy którym warunek konturu jest spełniony, przy ustalonej masie.
- **Masy:** indeks `j` (od zera) w siatce autorów: `m_j = 6e8 · (1e10/6e8)^(j/99)` g. Obowiązkowo `j = 22` (1.121174e9 g) i `j = 62` (3.494214e9 g). Opcjonalnie `j = 28, 34, 99`.

## 2. Wielkości do zgłoszenia

| nr | wielkość | gdzie |
|---|---|---|
| Q1 | `X0s`, `Y_code,SBBN`, `2·X0s`, `T1` [MeV] | j = 22 i j = 62 |
| Q2 | korzenie V0, V1, V2 (`log10 β`) | j = 22 i j = 62 |
| Q3 | przesunięcia `V1 − V0`, `V2 − V0` [dex] | j = 22 i j = 62 |
| Q4 (opcja) | to samo dla j = 28, 34, 99 | — |
| Q5 (opcja, tylko przebieg natywny) | przesunięcie korzenia V0 przy j = 22 dla wariantu `p13` (prawo `T^1.3` poniżej 1e9 g) i dla mapy `B_sym` | łatki Mech-S6, patrz §3C |

Do każdej liczby: metoda wyznaczenia korzenia, liczba punktów β, tolerancje solvera, wersje, SHA-256 kodu i surowych wyników.

## 3. Materiały (wszystko publiczne)

### A. Kod autorów — przypięty

Repozytorium `Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d` (2025-12-30; HEAD repozytorium w dniu 12.11.2026). Katalog `arXiv-2509.05618/`. Pliki potrzebne do wykonania, z blobami Git:

| plik | blob |
|---|---|
| `main-scan.jl` | `b368ba55d5a493f7bc185909730f7fe5691f10d6` |
| `main-scan-parameters.jl` | `53faee65beda383348580c28d0424188da69b660` |
| `tool_script-parameters.jl` | `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` |
| `tool_script-N_relativistic_species.jl` | `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc` |
| `tool_script-hadrons_from_PBH.jl` | `cc73432910f872d526113ce59b6204f38d0766a9` |
| `tool_script-geomspace.jl` | `85062aaa54093f11878a85c117fe18034ae6eae3` |
| `tool_script-directories.jl` | `8c54632fdc06e0981dcefb55f0a58e89659c7be3` |
| `tool_script-ArbNumerics_compat.jl` | `3f5b592c919c1e80c4b85ad44d437eec000fd65f` |
| `Project.toml` | `6297eb1682da77bbbfa87307795b655c677f98c4` |
| `data/ext/N_around_m_e.csv` (1000 wierszy: T [MeV], N_ρ, N_s) | `93f2494f026c5d0587ea40fe08bb938dd9d01fa8` |
| `data/ext/N_s_from_PDG2024.csv` | `33aceb876fc36cb2486d36c690e6401d85d76b46` |
| `data/ext/N_rho_OVER_N_s_from_PDG2024.csv` | `28b0c13563d7b3bdeaee191a3a981197345d05b8` |
| `data/out/hadrons_from_PBH.dat` (nagłówek + 100 wierszy: masa [GeV], pięć szybkości [GeV]) | `06d0883a27b108692720422294ba2baacd381a64` |

### B. Jednostki

`Fenyutanchan/NaturalUnits.jl`, commit `4a9f007ff1df416c9fef28c4d83d8fe8846099cf`. **Przypiąć ten commit** — gałąź `main` tej biblioteki jest już dalej. W tej wersji `M_Pl = 1/sqrt(8πG)` (zredukowana), `m_Pl = 1/sqrt(G)`, `G = 6.67430e-11` SI.

### C. Natywne środowisko wykonawcze spoza rodziny Claude — już istnieje w tym repozytorium

Komórka Mech-S6 (rodzina GPT) uruchomiła 18–19.10.2026 natywny kod autorów w Julii 1.12.3 na GitHub Actions:

- `.github/workflows/mech-s6-wuxu-charge-comparator.yml` (blob `4862c4171d37`), `.github/workflows/mech-s6-wuxu-paper-charge-2x2.yml` (blob `f8e759978b38`);
- `research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl` (blob `db9b5c8a4629`; przypięte wersje pakietów) i `run_one_point.jl` (blob `f9377d2be5fd`; jeden punkt `(m, β)`, zapis trajektorii z `X_n`, `T`);
- łatki wariantów: `research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py` (blob `4d1f2be94510`, mapa `B_sym`), `research/mech-s6/2026-10-19/apply_wuxu_paper_subedge_law.py` (blob `4198ab092af3`, prawo `M^-1.3`);
- zapis wykonania: `research/mech-s6/2026-10-18/mech_s6_frontb_wuxu_charge_map_dynamic_comparator_result_001.md` (podaje numer przebiegu Actions i status kroków).

Badacz odnotował 31.10 zgodność bit w bit własnego kontenera z wartością Mech-S6 dla punktu `6e9 g, β = 1e-16` (`research/badacz/2026-10-31/data/native_audit/RUNLOG.md`).

### D. Artefakty Badacza poddawane replice

- Definicje (wolno czytać): `research/badacz/2026-11-08/IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_PREREG_051_20261108.md` (blob `0e498f0cfea7`).
- Sterownik i siatki: `research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl` (blob `86bdee90f252`), `research/badacz/2026-11-08/data/yp051/configs_a.dat` (blob `763cac74f138`), `configs_b.dat` (blob `46bb25055cdf`).
- **Wartości odniesienia — nie otwierać przed zapisaniem własnych liczb:** `research/badacz/2026-11-08/data/yp051/yp_a.csv`, `yp_b.csv` oraz `IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_REVIEW_053_20261108.md`. Uczestnik, który te liczby już zna, zaznacza to w zwrocie (`NONBLIND`).

## 4. Poziomy repliki

- **L1 — odtwarzalność:** ten sam sterownik Badacza i te same siatki na innej maszynie, uruchomione przez inną rodzinę. Sprawdza środowisko, nie logikę sterownika.
- **L2 — niezależny operator:** własny sterownik wywołujący niezmienione `magic()` autorów i własne wyznaczenie korzeni. Sprawdza logikę sterownika i analizy.
- **L3 — niezależna implementacja:** własny kod (np. Python) tych samych równań, bez Julii. Sprawdza także odczyt równań z kodu autorów.

## 5. Okna porównania (zapisane przed replikami)

| wielkość | natywnie (L1, L2) | niezależna implementacja (L3) |
|---|---|---|
| `X0s` | różnica ≤ 1e-4 | ≤ 5e-4 |
| `T1` | ≤ 0.1% | ≤ 0.5% |
| korzenie przy j = 62 | ≤ 0.01 dex | ≤ 0.02 dex |
| korzenie przy j = 22 | ≤ 0.02 dex | ≤ 0.04 dex |
| przesunięcia Q3 | ≤ 0.02 dex | ≤ 0.03 dex |

Uzasadnienie szerszych okien przy j = 22: kontur jest tam płaski; Badacz podaje rozrzut ±0.011–0.013 dex na korzeń i przesunięcie ok. +0.025 dex przy zaostrzeniu tolerancji solvera. Wynik poza oknem nie jest porażką repliki — jest wynikiem i ma być zgłoszony tak, jak wyszedł.

## 6. Znane pułapki (każda już kogoś kosztowała przebieg)

1. **Nie poprawiać równań autorów.** Replikujemy kod taki, jaki jest: człon `−4 + q_ρ/(3 + q_s)` w ewolucji `ρ`, `n_B = η_B·n_γ(T)`, brak rozrzedzania hadronów, wzór `2X/(1−X)`. Wątpliwości fizyczne zgłasza się osobno.
2. **Domyślne tolerancje solvera.** Autorzy wołają `solve(problem, AutoTsit5(Rosenbrock23()))` bez tolerancji, w arytmetyce `ArbFloat` o 100 bitach. Wynik zależy od ścieżki kroku adaptacyjnego.
3. **Bity wejścia.** Dwie wartości `log10 β` równe do sześciu cyfr po przecinku, a różne w ostatnim bicie, dają różne `Y`. Zapisywać `%.17g`.
4. **Pliki punktów z komentarzami.** Sterownik `research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl` wykłada się na liniach zaczynających się od `#` (stwierdzone 12.11 przez REC11, INT9 i przebieg Badacza). Nie jest częścią tej repliki.
5. **Zapis gęsty przy ostrych tolerancjach** kończył się u Badacza brakiem pamięci. Zapisywać tylko potrzebne punkty.

## 7. Zwrot

- Uczestnik z rodziny GPT: zwykły zwrot w `research/<komórka>/<data>/` z kodem, surowymi wynikami i SHA-256.
- Grok: odpowiedź w rozmowie; Moderator przekazuje ją do projektu.
- Porównanie z wartościami odniesienia i ocena robi recenzent spoza rodziny Claude (REC11 lub AUD1). EKS1 ani Badacz nie zamykają tej repliki.

## 8. Czego ta paczka nie rozstrzyga

Która poprawka wzoru jest fizycznie właściwa (decyduje właściciel frontu B). Czy źródło hadronów poniżej 1e9 g jest poprawne. Czy opublikowana rycina powstała z tego kodu. Zgodność replik nie jest dowodem fizyki — jest warunkiem, żeby liczby w ogóle wolno było cytować.
