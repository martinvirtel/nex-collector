import requests
import json
from ambiverse_apikey import client_id, client_secret
from ambiverse_token import get_token
from joblib import Memory
import os
import logging
import sys
import time
import datetime
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
    try:
        response_matches =  response["matches"]

        entity_list= []
        try:
            if response["language"] != "de":
                output=[False,response]
            elif response["language"] == "de":
                try:
                    for entity in response["matches"]:
                        entity["surface"] = entity["text"]
                        entity["start"]= entity["charOffset"]
                        entity["end"]=int(entity["start"])+int(entity["charLength"])
                        entity["label"] = ""
                        t=time.time()
                        entity["timestamp"]='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t))
                        extra={"ambiverse":"None"}
                        entity["extra"] =str(extra)
                        try:
                            entity["confidene"] = entity["entity"]["confidence"]
                        except KeyError:
                            entity["confidene"] =""
                        try:
                            uri=entity["entity"]["id"]
                            uri=uri.replace("http://www.wikidata.org/entity/","")
                            entity["uri"] = uri
                        except KeyError:
                            entity["uri"] =""
                        del entity["entity"]
                        del entity ["charLength"]
                        del entity ["charOffset"]
                        del entity["text"]
                    output=[True,response["matches"]]
                
                except KeyError:
                    output= [KeyError,response]
        except KeyError:
            output= [KeyError,response]
    except KeyError:
        output= [KeyError,response]
    return output
