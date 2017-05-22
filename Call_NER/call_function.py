import json
from check_file import check_file
from call_txtwerk import txtwerk
from call_dandelion import dandelion
from call_ambiverse import ambiverse
from write_output_db import write_output_db
import logging
import sys
import os
import time
import datetime
logging.basicConfig(level=logging.INFO,stream=sys.stdout)


def call_fuction(item,ner_tools):
    ### dpa-text
    text = item["text"]
    dpa_id = item["dpa_id"]
    
    ### For every text there is a loop for every tool
    for tool in ner_tools:
        
        tool_name=tool.__name__

        output=tool(text)
        output.append(tool_name)
    
        ### if output[0] == False the detected language was not german. 
        ### Output will not be written in db 
        if output[0] == False:
            logging.error("Language error with dpa_id: %(dpa_id)s and tool: %(tool_name)s"%locals())

        ### if output[0] == KeyError there was an undefindes Error.
        ### Output will not be written in db
        ### actuall output will be printed
        elif output [0] == KeyError:
            message=output[1]
            logging.error("KeyError, undefinded Error for dpa_id %(dpa_id)s and tool: %(tool_name)s\nMessage:\n%(message)s"%locals())

        ### output[0] means language was detected as german 
        elif output[0] == True:
            ### if length > 0 entites were found
            if len(output[1]) > 0:
                logging.info("Entities found for dpa_id: %(dpa_id)s by tool: %(tool_name)s"%locals())
            
            ### if no entities are found, this is the "emtpy"-output
            else:
                t=time.time()
                output=["q0",
                [dict(
                    surface="",
                    label="",
                    start=0,
                    end=0,
                    confidence=0,
                    uri="q0",
                    timestamp='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(t)),
                    extra=str({tool_name:"None"})
                )],tool_name]
                logging.error("No entities found for dpa_id %(dpa_id)s by tool: %(tool_name)s"%locals())
            
            ### If there was no Error, file will be written into db
            write_output_db(output,item)

    

    


