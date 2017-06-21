# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
from textrazor import TextRazorAnalysisException
import textrazor as textrazor_function
from textrazor_apikey import api_key
import time
import datetime
from requests import HTTPError

def textrazor(text):
    
    textrazor_function.api_key=api_key
    #text=text.encode('UTF-8')  
    client = textrazor_function.TextRazor(extractors=["entities","words"])
    #response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")
    try:
        response = client.analyze(text)

        if response.ok != True:
            output=[False,response.message]
        else:
            if response.language != "ger":
                output=[False,response]
            else:
                entities_list=[]
                if len(response.entities())==0:
                    output=[True,entities_list]
                else:
                        
                    for entity in response.entities():
                        entity_dict={}
                        entity_dict["label"]= entity.id
                        entity_dict["confidence"] = entity.confidence_score
                        entity_dict["uri"]=entity.wikidata_id
                        entity_dict["surface"]= entity.matched_text
                        position=entity.matched_positions
                        #word_position(text,string,position)
                        entity_dict["start"]=entity.starting_position
                        entity_dict["end"]=entity.ending_position
                        #string_list=word_position(text,string,position)
                        # entity_dict["start"]=string_list[0]["start"]
                        # entity_dict["end"]=string_list[0]["end"]
                        t=time.time()
                        entity_dict["timestamp"]='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t))
                        extra={"textrazor":{
                            "freebase_id":entity.freebase_id,
                            "freebase_types":entity.freebase_types,
                            "dbpedia_types":entity.dbpedia_types,
                            "wikipedia_link":entity.wikipedia_link
                            }}
                        entity_dict["extra"] = str(extra)
                        entities_list.append(entity_dict)
                        output=[True,entities_list]
    except TextRazorAnalysisException:
        output=[False,"http error"]
        
    #     print("key")
    #     output= [KeyError,response]
    # except TypeError:
    #     print("type")
    #     output= [KeyError,response]
    return(output)