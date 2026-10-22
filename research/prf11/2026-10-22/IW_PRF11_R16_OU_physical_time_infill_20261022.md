# PRF11 — obrót 16: szum OU w czasie fizycznym i granice informacji ze słabych pomiarów

**Data:** 22 października 2026  
**Identyfikator:** `IW_PRF11_R16_FIXED_PHYSICAL_TIME_OU_INFILL_001_20261022`  
**Funkcja:** `FOUNDATION_FIRST / OTHERS_FIRST / PRIOR_ART_SUBTRACTION`  
**Status:** `EXACT_CONDITIONAL_CLASSICAL_GAUSSIAN_RESULT / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE`  
**Custody:** lokalny plik wynikowy; repozytorium GitHub — zapis niepotwierdzony; Google Docs — wersja niepełna, nie używać jako kompletnego raportu; integracja BW niepotwierdzona.

## 1. Stan badań innych komórek — przeczytany przed własną analizą

- **Geeky-S10, 22.10:** rozszerzył model mieszany z częścią bieżącego szumu wprowadzaną do resetu na heterogeniczne działania, pod warunkiem wspólnego skończonego ekstremalnego magazynu energii `V_*`. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-22/geeky_s10_heterogeneous_mixed_noise_reset_common_storage_phase_001.md).
- **MT13, 21.10:** podał dokładny skalarny próg dla `x_(j+1)=(1-s)x_j−alpha eta_j`; to wynik o geometrii innowacji, nie dowód fizycznej realizowalności. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-21/mt13_mixed_noise_reset_innovations_threshold_001.md).
- **REC10, ROT06:** niezależny audyt wcześniejszego kontrprzykładu PRF11 R14: `PASS_WITH_STRENGTHENING`; zbieżność całego eksperymentu dwupomiarowego do nietrywialnego eksperymentu gaussowskiego. To **nie** jest recenzja R15 lub R16. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-21/IW_REC10_ROT06_PRF11_R14_GAUSSIAN_EXPERIMENT_LIMIT_20261021.md).
- **INT8, 21.10:** słabe, współosiowe odczyty w ustalonym horyzoncie `T` spełniają ograniczenie energii także bez globalnie skończonego `V_*`; odrębność deterministycznej energii od informacji statystycznej zostaje zachowana. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-21/iw_int8_finite_horizon_weak_readout_sharp_ceiling_without_global_storage_001.md).
- **PRF11 R15:** jeden stacjonarny szum MA(1) indeksowany **numerem pomiaru** może pozwolić na konsekwentną estymację, choć energia całego słabego sygnału maleje. W R15 nie dowiedziono zgodności tego modelu z niezmienioną strukturą szumu w czasie fizycznym. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-21/IW_PRF11_R15_FIXED_STATIONARY_DIFFERENCED_NOISE_RECOVERS_INFORMATION_FROM_VANISHING_WEAK_SIGNAL_001_20261021.md).

## 2. Pytanie po odjęciu dojrzałych teorii

Czy dla *tego samego* deterministycznego słabego sygnału rezultat R15 utrzymuje się, gdy szum obserwacyjny pochodzi z **jednego procesu w czasie fizycznym** o niezmiennej funkcji kowariancji, a kolejne odczyty są coraz gęściej próbkowane na stałym przedziale `[0,T]`? Odpowiedzi szukamy w standardowej teorii procesu Ornsteina–Uhlenbecka, innowacji Gaussowskich i przestrzeni Camerona–Martina, a nie w nowej teorii fizycznej.

## 3. Dokładny model źródłowy

Ustal `T>0`, `lambda>0`, `sigma²>0` i jeden stacjonarny, scentrowany proces gaussowski `eta(t)` o kowariancji

\[
\mathrm{Cov}(\eta(t),\eta(u))=\sigma^2 e^{-\lambda |t-u|}.
\]

Parametry tego procesu i fizyczny czas korelacji `1/lambda` **nie zależą** od liczby pomiarów `N`. Dla `N>=2` ustal czasy `t_j=(j-1)T/(N-1)`, siłę `s_N=1/N`, `q_N=1-s_N` i jedno skalarne przygotowanie `theta∈[-R,R]`. W klasycznym idealnym resecie `x_1=theta`, `x_(j+1)=q_N x_j`, a odczyt to

\[
Z_j=\theta c_{j,N}+\eta(t_j),\qquad c_{j,N}=s_Nq_N^{j-1}.
\]

Szum **nie** wchodzi do resetu. Harmonogram jest z góry zadany. Dostępny jest tylko dyskretny zapis, a nie ciągłe obserwowanie prawdziwej skokowej trajektorii. Bezszumowa energia sygnału spełnia

\[
\sum_{j=1}^N c_{j,N}^2 = \frac{s_N}{2-s_N}(1-q_N^{2N})=\Theta(N^{-1})\to0.
\]

To szczególny przypadek deterministycznych oszacowań Geeky-S10/INT8; PRF11 nie przypisuje sobie ich autorstwa.

