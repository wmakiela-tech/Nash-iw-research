---
artifact_id: IW_BADACZ_LT7_ROT001_BOUNDED_CRITIQUE_REVIEW_045_20261102
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_BOUNDED_CRITIQUE_[▷] / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
responds_to: LT7 ROT001 (Slack 2 XI 12:42, prośba: ograniczona krytyka założeń o nierozróżnialności model/źródło i sufitu claimu)
target: research/lt7/2026-11-02/iw_lt7_rot001_cross_model_source_only_information_floor_001.md (commit d160a77)
---

# Krytyka LT7 ROT001: matematyka poprawna, przykład z Front B do przeetykietowania, prawdziwy przykład istnieje

**Status:** `[▷]`. Claude ocenia wynik komórki innej rodziny. To nie jest werdykt REC ani decyzja LT7.

## Werdykty

| punkt | werdykt |
|---|---|
| K1: (LT7.001), (LT7.002), przykład zabawkowy | **PASS** (klasyczne) |
| K2: kod i JSON | **PASS** z uwagą |
| K3: zastosowanie do Front B (`B_exec`/`B_sym`) | **DO KOREKTY**: para nie spełnia już założenia nierozróżnialności |
| K4: przykład z Front B, który założenie spełnia | **PROPOZYCJA** z liczbami |
| K5: sufit claimu i literatura | zgoda; uzupełnienie źródła |

## K1. Matematyka

- (LT7.001) jest poprawna. To skalarny przypadek „promienia informacji” z teorii złożoności informacyjnej.
  - Dla operatora o wartościach rzeczywistych promień lokalny równa się połowie średnicy zbioru możliwych
    wartości, a algorytm centralny to środek przedziału.
  - Tu zbiór zawiera indeks modelu: Traub i Woźniakowski, *A General Theory of Optimal Algorithms* (1980);
    Micchelli i Rivlin, *A survey of optimal recovery* (1977).
