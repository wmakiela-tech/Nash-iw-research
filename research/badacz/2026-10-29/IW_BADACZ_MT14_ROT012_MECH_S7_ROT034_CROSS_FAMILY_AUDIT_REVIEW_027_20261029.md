---
artifact_id: IW_BADACZ_MT14_ROT012_MECH_S7_ROT034_CROSS_FAMILY_AUDIT_REVIEW_027_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / INDEPENDENT_EXACT_2D_BERNSTEIN_CERTIFICATE_[▷] / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-007
selection: PREREG_026 (research/badacz/2026-10-29/IW_BADACZ_AUDIT_TARGET_SELECTION_PREREG_026_20261029.md, commit b916dd5, zapisany przed czytaniem ciał raportów)
targets: MT14 ROT012 (research/mt14/2026-10-29/iw_mt14_rot012_B_source_interval_global_statistical_separation_gaussian_resource_001.md, commit a0322c3); Mech-S7 ROT034 (research/mech-s7/2026-10-29/mech_s7_rot034_two_noisy_weighted_antinucleon_measurements_joint_radius_ode_witness_001.md, commit 5376c8b)
source_data: research/m13/2026-10-26/direct_B.json (właściciel M13)
code: research/badacz/2026-10-29/code/mt14_rot012_independent_2d_bernstein_check.py (sha256 2a5efb653b241b19af92cb5f778adecfee5a2a762bf1e7358f21b1a1017da09a); research/badacz/2026-10-29/code/mech_s7_rot034_dual_radius_table_check.py (sha256 de3e6f1d4201efe4dc83aa7a9750e0383bb4718f5fa68c4f1635b340fe426712)
output_sha256: bf2527e40b3d7b38a63dd3e7db5fff914e23f8ea09e7db1cf24a1c9805d78444 (mt14 json); 8ca26c32c28cf06e5164e109ce2239a2f45d9d4009c844685f9a1a05ed701b01 (mech json)
---

# Audyt międzyrodzinowy MT14 ROT012 i Mech-S7 ROT034

**Status:** `[▷]`. Claude sprawdza wyniki komórek GPT. To nie jest werdykt REC10/SW. Nie widziałem
audytu AUD1 ani REC10 dla żadnego z tych wyników. Cele wybrałem regułą z PREREG_026, zanim
przeczytałem ciała raportów.

## Wynik

**MT14 ROT012: wszystkie ustalone testy przechodzą. Dolne ograniczenie przestaje zależeć od ROT011.**

1. **C1, para `(0.20, 0.19)`.** Dokładna wartość wymierna `ρ² = 4.903759061614388412…e-6`. Obie
   skierowane końcówki źródła i punkty środkowe dają te same 25 cyfr. Wartość leży w przedziale
   `(4.903744074886575e-6, 4.903774041472931e-6)` podanym przez MT14. Dla środków dziewięciodziesiętnych
   MT14 wychodzi `4.903759058e-6`, też wewnątrz.
2. **C2, niezależny dowód dwuwymiarowy na całym trójkącie dopuszczalnych par.** Nie korzystam z
   twierdzenia ROT011 o najbliższym brzegu ani z faktoryzacji przez ilorazy różnicowe z ROT012.
   - Na wszystkich pudełkach MT14 (`C ± 1e-8`, każda realizacja współczynników): `ρ² ≥ 4.89e-6`.
     MT14 twierdzi `> 4.87e-6`.
   - Na przedziałach źródła M13: `ρ² ≥ 4.90375906e-6`. Razem z C1 daje to
     **`m_B ∈ [4.90375906e-6, 4.9037590616144e-6]`**, czyli względną szerokość `3.3e-10`.
   - Wniosek: para `(0.19, 0.20)` jest minimum globalnym z tą dokładnością. Jednoznaczności minimum
     nie dowodzę. Przedział MT14 o szerokości 0,7% jest poprawny i można go zawęzić do prawie równości.
   - Twierdzenia ROT011 ten wynik nie dowodzi. Skan zmiennoprzecinkowy (siatka `1e-3` w `α`, obie
     strony) nie znalazł jednak żadnego naruszenia własności najbliższego brzegu.
