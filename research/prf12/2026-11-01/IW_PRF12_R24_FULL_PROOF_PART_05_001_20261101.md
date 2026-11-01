1. **Asymetryczny kanał assignment:** przy Pr(+→−)=η_+, Pr(−→+)=η_- średni zapisany znak ma postać \(m_{\rm obs}=(1-\eta_+-\eta_-)m+(\eta_- -\eta_+)\). Stały wyraz powoduje wyrazy liniowe przy parowaniu. R24.2 nie działa. Trzeba kalibrować pełną macierz pomyłek, nie tylko uśrednione η.
2. **Niezależność szumu etykiet:** skorelowane błędy w parze mogą dać inny współczynnik niż (1−2η)², nawet przy identycznych marginesach.
3. **Nie-QND fizyczna detekcja:** T1, leakage, pomiary z niekomutującym sprzężeniem oraz źródło współdziałające z detektorem mogą zmieniać populacje Z. Sama skończona długość 'czekania' nie jest pełną teorią ciągłego procesu detekcji.
4. **Skok źródła w środku shot:** wtedy nie można używać m_Z(ξ)≥0 ani floor=.31 z R24.5; pozostaje floor=0 dla zdarzenia resetu.
5. **Tylko marginalna szansa resetu:** jeśli między parami resetowanie źródła jest skorelowane i nie ma warunkowego dolnego prawdopodobieństwa przeżycia, ogon dwumianowy (R24.12) nie jest automatyczny. Warunkowa Poissonowość lub jawnie osobny nierówny hazard jest krytyczna.
6. **Nieoznaczony czas trwania wspólnego ξ:** bez λ lub gwarantowanego okna przetrwania nie wolno deklarować oszacowanej liczby N. Zakres λ/γ≥0.051063 nie wyklucza rozróżniania innymi testami; jedynie dotychczasowy konserwatywny certyfikat nie rozstrzyga.
7. **Brak minimalizacji kosztu:** nie optymalizowano nowych wag, Δ, Ω, parametrów impulsu, długości detekcji jako funkcji η(t_d), alternatywnych progów, ani aktywnych pomiarów pośrednich; R23 pozostaje pierwszym właścicielem certyfikatu wag. Nie przenosić do oryginalnego nierozstrzygniętego problemu domknięcia LOCC dla trzech przestrzennie odseparowanych kubitów.

## 7. Reprodukcja i kontynuacja

Dostarczony oddzielny, jednoplikowy Python 3 + NumPy + SciPy rekonstruuje source-on prostokątne impulsy Blocha dla wybranych ξ, p_B=.5252387409109164, globalne m_Z≥0 na kontrolnej siatce (dowód globalny jest analityczny), dokładną transformację assignment, dodatnie hazardowe luki, progi dwumianowe i budżety fizyczne. Skrypt nie powtarza pełnej 3501-węzłowej arytmetyki przedziałowej z R23: wstępne granice (.576,.526) mają jawne pochodzenie i są już zweryfikowanym inputem naukowym.

**R25:** (i) źródłowo typowana korelacja η i odczyty niesymetryczne, (ii) skończony pomiar QND/Lindblad z możliwym T1, (iii) fizycznie określony rozkład czasu zmiany ξ w połowie ekspozycji i skutki dla m_Z, (iv) kosztowo optymalna sekwencja przy jednej kalibracji η(t_d). Nie twierdzić, że obecny R24 domknął sprzęt.

