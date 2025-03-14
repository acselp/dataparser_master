import os
import pandas as pd


def appendOrSet(arr, obj):
    for item in arr:
        if item["id"] == obj["id"]:
            if not item["data"]:
                item["data"] = []
            item["data"] += obj["data"]
            return

    arr.append(obj)

directory = "./data/"
output_file = "./data/extracted_data.csv"

excel_files = [
    "2016.xlsx", "2017.xlsx"
]

excel_files_2 = ["2018.xlsx", "2019.xlsx", "2020.xlsx",
    "2021.xlsx", "2022.xlsx", "2023.xlsx", "2024.xlsx"
]

cleanData = []



# parsing data from rest of the years
for file in excel_files_2:
    file_path = os.path.join(directory, file)
    year = file


    df = pd.read_excel(file_path, sheet_name=0, dtype=str, header=[2])

    date = df.loc[1:, df.columns.str.contains("Curent") + df.columns.str.contains("curenta")]

    df = pd.read_excel(file_path, sheet_name=0, dtype=str, header=[3])

    names = df.loc[:, df.columns.str.contains("Nume")]
    nr_carnet = df.loc[:, df.columns.str.contains("Nr. carnet")]

    names = names.to_dict()["Nume, prenume, patronimic"]
    nr_carnet = nr_carnet.to_dict()['Nr. carnet']
    date.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    date = date.to_dict()

    for index in names:
        object = {"name": names[index], "id": nr_carnet[index], "data": []}
        counterData = []

        for i in date:
            counterData.append(date[i][index + 1])

        object["data"] += counterData
        appendOrSet(cleanData, object)

    a = 5




# Parsing data from 2016 and 2017
# for file in excel_files:
#     file_path = os.path.join(directory, file)
#     year = file
#
#     df = pd.read_excel(file_path, sheet_name=0, dtype=str, header=[2])
#     names = df.loc[:, df.columns.str.contains("Nume")]
#     nr_carnet = df.loc[:, df.columns.str.contains("Nr. carnet")]
#     df.to_dict()
#     df = pd.read_excel(file_path, sheet_name=0, dtype=str, header=[1])
#     date = df.loc[:, df.columns.str.contains("Curent")]
#
#     names = names.to_dict()["Nume, prenume, patronimic"]
#     nr_carnet = nr_carnet.to_dict()['Nr. carnet']
#     date.columns = [0,1,2,3,4,5,6,7,8,9,10,11]
#     date = date.to_dict()
#
#     for index in names:
#         object = { "name": names[index], "id": nr_carnet[index], "data": [] }
#         counterData = []
#
#         for i in date:
#             counterData.append(date[i][index])
#
#         object["data"] += counterData
#         appendOrSet(cleanData, object)
#
#     a = 5