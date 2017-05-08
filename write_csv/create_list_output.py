
import os
from pathlib import Path
import csv
import glob
import pandas

tools = [
    "txtwerk"
    "dandelion",
    "ambiverse"
    ]

path_output="output/%s/**/*.csv"

name_list = "%s_file_list.csv"


for tool in tools:
    file_list = glob.glob(path_output%tool) 
    csvfile=open(name_list%tool,"w")
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows([str(a)] for a in file_list)
    csvfile.close()
    df_list = []


