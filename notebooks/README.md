Under mappen "notebooks" ligger kodene brukt i prosjektet. Under undermappen "old_notebooks" ligger notebooks brukt for å prøve å forstå hvordan metodene i prosjektet skulle brukes. 

Beskrivelse av filene:
weather_api_45.ipynb:
Her henter vi data fra et API og lagrer det i JSON-format. Dataene er hentet fra Frost, et REST-API levert av MET Norge, som gir tilgang til historiske vær- og klimadata. Vi valgte å hente dataen herfra ettersom vi met.no er en politelig kilde. Videre i notebooken gjør vi endringer for å gjøre datasettet mer oversiktlig. Vi endrer formatet, fjerner unødvendige kolonner, og sjekker for manglende verdier samt for høye eller for lave målinger. Til slutt står vi igjen med en ryddig DataFrame som viser dato, element, verdi og enhet. Dette gir oss en oversikt over de gjennomsnittlige daglige målingene av nedbør, temperatur og vindhastighet fra 1975 til 2020. 
[se datafilen](../data/gjsnitt_data.csv)


luftkvalitet_api.ipynb:
Her henter vi data fra en API, og lagrer dataen i et json.format. Denne dataen er hente fra api.nilu.no. Vi valgte å bruke denne dataen ettersom det er bekreftet at alle målingene er kvalitetkontrolleres grundig. 
I notebooken gjør vi endringer slik at vi til ender med et ryddig datasett som forteller oss daglige gjennomsnittlige målinger av NO2 og PM10 konsentrasjonen i luften i 2017. 
[se datafilen](../data/daglig_gjennomsnitt_2017.csv)



Gjennomsnitt_median.ipynb - her blir gjennomsnitt, median og standardavvik for daten funnet
Prediksjon.ipynb - her predikeres fremtidig data for temperatur, vind og nedbør


visualisering.ipynb:
I denne notebooken blir tre klasser kalt på fra mappen src, "interaktiv_visualisering.py", "scatterplot_visualisering.py" og "visualisering_seaborn.py" og fremstilt som grafer og scatterplot. For alle disse klassene er det først hentet data fra csv-filene "average_precipitaion.csv", "average_Temperatur.csv" og "average_Wind.csv". Først er klassen VisualiseringSeaborn kalt på. Denne bruker seaborn til å fremstille data fra kun én måned hvert år mellom 1975 og 2020 og man skriver selv inn hvilken måned man ønsker å se data fra. Deretter kalles klassen InteraktivVisualisering på. Denne bruker pandas, matplotlib og widgets for å hente data og fremstille en interaktiv graf med slider hvor brukeren kan velge et datointervall de ønsker å se værdata fra. Siste klassen som kalles på er ScatterPlot. Her brukes pandas til å hente data og matplotlib for å plotte scatterplottet, som viser data fra juli hvert år mellom 1975 og 2020. Til slutt er det fremstilt tre grafer som henter data fra "gjsnitt_data.csv" og "daglig_gjennomsnitt_2017.csv". Førstnavnte fil inneholder daglig gjennomsnitssdata for temperatur, vind og nedbør og sistnevnte inneholder daglig gjennomsnitsdata for luftkvalitet i 2017. Det er brukt pandas for å hente data og matplotlib for å plotte grafene. Grafene viser sammenhengen mellom luftkvalitet og temperatur, nedbør og vind. 