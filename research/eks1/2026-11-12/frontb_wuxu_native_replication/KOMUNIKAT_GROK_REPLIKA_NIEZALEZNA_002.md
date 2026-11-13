---
artifact_id: IW_EKS1_FRONTB_WUXU_GROK_INDEPENDENT_REPLICA_TASK_002_20261113
exposure: PUBLIC
claim_ceiling: TASK_MESSAGE_ONLY / NO_RESULT / MODEL_INTERNAL_TARGETS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-13
revision: 2 (2026-11-13, przed ogłoszeniem; dodana uwaga o nieregularności odpowiedzi)
supersedes: IW_EKS1_FRONTB_WUXU_GROK_INDEPENDENT_REPLICA_TASK_001_20261112
origin_cell: EKSPLORATOR / EKS1 (wątek Claude; solver DECLARED_ONLY)
document_type: PACKET
task_id: decyzja Moderatora 2026-11-12 — replika Groka po replice GPT
---

# KOMUNIKAT DO WKLEJENIA — Grok: niezależna replika (Wu–Xu, front B), wersja 002

> **Dla Moderatora (nie wklejać):** replika z rodziny GPT wróciła 12.11 (Mech-S9 ROT006–008, recenzja REC11 ROT025 i ROT027), więc ten komunikat można przekazać. Wersja 002 różni się od 001 jednym: dodaje wielkość Q0 (wartości funkcji w ustalonych punktach) i ostrzeżenie o złym uwarunkowaniu jednego korzenia — patrz `ERRATA_001_PO_REPLICE_GPT.md`. Nie dopisywać liczb z repliki GPT ani z raportów Badacza.

---

**Od:** EKS1 — wątek Claude w projekcie IW/Nash. **Rola Groka:** niezależny wykonawca spoza rodzin GPT i Claude.

Wszystkie materiały są publiczne: repozytorium `wmakiela-tech/Nash-iw-research`, folder
`research/eks1/2026-11-12/frontb_wuxu_native_replication/`. Indeks z blobami i definicjami:
`IW_EKS1_FRONTB_WUXU_REPLICATION_PACKAGE_INDEX_001_20261112.md`. Kod źródłowy autorów:
`Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d`, katalog `arXiv-2509.05618/`.

## 0. Zasady

- W tym projekcie zgoda modeli nie jest dowodem. Potrzebne są Twoje własne liczby z Twojego własnego wykonania.
- **Nie otwieraj** plików `research/badacz/2026-11-08/data/yp051/*.csv` ani `…REVIEW_053…md`, dopóki nie podasz swoich liczb. Są tam wartości odniesienia.
- Nie poprawiaj równań autorów. Replikujemy kod taki, jaki jest. Wątpliwości fizyczne zapisz osobno, na końcu.
- Wynik jest wewnętrzny dla modelu autorów. Nie jest granicą na PBH ani oceną opublikowanej pracy.
- Jeśli czegoś nie da się wykonać, napisz dokładnie czego i dlaczego. Blokada też jest wynikiem.

## 1. Krok 0 — zadeklaruj, co potrafisz wykonać

Zanim zaczniesz, odpowiedz jednym akapitem: czy w tej rozmowie możesz uruchamiać kod; w jakim języku; czy masz dostęp sieciowy do GitHub z poziomu kodu; czy możesz uruchomić Julię 1.12. Od tego zależy gałąź:

- **Gałąź N (jest Julia):** uruchom niezmienione `magic()` autorów własnym sterownikiem. Środowisko jak w `research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl` (przypnij `NaturalUnits.jl@4a9f007ff1df416c9fef28c4d83d8fe8846099cf`).
- **Gałąź P (jest Python lub inny język, bez Julii):** napisz własną implementację modelu z §3 i policz wielkości z §2.
- **Gałąź Z (nie możesz wykonywać kodu):** powiedz to wprost. Wtedy zrób tylko jedno: porównaj opis modelu z §3 z kodem autorów linia po linii i wypisz każdą różnicę. Nie podawaj żadnych liczb jako repliki.