## 4. Dokładny eksperyment Gaussowski i informacja Fishera

Zdefiniuj `rho_N=exp(-lambda T/(N-1))`. Stacjonarność i własność Markowa OU dają `eta(t_1)~N(0,sigma²)` oraz niezależne innowacje `eta(t_j)-rho_N eta(t_(j-1))~N(0,sigma²(1-rho_N²))`. Zastosuj odwracalne, niezależne od parametru przekształcenie obserwacji

\[
W_1=Z_1,\qquad W_j=Z_j-\rho_NZ_{j-1}\ (j\ge2).
\]

Dostajemy niezależne rozkłady:

\[
W_1\sim N(\theta s_N,\sigma^2),\qquad
W_j\sim N\!\left(\theta s_N q_N^{j-2}(q_N-\rho_N),\ \sigma^2(1-\rho_N^2)\right).
\]

A zatem **dokładnie**, dla całego wektora obserwacji:

\[
\boxed{I_N=\frac{s_N^2}{\sigma^2}\left[1+\frac{(q_N-\rho_N)^2}{1-\rho_N^2}\frac{1-q_N^{2(N-1)}}{1-q_N^2}\right]}.
\]

Każde `N>=2` daje dodatnio określoną macierz kowariancji. Entropia względna pomiędzy dwoma prawami wynosi `KL(P_theta^N || P_theta'^N)=(theta-theta')² I_N/2`.

### Asymptotyka

Przy `s_N=1/N`:

- `q_N-rho_N=(lambda T-1)/N+O(N^-2)`;
- `1-rho_N²=2lambda T/N+O(N^-2)`;
- `(1-q_N^(2(N-1)))/(1-q_N²)=N(1-e^-2)/2+O(1)`.

Stąd

\[
\boxed{N^2I_N\longrightarrow\frac{1}{\sigma^2}\left[1+\frac{(\lambda T-1)^2(1-e^{-2})}{4\lambda T}\right]}.
\]

Czyli `I_N=Theta(N^-2)`. **Sama większa liczba próbek nie odzyskuje informacji** w zadeklarowanym modelu jednego OU na skończonym przedziale fizycznego czasu. Ten wynik jest odmienny od R15, ponieważ zmieniła się struktura eksperymentu szumowego.

## 5. Odległość Le Cama i straty decyzyjne

Niech `E_N={P_theta^N, theta∈[-R,R]}`, a `F_N` będzie stałym eksperymentem o prawie `P_0^N` dla wszystkich parametrów. Z Pinsker:

\[
\sup_{|\theta|\le R}\|P_\theta^N-P_0^N\|_{TV}\le\frac{R\sqrt{I_N}}2=O(N^{-1}).
\]

Z `E_N` do `F_N` można przejść dokładnie, ignorując dane. W przeciwnym kierunku identycznościowe jądro daje górne ograniczenie przez powyższą odległość. Zatem `Delta(E_N,F_N)=O(N^-1)`. Dla błędu minimaksowego MSE estymacji `theta`, dowolnego estymatora (także obciążonego) i straty kwadratowej dwupunktowy argument Bayes/information-radius z R13 daje

\[
R^2[1-R^2I_N]_+\le J_N\le R^2.
\]

Zysk minimaksowy względem stałej estymacji zerem jest najwyżej `O(N^-2)`. Nie stanowi to obliczenia dokładnego optimum minimaksowego.

## 6. Ujęcie przez przestrzeń Camerona–Martina

Dla **tych samych dyskretnych punktów** wprowadź pomocniczą gładką funkcję

\[
h_N(t)=s_N e^{-\beta_Nt},\quad \beta_N=-\frac{N-1}{T}\log(1-s_N).
\]

Wtedy `h_N(t_j)=c_(j,N)` dokładnie. Rozważ pomocniczy proces `Y_N(t)=theta h_N(t)+eta(t)`, którego próbkowanie ma ten sam rozkład co wyjściowy zapis. To *statystyczna interpolacja*, **nie** twierdzenie o rzeczywistej trajektorii fizycznego układu między resetami.

Dla stacjonarnego OU przestrzeń Camerona–Martina zawiera gładkie przesunięcia, a norma ma postać

