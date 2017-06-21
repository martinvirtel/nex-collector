# string="Türkei"
# text= "Türkei Pause Türkei, Türkei dsbkfsfhj Türke"
"""text.replace("."," ")
text.replace(","," ")
text.replace(":"," ")
text.replace(";"," ")
text.replace("!"," ")
text.replace("?"," ")
text.replace("“"," ")
text.replace("'"," ")
text.replace('"'," ")
text.replace('&'," ")
text.replace('€'," ")
text.replace('$'," ")"""
def word_position(text,string,position):
    text_list=text.split()
    for x in position:
        if string in text:
    #     count=text.count(string)
    #     string_list =[]
    #     for x in range(count):
    #         string_dict ={}
    #         string_position=text.index(string,x)
    #         string_dict["string"]=string
    #         string_dict["start"]=string_position
    #         string_dict["end"]=string_position+len(string)
    #         string_list.append(string_dict)
    #     if len(string_list) > 1:
    #         print("Error: Same string more than once!")

    # return (string_list)
