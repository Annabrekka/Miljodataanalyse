import unittest
import pandas as pd
from pandas import json_normalize
from src.Weather_analysis import DataCleaner, DataQualityChecker, ObservationProcessor

#TestDataCleaner tester klassen Datacleaner. 
#Den sjekker at den klarer å gjøre ulike endringer for å få mer oversiktelig data. 
class TestDataCleaner(unittest.TestCase):
    #Oppretter data som vik kan bruke som eksempler 
    def setUp(self):
        self.data = [
            {"component": "NO2", "values": [{"value": 10}, {"value": 200}]},
            {"component": "PM10", "values": [{"value": 200}, {"value": 400}]}
        ]
        self.cleaner = DataCleaner(self.data)

    #Tester om dataene fra values blir hentet ut riktig. Sjekker derfor lengden på DataFramen, at kolonnen vår "component finnes" og at første rad har riktig navn.
    def test_extract_component_data(self):
        df = self.cleaner.extract_component_data("NO2")
        self.assertEqual(len(df), 2)
        self.assertIn("component", df.columns)
        self.assertEqual(df["component"].iloc[0], "NO2")

    #Sjekker ar kolonnen endrer navn
    def test_rename_columns(self):
        df = self.cleaner.extract_component_data("NO2")
        df = self.cleaner.rename_columns(df, {"value": "NO2"})
        self.assertIn("NO2", df.columns)

    #Lager en enkel DataFrame med kolonnene A og B, og sjekker at B blir slettet. 
    def test_drop_columns(self):
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        self.cleaner.df = df
        new_df = self.cleaner.drop_columns(["B"])
        self.assertNotIn("B", new_df.columns)


#Testen TestDataQualityChecker tester klassen DataQualityChecker. 
# Den sjekker dataen vår for manglende og ekstreme verdier.
class TestDataQualityChecker(unittest.TestCase):
    #Oppretter en DataFrame som innholder ulike verdier, blant annet tommer verdier, slik at vi kan bruke den som eksempel.
    def setUp(self):
        data = {
            "NO2": [50, None, 300, 600],
            "PM10": [20, 500, None, 450]
        }
        df = pd.DataFrame(data)
        self.checker = DataQualityChecker(df)
    
    #Sjekker at den finner 1 manglende verdi for hver komponent. 
    def test_check_missing_values(self):
        missing = self.checker.check_missing_values()
        self.assertEqual(missing["NO2"], 1)
        self.assertEqual(missing["PM10"], 1)

    #Sjekker for høye verdier. Sjekker at den finner 1 for høy verdi i NO2. Dobbelsjekker så at denne verdien er høyere enn 400. 
    def test_find_extreme_values(self):
        result = self.checker.find_extreme_values("NO2", 400)
        self.assertEqual(len(result), 1)
        self.assertGreater(result["NO2"].iloc[0], 400)

#Testen TestObservationProcessor tester klassen ObservationProcessor.
# Den sjekker at den henter ut dataen vår på riktig måte. 
class TestObservationProcessor(unittest.TestCase):
    def test_extract_observations_with_valid_data(self):
        #Oppretter et datasett jeg kan bruke som eksempel. 
        sample_data = [
            {
                "referenceTime": "2020-01-01T00:00:00Z",
                "sourceId": "SN18700",
                "observations": [
                    {"elementId": "mean(air_temperature P1D)", "value": 3.5},
                    {"elementId": "sum(precipitation_amount P1D)", "value": 15.0}
                ]
            }
        ]

        processor = ObservationProcessor(sample_data)
        result = processor.extract_observations()

        #Sjekker at resultatet har riktig lengde, og at innholdet er riktig.
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["referenceTime"], "2020-01-01T00:00:00Z")
        self.assertEqual(result[0]["sourceId"], "SN18700")
        self.assertEqual(result[0]["value"], 3.5)
        self.assertEqual(result[1]["elementId"], "sum(precipitation_amount P1D)")
    
    def test_extract_observations_with_missing_data(self):
        sample_data = [
            {
                "referenceTime": "2020-01-01T00:00:00Z",
                "sourceId": "SN18700"
                # "observations" mangler
            }
        ]

        processor = ObservationProcessor(sample_data)
        result = processor.extract_observations()
        #sjekker at den ikke finner neon observasjoner
        self.assertEqual(result, [])




#Laster ned begge testene fra begge klassene og legger den til i suite. 
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDataCleaner))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDataQualityChecker))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestObservationProcessor))
    return suite

#Kjører nå testene. Bruker verbosity=2 som gir mer detaljerte rapporter. 
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)  
    runner.run(suite())  










    


