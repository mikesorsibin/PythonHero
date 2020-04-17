import re

song = '''12 drummers drumming 11 pipers piping
10 lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves'''

regex = re.compile(r'\d+\s\w+')

mo = regex.findall(song)

print(mo)


regex = re.compile(r'[aeiouAEIOU]')

mo = regex.findall('robo cop eats baby food, do You know why')

print(mo)

regex = re.compile(r'[^aeiouAEIOU]')

mo = regex.findall('robo cop eats baby food, do You know why')

print(mo)

regex = re.compile(r'[^aeiouAEIOU]')

mo = regex.findall('robo cop eats baby food, do You know why')

print(mo)


