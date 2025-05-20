Under denne mappen "src" er det flere filer som inneholder klasser og funksjoner som kalles og brukes under i kodene under "notebooks".


Beskrivelse av filene:
"Prediksjonsanalyse.py"
Under denne filen er det laget to ulike klasser med flere funksjonen i. 
Klassen kalt "HistoricData" leser av en csv-fil og bruker dataen herfra til å trene en modell til å lage en graf. Til dette brukes metoden scikit-learn. Videre i klassen "Predictions10years" predikeres framtidig data. Dette er også gjort med scikit-learn og modellen som er trent opp i klassen "HistoricData". Til slutt vises både grafen laget i "HistoricData" og prediksjonene i et plot. Disse klassene og funksjonene blir kalt under mappen "notebooks" i filen "Prediksjon.ipynb".

"interaktiv_visualisering.py"
I denne filen er det laget en klasse med flere funksjoner som til sammen skal lage en interaktiv visualisering av ulik værdata hvor brukeren kan bruke en slider for å velge hvilket intervall de ønsker å se data for. Til dette er det brukt pandas for å hente data, matplotlib for å plotte grafer og widgets for å gi en interaktiv slider. Det er ikke hentet inn noen spesielle filer i klassen, men under notebooken "visualisering.ipynb" blir det først hentet inn data fra filene "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" før klassen blir kalt på og grafene visualisert. 

"scatterplot_visualisering.py"
I denne filen er det laget en klasse med flere funksjoner som til sammen lager et scatterplot av ulik værdata fra kun juli hvert år mellom 1975 og 2020. Til dette er det brukt pandas for å hente værdata og matplotlib for å plotte. Det er ikke hentet inn noe data i denne klassen, men under mappen "notebooks" er det hentet inn "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" og det er også her klassen blir kalt på og dataen visualisert. 

"visualisering_seaborn.py" 
I denne filen er det laget en klasse med flere funksjoner som til sammen lager en graf over værdata fra kun én måned hvert år mellom 1975 og 2020. Til dette er det brukt pandas for å hente inn værdata og seaborn for å plotte grafene. Det er heller ikke her hentet inn noe spesifikk data, men under "notebooks" så blir "average_Prectipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv" hentet inn og klassen blir senere kalt på og måned man ønsker å se data for kan velges og grafeb visualiseres. 