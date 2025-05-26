import sys
import os
import unittest
import pandas as pd
import matplotlib
matplotlib.use("Agg") # Unngår å vise graf ved kjøring av test

# Legger til src/ til systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from interaktiv_visualisering import InteraktivVisualisering

# Filstier
nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Precipitaion.csv"))
temp_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Temperatur.csv"))
vind_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Wind.csv"))

# Tester klassen InteraktivVisualisering
class TestInteraktivVisualisering(unittest.TestCase):

    def setUp(self):      # Leser inn filene
        self.df_nedbor = pd.read_csv(nedbor_fil)
        self.df_temp = pd.read_csv(temp_fil)
        self.df_vind = pd.read_csv(vind_fil)

    def test_init_og_attributter(self):     
        # Tester at df inneholder en 'date' kolonne og at datatype og kolonne inneholder riktige verdier
        vis = InteraktivVisualisering(self.df_nedbor, datatype='nedbor', kolonne='value')
        self.assertIn('date', vis.df.columns)
        self.assertTrue(hasattr(vis, 'dato_slider'))
        self.assertEqual(len(vis.dato_slider.options), len(vis.df['date'].dt.date.unique()))
        self.assertEqual(vis.datatype, 'nedbor')
        self.assertEqual(vis.kolonne, 'value')

    def test_hent_tittel_og_enhet(self):      
        # Tester at riktig tittel og enhet hentes
        vis = InteraktivVisualisering(self.df_temp, datatype='temp', kolonne='value')
        self.assertEqual(vis._hent_tittel(), 'Temperatur over tid')
        self.assertEqual(vis._hent_enhet(), 'Temperatur (°C)')

    def test_oppdater_graf_kjorer_uten_feil(self):      
        # Tester at funkjsonen _oppdater_graf() kjører riktig og ikke kaster feil
        vis = InteraktivVisualisering(self.df_vind, datatype='wind', kolonne='value')
        dato_start = vis.df['date'].dt.date.min()
        dato_slutt = vis.df['date'].dt.date.max()
        try:
            vis._oppdater_graf((dato_start, dato_slutt))
        except Exception as e:
            self.fail(f"_oppdater_graf kastet en uventet feil: {e}")

# Kjører testen
if __name__ == "__main__":     
    unittest.main()