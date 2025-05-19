import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
import pandas as pd
import numpy as np
from Prediksjonsanalyse import HistoricData
from Prediksjonsanalyse import Prediction10Years  

class TestHistoricData(unittest.TestCase):

    def setUp(self):
        # Laster inn avarage_temperatur filen, og filtrerer ut måned 7
        self.historic = HistoricData("../data/Avarage/avarage_temperatur.csv")
        self.historic.read_file(7)


    def test_read_file(self):
        # Sjekker at read_file leser filen riktig
        # Sjekker at objektet som lastes ned faktisk er en pandas dataframe
        self.assertIsInstance(self.historic.df, pd.DataFrame)
        # Sjekker at dataframen ikke er tom
        self.assertFalse(self.historic.df.empty)
        # Sjekker at dataframen kun inneholder verdier fra måned 7
        self.assertTrue((self.historic.df['month'] == 7).all())

    
    def test_read_file_invalid_month(self):
        # Tester hva som skjer dersom det er feil input i read_file()
        # Tester for en tekststreng, forventer altså at testen skal få en TypeError
        with self.assertRaises(TypeError): 
            self.historic.read_file("juli")
        # Tester for en måned som ikke finnes i dataframen, sjekker om dataframen er tom som forventet
        with self.assertRaises(ValueError):
            self.historic.read_file(13)
        #self.assertTrue(self.historic.df.empty)


    
    def test_train_model(self):
        self.historic.train_model()
        # Sjekker om self.historic.X kun har en kolonne, fordi vi skal kun ha en uavhengig variabel til lineær regresjon
        self.assertEqual(self.historic.X.shape[1], 1)
        # Sjekker at det er like mange x- og y-verdier
        self.assertEqual(len(self.historic.X), len(self.historic.Y))

    
    def test_train_model_without_data(self):
        # Tester at det blir ValueError dersom vi prøver å trene modellen uten data
        historic = HistoricData("../data/Avarage/avarage_temperatur.csv")
        with self.assertRaises(ValueError):
            historic.train_model()

    def test_train_model_with_empty_dataframe(self):
        # Tester at det blir ValueError dersom vi prøver å trene modellen med en tom dataframe
        historic = HistoricData("../data/Avarage/avarage_temperatur.csv")
        historic.df = pd.DataFrame(columns=["year", "value"])
        with self.assertRaises(ValueError):
            historic.train_model()



    def test_evaluate_model(self):
        self.historic.train_model()
        self.historic.evaluate_model()
        # Sjekker om r2 verdien er mellom 0 og 1, fordi dette er de eneste gyldige verdiene
        self.assertGreaterEqual(self.historic.r2, 0)
        self.assertLessEqual(self.historic.r2, 1)
            

class TestPrediction10Years(unittest.TestCase):

    def setUp(self):
        # Kjører før hver test, laster inn data og forbereder modellen
        self.historic = HistoricData("../data/Avarage/avarage_temperatur.csv")
        self.historic.read_file(7)
        self.historic.train_model()
        self.prediction = Prediction10Years(self.historic)


    def test_generate_future_years(self):
        # Tester generate_future_years ved å generere 10 år frem til tid, for å så sjekke om det faktisk er hentet ut 10 år
        self.prediction.generate_future_years(10)
        self.assertEqual(len(self.prediction.predict_years), 10)
        # Sjekker om det første året kommer 1 år etter det siste historiske året
        expected_first_year = self.historic.df['year'].max() + 1
        self.assertEqual(self.prediction.predict_years[0][0], expected_first_year)

    
    def test_predict_future(self):
        # Genererer en liste over 5 år, for å så teste om det faktisk er generert 5 år og om disse blir laget som float-verdier
        self.prediction.generate_future_years(5)
        self.prediction.predict_future()
        self.assertEqual(len(self.prediction.future_predictions), 5)
        self.assertTrue(all(isinstance(value, (float, np.floating)) for value in self.prediction.future_predictions))


if __name__ == '__main__':
    unittest.main()



 















