"""
txtwerk.get_output_dir(item["text"])

os.path.exists('./temp/joblib/call_txtwerk/txtwerk/44e176cbeed695aa8137aa8ca2295d2d')
sTrue
"""

import sqlite3
import dataset
import json
import glob
import csv
import os
import os.path
import datetime

db='sqlite:///test.db'
database = dataset.connect(db)
dpa_text=database["dpa_text"]
found_entities=database["found_entities"]
entity_db=database["entity"]
tools= database["tools"]
dpa_text= database["dpa_text"]


value_double=found_entities.find_one(dpa_id=1, entity_id=4,tool_id=1, start=75)
print(value_double)
        
   