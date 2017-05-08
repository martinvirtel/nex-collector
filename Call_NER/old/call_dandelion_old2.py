from dandelion_apikey import token
import json
from joblib import Memory
import os
import os.path
from dandelion import DataTXT
from wiki_link_import import wiki_query
from check_file import check_file


"""cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)
memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache"""
def dandelion(file_list):
    
    output = []
    for item in file_list:
        value = check_file((item))
        if value == False:
            text = item["text"]
            datatxt = DataTXT(app_id=token, app_key=token)
            response = datatxt.nex(text)
            for d in response.annotations:
                if len(response["annotations"])>0 :
                    wiki= str(d["id"])
                    d["uri"]=wiki_query(wiki)
                    output.append(response["annotations"])
        else:
            output.append("File = double")
    return output