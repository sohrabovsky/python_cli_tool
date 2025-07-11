import pandas as pd
import typer
from .cleaning import CleaningCsv

def summarizing(input: str = typer.Option(..., "--input", "-i", help="Path to the CSV file"), 
                summary: bool = True):
    file = CleaningCsv(path= input, columns=["pickup_datetime", "dropoff_datetime"])
    if summary:
        print("Summary Stats:")
        print("--------------")
        total_rows = file.row_numbers
        print(f"Total rows: {total_rows}")

        df = file.simulate_bad_entries()
        cleaned_rows = len(df)
        print(f"Valid rows after cleaning: {cleaned_rows}\n")

        print("Numeric Columns:")
        for column in file.numeric_columns:
            mean = df[column].mean()
            min = df[column].min()
            max = df[column].max()
            print(f"- {column}: mean={round(mean, 1)}, min={min}, max={max}")
        print("")

        print("Categorical Columns:")
        for column in file.string_columns:
            print(f"- {column}:")
            for item in df[column].unique():
                num_of_items = len(df[df[column] == item])
                print(f"- {item}: {num_of_items}")