## 2. Co policzyć

Definicje: `X = n/(n+p)`; `T0 = 0.078185270688319950 MeV`; `X(T)` — interpolacja liniowa `X` po zmiennej `Q/T`; SBBN — przebieg z `β = 1e-30`; `X0s = X_SBBN(T0)`; `Y_code = 2X/(1−X)`; `T1` — temperatura, przy której `2·X_SBBN(T1) = 0.245`.

Masy: `m_j = 6e8·(1e10/6e8)^(j/99)` g; obowiązkowo `j = 22` (1.121174e9 g) i `j = 62` (3.494214e9 g).

| nr | wielkość |
|---|---|
| Q0 | `X(T0)` w ustalonych punktach: j = 22 przy `log10 β = −18.0, −17.5, −17.2, −17.0`; j = 62 przy `log10 β = −20.0, −19.5, −19.4, −19.0` (osiem liczb, pełna precyzja) |
| Q1 | `X0s`, `Y_code,SBBN`, `2·X0s`, `T1` [MeV] — dla obu mas |
| Q2 | korzenie `log10 β` trzech konturów: V0: `Y_code(T0) = 0.251`; V1: `2X(T1) = 0.251`; V2: `2X(T0) − 2·X0s = 0.006` |
| Q3 | przesunięcia `V1 − V0` i `V2 − V0` w dex |

Korzenie leżą w przedziale `log10 β ∈ [−20, −16.5]`. Metodę ich wyznaczenia wybierz sam i opisz.

**Uwaga o uwarunkowaniu.** Przy j = 22 odpowiedź `X(T0)` rośnie z `β` coraz wolniej (bliskie nasycenie), więc korzeń V2 jest tam kilkakrotnie bardziej wrażliwy na drobne różnice numeryczne niż przy j = 62. Dlatego podstawą porównania są wartości Q0, a korzenie są wielkością pochodną. Dla każdego korzenia podaj też lokalne nachylenie `d ln(X − X0s) / d ln β`.

**Uwaga o nieregularności.** Kod autorów uruchamiany z ich domyślnymi ustawieniami solvera daje `X(T0)` jako funkcję `β`, która w drobnej skali nie jest gładka ani monotoniczna: sąsiednie wartości `β` potrafią dać wyniki różniące się o około `1e-4` w `Y` w przypadkowym kierunku. Bisekcja na takiej funkcji trafia w przypadkową zmianę znaku, nie w „korzeń". Dlatego:
- korzenie wyznaczaj z gładkiego dopasowania do co najmniej siedmiu równo rozłożonych punktów i podaj pasmo niepewności (na przykład rozrzut po kolejnym usuwaniu jednego punktu);
- podaj tolerancje solvera, których użyłeś (`reltol`, `abstol`), a w gałęzi P policz każdy punkt Q0 dla dwóch tolerancji różniących się co najmniej dziesięciokrotnie i podaj obie wartości;
- w gałęzi N nie zmieniaj ustawień solvera autorów dla wielkości Q0; ewentualny przebieg z ostrzejszą tolerancją zgłoś osobno.

## 3. Model (opis pomocniczy — w razie różnicy wygrywa kod autorów; różnicę zgłoś)

Jednostki naturalne, GeV. Stałe z `tool_script-parameters.jl`:
`m_p = 938.27208816 MeV`, `m_n = 939.5654205 MeV`, `Q = m_n − m_p`, `τ_n = 878.4 s`, `η_B = 6.1e-10`, `α = 1/137.035999084`, `m_π = 139.57039 MeV`, `τ_π = 2.6033e-8 s`, `m_K = 493.677 MeV`, `Γ_π = 1/τ_π`, `Γ_K⁻ = 8.1e7 s⁻¹`, `Γ_K0L = 2.0e7 s⁻¹`, `γ = 1/(3√3)`, `G = 6.67430e-11` SI, `M_Pl = 1/sqrt(8πG)`, `m_Pl = 1/sqrt(G)`.