- **Ogólniejsza postać,** obejmująca też niejednoznaczność samego źródła:

      R* ≥ (1/2) sup { |T_m(s) − T_{m'}(s')| : Y(s) = Y(s'), m, m' ∈ M }.

  (LT7.001) to przypadek `s = s'`. Wartość `1` dla `Y₁ = s₁` w przykładzie zabawkowym wynika z tej postaci
  wprost: `s = (0, ±1)`, ten sam odczyt, model B.
- „Ostrość” zachodzi dla pełnego źródła. Przy częściowym `Y` dolna granica zwykle nie jest osiągana.
  Przykład z `Y_d` jest szczególny, bo jedna kombinacja liniowa wystarcza.
- (LT7.002) to dualność norm, poprawnie.

## K2. Kod

- `lt7_rot001_exact_controls.py` uruchomiony lokalnie daje JSON zgodny z opublikowanym po normalizacji
  (`sort_keys`).
- **Uwaga:** linie „negative control” (`assert i-i==0 and j-j==0`) są tautologiczne i niczego nie sprawdzają.
  Siatka 62 834 porównań sprawdza górne ograniczenie błędu estymatora środka. Dolna granica wynika z dowodu,
  nie z siatki; raport nie powinien sugerować, że siatka ją weryfikuje.

## K3. Zastosowanie do Front B: para `B_exec`/`B_sym` nie jest już niejednoznacznością modelu

- Założenie rozstrzygające (§2 raportu): obserwacja przy danym `s` jest ta sama w obu modelach, a oba modele
  są dopuszczalne.
- Po REVIEW_044 T1 (2 XI) i MT14 ROT023 (kod generatora BlackHawk) kolumny tabeli to sumy po stanach
  ładunkowych. Mapę wyznaczają więc dane źródła: semantyka tabeli, kod generatora i symetria C emisji.
- `B_exec` nie jest alternatywnym modelem fizycznym, tylko błędem interfejsu kodu, warunkowo na semantyce
  populacji w ODE. To dokładnie falsyfikator z §3 raportu LT7: „legalna, niezależna informacja o modelu”
  zeruje barierę.
- **Wniosek:** połowa różnicy `4.37e-4` w `X_nuc` ilustruje usuniętą niejednoznaczność, nie podłogę. Proponuję
  to przeetykietować.
- **Dobór celu:**
  - Liczby `X_nuc` pochodzą z punktu głęboko wykluczonego (`6e9 g`, `β = 1e-16`, `Y_P ≈ 1.32`), gdzie różnica
    map to `0.2%`.
  - Na konturze `χ² = 4`, który jest celem decyzyjnym Front B, ta sama zmiana mapy przesuwa granicę o
    `0.27–0.30 dex` (czynnik `~2` w `β`; REVIEW_038 E5).
  - Podłoga z (LT7.001) zależy od funkcjonału celu. Dla Front B właściwym celem jest położenie konturu.

## K4. Przykład z Front B, który spełnia założenie z konstrukcji

- **Prawa emisji poniżej `1e9 g`.**
  - Warianty różnią się tylko poniżej pierwszego wiersza tabeli, więc dane źródła (tabela) są identyczne
    dla każdego `m`.
  - Cel: położenie granicy `χ² = 4` w `log₁₀ β` przy ustalonej masie, w natywnym kodzie autorów.
  - Połowa rozstępu po wariantach (bisekcja z REVIEW_038/042, szum metody `~0.01 dex`):

| `m` [g] | `M = {native −1.20, OLS-8, T^{1.3}}` | `M = {OLS-8, T^{1.3}}` (bez artefaktu brzegu) |
|---|---:|---:|
| 1.121e9 | 0.024 | 0.010 |
| 1.187e9 | 0.027 | 0.007 |
| 1.256e9 | 0.018 | 0.006 |
| 1.330e9 | 0.015 | 0.007 |
| 1.448e9 | 0.019 | 0.004 |
| 1.577e9 | 0.014 | 0.003 |
| ≥ 1.767e9 | ≤ 0.006 | ≤ 0.005 |

- **Odczyt:**
  - Gdy dopuścić nachylenie kodu, „podłoga tylko z tabeli” dla lewej ściany wynosi `~0.015–0.03 dex`.
  - Po odrzuceniu nachylenia kodu jako artefaktu (REVIEW_042) spada poniżej szumu metody.
  - Stopnie swobody spoza SM poszerzyłyby `M`, w nieznanym stopniu.
- To instancja, w której (LT7.001) działa bez zastrzeżeń z K3. Proponuję ją jako przykład z Front B.

## K5. Sufit i literatura

- Zgoda z `NO_MATH_NOVELTY`. Proponuję dodać do literatury teorię złożoności informacyjnej (promień
  informacji): Traub, Wasilkowski, Woźniakowski, *Information-Based Complexity* (1988).
- Sufit `NO_PBH_BOUND` należy utrzymać. Liczby z K4 to rozrzut położenia konturu w modelu autorów, nie
  granica fizyczna.

## Reprodukcja K4

```text
python3 -I - <<'EOF'
import csv
def rd(p): return {int(r["j"]): float(r["boundary_log10beta"]) for r in csv.DictReader([l for l in open(p) if not l.startswith("#")])}
n=rd("research/badacz/2026-10-31/data/native_audit/e2_native.csv"); o=rd("research/badacz/2026-10-31/data/native_audit/e2_ols8.csv")
p=rd("research/badacz/2026-10-31/data/subedge_pilot/e2_p13.csv")
for j in sorted(n): print(j, round((max(n[j],o[j],p[j])-min(n[j],o[j],p[j]))/2,3), round(abs(o[j]-p[j])/2,3))
EOF
```

Wynik jest Claude'a; to ocena międzyrodzinowa, nie zewnętrzny audyt dla Claude'a.
