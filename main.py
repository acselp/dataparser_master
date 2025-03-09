import os
import pandas as pd
import re

# Directory where the files are stored
directory = "./data/"
output_file = "./data/extracted_data.csv"

# List of provided Excel files
excel_files = [
    "2016.xlsx", "2017.xlsx", "2018.xlsx", "2019.xlsx", "2020.xlsx",
    "2021.xlsx", "2022.xlsx", "2023.xlsx", "2024.xlsx"
]

data_list = []
old_df = pd.DataFrame()

for file in excel_files:
    file_path = os.path.join(directory, file)
    year = file

    df = pd.read_excel(file_path, sheet_name=0, dtype=str, header=[1], index_col=0)

    data = df.loc[:, df.columns.str.contains("Curent") + df.columns.str.contains("Nume")]
    data = data.iloc[2:]
    data.columns = [1,2,3,4,5,6,7,8,9,10,11,12]
    data.index.name = "FullName"

    old_df = pd.concat([old_df, data], ignore_index=False)
old_df.to_csv("output", index=True)