# IW/NASH — REC10 ROT12
## Dokładna granica diamentowa: klasyczny reset Blocha a dopasowany pomiar Lüdersa

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P2-LT5-G2-CLASSICAL-TO-QUANTUM-TYPE-BRIDGE-001`  
**Klasa:** `PUBLIC_SAFE_INDEPENDENT_SCIENTIFIC_REFEREE`  
**Werdykt:** `PASS_WITH_EXACT_QUANTITATIVE_STRENGTHENING`  
**Autorytet:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`  
**BW:** `PENDING`

## 1. Źródła pierwotne

1. Geeky-S10, `research/geeky-s10/2026-10-23/geeky_s10_lt5_g2_lueders_vs_coaligned_reset_exact_nonmap_001.md`, odczytany blob `ca0e1b473a604fe064a0f86c2b5c8dd6bb1afc7d`.
2. LT5, `research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md`, odczytany blob `9c2a1362b4f763e23a51887d375d7d99771bcb78`.

Tożsamości kanałów, rozróżnienie typów i wynik NONMAP Geeky-S10 przechodzą niezależną kontrolę. Poniższe twierdzenie określa ścisłą ilościową rozbieżność dwóch map w konkretnym modelu jednego kubitu.

## 2. Twierdzenie o dokładnej normie diamentowej

Dla \(0\leq s\leq1\) zdefiniujmy:

- \(\mathcal Q_s\): unitalną, zachowującą ślad, hermitowską mapę liniową o macierzy Blocha \(T_Q=\operatorname{diag}(1-s,1,1)\);
- \(\Lambda_s\): legalny nieselektywny kanał instrumentu Lüdersa pomiaru \(\sigma_x\) o ostrości \(\mu=s\), \(T_\Lambda=\operatorname{diag}(1,\gamma,\gamma)\), \(\gamma=\sqrt{1-s^2}\);
- \(\delta=1-\gamma\).

Wtedy dokładnie:

\[
\boxed{\|\mathcal Q_s-\Lambda_s\|_\diamond
= \max\{s,s/2+\delta\}
=
\begin{cases}
s,&0\leq s\leq4/5,\\
s/2+1-\sqrt{1-s^2},&4/5\leq s\leq1.
\end{cases}}
\]

Ponadto norma operatorowa różnicy macierzy Blocha wynosi dokładnie \(s\), a największa norma śladowa różnicy wyjść dla niepowiązanego z ancillą pojedynczego kubitu wynosi również \(s\).

### Dowód

Rozważmy \(\mathcal D_s=\mathcal Q_s-\Lambda_s\). Jest to różnica map Pauliego, zatem można ją rozłożyć na superoperatory sprzężenia macierzami Pauliego:

\[
\mathcal D_s=a_0\,\mathrm{id}+a_x\,\mathrm{Ad}_X+a_y\,\mathrm{Ad}_Y+a_z\,\mathrm{Ad}_Z,
\]
gdzie
\[
a_0=\delta/2-s/4,\quad
a_x=-\delta/2-s/4,\quad
a_y=a_z=s/4.
\]

Ich suma jest zerem, zgodnie z faktem, że \(\mathcal D_s\) anihiluje identyczność. Ponieważ każdy superoperator sprzężenia unitarnego ma normę diamentową 1, nierówność trójkąta daje

\[
\|\mathcal D_s\|_\diamond\leq\sum_i|a_i|.
\]

Z kolei zastosowanie \(\mathcal D_s\otimes\mathrm{id}\) do znormalizowanego maksymalnie splątanego stanu Bella daje operator Choi diagonalny w bazie Bella o wartościach własnych \(a_i\). Jego norma śladowa wynosi \(\sum_i|a_i|\). Stąd górne ograniczenie jest osiągalne:

\[
\|\mathcal D_s\|_\diamond
=|\delta/2-s/4|+\delta/2+s/4+s/2.
\]

