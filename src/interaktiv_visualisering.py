# Interaktiv visualisering ved hjelp av widgets og matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets

class InteraktivVisualisering:
    def __init__(self, df, datatype, kolonne):
        self.df = df.copy()
        self.datatype = datatype
        self.kolonne = kolonne
        self._forbered_data()
        self.dato_slider = self._lag_dato_slider()

    def _forbered_data(self):    # Konverterer år og måned til en datetime-kolonne
        self.df['date'] = pd.to_datetime(self.df[['year', 'month']].assign(day=1))

    def _lag_dato_slider(self):   # Returnerer en slider widget for datointervall
        unike_datoer = self.df['date'].dt.date.unique().tolist()
        return widgets.SelectionRangeSlider(
            options=unike_datoer,
            index=(0, min(30, len(unike_datoer) - 1)),
            description='Dato:',
            layout={'width': '80%'}
        )

    def _oppdater_graf(self, dato_range):   # Oppdaterer grafen basert på valgt intervall
        start, slutt = pd.to_datetime(dato_range[0]), pd.to_datetime(dato_range[1])
        filtrert = self.df[(self.df['date'] >= start) & (self.df['date'] <= slutt)]

        plt.figure(figsize=(10, 5))
        plt.plot(filtrert['date'], filtrert['value'], marker='o', linestyle='-', color='b')
        plt.title(self._hent_tittel())
        plt.xlabel("Dato")
        plt.ylabel(self._hent_enhet())
        plt.grid(True)
        plt.show()

    def _hent_tittel(self):    # Henter tittel ut i fra hva slags data som skrives ut
        if self.datatype == 'nedbor':
            return 'Nedbør over tid'
        elif self.datatype == 'temp':
            return 'Temperatur over tid'
        elif self.datatype == 'wind':
            return 'Vind over tid'
        else:
            return 'Data'

    def _hent_enhet(self):   # Henter enhet til ylabel ut i fra hva slags data som skrives ut
        if self.datatype == 'nedbor':
            return 'Nedbør (mm)'
        elif self.datatype == 'temp':
            return 'Temperatur (°C)'
        elif self.datatype == 'wind':
            return 'Vind (m/s)'
        else:
            return 'Enhet'

    def _vis_interaktiv_graf(self):    # Kobler widget til oppdateringsfunksjonen og viser grafen
        widgets.interact(self._oppdater_graf, dato_range=self.dato_slider)