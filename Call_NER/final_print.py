
def final_print(ner_names,output_list):
    
    for x in range(len(ner_names)):
        counter=0
        for item in output_list[x]:
            laenge = len(item)
            counter = counter+laenge
        print(ner_names[x]," found in total ", counter, " entities")