import csv
import json
import logging
import sys

logging.basicConfig(level=logging.INFO,stream=sys.stdout)


def dpa_list(filename_csv):
    dpa_list = []
    #filename_csv="auswahl-2017-05-01_97.csv"
      
    ### Opening of the csv list    
    f = open(filename_csv)
    csv_f = csv.reader(f)

    ### read "filename_csv" for filenames of dpa-texts

    ### Creating the filepath
    for row in csv_f :
        filepath = "".join(["/Users/alex/python_project/",row[0]])

    ### open dpa json    
        text_json = (json.load(open(filepath)))

    ### write dpa-text and additional info in in dict
        temp_dic={
            "text":text_json["text"],
            "dpa_id":text_json["dpaId"],
            "date":text_json["createdAt"],
            "ressort":text_json["dpaRessort"],
            "title":text_json["dpaTitle"]
        }
        

    ### write  dict in list "dpa_list"
        dpa_list.append(temp_dic)
    logging.info("Created: dpa_list with %s items\n" %(len(dpa_list)))  
    return dpa_list
