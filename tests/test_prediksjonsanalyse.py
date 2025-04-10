import unittest
import pandas as pd

class TestHistoricData(unittest.TestCase):

    def setUp(self):
        # Laster inn avarage_temperatur filen, og filtrerer ut måned 7
        self.historic = HistoricData("data/Avarage/avarage_temperatur.csv")
        self.historic.read_file(7)


    def test_read_file(self):
        # Sjekker at read_file leser filen riktig
        # Sjekker at objektet som lastes ned faktisk er en pandas dataframe
        self.assertIsInstance(self.historic.df, pd.DataFrame)
        # Sjekker at dataframen ikke er tom
        self.assertFalse(self.historic.df.empty)
        # Sjekker at dataframen kun inneholder verdier fra måned 7
        self.assertTrue((self.historic.df['month'] == 7).all())

    
    def test_train_model(self):
        self.historic.train_model()
        # Sjekker om self.historic.X kun har en kolonne, fordi vi skal kun ha en uavhengig variabel til lineær regresjon
        self.assertEqual(self.historic.X.shape[1], 1)
        # Sjekker at det er like mange x- og y-verdier
        self.assertEqual(len(self.historic.X), len(self.historic.Y))


    def test_evaluate_model(self):
        self.historic.train_model()
        self.histroic.evaluate_model()
        # Sjekker om r2 verdien er mellom 0 og 1, fordi dette er de eneste gyldige verdiene
        self.assertGreaterEqual(self.r2, 0)
        self.assertLessEqual(self.r2, 1)
            







