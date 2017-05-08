import requests
import json
from ambiverse_apikey import client_id, client_secret
from ambiverse_token import get_token
from joblib import Memory
import os
from check_file import check_file
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)

cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def ambiverse(text):
    ambiverse_token=get_token(client_id, client_secret)
    ambiverse_request_url = "https://api.ambiverse.com/v1/entitylinking/analyze"
    text_string=json.dumps({"text" : text })
    payload= text_string
    headers = {
        'content-type': "application/json",
        'accept': "application/json",
        'authorization': ambiverse_token
    }
    response = requests.request("POST", ambiverse_request_url, data=payload, headers=headers)
    response= response.json()
    response_matches =  response["matches"]
    entity_list= []
    try:
        for x in response_matches:
            entity_list.append(x["entity"])
        for x in response_matches:
            x.update(x['entity'])
            del x['entity']
            output=[1,response_matches]

    except KeyError:
        output=[0,response]

    return output