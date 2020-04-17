s1 = {1,2,3,4}

s1.add(5)
s1.add(6)

print(s1)

##s.clear()
##print(s)

s2=s1.copy()

print(s2)

s1.add(7)

print(s1)

#difference

print(s1.difference(s2))

#difference update

s1={1,2,3,4}
s2={2,3,4}
s1.difference_update(s2)#the method returns set1 after removing elements found in set2

print(s1)

#discardd a value from set
s2.discard(4)
print(s2)


#intersection

s1={1,2,3,4}
s2={2,3,4,5}

print(s1.intersection(s2))

s1={1,2,3}
s2={2,3,4}
s1.intersection_update(s2)
print(s1)



#isdisjoint

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}


print(s1.isdisjoint(s2))

print(s1.isdisjoint(s3))

#issubset and issuperset

print(s1.issubset(s2))

print(s2.issuperset(s1))

# symmetric_difference and symmetric_update
print(s1.symmetric_difference(s2))

print(s1.union(s2))

s1.update(s2)

print(s2)