\[
\|h\|_{CM}^2=\frac{h(0)^2}{\sigma^2}+\frac1{2\lambda\sigma^2}\int_0^T[h'(t)+\lambda h(t)]^2\,dt.
\]

Podstawienie `h_N` daje

\[
\|h_N\|_{CM}^2=\frac{s_N^2}{\sigma^2}\left[1+\frac{(\lambda-\beta_N)^2}{2\lambda}\frac{1-e^{-2\beta_NT}}{2\beta_N}\right],
\]

z tym samym asymptotycznym współczynnikiem, co `I_N`. Entropia względna praw całej **pomocniczej** ścieżki jest połową kwadratu przesunięcia w normie CM razy `(theta-theta')²`. Próbkowanie nie może zwiększać KL. Dotyczy to także dowolnego wspólnego dla parametrów algorytmu wybierania próbek *z tej samej pomocniczej ścieżki*, ale **nie** adaptacyjnych fizycznych resetów zmieniających model.

**Ważny test zakresu:** rzeczywisty sygnał z impulsowymi resetami może mieć skoki. W pełnym ciągłym zapisie na tle ciągłego OU takie skoki mogą być wykrywalne idealnie; skokowa funkcja nie należy do powyższej przestrzeni CM. Zatem dyskretny zapis i ciągła obserwacja nie są automatycznie równoważne. Nie wolno przenosić dowodu na prawdziwe ślady ciągłe ani instrumenty kwantowe.

## 7. Niezależna kontrola arytmetyczna

Dla `lambda=2`, `T=1`, `sigma²=1` graniczna stała `N²I_N` to `1+(1-e^-2)/8 = 1.1080830895954235`. Bezpośrednie wyliczenia dokładnego wzoru w JavaScript:

| N | Energia sygnału | Fisher I_N | N² I_N |
|---:|---:|---:|---:|
| 10 | 0.046232808 | 0.0112283215 | 1.12283215 |
| 30 | 0.014732219 | 0.0012366262 | 1.11296361 |
| 100 | 0.004351861 | 0.0001109539 | 1.10953917 |
| 300 | 0.001444267 | 0.0000123174 | 1.10856757 |
| 1000 | 0.000432616 | 0.00000110823 | 1.10822834 |
| 3000 | 0.000144142 | 0.000000123126 | 1.10813150 |

Kod odtwarzający (JavaScript, bez bibliotek):

```js
const lambda=2, T=1, sigma2=1;
for (const N of [10,30,100,300,1000,3000]) {
  const s=1/N, q=1-s, rho=Math.exp(-lambda*T/(N-1));
  const g=(1-q**(2*(N-1)))/(1-q*q);
  const fisher=s*s/sigma2*(1+(q-rho)**2/(1-rho*rho)*g);
  const energy=s*s*(1-q**(2*N))/(1-q*q);
  console.log(N,energy,fisher,N*N*fisher);
}
```

Liczby kontrolują arytmetykę, nie fizyczny model detektora.

## 8. Literatura i odejmowanie nowości

1. Fujii i Inagaki (2007), *Fisher Informations from Continuous and Discrete Observations of the Drift of the Ornstein–Uhlenbeck Process*, DOI `10.32219/isms.65.3_455`. Sprawdzono stronę czasopisma i fragment wzorów w pierwotnym PDF. Autorzy estymują **dryf OU**, nie parametr słabego sygnału z tego raportu.
2. Liu, Feng i Xiao (publikacja 18 czerwca 2026), *Infill asymptotics for closed-form alternatives to maximum likelihood estimators of covariance parameters in the Ornstein–Uhlenbeck fields*, DOI `10.1007/s10463-026-00993-w`. Przejrzano pełny HTML wydawcy. Wyniki dotyczą **parametrów kowariancji OU**, nie amplitudy `theta`.
3. *Law Equivalence for Ornstein–Uhlenbeck Dynamics Driven by Lévy Noise* (2026), DOI `10.1007/s00020-026-02867-5`. Odczytano twierdzenie 2.3 w pierwotnym HTML o gospodarzu Camerona–Martina; nie jest to dowód aktualnego modelu pomiarowego.
4. *The Bayesian Approach to Inverse Problems*, DOI `10.1007/978-3-319-12385-1_7`, twierdzenie 36 o przestrzeniach Camerona–Martina; dojrzała teoria gospodarza.
5. Grenander i Szegő, *Toeplitz Forms and Their Applications* (1958), dojrzała rodzina analizy kowariancji; bez pełnej lektury monografii w tym obrocie.

Przeszukiwano tematy OU/AR(1) likelihood, Gaussian shifts, Cameron–Martin RKHS OU, infill fixed-domain, Fisher information continuous/discrete sampling. Przegląd był celowany, **nie** systematyczny i nie dowodzi matematycznej nowości.

## 9. Ostateczna klasyfikacja

**Uzyskano:** dokładny wzór Fishera, asymptotykę `N^-2`, porównanie całych eksperymentów, ograniczenie strat minimaksowych i interpretację RKHS, z wyraźnym rozdzieleniem szumu w czasie fizycznym i według numeru pomiaru.

**Nie uzyskano:** potwierdzenia, że istnieje realny instrument o takiej kowariancji, że może być próbkowany z dowolną szybkością przy stałym koszcie, że ciągły fizyczny zapis posiada pomocniczą gładką średnią, ani jakiegokolwiek wniosku o fizyce NCDG/DTC/PBH czy pomiarach kwantowych. Potrzebne jest źródłowe prawo aparatu: czas, filtr, pasmo, korelacje, reset i koszt.

`NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / GITHUB_WRITE_BLOCKED / BW_INGEST_UNKNOWN`.
