from collections import OrderedDict

d =OrderedDict()
d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5

for k,v in d.items():
    print (k,v)


d1 =OrderedDict()
d1['b']=2
d1['a']=1
d1['d']=4
d1['c']=3
d1['e']=5

for k,v in d1.items():
    print (k,v)


print(d==d1)
