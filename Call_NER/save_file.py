from check_folder import check_folder
import csv
from check_file import check_file
import sys
import logging
logging.basicConfig(level=logging.INFO,stream=sys.stdout)


def save_file(output_object):
    if output_object["message"]!="file exists already":
        filepath = output_object["filepath"]%(output_object["ner-tool"])
        check_folder (filepath)
        filename = output_object["filename"]%(output_object["ner-tool"])
        output_file="".join([filepath,filename])
        key_list=[]
        for dict in output_object["entities"]:
            for key in dict:
                key_list.append(key)
        key_list=set(key_list)
        with open(output_file,'w') as f:    
            writer = csv.DictWriter(f, key_list)
            writer.writeheader()
            for d in output_object["entities"]:
                writer.writerow(d)
        logging.info("File %s was saved"%output_object["filename"]%output_object["ner-tool"])
    else:
        logging.info("File %s exists already, file was not saved"%output_object["filename"]%output_object["ner-tool"])
