# OBS: kjør disse testene i pyhton 3.12

import sys
import os
import unittest
import pandas as pd
import matplotlib
matplotlib.use("Agg") # Unngår å vise graf ved kjøring av test

# Legger til src/ til systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from visualisering_seaborn import VisualiseringSeaborn

# Filstier
nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Precipitaion.csv"))

class TestVisualiseringSeaborn(unittest.TestCase):
    
    def setUp(self):
        self.df_nedbor = pd.read_csv(nedbor_fil)

    def test_last_data(self):         
        # Tester at df ikke er tom og at den inneholder 'date'-kolonnen
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        self.assertIsNotNone(vis.df)
        self.assertIn("date", vis.df.columns)
        self.assertGreaterEqual(len(vis.df), 0)

    def test_filtrer_maaned(self):      
        # Tester at den kan filtrere ut data fra én måned
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        vis.filtrer_maaned(1)
        self.assertIsNotNone(vis.df_filtrert)
        self.assertTrue(all(vis.df_filtrert["date"].dt.month == 1))

    def test_filtrer_maaned_uten_last_data(self):      
        # Tester at det gir feil om man prøver å filtrere uten å ha lastet inn data
        vis = VisualiseringSeaborn("avarage_precipitation.csv", enhet="mm", tittel="Test")
        with self.assertRaisesRegex(ValueError, "Data må lastes inn før filtrering"):
            vis.filtrer_maaned(1)

    def test_plott_uten_filtrering(self):     
        # Tester at man ikke kan plotte uten å filtrere data først
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        with self.assertRaisesRegex(ValueError, "Data ikke filtrert"):
            vis.plott()

    def test_plott_med_filtrering(self):    
        # Tester at det går å plotte når man har lastet og filtrert data riktig
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        vis.filtrer_maaned(1)
        try:
            vis.plott()
        except Exception as e:
            self.fail(f"plott() kastet en uventet feil: {e}")

# Kjører testen
if __name__ == "__main__":    
    unittest.main()