import pandas as pd
import matplotlib.pyplot as plt

# Oppretter en klasse som lager et scatter plot
class ScatterPlot:
    def __init__(self, file_path, datatype, kolonne, month=7):
        self.file_path = file_path
        self.datatype = datatype
        self.kolonne = kolonne
        self.month = month
        self.df = self._les_inn_data()
        self.df_filtrert = self._filtrer_data()

    def _les_inn_data(self):      # Henter data og gjør dato om til en  datetime-kolonne
        df = pd.read_csv(self.file_path)
        df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))
        return df

    def _filtrer_data(self):     # Filtrerer ut måneden vi vil se på
        return self.df[self.df["month"] == self.month]

    def plot_data(self):       # Lager et plott av dataen og tilpasser den
        plt.figure(figsize=(10, 5))
        plt.scatter(self.df_filtrert["date"], self.df_filtrert[self.kolonne], marker="o", color="b", label=self.datatype)

        plt.xlabel("År")
        plt.ylabel(self._hent_enhet())
        plt.title(self._hent_tittel())
        plt.legend()
        plt.grid(True)

        plt.show()

    def _hent_tittel(self):    # Henter tittel ut ifra hva slags data som skal vises
        if self.datatype == 'nedbor':
            return 'Nedbør i juli over alle år'
        elif self.datatype == 'temp':
            return 'Temperatur i juli over alle år'
        elif self.datatype == 'wind':
            return 'Vind i juli over alle år'
        else:
            return 'Data'

    def _hent_enhet(self):     # Henter enhet til y-label ut ifra hva slags data som vises
        if self.datatype == 'nedbor':
            return 'Nedbør (mm)'
        elif self.datatype == 'temp':
            return 'Temperatur (°C)'
        elif self.datatype == 'wind':
            return 'Vind (m/s)'
        else:
            return 'Enhet'