import requests
import json
import csv
import os
import os.path
import errno
from ambiverse_apikey import client_id, client_secret


filename_csv= "auswahl-2017-04-19.csv"

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
    filename="".join(["ambiverse_",string_begin,string_end])
    foldername=(text_json["createdAt"])
    foldername=foldername[0:10]
    file_path = "".join(["/Users/alex/python_project/outputs/ambiverse/",foldername,"/"])
    try: 
        os.makedirs(file_path)
    except OSError:
            if not os.path.isdir(file_path):
                raise
#text= "Apple is the biggest company in America."
#Ambiverse Token
ambiverse_api_url= "https://api.ambiverse.com/oauth/token"
data={"grant_type": "client_credentials", "client_id":client_id, "client_secret":client_secret}

r = requests.post(ambiverse_api_url, data=data)
ambiverse_token_output = r.json()
ambiverse_token = ambiverse_token_output ['access_token']


#Ambiverse Call
output_file="".join([file_path,filename])
ambiverse_request_url = "https://api.ambiverse.com/v1/entitylinking/analyze"
# text_string="".join(["{\"text\" : \"",text.encode("utf-8"),"\"}"])
text_string=json.dumps({"text" : text })

payload= text_string
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'authorization': ambiverse_token
    }

output = requests.request("POST", ambiverse_request_url, data=payload, headers=headers)
response= output.json()

response_matches=response["matches"]
entity_list= []
for x in response_matches:
     entity_list.append(x["entity"])

# for x in response_matches:
#    x.pop("entity", None)

#y=0
for x in response_matches:
    x.update(x['entity'])
    del x['entity']
    #print(type(x))
    #try:
    #    x.update ({"confidence":entity_list[y]["confidence"]})
    #except KeyError :
    #    x.update ({"confidence":""})
    #try:
    #    x.update ({"id":entity_list[y]["id"]},)
    #except KeyError :
    #    x.update ({"id":""})
    #try:
    #    x.update ({"url":entity_list[y]["url"]})
    #except KeyError :
    #    x.update ({"url":""})
    #
    #y=y+1

#if len(response.matches)>0 :

with open(output_file,'w') as f:
# Using dictionary keys as fieldnames for the CSV file header
    writer = csv.DictWriter(f, response_matches[0].keys())
    writer.writeheader()
    for d in response["matches"]:
        writer.writerow(d)
        #counter_annotations = counter_annotations + 1
        #f.close()

    #print("Found ", counter_annotations, "annotations")
    #print("Saved CSV-File", counter)
    #counter = counter + 1
    #counter_annotations_general= counter_annotations_general + counter_annotations
    #counter_annotations = 1
    #language = txt_werk_response["language"]
#else :
 #   print("No entities found in %s" % row)





print (response)