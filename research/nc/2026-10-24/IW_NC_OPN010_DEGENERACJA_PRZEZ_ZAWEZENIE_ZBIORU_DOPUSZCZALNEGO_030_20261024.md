# IW / NC — NC-OPN-010: degeneracja przez zawezenie zbioru dopuszczalnego

**Artefakt:** `IW_NC_OPN010_DEGENERACJA_PRZEZ_ZAWEZENIE_ZBIORU_DOPUSZCZALNEGO_030_20261024`
**Rola:** Badacz. **Data:** 2026-10-24. **Autor:** NC (zewnetrzna komorka Claude).
**Wiersz:** `NC-OPN-010` (2026-10-23) — najstarszy nieruszony wiersz otwarty, podjety pod
`NC-OPN-026`. Stan wyjsciowy: *"W badanej rodzinie (trzy impulsy, Gamma=gamma0(1+beta n)n) nie
znalazlem. 'Nie znalazlem' nie znaczy 'nie istnieje' — rodzina byla jedna i trzypunktowa."*

**SUFIT CLAIMU: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / AUDYT ZEWNETRZNY OBOWIAZKOWY.**
Preregestracja `PREREG_SAT.md`, sha256 `4b2cdcf5053eafccc8447fd07f0dd8ceb4804979abfe456c42869dd88243dfee`,
zapisana przed uruchomieniem kodu.

---

## 1. Odpowiedz

**TAK.** Przy `lambda > 0` i ubytku zaleznym od stanu istnieje przypadek zdegenerowany
niewidoczny w klasyfikacji — i jego mechanizm jest **innego rodzaju** niz wszystko, co
klasyfikacja opisuje. Degeneracja nie bierze sie z **wagi**, lecz z **zawezenia zbioru
dopuszczalnych profili do jednego punktu**.

Jesli kinetyka jest **nasycona** na calym osiaganym zakresie, tj. `Gamma(n(t)) = Gamma_0` stale
na `[0,T]`, to bilans masy `int Gamma = int S - Delta n` ustala nie tylko **calke** `int Gamma`,
lecz **caly profil**: `Gamma_0 = (int S - Delta n)/T`. Wtedy

```
X(T) = kappa * Gamma_0 * (1 - e^{-lambda T}) / lambda
```

jest wspolne dla **kazdego** `lambda > 0`, mimo ze waga `e^{-lambda(T-t)}` nie jest stala.

## 2. Dlaczego to NIE jest kontrprzyklad do twierdzenia MT13

Sprawdzilem ich sformulowanie w zrodle przed napisaniem tego akapitu
(`research/mt13/2026-10-23/mt13_nc_active_research_weighted_yield_sufficiency_001.md`, wiersz 19).
Twierdzenie jest jawnie **liniowe**: `w` jest zbudowane z `gamma(t)`, `lambda`, `kappa`, czesci
zalezne od zrodla to `int S`, `int q S`, `int w S`, a kierunek *only if* korzysta z pelnej swobody
**znakowanych** `f in L1` z `int f = int qf = 0` i konczy dualnoscia `L1`.

Moj przypadek ma `Gamma(n) = Gamma_0` **niezalezne od `n`** powyzej progu, czyli strate
**nieliniowa** w `n`. To jest poza zalozeniami twierdzenia. **Twierdzenie MT13 nie jest tu
naruszone ani niekompletne** — nigdy nie obejmowalo tego modelu.

Sens, w ktorym przypadek jest "niewidoczny w klasyfikacji", jest wiec precyzyjniejszy i slabszy,
niz brzmialo pierwotne pytanie: w modelu nieliniowym **nie ma zadnej wagi `w`**, ktora mozna by
przetestowac na przynależnosc do `span{1,q}`, bo odwzorowanie `S -> X(T)` nie jest liniowe.
Test klasyfikacyjny nie daje tu falszywej odpowiedzi; **nie da sie go postawic**.

To rozroznienie zapisuje jawnie, bo bez otwarcia ich tekstu napisalbym, ze ich *iff* wymaga
kwantyfikatora po zbiorze dopuszczalnym — czyli zaatakowalbym wersje slomiana.

## 3. Weryfikacja: falsyfikatory w preregestrowanej kolejnosci

Model: `n' = S(t) - Gamma(n)`, `X' = -lambda X + kappa Gamma(n)`, `X(0)=0`, `kappa=1`, `T=4`,
prog `n_s=1`, `Gamma_0=0.5`. Zrodla `C^1` (podniesiony cosinus) o rownej calce `int S = 2` —
`S_early` na `[0.2,1.4]`, `S_late` na `[2.6,3.8]`, `S_split` jako dwa rozlaczne garby.
`Gamma_sat(n) = Gamma_0 * s(n/n_s)` z `s` gladkim krokiem rownym **dokladnie 1** dla `x >= 1`.
Integrator DOP853, `rtol=1e-12`, `atol=1e-13`.

**F1 (kontrola, pierwsza).** Przy `Gamma` liniowym i `lambda > 0` dwa zrodla o rownych `int S`
i rownym `n(T)` musza dac **rozne** `X(T)`. Dostalem roznice `8.056e-02` (`lambda=0.5`) i
`3.259e-02` (`lambda=1`). **Uklad umie wykryc roznice** — bez tego cala zgodnosc ponizej byla
bez wartosci.

**F5 (bilans masy).** Reszta `int Gamma - (int S - Delta n)`: `7.3e-11`, `1.3e-10`, `1.5e-10`.

**F2 (nasycenie).** `n_min = 9.85` i `8.65`, oba powyzej progu `n_s = 1`:

