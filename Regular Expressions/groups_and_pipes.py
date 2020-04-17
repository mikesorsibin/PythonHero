#We can create a group using ()
#making use of () we can get area code seperately and number seperately
#this is done using group(1)
#if we want to directly match a () then use extra \ before the pattern and after the pattern

import re

mystring= "hi i am michael, my number is 044-9677209069"
compiled = re.compile(r"(\d\d\d)-(\d\d\d\d\d\d\d\d\d\d)")

mo=compiled.search(mystring)

print(mo.group())
print(mo.group(1))
print(mo.group(2))



mystring1= "hi i am michael, my number is (044)-9677209069"
compiled1 = re.compile(r"\((\d\d\d)\)-(\d\d\d\d\d\d\d\d\d\d)")

mo1=compiled1.search(mystring1)

print(mo1.group(1))


#pipe can match one of the pattern in a group

pipe_regex = re.compile(r'Bat(mobile|man|woman|virus)')

mo2=pipe_regex.search("I want to see a Batman movie")

print(mo2.group())
