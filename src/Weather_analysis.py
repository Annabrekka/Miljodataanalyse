import pandas as pd


class DataCleaner:

    def __init__(self, data):
        self.df = data

    def drop_columns(self, columns_to_drop):
        """ Her fjerner vi uønskede kolonner."""
        self.df = self.df.drop(columns=columns_to_drop)
        return self.df



