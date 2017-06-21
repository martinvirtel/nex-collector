from dandelion_apikey import token
import json
from dandelion import DataTXT
from wiki_link_import import wiki_query
import time
import datetime


def dandelion(text):
    
    datatxt = DataTXT(app_id=token, app_key=token)
    response = datatxt.nex(
        text,
        include_categories=True,
        include_types=True,
        include_image=True,
        include_lod=True,
        include_alternate_labels=True,
        include_abstract=True)
    try:
        if response["lang"] != "de":
            output=[False,response]
        elif response["lang"] == "de":
            try:
                for entity in response.annotations:
                    wiki= str(entity["id"])
                    uri=wiki_query(wiki).replace("https://www.wikidata.org/wiki/","")
                    entity["uri"]=uri
                    entity["surface"] = entity["spot"]
                    try:
                        alternate_labels=entity["alternate_labels"]
                    except KeyError:
                        alternate_labels="None"
                    if alternate_labels == None:
                        alternate_labels="None"          
                    types=entity["types"]
                    image=entity["image"]
                    lod=entity["lod"]
                    abstract=entity["abstract"]
                    extra_categories=entity["categories"]
                    extra={
                        "dandelion":{"category":types,
                        "image":image,
                        "alternate_labels":alternate_labels,
                        "lod":lod,
                        "abstract":abstract,
                        "extra_categories":extra_categories
                        }}
                    entity["extra"] =str(extra)
                    t=time.time()
                    entity["timestamp"]='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t))
                    del entity ["types"]
                    del entity["spot"]
                    del entity["id"]
                    del entity["title"]

                output=[True,response["annotations"]]

            except KeyError:
                output= [KeyError,response]
    except KeyError:
        output= [KeyError,response]

    return output