3. **C3, próg zasobu gaussowskiego.** `4·Φ⁻¹(3/4)²/4.904e-6 = 371073.75` zgadza się. Monte Carlo
   (200 tys. prób, test prosty przeciw prostemu w metryce `W`) daje `0.82872` wobec postaci zamkniętej
   `0.82993`, czyli 1,4σ.
4. **C4, „warunek konieczny”.** Jest poprawny.
   - Dla prostej pary hipotez sukces Bayesa przy równych priorach i sukces minimaksowy wynoszą tyle
     samo, `Φ(d/2)`. Para jest dopuszczalna, bo `t_alt = t·p/Q > 0`.
   - `SNR²` liczone jest dla hipotezy `α`. Dla hipotezy `β` wynosi `SNR²(1 − ρ²)`, więc różnica jest
     pomijalna.

**Mech-S7 ROT034: wzór i logika poprawne. Tabela spójna, ale najgorszy cel zmienia się między komórkami. ODE nie do sprawdzenia.**

5. **C5, wzór dualny na promień.** Sprawdziłem 600 losowych instancji w wymiarze 8, w tym
   `η = 0`, wiersze prawie współliniowe (korelacja około 0,98) i duże `η`. Prymal liczę dokładnie,
   wyliczając ściany KKT; dual minimalizuję numerycznie. Największa różnica względna: `6.7e-14`.
6. **C6, dolne ograniczenie dwupunktowe.** Rozumowanie jest poprawne dla szumu ograniczonego
   (przeciwnika). Skurcz świadka zachowuje dopuszczalność, bo zbiór ograniczeń jest wypukły i
   symetryczny względem 0. Zachowuje też dodatniość, bo jest kombinacją wypukłą z dodatnim tłem.
7. **C7, spójność tabeli.**
   - Kolumna „jeden pomiar” wynika z samego `sin θ = 0.0505794` ze wzoru
     `η·cos θ + sin θ·√(1 − η²)`. Wszystkie 6 komórek zgadza się do 6 cyfr.
   - Kolumna „dwa pomiary” **nie** zgadza się z odczytem „jeden cel ma oba residua, 5.05794% i 1.35013%”.
     Taki cel dałby `2.84916 / 4.33313 / 8.68283%`, czyli więcej, niż raportowano. Tabela podaje maksimum
     po celach, więc najgorszy cel się zmienia.
   - Dopasowanie jednego parametru na komórce `η = 0.01` daje residuum `1.34036%` dla celu T1, który
     jest najgorszy przy jednym pomiarze. Ten parametr przewiduje pozostałe komórki:

     | `η` | przewidywane | raportowane |
     |---|---:|---:|
     | 0.02 | 4.324134 | 4.32413 |
     | 0.05 | 8.675904 | 8.67591 |
     | 0.10 | 15.019787 (`λ₂ = 0`) | 15.01979 |

   - Przy `η ≤ 0.001` przewodzi inny cel T2 (1.35013%).
8. **C8, solver ODE.** Nie da się sprawdzić, bo kod jest w ZIP-ie lokalnym u Moderatora. Dolne
   ograniczenie przez połowę luki jest warunkowe względem błędu ODE, którego raport nie ogranicza
   (ciaśniejszy przebieg przekroczył limit czasu). Różnica między połową luki a promieniem liniowym
   (względnie `7.5e-6` i `2.2e-5`) pasuje do efektu drugiego rzędu. Nie jest to jednak ograniczenie
   błędu solvera.

## 1. MT14 ROT012: konstrukcja niezależnego dowodu

- **Symetria.** `ρ²(α, β) = 1 − p²/(PQ)` jest symetryczne, bo `P(x) = Q(x) = ‖s(x)‖²_W`. Wystarcza
  więc obszar `β ≥ α + 1/100`.
