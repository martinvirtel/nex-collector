import urllib.parse
import urllib.request
import requests
import requests_cache
from joblib import Memory
import os


cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)


memory = Memory(cachedir=cachedir, verbose=0)

session=requests.session()

@memory.cache
def wiki_query(name):
    #name= """Barack_Obama"""
    name = name
    url= "https://de.wikipedia.org/w/api.php?action=query&format=json&prop=pageprops&titles=%s"%name
    response = session.get(url).json()
    try :
        for x in response['query']['pages']:
            pageid=x
        uri=response['query']['pages'][pageid]['pageprops']['wikibase_item']
    except KeyError:
        uri=""
    return uri

if __name__=="__main__" :
    import doctest
    doctest.testmod(verbose=True)
    # assert wiki_query(100) == "https://www.wikidata.org/wiki/Q19577"
    # assert wiki_query(999) == "https://www.wikidata.org/wiki/Q688510"
    # assert wiki_query(101) == "https://www.wikidata.org/wiki/Q19577"
    # assert wiki_query(400) == "https://www.wikidata.org/wiki/Q19577"
