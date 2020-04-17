'''#for loop in strings
for i in "World":
    #prints hello world five times since the string "world" contains five characters
    print("Hello World")
    #prints charecters in "world" one by one
    print(i)'''


#for loops in list
'''mylist=[1,2,3,4,5,6]
for i in mylist:
    print(i) # prints the numbers one by one
    print('Hello World')#prints hello world 6 times'''


#for loops in tuples

"""tup = (1,2,3)
for i in tup:
    print(tup) #prints the value of tup, i.ev (1,2,3) 3 times
    print(i) # iterates through the value of tup and prints the items inside tuple one by one"""

'''tup = [(1,2),(3,4),(5,6)]
for (odd,even) in tup: # creating (odd,even) similar to data structure (1,2)
    print(odd)'''


#for loops in dictionaries

d = {'k1':1,'k2':2,'k3':3}

'''for values in d:
    print(values) # prints only the keys. i.e k1 k2 k3'''

'''for values in d.items():
    print(values)''' # prints both key and values

'''for key,value in d.items():
    print(value)''' # prints only the values using unpacking

for value in d.values():
    print(value) # prints the value using values method

    
