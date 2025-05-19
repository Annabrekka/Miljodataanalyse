# Visualisering som graf ved bruk av seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class VisualiseringSeaborn:
    def __init__(self, filsti, enhet, tittel):
        self.filsti = filsti
        self.enhet = enhet
        self.tittel = tittel
        self.df = None
        self.df_filtrert = None
        self.maaned = None

    def last_data(self):
        self.df = pd.read_csv(self.filsti)
        self.df["date"] = pd.to_datetime(self.df[["year", "month"]].assign(day=1))

    def filtrer_maaned(self, maaned):
        self.maaned = maaned
        if self.df is not None:
            self.df_filtrert = self.df[self.df["date"].dt.month == maaned]
        else:
            raise ValueError("Data må lastes inn før filtrering.")

    def plott(self):
        if self.df_filtrert is not None:
            sns.set_theme()
            plott = sns.relplot(
                data=self.df_filtrert, kind="line",
                x="date", y="value",
                height=5, aspect=2
            )
            månednavn = self.df_filtrert["date"].dt.month_name().iloc[0] if not self.df_filtrert.empty else f"Måned {self.maaned}"
            plott.fig.suptitle(f"{self.tittel} i {månednavn} for alle år", fontsize=16)
            plott.set_axis_labels("År", self.enhet)
            plott.fig.tight_layout()
            plott.fig.subplots_adjust(top=0.9)
        else:
            raise ValueError("Data ikke filtrert. Kjør filtrer_maaned() først.")
        

# Interaktiv visualisering ved hjelp av widgets og matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

class InteraktivVisualisering:
    def __init__(self, df, datatype, kolonne):
        self.df = df.copy()
        self.datatype = datatype
        self.kolonne = kolonne
        self._forbered_data()
        self.dato_slider = self._lag_dato_slider()
        self._vis_interaktiv_graf()

    def _forbered_data(self):
        #Konverterer år og måned til en datetime-kolonne.
        self.df['date'] = pd.to_datetime(self.df[['year', 'month']].assign(day=1))

    def _lag_dato_slider(self):
        #Returnerer en SelectionRangeSlider-widget for datointervall.
        unike_datoer = self.df['date'].dt.date.unique().tolist()
        return widgets.SelectionRangeSlider(
            options=unike_datoer,
            index=(0, min(30, len(unike_datoer) - 1)),
            description='Dato:',
            layout={'width': '80%'}
        )

    def _oppdater_graf(self, dato_range):
        #Oppdateringsfunksjon for grafen basert på valgt datointervall.
        start, slutt = pd.to_datetime(dato_range[0]), pd.to_datetime(dato_range[1])
        filtrert = self.df[(self.df['date'] >= start) & (self.df['date'] <= slutt)]

        plt.figure(figsize=(10, 5))
        plt.plot(filtrert['date'], filtrert['value'], marker='o', linestyle='-', color='b')
        plt.title(self._hent_tittel())
        plt.xlabel("Dato")
        plt.ylabel(self._hent_enhet())
        plt.grid(True)
        plt.show()

    def _hent_tittel(self):
        if self.datatype == 'nedbor':
            return 'Nedbør over tid'
        elif self.datatype == 'temp':
            return 'Temperatur over tid'
        elif self.datatype == 'wind':
            return 'Vind over tid'
        else:
            return 'Data'

    def _hent_enhet(self):
        if self.datatype == 'nedbor':
            return 'Nedbør (mm)'
        elif self.datatype == 'temp':
            return 'Temperatur (°C)'
        elif self.datatype == 'wind':
            return 'Vind (m/s)'
        else:
            return 'Enhet'

    def _vis_interaktiv_graf(self):
        #Kobler widget til oppdateringsfunksjonen og viser grafen.
        widgets.interact(self._oppdater_graf, dato_range=self.dato_slider)


# Scatterplot av værdata
import pandas as pd
import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, file_path, datatype, kolonne, month=7):
        self.file_path = file_path
        self.datatype = datatype
        self.kolonne = kolonne
        self.month = month
        self.df = self._les_inn_data()
        self.df_filtrert = self._filtrer_data()

    def _les_inn_data(self):
        df = pd.read_csv(self.file_path)
        df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))
        return df

    def _filtrer_data(self):
        return self.df[self.df["month"] == self.month]

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.scatter(self.df_filtrert["date"], self.df_filtrert[self.kolonne], marker="o", color="b", label=self.datatype)

        # Tilpass plottet
        plt.xlabel("År")
        plt.ylabel(self._hent_enhet())
        plt.title(self._hent_tittel())
        plt.legend()
        plt.grid(True)

        # Vise plottet
        plt.show()

    def _hent_tittel(self):
        if self.datatype == 'nedbor':
            return 'Nedbør i juli over alle år'
        elif self.datatype == 'temp':
            return 'Temperatur i juli over alle år'
        elif self.datatype == 'wind':
            return 'Vind i juli over alle år'
        else:
            return 'Data'

    def _hent_enhet(self):
        if self.datatype == 'nedbor':
            return 'Nedbør (mm)'
        elif self.datatype == 'temp':
            return 'Temperatur (°C)'
        elif self.datatype == 'wind':
            return 'Vind (m/s)'
        else:
            return 'Enhet'

