# -*- coding: utf-8 -*-

import json
from rosette_apikey import api_key
from rosette.api import API, DocumentParameters, RosetteException

#text="Bill Murray will appear in new Ghostbusters film: Dr. Peter Venkman was spotted filming a cameo in Boston this… http://dlvr.it/BnsFfS"
#text="Barack Obama ist the president of the United States of America. The capital of the USA is New York. Barack Obama lives in Washington."
text="Barack Obama ist der Präsident der Vereinigten Staaten von Amerika. Die Hauptstadt der USA ist New York. Barack Obama lebt in Washington."
key=api_key
altUrl='https://api.rosette.com/rest/v1/'
api = API(user_key=key, service_url=altUrl)
entities_text_data = text
params = DocumentParameters()
params["content"] = entities_text_data
params["genre"] = "social-media"
try:
    response=  api.entities(params)

    if response["responseHeaders"]["X-RosetteAPI-ProcessedLanguage"] !="deu":
        output=[False,response]
    elif response["responseHeaders"]["X-RosetteAPI-ProcessedLanguage"] =="deu":
        entities=response["entities"]
        entity_list=[]
        for found_entity in entities:
            count=found_entity["count"]
            start=0
            end=0
            text_position=text
            for y in range(0,count):
                entity={}
                entity["label"]=found_entity["normalized"]
                if found_entity["entityId"][0]=="Q":
                    entity["uri"]=found_entity["entityId"]
                else:
                    entity["uri"]=""
                surface=found_entity["mention"]
                entity["surface"]=surface
                start_marker=text_position.find(surface)
                text_postion=text_position[start_marker:]
                entity["start"]=start+start_marker
                end=start+len(surface)
                entity["end"]=end+start_marker
                extra={
                    "textrazor":{
                        "type":found_entity["type"]
                    }
                }
                entity["extra"]=str(extra)
    entity_list.append(entity)

except RosetteException as e:
    output= [KeyError,e]