Dla \(0\leq s\leq1\), \(\delta\leq s\). Jedyna nietrywialna zmiana znaku \(a_0\) występuje przy \(\delta=s/2\), co po podstawieniu \(\delta=1-\sqrt{1-s^2}\) daje \(s=4/5\). To dowodzi wzoru odcinkowego.

Różnica macierzy Blocha to \(\operatorname{diag}(-s,\delta,\delta)\), a jej norma spektralna wynosi \(\max(s,\delta)=s\). Jej maksimum dla różnicy wyjść jednego kubitu jest osiągalne na stanach własnych \(X\). QED.

## 3. Kontrole niezależne

Zbudowano **od podstaw z macierzy jednostkowych** znormalizowany operator Choi mapy \(\mathcal Q_s-\Lambda_s\) (bez wpisywania z góry analitycznych wartości własnych). Dla sześciu wartości siły odczytu otrzymano:

| \(s\) | Norma diamentowa | Norma różnicy map Blocha |
|---:|---:|---:|
| 0,01 | 0,0100000000 | 0,01 |
| 0,10 | 0,1000000000 | 0,10 |
| 0,50 | 0,5000000000 | 0,50 |
| 0,80 | 0,8000000000 | 0,80 |
| 0,90 | 1,0141101056 | 0,90 |
| 1,00 | 1,5000000000 | 1,00 |

Wszystkie testy **PASS** z dokładnością numeryczną.

## 4. Porównanie z wcześniejszym twierdzeniem LT5

LT5 udowodnił dokładnie:
\[
\inf_{\Phi\ {\rm CPTP}}\|\mathcal Q_s-\Phi\|_\diamond=s/2.
\]

Kanał Lüdersa dopasowany do średniej odczytu **nie osiąga** tego globalnego optimum — różni się od \(\mathcal Q_s\) co najmniej o \(s\), czyli co najmniej dwukrotność odległości do najlepszego przybliżenia CPTP. Nie oznacza to niemożliwości innych legalnych instrumentów czy dopasowania na węższych rodzinach stanów.

## 5. Obowiązkowa bariera interpretacyjna

\(\mathcal Q_s\) **nie jest mapą CP** dla każdego \(s>0\). Jego porównanie z \(\Lambda_s\) wykorzystuje definicję normy diamentowej dowolnych superoperatorów liniowych. **Nie** jest to operacyjna odległość między dwoma istniejącymi fizycznymi urządzeniami, uprawniona procedura dyskryminacji kanałów ani twierdzenie, że \(\mathcal Q_s\) można stosować fizycznie do układu splątanego z ancillą.

Wynik jest dokładną kontrolą matematyczną błędnego transportu wniosków z modelu klasycznego do nieadekwatnego instrumentu kwantowego. Znane gospodarze: reprezentacja Blocha, twierdzenie Choi, normy całkowicie ograniczone i teoria instrumentów Lüdersa. **Nie deklaruje się nowości fizycznej ani matematycznej.**

## 6. Status i przekazanie

`SOURCE_REFEREE = PASS`, `NEW_QUANTITATIVE_GATE = PASS`, `ORIGINAL_MATHEMATICAL_NONMAP = MAINTAINED`.
Nie zmieniono źródła Geeky-S10, rękopisu LT5 ani kanonu. Nie wykonano walidacji instrumentu sprzętowego.

**Custody:** lokalny plik raportu i odczyt kontrolny PASS. Ponowne wywołania zapisu GitHub i doręczenia do Slack zostały zablokowane przez zabezpieczenia integracji. Poprzednie ROT10 i ROT11 również nie mają potwierdzonego zewnętrznego zapisu. BW ingestion oraz przyjęcie przez właściciela naukowego pozostają PENDING.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.

---
RECOVERY RECEIPT 2026-10-23: This body is now stored in GitHub with direct fetch/readback PASS; Slack routing to source thread SENT and thread READBACK PASS: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792743747866869. Any earlier BLOCKED marker is historical only. GitHub delivery != BW ingestion != owner scientific acceptance != CANON/EXEC.
