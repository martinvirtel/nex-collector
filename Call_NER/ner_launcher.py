
from dpa_list import dpa_list
from call_function import call_fuction
from call_txtwerk import txtwerk
from call_ambiverse import ambiverse
from call_dandelion import dandelion
from write_output_db import write_output_db
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)




### Parameters
### Here are the parameters to run "ner_launcher.py"
### dpa-articles are stored as json-files
### The module "auswahl.py" creates a random list of theses json files.
### The module "auswahl.py" creates a random list of theses json files.
### "filename_csv" is the csv-file with the file names of these random articles
filename_csv= "auswahl-2017-04-19.csv"


### In the list "ner_tools" all the NER-Tools are listed as functions.
### There will be a request for every tool in the list.
### As funtions:
ner_tools= [ 
    txtwerk,
    dandelion,
    ambiverse
]

### This list makes strings from the functions
ner_names=[]
for x in ner_tools:
    ner_names.append(x.__name__)
logging.info("\n***Starting*** \nwith the list  %s and Ner-Tools %s\n"%(filename_csv,ner_names))


### This functions creates a list.
### Every item in the list has the text, dpa_id, date, ressort and title of the dpa-text

dpa_list = dpa_list(filename_csv)


### This functions calls the NER-APIs with the texts from "dpa_list".
### For every text from the list there is an API-request for every NER-Tool.
### After the request is done, the the ouput will be written in the database (write_output_db)


for item in dpa_list:
    #item["text"]="Dieser Text enthält keine Entis"
    #item["text"] = "Sanan Suomi  etymologiasta ei  ole täyttä varmuutta. Se on ilmeisesti ollut alun perin Suomenlahden ympäristöä ja sittemmin lähinnä Varsinais-Suomea koskeva nimitys ja laajentunut vasta myöhemmin tarkoittamaan koko maata."

    call_fuction(item,ner_tools)

logging.info("\n***END***\nner_launcher done for %s documents with %s tools"%(len(dpa_list),(len(ner_tools))))
