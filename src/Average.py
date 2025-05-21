import os
import pandas as pd  


# Oppretter en klasse som definerer en ny dataframe og filtrer og år og måned
class Data:
    def __init__(self, data):
        self.df = data

    def prepare_data(self, parameter):
        # Lager en ny datafram som kun inneholder en parameter
        df_param = self.df[self.df["elementId"] == parameter].copy()
        # Filtrerer ut år og måned
        df_param.loc[:, "year"] = df_param["date"].dt.year
        df_param.loc[:, "month"] = df_param["date"].dt.month
        return df_param.groupby(["year", "month"])



# Oppretter en klasse som finner gjennomsnittet for de tre ulike parameterene, denne klassen bruker også klassen "Data" 
class FindAverage(Data):

    def mean_per_year(self, parameter, unit):
        # Bruker "Data" for å gruppere etter år og måned for gitt parameter
        grouped = self.prepare_data(parameter)
        # Finner gjennomsnittet per måned per år, og runder av til 3 desimaler
        monthly_average_per_year = grouped["value"].mean().reset_index()
        monthly_average_per_year["value"] = monthly_average_per_year["value"].round(3) 
        # Lagrer med trygg sti
        save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'Avarage', f'average_{unit}.csv'))
        monthly_average_per_year.to_csv(save_path)
        print(f"Gjennomsnittet for {unit}")  
        print(monthly_average_per_year.head())
        return monthly_average_per_year


# Oppretter en klasse som finner medianen for de tre ulike parameterene, denne klassen bruker også klassen "Data"
class FindMedian(Data):
    
    def median_per_year(self, parameter, unit):
        # Bruker "Data" for å gruppere etter gitt parameter
        grouped = self.prepare_data(parameter)
        # Finner medianen for gitt gruppen over per måned per år
        monthly_median_per_year = grouped["value"].median().reset_index()
        monthly_median_per_year["value"] = monthly_median_per_year["value"].round(3)
        # Lagrer med en absolutt sti
        save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'Avarage', f'median_{unit}.csv'))
        monthly_median_per_year.to_csv(save_path)
        print(f"Median for {unit}")
        print(monthly_median_per_year.head())
        return monthly_median_per_year


# Oppretter en klasse som finner standardavik for de tre ulike parameterene, denne klassen bruker også klassen "Data"
class FindStd(Data):

    def std_per_year(self, parameter, unit):
        # Bruker "Data" for å gruppere etter gitt parameter
        grouped = self.prepare_data(parameter)
        # Finner standardavviket for gitt gruppe
        monthly_std_per_year = grouped["value"].std().reset_index()
        monthly_std_per_year["value"] = monthly_std_per_year["value"].round(3)
        # Lagrer med absolutt sti
        save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'Avarage', f'standard_{unit}.csv'))
        monthly_std_per_year.to_csv(save_path)
        print(f"Standardavvik for {unit}")
        print(monthly_std_per_year.head())
        return monthly_std_per_year
        




   