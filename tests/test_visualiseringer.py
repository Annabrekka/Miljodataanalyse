import sys
import os
import pytest
import pandas as pd
from io import StringIO
import matplotlib
matplotlib.use("Agg")

# Legg til src/ til systemets import-sti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

nedbor_fil = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/Avarage/average_Precipitaion.csv"))
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

from visualisering_seaborn import VisualiseringSeaborn

class TestVisualiseringSeaborn:

    def test_last_data(self, df_nedbor):   # Tester at vi har en dataframe med tre rader og en kolonne "date"
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        assert vis.df is not None
        assert "date" in vis.df.columns
        assert len(vis.df) >=0

    def test_filtrer_maaned(self, df_nedbor):   # Tester at vi fortsatt har data etter at vi har filtrert og at vi kun har data fra måneden januar. 
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        vis.filtrer_maaned(1)
        assert vis.df_filtrert is not None
        assert all(vis.df_filtrert["date"].dt.month == 1)

    def test_filtrer_maaned_uten_last_data(self, df_nedbor):   # Tester at vi har lastet inn data før vi starter testen
        vis = VisualiseringSeaborn("avarage_precipitation.csv", enhet="mm", tittel="Test")
        with pytest.raises(ValueError, match="Data må lastes inn før filtrering"):
            vis.filtrer_maaned(1)

    def test_plott_uten_filtrering(self, df_nedbor):    # Tester at funksjonen plott() ikke kjøres uten at dataen er filtrert
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        with pytest.raises(ValueError, match="Data ikke filtrert"):
            vis.plott()

    def test_plott_med_filtrering(self, df_nedbor):    # Tester at funksjonen plott() kjører som den skal etter at dataen er filtrert
        vis = VisualiseringSeaborn(nedbor_fil, enhet="mm", tittel="Nedbør")
        vis.last_data()
        vis.filtrer_maaned(1)
        try:
            vis.plott() 
        except Exception as e:
            pytest.fail(f"plott() kastet en uventet feil: {e}")