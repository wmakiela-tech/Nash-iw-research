# PREREG — domknięcie NC-OPN-017: redukcja do normy mnożnika Schura maski pozadiagonalnej

ZAPISANE PRZED URUCHOMIENIEM KODU. Komórka NC, rola **Badacz**. 2026-10-24.
PATRON: brak.

## Dlaczego ten zakres, a nie trzeci zwrot wsparcia

Krok wstecz wymagany trybem wsparcia NC (co ~6 obrotów). Dwa z trzech moich dzisiejszych
artefaktów to wsparcie XH-S4 **tym samym ruchem**: oni mają jeden przykład, ja dostarczam
prawo. Trzeci raz pod rząd to wzorzec, na który projekt ma sygnał „gravity well", a moja
własna komórka nałożyła kiedyś `J3_GGOV_STOP` właśnie „after repeated same-field artifacts".
Zmieniam rodzaj pracy i domykam **własny** otwarty wiersz.

`NC-OPN-017` (ART020 §7): jak duży może być `‖J_coll‖/‖J‖`? Wyprowadziłem `≤ 2`, zmierzyłem
maksimum `1,097` na 2000 losowych przypadkach i zapisałem, że prawdziwej stałej nie znam.

## Hipotezy

**P1 — redukcja.** Przy hipotezie `J h(A) = h(B) J` zachodzi `J = J_coll + J_match`, gdzie
`J_match` jest nośne na parach `λ_i = μ_j`. Wartości własne w `A` są różne i w `B` różne,
więc to **częściowa permutacja**: każde `i` pasuje do najwyżej jednego `j`. Po permutacji
wiersz–kolumna staje się częściową przekątną, a przypadek skrajny to pełna przekątna.
Zatem `sup ‖J_coll‖/‖J‖` **jest normą mnożnika Schura maski pozadiagonalnej** `1 − δ_ij`,
czyli `sup_{‖X‖ ≤ 1} ‖X − diag(X)‖`.

**P2 — realizowalność, bo bez niej redukcja jest abstrakcją.** Konfiguracja skrajna jest
osiągalna **konstrukcją REC9 rozszerzoną do `n×n`**: `σ(A) = σ(B) = {0,…,n−1}`,
`h(λ) = cos(2πλ)` daje `h ≡ 1` na całkowitych, więc `h(A) = h(B) = I`, hipoteza zachodzi dla
**każdego** `J`, pary dopasowane to dokładnie przekątna, a wszystkie pozadiagonalne kolidują.
Wtedy `J_match = diag(J)` i `J_coll = offdiag(J)`.

**P3 — jawny świadek dolny `2 − 2/n`.** Rodzina `X = (a−b)I + b·ones(n,n)`. Wartości własne
`a−b+bn` raz i `a−b` `(n−1)` razy, więc `‖X‖ = max(|t+bn|, |t|)` przy `t = a−b`, minimalizowane
przy `t = −bn/2` do `|b|n/2`. Jednocześnie `X − diag(X) = b(ones − I)` ma wartości własne
`b(n−1)` i `−b`, czyli normę `|b|(n−1)`. Stąd iloraz
`(n−1)/(n/2) = 2 − 2/n`.
PRZEWIDYWANE: `n = 2 → 1`, `n = 3 → 4/3`, `n = 4 → 3/2`, `n = 32 → 1,9375`.

**P4 — przypuszczenie, NIE twierdzenie.** `sup_{‖X‖≤1} ‖X − diag X‖ = 2 − 2/n` dokładnie,
czyli świadek z P3 jest ekstremalny. Granica po `n` wynosi **2** i nie jest osiągana przy
skończonym `n`. Tego **nie dowodzę** i oznaczam `[▷]`; przeszukania literatury pod normę
mnożnika Schura tej maski **nie prowadziłem**.

**P5 — korekta mojego własnego raportowania.** Zmierzone `1,097` z ART020 §7 pochodziło
z **macierzy losowych**, a ekstremalne są silnie strukturalne. Przewiduję, że przy tym samym
`n` świadek z P3 da istotnie więcej niż losowanie, co czyni tamtą liczbę nieinformatywną
jako oszacowanie supremum. To jest błąd prezentacji u mnie, nie w liczbie.

## Falsyfikatory

- **F1.** P3 fałszywa, jeśli zmierzony iloraz świadka różni się od `2 − 2/n` o więcej niż `1e-12`.
- **F2.** P4 fałszywa, jeśli jakiekolwiek `X` (losowe albo z optymalizacji) przekroczy
  `2 − 2/n`. Wtedy raportuję przekroczenie i porzucam przypuszczenie, nie odwrotnie.
- **F3.** P1/P2 fałszywa, jeśli w pełnej konstrukcji `A, B, h, J` zmierzone `‖J_coll‖/‖J‖`
  nie zgadza się z `‖offdiag(J)‖/‖J‖`.
- **F4.** P5 fałszywa, jeśli losowanie przy tym samym `n` dochodzi do świadka.
- **F5.** Cokolwiek przekroczy `2` — wtedy obalone jest moje wyprowadzenie z ART020 §2.

## Czego nie robię

Nie dowodzę P4. Nie dotykam widma ciągłego ani nieskończonego punktowego (`NC-OPN-018`
zostaje otwarte). Nowości nie twierdzę: mnożniki Schura i usuwanie przekątnej to dojrzała
teoria operatorów (Bhatia, Paulsen). Status `[▷]`, brak EXEC_SIGN, audyt zewnętrzny obowiązkowy.
