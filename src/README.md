Under denne mappen "src" er det flere filer som inneholder klasser og funksjoner som kalles og brukes under i kodene under "notebooks".


Beskrivelse av filene:
"Prediksjonsanalyse.py"
Under denne filen er det laget to ulike klasser med flere funksjonen i. 
Klassen kalt "HistoricData" leser av en csv-fil og bruker dataen herfra til å trene en modell til å lage en graf. Til dette brukes metoden scikit-learn. Videre i klassen "Predictions10years" predikeres framtidig data. Dette er også gjort med scikit-learn og modellen som er trent opp i klassen "HistoricData". Til slutt vises både grafen laget i "HistoricData" og prediksjonene i et plot. Disse klassene og funksjonene blir kalt under mappen "notebooks" i filen "Prediksjon.ipynb".
