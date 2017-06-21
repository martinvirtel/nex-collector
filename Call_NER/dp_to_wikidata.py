# -*- encoding: utf-8 -*-
import urllib.request
import requests
def dp_to_wikidata(dp):
    try:
        try:
            with urllib.request.urlopen(dp) as response:
                html = response.read()

            html_text=html.decode("utf-8")
            same_as=html_text.find("owl:sameAs")
            same_as_text=html_text[same_as:]
            wiki_text=same_as_text[same_as_text.find("wikidata"):]
            wiki_text_split=wiki_text.split('"')
            uri=wiki_text_split[0][20:]
        except UnicodeEncodeError:
            uri=""
    except urllib.request.HTTPError:
        uri=""

    if uri.find("resource")!=-1:
        uri=uri[10:]
    else: uri=""
    return(uri)
    print(uri)
