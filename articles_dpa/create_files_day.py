from neofonie import show, query
import json
import os.path
import string

# Dateien schreiben mit Modul json
# Dateien in einen eigenen Ordner schreiben
# Strings erzeugen mit https://docs.python.org/3.6/library/string.html#format-examples

#Amount of articles that day:
output_number=(query('*:*',
    wt="json",
    fq=[
        "sourceId:dpa",
        "createdAt:[2017-04-04T00:00:00.001Z TO 2017-04-04T23:59:59.999Z]",
        "-dpaRessort:rs",
         ],  
        
        start=1,
        rows=1
        )
    )
numFound=int(output_number["response"]["numFound"])
print("\n Amount of articles:",numFound,"\n")
# numFound=int("{numFound}".format(**y["response"]))


#counters
position=0
#counter=numFound//100
#extra_counter=numFound%100
while position <= numFound:
    y=(query('*:*',
                wt="json",
                fq=[
                    "sourceId:dpa",
                    "createdAt:[2017-04-04T00:00:00.001Z TO 2017-04-04T23:59:59.999Z]",
                    "dpaRessort:rs",
                ],
                fl="createdAt,dpaTitle,text,dpaId",
                    #"dpaServices",
                    #"createdAt",
                    #"dpaId",
                   
                start=position,
                rows=1
                )
            )
    docs=y["response"]["docs"]
#For Loop
    for d in docs :
        #print("Schleife fuer Datei {0} fuer Titel {dpaTitle}".format(filename,**d)) # d["dpaTitle"]
      
    ##DPA ID as filename
        string_begin_temp =(docs[0]["dpaId"])
        string_begin=string_begin_temp.replace('/', 'v-')
    #Writing the file               
        string_end=".json"
        #filename="".join([string_begin,string_end])
        filename='{string_begin}, {string_end}'.format('ab')
        with open(filename, 'w') as f:    
            json.dump(docs,f)
            f.close()

    #Moving the file
    old_position="".join(["/Users/alex/python_project/Martin/",filename])
    new_position="".join(["/Users/alex/python_project/Martin/outputs/",filename])
    os.rename(old_position, new_position)
    print("\nMoved file",filename)  
    
    #position=position+100
    position=position+1
    

print("\n\n**FINISHED**")