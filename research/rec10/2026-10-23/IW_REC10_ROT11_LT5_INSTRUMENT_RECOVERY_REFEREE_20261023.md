# IW/NASH — REC10 ROT11
## Niezależna recenzja instrumentów kwantowych LT5 i dokładny błąd korekcji

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P2_LT5_QUANTUM_INSTRUMENT_BRANCH_FEEDBACK_001`  
**Klasa:** `PUBLIC_SAFE_INDEPENDENT_REFEREE`  
**Werdykt:** `PASS_WITH_EXACT_STRENGTHENING`  
**Autorytet:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`

### 1. Podstawy źródłowe i zakres

Przeczytano i oceniono bezpośrednio następujące materiały GitHub projektu:

1. `research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md` — odczytany blob `9c2a1362b4f763e23a51887d375d7d99771bcb78`.
2. `research/lt5/2026-10-23/lt5_same_channel_same_povm_distinct_instrument_exact_causal_recovery_001.md` — blob `6b80223b97856bdce42a19f13e4bdbfb6990befb`.
3. `research/lt5/2026-10-23/lt5_rev020_manuscript_impact_gap_audit_001.md` — blob `e25ecbc6a218065f84ecba3529e4fb26134e037f`.

Właściciel LT5 prosił o kontrolę konkretnych twierdzeń — nie o akceptację całej monografii.

### 2. LT5 obrót 6 — kontrola Choi i diamentowej odległości

Dla formalnego przejścia Blocha \(T_s=\mathrm{diag}(1-s,1,1)\), \(0<s\leq1\), znormalizowane wartości własne macierzy Choi wynoszą dokładnie
\[
1-s/4,\quad -s/4,\quad s/4,\quad s/4.
\]
Przejście zachowuje dodatniość dla pojedynczego kubitu, ale nie jest całkowicie dodatnie, ponieważ \(-s/4<0\).

**PASS** dla dokładnej odległości
\[
\inf_{\Phi\;\mathrm{CPTP}}\|\mathcal Q_s-\Phi\|_\diamond=s/2.
\]
Ujemny kierunek Choi daje dolną granicę, a jawna mieszanina kanałów Pauliego \(\Phi_s=(1-s/2)\mathrm{id}+(s/4)\mathrm{Ad}_{\sigma_y}+(s/4)\mathrm{Ad}_{\sigma_z}\) osiąga tę granicę. Legalne domknięcie na ograniczonej rodzinie stanów jest oddzielnym zagadnieniem; brak globalnej CP nie oznacza zakazu wszystkich realizacji częściowych. Legalny instrument Lüdersa ma wynik Bornowski, nie deterministyczny klasyczny odczyt z arbitralnym szumem ograniczonym.

### 3. LT5 obrót 7 — kontrola instrumentów

Niech \(Z=\sigma_z\), \(p\in[0,1]\), a
\[
\Lambda_p=(1-p)\mathrm{id}+p\mathrm{Ad}_Z.
\]

Źródło definiuje instrument z prawdziwą flagą błędu
\[
\mathcal F_0=(1-p)\mathrm{id},\quad
\mathcal F_1=p\mathrm{Ad}_Z
\]
oraz instrument z niezależną monetą
\[
\mathcal C_0=(1-p)\Lambda_p,\quad
\mathcal C_1=p\Lambda_p.
\]

Oba są legalnymi instrumentami CP, mają wspólny kanał nieselektywny \(\Lambda_p\) i te same efekty POVM:
\(E_0=(1-p)I\), \(E_1=pI\). Flaga w \(\mathcal F\) ujawnia faktycznie zastosowaną operację. W \(\mathcal C\) jest niezależna od operacji.

**PASS** dla dokładnej korekcji \(\mathcal F\) przez warunkowe \(\mathrm{id}\) lub \(\mathrm{Ad}_Z\). **PASS** dla niemożności doskonałego skorygowania \(\mathcal C\) przy \(0<p<1\). **PASS** dla dokładnej normy diamentowej instrumentów z zachowanym rejestrem:
\[
\|\widehat{\mathcal F}_p-\widehat{\mathcal C}_p\|_\diamond=4p(1-p).
\]

### 4. NOWE dokładne wzmocnienie — pełne optimum korekcji \(\mathcal C\)

**Twierdzenie.** Niech \(\widehat{\mathcal C}_p\) będzie kanałem od kubitu do jego rejestru klasycznego oraz zachowanego kubitu. Minimum przebiega po **wszystkich** CPTP operacjach korekcji \(\mathcal R\) z obu rejestrów do jednego kubitu, także warunkowych i używających pomocniczych układów. Wtedy
\[
\boxed{
\inf_{\mathcal R\ \mathrm{CPTP}}
\|\mathcal R\circ\widehat{\mathcal C}_p-\mathrm{id}\|_\diamond
=2\min(p,1-p).
}
\]
Dla \(\widehat{\mathcal F}_p\) analogiczne optimum jest zerowe.

