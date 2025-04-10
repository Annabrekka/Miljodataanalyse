# Importerer biblioteker
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 

class historic_data:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.X = None
        self.Y = None
        self.model = LinearRegression()


    def read_file(self, maaned):
       # Leser csv-filen
        self.df = pd.read_csv(self.csv_path)
        # Endrer til å kun bruke verdier for juli
        self.df = self.df[self.df['month'] == maaned] 


    def train_model(self):
        #trener modellen, baser på x- og y-verdier
        self.X = self.df['year'].values.reshape(-1, 1)
        self.Y = self.df['value'].values
        self.model.fit(self.X, self.Y)


    def plot_data(self, title):
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
        plt.ylabel('Temperatur')
        plt.legend()
        plt.tight_layout()
        plt.show()
    

class prediction_10years:
    def __init__(self, historic_obj):
        self.df = historic_obj.df
        self.X = historic_obj.X
        self.Y = historic_obj.Y
        self.model = historic_obj.model
        self.current_year = self.df['year'].max()
        self.predict_years = None
        self.future_predictions = None


    def generate_future_years(self, years):
        # Finner det siste året for historisk data, og oppretter et array for å vise prediksjoner for årene framover
        current_year = self.df['year'].max()
        self.predict_years = np.array([[self.current_year + i] for i in range(1, years + 1)])


    def predict_future(self):
        self.future_predictions = self.model.predict(self.predict_years)
        for i, prediction in enumerate(self.future_predictions, start=1):
            print(f"Predikert gjennomsnittstemperatur for {self.current_year + i}: {prediction:.2f}")


   """  def future_predictions(self, ):
        # Bruker modellen over for å predikere de 10 årene fram i tid
        future_predictions = model.predict(predict_years)

        # Lager er for-løkke som itererer gjennom fututre_prediuctions, og printer det ut
        for i, prediction in enumerate(future_predictions, start=1):
        print(f"Predikert gjennomsnittstemperatur for {current_year + i}: {prediction:.2f}") """

    def predictions_plot(self,title, unit):
        # Plotter dataene og prediksjonene
        plt.scatter(self.X, self.Y, color='blue', label='Historiske data')
        plt.plot(self.X, self.model.predict(X), color='green', label='Lineær regresjonsmodell') # Lineær graf tilpasset historisk data
        plt.plot(self.predict_years, self.future_predictions, color='red', linestyle='dashed', label='Prediksjoner for kommende år') # Lineær graf som predikerer 10 år fram i tid

        # Legger til navn på akser, tittel og viser plot
        plt.title('title')   
        plt.xlabel('År')
        plt.ylabel('unit')
        plt.legend()
        plt.tight_layout()
        plt.show()




    




