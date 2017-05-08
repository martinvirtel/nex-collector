import os
import os.path

def check_file(item,tool_name):
    filepath = item["filepath"]%tool_name
    filename = item["filename"]%tool_name
    path_output= "".join([filepath,filename])
    value = os.path.exists(path_output)
    if value == True:
        """print("File ",path_output," exists already")"""
    #print("filecheck done")
    return value
