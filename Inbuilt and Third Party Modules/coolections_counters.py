from collections import Counter

l=[1,2,33,4,5,6,5,7,8,5,3,5,6,7,8,5,3,5,6,7,8,6]

print(Counter(l))


s ="helllofdodsoddsg"

print(Counter(s))


s='how are you boy where are you from boy how is life'

w = s.split()

print(Counter(w))

c= Counter(w)

print(c.most_common(2))

print(sum(c.values()))


