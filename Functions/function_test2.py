'''def myfunc(mystring):
    for letters in mystring:
        if len(letters)%2 ==0:
            print(letters)
            letters.upper()
    return mystring
    
     
    


print(myfunc("constable"))'''





'''a ='Constable'
mylist=[]

for letters in range(len(a)):
    if letters%2==0:
        print(letters)
        mylist.append(a[letters].lower())
    else:
        mylist.append(a[letters].upper())
	
output=''.join(mylist)
print(output)'''



def myfunc5(mystring):
    
    mylist=[]
    for letters in range(len(mystring)):
        print(letters)
        if letters%2==0:
            mylist.append(mystring[letters].lower())
        else:
            mylist.append(mystring[letters].upper())
    return ''.join(mylist)
output = myfunc5('constable')
print(output)


    
 
