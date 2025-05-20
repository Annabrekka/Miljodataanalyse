import sys
import os

import unittest
import pandas as pd
import math
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.Average import Data, FindAverage, FindMedian, FindStd 

# Lager en basetest som oppretter en dataframe som benyttes videre i de andre testene
class BaseTestData(unittest.TestCase):

# Lager en dataframe med med kolonnene elementId, date og value. 
# Oppretter ro rader for temperatur for ulike datoer for å teste gjennomsnittet, og en rad for vind
    def setUp(self):
        self.df = pd.DataFrame({
            "elementId": [
                "mean(air_temperature P1D)", "mean(air_temperature P1D)", 
                "mean(wind_speed P1D)"
            ],
            "date": [
                datetime(2020, 1, 1), datetime(2020,1, 2), datetime(2020, 1, 3)
            ],
            "value": [5.0, 7.0, 3.0]
        })
    

# Tester klassen "Data"
class TestData(BaseTestData):

# Oppretter en dataframe for datahåndtering    
    def setUp(self):
        super().setUp() # Kaller på setUp() fra baseklassen
        self.data_handler = Data(data = self.df)

# Tester klassen "prepare_data"
    def test_prepare_data(self):
        # Kjører metoden for en gitt parameter, og grupperer for år og måned, og gjør om til en liste
        grouped = self.data_handler.prepare_data("mean(air_temperature P1D)")
        groups = list(grouped.groups.keys()) 
        # Sjekker at det kun er en gruppe
        self.assertEqual(len(groups), 1)
        # Sjekker at gruppen faktisk er (2020, 1)
        self.assertEqual(groups[0], (2020, 1))

# Negative tester for klassen "Data"
class TestDataNegative(BaseTestData):
    def setUp(self):
        super().setUp()
        self.data_handler = Data(data = self.df)

# Tester at det returneres en tom gruppe dersom vi skriver inn en parameter som ikke finnes i dataframen
    def test_invalid_parameter(self):
        grouped = self.data_handler.prepare_data("parameter_nonexicting")
        self.assertEqual(len(grouped.groups), 0)

# Tester at det "prepare_data" håndterer et tomt datasett og returnerer en tom gruppering
    def test_prepare_data_empty_dataframe(self):
        # Oppretter en tom dataframe
        empty_df = pd.DataFrame({
            "elementId": pd.Series(dtype = "object"),
            "date": pd.Series(dtype = "datetime64[ns]"),
            "value": pd.Series(dtype = "float")
        })
        empty_handler = Data(data = empty_df)
        grouped = empty_handler.prepare_data("mean(air_temperature P1D)")
        self.assertEqual(len(grouped.groups), 0)



# Tester klassen "FindAverage"
class TestFindAverage(BaseTestData):
        
# Oppretter en datafram for å teste FindAverage
    def setUp(self):
        super().setUp() # Kaller på setUp() fra baseklassen
        self.average_handler = FindAverage(data = self.df)

    def test_mean_per_year(self):
        result_df = self.average_handler.mean_per_year("mean(air_temperature P1D)", "Temperature")
        expected_mean = (5.0 + 7.0) / 2
        # Sjekker at resultatet ha en rad, altså en gruppe med år og måned
        self.assertEqual(len(result_df), 1)
        # Sjekker at gjennomsnittsverdien stemmer, med 3 desimaler
        self.assertAlmostEqual(result_df.loc[0, "value"], expected_mean, places=3)
        # Sjekker at året og måned er det samme som testdataen
        self.assertEqual(result_df.loc[0, "year"], 2020)
        self.assertEqual(result_df.loc[0, "month"], 1)
        

# Tester klassen "FindMedian"
class TestFindMedian(BaseTestData):
        
# Oppretter en datafram for å teste FindMedian
    def setUp(self):
        super().setUp() # Kaller på setUp() fra baseklassen
        self.median_handler = FindMedian(data = self.df)

    def test_median_per_year(self):
        result_df = self.median_handler.median_per_year("mean(air_temperature P1D)", "Temperature")
        expected_median = 6.0 # Medianen av [5.0, 7.0]
        # Sjekker at resultatet ha en rad, altså en gruppe med år og måned
        self.assertEqual(len(result_df), 1)
        # Sjekker at medianen stemmer, med 3 desimaler
        self.assertAlmostEqual(result_df.loc[0, "value"], expected_median, places=3)
        # Sjekker at året og måned er det samme som testdataen
        self.assertEqual(result_df.loc[0, "year"], 2020)
        self.assertEqual(result_df.loc[0, "month"], 1)
       


class TestFindStd(BaseTestData):
        
# Oppretter en datafram for å teste FindMedian
    def setUp(self):
        super().setUp() # Kaller på setUp() fra baseklassen
        self.std_handler = FindStd(data = self.df)

    def test_std_per_year(self):
        result_df = self.std_handler.std_per_year("mean(air_temperature P1D)", "Temperature")
        expected_std = math.sqrt(((5-6)**2 + (7-6)**2)/1) # Standardavvik av [5.0, 7.0]
        # Sjekker at resultatet ha en rad, altså en gruppe med år og måned
        self.assertEqual(len(result_df), 1)
        # Sjekker at standardavvik stemmer, med 3 desimaler
        self.assertAlmostEqual(result_df.loc[0, "value"], expected_std, places=3)
        # Sjekker at året og måned er det samme som testdataen
        self.assertEqual(result_df.loc[0, "year"], 2020)
        self.assertEqual(result_df.loc[0, "month"], 1)



if __name__ == '__main__':
    unittest.main()
    