import sqlite3
import dataset
import json
import glob
import csv
import os
import os.path
import datetime
import ast
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)

def write_output_db(output,item):

    ###Path Explanation
    path_original = "/Users/alex/nex-analysis"
    path = "/Users/alex/python_project/write_csv"

    #os.chdir(path)
    ### Location of the database
    db='sqlite:///test.db'
    database = dataset.connect(db)
    #os.chdir(path_original)

    ### Every table of the database is opened
    dpa_text=database["dpa_text"]
    found_entities=database["found_entities"]
    entity_db=database["entity"]
    tools= database["tools"]
    dpa_text= database["dpa_text"]

    ### Check if tool exists already
    tool=output[2]
    value_tool=tools.find_one(tool=tool)
    ### If tool does not exist, it will be generated
    if  value_tool == None:
        tools.insert({"tool":tool})
        logging.info("tool: %(tool)s was generated"%locals())
    
    ### looking up the tool_id (keyrow of the tool)
    tool_id=list(database.query("select rowid from tools  where tool=:tool",tool=tool))[0]["rowid"]

    dpa_id=item["dpa_id"]
    
    ### Check if dpa_text exists already
    value_dpaid=dpa_text.find_one(dpa_id=dpa_id)
    ### If dpa-text does not exist, it will be generated
    if value_dpaid == None:
        dpa_text.insert(dict(
            dpa_id=dpa_id,
            title=item["title"],
            ressort=item["ressort"],
            text=item["text"],
            date=item["date"]
            ))
        logging.info("dpa_id: %(dpa_id)s was generated"%locals())

    ### Looking up the dpa_id_id (keyrow of this text)
    dpa_id_id=list(database.query("select rowid from dpa_text  where dpa_id=:dpa_id",dpa_id=dpa_id))[0]["rowid"]
    
    ### if the entity has an uri, the uri is the entity_id, if not the surface is the entity_id
    for entity in output[1]:
        uri=entity["uri"]
        surface=entity["surface"]
        if uri==None or uri=='':
            entity_id=surface
        else:
            entity_id=uri
        
        ### if the entity has no label, surface = label (and labelfromsurface=True)
        if entity["label"] == None or  entity["label"] == '' :
            label=surface
            labelfromsurface=True
        else:
            label=entity["label"]
            labelfromsurface=False
            
        ### Check if entity exists already
        value_entity=entity_db.find_one(entity_id=entity_id)

        ### If entity does not exist, it will be generated
        if value_entity == None:
            entity_db.insert(dict(
                uri=uri,
                label=label,
                labelfromsurface=labelfromsurface,
                extra=(entity["extra"]),
                entity_id=entity_id))
            logging.info("Entity: %(surface)s with the entity_id: %(entity_id)s was generated"%locals())
            
            ### Looking up the entity_id_id (keyrow from entity_id)
            entity_id_id=list(database.query("select rowid from entity  where entity_id=:entity_id",entity_id=entity_id))[0]["rowid"]
            
            ### check if the exact found_entity with the tool, text, start and time stamp exists
            found=entity["timestamp"]
            value_double=found_entities.find_one(dpa_id=dpa_id_id, entity_id=entity_id_id,tool_id=tool_id, start=entity["start"],found=found)
            
            ### If the exact found entity does not exist, it will be generated
            if value_double == None:

                try:
                    confidence=float(entity["confidence"])
                except ValueError:
                    confidence = None
                except KeyError:
                    confidence = None
                found_entities.insert(dict(
                    surface=surface,
                    start=int(entity["start"]),
                    end=int(entity["end"]),
                    confidence=confidence,
                    found=found,
                    dpa_id=dpa_id_id,
                    tool_id=tool_id,
                    entity_id=entity_id_id
                ))
        
        ### If the entity exists already, only the "extra"-part will be updated
        else:
            entity_id_id=list(database.query("select rowid from entity  where entity_id=:entity_id",entity_id=entity_id))[0]["rowid"]
            value_extra=found_entities.find_one(entity_id=entity_id_id,tool_id=tool_id)
            if value_extra == None:
                ex_extra = ast.literal_eval(entity_db.find_one(entity_id=entity_id)["extra"])
                new_extra = ast.literal_eval(entity["extra"])
                extra=ex_extra
                extra.update(new_extra)
                entity_db.upsert(dict(
                    extra=str(extra),
                    entity_id=entity_id
                    ),["entity_id"])
       
        found=entity["timestamp"]
        value_double=found_entities.find_one(dpa_id=dpa_id_id, entity_id=entity_id_id,tool_id=tool_id, start=entity["start"],found=found)
            
        ### If the exact found entity does not exist, it will be generated
        if value_double == None:
            
            try:
                confidence=float(entity["confidence"])
            except ValueError:
                confidence = None
            except KeyError:
                confidence = None
            found_entities.insert(dict(
                surface=surface,
                start=int(entity["start"]),
                end=int(entity["end"]),
                confidence=confidence,
                found=found,
                dpa_id=dpa_id_id,
                tool_id=tool_id,
                entity_id=entity_id_id
            ))
                
            

        logging.info("output from dpa_id: %(dpa_id)s from tool: %(tool)s was writen into db"%locals())