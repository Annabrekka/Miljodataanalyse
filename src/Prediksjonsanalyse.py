# Importerer biblioteker
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 

# Oppretter klassen "HistoricData" som laster inn csv-filen og gjør klar for å lage treningsmodellen
class HistoricData:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.X = None
        self.Y = None
        self.model = LinearRegression()

# Funksjon som leser filen, og først passer på at det er gyldig data
    def read_file(self, maaned):
        # Passer på at det kun er gyldig data for maaneden
        if not isinstance(maaned, int):
            raise TypeError ("Skriv inn et tall, ikke streng")
        if maaned < 1 or maaned > 12:
            raise ValueError ("Kun maaneder mellom 1 og 12")
       # Leser csv-filen
        self.df = pd.read_csv(self.csv_path)
        # Endrer til å kun bruke verdier for juli
        self.df = self.df[self.df['month'] == maaned] 


# Funksjon som trener modellen
    def train_model(self):
        # Skal trene en modell, men må passe på at den ikke trener den uten data eller for en tom dataframe
        if self.df is None:
            raise ValueError("Kan ikke trene modellen uten data") 
        if self.df.empty:
            raise ValueError("Kan ikke trene modellen med en tom dataframe") 
        #trener modellen, basert på x- og y-verdier
        self.X = self.df['year'].values.reshape(-1, 1)
        self.Y = self.df['value'].values
        self.model.fit(self.X, self.Y)


# Funksjon som lager plottene for grafen/regresjonen
    def plot_data(self, title,ylabel):
        # Finner de historiske prediksjonene
        X_sorted = np.sort(self.X, axis = 0)
        y_train = self.model.predict(X_sorted)

        # Plotter data og modellen  
        plt.plot(X_sorted, y_train, color='r', label='Lineær modell')
        plt.scatter(self.X, self.Y, s=10, label='Data')  # Gir et label til dataene


        # Viser hvert femte år på x-aksen
        years = np.arange(self.df['year'].min(), self.df['year'].max() + 1, 5)
        plt.xticks(years, rotation=45)

        # Legger til labels
        plt.title(title)
        plt.xlabel('År')
        plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()
        plt.show()

# Funksjon som gir R2-verdi, slik at man evaluere hvor godt grafen passer punktene
    def evaluate_model(self):
        Y_pred = self.model.predict(self.X)
        self.r2 = r2_score(self.Y, Y_pred)
        print(f"R2 verdien er {self.r2}")
    

# Klasse som predikerer fremtidig data
class Prediction10Years:

# Funksjon som henter den historiske dataen og modellen
    def __init__(self, historic_obj):
        self.df = historic_obj.df
        self.X = historic_obj.X
        self.Y = historic_obj.Y
        self.model = historic_obj.model
        self.current_year = self.df['year'].max()
        self.predict_years = None
        self.future_predictions = None

# Funksjon som oppretter en liste for fremtidige år
    def generate_future_years(self, years):
        # Finner det siste året for historisk data, og oppretter et array for å vise prediksjoner for årene framover
        current_year = self.df['year'].max()
        self.predict_years = np.array([[self.current_year + i] for i in range(1, years + 1)])


# Funksjon som predikerer fremtiden, ved å se på den trente modellen
    def predict_future(self):
        # Lager prediksjoner for fremtidige år, ved å iterere gjennom de fremtidige årene
        self.future_predictions = self.model.predict(self.predict_years)
        for i, prediction in enumerate(self.future_predictions, start=1):
            print(f"Predikert gjennomsnittstemperatur for {self.current_year + i}: {prediction:.2f}")


# Funksjon som plotter prediksjonene og tidligere graf
    def predictions_plot(self,title, unit):
        # Plotter dataene og prediksjonene
        plt.scatter(self.X, self.Y, color='blue', label='Historiske data')
        plt.plot(self.X, self.model.predict(self.X), color='green', label='Lineær regresjonsmodell') # Lineær graf tilpasset historisk data
        plt.plot(self.predict_years, self.future_predictions, color='red', linestyle='dashed', label='Prediksjoner for kommende år') # Lineær graf som predikerer 10 år fram i tid

        # Legger til navn på akser, tittel og viser plot
        plt.title(title)   
        plt.xlabel('År')
        plt.ylabel(unit)
        plt.legend()
        plt.tight_layout()
        plt.show()




    




