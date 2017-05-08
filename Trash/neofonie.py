"""

@author: alex gaus
"""
import requests
#Requests will allow you to send HTTP/1.1 requests using Python.
# With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries.
# It also allows you to access the response data of Python in the same way.

import re
#Regular Expressions
#RE are text matching patterns described with a formal syntax.
#The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original.
#The term “regular expressions” is frequently shortened to as “regex” or “regexp” in conversation.
#Expressions can include literal text matching, repetition, pattern-composition, branching, and other sophisticated rules.
#A large number of parsing problems are easier to solve with a regular expression than by creating a special-purpose lexer and parser.

import csv
#The csv module implements classes to read and write tabular data in CSV format.
#It allows programmers to say, “write this data in the format preferred by Excel,” or “read data from this file which was generated by Excel,” without knowing the precise details of the CSV format used by Excel.
#Programmers can also describe the CSV formats understood by other applications or define their own special-purpose CSV formats.

import sys
#The sys module provides information about constants, functions and methods of the Python interpreter.
#dir(system) gives a summary of the available constants, functions and methods.
#Another possibility is the help() function. Using help(sys) provides valuable detail information.

import logging
#This module defines functions and classes which implement a flexible event logging system for applications and libraries.
#The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging,
#so your application log can include your own messages integrated with messages from third-party modules.

import urllib
#is a package that collects several modules for working with URLs:

import collections
#This module implements some nice data structures which will help you to solve various real life problems.

import datapipeline
#???

# logging.basicConfig(level=logging.DEBUG,stream=sys.stderr)
logging.getLogger("requests").setLevel(logging.ERROR)
logger=logging.getLogger(__name__)
#???

from credentials import username, password
    """
    try :
        from credentials import dpa as auth
    except ImportError :
        raise RuntimeError("Credentials must be supplied as dict in credentials.py. See example_credentials.py or use this as a template: dpa=dict(login='user',password='secret')")
    """
prefix = "https://nstr.neofonie.de/solr-dev/news/select?q="
#URL von Neofonie = prefix



def neofonie(query) :
    response=requests.get(prefix,query)
    return response.json()



if __name__ == "__main__" :
    print(neofonie("*:*"))