**Stan** (kod całkuje logarytmy, zmienna niezależna `η = ln a`, start `a = 1` w chwili formacji):
`t, ρ_SM, m, X, n_π⁻, n_π⁺, n_K⁻, n_K0L, n_p̄, n_n̄`.

**Warunki początkowe** dla masy `m0` i ułamka `β`:
`t_f = m0/(γ·m_Pl²)`, `H_f = 1/(2t_f)`, `ρ_f = 3·M_Pl²·H_f²`, `T_f = T(ρ_f)`, `n_PBH,f = β·ρ_f/m0`, `X_f = 1/(1 + exp(Q/T_f))`, każda gęstość hadronów `= 1e-60 · 2ζ(3)T_f³/π²`.
Koniec: `a_end = 10·cbrt( N_ρ(T_f)·T_f³ / (N_ρ(T0)·T0³) )`.

**Wielkości pomocnicze:**
`n_PBH = n_PBH,f / a³`; `T_BH = M_Pl²/m`; `T = T(ρ_SM)`; `n_γ = 2ζ(3)T³/π²`; `n_B = η_B·n_γ`; `x = Q/T`;
`H = sqrt( (ρ_SM + m·n_PBH) / (3·M_Pl²) )`;
`N_BH = (27/4)·N_ρ(T_BH)/(30720π)`; `dm/dt = −N_BH·m_Pl⁴/m²`.
Gdy `ln m ≤ max(ln m0 − 20, ln m_Pl)`: `n_PBH = 0` i `dm/dt = 0`.

**Równania** (pochodne po czasie; po `η` — podzielić przez `H`):

```
d ln t / dη    = 1/(H t)
d ln ρ_SM / dη = −4 + q_ρ/(3 + q_s) − (dm/dt)·n_PBH/(H·ρ_SM)        q_ρ = d ln N_ρ/d ln T,  q_s = d ln N_s/d ln T
dX/dt = −Γ_n·(X − (1−X)·e^(−x)) − X/τ_n                              Γ_n = (255/τ_n)·(12 + 6x + x²)/x⁵
        + (1−X)·n_π⁻·σ[π⁻ p→n] − X·n_π⁺·σ[π⁺ n→p]
        + (1−X)·n_K⁻·σ[K⁻ p→n] − X·n_K⁻·σ[K⁻ n→p]
        + (1−X)·n_K0L·σ[K0L p→n] − X·n_K0L·σ[K0L n→p]
        − X·n_p̄·σ[p̄ n→p] + (1−X)·n_n̄·σ[n̄ p→n]
dn_π⁻/dt = S_π·n_PBH − Γ_π·n_π⁻ − σ[π⁻ p→n]·(1−X)·n_B·n_π⁻
dn_π⁺/dt = S_π·n_PBH − Γ_π·n_π⁺ − σ[π⁺ n→p]·X·n_B·n_π⁺
dn_K⁻/dt = S_K·n_PBH − Γ_K⁻·n_K⁻ − (σ[K⁻ n→n]·X + σ[K⁻ n→p]·X + σ[K⁻ p→n]·(1−X) + σ[K⁻ p→p]·(1−X))·n_B·n_K⁻
dn_K0L/dt = S_K0L·n_PBH − Γ_K0L·n_K0L − (σ[K0L n→n]·X + σ[K0L n→p]·X + σ[K0L p→n]·(1−X) + σ[K0L p→p]·(1−X))·n_B·n_K0L
dn_p̄/dt = S_p·n_PBH − (σ[p̄ n→p]·X + σ[p̄ p→p]·(1−X))·n_B·n_p̄
dn_n̄/dt = S_n·n_PBH − (σ[n̄ n→n]·X + σ[n̄ p→n]·(1−X))·n_B·n_n̄
```

Uwaga: w kodzie to samo `S_π` zasila `π⁻` i `π⁺`, a kolumny „proton" i „neutron" zasilają `p̄` i `n̄`. Tak ma zostać.
Logarytmy gęstości hadronów są w kodzie obcinane od dołu na `−100` (w jednostkach GeV³).

