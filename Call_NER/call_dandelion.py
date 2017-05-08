from dandelion_apikey import token
import json
from dandelion import DataTXT
from wiki_link_import import wiki_query





def dandelion(text):
    try:

        datatxt = DataTXT(app_id=token, app_key=token)
        response = datatxt.nex(text)
        for d in response.annotations:
            wiki= str(d["id"])
            d["uri"]=wiki_query(wiki)
        output=[1,response["annotations"]]

    except KeyError:
        output= [0,response]

    return output
