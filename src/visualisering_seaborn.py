# Visualisering som graf ved bruk av seaborn
import pandas as pd
import seaborn as sns

class VisualiseringSeaborn:
    def __init__(self, filsti, enhet, tittel):
        self.filsti = filsti
        self.enhet = enhet
        self.tittel = tittel
        self.df = None
        self.df_filtrert = None
        self.maaned = None

    def last_data(self):     # Laster inn data og gjør dato om til en datetime-kolonne
        self.df = pd.read_csv(self.filsti)
        self.df["date"] = pd.to_datetime(self.df[["year", "month"]].assign(day=1))

    def filtrer_maaned(self, maaned):     # Filtrerer ut data fra kun en måned
        self.maaned = maaned
        if self.df is not None:
            self.df_filtrert = self.df[self.df["date"].dt.month == maaned]
        else:
            raise ValueError("Data må lastes inn før filtrering.")

    def plott(self):      # Plotter data og tilpasser plottet
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