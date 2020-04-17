#greet and welcome are limited to hello 
def hello(name="mike"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() function inside hello"

    def welcome():
        return "\t this is welcome() inside hello"
    
    print("i am going to return a fucntion")

    if name =='mike':
        return greet
    else:
        return welcome

myfunc = hello('mike')

print("Extracting the function myfunc below")

print(myfunc())
