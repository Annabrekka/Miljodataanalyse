import sys
import os
import pytest
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # Unngår å printe grafen ved testing

# Legger til src/ til systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_precipitaion.csv"))
temp_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Temperatur.csv"))
vind_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Wind.csv"))

@pytest.fixture
def df_nedbor():
    return pd.read_csv(nedbor_fil)

@pytest.fixture
def df_temp():
    return pd.read_csv(temp_fil)

@pytest.fixture
def df_vind():
    return pd.read_csv(vind_fil)

from interaktiv_visualisering import InteraktivVisualisering  

class TestInteraktivVisualisering:

    def test_init_og_attributter(self, df_nedbor):  
        vis = InteraktivVisualisering(df_nedbor, datatype='nedbor', kolonne='value')
        assert 'date' in vis.df.columns    # Sjekker at dataframe er kopiert og 'date' er lagt til
        assert hasattr(vis, 'dato_slider')   # Sjekker at dato_slider er en widget med riktig antall alternativer
        assert len(vis.dato_slider.options) == len(vis.df['date'].dt.date.unique())
        assert vis.datatype == 'nedbor' # Sjekker datatype og kolonne
        assert vis.kolonne == 'value'

    def test_hent_tittel_og_enhet(self, df_temp):    # Tester at tittel og enhet blir hentet
        vis = InteraktivVisualisering(df_temp, datatype='temp', kolonne='value')
        assert vis._hent_tittel() == 'Temperatur over tid'
        assert vis._hent_enhet() == 'Temperatur (°C)'

    def test_oppdater_graf_kjorer_uten_feil(self, df_vind):    # Tester at grafen blir vist uten feil
        vis = InteraktivVisualisering(df_vind, datatype='wind', kolonne='value')
        dato_start = vis.df['date'].dt.date.min()
        dato_slutt = vis.df['date'].dt.date.max()
        try:
            vis._oppdater_graf((dato_start, dato_slutt))  # Skulle ikke kaste feil
        except Exception as e:
            pytest.fail(f"_oppdater_graf kastet en uventet feil: {e}")