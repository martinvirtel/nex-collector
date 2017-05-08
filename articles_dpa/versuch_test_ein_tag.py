# coding: utf-8

from neofonie import show, query
import csv




y=(query('*:*',
            wt="json",
            fq=[
                "sourceId:dpa",
                "createdAt:[2017-04-03T00:00:00.001Z TO 2017-04-03T23:59:59.999Z]",
                "-dpaRessort:rs",
                #"-dpaTitle:*überblick*,*DGAP*,*MDAX*",
               
            ],
            fl="createdAt,dpaTitle",
            #dpaRessort",
            #"createdAt",
            # dpaServices,
            #,dpaId,text",
            start=0,
            rows=100,
            sort= "createdAt asc",
            sort_order="decs"
            )
        )
show(y)

x=str(y)
file=open("output.csv","x")
file.write (x)
file.close()

file2=open("output.txt", "x")
file2.write(x)
file.close()

with open('output2.csv', 'w') as f: 
    w = csv.DictWriter(f, y.keys())
    w.writeheader()
    w.writerow(y)