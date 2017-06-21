from aylienapiclient import textapi
from requests import HTTPError
from aylien_apikey import app_id,app_key
from dp_to_wikidata import dp_to_wikidata
import time
import datetime
from requests import HTTPError

def aylien(text):
    client = textapi.Client(app_id, app_key)

    #text="Barack Obama is the president of the United States of America. Obama lives in Washington, a city in the West of the USA"

    #entities = client.Entities({"text": text})
    try:
        concepts = client.Concepts({"text": text})
        response=[]
        try:
            if concepts["language"] != "en":
                    output=[False,concepts]
            elif concepts["language"] == "en":
                try:
                    for entity in concepts["concepts"]:
                        dp=entity
                        try:
                            uri=dp_to_wikidata(dp)
                        except HTTPError:
                            uri=""
                        label=dp[28:].replace("_"," ")
                        extra={"aylien":{"types":concepts["concepts"][entity]["types"]}}
                        for surface in concepts["concepts"][entity]["surfaceForms"]:
                            entity_dict={}
                            confidence=surface["score"]
                            surface_form=surface["string"]
                            start=surface["offset"]
                            end=start+len(surface_form)
                            entity_dict["surface"]=surface_form
                            entity_dict["label"]=label
                            entity_dict["start"]=start
                            entity_dict["end"]=end
                            entity_dict["confidence"]=confidence
                            entity_dict["extra"]=str(extra)
                            entity_dict["uri"]=uri
                            t=time.time()
                            entity_dict["timestamp"]='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t))
                            response.append(entity_dict)
                    output=[True,response]
                except KeyError:
                    output= [KeyError,concepts]
        except KeyError:
            output= [KeyError,concepts]
    except HTTPError:
        output=[False,"http-error"]
    return(output)
            