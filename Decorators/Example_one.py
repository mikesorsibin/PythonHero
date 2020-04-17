def func():
    print("Welcome to Decorator Concept")

    def myfunc():
        return "I am a function inside a function"
    return myfunc


mynewfunc = func()

print(mynewfunc())
