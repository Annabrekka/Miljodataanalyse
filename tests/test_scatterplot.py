import sys
import os
import pytest
import pandas as pd
from io import StringIO
import matplotlib
matplotlib.use("Agg")

# Legger til src/ til systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/avarage_precipitation.csv"))
temp_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/avarage_temperatur.csv"))
vind_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/avarage_wind.csv"))

@pytest.fixture
def df_nedbor():
    return pd.read_csv(nedbor_fil)

@pytest.fixture
def df_temp():
    return pd.read_csv(temp_fil)

@pytest.fixture
def df_vind():
    return pd.read_csv(vind_fil)

from scatterplot_visualisering import ScatterPlot

class TestScatterPlot:
    def test_filtrer_data(df_nedbor):     # Tester at vi kun får data fra ønsket måned
        sp = ScatterPlot(file_path=nedbor_fil, datatype="nedbor", kolonne="value", month=7)
        assert isinstance(sp.df_filtrert, pd.DataFrame)
        assert all(sp.df_filtrert["month"] == 7)

    def test_hent_tittel_og_enhet(self):    # Tester at tiitel og enhet hentes riktig
        assert ScatterPlot(nedbor_fil, "nedbor", "value")._hent_tittel() == "Nedbør i juli over alle år"
        assert ScatterPlot(temp_fil, "temp", "value")._hent_tittel() == "Temperatur i juli over alle år"
        assert ScatterPlot(vind_fil, "wind", "value")._hent_tittel() == "Vind i juli over alle år"
        assert ScatterPlot(nedbor_fil, "annet", "value")._hent_tittel() == "Data"

        assert ScatterPlot(nedbor_fil, "nedbor", "value")._hent_enhet() == "Nedbør (mm)"
        assert ScatterPlot(temp_fil, "temp", "value")._hent_enhet() == "Temperatur (°C)"
        assert ScatterPlot(vind_fil, "wind", "value")._hent_enhet() == "Vind (m/s)"
        assert ScatterPlot(nedbor_fil, "ukjent", "value")._hent_enhet() == "Enhet"

    def test_plot_data_kjorer_uten_feil(df_vind):    # Tester at grafen plottes riktig
        sp = ScatterPlot(file_path=vind_fil, datatype="wind", kolonne="value", month=7)
        try:
            sp.plot_data()
        except Exception as e:
            pytest.fail(f"plot_data() kastet en uventet feil: {e}")