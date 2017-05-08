from dandelion_apikey import token
import json
from joblib import Memory
import os
import os.path
from dandelion import DataTXT
from wiki_link_import import wiki_query
from check_file import check_file
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)


"""cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache"""
def dandelion(item,ner_names,tool_counter):
    try:
        global output
        value = check_file(item,ner_names,tool_counter)
        if value == False:
            text = item["text"]
            datatxt = DataTXT(app_id=token, app_key=token)
            response = datatxt.nex(text)
            for d in response.annotations:
                if len(response["annotations"])>0 :
                    wiki= str(d["id"])
                    d["uri"]=wiki_query(wiki)
                    output=(response["annotations"])
                else:
                    output= [{"message": "no entities found"}]
                    logging.error("dandelion didnt find any entities for the file %s"%item["filename"])
        elif value == True:
            output=[{"error": "file double"}]
        return output
    except KeyError:
        logging.error("dandelion Call for file %s not successfull. Output: %s"%(item["filename"],response))
   