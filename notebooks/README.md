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





