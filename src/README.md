Under denne mappen "src" er det flere filer som inneholder klasser og funksjoner som kalles og brukes under i kodene under "notebooks".


Beskrivelse av filene:
"Weather_analysis.py"([se filen](/src/Weather_analysis.py))
I denne filen er det laget 3 klasser som består av ulike funksjoner som vi bruker helt i starten av prosjektet for å bearbeide rådata. Klassen "Datacleaner" blir brukt til å få overført alle målingene til en ryddig dataframe. Videre inneholder klassen funskjoner slik at vi kan rense bort unødvendige kolonner og endre navn til mer presise kolonnenavn. Klassen "DataQualityChecker" blir brukt til å sjekke for manglende og ekstreme verdier. Siste klassen er "ObservationProcessor" som blir brukt til å hente dataen å strukturere det på riktig måte. Disse klassene blir brukt i notebookene "luftkvalitet_api.ipynb"([se filen](../notebooks/luftkvalitet_api.ipynb)) og "weather_api_45.ipynb"([se filen](../notebooks/weather_api_45.ipynb)) under mappen "notebooks". Her vil det også være grundigere forklaring på hvorfor jeg har valgt å bruke de ulike funksjonene. 


"Prediksjonsanalyse.py" ([se filen](/src/Prediksjonsanalyse.py))
Under denne filen er det laget to ulike klasser med flere funksjonen i. 
Klassen kalt "HistoricData" leser av en csv-fil og bruker dataen herfra til å trene en modell til å lage en graf. Til dette brukes metoden scikit-learn. Videre i klassen "Predictions10years" predikeres framtidig data. Dette er også gjort med scikit-learn og modellen som er trent opp i klassen "HistoricData". Til slutt vises både grafen laget i "HistoricData" og prediksjonene i et plot. Disse klassene og funksjonene blir kalt under mappen "notebooks" i filen "Prediksjon.ipynb" [se filen](../notebooks/Prediksjon.ipynb).

"interaktiv_visualisering.py"([se filen](/src/interaktiv_visualisering.py))
I denne filen er det laget en klasse med flere funksjoner som til sammen skal lage en interaktiv visualisering av ulik værdata hvor brukeren kan bruke en slider for å velge hvilket intervall de ønsker å se data for. Til dette er det brukt pandas for å hente data, matplotlib for å plotte grafer og widgets for å gi en interaktiv slider. Det er ikke hentet inn noen spesielle filer i klassen, men under notebooken "visualisering.ipynb" ([se filen](../notebooks/visualisering.ipynb)) blir det først hentet inn data fra filene "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" før klassen blir kalt på og grafene visualisert. 

"scatterplot_visualisering.py" [se filen](/src/scatterplot_visualisering.py)
I denne filen er det laget en klasse med flere funksjoner som til sammen lager et scatterplot av ulik værdata fra kun juli hvert år mellom 1975 og 2020. Til dette er det brukt pandas for å hente værdata og matplotlib for å plotte. Det er ikke hentet inn noe data i denne klassen, men under mappen "notebooks" er det hentet inn "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" og det er også her klassen blir kalt på og dataen visualisert. 

"visualisering_seaborn.py" ([se filen](/src/visualisering_seaborn.py))
I denne filen er det laget en klasse med flere funksjoner som til sammen lager en graf over værdata fra kun én måned hvert år mellom 1975 og 2020. Til dette er det brukt pandas for å hente inn værdata og seaborn for å plotte grafene. Det er heller ikke her hentet inn noe spesifikk data, men under "notebooks" så blir "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" hentet inn og klassen blir senere kalt på og måned man ønsker å se data for kan velges og grafen visualiseres. 