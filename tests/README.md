## Test-mappen
Under denne mappen "tests" er det flere filer som inneholder tester av klasser og funksjoner laget under mappen "src". Enhetstester hjelper oss for å sikre at funskjonen oppfører seg slik de skal og fanger fort opp eventuelle feil. 

OBS: For noen av test-filene må man bruke python 3.12 for å kjøre testene, fordi det ikke er oppdatert med alle metoder i python 3.13. Det er spesifisert i filene det trengs ("test_interaktive_visualiseringer", "test_scatterplot" og "test_visulaiseringer")

#### Beskrivelse av filene:
I filen "test_average.py"([se fil](/tests/test_average.py)) er det laget 6 testklasser som blir brukt under "Average.py" ([se fil](../src/Average.py)). Hva som testes er beskrevet underveis i koden. 

I filen "test_weather_analysis.py"([se fil](/tests/test_weather_analysis.py)) er det tre testklasser: TestDataCleaner, TestDataQualityChecker og TestDataObservationProccesor. Disse testene sjekker ulike funskjoner for klassen DataCleaner, DataQualityChecker og ObservationProccesor i weather_analysis.py ([se fil](../src/Weather_analysis.py)). Dette er funksjoner som blir brukt helt i starten av prosjektet for å behandle rådata. Det er beskrevet underveis i kodene hva som skjer. 

I filen "test_prediktiv.py" ([se fil](/tests/test_predektiv.py)) er det tester som tester funksjonene i klassene "HistoricData" og "Prediction10Years" under filen "Prediksjonsnalayse.py"([se fil](../src/Prediksjonsanalyse.py)). Det er mer detaljert beskrivelse underveis i filen.

I filen "test_interaktive_visualiseringer.py"([se fil](/tests/test_interaktive_visualiseringer.py)) er det laget en testklasse som tester funksjonene i klassen "InteraktiveVisualiseringer" under "interaktive_visualiseringer.py"([se fil](../src/interaktiv_visualisering.py)). Hva som testes er beskrevet underveis i koden.

I filen "test_scatterplot.py"([se fil](/tests/test_scatterplot.py)) er det laget en testklasse som tester funksjonene i klassen "ScatterPlot" under "scatterplot_visualisering.py"([se fil](../src/scatterplot_visualisering.py)). Hva som testes er beskrevet underveis i koden. 

I filen "test_visualiseringer.py"([se fil](/tests/test_visualiseringer.py)) er det laget en testklasse som tester funksjonene i klassen "VisualiseringSeaborn" under "visualisering_seaborn.py"([se fil](../src/visualisering_seaborn.py)). Hva som testes er beskrevet underveis i koden. 
