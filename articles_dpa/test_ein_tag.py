from neofonie import show, query
import csv


#show(query('*:*',
            #wt="json",
            #fq=[
                #"-dpaTitle:Tagesvorschau",
                #"sourceId:dpa",
                #"createdAt:[2017-04-03T00:00:00.001Z TO 2017-04-03T23:59:59.999Z]"
            #],
            #fl="dpaTitle,dpaServices,createdAt,dpaId",
           # rows=30
           # )
      #  )

y=(query('*:*',
            wt="json",
            fq=[
                "-dpaTitle:Tagesvorschau",
                "sourceId:dpa",
                "createdAt:[2017-04-03T00:00:00.001Z TO 2017-04-03T23:59:59.999Z]"
            ],
            fl="dpaTitle,dpaServices,createdAt,dpaId",
            rows=30
            )
        )
 
x=str(y)
file=open("output.csv","x")
file.write (x)
file.close()

import csv
with open('output2.csv', 'w') as f: 
    w = csv.DictWriter(f, y.keys())
    w.writeheader()
    w.writerow(y)