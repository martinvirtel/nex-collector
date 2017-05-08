import requests
import json
from joblib import Memory
import os

cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def txtwerk(file_list):
    output = []
    for item in file_list:
        text = item["text"]
        from txt_werk_apikey import txt_werk
        #except ImportError :
            #raise RuntimeError("Credentials must be supplied as dict in txt_werk_apikey.py. See example_txt_werk_apikey.py or use this as a template: txt_werk=dict(apikey='apikey')")
    
        TXT_WERK_URL = "https://api.neofonie.de/rest/txt/analyzer"
        key = str(txt_werk['apikey'])
        headers={'X-Api-Key' : key}
        r = requests.post(TXT_WERK_URL, data={'text': text, 'services' : 'entities'}, headers=headers)
        txt_werk_response = r.json()
        if len(txt_werk_response["entities"])>0 :
            output.append(txt_werk_response["entities"])
    return output