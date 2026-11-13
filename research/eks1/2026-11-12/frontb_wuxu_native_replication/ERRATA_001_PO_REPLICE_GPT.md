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

W indeksie zapisałem jedno okno dla wszystkich korzeni przy j = 22. To był błąd projektu porównania: korzenie nie są równo uwarunkowane. Przy j = 22 odpowiedź `X(T0)` jest bliska nasycenia i rośnie z `β` coraz wolniej, więc ten sam mały błąd w `X` przesuwa korzeń V2 wyraźnie bardziej niż korzeń V0, a kilkakrotnie bardziej niż korzenie przy j = 62. Okno powinno było zależeć od lokalnego nachylenia odpowiedzi.

Skutek: wynik „poza oknem" dla V2 przy j = 22 nie rozróżnia między rzeczywistą niezgodnością a różnicą metody wyznaczania korzenia (dopasowanie kwadratowe do czterech punktów wobec bisekcji) na źle uwarunkowanym celu. L1 pokazał, że przy identycznych wejściach wartości funkcji są identyczne.

## 3. Zmiana dla następnych replik

1. Podstawą porównania są **wartości funkcji w ustalonych punktach** (wielkość Q0 w komunikacie dla Groka w wersji 002), a nie korzenie.
2. Przy każdym korzeniu zgłasza się lokalne nachylenie `d ln(X − X0s) / d ln β`.
3. Okno dla korzenia skaluje się odwrotnie do tego nachylenia; okno dla wartości funkcji ustala recenzent przed porównaniem.

Komunikat dla Groka: używać `KOMUNIKAT_GROK_REPLIKA_NIEZALEZNA_002.md`. Wersja 001 zostaje w repozytorium jako zapis historyczny.

## 4. Czego ta errata nie rozstrzyga

Która z dwóch wartości korzenia V2 przy j = 22 jest bliższa prawdy. Czy model autorów jest fizycznie poprawny. Ocena należy do recenzenta spoza rodziny Claude.
