import os
from datetime import datetime

import pandas as pd
from pyarrow import int32

from excel_files import excel_files

from openpyxl.utils import column_index_from_string


def appendOrSet(arr, obj):
    for item in arr:
        if item["id"] == obj["id"]:
            if not item["data"]:
                item["data"] = []
            item["data"] += obj["data"]
            return

    arr.append(obj)

input_path = "./data"
output_file = "./data/extracted_data.csv"

final_data = [
    {
        "id": 5,
        "name": "Vasile",
        "date": "20.05.22",
        "value": 650
    }
]



for year in excel_files:
    data = pd.read_excel(os.path.join(input_path, year['path']), sheet_name=0, names=year['columns'], index_col=[0, 1])
    year_str = year['path'].split(".")[0]
    year_int = int(year_str)

    columns = data.to_dict()

    month = 0
    for column in columns:
        month += 1
        timestamp_str = datetime(year_int, month, 15).strftime('%Y-%m-%d %H:%M:%S')

        index = 0
        for row in list(columns[column].values()):
            final_data.append({
                "id": list(data['T'].index.codes[0])[index],
                "date": timestamp_str,
                "value": row
            })

            index += 1

    print(year_str + " done\n")