**Dowód dolnej granicy.** Wybierz ortogonalne stany
\(\rho_\pm=(I\pm\sigma_x)/2\).
Ich obrazy po \(\widehat{\mathcal C}_p\) mają odległość śladową
\(D=|1-2p|\), ponieważ losowa moneta jest niezależna od stanu, a kanał \(\Lambda_p\) tłumi składową \(x\) przez \(1-2p\).

Dla dowolnej korekcji CPTP \(\mathcal R\) kontraktywność normy śladowej zapewnia
\[
\|\mathcal R\widehat{\mathcal C}_p(\rho_+)-
\mathcal R\widehat{\mathcal C}_p(\rho_-)\|_1
\leq 2|1-2p|.
\]
Jeżeli \(\delta=\|\mathcal R\widehat{\mathcal C}_p-\mathrm{id}\|_\diamond\), to z nierówności trójkąta dla dwóch stanów ortogonalnych:
\[
2\leq2\delta+2|1-2p|.
\]
Stąd
\[
\delta\geq1-|1-2p|=2\min(p,1-p).
\]

**Dowód osiągalności.** Wystarczy odrzucić niezależną monetę. Dla \(p\leq1/2\) nie stosuj żadnej korekcji; powstaje \(\Lambda_p\) o błędzie diamentowym \(2p\). Dla \(p\geq1/2\) zastosuj globalnie \(\mathrm{Ad}_Z\), uzyskując błąd \(2(1-p)\). Wynika to z \(\|\mathrm{id}-\mathrm{Ad}_Z\|_\diamond=2\). Osiągamy dolne ograniczenie. QED.

**Granica modelu:** jedno użycie instrumentu na jednym kubicie, dostęp do jego klasycznego wyniku i pozostałego kubitu oraz późniejsza dowolna korekcja CPTP. Nie dopuszcza się wstępnego kodowania na wielu kubitach, nowych kopii, informacji o środowisku poza tą flagą ani dodatkowej przyszłej dynamiki.

### 5. Niezależny test macierzowy

Skontrolowano w NumPy dziewięć wartości \(p\in\{0,0.01,0.1,0.25,0.5,0.75,0.9,0.99,1\}\).
Sprawdzono sumy gałęzi kanałów, odwracanie dla \(\mathcal F\), kontrakcję odległości ortogonalnych stanów dla \(\mathcal C\), a także świadectwo osiągnięcia \(2\min(p,1-p)\). **9/9 PASS**.

| p | Najmniejszy błąd korekcji instrumentu F | Najmniejszy błąd instrumentu C | Różnica instrumentów w normie diamentowej |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0.10 | 0 | 0.20 | 0.36 |
| 0.25 | 0 | 0.50 | 0.75 |
| 0.50 | 0 | 1.00 | 1.00 |
| 0.75 | 0 | 0.50 | 0.75 |
| 0.90 | 0 | 0.20 | 0.36 |
| 1 | 0 | 0 | 0 |

Test macierzy stanów jest pomocniczy; pełną normę diamentową zapewnia wyżej przedstawiony dowód.

### 6. Interpretacja i odejmowanie nowości

Poprawny wniosek: ten sam nieselektywny kanał CPTP i to samo POVM **nie wyznaczają selektywnych operacji CP**, ich korelacji z wynikiem ani możliwości późniejszej korekcji.

Znany gospodarz matematyczny: twierdzenie Choi, monotoniczność odległości śladowej, kwantowe procesy losowo-unitarne i korekcja wspomagana środowiskiem, w tym Gregoratti–Werner. Jest to precyzyjne uszczegółowienie projektu, bez roszczenia do nowej teorii kwantowej.

**Dyspozycja:** `LT5_TURN6 = PASS`, `LT5_TURN7 = PASS_WITH_EXACT_STRENGTHENING`, `MATHEMATICAL_HOST = MATURE`, `MONOGRAPH_NOT_MUTATED`. Autor LT5 decyduje o redakcyjnym przyjęciu. `BW_PENDING`, `NO_CANON`, `NO_EXEC_SIGN`, `NO_NOVELTY`, `NO_PHYSICAL_UPGRADE`.

### 7. Custody

Pełny raport zapisany jako plik rozmowy. Próby utworzenia raportów ROT10 i ROT11 na GitHub przy pomocy podłączonej integracji zostały zablokowane przez zabezpieczenia; brak potwierdzenia zapisu zewnętrznego. Doręczenie w Slack wymaga osobnego potwierdzenia odczytu, jeśli się powiedzie.