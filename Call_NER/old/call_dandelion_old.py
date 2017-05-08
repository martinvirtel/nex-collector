from dandelion import DataTXT
import csv
import json
import os
import os.path
import errno
from wiki_link_import import wiki_query 


# ##### n
# for dateiname in csv :
#     daten=dandelion(dateiname)
#     write(list_von_dictionaries,anderdateiname)
#
###### Daten wiederholen fuer Auswertung
#     list_von_dictionaries=read(andererdateiname)
#
#
#
# @memory.cache
# dandelion(dateiname)
#    return list_von_dictionaries
#
# @memory.cache
# txtwerk(dateiname)
#    return list_von_dictionaries


#
# def force_open(dateiname_mit_pfad) :
#

def dandelion(filename_csv):
    print("** dandelion starts **")
    counter = 1
    counter_annotations = 1
    counter_annotations_general = 0
    from dandelion_apikey import token
    #filename_csv= "auswahl-2017-04-19.csv"

    f = open(filename_csv)
    csv_f = csv.reader(f)

    for row in csv_f:
        filename = "".join(["/Users/alex/python_project/",str(row)])
        filename = filename.replace("[", "")
        filename = filename.replace("]", "")
        filename = filename.replace("'", "")
        text_json=(json.load(open(filename)))
        text=text_json["text"]
        #print(text, "\n\n")

        string_begin_temp =(text_json["dpaId"])
        string_begin_temp = string_begin_temp.replace(":","_")
        string_begin=string_begin_temp.replace('/', 'v-')
        string_end=".csv"
        filename="".join(["dandelion_",string_begin,string_end])
        foldername=(text_json["createdAt"])
        foldername=foldername[0:10]
        file_path = "".join(["/Users/alex/python_project/outputs/dandelion/",foldername,"/"])
        try: 
            os.makedirs(file_path)
        except OSError:
                if not os.path.isdir(file_path):
                    raise   

        datatxt = DataTXT(app_id=token, app_key=token)
        response = datatxt.nex(text)
        output_file="".join([file_path,filename])
        fieldnames=['confidence', 'end', 'id',
                    'label', 'spot', 'start',
                    'title', 'uri']
        
        if len(response.annotations)>0 :
            with open(output_file,'w') as f:
            # Using dictionary keys as fieldnames for the CSV file header
                writer = csv.DictWriter(f, response.annotations[0].keys())
                writer.writeheader()
                for d in response.annotations:
                    
                    wiki= str(d["id"])
                    #import wiki_link_import
                    #from wiki_link_import import wiki_query 
                    d["uri"]=wiki_query(wiki)
                    #r = open("temp.txt", "r")
                    #for t in r:
                    #    d["uri"] = str(t)
                    writer.writerow(d)


                    counter_annotations = counter_annotations + 1
        else :
            print("No entities found in %s" % row)
        print("Found ", counter_annotations, "annotations")
        print("Saved CSV-File", counter)
        counter = counter + 1
        counter_annotations_general= counter_annotations_general + counter_annotations
        counter_annotations = 1

    




    print (counter_annotations_general, "annotations found in total")
    print("Language: ",response.lang)
    print ("** Dandelion finished **")