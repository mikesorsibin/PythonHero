import re

regex_zero_one = re.compile(r'bat(wo)?man')
mo=regex_zero_one.search("I am batwoman")
print(mo.group())

regex_zero_more = re.compile(r'bat(wo)*man')
mo1=regex_zero_more.search("I am batwowowowowowowoman")
print(mo1.group())

regex_one_more = re.compile(r'bat(wo)+man')
mo2=regex_one_more.search("I am batman")
print(mo2==None)
