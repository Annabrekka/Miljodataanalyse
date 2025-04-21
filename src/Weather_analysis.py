import pandas as pd
from pandas import json_normalize





class DataCleaner:

    def __init__(self, data):
        self.df = data

   
    def extract_component_data(self, component_name):
        # Filtrer dataene for den spesifikke komponenten 
        component_data = [item for item in self.df if item['component'] == component_name]
        
        # Normaliser 'values' for hver komponent
        df_list = [json_normalize(item['values'], sep='_') for item in component_data]
        
        # Slår sammen alle DataFrame-ene til én DataFrame
        df = pd.concat(df_list, ignore_index=True)
        
        # Legger til en kolonne for komponenten
        df['component'] = component_name
        
        return df
    
    def rename_columns(self, df, column_rename_map):
        #Endrer navn på kolonner i DataFramen.
        df = df.rename(columns=column_rename_map)
        return df


    def drop_columns(self, columns_to_drop):
        #Fjerner kolonner.
        self.df = self.df.drop(columns=columns_to_drop)
        return self.df
    





class DataQualityChecker:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
    
        #Returnerer antall manglende verdier i DataFrame.
        
        missing = self.df.isnull().sum()
        print("Manglende verdier:\n", missing)
        return missing

    def find_extreme_values(self, column, threshold):
        
        #Returnerer rader med verdier som overstiger en gitt grense.
        
        extremes = self.df[self.df[column] > threshold]
        print(f"Ekstreme verdier i {column} over {threshold}:\n", extremes)
        return extremes



