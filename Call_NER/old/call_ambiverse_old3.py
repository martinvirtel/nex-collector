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
def ambiverse (item,ner_names,tool_counter):
    try:
        global output
        value = check_file(item,ner_names,tool_counter)
        if value == False:
            ambiverse_token=get_token(client_id, client_secret)
            #Ambiverse Call
            text = item["text"]
            ambiverse_request_url = "https://api.ambiverse.com/v1/entitylinking/analyze"
            # text_string="".join(["{\"text\" : \"",text.encode("utf-8"),"\"}"])
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
            if len(response_matches)>0 :
                for x in response_matches:
                    entity_list.append(x["entity"])
                for x in response_matches:
                    x.update(x['entity'])
                    del x['entity']
                    output=response_matches
            else:
                output= [{"message": "no entities found"}]
                logging.error("ambiverse didnt find any entities for the file %s"%item["filename"])
        elif value == True:
            output=[{"error": "file double"}]
        return output
    except KeyError:
        logging.error("ambiverse Call for file %s not successfull. Output: %s"%(item["filename"],response))