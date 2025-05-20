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
        # Finner gjennomsnittet per måned per år, og runder av til 3 desimaler
        grouped = self.prepare_data(parameter)
        monthly_average_per_year = grouped["value"].mean().reset_index()
        monthly_average_per_year["value"] = monthly_average_per_year["value"].round(3) 
        monthly_average_per_year.to_csv(f"../data/Avarage/average_{unit}.csv")
        print(f"Gjennomsnittet for {unit}")  
        print(monthly_average_per_year.head())


# Oppretter en klasse som finner medianen for de tre ulike parameterene, denne klassen bruker også klassen "Data"
class FindMedian(Data):
    
    def median_per_year(self, parameter, unit):
        grouped = self.prepare_data(parameter)
        monthly_median_per_year = grouped["value"].median().reset_index()
        monthly_median_per_year["value"] = monthly_median_per_year["value"].round(3)
        monthly_median_per_year.to_csv(f'../data/Avarage/median_{unit}.csv')
        print(f"Median for {unit}")
        print(monthly_median_per_year.head())


# Oppretter en klasse som finner standardavik for de tre ulike parameterene, denne klassen bruker også klassen "Data"
class FindStd(Data):

    def std_per_year(self, parameter, unit):
        grouped = self.prepare_data(parameter)
        monthly_std_per_year = grouped["value"].std().reset_index()
        monthly_std_per_year["value"] = monthly_std_per_year["value"].round(3)
        monthly_std_per_year.to_csv(f'../data/Avarage/std_{unit}.csv')
        print(f"Standardavvik for {unit}")
        print(monthly_std_per_year.head())
        




   