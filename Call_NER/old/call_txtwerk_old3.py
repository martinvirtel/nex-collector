import requests
import json
from joblib import Memory
import os
from txt_werk_apikey import txt_werk
from check_file import check_file
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)

cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def txtwerk(item,ner_names,tool_counter):
    try:
        global output
        value = check_file(item,ner_names,tool_counter)
        if value == False:
            text = item["text"]
            #except ImportError :
                #raise RuntimeError("Credentials must be supplied as dict in txt_werk_apikey.py. See example_txt_werk_apikey.py or use this as a template: txt_werk=dict(apikey='apikey')")
            TXT_WERK_URL = "https://api.neofonie.de/rest/txt/analyzer"
            key = str(txt_werk['apikey'])
            headers={'X-Api-Key' : key}
            r = requests.post(TXT_WERK_URL, data={'text': text, 'services' : 'entities'}, headers=headers)
            txt_werk_response = r.json()
            if len(txt_werk_response["entities"])>0 :
                output=txt_werk_response["entities"]
            else:
                output= [{"message": "no entities found"}]
                logging.error("txtwerk didnt find any entities for the file %s"%item["filename"])
        elif value == True:
            output=[{"error": "file double"}]
        return output
    except KeyError:
        logging.error("txtwerk Call for file %s not successfull. Output: %s"%(item["filename"],r))

   