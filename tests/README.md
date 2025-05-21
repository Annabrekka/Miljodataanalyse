#Test-mappen
Under denne mappen "tests" er det flere filer som inneholder tester av klasser og funksjoner laget under mappen "src". Enhetstester hjelper oss for å sikre at funskjonen oppfører seg slik de skal og fanger fort opp eventuelle feil. 

OBS: For noen av test-filene lønner det seg å innstallere python 3.12 å kjør testene i denne versjonen, fordi det ikke er oppdatert med alle metoder i python 3.13.

I filen "test_weather_analysis.py" [se filen](/tests/test_weather_analysis.py) har jeg opprettet tre testklasser: TestDataCleaner, TestDataQualityChecker og TestDataObservationProccesor. Disse testene sjekker ulike funskjoner for klassen DataCleaner, DataQualityChecker og ObservationProccesor i weather_analysis.py [se filen](../src/Weather_analysis.py). Dette er funksjoner som blir brukt helt i starten av prosjektet for å behandle rådata. Det er beskrevet underveis i kodene hva som skjer. 

I filen "test_prediktiv.py" [se fil](/tests/test_predektiv.py) er det tester som tester funksjonene i klassene "HistoricData" og "Prediction10Years" under filen "Prediksjonsnalayse.py" [se filen](../src/Prediksjonsanalyse.py).

I filen "test_interaktive_visualiseringer.py" [se filen](/tests/test_interaktive_visualiseringer.py) er det laget en testklasse som tester funksjonene i klassen "InteraktiveVisualiseringer" under "interaktive_visualiseringer.py" [se fil](../src/interaktiv_visualisering.py). Hva som testes er beskrevet underveis i koden.

I filen "test_scatterplot.py" [se fil](/tests/test_scatterplot.py) er det laget en testklasse som tester funksjonene i klassen "ScatterPlot" under "scatterplot_visualisering.py" [se filen](../src/scatterplot_visualisering.py). Hva som testes er beskrevet underveis i koden. 

I filen "test_visualiseringer.py" [se filen](/tests/test_visualiseringer.py) er det laget en testklasse som tester funksjonene i klassen "VisualiseringSeaborn" under "visualisering_seaborn.py" [se filen](../src/visualisering_seaborn.py). Hva som testes er beskrevet underveis i koden. 

I filen "test_average.py" [se filen](/tests/test_average.py) er det laget 6 testklasser som blir brukt under "Average.py" [se filen](../src/Average.py). Hva som testes er beskrevet underveis i koden. 


