#! /usr/bin/env python

import datetime
import click

@click.command()
@click.option('--parameter',help='irgendein wert')
def spielwiese(parameter) :
    jetzt=datetime.datetime.now()

    x="anfang"
    y="ende"
    print("{}_{}.txt".format(x,y))

    liste=[ { "dpaId": 1 },
    { "dpaId": 2 },
    { "dpaId": 3 },
    { "dpaId": 4 }]

    for element in liste[1:-1] :
        print("Element:",element)
    print(parameter)

def hallo(parameter):
    print("hallo", parameter)

print("test")

if __name__=="__main__" :
    spielwiese()