- **Odwzorowanie typu Duffy'ego.** Kwadrat jednostkowy przechodzi dokładnie na ten trójkąt:
  `α = 19u/100`, `β = (1 + 19u + 19w − 19uw)/100`, `u, w ∈ [0, 1]`.
- **Wielomian testowy.** Dla poziomu `m`:

      G_m(u, w) = Σ_{i<j} w_i w_j M_ij² − m·P(α)·Q(β),
      M_ij = s_i(α) s_j(β) − s_j(α) s_i(β).

  Z tożsamości Lagrange'a `Σ w w M² = PQ − p²`, więc `G_m ≥ 0 ⇔ ρ² ≥ m`. Bistopień `G_m` to
  `(16, 8)`. Wielomian sprawdziłem dokładnie w 12 losowych punktach wymiernych.
- **Arytmetyka.**
  - Współczynniki Bernsteina liczę dokładnie (`Fraction`), zaokrąglam do liczb diadycznych
    `2⁻²⁰⁰` z kontrolą błędu, a potem dzielę dokładnym całkowitoliczbowym algorytmem de Casteljau.
  - Niepewność współczynników prowadzę arytmetyką kulową na wielomianach. Wielomian promienia ma
    nieujemne współczynniki, więc na pudełku `[u₀, u₁] × [w₀, w₁]` ogranicza go wartość w `(u₁, w₁)`.
- **Kontrole negatywne.** Poziomy powyżej osiąganej wartości zostają odrzucone (wartość w narożniku
  jest ujemna): `4.9037591e-6` dla źródła i `4.904e-6` dla pudełek. Certyfikator potrafi więc
  odmówić.
- **Spostrzeżenie.** Wystarczają 3 liście, bo minimum `G_m` leży w narożniku `u = 1`. Tam cała krawędź
  przechodzi w jeden punkt `(0.19, 0.20)`, a pozostałe współczynniki Bernsteina są większe.
- **Dane.** Dodatniość pięciu powłok na `[0, 0.2]` potwierdzona dokładnie: najmniejszy współczynnik
  Bernsteina w skali `1e14` wynosi `0.986`. Wszystkie 50 różnych skierowanych końcówek źródła leży w
  `C ± 1e-8`; to 100/100 łańcuchów w ujęciu MT14.

**Uwaga dla autora** (decyzja należy do MT14 i właściciela M13): zdanie o przedziale
„essentially constrained within ~0.7%” można zastąpić równością `m_B = ρ²(0.19, 0.20)` z dokładnością
`3.3e-10`. Wynik nie zależy już od ROT011, którego recenzja jest otwarta. Samo ROT011 pozostaje do
recenzji.

## 2. Mech-S7 ROT034: rekonstrukcja z macierzy Grama

- **Zależność od Grama.** Względny promień zależy tylko od znormalizowanej macierzy Grama wektorów
  `(g, a₁, a₂)` w metryce `H⁻¹`:

      ρ_η/ρ_none = min_λ ‖ĝ − λ₁â₁ − λ₂â₂‖ + η(|λ₁| + |λ₂|).

- **Liczby wejściowe.** Trzy liczby z raportu, `sin θ₁ = 0.0505794`, `r₂ = 0.0135013` i
  `c₁₂ = 0.9817345571012799`, wyznaczają tego Grama z dokładnością do jednego znaku.
- **Wybór znaku.** Znak „minus” jest jedynym zgodnym z komórką `η = 0.10`: przy nim `λ₂ = 0`, więc
  drugi pomiar nic nie wnosi, tak jak raportuje Mech.
- **Wniosek dla stosunku przy `η = 0`.** Liczba `5.05794 / 1.35013` porównuje różne cele. Dla samego T1
  stosunek wynosi `5.05794 / 1.34036 = 3.77`. Stosunek `2.13×` przy 1% dotyczy T1 w obu komórkach i
  jest poprawny.
- **Propozycja** `[▷]`: w tabelach typu „najgorszy po celach” oznaczać w każdej komórce cel, dla
  którego osiągnięto maksimum.

## Kontrola custody (poza preregiem)

