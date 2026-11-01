Zewnętrzny gospodarz: modele *readout assignment* jako macierze stochastyczne są standardowe (IBM Quantum Learning, https://quantum.cloud.ibm.com/learning/en/courses/tools-for-quantum-advantage/error-mitigation ; IBM Noise Models https://quantum.cloud.ibm.com/docs/en/guides/build-noise-models ). Dominacja stochastyczna dla bitów o warunkowo ograniczonych prawdopodobieństwach jest klasyczną konsekwencją sprzężenia Bernoulliego; zob. literaturę koncentracji martyngałów, np. https://adityam.github.io/stochastic-control/probability/martingales.html. Brak roszczenia pierwszeństwa.

## 1. Mrożony kontrakt urządzenia (R23 + R24)

W każdym z dwóch **oddzielnych i kolejno wykonywanych** odczytów pary czujnik jest przygotowywany od początku w |0⟩; źródło jest aktywne w czasie skończonego przygotowania Y(π/2), swobodnej ekspozycji Δ i analizy X/Y przez impuls(π/2). Z wymaga bezpośredniego odczytu Z bez impulsu analizy. Każdej parze losujemy jedno wspólne prywatne ustawienie X/Y/Z z wagami (.18,.20,.62), niezależne od źródła. Pierwszy odczyt jest destrukcyjny, po nim następuje reset **sensora** i świeże przygotowanie drugiego odczytu.

Źródło A: ukryta częstotliwość ξ(t) daje Hamiltonian ξ(t)Z/2. Jeżeli brak resetu w całej parze, ξ(t) jest jedną dowolną stałą ξ; między parami historia może zależeć dowolnie od przeszłości. Źródło B: dephasing Lévy'ego generator (γ/2)(Ad_Z−Id) działa w czasie źródłowo aktywnych impulsów, ekspozycji oraz oczekiwania, z niezależnymi przyrostami między pomiarami. Przyjmujemy γ=1, Ωmax=10, Δ=.5, tπ/2=π/(2Ωmax)=π/20.

NOWY, jawnie ograniczony model detektora D: po odpowiednim skończonym impulsie analizy (albo bez impulsu dla Z) sensor przez t_d=.05/γ podlega wyłącznie Hamiltonianowi proporcjonalnemu do Z (A) albo dephasingowi w Z (B), bez T1 i bez sterowania poprzecznego. Na koniec następuje idealny projektor Z, a niezależny dla każdego odczytu klasyczny kanał pomyłki etykiet +↔− z symetryczną częstością η (jednakową pod A i B). Nie modelujemy rzeczywistej ciągłej detekcji ani sprzężenia detektor–sensor: to **skończone oczekiwanie QND + końcowa projekcja + błąd klasycznego przypisania**, a nie kompletny certyfikat SPAM. Reset sensora zajmuje t_r=.05/γ, lecz nie zmienia ξ sam z siebie; źródło może zresetować się autonomicznie w dowolnej chwili. Zakładamy poprawne przygotowanie świeżego sensora po każdym resecie (bez błędu inicjalizacji).

## 2. Twierdzenie R24.1 — dokładna niezmienniczość względem czasu Z-QND i kontrakcja readout assignment

Dla Π±=(I±Z)/2 i dowolnego ρ zachodzi, jeżeli w czasie t_d działa tylko commutujące z Z H albo dephasing w Z:

