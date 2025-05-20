
class FindAverage:

    def __init__(self, data):
        self.df = data

    def mean_per_year(self, parameter, unit):
        # Lager en ny datafram som kun inneholder en parameter
        df_parameter = self.df[self.df["elementId"] == parameter].copy()
        # Filtrerer ut år og måned
        df_parameter.loc[:, "year"] = df_parameter["date"].dt.year
        df_parameter.loc[:, "month"] = df_parameter["date"].dt.month
        # Finner gjennomsnittet per måned per år, og runder av til 3 desimaler
        monthly_average_per_year = df_parameter.groupby(["year", "month"])["value"].mean().reset_index()
        monthly_average_per_year["value"] = monthly_average_per_year["value"].round(3)  
        monthly_average_per_year.to_csv(f"../data/Avarage/average_{unit}.csv")
        print(f"Gjennomsnittet for {unit}")  
        print(monthly_average_per_year.head())



   