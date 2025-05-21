# Miljødataanalyseprosjekt
I dette prosjektet har vi hentet inn værdata i form av temperatur, nedbør, vind og luftkvalitet. Vi har ryddet opp i dataen og filtrert ut undøvendige verdier og informasjon og det som ikke er innenfor en rimelig grense. For temperatur, nedbør og vind har vi funnet gjennomsnitt og median for hver måned og standard avvik. Videre brukte vi dette til å lage en visualisering av dataen, både i form av en graf og et scatterplot, og som en interaktiv graf hvor brukeren selv kan velge datointervall. For luftkvalitet har det blitt funnet gjennomsnitt per dag i 2017. Her er det også visualisert hvordan temperatur, nedbør og vind påvirker luftkvaliteten. Til slutt i oppgaven har det blitt laget en regresjonanalyse som predikerer hvordan disse verdiene vil være i fremtiden. 

## Prosjektstruktur
Miljødataanalyse/
├── data/         # Inneholder rådata og bearbeidede datafiler (CSV og JSON)
├── docs/         # ki-deklerasjon, refleksjonsnotat og opgavebeskrivelse
├── notebooks/    # Jupyter Notebooks brukt til databehandling, dataanalyse og visualisering
├── resources/    # Eksterne ressurser som PDF-er, bilder eller andre relevante filer
├── src/          # Inneholder klasser og funksjoner som blir brukt i notebooks/
├── tests/        # Enhetstester for funksjonene og klassene i src/
├── .gitignore    # Spesifiserer filer og mapper som skal ignoreres av Git
├── requirements.txt  # Liste over alle avhengigheter prosjektet trenger for å fungere
└── README.md     # Introduksjon og dokumentasjon av hele prosjektet



### Her er en liten oversikt over hvordan vi har gått frem i prosjektet, mer detaljert beskrivelse om hva som skjer i de ulike filene er beskrevet i readmefilene i undermappene og underveis i kodingen. 

Vi startet prosjektet med å hente ut værdata fra Meterologisk institutt. Vi valgte å undersøk nedbørsmengde, temperatur og vind, ettersom vi tenkte at det ville være spennende å undersøke hva som har endret seg over tid. I notebooken [se fil](/notebooks/weather_api_45.ipynb) henter vi ut værdata og etter å behandla dataen sto vi da med dataen [se fil](/data/gjsnitt_data.csv)  som viser gjennomsnittet av målinger av nedbør, temperatur og vind fra 1975 til 2020 i Oslo. 

Vi hentet også ut målinger av luftkvalitet ettersom vi tenkte det ville være spennende å undersøke hvordan luftkvaliteten blir påvirket av været. Værdataen er hentet ut fra Norsk institutt for luftforskning. I notebooken [se filen](/notebooks/luftkvalitet_api.ipynb) henter vi ut målinger av konsentrasjonen av NO2 og PM10 i luften gjennom hele 2017, i Oslo. Etter å ha renset dataen fikk vi da dataen [se filen](/data/daglig_gjennomsnitt_2017.csv) som viser gjenommsnittet av målingene for hver dag. 

Videre i notebooken "Gjennomsnitt_median" [se filen](/notebooks/Gjennomsnitt_median.ipynb) har vi benyttet dataen fra 
Her har vi funnet gjennomsnitt, median og standardavik for tre ulike parameterene per måned per år. 

Så kom vi til visualiseringsdelen. I notebooken "Visualisering.ipynb" [se filen](/notebooks/visualisering.ipynb) er det visualisert i form av graf og scatterplot, og en interaktiv graf. Tislutt har vi visualisert en sammenheng mellom vær og luftkvalitet. Resultatet av visualisering ligger altså i notebooken, og her har vi da også kommentert resultatene. 

Deretter gikk vi over til prediksjonsanalyse. I notebooken "Prediksjon.ipynb" [se fil](/notebooks/Prediksjon.ipynb) benyttes metoden scikit-learn for å lære av dataen vi tidligere har funnet for de siste 45 årene. Dette brukes til å lære opp en modell som videre predikerer framtidige målinger for de neste 10 årene, basert på den historiske datan. Til dette er det brukt lineær regresjon, slik som oppgaven ba om.  


















