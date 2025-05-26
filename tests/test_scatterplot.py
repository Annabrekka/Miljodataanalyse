import sys
import os
import unittest
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Unngår å vise graf ved kjøring av test

# Legger til src/ i systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Filstier
nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Precipitaion.csv"))
temp_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Temperatur.csv"))
vind_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Wind.csv"))

from scatterplot_visualisering import ScatterPlot

# Tester klassen ScatterPlot
class TestScatterPlot(unittest.TestCase):

    def setUp(self):     
        # Leser inn filene
        self.df_nedbor = pd.read_csv(nedbor_fil)
        self.df_temp = pd.read_csv(temp_fil)
        self.df_vind = pd.read_csv(vind_fil)

    def test_filtrer_data(self):     
        # Tester at data kun fra juli filtreres ut
        sp = ScatterPlot(file_path=nedbor_fil, datatype="nedbor", kolonne="value", month=7)
        self.assertIsInstance(sp.df_filtrert, pd.DataFrame)
        self.assertTrue(all(sp.df_filtrert["month"] == 7))

    def test_hent_tittel_og_enhet(self):      
        # Tester at riktig tittel og enhet hentes
        self.assertEqual(
            ScatterPlot(nedbor_fil, "nedbor", "value")._hent_tittel(), "Nedbør i juli over alle år"
        )
        self.assertEqual(
            ScatterPlot(temp_fil, "temp", "value")._hent_tittel(), "Temperatur i juli over alle år"
        )
        self.assertEqual(
            ScatterPlot(vind_fil, "wind", "value")._hent_tittel(), "Vind i juli over alle år"
        )
        self.assertEqual(
            ScatterPlot(nedbor_fil, "annet", "value")._hent_tittel(), "Data"
        )

        self.assertEqual(
            ScatterPlot(nedbor_fil, "nedbor", "value")._hent_enhet(), "Nedbør (mm)"
        )
        self.assertEqual(
            ScatterPlot(temp_fil, "temp", "value")._hent_enhet(), "Temperatur (°C)"
        )
        self.assertEqual(
            ScatterPlot(vind_fil, "wind", "value")._hent_enhet(), "Vind (m/s)"
        )
        self.assertEqual(
            ScatterPlot(nedbor_fil, "ukjent", "value")._hent_enhet(), "Enhet"
        )

    def test_plot_data_kjorer_uten_feil(self):     
        # Tester at grafen plottes riktig
        sp = ScatterPlot(file_path=vind_fil, datatype="wind", kolonne="value", month=7)
        try:
            sp.plot_data()
        except Exception as e:
            self.fail(f"plot_data() kastet en uventet feil: {e}")

# Kjører testen
if __name__ == "__main__":     
    unittest.main()