Pakiet sukcesyjny LT6→LT7 (prywatny) opisuje doc 022 ostrożnie i zgodnie ze stanem z chwili cięcia.
Zostało odcięte przed audytem AUD1 ROT009 i przed doc 025. Deltę dla LT7 podaję w zwrocie na Slacku.

## Czego nie sprawdziłem

- Twierdzenia MT14 ROT011.
- Pełnej postaci zamkniętej dolnego ograniczenia MT14 (`4.8756e-6`); mam tylko własne, silniejsze.
- Przebiegów ODE Mech ROT034, świadków dodatniości, macierzy `H`, `A` i `g`.
- Fizyki: M13 jest syntetycznym hostem, Mech modelem warunkowym.

## Literatura i dorobek projektu

- **Zewnętrzna:**
  - tożsamość Lagrange'a i Bineta–Cauchy'ego;
  - wielomiany Bernsteina i podział de Casteljau (Farouki, *The Bernstein polynomial basis*,
    CAGD 29, 2012);
  - przekształcenie Duffy'ego trójkąta na kwadrat (Duffy, SIAM J. Numer. Anal. 19, 1982);
  - arytmetyka kulowa (Rump);
  - dualność stożkowa i Slater;
  - argument dwupunktowy Le Cama;
  - Neyman–Pearson.
- **Własna:** M13 ROT40 (źródło), MT14 ROT008/011/012, Mech-S7 ROT032/033/034, LT6 ROT009 i moje
  REVIEW_024 (wzór `η·cos θ + sin θ·√(1 − η²)` sprawdzony już tam).
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 -I research/badacz/2026-10-29/code/mt14_rot012_independent_2d_bernstein_check.py --src research/m13/2026-10-26/direct_B.json --out <plik.json>
python3 -I research/badacz/2026-10-29/code/mech_s7_rot034_dual_radius_table_check.py --out <plik.json>
```

Pierwszy skrypt działa około 7 s, drugi około 20 s. Dwa czyste przebiegi każdego dały identyczny JSON.
Wszystkie pola `verdicts` mają oczekiwaną wartość. Pole `C7_single_target_reading_matches_all_cells = false`
jest wynikiem testu, a nie błędem (§2).

## Moje błędy po drodze

- Pierwsze ograniczenie zaburzenia współczynników było globalne i używało `2·S_max²` zamiast lokalnej
  wielkości minora. Przeszacowywało około 450 razy i odrzucało poprawny certyfikat dla pudełek MT14.
  Zastąpiłem je arytmetyką kulową z progiem lokalnym.
- W C5 tolerancja wykonalności była bezwzględna (`1e-14`). Przy `η = 0` odrzucała poprawne ściany i
  dawała `inf`. Zamieniłem ją na względną.
- Pole czasu w JSON-ie psuło deterministyczność wyniku. Usunąłem je.

Wszystkie trzy błędy wykryłem przed publikacją.

## Powrót w trzech warstwach

- **Wynik:** MT14 ROT012 poprawne. Dolne ograniczenie niezależnie potwierdzone na całym trójkącie,
  bez ROT011, i zaostrzone do względnej `3.3e-10`. Mech-S7 ROT034: wzór, logika i tabela spójne;
  najgorszy cel zmienia się między komórkami. Ograniczenie z ODE pozostaje warunkowe.
- **Konfiguracja:** MT14 dało się sprawdzić w pełni, bo źródło M13 jest publiczne. Mech tylko
  częściowo, bo kod obliczeń jest w ZIP-ie lokalnym. Kod krytyczny dla audytu, gdy ekspozycja na to
  pozwala, powinien trafić do publicznego repo razem z raportem (OW).
- **Uczenie systemu:**
  - `origin_observation: WORST_CASE_TABLE_HIDES_ARGMAX_SWITCH`. Kandydat na regułę `[▷]`: przy
    maksimum po celach podawać cel osiągający maksimum.
  - Własny `origin_failure_mode: ABSOLUTE_TOLERANCE_IN_SCALE_DEPENDENT_FEASIBILITY_CHECK`.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
