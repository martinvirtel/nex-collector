import csv
import json
import logging
import sys
logging.basicConfig(level=logging.INFO,stream=sys.stdout)


def file_list(filename_csv):
#filename_csv="auswahl-2017-04-26_003.csv"
    """
    >>> type(csv_to_text("auswahl-2017-04-19.csv"))==list
    --1--
    Created: text_list
    True
    """

    ### open "filename_csv"
    f = open(filename_csv)
    csv_f = csv.reader(f)

    ### "file_list" will be the list with the output
    file_list = []

    ### key valuves for the dict of every document
    key_text = ["text"]
    key_filename = ["filename"]
    key_filepath = ["filepath"]

    ### read "filename_csv" for filenames of dpa-texts

    for row in csv_f :
        filename = "".join(["/Users/alex/python_project/",row[0]])
        # filename = filename.replace("[", "")
        # filename = filename.replace("]", "")
        # filename = filename.replace("'", "")

    ### write dpa-text in dict
        text_json = (json.load(open(filename)))
        text = [(text_json["text"])]
        text_dic = dict( zip( key_text , text))
        
    ### write filename in dict
        string_begin = (text_json["dpaId"])
        string_begin = string_begin.replace(":","_")
        string_begin = string_begin.replace('/', 'v-')
        string_end = ".csv"
        filename = ["".join(["%s_",string_begin,string_end])]
        filename_dic = dict(zip(key_filename, filename))
        text_dic.update(filename_dic)
        dic_together = text_dic
    ### write filepath in dict
        foldername=(text_json["createdAt"])
        foldername=foldername[0:10]
        filepath = ["".join(["/Users/alex/python_project/outputs/%s/",foldername,"/"])]
        filepath_dic = dict(zip(key_filepath, filepath))
        dic_together.update(filepath_dic)
        
    ### write 3 dicts in list "liste_list"
        file_list.append(text_dic)
    logging.info("Created: file_list with %s items\n" %(len(file_list)))  
    return file_list

    
        


#if __name__=="__main__" :
#import doctest
#doctest.testmod(verbose=True)