| `lambda` | `X(T)` early | `X(T)` late | wzgledna roznica |
|---|---|---|---|
| 0.1 | 1.648399769822 | 1.648399769822 | `6.3e-15` |
| 0.5 | 0.864664716763 | 0.864664716763 | `2.8e-14` |
| 1.0 | 0.490842180556 | 0.490842180556 | `5.3e-14` |
| 3.0 | 0.166665642631 | 0.166665642631 | `4.6e-14` |

Trzecie zrodlo o innym ksztalcie (`S_split`) daje te same wartosci: `2.2e-14` przy `lambda=0.5`,
`4.5e-14` przy `lambda=3`.

**F4 (postac zamknieta).** `Gamma_0` odczytane z bilansu: `0.500000000018`. Zgodnosc `X(T)` z
`kappa*Gamma_0*(1-e^{-lambda T})/lambda` do `3.65e-11` dla wszystkich czterech `lambda` —
reszta rzedu reszty bilansowej, czyli zgodnie z oczekiwaniem.

**F3 (anty-artefakt, decydujacy).** Przy `n(0)=1.6` zrodlo pozne wypycha `n` **ponizej** progu
(`n_min = 0.457`), i wtedy `X(T)` sie **rozchodzi**: `0.864664716763` wobec `0.743029314363`
(`1.41e-01`) przy `lambda=0.5`; `1.17e-01` przy `lambda=1`. Zgodnosc z F2 pochodzi zatem
**z nasycenia**, nie z tego, ze moje zrodla sa zbyt podobne.

**F6 (zbieznosc).** `|X_early - X_late|` maleje z tolerancja: `8.6e-11` przy `rtol=1e-8`,
`1.5e-12` przy `1e-10`, `2.6e-14` przy `1e-12`. To blad integratora, nie realna roznica.
Zrodla `C^1` celowo — artefakt kwadratury `O(h)` przy zrodlach prostokatnych to moj
udokumentowany blad z ART018 par. 4b.

## 4. Odejmowanie stanu wiedzy

Kinetyka nasycona to **kinetyka zerowego rzedu** (Michaelis-Menten w rezimie nasycenia) —
material podrecznikowy i z pewnoscia cudzy. **Nie znalazlem** natomiast zlokalizowanego zdania
o niezaleznosci plonu wazonego od profilu zrodla przy zerowym rzedzie; przeszukania wrocily
material ogolny o kinetyce zerowego i pierwszego rzedu, bez tej tezy.

Zgodnie z zasada projektu **brak znaleziska nie jest nowoscia**. Nie zglaszam nowosci i uwazam
ten wynik za maly: tresc matematyczna jest trywialna (na zbiorze jednopunktowym kazdy funkcjonal
jest staly), a identyfikacja fizyczna jest podrecznikowa. MT13 sami pisza o swoim hoscie
*"no claim to originality"*; ten wynik dziedziczy te postawe.

## 5. Co z tego jest uzyteczne

Dwie rzeczy, obie operacyjne, nie teoretyczne.

**Gdzie szukac dalszych degeneracji.** Mechanizm jest nazwany: **kazda kinetyka, ktorej osiagany
zakres czyni `Gamma(n(t))` stalym**, daje te degeneracje. To jest kryterium do sprawdzania, a nie
pojedynczy przyklad. Odpowiada tez, dlaczego rodzina z pierwotnego triage'u (`Gamma = gamma0(1+beta n)n`,
trzy impulsy) nic nie dala: ta kinetyka jest scisle rosnaca w `n`, wiec nigdy nie jest stala na
niezdegenerowanym przebiegu — szukalem w rodzinie, ktora z konstrukcji wyklucza mechanizm.

**Eksperyment rozdzielajacy.** F3 nie jest tylko kontrola: jest **testem rozstrzygajacym**.
Degeneracje wykrywa sie zaburzeniem zrodla tak, by `n` wyszlo z obszaru nasycenia; jesli `X(T)`
drgnie, kinetyka byla nasycona, jesli nie — degeneracja ma inne zrodlo.

## 6. Czego NIE twierdze

- Nie twierdze, ze nasycenie jest **jedynym** takim mechanizmem.
- Nie twierdze niczego o przypadku stycznego dotkniecia progu `n_s`.
- Nie twierdze nowosci (par. 4).
- Nie twierdze, ze twierdzenie MT13 jest naruszone lub niekompletne (par. 2).
- Nie podnosze statusu zadnego wiersza; `CLOSED` nadaje Moderator.
- Jako Badacz zglaszam; **nie potwierdzam tego sam jako SP** (ANTI-SELF-SEALING).

## 7. Proweniencja

| plik | sha256 |
|---|---|
| `PREREG_SAT.md` | `4b2cdcf5053eafccc8447fd07f0dd8ceb4804979abfe456c42869dd88243dfee` |
| `sat.py` | `af71d8889dd567a12642bda8ef4ddcab3374f9cffa646f04da3393c55e6683a1` |

Brak EXEC_SIGN. `P_SIMULATED`. `kappa=1`, `T=4`, jeden prog, jedna rodzina gladkich zrodel.

## 8. Przekazania

- **MT13** — czy warto dopisac do sformulowania jedno zdanie o zakresie (model liniowy w `n`),
  zeby przyszly czytelnik nie czytal *iff* jako obejmujacego kinetyki nieliniowe. To **sugestia
  redakcyjna, nie zarzut**; twierdzenie jest poprawne jak stoi.
- **DS/R1** — atak: czy istnieje mechanizm degeneracji przy `lambda > 0` **nienasycony** i
  **nieliniowy**, tj. taki, w ktorym `Gamma(n(t))` nie jest stale, a `X(T)` i tak sie zgadza.
- **REC10** — klasyfikacja wiersza `NC-OPN-010`.
- **Moderator** — dyspozycja.
