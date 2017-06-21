# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from semantria_apikey import key, secret
from wiki_link_name import wiki_query
import semantria as semantria_f
import uuid
import time
import datetime

import sys

def semantria(text):
    serializer = semantria_f.JsonSerializer()
    session = semantria_f.Session(key, secret) 
    # serializer, use_compression=True)
    #text="Barack Obama it der Präsident der Vereinigten Staaten von Amerika. Obama lebt in Washington, einer Stadt im Westen der USA"
    # text=text.replace("'"," ")
    # text=text.replace('"',' ' )
    # text=text.replace("<"," ")
    # text=text.replace("<"," ")
    # text=text.replace(">"," ")
    # text=text.replace("»"," ")
    # text=text.replace("«"," ")
    # text=text.replace("»"," ")
    # text=text.replace("»"," ")
    # text=text.replace("«"," ")
    text_cut=text
    text_list=[]
    
    length=len(text_cut)
    for x in range(-1,length//1400):
        text_element=text_cut[:1400]
        text_cut=text_cut[1400:]
        text_list.append(text_element)
    #print(text_list)
    x=0
    response_entities=[]   
    for text in text_list:
        doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}
        #print(doc)
        session.queueDocument(doc)

        response = session.getProcessedDocuments()
        response = response[0]
        import pprint
        #pprint.pprint(response)
        #pprint.pprint(response["entities"])
        try:
            if response["language"] != "German":
                        output=[False,response]
            elif response["language"] == "German":
                try:
                    for entity in response["entities"]:
                        
                        if entity["entity_type"] != "Quote":
                            label=entity["title"]
                            uri=wiki_query(label)
                            confidence=entity["evidence"]
                            if entity["label"].find("wiki") !=-1:
                                wiki=entity["label"]
                                type_e="None"
                            else:
                                wiki = "None"
                                type_e=entity["label"]
                            extra={"semantria":{
                                "type":type_e,
                                "entity_type":entity["entity_type"],
                                "wikipedia":wiki,
                                "sentiment_polarity":entity["sentiment_polarity"],
                                "sentiment_score":entity["sentiment_score"]
                            }}

                            for appearing in entity["mentions"]:
                                surface=appearing["label"]
                                for same in appearing["locations"]:
                                    entity_dict={}
                                    start=same["offset"]
                                    end=start+same["length"]
                                    entity_dict["surface"]=surface
                                    entity_dict["label"]=label
                                    entity_dict["start"]=start+x
                                    entity_dict["end"]=end+x
                                    entity_dict["confidence"]=confidence
                                    entity_dict["extra"]=str(extra)
                                    entity_dict["uri"]=uri
                                    t=time.time()
                                    entity_dict["timestamp"]='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t))
                                    response_entities.append(entity_dict)
                    output=[True,response_entities]
                except KeyError:
                    output= [True,response_entities]
        except KeyError:
            output= [True,response_entities]
        x=x+1400
        #pprint.pprint(output)
    return output
