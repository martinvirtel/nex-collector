import requests
from txt_werk_apikey import txt_werk
from joblib import Memory
import os
import os.path

cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def txtwerk (text):
    #except ImportError :
    #raise RuntimeError("Credentials must be supplied as dict in txt_werk_apikey.py. See example_txt_werk_apikey.py or use this as a template: txt_werk=dict(apikey='apikey')")
    TXT_WERK_URL = "https://api.neofonie.de/rest/txt/analyzer"
    key = str(txt_werk['apikey'])
    headers={'X-Api-Key' : key}
    r = requests.post(TXT_WERK_URL, data={'text': text, 'services' : 'entities'}, headers=headers)
    txt_werk_response = r.json()
    try:
        output=[1,txt_werk_response["entities"]]
    except KeyError:
        output=[0,txt_werk_response]
    return output