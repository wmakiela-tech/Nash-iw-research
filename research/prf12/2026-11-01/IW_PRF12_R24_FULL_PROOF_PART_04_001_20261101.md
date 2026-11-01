Obowiązuje również dla nierównego warunkowego prawdopodobieństwa par i dowolnie skorelowanych ξ między parami pod A, przy utrzymaniu warunkowej granicy hazardu i niezależności prywatnych losowań. Pod B standardowe niezależne przyrosty Lévy'ego zapewniają potrzebną własność. Nie jest to dowód źródłowej identyfikowalności przy arbitralnym adversarial ξ(t) bez granicy hazardu.

## 5. Wyniki weryfikowane dla modelu D i H

W tabeli η to prawdopodobieństwo niezależnej symetrycznej błędnej etykiety jednego odczytu; λ podane w jednostkach γ; dla resetu w dowolnej chwili stosujemy floor=0, a dla zmiany tylko między całymi strzałami floor=.31. Wszystkie liczby N wyznaczono skanem dokładnych ogonów dwumianowych przy jednym ustalonym progu ilorazu wiarygodności; są to **gwarantowane wystarczające liczebności dla tego wyboru testu**, nie minima po wszystkich progach ani po wszystkich urządzeniach.

| Scenariusz | η | λ/γ | Dolna a / górna b | Najmniejsza N dla wskazanego progu, oba błędy <5% | Decyzja A gdy K≥ | Górny budżet γ T_all |
|---|---:|---:|---|---:|---:|---:|
| Bez resetów i bez błędów etykiet | 0 | 0 | .576 / .526 | 1075 | 593 | 1965.44 |
| Tylko błędy etykiet | .01 | 0 | .5729904 / .5249704 | 1170 | 643 | 2139.13 |
| Reset wszędzie, rzadki | .01 | .01 | .5632399 / .5249704 | 1835 | 999 | 3354.96 |
| Reset wszędzie, umiarkowany | .01 | .02 | .5536612 / .5249704 | 3277 | 1768 | 5991.40 |
| Reset wszędzie, λ/γ=.04 | .01 | .04 | .5350074 / .5249704 | 26775 | 14191 | 48953.23 |
| Reset WYŁĄCZNIE między odczytami, ten sam konserwatywny hazard .04 | .01 | .04 | .5554496 / .5249704 | 2907 | 1571 | 5314.92 |

Użyto t_d=t_r=.05/γ, wspólnego zegara γΔ=.5, Ω/γ=10. Dla przykładu przy η=.01, λ/γ=.02: Pr_A(K<1768)≤0.0499591, Pr_B(K≥1768)≤0.0493994. Czasy w tabeli zawierają 2× czas detekcji i 2× reset sensora **na parę**. Nie uwzględniono wymiany źródła, kosztu kalibracji i sprzężenia z rzeczywistym detektorem.

## 6. Falsyfikatory i ograniczenia; ścisła separacja kontraktów

