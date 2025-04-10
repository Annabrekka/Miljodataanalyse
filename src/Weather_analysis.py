import pandas as pd
from pandas import json_normalize





class DataCleaner:

    def __init__(self, data):
        self.df = data

   
    def extract_component_data(self, component_name):
        """Filtrer og hent ut data for en spesifikk komponent."""
        # Filtrer dataene for den spesifikke komponenten 
        component_data = [item for item in self.df if item['component'] == component_name]
        
        # Normaliser 'values' for hver komponent
        df_list = [json_normalize(item['values'], sep='_') for item in component_data]
        
        # Slå sammen alle DataFrame-ene til én DataFrame
        df = pd.concat(df_list, ignore_index=True)
        
        # Legg til en kolonne for komponenten
        df['component'] = component_name
        
        return df
    
    def rename_columns(self, df, column_rename_map):
        """Endre navn på kolonner i DataFrame."""
        # Omdøper kolonnene i DataFrame
        df = df.rename(columns=column_rename_map)
        return df


    def drop_columns(self, columns_to_drop):
        """ Her fjerner vi uønskede kolonner."""
        self.df = self.df.drop(columns=columns_to_drop)
        return self.df
    




