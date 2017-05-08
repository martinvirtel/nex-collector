#! /usr/bin/env python


import urllib.parse
import urllib.request
import click

@click.command()
@click.option('--wiki', default=736,prompt="PageID Wikipedia",help='Put here the PageID')


def wiki_query(wiki):
    
    pageid =str (wiki)
    api_url= "https://de.wikipedia.org/w/api.php?action=query&format=json&prop=pageprops&pageids="
    #pageid="736"
    url="".join([api_url,pageid])

        


    f = urllib.request.urlopen(url)
    response=(f.read().decode('utf-8'))
    response= response.split(":")

    #print(response)
    wikidata_id = response[-1]
    wikidata_id = wikidata_id.replace("'", "")
    wikidata_id = wikidata_id.replace('"', "")
    wikidata_id = wikidata_id.replace('}', "")
    print("WIKIDATA ID: ",wikidata_id)

    wikidata_base="https://www.wikidata.org/wiki/"
    wikidata_url= "".join([wikidata_base,wikidata_id])
    wikipedia_base= "https://de.wikipedia.org/wiki?curid="
    wikipedia_url= "".join ([wikipedia_base,pageid])
    print('URL WIKIDATA: ', wikidata_url)
    print ('URL WIKIPEDIA: ', wikipedia_url)

if __name__=="__main__":
    wiki_query()