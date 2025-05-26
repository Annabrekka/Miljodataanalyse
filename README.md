# Miljødataanalyseprosjekt
I dette prosjektet har vi hentet inn værdata i form av temperatur, nedbør, vind og luftkvalitet. Vi har ryddet opp i dataen og filtrert ut undøvendige verdier og informasjon og det som ikke er innenfor en rimelig grense. For temperatur, nedbør og vind har vi funnet gjennomsnitt, median og standard avvik for hver måned. Videre brukte vi dette til å lage en visualisering av dataen, både i form av grafer og scatterplot, og som interaktiv grafer hvor brukeren selv kan velge datointervall. For luftkvalitet har det blitt funnet gjennomsnitt per dag i 2017. Her er det også visualisert hvordan temperatur, nedbør og vind påvirker luftkvaliteten. Til slutt i oppgaven har det blitt laget en regresjonanalyse som predikerer hvordan temperatur, nedbør og vind kan være i fremtiden. 


#### Her er en liten oversikt over hvordan vi har gått frem i prosjektet, mer detaljert beskrivelse om hva som skjer i de ulike filene er beskrevet i readmefilene i undermappene og underveis i kodingen. 

Vi startet prosjektet med å hente ut værdata fra Meterologisk institutt. Vi valgte å undersøk nedbørsmengde, temperatur og vind, ettersom vi tenkte at det ville være spennende å undersøke hva som har endret seg over tid. I notebooken "weather_api_45.pipynb" ([se fil](/notebooks/weather_api_45.ipynb)) henter vi ut værdata, og videre blir dataen behandlet  og ble lagt i csv-filen "gjsnitt_data.csv" ([se fil](/data/gjsnitt_data.csv)). Filen viser gjennomsnittet av målinger av nedbør, temperatur og vind fra 1975 til 2020 i Oslo. 

Vi hentet også ut målinger av luftkvalitet, ettersom vi tenkte det ville være spennende å undersøke hvordan luftkvaliteten blir påvirket av været. Luftkvalitet-dataen er hentet ut fra Norsk institutt for luftforskning. I notebooken "luftkvalitet_api" ([se fil](/notebooks/luftkvalitet_api.ipynb)) henter vi ut målinger av konsentrasjonen av NO2 og PM10 i luften gjennom hele 2017, i Oslo. Etter rensing og behandling av dataen, står vi igjen med filen "daglig_gjennomsnitt_2017.csv"([se fil](/data/daglig_gjennomsnitt_2017.csv)), som viser gjenommsnittet av målingene for hver dag. 

Videre i notebooken "Gjennomsnitt_median" ([se fil](/notebooks/Gjennomsnitt_median.ipynb)) er csv-filen "gjsnitt_data.csv" brukt. Her blir gjennomsnitt, median og standardavvik for værdataen funnet, slik at den videre kan bli benyttet til visulaliseringer. 

I notebooken "Visualisering.ipynb"([se fil](/notebooks/visualisering.ipynb)) er det laget visualiseringer av værdataen i form av grafer, scatterplot og interaktiv graf. Til slutt har vi visualisert en sammenheng mellom vær og luftkvalitet. Resultatet av visualisering ligger også i notebooken, med kommentar til resultatene. 

Til slutt er det gjort en prediksjonsanalyse, som ligger i notebooken "Prediksjon.ipynb" ([se fil](/notebooks/Prediksjon.ipynb)). Der benyttes metoden scikit-learn og dataen vi tidligere har funnet for de siste 45 årene. Dette brukes til å lære opp en modell som videre predikerer framtidige målinger for de neste 10 årene, basert på den historiske datan. Til dette er det brukt lineær regresjon, slik som oppgaven ba om.  


















