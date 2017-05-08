import requests
import csv
import json
import os
import os.path
import errno

def txtwerk(file_list):
    txtwerk_output = []
    print("** txtwerk starts **")
    counter = 1
    counter_annotations = 1
    counter_annotations_general = 0
    #filename_csv= "auswahl-2017-04-19_20.csv"

    #Change here!
    for item in file_list:
        text = item["text"]
        
        
       
        """try: 
            os.makedirs(file_path)
        except OSError:
                if not os.path.isdir(file_path):
                    raise   
        
        path_output= "".join([file_path,filename])
        value = os.path.exists(path_output)
        print(value)
        if value == False:
            try :"""
    from txt_werk_apikey import txt_werk
    #except ImportError :
        #raise RuntimeError("Credentials must be supplied as dict in txt_werk_apikey.py. See example_txt_werk_apikey.py or use this as a template: txt_werk=dict(apikey='apikey')")
    #output_file="".join([file_path,filename])

    TXT_WERK_URL = "https://api.neofonie.de/rest/txt/analyzer"

    ## Set Txt Werk Api-Key in headers
    key = str(txt_werk['apikey'])
    headers={'X-Api-Key' : key}

    ## Let's go

    r = requests.post(TXT_WERK_URL, data={'text': text, 'services' : 'entities'}, headers=headers)
    txt_werk_response = r.json()
    txtwerk_output.append(txt_werk_response)
    return txtwerk_output

                
            """#print("Txt Werk Request:\n\n\"" + text + "\"\n\n")
            #print("Txt Werk Response:\n\n" + json.dumps(txt_werk_response, indent=4))

            if len(txt_werk_response["entities"])>0 :
                with open(output_file,'w') as f:
                    # Using dictionary keys as fieldnames for the CSV file header
                        writer = csv.DictWriter(f, txt_werk_response["entities"][0].keys())
                        writer.writeheader()
                        for d in txt_werk_response["entities"]:
                            writer.writerow(d)
                            counter_annotations = counter_annotations + 1
                f.close()
                print("Found ", counter_annotations, "annotations")
                print("Saved CSV-File", counter)
                counter = counter + 1
                counter_annotations_general= counter_annotations_general + counter_annotations
                counter_annotations = 1
                language = txt_werk_response["language"]
            else :
                print("No entities found in %s" % row)
                
        else:
            print ("File ", path_output, " exists already")
            language= "file exists already, language not detected"
    print (counter_annotations_general, "annotations found in total")

    print("Language: ",language)
    print ("** txtwerk finished **")"""