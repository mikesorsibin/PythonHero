#Import re library
#To get a pattern that we want to match in a string and return it
#We can use compile method in re and create a similar pattern
#https://automatetheboringstuff.com/chapter7/

import re

mystring = "My phone number is 044-9677209069 and my other number is 044-8848403140"

regex_compilation= re.compile(r"\d\d\d-\d\d\d\d\d\d\d\d\d\d")#\d is regex for numeric digit numbers

match_object = regex_compilation.search(mystring)

match_object_all = regex_compilation.findall(mystring)#does not need a group()

print(match_object.group())

print(match_object_all)
