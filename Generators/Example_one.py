#This is simple way of using range() as a generator
#function for getting a number and coverting it into a range of numbers and
#storing the range of numbers in a list and returning its cube

'''def cube_formula(n):
    result =[]
    for x in range(n):
        result.append(x**3)
    return result


print(cube_formula(20))'''


#Now using our own generator instead of returning thr result
#Here we are storing the result in memory and getting each value.
'''def cube_formula(n):
    result =[]
    for x in range(n):
        result.append(x**3)
    return result

#using a for loop and calling the function.
#for every item in cube_formula, we are printing the items one by one after computing 
for x in cube_formula(20):
    print(x)'''

#we dont need the list anymore since we are not going to store it in memory.
#introducing "yield" keyword. We dont have the list in memory.
def cube_formula(n):
    for x in range(n):
        yield x**3
    
#iterating the function will give the cubes of each numbers of range(0,20)
#now cube_formula(20) is an generator object
#we can cast cube_fomula(20) into a list too.
for x in cube_formula(20):
    print(x)

print(list(cube_formula(20)))