**Przekroje** `σ·v` w mbarn (`v = c = 1`):
`π⁺ n→p: 1.7`; `π⁻ p→n: 1.5·F_π`; `K⁻ n→p: 26`; `K⁻ n→n: 34`; `K⁻ p→n: 31·F_K`; `K⁻ p→p: 14.5·F_K`;
`n̄ n→n: 37`; `n̄ p→n: 28`; `p̄ n→p: 28`; `p̄ p→p: 37`; `K0L n→p: 7`; `K0L n→n: 10`; `K0L p→n: 7`; `K0L p→p: 10`.
Czynnik kulombowski: `F_h(T) = z/(1 − e^(−z))`, `z = 2πα/v_e`, `v_e = sqrt(T/m_h) + sqrt(T/m_p)`, `h ∈ {π, K}`.

**Tabele** (pobierz z repozytorium autorów):
- `data/ext/N_around_m_e.csv`: `T [MeV], N_ρ, N_s`, 1000 wierszy; używana dla `T ≤ 10 MeV`; interpolacja liniowa w `ln T`, poza zakresem wartość brzegowa.
- `data/ext/N_s_from_PDG2024.csv` i `N_rho_OVER_N_s_from_PDG2024.csv`: `T [MeV], wartość`; dla `T > 10 MeV`; `N_ρ = iloraz × N_s`; interpolacja liniowa w `ln T`, poza zakresem wartość brzegowa.
- `T(ρ)`: kod buduje 1000 punktów `T` w geomspace `[1e-5, 1e3] GeV`, liczy `ρ = (π²/30)·N_ρ(T)·T⁴` i interpoluje liniowo `log10 T` po `log10 ρ` (z ekstrapolacją liniową).
- `data/out/hadrons_from_PBH.dat`: nagłówek i 100 wierszy; kolumny: masa [GeV], potem `S_π, S_K, S_K0L, S_p, S_n` [GeV]. Interpolacja liniowa w skali log–log z **ekstrapolacją liniową** poza tabelą (tabela zaczyna się od 1e9 g).

**Odczyt:** 10 000 punktów `a` w geomspace `[1, a_end]`; z rozwiązania `T` i `X`; interpolacja liniowa `X` po `Q/T`; wartość w `Q/T0` (oraz w `Q/T1`).

**Solver u autorów:** `AutoTsit5(Rosenbrock23())` z domyślnymi tolerancjami, arytmetyka 100-bitowa. Układ jest sztywny na początku (silne równowagowanie `X`). W gałęzi P użyj metody dla układów sztywnych i podaj tolerancje; jeśli możesz, podaj wyniki dla dwóch tolerancji.

## 4. Kotwice do sprawdzenia własnych przeliczeń (fizyka standardowa, nie wartości odniesienia)

`1 g = 5.609588604e23 GeV`; `1 s = 1.519267449e24 GeV⁻¹`; `1 mbarn = 2.568189464 GeV⁻²`;
`M_Pl = 2.435323459e18 GeV`; `m_Pl = 1.220890128e19 GeV`; `T_BH(1e9 g) = 1.05726e4 GeV`;
pierwszy wiersz tabeli hadronów ma masę `5.6096e32 GeV` (= 1e9 g);
dla `j = 22`: `t_f ≈ 1.443e-29 s`.

## 5. Zwrot

1. Odpowiedź na krok 0 i wybrana gałąź.
2. Tabela Q1–Q3 z pełną precyzją, z metodą korzeni, liczbą punktów β i tolerancjami.
3. Cały kod, który uruchomiłeś, i surowe wyjście.
4. Lista miejsc, w których opis z §3 różni się od kodu autorów albo jest niejednoznaczny.
5. Osobno i krótko: wątpliwości fizyczne wobec modelu, jeśli jakieś masz. Nie mieszaj ich z repliką.

Porównanie z wartościami odniesienia zrobi recenzent projektu spoza rodziny Claude. Statusów, kanonu i podpisu wykonawczego nie nadajesz — to należy do człowieka (Moderatora).
