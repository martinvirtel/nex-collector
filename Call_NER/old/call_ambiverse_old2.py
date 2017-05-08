import requests
import json
from ambiverse_apikey import client_id, client_secret
from joblib import Memory
import os

cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def ambiverse (file_list):
    #Ambiverse Token
    ambiverse_api_url= "https://api.ambiverse.com/oauth/token"
    data={"grant_type": "client_credentials", "client_id":client_id, "client_secret":client_secret}
    r = requests.post(ambiverse_api_url, data=data)
    ambiverse_token_output = r.json()
    ambiverse_token = ambiverse_token_output ['access_token']
    #Ambiverse Call
    output = []
    for item in file_list:
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
        
        for x in response_matches:
            entity_list.append(x["entity"])
        
        for x in response_matches:
            x.update(x['entity'])
            del x['entity']
        if len(response_matches)>0 :
            output.append(response_matches)
    return output
        