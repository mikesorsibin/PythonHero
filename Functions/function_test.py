

'''def myfunc(*args):
    return[n for n in args if n%2==0]

print(myfunc(1,2,3,4,5,6))'''




def myfunc1(*args):
    output=[]
    for num in args:
        if num%2 ==0:
            output.append(num)
    return output
            
    
        

print(myfunc1(1,2,3,4,5,6))
    













