import csv
from check_folder import check_folder

tools = [
    "txtwerk",
    "dandelion",
    "ambiverse"
    ]


for tool in tools:
    length=len(tool)
    f = open("%s_file_list.csv"%tool)
    csv_list = csv.reader(f)
    for row in csv_list:
        filename= row[0]
        #filename="test.csv"
        new_filename=row[0].replace("outputs","data")
        filepath=new_filename[:(17+length)]
        check_folder(filepath)     
        dpaid=new_filename[(18+(2*length)):-4]

        output_csv = csv.DictReader(open(filename))
        entity_list=[]

        if tool == "dandelion":
            for row in output_csv:
                entity=dict(row)
                entity_list.append(entity)
                entity["surface"] = entity["spot"]
                del entity["spot"]
                del entity["id"]
                del entity["title"]
                entity["tool"] = tool
                entity["dpaid"] = dpaid


        if tool == "ambiverse":
            for row in output_csv:    
                entity=dict(row)              
                entity_list.append(entity)
                entity["surface"] = entity["text"]
                entity["start"]= entity["charOffset"]
                entity["end"]=int(entity["start"])+int(entity["charLength"])
                entity["tool"] = tool
                entity["dpaid"] = dpaid
                entity["label"] = ""
                del entity ["charLength"]
                del entity ["charOffset"]
                del entity["text"]
                try:
                    entity["uri"] = entity["id"]
                except KeyError:
                    print("key error")
                try:
                    del entity["id"]
                except KeyError:
                    print("key error")
                try:
                    del entity["url"]
                except KeyError:
                    print("key error")
        if tool == "txtwerk":
            for row in output_csv:
                if len(row)>0:
                    entity=dict(row)
                    entity_list.append(entity)
                    entity["tool"] = tool
                    entity["dpaid"] = dpaid
                    del entity["type"]
                else:
                    print("no entities found")

       
        key_list=[]
        for dic in entity_list:
            for key in dic:
                key_list.append(key)
                
        key_list=set(key_list)

        with open(new_filename, "w") as output_file:
            writer = csv.DictWriter(output_file, key_list)
            writer.writeheader()
            for d in entity_list:
                writer.writerow(d)
