import pandas as pd

class CleaningCsv:
    def __init__(self, path, columns) -> None:
        self.data = pd.read_csv(path, parse_dates=[column for column in columns])
        self.string_columns = self.data.select_dtypes(include='object').columns
        self.numeric_columns = self.data.select_dtypes(include='number').columns
        self.row_numbers = len(self.data)
    
    def simulate_bad_entries(self):
        df = self.data
        string_columns = self.string_columns

        for column in string_columns:
            df[column] = df[column].str.lower()
            null_idxs = df[df[column].isna()].index
            df.loc[null_idxs, column] = 'no_data'
            empty_idxs = df[df[column] == ''].index
            df.loc[empty_idxs, column] = 'no_data'
            df[column] = df[column].str.replace(' ', '_')
        
        numeric_columns = self.numeric_columns
        for column in numeric_columns:
            minues_idxs = df[df[column] < 0].index
            df = df.drop(index=minues_idxs).reset_index(drop=True)
        return df

        