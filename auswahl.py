"""
Produziert eine zufaellig ausgewaehlte Dateiliste
"""

from pathlib import Path
import random
import csv


laenge = 97
name = "CALL_NER/auswahl-2017-05-01_97.csv"
verzeichnis = "outputs/**/*dpa.com*.json"

auswahl=random.sample(list(Path(".").glob(verzeichnis)),laenge)
csvfile=open(name,"w")
csvwriter=csv.writer(csvfile)
csvwriter.writerows([str(a)] for a in auswahl)
csvfile.close()
print("Random selection of ", laenge ," files in the file ", name , " was successful!")
