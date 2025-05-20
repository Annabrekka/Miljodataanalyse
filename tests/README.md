Under denne mappen "tests" er det flere filer som inneholder tester av klasser og funksjoner laget under mappen "src". Enhetstester hjelper oss for å sikre at funskjonen oppfører seg slik de skal og fanger fort opp eventuelle feil. 

I filen test Weather_analysis.py har jeg opprettet tre testklasser: TestDataCleaner, TestDataQualityChecker og TestDataObservationProccesor. Disse testene sjekker ulike funskjoner for klassen DataCleaner, DataQualityChecker og ObservationProccesor. Detter er funksjoner som blir brukt helt i starten av prosjektet for å behandle rådata. Det er beskrevet underveis i kodene hva som skjer. 












I filen "test_prediksjonsanalyse.py" er det tester som tester funksjonene i klassene "HistoricData" og "Prediction10Years" under filen "Prediksjonsnalayse.py".

"test_interaktive_visualiseringer.py"
Her er det laget en testklasse med pytest som tester funksjonene i klassen "InteraktiveVisualiseringer" under "interaktive_visualiseringer.py". Hva som testes er beskrevet underveis i koden.

"test_scatterplot.py"
Her er det laget en testklasse med pytest som tester funksjonene i klassen "ScatterPlot" under "scatterplot_visualisering.py". Hva som testes er beskrevet underveis i koden. 

"test_visualiseringer.py"
Her er det laget en testklasse med pytest som tester funksjonene i klassen "VisualiseringSeaborn" under "visualisering_seaborn.py". Hva som testes er beskrevet underveis i koden. 