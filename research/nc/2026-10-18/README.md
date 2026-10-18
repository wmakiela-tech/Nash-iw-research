# NC — zwroty z 2026-10-18

Zewnętrzna, niezależna komórka Claude (NC). Rola: audyt, prior-art subtraction, wkład matematyczny.

**STATUS CAŁOŚCI: `[▷]` — nierecenzowane.** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`

EXEC_SIGN jest ludzki; żaden wynik stąd nie wchodzi do claimu ani artykułu bez uruchomienia kodu,
proweniencji i zatwierdzenia Moderatora. **Audyt zewnętrzny obowiązkowy** per ANTI-SELF-SEALING —
nie mogę wystawić go sobie sam.

Autorstwo monografii i wszelkie decyzje redakcyjne należą do LT4. Zwroty 004–007 audytują jej tekst;
008–009 nie są audytem, tylko próbą rozwiązania problemu, który monografia stawia jako otwarty
(§7.5b.5 — czujnik oddziałujący zwrotnie na układ).

## Zwroty

| plik | treść | sha256 |
|---|---|---|
| `IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018.md` | minimaks dla czujnika oddzialujacego zwrotnie (problem otwarty par. 7.5b.5): postac zamknieta, prog dopuszczalnosci, nieciaglosc optymalnego wzmocnienia | `1d78b2d21db4ae744ad3d991493ee0555d8876bc2809f10d3507cc1b74c30f4a` |
| `IW_NC_LT4_FOUR_MISSING_WITNESSES_006_20261018.md` | cztery skonstruowane swiadki, w tym jadro analityczne na (0,inf) o WSZYSTKICH momentach zerowych (nieoznaczonosc Stieltjesa) | `e9121b989043c4d76e6e3ed62546239cc7184d0c811ba6a1e6eb8363b9ea0833` |
| `IW_NC_LT4_NONMAP_LAYER_AUDIT_005_20261018.md` | audyt warstwy non-mapow jako klasy: 96 zdan negatywnych, 44 ze swiadkiem, probka 10 swiadkow zweryfikowana 10/10, 12 dziur ze wzorcem na granicach rezimu | `8eeb5bc1da55b18f667f9a17eecfe389ebc2ed2441517b0dad2a65594f84427b` |
| `IW_NC_LT4_PRIOR_ART_SUBTRACTION_FULL_MANUSCRIPT_004_20261018.md` | prior-art subtraction calej monografii: 68 obiektow numerowanych; po odjeciu gospodarzy i dwoch demotacjach zostaje 5 kandydatow do hierarchii B; 7 niecytowanych gospodarzy | `2d5303803b88c20511c8dc6a8ff425db2a56804623bfc5877db43764600c215a` |
| `IW_NC_LT4_TWELVE_HOLES_FINAL_DISPOSITION_007_20261018.md` | domkniecie dwunastki: 6 swiadkow, 3 odsylacze wewnatrz manuskryptu, 1 przeredagowanie, 1 cytowanie, 2 otwarte | `05e35659aae944a9ecdeab5f747a1db2940edffe173f6ff32162a32148adbcbb` |
| `IW_NC_SACRIFICIAL_MEASUREMENT_AND_PROTOCOL_CEILING_009_20261018.md` | sufit niezalezny od protokolu M < 1/gamma (dowod elementarny) oraz pomiar OFIARNY: zysk 1.9x przy ograniczonych czasach pomiaru | `577617b58c05bed8a0aa34323a9e0378bdd30b8f312bf83368bea309f597630e` |

## Kod

Reguła przyjęta po własnym błędzie z 11–12 X: **bez tekstu interpretacyjnego w `print`** —
skrypty drukują wyłącznie tabele, odczyty dopisywane są po fakcie. `PREREG_DELAY.md` to
prerejestracja zapisana i zahaszowana PRZED uruchomieniem kodu, który opisuje.

| plik | sha256 |
|---|---|
| `code/PREREG_DELAY.md` | `3fc3386a23f25ab70269950beaf7bce232f9d3ae31afcc20af9de5658d54cb18` |
| `code/backaction.py` | `3a9c197274d4b99ba72db335ab52ec8e43d0f5c1b392372aa0290c4e171f9775` |
| `code/bridge.py` | `34848e5a1ec64fdd73ac99dc224fe0d4221d9e06b79733a7a0df66211e26ced5` |
| `code/cont.py` | `f7bac31c63b846a869bb4c8ad38047732ad96a6a8d186ea4d08ba8429a4af54d` |
| `code/cont2.py` | `b5e6677f8c737d98d26541a437fa018d8c2ce53d0784a5203bd1d1b4902d2dd2` |
| `code/delay.py` | `cccbc2a79d96dc2b2ec24f36c9403129ac076da2eae1d6ff18c39124e82c1fbf` |
| `code/holes.py` | `a20b843fa9fa812f426e2ac819da4e14f09ed0fbf55919fab58992f4cc760d76` |
| `code/logn.py` | `22db7c3c3bfc0f66dea5eb4178084e1f12ffa1a779d1a668d81f8562f7e30433` |
| `code/multi.py` | `5b94fb6c0e8e1f438e1c71b289ff20480a25632e531b873ca8a868279137a165` |
| `code/repair.py` | `d66137c80715f62e677e6a9a63ffd8a126f173ba46557e55dfb31e3b83549f14` |
| `code/resolv.py` | `5b9fa52e1c5deedf1295290d801a09b6b9803e10cbe229f58683ec36ff8ba5ae` |
| `code/semi.py` | `d6b800c835f86cb1527acf3cd01e22bd01dc308d5123661d0a41fd832ca2d6d5` |
| `code/sharp.py` | `7c5cc996aab3cc25d0971d6789e4d886141a9ccd255ecfcb81be5894ead5d40d` |
| `code/twin.py` | `bbe9464dbf5fd00ccaadc795b601425b341d334a82887ff472e9f3c62b387f3b` |
| `code/witness.py` | `4aa74e161e6714b671c666d852ddec3162e54a4bdbb7f750104bc4fb90bbfc1c` |

## Błędy własne zapisane w tych zwrotach

Zapisane celowo. Są materiałem (error-as-data), a bez bazowej stopy błędu audytor kalibruje się źle:

- oszacowanie transportu spektralnego przez **supremum** bloków kolizyjnych — **FAŁSZYWE**,
  obalone kontrprzykładem LT4 (poprawna wielkość to norma **sumy**), wycofane; jego wersję
  potwierdziłem potem na ~11 900 układach, 0 naruszeń;
- wniosek, że kinetyka dyssypatywna pociąga ujemną normę logarytmiczną — **ODRZUCONY**
  kontrprzykładem M13 (generator Metzlera, masa maleje, a `mu2 = +0.3155`);
- falsyfikator momentowy zgłoszony jako nowy — okazał się **REKONSTRUKCJĄ** Tw. 8 rozdz. 1;
- **trzy claimy o tym, czego manuskrypt NIE MA**, postawione z pośrednika (regex, plan
  redakcyjny, liczba znaków) zamiast z tekstu;
- predykcja `a* = 2/(gamma t_s)` — **FAŁSZYWA**; pominięty człon współrządzi optimum;
- przewidywanie optymalnej liczby pomiarów `k > 1` — **FAŁSZYWE**, optimum to `k = 1`
  przy swobodnych czasach.

Dwie reguły proceduralne zaproponowane po tych błędach, do decyzji Moderatora:

1. **Claim o BRAKU jest claimem numerycznym** i wymaga podania miejsca, narzędzia oraz
   walidacji narzędzia na elemencie znanym jako obecny. Streszczenie manuskryptu nie jest
   dopuszczalnym źródłem dla claimu o braku.
2. **Przed wysłaniem OSZACOWANIA** trzeba skonstruować konfigurację oddzielającą je od
   najbliższego fałszywego wariantu i podać parametr oddzielający. Rodzina testowa
   zdegenerowana w tym parametrze nie dowodzi niczego, choćby przechodziła w 100%.
