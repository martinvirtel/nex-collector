
from file_list import file_list
from call_function import call_fuction
from call_txtwerk import txtwerk
from call_ambiverse import ambiverse
from call_dandelion import dandelion
from save_file import save_file
from final_print import final_print
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)




### Parameters
### Here are the parameters to run "ner_launcher.py"
### dpa-articles are stored as json-files
### The module "auswahl.py" creates a random list of theses json files.
### "filename_csv" is the csv-file with the file names of these random articles
filename_csv= "auswahl-2017-04-19.csv"


### In the list "ner_tools" all the NER-Tools are listed.
### There will be a request to every tool in the list.
### as funtions
ner_tools= [ 
    txtwerk,
    dandelion,
    ambiverse
]

ner_names=[]
for x in ner_tools:
    ner_names.append(x.__name__)
logging.info("\n***Starting*** \nwith the list  %s and Ner-Tools %s\n"%(filename_csv,ner_names))


### This functions creates a list of texts.
### It gets the texts from the files stored in the folder "outputs"
### The module "auswahl.py" creates a random list of theses json files.
### The function "file_list" takes these texts from the files of the list.
### It creates the list "file_list" with all documents in this list.
### Every item in this list has a dict with the values "text", "filepath", and "filename".


file_list= file_list(filename_csv)


#file_list=[{"text": "Sanan Suomi  etymologiasta ei  ole täyttä varmuutta. Se on ilmeisesti ollut alun perin Suomenlahden ympäristöä ja sittemmin lähinnä Varsinais-Suomea koskeva nimitys ja laajentunut vasta myöhemmin tarkoittamaan koko maata.", "filename": "%s_test.csv", "filepath": "/Users/alex/python_project/outputs/test/%s/"}]



### This functions calls the NER-APIs with the texts from "file_list".
### For every text from the list there is an API-request for every NER-Tool.
### After the request is done, the file will be saved. The filename and directory is stored in file_list


for item in file_list:
    output_object= call_fuction (item,ner_tools)

logging.info("\n***END***\nner_launcher done for %s documents with %s tools"%(len(file_list),(len(ner_tools))))
