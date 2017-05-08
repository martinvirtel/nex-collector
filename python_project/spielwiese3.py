import csv

dics = [  {'confidence': 0.637,
   'end': 1248,
   'id': 133094,
   'label': 'Karnevalsverein',
   'spot': 'Karnevalsverein',
   'start': 1233,
   'title': 'Karnevalsverein',
   'uri': 'http://de.wikipedia.org/wiki/Karnevalsverein'},
  {'confidence': 0.8755,
   'end': 1370,
   'id': 1356496,
   'label': 'Blackface',
   'spot': 'Blackfacing',
   'start': 1359,
   'title': 'Blackface',
   'uri': 'http://de.wikipedia.org/wiki/Blackface'}]

with open("file.csv",'w') as f:
   # Using dictionary keys as fieldnames for the CSV file header
   writer = csv.DictWriter(f, dics[0].keys())
   writer.writeheader()
   for d in dics:
      writer.writerow(d)


"""
    for annotation in response.annotations:
      print ("Annotation = ",annotation, "*****__*****")
      print ("Output = ",response)
      
      with open(output_file, 'w') as f:
            w = csv.DictWriter(f, annotation.keys())
            w.writeheader()
            w.writerow(annotation)
    
    with open(output_file, "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for annotation in response.annotations:
            writer.writerow(annotation)


 delimiter=' ', skipinitialspace=True,
        #fieldnames=['confidence', 'end', 'id','label', 'spot', 'start','title', 'uri'])
   csvfile=open(output_file,"w")
    csvwriter=csv.DictWriter(csvfile)
    for annotation in response.annotations:
        #annotation_edit = str(annotation) 
        #annotation_edit = annotation_edit.replace(":",",")

"""