from check_folder import check_folder
import csv
from check_file import check_file

def safe_file(file_list,output_list, ner_names):
    x=0
    for ner_tool in ner_names:
        for item in file_list:
            value = check_file((item))
            if value == False:
                filepath = item["filepath"]%(ner_tool)
                check_folder (filepath)
                filename = item["filename"]%(ner_tool)
                output_file="".join([filepath,filename])
                for item in output_list[x]:
                    with open(output_file,'w') as f:    
                        writer = csv.DictWriter(f, item[0].keys())
                        writer.writeheader()
                        for d in item:
                            writer.writerow(d)
                x=x+1
    print("--3--\nSaving file done")
        
            