from collections import defaultdict
# default dict is used for assigning a default value to a key.
#this helps in removing key error
'''d={'k1':1}

print(d['k2'])'''

d = defaultdict(lambda:0)

d['one']
d['two'] = 2

print(d)
