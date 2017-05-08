
import os
from pathlib import Path
import csv
import glob
import pandas

tools = [
    "txtwerk",
    "dandelion",
    "ambiverse"
    ]



name_list = "%s_data_file_list.csv"
name_outputs="%s_outputs.csv"
name_final_output="final_output.csv"
file_list=[]
for tool in tools:
    
    f = open(name_list%tool)
    csv_list = csv.reader(f)
    df_list = []
    for filename in sorted(csv_list):
        try:
            file_list.append(filename)
            df_list.append(pandas.read_csv(filename[0]))
            full_df = pandas.concat(df_list)
            full_df.to_csv(name_outputs%tool)
        except:
            print("EmptyDataError")


df_list = []
for filename in sorted(file_list):
    file_list.append(filename)
    try:
        df_list.append(pandas.read_csv(filename[0]))
        full_df = pandas.concat(df_list)
        full_df.to_csv(name_final_output)
    except:
        print("EmptyDataError")

