import textrazor
from word_position import word_position

textrazor.api_key = "b9db6904310711df1032711c8ccafaa81d632448f2771c04d5662e97"
text= "This is a test text. about the histroy of: Barak Obama in the United staates of America. Barak Obama was the second president"
client = textrazor.TextRazor(extractors=["entities"])
#response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")
response = client.analyze(text)



output=[]
for entity in response.entities():
    entity_dict={}
    entity_dict["label"]= entity.id
    entity_dict["confidence"] = entity.confidence_score
    entity_dict["uri"]="https://www.wikidata.org/wiki/%s"%entity.wikidata_id
    string=entity.matched_text
    entity_dict["surface"]= entity.matched_text
    string_list=word_position(text,string)
    entity_dict["start"]=string_list[0]["start"]
    entity_dict["end"]=string_list[0]["end"]
    output.append(entity_dict)