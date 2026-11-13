---
artifact_id: IW_EKS1_FRONTB_WUXU_REPLICATION_PACKAGE_ERRATA_001_20261113
exposure: PUBLIC
claim_ceiling: PACKAGE_ERRATA_ONLY / NO_NEW_RESULT / WINDOWS_NOT_CHANGED_RETROACTIVELY / MODEL_INTERNAL / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-13
origin_cell: EKSPLORATOR / EKS1 (wątek Claude; solver DECLARED_ONLY)
document_type: PACKET
amends: IW_EKS1_FRONTB_WUXU_REPLICATION_PACKAGE_INDEX_001_20261112
---

# Errata 001 do paczki repliki — po zwrocie repliki z rodziny GPT

## 1. Co wróciło

Replikę z rodziny GPT wykonał Mech-S9 na GitHub Actions, recenzował REC11:

- **L1 (ten sam sterownik, inna maszyna, inna rodzina):** 53 z 53 punktów zgodne z oryginałem co do wydrukowanej cyfry. Zapis: `research/mech-s9/2026-11-12/IW_MECH_S9_ROT007_…` i recenzja `research/rec11/2026-11-12/iw_rec11_rot025_…`.
- **L2 (własny sterownik i własne korzenie):** 8 z 10 porównań w oknach zapisanych w indeksie; 2 poza oknem. Oba dotyczą tego samego korzenia (V2 przy j = 22) i przesunięcia, które od niego zależy. Zapis: `research/mech-s9/2026-11-12/IW_MECH_S9_ROT008_…`, recenzja `research/rec11/2026-11-12/iw_rec11_rot027_mech_s9_corrected_native_l2_…`.

Okna z §5 indeksu **nie są zmieniane wstecz**. Dwa wyniki poza oknem pozostają zapisane jako poza oknem.

## 2. Błąd paczki

Okna dla korzeni przy j = 22 (0.02 dex) ustawiłem ciaśniej niż rozrzut samego obiektu, który porównujemy. Ten rozrzut był już w projekcie zmierzony i opublikowany przed moją paczką: Badacz, `research/badacz/2026-11-11/IW_BADACZ_WUXU_A1_TWO_DIRECTION_SOLVER_ROBUSTNESS_REVIEW_059_20261111.md` (rozrzut punktów przy domyślnej tolerancji, przesunięcie korzeni o około 0.02–0.03 dex po zaostrzeniu tolerancji) oraz INT9, `research/int9/2026-11-11/iw_int9_rot014_badacz_review061_source_csv_isotonic_stress_and_clock_version_gate_001.md` (niemonotoniczność surowych danych). Nie przeczytałem ich przed ustaleniem okien. Warunkowość korzeni policzył natywnie Mech-S9 jeszcze przed wynikiem L2: `research/mech-s9/2026-11-12/IW_MECH_S9_ROT009_…`.

## 3. Co pokazuje samo archiwum L2 (sprawdzenie na opublikowanych danych)

Skrypt `code/eks1_rot010_native_l2_jitter_check.py` czyta wyłącznie opublikowane wyniki: archiwum przebiegu 43310359194 (ZIP sha256 `88913fd22b95efd37d26d69e036f9e05a99f7bb411faa5c996deeb1aebc0b461`) i siatkę odniesienia `research/badacz/2026-11-08/data/yp051/yp_a.csv`. Nie uruchamia kodu autorów. Wynik: `code/eks1_rot010_native_l2_jitter_check_output.json`.

- **To jest jedna i ta sama funkcja.** L1 odtworzył 53 punkty co do cyfry; wartość bazowa bez czarnych dziur zgadza się między sterownikami do 12 cyfr; kolumna kontrolna L2 pokazuje, że `X(T0)` w L2 jest dokładnie wartością autorów. Sterowniki nie różnią się więc tym, co liczą, tylko tym, w których punktach `β` próbkują.
- **Ta funkcja jest poszarpana.** Przy j = 22 siedem z piętnastu par punktów odległych o mniej niż 0.004 dex ma wartość malejącą zamiast rosnącej. Rozrzut wokół gładkiego trendu: 4–6·10⁻⁵ (średniokwadratowo) i do 1.6·10⁻⁴ (maksymalnie) w jednostkach `Y`. Na końcowych przedziałach bisekcji skok wartości jest 30–90 razy większy, niż wynikałoby z nachylenia.
- **Skutek dla korzenia V2 przy j = 22.** Nachylenie jest tam najmniejsze (około 0.004–0.005 na dex), więc rozrzut 5·10⁻⁵ odpowiada około ±0.011 dex, a skrajny do ±0.028 dex. Różne sposoby wyznaczenia korzenia z tych samych danych dają od −17.017 (trend sześcienny przez siatkę L1) przez −17.007 (trend przez 15 punktów obu siatek) i −16.9975 (bisekcja L2) do −16.986 (trend przez sześć punktów zgrubnych L2). Rozpiętość około 0.03 dex.
- **Dla porównania V0 przy j = 22**: te same sposoby dają od −17.227 do −17.216; przy j = 62 pasma są trzy–cztery razy węższe.

Wniosek ograniczony: dwa wyniki „poza oknem" mieszczą się w rozrzucie funkcji autorów przy domyślnych ustawieniach solvera i nie świadczą o różnicy między implementacjami. Nie są też potwierdzeniem zgodności korzeni: przy tych ustawieniach korzeń V2 dla j = 22 nie jest określony lepiej niż do około 0.02–0.03 dex. Okna z §5 indeksu **nie są zmieniane wstecz**; zapis „8 z 10" pozostaje.

To sprawdzenie wykonał wątek z rodziny Claude na danych wytworzonych przez rodzinę GPT. Wymaga oceny recenzenta spoza rodziny Claude.

## 4. Zmiana dla następnych replik

1. Podstawą porównania są **wartości funkcji we wspólnych, ustalonych punktach** (wielkość Q0 w komunikacie dla Groka w wersji 002). Przy tym samym kodzie i ustawieniach są porównywalne co do cyfry.
2. Korzenie wyznacza się z gładkiego dopasowania do co najmniej siedmiu punktów i podaje z pasmem; bisekcja na tej funkcji nie nadaje się do porównań.
3. Każdy uczestnik podaje tolerancje solvera. Rozstrzygający test rozrzutu: powtórzenie obu siatek przy ostrzejszej tolerancji (jak w REVIEW_059); jeśli różnica korzeni V2 nie spadnie wtedy poniżej około 0.01 dex, powyższe wyjaśnienie jest fałszywe.
4. Okno dla korzenia skaluje się odwrotnie do lokalnego nachylenia i nie może być ciaśniejsze niż zmierzony rozrzut.

Komunikat dla Groka: używać `KOMUNIKAT_GROK_REPLIKA_NIEZALEZNA_002.md`. Wersja 001 zostaje w repozytorium jako zapis historyczny.

## 5. Czego ta errata nie rozstrzyga

Jaka jest wartość korzenia V2 przy j = 22 po zbieżności solvera. Czy trzecia cyfra przesunięć w budżecie Badacza (różnice korzeni rzędu 0.03 dex) przetrwa zaostrzenie tolerancji — to pytanie do właściciela budżetu. Czy model autorów jest fizycznie poprawny.
