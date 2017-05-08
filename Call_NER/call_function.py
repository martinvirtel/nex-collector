import json
from check_file import check_file
from call_txtwerk import txtwerk
from call_dandelion import dandelion
from call_ambiverse import ambiverse
from save_file import save_file
import logging
import sys
import os
logging.basicConfig(level=logging.INFO,stream=sys.stdout)


def call_fuction(item,ner_tools):
    text = item["text"]
    output_object={
        "entities":"",
        "text": text,
        "status":"",
        "message":"",
        "filename":item["filename"],
        "filepath":item["filepath"],
        "ner-tool":"",
        "cache":""
        }
# class NER_result(object)
#   entities=[]
# 
    #noch ändern!
    
    for tool in ner_tools:
        tool_name=tool.__name__
        output_object["ner-tool"]=tool_name

        value = check_file (item,tool_name)
        if value == False:
            
            output=tool(text)
            if output[0] == 1:
                
                if len(output[1]) > 0:
                    output_object["entities"]=output[1]
                    output_object["status"]=True
                    logging.info("Entities found for file %s"%item["filename"]%tool.__name__)

                else:
                    output_object["status"]=False
                    output_object["message"]="No entities found"
                    logging.error("txtwerk didnt find any entities for the file %s"%item["filename"]%tool.__name__)
            else:   
                output_object["status"]=False
                output_object["message"]=output[1]
                logging.error("txtwerk Call for file %s not successfull. Output: %s"%item["filename"]%tool.__name__)
        
        elif value == True:
            output_object["status"]=False
            output_object["message"]="file exists already"
            logging.info("File %s exists already."%item["filename"]%tool.__name__)
        try:    
            cache=tool.get_output_dir(text)
            if os.path.exists(cache[0]) == True:
                output_object["cache"]=True
            elif os.path.exists(cache[0]) == False:
                output_object["cache"]=True
        except AttributeError:
                output_object["cache"]="no caching for %s"%tool.__name__
        save_file(output_object)
        logging.info("Request and saving file done for %s\n"%item["filename"]%tool.__name__)
   