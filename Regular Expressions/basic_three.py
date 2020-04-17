#Matching n number of times
#greedy and non greedy match

import re


regex = re.compile(r"(ha){3}")

mo = regex.search("I smiled hahaha")

print(mo.group())


regex = re.compile(r"(ha){3,5}")

mo = regex.search("I smiled hahahahahahahahahahaha")

print(mo.group())


regex = re.compile(r"(ha){3,5}?")

mo = regex.search("I smiled hahahahahahahahahahaha")

print(mo.group())


regex = re.compile(r"(ha){3,}")

mo = regex.search("I smiled hahahahahahahahahahaha")

print(mo.group())


regex = re.compile(r"(\d){3,}")

mo = regex.search("I smiled 4562345235234")

print(mo.group())




regex = re.compile(r"((\d\d\d-)(\d\d\d\d\d)(,)?){3}")

mo = regex.search("044-96772,044-88485,044-34566")

print(mo.group())


